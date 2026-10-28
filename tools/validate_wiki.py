#!/usr/bin/env python3
"""Optional offline checks for this Markdown wiki. Requires Python 3 and PyYAML.

Checks the repository's documented conventions, not the complete OKF schema or
historical truth. Markdown handling covers inline/reference links, balanced URL
parentheses, Unicode heading anchors, explicit HTML anchors and fenced code.
"""
import argparse
from collections import Counter
from datetime import datetime
import html
import json
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit

import yaml

# Standalone publications have their own editorial and build validation.
NON_WIKI_DIRS = {"books"}


def is_wiki_path(relative):
    return not (any(part.startswith(".") for part in relative.parts)
                or relative.parts[0] in NON_WIKI_DIRS)


class UniqueLoader(yaml.SafeLoader):
    pass


def mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise yaml.constructor.ConstructorError(None, None, f"duplicate key {key!r}", key_node.start_mark)
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)


def without_fences(text):
    lines, fence = [], None
    for line in text.splitlines():
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
            lines.append("")
        elif match:
            fence = match[1]
            lines.append("")
        else:
            lines.append(line)
    return "\n".join(lines)


def destination(text, start=0):
    """Read a Markdown destination, without consuming its optional title."""
    start += len(text[start:]) - len(text[start:].lstrip())
    if text[start:start + 1] == "<":
        end = text.find(">", start + 1)
        return text[start + 1:end] if end >= 0 else ""
    chars, depth, i = [], 0, start
    while i < len(text):
        char = text[i]
        if char == "\\" and i + 1 < len(text):
            chars.append(text[i + 1]); i += 2; continue
        if char == "(":
            depth += 1
        elif char == ")":
            if depth == 0: break
            depth -= 1
        elif char.isspace() and depth == 0:
            break
        chars.append(char); i += 1
    return "".join(chars)


def links(text):
    found = [(destination(text, m.end()), text.count("\n", 0, m.start()) + 1)
             for m in re.finditer(r"\]\(", text)]
    norm = lambda s: " ".join(s.split()).casefold()
    definitions = {norm(m[1]): destination(m[2]) for m in
                   re.finditer(r"^ {0,3}\[([^\]^][^\]]*)\]:\s*(.*)$", text, re.M)}
    for match in re.finditer(r"!?\[([^\]\n]+)\](?:\[([^\]\n]*)\])?", text):
        if match[1].startswith("^") or text[match.end():match.end() + 1] in ("(", ":"):
            continue
        key = norm(match[2] or match[1])
        if key in definitions:
            found.append((definitions[key], text.count("\n", 0, match.start()) + 1))
    return found


def anchors(text):
    result = set(re.findall(r'<[^>]+\b(?:id|name)=["\']([^"\']+)["\']', text, re.I))
    lines = text.splitlines()
    for i, line in enumerate(lines):
        match = re.match(r"^ {0,3}#{1,6}\s+(.+)$", line)
        heading = match[1] if match else (lines[i - 1] if i and re.fullmatch(r" {0,3}(?:=+|-+)\s*", line) else None)
        if not heading: continue
        heading = re.sub(r"\s+#+\s*$", "", heading)
        heading = re.sub(r"!?\[([^\]]+)\]\([^)]*\)", r"\1", heading)
        heading = html.unescape(re.sub(r"<[^>]*>|[`*~]", "", heading)).lower()
        slug = "".join(c for c in heading.strip() if c in "-_" or c.isspace() or unicodedata.category(c)[0] in "LNM")
        slug = re.sub(r"\s", "-", slug)
        candidate, suffix = slug, 0
        while candidate in result:
            suffix += 1; candidate = f"{slug}-{suffix}"
        result.add(candidate)
    return result


