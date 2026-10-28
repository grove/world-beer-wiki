---
type: Validation Report
title: World Beer Atlas edition 1.13 validation
description: Actual local and later hosted validation results with their limitations.
tags:
- wiki-documentation
- edition-1.13
- validation
status: draft
generated:
  by: world-beer-wiki/1.13
  at: '2026-10-28T09:30:00Z'
sources:
- id: atlas-spec
  resource: /editorial/atlas-specification.md
  title: World Beer Atlas expansion specification
---

# World Beer Atlas edition 1.13 validation

This report records the actual **local** checks run against edition 1.13 after the final content and navigation changes. The checks validate structure, references and staging; they do not prove that the external research is correct or independently reviewed.

## Reproduction commands

```bash
python tools/validate_wiki.py --json
python tools/atlas.py check --json
python tools/research_quality.py --edition 1.13 --json
python tools/check_inventory.py --json
python tools/build_subject_index.py --check
python tools/build_names_index.py --check
python -m unittest discover -s tests -v
python tools/build_site.py
```

## Results

All values below were measured from the fully linked local working tree on 28 October 2026. No GitHub-hosted check is claimed in this offline report; verify the exact PR commit's workflow status independently.

| Local validation | Observed result |
|---|---:|
| Markdown files reachable from root | **702 / 702** |
| Canonical subject articles | **614 across 13 sections** |
| Resolved local link occurrences | **9,825** |
| Structured relations with valid targets and body links | **1,832** |
| Evidence-bearing relations (entire corpus) | **86** |
| Source-qualified new relations in edition 1.13 | **18 in 16 articles** |
| Footnote citations paired with sources | **2,404** |
| Regression tests | **137 passed** |
| Local source hygiene for edition 1.13 | **35 new, 19 revised, 21 works, 93 uses; passed** |
| Deterministic subject/name directories | **Both checks passed** |
| Searchable website staging | **702 pages staged successfully** |
| Structural errors | **0** |

The existing CLI inventory checker also confirms the README and root index report exactly 614 subject articles. The site-staging check is not itself proof of completed MkDocs HTML publishing. The per-edition research checks for **1.6–1.13** remain executable, preserving earlier evidence-hygiene checks without rewriting historical research records.

## What remains unverified

Structural checks do not independently verify historical dates, journal full-text access, environmental LCA assumptions, clinical effects, microbial food safety or cultural consent. The [annotated source register](../references/atlas-sources-1-13.md) reports source scope; the [review queue](source-review-queue-1-13.md) tracks unperformed expert consultation. All research articles remain `draft`.

[Research update](research-update-1-13.md) · [Sources](../references/atlas-sources-1-13.md) · [Home](../index.md).
