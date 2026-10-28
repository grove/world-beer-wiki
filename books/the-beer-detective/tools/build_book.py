#!/usr/bin/env python3
"""Build the PDF and EPUB from the single release master, without network access."""
from pathlib import Path
from xml.sax.saxutils import escape
import argparse
import copy
import hashlib
import json
import os
import re
import subprocess
import zipfile
import xml.etree.ElementTree as ET

from reportlab import rl_config
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                               PageBreak, NextPageTemplate, Spacer, HRFlowable,
                               Table, TableStyle)
from reportlab.platypus.tableofcontents import TableOfContents
from pypdf import PdfReader, PdfWriter

from design_cover import fonts

ROOT = Path(__file__).resolve().parents[1]
BUILD, DIST = ROOT / '.build', ROOT / 'dist'
MASTER = ROOT / 'the-beer-detective.md'
WIDTH, HEIGHT = 432, 648
NAVY, ORANGE, GREY = '#152D3B', '#C84F2D', '#657078'
DATE = '2026-10-28T00:00:00Z'
SOURCE_DATE_EPOCH = '1793145600'
rl_config.warnOnMissingFontGlyphs = 1


def run(args, **kwargs):
    env = dict(os.environ, SOURCE_DATE_EPOCH=SOURCE_DATE_EPOCH)
    return subprocess.run(args, check=True, env=env, **kwargs)


