---
type: Validation Report
title: Edition 1.6 validation and reproduction
description: Actual offline structural, evidence-hygiene and site-staging checks for the 2026-10-28 research expansion.
tags: [editorial, validation, research-edition-1.6]
status: draft
generated:
  by: world-beer-wiki/1.6
  at: '2026-10-28T05:45:00Z'
sources:
- id: atlas-v16-research
  resource: /editorial/research-update-1-6.md
  title: Edition 1.6 research update
---

# Edition 1.6 validation and reproduction

This report records structure and maintenance checks, not independent historical, ethnographic, microbiological, community or safety review. The original Markdown files remain the source of truth; tests run offline without querying external sources.

## Reproduce from repository root

```bash
python tools/validate_wiki.py --json
python tools/atlas.py check --json
python tools/research_quality.py --json
python -m unittest discover -s tests -v
python tools/build_subject_index.py --check
python tools/build_site.py
```

## Results

The metrics below are populated from the current edition's actual validator and test output; subsequent edits require running the commands again.

| Reproducible check | Result |
|---|---:|
| Canonical subject articles | **402** across **13** layers |
| New edition 1.6 subject articles | **30** |
| Previously existing articles with newly cited research | **22** |
| Fully reachable Markdown pages | **455 / 455** |
| Resolved internal Markdown link occurrences | **6,352** |
| Valid target/body-linked structured relations | **1,155** |
| Evidence-bearing qualified relations | **66** |
| Matched footnote citation references | **1,542** |
| Distinct source IDs across all Markdown | **483** (includes internal and editorial records) |
| Distinct edition 1.6 external source records | **21** |
| Edition 1.6 source uses across articles | **90** |
| Implementation ledger | **45** work items: 42 implemented, 1 planned, 2 deferred |
| Regression tests | **47 passed** |
| Staged pages for optional searchable website | **455** |
| Base structural validator errors | **0** |
| Atlas structural validator errors | **0** |
| Edition evidence-hygiene errors | **0** |

`python tools/build_subject_index.py --check` passed against the regenerated **402-entry** index. `python tools/atlas.py source-audit` reported **zero missing source-access scopes**. `python tools/build_site.py` staged the Markdown website and performed a preflight audit for links to unpublished files; the local result alone does not claim that MkDocs rendered HTML. GitHub Actions checks must be inspected separately after the PR is opened.

The research-hygiene check only audits newly created 1.6 subjects and explicitly marked additions to earlier articles. Its source-count metadata is not a census of new independent research publications. It checks a local evidence contract, not that the attributed publication or the evidence itself has been independently assessed.

## What the checks do not establish

- A resolved link does not prove the interpretation in the linked article.
- A well-described source-access scope does not mean researchers read a restricted full text or obtained community consent.
- The source bibliography is a catalog of records consulted or inherited, not an index of independent peer-review endorsements.
- Laboratory isolate surveys, archaeological inference and community field narratives have distinct evidentiary scope.

## Related documentation

[Research update](research-update-1-6.md) · [Research method](methodology.md) · [Scope tracker](atlas-progress.md) · [Source supplement](../references/atlas-sources-1-6.md) · [Home](../index.md)
