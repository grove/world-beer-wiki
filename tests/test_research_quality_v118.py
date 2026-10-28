"""Edition 1.18: source-provenance, archival calendar, study-scope and navigation regression tests.

Offline metadata and link hygiene only; not independent legal or safety certification.
"""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from atlas import load_documents
from build_edition_sources import audit, render as render_sources
from build_subject_index import render as render_subjects
from build_names_index import render as render_names
from research_quality import check_article, validate as research_quality
from check_inventory import validate as inventory

class Edition118Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.docs, cls.load_errors = load_documents(ROOT)
        cls.report = audit(ROOT, "1.18")

    def test_cited_new_and_revised_work_counts(self):
        self.assertFalse(self.load_errors, self.load_errors[:10])
        self.assertTrue(self.report["ok"], self.report["errors"][:15])
        self.assertEqual(
            (27, 15, 22, 101),
            tuple(self.report["counts"][k] for k in
                  ("new_subjects", "revised_subjects", "distinct_source_records", "source_usages")))
        check = research_quality(ROOT, "1.18")
        self.assertTrue(check["ok"], check["errors"][:12])
        self.assertEqual(self.report["counts"], check["counts"])

    def test_source_register_matches_manifest_and_real_links(self):
        register = (ROOT/"references/atlas-sources-1-18.md").read_text(encoding="utf-8")
        self.assertEqual(register, render_sources(ROOT, "1.18"))
        for sid, paths in self.report["uses"].items():
            with self.subTest(source_id=sid):
                self.assertIn(sid, register)
                self.assertIn("Citing pages (" + str(len(paths)) + ")", register)
                for path in paths:
                    self.assertIn("../" + path, register)

    def test_source_id_reuse_rejects_changed_metadata(self):
        manifest = {"edition": "1.18", "sources": [
            {"id": "v118-fixture", "resource": "https://example.org/study",
             "title": "Scoped fixture", "author_label": "Fixture researcher",
             "source_kind": "primary-experiment", "access_scope": "Abstract only"}
        ]}
        docs = {"sensory/fixture.md": {"data": {
            "generated": {"by": "world-beer-wiki/1.18"},
            "sources": [dict(manifest["sources"][0])]
        }, "body": "Study body [^v118-fixture]."}}
        self.assertTrue(audit(ROOT, "1.18", documents=docs, manifest=manifest)["ok"])
        mutated = deepcopy(docs)
        mutated["sensory/fixture.md"]["data"]["sources"][0]["access_scope"] = "Full study"
        report = audit(ROOT, "1.18", documents=mutated, manifest=manifest)
        self.assertFalse(report["ok"])
        self.assertTrue(any("inconsistent access_scope" in e for e in report["errors"]))
        extra = deepcopy(manifest)
        extra["sources"].append(dict(extra["sources"][0]))
        self.assertFalse(audit(ROOT, "1.18", documents=docs, manifest=extra)["ok"])

    def test_new_page_requires_claim_citation_and_access(self):
        path = "environment/seven-breweries-versus-pet-keg-case.md"
        doc = self.docs[path]
        self.assertEqual([], check_article(path, doc["data"], doc["body"], True, "1.18"))
        altered = deepcopy(doc["data"])
        altered["sources"][0]["access_scope"] = ""
        self.assertTrue(any("access_scope" in e for e in
                            check_article(path, altered, doc["body"], True, "1.18")))
        body = doc["body"].replace("[^v118-lca22]", "")
        self.assertTrue(any("citation missing" in e for e in
                            check_article(path, doc["data"], body, True, "1.18")))

    def test_archival_dates_are_not_recurring_festivals(self):
        for path, date, source in (
            ("calendar/crown-cork-patent-1892.md", "1892-02-02", "v118-patent1892"),
            ("calendar/eu-ppwr-application-2026.md", "2026-08-12", "v118-ppwr-news26"),
        ):
            with self.subTest(path=path):
                d = self.docs[path]
                cal = d["data"]["calendar"]
                self.assertEqual("historical-event", cal["kind"])
                self.assertEqual("Gregorian", cal["system"])
                self.assertNotIn("fixed_date", cal)
                self.assertEqual(date, cal["editions"][0]["start"])
                self.assertEqual(date, cal["editions"][0]["end"])
                self.assertEqual(source, cal["editions"][0]["source_id"])
                self.assertIn("not", d["body"].lower())

    def test_packaging_lcas_keep_distinct_conclusions(self):
        body = self.docs["categories/why-packaging-lca-rankings-disagree.md"]["body"].lower()
        self.assertIn("short", body)
        self.assertIn("pet", body)
        self.assertIn("not", body)
        self.assertIn("[^v118-lca22]", body)
        self.assertIn("[^v118-lca24]", body)

    def test_microbial_and_legal_scope_are_explicit(self):
        micro = self.docs["microbiology/package-refermentation-pressure-vs-quality.md"]["body"].lower()
        self.assertIn("unintended", micro)
        self.assertIn("pressure", micro)
        food = self.docs["food/can-liners-and-food-contact-evidence.md"]["body"].lower()
        self.assertIn("2026", food)
        self.assertIn("not", food)

    def test_current_inventory_and_generated_indexes(self):
        inv = inventory(ROOT)
        self.assertTrue(inv["ok"], inv["errors"])
        self.assertGreaterEqual(inv["subject_articles"], 740)
        self.assertEqual(13, len(inv["sections"]))
        self.assertEqual(render_subjects(ROOT),
                         (ROOT/"navigation/all-atlas-subjects.md").read_text(encoding="utf-8"))
        self.assertEqual(render_names(ROOT),
                         (ROOT/"navigation/all-names.md").read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
