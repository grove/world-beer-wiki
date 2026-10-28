#!/usr/bin/env python3
"""Offline atlas checks and deterministic catalog/progress exports.

Uses the wiki's existing YAML/Markdown helpers. No network access or database.
Run the base validator too; this module adds atlas-specific semantic checks.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import date
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml

from validate_wiki import UniqueLoader, is_wiki_path, links, without_fences

SUBJECT_DIRS = (
    'styles', 'ingredients', 'categories', 'culture', 'calendar',
    'microbiology', 'processes', 'objects', 'stories', 'sensory', 'history',
    'environment', 'food',
)
NEW_DIRS = SUBJECT_DIRS[3:]
RELATIONS = {
    'compare_with', 'compares', 'uses_ingredient', 'uses_process', 'associated_with',
    'observed_organism', 'uses_object',
}
RELATION_TARGET_SECTIONS = {
    'uses_ingredient': 'ingredients', 'uses_process': 'processes',
    'observed_organism': 'microbiology', 'uses_object': 'objects',
}

STATES = {'planned', 'partial', 'implemented', 'deferred'}
SPEC = 'editorial/atlas-specification.md'
FRONT = re.compile(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', re.S)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def local_path(root, name, canonical=False):
    """Return a safe repository path or raise ValueError (never accept a URL)."""
    if not nonempty(name):
        raise ValueError('path must be a nonempty string')
    parsed = urlsplit(name)
    if parsed.scheme or parsed.netloc or parsed.query or parsed.fragment or '\\' in name:
        raise ValueError('expected a repository-relative path without URL/query/fragment')
    decoded = unquote(parsed.path)
    if decoded.startswith('/') or '..' in Path(decoded).parts:
        raise ValueError('path must be relative and must not traverse parents')
    candidate = root / decoded
    if canonical:
        if candidate.suffix:
            raise ValueError('canonical targets must omit the file extension')
        candidate = candidate.with_suffix('.md')
    candidate = candidate.resolve()
    if not candidate.is_relative_to(root.resolve()):
        raise ValueError('path escapes repository')
    return candidate


def load_documents(root):
    documents, errors = {}, []
    for path in sorted(root.rglob('*.md')):
        relative = path.relative_to(root)
        if not is_wiki_path(relative):
            continue
        name = relative.as_posix()
        try:
            if not path.resolve().is_relative_to(root.resolve()):
                raise ValueError('document symlink escapes repository')
            text = path.read_text(encoding='utf-8-sig')
            front = FRONT.match(text)
            data = yaml.load(front[1], Loader=UniqueLoader) if front else {}
            if not isinstance(data, dict):
                raise ValueError('frontmatter must be a mapping')
            documents[name] = {'data': data, 'body': text[front.end():] if front else text}
        except (OSError, UnicodeError, yaml.YAMLError, ValueError, TypeError) as exc:
            errors.append(f'{name}: {exc}')
    return documents, errors


def list_of_strings(value, nonempty_list=False):
    return (isinstance(value, list) and (not nonempty_list or bool(value))
            and all(nonempty(item) for item in value))


def source_ids(data):
    values = data.get('sources', [])
    if not isinstance(values, list):
        return set()
    return {item['id'] for item in values if isinstance(item, dict) and nonempty(item.get('id'))}


def parse_day(value):
    if not isinstance(value, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
        raise ValueError('use a quoted YYYY-MM-DD string')
    return date.fromisoformat(value)


def check_calendar(calendar, ids, error):
    if not isinstance(calendar, dict):
        error('calendar must be a mapping')
        return
    kind = calendar.get('kind')
    if not isinstance(kind, str) or kind not in {'seasonal', 'recurring-event', 'historical-event'}:
        error('invalid calendar.kind')
    for field in ('system', 'timing'):
        if not nonempty(calendar.get(field)):
            error(f'calendar.{field} must be nonempty')
    references = calendar.get('source_ids')
    if not list_of_strings(references, True) or not set(references).issubset(ids):
        error('calendar.source_ids must name locally registered sources')
    if 'months' in calendar:
        months = calendar['months']
        if (not isinstance(months, list) or not months
                or any(type(month) is not int or not 1 <= month <= 12 for month in months)
                or len(set(map(str, months))) != len(months)):
            error('calendar.months must be unique integers from 1 through 12')
    editions = calendar.get('editions', [])
    if not isinstance(editions, list):
        error('calendar.editions must be a list')
        return
    if kind == 'historical-event' and not editions:
        error('historical-event requires a dated edition record')
    seen = set()
    for edition in editions:
        if not isinstance(edition, dict):
            error('calendar edition must be a mapping')
            continue
        year = edition.get('year')
        if type(year) is not int or not 1 <= year <= 9999:
            error('calendar edition year must be an integer from 1 through 9999')
        try:
            if year in seen:
                error('duplicate calendar edition year')
            seen.add(year)
        except TypeError:
            error('calendar edition year must be scalar')
        if not nonempty(edition.get('source_id')) or edition.get('source_id') not in ids:
            error('calendar edition source_id is not registered locally')
        if not nonempty(edition.get('evidence_status')):
            error('calendar edition needs evidence_status, not an inferred current status')
        try:
            start, end, checked = (parse_day(edition.get(field)) for field in ('start', 'end', 'checked_on'))
            if start > end:
                error('calendar edition start is after end')
            if start.year != year:
                error('calendar edition year must match start year')
        except (ValueError, TypeError) as exc:
            error(f'invalid calendar edition date: {exc}')


def check_ledger(root, items, error):
    if not isinstance(items, list) or not items:
        error('work_items must be a nonempty list')
        return
    seen = set()
    for item in items:
        if not isinstance(item, dict):
            error('work item must be a mapping')
            continue
        ident = item.get('id')
        if not nonempty(ident) or not re.fullmatch(r'ATLAS-\d{3}', ident):
            error('work item needs an ATLAS-NNN id')
        elif ident in seen:
            error(f'duplicate work id {ident}')
        else:
            seen.add(ident)
        if not nonempty(item.get('title')):
            error(f'{ident}: missing work title')
        state = item.get('state')
        if not isinstance(state, str) or state not in STATES:
            error(f'{ident}: unknown work state')
        paths = item.get('paths')
        if not list_of_strings(paths):
            error(f'{ident}: paths must be a list of nonempty strings')
            continue
        if isinstance(state, str) and state in {'implemented', 'partial'} and not paths:
            error(f'{ident}: {state} work requires deliverable paths')
        if len(set(paths)) != len(paths):
            error(f'{ident}: duplicate deliverable path')
        for name in paths:
            try:
                candidate = local_path(root, name)
                if not candidate.is_file():
                    raise ValueError('deliverable is not an existing file')
            except (ValueError, OSError) as exc:
                error(f'{ident}: {name}: {exc}')


def validate(root, documents=None):
    root = Path(root).resolve()
    if documents is None:
        documents, errors = load_documents(root)
    else:
        errors = []
    counts = Counter(subject_articles=0, evidence_bearing_relations=0, calendar_records=0)
    for directory in SUBJECT_DIRS:
        members = {name for name in documents if name.startswith(directory + '/')
                   and Path(name).name not in {'index.md', 'log.md'}}
        counts[directory] = len(members)
        if not members:
            continue
        index = f'{directory}/index.md'
        if index not in documents:
            errors.append(f'{index}: missing section index')
            continue
        linked = set()
        for destination, _ in links(without_fences(documents[index]['body'])):
            try:
                parsed = urlsplit(destination)
                if parsed.scheme or parsed.netloc:
                    continue
                candidate = (root / directory / unquote(parsed.path)).resolve()
                if candidate.is_relative_to(root):
                    linked.add(candidate.relative_to(root).as_posix())
            except ValueError:
                pass
        for name in sorted(members - linked):
            errors.append(f'{index}: unindexed subject {name}')
        counts['subject_articles'] += len(members)
    for name, document in documents.items():
        data = document['data']
        error = lambda message, name=name: errors.append(f'{name}: {message}')
        ids = source_ids(data)
        section = name.split('/')[0]
        if section in NEW_DIRS and Path(name).name != 'index.md':
            for field in ('scope', 'review_note'):
                if not nonempty(data.get(field)):
                    error(f'new subject needs {field}')
            if data.get('status') != 'draft':
                error('atlas research articles must retain draft status in this release')
            if not ids:
                error('new subject must register sources')
        relations = data.get('relations', [])
        if not isinstance(relations, list):
            error('relations must be a list')
            continue
        for relation in relations:
            if not isinstance(relation, dict):
                error('relation must be a mapping')
                continue
            kind = relation.get('relation')
            if not isinstance(kind, str) or kind not in RELATIONS:
                error(f'unknown relation type {kind!r}')
            expected = RELATION_TARGET_SECTIONS.get(kind) if isinstance(kind, str) else None
            if expected and isinstance(relation.get('target'), str) and not relation['target'].startswith(expected + '/'):
                error(f'{kind} must target {expected}/, not {relation["target"]}')
            try:
                target = local_path(root, relation.get('target'), canonical=True)
                if not target.is_file():
                    error('relation target does not exist')
            except (ValueError, OSError) as exc:
                error(f'invalid relation target: {exc}')
            if kind not in ('compare_with', 'compares'):
                counts['evidence_bearing_relations'] += 1
                refs = relation.get('source_ids')
                if not list_of_strings(refs, True) or not set(refs).issubset(ids):
                    error('factual relation source_ids must name locally registered sources')
                if not nonempty(relation.get('qualifier')):
                    error('factual relation requires a qualifier')
        if 'calendar' in data:
            counts['calendar_records'] += 1
            check_calendar(data['calendar'], ids, error)
        elif section == 'calendar' and Path(name).name != 'index.md':
            error('calendar article requires calendar metadata')
    spec = documents.get(SPEC)
    if spec is None:
        errors.append(f'{SPEC}: missing tracked specification')
    else:
        items = spec['data'].get('work_items')
        check_ledger(root, items, lambda message: errors.append(f'{SPEC}: {message}'))
        if isinstance(items, list):
            counts['work_items'] = len(items)
    return {'ok': not errors, 'counts': dict(sorted(counts.items())), 'errors': sorted(set(errors))}


def catalog(documents):
    concepts, incoming = [], defaultdict(list)
    for name, document in sorted(documents.items()):
        if name.split('/')[0] not in SUBJECT_DIRS or Path(name).name == 'index.md':
            continue
        data = document['data']
        ident = name[:-3]
        item = {'id': ident, 'path': name}
        for field in ('type', 'title', 'description', 'aliases', 'tags', 'regions', 'scope',
                      'status', 'review_note', 'source_checked_on', 'calendar', 'sources', 'relations'):
            if field in data:
                item[field] = data[field]
        concepts.append(item)
        for relation in data.get('relations', []):
            if isinstance(relation, dict) and nonempty(relation.get('target')):
                incoming[relation['target']].append({'from': ident, **relation})
    return {'schema_version': '1.0', 'evidence_policy': 'Preserve scope, source access limits and relation qualifiers; comparisons do not assert descent.',
            'concepts': concepts, 'incoming_relations': dict(sorted(incoming.items()))}


def progress(documents):
    data = documents[SPEC]['data']
    items = data['work_items']
    counts = Counter(item['state'] for item in items)
    return {'specification': SPEC, 'specification_version': data.get('specification_version'),
            'implementation_status': data.get('implementation_status'),
            'review_status': data.get('review_status'),
            'interpretation': 'Counts concern this finite work ledger; implemented does not mean independently verified or globally complete.',
            'counts': {state: counts[state] for state in sorted(STATES)}, 'work_items': items}


def timeline(documents):
    """Offline, evidence-scoped timeline: never infer future event instances.

    Preserves local systems and timing strings, and exact historical editions only
    when an article explicitly registered them. Historical articles without a
    calendar block remain research narratives rather than invented event dates.
    """
    events, editions = [], []
    for path, document in sorted(documents.items()):
        cal = document['data'].get('calendar')
        if not isinstance(cal, dict):
            continue
        meta = document['data']
        record = {
            'id': path[:-3], 'title': meta.get('title'), 'type': meta.get('type'),
            'regions': meta.get('regions', []), 'status': meta.get('status'),
            'review_note': meta.get('review_note', ''),
            'kind': cal.get('kind'), 'system': cal.get('system'),
            'timing': cal.get('timing'), 'months': cal.get('months', []),
            'source_ids': cal.get('source_ids', []),
            'source_details': [dict(id=s.get('id'), title=s.get('title'),
                                    resource=s.get('resource'),
                                    access_scope=s.get('access_scope'))
                               for s in meta.get('sources', [])
                               if isinstance(s, dict) and s.get('id') in cal.get('source_ids', [])],
        }
        events.append(record)
        for edition in cal.get('editions', []):
            editions.append({'event': path[:-3], 'title': meta.get('title'),
                             'system': cal.get('system'), **edition})
    return {'schema_version': '1.0',
            'interpretation': 'Documented seasonal and event metadata only. Not a live calendar; do not infer future dates, participation or current status.',
            'events': events, 'editions': sorted(editions, key=lambda x:(x['start'],x['event']))}


def source_audit(documents):
    """Deterministic, offline index of citation provenance; no quality certification."""
    records = {}
    occurrence_counts = Counter()
    checked = 0
    limited = []
    for path, document in sorted(documents.items()):
        if path.split('/')[0] not in SUBJECT_DIRS or path.endswith('/index.md'):
            continue
        data = document['data']
        for source in data.get('sources', []):
            if not isinstance(source, dict) or not source.get('id'):
                continue
            key = str(source['id'])
            occurrence_counts[key] += 1
            if not source.get('access_scope'):
                limited.append({'page': path, 'id': key, 'problem': 'no explicit access_scope'})
            if key not in records:
                records[key] = {
                    'id': key, 'resource': source.get('resource'),
                    'title': source.get('title'), 'source_kind': source.get('source_kind'),
                    'access_scope': source.get('access_scope'), 'pages': [],
                }
            records[key]['pages'].append(path)
            checked += 1
    kinds = Counter(str(item.get('source_kind') or 'unclassified') for item in records.values())
    return {'schema_version': '1.0',
            'interpretation': 'Counts are catalog metadata and source reuse, not distinct publications or independent fact checking.',
            'source_records': len(records), 'source_citation_occurrences': checked,
            'source_kinds': dict(sorted(kinds.items())),
            'missing_access_scopes': sorted(limited,key=lambda x:(x['page'],x['id'])),
            'sources': [records[key] for key in sorted(records)]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['check', 'catalog', 'progress', 'timeline', 'source-audit'])
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--json', action='store_true', help='JSON check report; exports are always JSON')
    args = parser.parse_args(argv)
    if not args.root.is_dir():
        parser.error(f'not a directory: {args.root}')
    documents, parse_errors = load_documents(args.root.resolve())
    report = validate(args.root, documents)
    report['errors'] = sorted(set(report['errors'] + parse_errors))
    report['ok'] = not report['errors']
    if args.command == 'check':
        if args.json:
            print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))
        else:
            print('PASS' if report['ok'] else 'FAIL')
            for key, value in report['counts'].items():
                print(f'{key}: {value}')
            for error in report['errors']:
                print(f'ERROR: {error}')
        return 0 if report['ok'] else 1
    if not report['ok']:
        print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2), file=sys.stderr)
        return 1
    payload = {'catalog': lambda: catalog(documents), 'progress': lambda: progress(documents), 'timeline': lambda: timeline(documents), 'source-audit': lambda: source_audit(documents)}[args.command]()
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2, default=str))
    return 0


if __name__ == '__main__':
    sys.exit(main())
