"""Edition 1.17: literature-scope, provenance, typed links and current directory checks.

These are offline editorial integrity checks, NOT external scientific or food-safety review.
"""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from atlas import SUBJECT_DIRS, load_documents
from build_edition_sources import audit, render as render_sources
from build_subject_index import render as render_subjects
from build_names_index import render as render_names
from research_quality import check_article, validate as research_quality
from check_inventory import validate as inventory

class Edition117Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.docs, cls.load_errors = load_documents(ROOT)
        cls.report = audit(ROOT, "1.17")

    def test_new_release_counts(self):
        self.assertFalse(self.load_errors, self.load_errors[:8])
        self.assertTrue(self.report["ok"], self.report["errors"][:15])
        self.assertEqual(
            (28, 18, 19, 95),
            tuple(self.report["counts"][key] for key in
                  ("new_subjects", "revised_subjects", "distinct_source_records", "source_usages")))
        checked = research_quality(ROOT, "1.17")
        self.assertTrue(checked["ok"], checked["errors"][:12])
        self.assertEqual(self.report["counts"], checked["counts"])

    def test_generated_source_register_is_exact(self):
        self.assertEqual(
            (ROOT / "references/atlas-sources-1-17.md").read_text(encoding="utf-8"),
            render_sources(ROOT, "1.17"))
        content = self.docs["references/atlas-sources-1-17.md"]["body"]
        for sid, pages in self.report["uses"].items():
            with self.subTest(sid=sid):
                self.assertIn(sid, content)
                self.assertIn(f"Citing pages ({len(pages)})", content)
                for page in pages:
                    self.assertIn("../" + page, content)

    def test_manifest_rejects_mismatched_source_metadata(self):
        man = {"edition": "1.17", "sources": [{
            "id": "v117-case", "resource": "https://example.org/source",
            "title": "Case report", "author_label": "Study group",
            "source_kind": "observational-study", "access_scope": "Abstract only"
        }]}
        doc = {"culture/example.md": {
            "data": {"generated": {"by": "world-beer-wiki/1.17"},
                     "sources": [dict(man["sources"][0])]},
            "body": "A bounded case.[^v117-case]"}}
        self.assertTrue(audit(ROOT, "1.17", documents=doc, manifest=man)["ok"])
        changed = deepcopy(doc)
        changed["culture/example.md"]["data"]["sources"][0]["resource"] = "https://example.org/different"
        self.assertTrue(any("inconsistent resource" in e for e in
                            audit(ROOT, "1.17", documents=changed, manifest=man)["errors"]))
        extra = deepcopy(man)
        extra["sources"].append(dict(man["sources"][0]))
        self.assertFalse(audit(ROOT, "1.17", documents=doc, manifest=extra)["ok"])

    def test_new_article_source_citations_and_draft(self):
        name = "microbiology/fungal-dna-versus-mycotoxin-measurement.md"
        doc = self.docs[name]
        self.assertEqual([], check_article(name, doc["data"], doc["body"], True, "1.17"))
        changed = deepcopy(doc["data"])
        changed["sources"][0]["access_scope"] = ""
        self.assertTrue(any("access_scope" in e for e in
                            check_article(name, changed, doc["body"], True, "1.17")))
        without = doc["body"].replace("[^v117-fusarium-trial]", "")
        self.assertTrue(any("citation missing" in e for e in
                            check_article(name, doc["data"], without, True, "1.17")))

    def test_seasonal_calendar_has_no_invented_fixed_date(self):
        doc = self.docs["calendar/barley-harvest-window-not-fixed.md"]
        cal = doc["data"]["calendar"]
        self.assertEqual("seasonal", cal["kind"])
        self.assertNotIn("fixed_date", cal)
        self.assertNotIn("editions", cal)
        self.assertIn("not fixed", doc["body"].lower())

    def test_crop_pathogen_is_not_living_tradition_or_safe_batch(self):
        text = self.docs["categories/field-fungus-vs-starter-microbes.md"]["body"].lower()
        self.assertIn("not", text)
        self.assertIn("starter", text)
        result = self.docs["processes/fusarium-malt-to-beer-transformation.md"]["body"].lower()
        self.assertIn("inoculated", result)
        self.assertIn("not", result)

    def test_regulation_is_not_universal_beer_limit(self):
        doc = self.docs["food/spent-grain-and-food-safety-boundaries.md"]["body"].lower()
        self.assertIn("not", doc)
        self.assertIn("product", doc)
        self.assertIn("eu", doc)

    def test_bere_introduction_not_assigned_exact_day(self):
        d = self.docs["history/bere-introduction-date-uncertain.md"]
        self.assertNotIn("calendar", d["data"])
        self.assertIn("uncertain", d["body"].lower())
        self.assertEqual("draft", d["data"]["status"])

    def test_current_inventory_and_deterministic_navigation(self):
        inv = inventory(ROOT)
        self.assertTrue(inv["ok"], inv["errors"])
        self.assertEqual(713, inv["subject_articles"])
        self.assertEqual(13, len(inv["sections"]))
        self.assertEqual(render_subjects(ROOT),
                         (ROOT / "navigation/all-atlas-subjects.md").read_text(encoding="utf-8"))
        self.assertEqual(render_names(ROOT),
                         (ROOT / "navigation/all-names.md").read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
