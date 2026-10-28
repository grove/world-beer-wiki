---
type: Implementation Progress Report
title: Atlas scope and progress
description: Source-derived implementation ledger for World Beer Wiki edition 1.6.
tags: [wiki-documentation, atlas, progress]
status: draft
generated:
  by: world-beer-wiki/1.6
  at: '2026-10-28T05:40:00Z'
sources:
- id: atlas-spec
  resource: /editorial/atlas-specification.md
  title: World Beer Atlas expansion specification
---

# Atlas scope and progress

**Edition 1.6: 42 implemented, 1 planned, 2 deferred items** from the finite scope ledger. “Implemented” means the named deliverable exists, not independent verification, community approval or completion of world beer knowledge.

| ID | Workstream | State | Verified deliverable paths |
| --- | --- | --- | --- |
| ATLAS-001 | Scope and evidence contract | implemented | [atlas-specification.md](../editorial/atlas-specification.md) |
| ATLAS-002 | Cultural case studies | implemented | [index.md](../culture/index.md) |
| ATLAS-003 | Calendar and historical events | implemented | [index.md](../calendar/index.md) |
| ATLAS-004 | Microbiology reference layer | implemented | [index.md](../microbiology/index.md) |
| ATLAS-005 | Botanicals and adjuncts | implemented | [juniper.md](../ingredients/juniper.md) · [gesho.md](../ingredients/gesho.md) · [coriander.md](../ingredients/coriander.md) · [citrus-peel.md](../ingredients/citrus-peel.md) · [lactose.md](../ingredients/lactose.md) · [smoked-malt.md](../ingredients/smoked-malt.md) |
| ATLAS-006 | Brewing process explanations | implemented | [index.md](../processes/index.md) |
| ATLAS-007 | Objects and serving practices | implemented | [index.md](../objects/index.md) |
| ATLAS-008 | Stories and sensory reading routes | implemented | [index.md](../stories/index.md) · [index.md](../sensory/index.md) |
| ATLAS-009 | Typed evidence-bearing relationships | implemented | [atlas.py](../tools/atlas.py) · [reading-with-an-llm.md](../editorial/reading-with-an-llm.md) |
| ATLAS-010 | Offline exports, validation and tests | implemented | [atlas.py](../tools/atlas.py) · [test_atlas.py](../tests/test_atlas.py) · [validate.yml](https://github.com/grove/world-beer-wiki/blob/main/.github/workflows/validate.yml) · [validation-report-1-2.md](../editorial/validation-report-1-2.md) |
| ATLAS-011 | Navigation and existing-profile integration | implemented | [index.md](../index.md) · [atlas.md](../navigation/atlas.md) · [atlas-sources.md](../references/atlas-sources.md) · [build_site.py](../tools/build_site.py) |
| ATLAS-012 | Community and specialist review | planned | No completed deliverable asserted |
| ATLAS-013 | Licensed illustrations and pronunciation recordings | deferred | No completed deliverable asserted |
| ATLAS-014 | Optional interactive atlas and date-aware discovery | deferred | No completed deliverable asserted |
| ATLAS-015 | Focused history and archaeological context | implemented | [index.md](../history/index.md) |
| ATLAS-016 | Extended cultural and seasonal source research | implemented | [index.md](../culture/index.md) |
| ATLAS-017 | Microbial genomes and fermentation ecology | implemented | [index.md](../microbiology/index.md) |
| ATLAS-018 | Expanded grains, botanical materials and brewing processes | implemented | [index.md](../ingredients/index.md) |
| ATLAS-019 | Historical stories, serving objects and sensory chemistry | implemented | [index.md](../stories/index.md) |
| ATLAS-020 | More comparative family/category guides | implemented | [index.md](../categories/index.md) |
| ATLAS-021 | Meaningful updates to canonical existing profiles | implemented | [atlas.md](../navigation/atlas.md) |
| ATLAS-022 | Source supplement, 1.3 release and reproducible quality checks | implemented | [atlas-sources-1-3.md](../references/atlas-sources-1-3.md) |
| ATLAS-023 | Date-aware offline event and season export | implemented | [atlas.py](../tools/atlas.py) |
| ATLAS-024 | Broaden culturally located social and ritual accounts | implemented | [index.md](../culture/index.md) |
| ATLAS-025 | Expand archeological and industrial-science histories | implemented | [index.md](../history/index.md) |
| ATLAS-026 | Introduce climate and environmental research section | implemented | [index.md](../environment/index.md) |
| ATLAS-027 | Introduce evidence-based food pairing section | implemented | [index.md](../food/index.md) |
| ATLAS-028 | Deepen fermentation, chemistry, beer stability and serving | implemented | [index.md](../sensory/index.md) |
| ATLAS-029 | Revise canonical existing pages using new research | implemented | [pito.md](../styles/pito.md) |
| ATLAS-030 | Publish source provenance, tests and edition documentation | implemented | [atlas-sources-1-4.md](../references/atlas-sources-1-4.md) |
| ATLAS-031 | Improve queryable provenance and data checks | implemented | [atlas.py](../tools/atlas.py) |
| ATLAS-032 | Cerro Baúl archaeology, materials and social context | implemented | [cerro-baul-wari-brewery.md](../history/cerro-baul-wari-brewery.md) · [wari-brewing-and-state-hospitality.md](../culture/wari-brewing-and-state-hospitality.md) · [wari-brewing-vats-and-kero-cups.md](../objects/wari-brewing-vats-and-kero-cups.md) |
| ATLAS-033 | Documented labor, medieval trade and contemporary US voices | implemented | [medieval-england-brewsters-and-change.md](../history/medieval-england-brewsters-and-change.md) · [american-beer-oral-histories.md](../culture/american-beer-oral-histories.md) · [peoples-brewing-and-ownership.md](../history/peoples-brewing-and-ownership.md) |
| ATLAS-034 | Mixed starters in Asian traditions and African isolate research | implemented | [himalayan-dry-starter-diversity.md](../microbiology/himalayan-dry-starter-diversity.md) · [vietnamese-banh-men-communities.md](../microbiology/vietnamese-banh-men-communities.md) · [non-saccharomyces-yeasts-in-abidjan-sorghum-beer.md](../microbiology/non-saccharomyces-yeasts-in-abidjan-sorghum-beer.md) |
| ATLAS-035 | Botanicals, perception, food and research-stage uncertainty | implemented | [schinus-molle-in-andean-ferments.md](../ingredients/schinus-molle-in-andean-ferments.md) · [bitterness-is-not-one-number.md](../sensory/bitterness-is-not-one-number.md) · [situational-pairing-and-storage-evidence.md](../food/situational-pairing-and-storage-evidence.md) |
| ATLAS-036 | Edition-aware current style guideline comparison | implemented | [bjcp-2021-versus-ba-2026.md](../categories/bjcp-2021-versus-ba-2026.md) · [one-title-two-guidelines.md](../stories/one-title-two-guidelines.md) |
| ATLAS-037 | Complete source-derived subject directory and stale-index regression check | implemented | [all-atlas-subjects.md](../navigation/all-atlas-subjects.md) · [build_subject_index.py](../tools/build_subject_index.py) · [test_subject_index.py](../tests/test_subject_index.py) |
| ATLAS-038 | Source register, review queue and existing-article research integration | implemented | [atlas-sources-1-5.md](../references/atlas-sources-1-5.md) · [source-review-queue-1-5.md](../editorial/source-review-queue-1-5.md) · [research-update-1-5.md](../editorial/research-update-1-5.md) |
| ATLAS-039 | Document banana-based ferments and community-named Assam rice drinks | implemented | [tonto.md](../styles/tonto.md) · [urugwa.md](../styles/urugwa.md) · [hor-alank.md](../styles/hor-alank.md) · [zu-hmar.md](../styles/zu-hmar.md) |
| ATLAS-040 | Research situated cultural learning and non-fixed ceremonial timing | implemented | [southern-assam-five-beverage-study.md](../culture/southern-assam-five-beverage-study.md) · [sahti-apprenticeship-and-celebration.md](../culture/sahti-apprenticeship-and-celebration.md) · [mapuche-fermented-drinks-and-source-voices.md](../culture/mapuche-fermented-drinks-and-source-voices.md) · [sahti-occasions-without-a-fixed-date.md](../calendar/sahti-occasions-without-a-fixed-date.md) |
| ATLAS-041 | Deepen microbial survey interpretation and farmhouse population studies | implemented | [assam-rice-ferment-sampling.md](../microbiology/assam-rice-ferment-sampling.md) · [umqombothi-amplicons-and-predicted-function.md](../microbiology/umqombothi-amplicons-and-predicted-function.md) · [kveik-population-history-2026.md](../microbiology/kveik-population-history-2026.md) · [hop-resistant-lactic-acid-bacteria.md](../microbiology/hop-resistant-lactic-acid-bacteria.md) · [maltose-negative-yeast-and-low-alcohol.md](../microbiology/maltose-negative-yeast-and-low-alcohol.md) |
| ATLAS-042 | Connect materials, processes, sensory pathways, objects and historical inference | implemented | [rhynchosia-root-for-munkoyo.md](../ingredients/rhynchosia-root-for-munkoyo.md) · [banana-juice.md](../ingredients/banana-juice.md) · [ferulic-acid-in-wort.md](../ingredients/ferulic-acid-in-wort.md) · [munkoyo-root-starch-conversion.md](../processes/munkoyo-root-starch-conversion.md) · [clove-aroma-and-4-vinylguaiacol.md](../sensory/clove-aroma-and-4-vinylguaiacol.md) · [assam-earthen-pots-and-covers.md](../objects/assam-earthen-pots-and-covers.md) |
| ATLAS-043 | Separate environmental LCA units and system boundaries | implemented | [mexican-microbrewery-footprint-case.md](../environment/mexican-microbrewery-footprint-case.md) · [japanese-small-brewery-lca-case.md](../environment/japanese-small-brewery-lca-case.md) |
| ATLAS-044 | Integrate new citations into existing research and review queue | implemented | [munkoyo.md](../styles/munkoyo.md) · [umqombothi.md](../styles/umqombothi.md) · [kveik.md](../ingredients/kveik.md) · [atlas-sources-1-6.md](../references/atlas-sources-1-6.md) · [source-review-queue-1-6.md](../editorial/source-review-queue-1-6.md) |
| ATLAS-045 | Add offline editorial hygiene checks and edition 1.6 reproducibility | implemented | [research_quality.py](../tools/research_quality.py) · [test_research_quality.py](../tests/test_research_quality.py) · [validation-report-1-6.md](../editorial/validation-report-1-6.md) · [all-atlas-subjects.md](../navigation/all-atlas-subjects.md) |

## Edition 1.6 delivery

The research adds [30 new source-scoped subject articles](../editorial/research-update-1-6.md), 22 extensions to established subjects, and a reproducible [source provenance supplement](../references/atlas-sources-1-6.md). The new offline quality checker verifies access-scope metadata and referenced footnotes; it is **not** a peer review.

## Work deliberately incomplete

**ATLAS-012 — independent community and specialist review** remains planned. Neither primary paper metadata nor an AI citation check documents permission to republish restricted knowledge or validates community practices. Local-language corrections, fuller access to abstract-only studies, and individual brewer/historian/microbiologist review remain high priorities. Licensed media and an interactive live calendar remain deferred under ATLAS-013 and ATLAS-014.

## Reproduce current results

```bash
python tools/validate_wiki.py --json
python tools/atlas.py check --json
python tools/research_quality.py --json
python tools/build_subject_index.py --check
python -m unittest discover -s tests -v
python tools/build_site.py
```

[Specification](atlas-specification.md) · [Research update](research-update-1-6.md) · [Source review queue](source-review-queue-1-6.md) · [Validation report](validation-report-1-6.md) · [Home](../index.md)
