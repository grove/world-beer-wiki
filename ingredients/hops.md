---
type: Ingredient Reference
title: Hops
description: Hop materials, bitterness, aroma and why hopping does not map directly to one beer style.
tags:
- ingredient
- hops
- bitterness
- aroma
status: draft
generated:
  by: world-beer-wiki/1.1
  at: '2026-10-27T19:30:00Z'
sources:
- id: ing-hop-study-guide
  resource: https://www.bjcp.org/exam-certification/program/studying/beer-exam-study-guide/hops/
  title: Hops — Beer Exam Study Guide
  author_label: Peter Garofalo; updated by Scott Bickham
  source_kind: official-technical-education
  access_scope: botanical identity and distinction between measured and perceived bitterness; historical
    and simplistic universal IBU claims not used
- id: ing-yakima-handbook
  resource: https://tools.yakimachief.com/documents/Survivable-Compounds-Handbook-2022.pdf
  title: 'A Brewer''s Handbook: Survivable Compounds (2022)'
  author_label: Yakima Chief Hops
  source_kind: producer-technical-documentation
  access_scope: readable indexed glossary excerpts on alpha acids, additions and biotransformation; direct
    PDF text extraction was corrupted
- id: ing-yakima-products
  resource: https://www.yakimachief.eu/resources/product-usage-matrix
  title: Introducing the Product Usage Matrix
  author_label: Yakima Chief Hops
  source_kind: producer-technical-documentation
  access_scope: product descriptions for whole cones, pellets, extracts and aroma products; commercial
    claims kept product-specific
- id: ing-hop-creep
  resource: https://pubmed.ncbi.nlm.nih.gov/30084254/
  title: Evidence of Dextrin Hydrolyzing Enzymes in Cascade Hops (2018)
  author_label: Kaylyn R. Kirkpatrick and Thomas H. Shellhammer
  source_kind: primary-research
  access_scope: indexed abstract; DOI 10.1021/acs.jafc.8b03563; Cascade-hop experiment, not a fixed effect
    for every beer
- id: v13-hopcreep
  resource: https://www.brewersassociation.org/educational-publications/hop-creep-technical-brief/
  title: Hop Creep – Technical Brief
  author_label: Arnbjørn Stokholm and Thomas H. Shellhammer, Brewers Association
  source_kind: brewing-technical-explanation
  access_scope: Technical summary accessible; conditions and possible outcomes, no universal batch predictions.
- id: v14-hops-climate
  resource: https://pmc.ncbi.nlm.nih.gov/articles/PMC10564787/
  title: Climate-induced Decline in the Quality and Quantity of European Hops (2023)
  author_label: European hop climate researchers
  source_kind: climate-primary-open-text
  access_scope: 'Open full study: historical records and projections for specific European growing regions;
    not all worldwide hops.'
- id: v16-hop-review
  resource: https://pmc.ncbi.nlm.nih.gov/articles/PMC10910910/
  title: The two faces of microorganisms in traditional brewing and implications for no- and low-alcohol
    beer (2024)
  author_label: Review authors
  source_kind: open-scientific-review
  access_scope: Open review text on iso-alpha acid antimicrobial effects, resistance and selected yeasts;
    organism behavior depends on strain and conditions.
- id: v16-hop-primary
  resource: https://pubmed.ncbi.nlm.nih.gov/17021196/
  title: Characterization of a highly hop-resistant Lactobacillus brevis strain lacking hop transport (2006)
  author_label: Study authors
  source_kind: primary-microbiology-abstract
  access_scope: Indexed abstract of L. brevis TMW 1.465 experimental adaptation; strain-specific resistance
    mechanisms, not a universal species trait.
- id: v18-hop-thiol-survey
  resource: https://brewingscience.de/index.php/brewingscience/article/view/106
  title: Determination of Variety Dependent Thiol Impact Based on LC-MS/MS Analysis (2024)
  author_label: Christina Schmidt, Laura Hoferer and Martin Biendl
  source_kind: primary-analytical-research-abstract
  access_scope: 'Open journal abstract: 250 samples, 97 hop varieties and harvest/location variation;
    not stable cultivar sensory grades.'
- id: v18-hop-terpenes
  resource: https://www.sciencedirect.com/science/article/pii/S2772753X24000881
  title: Analysis of terpenoid biotransformation in beer by commercial Saccharomyces cerevisiae using
    SPME-GC/MS (2024)
  author_label: Food Chemistry Advances authors
  source_kind: primary-model-fermentation-study
  access_scope: 'Open publisher abstract: eleven terpenoid standards added individually to US-05 model
    beer fermentation, not all finished beer recipes.'
