---
type: Expansion Specification
title: World Beer Atlas expansion specification
description: Scope, architecture, acceptance criteria and implementation tracking for the cultural and scientific
  expansion.
tags:
- wiki-documentation
- specification
- roadmap
status: draft
generated:
  by: world-beer-wiki/1.5
  at: '2026-10-27T23:15:00Z'
sources:
- id: atlas-baseline
  resource: /editorial/research-update-1-1.md
  title: Edition 1.1 baseline research update
specification_version: '1.3'
implementation_status: fourth-installment-implemented
review_status: not-independently-reviewed
work_items:
- id: ATLAS-001
  title: Scope and evidence contract
  state: implemented
  paths:
  - editorial/atlas-specification.md
- id: ATLAS-002
  title: Cultural case studies
  state: implemented
  paths:
  - culture/index.md
  delivered_scope: Six situated case studies; additional regions and independent community review remain outside
    this installment.
- id: ATLAS-003
  title: Calendar and historical events
  state: implemented
  paths:
  - calendar/index.md
  delivered_scope: Five entries and an explicit 2026 edition record; no live schedules or universal agricultural
    calendar.
- id: ATLAS-004
  title: Microbiology reference layer
  state: implemented
  paths:
  - microbiology/index.md
  delivered_scope: Nine bounded references; some deliberately retain corpus-only or producer-specific evidence.
- id: ATLAS-005
  title: Botanicals and adjuncts
  state: implemented
  paths:
  - ingredients/juniper.md
  - ingredients/gesho.md
  - ingredients/coriander.md
  - ingredients/citrus-peel.md
  - ingredients/lactose.md
  - ingredients/smoked-malt.md
  delivered_scope: Six focused references; not an exhaustive botanical or adjunct encyclopedia.
- id: ATLAS-006
  title: Brewing process explanations
  state: implemented
  paths:
  - processes/index.md
  delivered_scope: Eight process explanations, not complete operational recipes.
- id: ATLAS-007
  title: Objects and serving practices
  state: implemented
  paths:
  - objects/index.md
  delivered_scope: Four text-based object/service references; licensed illustrations deferred.
- id: ATLAS-008
  title: Stories and sensory reading routes
  state: implemented
  paths:
  - stories/index.md
  - sensory/index.md
  delivered_scope: Four narrative routes and two sensory reasoning guides.
- id: ATLAS-009
  title: Typed evidence-bearing relationships
  state: implemented
  paths:
  - tools/atlas.py
  - editorial/reading-with-an-llm.md
  delivered_scope: Initial qualified relation vocabulary, source preservation and reverse-edge export; no unsupported
    ancestry edges.
- id: ATLAS-010
  title: Offline exports, validation and tests
  state: implemented
  paths:
  - tools/atlas.py
  - tests/test_atlas.py
  - .github/workflows/validate.yml
  - editorial/validation-report-1-2.md
  delivered_scope: Offline checks, deterministic JSON exports, regression tests and read-only pull-request
    artifacts.
- id: ATLAS-011
  title: Navigation and existing-profile integration
  state: implemented
  paths:
  - index.md
  - navigation/atlas.md
  - references/atlas-sources.md
  - tools/build_site.py
  delivered_scope: Ten-layer navigation, source supplement and twelve original-article connection sections;
    searchable-site compatibility preserved.
- id: ATLAS-012
  title: Community and specialist review
  state: planned
  paths: []
- id: ATLAS-013
  title: Licensed illustrations and pronunciation recordings
  state: deferred
  paths: []
- id: ATLAS-014
  title: Optional interactive atlas and date-aware discovery
  state: deferred
  paths: []
- id: ATLAS-015
  title: Focused history and archaeological context
  state: implemented
  paths:
  - history/index.md
  delivered_scope: Seven evidence-bounded historical cases and a method guide; not a universal archaeological
    chronology.
- id: ATLAS-016
  title: Extended cultural and seasonal source research
  state: implemented
  paths:
  - culture/index.md
  delivered_scope: Seven new cultural accounts and four seasonal/calendar articles; local evidence boundaries
    retained.
- id: ATLAS-017
  title: Microbial genomes and fermentation ecology
  state: implemented
  paths:
  - microbiology/index.md
  delivered_scope: Eight newer microbial references, strain versus species and study-design caveats.
- id: ATLAS-018
  title: Expanded grains, botanical materials and brewing processes
  state: implemented
  paths:
  - ingredients/index.md
  delivered_scope: Eight ingredient references and six process explanations; no foraging or microbiological
    safety protocols.
