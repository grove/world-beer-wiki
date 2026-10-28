"""Edition 1.8: require accessed-source descriptions, actual citation use and provenance.

Tests protect structural evidence hygiene, not historical facts or human approval.
"""
from pathlib import Path
import sys
import unittest
from copy import deepcopy

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from research_quality import check_article, validate

SRC={'id':'v18-fixture','resource':'https://example.org/paper','title':'Study of selected samples',
     'author_label':'Research team','source_kind':'primary-abstract','access_scope':'Indexed abstract only; no full paper read.'}
DATA={'type':'Research Case','title':'Case','scope':'One named field study',
      'status':'draft','review_note':'No independent community review',
      'source_checked_on':'2026-10-28','sources':[SRC]}
BODY=('A primary study records a bounded case, specific samples and meaningful limitations. '*30+
      '\n\n[Culture](../culture/index.md) and [Methods](../processes/index.md) distinguish case and process. '
      '[^v18-fixture]\n\n## Source notes\n\n[^v18-fixture]: Indexed abstract.\n')

class Research18Tests(unittest.TestCase):
    def audit(self,data=None,body=None,new=True):
        return check_article('culture/fixture.md',data if data is not None else DATA,
                             body if body is not None else BODY,new,edition='1.8')
    def test_good_record(self):self.assertEqual(self.audit(),[])
    def test_uncited_metadata_is_rejected(self):
        text=BODY.replace('[^v18-fixture]\n\n## Source notes','\n\n## Source notes')
        self.assertTrue(any('citation missing' in e for e in self.audit(body=text)))
    def test_source_kind_required(self):
        data=deepcopy(DATA);data['sources'][0]['source_kind']=''
        self.assertTrue(any('source_kind' in e for e in self.audit(data=data)))
    def test_access_scope_required(self):
        data=deepcopy(DATA);data['sources'][0]['access_scope']=''
        self.assertTrue(any('access_scope' in e for e in self.audit(data=data)))
    def test_review_status_cannot_be_upgrade(self):
        data={**DATA,'status':'reviewed'}
        self.assertTrue(any('draft' in e for e in self.audit(data=data)))
    def test_missing_edition_source_fails(self):
        data={**DATA,'sources':[]}
        self.assertIn('missing edition source record',self.audit(data=data))
    def test_inadequate_prose_fails(self):
        short='Brief. [Culture](../culture/index.md) [Process](../processes/index.md) [^v18-fixture]\n## Source notes\n[^v18-fixture]: Abstract.'
        self.assertTrue(any('insufficient substantive' in e for e in self.audit(body=short)))
    def test_unlinked_canonical_context_fails(self):
        bad=BODY.replace('[Culture](../culture/index.md) and [Methods](../processes/index.md)','Culture and methods')
        self.assertTrue(any('fewer than two' in e for e in self.audit(body=bad)))
    def test_existing_revision_citations_checked(self):
        body='Old article\n\n## Edition 1.8: newly sourced connections\n\n'+BODY
        self.assertEqual(self.audit(body=body,new=False),[])
        self.assertTrue(any('citation missing' in e for e in self.audit(body=body.replace('[^v18-fixture]\n\n## Source notes','\n\n## Source notes'),new=False)))
    def test_previous_editions_not_regressed(self):
        root=Path(__file__).resolve().parents[1]
        for edition,new,revised in [('1.6',30,22),('1.7',26,16)]:
            with self.subTest(edition=edition):
                result=validate(root,edition=edition)
                self.assertTrue(result['ok'],result['errors'][:5])
                self.assertEqual((new,revised),(result['counts']['new_subjects'],result['counts']['revised_subjects']))
    def test_current_research_edition_coverage(self):
        result=validate(Path(__file__).resolve().parents[1],edition='1.8')
        self.assertTrue(result['ok'],result['errors'][:8])
        self.assertEqual((29,14,16),tuple(result['counts'][x] for x in ('new_subjects','revised_subjects','distinct_source_records')))

if __name__=='__main__':unittest.main()
