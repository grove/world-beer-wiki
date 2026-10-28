#!/usr/bin/env python3
"""Generate/check one searchable Markdown directory spanning every atlas subject.

All links are relative and derived from canonical articles and their frontmatter.
No network calls; deterministic output makes PR review practical.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

from atlas import SUBJECT_DIRS, load_documents

HEADER = '''---
type: Navigation Guide
title: Complete World Beer Atlas subject index
description: Automatically maintained index of all named subject articles in every atlas section.
tags: [wiki-navigation, subjects]
status: draft
generated:
  by: world-beer-wiki/1.12
  at: '2026-10-28T08:00:00Z'
sources:
- id: atlas-spec
  resource: /editorial/atlas-specification.md
  title: World Beer Atlas expansion specification
---

# Complete World Beer Atlas subject index

This is a **generated directory**, not a count of standardized beer styles. It includes named
beer/tradition profiles, ingredients, cultural cases, events, microbes, processes and research
guides. The `type` and article `scope` explain what any one row represents. For cross-links and
actual research conclusions open the article, rather than inferring a connection from proximity
in this list.

Regenerate/check with `python tools/build_subject_index.py` or `--check`.
'''


def esc(value):
    return str(value).replace('|', '\\|').replace('\n', ' ').strip()


def render(root):
    root = Path(root).resolve()
    docs, errs = load_documents(root)
    if errs:
        raise ValueError(f'invalid source documents: {errs[:5]}')
    lines = [HEADER]
    total = 0
    for dirname in SUBJECT_DIRS:
        records = []
        for path, obj in docs.items():
            if not path.startswith(dirname + '/') or Path(path).name in ('index.md', 'log.md'):
                continue
            data = obj['data']
            title = data.get('title')
            kind = data.get('type')
            if not isinstance(title, str) or not title.strip() or not isinstance(kind, str) or not kind.strip():
                raise ValueError(f'{path}: missing title/type')
            regions = data.get('regions') or []
            if not isinstance(regions,list):
                regions = [str(regions)]
            # Some frontmatter contains multiline or unusual geographical scope; keep it compact.
            region = ', '.join(map(str, regions[:2])) if regions else '—'
            records.append((title.casefold(),path, title, kind,region))
        records.sort()
        total += len(records)
        lines += [f'\n## {dirname.replace("-", " ").title()} ({len(records)})\n',
                  '\n| Subject | Kind | Region / scope hint |\n|---|---|---|']
        for _,path,title,kind,region in records:
            lines.append(f'| [{esc(title)}](../{path}) | {esc(kind)} | {esc(region)} |')
    lines.insert(1, f'\n**{total} canonical subject articles · {len(SUBJECT_DIRS)} reference sections · research edition 1.12.**\n')
    return '\n'.join(lines).rstrip()+'\n'


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--check',action='store_true',help='report stale directory without rewriting it')
    args=parser.parse_args()
    target=args.root/'navigation/all-atlas-subjects.md'
    new=render(args.root)
    if args.check:
        if not target.exists() or target.read_text(encoding='utf-8')!=new:
            print('FAIL: navigation/all-atlas-subjects.md is missing or stale',file=sys.stderr)
            return 1
        print('PASS: complete subject index is up-to-date')
        return 0
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(new,encoding='utf-8')
    print(f'Generated {target.relative_to(args.root)}')
    return 0

if __name__=='__main__':sys.exit(main())
