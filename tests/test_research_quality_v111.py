"""1.11 editorial hygiene. Tests cannot establish a historical truth or authorize ritual details."""
from pathlib import Path
from copy import deepcopy
import re
import sys
import unittest
import yaml
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from research_quality import check_article, validate
from atlas import load_documents, SUBJECT_DIRS
ROOT=Path(__file__).resolve().parents[1]
SOURCE={'id':'v111-fixture', 'resource':'https://example.org/study', 'title':'A bounded research example',
        'author_label':'Study authors', 'source_kind':'primary-study-abstract',
        'access_scope':'Abstract of one selected sample; no full-text or clinical review'}
DATA={'type':'Research case','title':'Sample','status':'draft','scope':'One experiment and its measured conditions',
      'source_checked_on':'2026-10-28','review_note':'Not independently reviewed','sources':[SOURCE]}
BODY=('This example distinguishes the sample from an untested population and refuses to infer product safety. '*24 +
      'The actual study method limits what the author can claim. [^v111-fixture] '\
      'See [Traditions](../culture/index.md) and [Processes](../processes/index.md).\n\n'
      '## Source notes\n\n[^v111-fixture]: Accessible abstract only.\n')

class Edition111ResearchTests(unittest.TestCase):
    def audit(self,data=None,body=None,new=True):
        return check_article('culture/example.md',DATA if data is None else data,BODY if body is None else body,new,edition='1.11')
    def test_valid_fixture(self):self.assertEqual([],self.audit())
    def test_metadata_access_scope_required(self):
        d=deepcopy(DATA);d['sources'][0]['access_scope']=''
        self.assertTrue(any('access_scope' in e for e in self.audit(data=d)))
    def test_source_author_and_kind_required(self):
        for field in ('author_label','source_kind'):
            with self.subTest(field=field):
                d=deepcopy(DATA);d['sources'][0][field]=''
                self.assertTrue(any(field in e for e in self.audit(data=d)))
    def test_body_citation_required_not_just_a_footnote(self):
        b=BODY.replace('[^v111-fixture] See','See')
        self.assertTrue(any('citation missing' in e for e in self.audit(body=b)))
    def test_source_note_required(self):
        b=BODY.replace('[^v111-fixture]: Accessible abstract only.','')
        self.assertTrue(any('missing source footnote' in e for e in self.audit(body=b)))
    def test_no_review_claim_by_status(self):
        d=deepcopy(DATA);d['status']='community-approved'
        self.assertTrue(any('not a draft' in e for e in self.audit(data=d)))
    def test_reading_links_and_substance_required(self):
        b=BODY.replace('[Traditions](../culture/index.md)','Traditions').replace('[Processes](../processes/index.md)','Processes')
        self.assertTrue(any('fewer than two' in e for e in self.audit(body=b)))
        b='Brief. [^v111-fixture] [Culture](../culture/index.md) [Process](../processes/index.md)\n## Source notes\n[^v111-fixture]: Note.'
        self.assertTrue(any('insufficient' in e for e in self.audit(body=b)))
    def test_revision_edition_section_citations_only(self):
        extension='Old source citations [^v111-fixture]\n\n## Edition 1.11: newly sourced connections\n\n'+BODY
        self.assertEqual([],self.audit(body=extension,new=False))
        extension=extension.replace('[^v111-fixture] See','See')
        self.assertTrue(any('citation missing' in e for e in self.audit(body=extension,new=False)))
    def test_edition_counts_and_source_hygiene(self):
        report=validate(ROOT,edition='1.11')
        self.assertTrue(report['ok'],report['errors'][:15])
        self.assertEqual((34,18,21,90),tuple(report['counts'][key] for key in ('new_subjects','revised_subjects','distinct_source_records','source_usages')))
    def test_old_edition_audits_unchanged(self):
        for ed,n,r in [('1.6',30,22),('1.7',26,16),('1.8',29,14),('1.9',31,18),('1.10',27,15)]:
            with self.subTest(edition=ed):
                report=validate(ROOT,edition=ed)
                self.assertTrue(report['ok'],report['errors'][:6])
                self.assertEqual((n,r),(report['counts']['new_subjects'],report['counts']['revised_subjects']))
    def test_new_source_backlinks_include_all_citations(self):
        docs,errors=load_documents(ROOT);self.assertEqual([],errors)
        listed=docs['references/atlas-sources-1-11.md']['body']
        paths={}
        for path,doc in docs.items():
            for source in doc['data'].get('sources',[]):
                if source['id'].startswith('v111-'):
                    paths.setdefault(source['id'],[]).append(path)
        self.assertEqual(21,len(paths))
        for sid,locations in paths.items():
            with self.subTest(source=sid):
                self.assertIn('`'+sid+'`',listed)
                for location in locations:self.assertIn('../'+location,listed)
    def test_calendar_is_seasonal_not_fictitious_event_date(self):
        docs,errors=load_documents(ROOT);self.assertEqual([],errors)
        info=docs['calendar/kunun-zaki-dry-season-association.md']['data']['calendar']
        self.assertEqual('seasonal',info['kind'])
        self.assertNotIn('months',info)
        self.assertNotIn('editions',info)
    def test_new_trails_link_every_section_used(self):
        docs,errors=load_documents(ROOT);self.assertEqual([],errors)
        trails=docs['navigation/edition-1-11-reading-trails.md']['body']
        for path,doc in docs.items():
            if doc['data'].get('generated',{}).get('by')=='world-beer-wiki/1.11' and path.split('/')[0] in SUBJECT_DIRS:
                with self.subTest(path=path):
                    self.assertIn('source_checked_on',doc['data'])
                    self.assertEqual('draft',doc['data']['status'])
        self.assertIn('A cereal refreshment need not be beer',trails)
        self.assertIn('Sap is not cereal wort',trails)
    def test_no_duplicate_related_ferment_style_paths(self):
        for path in ('styles/pulque.md','styles/cauim.md','styles/giroba.md','styles/kunun-zaki.md','styles/tepache.md'):
            data=yaml.safe_load((ROOT/path).read_text().split('---')[1]);self.assertEqual('Related Ferment Profile',data['type'])

if __name__=='__main__':unittest.main()
