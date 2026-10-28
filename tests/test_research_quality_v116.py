"""Edition 1.16: provenance, study-scope, navigation and negative-case tests.

These checks do not independently validate source accuracy or food safety.
"""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from atlas import SUBJECT_DIRS, load_documents
from research_quality import check_article, validate as check_research
from check_inventory import validate as check_inventory
from build_subject_index import render as render_subjects
from build_names_index import render as render_names
from build_edition_sources import audit, render as render_sources


class Edition116Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.docs, cls.load_errors = load_documents(ROOT)
        cls.report = audit(ROOT, "1.16")

    def test_release_counts_and_metadata(self):
        self.assertFalse(self.load_errors, self.load_errors[:8])
        self.assertTrue(self.report["ok"], self.report["errors"][:12])
        self.assertEqual(
            (23, 16, 19, 94),
            tuple(self.report["counts"][key] for key in
                  ("new_subjects", "revised_subjects", "distinct_source_records", "source_usages"))
        )
        quality = check_research(ROOT, "1.16")
        self.assertTrue(quality["ok"], quality["errors"][:12])
        self.assertEqual(self.report["counts"], quality["counts"])

    def test_source_register_is_derived_and_current(self):
        text = (ROOT / "references/atlas-sources-1-16.md").read_text(encoding="utf-8")
        self.assertEqual(render_sources(ROOT), text)
        for sid, paths in self.report["uses"].items():
            self.assertIn(sid, text)
            self.assertIn("Citing pages (" + str(len(paths)) + ")", text)
            for path in paths:
                self.assertIn("../" + path, text)

    def test_reused_source_metadata_must_be_identical(self):
        manifest = {"edition": "1.16", "sources": [
            {"id": "v116-lab", "resource": "https://example.org/paper",
             "title": "Fixture study", "author_label": "A. Researcher",
             "source_kind": "primary", "access_scope": "Abstract only"}
        ]}
        page = {"data": {"generated": {"by": "world-beer-wiki/1.16"},
                         "sources": [dict(manifest["sources"][0])]},
                "body": "Study [^v116-lab]."}
        docs = {"history/fixture.md": page}
        self.assertTrue(audit(ROOT, documents=docs, manifest=manifest)["ok"])
        changed = deepcopy(docs)
        changed["history/fixture.md"]["data"]["sources"][0]["title"] = "Different work"
        report = audit(ROOT, documents=changed, manifest=manifest)
        self.assertFalse(report["ok"])
        self.assertTrue(any("inconsistent title" in e for e in report["errors"]))
        changed = deepcopy(docs)
        changed["history/fixture.md"]["data"]["sources"][0]["id"] = "v116-unknown"
        report = audit(ROOT, documents=changed, manifest=manifest)
        self.assertFalse(report["ok"])
        self.assertTrue(any("unknown manifest source" in e for e in report["errors"]))
        changed = deepcopy(manifest)
        changed["sources"].append(dict(changed["sources"][0]))
        self.assertFalse(audit(ROOT, documents=docs, manifest=changed)["ok"])

    def test_source_access_and_reference_in_body_required(self):
        doc = self.docs["sensory/triangle-tests-for-beer.md"]
        body = doc["body"]
        data = doc["data"]
        self.assertEqual([], check_article("sensory/example.md", data, body, True, "1.16"))
        altered = deepcopy(data)
        altered["sources"][0]["access_scope"] = ""
        self.assertTrue(any("access_scope" in e for e in
                            check_article("sensory/example.md", altered, body, True, "1.16")))
        missing = body.replace("[^v116-triangle]", "")
        self.assertTrue(any("citation missing" in e for e in
                            check_article("sensory/example.md", data, missing, True, "1.16")))

    def test_history_is_not_a_fake_festival(self):
        for name in ("history/richardson-saccharometry-and-extract.md",
                     "objects/saccharometer-in-the-museum.md"):
            self.assertNotIn("calendar", self.docs[name]["data"])
            self.assertEqual("draft", self.docs[name]["data"]["status"])
        self.assertIn("1784", self.docs["history/richardson-saccharometry-and-extract.md"]["body"])

    def test_different_methods_not_mistaken_for_safety(self):
        acid = self.docs["categories/acidity-ph-ta-and-sourness.md"]["body"].lower()
        self.assertIn("food-safety", acid)
        self.assertIn("not", acid)
        test = self.docs["sensory/triangle-tests-for-beer.md"]["body"].lower()
        self.assertIn("preferred", test)
        self.assertIn("chance", test)
        self.assertIn("not", test)

    def test_inventory_and_generated_indices(self):
        inv = check_inventory(ROOT)
        self.assertTrue(inv["ok"], inv["errors"])
        self.assertEqual(685, inv["subject_articles"])
        self.assertEqual(13, len(inv["sections"]))
        self.assertEqual(render_subjects(ROOT),
                         (ROOT / "navigation/all-atlas-subjects.md").read_text(encoding="utf-8"))
        self.assertEqual(render_names(ROOT),
                         (ROOT / "navigation/all-names.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