def roman(number):
    result = ''
    for value, glyph in [(1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'),
                         (100, 'c'), (90, 'xc'), (50, 'l'), (40, 'xl'),
                         (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i')]:
        while number >= value:
            result += glyph
            number -= value
    return result


def inlines(nodes):
    out = []
    for node in nodes:
        kind, value = node['t'], node.get('c')
        if kind == 'Str':
            out.append(escape(value))
        elif kind in {'Space', 'SoftBreak'}:
            out.append(' ')
        elif kind == 'LineBreak':
            out.append('<br/>')
        elif kind in {'Emph', 'Strong', 'Superscript', 'Subscript', 'Strikeout'}:
            tag = {'Emph': 'i', 'Strong': 'b', 'Superscript': 'super', 'Subscript': 'sub', 'Strikeout': 'strike'}[kind]
            out.append(f'<{tag}>{inlines(value)}</{tag}>')
        elif kind == 'Code':
            out.append(f'<font name="Sans" size="8">{escape(value[1])}</font>')
        elif kind == 'Link':
            target = escape(value[2][0], {'"': '&quot;'})
            out.append(f'<link href="{target}" color="{NAVY}">{inlines(value[1])}</link>')
        elif kind == 'Span':
            anchor = value[0][0]
            if anchor:
                out.append(f'<a name="{escape(anchor)}"/>')
            out.append(inlines(value[1]))
        elif kind == 'Quoted':
            quote = ('“', '”') if value[0]['t'] == 'DoubleQuote' else ('‘', '’')
            out.append(quote[0] + inlines(value[1]) + quote[1])
        elif kind == 'SmallCaps':
            out.append(inlines(value))
        elif kind == 'RawInline' and value[0] == 'html':
            # No arbitrary HTML is executed. The master uses native spans.
            if value[1].strip():
                raise ValueError(f'Unsupported raw HTML: {value[1]}')
        else:
            raise ValueError(f'Unsupported inline {kind}: {value}')
    return ''.join(out)


def plaintext(nodes):
    return re.sub(r'<[^>]+>', '', inlines(nodes)).replace('&amp;', '&')


def register_fonts():
    fonts()
    for name in ['Body', 'BodyBold', 'BodyItalic', 'Display', 'Sans']:
        pdfmetrics.registerFont(TTFont(name, str(BUILD / 'fonts' / f'{name}.ttf')))
    pdfmetrics.registerFontFamily('Body', normal='Body', bold='BodyBold', italic='BodyItalic', boldItalic='BodyBold')


def styles():
    base = ParagraphStyle('Body', fontName='Body', fontSize=10.7, leading=14.1,
                          alignment=TA_JUSTIFY, firstLineIndent=12,
                          spaceAfter=0, allowWidows=0, allowOrphans=0,
                          textColor=colors.HexColor('#242B30'), splitLongWords=1)
    return {
        'body': base,
        'first': ParagraphStyle('First', parent=base, firstLineIndent=0),
        'small': ParagraphStyle('Small', parent=base, fontSize=9.3, leading=12.4, firstLineIndent=0, spaceAfter=8),
        'note': ParagraphStyle('Note', parent=base, fontSize=9.0, leading=11.8, leftIndent=13, firstLineIndent=-13, spaceAfter=6),
        'reading': ParagraphStyle('Reading', parent=base, fontSize=9.6, leading=12.5, firstLineIndent=0, spaceAfter=8),
        'heading': ParagraphStyle('Heading', fontName='Display', fontSize=26, leading=29, spaceAfter=28,
                                  textColor=colors.HexColor(NAVY), keepWithNext=True),
        'noteheading': ParagraphStyle('NoteHeading', fontName='Sans', fontSize=12, leading=15, spaceBefore=15,
                                      spaceAfter=9, textColor=colors.HexColor(NAVY), keepWithNext=True),
        'part': ParagraphStyle('Part', fontName='Display', fontSize=35, leading=38, spaceAfter=30, textColor=colors.HexColor(NAVY)),
        'parttext': ParagraphStyle('PartText', parent=base, fontSize=12.5, leading=17, firstLineIndent=0, alignment=TA_LEFT),
        'label': ParagraphStyle('Label', fontName='Sans', fontSize=10, leading=13, spaceAfter=17, textColor=colors.HexColor(ORANGE)),
        'title': ParagraphStyle('Title', fontName='Display', fontSize=47, leading=48, textColor=colors.HexColor(NAVY), spaceAfter=26),
        'subtitle': ParagraphStyle('Subtitle', fontName='Body', fontSize=17, leading=22, spaceAfter=35),
    }


class BookDocument(BaseDocTemplate):
    def __init__(self, filename):
        super().__init__(str(filename), pagesize=(WIDTH, HEIGHT), leftMargin=54,
                         rightMargin=48, topMargin=55, bottomMargin=48,
                         title='The Beer Detective', author='A World Beer Wiki book project',
                         subject='Uncovering the Myths, Mysteries and Untold Stories of Beer',
                         pageCompression=1, allowSplitting=1)
        frame = Frame(54, 48, WIDTH-102, HEIGHT-103, leftPadding=0, rightPadding=0,
                      topPadding=0, bottomPadding=0, id='text')
        self.addPageTemplates([
            PageTemplate(id='cover', frames=copy.copy(frame)),
            PageTemplate(id='book', frames=frame, onPageEnd=self.furniture),
        ])
        self.intro_page = None
        self.openers = set()
        self.locations = {}
        self.running = ''

    def beforeDocument(self):
        self.intro_page = None
        self.openers = set()
        self.locations = {}
        self.running = ''

    def label(self, page):
        return str(page - self.intro_page + 1) if self.intro_page and page >= self.intro_page else roman(page - 1)

    def afterFlowable(self, flowable):
        if not hasattr(flowable, 'book_anchor'):
            return
        anchor, title = flowable.book_anchor, flowable.book_title
        self.canv.bookmarkPage(anchor)
        self.locations[anchor] = self.page
        if anchor == 'introduction':
            self.intro_page = self.page
        if getattr(flowable, 'book_opening', False):
            self.openers.add(self.page)
        if getattr(flowable, 'book_running', False):
            self.running = title
        toc_level = getattr(flowable, 'toc_level', None)
        if toc_level is not None:
            self.notify('TOCEntry', (toc_level, escape(title), self.page - self.intro_page + 1, anchor))
            outline_level = 1 if toc_level == 1 else 0
            self.canv.addOutlineEntry(title, anchor, outline_level, closed=False)

    def furniture(self, canvas, doc):
        if doc.page <= 3:
            return
        canvas.saveState()
        canvas.setFillColor(colors.HexColor(GREY))
        canvas.setFont('Body', 10)
        canvas.drawCentredString(WIDTH/2, 27, self.label(doc.page))
        if doc.page not in self.openers:
            title = self.running if doc.page % 2 else 'The Beer Detective'
            size = 8.0
            while pdfmetrics.stringWidth(title, 'Sans', size) > WIDTH-102:
                size -= 0.2
            canvas.setFont('Sans', size)
            canvas.drawString(54, HEIGHT-29, title)
        canvas.restoreState()


class BookContents(TableOfContents):
    """Consistent table rows and unsplit part-heading/first-chapter pairs."""
    def wrap(self, width, height):
        entries = self._lastEntries or [(0, 'Contents', 1, 'introduction')]
        rows, rules = [], []
        for i, (level, title, number, key) in enumerate(entries):
            style = self.levelStyles[level]
            target = escape(key)
            rows.append([Paragraph(f'<link href="#{target}">{title}</link>', style),
                         Paragraph(f'<link href="#{target}">{number}</link>',
                                   ParagraphStyle('TOCPage', parent=style, leftIndent=0, alignment=2))])
            if level == 0:
                rules += [('TOPPADDING', (0, i), (-1, i), 10), ('BOTTOMPADDING', (0, i), (-1, i), 5)]
                if i + 1 < len(entries) and entries[i+1][0] == 1:
                    rules.append(('NOSPLIT', (0, i), (-1, i+1)))
        self._table = Table(rows, colWidths=[width-26, 26], style=TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0), ('TOPPADDING', (0, 0), (-1, -1), 2),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2), *rules]))
        return self._table.wrapOn(self.canv, width, height)