- id: ATLAS-019
  title: Historical stories, serving objects and sensory chemistry
  state: implemented
  paths:
  - stories/index.md
  delivered_scope: Four new stories, three objects and three sensory explanations, all linked to canonical
    topics.
- id: ATLAS-020
  title: More comparative family/category guides
  state: implemented
  paths:
  - categories/index.md
  delivered_scope: Four new comparison guides, without collapsing local traditions into a global style ladder.
- id: ATLAS-021
  title: Meaningful updates to canonical existing profiles
  state: implemented
  paths:
  - navigation/atlas.md
  delivered_scope: Fifteen original articles received sourced edition-1.3 research extensions, with original
    URLs preserved.
- id: ATLAS-022
  title: Source supplement, 1.3 release and reproducible quality checks
  state: implemented
  paths:
  - references/atlas-sources-1-3.md
  delivered_scope: A full source register for 1.3, validation and release notes. Structural tests cannot substitute
    for expert review.
- id: ATLAS-023
  title: Date-aware offline event and season export
  state: implemented
  paths:
  - tools/atlas.py
  delivered_scope: Deterministic timeline export from metadata; does not predict future festival dates or create
    notifications.
- id: ATLAS-024
  title: Broaden culturally located social and ritual accounts
  state: implemented
  paths:
  - culture/index.md
  delivered_scope: Seven located social and economic cases and two additional calendar references; no community
    endorsement asserted.
- id: ATLAS-025
  title: Expand archeological and industrial-science histories
  state: implemented
  paths:
  - history/index.md
  delivered_scope: Six historical source-bound explanations; excludes unsourced direct lineage and precise
    reconstructions.
- id: ATLAS-026
  title: Introduce climate and environmental research section
  state: implemented
  paths:
  - environment/index.md
  delivered_scope: Six cross-source articles on barley, hops, water, energy and spent grain; no universal carbon
    ranking.
- id: ATLAS-027
  title: Introduce evidence-based food pairing section
  state: implemented
  paths:
  - food/index.md
  delivered_scope: Three experimental/interview-based articles; not prescriptive universal pairing lists.
- id: ATLAS-028
  title: Deepen fermentation, chemistry, beer stability and serving
  state: implemented
  paths:
  - sensory/index.md
  delivered_scope: Microbiology, ingredients, processes, objects and sensory material with traceable references.
- id: ATLAS-029
  title: Revise canonical existing pages using new research
  state: implemented
  paths:
  - styles/pito.md
  delivered_scope: Nineteen existing subject pages updated with sourced context and citations; canonical URLs
    kept.
- id: ATLAS-030
  title: Publish source provenance, tests and edition documentation
  state: implemented
  paths:
  - references/atlas-sources-1-4.md
  delivered_scope: 35 source records with actual access scopes; validators and CI remain separate from expert
    review.
- id: ATLAS-031
  title: Improve queryable provenance and data checks
  state: implemented
  paths:
  - tools/atlas.py
  delivered_scope: Add portable source-audit output and typed-target relation validation with focused regression
    tests.
- id: ATLAS-032
  title: Cerro Baúl archaeology, materials and social context
  state: implemented
  paths:
  - history/cerro-baul-wari-brewery.md
  - culture/wari-brewing-and-state-hospitality.md
  - objects/wari-brewing-vats-and-kero-cups.md
  delivered_scope: Original excavation and later abstract-based reassessment; no claim of exact ancient recipe
    or empire-wide domestic production.
- id: ATLAS-033
  title: Documented labor, medieval trade and contemporary US voices
  state: implemented
  paths:
  - history/medieval-england-brewsters-and-change.md
  - culture/american-beer-oral-histories.md
  - history/peoples-brewing-and-ownership.md
  delivered_scope: Four source families with explicitly distinguished museum, book-abstract and archival evidence;
    no oral histories passed off as listened-to.
- id: ATLAS-034
  title: Mixed starters in Asian traditions and African isolate research
  state: implemented
  paths:
  - microbiology/himalayan-dry-starter-diversity.md
  - microbiology/vietnamese-banh-men-communities.md
  - microbiology/non-saccharomyces-yeasts-in-abidjan-sorghum-beer.md
  delivered_scope: Microbial sampling, function and local naming remain separate; neither isolate detection
    nor cultured strains certify safety.
- id: ATLAS-035
  title: Botanicals, perception, food and research-stage uncertainty
  state: implemented
  paths:
  - ingredients/schinus-molle-in-andean-ferments.md
  - sensory/bitterness-is-not-one-number.md
  - food/situational-pairing-and-storage-evidence.md
  delivered_scope: Ingredient-context, controlled sensory and Tuscan study interpretation with specific access
    limits; no universal pairing prescription.
