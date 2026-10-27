"""Regression checks for evidence edges, dates, scope tracking and exports."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile
import unittest

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import atlas


class AtlasTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write('index.md', '# Wiki\n[Culture](culture/index.md)\n')
        self.write('culture/index.md', '# Culture\n[Case](case.md)\n')
        self.subject = {
            'type': 'Cultural Practice', 'title': 'Case', 'status': 'draft',
            'scope': 'A particular account, not a universal claim.',
            'review_note': 'Not independently reviewed.',
            'sources': [{'id': 'study', 'resource': 'https://example.org/study',
                         'title': 'Study', 'access_scope': 'Abstract only'}],
            'relations': [{'relation': 'associated_with', 'target': 'culture/case',
                           'source_ids': ['study'], 'qualifier': 'One observed setting.'}],
        }
        self.write_doc('culture/case.md', self.subject, '# Case\n[Case](case.md)\n')
        self.spec = {
            'type': 'Specification', 'title': 'Scope', 'specification_version': '1.0',
            'review_status': 'not-independently-reviewed',
            'work_items': [{'id': 'ATLAS-001', 'title': 'Case', 'state': 'implemented',
                            'paths': ['culture/case.md']}],
        }
        self.write_doc(atlas.SPEC, self.spec)

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')

    def write_doc(self, name, data, body=''):
        self.write(name, '---\n' + yaml.safe_dump(data, allow_unicode=True, sort_keys=False) + '---\n\n' + body)

    def report(self):
        return atlas.validate(self.root)

    def assert_error(self, text):
        report = self.report()
        self.assertFalse(report['ok'], report)
        self.assertTrue(any(text in error for error in report['errors']), report)

    def test_valid_fixture(self):
        self.assertTrue(self.report()['ok'], self.report())

    def test_duplicate_yaml_key(self):
        self.write('culture/case.md', '---\ntitle: A\ntitle: B\n---\n')
        self.assert_error('duplicate key')

    def test_factual_relation_needs_qualifier(self):
        del self.subject['relations'][0]['qualifier']
        self.write_doc('culture/case.md', self.subject)
        self.assert_error('requires a qualifier')

    def test_factual_relation_needs_local_source(self):
        self.subject['relations'][0]['source_ids'] = ['missing']
        self.write_doc('culture/case.md', self.subject)
        self.assert_error('locally registered sources')

    def test_editorial_comparison_does_not_require_causal_evidence(self):
        for kind in ('compare_with', 'compares'):
            self.subject['relations'] = [{'relation': kind, 'target': 'culture/case'}]
            self.write_doc('culture/case.md', self.subject)
            self.assertTrue(self.report()['ok'])

    def test_unknown_and_malformed_relation_types(self):
        for value in ('descended_from', []):
            with self.subTest(value=value):
                self.subject['relations'][0]['relation'] = value
                self.write_doc('culture/case.md', self.subject)
                self.assert_error('unknown relation type')

    def test_missing_target(self):
        self.subject['relations'][0]['target'] = 'culture/missing'
        self.write_doc('culture/case.md', self.subject)
        self.assert_error('target does not exist')

    def test_unsafe_targets(self):
        for value in ('../secret', '%2e%2e/secret', '/absolute', 'https://example.org/x',
                      'culture/case.md', 'culture/case#fragment', 'culture\\case'):
            with self.subTest(value=value):
                self.subject['relations'][0]['target'] = value
                self.write_doc('culture/case.md', self.subject)
                self.assert_error('invalid relation target')

    def test_unindexed_subject(self):
        self.write_doc('culture/orphan.md', self.subject)
        self.assert_error('unindexed subject')

    def test_missing_section_index(self):
        (self.root / 'culture/index.md').unlink()
        self.assert_error('missing section index')

    def test_source_and_scope_required(self):
        for field in ('scope', 'review_note', 'sources'):
            with self.subTest(field=field):
                data = deepcopy(self.subject)
                del data[field]
                self.write_doc('culture/case.md', data)
                self.assertFalse(self.report()['ok'])

    def test_draft_status_not_promoted(self):
        self.subject['status'] = 'verified'
        self.write_doc('culture/case.md', self.subject)
        self.assert_error('retain draft status')

    def test_symlink_escape(self):
        outside = Path(self.temp.name).parent / (Path(self.temp.name).name + '-outside.md')
        outside.write_text('# Outside', encoding='utf-8')
        self.addCleanup(lambda: outside.unlink(missing_ok=True))
        (self.root / 'culture/escape.md').symlink_to(outside)
        self.assert_error('symlink escapes')

    def calendar(self):
        return {'kind': 'recurring-event', 'system': 'Gregorian', 'timing': 'Edition-specific dates.',
                'source_ids': ['study'], 'months': [9, 10], 'editions': [
                    {'year': 2026, 'start': '2026-09-19', 'end': '2026-10-04',
                     'checked_on': '2026-10-27', 'source_id': 'study',
                     'evidence_status': 'organizer-announced-dates'}]}

    def check_calendar(self, calendar):
        errors = []
        atlas.check_calendar(calendar, {'study'}, errors.append)
        return errors

    def test_past_edition_is_valid_data_not_an_upcoming_claim(self):
        self.assertEqual(self.check_calendar(self.calendar()), [])

    def test_calendar_date_errors(self):
        mutations = [
            {'start': '2026-02-30'}, {'start': '2026-11-01'}, {'year': 2025},
            {'checked_on': '27-10-2026'}, {'source_id': 'missing'}, {'evidence_status': ''},
            {'year': []}, {'source_id': []},
        ]
        for change in mutations:
            with self.subTest(change=change):
                value = self.calendar()
                value['editions'][0].update(change)
                self.assertTrue(self.check_calendar(value))

    def test_months_are_bounded_unique_integers(self):
        for months in ([0], [13], [1, 1], [True], ['5'], [], {'month': 1}):
            with self.subTest(months=months):
                value = self.calendar()
                value['months'] = months
                self.assertTrue(self.check_calendar(value))

    def test_calendar_kind_and_sources(self):
        for field, value in [('kind', 'holiday'), ('kind', []), ('source_ids', []),
                             ('system', ''), ('timing', '')]:
            with self.subTest(field=field, value=value):
                calendar = self.calendar()
                calendar[field] = value
                self.assertTrue(self.check_calendar(calendar))

    def test_historical_event_requires_date(self):
        calendar = self.calendar()
        calendar.update(kind='historical-event', editions=[])
        self.assertTrue(self.check_calendar(calendar))

    def test_duplicate_edition_rejected(self):
        calendar = self.calendar()
        calendar['editions'] *= 2
        self.assertTrue(self.check_calendar(calendar))

    def test_incomplete_work_is_not_implemented(self):
        self.spec['work_items'][0]['paths'] = []
        self.write_doc(atlas.SPEC, self.spec)
        self.assert_error('requires deliverable paths')

    def test_work_state_and_path_errors(self):
        for change in ({'state': 'done'}, {'state': []}, {'paths': ['missing.md']},
                       {'paths': ['../secret']}, {'paths': ['culture/case.md', 'culture/case.md']}):
            with self.subTest(change=change):
                item = {'id': 'ATLAS-001', 'title': 'Case', 'state': 'implemented', 'paths': ['culture/case.md']}
                item.update(change)
                errors = []
                atlas.check_ledger(self.root, [item], errors.append)
                self.assertTrue(errors)

    def test_duplicate_work_id(self):
        self.spec['work_items'] *= 2
        self.write_doc(atlas.SPEC, self.spec)
        self.assert_error('duplicate work id')

    def test_missing_spec(self):
        (self.root / atlas.SPEC).unlink()
        self.assert_error('missing tracked specification')

    def test_export_preserves_limits_and_edge_evidence(self):
        documents, errors = atlas.load_documents(self.root)
        self.assertEqual(errors, [])
        output = atlas.catalog(documents)
        article = output['concepts'][0]
        self.assertEqual(article['scope'], self.subject['scope'])
        self.assertEqual(article['sources'][0]['access_scope'], 'Abstract only')
        edge = output['incoming_relations']['culture/case'][0]
        self.assertEqual(edge['source_ids'], ['study'])
        self.assertEqual(edge['qualifier'], 'One observed setting.')
        self.assertEqual(edge['from'], 'culture/case')

    def test_exports_are_deterministic(self):
        documents, _ = atlas.load_documents(self.root)
        reverse = dict(reversed(list(documents.items())))
        encode = lambda value: json.dumps(value, sort_keys=True, ensure_ascii=False)
        self.assertEqual(encode(atlas.catalog(documents)), encode(atlas.catalog(reverse)))
        output = atlas.progress(documents)
        self.assertEqual(output['counts']['implemented'], 1)
        self.assertIn('finite work ledger', output['interpretation'])
        self.assertNotIn('percent_complete', output)


if __name__ == '__main__':
    unittest.main()


class TimelineExportTests(unittest.TestCase):
    """Timeline must preserve evidence and must never invent future event editions."""

    def sample(self):
        return {'calendar/event.md': {'data': {
            'type': 'Recurring Festival Reference', 'title': 'Documented example',
            'regions': ['A particular town'], 'status': 'draft',
            'review_note': 'Not externally reviewed.',
            'calendar': {'kind': 'recurring-event', 'system': 'local agricultural',
                         'timing': 'Occasion in spring, year varies', 'months': [3],
                         'source_ids': ['record'],
                         'editions': [{'year': 2025, 'start': '2025-03-01', 'end': '2025-03-02',
                                       'checked_on': '2026-10-27', 'source_id': 'record',
                                       'evidence_status': 'archival-edition'}]},
            'sources': [{'id': 'record', 'title': 'Example source',
                         'resource': 'https://example.org/record',
                         'access_scope': 'Published summary'}]}, 'body': '# Example'},
                'history/undated.md': {'data': {'title': 'Not an event'}, 'body': ''}}

    def test_timeline_keeps_evidence_and_exact_dates(self):
        output = atlas.timeline(self.sample())
        self.assertEqual(len(output['events']), 1)
        self.assertEqual(len(output['editions']), 1)
        self.assertEqual(output['events'][0]['source_details'][0]['access_scope'], 'Published summary')
        self.assertEqual(output['events'][0]['system'], 'local agricultural')
        self.assertEqual(output['editions'][0]['start'], '2025-03-01')
        self.assertNotIn('2027', json.dumps(output))

    def test_timeline_empty_editions_are_not_projected(self):
        data = self.sample()
        data['calendar/event.md']['data']['calendar']['editions'] = []
        self.assertEqual(atlas.timeline(data)['editions'], [])

    def test_timeline_deterministic_under_key_reordering(self):
        original = self.sample()
        original['calendar/event-2.md'] = deepcopy(original['calendar/event.md'])
        original['calendar/event-2.md']['data']['title'] = 'Other documented event'
        reversed_docs = dict(reversed(list(original.items())))
        self.assertEqual(json.dumps(atlas.timeline(original),sort_keys=True),
                         json.dumps(atlas.timeline(reversed_docs),sort_keys=True))

    def test_no_calendar_history_is_not_a_calendar_event(self):
        out=atlas.timeline({'history/undated.md':{'data':{'title':'Historical research'},'body':''}})
        self.assertEqual(out['events'], [])
        self.assertEqual(out['editions'], [])
