"""Tests for dynamic navigation, source preservation and search metadata."""
import sys
import tempfile
from pathlib import Path
import unittest

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from build_site import build  # noqa: E402


def paths_in_nav(nav):
    if isinstance(nav, str):
        yield nav
    elif isinstance(nav, list):
        for part in nav:
            yield from paths_in_nav(part)
    elif isinstance(nav, dict):
        for value in nav.values():
            yield from paths_in_nav(value)


class BuildSiteTests(unittest.TestCase):
    def write(self, name, content):
        target = self.root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write("mkdocs.yml", "site_name: Example\n")
        self.write("index.md", "# Wiki\n\n[Reading guide](README.md)\n")
        self.write("README.md", "# Reading guide\n")
        self.write("styles/index.md", "# Profiles\n")
        self.write(
            "styles/amber-ale.md",
            "---\ntitle: Amber Ale\ntype: Beer Style\nstatus: draft\n"
            "regions:\n- Europe\naliases:\n- Ale & Malt\n---\n\n# Amber Ale\n\nExample\n",
        )
        self.write("styles/zebra-lager.md", "# Zebra Lager\n")
        self.write("categories/index.md", "# Guides\n")
        self.write("categories/guide.md", "# Brewing guide\n")
        self.write("ingredients/index.md", "# Ingredients\n")
        self.write("ingredients/hops.md", "# Hops\n")
        self.write("future-section/index.md", "# New area\n")
        self.write("future-section/example.md", "# Future article\n")
        self.write("tools/hidden.md", "# Internal tool documentation\n")
        self.write("tools/atlas.py", "# readable maintenance source\n")
        self.write("tests/test_atlas.py", "# readable regression source\n")
        self.write("culture/index.md", "# Culture\n")
        self.write("culture/case.md", "---\ntitle: Case\ntype: Cultural Practice\nstatus: draft\n---\n\n# Case\n")
        self.write("website/assets/stylesheets/extra.css", "/* fixture */")

    def test_excluded_repository_file_requires_absolute_link(self):
        self.write(".github/workflows/validate.yml", "name: Validate\n")
        self.write("editorial/index.md", "# Editorial\n")
        self.write("editorial/progress.md", "# Progress\n\n[CI](../.github/workflows/validate.yml)\n")
        with self.assertRaisesRegex(ValueError, "site link target is not published"):
            build(self.root)

    def test_external_github_link_is_allowed(self):
        self.write("editorial/index.md", "# Editorial\n")
        self.write("editorial/progress.md", "# Progress\n\n[CI](https://github.com/example/repo/blob/main/.github/workflows/validate.yml)\n")
        build(self.root)
        self.assertTrue((self.root / ".build/docs/editorial/progress.md").is_file())

    def test_nav_search_aliases_and_growth(self):
        original = (self.root / "styles/amber-ale.md").read_text()
        build(self.root)
        docs = self.root / ".build/docs"
        config = yaml.safe_load((self.root / ".build/mkdocs.yml").read_text())
        all_pages = {p.relative_to(docs).as_posix() for p in docs.rglob("*.md")}
        self.assertEqual(set(paths_in_nav(config["nav"])), all_pages)
        self.assertEqual(config["docs_dir"], str(docs))
        self.assertTrue((docs / "assets/stylesheets/extra.css").is_file())
        self.assertFalse((docs / "tools/hidden.md").exists())
        self.assertTrue((docs / "tools/atlas.py").is_file())
        self.assertTrue((docs / "tests/test_atlas.py").is_file())
        self.assertIn("Research draft", (docs / "culture/case.md").read_text())
        homepage = (docs / "index.md").read_text()
        self.assertIn("<strong>2</strong>", homepage)
        self.assertIn("[Reading guide](reading-guide.md)", homepage)
        self.assertTrue((docs / "reading-guide.md").is_file())
        self.assertFalse((docs / "README.md").exists())
        self.assertIn("<strong>1</strong>", homepage)
        profile = (docs / "styles/amber-ale.md").read_text()
        self.assertIn("Research draft", profile)
        self.assertIn("Ale &amp; Malt", profile)
        self.assertEqual((self.root / "styles/amber-ale.md").read_text(), original)

        self.write("styles/new-lager.md", "# New Lager\n")
        build(self.root)
        updated_docs = self.root / ".build/docs"
        updated_config = yaml.safe_load((self.root / ".build/mkdocs.yml").read_text())
        self.assertIn("<strong>3</strong>", (updated_docs / "index.md").read_text())
        self.assertIn("styles/new-lager.md", set(paths_in_nav(updated_config["nav"])))


if __name__ == "__main__":
    unittest.main()
