"""Keep a standalone manuscript out of the reference-wiki ingestion path."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from atlas import load_documents
from build_site import wiki_files
from validate_wiki import is_wiki_path


class BookBoundaryTests(unittest.TestCase):
    def test_book_is_excluded_without_excluding_future_wiki_sections(self):
        self.assertFalse(is_wiki_path(Path('books/the-beer-detective/chapter.md')))
        self.assertTrue(is_wiki_path(Path('new-research/topic.md')))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for relative in ('books/book/chapter.md', 'new-research/topic.md'):
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('# A page\n', encoding='utf-8')
            documents, errors = load_documents(root)
            self.assertEqual(errors, [])
            self.assertEqual(set(documents), {'new-research/topic.md'})
            self.assertEqual([str(path) for path, _ in wiki_files(root)],
                             ['new-research/topic.md'])


if __name__ == '__main__':
    unittest.main()