aliases:
- Humulus lupulus
regions:
- Cross-regional
scope: Hop function and material forms; not an exhaustive cultivar atlas or universal hopping schedule.
evidence_basis:
- official-technical-education
- primary-research
- producer-technical-documentation
source_checked_on: '2026-10-28'
review_note: AI source-checked research draft; not independently reviewed by a brewer, scientist, historian
  or community representative.
relations:
- relation: compare_with
  target: styles/english-ipa
- relation: compare_with
  target: styles/american-ipa
- relation: compare_with
  target: styles/hazy-ipa
- relation: compare_with
  target: styles/german-pils
- relation: compare_with
  target: styles/lambic
- relation: compare_with
  target: ingredients/herbs-and-spices
---

# Hops

Brewers use the cone-like flowers of *Humulus lupulus*. Resins and aromatic compounds associated with their lupulin glands contribute different aspects of beer character. “Hoppy” can therefore refer to aroma, flavour, bitterness or several of them; it is not one numerical property.[^ing-hop-study-guide]

## Bitterness and aroma are related but distinct

Alpha acids are precursors of bitter iso-alpha acids formed through isomerization during hot-side brewing. Aroma compounds behave differently: some are lost, retained or transformed as processing continues. Yakima Chief's technical glossary distinguishes early kettle additions, later aroma-focused applications and biological transformations during fermentation.[^ing-yakima-handbook]

An IBU value is an analytical or calculated bitterness-related measure, depending on its origin. It is not a complete measure of perceived bitterness, aroma intensity or quality. The beer's attenuation and other sensory context affect the impression. Preserve whether a reported number was measured, estimated or merely taken from a style range.[^ing-hop-study-guide]

## Record the material as well as the cultivar

| Form | Information worth preserving |
| --- | --- |
| Dried whole cones | The physical flower material and its condition. |
| Pellets | Processed hop material; the product type matters. |
| Concentrated or extracted products | Which fraction is supplied and whether its purpose is bitterness, aroma or both. |
| Fresh harvest material | Distinguish a seasonal fresh-hop application from an ordinary dried-hop addition. |

Yakima Chief's product matrix separates these forms and describes products intended for different brewing stages. Two products bearing the same cultivar name are not necessarily interchangeable by weight or role.[^ing-yakima-products]

## Dry hopping can change fermentation

Kirkpatrick and Shellhammer demonstrated dextrin-degrading activity in Cascade hops and further fermentation in beer containing viable yeast. This supports the phenomenon called hop creep: dry hops can affect fermentability as well as aroma. The magnitude depended on experimental conditions, so the result is not a fixed alcohol increase to attach to all dry-hopped beer.[^ing-hop-creep]

## Style connections

Compare [English IPA](../styles/english-ipa.md), [American IPA](../styles/american-ipa.md), [Hazy IPA](../styles/hazy-ipa.md), [German Pils](../styles/german-pils.md) and [Lambic](../styles/lambic.md) for different relationships between hop use and the beer's overall identity. For botanical additions serving other purposes, see [Herbs and spices](herbs-and-spices.md).

## Evidence note

Product descriptions are examples of current materials; they are not endorsements or historical proofs. The handbook was available through readable indexed excerpts, while direct PDF text extraction was corrupted. No universal cultivar flavour, dose or hop-creep magnitude is asserted.

[Ingredient directory](index.md) · [All beer entries](../styles/index.md) · [Research method](../editorial/methodology.md)

## Edition 1.4: Growing conditions change the raw material

European field observations and modeling identify changes in hop-ripening timing, yield and alpha-acid content in specific growing regions. Those measurements do not predict the sensory profile of every beer. See [climate and hop crops](../environment/climate-and-hop-crops.md).[^v14-hops-climate]

## Edition 1.8: newly sourced connections

A 2024 LC-MS/MS survey of **250 hop samples across 97 varieties** reported substantial free-thiol variability by cultivar, origin, crop year and harvest timing. The variety name alone cannot guarantee one quantitative aroma profile. A separate 2024 model-beer experiment showed that a commercial yeast changed the measured composition of individually supplied terpenoids during fermentation.[^v18-hop-thiol-survey][^v18-hop-terpenes]

Follow [thiol precursors](polyfunctional-thiol-precursors.md), [terpenoid transformation](../sensory/hop-terpenoid-biotransformation.md), and [why aroma does not identify a hop](../stories/why-fruity-beer-does-not-identify-the-hop.md). Chemical measurements, perceived flavor and advertised descriptors ask different questions.

