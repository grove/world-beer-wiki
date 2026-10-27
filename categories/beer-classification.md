---
type: Beer Category Guide
title: How beer categories work
description: A practical model for separating beer styles, local traditions, ingredients, processes,
  and dated judging systems.
tags:
- classification
- taxonomy
- llm-retrieval
- category-guide
status: draft
generated:
  by: world-beer-wiki/1.1
  at: '2026-10-27T19:39:23Z'
sources:
- id: wiki-bjcp-introduction
  resource: https://www.bjcp.org/beer-styles/introduction-to-the-2021-guidelines/
  title: 'BJCP 2021: Introduction to the guidelines'
  author: team:beer-judge-certification-program
  source_kind: official-style-guideline
  access_scope: Styles and Categories; purpose and limitations of judging categories
  author_label: Beer Judge Certification Program
- id: wiki-bjcp-basic-categorization
  resource: https://styles.bjcp.org/bjcp-2021-beer/introduction-to-beer-styles/basic-categorization
  title: 'BJCP 2021: Basic Categorization'
  author: team:beer-judge-certification-program
  source_kind: official-style-guideline
  access_scope: modern and regional meanings of ale, lager, wild, and spontaneous fermentation
  author_label: Beer Judge Certification Program
- id: bjcp-2021-5b
  resource: https://styles.bjcp.org/bjcp-2021-beer/5/5b-kolsch
  title: 'BJCP 2021: Kölsch'
  author: team:beer-judge-certification-program
  source_kind: official-style-guideline
  access_scope: style description
  author_label: Beer Judge Certification Program
- id: bjcp-2021-24c
  resource: https://styles.bjcp.org/bjcp-2021-beer/24/24c-biere-de-garde
  title: 'BJCP 2021: Bière de Garde'
  author: team:beer-judge-certification-program
  source_kind: official-style-guideline
  access_scope: style description
  author_label: Beer Judge Certification Program
- id: v14-food
  resource: https://www.sciencedirect.com/science/article/pii/S1878450X18300830
  title: From Expert Knowledge and Sensory Science to Food-and-Beer Pairing (2019)
  author_label: Food-pairing interview study authors
  source_kind: sensory-interview-abstract
  access_scope: 'Publisher abstract: interviews with ten beer experts and ten sommeliers, fifteen principles;
    not consumer preference laws.'
category_axis: multiple
scope: Educational comparison across the linked profiles; not a new universal competition category or
  an exhaustive world taxonomy.
evidence_basis: cited-primary-sources-and-editorial-comparison
source_checked_on: '2026-10-27'
review_note: AI source-checked research draft; not independently reviewed by a historian, brewer, or
  community representative.
relations:
- relation: compares
  target: styles/kolsch
- relation: compares
  target: styles/biere-de-garde
---

# How beer categories work

Beer is easier to understand through several overlapping descriptions than through one family tree. A beer can have a named style, a local identity, a particular fermentation, an ingredient emphasis, and a serving method at the same time. This wiki uses those as **separate questions**, then links the answers.

BJCP explicitly organizes its categories for judging. Membership in the same numbered group does not establish common ancestry or geography, and an unlisted beer is not thereby outside the world's brewing traditions. Its style descriptions and the educational groupings in this directory serve different purposes.[^wiki-bjcp-introduction]

## Choose the question before the category

| Question | Useful description | Where to look |
|---|---|---|
| What named beer or tradition is this? | A canonical profile, with its scope and aliases | [All profiles](../styles/index.md) |
| Who makes it, and where? | Community, region, producer and period | [Regional navigation](../navigation/by-region.md), [traditional brewing](traditional-and-indigenous-beers.md) |
| What fermented it? | Named cultures and their documented roles | [Brewing yeast](../ingredients/brewing-yeast.md), [bacteria](../ingredients/brewing-bacteria.md), [mixed starters](../ingredients/mould-and-mixed-starters.md) |
| What supplied starch or sugar? | Ingredients and conversion method | [Ingredient directory](../ingredients/index.md) |
| What shaped its character? | Hopping, smoke, fruit, wood or maturation | [Hop-forward beers](ipa-and-hop-forward-beers.md), [specialty treatments](smoke-wood-and-specialty-beers.md) |
| How was it conditioned or served? | Cold conditioning, bottle or cask conditioning, dispense | [Lager and conditioning](lagers-and-cold-conditioning.md), [British and Irish ales](british-and-irish-ales.md) |
| Which judging definition is intended? | Organization, edition and exact entry | Each profile's `classification`, where supplied |

