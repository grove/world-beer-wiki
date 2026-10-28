---
type: Fermentation Ecology Reference
title: Microbial succession and the limits of a species list
description: How to read changing populations, functional evidence and sampling limits across fermentation
  studies.
tags:
- microbiology
- ecology
- evidence
- fermentation
status: draft
generated:
  by: world-beer-wiki/1.2
  at: '2026-10-27T20:20:00Z'
scope: Interpretation of two specified research settings and of microbial evidence; not a universal succession
  timetable.
sources:
- id: atlas-sesotho
  resource: https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2020.01451/full
  title: Bacterial and Fungal Dynamics During the Fermentation Process of Sesotho, a Traditional Beer of Southern
    Africa
  author_label: Errol D. Cason and colleagues
  source_kind: primary-research
  access_scope: 2020 article, introduction and sampling design; five breweries and five production stages,
    without biological batch replicates within breweries.
- id: atlas-bacteria-overview
  resource: /ingredients/brewing-bacteria.md
  title: Brewing bacteria overview in World Beer Wiki
  source_kind: existing-corpus-synthesis
  access_scope: Retained distinctions among organism detection, metabolites, sensory effect and inoculation
    method.
- id: v18-borde
  resource: https://www.sciencedirect.com/science/article/pii/S2666154324005350
  title: 'Characterization of borde: microbial analysis, rheological profiling, and functional attributes (2024)'
  author_label: Borde study authors
  source_kind: primary-laboratory-field-study
  access_scope: Open publisher abstract and highlights; three Ethiopian sampling locations; biochemical and
    in-vitro results are not human health effects.
- id: v18-jaanr
  resource: https://indianjournals.com/article/ijm-46-4-004
  title: Microbiological and physico-chemical changes during fermentation of kodo ko jaanr (2006)
  author_label: S. Thapa and J. P. Tamang
  source_kind: primary-research-abstract
  access_scope: Publisher-indexed abstract of measured finger-millet fermentation in Darjeeling/Sikkim; original
    full paper not reviewed.
- id: v111-pulque-stages
  resource: https://pmc.ncbi.nlm.nih.gov/articles/PMC7493934/
  title: Genomic profiling of bacterial and fungal communities and their predictive functionality during pulque
    fermentation by whole-genome shotgun sequencing (2020)
  author_label: Shotgun-metagenomic research team
  source_kind: primary-metagenomic-study
  access_scope: Open study abstract and indexed methods/results of five pulque stages; read counts and predicted
    functions do not demonstrate universal organisms or causation.
- id: v111-cauim-dynamics
  resource: https://pubmed.ncbi.nlm.nih.gov/20413168/
  title: Determination of dynamic characteristics of microbiota in a fermented beverage produced by Brazilian
    Amerindians (2010)
  author_label: Fermentation-microbiology research team
  source_kind: primary-mixed-methods-abstract
  access_scope: PubMed indexed abstract of Tapirapé peanut/rice cauim with culture-dependent and DGGE methods;
    separate substrate and sample.
- id: v113-tchou-2013
  resource: https://pubmed.ncbi.nlm.nih.gov/23756236/
  title: Yeast dynamics during spontaneous fermentation of mawè and tchoukoutou (2013)
  author_label: A. Greppi and colleagues
  source_kind: primary-fermentation-study-abstract
  access_scope: PubMed indexed abstract, two monitored productions of each food; culture-dependent and
    -independent profiles differ and do not define a standard starter.
- id: v113-tchapalo-2022
  resource: https://pubmed.ncbi.nlm.nih.gov/35344598/
  title: Detection of spoilage-causing yeasts and bacteria in tchapalo (2022)
  author_label: C. K. Attchelouwa and colleagues
  source_kind: primary-shelf-life-challenge-study-abstract
  access_scope: 'PubMed abstract: 11 selected strains inoculated into sterile-filtered tchapalo over three
    days; sensory and volatiles are specific to that challenge system.'
source_checked_on: '2026-10-27'
review_note: Research draft; no independent microbiologist review.
relations:
- relation: compare_with
  target: culture/sesotho-social-occasions
- relation: compare_with
  target: processes/spontaneous-fermentation
- relation: compare_with
  target: microbiology/brettanomyces
---

# Microbial succession and the limits of a species list

Fermentation is a changing environment. A study of Sesotho beer followed bacterial and fungal communities at successive production stages and found patterned changes despite differences among the sampled breweries. That observation is more informative than treating the final sample as a complete picture of the process.[^atlas-sesotho]

## Four claims that require different evidence

| Claim | What to look for |
|---|---|
| An organism was detected | Identification method, sample and stage. |
| It was alive and growing | Evidence beyond a name in sequence data. |
| It contributed a transformation | Functional or combined microbial/metabolite evidence. |
| A drinker perceived the result | Sensory evidence under stated conditions. |

The existing [brewing bacteria overview](../ingredients/brewing-bacteria.md) makes the same distinction between organisms, chemistry and sensory sourness. These records should be linked, not collapsed.[^atlas-bacteria-overview]

## The missing dimension is often time

A later organism can act on an environment altered by earlier participants. A starter addition and environmental inoculation are different starting conditions, while a measured endpoint does not reconstruct every earlier step. Read [Spontaneous fermentation](../processes/spontaneous-fermentation.md) and [Brettanomyces](brettanomyces.md) with those questions in mind.

