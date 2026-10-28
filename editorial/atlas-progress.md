---
type: Implementation Progress Report
title: Atlas scope and progress
description: Source-derived finite scope ledger for World Beer Atlas edition 1.7.
tags:
- wiki-documentation
- atlas
- progress
status: draft
generated:
  by: world-beer-wiki/1.8
  at: '2026-10-28T07:55:00Z'
sources:
- id: atlas-spec
  resource: /editorial/atlas-specification.md
  title: World Beer Atlas expansion specification
---

# Atlas scope and progress

**Edition 1.8: 56 implemented, 1 planned, 2 deferred** items from the finite scope ledger. An implemented item means its stated file-level deliverable exists, not that a region has been exhaustively covered or independently verified.

| ID | Workstream | Status | Reproducible deliverable paths |
|---|---|---|---|
| ATLAS-001 | Scope and evidence contract | implemented | [atlas-specification.md](../editorial/atlas-specification.md) |
| ATLAS-002 | Cultural case studies | implemented | [index.md](../culture/index.md) |
| ATLAS-003 | Calendar and historical events | implemented | [index.md](../calendar/index.md) |
| ATLAS-004 | Microbiology reference layer | implemented | [index.md](../microbiology/index.md) |
| ATLAS-005 | Botanicals and adjuncts | implemented | [juniper.md](../ingredients/juniper.md) · [gesho.md](../ingredients/gesho.md) · [coriander.md](../ingredients/coriander.md) · [citrus-peel.md](../ingredients/citrus-peel.md) · [lactose.md](../ingredients/lactose.md) · [smoked-malt.md](../ingredients/smoked-malt.md) |
| ATLAS-006 | Brewing process explanations | implemented | [index.md](../processes/index.md) |
| ATLAS-007 | Objects and serving practices | implemented | [index.md](../objects/index.md) |
| ATLAS-008 | Stories and sensory reading routes | implemented | [index.md](../stories/index.md) · [index.md](../sensory/index.md) |
| ATLAS-009 | Typed evidence-bearing relationships | implemented | `tools/atlas.py` · [reading-with-an-llm.md](../editorial/reading-with-an-llm.md) |
| ATLAS-010 | Offline exports, validation and tests | implemented | `tools/atlas.py` · `tests/test_atlas.py` · `.github/workflows/validate.yml` · [validation-report-1-2.md](../editorial/validation-report-1-2.md) |
| ATLAS-011 | Navigation and existing-profile integration | implemented | [index.md](../index.md) · [atlas.md](../navigation/atlas.md) · [atlas-sources.md](../references/atlas-sources.md) · `tools/build_site.py` |
| ATLAS-012 | Community and specialist review | planned | Not completed |
| ATLAS-013 | Licensed illustrations and pronunciation recordings | deferred | Not completed |
| ATLAS-014 | Optional interactive atlas and date-aware discovery | deferred | Not completed |
| ATLAS-015 | Focused history and archaeological context | implemented | [index.md](../history/index.md) |
| ATLAS-016 | Extended cultural and seasonal source research | implemented | [index.md](../culture/index.md) |
| ATLAS-017 | Microbial genomes and fermentation ecology | implemented | [index.md](../microbiology/index.md) |
| ATLAS-018 | Expanded grains, botanical materials and brewing processes | implemented | [index.md](../ingredients/index.md) |
| ATLAS-019 | Historical stories, serving objects and sensory chemistry | implemented | [index.md](../stories/index.md) |
| ATLAS-020 | More comparative family/category guides | implemented | [index.md](../categories/index.md) |
| ATLAS-021 | Meaningful updates to canonical existing profiles | implemented | [atlas.md](../navigation/atlas.md) |
| ATLAS-022 | Source supplement, 1.3 release and reproducible quality checks | implemented | [atlas-sources-1-3.md](../references/atlas-sources-1-3.md) |
| ATLAS-023 | Date-aware offline event and season export | implemented | `tools/atlas.py` |
| ATLAS-024 | Broaden culturally located social and ritual accounts | implemented | [index.md](../culture/index.md) |
| ATLAS-025 | Expand archeological and industrial-science histories | implemented | [index.md](../history/index.md) |
| ATLAS-026 | Introduce climate and environmental research section | implemented | [index.md](../environment/index.md) |
| ATLAS-027 | Introduce evidence-based food pairing section | implemented | [index.md](../food/index.md) |
| ATLAS-028 | Deepen fermentation, chemistry, beer stability and serving | implemented | [index.md](../sensory/index.md) |
| ATLAS-029 | Revise canonical existing pages using new research | implemented | [pito.md](../styles/pito.md) |
| ATLAS-030 | Publish source provenance, tests and edition documentation | implemented | [atlas-sources-1-4.md](../references/atlas-sources-1-4.md) |
| ATLAS-031 | Improve queryable provenance and data checks | implemented | `tools/atlas.py` |
| ATLAS-032 | Cerro Baúl archaeology, materials and social context | implemented | [cerro-baul-wari-brewery.md](../history/cerro-baul-wari-brewery.md) · [wari-brewing-and-state-hospitality.md](../culture/wari-brewing-and-state-hospitality.md) · [wari-brewing-vats-and-kero-cups.md](../objects/wari-brewing-vats-and-kero-cups.md) |
| ATLAS-033 | Documented labor, medieval trade and contemporary US voices | implemented | [medieval-england-brewsters-and-change.md](../history/medieval-england-brewsters-and-change.md) · [american-beer-oral-histories.md](../culture/american-beer-oral-histories.md) · [peoples-brewing-and-ownership.md](../history/peoples-brewing-and-ownership.md) |
| ATLAS-034 | Mixed starters in Asian traditions and African isolate research | implemented | [himalayan-dry-starter-diversity.md](../microbiology/himalayan-dry-starter-diversity.md) · [vietnamese-banh-men-communities.md](../microbiology/vietnamese-banh-men-communities.md) · [non-saccharomyces-yeasts-in-abidjan-sorghum-beer.md](../microbiology/non-saccharomyces-yeasts-in-abidjan-sorghum-beer.md) |
| ATLAS-035 | Botanicals, perception, food and research-stage uncertainty | implemented | [schinus-molle-in-andean-ferments.md](../ingredients/schinus-molle-in-andean-ferments.md) · [bitterness-is-not-one-number.md](../sensory/bitterness-is-not-one-number.md) · [situational-pairing-and-storage-evidence.md](../food/situational-pairing-and-storage-evidence.md) |
| ATLAS-036 | Edition-aware current style guideline comparison | implemented | [bjcp-2021-versus-ba-2026.md](../categories/bjcp-2021-versus-ba-2026.md) · [one-title-two-guidelines.md](../stories/one-title-two-guidelines.md) |
| ATLAS-037 | Complete source-derived subject directory and stale-index regression check | implemented | [all-atlas-subjects.md](../navigation/all-atlas-subjects.md) · `tools/build_subject_index.py` · `tests/test_subject_index.py` |
| ATLAS-038 | Source register, review queue and existing-article research integration | implemented | [atlas-sources-1-5.md](../references/atlas-sources-1-5.md) · [source-review-queue-1-5.md](../editorial/source-review-queue-1-5.md) · [research-update-1-5.md](../editorial/research-update-1-5.md) |
| ATLAS-039 | Document banana-based ferments and community-named Assam rice drinks | implemented | [tonto.md](../styles/tonto.md) · [urugwa.md](../styles/urugwa.md) · [hor-alank.md](../styles/hor-alank.md) · [zu-hmar.md](../styles/zu-hmar.md) |
| ATLAS-040 | Research situated cultural learning and non-fixed ceremonial timing | implemented | [southern-assam-five-beverage-study.md](../culture/southern-assam-five-beverage-study.md) · [sahti-apprenticeship-and-celebration.md](../culture/sahti-apprenticeship-and-celebration.md) · [mapuche-fermented-drinks-and-source-voices.md](../culture/mapuche-fermented-drinks-and-source-voices.md) · [sahti-occasions-without-a-fixed-date.md](../calendar/sahti-occasions-without-a-fixed-date.md) |
| ATLAS-041 | Deepen microbial survey interpretation and farmhouse population studies | implemented | [assam-rice-ferment-sampling.md](../microbiology/assam-rice-ferment-sampling.md) · [umqombothi-amplicons-and-predicted-function.md](../microbiology/umqombothi-amplicons-and-predicted-function.md) · [kveik-population-history-2026.md](../microbiology/kveik-population-history-2026.md) · [hop-resistant-lactic-acid-bacteria.md](../microbiology/hop-resistant-lactic-acid-bacteria.md) · [maltose-negative-yeast-and-low-alcohol.md](../microbiology/maltose-negative-yeast-and-low-alcohol.md) |
| ATLAS-042 | Connect materials, processes, sensory pathways, objects and historical inference | implemented | [rhynchosia-root-for-munkoyo.md](../ingredients/rhynchosia-root-for-munkoyo.md) · [banana-juice.md](../ingredients/banana-juice.md) · [ferulic-acid-in-wort.md](../ingredients/ferulic-acid-in-wort.md) · [munkoyo-root-starch-conversion.md](../processes/munkoyo-root-starch-conversion.md) · [clove-aroma-and-4-vinylguaiacol.md](../sensory/clove-aroma-and-4-vinylguaiacol.md) · [assam-earthen-pots-and-covers.md](../objects/assam-earthen-pots-and-covers.md) |
| ATLAS-043 | Separate environmental LCA units and system boundaries | implemented | [mexican-microbrewery-footprint-case.md](../environment/mexican-microbrewery-footprint-case.md) · [japanese-small-brewery-lca-case.md](../environment/japanese-small-brewery-lca-case.md) |
| ATLAS-044 | Integrate new citations into existing research and review queue | implemented | [munkoyo.md](../styles/munkoyo.md) · [umqombothi.md](../styles/umqombothi.md) · [kveik.md](../ingredients/kveik.md) · [atlas-sources-1-6.md](../references/atlas-sources-1-6.md) · [source-review-queue-1-6.md](../editorial/source-review-queue-1-6.md) |
| ATLAS-045 | Add offline editorial hygiene checks and edition 1.6 reproducibility | implemented | `tools/research_quality.py` · `tests/test_research_quality.py` · [validation-report-1-6.md](../editorial/validation-report-1-6.md) · [all-atlas-subjects.md](../navigation/all-atlas-subjects.md) |
| ATLAS-046 | Investigate Abydos early royal brewery and excavation interpretation | implemented | [abydos-early-royal-brewery.md](../history/abydos-early-royal-brewery.md) · [abydos-vats-and-fire-legs.md](../objects/abydos-vats-and-fire-legs.md) · [the-brewery-once-called-a-kiln.md](../stories/the-brewery-once-called-a-kiln.md) |
| ATLAS-047 | Differentiate Andean household chicha, local service calendars and archival histories | implemented | [piura-chicheras-and-household-sales.md](../culture/piura-chicheras-and-household-sales.md) · [piura-chicha-sales-days.md](../calendar/piura-chicha-sales-days.md) · [piura-chicha-white-flags.md](../objects/piura-chicha-white-flags.md) · [arequipa-chicherias-colonial-republican-records.md](../history/arequipa-chicherias-colonial-republican-records.md) |
| ATLAS-048 | Broaden Ghanaian, Ethiopian and Japanese brewing social research | implemented | [ghana-pito-bars-migration-and-identity.md](../culture/ghana-pito-bars-migration-and-identity.md) · [ghana-pito-women-enterprise-survey.md](../culture/ghana-pito-women-enterprise-survey.md) · [tella-hospitality-and-household-economy.md](../culture/tella-hospitality-and-household-economy.md) · [japanese-koji-sake-heritage-and-apprenticeship.md](../culture/japanese-koji-sake-heritage-and-apprenticeship.md) |
| ATLAS-049 | Explain Philippine tapuy, bubod and parallel mixed fermentation | implemented | [tapuy-philippine-rice-ferment.md](../styles/tapuy-philippine-rice-ferment.md) · [bubod-starter.md](../ingredients/bubod-starter.md) · [bubod-tapuy-isolate-study.md](../microbiology/bubod-tapuy-isolate-study.md) · [parallel-starch-and-alcohol-fermentation.md](../processes/parallel-starch-and-alcohol-fermentation.md) · [koji-sake-and-rice-ferment-boundaries.md](../categories/koji-sake-and-rice-ferment-boundaries.md) |
| ATLAS-050 | Deepen spoilage microbiology and dynamic sensory chemistry | implemented | [hora-horc-and-hop-resistance-markers.md](../microbiology/hora-horc-and-hop-resistance-markers.md) · [craft-brewery-filling-line-microbes.md](../microbiology/craft-brewery-filling-line-microbes.md) · [vicinal-diketones-as-moving-target.md](../sensory/vicinal-diketones-as-moving-target.md) |
| ATLAS-051 | Compare environment and sensory research with reproducible evidence boundaries | implemented | [beer-packaging-transport-and-return-loops.md](../environment/beer-packaging-transport-and-return-loops.md) · [spent-grain-food-safety-and-circularity.md](../environment/spent-grain-food-safety-and-circularity.md) · [cheese-beer-preference-is-not-a-rule.md](../food/cheese-beer-preference-is-not-a-rule.md) |
| ATLAS-052 | Improve gender-history comparisons, narrative trails and original articles | implemented | [gender-and-brewing-what-the-sources-show.md](../categories/gender-and-brewing-what-the-sources-show.md) · [brewsters-household-labor-in-medieval-england.md](../history/brewsters-household-labor-in-medieval-england.md) · [ale-tasters-and-brewster-protests.md](../history/ale-tasters-and-brewster-protests.md) · [edition-1-7-reading-trails.md](../navigation/edition-1-7-reading-trails.md) |
| ATLAS-053 | Maintain source provenance, research hygiene and edition navigation | implemented | [atlas-sources-1-7.md](../references/atlas-sources-1-7.md) · `tools/research_quality.py` · `tests/test_research_quality_v17.py` · [research-update-1-7.md](../editorial/research-update-1-7.md) · [validation-report-1-7.md](../editorial/validation-report-1-7.md) |

