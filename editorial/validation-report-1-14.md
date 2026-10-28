---
type: Editorial Validation Report
title: Edition 1.14 validation report
description: Edition 1.14 validation report
tags:
- wiki-documentation
- edition-1.14
- validation
status: draft
generated:
  by: world-beer-wiki/1.14
  at: '2026-10-28T11:20:00Z'
sources:
- id: atlas-spec
  resource: /editorial/atlas-specification.md
  title: World Beer Atlas expansion specification
---


# Edition 1.14 — validation and limitations

This report describes **checks actually performed** on the edition 1.14 worktree. It is a structural and editorial integrity report, not an independent source audit, historical fact check, consumer safety test or community approval. Previous release reports remain unchanged.

| Validation | Measured result |
| --- | ---: |
| Markdown pages reachable from the root | 736 / 736 |
| Subject articles in 13 reference sections | 643 |
| Resolved local Markdown link occurrences | 10,327 |
| Structured article relations and body links | 1,934 |
| Qualified factual relations overall | 101 |
| Citation references matched to local source records | 2,558 |
| Calendar metadata records | 24 |
| Edition 1.14 new subjects | 29 |
| Edition 1.14 substantive revisions | 18 |
| New distinct source records / locally attributed uses | 15 / 70 |
| Offline regression tests | 149 passed |
| Offline structural errors | 0 |

The generated [all-subjects index](../navigation/all-atlas-subjects.md) and [names index](../navigation/all-names.md) are checked against the source articles. The [subject inventory](../navigation/all-atlas-subjects.md) is consistent with the README and root home. The searchable-site staging step included **736 pages**. Staging is not itself a claim that HTML deployed; GitHub's separate website workflow provides that check.

## Offline commands

```bash
python tools/validate_wiki.py --json
python tools/atlas.py check --json
python tools/research_quality.py --edition 1.14 --json
python tools/check_inventory.py --json
python -m unittest discover -s tests -v
python tools/build_site.py
python tools/build_subject_index.py --check
python tools/build_names_index.py --check
python tools/atlas.py catalog
python tools/atlas.py progress
python tools/atlas.py timeline
python tools/atlas.py source-audit
```

## What these checks do not demonstrate

An accessible abstract or a historical producer narrative is not the same as reading contemporaneous records or raw experimental data. A well-formed citation is not independent corroboration; a test of a microbial model is not a food-safety certification. No source-verified statement here implies that Belgian, Ethiopian, Czech or English makers reviewed this edition. The [edition review queue](source-review-queue-1-14.md) tracks remaining specialist and community work.

[Research update](research-update-1-14.md) · [Source register](../references/atlas-sources-1-14.md) · [Specification](atlas-specification.md) · [Home](../index.md).
