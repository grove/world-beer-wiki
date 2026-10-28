"""Edition 1.19: energy, carbon, wastewater, history and provenance regressions.

Offline editorial checks are not engineering, legal, safety or community approval.
"""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from atlas import load_documents
from research_quality import check_article, validate as research_quality
from build_edition_sources import audit, render as render_sources
from build_subject_index import render as render_subjects
from build_names_index import render as render_names
from check_inventory import validate as inventory

class Edition119Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.docs, cls.load_errors = load_documents(ROOT)
        cls.report = audit(ROOT, "1.19")

    def test_actual_release_counts_and_hygiene(self):
        self.assertFalse(self.load_errors, self.load_errors[:12])
        self.assertTrue(self.report["ok"], self.report["errors"][:15])
        self.assertEqual(
            (26, 21, 21, 109),
            tuple(self.report["counts"][k] for k in
                  ("new_subjects", "revised_subjects", "distinct_source_records", "source_usages"))
        )
        result = research_quality(ROOT, "1.19")
        self.assertTrue(result["ok"], result["errors"][:12])
        self.assertEqual(self.report["counts"], result["counts"])

    def test_generated_register_is_current_and_backlinks_are_actual(self):
        registered = (ROOT / "references/atlas-sources-1-19.md").read_text(encoding="utf-8")
        self.assertEqual(registered, render_sources(ROOT, "1.19"))
        for sid, pages in self.report["uses"].items():
            with self.subTest(sid=sid):
                self.assertIn(sid, registered)
                self.assertIn("Citing pages (" + str(len(pages)) + ")", registered)
                for page in pages:
                    self.assertIn("../" + page, registered)

    def test_mismatched_citation_metadata_and_unknown_source_rejected(self):
        source = {"id": "v119-case", "title": "A source", "resource": "https://example.org",
                  "author_label": "Researcher", "source_kind": "experiment",
                  "access_scope": "Abstract"}
        m = {"edition": "1.19", "sources": [source]}
        d = {"history/fixture.md": {"data": {"generated": {"by": "world-beer-wiki/1.19"},
              "sources": [dict(source)]}, "body": "Bounded case.[^v119-case]"}}
        self.assertTrue(audit(ROOT, "1.19", documents=d, manifest=m)["ok"])
        inconsistent = deepcopy(d)
        inconsistent["history/fixture.md"]["data"]["sources"][0]["resource"] = "https://invalid.example"
        self.assertFalse(audit(ROOT, "1.19", documents=inconsistent, manifest=m)["ok"])
        other = deepcopy(d)
        other["history/fixture.md"]["data"]["sources"][0]["id"] = "v119-unknown"
        self.assertTrue(any("unknown manifest source" in e
                            for e in audit(ROOT, "1.19", documents=other, manifest=m)["errors"]))
        extra = deepcopy(m)
        extra["sources"].append(dict(source))
        self.assertFalse(audit(ROOT, "1.19", documents=d, manifest=extra)["ok"])

    def test_new_article_requires_draft_access_and_body_citations(self):
        path = "categories/fermentation-co2-recovery-is-not-net-zero.md"
        item = self.docs[path]
        self.assertEqual([], check_article(path, item["data"], item["body"], True, "1.19"))
        changed = deepcopy(item["data"])
        changed["sources"][0]["access_scope"] = ""
        self.assertTrue(any("access_scope" in e for e in
                            check_article(path, changed, item["body"], True, "1.19")))
        body = item["body"].replace("[^v119-craftco2]", "")
        self.assertTrue(any("citation missing" in e for e in
                            check_article(path, item["data"], body, True, "1.19")))

    def test_nonfixed_ice_harvest_never_fabricates_festival_date(self):
        entry = self.docs["calendar/historic-natural-ice-harvest-season.md"]
        data = entry["data"]["calendar"]
        self.assertEqual("seasonal", data["kind"])
        self.assertNotIn("fixed_date", data)
        self.assertNotIn("editions", data)
        self.assertIn("not", entry["body"].lower())

    def test_industrial_cases_are_not_global_measured_reductions(self):
        model = self.docs["environment/industrial-heat-pump-model-boundaries.md"]["body"].lower()
        self.assertIn("model", model)
        self.assertIn("not", model)
        co2 = self.docs["categories/fermentation-co2-recovery-is-not-net-zero.md"]["body"].lower()
        self.assertIn("not", co2)
        self.assertIn("permanent", co2)

    def test_treatment_not_potable_water_or_food_safety(self):
        water = self.docs["stories/the-wastewater-does-not-become-drinking-water.md"]["body"].lower()
        self.assertIn("not", water)
        self.assertIn("cod", water)
        micro = self.docs["microbiology/digester-consortia-versus-brewing-starters.md"]["body"].lower()
        self.assertIn("not", micro)
        self.assertIn("starters", micro)

    def test_inventory_and_generated_indexes(self):
        inv = inventory(ROOT)
        self.assertTrue(inv["ok"], inv["errors"])
        self.assertEqual(766, inv["subject_articles"])
        self.assertEqual(13, len(inv["sections"]))
        self.assertEqual(render_subjects(ROOT),
                         (ROOT / "navigation/all-atlas-subjects.md").read_text(encoding="utf-8"))
        self.assertEqual(render_names(ROOT),
                         (ROOT / "navigation/all-names.md").read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