## Source notes
[^ing-hop-study-guide]: [Hops — Beer Exam Study Guide](https://www.bjcp.org/exam-certification/program/studying/beer-exam-study-guide/hops/). Peter Garofalo; updated by Scott Bickham. Consulted 2026-10-27. Evidence used: botanical identity and distinction between measured and perceived bitterness; historical and simplistic universal IBU claims not used.
[^ing-yakima-handbook]: [A Brewer's Handbook: Survivable Compounds (2022)](https://tools.yakimachief.com/documents/Survivable-Compounds-Handbook-2022.pdf). Yakima Chief Hops. Consulted 2026-10-27. Evidence used: readable indexed glossary excerpts on alpha acids, additions and biotransformation; direct PDF text extraction was corrupted.
[^ing-yakima-products]: [Introducing the Product Usage Matrix](https://www.yakimachief.eu/resources/product-usage-matrix). Yakima Chief Hops. Consulted 2026-10-27. Evidence used: product descriptions for whole cones, pellets, extracts and aroma products; commercial claims kept product-specific.
[^ing-hop-creep]: [Evidence of Dextrin Hydrolyzing Enzymes in Cascade Hops (2018)](https://pubmed.ncbi.nlm.nih.gov/30084254/). Kaylyn R. Kirkpatrick and Thomas H. Shellhammer. Consulted 2026-10-27. Evidence used: indexed abstract; DOI 10.1021/acs.jafc.8b03563; Cascade-hop experiment, not a fixed effect for every beer.

## Atlas connections — added in edition 1.2

[Dry hopping and hop creep](../processes/dry-hopping-and-hop-creep.md) · [Flavor detective](../sensory/aroma-is-not-an-ingredient.md)

These reading links extend navigation; the original source access notes above remain unchanged.

## Research extension 1.3: Hops can also affect carbohydrate availability

Brewers Association material describes dry-hop-associated enzyme activity that can convert residual carbohydrates into fermentable sugars, under relevant brewing conditions. This is **hop creep**, not a guarantee attached to each hop cultivar. Further fermentation and package instability may follow. Read [hop creep chemistry](../processes/dry-hop-enzymes-and-refermentation.md) and [the earlier process overview](../processes/dry-hopping-and-hop-creep.md).[^v13-hopcreep]

[^v13-hopcreep]: [Hop Creep – Technical Brief](https://www.brewersassociation.org/educational-publications/hop-creep-technical-brief/). Arnbjørn Stokholm and Thomas H. Shellhammer, Brewers Association. Consulted 2026-10-27. Evidence accessed: Technical summary accessible; conditions and possible outcomes, no universal batch predictions.

[^v14-hops-climate]: [Climate-induced Decline in the Quality and Quantity of European Hops (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10564787/). European hop climate researchers. Consulted 2026-10-27. Access: Open full study: historical records and projections for specific European growing regions; not all worldwide hops.

## Edition 1.6: sourced research connections

A scientific review explains that hop iso-alpha acids can inhibit many sensitive Gram-positive bacteria, while some beer-associated lactic acid bacteria tolerate them. A targeted *Lactobacillus brevis* experiment demonstrated several resistance-related physiological changes, rather than one universal export mechanism. The bacterium's identity alone does not predict whether a given beer will spoil.[^v16-hop-review][^v16-hop-primary]

The [hop-resistant LAB reference](../microbiology/hop-resistant-lactic-acid-bacteria.md) distinguishes deliberate acidification from unwanted growth.

[^v16-hop-review]: [The two faces of microorganisms in traditional brewing and implications for no- and low-alcohol beer (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10910910/). Review authors. Consulted 2026-10-28. Access: Open review text on iso-alpha acid antimicrobial effects, resistance and selected yeasts; organism behavior depends on strain and conditions.
[^v16-hop-primary]: [Characterization of a highly hop-resistant Lactobacillus brevis strain lacking hop transport (2006)](https://pubmed.ncbi.nlm.nih.gov/17021196/). Study authors. Consulted 2026-10-28. Access: Indexed abstract of L. brevis TMW 1.465 experimental adaptation; strain-specific resistance mechanisms, not a universal species trait.

[^v18-hop-thiol-survey]: [Determination of Variety Dependent Thiol Impact Based on LC-MS/MS Analysis (2024)](https://brewingscience.de/index.php/brewingscience/article/view/106). Christina Schmidt, Laura Hoferer and Martin Biendl. Consulted 2026-10-28. Access: Open journal abstract: 250 samples, 97 hop varieties and harvest/location variation; not stable cultivar sensory grades.

[^v18-hop-terpenes]: [Analysis of terpenoid biotransformation in beer by commercial Saccharomyces cerevisiae using SPME-GC/MS (2024)](https://www.sciencedirect.com/science/article/pii/S2772753X24000881). Food Chemistry Advances authors. Consulted 2026-10-28. Access: Open publisher abstract: eleven terpenoid standards added individually to US-05 model beer fermentation, not all finished beer recipes.
