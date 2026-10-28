---
type: "Brewing Analytics and Fermentation Reference"
title: "Original gravity, residual extract, attenuation and estimated alcohol"
description: "A bounded research discussion of analytical evidence, method scope and interpretation."
tags: [research-edition-1.16, measurement, evidence-boundaries]
status: draft
generated:
  by: world-beer-wiki/1.16
  at: "2026-10-28T13:00:00Z"
sources:
- id: v116-lab
  resource: "https://pmc.ncbi.nlm.nih.gov/articles/PMC9286407/"
  title: "A Hands-On Guide to Brewing and Analyzing Beer in the Laboratory (2019)"
  author_label: "Florian A. Thesseling and colleagues"
  source_kind: "open-laboratory-protocol-public-index"
  access_scope: "Full paper indexed through PubMed Central search output including named laboratory methods; direct open intermittently presented a browser check. Published lab protocols, not validated consumer operations."
- id: v116-methodVideos
  resource: "https://www.asbcnet.org/lab/methods-videos/beer-methods-series"
  title: "Beer Methods Series"
  author_label: "American Society of Brewing Chemists and Brewers Association"
  source_kind: "official-analytical-method-index"
  access_scope: "Public method-demonstration index for gravity, apparent extract, acidity, pH and degassing; full member-only procedural text not claimed."
- id: v116-nolo
  resource: "https://www.asbcnet.org/methods/nablab-0-0-methods"
  title: "NA Beer / Low Alcohol Beer / 0.0 Beer Methods"
  author_label: "American Society of Brewing Chemists"
  source_kind: "official-method-applicability-index"
  access_scope: "Public matrix of method applicability to low-/no-alcohol beer; full testing data and methods are not reproduced."
regions:
- "Cross-regional"
scope: "What the cited analytical and institutional sources can establish in original gravity, residual extract, attenuation and estimated alcohol; not a global classification, operational recipe or safety certification."
evidence_basis:
- "open-laboratory-protocol-public-index"
- "official-analytical-method-index"
- "official-method-applicability-index"
source_checked_on: "2026-10-28"
review_note: "AI source-scoped research draft. Independent brewer, scientist, historian, cultural and food-safety review not performed."
relations:
- relation: compare_with
  target: objects/hydrometers-and-reading-conditions
- relation: compare_with
  target: microbiology/fermentation-endpoints-are-not-identities
- relation: compare_with
  target: categories/beer-metrics-versus-beverage-identity
---

# Original gravity, residual extract, attenuation and estimated alcohol

## Before and after fermentation are different samples

Gravity describes a density relationship for a given liquid at a given condition. A wort measurement before fermentation is often reported as original gravity or original extract; a beer measurement after fermentation reflects a mixture that now includes alcohol as well as residual dissolved solids. The published laboratory guide by Thesseling and colleagues distinguishes these states and describes a common gravity-difference equation for **estimating**, rather than directly assaying, alcohol.[^v116-lab]

The ASBC/BA method-demonstration index separately lists specific gravity, apparent extract and other analyses. Separate methods matter: residual gravity in alcohol-containing beer is not a direct sugar concentration. It is therefore possible to report a high apparent attenuation while the interpretation of residual carbohydrates still requires another measurement.[^v116-methodVideos]

## Low and no alcohol are instructive edge cases

ASBC's published applicability directory lists different methods for low- and no-alcohol beers, reminding readers that measurement range and matrix affect method suitability. A simple homebrew approximation from original and final gravity is not proof that a product meets a regulatory strength threshold or is safe.[^v116-nolo]

In historical and cultural descriptions, a numerical result also cannot be projected backward onto a beverage whose recipe, temperature, service or measurement protocol is undocumented. The distinction between apparent and real extract matters if comparing laboratory reports across institutions.

Use [hydrometer conditions](../objects/hydrometers-and-reading-conditions.md), [fermentation endpoint interpretation](../microbiology/fermentation-endpoints-are-not-identities.md) and [the measurement/identity guide](../categories/beer-metrics-versus-beverage-identity.md). This is interpretive literacy, not a recipe or alcohol-compliance calculator.

## Explore connected subjects

- [hydrometers and reading conditions](../objects/hydrometers-and-reading-conditions.md)
- [fermentation endpoints are not identities](../microbiology/fermentation-endpoints-are-not-identities.md)
- [beer metrics versus beverage identity](../categories/beer-metrics-versus-beverage-identity.md)

## Evidence boundary

Sources are attributed according to what was actually accessible; numerical procedures and examples are not general manufacturing recommendations. This research is an editorial synthesis without independent specialist or community sign-off.

## Source notes

[^v116-lab]: [A Hands-On Guide to Brewing and Analyzing Beer in the Laboratory (2019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9286407/). Florian A. Thesseling and colleagues. Checked 2026-10-28. Access: Full paper indexed through PubMed Central search output including named laboratory methods; direct open intermittently presented a browser check. Published lab protocols, not validated consumer operations.

[^v116-methodVideos]: [Beer Methods Series](https://www.asbcnet.org/lab/methods-videos/beer-methods-series). American Society of Brewing Chemists and Brewers Association. Checked 2026-10-28. Access: Public method-demonstration index for gravity, apparent extract, acidity, pH and degassing; full member-only procedural text not claimed.

[^v116-nolo]: [NA Beer / Low Alcohol Beer / 0.0 Beer Methods](https://www.asbcnet.org/methods/nablab-0-0-methods). American Society of Brewing Chemists. Checked 2026-10-28. Access: Public matrix of method applicability to low-/no-alcohol beer; full testing data and methods are not reproduced.
