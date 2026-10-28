#!/usr/bin/env python3
"""Draw three original vector covers and export the selected front cover."""
from pathlib import Path
from xml.sax.saxutils import escape
import shutil
import sys
import xml.etree.ElementTree as ET

from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen

ROOT = Path(__file__).resolve().parents[1]
DESIGN = ROOT / 'design'
BUILD = ROOT / '.build'
BUILD.mkdir(exist_ok=True)


def fonts():
    out = BUILD / 'fonts'
    out.mkdir(exist_ok=True)
    specifications = [
        ('EBGaramond-variable.ttf', 'Body.ttf', {'wght': 400}),
        ('EBGaramond-variable.ttf', 'BodyBold.ttf', {'wght': 650}),
        ('EBGaramond-Italic-variable.ttf', 'BodyItalic.ttf', {'wght': 400}),
        ('BricolageGrotesque-variable.ttf', 'Display.ttf',
         {'wght': 800, 'wdth': 90, 'opsz': 48}),
        ('BricolageGrotesque-variable.ttf', 'Sans.ttf',
         {'wght': 450, 'wdth': 100, 'opsz': 14}),
    ]
    for source, target, axes in specifications:
        destination = out / target
        unique_name = 'BeerDetective' + destination.stem
        cached_name = TTFont(destination)['name'].getDebugName(6) if destination.exists() else None
        if cached_name != unique_name or destination.stat().st_mtime < (DESIGN / 'fonts' / source).stat().st_mtime:
            font = instantiateVariableFont(TTFont(DESIGN / 'fonts' / source), axes, inplace=True)
            # Distinct PostScript names prevent PDF engines conflating different
            # static instances; derivative names avoid reserved upstream names.
            for record in font['name'].names:
                if record.nameID in {1, 3, 4, 6}:
                    value = unique_name
                elif record.nameID == 2:
                    value = 'Regular'
                else:
                    continue
                font['name'].setName(value, record.nameID, record.platformID, record.platEncID, record.langID)
            font.save(destination)
    conf = BUILD / 'fonts.conf'
    conf.write_text('<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd">'
                    '<fontconfig><dir>' + escape(str(out)) + '</dir>'
                    '<cachedir>' + escape(str(BUILD / 'font-cache')) + '</cachedir>'
                    '</fontconfig>', encoding='utf-8')
    return conf


def text(x, y, content, size, fill, weight=800, family='Bricolage Grotesque', spacing=0):
    return (f'<text x="{x}" y="{y}" fill="{fill}" font-family="{family}" '
            f'font-weight="{weight}" font-size="{size}" letter-spacing="{spacing}">'
            f'{escape(content)}</text>')


def svg(label, color, content):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="2700" '
            f'viewBox="0 0 600 900" role="img" aria-labelledby="title desc">'
            f'<title id="title">The Beer Detective — {escape(label)}</title>'
            '<desc id="desc">An original typographic book cover with a spare, flat vector illustration.</desc>'
            f'<rect width="600" height="900" fill="{color}"/>{content}</svg>')


def concept_a():
    navy, cream, orange = '#152D3B', '#FFF2D5', '#ED6036'
    c = text(42, 64, 'THE', 34, navy, spacing=3)
    c += text(35, 277, 'BEER', 226, cream)
    c += text(40, 388, 'DETECTIVE', 109, navy)
    c += text(44, 460, 'Uncovering the Myths, Mysteries', 24, navy, 450)
    c += text(44, 492, 'and Untold Stories of Beer', 24, navy, 450)
    # A deliberately schematic clay tablet. Marks are graphic texture, not a
    # purported transcription of a historical inscription.
    c += '<g transform="translate(223 566) rotate(-8 80 96)">'
    c += f'<path d="M12 9 Q78 -2 145 10 L154 162 Q151 185 128 190 L17 184 Q-2 176 2 153 Z" fill="{cream}"/>'
    for x, y in [(27,35),(68,32),(109,37),(24,77),(68,77),(110,78),(29,119),(71,119),(111,121),(32,155),(78,155)]:
        c += f'<path d="M{x} {y} l16 -7 l-3 16 Z M{x+3} {y+2} l18 8" fill="{navy}" stroke="{navy}" stroke-width="2.5"/>'
    c += '</g>'
    c += text(44, 847, 'A WORLD BEER WIKI BOOK', 16, navy, 450, spacing=1.2)
    return svg('The evidence', orange, c)


def concept_b():
    blue, yellow, coral = '#204AC8', '#F9EFAB', '#FF7D6A'
    c = text(44, 66, 'THE BEER', 64, yellow)
    c += text(42, 145, 'DETECTIVE', 67, yellow)
    c += f'<circle cx="286" cy="435" r="146" fill="{yellow}"/>'
    c += f'<circle cx="286" cy="435" r="115" fill="{blue}"/>'
    c += f'<path d="M384 540 L480 674" stroke="{yellow}" stroke-width="47" stroke-linecap="round"/>'
    c += f'<ellipse cx="266" cy="428" rx="47" ry="65" transform="rotate(-25 266 428)" fill="{coral}"/>'
    c += f'<ellipse cx="316" cy="371" rx="28" ry="36" transform="rotate(30 316 371)" fill="{coral}"/>'
    c += text(44, 750, 'Uncovering the Myths, Mysteries', 24, yellow, 450)
    c += text(44, 784, 'and Untold Stories of Beer', 24, yellow, 450)
    c += text(44, 853, 'A WORLD BEER WIKI BOOK', 16, yellow, 450, spacing=1.2)
    return svg('Look closer', blue, c)