def make_heading(text, anchor, style, level=None, opening=True, running=True):
    para = Paragraph(text, style)
    para.book_anchor = anchor
    para.book_title = re.sub('<[^>]*>', '', text).replace('&amp;', '&')
    para.book_opening = opening
    para.book_running = running
    para.toc_level = level
    return para


def pdf(ast):
    register_fonts()
    st = styles()
    story = [NextPageTemplate('book'), Spacer(1, 1), PageBreak()]
    toc = BookContents()
    toc.levelStyles = [
        ParagraphStyle('TOC0', fontName='Sans', fontSize=10.2, leading=13.4, spaceBefore=9,
                       textColor=colors.HexColor(NAVY)),
        ParagraphStyle('TOC1', fontName='Body', fontSize=10.4, leading=13.2, leftIndent=12,
                       firstLineIndent=0, spaceBefore=2),
    ]
    toc.dotsMinLevel = 1
    section, first, skip = '', True, False
    for block in ast['blocks']:
        kind, val = block['t'], block.get('c')
        if kind == 'Header':
            level, attr, content = val
            anchor, classes = attr[0], attr[1]
            title = inlines(content)
            if 'subtitle' in classes:
                continue
            skip = False
            if anchor == 'title-page':
                section, skip = 'title', True
                story += [Spacer(1, 80), Paragraph('THE BEER<br/>DETECTIVE', st['title']),
                          Paragraph('Uncovering the Myths, Mysteries<br/>and Untold Stories of Beer', st['subtitle']),
                          Paragraph('A WORLD BEER WIKI BOOK PROJECT', st['label']),
                          Spacer(1, 50), Paragraph('Review edition · October 2026', st['small'])]
                continue
            if anchor == 'contents':
                section, skip = 'contents', True
                story += [PageBreak(), make_heading('Contents', anchor, st['heading'], None), toc]
                continue
            if 'note-group' in classes or 'reading-group' in classes:
                section = 'notes' if 'note-group' in classes else 'reading'
                story += [make_heading(title, anchor, st['noteheading'], None, False, False)]
                first = True
                continue
            story.append(PageBreak())
            if 'part' in classes:
                section = 'part'
                label, part_title = plaintext(content).split(' · ', 1)
                story += [Spacer(1, 100), Paragraph(label.upper(), st['label']),
                          make_heading(escape(part_title), anchor, st['part'], 0),
                          HRFlowable(width=35, thickness=2, color=colors.HexColor(ORANGE), spaceAfter=25)]
                # The display heading omits the part number; TOC keeps it.
                story[-2].book_title = plaintext(content)
            elif 'chapter' in classes:
                section = 'chapter'
                number, name = title.split('. ', 1)
                story += [Spacer(1, 24), Paragraph(number.zfill(2), st['label']),
                          make_heading(name, anchor, st['heading'], 1)]
                story[-1].book_title = plaintext(content)
            else:
                section = {'edition': 'edition', 'notes': 'notes', 'further-reading': 'reading'}.get(anchor, 'body')
                include = anchor not in {'edition'}
                story += [Spacer(1, 20), make_heading(title, anchor, st['heading'], 0 if include else None)]
            first = True
        elif skip:
            continue
        elif kind in {'Para', 'Plain'}:
            if section == 'part':
                style = st['parttext']
            elif section == 'edition':
                style = st['small']
            elif section in {'notes', 'reading'}:
                style = st['reading']
            else:
                style = st['first'] if first else st['body']
            story.append(Paragraph(inlines(val), style))
            first = False
        elif kind in {'OrderedList', 'BulletList'}:
            start, items = (val[0][0], val[1]) if kind == 'OrderedList' else (1, val)
            for i, item in enumerate(items, start):
                texts = [inlines(b['c']) for b in item if b['t'] in {'Para', 'Plain'}]
                if len(texts) != len(item):
                    raise ValueError('Nested list not supported in release master.')
                marker = f'{i}. ' if kind == 'OrderedList' else '• '
                story.append(Paragraph(marker + '<br/>'.join(texts), st['note'] if section == 'notes' else st['reading']))
        elif kind == 'HorizontalRule':
            story.append(HRFlowable(width=35, thickness=0.5, color=colors.HexColor(GREY), spaceBefore=15, spaceAfter=15))
        else:
            raise ValueError(f'Unsupported block {kind}')
    raw = BUILD / 'book-unbound.pdf'
    doc = BookDocument(raw)
    doc.multiBuild(story, maxPasses=5)
    writer = PdfWriter(clone_from=str(raw))
    writer.pages[0].merge_page(PdfReader(ROOT / 'design/cover-print.pdf').pages[0])
    writer.add_metadata({'/Title': 'The Beer Detective', '/Author': 'A World Beer Wiki book project',
                         '/Subject': 'Uncovering the Myths, Mysteries and Untold Stories of Beer',
                         '/CreationDate': 'D:20261028000000+00\'00\'', '/ModDate': 'D:20261028000000+00\'00\''})
    for path in [ROOT / 'LICENSE', ROOT / 'NOTICE.md', ROOT / 'design/fonts/EBGaramond-OFL.txt',
                 ROOT / 'design/fonts/BricolageGrotesque-OFL.txt']:
        writer.add_attachment(path.name, path.read_bytes())
    writer.set_page_label(0, 0, prefix='Cover')
    writer.set_page_label(1, doc.intro_page-2, style='/r', start=1)
    writer.set_page_label(doc.intro_page-1, len(writer.pages)-1, style='/D', start=1)
    output = DIST / 'the-beer-detective.pdf'
    with output.open('wb') as handle:
        writer.write(handle)
    return {'pages': len(writer.pages), 'trim_inches': [6, 9], 'body_type': 'EB Garamond 10.7 pt / 14.1 pt',
            'page_locations': doc.locations, 'intro_pdf_page': doc.intro_page}


