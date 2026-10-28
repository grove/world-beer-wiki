"""Edition 1.9 evidence hygiene and cross-edition regression tests.

No offline check can establish historical accuracy or a community endorsement.
"""
from pathlib import Path
import sys
import unittest
from copy import deepcopy

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from research_quality import check_article, validate

ROOT = Path(__file__).resolve().parents[1]
SRC = {'id': 'v19-case-study', 'resource': 'https://example.org/source',
       'title': 'A bounded, named field observation', 'author_label': 'Research authors',
       'source_kind': 'primary-study',
       'access_scope': 'Indexed abstract only. The full study has not been read.'}
DATA = {'type': 'Cultural case', 'title': 'One documented case',
        'scope': 'The selected case, date and sample; not a worldwide generalization',
        'status': 'draft', 'review_note': 'No independent human or community review',
        'source_checked_on': '2026-10-28', 'sources': [SRC]}
BODY = ('The study names a selected context and distinguishes the sampled community from other makers. '
        'Its measurements describe the observed material and do not imply safety or clinical benefits. ' * 18
        + '\n\nRead [Cultural context](../culture/index.md) and '
        '[Brewing processes](../processes/index.md) for boundaries. [^v19-case-study]\n\n'
        '## Source notes\n\n[^v19-case-study]: Access-limited summary.\n')

class Research19Tests(unittest.TestCase):
    def audit(self, data=None, body=None, new=True):
        return check_article('culture/one-case.md', data if data is not None else DATA,
                             body if body is not None else BODY, new, edition='1.9')

    def test_valid_case(self):
        self.assertEqual([], self.audit())

    def test_unreferenced_source_rejected(self):
        changed = BODY.replace(' [^v19-case-study]\n\n## Source notes', '\n\n## Source notes')
        self.assertTrue(any('citation missing' in x for x in self.audit(body=changed)))

    def test_missing_source_access_rejected(self):
        changed = deepcopy(DATA); changed['sources'][0]['access_scope'] = ''
        self.assertTrue(any('access_scope' in x for x in self.audit(data=changed)))

    def test_missing_attribution_rejected(self):
        changed = deepcopy(DATA); changed['sources'][0]['author_label'] = ''
        self.assertTrue(any('author_label' in x for x in self.audit(data=changed)))

    def test_unsupported_review_upgrade_rejected(self):
        changed = deepcopy(DATA); changed['status'] = 'reviewed'
        self.assertTrue(any('draft' in x for x in self.audit(data=changed)))

    def test_no_scope_rejected(self):
        changed = deepcopy(DATA); changed['scope'] = ''
        self.assertTrue(any('scoped' in x for x in self.audit(data=changed)))

    def test_not_enough_explanation_rejected(self):
        changed = 'Brief description. [Culture](../culture/index.md) [Process](../processes/index.md) [^v19-case-study]\n## Source notes\n[^v19-case-study]: Note.'
        self.assertTrue(any('insufficient substantive' in x for x in self.audit(body=changed)))

    def test_missing_reading_links_rejected(self):
        changed = BODY.replace('[Cultural context](../culture/index.md) and '
                               '[Brewing processes](../processes/index.md)',
                               'Cultural context and brewing processes')
        self.assertTrue(any('fewer than two' in x for x in self.audit(body=changed)))

    def test_revision_requires_citation_in_new_section(self):
        updated = 'Old article body with unrelated footnotes.\n\n## Edition 1.9: newly sourced connections\n\n' + BODY
        self.assertEqual([], self.audit(body=updated, new=False))
        altered = updated.replace(' [^v19-case-study]\n\n## Source notes', '\n\n## Source notes')
        self.assertTrue(any('citation missing' in x for x in self.audit(body=altered, new=False)))

    def test_edition_19_exact_scope(self):
        report = validate(ROOT, edition='1.9')
        self.assertTrue(report['ok'], report['errors'][:10])
        self.assertEqual((31, 18, 18, 79), tuple(report['counts'][key] for key in
                         ('new_subjects', 'revised_subjects', 'distinct_source_records', 'source_usages')))

    def test_earlier_edition_reports_still_pass(self):
        for edition, expected in [('1.6', (30,22)), ('1.7', (26,16)), ('1.8', (29,14))]:
            with self.subTest(edition=edition):
                report = validate(ROOT, edition=edition)
                self.assertTrue(report['ok'], report['errors'][:6])
                self.assertEqual(expected, (report['counts']['new_subjects'], report['counts']['revised_subjects']))

    def test_release_trails_and_source_review_queue_exist(self):
        for rel in ('editorial/source-review-queue-1-9.md',
                    'references/atlas-sources-1-9.md',
                    'navigation/edition-1-9-reading-trails.md'):
            with self.subTest(rel=rel):
                self.assertTrue((ROOT / rel).is_file())

if __name__ == '__main__':
    unittest.main()
