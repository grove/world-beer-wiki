"""Edition 1.13 tests: evidence hygiene, cultural boundaries and reproducible navigation.

These tests check source and publishing *integrity*, never certify external truth,
tradition, laboratory safety or community endorsement.
"""
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch
import re
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from atlas import load_documents, SUBJECT_DIRS
from check_inventory import validate as check_inventory
from research_quality import check_article, validate as check_release
from build_names_index import render as render_names
from build_subject_index import render as render_subjects

SOURCE = {
    'id': 'v113-experiment', 'resource': 'https://example.org/study',
    'title': 'One study in a known place', 'author_label': 'Researcher',
    'source_kind': 'primary-abstract',
    'access_scope': 'Abstract only; neither an entire region nor proven safety.',
}
DATA = {
    'type': 'Experimental Study', 'title': 'Fixture', 'status': 'draft',
    'scope': 'Particular samples under particular laboratory conditions',
    'source_checked_on': '2026-10-28',
    'review_note': 'Not independently reviewed', 'sources': [SOURCE],
}
BODY = (
    'This limited study describes specific observations without certifying safety, '
    'proving historical ancestry or defining an entire regional drinking culture. ' * 20
    + '[^v113-experiment] Compare [Culture](../culture/index.md) and '
    '[Processes](../processes/index.md).\n\n'
    '## Source notes\n\n[^v113-experiment]: Original study abstract.\n'
)

