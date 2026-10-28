#!/usr/bin/env python3
"""Assemble the release master and evidence map from reviewed working files.

The PDF/EPUB builder reads only the resulting master. Run this deliberately
after editing a working chapter; it never runs implicitly during typesetting.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
BASELINE = '3b985c19a9dcccef8d334be54b5405e42093e812'
WIKI = f'https://github.com/grove/world-beer-wiki/blob/{BASELINE}/'
PARTS = [
    ('I', 'What Survives', 'A stone, a poem, a tablet, a pot. Each preserves something different. The first six investigations follow the distance between an object and the story it can support.'),
    ('II', 'Inside the Glass', 'Aroma, bitterness, light, time and foam turn the glass into a small laboratory. The explanations lead through things a brewer can control and things a drinker may never notice.'),
    ('III', 'A Living Trade', 'The work moves between households, shared buildings, fields and places of sale. Following the drink makes its makers harder to leave out of the story.'),
    ('IV', 'The Unfinished Case', 'Laws, anniversaries and expectations shape what beer seems to be. Beyond them lie the practical questions of keeping it cold, growing its ingredients and deciding what knowledge to carry forward.'),
]
NOTE = re.compile(r'^\[\^([^\]]+)\]:\s*(.*?)(?=^\[\^|\Z)', re.M | re.S)
CALL = re.compile(r'\[\^([^\]]+)\]')


def split_notes(text):
    matches = list(NOTE.finditer(text))
    body = text[:matches[0].start()].rstrip() if matches else text.rstrip()
    notes = {m[1]: m[2].strip() for m in matches}
    calls = CALL.findall(body)
    if len(notes) != len(matches) or set(calls) != set(notes):
        raise ValueError(f'Note mismatch: calls={set(calls)}, definitions={set(notes)}')
    return body, notes


def local_notes(text):
    body, notes = split_notes(text)
    order = list(dict.fromkeys(CALL.findall(body)))
    indices = {key: i + 1 for i, key in enumerate(order)}
    seen = Counter()
    def call(match):
        key = match[1]
        seen[key] += 1
        suffix = '' if seen[key] == 1 else f'-{seen[key]}'
        return f'[]{{#ref-{key}{suffix}}}^[{indices[key]}](#note-{key})^'
    body = CALL.sub(call, body)
    items = []
    for key in order:
        if seen[key] == 1:
            returns = f'[Back to text](#ref-{key})'
        else:
            returns = ' · '.join(f'[Return {i}](#ref-{key}' + (f'-{i}' if i > 1 else '') + ')'
                                 for i in range(1, seen[key] + 1))
        items.append(f'{indices[key]}. []{{#note-{key}}} {notes[key]} {returns}.')
    return body, '\n\n'.join(items), len(notes)


def word_count(text):
    body, _ = split_notes(text)
    body = re.sub(r'^#{1,6} .*$', '', body, flags=re.M)
    body = CALL.sub('', body)
    body = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', body)
    return len(re.findall(r"\b\w+(?:[’'-]\w+)*\b", body))


def portable_links(text, source):
    """Resolve a fragment's local wiki links before moving it into the master."""
    def replace(match):
        label, target = match[1], match[2]
        url = urlsplit(target)
        if url.scheme or target.startswith('#'):
            return match[0]
        resolved = (source.parent / unquote(url.path)).resolve()
        if not resolved.is_file():
            raise ValueError(f'Broken source-relative link in {source}: {target}')
        relative = resolved.relative_to(ROOT.parents[1]).as_posix()
        suffix = ('#' + url.fragment) if url.fragment else ''
        if relative.startswith('books/the-beer-detective/chapters/'):
            return f'[{label}](#chapter-{resolved.name[:2]})'
        return f'[{label}]({WIKI}{relative}{suffix})'
    return re.sub(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)', replace, text)


