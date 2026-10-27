---
type: Editorial Research Update
title: World Beer Atlas research extension 1.3
status: draft
description: Evidence-led expansion into living brewing culture, historical debates, materials, microbiology and service.
tags: [wiki-documentation, research, edition-1.3]
generated:
  by: world-beer-wiki/1.3
  at: '2026-10-27T22:50:00Z'
sources:
- id: atlas-spec
  resource: /editorial/atlas-specification.md
  title: World Beer Atlas expansion specification
- id: atlas-sources-13
  resource: /references/atlas-sources-1-3.md
  title: Research source supplement 1.3
---

# Edition 1.3: deepen the connected World Beer Atlas

**Research and consultation date: 27 October 2026.** This installment builds on merged PR #2 while preserving all 166 canonical beer/tradition profile paths, the 1.2 research report and the optional searchable site. It adds **55 source-bounded articles**, expands **15 existing articles** with new researched passages, introduces an independent `history/` layer, and extends the [tracked specification](atlas-specification.md) with **ATLAS-015–023**. The corpus now has **295 subject articles across eleven sections**.

## What's new

| Subject layer | Additional articles | New lines of inquiry |
|---|---:|---|
| [Culture](../culture/index.md) | 7 | Beer as Belgian cultural heritage; makgeolli sharing; Gawai rice tuak; Nubri chang; Norwegian Christmas practices; British pub service; sorghum-based livelihoods |
| [Calendar](../calendar/index.md) | 4 | Mising Ali-Aye-Ligang; Sarawak Gawai; Norwegian bryggjardøgra; harvest as geographically distinct time |
| [History and archaeology](../history/index.md) | 8 | Raqefet, Mijiaya/Shangshan method, Egyptian residues, Kirikongo, industrial porter, Bavarian purity regulation, U.S. Prohibition, UNESCO's 2016 recognition |
| [Microbiology](../microbiology/index.md) | 8 | Two 2026 farmhouse yeast genomic studies; diastatic yeast; spoilage LAB; aromatic metabolites; nuruk isolates; ancient fungal inference |
| [Ingredients](../ingredients/index.md) | 8 | Bog myrtle, yarrow, heather, spruce/pine tips; jora; sorghum malt; Job's tears; kilned malt colors and chemistry |
| [Processes](../processes/index.md) | 6 | Malting, cask conditioning, gravity service, botanical additions, maintained microbial cultures, enzyme-associated hop creep |
| [Objects and service](../objects/index.md) | 3 | Beer engines, casks and cellars, archaeological vessels |
| [Sensory](../sensory/index.md) | 3 | Yeast esters and phenols, thiols, DMS and perception |
| [Stories](../stories/index.md) | 4 | Porter invention story, purity law myth, yeast-community surprise, beer-before-farming question |
| [Category guides](../categories/index.md) | 4 | Herbal/gruit, heritage, social institutions and fermentation beyond ale/lager |

## Research decisions that matter

**Living culture is not a beer style.** The [Belgian UNESCO inscription](../culture/belgian-beer-as-living-heritage.md) and [South Korea's nationally recognized makgeolli practice](../culture/makgeolli-making-and-sharing.md) are examples of institutional recognition at *different* levels, not a ranking of cultural worth. [Sarawak's Gawai](../culture/gawai-dayak-rice-tuak.md) and [Ali-Aye-Ligang](../calendar/ali-aye-ligang.md) are located seasonal accounts; neither defines every local ceremony or a fixed worldwide calendar.

**Household yeast can be a population.** The [farmhouse diversity reference](../microbiology/farmhouse-yeast-diversity.md) describes a 2026 study of 1,760 isolates across 44 European cultures; [Norwegian kveik genomic work](../microbiology/kveik-genomic-research-2026.md) samples a different set. A household culture, a cloned strain and a species name should not be substituted for one another.

**Ancient brewing is inferred from multiple proxies.** [Raqefet Cave](../history/raqefet-cave-brewing-evidence.md) supplies evidence interpreted as Natufian brewing before local cereal domestication, not proof that beer caused farming. [Mijiaya](../styles/mijiaya-beer.md), [Shangshan](../styles/shangshan-beer.md) and [Egyptian residue research](../history/egyptian-brewing-residue-studies.md) illustrate different methods and chronologies. There is no asserted straight lineage between the sites.

**A good origin story may be historically misleading.** [London porter](../history/london-porter-and-industrialization.md) is treated in light of scholarship questioning the single-inventor story; [Bavarian purity regulation](../history/bavarian-purity-law-and-its-afterlife.md) separates the actual 1516 ordinance from the later name and national branding. These articles are histories, not authoritative statements of current law.

**The ingredient list is not a chemistry report.** [Jora](../ingredients/jora-maize.md) describes processed maize rather than raw-grain equivalence. [Herbal gruit](../categories/herbal-beer-and-gruit.md) separates named plants from tax and trading histories. [Esters](../sensory/yeast-esters-and-phenols.md), [thiols](../sensory/thiols-and-fruit-aromas.md) and [DMS](../sensory/dms-and-cooked-cereal.md) show why a familiar flavor descriptor alone cannot prove an ingredient.

## Review, source access and cultural stewardship

The [source supplement](../references/atlas-sources-1-3.md) lists **45 source records** with what was actually used. These are not 45 newly published studies; some were already used earlier and some sources were consulted only through abstracts, official summaries or producer accounts. The original articles retain claim-linked footnotes and source-specific boundaries. We did not claim to read paywalled full articles where only an abstract was accessible.

All articles remain **AI-researched drafts without independent expert or community review**. Ritual accounts are situated, do not disclose private knowledge, and do not imply participation is mandatory. Sources are in English and some Norwegian; local-language and community review are priorities, especially for underrepresented regions. Archaeological interpretation is not a living people's authorized origin account. No copyrighted source illustrations or audio were reproduced.

## Reproducibility and next work

The repository's [validation report](validation-report-1-3.md) describes structural checks. `python tools/atlas.py timeline` exports documented seasonal and event records **without calculating future dates**. For a contextual reading route, use the updated [Atlas navigation](../navigation/atlas.md) and [scope ledger](atlas-progress.md).

Highest-value unfinished work is independent review and situated, community-authored coverage beyond this initial set; primary-source historical detail; more research in currently thin regions; verified bibliography locators; safe licensing for media; and carefully designed interactive discovery. These have not been silently marked complete.

[Home](../index.md) · [Sources](../references/atlas-sources-1-3.md) · [Specification](atlas-specification.md) · [Progress](atlas-progress.md)