| ATLAS-054 | Shawi cassava fermentation and cultural evidence | implemented | [shawi-masato-and-water.md](../culture/shawi-masato-and-water.md) · [shawi-masato-preparation.md](../processes/shawi-masato-preparation.md) |
| ATLAS-055 | Mbege process, botanical input and contextual ritual evidence | implemented | [mbege-as-regional-knowledge.md](../culture/mbege-as-regional-knowledge.md) · [mbege-nyalu-and-mso.md](../processes/mbege-nyalu-and-mso.md) · [msesewe-stem-bark-in-mbege.md](../ingredients/msesewe-stem-bark-in-mbege.md) · [chagga-ritual-beer-in-rombo.md](../culture/chagga-ritual-beer-in-rombo.md) |
| ATLAS-056 | Ethiopian food-drinks and Himalayan millet ecology | implemented | [borde-ethiopian-fermented-cereal.md](../styles/borde-ethiopian-fermented-cereal.md) · [shamita-ethiopian-fermented-barley.md](../styles/shamita-ethiopian-fermented-barley.md) · [jaanr-microbial-succession.md](../microbiology/jaanr-microbial-succession.md) |
| ATLAS-057 | Beer foam proteins and aging chemistry | implemented | [beer-foam-active-proteins.md](../ingredients/beer-foam-active-proteins.md) · [heat-ltp1-and-beer-foam.md](../sensory/heat-ltp1-and-beer-foam.md) · [beer-staling-and-aldehydes.md](../sensory/beer-staling-and-aldehydes.md) |
| ATLAS-058 | Hop chemistry, yeast effects and source-to-aroma uncertainty | implemented | [polyfunctional-thiol-precursors.md](../ingredients/polyfunctional-thiol-precursors.md) · [thiol-release-and-yeast-timing.md](../microbiology/thiol-release-and-yeast-timing.md) · [hop-terpenoid-biotransformation.md](../sensory/hop-terpenoid-biotransformation.md) |
| ATLAS-059 | Evidence QA, indexes, research register and reading trails | implemented | [atlas-sources-1-8.md](../references/atlas-sources-1-8.md) · [research-update-1-8.md](../editorial/research-update-1-8.md) · [validation-report-1-8.md](../editorial/validation-report-1-8.md) · [edition-1-8-reading-trails.md](../navigation/edition-1-8-reading-trails.md) · `tests/test_research_quality_v18.py` |

## What remains unverified

**ATLAS-012**, independent community and specialist review, is still planned. Source access from a publisher abstract or a project narrative is not equivalent to reading all underlying records; an archival citation cannot certify the account’s representativeness. Licensed illustrations/recordings and a live interactive calendar remain deferred. The [edition 1.7 review queue](source-review-queue-1-7.md) and [earlier 1.6 queue](source-review-queue-1-6.md) identify specific work.

## Machine-readable check

`python tools/atlas.py progress` exports this finite ledger without inventing a worldwide completeness percentage. `python tools/atlas.py check` verifies declared delivered files; `python tools/research_quality.py --edition 1.7` checks local source hygiene. All remain independent of actual external professional validation.

[Specification](atlas-specification.md) · [Research update](research-update-1-7.md) · [Validation](validation-report-1-7.md) · [All subjects](../navigation/all-atlas-subjects.md)

## Edition 1.8 delivered scope

29 source-bounded articles and 14 original-article additions; 6 finite ledger items. All community and scientific peer review remains uncompleted. [Research update](research-update-1-8.md) · [Sources](../references/atlas-sources-1-8.md) · [Independent-review queue](source-review-queue-1-8.md).
