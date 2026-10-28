---
type: Validation Report
title: Edition 1.7 — validation record
description: Locally reproduced structure, citation and website checks for research edition 1.7.
tags:
- editorial
- research
- release
- edition-1.7
status: draft
generated:
  by: world-beer-wiki/1.7
  at: '2026-10-28T05:45:00Z'
sources:
- id: atlas-spec
  resource: /editorial/atlas-specification.md
  title: World Beer Atlas expansion specification
---

# Edition 1.7 — validation record

**Research edition 1.7: local checks passed on 28 October 2026.** These results describe the working tree before upload and are separate from GitHub Actions status, historical verification, independent expert review, and external URL health.

| Local quality check | Recorded result |
|---|---:|
| Markdown pages found and reachable from the root | 486 / 486 |
| Subject articles across 13 reference sections | 428 |
| Resolved local Markdown link occurrences | 6,785 |
| Structured comparison / article relations | 1,156 |
| Evidence-bearing qualified relations | 67 |
| Matched source-note citations | 1,656 |
| Unique source IDs in all wiki pages | 508 |
| Edition 1.7 distinct documented sources | 25 |
| Edition 1.7 new subject articles | 26 |
| Edition 1.7 existing articles with source-bearing extensions | 16 |
| Edition 1.7 source usages | 69 |
| Specification work items | 53 |
| Regression tests | 57 passed |
| Validation failures | **0** |

## Reproduction commands

Run from the repository root with Python and the documented optional dependencies:

```bash
python tools/validate_wiki.py --json
python tools/atlas.py check --json
python tools/research_quality.py --edition 1.7 --json
python tools/research_quality.py --edition 1.6 --json
python tools/build_subject_index.py --check
python -m unittest discover -s tests -v
python tools/build_site.py
```

The legacy 1.6 research-quality audit also passes; its historical research set is not erased by the 1.7 additions. The subject index check reports no stale, missing, or extra entry. The website staging step reports **486 searchable pages staged**. This is a local content-stage check, not an HTML renderer result; the separate GitHub website workflow checks its hosted build after publication.

## Scope of validation

These tools validate YAML syntax, local navigation, source identifiers, link targets, required access-scope metadata, metadata consistency, and tracked file presence. They do **not** reread the full text of external papers, verify that ethnographic generalizations are appropriate, certify microbial safety, or establish community consent. The source register explicitly records when a full paper or archival record was **not** inspected. All articles remain research drafts.

[Research update](research-update-1-7.md) · [Specification](atlas-specification.md)