class Edition113Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.docs, cls.load_errors = load_documents(ROOT)

    def test_fixture_accepted(self):
        self.assertEqual([], check_article('microbiology/example.md', DATA, BODY, True, '1.13'))

    def test_source_access_provenance_required(self):
        for field in ('resource','title','author_label','source_kind','access_scope'):
            with self.subTest(field=field):
                d=deepcopy(DATA)
                d['sources'][0][field]=''
                errs=check_article('microbiology/example.md',d,BODY,True,'1.13')
                self.assertTrue(any(field in e for e in errs), errs)

    def test_claim_citation_and_footnote_required(self):
        errs=check_article('microbiology/example.md',DATA,BODY.replace('[^v113-experiment] Compare','Compare'),True,'1.13')
        self.assertTrue(any('citation missing' in e for e in errs))
        errs=check_article('microbiology/example.md',DATA,BODY.replace('[^v113-experiment]: Original study abstract.',''),True,'1.13')
        self.assertTrue(any('missing source footnote' in e for e in errs))

    def test_substance_links_and_draft_required(self):
        e=check_article('microbiology/example.md',DATA,'Short [^v113-experiment].\n## Source notes\n[^v113-experiment]: Abstract.\n',True,'1.13')
        self.assertTrue(any('insufficient' in x for x in e))
        self.assertTrue(any('fewer than two' in x for x in e))
        d=deepcopy(DATA)
        d['status']='reviewed'
        self.assertTrue(any('not a draft' in x for x in check_article('microbiology/example.md',d,BODY,True,'1.13')))
        d=deepcopy(DATA)
        d['source_checked_on']='2021-01-01'
        self.assertTrue(any('source_checked_on' in x for x in check_article('microbiology/example.md',d,BODY,True,'1.13')))

    def test_revision_only_audits_new_evidence_section(self):
        revision='## Edition 1.13: newly sourced connections\n\n'+BODY
        self.assertEqual([],check_article('styles/example.md',DATA,revision,False,'1.13'))
        self.assertTrue(any('citation missing' in e for e in check_article(
            'styles/example.md',DATA,revision.replace('[^v113-experiment] Compare','Compare'),False,'1.13')))

    def test_actual_release_scope(self):
        report=check_release(ROOT,'1.13')
        self.assertTrue(report['ok'],report['errors'][:16])
        self.assertEqual((35,19,21,93),tuple(report['counts'][n] for n in
            ('new_subjects','revised_subjects','distinct_source_records','source_usages')))

    def test_prior_edition_qa_remains_runnable(self):
        for ed,count in [('1.6',30),('1.8',29),('1.10',27),('1.11',34),('1.12',30)]:
            with self.subTest(edition=ed):
                report=check_release(ROOT,ed)
                self.assertTrue(report['ok'],report['errors'][:6])
                self.assertEqual(count,report['counts']['new_subjects'])

    def test_source_register_has_all_real_backlinks(self):
        self.assertEqual([],self.load_errors)
        ledger=self.docs['references/atlas-sources-1-13.md']['body']
        by_source={}
        for path,doc in self.docs.items():
            if path.split('/')[0] not in SUBJECT_DIRS: continue
            for src in doc['data'].get('sources',[]):
                if str(src.get('id','')).startswith('v113-'):
                    by_source.setdefault(src['id'],set()).add(path)
        self.assertEqual(21,len(by_source))
        self.assertEqual(93,sum(len(paths) for paths in by_source.values()))
        for sid,paths in by_source.items():
            with self.subTest(source=sid):
                self.assertIn('`'+sid+'`',ledger)
                for path in paths:
                    self.assertIn('../'+path,ledger)

    def test_evidence_bearing_relations_have_local_sources(self):
        self.assertEqual([],self.load_errors)
        n=0
        for path,doc in self.docs.items():
            if path.split('/')[0] not in SUBJECT_DIRS:continue
            local={s['id'] for s in doc['data'].get('sources',[])}
            for rel in doc['data'].get('relations',[]):
                if not isinstance(rel,dict) or not any(str(x).startswith('v113-') for x in rel.get('source_ids',[])):continue
                n+=1
                self.assertTrue(rel.get('qualifier','').strip(),path)
                self.assertTrue(set(rel['source_ids']).issubset(local),path)
                self.assertTrue(any(s.startswith('v113-') for s in rel['source_ids']),path)
        self.assertGreaterEqual(n,15)

    def test_jiahu_two_evidence_horizons_not_recipe(self):
        b=self.docs['history/jiahu-2004-to-2026-reinterpretation.md']['body'].lower()
        self.assertIn('2004',b)
        self.assertIn('2026',b)
        self.assertIn('not',b)
        for sid in ('v113-jiahu-2004','v113-jiahu-2026'):
            self.assertIn('[^'+sid+']',b)

    def test_muratina_social_occasion_not_fixed_festival(self):
        d=self.docs['calendar/muratina-and-marriage-occasions.md']
        cal=d['data'].get('calendar')
        self.assertIsInstance(cal,dict)
        self.assertNotIn('editions',cal)
        self.assertNotIn('fixed_date',cal)
        self.assertIn('marriage',d['body'].lower())
        self.assertIn('kigelia',self.docs['ingredients/kigelia-fruit-fibre.md']['body'].lower())

    def test_sampling_is_not_a_universal_yeast_starter(self):
        body=self.docs['microbiology/tchoukoutou-yeast-surveys-in-disagreement.md']['body'].lower()
        for year in ('2011','2013','2025'):
            self.assertIn(year,body)
        self.assertIn('sampling',body)
        self.assertIn('not',body)

    def test_bushera_food_drink_not_standardized_beer(self):
        body=self.docs['styles/bushera.md']['body'].lower()
        self.assertIn('cereal',body)
        self.assertIn('food',body)
        self.assertIn('not',body)

    def test_inventory_and_name_index_current(self):
        report=check_inventory(ROOT)
        self.assertTrue(report['ok'],report['errors'])
        self.assertEqual(614,report['subject_articles'])
        self.assertEqual(13,len(report['sections']))
        self.assertEqual((ROOT/'navigation/all-names.md').read_text(encoding='utf-8'),render_names(ROOT))
        self.assertEqual((ROOT/'navigation/all-atlas-subjects.md').read_text(encoding='utf-8'),render_subjects(ROOT))

    def test_name_index_detects_stale_omission(self):
        current=render_names(ROOT)
        self.assertIn('Muratina',current)
        self.assertIn('Jiahu',current)
        self.assertNotEqual(current,current.replace('Muratina','[OMITTED]'))

if __name__=='__main__':
    unittest.main()
