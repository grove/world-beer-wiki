#!/usr/bin/env python3
"""Offline manifest consistency audit and generated article/source backlink register."""
from __future__ import annotations
import argparse
from collections import defaultdict
import json
from pathlib import Path
import sys
from atlas import SUBJECT_DIRS, load_documents

FIELDS = ("resource", "title", "author_label", "source_kind", "access_scope")


def audit(root, edition="1.16", documents=None, manifest=None):
    root = Path(root)
    if documents is None:
        documents, errors = load_documents(root)
    else:
        errors = []
    if manifest is None:
        try:
            manifest = json.loads((root / "references" / f"atlas-source-manifest-{edition.replace(chr(46), chr(45))}.json").read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            return {"ok": False, "errors": [str(exc)], "counts": {}, "sources": {}, "uses": {}}
    if not isinstance(manifest, dict) or manifest.get("edition") != edition or not isinstance(manifest.get("sources"), list):
        return {"ok": False, "errors": errors + ["invalid manifest edition or sources"], "counts": {}, "sources": {}, "uses": {}}
    prefix = "v" + edition.replace(".", "") + "-"
    stamp = "world-beer-wiki/" + edition
    ext = "## Edition " + edition + ": newly sourced connections"
    sources, uses = {}, defaultdict(set)
    for item in manifest["sources"]:
        if not isinstance(item, dict):
            errors.append("manifest entry must be a mapping")
            continue
        sid = item.get("id")
        if not isinstance(sid, str) or not sid.startswith(prefix) or len(sid) <= len(prefix):
            errors.append("invalid source identifier " + str(sid))
            continue
        if sid in sources:
            errors.append("duplicate source " + sid)
        for field in FIELDS:
            if not isinstance(item.get(field), str) or not item[field].strip():
                errors.append(f"{sid}: missing {field}")
        sources[sid] = item
    new = revised = 0
    for path, obj in sorted(documents.items()):
        if path.split("/")[0] not in SUBJECT_DIRS or path.endswith("/index.md"):
            continue
        meta, body = obj["data"], obj["body"]
        new_page = meta.get("generated", {}).get("by") == stamp
        revised_page = not new_page and ext in body
        new += int(new_page)
        revised += int(revised_page)
        for item in meta.get("sources", []):
            if not isinstance(item, dict):
                continue
            sid = str(item.get("id", ""))
            if not sid.startswith(prefix):
                continue
            if not (new_page or revised_page):
                errors.append(f"{path}: untracked edition source {sid}")
            canonical = sources.get(sid)
            if canonical is None:
                errors.append(f"{path}: unknown manifest source {sid}")
                continue
            for field in FIELDS:
                if item.get(field) != canonical.get(field):
                    errors.append(f"{path}: {sid} inconsistent {field}")
            uses[sid].add(path)
    for sid in sources:
        if not uses[sid]:
            errors.append(f"{sid}: unused source")
    counts = {"new_subjects": new, "revised_subjects": revised,
              "distinct_source_records": len(sources),
              "source_usages": sum(len(v) for v in uses.values())}
    return {"ok": not errors, "errors": sorted(set(errors)), "counts": counts,
            "sources": sources, "uses": {k: sorted(v) for k, v in sorted(uses.items())}}


def render(root, edition="1.16", report=None):
    report = audit(root, edition) if report is None else report
    if not report["ok"]:
        raise ValueError("; ".join(report["errors"][:8]))
    count = report["counts"]
    lines = [
        "---", "type: Research Source Register",
        f"title: Edition {edition} — actual sources and backlinks",
        "description: Generated source register with actual article backlinks and access limitations.",
        f"tags: [wiki-documentation, edition-{edition}, sources]",
        "status: draft", "generated:", f"  by: world-beer-wiki/{edition}",
        "  at: '2026-10-28T13:00:00Z'", "sources:",
        "- id: atlas-spec", "  resource: /editorial/atlas-specification.md",
        "  title: World Beer Atlas expansion specification", "---", "",
        f"# Edition {edition}: annotated bibliography and article uses", "",
        f"**{count['distinct_source_records']} distinct works · {count['source_usages']} article-source placements · "
        f"{count['new_subjects']} new and {count['revised_subjects']} revised subjects.**", "",
        "A repeated citation does not constitute independent corroboration. Access descriptions are "
        "specific to the consulted pages, abstracts, previews and texts.",
    ]
    for sid, entry in sorted(report["sources"].items()):
        pages = report["uses"].get(sid, [])
        lines += ["", "## " + chr(96) + sid + chr(96) + " — " + entry["title"], "",
                  "- Credited to: " + entry["author_label"] + ".",
                  "- Evidence class: " + chr(96) + entry["source_kind"] + chr(96) + ".",
                  "- Actual access: " + entry["access_scope"],
                  f"- [Source URL]({entry['resource']}) · checked 2026-10-28.",
                  f"- Citing pages ({len(pages)}): " + " · ".join(
                      "[" + p.split("/")[-1][:-3].replace("-", " ") + "](../" + p + ")"
                      for p in pages) + "."]
    lines += ["", "## Independent review and limitations", "",
              "This record checks source metadata and backlinks; it does not access restricted "
              "standards in full, certify historical claims, or stand in for community, "
              "regulatory, brewing or food-safety review.", "",
              "[Research update](../editorial/research-update-1-16.md) · "
              "[Review queue](../editorial/source-review-queue-1-16.md) · "
              "[Reading trails](../navigation/edition-1-16-reading-trails.md) · "
              "Source manifest: references/atlas-source-manifest-1-16.json."]
    return "\n".join(lines).rstrip() + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--edition", default="1.16")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    result = audit(args.root, args.edition)
    if not result["ok"]:
        print(json.dumps({"ok": False, "errors": result["errors"]}, indent=2), file=sys.stderr)
        return 1
    path = args.root / "references" / f"atlas-sources-{args.edition.replace(chr(46), chr(45))}.md"
    output = render(args.root, args.edition, result)
    if args.check and (not path.exists() or path.read_text(encoding="utf-8") != output):
        print("FAIL: source register is stale", file=sys.stderr)
        return 1
    if not args.check:
        path.write_text(output, encoding="utf-8")
    if args.json:
        print(json.dumps({"ok": True, "counts": result["counts"], "errors": []}, indent=2))
    else:
        print("PASS" if args.check else "Generated", path.relative_to(args.root), result["counts"])
    return 0

if __name__ == "__main__":
    sys.exit(main())
