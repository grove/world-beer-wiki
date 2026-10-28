#!/usr/bin/env python3
"""Check the book's structure and generated editions; not a factual verifier."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import posixpath
import re
import subprocess
import unicodedata
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
STEM = "100-things-beer-teaches-us"


def word_count(text):
    return len(re.findall(r"\b[\w]+(?:[’'-][\w]+)*\b", text, re.UNICODE))


def normalized_license(text):
    """Ignore layout whitespace and typographic quotes, but preserve all terms."""
    text = unicodedata.normalize("NFKC", text).translate(str.maketrans({
        "“": '"', "”": '"', "‘": "'", "’": "'"}))
    return re.sub(r"\s+", " ", text).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    errors, report = [], {"scope": "Structure, navigation and document integrity; not factual truth or independent review."}
    manuscript = ROOT / (STEM + ".md")
    text = manuscript.read_text(encoding="utf-8")
    source_license = (ROOT / "LICENSE-APACHE-2.0.txt").read_text(encoding="utf-8")
    expected_license = normalized_license(source_license)
    appendix = text.split("# Appendix: Apache License, Version 2.0 {#apache-license}", 1)[-1]
    license_start = re.search(r"Apache License\s+Version 2\.0, January 2004", appendix)
    markdown_license = re.sub(r"\\([.()])", r"\1", appendix[license_start.start():]) if license_start else ""
    license_checks = {"manuscript": normalized_license(markdown_license) == expected_license}
    if not license_checks["manuscript"]: errors.append("Manuscript Apache appendix differs from the preserved source license.")
    headings = list(re.finditer(r"^## (\d+)\. (.+?) \{#lesson-(\d{3})\}\s*$", text, re.M))
    numbers = [int(m[1]) for m in headings]
    if numbers != list(range(1, 101)): errors.append("Lesson sequence must be exactly 1–100.")
    for m in headings:
        if int(m[1]) != int(m[3]): errors.append(f"Wrong lesson anchor: {m[0]}")
    part_matches = list(re.finditer(r"^# Part ([IVX]+) [—–-] Beer & (History|Science|Culture) \{#part-[ivx]+\}$", text, re.M))
    part_counts = []
    for i, part in enumerate(part_matches):
        end = part_matches[i+1].start() if i+1 < len(part_matches) else text.index("# Afterword:")
        part_counts.append(len(re.findall(r"^## \d+\.", text[part.start():end], re.M)))
    if part_counts != [34, 33, 33]: errors.append(f"Invalid part counts: {part_counts}")
    definitions = re.findall(r"^\[\^n(\d{3})\]:", text, re.M)
    marker_body = re.sub(r"^\[\^n\d{3}\]:.*(?:\n[ \t]+.*)*", "", text, flags=re.M)
    references = re.findall(r"\[\^n(\d{3})\]", marker_body)
    expected = [f"{n:03d}" for n in range(1, 101)]
    if definitions != expected: errors.append("Source notes must be defined exactly once in order 001–100.")
    if Counter(references) != Counter(expected): errors.append("Each lesson must cite its one source-note identifier exactly once.")
    lengths = {}
    for i, match in enumerate(headings):
        end = headings[i+1].start() if i+1 < len(headings) else text.index("# Afterword:")
        body = text[match.end():end]
        body = re.split(r"^# Part", body, flags=re.M)[0]
        body = re.sub(r"\[\^n\d+\]", "", body)
        lengths[int(match[1])] = word_count(body)
        if lengths[int(match[1])] < 200: errors.append(f"Lesson {match[1]} has under 200 prose words.")
    required = ["title-page", "edition-note", "contents", "introduction", "part-i", "part-ii", "part-iii",
                "afterword", "acknowledgments", "research-method", "reading-onward", "notes", "apache-license"]
    identifiers = re.findall(r"\{#([^}]+)\}", text)
    for key in required:
        if key not in identifiers: errors.append(f"Missing required section: {key}")
    if len(identifiers) != len(set(identifiers)): errors.append("Duplicate explicit document anchors.")
    internal = re.findall(r"\]\(#([^)]+)\)", text)
    for anchor in internal:
        if anchor not in identifiers: errors.append(f"Missing internal destination: {anchor}")
    if re.search(r"BOOK-CONTENTS|BOOK-NOTES|BOOK-APACHE|\bTODO\b|\bTBD\b|lorem ipsum", text, re.I):
        errors.append("Unresolved production placeholder.")
    matrix = json.loads((ROOT / "research/source-to-chapter.json").read_text())
    if [r["number"] for r in matrix] != list(range(1, 101)): errors.append("Source map sequence differs from manuscript.")
    by_number = {int(m[1]): m[2] for m in headings}
    wiki_paths, original_urls = set(), set()
    repository = ROOT.parents[1]
    for row in matrix:
        if row["title"] != by_number.get(row["number"]): errors.append(f"Source map title mismatch: {row['number']}")
        for path in row["wiki_articles"]:
            wiki_paths.add(path)
            # The standalone publishing bundle remains independently usable;
            # existence checks are available when built inside its source repo.
            if (repository / "tools/atlas.py").exists() and not (repository / path).is_file():
                errors.append(f"Source map references absent wiki file: {path}")
        for source in row["original_sources"]: original_urls.add(source["url"])
    report["manuscript"] = {
        "lessons": len(numbers), "part_counts": part_counts, "source_notes": len(definitions),
        "lesson_prose_words": sum(lengths.values()), "shortest_lesson": min(lengths.values()),
        "longest_lesson": max(lengths.values()), "words_per_lesson": lengths,
        "plain_markdown_word_count_including_urls_and_metadata": word_count(text),
        "wiki_articles_mapped": len(wiki_paths), "underlying_source_urls_mapped": len(original_urls),
    }
    # Pandoc plain text gives a readable count without counting URL syntax and
    # YAML metadata as if they were prose.
    plain = subprocess.run(["pandoc", str(manuscript), "-t", "plain", "--wrap=none"],
                           check=True, capture_output=True, text=True).stdout
    report["manuscript"]["reading_edition_words_including_toc_notes_license"] = word_count(plain)

    epub = ROOT / (STEM + ".epub")
    if epub.exists():
        with zipfile.ZipFile(epub) as archive:
            names = archive.namelist()
            if names[0] != "mimetype" or archive.read("mimetype") != b"application/epub+zip":
                errors.append("EPUB mimetype packaging is invalid.")
            if archive.getinfo("mimetype").compress_type != zipfile.ZIP_STORED:
                errors.append("EPUB mimetype must be uncompressed.")
            docs, ids = {}, {}
            for name in names:
                if name.endswith((".xhtml", ".opf", ".ncx")):
                    try: docs[name] = ET.fromstring(archive.read(name))
                    except ET.ParseError as exc: errors.append(f"EPUB XML: {name}: {exc}")
                    if name in docs: ids[name] = {el.attrib["id"] for el in docs[name].iter() if "id" in el.attrib}
            links_checked = 0
            for name, doc in docs.items():
                for el in doc.iter():
                    target = el.attrib.get("href") or el.attrib.get("src")
                    if not target: continue
                    parsed = urlsplit(target)
                    if parsed.scheme or parsed.netloc: continue
                    resolved = posixpath.normpath(posixpath.join(posixpath.dirname(name), unquote(parsed.path))) if parsed.path else name
                    if resolved not in names: errors.append(f"EPUB missing resource {name} -> {target}")
                    elif parsed.fragment and resolved in ids and unquote(parsed.fragment) not in ids[resolved]:
                        errors.append(f"EPUB missing anchor {name} -> {target}")
                    links_checked += 1
            all_ids = set().union(*ids.values())
            missing_lessons = [f"lesson-{n:03d}" for n in range(1,101) if f"lesson-{n:03d}" not in all_ids]
            if missing_lessons: errors.append(f"EPUB missing lessons: {missing_lessons}")
            report["epub"] = {"xml_documents": len(docs), "internal_resource_links_checked": links_checked,
                              "all_lesson_anchors_present": not missing_lessons}
            license_checks["epub_reading_text"] = False
            for name, doc in docs.items():
                if "apache-license" in ids[name]:
                    appendix_text = " ".join(doc.itertext())
                    start = re.search(r"Apache License\s+Version 2\.0, January 2004", appendix_text)
                    if start:
                        license_checks["epub_reading_text"] = normalized_license(appendix_text[start.start():]) == expected_license
            license_checks["epub_embedded_original"] = archive.read("META-INF/source-license.txt") == source_license.encode("utf-8")
            if not license_checks["epub_reading_text"]: errors.append("EPUB Apache appendix differs from the preserved source license.")
            if not license_checks["epub_embedded_original"]: errors.append("EPUB embedded source license differs from the original file.")
    else: errors.append("EPUB has not been built.")
    pdf = ROOT / (STEM + ".pdf")
    if pdf.exists():
        from pypdf import PdfReader
        reader = PdfReader(pdf)
        extracted = "\n".join(page.extract_text() or "" for page in reader.pages)
        present = [n for n in range(1,101) if re.search(rf"LESSON\s+{n:02d}\s*/", extracted)]
        if len(present) != 100: errors.append("PDF text does not contain all 100 lesson labels.")
        uri_count, internal_count = 0, 0
        for page in reader.pages:
            for annotation in page.get("/Annots", []):
                obj = annotation.get_object()
                if obj.get("/A", {}).get("/S") == "/URI": uri_count += 1
                if "/Dest" in obj or obj.get("/A", {}).get("/S") == "/GoTo": internal_count += 1
        report["pdf"] = {"pages": len(reader.pages), "lesson_labels_present": len(present),
                         "external_link_annotations": uri_count, "internal_link_annotations": internal_count,
                         "metadata": {str(k):str(v) for k,v in reader.metadata.items()}}
        appendix_start = re.search(r"Apache License\s+Version 2\.0, January 2004", extracted)
        pdf_license = extracted[appendix_start.start():] if appendix_start else ""
        pdf_license = re.sub(r"(?m)^100 THINGS BEER TEACHES US\s*$", "", pdf_license)
        pdf_license = re.sub(r"(?m)^\d{1,3}\s*$", "", pdf_license)
        license_checks["pdf_reading_text"] = normalized_license(pdf_license) == expected_license
        if not license_checks["pdf_reading_text"]: errors.append("PDF Apache appendix differs from the preserved source license.")
    else: errors.append("PDF has not been built.")
    report["source_license_fidelity"] = license_checks
    report["sha256"] = {p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in [manuscript, epub, pdf] if p.exists()}
    report["errors"], report["ok"] = errors, not errors
    (ROOT / "research/validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    if args.json: print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"Lessons: {len(numbers)}; parts: {part_counts}; notes: {len(definitions)}")
        print(f"Lesson prose: {sum(lengths.values()):,} words; readable full book: {report['manuscript']['reading_edition_words_including_toc_notes_license']:,} words")
        print("PASS" if not errors else "FAIL\n" + "\n".join(errors))
    raise SystemExit(0 if not errors else 1)


if __name__ == "__main__":
    main()
