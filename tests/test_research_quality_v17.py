"""Regression cases for new research metadata while preserving the edition 1.6 audit."""
import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from research_quality import check_article, validate

SRC={'id':'v17-example', 'resource':'https://example.org/study', 'title':'A named source',
     'author_label':'Research author', 'source_kind':'primary-study-abstract',
     'access_scope':'Publisher abstract only, not full experiment'}
DATA={'type':'Research Example', 'title':'Example', 'scope':'One bounded experiment', 'status':'draft',
      'review_note':'AI draft, not reviewed', 'source_checked_on':'2026-10-28', 'sources':[SRC]}
BODY=('A bounded experiment, its sample and its limitations are described carefully. '*32 +
      '\n\n[Beer](../styles/pito.md) [Process](../processes/starch-conversion.md) '
      '[^v17-example]\n\n## Source notes\n\n[^v17-example]: Publisher abstract.\n')
class Research17Tests(unittest.TestCase):
    def errors(self,data=None,body=None,new=True):
        return check_article('culture/example.md',data or DATA,body if body is not None else BODY,new,edition='1.7')
    def test_fixture_passes(self):
        self.assertEqual(self.errors(),[])
    def test_uncited_source_fails_even_if_definition_exists(self):
        bad=BODY.split('## Source notes')[0].replace('[^v17-example]','') + '## Source notes' + BODY.split('## Source notes',1)[1]
        self.assertTrue(any('explanatory body' in e for e in self.errors(body=bad)))
    def test_source_access_is_not_optional(self):
        data=copy.deepcopy(DATA);data['sources'][0]['access_scope']=''
        self.assertTrue(any('access_scope' in e for e in self.errors(data=data)))
    def test_no_fabricated_review_status(self):
        data={**DATA,'status':'reviewed'}
        self.assertTrue(any('draft' in e for e in self.errors(data=data)))
    def test_no_unsourced_page(self):
        data={**DATA,'sources':[]}
        self.assertIn('missing edition source record',self.errors(data=data))
    def test_no_obsolete_check_date(self):
        data={**DATA,'source_checked_on':'2025-10-28'}
        self.assertTrue(any('source_checked_on' in e for e in self.errors(data=data)))
    def test_too_little_explanation(self):
        body='Only one sentence.\n'+'[Beer](../styles/pito.md) [Process](../processes/starch-conversion.md) [^v17-example]\n## Source notes\n[^v17-example]: Note.'
        self.assertTrue(any('insufficient' in e for e in self.errors(body=body)))
    def test_canonical_existing_revision_is_audited(self):
        body='Original article\n## Edition 1.7: newly sourced connections\n\n'+BODY
        self.assertEqual(self.errors(body=body,new=False),[])
    def test_old_edition_still_valid(self):
        report=validate(Path(__file__).resolve().parents[1],edition='1.6')
        self.assertTrue(report['ok'],report['errors'][:4])
        self.assertEqual((30,22),(report['counts']['new_subjects'],report['counts']['revised_subjects']))
    def test_full_current_corpus(self):
        report=validate(Path(__file__).resolve().parents[1],edition='1.7')
        self.assertTrue(report['ok'],report['errors'][:4])
        self.assertEqual((26,16,25),tuple(report['counts'][k] for k in ('new_subjects','revised_subjects','distinct_source_records')))
if __name__=='__main__':unittest.main()