def epub():
    output = DIST / 'the-beer-detective.epub'
    # The subtitle belongs on the title page, not in the chapter navigation.
    epub_source = re.sub(r'^## (.+) \{\.subtitle \.unnumbered\}$', r'[\1]{.subtitle}', MASTER.read_text(), flags=re.M)
    input_file = BUILD / 'epub-input.md'
    input_file.write_text(epub_source)
    args = ['pandoc', str(input_file), '--from=markdown+bracketed_spans+superscript', '--to=epub3',
            '--output', str(output), '--metadata-file', str(ROOT / 'metadata.yaml'),
            '--epub-cover-image', str(ROOT / 'design/cover.png'), '--epub-title-page=false',
            '--css', str(ROOT / 'design/book.css'), '--split-level=2', '--toc-depth=2']
    for name in ['Body', 'BodyItalic', 'BodyBold', 'Display']:
        args += ['--epub-embed-font', str(BUILD / f'fonts/{name}.ttf')]
    run(args, capture_output=True)
    with zipfile.ZipFile(output) as archive:
        contents = {name: archive.read(name) for name in archive.namelist()}
    ns = {'opf': 'http://www.idpf.org/2007/opf', 'dc': 'http://purl.org/dc/elements/1.1/'}
    ET.register_namespace('', ns['opf'])
    ET.register_namespace('dc', ns['dc'])
    opf_name = next(name for name in contents if name.endswith('.opf'))
    opf = ET.fromstring(contents[opf_name])
    metadata, manifest = opf.find('opf:metadata', ns), opf.find('opf:manifest', ns)
    for meta in metadata.findall('opf:meta', ns):
        if meta.get('property') == 'dcterms:modified':
            meta.text = DATE
    for property_name, value in [('schema:accessMode', 'textual'), ('schema:accessibilityFeature', 'tableOfContents'),
                                 ('schema:accessibilityFeature', 'structuralNavigation')]:
        ET.SubElement(metadata, '{'+ns['opf']+'}meta', {'property': property_name}).text = value
    for i, path in enumerate([ROOT / 'LICENSE', ROOT / 'NOTICE.md', ROOT / 'design/fonts/EBGaramond-OFL.txt',
                              ROOT / 'design/fonts/BricolageGrotesque-OFL.txt']):
        target = 'licenses/' + path.name.replace('.md', '.txt')
        contents[str(Path(opf_name).parent / target)] = path.read_bytes()
        ET.SubElement(manifest, '{'+ns['opf']+'}item', {'id': f'license-{i}', 'href': target, 'media-type': 'text/plain'})
    contents[opf_name] = ET.tostring(opf, encoding='utf-8', xml_declaration=True)
    with zipfile.ZipFile(output, 'w') as archive:
        for name in ['mimetype'] + sorted(n for n in contents if n != 'mimetype'):
            info = zipfile.ZipInfo(name, (2026, 10, 28, 0, 0, 0))
            info.compress_type = zipfile.ZIP_STORED if name == 'mimetype' else zipfile.ZIP_DEFLATED
            archive.writestr(info, contents[name])
    return {'format': 'EPUB 3', 'reflowable': True, 'embedded_fonts': 4}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--format', choices=['all', 'pdf', 'epub'], default='all')
    options = parser.parse_args()
    BUILD.mkdir(exist_ok=True)
    DIST.mkdir(exist_ok=True)
    if not (ROOT / 'LICENSE').exists():
        raise SystemExit('The book LICENSE must be present before building.')
    fonts()
    manifest_file = ROOT / 'research/build-manifest.json'
    manifest = json.loads(manifest_file.read_text()) if manifest_file.exists() else {}
    manifest.update({'master_sha256': hashlib.sha256(MASTER.read_bytes()).hexdigest(),
                     'pandoc_version': run(['pandoc', '--version'], capture_output=True, text=True).stdout.splitlines()[0]})
    if options.format in {'all', 'pdf'}:
        ast = json.loads(run(['pandoc', str(MASTER), '--from=markdown+bracketed_spans+superscript', '--to=json'], capture_output=True, text=True).stdout)
        manifest['pdf'] = pdf(ast)
        manifest['pdf']['master_sha256'] = manifest['master_sha256']
    if options.format in {'all', 'epub'}:
        manifest['epub'] = epub()
        manifest['epub']['master_sha256'] = manifest['master_sha256']
    for format_name in ['pdf', 'epub']:
        file = DIST / f'the-beer-detective.{format_name}'
        if file.exists():
            manifest[format_name].update({'bytes': file.stat().st_size, 'sha256': hashlib.sha256(file.read_bytes()).hexdigest()})
    manifest_file.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in manifest.items() if k != 'pdf'}, indent=2))
    if 'pdf' in manifest:
        print(f"PDF: {manifest['pdf']['pages']} pages, 6 × 9 inches")


if __name__ == '__main__':
    main()
