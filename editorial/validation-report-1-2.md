---
type: Validation Report
title: Edition 1.2 validation report
description: Edition 1.2 validation report
tags:
- wiki-documentation
- atlas
status: draft
generated:
  by: world-beer-wiki/1.2
  at: '2026-10-27T20:40:00Z'
sources:
- id: atlas-spec
  resource: /editorial/atlas-specification.md
  title: World Beer Atlas expansion specification
---

# Edition 1.2 validation report

**27 October 2026 · structural checks, not independent historical or community verification.** The earlier [1.1 report](validation-report.md) remains a historical release record.

## Checks actually run

| Check | Result |
|---|---:|
| Markdown documents | 275 |
| Documents reachable from the root | 275 |
| Subject articles across ten reference layers | 240 |
| Beer and tradition profiles, with original paths retained | 166 |
| Ingredient references | 23 |
| Category guides | 13 |
| New culture/calendar/microbiology/process/object/sensory/story references | 38 |
| Structured relations with existing targets and body links | 825 |
| Evidence-bearing qualified relations | 18 |
| Calendar metadata records | 5 |
| Tracked scope work items | 14 |
| Footnote references resolved to definitions and registered sources | 985 |
| Regression tests passed, including the existing site-generator suite | 26 |
| Broken local links, unresolved footnotes, structural validation errors | 0 |

The base validator additionally checks source-ID consistency, nonempty metadata, reserved index conventions, generated timestamps, anchors and directory membership. The atlas validator checks source-qualified factual relations, legacy editorial comparisons, calendar kinds and dates, canonical paths and work-ledger deliverables.

The catalog was generated twice and compared byte-for-byte successfully. Its reverse links retain the originating article, relation type, source IDs and qualifier. The progress export reports eleven implemented items, one planned review item and two deferred features; it does not claim a percentage of world knowledge completed.

## Website compatibility

The site staging command discovered all 275 Markdown pages and included every staged page in generated navigation. New subject layers receive the research-draft metadata presentation. Linked maintenance Python files remain available as readable source in the staged site. The existing website tests were extended to cover those behaviors.

The local environment did not have MkDocs installed, so a local HTML build is **not** claimed here. The repository's separate searchable-site workflow performs the strict HTML build on the PR. Its latest result should be checked in GitHub; staging and offline validation are not substitutes for that result.

## Reproduce

```bash
python tools/validate_wiki.py --json
python tools/atlas.py check --json
python -m unittest discover -s tests -v
python tools/atlas.py catalog > atlas-catalog.json
python tools/atlas.py progress > atlas-progress.json
python tools/build_site.py
```

The read-only validation workflow attaches JSON results and a ZIP of tracked repository files. No external source URLs are fetched by the offline checks. They cannot prove a source's historical claim, establish cultural consent, guarantee external-link availability or certify a brewing process as safe.

[Specification](atlas-specification.md) · [Scope and progress](atlas-progress.md) · [Research update](research-update-1-2.md) · [Source supplement](../references/atlas-sources.md) · [Home](../index.md)