def concept_c():
    green, pink, cream = '#164D40', '#F4B8B9', '#FFF8E8'
    c = text(42, 66, 'THE', 38, cream, spacing=4)
    c += text(36, 192, 'BEER', 146, pink)
    c += text(40, 275, 'DETECTIVE', 65, cream)
    c += f'<path d="M188 405 Q174 452 186 494 L217 686 Q283 714 363 684 L399 490 Q409 443 392 405 Z" fill="{pink}"/>'
    c += f'<path d="M188 405 Q282 435 392 405 Q284 370 188 405 Z" fill="{cream}"/>'
    c += f'<path d="M223 516 Q286 477 359 518 Q302 568 248 609" fill="none" stroke="{green}" stroke-width="19" stroke-linecap="round"/>'
    c += f'<circle cx="262" cy="657" r="11" fill="{green}"/>'
    c += text(44, 762, 'Uncovering the Myths, Mysteries', 24, cream, 450)
    c += text(44, 794, 'and Untold Stories of Beer', 24, cream, 450)
    c += text(44, 853, 'A WORLD BEER WIKI BOOK', 16, pink, 450, spacing=1.2)
    return svg('The curious vessel', green, c)


def main():
    conf = fonts()
    if (BUILD / 'vendor').exists():
        sys.path.insert(0, str(BUILD / 'vendor'))
    import cairosvg
    def outlined(source):
        """Export with exact bundled glyph outlines; retain editable text SVGs."""
        root = ET.fromstring(source)
        for element in list(root):
            if not element.tag.endswith('text'):
                continue
            font = TTFont(BUILD / 'fonts' / ('Display.ttf' if int(element.get('font-weight')) >= 700 else 'Sans.ttf'))
            glyphs = font.getGlyphSet()
            cmap = font.getBestCmap()
            units = font['head'].unitsPerEm
            size = float(element.get('font-size'))
            scale = size / units
            x, y = float(element.get('x')), float(element.get('y'))
            group = ET.Element('{http://www.w3.org/2000/svg}g', {'fill':element.get('fill')})
            for char in element.text:
                name = cmap.get(ord(char), '.notdef')
                pen = SVGPathPen(glyphs)
                glyphs[name].draw(pen)
                ET.SubElement(group, '{http://www.w3.org/2000/svg}path',
                              {'d':pen.getCommands(), 'transform':f'translate({x} {y}) scale({scale} {-scale})'})
                x += font['hmtx'][name][0]*scale + float(element.get('letter-spacing', '0'))
            root.insert(list(root).index(element), group)
            root.remove(element)
        return ET.tostring(root)
    for label, maker in [('a', concept_a), ('b', concept_b), ('c', concept_c)]:
        file = DESIGN / f'concept-{label}.svg'
        file.write_text(maker(), encoding='utf-8')
        cairosvg.svg2png(bytestring=outlined(maker()), output_width=600, output_height=900,
                        write_to=str(BUILD / f'concept-{label}.png'))
    shutil.copyfile(DESIGN / 'concept-a.svg', DESIGN / 'cover.svg')
    cairosvg.svg2png(bytestring=outlined(concept_a()), output_width=1800, output_height=2700,
                    write_to=str(DESIGN / 'cover.png'))
    # A 6 × 9 inch front cover, with the same vector artwork and exact glyph outlines.
    print_svg = (DESIGN / 'cover.svg').read_text().replace('width="1800" height="2700"',
                                                         'width="6in" height="9in"')
    (BUILD / 'cover-print.svg').write_text(print_svg, encoding='utf-8')
    cairosvg.svg2pdf(bytestring=outlined(print_svg), write_to=str(DESIGN / 'cover-print.pdf'))
    from PIL import Image, ImageDraw, ImageFont
    Image.open(DESIGN / 'cover.png').convert('RGB').save(DESIGN / 'cover.png', dpi=(300, 300))
    sheet = Image.new('RGB', (1920, 1020), '#eeeae2')
    draw = ImageDraw.Draw(sheet)
    for i, name in enumerate('abc'):
        im = Image.open(BUILD / f'concept-{name}.png').convert('RGB')
        sheet.paste(im, (30 + 630*i, 30))
        draw.text((30 + 630*i, 955), ['A  THE EVIDENCE — SELECTED', 'B  LOOK CLOSER', 'C  THE CURIOUS VESSEL'][i], fill='#152D3B', font=ImageFont.truetype(str(BUILD / 'fonts/Sans.ttf'), 20))
    sheet.save(DESIGN / 'cover-concepts.png')
    print('Exported three concepts, editable cover, 1800 × 2700 PNG and vector front-cover PDF.')


if __name__ == '__main__':
    main()