The table is an editorial retrieval model, not a claim that every community divides its beverages this way. Preserve a drink's own name when comparing it with a technical process.

## Ale, lager, mixed, and spontaneous

In contemporary craft usage, ale and lager commonly refer to yeast-associated groups. Historical and regional usage differs: lagering can describe conditioning, while an older English use of *ale* can distinguish it from more heavily hopped *beer*. Consequently a historical text must be interpreted in its own vocabulary.[^wiki-bjcp-basic-categorization]

*Mixed* describes a combination of organisms; *spontaneous* describes how a fermentation is initiated. A brewer can deliberately pitch a mixed culture. Neither label alone states the final acidity, the grain bill, or the cultural identity. See [sour and mixed fermentation](sour-and-mixed-fermentation-beers.md) for a comparison of actual cases.[^wiki-bjcp-basic-categorization]

## A worked reading example

[Kölsch](../styles/kolsch.md) combines top fermentation with cold conditioning. Record both attributes instead of forcing one to erase the other. [Bière de Garde](../styles/biere-de-garde.md) illustrates a different issue: the cited modern description permits ale or lager yeast, while retaining a recognizably malt-led, conditioned family.[^bjcp-2021-5b][^bjcp-2021-24c]

For an LLM, retrieve the canonical page first, then its category guide and relevant ingredient pages. Carry forward the page's `type`, `scope`, date and evidence limits. A [related starch ferment](starch-fermentation-and-beer-boundaries.md) should not silently become a standardized beer style because it appears in the same directory.

## What to avoid

Do not count aliases as additional styles, infer a genealogy from comparison links, or assign a laboratory measurement to every drink sharing a name. A new competition category dates a classification decision; it does not date the invention of its ingredients or process. Where systems differ, report each definition with its edition rather than manufacturing one supposedly universal range.

[All category guides](index.md) · [Ingredient reference](../ingredients/index.md) · [All beer profiles](../styles/index.md) · [Evidence method](../editorial/methodology.md)

## Edition 1.4: Classification does not explain every pairing

A sensory-study abstract reports experts’ reasoning about beer and food combinations. Such contextual judgments are another dimension of experience, distinct from recipe, geography, fermentation and judging style. See [beer and food](../food/beer-food-pairing-as-a-hypothesis.md).[^v14-food]

## Source notes

[^wiki-bjcp-introduction]: [BJCP 2021: Introduction to the guidelines](https://www.bjcp.org/beer-styles/introduction-to-the-2021-guidelines/). Beer Judge Certification Program. Consulted 2026-10-27. Evidence used: Styles and Categories; purpose and limitations of judging categories.

[^wiki-bjcp-basic-categorization]: [BJCP 2021: Basic Categorization](https://styles.bjcp.org/bjcp-2021-beer/introduction-to-beer-styles/basic-categorization). Beer Judge Certification Program. Consulted 2026-10-27. Evidence used: modern and regional meanings of ale, lager, wild, and spontaneous fermentation.

[^bjcp-2021-5b]: [BJCP 2021: Kölsch](https://styles.bjcp.org/bjcp-2021-beer/5/5b-kolsch). Beer Judge Certification Program. Consulted 2026-10-27. Evidence used: style description.

[^bjcp-2021-24c]: [BJCP 2021: Bière de Garde](https://styles.bjcp.org/bjcp-2021-beer/24/24c-biere-de-garde). Beer Judge Certification Program. Consulted 2026-10-27. Evidence used: style description.

[^v14-food]: [From Expert Knowledge and Sensory Science to Food-and-Beer Pairing (2019)](https://www.sciencedirect.com/science/article/pii/S1878450X18300830). Food-pairing interview study authors. Consulted 2026-10-27. Access: Publisher abstract: interviews with ten beer experts and ten sommeliers, fifteen principles; not consumer preference laws.
