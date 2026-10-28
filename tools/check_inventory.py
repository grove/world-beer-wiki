#!/usr/bin/env python3
"""Check current homepage/README counts against canonical article metadata, offline.

Checks only the current inventory tables and current total, never historical release
statistics. This does not imply complete coverage or external source verification.
"""
from pathlib import Path
import argparse,json,re,sys
from atlas import SUBJECT_DIRS,load_documents

def validate(root):
    root=Path(root)
    docs, errors=load_documents(root)
    counts={section:sum(p.startswith(section+'/') and p!=section+'/index.md' for p in docs) for section in SUBJECT_DIRS}
    total=sum(counts.values())
    for fname in ('index.md','README.md'):
        text=(root/fname).read_text(encoding='utf-8')
        for section,n in counts.items():
            # Only the current primary inventory table row, not historic sections.
            matches=re.findall(r'(?m)^\| \[[^\n|]+\]\('+re.escape(section)+r'/index\.md\) \| ([0-9]+)\b',text)
            if len(matches)!=1 or int(matches[0])!=n:
                errors.append(f'{fname}: current {section} inventory mismatch ({matches} vs {n})')
        if fname=='README.md':
            match=re.search(r'That is \*\*([0-9]+) subject articles\*\*',text)
        else:
            match=re.search(r'Research edition 1\.12[^\n]*?([0-9]+) subject articles',text)
        if not match or int(match[1])!=total:
            errors.append(f'{fname}: current total differs from {total}')
        if fname=='index.md':
            match=re.search(r'\| \[Complete atlas subject index\]\(navigation/all-atlas-subjects\.md\) \| All ([0-9]+) entries',text)
            if not match or int(match[1])!=total:
                errors.append(f'{fname}: complete index count differs from {total}')
    return {'ok':not errors,'subject_articles':total,'sections':counts,'errors':errors}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('root',nargs='?',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--json',action='store_true')
    a=ap.parse_args();report=validate(a.root)
    print(json.dumps(report,indent=2,sort_keys=True) if a.json else ('PASS' if report['ok'] else '\n'.join(report['errors'])))
    return 0 if report['ok'] else 1
if __name__=='__main__':sys.exit(main())
