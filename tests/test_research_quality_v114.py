"""Edition 1.14 regression tests: source use, calendar semantics, institutions and experiments.

These tests verify corpus integrity, not independent cultural or scientific correctness.
"""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from atlas import load_documents, SUBJECT_DIRS
from check_inventory import validate as check_inventory
from research_quality import check_article, validate as check_release
from build_subject_index import render as render_subjects
from build_names_index import render as render_names

SOURCE = {
    'id': 'v114-paper', 'resource': 'https://example.org/study',
    'title': 'A measured intervention', 'author_label': 'Named researchers',
    'source_kind': 'primary-experimental-abstract',
    'access_scope': 'Abstract only; model treatment is not evidence of general quality or safety.',
}
DATA = {
    'type': 'Scientific Reference', 'title': 'Fixture', 'status': 'draft',
    'scope': 'One observed experimental comparison, not a general product rule.',
    'source_checked_on': '2026-10-28',
    'review_note': 'Not independently reviewed.', 'sources': [SOURCE],
}
BODY = (
    ('This study characterizes samples under one specific controlled condition; it does not establish '
     'a universal recipe or demonstrate consumer quality, causal ancestry or safety. ')*19 +
    '[^v114-paper] See [Beer foam](../sensory/index.md) and [Hop ingredients](../ingredients/index.md).\n'
    '## Source notes\n[^v114-paper]: A scoped original study.\n'
)

class Edition114Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.docs, cls.load_errors = load_documents(ROOT)

    def test_fixture_accepted_and_source_scope_required(self):
        self.assertEqual([], check_article('sensory/sample.md', DATA, BODY, True, '1.14'))
        for field in ('resource','title','author_label','source_kind','access_scope'):
            with self.subTest(field=field):
                d=deepcopy(DATA);d['sources'][0][field]=''
                self.assertTrue(any(field in x for x in check_article('sensory/sample.md',d,BODY,True,'1.14')))

    def test_claim_citation_and_footnote_enforced(self):
        self.assertTrue(any('citation missing' in x for x in check_article(
            'sensory/sample.md', DATA, BODY.replace('[^v114-paper] See','See'), True,'1.14')))
        self.assertTrue(any('missing source footnote' in x for x in check_article(
            'sensory/sample.md', DATA, BODY.replace('[^v114-paper]: A scoped original study.',''), True,'1.14')))

    def test_draft_scoped_and_not_a_bare_stub(self):
        d=deepcopy(DATA);d['status']='reviewed'
        self.assertTrue(any('not a draft' in x for x in check_article('sensory/sample.md',d,BODY,True,'1.14')))
        short='Short [^v114-paper].\n## Source notes\n[^v114-paper]: Paper.\n'
        errs=check_article('sensory/sample.md',DATA,short,True,'1.14')
        self.assertTrue(any('insufficient' in x for x in errs))
        self.assertTrue(any('fewer than two' in x for x in errs))

    def test_revision_scope_audits_only_current_extension(self):
        text='## Edition 1.14: newly sourced connections\n\n'+BODY
        self.assertEqual([],check_article('styles/example.md',DATA,text,False,'1.14'))
        self.assertTrue(any('citation missing' in x for x in check_article(
            'styles/example.md',DATA,text.replace('[^v114-paper] See','See'),False,'1.14')))

    def test_release_counts_and_prior_quality(self):
        report=check_release(ROOT,'1.14')
        self.assertTrue(report['ok'],report['errors'][:8])
        self.assertEqual((29,18,15,70),tuple(report['counts'][name] for name in
                        ('new_subjects','revised_subjects','distinct_source_records','source_usages')))
        for ed,n in [('1.12',30),('1.13',35)]:
            past=check_release(ROOT,ed)
            self.assertTrue(past['ok'],past['errors'][:5]);self.assertEqual(n,past['counts']['new_subjects'])

    def test_source_register_contains_actual_backlinks(self):
        self.assertFalse(self.load_errors,self.load_errors[:5])
        register=self.docs['references/atlas-sources-1-14.md']['body']
        usage={}
        for name,doc in self.docs.items():
            if name.split('/')[0] not in SUBJECT_DIRS:continue
            for src in doc['data'].get('sources',[]):
                if str(src.get('id','')).startswith('v114-'):
                    usage.setdefault(src['id'],set()).add(name)
        self.assertEqual(15,len(usage))
        self.assertEqual(70,sum(map(len,usage.values())))
        for sid,paths in usage.items():
            self.assertIn('`'+sid+'`',register)
            for path in paths:self.assertIn('../'+path,register)

    def test_historical_day_is_not_annual_festival(self):
        cal=self.docs['calendar/first-pilsen-batch-1842.md']['data']['calendar']
        self.assertEqual('historical-event',cal['kind'])
        self.assertEqual('1842-10-05',cal['editions'][0]['start'])
        self.assertEqual('1842-10-05',cal['editions'][0]['end'])
        self.assertEqual('v114-plzen',cal['editions'][0]['source_id'])
        self.assertIn('not',self.docs['calendar/first-pilsen-batch-1842.md']['body'].lower())

    def test_hop_calendar_is_seasonal_not_a_fixed_date(self):
        cal=self.docs['calendar/english-hop-harvest-and-drying-season.md']['data']['calendar']
        self.assertEqual('seasonal',cal['kind'])
        self.assertNotIn('editions',cal)
        self.assertNotIn('fixed_date',cal)
        self.assertIn('not',self.docs['calendar/english-hop-harvest-and-drying-season.md']['body'].lower())

    def test_foam_experiment_is_not_sensory_claim(self):
        body=self.docs['sensory/protein-z-humulinone-foam.md']['body'].lower()
        self.assertIn('protein z',body)
        self.assertIn('humulinone',body)
        self.assertIn('not',body)
        self.assertIn('[^v114-humulinone]',body)

    def test_tella_smoking_distinguishes_vessel_from_malt(self):
        text=self.docs['culture/tella-household-vessels-and-hospitality.md']['body'].lower()
        self.assertIn('container',text)
        self.assertIn('malt',text)
        self.assertIn('[^v114-tella]',text)

    def test_typed_relationships_locally_qualified(self):
        count=0
        for name,doc in self.docs.items():
            if name.split('/')[0] not in SUBJECT_DIRS:continue
            ids={s['id'] for s in doc['data'].get('sources',[])}
            for relation in doc['data'].get('relations',[]):
                scoped=[x for x in relation.get('source_ids',[]) if x.startswith('v114-')]
                if not scoped:continue
                count+=1
                self.assertTrue(relation.get('qualifier','').strip(),name)
                self.assertTrue(set(relation.get('source_ids',[])).issubset(ids),name)
        self.assertGreaterEqual(count,10)

    def test_generated_navigation_and_inventory_current(self):
        self.assertFalse(self.load_errors,self.load_errors[:5])
        inv=check_inventory(ROOT)
        self.assertTrue(inv['ok'],inv['errors'])
        self.assertGreaterEqual(inv['subject_articles'],643)
        self.assertEqual(13,len(inv['sections']))
        self.assertEqual((ROOT/'navigation/all-names.md').read_text(),render_names(ROOT))
        self.assertEqual((ROOT/'navigation/all-atlas-subjects.md').read_text(),render_subjects(ROOT))

if __name__=='__main__':unittest.main()