def validate(root):
    root = root.resolve()
    paths = sorted(p for p in root.rglob("*.md") if is_wiki_path(p.relative_to(root)))
    errors, documents, source_map, graph = [], {}, {}, {}
    counts = Counter(concept_files=0, comparison_relations=0, footnote_citations=0, local_link_occurrences=0)
    def error(path, message): errors.append(f"{path.relative_to(root)}: {message}")
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8-sig")
            front = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
            data = yaml.load(front[1], Loader=UniqueLoader) if front else None
            if front and not isinstance(data, dict): raise ValueError("frontmatter must be a mapping")
        except (OSError, UnicodeError, yaml.YAMLError, ValueError, TypeError) as exc:
            error(path, f"cannot parse document: {exc}"); continue
        body = without_fences(text[front.end():] if front else text)
        masked = re.sub(r"(`+)(.*?)\1", lambda m: " " * len(m[0]), body)
        documents[path] = (data or {}, masked, anchors(body))
        graph[path] = set()
        if path == root / "index.md":
            if not data or str(data.get("okf_version")) != "0.2": error(path, 'root must declare okf_version: "0.2"')
            if data and "type" in data: error(path, "root index must not carry concept type")
        elif path.name in ("index.md", "log.md"):
            if front: error(path, "reserved index/log must not carry frontmatter")
        else:
            counts["concept_files"] += 1
            for field in ("type", "title", "status"):
                if not isinstance((data or {}).get(field), str) or not data[field].strip(): error(path, f"missing nonempty {field}")
            generated = (data or {}).get("generated", {})
            if not isinstance(generated, dict): generated = {}
            if not isinstance(generated.get("by"), str) or not generated["by"].strip(): error(path, "missing generated.by")
            try:
                stamp = datetime.fromisoformat(str(generated.get("at", "")).replace("Z", "+00:00"))
                if stamp.utcoffset() is None: raise ValueError()
            except ValueError: error(path, "generated.at must be an ISO timestamp with timezone offset")
    def resolve(path, target, context, canonical=False):
        try: parsed = urlsplit(html.unescape(target))
        except ValueError: error(path, f"{context}: malformed target {target!r}"); return None
        if parsed.scheme or parsed.netloc: return None
        name = unquote(parsed.path)
        base = root if canonical or name.startswith("/") else path.parent
        candidate = (base / name.lstrip("/")) if name else path
        if canonical and not candidate.suffix: candidate = candidate.with_suffix(".md")
        if candidate.is_dir(): candidate /= "index.md"
        candidate = candidate.resolve()
        if not candidate.is_relative_to(root): error(path, f"{context}: target escapes repository: {target}"); return None
        if not candidate.is_file(): error(path, f"{context}: missing file {target}"); return None
        fragment = unquote(parsed.fragment)
        if fragment and candidate.suffix == ".md" and fragment not in documents.get(candidate, ({}, "", set()))[2]:
            error(path, f"{context}: missing anchor #{fragment} in {candidate.relative_to(root)}")
        return candidate
    for path, (data, body, _) in documents.items():
        for target, line in links(body):
            resolved = resolve(path, target, f"body line {line}")
            if resolved:
                counts["local_link_occurrences"] += 1
                if resolved.suffix == ".md": graph[path].add(resolved)
        sources = data.get("sources", [])
        if not isinstance(sources, list): error(path, "sources must be a list"); sources = []
        ids = set()
        for source in sources:
            if not isinstance(source, dict) or any(not isinstance(source.get(k), str) or not source[k].strip() for k in ("id", "resource", "title")):
                error(path, "each source needs nonempty id, resource and title"); continue
            key = source["id"]
            if key in ids: error(path, f"duplicate source id {key}")
            ids.add(key)
            identity = (source["resource"], source["title"])
            if key in source_map and source_map[key][:2] != identity:
                error(path, f"source {key!r} resource/title conflicts with {source_map[key][2]}")
            else: source_map.setdefault(key, (*identity, str(path.relative_to(root))))
            resolve(path, source["resource"], f"source {key}")
        definitions = re.findall(r"^ {0,3}\[\^([^\]]+)\]:", body, re.M)
        reference_text = re.sub(r"^ {0,3}\[\^[^\]]+\]:", "", body, flags=re.M)
        references = re.findall(r"\[\^([^\]]+)\]", reference_text)
        counts["footnote_citations"] += len(references)
        for key, n in Counter(definitions).items():
            if n > 1: error(path, f"duplicate footnote definition {key}")
        for key in sorted(set(references) - set(definitions)): error(path, f"undefined footnote {key}")
        for key in sorted(set(definitions) - set(references)): error(path, f"unused footnote definition {key}")
        for key in sorted(set(definitions + references) - ids): error(path, f"footnote {key} missing from sources")
        relations = data.get("relations", [])
        if not isinstance(relations, list): error(path, "relations must be a list"); relations = []
        for relation in relations:
            counts["comparison_relations"] += 1
            if not isinstance(relation, dict) or not isinstance(relation.get("target"), str):
                error(path, "relation needs a string target"); continue
            resolved = resolve(path, relation["target"], "relation", canonical=True)
            if resolved and resolved not in graph[path]: error(path, f"relation target is not linked in body: {relation['target']}")
    visited, pending = set(), [root / "index.md"]
    if pending[0] not in documents: errors.append("index.md: missing or invalid root index")
    while pending:
        path = pending.pop()
        if path in visited or path not in documents: continue
        visited.add(path); pending.extend(graph.get(path, set()) - visited)
    for path in sorted(set(paths) - visited): error(path, "not reachable through Markdown links from index.md")
    for directory, key in (("styles", "style_profiles"), ("ingredients", "ingredient_profiles"), ("categories", "category_guides")):
        members = {p for p in paths if directory in p.relative_to(root).parts[:1] and p.name not in ("index.md", "log.md")}
        counts[key] = len(members)
        index = root / directory / "index.md"
        if index not in documents: error(index, "missing or invalid directory index")
        for path in sorted(members - graph.get(index, set())): error(index, f"missing directory member link: {path.relative_to(root)}")
    counts.update(markdown_files=len(paths), source_records=len(source_map), reachable_markdown_files=len(visited))
    return {"ok": not errors, "counts": dict(sorted(counts.items())), "errors": sorted(set(errors))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json", action="store_true", help="emit a deterministic JSON report")
    args = parser.parse_args()
    if not args.root.is_dir(): parser.error(f"not a directory: {args.root}")
    report = validate(args.root)
    if args.json: print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print("PASS" if report["ok"] else "FAIL")
        for key, value in report["counts"].items(): print(f"{key}: {value}")
        for message in report["errors"]: print(f"ERROR: {message}")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