- id: ATLAS-036
  title: Edition-aware current style guideline comparison
  state: implemented
  paths:
  - categories/bjcp-2021-versus-ba-2026.md
  - stories/one-title-two-guidelines.md
  delivered_scope: Compare BJCP beer 2021 and Brewers Association 2026 with attribution, without reproducing
    proprietary category definitions.
- id: ATLAS-037
  title: Complete source-derived subject directory and stale-index regression check
  state: implemented
  paths:
  - navigation/all-atlas-subjects.md
  - tools/build_subject_index.py
  - tests/test_subject_index.py
  delivered_scope: All subject types included with deterministic sorting; CI and tests fail when the generated
    directory is stale.
- id: ATLAS-038
  title: Source register, review queue and existing-article research integration
  state: implemented
  paths:
  - references/atlas-sources-1-5.md
  - editorial/source-review-queue-1-5.md
  - editorial/research-update-1-5.md
  delivered_scope: Twenty-two distinct referenced works with source access limits, fourteen existing-source
    revisions and a review queue without claims of external sign-off.
---

# World Beer Atlas expansion specification

**Specification 1.3 · fourth installment implemented · 27 October 2026.** This is the scope and acceptance contract for extending World Beer Wiki beyond style descriptions. “Atlas” describes the connected reference model, not a compulsory project rename or a claim of complete geographical coverage.

The [human-readable progress report](atlas-progress.md) and `python tools/atlas.py progress` reflect the YAML ledger in this document’s frontmatter. The ledger tracks delivered scope, not human approval.

## 1. Purpose and baseline

The 1.1 baseline contains 166 beer/tradition profiles, 17 ingredient references and 13 category guides. It already distinguishes living traditions, judging categories, related ferments and archaeological evidence. Preserve that investment and its canonical filenames.[^atlas-baseline]

The expansion should answer not only *what is this beer?* but *who makes it, why, when, with what materials and organisms, using which techniques, and according to whose account?* Readers should be able to follow an ingredient, a fermentation practice, a celebration or an object across several articles without mistaking similarity for descent.

This continuing release is a substantial, source-bounded installment across the proposed layers. It is not a promise to complete an encyclopedia of every ritual, plant, organism or beer festival.

## 2. Deliverable states and progress rules

`work_items` in this document is the authoritative implementation ledger. Stable IDs belong in change descriptions and review discussions. States mean:

| State | Meaning |
|---|---|
| `planned` | Accepted scope; no completed deliverable is asserted. |
| `partial` | A useful subset exists; the remaining acceptance work must be recorded. |
| `implemented` | The explicitly scoped deliverable exists, is linked, and passes applicable structural checks. |
| `deferred` | Deliberately outside this installment; not silently forgotten. |

Implementation is **not** epistemic verification. All researched articles remain `status: draft`. Independent human review, community consultation and implementation progress are separate facts. Never mark an article community-approved without an actual, attributable review and permission to disclose it. Do not produce a global “percent complete” for an open-ended world encyclopedia. Counts may summarize this finite work ledger and its named deliverables only.

A work item marked implemented must have nonempty repository paths that exist. Planned article titles must not be represented by broken Markdown links or empty placeholder articles. If scope changes, preserve the work ID, explain the change and update the log.

## 3. Information architecture

Keep `styles/`, `ingredients/` and `categories/` intact. Add independent, linked concepts in these sections as evidence permits:

| Section | Unit of knowledge | Boundary |
|---|---|---|
| `culture/` | A situated institution, social practice or knowledge-transmission case | Not a universal account of a nation, gender or Indigenous people. |
| `calendar/` | A seasonal practice, recurring event or dated historical episode | Not an automatically current travel/event schedule. |
| `microbiology/` | An organism, culture concept or ecological mechanism | Species, strain, starter and community are distinct levels. |
| `processes/` | A named transformation or production operation | Explanatory reference, not a complete validated operating procedure. |
| `objects/` | Equipment, vessels or a documented serving practice | An object does not establish a beer's ancestry or authenticity. |
| `stories/` | A short narrative or comparative reading route | Claims still require evidence; entertaining framing must not invent events. |
| `sensory/` | A perceptual distinction and its possible causes | Aroma descriptors are not ingredient declarations. |

Botanicals and adjuncts remain under `ingredients/`; do not create parallel duplicate articles under a second plant directory. Existing `ingredients/kveik.md`, yeast and bacteria overviews remain stable entry points. New organism pages deepen rather than replace them.

Every populated subject directory needs an `index.md`. The root must expose all layers. Cross-links should let readers return from a process or culture article to the relevant beers. Navigation, exports and reverse-link views are derivative access aids, never independent historical evidence.