def assemble():
    chapters = sorted((ROOT / 'chapters').glob('[0-9][0-9]-*.md'))
    if len(chapters) != 24 or [int(p.name[:2]) for p in chapters] != list(range(1, 25)):
        raise ValueError('Exactly 24 numbered chapters are required.')
    titles = {int(p.name[:2]): p.read_text().splitlines()[0][2:] for p in chapters}
    records = []
    for name in ['part-i', 'part-ii', 'part-iii', 'part-iva', 'part-ivb']:
        records.extend(json.loads((ROOT / 'research' / f'{name}-sources.json').read_text()))
    required = {'chapter', 'claim', 'wiki_paths', 'sources', 'uncertainty'}
    for record in records:
        assert required <= record.keys(), record
        assert record['sources'] and record['wiki_paths'], record
        for path in record['wiki_paths']:
            assert (ROOT.parents[1] / path).is_file(), path
    counts = Counter(r['chapter'] for r in records)
    assert all(counts[n] >= 5 for n in range(1, 25)), counts
    records.sort(key=lambda r: r['chapter'])
    (ROOT / 'research/claim-register.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')

    front_raw = (ROOT / 'front-matter.md').read_text()
    front, intro_notes, intro_note_count = local_notes(front_raw)
    toc = ['# Contents {#contents .unnumbered}', '', '- [The Case for Beer](#introduction)']
    for i, (roman, title, _) in enumerate(PARTS):
        toc += [f'- [Part {roman} · {title}](#part-{roman.lower()})']
        toc += [f'  - [{titles[n]}](#chapter-{n:02d})' for n in range(i*6+1, i*6+7)]
    toc += ['- [Afterword: An Empty Glass](#afterword)', '- [Acknowledgments](#acknowledgments)',
            '- [Research Note](#research-note)', '- [Notes](#notes)',
            '- [Selected Further Reading](#further-reading)', '']
    front = front.replace('# The Case for Beer', '\n'.join(toc) + '\n# The Case for Beer', 1)
    pieces = [front]
    all_notes = ['# Notes {#notes .unnumbered}',
                 'Notes restart at 1 in each chapter. Each entry links to its source and back to the passage. Source access was checked on 28 October 2026 unless otherwise stated.',
                 '## Introduction {#notes-intro .note-group}', intro_notes]
    stats = []
    for i, path in enumerate(chapters):
        number = i + 1
        if i % 6 == 0:
            roman, title, description = PARTS[i//6]
            pieces += [f'# Part {roman} · {title} {{#part-{roman.lower()} .part}}', description]
        raw = portable_links(path.read_text(), path)
        body, notes, note_count = local_notes(raw)
        body = re.sub(r'^# .*', f'## {titles[number]} {{#chapter-{number:02d} .chapter}}', body, count=1)
        pieces.append(body)
        all_notes += [f'## {titles[number]} {{#notes-{number:02d} .note-group}}', notes]
        stats.append({'chapter': number, 'title': titles[number], 'narrative_words': word_count(raw),
                      'notes': note_count, 'registered_claims': counts[number], 'file': str(path.relative_to(ROOT))})
    back = (ROOT / 'back-matter.md').read_text().strip()
    pieces += [back, '\n\n'.join(all_notes)]

    # A deliberately selected route, with the exhaustive bibliography retained
    # in the chapter notes and the separate evidence map.
    reading = ['# Selected Further Reading {#further-reading .unnumbered}',
               'These starting points offer a shorter route into the investigations. The chapter notes and accompanying source map contain the fuller bibliography and precise access limits. Inclusion does not imply endorsement of this book.']
    used = set()
    for i, (roman, title, _) in enumerate(PARTS):
        reading.append(f'## {title} {{#reading-{roman.lower()} .reading-group}}')
        for number in range(i*6+1, i*6+7):
            options = [s for r in records if r['chapter'] == number for s in r['sources'] if s['url'] not in used]
            if not options:
                continue
            preferred = [s for s in options if re.search(r'full', s['access'], re.I) and not re.search(r'not (read|examined|accessed)|not a full|no full|not available|not retrieved|full.*(failed|blocked)', s['access'], re.I)]
            source = (preferred or options)[0]
            used.add(source['url'])
            reading.append(f"- **Chapter {number}:** [{source['title']}]({source['url']}). {source['access']}")
    pieces.append('\n\n'.join(reading))
    manuscript = '\n\n'.join(pieces).rstrip() + '\n'
    (ROOT / 'the-beer-detective.md').write_text(manuscript)

    source_map = ['# Sources and chapters',
                  f'Research baseline: World Beer Wiki edition 1.19, commit [`{BASELINE}`](https://github.com/grove/world-beer-wiki/commit/{BASELINE}). Source checks closed 28 October 2026.',
                  'This map is generated from the reviewed claim register. It records actual access rather than treating a citation as proof of a full reading. Entries describe evidence and outstanding questions; they are not endorsements. The companion selection and review records explain narrative choices.']
    for number in range(1, 25):
        group = [r for r in records if r['chapter'] == number]
        wiki_paths = sorted({p for r in group for p in r['wiki_paths']})
        sources = {s['url']: s for r in group for s in r['sources']}
        source_map += [f'## {titles[number]}', '### Originating wiki routes',
                       '\n'.join(f'- [{p}]({WIKI}{p})' for p in wiki_paths), '### Independent sources and access']
        for s in sources.values():
            source_map.append(f"- [{s['title']}]({s['url']}). **Access:** {s['access']} **Location:** {s.get('locator', 'See chapter note')}. **Consulted:** {s['accessed_on']}.")
        source_map.append('### Claims requiring care and unresolved questions')
        source_map += [f"- **{r['claim']}** {r['uncertainty']}" for r in group]
    (ROOT / 'sources-and-chapters.md').write_text('\n\n'.join(source_map).rstrip() + '\n')
    introduction = front_raw[front_raw.index('# The Case for Beer'):]
    afterword = back.split('# Acknowledgments', 1)[0]
    narrative = sum(s['narrative_words'] for s in stats) + word_count(introduction) + word_count(afterword)
    if not 35000 <= narrative <= 50000:
        raise ValueError(f'Narrative count outside brief: {narrative}')
    manifest = {
        'title': 'The Beer Detective', 'subtitle': 'Uncovering the Myths, Mysteries and Untold Stories of Beer',
        'attribution': 'A World Beer Wiki book project', 'edition': 'Review edition, October 2026',
        'baseline_commit': BASELINE, 'research_cutoff': '2026-10-28', 'chapter_count': 24,
        'part_count': 4, 'narrative_words': narrative,
        'count_definition': 'Introduction, 24 chapter bodies and afterword; headings, note markers, notes, acknowledgments, methodology and bibliography excluded. Unicode word tokens with internal apostrophes/hyphens retained.',
        'chapter_words': sum(s['narrative_words'] for s in stats),
        'introduction_words': word_count(introduction), 'afterword_words': word_count(afterword),
        'notes': sum(s['notes'] for s in stats) + intro_note_count,
        'registered_claims': len(records), 'unique_source_urls': len({s['url'] for r in records for s in r['sources']}),
        'human_review': 'Not performed; awaiting independent editorial, specialist and community review.',
        'master_sha256': hashlib.sha256(manuscript.encode()).hexdigest(), 'chapters': stats,
    }
    (ROOT / 'research/manuscript-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: manifest[k] for k in ['chapter_count', 'narrative_words', 'notes', 'registered_claims', 'unique_source_urls']}, indent=2))


if __name__ == '__main__':
    assemble()
