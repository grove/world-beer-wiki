#!/usr/bin/env python3
"""Stage the canonical Markdown wiki for MkDocs, generating growth-safe navigation.

Nothing in the source wiki is moved or rewritten. All HTML embellishments are
applied only to the disposable .build/docs copy.
"""
from collections import defaultdict
import html
import os
from pathlib import Path, PurePosixPath
import re
import shutil

import yaml


ROOT = Path(__file__).resolve().parents[1]
IGNORED_DIRS = {
    ".git", ".github", ".build", ".venv", "venv", "site",
    "node_modules", "__pycache__", "tools", "tests", "website",
}
CONTENT_SUFFIXES = {
    ".md", ".markdown", ".png", ".jpg", ".jpeg", ".gif",
    ".webp", ".avif", ".svg", ".pdf",
}
TOP_LEVEL = (
    ("styles", "Beer & traditions"),
    ("categories", "Category guides"),
    ("ingredients", "Ingredients & cultures"),
    ("navigation", "Explore by topic"),
)
RESEARCH = (
    ("editorial", "Editorial & methodology"),
    ("references", "Sources & references"),
)


def wiki_files(root):
    """Mirror Markdown and local media, including any future content section."""
    for base, directories, filenames in os.walk(root):
        directories[:] = sorted(
            name for name in directories
            if not name.startswith(".") and name not in IGNORED_DIRS
        )
        for name in sorted(filenames):
            if name.startswith(".") or Path(name).suffix.lower() not in CONTENT_SUFFIXES:
                continue
            file = Path(base) / name
            yield file.relative_to(root), file


def frontmatter(text):
    match = re.match(r"\A---[ \t]*\n(.*?)\n---[ \t]*\n", text, flags=re.S)
    if not match:
        return {}
    return yaml.safe_load(match.group(1)) or {}


def page_title(file):
    contents = file.read_text(encoding="utf-8")
    title = frontmatter(contents).get("title")
    if not title:
        match = re.search(r"(?m)^# (.+)$", contents)
        title = match.group(1) if match else file.stem.replace("-", " ").title()
    return re.sub(r"[*_]", "", str(title)).replace(chr(96), "").strip()


def insert_below_title(source, snippet):
    match = re.search(r"(?m)^# .+\n", source)
    if not match:
        return source
    return source[:match.end()] + "\n" + snippet + "\n" + source[match.end():]


def article_chips(source):
    meta = frontmatter(source)
    properties = []
    if meta.get("type"):
        properties.append(str(meta["type"]))
    if meta.get("regions") and isinstance(meta["regions"], list):
        properties.extend(str(region) for region in meta["regions"][:2])
    if meta.get("status") == "draft":
        properties.append("Research draft")
    aliases = meta.get("aliases") or []
    if not properties and not aliases:
        return source

    chips = "".join(
        '<span class="ww-chip">' + html.escape(item) + "</span>"
        for item in properties
    )
    snippet = '<div class="ww-chips" aria-label="Article details">' + chips + "</div>"
    if isinstance(aliases, list) and aliases:
        names = ", ".join(html.escape(str(alias)) for alias in aliases)
        snippet += (
            '<p class="ww-alias"><strong>Indexed names:</strong> '
            + names + "</p>"
        )
    return insert_below_title(source, snippet)


def home_intro(pages):
    def count(folder):
        return sum(
            path.parts[0] == folder and path.name.lower() != "index.md"
            for path in pages
            if len(path.parts) > 1
        )

    styles, categories, ingredients = (
        count("styles"), count("categories"), count("ingredients")
    )
    return f"""<section class="ww-hero" aria-label="Explore the world of beer">
  <div class="ww-hero-eyebrow">AN OPEN ATLAS OF BREWING CULTURE</div>
  <div class="ww-hero-title">Every tradition has a story.</div>
  <p class="ww-hero-copy">Discover beer styles, regional practices and the ingredients behind them.
  Follow the evidence, compare the traditions, and find your next rabbit hole.</p>
  <div class="ww-hero-actions">
    <a class="ww-hero-button ww-hero-button-primary" href="styles/">Browse beer profiles</a>
    <a class="ww-hero-button" href="navigation/">Find a reading path</a>
  </div>
  <div class="ww-hero-stats" aria-label="Wiki coverage">
    <a href="styles/"><strong>{styles}</strong><span>Profiles & traditions</span></a>
    <a href="categories/"><strong>{categories}</strong><span>Category guides</span></a>
    <a href="ingredients/"><strong>{ingredients}</strong><span>Ingredient references</span></a>
  </div>
</section>"""


