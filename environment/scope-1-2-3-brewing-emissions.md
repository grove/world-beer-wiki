---
type: "Brewery GHG Inventory and Accounting Guide"
title: "Brewing Scope 1, 2 and 3 emissions should not be combined without definitions"
description: "Source-scoped heat, carbon, brewing process and wastewater evidence with explicit boundaries."
tags: [research-edition-1.19, energy-and-waste, evidence-boundaries]
status: draft
generated:
  by: world-beer-wiki/1.19
  at: "2026-10-28T14:00:00Z"
sources:
- id: v119-ghgfaq
  resource: "https://ghgprotocol.org/calculation-tools-faq"
  title: "GHG Protocol Calculation Tools FAQ: emissions scopes and biogenic reporting"
  author_label: "Greenhouse Gas Protocol / World Resources Institute"
  source_kind: "official-carbon-accounting-guidance"
  access_scope: "Full public accounting FAQ distinguishing scopes 1/2/3 and separately reported biogenic CO2 from biomass combustion; specific fermentation carbon-cycle calculation requires its own applicable guidance."
- id: v119-closed25
  resource: "https://link.springer.com/article/10.1007/s43621-025-01962-8"
  title: "Closed loop supply chains enable carbon reduction and resource circularity in the brewing industry (2025)"
  author_label: "Wu Hao, Liu Lijing, Qu Tianxiao and Kim Hae-young"
  source_kind: "open-supply-chain-lca-and-industrial-case-model"
  access_scope: "Full open published paper discussing Tsingtao operational measures, CO2 capture, packaging and reported Scope 1/2 changes; site data and upstream comparisons not independently audited."
- id: v119-baenergy26
  resource: "https://www.brewersassociation.org/playlist/sustainability-manuals/"
  title: "Sustainability Manuals: Energy Sustainability (9 June 2026)"
  author_label: "Brewers Association Sustainability Subcommittee"
  source_kind: "industry-energy-guidance-landing-page"
  access_scope: "Public Brewers Association directory discussing brewery energy management and greenhouse gas reduction; detailed manual content not separately verified."
regions:
- "Cross-regional"
scope: "Brewing Scope 1, 2 and 3 emissions should not be combined without definitions; interpretation of specified experiments, standards or institutional sources, not a universal performance or safety guarantee."
evidence_basis:
- "official-carbon-accounting-guidance"
- "open-supply-chain-lca-and-industrial-case-model"
- "industry-energy-guidance-landing-page"
source_checked_on: "2026-10-28"
review_note: "AI source-scoped draft; independent scientific, brewery engineering, community and food-safety review not performed."
relations:
- relation: compare_with
  target: categories/fermentation-co2-recovery-is-not-net-zero
- relation: compare_with
  target: environment/how-to-compare-brewing-footprints
- relation: compare_with
  target: environment/beer-packaging-transport-and-return-loops
---

# Brewing Scope 1, 2 and 3 emissions should not be combined without definitions

## One company's reduction needs an organizational boundary

The Greenhouse Gas Protocol defines Scope 1 as direct greenhouse gases from sources owned or controlled by the reporting organization, Scope 2 as indirect emissions from purchased energy, and Scope 3 as other indirect activity such as material supply, transportation and contracted disposal. A brewery can reduce gas-burner fuel while still needing to account for grid energy, barley cultivation and packaging.[^v119-ghgfaq]

Wu and colleagues' 2025 open Tsingtao case describes reported operational Scope 1/2 intensity changes alongside CO₂ recovery, water improvements and glass-loop measures. It also presents life-cycle hotspots beyond the production site. Those figures and scenarios belong to the studied system and have not been independently replicated here; a percentage change in **operational intensity** is not automatically an absolute whole-product-footprint reduction.[^v119-closed25]

The Brewers Association's Energy Sustainability directory gives industry-level guidance categories but does not expose site-specific audited GHG inventories in its public listing.[^v119-baenergy26]

## Keep the carbon arithmetic traceable

A source record should identify the organization and year, baseline, reporting units, output denominator, treatment of biogenic CO₂, electricity factors, purchased ingredients and transport coverage. If a paper says “net zero” without showing its boundary, record the claim as a stated aim rather than a demonstrated lifecycle fact. Compare [fermentation CO₂ recovery](../categories/fermentation-co2-recovery-is-not-net-zero.md), [LCA method boundaries](how-to-compare-brewing-footprints.md) and [transport packaging](beer-packaging-transport-and-return-loops.md).

## Explore connected subjects

- [fermentation co2 recovery is not net zero](../categories/fermentation-co2-recovery-is-not-net-zero.md)
- [how to compare brewing footprints](how-to-compare-brewing-footprints.md)
- [beer packaging transport and return loops](beer-packaging-transport-and-return-loops.md)

## Evidence boundary

The cited measurements and model estimates are not product or environmental certificates; no operational designs, microbiological treatments or local community viewpoints are independently validated in this article.

## Source notes

[^v119-ghgfaq]: [GHG Protocol Calculation Tools FAQ: emissions scopes and biogenic reporting](https://ghgprotocol.org/calculation-tools-faq). Greenhouse Gas Protocol / World Resources Institute. Checked 2026-10-28. Access: Full public accounting FAQ distinguishing scopes 1/2/3 and separately reported biogenic CO2 from biomass combustion; specific fermentation carbon-cycle calculation requires its own applicable guidance.

[^v119-closed25]: [Closed loop supply chains enable carbon reduction and resource circularity in the brewing industry (2025)](https://link.springer.com/article/10.1007/s43621-025-01962-8). Wu Hao, Liu Lijing, Qu Tianxiao and Kim Hae-young. Checked 2026-10-28. Access: Full open published paper discussing Tsingtao operational measures, CO2 capture, packaging and reported Scope 1/2 changes; site data and upstream comparisons not independently audited.

[^v119-baenergy26]: [Sustainability Manuals: Energy Sustainability (9 June 2026)](https://www.brewersassociation.org/playlist/sustainability-manuals/). Brewers Association Sustainability Subcommittee. Checked 2026-10-28. Access: Public Brewers Association directory discussing brewery energy management and greenhouse gas reduction; detailed manual content not separately verified.
