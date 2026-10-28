#!/usr/bin/env python3
"""Offline *editorial hygiene* checks for one research edition, not fact checking.

Check citation use, explicit source access, scope and useful reading paths on
new edition pages, and evidence in the edition's existing-page extensions.
Does not fetch URLs or certify historical, scientific or community accuracy.
"""
from __future__ import annotations
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys
import yaml

from atlas import SUBJECT_DIRS, FRONT, nonempty, load_documents

EDITION='1.6'
SOURCE_PREFIX='v16-'
STAMP='world-beer-wiki/1.6'
EXTENSION='## Edition 1.6: sourced research connections'
WORD_RE=re.compile(r"\b[\w-]+\b",re.UNICODE)

def check_article(name, data, body, new, edition=EDITION):
    """Return errors; intended for simple negative regression fixtures too."""
    errors=[]
    source_prefix='v'+edition.replace('.','')+'-'
    extension='## Edition '+edition+': '+('sourced research connections' if edition=='1.6' else 'newly sourced connections')
    check_date='2026-10-28'
    if not new and extension not in body: return errors
    if new:
        if not nonempty(data.get('scope')): errors.append('missing scoped description')
        if not nonempty(data.get('review_note')): errors.append('missing independent-review status')
        if data.get('status')!='draft': errors.append('research item is not a draft')
        if str(data.get('source_checked_on',''))!=check_date: errors.append('edition source_checked_on not current')
        main_body=re.split(r'(?m)^## (?:Explore connected subjects|Related reading|Evidence and uncertainty|Source notes)\s*$',body,maxsplit=1)[0]
        if len(WORD_RE.findall(main_body))<150: errors.append('insufficient substantive explanatory text (<150 words)')
        # Includes manual contextual cross-links, not just the source bibliography.
        if len(re.findall(r'\]\((?!https?://)[^)]+\.md(?:#[^)]*)?\)',body))<2:
            errors.append('fewer than two internal reading links')
    sources=data.get('sources',[])
    if not isinstance(sources,list):return errors+['sources not a list']
    selected=[s for s in sources if isinstance(s,dict) and str(s.get('id','')).startswith(source_prefix)]
    if not selected:errors.append('missing edition source record')
    if not new:
        body=body.split(extension,1)[-1] # Only audit the newly supplied evidence.
    cited_body=re.sub(r'(?m)^\[\^[^\]]+\]:.*$', '', body.split('## Source notes',1)[0])
    for source in selected:
        key=source.get('id','')
        for field in ('resource','title','author_label','source_kind','access_scope'):
            if not nonempty(source.get(field)):
                errors.append(f'{key}: missing source {field}')
        if not re.search(r'\[\^'+re.escape(key)+r'\]',cited_body):
            errors.append(f'{key}: citation missing from explanatory body')
        if not re.search(r'^\[\^'+re.escape(key)+r'\]:',body,re.M):
            errors.append(f'{key}: missing source footnote')
    return errors

def validate(root, edition=EDITION):
    if edition not in {'1.6','1.7','1.8','1.9'}: raise ValueError('supported research editions: 1.6, 1.7, 1.8, 1.9')
    source_prefix='v'+edition.replace('.','')+'-'
    stamp='world-beer-wiki/'+edition
    extension='## Edition '+edition+': '+('sourced research connections' if edition=='1.6' else 'newly sourced connections')
    documents,load_errors=load_documents(Path(root))
    errors=list(load_errors)
    counts=Counter(new_subjects=0,revised_subjects=0,source_usages=0)
    kinds=Counter()
    for name,doc in sorted(documents.items()):
        if name.split('/')[0] not in SUBJECT_DIRS or name.endswith('/index.md'):continue
        data=doc['data']; body=doc['body']
        new=data.get('generated',{}).get('by')==stamp
        revised=not new and extension in body
        if new or revised:
            counts['new_subjects' if new else 'revised_subjects']+=1
            selected=[x for x in data.get('sources',[]) if isinstance(x,dict) and str(x.get('id','')).startswith(source_prefix)]
            counts['source_usages']+=len(selected)
            for s in selected:kinds[s.get('source_kind','unclassified')]+=1
            for message in check_article(name,data,body,new,edition):errors.append(f'{name}: {message}')
    counts['distinct_source_records']=len({s['id'] for d in documents.values() for s in d['data'].get('sources',[]) if isinstance(s,dict) and str(s.get('id','')).startswith(source_prefix)})
    return {'ok':not errors,'edition':edition,'interpretation':'Checks local evidence metadata and structural editorial hygiene, NOT source accuracy, external URL health, ethnographic consent or expert review.',
            'counts':dict(sorted(counts.items())),'source_kinds':dict(sorted(kinds.items())),'errors':sorted(set(errors))}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('root',nargs='?',type=Path,default=Path(__file__).resolve().parents[1])
    p.add_argument('--json',action='store_true')
    p.add_argument('--edition',choices=['1.6','1.7','1.8','1.9'],default='1.6',help='research release to audit; older reports remain checkable')
    a=p.parse_args()
    report=validate(a.root,edition=a.edition)
    if a.json:print(json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True))
    else:
        print('PASS' if report['ok'] else 'FAIL',report['counts'])
        for err in report['errors']:print('ERROR',err)
    return 0 if report['ok'] else 1
if __name__=='__main__':sys.exit(main())
