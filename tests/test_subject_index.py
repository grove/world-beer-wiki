"""Regression checks for the complete Markdown subject index (Python 3.11+)."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import build_subject_index as registry
from atlas import SUBJECT_DIRS

class SubjectIndexTests(unittest.TestCase):
    def test_deterministic_and_checked_in(self):
        expected=(ROOT/'navigation/all-atlas-subjects.md').read_text(encoding='utf-8')
        self.assertEqual(registry.render(ROOT), expected)
        self.assertEqual(registry.render(ROOT), registry.render(ROOT))

    def test_all_families_represented(self):
        page=registry.render(ROOT)
        for section in SUBJECT_DIRS:
            self.assertIn(f'## {section.replace("-", " ").title()} (',page)
        for section in SUBJECT_DIRS:
            for subject in (ROOT/section).glob('*.md'):
                if subject.name == 'index.md': continue
                self.assertEqual(page.count(f'](../{section}/{subject.name})'),1,subject)

    def test_check_rejects_stale_directory(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            (root/'styles').mkdir()
            (root/'styles/test.md').write_text('''---
type: Test
title: Example
status: draft
---
# Example
''',encoding='utf-8')
            (root/'navigation').mkdir()
            target=root/'navigation/all-atlas-subjects.md'
            target.write_text('outdated',encoding='utf-8')
            argv=[sys.executable,str(ROOT/'tools/build_subject_index.py'),'--root',str(root),'--check']
            self.assertNotEqual(subprocess.run(argv,capture_output=True,check=False).returncode,0)
            self.assertIn('Example',registry.render(root))
            target.write_text(registry.render(root),encoding='utf-8')
            self.assertEqual(subprocess.run(argv,capture_output=True,check=False).returncode,0)

    def test_invalid_subject_title_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            (root/'styles').mkdir()
            (root/'styles/broken.md').write_text('''---
type: Test
status: draft
---
# Missing frontmatter title
''',encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'missing title/type'):
                registry.render(root)

    def test_pipe_in_title_is_escaped(self):
        self.assertEqual(registry.esc('One | Two'),'One \\| Two')

if __name__=='__main__':unittest.main()
