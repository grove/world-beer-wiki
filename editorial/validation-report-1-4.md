---
type: Validation Report
title: Research edition 1.4 validation report
description: Reproducible structural tests and limits for the latest expansion.
tags: [editorial, validation]
status: draft
generated:
  by: world-beer-wiki/1.4
  at: '2026-10-27T22:50:00Z'
sources:
- id: scope
  resource: /editorial/atlas-specification.md
  title: World Beer Atlas expansion specification
---

# Edition 1.4 validation

The release checks below are structural; they do **not** verify historical or microbiological truth. The [source supplement](../references/atlas-sources-1-4.md) records actual access limits.

## Reproduction

```bash
python tools/validate_wiki.py --json
python tools/atlas.py check --json
python -m unittest discover -s tests -v
python tools/atlas.py catalog > catalog.json
python tools/atlas.py progress > progress.json
python tools/atlas.py timeline > timeline.json
python tools/atlas.py source-audit > audit.json
python tools/build_site.py
```

## Results

All checks listed above ran locally on the exact staged repository snapshot (Python 3.13 with PyYAML). Structural results:

| Check | Verified result |
|---|---:|
| Markdown files and root-reachable files | 385 / 385 |
| Subject articles / preserved original beer-tradition paths | 341 / 166 |
| Local link occurrences resolved | 5,124 |
| Structured relations checked | 1,020 |
| Qualified evidence-bearing relationships | 46 |
| Footnote citations matched to local source metadata | 1,275 |
| Atlas events and seasonal records | 11 |
| Stable work ledger items | 31 |
| Distinct source IDs (base metadata index) | 434 |
| Distinct subject-source IDs (provenance audit) | 395 |
| Source occurrences in subject articles | 621 |
| Subject-source records missing explicit access notes | 0 |
| Python regression tests | 33 passed |
| Base and atlas structural errors | 0 |

`python tools/build_site.py` staged all **385 Markdown pages** for the searchable website; local staging does not itself establish an HTML rendering pass. `git diff --cached --check` detected no whitespace errors. Deterministic `catalog`, `timeline`, `progress` and `source-audit` exports are available; source reuse is not counted as independent corroboration. GitHub Actions results, if available, should be checked on the corresponding pull request.

No claim of independent human review is made. The checks do **not** prove source URLs remain reachable, assert microbiological safety, verify every source interpretation, or establish community approval.

[Progress](atlas-progress.md) · [Home](../index.md)