## 4. Article acceptance criteria

Each new subject article must have a useful opening answer, a bounded `scope`, source metadata, claim-linked footnotes, an evidence/limitations note, and at least two relevant internal reading links. A small number of substantive paragraphs is preferable to padded or repetitive sections.

A cultural article records place, community or institution where documented, the time represented by the evidence, participants and social function, and variation or limits. Preserve original-language names and attribution to narrators and translators. Do not manufacture a pronunciation guide from English spelling.

A process article distinguishes input, transformation and outcome, and identifies what can vary. A microbial article distinguishes detection from demonstrated function, notes the studied strain or setting, and does not turn a sample into a universal microbial recipe. An ingredient article distinguishes plant or material identity, processing form, brewing role and sensory association.

A story should pose an engaging question, provide the documented account, state what remains uncertain, and lead to deeper canonical references. Anecdotes may be attributed as anecdotes; a repeated legend is not an established origin story. Do not create redundant pages solely to increase counts.

## 5. Research and cultural stewardship

Prefer primary studies, named firsthand fieldwork, community-authored or community-partnered accounts, archival evidence, and institutions describing their own practices. A producer is a primary source for its own method, not an independent arbiter of a universal origin. Reviews can establish orientation but must be labelled and not substituted for an experiment they summarize.

Record what was actually accessed: full article, particular sections, abstract, translation or indexed excerpt. A URL is not proof that the full source was read. Preserve inherited access notes when retaining existing text; distinguish new research from existing corpus synthesis. Record source date separately from consultation date.

Use community-specific language. Avoid describing all African grain beers, all Asian rice ferments or all farmhouse cultures as interchangeable. Do not portray living communities as unchanged archaeological survivals. Describe gendered labor only for the documented setting and period. Participation in a festival or community must not be equated with compulsory alcohol consumption.

Public availability is not blanket permission to reproduce sacred, restricted or personally identifying knowledge. Prefer respectful high-level descriptions; seek community guidance before adding sensitive detail. Do not solicit private ritual instructions, copy substantial source text, or publish unlicensed images/audio. Add corrections as attributable changes, not quiet erasure of disagreement.

## 6. Calendar model

Calendar metadata must distinguish `seasonal`, `recurring-event` and `historical-event`. Each record carries a calendar system or explicitly states that it is a local seasonal description. Store human-readable timing and geographical context; do not silently force local, religious or agricultural calendars into fixed Gregorian dates.

Exact event editions require an explicit year, start/end date, source identifier and checked-on date. Annual or biennial occurrence does not imply an unbroken series or a calculable future date. A December field observation supports that observation, not a rule for all northern brewing. Northern and southern hemispheres must not share an unlabeled harvest calendar.

For this installment, a readable seasonal/event directory is in scope. Live schedules, reminders, booking recommendations, “on this day” notifications and automatic lunisolar conversion are deferred. A future date-aware feature must never advertise a past edition as upcoming.

## 7. Relationship and retrieval contract

Retain existing `compare_with` relations and the legacy `compares` spelling as editorial comparisons without ancestry implications. New articles use `compare_with`; exports preserve legacy spelling rather than silently changing existing metadata. New factual relations should have `relation`, canonical `target`, `source_ids` and a nonempty `qualifier` stating the setting and limitation. All referenced sources must exist in the containing article, and all targets must also be linked in its body.

Initial relationship vocabulary: `compare_with`, `uses_ingredient`, `uses_process`, `associated_with`, `observed_organism`, and `uses_object`. `associated_with` is deliberately weaker than “invented by” or “descended from.” `observed_organism` must not become a mandatory ingredient claim. The first release does not encode unverified ancestry, ethnicity ownership, universal safety or exclusive invention.

An export should preserve source identifiers, scope, review status and qualifiers. It must not flatten a qualified relation into an unqualified triple or infer that an ingredient contributes every aroma descriptor associated with it. Reverse links should retain their originating article and evidence.

## 8. Maintenance and automated acceptance

Reading stays Markdown-only and offline. Supporting Python tooling is optional. Keep the existing validator and add narrowly tested checks for new subject directories, relationship evidence, calendar data and implementation-ledger paths. Reject duplicate YAML keys, missing citations, escaped paths, broken links and unindexed new subject pages.

Provide a deterministic machine-readable catalog and progress report from the source Markdown rather than requiring a database. Sort outputs so review diffs are meaningful. Do not fetch external sites during offline validation. A successful check verifies structure, not historical truth or live URL health.

