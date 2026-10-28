---
type: Beer Category Guide
title: How beer categories work
description: A practical model for separating beer styles, local traditions, ingredients, processes, and dated judging
  systems.
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
  access_scope: 'Publisher abstract: interviews with ten beer experts and ten sommeliers, fifteen principles; not
    consumer preference laws.'
- id: v15-bjcp-2021
  resource: https://www.bjcp.org/beer-styles/introduction-to-the-2021-guidelines/
  title: 'BJCP 2021 Beer Style Guidelines: Official Introduction'
  author_label: Beer Judge Certification Program
  source_kind: official-guideline
  access_scope: 'Official current beer-guideline introduction: grouping decisions, judging use and edition; not
    a global historical taxonomy.'
- id: v15-ba-2026
  resource: https://www.brewersassociation.org/edu/brewers-association-beer-style-guidelines/
  title: Brewers Association 2026 Beer Style Guidelines
  author_label: Brewers Association
  source_kind: official-guideline
  access_scope: Official 2026 guideline directory and use terms; names/edition referenced, no copied, altered or
    paraphrased guideline definitions.
- id: v19-vietnam-review
  resource: https://pmc.ncbi.nlm.nih.gov/articles/PMC4725306/
  title: 'Alcohol and Drinking Cultures in Vietnam: A Review (2015)'
  author_label: Review authors of Vietnam alcohol ethnography/public-health literature
  source_kind: scientific-social-review
  access_scope: Open indexed sections describing cultural variability, rural distillation and risks; explicitly
    a review, not direct S’Tieng fieldwork.
- id: v114-unesco
  resource: https://ich.unesco.org/en/RL/beer-culture-in-belgium-01062
  title: Beer culture in Belgium (2016 inscription)
  author_label: UNESCO Intergovernmental Committee / Belgian submitting communities
  source_kind: intangible-heritage-inscription
  access_scope: Full UNESCO inscription page with description of social transmission and food context; inscription
    is not a technical recipe or heritage status for each named beer.
- id: v114-plzen
  resource: https://www.prazdroj.cz/en/our-story/history
  title: 'Prazdroj history: birth and spread of Pilsen lager'
  author_label: Plzeňský Prazdroj
  source_kind: producer-archival-history
  access_scope: Full public producer-authored chronology; records the company's account of the 1842 Burghers Brewery,
    brewing rights and later transport infrastructure; independent contemporaneous archives not checked.
- id: v115-defs
  resource: "https://www.ttb.gov/regulated-commodities/beverage-alcohol/beer/beer-and-malt-beverage-definitions"
  title: "Beer and Malt Beverages"
  author_label: "Alcohol and Tobacco Tax and Trade Bureau"
  source_kind: "official-us-regulatory-guidance"
  access_scope: "Full public US agency definitions under the IRC and FAA Act; not a definition for other countries."
- id: v115-clas
  resource: "https://www.ttb.gov/regulated-commodities/beverage-alcohol/beer/labeling/malt-beverage-class-and-type"
  title: "Malt Beverage Labeling: Class and Type Designation"
  author_label: "Alcohol and Tobacco Tax and Trade Bureau"
  source_kind: "official-us-regulatory-guidance"
  access_scope: "Full public TTB 2023 designation guidance, including under-0.5% malt beverages, not global style terminology."
category_axis: multiple
scope: Educational comparison across the linked profiles; not a new universal competition category or an exhaustive
  world taxonomy.
evidence_basis: cited-primary-sources-and-editorial-comparison
source_checked_on: '2026-10-27'
review_note: AI source-checked research draft; not independently reviewed by a historian, brewer, or community representative.
relations:
- relation: compares
  target: styles/kolsch
- relation: compares
  target: styles/biere-de-garde
- relation: associated_with
  target: categories/bjcp-2021-versus-ba-2026
  source_ids:
  - v15-bjcp-2021
  qualifier: Two separately published guidelines; neither a universal ancestry schema.
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

## Research extension 1.5: 2026 classification cross-check

Two influential modern classification systems have different purposes and update cycles. BJCP’s currently published beer guide is the 2021 edition, while the Brewers Association’s public beer style directory is labeled 2026. The BJCP introduction says category groups are designed for judging characteristics rather than necessarily reflecting common heritage.[^v15-bjcp-2021][^v15-ba-2026]

A category named in one framework can be absent or grouped differently in another. The wiki preserves each publisher and edition rather than synthesizing an imaginary universal classification. The [side-by-side guide](bjcp-2021-versus-ba-2026.md) explains how to interpret these claims without reproducing the BA’s protected guideline definitions.


## Edition 1.9: newly sourced connections

A regional drinking-cultures review from Vietnam is a reminder that English words such as *beer*, *wine* and *liquor* can follow different rules from a local beverage's actual processing. Rice may be fermented into a communal jar drink or fermented and then distilled for a spirit. Neither belongs to a modern judging category solely because of the substrate. The [new comparative guide](rice-wine-beer-and-distillation-boundaries.md) and [rượu cần profile](../styles/ruou-can-vietnamese-jar-ferment.md) keep technology, local naming, service and social setting separate—without declaring a superior universal vocabulary.[^v19-vietnam-review]



## Edition 1.14: newly sourced connections

