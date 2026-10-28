---
type: Validation Report
title: World Beer Atlas edition 1.12 validation
status: draft
generated:
  by: world-beer-wiki/1.12
  at: '2026-10-28T08:00:00Z'
sources:
- id: release
  resource: /editorial/research-update-1-12.md
  title: Research edition 1.12 delivery record
---

# Edition 1.12 — validation report

This report records **local structural and source-hygiene checks**, not independent external fact checking. See the [research update](research-update-1-12.md), [full source provenance](../references/atlas-sources-1-12.md), and [open review tasks](source-review-queue-1-12.md).

## Reproduce the checks

```bash
python tools/validate_wiki.py --json
python tools/atlas.py check --json
python tools/research_quality.py --edition 1.12 --json
python tools/check_inventory.py --json
python tools/build_subject_index.py --check
python -m unittest discover -s tests -v
python tools/build_site.py
```

## Actual local validation results

Every check below ran against the **edition 1.12 local worktree on 28 October 2026**, before the GitHub upload.

| Test | Recorded result |
|---|---:|
| Markdown files validated / reachable from root | **662 / 662** |
| Subject articles | **579** |
| Source-footnote citations matched to definitions | **2,254** |
| Resolved internal Markdown link occurrences | **8,954** |
| Structured comparison / relation targets | **1,674** |
| Qualified evidence-bearing atlas relations | **68** |
| 1.12 researched subjects | **30** |
| 1.12 sourced revisions | **18** |
| 1.12 distinct external works | **15** |
| 1.12 source uses | **73** |
| Scope ledger work items | **86** (83 implemented, 1 planned, 2 deferred) |
| Automated regression tests | **122 passed** |
| Inventory and generated subject-index checks | **passed** |
| Website Markdown/navigation staging | **662 pages staged** |
| Broken links, invalid relations or metadata structural errors | **0** |

The optional local **MkDocs HTML build could not run** because `mkdocs` was not installed in the local environment; **GitHub's dedicated searchable-website workflow** provides an actual hosted HTML-build check when the PR runs. These separate results should not be conflated. The Python staging step completed without error.

### Validation that was and was not performed

`tools/validate_wiki.py`, `tools/atlas.py`, `tools/research_quality.py --edition 1.12`, `tools/check_inventory.py`, `tools/build_subject_index.py --check`, `unittest`, and `tools/build_site.py` all passed. The edition-specific source checker preserved the older 1.6–1.11 audits and confirmed article citations, notes and metadata. The source register has backlinks from all 15 distinct cited external works.

No check verifies legal history, field testimony, exact botanical species, food safety, cultural endorsement, health claims, external URL uptime, or that a full journal paper was accessible where the metadata says only an abstract was consulted. All articles remain research drafts. See the [open review queue](source-review-queue-1-12.md).

[Home](../index.md) · [Research update](research-update-1-12.md)
