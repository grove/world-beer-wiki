"""Edition 1.15 evidence hygiene and cross-section regression tests.

These are offline structural/source-use checks, not expert or legal review.
"""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from atlas import load_documents, SUBJECT_DIRS
from research_quality import validate as check_release, check_article
from check_inventory import validate as inventory_check
from build_subject_index import render as render_subjects
from build_names_index import render as render_names

SOURCE = {
    "id": "v115-document",
    "resource": "https://example.org/example",
    "title": "Scoped public source",
    "author_label": "Test authors",
    "source_kind": "primary-source",
    "access_scope": "Public extract; does not establish worldwide practice.",
}
DATA = {
    "type": "Evidence Reference",
    "title": "Fixture",
    "status": "draft",
    "scope": "One bounded event in a named region and year.",
    "source_checked_on": "2026-10-28",
    "review_note": "Not independently reviewed.",
    "sources": [SOURCE],
}
BODY = (
    "This is one specific studied case, and the available publication must be read "
    "in context before any conclusion can be transferred to a new system. "
    "The observations concern a defined sample and are not universal. "
) * 18 + (
    "[^v115-document] See [Methods](../editorial/methodology.md) "
    "and [Regions](../navigation/by-region.md).\n\n"
    "## Source notes\n[^v115-document]: Public source.\n"
)

class Edition115Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.docs, cls.errors = load_documents(ROOT)

    def test_new_release_counts_and_scope(self):
        report = check_release(ROOT, "1.15")
        self.assertTrue(report["ok"], report["errors"][:20])
        self.assertEqual(
            (19, 13, 16, 76),
            tuple(report["counts"][key] for key in
                  ("new_subjects", "revised_subjects", "distinct_source_records", "source_usages"))
        )
        for edition, n in [("1.13", 35), ("1.14", 29)]:
            older = check_release(ROOT, edition)
            self.assertTrue(older["ok"], older["errors"][:8])
            self.assertEqual(n, older["counts"]["new_subjects"])

    def test_negative_citation_and_access_fixtures(self):
        self.assertEqual([], check_article("history/fixture.md", DATA, BODY, True, "1.15"))
        short = "Short [^v115-document].\n## Source notes\n[^v115-document]: Source.\n"
        self.assertTrue(any("insufficient" in x for x in check_article(
            "history/fixture.md", DATA, short, True, "1.15")))
        for key in ("title", "resource", "author_label", "source_kind", "access_scope"):
            meta = deepcopy(DATA)
            meta["sources"][0][key] = ""
            self.assertTrue(any(key in x for x in check_article(
                "history/fixture.md", meta, BODY, True, "1.15")))
        self.assertTrue(any("citation missing" in x for x in check_article(
            "history/fixture.md", DATA, BODY.replace("[^v115-document] See", "See"), True, "1.15")))
        extension = "## Edition 1.15: newly sourced connections\n\n" + BODY
        self.assertEqual([], check_article("styles/fixture.md", DATA, extension, False, "1.15"))

    def test_actual_source_backlinks(self):
        self.assertFalse(self.errors, self.errors[:15])
        register = self.docs["references/atlas-sources-1-15.md"]["body"]
        used = {}
        for path, obj in self.docs.items():
            if path.split("/")[0] not in SUBJECT_DIRS or path.endswith("/index.md"):
                continue
            for source in obj["data"].get("sources", []):
                if str(source.get("id", "")).startswith("v115-"):
                    used.setdefault(source["id"], set()).add(path)
        self.assertEqual(16, len(used))
        self.assertEqual(76, sum(map(len, used.values())))
        for source_id, paths in used.items():
            with self.subTest(source_id=source_id):
                self.assertIn("`"+source_id+"`", register)
                self.assertIn("Citing pages ("+str(len(paths))+")", register)
                for path in paths:
                    self.assertIn("../"+path, register)

    def test_calendar_is_historical_and_not_a_recurring_holiday(self):
        event = self.docs["calendar/atf-nonalcoholic-marketing-circular-1991.md"]
        data = event["data"]["calendar"]
        self.assertEqual("historical-event", data["kind"])
        self.assertEqual("Gregorian", data["system"])
        self.assertEqual("1991-08-20", data["editions"][0]["start"])
        self.assertEqual("1991-08-20", data["editions"][0]["end"])
        self.assertNotIn("fixed_date", data)
        self.assertIn("not an annual", event["body"].lower())

    def test_sample_regulatory_and_foam_boundaries(self):
        uk = self.docs["categories/no-low-alcohol-descriptors-across-borders.md"]["body"].lower()
        self.assertIn("consultation", uk)
        self.assertIn("not", uk)
        foam = self.docs["sensory/beer-bubbles-and-model-boundaries.md"]["body"].lower()
        self.assertIn("one commercial", foam)
        self.assertIn("not", foam)
        water = self.docs["environment/brewery-water-ratio-versus-water-footprint.md"]["body"].lower()
        self.assertIn("direct", water)
        self.assertIn("indirect", water)

    def test_deterministic_indexes_and_inventory(self):
        inv = inventory_check(ROOT)
        self.assertTrue(inv["ok"], inv["errors"])
        self.assertGreaterEqual(inv["subject_articles"], 662)
        self.assertEqual(13, len(inv["sections"]))
        self.assertEqual(
            (ROOT/"navigation/all-names.md").read_text(encoding="utf-8"),
            render_names(ROOT)
        )
        self.assertEqual(
            (ROOT/"navigation/all-atlas-subjects.md").read_text(encoding="utf-8"),
            render_subjects(ROOT)
        )

if __name__ == "__main__":
    unittest.main()
