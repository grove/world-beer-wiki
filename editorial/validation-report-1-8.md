---
type: Editorial Validation Report
title: Research edition 1.8 validation and reproducibility
description: Recorded structural checks, regression tests and known limits.
tags:
- wiki-documentation
- research
- edition-1.8
status: draft
generated:
  by: world-beer-wiki/1.8
  at: '2026-10-28T07:55:00Z'
sources:
- id: atlas-spec
  resource: /editorial/atlas-specification.md
  title: World Beer Atlas expansion specification
---

# Research edition 1.8 — reproducible validation report

**28 October 2026 · local structural validation passed before GitHub upload.** All results below refer to the complete local candidate tree. Hosted CI outcomes will be assessed on the uploaded commit. This report does not claim independent expert or cultural review, health safety, external link uptime, or complete access to referenced papers.

| Validation check | Recorded result |
|---|---:|
| Markdown pages reachable from the root | **520 / 520** |
| Canonical subject articles across 13 sections | **457** |
| Resolved internal link occurrences | **7209** |
| Structured comparison and other relations | **1243** |
| Evidence-bearing qualified relations | **67** |
| Matched source-note citations | **1756** |
| Unique source identifiers in all pages | **524** |
| Source-audit records (cross-section metadata) | **479** |
| Entries with missing source access descriptions | **0** |
| Edition 1.8 distinct source IDs | **16** |
| Edition 1.8 new article count | **29** |
| Edition 1.8 existing-page research updates | **14** |
| Edition 1.8 documented source uses | **75** |
| Specification work items | **59** |
| Python regression tests | **68 passed** |
| Pages staged for optional website | **520 / 520** |
| Structural validation errors | **0** |

## Commands actually run

From the repository root, with PyYAML and Python installed:

```bash
python tools/validate_wiki.py --json
python tools/atlas.py check --json
python tools/atlas.py source-audit
python tools/research_quality.py --edition 1.6 --json
python tools/research_quality.py --edition 1.7 --json
python tools/research_quality.py --edition 1.8 --json
python tools/build_subject_index.py --check
python -m unittest discover -s tests -q
python tools/build_site.py
```

The index is deterministic, and **520** Markdown pages were staged for the optional searchable website. MkDocs is not installed in the local execution environment; a successful staging run is **not** a claim that the HTML generator passed. The GitHub website workflow remains the authoritative hosted build check.

The edition 1.8 research checker requires actual in-body citations to each edition source ID and footnotes, nonempty access descriptions, readable internal links, new-page scope and draft-review status. The source-audit report checks source metadata across all sections. Tests of **both** edition 1.6 and 1.7 still pass. Citation use proves neither statement correctness nor independence of repeated source records.

## Known limits and next steps

Laboratory samples, original field contexts, review articles and abstract-only studies remain distinguished. No result is a potable-water claim about Shawi masato, an instruction to use msesewe bark, a universal fermentation procedure, or a guaranteed beer-foam/aroma outcome. Obtain community and domain-specialist review before upgrading draft status. The [ranked research queue](source-review-queue-1-8.md) identifies open tasks.

[Research update](research-update-1-8.md) · [Source register](../references/atlas-sources-1-8.md) · [Specification](atlas-specification.md) · [Home](../index.md)