For an LLM or researcher, a useful summary keeps the sample location, stage, method, organism name as reported, and the author's confidence in the proposed function. A flat list of organisms loses those qualifiers.

## Evidence note

The Sesotho study sampled five locations and five stages; its authors state that within-brewery biological batch replicates were unavailable. It therefore cannot establish the frequency of every pattern across repeated batches or every maker.[^atlas-sesotho] See [the cultural context](../culture/sesotho-social-occasions.md) for a separate limit: microbial sampling is not a detailed ethnography of ceremonies.

## Edition 1.8: newly sourced connections

Two further cases illustrate why fermentation **stage** and **sampling method** must accompany organism names. A 2024 Ethiopian borde study followed changing populations in three sampling locations and later dominance of yeasts and lactic-acid bacteria. A 2006 kodo ko jaanr study describes different trajectories for moulds, yeasts, lactic-acid bacteria and sugar conversion in finger millet. Neither dataset is a census of its entire geographical tradition.[^v18-borde][^v18-jaanr]

Compare [borde ecology](borde-microbial-succession.md), [jaanr ecology](jaanr-microbial-succession.md), and the [Shamita time-course](shamita-overnight-fermentation.md). Culture detection, demonstrated metabolic function and drinker perception remain separate claims.

## Edition 1.11: newly sourced connections

A five-stage whole-genome survey of [pulque](../microbiology/pulque-five-stage-metagenomics.md) reports changes in relative organisms alongside sugar, ethanol and acid. A separate [Tapirapé cauim study](tapirape-cauim-bacteria-and-yeast.md) examined peanut/rice fermentations with both culture-dependent methods and molecular profiles. The key finding across these **different** studies is the importance of stage, substrate and detection method—not a globally universal microbial order.[^v111-pulque-stages][^v111-cauim-dynamics]

Relative read abundance, isolate counts and measured metabolites answer different questions. Neither experiment proves that a named community maintains one unchanging culture or supplies evidence of food safety in an untested batch.

## Edition 1.13: newly sourced connections

A 2013 Beninese study monitored spontaneous fermentations and noted that direct molecular detection and culturing did not reveal exactly the same yeast species. By contrast, a 2022 Ivorian study challenged finished filtered tchapalo with selected strains and recorded shelf-life sensory changes. The first observes evolving communities; the second tests behavior in an altered beer system. Neither is a universal demonstration of which organisms must appear in every traditional beer.[^v113-tchou-2013][^v113-tchapalo-2022]

See [the isolate-method comparison](../categories/yeast-survey-method-disagreements.md) and [tchapalo fermentation versus spoilage](tchapalo-fermentation-versus-spoilage.md).

## Source notes
[^atlas-sesotho]: [Bacterial and Fungal Dynamics During the Fermentation Process of Sesotho, a Traditional Beer of Southern Africa](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2020.01451/full), Cason and colleagues, 2020. Sampling design and abstract consulted 27 October 2026.
[^atlas-bacteria-overview]: [Brewing bacteria overview in World Beer Wiki](../ingredients/brewing-bacteria.md), retained methodological distinctions and cited sources.

[^v18-borde]: [Characterization of borde: microbial analysis, rheological profiling, and functional attributes (2024)](https://www.sciencedirect.com/science/article/pii/S2666154324005350). Borde study authors. Consulted 2026-10-28. Access: Open publisher abstract and highlights; three Ethiopian sampling locations; biochemical and in-vitro results are not human health effects.

[^v18-jaanr]: [Microbiological and physico-chemical changes during fermentation of kodo ko jaanr (2006)](https://indianjournals.com/article/ijm-46-4-004). S. Thapa and J. P. Tamang. Consulted 2026-10-28. Access: Publisher-indexed abstract of measured finger-millet fermentation in Darjeeling/Sikkim; original full paper not reviewed.
[^v111-pulque-stages]: [Genomic profiling of bacterial and fungal communities and their predictive functionality during pulque fermentation by whole-genome shotgun sequencing (2020)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7493934/). Shotgun-metagenomic research team. Consulted 2026-10-28. Access: Open study abstract and indexed methods/results of five pulque stages; read counts and predicted functions do not demonstrate universal organisms or causation.
[^v111-cauim-dynamics]: [Determination of dynamic characteristics of microbiota in a fermented beverage produced by Brazilian Amerindians (2010)](https://pubmed.ncbi.nlm.nih.gov/20413168/). Fermentation-microbiology research team. Consulted 2026-10-28. Access: PubMed indexed abstract of Tapirapé peanut/rice cauim with culture-dependent and DGGE methods; separate substrate and sample.

[^v113-tchou-2013]: [Yeast dynamics during spontaneous fermentation of mawè and tchoukoutou (2013)](https://pubmed.ncbi.nlm.nih.gov/23756236/). A. Greppi and colleagues. Consulted 2026-10-28. Access: PubMed indexed abstract, two monitored productions of each food; culture-dependent and -independent profiles differ and do not define a standard starter.

[^v113-tchapalo-2022]: [Detection of spoilage-causing yeasts and bacteria in tchapalo (2022)](https://pubmed.ncbi.nlm.nih.gov/35344598/). C. K. Attchelouwa and colleagues. Consulted 2026-10-28. Access: PubMed abstract: 11 selected strains inoculated into sterile-filtered tchapalo over three days; sensory and volatiles are specific to that challenge system.
