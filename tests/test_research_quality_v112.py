"""Edition 1.12 regression tests: metadata integrity is not historical or safety validation."""
from pathlib import Path
from copy import deepcopy
import sys,unittest,re
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from atlas import SUBJECT_DIRS,load_documents
from research_quality import check_article,validate
from check_inventory import validate as validate_inventory
ROOT=Path(__file__).resolve().parents[1]
SOURCE={'id':'v112-fixture','resource':'https://example.org/abstract','title':'One bounded study','author_label':'Authors','source_kind':'primary-abstract','access_scope':'Indexed abstract, not full text.'}
DATA={'type':'Research Example','title':'Example','status':'draft','scope':'One measured fermentation study, not a population-level inference','source_checked_on':'2026-10-28','review_note':'Not independently reviewed','sources':[SOURCE]}
BODY=('A limited experiment describes these particular samples but cannot define a regional tradition or certify food safety. '*23+'[^v112-fixture] See [Culture](../culture/index.md) and [Process](../processes/index.md).\n\n## Source notes\n\n[^v112-fixture]: Indexed abstract.\n')
class Edition112ResearchTests(unittest.TestCase):
    def audit(self,data=None,body=None,new=True):
        return check_article('culture/example.md',DATA if data is None else data,BODY if body is None else body,new,edition='1.12')
    def test_valid_source_fixture(self):self.assertEqual([],self.audit())
    def test_access_scope_is_required(self):
        data=deepcopy(DATA);data['sources'][0]['access_scope']=''
        self.assertTrue(any('access_scope' in x for x in self.audit(data=data)))
    def test_author_and_kind_are_required(self):
        for field in ('author_label','source_kind'):
            with self.subTest(field=field):
                d=deepcopy(DATA);d['sources'][0][field]=''
                self.assertTrue(any(field in x for x in self.audit(data=d)))
    def test_inline_citation_is_required(self):
        self.assertTrue(any('citation missing' in x for x in self.audit(body=BODY.replace('[^v112-fixture] See','See'))))
    def test_source_footnote_is_required(self):
        self.assertTrue(any('missing source footnote' in x for x in self.audit(body=BODY.replace('[^v112-fixture]: Indexed abstract.',''))))
    def test_substance_and_links_are_required(self):
        self.assertTrue(any('insufficient' in x for x in self.audit(body='Brief. [^v112-fixture] [Culture](../culture/index.md) [Process](../processes/index.md)\n## Source notes\n[^v112-fixture]: Sample.')))
        self.assertTrue(any('fewer than two' in x for x in self.audit(body=BODY.replace('[Culture](../culture/index.md)','Culture').replace('[Process](../processes/index.md)','Process'))))
    def test_cannot_fake_review(self):
        d=deepcopy(DATA);d['status']='approved'
        self.assertTrue(any('not a draft' in x for x in self.audit(data=d)))
    def test_revision_only_validates_new_section(self):
        old='Older paragraph with earlier citation [^v112-fixture].\n\n## Edition 1.12: newly sourced connections\n\n'
        self.assertEqual([],self.audit(body=old+BODY,new=False))
        self.assertTrue(any('citation missing' in x for x in self.audit(body=old+BODY.replace('[^v112-fixture] See','See'),new=False)))
    def test_edition_counts_and_hygiene(self):
        report=validate(ROOT,'1.12');self.assertTrue(report['ok'],report['errors'][:10]);self.assertEqual((30,18,15,73),tuple(report['counts'][key] for key in ('new_subjects','revised_subjects','distinct_source_records','source_usages')))
    def test_prior_editions_remain_checkable(self):
        for ed,n,r in [('1.6',30,22),('1.7',26,16),('1.8',29,14),('1.9',31,18),('1.10',27,15),('1.11',34,18)]:
            with self.subTest(edition=ed):
                report=validate(ROOT,ed);self.assertTrue(report['ok'],report['errors'][:4]);self.assertEqual((n,r),(report['counts']['new_subjects'],report['counts']['revised_subjects']))
    def test_source_ledger_backlinks_really_exist(self):
        docs,errors=load_documents(ROOT);self.assertEqual([],errors)
        listed=docs['references/atlas-sources-1-12.md']['body']
        refs={}
        for path,doc in docs.items():
            for s in doc['data'].get('sources',[]):
                if str(s.get('id','')).startswith('v112-'):refs.setdefault(s['id'],[]).append(path)
        self.assertEqual(15,len(refs))
        for sid,paths in refs.items():
            with self.subTest(source=sid):
                self.assertIn('`'+sid+'`',listed)
                for path in paths:self.assertIn('../'+path,listed)
    def test_paiwan_and_laboratory_sample_are_not_equated(self):
        docs,errors=load_documents(ROOT);self.assertEqual([],errors)
        lab=docs['microbiology/taiwan-millet-starter-lab-study.md']['body'].lower()
        cultural=docs['culture/paiwan-millet-and-community-occasions.md']['body'].lower()
        self.assertIn('does **not** identify',lab)
        self.assertIn('paiwan',cultural)
        for path in ('calendar/paiwan-five-year-ritual-and-millet-wine.md','calendar/aludi-summer-gatherings.md'):
            data=docs[path]['data']['calendar'];self.assertNotIn('editions',data)
    def test_alcohol_is_not_universal_limit(self):
        docs,errors=load_documents(ROOT);self.assertEqual([],errors)
        self.assertIn('0.79%',docs['styles/boza.md']['body'])
        self.assertIn('not',docs['styles/boza.md']['body'].split('0.79%',1)[1][:180].lower())
    def test_no_duplicate_canonical_styles(self):
        docs,errors=load_documents(ROOT);self.assertEqual([],errors)
        for path in ('styles/boza.md','styles/kvass.md','styles/ikigage.md'):
            self.assertNotEqual('world-beer-wiki/1.12',docs[path]['data']['generated']['by'])
            self.assertIn('## Edition 1.12: newly sourced connections',docs[path]['body'])
    def test_homepage_inventory_must_stay_current(self):
        report=validate_inventory(ROOT);self.assertTrue(report['ok'],report['errors']);self.assertGreaterEqual(report['subject_articles'],579)
    def test_inventory_regression_catches_stale_current_number(self):
        import tempfile, shutil
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)
            # Only the material needed by inventory check: sampled documents of the actual repository.
            # Mock the loader to avoid duplicating 579 source files.
            from unittest.mock import patch
            (dest/'index.md').write_text(re.sub(r'All \d+ entries','All 999 entries',(ROOT/'index.md').read_text()),encoding='utf-8')
            (dest/'README.md').write_text((ROOT/'README.md').read_text(),encoding='utf-8')
            docs,_=load_documents(ROOT)
            with patch('check_inventory.load_documents',return_value=(docs,[])):
                errors=validate_inventory(dest)['errors']
            self.assertTrue(any('complete index' in e for e in errors))
if __name__=='__main__':unittest.main()
