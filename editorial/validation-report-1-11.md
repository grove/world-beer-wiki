---
type: Validation Report
title: Research edition 1.11 validation and scope
status: draft
description: Offline checks for the source-bounded 1.11 research edition; structural passes are not historical review.
tags: [wiki-documentation, edition-1.11, validation]
generated:
  by: world-beer-wiki/1.11
  at: '2026-10-28T08:55:00Z'
sources:
- id: atlas-spec
  resource: /editorial/atlas-specification.md
  title: World Beer Atlas expansion specification
---

# Research edition 1.11 — validation and scope

This report covers the **1.11 candidate**, based on merged edition 1.10. Offline checks validate article structure, paths, source metadata, use of citations, directory membership and deterministic exports, **not** the truth of historical claims, microbiological safety, outside website availability or community endorsement.

## Reproduce

```bash
python tools/validate_wiki.py --json
python tools/atlas.py check --json
python tools/research_quality.py --edition 1.11 --json
python -m unittest discover -s tests -v
python tools/build_subject_index.py --check
python tools/build_site.py
```

## Candidate scope

The release adds 34 subject articles and 18 source-cited revisions, recording 21 named external works. Every original 166 beer-and-tradition profile path is preserved. The [source supplement](../references/atlas-sources-1-11.md) distinguishes abstract-limited research, review-level statements, and original experimental results and links each source to its citing articles.

The [specification](atlas-specification.md) now has 79 work items, with 76 implemented within their stated scope, one planned community/expert review item and two deferred features. [Open research tasks](source-review-queue-1-11.md) remain open; there has been **no independent community or specialist review**.

## Structural validation

All commands below were run against the same local edition 1.11 working tree on 28 October 2026. Values count different things and are **not** a measure of historical accuracy.

| Local check | Observed result |
|---|---:|
| Markdown files reachable from `index.md` | **627 / 627** |
| Canonical subject articles | **549** |
| Resolved local link occurrences | **8,482** |
| Structured comparison/qualified relations | **1,553** |
| Footnote citations matched to local source records | **2,135** |
| Calendar metadata records | **18** |
| Qualified factual relations in all editions | **68** |
| 1.11 source record identities | **21** |
| 1.11 source usages | **90** |
| 1.11 new and revised subjects | **34 + 18** |
| Full regression suite | **106 tests passed** |
| Errors in offline validators | **0** |

`python tools/build_subject_index.py --check` passed and `python tools/build_site.py` staged **627 Markdown pages** for the searchable website. The source audit, catalog, progress and timeline exports were generated successfully with no external fetches. `git diff --check` passed.

The local environment did **not** have MkDocs installed, so local website staging is not a claim of an HTML build; GitHub Actions performs the separate website build. Source URLs were not live-checked by the offline validators. Any CI status mentioned in the PR must be checked separately on the actual PR commit.

## Interpretation and outstanding review

The results establish reproducible structure and metadata consistency only. Research was based on a mixture of accessible full-text reviews, abstracts, indexed experimental descriptions, museum writing and historical interpretations. The 2007 cauim microbiology isolates, five-stage pulque survey, 2015 kunun-zaki recipe and 2025 single-batch tepache experiment are **not** interchangeable or sufficient to certify food safety. The [open 1.11 review queue](source-review-queue-1-11.md) records community, language, subject and primary-source checks yet to be performed.
