---
type: Sensory Reasoning Guide
title: Flavor detective — aroma is not an ingredient
description: Read banana, citrus, coffee and cream as observations before treating them as ingredient declarations.
tags: [sensory, aroma, evidence, comparison]
status: draft
generated: {by: world-beer-wiki/1.2, at: '2026-10-27T20:35:00Z'}
scope: Comparative reasoning from existing profiles and the new ingredient references; not chemical identification of a specific beer.
sources:
- id: atlas-weissbier-context
  resource: /styles/weissbier.md
  title: Weissbier profile in World Beer Wiki
  source_kind: existing-corpus-synthesis
  access_scope: Retained distinction between fermentation-derived clove/banana impressions and actual additions.
- id: atlas-voss-context
  resource: /styles/vossaol.md
  title: Vossaøl profile in World Beer Wiki
  source_kind: existing-corpus-synthesis
  access_scope: Retained fieldwork account of orange-peel-like aroma without an orange-peel ingredient; attribution rather than a chemical assay.
- id: atlas-stout-context
  resource: /styles/american-stout.md
  title: American Stout profile in World Beer Wiki
  source_kind: existing-corpus-synthesis
  access_scope: Retained distinction between roast-derived impressions and required coffee or chocolate additions.
- id: atlas-sugars-context
  resource: /ingredients/sugars.md
  title: Sugars, syrups and lactose reference in World Beer Wiki
  source_kind: existing-corpus-synthesis
  access_scope: Retained distinctions between fermentable additions, residual sweetness and lactose.
source_checked_on: '2026-10-27'
review_note: Research draft; no sensory panel or analytical experiment conducted for this page.
relations:
- {relation: compare_with, target: ingredients/citrus-peel}
- {relation: compare_with, target: ingredients/coriander}
- {relation: compare_with, target: ingredients/lactose}
---

# Flavor detective — aroma is not an ingredient

Imagine reading four tasting notes: **banana**, **orange peel**, **coffee**, and **cream**. Before turning them into a shopping list, ask what kind of statement each note is making. A resemblance can be accurately described even when the food being evoked never entered the brew.

## Four useful cases

| Impression | What the cited profile actually supports |
|---|---|
| Banana and clove | The Weissbier reference associates these with fermentation, not required fruit and spice additions.[^atlas-weissbier-context] |
| Orange peel | The Vossaøl account reports the impression without orange peel in the documented ingredients and attributes it to fermentation.[^atlas-voss-context] |
| Coffee or chocolate | American Stout can evoke these through its dark-grain character; actual coffee or chocolate is not required.[^atlas-stout-context] |
| Cream | A creamy impression does not establish lactose or another dairy ingredient.[^atlas-sugars-context] |

None of this means such foods can never be added. It means the flavor word alone cannot decide whether they were.

## A better three-line tasting record

**Observation:** What did the taster perceive, and under what serving conditions?

**Documented production fact:** What does the brewer or source actually identify as an ingredient, culture or process?

**Interpretation:** What connection is plausible, and what additional evidence would be needed to establish it?

This distinction improves both human notes and machine retrieval. A system can retain “orange-like aroma” without incorrectly asserting `uses_ingredient: citrus-peel`.

## Follow the alternative explanations

[Citrus peel](../ingredients/citrus-peel.md) describes an actual addition. [Coriander](../ingredients/coriander.md) distinguishes a spice ingredient from spice-like fermentation character. [Lactose](../ingredients/lactose.md) separates sugar identity from residual sweetness and texture. Read those pages as possible explanations, not a diagnostic decision tree that guarantees an answer from a sip.

## Evidence note

These are comparisons of source-backed descriptions, not a blinded sensory experiment or chemical analysis. A specific compound name, concentration or ingredient claim needs its own evidence. Avoid turning a vivid metaphor into a falsely precise laboratory result.

## Source notes

[^atlas-weissbier-context]: [Weissbier](../styles/weissbier.md), retained profile and its source.
[^atlas-voss-context]: [Vossaøl](../styles/vossaol.md), retained field observations and attribution.
[^atlas-stout-context]: [American Stout](../styles/american-stout.md), retained ingredient and flavor distinctions.
[^atlas-sugars-context]: [Sugars, syrups and lactose](../ingredients/sugars.md), retained ingredient-versus-sensory distinction.
