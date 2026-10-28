#!/usr/bin/env python3
"""Rebuild/check scoped titles and explicit aliases across all atlas article sections.

No fuzzy matching, hidden genealogy, invented synonyms or external dependencies
beyond PyYAML. Names refer to the canonical page that supplied them.
"""
import argparse
from pathlib import Path
import sys
from atlas import SUBJECT_DIRS, load_documents

HEADER = '''---
type: Navigation Guide
title: All names and scoped aliases
description: Every canonical subject title and explicitly declared alias across the atlas.
tags: [wiki-documentation, navigation, aliases]
status: draft
generated:
  by: world-beer-wiki/1.15
  at: '2026-10-28T12:00:00Z'
sources:
- id: atlas-spec
  resource: /editorial/atlas-specification.md
  title: World Beer Atlas expansion specification
---

# Names and scoped aliases

This alphabetical directory covers **all 13 reference sections**. An alias is recorded
only when a canonical article explicitly declares it. Neither a shared spelling nor
translation proves that two regional traditions are interchangeable. To compare
similar names, open their linked articles and examine the `scope` and evidence notes.

| Name | Canonical subject | Kind | Name role |
|---|---|---|---|
'''


def escape(text):
    return str(text).replace('\\','\\\\').replace('|','\\|').replace('\n',' ').strip()


def render(root):
    root = Path(root)
    docs, errors = load_documents(root)
    if errors: raise ValueError(errors[:5])
    rows=[]
    for path, doc in docs.items():
        if path.split('/')[0] not in SUBJECT_DIRS or Path(path).name=='index.md':continue
        meta=doc['data'];title=meta.get('title');kind=meta.get('type')
        if not isinstance(title,str) or not title.strip() or not isinstance(kind,str) or not kind.strip():
            raise ValueError(f'{path}: missing subject name or kind')
        names=[(title,'canonical title')]
        aliases=meta.get('aliases',[])
        if aliases is None:aliases=[]
        if not isinstance(aliases,list) or any(not isinstance(a,str) or not a.strip() for a in aliases):
            raise ValueError(f'{path}: aliases must be nonempty strings')
        names += [(name,'article-scoped alias') for name in aliases]
        seen=set()
        for name,role in names:
            key=name.casefold().strip()
            if key in seen:continue
            seen.add(key)
            rows.append((name.casefold(),path,role, f'| {escape(name)} | [{escape(title)}](../{path}) | {escape(kind)} | {role} |'))
    rows.sort(key=lambda x:(x[0],x[1],x[2]))
    return HEADER + '\n'.join(row[-1] for row in rows) + f'\n\n**{len(rows)} name records** across {len(SUBJECT_DIRS)} reference sections. [All atlas subjects](all-atlas-subjects.md) · [Research method](../editorial/methodology.md).\n'


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();target=args.root/'navigation/all-names.md';new=render(args.root)
    if args.check:
        if not target.is_file() or target.read_text(encoding='utf8')!=new:
            print('FAIL: stale scoped-name directory',file=sys.stderr);return 1
        print('PASS: scoped-name directory current');return 0
    target.write_text(new,encoding='utf8');print('Generated',target);return 0

if __name__=='__main__':sys.exit(main())
