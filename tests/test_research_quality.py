"""Deliberately negative cases for the edition research-hygiene checker."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from research_quality import check_article, validate

SOURCE={'id':'v16-example','resource':'https://example.org/research','title':'Source','author_label':'Author','source_kind':'primary-abstract','access_scope':'Abstract only'}
DATA={'type':'Research Reference','title':'Example','scope':'Scoped to a study', 'review_note':'Not independently reviewed','status':'draft','source_checked_on':'2026-10-28','sources':[SOURCE]}
BODY='Research-based context and explanation. '*45+'\n[One](../styles/sahti.md) [Two](../ingredients/kveik.md) [^v16-example]\n\n[^v16-example]: [Source](https://example.org/research).\n'
class ResearchHygieneTests(unittest.TestCase):
    def test_valid_fixture(self):
        self.assertEqual([],check_article('culture/example.md',DATA,BODY,True))
    def test_missing_access_scope(self):
        bad={**DATA,'sources':[{**SOURCE,'access_scope':''}]}
        self.assertTrue(any('access_scope' in x for x in check_article('culture/example.md',bad,BODY,True)))
    def test_missing_actual_reference(self):
        bad=BODY.replace('[^v16-example]\n\n','\n\n')
        self.assertTrue(any('citation' in x for x in check_article('culture/example.md',DATA,bad,True)))
    def test_missing_links(self):
        bad=BODY.replace('[One](../styles/sahti.md) [Two](../ingredients/kveik.md)','None')
        self.assertTrue(any('reading links' in x for x in check_article('culture/example.md',DATA,bad,True)))
    def test_review_status_not_upgraded(self):
        bad={**DATA,'status':'reviewed'}
        self.assertTrue(any('draft' in x for x in check_article('culture/example.md',bad,BODY,True)))
    def test_existing_page_extension_checked(self):
        revised=BODY.split('[^v16-example]:')[0].replace('[^v16-example]','')
        self.assertEqual([],check_article('styles/example.md',DATA,'Old content\n',False))
        self.assertTrue(check_article('styles/example.md',DATA,'Old\n## Edition 1.6: sourced research connections\n'+revised,False))
    def test_real_corpus_passes(self):
        report=validate(Path(__file__).resolve().parents[1])
        self.assertTrue(report['ok'],report['errors'][:5])
        self.assertEqual(30,report['counts']['new_subjects'])
        self.assertEqual(22,report['counts']['revised_subjects'])
if __name__=='__main__':unittest.main()
