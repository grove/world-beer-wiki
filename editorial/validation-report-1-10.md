---
type: Validation Report
title: Edition 1.10 validation report
description: Reproducible checks for research edition 1.10.
tags:
- wiki-documentation
- edition-1.10
status: draft
generated:
  by: world-beer-wiki/1.10
  at: '2026-10-28T08:50:00Z'
sources:
- id: atlas-spec
  resource: /editorial/atlas-specification.md
  title: World Beer Atlas expansion specification
---

# Edition 1.10 validation report

**Local checks passed on 28 October 2026.** These numbers describe the final local Markdown tree, not independent fact checking, live URL health or human/community review. Historic validation reports remain unchanged.

| Check | Observed result |
|---|---:|
| Total Markdown files | **588** |
| Markdown files reachable from the root | **588 / 588** |
| Canonical subject articles | **515** |
| Subject sections | **13** |
| Local Markdown link occurrences resolved | **7,997** |
| Structured comparison and evidence relations | **1,417** |
| Evidence-bearing qualified relations | **67** |
| Matched footnote citation references | **1,986** |
| Distinct local source identifiers (base validator) | **561** |
| Source metadata records in cross-section audit | **516** |
| Sources lacking an access-scope description | **0** |
| Edition 1.10 new articles / revised existing articles | **27 / 15** |
| Edition 1.10 distinct external source records | **19** |
| Edition 1.10 source-record usages | **72** |
| Specification work items | **72** |
| Specification states | **69 implemented, 1 planned, 2 deferred** |
| Regression tests | **92 passed** |
| Markdown pages staged for optional searchable website | **588 / 588** |
| Structural validation errors | **0** |

## How to reproduce

Run from the repository root with Python 3.11+ and PyYAML:

```bash
python tools/validate_wiki.py --json
python tools/atlas.py check --json
python tools/atlas.py source-audit
python tools/atlas.py catalog
python tools/atlas.py progress
python tools/atlas.py timeline
python tools/research_quality.py --edition 1.6 --json
python tools/research_quality.py --edition 1.7 --json
python tools/research_quality.py --edition 1.8 --json
python tools/research_quality.py --edition 1.9 --json
python tools/research_quality.py --edition 1.10 --json
python tools/build_subject_index.py --check
python -m unittest discover -s tests -q
python tools/build_site.py
```

The complete source register is [annotated and backlinked](../references/atlas-sources-1-10.md). The [scope specification](atlas-specification.md) retains explicit review status.

## Limitations

The validators prove local link and source-metadata consistency, **not** the correctness of every historical, chemical, food-safety or cultural interpretation. Some referenced works were available only through abstracts or indexed extracts. The edition quality checker verifies that cited works are actually used in explanatory text; it cannot audit their original experimental methods.

The optional MkDocs HTML generator was **not installed locally**: website staging was checked, but this report makes no local HTML-build claim. Any GitHub Actions result should be checked independently against the final PR commit.

No independent regional practitioner, community representative, historian, microbiologist or coeliac specialist approved these drafts. The queued work remains explicit in the [independent-review list](source-review-queue-1-10.md).

[Home](../index.md) · [Research report](research-update-1-10.md) · [Progress ledger](atlas-progress.md)
