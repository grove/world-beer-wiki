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

**Research edition 1.3: 20 implemented, 1 planned, 2 deferred work items.** These are bounded implementation deliverables, not a percentage of the world’s beer knowledge.

| ID | Deliverable | State | Entry point |
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
| ATLAS-010 | Offline exports, validation and tests | implemented | [tools/atlas.py](../tools/atlas.py) · [tests/test_atlas.py](../tests/test_atlas.py) · [.github/workflows/validate.yml](../.github/workflows/validate.yml) · [editorial/validation-report-1-2.md](../editorial/validation-report-1-2.md) |
| ATLAS-011 | Navigation and existing-profile integration | implemented | [index.md](../index.md) · [navigation/atlas.md](../navigation/atlas.md) · [references/atlas-sources.md](../references/atlas-sources.md) · [tools/build_site.py](../tools/build_site.py) |
| ATLAS-012 | Community and specialist review | planned | No completed deliverable asserted |
| ATLAS-013 | Licensed illustrations and pronunciation recordings | deferred | No completed deliverable asserted |
| ATLAS-014 | Optional interactive atlas and date-aware discovery | deferred | No completed deliverable asserted |
| ATLAS-015 | Focused history and archaeological context | implemented | [history/index.md](../history/index.md) |
| ATLAS-016 | Extended cultural and seasonal source research | implemented | [culture/index.md](../culture/index.md) |
| ATLAS-017 | Microbial genomes and fermentation ecology | implemented | [microbiology/index.md](../microbiology/index.md) |
| ATLAS-018 | Expanded grains, botanical materials and brewing processes | implemented | [ingredients/index.md](../ingredients/index.md) |
| ATLAS-019 | Historical stories, serving objects and sensory chemistry | implemented | [stories/index.md](../stories/index.md) |
| ATLAS-020 | More comparative family/category guides | implemented | [categories/index.md](../categories/index.md) |
| ATLAS-021 | Meaningful updates to canonical existing profiles | implemented | [navigation/atlas.md](../navigation/atlas.md) |
| ATLAS-022 | Source supplement, 1.3 release and reproducible quality checks | implemented | [references/atlas-sources-1-3.md](../references/atlas-sources-1-3.md) |
| ATLAS-023 | Date-aware offline event and season export | implemented | [tools/atlas.py](../tools/atlas.py) |

## What remains

**Independent human, community and specialist review has not occurred.** Edition 1.3 researched and added 55 sourced subject pages and improved fifteen existing profile/ingredient/category references. This is not independent historical verification; the reviewed-source access limitations remain in each article and the [1.3 supplement](../references/atlas-sources-1-3.md). Previously deferred licensed media and real-time interactive features remain deferred.

## Reproduce

```bash
python tools/validate_wiki.py --json
python tools/atlas.py check --json
python tools/atlas.py catalog
python tools/atlas.py progress
python tools/atlas.py timeline
python -m unittest discover -s tests -v
```

[Specification](atlas-specification.md) · [1.3 research update](research-update-1-3.md) · [Validation report](validation-report-1-3.md)
