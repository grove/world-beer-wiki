---
type: "Beer Energy and Accounting Category Guide"
title: "A brewery's heat use, cooling load and climate impact are different numbers"
description: "Source-scoped heat, carbon, brewing process and wastewater evidence with explicit boundaries."
tags: [research-edition-1.19, energy-and-waste, evidence-boundaries]
status: draft
generated:
  by: world-beer-wiki/1.19
  at: "2026-10-28T14:00:00Z"
sources:
- id: v119-pinch26
  resource: "https://orbit.dtu.dk/en/publications/generalized-electrification-solutions-for-breweries-a-pinch-analy/"
  title: "Generalized electrification solutions for breweries: Pinch Analysis and heat pump integration (2026)"
  author_label: "Roger Padullés, Martin Pihl Andersen, Niklas Bagge Mogensen and colleagues"
  source_kind: "open-peer-reviewed-brewery-thermal-system-model"
  access_scope: "Full public Danish Technical University research entry and journal abstract; final CC BY article linked, but design inputs were not independently re-calculated. Generalized brewery model, not measured results at every plant."
- id: v119-heatglobal25
  resource: "https://www.sciencedirect.com/science/article/pii/S0360544225018262"
  title: "Electrification and decarbonization in global brewing industry driven by industrial heat pumps (2025)"
  author_label: "Zhongyi Liu, Bin Hu, Di Wu and Ruzhu Wang"
  source_kind: "peer-reviewed-global-techno-economic-model-abstract"
  access_scope: "Public publisher abstract of a global sector model under assumed boiler and electricity scenarios; article full methods not independently read. Potential avoided emissions are model outputs, not measured reductions."
- id: v119-ghgfaq
  resource: "https://ghgprotocol.org/calculation-tools-faq"
  title: "GHG Protocol Calculation Tools FAQ: emissions scopes and biogenic reporting"
  author_label: "Greenhouse Gas Protocol / World Resources Institute"
  source_kind: "official-carbon-accounting-guidance"
  access_scope: "Full public accounting FAQ distinguishing scopes 1/2/3 and separately reported biogenic CO2 from biomass combustion; specific fermentation carbon-cycle calculation requires its own applicable guidance."
regions:
- "Cross-regional"
scope: "A brewery's heat use, cooling load and climate impact are different numbers; interpretation of specified experiments, standards or institutional sources, not a universal performance or safety guarantee."
evidence_basis:
- "open-peer-reviewed-brewery-thermal-system-model"
- "peer-reviewed-global-techno-economic-model-abstract"
- "official-carbon-accounting-guidance"
source_checked_on: "2026-10-28"
review_note: "AI source-scoped draft; independent scientific, brewery engineering, community and food-safety review not performed."
relations:
- relation: compare_with
  target: environment/industrial-heat-pump-model-boundaries
- relation: compare_with
  target: processes/wort-cooling-and-heat-recovery
- relation: compare_with
  target: environment/brewery-heat-and-refrigeration
---

# A brewery's heat use, cooling load and climate impact are different numbers

## A heat-demand number is not a carbon footprint

A brewery uses high-temperature energy for operations such as wort boiling, and lower-temperature cooling for fermentation and storage. Padullés and colleagues' 2026 analysis constructed a *generalized* industrial brewing process and used pinch analysis to investigate heat-recovery options. Their energy values describe the model's functional system, not a direct meter reading from all breweries in all countries.[^v119-pinch26]

Liu and colleagues modeled wider industrial-heat-pump opportunities across global beer production and Chinese baijiu. Their published avoided-emissions potential depends on assumptions about heat supply, electricity and adoption. A technical potential estimated for one fuel mix cannot be converted into a measured Scope 1 or 2 reduction at an arbitrary small brewery.[^v119-heatglobal25]

## Put the claim into an accounting category

The GHG Protocol's public FAQ distinguishes direct emissions, indirect emissions from purchased electricity/heat/steam, and other upstream or downstream value-chain emissions. A brewery's onsite energy efficiency may improve while its electricity-related Scope 2 and ingredient-related Scope 3 still require separate measurement and reporting.[^v119-ghgfaq]

A researcher should capture the meter or model, time period, brewery size, delivered heat versus purchased electricity, refrigerant and fuel assumptions, and the scope or life-cycle boundary. “Electric” is a technology description, not by itself a zero-carbon certification. Follow [model limits](../environment/industrial-heat-pump-model-boundaries.md), [wort heat integration](../processes/wort-cooling-and-heat-recovery.md), and [the existing refrigeration overview](../environment/brewery-heat-and-refrigeration.md).

## Explore connected subjects

- [industrial heat pump model boundaries](../environment/industrial-heat-pump-model-boundaries.md)
- [wort cooling and heat recovery](../processes/wort-cooling-and-heat-recovery.md)
- [brewery heat and refrigeration](../environment/brewery-heat-and-refrigeration.md)

## Evidence boundary

The cited measurements and model estimates are not product or environmental certificates; no operational designs, microbiological treatments or local community viewpoints are independently validated in this article.

## Source notes

[^v119-pinch26]: [Generalized electrification solutions for breweries: Pinch Analysis and heat pump integration (2026)](https://orbit.dtu.dk/en/publications/generalized-electrification-solutions-for-breweries-a-pinch-analy/). Roger Padullés, Martin Pihl Andersen, Niklas Bagge Mogensen and colleagues. Checked 2026-10-28. Access: Full public Danish Technical University research entry and journal abstract; final CC BY article linked, but design inputs were not independently re-calculated. Generalized brewery model, not measured results at every plant.

[^v119-heatglobal25]: [Electrification and decarbonization in global brewing industry driven by industrial heat pumps (2025)](https://www.sciencedirect.com/science/article/pii/S0360544225018262). Zhongyi Liu, Bin Hu, Di Wu and Ruzhu Wang. Checked 2026-10-28. Access: Public publisher abstract of a global sector model under assumed boiler and electricity scenarios; article full methods not independently read. Potential avoided emissions are model outputs, not measured reductions.

[^v119-ghgfaq]: [GHG Protocol Calculation Tools FAQ: emissions scopes and biogenic reporting](https://ghgprotocol.org/calculation-tools-faq). Greenhouse Gas Protocol / World Resources Institute. Checked 2026-10-28. Access: Full public accounting FAQ distinguishing scopes 1/2/3 and separately reported biogenic CO2 from biomass combustion; specific fermentation carbon-cycle calculation requires its own applicable guidance.
