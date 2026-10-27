---
type: Implementation Progress Report
title: Atlas scope and progress
description: Atlas scope and progress
tags:
- wiki-documentation
- atlas
status: draft
generated:
  by: world-beer-wiki/1.2
  at: '2026-10-27T20:40:00Z'
sources:
- id: atlas-spec
  resource: /editorial/atlas-specification.md
  title: World Beer Atlas expansion specification
---

# Atlas scope and progress

**First installment: 11 implemented work items, 1 planned review item, 2 deferred features.** This is a finite implementation ledger, not a percentage of world beer knowledge covered. All researched articles remain drafts.

| ID | Deliverable | State | Entry points |
|---|---|---|---|
| ATLAS-001 | Scope and evidence contract | implemented | [editorial/atlas-specification.md](../editorial/atlas-specification.md) |
| ATLAS-002 | Cultural case studies | implemented | [culture/index.md](../culture/index.md) |
| ATLAS-003 | Calendar and historical events | implemented | [calendar/index.md](../calendar/index.md) |
| ATLAS-004 | Microbiology reference layer | implemented | [microbiology/index.md](../microbiology/index.md) |
| ATLAS-005 | Botanicals and adjuncts | implemented | [ingredients/juniper.md](../ingredients/juniper.md) · [ingredients/gesho.md](../ingredients/gesho.md) · [ingredients/coriander.md](../ingredients/coriander.md) · [ingredients/citrus-peel.md](../ingredients/citrus-peel.md) · [ingredients/lactose.md](../ingredients/lactose.md) · [ingredients/smoked-malt.md](../ingredients/smoked-malt.md) |
| ATLAS-006 | Brewing process explanations | implemented | [processes/index.md](../processes/index.md) |
| ATLAS-007 | Objects and serving practices | implemented | [objects/index.md](../objects/index.md) |
| ATLAS-008 | Stories and sensory reading routes | implemented | [stories/index.md](../stories/index.md) · [sensory/index.md](../sensory/index.md) |
| ATLAS-009 | Typed evidence-bearing relationships | implemented | [tools/atlas.py](../tools/atlas.py) · [editorial/reading-with-an-llm.md](../editorial/reading-with-an-llm.md) |
| ATLAS-010 | Offline exports, validation and tests | implemented | [tools/atlas.py](../tools/atlas.py) · [tests/test_atlas.py](../tests/test_atlas.py) · `.github/workflows/validate.yml` · [editorial/validation-report-1-2.md](../editorial/validation-report-1-2.md) |
| ATLAS-011 | Navigation and existing-profile integration | implemented | [index.md](../index.md) · [navigation/atlas.md](../navigation/atlas.md) · [references/atlas-sources.md](../references/atlas-sources.md) · [tools/build_site.py](../tools/build_site.py) |
| ATLAS-012 | Community and specialist review | planned | No completed deliverable asserted |
| ATLAS-013 | Licensed illustrations and pronunciation recordings | deferred | No completed deliverable asserted |
| ATLAS-014 | Optional interactive atlas and date-aware discovery | deferred | No completed deliverable asserted |

## What remains deliberately unfinished

Independent community, brewer, historian and microbiologist review has **not** occurred. Original-language checking, deeper coverage outside the initial case studies, botanical identification, compound-level sensory science, and additional primary-paper access remain research priorities. No images or audio were added without rights review. Live schedules, interactive maps and date-triggered features are deferred.

The [specification](atlas-specification.md) records each implemented item's precise delivered scope and the follow-on backlog. A new article does not automatically finish a broader region or topic. Reclassify an item only when its stated acceptance criteria are satisfied.

## Reproduce the ledger

```bash
python tools/atlas.py check --json
python tools/atlas.py progress
python tools/atlas.py catalog
```

The progress export reads the specification, while the catalog retains source access limits, article scope, review status, calendar records, relation qualifiers and reverse links. Neither export upgrades evidence quality.

[Research update](research-update-1-2.md) · [Validation](validation-report-1-2.md) · [Home](../index.md)
