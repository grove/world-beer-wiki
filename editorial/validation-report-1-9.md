---
type: Editorial Validation Report
title: Research edition 1.9 validation and reproducibility
description: Reproducible checks, tested scope and limits for the 1.9 release.
tags: [wiki-documentation, research, edition-1-9]
status: draft
generated:
  by: world-beer-wiki/1.9
  at: '2026-10-28T07:35:00Z'
sources:
- id: atlas-spec
  resource: /editorial/atlas-specification.md
  title: World Beer Atlas expansion specification
---

# Research edition 1.9 — reproducible validation

This report records local validation **after** the 1.9 research and navigation changes. It will not claim externally verified source accuracy, community consent, or human expert review. GitHub Actions results must be assessed separately on the PR commit.

## Recorded checks

All values below were observed from local checks on the 1.9 candidate tree (Python 3 and PyYAML); they describe structure and local editorial hygiene only.

| Local check | Observed result |
|---|---:|
| Markdown files reachable from `index.md` | **556 / 556** |
| Subject articles across 13 sections | **488** |
| Internal link occurrences resolved | **7,638** |
| Structured relations with targets and text links | **1,336** |
| Evidence-bearing qualified relations | **67** |
| Footnote citations matched to source metadata and definitions | **1,880** |
| Distinct source IDs in all pages | **542** |
| Cross-section source-audit records | **497** |
| Sources lacking access descriptions | **0** |
| Edition 1.9 new / revised subjects | **31 / 18** |
| Edition 1.9 distinct named sources / usage records | **18 / 79** |
| Specification work items | **66** |
| Python regression tests | **80 passed** |
| Markdown pages staged for the optional website | **556 / 556** |
| Structural validation errors | **0** |

The updated edition 1.9 checker tests source attribution, actual explanatory citation use, source-access limits, draft status, useful internal links and independent-review boundaries. Checks for editions 1.6, 1.7 and 1.8 remain operational. The subject index is regenerated from frontmatter and checked byte-for-byte; website staging is not itself an HTML-rendering result.

## Reproduce

```bash
python tools/validate_wiki.py --json
python tools/atlas.py check --json
python tools/atlas.py source-audit
python tools/research_quality.py --edition 1.6 --json
python tools/research_quality.py --edition 1.7 --json
python tools/research_quality.py --edition 1.8 --json
python tools/research_quality.py --edition 1.9 --json
python tools/build_subject_index.py --check
python -m unittest discover -s tests -q
python tools/build_site.py
```

## Limitations

Local checks confirm metadata, links and citation **presence**, not the truth of the cited claim. A heritage report is not endorsement by every member of the named community; a lab result for a selected ferment is not a general recipe. Historical transcriptions, dated law and calendar claims retain their stated source-access boundaries. Independent review under [ATLAS-012](atlas-specification.md) remains planned.

[Research update](research-update-1-9.md) · [Source register](../references/atlas-sources-1-9.md) · [Review queue](source-review-queue-1-9.md) · [Home](../index.md)