def subtree(folder, pages, docs, alphabetical=False):
    """Build section navigation from actual files, never from a fixed page list."""
    prefix = PurePosixPath(folder)
    direct = [p for p in pages if p.parent == prefix]
    index = next((p for p in direct if p.name.lower() == "index.md"), None)
    result = [{"Overview": index.as_posix()}] if index else []
    others = sorted(
        (p for p in direct if p != index),
        key=lambda p: (page_title(docs / p.as_posix()).casefold(), p.as_posix()),
    )

    if alphabetical:
        letters = defaultdict(list)
        for path in others:
            name = page_title(docs / path.as_posix())
            initial = name[0].upper() if name and name[0].isalpha() else "#"
            letters[initial].append({name: path.as_posix()})
        result.extend({letter: letters[letter]} for letter in sorted(letters))
    else:
        result.extend(
            {page_title(docs / path.as_posix()): path.as_posix()}
            for path in others
        )

    children = sorted({
        p.parts[len(prefix.parts)]
        for p in pages
        if len(p.parts) > len(prefix.parts) + 1
        and p.parts[:len(prefix.parts)] == prefix.parts
    })
    for child in children:
        nested = subtree(f"{folder}/{child}", pages, docs)
        if nested:
            result.append({child.replace("-", " ").title(): nested})
    return result


def navigation(pages, docs):
    nav = [{"Home": "index.md"}] if PurePosixPath("index.md") in pages else []
    for folder, label in TOP_LEVEL:
        items = subtree(folder, pages, docs, alphabetical=(folder == "styles"))
        if items:
            nav.append({label: items})

    research = []
    for folder, label in RESEARCH:
        items = subtree(folder, pages, docs)
        if items:
            research.append({label: items})
    for path, label in (("README.md", "Reading guide"), ("log.md", "Release log")):
        if PurePosixPath(path) in pages:
            research.append({label: path})

    known_roots = {"index.md", "README.md", "log.md"}
    for path in sorted(p for p in pages if len(p.parts) == 1):
        if path.name not in known_roots:
            research.append({page_title(docs / path.as_posix()): path.as_posix()})
    if research:
        nav.append({"Research & sources": research})

    known_dirs = {folder for folder, _ in TOP_LEVEL + RESEARCH}
    extra_dirs = sorted({
        p.parts[0] for p in pages
        if len(p.parts) > 1 and p.parts[0] not in known_dirs
    })
    for folder in extra_dirs:
        items = subtree(folder, pages, docs)
        if items:
            nav.append({folder.replace("-", " ").title(): items})
    return nav


def build(root=ROOT):
    root = Path(root).resolve()
    output = root / ".build"
    docs = output / "docs"
    if docs.exists():
        shutil.rmtree(docs)
    docs.mkdir(parents=True)

    for relative, source in wiki_files(root):
        target = docs / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)

    # Keep the README maintenance-tool link valid on the published site.
    validator = root / "tools" / "validate_wiki.py"
    if validator.is_file():
        (docs / "tools").mkdir(parents=True, exist_ok=True)
        shutil.copy2(validator, docs / "tools" / "validate_wiki.py")

    assets = root / "website" / "assets"
    if assets.is_dir():
        shutil.copytree(assets, docs / "assets", dirs_exist_ok=True)

    pages = {PurePosixPath(p.relative_to(docs).as_posix()) for p in docs.rglob("*.md")}
    for path in pages:
        article = docs / path.as_posix()
        content = article.read_text(encoding="utf-8")
        if path == PurePosixPath("index.md"):
            content = insert_below_title(content, home_intro(pages))
        elif path.parts[0] in {"styles", "ingredients", "categories"}:
            content = article_chips(content)
        article.write_text(content, encoding="utf-8")

    config = yaml.safe_load((root / "mkdocs.yml").read_text(encoding="utf-8"))
    config["docs_dir"] = str(docs)
    config["site_dir"] = str(output / "site")
    config["nav"] = navigation(pages, docs)
    (output / "mkdocs.yml").write_text(
        yaml.safe_dump(config, allow_unicode=True, sort_keys=False, width=110),
        encoding="utf-8",
    )
    print(f"Staged {len(pages)} searchable pages in {docs}")


if __name__ == "__main__":
    build()
