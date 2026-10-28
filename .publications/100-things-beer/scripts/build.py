#!/usr/bin/env python3
"""Build the two reading editions from the single canonical Markdown manuscript.

Requires Python 3.10+, ReportLab, PyYAML, pypdf, and Pandoc 3.x on PATH.
All generated intermediate files stay in .build/; no network is used.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from functools import partial
import html
import json
import os
from pathlib import Path
import re
import subprocess
import uuid
import zipfile

import yaml

ROOT = Path(__file__).resolve().parents[1]
STEM = "100-things-beer-teaches-us"
SOURCE = ROOT / (STEM + ".md")
BUILD = ROOT / ".build"
EPOCH = int(datetime(2026, 10, 28, tzinfo=timezone.utc).timestamp())


def run(command, **kwargs):
    return subprocess.run(command, check=True, **kwargs)


def source_document():
    text = SOURCE.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise ValueError("The canonical manuscript needs YAML publication metadata.")
    metadata = yaml.safe_load(match[1])
    return text, metadata


def epub(metadata):
    destination = ROOT / (STEM + ".epub")
    env = dict(os.environ, SOURCE_DATE_EPOCH=str(EPOCH))
    cmd = ["pandoc", str(SOURCE), "--from=markdown", "--to=epub3",
           "--output=" + str(destination), "--standalone", "--toc", "--epub-title-page=false",
           "--toc-depth=2", "--split-level=2",
           "--epub-cover-image=" + str(ROOT / "assets/cover.png"),
           "--css=" + str(ROOT / "assets/epub.css"),
           "--metadata=identifier:urn:uuid:" + str(uuid.uuid5(
               uuid.NAMESPACE_URL, "https://github.com/grove/world-beer-wiki/books/100-things-beer/2026")),
           "--metadata=lang:en", "--metadata=date:2026-10-28",
           "--resource-path=" + str(ROOT)]
    for font in sorted((ROOT / "assets/fonts").glob("*.ttf")):
        cmd.append("--epub-embed-font=" + str(font))
    run(cmd, cwd=ROOT, env=env)
    # Keep the source license and font license inside the book package, and make
    # ZIP ordering/timestamps reproducible. The full source license is also a
    # readable appendix in the manuscript and both reading editions.
    with zipfile.ZipFile(destination) as archive:
        entries = {name: archive.read(name) for name in archive.namelist()}
    entries["META-INF/source-license.txt"] = (ROOT / "LICENSE-APACHE-2.0.txt").read_bytes()
    entries["META-INF/font-license.txt"] = (ROOT / "assets/fonts/LICENSE.txt").read_bytes()
    with zipfile.ZipFile(destination, "w") as archive:
        for name in ["mimetype"] + sorted(n for n in entries if n != "mimetype"):
            info = zipfile.ZipInfo(name, (2026, 10, 28, 0, 0, 0))
            info.compress_type = zipfile.ZIP_STORED if name == "mimetype" else zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, entries[name])
    print(f"EPUB: {destination.name} ({destination.stat().st_size:,} bytes)")


def pdf(metadata):
    os.environ["SOURCE_DATE_EPOCH"] = str(EPOCH)
    from reportlab import rl_config
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen.canvas import Canvas
    from reportlab.platypus import (BaseDocTemplate, Flowable, Frame, KeepTogether,
                                  PageBreak, PageTemplate, Paragraph, Spacer)
    from reportlab.platypus.tableofcontents import TableOfContents

    rl_config.warnOnMissingFontGlyphs = 1
    fontdir = ROOT / "assets/fonts"
    for name, file in [("Book", "SourceSerif4-Regular.ttf"),
                       ("BookItalic", "SourceSerif4-It.ttf"),
                       ("BookBold", "SourceSerif4-Semibold.ttf"),
                       ("BookBoldItalic", "SourceSerif4-SemiboldIt.ttf")]:
        pdfmetrics.registerFont(TTFont(name, str(fontdir / file)))
    pdfmetrics.registerFontFamily("Book", normal="Book", bold="BookBold",
                                  italic="BookItalic", boldItalic="BookBoldItalic")
    ink = colors.HexColor("#173343")
    teal = colors.HexColor("#286A6B")
    amber = colors.HexColor("#A46625")
    grey = colors.HexColor("#617079")
    light = colors.HexColor("#E6DED1")
    width, height = 432, 648
    margin, top, bottom = 42, 45, 45
    usable = width - 2 * margin
    styles = {
        "body": ParagraphStyle("Body", fontName="Book", fontSize=10.8,
            leading=14.4, textColor=ink, spaceAfter=7,
            allowWidows=0, allowOrphans=0, splitLongWords=True),
        "section": ParagraphStyle("Section", fontName="BookBold", fontSize=26,
            leading=29.5, textColor=ink, spaceAfter=24, keepWithNext=True),
        "lesson": ParagraphStyle("Lesson", fontName="BookBold", fontSize=20,
            leading=23, textColor=ink, spaceAfter=14, keepWithNext=True),
        "subhead": ParagraphStyle("Subhead", fontName="BookBold", fontSize=13,
            leading=17, textColor=teal, spaceBefore=12, spaceAfter=8, keepWithNext=True),
        "kicker": ParagraphStyle("Kicker", fontName="Helvetica", fontSize=8,
            leading=10, textColor=amber, spaceAfter=9, keepWithNext=True),
        "note": ParagraphStyle("Note", fontName="Book", fontSize=9.4,
            leading=12.8, textColor=ink, spaceAfter=10, allowWidows=0, allowOrphans=0),
        "notehead": ParagraphStyle("NoteHeading", fontName="BookBold", fontSize=11.5,
            leading=15, textColor=teal, spaceBefore=13, spaceAfter=6, keepWithNext=True),
        "license": ParagraphStyle("License", fontName="Book", fontSize=9.0,
            leading=12.2, textColor=ink, spaceAfter=6, allowWidows=0, allowOrphans=0),
    }
    ast = json.loads(run(["pandoc", str(SOURCE), "--from=markdown", "--to=json"],
                         capture_output=True, text=True).stdout)
    notes = []
    lesson_titles = {}
    current_part = ""

    def plain(items):
        result = []
        for item in items:
            typ, val = item["t"], item.get("c")
            if typ == "Str": result.append(val)
            elif typ in ("Space", "SoftBreak", "LineBreak"): result.append(" ")
            elif typ in ("Emph", "Strong", "SmallCaps", "Superscript", "Subscript"):
                result.append(plain(val))
            elif typ in ("Link", "Image", "Span"): result.append(plain(val[1]))
            elif typ == "Code": result.append(val[1])
            elif typ == "Quoted": result.append(plain(val[1]))
        return "".join(result)

    def inline(items, collect_notes=True):
        result = []
        for item in items:
            typ, val = item["t"], item.get("c")
            if typ == "Str": result.append(html.escape(val))
            elif typ in ("Space", "SoftBreak"): result.append(" ")
            elif typ == "LineBreak": result.append("<br/>")
            elif typ in ("Emph", "Strong", "Superscript", "Subscript"):
                tag = {"Emph":"i", "Strong":"b", "Superscript":"super", "Subscript":"sub"}[typ]
                result.append(f"<{tag}>{inline(val, collect_notes)}</{tag}>")
            elif typ == "SmallCaps": result.append(inline(val, collect_notes))
            elif typ == "Code": result.append(html.escape(val[1]))
            elif typ == "Quoted": result.append("“" + inline(val[1], collect_notes) + "”")
            elif typ == "Span": result.append(inline(val[1], collect_notes))
            elif typ == "Link":
                target = val[2][0]
                result.append('<link href="' + html.escape(target, quote=True) +
                              '" color="#286A6B">' + inline(val[1], collect_notes) + "</link>")
            elif typ == "Note":
                if not collect_notes:
                    raise ValueError("Nested source notes are not supported")
                number = len(notes) + 1
                notes.append(val)
                result.append(f'<super><link href="#note-{number:03d}" color="#286A6B">[{number}]</link></super>')
            elif typ == "Math": result.append(html.escape(val[1]))
            elif typ == "RawInline" and val[0] == "html":
                if re.match(r'<(?:a|span)\s+(?:id|name)=', val[1]):
                    match = re.search(r'(?:id|name)=["\']([^"\']+)', val[1])
                    if match: result.append('<a name="' + match[1] + '"/>')
            elif typ == "Image":
                raise ValueError("Place illustration assets through the explicit cover flow")
            else: raise ValueError(f"Unhandled inline: {typ}")
        return "".join(result)

    class FullCover(Flowable):
        def __init__(self):
            Flowable.__init__(self)
            self.width, self.height = usable, height-top-bottom-12
        def draw(self):
            self.canv.saveState()
            self.canv.resetTransforms()
            self.canv.drawImage(str(ROOT / "assets/cover.png"), 0, 0, width, height)
            self.canv.restoreState()

    class TitleLeaf(Flowable):
        def __init__(self):
            Flowable.__init__(self)
            self.width, self.height = usable, height-top-bottom-12
        def draw(self):
            c = self.canv
            c.setFillColor(amber)
            c.setFont("BookBold", 87)
            c.drawString(0, self.height-105, "100")
            p = Paragraph("Things Beer Teaches Us<br/>About History,<br/>Science &amp; Culture",
                ParagraphStyle("Title", fontName="BookBold", fontSize=29,
                               leading=34, textColor=ink))
            pw, ph = p.wrap(usable, 250)
            p.drawOn(c, 0, self.height-130-ph)
            p = Paragraph(html.escape(metadata.get("subtitle", "")),
                ParagraphStyle("Subtitle", fontName="BookItalic", fontSize=15,
                               leading=20, textColor=teal))
            pw, ph = p.wrap(usable-10, 100)
            p.drawOn(c, 0, self.height-340-ph)
            c.setStrokeColor(light)
            c.line(0, 85, usable, 85)
            c.setFont("Helvetica", 8)
            c.setFillColor(grey)
            c.drawString(0, 63, "A FREE READING EDITION")
            c.drawString(0, 46, "Prepared from World Beer Wiki, research edition 1.19")
            c.drawString(0, 29, "28 October 2026")

    class PartLeaf(Flowable):
        def __init__(self, title, description, key, label):
            Flowable.__init__(self)
            self.width, self.height = usable, height-top-bottom-12
            self.title, self.description, self.key, self.label = title, description, key, label
        def draw(self):
            c = self.canv
            c.setFillColor(amber)
            c.setFont("Helvetica", 10)
            c.drawString(0, self.height-125, self.label)
            p = Paragraph(html.escape(self.title), ParagraphStyle("PartTitle", fontName="BookBold",
                          fontSize=37, leading=43, textColor=ink))
            pw, ph = p.wrap(usable, 240)
            p.drawOn(c, 0, self.height-155-ph)
            c.setStrokeColor(amber)
            c.setLineWidth(1)
            c.line(0, self.height-180-ph, 55, self.height-180-ph)
            y = self.height-204-ph
            for markup in self.description:
                p = Paragraph(markup, styles["body"])
                pw, ph = p.wrap(usable, 400)
                y -= ph
                p.drawOn(c, 0, y)
                y -= 10

    class BookDoc(BaseDocTemplate):
        def beforeDocument(self):
            self.running = ""
        def afterFlowable(self, flowable):
            if isinstance(flowable, PartLeaf):
                self.running = flowable.title.upper()
                self.canv.bookmarkPage(flowable.key)
                self.canv.addOutlineEntry(flowable.label + " — " + flowable.title, flowable.key, 0, False)
                self.notify("TOCEntry", (0, flowable.label + " — " + flowable.title, self.page, flowable.key))
            if isinstance(flowable, Paragraph) and hasattr(flowable, "_bookkey"):
                key, label, level, toc = flowable._bookkey
                self.canv.bookmarkPage(key)
                if toc:
                    self.canv.addOutlineEntry(label, key, level, False)
                    self.notify("TOCEntry", (level, html.escape(label), self.page, key))
                if level == 0: self.running = label.upper()

    def page_frame(canvas, doc):
        if doc.page <= 2: return
        canvas.saveState()
        canvas.setStrokeColor(light)
        canvas.setLineWidth(0.5)
        canvas.line(margin, 34, width-margin, 34)
        canvas.setFillColor(grey)
        canvas.setFont("Helvetica", 8)
        canvas.drawString(margin, 22, "100 THINGS BEER TEACHES US")
        canvas.drawRightString(width-margin, 22, str(doc.page))
        canvas.restoreState()

    doc = BookDoc(str(ROOT / (STEM + ".pdf")), pagesize=(width, height),
                  leftMargin=margin, rightMargin=margin, topMargin=top, bottomMargin=bottom,
                  invariant=1, creator="World Beer Wiki book production",
                  title=metadata["title"], author=metadata.get("author", "World Beer Wiki book project"),
                  subject=metadata.get("subtitle", ""))
    frame = Frame(margin, bottom, usable, height-top-bottom, id="text", leftPadding=0,
                  rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates(PageTemplate(id="Book", frames=[frame], onPage=page_frame))
    story = [FullCover(), PageBreak(), TitleLeaf()]
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle("TOCPart", fontName="BookBold", fontSize=11.2, leading=15,
                       textColor=ink, spaceBefore=10, spaceAfter=4, leftIndent=0, firstLineIndent=0),
        ParagraphStyle("TOCLesson", fontName="Book", fontSize=9.7, leading=12.5,
                       textColor=ink, spaceBefore=1.5, spaceAfter=1.5, leftIndent=12, firstLineIndent=0),
    ]

    def add_heading(text, key, kind="section", level=0, include_toc=True):
        p = Paragraph('<a name="' + key + '"/>' + html.escape(text), styles[kind])
        p._bookkey = (key, text, level, include_toc)
        story.append(p)

    def ordinary_block(block, style="body"):
        typ, val = block["t"], block.get("c")
        if typ in ("Para", "Plain"):
            markup = inline(val)
            if markup.strip(): story.append(Paragraph(markup, styles[style]))
        elif typ in ("BulletList", "OrderedList"):
            items = val if typ == "BulletList" else val[1]
            for index, item in enumerate(items, 1):
                for j, child in enumerate(item):
                    if child["t"] in ("Para", "Plain"):
                        bullet = "•" if typ == "BulletList" else f"{index}."
                        story.append(Paragraph(inline(child["c"]), styles[style], bulletText=bullet if j == 0 else None))
                    else: ordinary_block(child, style)
        elif typ == "BlockQuote":
            for child in val: ordinary_block(child, style)
        elif typ == "Div":
            for child in val[1]: ordinary_block(child, style)
        elif typ == "HorizontalRule": story.append(Spacer(1, 12))
        elif typ in ("RawBlock", "Null"): pass
        elif typ == "CodeBlock":
            story.append(Paragraph(html.escape(val[1]).replace("\n", "<br/>"), styles["note"]))
        else: raise ValueError(f"Unhandled block: {typ}")

    blocks = ast["blocks"]
    i, skip_title, skip_contents, license_mode = 0, True, False, False
    while i < len(blocks):
        block = blocks[i]
        if block["t"] == "Header":
            level, attrs, content = block["c"]
            label, key = plain(content), attrs[0]
            if key == "title-page":
                skip_title = True; i += 1; continue
            skip_title = False
            if key == "contents":
                story.append(PageBreak()); add_heading("Contents", key, include_toc=False)
                story.append(toc); skip_contents = True; i += 1; continue
            skip_contents = False
            if key.startswith("part-"):
                match = re.match(r"Part\s+([IVX]+)\s*[—–-]\s*(.*)", label)
                if not match: raise ValueError(f"Invalid part heading: {label}")
                description = []
                j = i + 1
                while j < len(blocks) and blocks[j]["t"] != "Header":
                    if blocks[j]["t"] in ("Para", "Plain"):
                        description.append(inline(blocks[j]["c"]))
                    j += 1
                story.append(PageBreak())
                current_part = match[2].replace("Beer & ", "").upper()
                story.append(PartLeaf(match[2], description, key, "PART " + match[1]))
                i = j; continue
            if key.startswith("lesson-"):
                number = int(key.split("-")[1])
                title = re.sub(r"^\d+\.\s*", "", label)
                lesson_titles[number] = title
                story.append(PageBreak())
                story.append(Paragraph(f"LESSON {number:02d}  /  {current_part}", styles["kicker"]))
                add_heading(title, key, "lesson", 1, False)
                # The title shown in the reading page excludes the repeated
                # number; navigation retains it.
                story[-1]._bookkey = (key, f"{number}. {title}", 1, True)
                i += 1; continue
            if key == "notes":
                story.append(PageBreak()); add_heading(label, key)
                story.append(Paragraph("Each note links back to its lesson and outward to the research. The access register in the production bundle gives the exact scope of this edition’s source checks.", styles["body"]))
                for number, note in enumerate(notes, 1):
                    title = lesson_titles.get(number, "Source note")
                    p = Paragraph(f'<a name="note-{number:03d}"/><link href="#lesson-{number:03d}" color="#286A6B">{number}. {html.escape(title)} ↗</link>', styles["notehead"])
                    story.append(p)
                    for child in note:
                        if child["t"] in ("Para", "Plain"):
                            story.append(Paragraph(inline(child["c"], False), styles["note"]))
                        else: ordinary_block(child, "note")
                i += 1; continue
            if level == 1:
                story.append(PageBreak()); add_heading(label, key)
                license_mode = key == "apache-license"
            else:
                add_heading(label, key or "sub-"+str(i), "subhead", 1, False)
        elif not skip_title and not skip_contents:
            ordinary_block(block, "license" if license_mode else "body")
        i += 1
    if len(notes) != 100:
        raise ValueError(f"Expected 100 source notes, got {len(notes)}")
    doc.multiBuild(story, canvasmaker=partial(Canvas, invariant=1, pageCompression=1))
    destination = ROOT / (STEM + ".pdf")
    print(f"PDF: {destination.name} ({destination.stat().st_size:,} bytes)")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=["all", "epub", "pdf"], default="all")
    args = parser.parse_args()
    BUILD.mkdir(exist_ok=True)
    _, metadata = source_document()
    if args.format in ("all", "epub"): epub(metadata)
    if args.format in ("all", "pdf"): pdf(metadata)


if __name__ == "__main__":
    main()