Continuous integration should run with read-only repository permissions, use ordinary pull-request events rather than privileged `pull_request_target`, and upload validation results and a portable repository snapshot. It must not publish secrets or require credentials for reading the wiki. Add focused regression tests for negative cases as well as the happy path.

## 9. Completion gates for this installment

The candidate is ready for review when the ledger points to the delivered files; all populated directories and the root connect; new factual passages have source support and access limits; calendar entries distinguish recurrence from dated editions; the source supplement identifies its coverage; the validators and tests have actually run; and the PR reports exact checked counts and any remaining limitations.

Do not claim that all earlier articles have been re-researched. Identify actual updated profiles and distinguish substantive corrections from navigation additions. Preserve the prior release reports as historical reports rather than rewriting their results to match the new corpus.

## 10. Prioritized follow-on backlog

Community-reviewed coverage remains the highest-value unfinished work. Priorities include locally authored accounts of Ali-Aye-Ligang and Apong, Gawai and rice tuak, chicha festivals and labor, regional Sahti calendars, women’s brewing economies, and traditions from underrepresented parts of Asia, Africa, the Americas and the Pacific.

Further research candidates include malt-house associations; beer in weddings, funerals and hospitality; historical tax and trade systems; hop harvests by region; historical winter brewing laws; botanical species and plant-part identification; nursery and starter terminology; additional mold-assisted traditions; cask service; and licensed material-culture illustrations. These are research questions, not facts established by listing them here.

Defer exhaustive hop cultivar/strain/product catalogs, brewery inventory, medical/nutritional advice, recipe calculators, real-time event schedules, automatic regulatory labeling advice, an interactive map application, and independent human verification claims. A future map must distinguish place of documented practice from claimed origin and present distribution.

## Reference

[^atlas-baseline]: [Edition 1.1 baseline research update](research-update-1-1.md). Repository release record, not an external historical source.

[Home](../index.md) · [Evidence method](methodology.md) · [Coverage and gaps](coverage-and-gaps.md)


## 11. Edition 1.3 research expansion

The second installment adds 55 subject pages across 10 topic sections, including the new `history/` section. It also extends fifteen previously researched canonical entries. Stable work IDs **ATLAS-015 to ATLAS-023** track the new finite deliverables and their actual paths. Each article carries a claim-specific source and access limit. The prior fourteen IDs remain intact.

A new offline `timeline` export presents only explicitly documented seasons and event editions; it does not project annual dates into the future. Comparisons remain qualified and do not infer shared ancestry. Research articles stay draft; ATLAS-012 remains unfulfilled. This installment **does not** deliver community endorsement, licensed media, or a live event-service application.

### Remaining high-value research

The next research cycle should broaden living-source coverage in Africa, Central/South America, the Pacific and underrepresented parts of Asia; improve community-language checking and reciprocal review; revisit inaccessible full papers and historical records; and add more verified traditions around weddings, memorials, taverns, craft guilds and changing consumption laws. The use of a secondary history source must remain visible until original documents are actually inspected.

## 11. Edition 1.4: environment, dining and historic inference

The edition adds `environment/` and `food/` as evidence-based comparison sections. Environmental claims require defined geography and system boundaries; interview-based pairing strategies are not universally confirmed human preferences. Histories of science are distinguishable from earlier community techniques, and a literary hymn is not silently converted into a quantified brewing recipe. New source audit reports describe **provenance coverage**, not independent truth verification. The implementation ledger retains community/specialist review as planned, not completed.


## 11. Edition 1.5 research and navigation requirements

The source-backed 1.5 expansion records specific bounded case studies and increases the corpus to **372** subject articles. The 31 additions and fourteen existing-entry research extensions are listed in the [research update](research-update-1-5.md); the [complete subject index](../navigation/all-atlas-subjects.md) is deterministic and spans every subject section, including ones outside the original style/name lists. `python tools/build_subject_index.py --check` must pass in CI.

Interpretation of oral-history catalog records must retain narrator and access distinctions; citation of an archive finding aid is *not* equivalent to reading an individual transcript. An excavated brewery supports a particular site, not an exact ancient recipe or proof of a direct living lineage. Microbiological detections must not be promoted to universal practices or food safety assessments. Style guideline version claims require both publisher and edition; do not combine 2021 BJCP and 2026 BA into one undated taxonomy. See the [source review queue](source-review-queue-1-5.md) for research not yet independently verified.

**Current scope is finite and reviewable:** implementation of ATLAS-032 through ATLAS-038 completes those *specified deliverables only*. ATLAS-012 human/community review remains planned. Licensed media and interactive live calendars remain deferred. The remaining-source questions have responsible next actions, not false completion labels.