A heritage inscription, a brewer's first-batch chronology and a modern competition category are not three ways of reporting the same fact. UNESCO documents Belgian beer's social transmission and significance; Pilsen's producer documents a dated institutional history. Neither defines the entire sensory universe of “Belgian beer” or “Pilsner” for all eras.[^v114-unesco][^v114-plzen]

Use [heritage versus style](heritage-inscription-is-not-a-style.md) and [field-to-glass evidence layers](from-field-to-glass-evidence-chain.md) to ask what each document is able to prove before grouping subjects into a family.[^v114-unesco]

## Source notes

[^wiki-bjcp-introduction]: [BJCP 2021: Introduction to the guidelines](https://www.bjcp.org/beer-styles/introduction-to-the-2021-guidelines/). Beer Judge Certification Program. Consulted 2026-10-27. Evidence used: Styles and Categories; purpose and limitations of judging categories.

[^wiki-bjcp-basic-categorization]: [BJCP 2021: Basic Categorization](https://styles.bjcp.org/bjcp-2021-beer/introduction-to-beer-styles/basic-categorization). Beer Judge Certification Program. Consulted 2026-10-27. Evidence used: modern and regional meanings of ale, lager, wild, and spontaneous fermentation.

[^bjcp-2021-5b]: [BJCP 2021: Kölsch](https://styles.bjcp.org/bjcp-2021-beer/5/5b-kolsch). Beer Judge Certification Program. Consulted 2026-10-27. Evidence used: style description.

[^bjcp-2021-24c]: [BJCP 2021: Bière de Garde](https://styles.bjcp.org/bjcp-2021-beer/24/24c-biere-de-garde). Beer Judge Certification Program. Consulted 2026-10-27. Evidence used: style description.

[^v14-food]: [From Expert Knowledge and Sensory Science to Food-and-Beer Pairing (2019)](https://www.sciencedirect.com/science/article/pii/S1878450X18300830). Food-pairing interview study authors. Consulted 2026-10-27. Access: Publisher abstract: interviews with ten beer experts and ten sommeliers, fifteen principles; not consumer preference laws.

[^v15-bjcp-2021]: [BJCP 2021 Beer Style Guidelines: Official Introduction](https://www.bjcp.org/beer-styles/introduction-to-the-2021-guidelines/). Beer Judge Certification Program. Consulted 2026-10-27. Source access: Official current beer-guideline introduction: grouping decisions, judging use and edition; not a global historical taxonomy.

[^v15-ba-2026]: [Brewers Association 2026 Beer Style Guidelines](https://www.brewersassociation.org/edu/brewers-association-beer-style-guidelines/). Brewers Association. Consulted 2026-10-27. Source access: Official 2026 guideline directory and use terms; names/edition referenced, no copied, altered or paraphrased guideline definitions.

[^v19-vietnam-review]: [Alcohol and Drinking Cultures in Vietnam: A Review (2015)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4725306/). Review authors of Vietnam alcohol ethnography/public-health literature. Checked 2026-10-28. Access: Open indexed sections describing cultural variability, rural distillation and risks; explicitly a review, not direct S’Tieng fieldwork.

[^v114-unesco]: [Beer culture in Belgium (2016 inscription)](https://ich.unesco.org/en/RL/beer-culture-in-belgium-01062). UNESCO Intergovernmental Committee / Belgian submitting communities. Consulted 2026-10-28. Access: Full UNESCO inscription page with description of social transmission and food context; inscription is not a technical recipe or heritage status for each named beer.
[^v114-plzen]: [Prazdroj history: birth and spread of Pilsen lager](https://www.prazdroj.cz/en/our-story/history). Plzeňský Prazdroj. Consulted 2026-10-28. Access: Full public producer-authored chronology; records the company's account of the 1842 Burghers Brewery, brewing rights and later transport infrastructure; independent contemporaneous archives not checked.

## Edition 1.15: newly sourced connections

The US example supplies a practical warning against treating technical style names as legal classes. TTB explains that *beer* as defined for US federal excise purposes and *malt beverage* as used for FAA Act labeling have **different scope**: in the latter definition both malted barley and hops are essential. The distinction is about the governing statute, not which drinks deserve a place in a global brewing reference.[^v115-defs]

TTB class-and-type guidance also addresses the labels of products below 0.5% ABV, which can have permissible designations different from beer styles used in judging. Store legal scope, jurisdiction, style-guide edition, strength and culturally situated name separately rather than making one hierarchy do every job.[^v115-clas]

Compare the [new multi-authority guide](jurisdictional-beer-names-vs-styles.md) and [historic US category context](../history/us-beer-vs-malt-beverage-definitions.md).

[^v115-defs]: [Beer and Malt Beverages](https://www.ttb.gov/regulated-commodities/beverage-alcohol/beer/beer-and-malt-beverage-definitions). Alcohol and Tobacco Tax and Trade Bureau. Consulted 2026-10-28. Access: Full public US agency definitions under the IRC and FAA Act; not a definition for other countries.

[^v115-clas]: [Malt Beverage Labeling: Class and Type Designation](https://www.ttb.gov/regulated-commodities/beverage-alcohol/beer/labeling/malt-beverage-class-and-type). Alcohol and Tobacco Tax and Trade Bureau. Consulted 2026-10-28. Access: Full public TTB 2023 designation guidance, including under-0.5% malt beverages, not global style terminology.
