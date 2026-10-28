"""Edition 1.10 evidence-hygiene tests; never interpreted as historical or safety validation."""
from pathlib import Path
import unittest,sys
from copy import deepcopy
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from research_quality import check_article,validate
from atlas import load_documents
ROOT=Path(__file__).resolve().parents[1]
SOURCE={'id':'v110-example','resource':'https://example.org/research','title':'Study of one bounded system','author_label':'Named study authors','source_kind':'primary-experiment-abstract','access_scope':'Indexed abstract; sample and method constraints remain open.'}
DATA={'type':'Research Case','title':'Selected sample','status':'draft','scope':'One laboratory sample, not all products','review_note':'Not independently reviewed','source_checked_on':'2026-10-28','sources':[SOURCE]}
BODY=('This study concerns a particular sample and analytic question rather than a universal practice. '*22+
'[^v110-example] See [Culture](../culture/index.md) and [Methods](../processes/index.md).\n\n## Source notes\n\n[^v110-example]: Study summary.\n')

class Edition110Tests(unittest.TestCase):
    def audit(self,data=None,body=None,new=True):
        return check_article('culture/sample.md',DATA if data is None else data,BODY if body is None else body,new,edition='1.10')
    def test_positive_fixture(self):self.assertEqual([],self.audit())
    def test_source_access_required(self):
        d=deepcopy(DATA);d['sources'][0]['access_scope']=''
        self.assertTrue(any('access_scope' in x for x in self.audit(d)))
    def test_reference_in_explanation_required(self):
        b=BODY.replace('[^v110-example] See','See')
        self.assertTrue(any('citation missing' in x for x in self.audit(body=b)))
    def test_missing_review_disallowed(self):
        d=deepcopy(DATA);d.pop('review_note')
        self.assertTrue(any('review' in x for x in self.audit(d)))
    def test_unsupported_review_label(self):
        d=deepcopy(DATA);d['status']='community-approved'
        self.assertTrue(any('draft' in x for x in self.audit(d)))
    def test_explanatory_content_required(self):
        self.assertTrue(any('substantive' in x for x in self.audit(body='Small. [Culture](../culture/index.md) [Methods](../processes/index.md) [^v110-example]\n## Source notes\n[^v110-example]: Note.')))
    def test_version_specific_revision_only(self):
        updated='Original text and notes.\n\n## Edition 1.10: newly sourced connections\n\n'+BODY
        self.assertEqual([],self.audit(body=updated,new=False))
        self.assertTrue(any('citation missing' in x for x in self.audit(body=updated.replace('[^v110-example] See','See'),new=False)))
    def test_release_counts_and_hygiene(self):
        r=validate(ROOT,edition='1.10')
        self.assertTrue(r['ok'],r['errors'][:15])
        self.assertEqual(27,r['counts']['new_subjects'])
        self.assertEqual(15,r['counts']['revised_subjects'])
        self.assertEqual(19,r['counts']['distinct_source_records'])
    def test_previous_edition_counts_unchanged(self):
        for edition,new,revised in [('1.6',30,22),('1.7',26,16),('1.8',29,14),('1.9',31,18)]:
            with self.subTest(edition=edition):
                r=validate(ROOT,edition=edition)
                self.assertTrue(r['ok'],r['errors'][:7])
                self.assertEqual((new,revised),(r['counts']['new_subjects'],r['counts']['revised_subjects']))
    def test_source_records_have_local_backlinks(self):
        docs,errs=load_documents(ROOT)
        self.assertEqual([],errs)
        selected={}
        for path,doc in docs.items():
            for src in doc['data'].get('sources',[]):
                if src.get('id','').startswith('v110-'):selected.setdefault(src['id'],[]).append(path)
        self.assertEqual(19,len(selected))
        supplement=docs['references/atlas-sources-1-10.md']['body']
        for key in selected:
            self.assertIn('`'+key+'`',supplement)
            for path in selected[key]:self.assertIn('../'+path,supplement)
    def test_gluten_free_grain_misstatement_guard(self):
        text=(ROOT/'categories/gluten-free-beer-and-process-boundaries.md').read_text()
        self.assertIn('40-percent',text)
        self.assertIn('barley malt',text)
    def test_release_artifact_links_present(self):
        for path in ['editorial/research-update-1-10.md','editorial/atlas-progress.md','editorial/source-review-queue-1-10.md','references/atlas-sources-1-10.md','navigation/edition-1-10-reading-trails.md']:
            self.assertTrue((ROOT/path).is_file())
if __name__=='__main__':unittest.main()
