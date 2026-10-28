#!/usr/bin/env python3
"""Validate the finished book, independently of the assembly/typesetting code.

Run after assemble.py and build_book.py. This deliberately reads the delivered
Markdown, ZIP/XML, image pixels, PDF objects and extracted text; it never imports
the production scripts or treats a successful build as proof of a valid book.
EPUBCheck and visual inspection remain separate, complementary release gates.

Dependencies: Python standard library, pypdf and Pillow (requirements.txt).
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import html
import io
import json
from pathlib import Path
import posixpath
import re
import unicodedata
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET
from zipfile import ZIP_STORED, ZipFile

from PIL import Image
from pypdf import PdfReader
from pypdf.generic import ContentStream, IndirectObject


ROOT = Path(__file__).resolve().parents[1]
XHTML = "http://www.w3.org/1999/xhtml"
EPUB = "http://www.idpf.org/2007/ops"
OPF = "http://www.idpf.org/2007/opf"
DC = "http://purl.org/dc/elements/1.1/"
WORD = re.compile(r"\b\w+(?:[’'-]\w+)*\b")


@dataclass
class Section:
    level: int
    title: str
    anchor: str
    start: int
    content_start: int
    end: int
    body: str = ""


@dataclass
class Link:
    start: int
    end: int
    label: str
    target: str


class Report:
    def __init__(self, root: Path):
        self.root = root
        self.checks = []
        self.artifacts = {}

    def add(self, identifier, passed, summary, **details):
        self.checks.append({"id": identifier, "status": "pass" if passed else "fail",
                            "summary": summary, **details})

    def warning(self, identifier, summary, **details):
        self.checks.append({"id": identifier, "status": "warning",
                            "summary": summary, **details})

    def exception(self, identifier, exc):
        self.add(identifier, False, f"Validation could not complete: {type(exc).__name__}: {exc}")

    def fingerprint(self, relative):
        path = self.root / relative
        if not path.is_file():
            self.add(f"file:{relative}", False, "Required deliverable is missing.")
            return None
        data = path.read_bytes()
        result = {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
        self.artifacts[relative] = result
        self.add(f"file:{relative}", True, "Deliverable exists and is readable.", **result)
        return result

    def result(self):
        counts = Counter(item["status"] for item in self.checks)
        return {
            "schema_version": 1,
            "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "book": "The Beer Detective",
            "validator": "tools/validate_book.py",
            "passed": not counts["fail"],
            "totals": dict(counts),
            "artifacts": self.artifacts,
            "checks": self.checks,
            "limits": [
                "This is an artifact-level technical check, not a judgment of historical or scientific truth.",
                "EPUB standards conformance is checked separately with EPUBCheck; this script checks actual packaged targets and reading order.",
                "PDF paragraph presence is sampled at the beginning, middle and end of every narrative and note paragraph; it is not a pixel-level proof of rendering.",
                "PDF font checks inspect fonts used by text-show operators, including Form XObjects, rather than failing unused fallback resources.",
                "Embedding checks do not substitute for visual inspection of glyph shapes, line breaks, color, typography, margins or cover composition.",
                "External URLs are checked for preservation in the deliverables, not for continued network availability.",
                "Recorded build hashes prove consistency of the files and manifests inspected; they do not independently establish build authorship or historical provenance.",
            ],
        }


def deref(value):
    return value.get_object() if isinstance(value, IndirectObject) else value


def md_links(text):
    """Read inline Markdown destinations, including balanced parentheses in URLs."""
    result = []
    i = 0
    while i < len(text):
        if text[i] != "[" or (i and text[i - 1] == "\\"):
            i += 1
            continue
        start = i
        depth = 1
        j = i + 1
        while j < len(text) and depth:
            if text[j] == "\\":
                j += 2
                continue
            if text[j] == "[":
                depth += 1
            elif text[j] == "]":
                depth -= 1
            j += 1
        if depth or j >= len(text) or text[j] != "(":
            i += 1
            continue
        label = text[start + 1:j - 1]
        k, depth = j + 1, 1
        while k < len(text) and depth:
            if text[k] == "\\":
                k += 2
                continue
            if text[k] == "(":
                depth += 1
            elif text[k] == ")":
                depth -= 1
            k += 1
        if depth:
            i += 1
            continue
        target = text[j + 1:k - 1].strip()
        if target.startswith("<") and ">" in target:
            target = target[1:target.index(">")]
        else:
            target = re.sub(r'\s+["\'].*["\']$', "", target)
        result.append(Link(start, k, label, html.unescape(target)))
        i = k
    return result


def plain_markdown(text):
    text = re.sub(r"^#{1,6}\s+.*$", "", text, flags=re.M)
    text = re.sub(r"\[\]\{#[^}]+\}", "", text)
    text = re.sub(r"\^\[\d+\]\(#note-[^)]+\)\^", "", text)
    for link in reversed(md_links(text)):
        text = text[:link.start] + link.label + text[link.end:]
    text = re.sub(r"\{[.#][^}\n]*\}", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\\([\\`*_{}\[\]()#+.!-])", r"\1", text)
    return html.unescape(text.replace("`", "").replace("*", ""))


def letters(text):
    """Ignore punctuation, layout whitespace, ligatures and note-call digits."""
    return "".join(c for c in unicodedata.normalize("NFKC", text).casefold() if c.isalpha())


def letters_and_numbers(text):
    return "".join(c for c in unicodedata.normalize("NFKC", text).casefold() if c.isalnum())


def epub_visible_text(element):
    """Omit superscript citation labels while retaining dates and quantities."""
    if (element.tag == f"{{{XHTML}}}a"
            and urlsplit(element.get("href", "")).fragment.startswith("note-")):
        return ""
    result = [element.text or ""]
    for child in element:
        result.append(epub_visible_text(child))
        result.append(child.tail or "")
    return "".join(result)


def token_count(text):
    return len(WORD.findall(plain_markdown(text)))


def sections_of(text):
    sections = []
    for match in re.finditer(r"^(#{1,6})\s+([^\n]+)$", text, re.M):
        title = match[2]
        attr = re.search(r"\s+\{([^}\n]+)\}\s*$", title)
        anchor = ""
        if attr:
            ident = re.search(r"(?:^|\s)#([^\s}]+)", attr[1])
            anchor = ident[1] if ident else ""
            title = title[:attr.start()]
        sections.append(Section(len(match[1]), title, anchor, match.start(), match.end(), len(text)))
    for index, section in enumerate(sections):
        for later in sections[index + 1:]:
            if later.level <= section.level:
                section.end = later.start
                break
        section.body = text[section.content_start:section.end].strip()
    return sections


def owner_at(sections, position):
    options = [s for s in sections if s.start <= position < s.end]
    return max(options, key=lambda s: s.start).anchor if options else ""


def load_json(report, relative):
    if not report.fingerprint(relative):
        return {}
    try:
        value = json.loads((report.root / relative).read_text(encoding="utf-8"))
        report.add(f"json:{relative}", isinstance(value, dict), "Manifest parses as a JSON object.")
        return value if isinstance(value, dict) else {}
    except (ValueError, OSError) as exc:
        report.exception(f"json:{relative}", exc)
        return {}


def inspect_master(report, manifest):
    relative = "the-beer-detective.md"
    if not report.fingerprint(relative):
        return None
    text = (report.root / relative).read_text(encoding="utf-8")
    sections = sections_of(text)
    by_id = {s.anchor: s for s in sections if s.anchor}
    anchors = re.findall(r"\{[^}\n]*#([^\s}]+)[^}\n]*\}", text)
    duplicates = [key for key, count in Counter(anchors).items() if count > 1]
    report.add("master.unique-anchors", not duplicates, "Every explicit Markdown anchor is unique.", duplicates=duplicates)
    chapter_sections = [s for s in sections if re.fullmatch(r"chapter-\d\d", s.anchor)]
    expected_ids = [f"chapter-{n:02d}" for n in range(1, 25)]
    actual_ids = [s.anchor for s in chapter_sections]
    bad_titles = [s.title for n, s in enumerate(chapter_sections, 1) if not re.match(rf"{n}\.\s+\S", s.title)]
    report.add("master.24-complete-chapters", actual_ids == expected_ids and not bad_titles,
               "There are 24 distinct chapters, numbered and ordered 1–24.",
               chapter_ids=actual_ids, invalid_titles=bad_titles)
    required = ["title-page", "edition", "contents", "introduction", "afterword", "acknowledgments", "research-note", "notes", "further-reading"]
    missing = [key for key in required if key not in by_id]
    part_ids = [s.anchor for s in sections if re.fullmatch(r"part-[ivx]+", s.anchor)]
    report.add("master.required-structure", not missing and len(part_ids) in (3, 4),
               "Front matter, three or four parts, afterword, acknowledgments, research note, notes and reading list are present.",
               missing=missing, parts=part_ids)
    links = md_links(text)
    bad_links = []
    for link in links:
        target = urlsplit(link.target)
        if target.scheme or target.netloc:
            continue
        if not target.path:
            if target.fragment and unquote(target.fragment) not in anchors:
                bad_links.append({"target": link.target, "reason": "missing master fragment"})
        else:
            path = report.root / unquote(target.path)
            if not path.is_file():
                bad_links.append({"target": link.target, "reason": "missing local file"})
            else:
                bad_links.append({"target": link.target, "reason": "nonportable local resource in release manuscript"})
    report.add("master.portable-links", not bad_links, "Internal fragments resolve and source links are portable external URLs.",
               checked=len(links), errors=bad_links)
    unresolved = re.findall(r"\[\^[^\]]+\]", text)
    report.add("master.no-unresolved-footnotes", not unresolved, "No working-copy footnote syntax remains in the release manuscript.", unresolved=unresolved)
    narrative_sections = [s for s in sections if s.anchor in {"introduction", "afterword"} or s.anchor in expected_ids]
    counts = {s.anchor: token_count(s.body) for s in narrative_sections}
    total = sum(counts.values())
    report.add("master.narrative-length", 35000 <= total <= 50000 and len(counts) == 26,
               "Independent narrative count excludes headings, notes, bibliography and other non-narrative matter.",
               narrative_words=total, accepted_range=[35000, 50000], section_words=counts)
    differences = []
    if manifest.get("narrative_words") != total:
        differences.append({"field": "narrative_words", "manifest": manifest.get("narrative_words"), "actual": total})
    for item in manifest.get("chapters", []):
        key = f"chapter-{int(item['chapter']):02d}"
        if item.get("narrative_words") != counts.get(key):
            differences.append({"field": key, "manifest": item.get("narrative_words"), "actual": counts.get(key)})
    report.add("master.word-count-manifest", not differences and manifest.get("chapter_count") == 24,
               "Recorded manuscript counts agree with the finished master.", differences=differences)
    note_calls = []
    pattern = re.compile(r"\[\]\{#(ref-[^}]+)\}\^\[(\d+)\]\(#(note-[^)]+)\)\^")
    for match in pattern.finditer(text):
        note_calls.append({"reference": match[1], "number": int(match[2]), "target": match[3],
                           "section": owner_at(sections, match.start()), "position": match.start()})
    note_entries = []
    entries = list(re.finditer(r"^(\d+)\.\s+\[\]\{#(note-[^}]+)\}", text, re.M))
    for index, match in enumerate(entries):
        end = entries[index + 1].start() if index + 1 < len(entries) else len(text)
        for section in sections:
            if match.start() < section.start < end:
                end = section.start
                break
        body = text[match.end():end].strip()
        note_entries.append({"id": match[2], "number": int(match[1]), "section": owner_at(sections, match.start()),
                             "body": body, "backlinks": [x.target[1:] for x in md_links(body) if x.target.startswith("#ref-")]})
    call_by_ref = {c["reference"]: c for c in note_calls}
    notes_by_id = {n["id"]: n for n in note_entries}
    errors = []
    counts_by_group = defaultdict(list)
    for note in note_entries:
        counts_by_group[note["section"]].append(note["number"])
        match = re.fullmatch(r"note-(c(\d\d)|intro)-(\d+)", note["id"])
        expected_group = f"notes-{match[2]}" if match and match[2] else "notes-intro"
        if not match or note["section"] != expected_group:
            errors.append({"note": note["id"], "reason": "note is outside its chapter-local group"})
        calls = [c for c in note_calls if c["target"] == note["id"]]
        if not calls:
            errors.append({"note": note["id"], "reason": "note is never cited"})
        if Counter(note["backlinks"]) != Counter(c["reference"] for c in calls):
            errors.append({"note": note["id"], "reason": "backlinks do not cover each call exactly once",
                           "calls": [c["reference"] for c in calls], "backlinks": note["backlinks"]})
        for backlink in note["backlinks"]:
            if backlink not in call_by_ref or call_by_ref[backlink]["target"] != note["id"]:
                errors.append({"note": note["id"], "reason": "backlink points to a different or missing citation", "target": backlink})
    for group, numbers in counts_by_group.items():
        if numbers != list(range(1, len(numbers) + 1)):
            errors.append({"group": group, "reason": "note numbers do not restart at 1 and increase without gaps", "numbers": numbers})
    for call in note_calls:
        note = notes_by_id.get(call["target"])
        expected = "introduction" if call["target"].startswith("note-intro-") else "chapter-" + call["target"][6:8]
        if note is None or note["number"] != call["number"] or call["section"] != expected:
            errors.append({"reference": call["reference"], "reason": "citation label, chapter or note target mismatch"})
    expected_groups = {"notes-intro", *[f"notes-{n:02d}" for n in range(1, 25)]}
    if set(counts_by_group) != expected_groups:
        errors.append({"reason": "missing or unexpected chapter note groups", "groups": sorted(counts_by_group)})
    found_ref_ids = {a for a in anchors if a.startswith("ref-")}
    found_note_ids = {a for a in anchors if a.startswith("note-")}
    if found_ref_ids != set(call_by_ref) or found_note_ids != set(notes_by_id):
        errors.append({"reason": "unparsed or unmatched note/call anchor"})
    if len(note_entries) != manifest.get("notes"):
        errors.append({"reason": "manifest note count mismatch", "actual": len(note_entries), "manifest": manifest.get("notes")})
    report.add("master.chapter-local-notes", not errors,
               "Every citation resolves to its correctly numbered chapter note, with an individual backlink to every occurrence.",
               notes=len(note_entries), calls=len(note_calls), note_groups=len(counts_by_group), errors=errors)
    paragraphs = []
    for section in narrative_sections:
        for index, paragraph in enumerate(re.split(r"\n\s*\n", section.body), 1):
            value = plain_markdown(paragraph).strip()
            if len(letters(value)) >= 30:
                paragraphs.append({"section": section.anchor, "paragraph": index, "text": value})
    for index, note in enumerate(note_entries, 1):
        paragraphs.append({"section": note["id"], "paragraph": index, "text": plain_markdown(note["body"])})
    return {"text": text, "sections": sections, "by_id": by_id, "chapters": chapter_sections,
            "links": links, "anchors": anchors, "calls": note_calls, "notes": note_entries,
            "paragraphs": paragraphs, "narrative_words": total}


def inspect_cover(report):
    if report.fingerprint("design/cover.png"):
        try:
            with Image.open(report.root / "design/cover.png") as image:
                size, mode, image_format = image.size, image.mode, image.format
                image.verify()
            with Image.open(report.root / "design/cover.png") as image:
                image.load()
            report.add("cover.raster", size == (1800, 2700) and image_format == "PNG",
                       "Final cover decodes and measures 1800 × 2700 pixels.", size=list(size), mode=mode, format=image_format)
        except Exception as exc:
            report.exception("cover.raster", exc)
    if report.fingerprint("design/cover.svg"):
        try:
            svg = ET.parse(report.root / "design/cover.svg").getroot()
            texts = ["".join(e.itertext()) for e in svg.iter() if e.tag.rsplit("}", 1)[-1] == "text"]
            report.add("cover.editable-vector", svg.tag.endswith("}svg") and bool(texts),
                       "The editable source contains vector artwork and editable text.", text_objects=len(texts), view_box=svg.get("viewBox"))
        except Exception as exc:
            report.exception("cover.editable-vector", exc)
    if report.fingerprint("design/cover-print.pdf"):
        try:
            reader = PdfReader(report.root / "design/cover-print.pdf")
            size = (float(reader.pages[0].mediabox.width), float(reader.pages[0].mediabox.height))
            report.add("cover.print-size", len(reader.pages) == 1 and all(abs(a - b) < .5 for a, b in zip(size, (432, 648))),
                       "The print front cover is one 6 × 9 inch page.", points=list(size))
        except Exception as exc:
            report.exception("cover.print-size", exc)


def resolve_epub(base, target):
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None
    path = unquote(parsed.path)
    resolved = posixpath.normpath(posixpath.join(posixpath.dirname(base), path)) if path else base
    return resolved, unquote(parsed.fragment)


def xml_id(element):
    return element.get("id") or element.get("{http://www.w3.org/XML/1998/namespace}id")


def inspect_epub(report, master, manifest):
    relative = "dist/the-beer-detective.epub"
    if not report.fingerprint(relative):
        return
    with ZipFile(report.root / relative) as archive:
        files = archive.namelist()
        data = {name: archive.read(name) for name in files}
        first = archive.infolist()[0]
        report.add("epub.container-mimetype", first.filename == "mimetype" and first.compress_type == ZIP_STORED
                   and data.get("mimetype") == b"application/epub+zip" and len(files) == len(set(files)),
                   "EPUB mimetype is the first uncompressed ZIP entry, and package paths are unique.")
        container = ET.fromstring(data["META-INF/container.xml"])
        roots = container.findall(".//{urn:oasis:names:tc:opendocument:xmlns:container}rootfile")
        root_paths = [r.get("full-path") for r in roots]
        report.add("epub.rootfile", len(root_paths) == 1 and root_paths[0] in data,
                   "The container identifies exactly one existing package document.", rootfiles=root_paths)
        opf_path = root_paths[0]
        package = ET.fromstring(data[opf_path])
        items = package.findall(f"{{{OPF}}}manifest/{{{OPF}}}item")
        item_by_id = {item.get("id"): item for item in items}
        item_paths = {item.get("id"): resolve_epub(opf_path, item.get("href", ""))[0] for item in items}
        manifest_errors = []
        for item in items:
            name = item_paths[item.get("id")]
            if name not in data or not item.get("media-type"):
                manifest_errors.append({"id": item.get("id"), "path": name, "reason": "missing file or media type"})
        if len(item_by_id) != len(items) or len(set(item_paths.values())) != len(items):
            manifest_errors.append({"reason": "duplicate manifest ID or resource path"})
        report.add("epub.manifest-resources", not manifest_errors, "All manifest resources exist with unique IDs and paths.",
                   resources=len(items), errors=manifest_errors)
        documents = {}
        id_sets = {}
        parse_errors = []
        for name, raw in data.items():
            if name.endswith((".xhtml", ".html", ".svg", ".ncx", ".opf")):
                try:
                    doc = ET.fromstring(raw)
                    documents[name] = doc
                    identities = [xml_id(e) for e in doc.iter() if xml_id(e)]
                    id_sets[name] = set(identities)
                    dupes = [key for key, count in Counter(identities).items() if count > 1]
                    if dupes:
                        parse_errors.append({"file": name, "reason": "duplicate XML IDs", "ids": dupes})
                except ET.ParseError as exc:
                    parse_errors.append({"file": name, "reason": str(exc)})
        report.add("epub.well-formed-documents", not parse_errors, "Packaged XHTML, SVG, NCX and OPF parse with unique per-document IDs.",
                   documents=len(documents), errors=parse_errors)
        local_errors = []
        local_count = 0
        all_links = []
        def check_target(base, target, kind):
            nonlocal local_count
            resolved = resolve_epub(base, target)
            if resolved is None:
                return
            local_count += 1
            path, fragment = resolved
            if path.startswith(("/", "../")) or path not in data:
                local_errors.append({"file": base, "target": target, "kind": kind, "reason": "missing or out-of-package resource"})
            elif fragment and fragment not in id_sets.get(path, set()):
                local_errors.append({"file": base, "target": target, "kind": kind, "reason": "missing target fragment"})
        for name, doc in documents.items():
            for element in doc.iter():
                for attr, target in element.attrib.items():
                    kind = attr.rsplit("}", 1)[-1]
                    if kind in {"href", "src", "poster", "data"}:
                        check_target(name, target, kind)
                        if element.tag.rsplit("}", 1)[-1] == "a" and kind == "href":
                            all_links.append((name, element, target))
                style = element.get("style", "")
                if element.tag.rsplit("}", 1)[-1] == "style":
                    style += element.text or ""
                for target in re.findall(r"url\(\s*['\"]?([^)'\"]+)['\"]?\s*\)", style):
                    check_target(name, target.strip(), "inline CSS url")
        for name, raw in data.items():
            if name.endswith(".css"):
                for target in re.findall(r"url\(\s*['\"]?([^)'\"]+)['\"]?\s*\)", raw.decode("utf-8")):
                    check_target(name, target.strip(), "CSS url")
        report.add("epub.all-local-targets", not local_errors, "Every local href/src, image reference and CSS URL resolves, including fragments.",
                   checked=local_count, errors=local_errors)
        spine_items = package.findall(f"{{{OPF}}}spine/{{{OPF}}}itemref")
        spine_ids = [item.get("idref") for item in spine_items]
        spine_errors = []
        spine_paths = []
        for item in spine_items:
            key = item.get("idref")
            if key not in item_by_id or item_by_id[key].get("media-type") != "application/xhtml+xml":
                spine_errors.append({"idref": key, "reason": "missing or non-XHTML spine item"})
            else:
                spine_paths.append(item_paths[key])
        if len(spine_ids) != len(set(spine_ids)):
            spine_errors.append({"reason": "duplicate spine item"})
        chapter_locations = {}
        for path in spine_paths:
            for anchor in id_sets.get(path, set()):
                if re.fullmatch(r"chapter-\d\d", anchor):
                    if anchor in chapter_locations:
                        spine_errors.append({"chapter": anchor, "reason": "chapter repeated in reading order"})
                    chapter_locations[anchor] = path
        chapter_order = [anchor for path in spine_paths for anchor in sorted(id_sets.get(path, set())) if re.fullmatch(r"chapter-\d\d", anchor)]
        if chapter_order != [f"chapter-{n:02d}" for n in range(1, 25)]:
            spine_errors.append({"reason": "reading order does not contain all 24 chapters in order", "chapters": chapter_order})
        report.add("epub.spine", not spine_errors, "The spine contains readable XHTML and all 24 chapters once, in sequence.",
                   reading_documents=len(spine_paths), errors=spine_errors)
        nav_items = [item for item in items if "nav" in item.get("properties", "").split()]
        nav_errors = []
        nav_chapters = []
        if len(nav_items) != 1:
            nav_errors.append({"reason": "expected exactly one EPUB navigation document"})
        else:
            nav_path = item_paths[nav_items[0].get("id")]
            nav = documents.get(nav_path)
            tocs = [e for e in nav.iter() if e.tag == f"{{{XHTML}}}nav" and "toc" in e.get(f"{{{EPUB}}}type", "").split()] if nav is not None else []
            if len(tocs) != 1:
                nav_errors.append({"reason": "expected one EPUB table-of-contents nav"})
            else:
                for anchor in tocs[0].iter(f"{{{XHTML}}}a"):
                    target = resolve_epub(nav_path, anchor.get("href", ""))
                    if not target:
                        continue
                    path, fragment = target
                    for chapter, chapter_path in chapter_locations.items():
                        if path == chapter_path and (not fragment or fragment == chapter):
                            nav_chapters.append(chapter)
                if nav_chapters != [f"chapter-{n:02d}" for n in range(1, 25)]:
                    nav_errors.append({"reason": "TOC does not link every chapter exactly once in sequence", "chapters": nav_chapters})
        report.add("epub.navigation", not nav_errors, "EPUB navigation reaches every chapter in the actual reading order.", errors=nav_errors)
        metadata = package.find(f"{{{OPF}}}metadata")
        values = {name: [e.text or "" for e in metadata.findall(f"{{{DC}}}{name}")] for name in ["title", "creator", "language", "identifier", "rights", "description"]}
        unique = package.get("unique-identifier")
        identifier_ok = any(e.get("id") == unique and (e.text or "").strip() for e in metadata.findall(f"{{{DC}}}identifier"))
        modified = [e.text or "" for e in metadata.findall(f"{{{OPF}}}meta") if e.get("property") == "dcterms:modified"]
        fixed_layout = [e.text for e in metadata.findall(f"{{{OPF}}}meta") if e.get("property") == "rendition:layout" and e.text == "pre-paginated"]
        fixed_layout += [i.get("properties") for i in spine_items if "rendition:layout-pre-paginated" in i.get("properties", "").split()]
        metadata_ok = (package.get("version", "").startswith("3") and identifier_ok and all(any(v.strip() for v in vals) for vals in values.values())
                       and any(letters(v) == letters(manifest.get("title", "")) for v in values["title"])
                       and any(letters(v) == letters(manifest.get("attribution", "")) for v in values["creator"])
                       and len(modified) == 1 and bool(re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", modified[0])) and not fixed_layout)
        report.add("epub.metadata-reflow", metadata_ok, "EPUB 3 metadata identifies the book, language, creator, rights and modification time, without fixed-layout settings.",
                   metadata=values, modified=modified, fixed_layout=fixed_layout)
        covers = [item for item in items if "cover-image" in item.get("properties", "").split()]
        cover_ok = len(covers) == 1
        cover_details = {}
        if cover_ok:
            cover_path = item_paths[covers[0].get("id")]
            with Image.open(io.BytesIO(data[cover_path])) as image:
                image.load()
                cover_details = {"path": cover_path, "size": list(image.size), "format": image.format}
                cover_ok = image.size == (1800, 2700)
            source_cover = report.root / "design/cover.png"
            cover_ok = cover_ok and source_cover.is_file() and data[cover_path] == source_cover.read_bytes()
            cover_docs = []
            for path in spine_paths:
                doc = documents.get(path)
                if doc is None:
                    continue
                if any(resolve_epub(path, target) == (cover_path, "") for e in doc.iter() for attr, target in e.attrib.items() if attr.rsplit("}", 1)[-1] in {"src", "href"}):
                    cover_docs.append(path)
            cover_details["spine_documents"] = cover_docs
            cover_ok = cover_ok and len(cover_docs) == 1 and spine_paths[0] in cover_docs
        report.add("epub.cover", cover_ok, "The actual 1800 × 2700 final cover is declared and displayed first in the spine.", **cover_details)
        fonts = [item_paths[i.get("id")] for i in items if "font" in i.get("media-type", "") or item_paths[i.get("id")].endswith((".ttf", ".otf", ".woff", ".woff2"))]
        font_ok = len(fonts) >= 4 and all(len(data.get(name, b"")) > 1000 for name in fonts)
        report.add("epub.embedded-fonts", font_ok, "Body, italic, bold and display font resources are embedded and nonempty.", fonts=fonts)
        if master:
            anchor_locations = defaultdict(list)
            for path in spine_paths:
                for anchor in id_sets.get(path, set()):
                    anchor_locations[anchor].append(path)
            missing = [anchor for anchor in master["anchors"] if len(anchor_locations.get(anchor, [])) != 1]
            report.add("epub.master-anchors", not missing, "Every master anchor appears exactly once in the EPUB spine.", errors=missing)
            expected_edges = Counter((c["reference"], c["target"]) for c in master["calls"])
            expected_returns = Counter((n["id"], back) for n in master["notes"] for back in n["backlinks"])
            seen_edges, seen_returns = Counter(), Counter()
            for path in spine_paths:
                doc = documents.get(path)
                if doc is None:
                    continue
                parents = {child: parent for parent in doc.iter() for child in parent}
                for element in doc.iter(f"{{{XHTML}}}a"):
                    resolved = resolve_epub(path, element.get("href", ""))
                    if not resolved:
                        continue
                    _, fragment = resolved
                    if fragment.startswith("note-"):
                        ancestor = parents.get(element)
                        while ancestor is not None and ancestor.tag.rsplit("}", 1)[-1] not in {"p", "li"}:
                            ancestor = parents.get(ancestor)
                        if ancestor is not None:
                            nodes = list(ancestor.iter())
                            index = nodes.index(element)
                            references = [xml_id(e) for e in nodes[:index] if (xml_id(e) or "").startswith("ref-")]
                            if references:
                                seen_edges[(references[-1], fragment)] += 1
                    elif fragment.startswith("ref-"):
                        ancestor = parents.get(element)
                        while ancestor is not None and ancestor.tag.rsplit("}", 1)[-1] != "li":
                            ancestor = parents.get(ancestor)
                        if ancestor is not None:
                            notes = [xml_id(e) for e in ancestor.iter() if (xml_id(e) or "").startswith("note-")]
                            if len(notes) == 1:
                                seen_returns[(notes[0], fragment)] += 1
            edge_errors = {"missing_calls": list((expected_edges - seen_edges).elements()), "unexpected_calls": list((seen_edges - expected_edges).elements()),
                           "missing_returns": list((expected_returns - seen_returns).elements()), "unexpected_returns": list((seen_returns - expected_returns).elements())}
            report.add("epub.note-links-and-backlinks", not any(edge_errors.values()), "Every master note-call and individual return link survives EPUB conversion.",
                       calls=sum(seen_edges.values()), backlinks=sum(seen_returns.values()), **edge_errors)
            all_text = letters_and_numbers(" ".join(epub_visible_text(doc) for path in spine_paths if (doc := documents.get(path)) is not None))
            missing_paragraphs = [{"section": p["section"], "paragraph": p["paragraph"]} for p in master["paragraphs"] if letters_and_numbers(p["text"]) not in all_text]
            report.add("epub.complete-narrative-and-notes", not missing_paragraphs,
                       "Every narrative and note paragraph, including its dates and quantities, occurs in spine content after removing citation labels and normalizing punctuation.",
                       paragraphs=len(master["paragraphs"]), missing=missing_paragraphs)
            expected_urls = {link.target for link in master["links"] if urlsplit(link.target).scheme in {"http", "https"}}
            actual_urls = {target for _, _, target in all_links if urlsplit(target).scheme in {"http", "https"}}
            report.add("epub.external-source-links", not expected_urls - actual_urls,
                       "All external reference URLs in the master remain clickable in the EPUB.", expected=len(expected_urls), missing=sorted(expected_urls - actual_urls))


def flatten_outline(outline):
    for item in outline:
        if isinstance(item, list):
            yield from flatten_outline(item)
        else:
            yield item


def font_embedding(font):
    font = deref(font)
    if font.get("/Subtype") == "/Type3":
        return bool(deref(font.get("/CharProcs"))), "Type 3 glyph programs"
    descriptors = []
    if font.get("/FontDescriptor"):
        descriptors.append(deref(font["/FontDescriptor"]))
    for descendant in deref(font.get("/DescendantFonts", [])):
        child = deref(descendant)
        if child.get("/FontDescriptor"):
            descriptors.append(deref(child["/FontDescriptor"]))
    embedded = []
    for descriptor in descriptors:
        for name in ["/FontFile", "/FontFile2", "/FontFile3"]:
            if descriptor.get(name):
                stream = deref(descriptor[name])
                embedded.append({"kind": name, "bytes": len(stream.get_data())})
    return bool(embedded) and all(x["bytes"] for x in embedded), embedded


def actual_font_usage(reader):
    usage = {}
    unresolved = []
    def walk(stream, resources, page_number, inherited=None, active=()):
        if stream is None:
            return
        resources = deref(resources) or {}
        font = inherited
        stack = []
        content = ContentStream(stream, reader)
        for operands, operator in content.operations:
            if operator == b"q":
                stack.append(font)
            elif operator == b"Q":
                font = stack.pop() if stack else inherited
            elif operator == b"Tf":
                font = operands[0]
            elif operator in {b"Tj", b"TJ", b"'", b'"'}:
                objects = operands[-1] if operator == b"TJ" else [operands[-1]]
                visible = sum(len(value) for value in objects if isinstance(value, (str, bytes)))
                if not visible:
                    continue
                available = deref(resources.get("/Font", {}))
                if font not in available:
                    unresolved.append({"page": page_number, "resource": str(font)})
                    continue
                reference = available[font]
                resolved = deref(reference)
                key = (reference.idnum, reference.generation) if isinstance(reference, IndirectObject) else (id(resolved), 0)
                if key not in usage:
                    embedded, details = font_embedding(resolved)
                    usage[key] = {"base_font": str(resolved.get("/BaseFont", "")), "subtype": str(resolved.get("/Subtype", "")),
                                  "embedded": embedded, "embedding": details, "pages": set(), "text_operations": 0, "encoded_characters": 0}
                usage[key]["pages"].add(page_number)
                usage[key]["text_operations"] += 1
                usage[key]["encoded_characters"] += visible
            elif operator == b"Do":
                xobjects = deref(resources.get("/XObject", {}))
                reference = xobjects.get(operands[0])
                if reference is None:
                    continue
                obj = deref(reference)
                if obj.get("/Subtype") == "/Form":
                    key = (reference.idnum, reference.generation) if isinstance(reference, IndirectObject) else id(obj)
                    if key not in active:
                        walk(obj, obj.get("/Resources", resources), page_number, font, (*active, key))
    for number, page in enumerate(reader.pages, 1):
        walk(page.get_contents(), page.get("/Resources"), number)
    result = []
    for item in usage.values():
        pages = sorted(item.pop("pages"))
        item["first_page"] = pages[0]
        item["pages_used"] = len(pages)
        result.append(item)
    return sorted(result, key=lambda item: item["base_font"]), unresolved


def inspect_pdf(report, master, manuscript, build):
    relative = "dist/the-beer-detective.pdf"
    if not report.fingerprint(relative):
        return
    reader = PdfReader(report.root / relative)
    page_count = len(reader.pages)
    size_errors = []
    for number, page in enumerate(reader.pages, 1):
        for box_name in ("mediabox", "cropbox"):
            box = getattr(page, box_name)
            if abs(float(box.width) - 432) > .5 or abs(float(box.height) - 648) > .5:
                size_errors.append({"page": number, "box": box_name, "points": [float(box.width), float(box.height)]})
        if page.rotation % 360:
            size_errors.append({"page": number, "reason": "rotated page", "rotation": page.rotation})
    report.add("pdf.trim-and-pages", not size_errors and page_count == build.get("pdf", {}).get("pages"),
               "Every page has the 6 × 9 inch trim and the actual page count matches the build manifest.",
               pages=page_count, errors=size_errors)
    page_text = [page.extract_text() or "" for page in reader.pages]
    empty = [number for number, text in enumerate(page_text[1:], 2) if not text.strip()]
    report.add("pdf.extractable-text", not empty and sum(len(t) for t in page_text) > 100000,
               "All interior pages contain extractable text; the vector cover may contain outlined text.",
               characters=sum(len(t) for t in page_text), empty_interior_pages=empty)
    metadata = reader.metadata or {}
    report.add("pdf.metadata", letters(str(metadata.get("/Title", ""))) == letters(manuscript.get("title", ""))
               and letters(str(metadata.get("/Author", ""))) == letters(manuscript.get("attribution", "")),
               "PDF title and project attribution match the manuscript manifest.",
               title=str(metadata.get("/Title", "")), author=str(metadata.get("/Author", "")))
    outlines = list(flatten_outline(reader.outline))
    outline_details = []
    outline_errors = []
    for item in outlines:
        page = reader.get_destination_page_number(item)
        title = str(item.get("/Title", ""))
        outline_details.append({"title": title, "page": page + 1 if page is not None else None})
        if page is None or not 0 <= page < page_count:
            outline_errors.append({"title": title, "reason": "invalid destination"})
    outline_by_title = {letters(item["title"]): item["page"] for item in outline_details}
    section_pages = {}
    if master:
        required_sections = [s for s in master["sections"] if s.anchor in {"introduction", "afterword", "acknowledgments", "research-note", "notes", "further-reading"}
                             or s.anchor.startswith("part-") or re.fullmatch(r"chapter-\d\d", s.anchor)]
        for section in required_sections:
            page = outline_by_title.get(letters(section.title))
            if page is None:
                outline_errors.append({"section": section.anchor, "reason": "missing outline entry"})
            else:
                section_pages[section.anchor] = page
                recorded = build.get("pdf", {}).get("page_locations", {}).get(section.anchor)
                if page != recorded:
                    outline_errors.append({"section": section.anchor, "reason": "outline page differs from manifest", "actual": page, "manifest": recorded})
        chapter_pages = [section_pages.get(f"chapter-{n:02d}") for n in range(1, 25)]
        if any(p is None for p in chapter_pages) or chapter_pages != sorted(set(p for p in chapter_pages if p is not None)):
            outline_errors.append({"reason": "chapter bookmarks are missing, duplicate or out of order"})
    report.add("pdf.bookmarks", not outline_errors, "Bookmarks cover the introduction, all parts and chapters, and the closing material, with valid, correctly recorded pages.",
               bookmarks=len(outline_details), errors=outline_errors)
    if master:
        joined = letters(" ".join(page_text))
        missing_paragraphs = []
        for paragraph in master["paragraphs"]:
            value = letters(paragraph["text"])
            width = min(90, len(value))
            starts = sorted({0, max(0, (len(value) - width) // 2), max(0, len(value) - width)})
            probes = [value[start:start + width] for start in starts]
            present = sum(probe in joined for probe in probes)
            needed = min(2, len(probes))
            if present < needed:
                missing_paragraphs.append({"section": paragraph["section"], "paragraph": paragraph["paragraph"], "present": present, "probes": len(probes)})
        report.add("pdf.narrative-and-note-text", not missing_paragraphs,
                   "At least two of three text windows from each substantial narrative and note paragraph survive PDF extraction; short paragraphs are checked in full.",
                   paragraphs=len(master["paragraphs"]), missing=missing_paragraphs)
    fonts, unresolved_fonts = actual_font_usage(reader)
    report.add("pdf.actual-used-fonts-embedded", bool(fonts) and all(font["embedded"] for font in fonts) and not unresolved_fonts,
               "All fonts actually used to show text have embedded font programs, including fonts inside Form XObjects.",
               fonts=fonts, unresolved=unresolved_fonts)
    page_references = {}
    for index, page in enumerate(reader.pages, 1):
        reference = page.indirect_reference
        if reference:
            page_references[(reference.idnum, reference.generation)] = index
    named = reader.named_destinations
    def destination(value):
        value = deref(value)
        if isinstance(value, str):
            found = named.get(value) or named.get(value.lstrip("/"))
            if found is None:
                return None
            number = reader.get_destination_page_number(found)
            return {"page": number + 1, "key": (number + 1, "named", value)} if number is not None else None
        if isinstance(value, dict):
            return destination(value.get("/D"))
        if isinstance(value, (list, tuple)) and len(value) >= 2:
            reference = value[0]
            if isinstance(reference, IndirectObject):
                number = page_references.get((reference.idnum, reference.generation))
            elif isinstance(reference, int):
                number = reference + 1
            else:
                number = None
            if number is None or not 1 <= number <= page_count:
                return None
            def scalar(v):
                return round(float(v), 3) if isinstance(v, (int, float)) else str(v)
            return {"page": number, "key": (number, *[scalar(v) for v in value[1:]])}
        return None
    internal = []
    external = []
    link_errors = []
    for page_number, page in enumerate(reader.pages, 1):
        for reference in page.get("/Annots", []):
            annotation = deref(reference)
            if annotation.get("/Subtype") != "/Link":
                continue
            rectangle = [float(n) for n in annotation.get("/Rect", [])]
            if len(rectangle) != 4 or rectangle[0] < -1 or rectangle[1] < -1 or rectangle[2] > 433 or rectangle[3] > 649:
                link_errors.append({"page": page_number, "reason": "link rectangle outside page", "rect": rectangle})
            action = deref(annotation.get("/A", {}))
            if action.get("/S") == "/URI":
                target = str(action.get("/URI", ""))
                external.append(target)
                if urlsplit(target).scheme not in {"https", "http", "mailto"}:
                    link_errors.append({"page": page_number, "reason": "nonportable external action", "target": target})
            else:
                target = annotation.get("/Dest") or (action.get("/D") if action.get("/S") == "/GoTo" else None)
                resolved = destination(target)
                if resolved is None:
                    link_errors.append({"page": page_number, "reason": "unresolved internal destination"})
                else:
                    internal.append({"page": page_number, "rect": rectangle, "destination": resolved})
    report.add("pdf.all-link-destinations", not link_errors, "All PDF link annotations have valid in-document destinations or portable external URLs and usable page rectangles.",
               internal=len(internal), external_annotations=len(external), errors=link_errors)
    if master:
        expected_urls = {link.target for link in master["links"] if urlsplit(link.target).scheme in {"http", "https"}}
        report.add("pdf.external-source-links", not expected_urls - set(external), "Every external master reference URL remains clickable in the PDF.",
                   expected=len(expected_urls), missing=sorted(expected_urls - set(external)))
        intro = section_pages.get("introduction")
        notes_start = section_pages.get("notes")
        reading_start = section_pages.get("further-reading")
        if intro and notes_start and reading_start:
            calls = [link for link in internal if intro <= link["page"] < notes_start and notes_start <= link["destination"]["page"] < reading_start]
            return_rectangles = [link for link in internal if notes_start <= link["page"] < reading_start and intro <= link["destination"]["page"] < notes_start]
            # A link that wraps across lines has one PDF annotation rectangle
            # per line. Consecutive rectangles to the same unique citation
            # destination are one logical return link, not duplicate links.
            returns = []
            for link in return_rectangles:
                if (returns and returns[-1]["destination"]["key"] == link["destination"]["key"]
                        and 0 <= link["page"] - returns[-1]["page"] <= 1):
                    continue
                returns.append(link)
            expected_returns = [(note, back) for note in master["notes"] for back in note["backlinks"]]
            note_errors = []
            if len(calls) != len(master["calls"]):
                note_errors.append({"reason": "PDF citation annotation count differs from master", "actual": len(calls), "expected": len(master["calls"])})
            if len(returns) != len(expected_returns):
                note_errors.append({"reason": "PDF return annotation count differs from master", "actual": len(returns), "expected": len(expected_returns)})
            ref_locations = {}
            note_destinations = defaultdict(set)
            for expected, actual in zip(master["calls"], calls):
                ref_locations[expected["reference"]] = actual
                note_destinations[expected["target"]].add(actual["destination"]["key"])
                source_start = section_pages.get(expected["section"], intro)
                later = sorted(p for p in section_pages.values() if p and p > source_start)
                source_end = later[0] if later else notes_start
                if not source_start <= actual["page"] < source_end:
                    note_errors.append({"reference": expected["reference"], "reason": "citation annotation occurs outside its chapter"})
            duplicates = [note for note, targets in note_destinations.items() if len(targets) != 1]
            if duplicates:
                note_errors.append({"reason": "repeated citations disagree about note destination", "notes": duplicates})
            all_note_positions = [next(iter(targets)) for targets in note_destinations.values() if len(targets) == 1]
            if len(set(all_note_positions)) != len(master["notes"]):
                note_errors.append({"reason": "notes do not have distinct, fully covered PDF destinations", "distinct": len(set(all_note_positions)), "expected": len(master["notes"])})
            ordered_positions = []
            for note in master["notes"]:
                targets = note_destinations.get(note["id"], set())
                if len(targets) == 1:
                    point = next(iter(targets))
                    if len(point) >= 4 and point[1] == "/XYZ":
                        ordered_positions.append((point[0], -point[3], point[2]))
            if ordered_positions != sorted(ordered_positions):
                note_errors.append({"reason": "note destinations are not in the master's note order on the PDF pages"})
            for (note, ref), actual in zip(expected_returns, returns):
                reference = ref_locations.get(ref)
                note_positions = note_destinations.get(note["id"], set())
                if reference is None or actual["destination"]["page"] != reference["page"]:
                    note_errors.append({"reference": ref, "reason": "return link lands on the wrong citation page"})
                elif len(actual["destination"]["key"]) >= 4 and actual["destination"]["key"][1] == "/XYZ":
                    point = actual["destination"]["key"]
                    if abs(point[2] - reference["rect"][0]) > 1 or abs(point[3] - reference["rect"][3]) > 1:
                        note_errors.append({"reference": ref, "reason": "return link lands away from the citation's actual rectangle", "destination": point, "citation_rect": reference["rect"]})
                if note_positions and actual["page"] not in {position[0] for position in note_positions}:
                    # A long note can wrap onto the following page before its return links.
                    if actual["page"] not in {position[0] + 1 for position in note_positions}:
                        note_errors.append({"note": note["id"], "reason": "return link is not on its note's page or continuation"})
            report.add("pdf.note-calls-and-backlinks", not note_errors,
                       "Citation and return annotations match the master's complete note network, chapter locations and distinct note destinations.",
                       calls=len(calls), backlinks=len(returns), backlink_annotation_rectangles=len(return_rectangles),
                       distinct_note_destinations=len(set(all_note_positions)), errors=note_errors)
            toc_links = [link for link in internal if link["page"] < intro]
            reached = {link["destination"]["page"] for link in toc_links}
            missing_toc = [key for key, page in section_pages.items() if page not in reached]
            report.add("pdf.table-of-contents-links", not missing_toc, "The PDF's front table of contents links to every bookmarked main section.", missing=missing_toc)
            labels = reader.page_labels
            report.add("pdf.page-labels", len(labels) == page_count and labels[0] == "Cover" and labels[intro - 1] == "1",
                       "PDF page labels distinguish the cover and front matter and begin Arabic page 1 at the introduction.",
                       first_labels=labels[:intro + 2], last_label=labels[-1])


def inspect_hashes(report, manuscript, build):
    errors = []
    master = report.artifacts.get("the-beer-detective.md", {}).get("sha256")
    for name, record in [("manuscript", manuscript), ("build", build)]:
        if not master or record.get("master_sha256") != master:
            errors.append({"manifest": name, "field": "master_sha256", "recorded": record.get("master_sha256"), "actual": master})
    for format_name in ("epub", "pdf"):
        actual = report.artifacts.get(f"dist/the-beer-detective.{format_name}", {})
        recorded = build.get(format_name, {})
        for field in ("bytes", "sha256"):
            if recorded.get(field) != actual.get(field) or field not in actual:
                errors.append({"format": format_name, "field": field, "recorded": recorded.get(field), "actual": actual.get(field)})
        if recorded.get("master_sha256") != master:
            errors.append({"format": format_name, "field": "master_sha256", "recorded": recorded.get("master_sha256"), "actual": master,
                           "reason": "each format needs its own current master hash to detect stale partial builds"})
    report.add("release.sha-coherence", not errors, "The actual master and both delivered formats match their hashes, sizes and per-format input-master hashes.", errors=errors)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--book-root", type=Path, default=ROOT)
    parser.add_argument("--report", type=Path, help="Defaults to BOOK_ROOT/research/validation-report.json")
    args = parser.parse_args()
    root = args.book_root.resolve()
    report = Report(root)
    manuscript = load_json(report, "research/manuscript-manifest.json")
    build = load_json(report, "research/build-manifest.json")
    master = None
    try:
        master = inspect_master(report, manuscript)
    except Exception as exc:
        report.exception("master.validation", exc)
    for identifier, work in [
        ("cover.validation", lambda: inspect_cover(report)),
        ("epub.validation", lambda: inspect_epub(report, master, manuscript)),
        ("pdf.validation", lambda: inspect_pdf(report, master, manuscript, build)),
        ("release.hash-validation", lambda: inspect_hashes(report, manuscript, build)),
    ]:
        try:
            work()
        except Exception as exc:
            report.exception(identifier, exc)
    changed = []
    for relative, fingerprint in report.artifacts.items():
        path = root / relative
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != fingerprint["sha256"]:
            changed.append(relative)
    report.add("release.stable-validation-snapshot", not changed,
               "All inspected deliverables and manifests remained unchanged for the duration of validation.", changed=changed)
    result = report.result()
    path = args.report or root / "research/validation-report.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"passed": result["passed"], "totals": result["totals"], "report": str(path)}, ensure_ascii=False))
    for check in report.checks:
        if check["status"] != "pass":
            print(f"{check['status'].upper()}: {check['id']}: {check['summary']}")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
