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
  by: world-beer-wiki/1.18
  at: '2026-10-28T11:20:00Z'
sources:
- id: atlas-baseline
  resource: /editorial/research-update-1-1.md
  title: Edition 1.1 baseline research update
specification_version: '1.13'
implementation_status: research-edition-1.18
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
  delivered_scope: Offline checks, deterministic JSON exports, regression tests and read-only pull-request artifacts.
- id: ATLAS-011
  title: Navigation and existing-profile integration
  state: implemented
  paths:
  - index.md
  - navigation/atlas.md
  - references/atlas-sources.md
  - tools/build_site.py
  delivered_scope: Ten-layer navigation, source supplement and twelve original-article connection sections; searchable-site
    compatibility preserved.
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
  delivered_scope: Seven evidence-bounded historical cases and a method guide; not a universal archaeological chronology.
- id: ATLAS-016
  title: Extended cultural and seasonal source research
  state: implemented
  paths:
  - culture/index.md
  delivered_scope: Seven new cultural accounts and four seasonal/calendar articles; local evidence boundaries retained.
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
  delivered_scope: Eight ingredient references and six process explanations; no foraging or microbiological safety
    protocols.
- id: ATLAS-019
  title: Historical stories, serving objects and sensory chemistry
  state: implemented
  paths:
  - stories/index.md
  delivered_scope: Four new stories, three objects and three sensory explanations, all linked to canonical topics.
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
  delivered_scope: Fifteen original articles received sourced edition-1.3 research extensions, with original URLs
    preserved.
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
  delivered_scope: Six historical source-bound explanations; excludes unsourced direct lineage and precise reconstructions.
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
  delivered_scope: Nineteen existing subject pages updated with sourced context and citations; canonical URLs kept.
- id: ATLAS-030
  title: Publish source provenance, tests and edition documentation
  state: implemented
  paths:
  - references/atlas-sources-1-4.md
  delivered_scope: 35 source records with actual access scopes; validators and CI remain separate from expert review.
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
  delivered_scope: Microbial sampling, function and local naming remain separate; neither isolate detection nor
    cultured strains certify safety.
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
  delivered_scope: Compare BJCP beer 2021 and Brewers Association 2026 with attribution, without reproducing proprietary
    category definitions.
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
  delivered_scope: Twenty-two distinct referenced works with source access limits, fourteen existing-source revisions
    and a review queue without claims of external sign-off.
- id: ATLAS-039
  title: Document banana-based ferments and community-named Assam rice drinks
  state: implemented
  paths:
  - styles/tonto.md
  - styles/urugwa.md
  - styles/hor-alank.md
  - styles/zu-hmar.md
  delivered_scope: Four explicitly bounded local beverage profiles, with unlike substrates and community names
    kept distinct; not universal beer-style rules.
- id: ATLAS-040
  title: Research situated cultural learning and non-fixed ceremonial timing
  state: implemented
  paths:
  - culture/southern-assam-five-beverage-study.md
  - culture/sahti-apprenticeship-and-celebration.md
  - culture/mapuche-fermented-drinks-and-source-voices.md
  - calendar/sahti-occasions-without-a-fixed-date.md
  delivered_scope: Community-specific research accounts, source mediation and occasion-linked timing without invented
    annual dates or consent claims.
- id: ATLAS-041
  title: Deepen microbial survey interpretation and farmhouse population studies
  state: implemented
  paths:
  - microbiology/assam-rice-ferment-sampling.md
  - microbiology/umqombothi-amplicons-and-predicted-function.md
  - microbiology/kveik-population-history-2026.md
  - microbiology/hop-resistant-lactic-acid-bacteria.md
  - microbiology/maltose-negative-yeast-and-low-alcohol.md
  delivered_scope: Five microbiology references distinguishing culture, isolate, DNA detection, biochemical function
    and study size.
- id: ATLAS-042
  title: Connect materials, processes, sensory pathways, objects and historical inference
  state: implemented
  paths:
  - ingredients/rhynchosia-root-for-munkoyo.md
  - ingredients/banana-juice.md
  - ingredients/ferulic-acid-in-wort.md
  - processes/munkoyo-root-starch-conversion.md
  - sensory/clove-aroma-and-4-vinylguaiacol.md
  - objects/assam-earthen-pots-and-covers.md
  delivered_scope: Root enzymes, fruit substrate, yeast-derived flavor, process comparison and vessels with bounded
    sources.
- id: ATLAS-043
  title: Separate environmental LCA units and system boundaries
  state: implemented
  paths:
  - environment/mexican-microbrewery-footprint-case.md
  - environment/japanese-small-brewery-lca-case.md
  delivered_scope: Two independent local case studies; no misleading single score across incompatible system boundaries.
- id: ATLAS-044
  title: Integrate new citations into existing research and review queue
  state: implemented
  paths:
  - styles/munkoyo.md
  - styles/umqombothi.md
  - ingredients/kveik.md
  - references/atlas-sources-1-6.md
  - editorial/source-review-queue-1-6.md
  delivered_scope: Twenty-two original entries revised with source-specific context; 21 external source records
    used, access and review limitations logged.
- id: ATLAS-045
  title: Add offline editorial hygiene checks and edition 1.6 reproducibility
  state: implemented
  paths:
  - tools/research_quality.py
  - tests/test_research_quality.py
  - editorial/validation-report-1-6.md
  - navigation/all-atlas-subjects.md
  delivered_scope: New regression-tested evidence hygiene checks and generated complete index; validators remain
    distinct from factual expert review.
- id: ATLAS-046
  title: Investigate Abydos early royal brewery and excavation interpretation
  state: implemented
  paths:
  - history/abydos-early-royal-brewery.md
  - objects/abydos-vats-and-fire-legs.md
  - stories/the-brewery-once-called-a-kiln.md
  delivered_scope: Three distinct evidence-bounded accounts, separating material traces, excavator estimates and
    royal ritual hypothesis.
- id: ATLAS-047
  title: Differentiate Andean household chicha, local service calendars and archival histories
  state: implemented
  paths:
  - culture/piura-chicheras-and-household-sales.md
  - calendar/piura-chicha-sales-days.md
  - objects/piura-chicha-white-flags.md
  - history/arequipa-chicherias-colonial-republican-records.md
  delivered_scope: Four local accounts with their own periods and methods; no future sales schedules or direct
    prehistoric lineage inferred.
- id: ATLAS-048
  title: Broaden Ghanaian, Ethiopian and Japanese brewing social research
  state: implemented
  paths:
  - culture/ghana-pito-bars-migration-and-identity.md
  - culture/ghana-pito-women-enterprise-survey.md
  - culture/tella-hospitality-and-household-economy.md
  - culture/japanese-koji-sake-heritage-and-apprenticeship.md
  delivered_scope: Four context-specific cases retaining survey, anthropology, review and heritage inscription
    limitations.
- id: ATLAS-049
  title: Explain Philippine tapuy, bubod and parallel mixed fermentation
  state: implemented
  paths:
  - styles/tapuy-philippine-rice-ferment.md
  - ingredients/bubod-starter.md
  - microbiology/bubod-tapuy-isolate-study.md
  - processes/parallel-starch-and-alcohol-fermentation.md
  - categories/koji-sake-and-rice-ferment-boundaries.md
  delivered_scope: Five coordinated references, never confusing isolate counts with mandatory starter composition
    or sake with beer.
- id: ATLAS-050
  title: Deepen spoilage microbiology and dynamic sensory chemistry
  state: implemented
  paths:
  - microbiology/hora-horc-and-hop-resistance-markers.md
  - microbiology/craft-brewery-filling-line-microbes.md
  - sensory/vicinal-diketones-as-moving-target.md
  delivered_scope: Selected mechanistic and facility research with strain, precursor and study design limitations.
- id: ATLAS-051
  title: Compare environment and sensory research with reproducible evidence boundaries
  state: implemented
  paths:
  - environment/beer-packaging-transport-and-return-loops.md
  - environment/spent-grain-food-safety-and-circularity.md
  - food/cheese-beer-preference-is-not-a-rule.md
  delivered_scope: Three study-based guides; no universal footprint, safe handling or pairing claims.
- id: ATLAS-052
  title: Improve gender-history comparisons, narrative trails and original articles
  state: implemented
  paths:
  - categories/gender-and-brewing-what-the-sources-show.md
  - history/brewsters-household-labor-in-medieval-england.md
  - history/ale-tasters-and-brewster-protests.md
  - navigation/edition-1-7-reading-trails.md
  delivered_scope: New cross-cultural/archival guides and 16 original subject-page evidence extensions, without
    modifying prior canonical paths.
- id: ATLAS-053
  title: Maintain source provenance, research hygiene and edition navigation
  state: implemented
  paths:
  - references/atlas-sources-1-7.md
  - tools/research_quality.py
  - tests/test_research_quality_v17.py
  - editorial/research-update-1-7.md
  - editorial/validation-report-1-7.md
  delivered_scope: Reproducible audit for edition 1.7 and existing 1.6, updated subject index, complete backlinks
    and CI checks.
- id: ATLAS-054
  title: Shawi cassava fermentation and cultural evidence
  state: implemented
  paths:
  - culture/shawi-masato-and-water.md
  - processes/shawi-masato-preparation.md
  delivered_scope: Community-partnered photographic and microbiological observations in one Shawi community; no
    public-health generalization.
- id: ATLAS-055
  title: Mbege process, botanical input and contextual ritual evidence
  state: implemented
  paths:
  - culture/mbege-as-regional-knowledge.md
  - processes/mbege-nyalu-and-mso.md
  - ingredients/msesewe-stem-bark-in-mbege.md
  - culture/chagga-ritual-beer-in-rombo.md
  delivered_scope: One northeastern Tanzania process and abstract-bounded Rombo anthropology, explicitly separated.
- id: ATLAS-056
  title: Ethiopian food-drinks and Himalayan millet ecology
  state: implemented
  paths:
  - styles/borde-ethiopian-fermented-cereal.md
  - styles/shamita-ethiopian-fermented-barley.md
  - microbiology/jaanr-microbial-succession.md
  delivered_scope: Primary sampling and review evidence for locally named beverages, distinguishing food use, organisms
    and process stages.
- id: ATLAS-057
  title: Beer foam proteins and aging chemistry
  state: implemented
  paths:
  - ingredients/beer-foam-active-proteins.md
  - sensory/heat-ltp1-and-beer-foam.md
  - sensory/beer-staling-and-aldehydes.md
  delivered_scope: Laboratory protein and chemical-aging evidence; no universal head-retention or shelf-life prescription.
- id: ATLAS-058
  title: Hop chemistry, yeast effects and source-to-aroma uncertainty
  state: implemented
  paths:
  - ingredients/polyfunctional-thiol-precursors.md
  - microbiology/thiol-release-and-yeast-timing.md
  - sensory/hop-terpenoid-biotransformation.md
  delivered_scope: Original research on measured precursors, terpenoids and thiols with strain and sampling qualifications.
- id: ATLAS-059
  title: Evidence QA, indexes, research register and reading trails
  state: implemented
  paths:
  - references/atlas-sources-1-8.md
  - editorial/research-update-1-8.md
  - editorial/validation-report-1-8.md
  - navigation/edition-1-8-reading-trails.md
  - tests/test_research_quality_v18.py
  delivered_scope: Cite-used research edition hygiene, persistent backlog and reproducible checks across new and
    revised articles.
- id: ATLAS-060
  title: Vietnamese jar-ferment traditions, materials, occasions and livelihoods
  state: implemented
  paths:
  - styles/ruou-can-vietnamese-jar-ferment.md
  - culture/stieng-ruou-can-and-transmission.md
  - culture/ma-ruou-can-in-lam-dong.md
  - objects/vietnamese-communal-jar-and-straws.md
  delivered_scope: Four situated accounts and wider navigation; national heritage reporting remains distinct from
    UNESCO and community endorsement.
- id: ATLAS-061
  title: Bhutanese ara culture and Himalayan phab laboratory comparison
  state: implemented
  paths:
  - culture/bhutan-ara-and-social-ritual.md
  - microbiology/phab-dry-starter-research.md
  delivered_scope: Bhutanese fieldwork abstract versus 35-starter isolate research; distillation and practice remain
    distinct.
- id: ATLAS-062
  title: Ur III and Sumerian archives, terminology and inference
  state: implemented
  paths:
  - history/ur-iii-beer-ration-tablet.md
  - history/sumerian-beer-terms-and-uncertainty.md
  - stories/the-tablet-was-not-the-recipe.md
  delivered_scope: One catalogued artifact and a full specialist analytical text; neither supplies a modern beer
    recipe.
- id: ATLAS-063
  title: Beer laws, civic gardens, public food and seasonal service
  state: implemented
  paths:
  - history/beerhouse-act-1830-debates.md
  - history/munich-beer-garden-1812.md
  - food/brotzeit-and-the-munich-beer-garden.md
  - calendar/munich-cellars-and-summer-service.md
  delivered_scope: Official debate and city narratives, with precise legal-text and historical-season limitations.
- id: ATLAS-064
  title: Korean and Chinese cereal starter ecology, process and sensory boundaries
  state: implemented
  paths:
  - microbiology/nuruk-42-sample-survey.md
  - microbiology/huangjiu-manual-and-mechanized-microbes.md
  - styles/huangjiu-chinese-cereal-wine.md
  - ingredients/wheat-qu-and-huangjiu.md
  delivered_scope: Distinguishes organism detection, fermentation time course, enzyme input, gene prediction and
    sensory inference.
- id: ATLAS-065
  title: Nubian ancient-grain genetics and archaeological interpretive limits
  state: implemented
  paths:
  - history/qasr-ibrim-barley-ancient-dna.md
  - ingredients/barley-row-type-and-brewing-assumptions.md
  delivered_scope: A primary ancient-DNA paper treated as crop history, not proof of beer at the site or a climate
    forecast.
- id: ATLAS-066
  title: Cross-domain revisions, original-source register, reproducible QA and reading trails
  state: implemented
  paths:
  - references/atlas-sources-1-9.md
  - editorial/research-update-1-9.md
  - editorial/validation-report-1-9.md
  - navigation/edition-1-9-reading-trails.md
  - tests/test_research_quality_v19.py
  delivered_scope: 18 existing-article source extensions, independent-review queue, source-use checks and site-preserving
    indexes.
- id: ATLAS-067
  title: Amazonian feasts and Andean chicha social research
  state: implemented
  paths:
  - culture/yaminahua-masateadas-and-kinship.md
  - culture/cusco-chicherias-maize-and-gendered-work.md
  - culture/north-peru-chicha-labor-and-scale.md
  - calendar/masateada-gatherings-without-fixed-dates.md
  delivered_scope: Three situated cases and a social-time page, with no invented universal calendar dates.
- id: ATLAS-068
  title: Wari archaeological interpretation and laboratory-history boundaries
  state: implemented
  paths:
  - history/cerro-baul-dregs-and-state-brewing.md
  - history/tape-fermentation-laboratory-model-1972.md
  delivered_scope: Two analyses distinguish excavation from experiment and laboratory model from living producer
    practice.
- id: ATLAS-069
  title: Ragi, tapai, khao mak and rice-ferment classification
  state: implemented
  paths:
  - ingredients/ragi-tapai.md
  - styles/tapai-ketan.md
  - styles/khao-mak-thai-fermented-rice.md
  - food/tapai-as-food-and-beverage.md
  delivered_scope: Named food and starter references, not new standardized beer styles or guaranteed safe preparations.
- id: ATLAS-070
  title: Alternative grains, enzymatic constraints and photo-chemistry
  state: implemented
  paths:
  - ingredients/buckwheat-and-extract-limits.md
  - ingredients/quinoa-and-amaranth-in-beer.md
  - processes/gluten-free-starch-conversion.md
  - ingredients/riboflavin-and-beer-light.md
  delivered_scope: Ingredient and process studies with explicit non-certified gluten-free and product-level photo-stability
    caveats.
- id: ATLAS-071
  title: Low-alcohol methods, sensory effects and microbial challenge research
  state: implemented
  paths:
  - microbiology/nonalcoholic-beer-pathogen-challenge.md
  - processes/thermal-and-membrane-dealcoholisation.md
  - sensory/worty-aroma-in-low-alcohol-beer.md
  - categories/nonalcoholic-beer-methods-and-safety.md
  delivered_scope: Selected technical studies and a safety research comparison, not process operating instructions.
- id: ATLAS-072
  title: Edition 1.10 provenance, 15 revisions, automation and reading paths
  state: implemented
  paths:
  - references/atlas-sources-1-10.md
  - editorial/research-update-1-10.md
  - editorial/validation-report-1-10.md
  - navigation/edition-1-10-reading-trails.md
  - tests/test_research_quality_v110.py
  delivered_scope: Cited revisions, 19-source register, reproducible checks and seven navigation trails; expert
    review remains uncompleted.
- id: ATLAS-073
  title: Document agave sap and Mexican pulque culture
  state: implemented
  paths:
  - styles/pulque.md
  - ingredients/agave-aguamiel.md
  - history/chalco-pulque-taxation-1778-1821.md
  delivered_scope: Named beverage, microbial processes and colonial archives are distinguished; neither rituals
    nor taxes become universal contemporary practice.
- id: ATLAS-074
  title: Deepen Brazilian Indigenous cassava fermentation without erasure
  state: implemented
  paths:
  - styles/cauim.md
  - styles/giroba.md
  - history/cauim-and-colonial-source-problems.md
  delivered_scope: Distinguish Guarani, Tupinambá and Tapirapé communities and different centuries, substrates
    and evidence genres.
- id: ATLAS-075
  title: Document Nigerian food-drinks and South African social use
  state: implemented
  paths:
  - styles/kunun-zaki.md
  - culture/umqombothi-and-shared-social-work.md
  - calendar/kunun-zaki-dry-season-association.md
  delivered_scope: A mild grain drink, social service and reported seasonal preference are not reduced to fixed
    beer styles or a festival date.
- id: ATLAS-076
  title: Reconcile organism detection, process and food-safety evidence
  state: implemented
  paths:
  - microbiology/pulque-five-stage-metagenomics.md
  - microbiology/tapirape-cauim-bacteria-and-yeast.md
  - categories/acidification-is-not-safety-certification.md
  delivered_scope: Five-stage sequencing, sampled cultures and health/safety inferences remain separate; no uncontrolled
    fermentation protocol.
- id: ATLAS-077
  title: Extend hoppy-aging, aldehyde and colloidal science
  state: implemented
  paths:
  - sensory/hoppy-ale-aroma-during-storage.md
  - sensory/haze-and-protein-polyphenol-bonds.md
  - processes/wort-aldehydes-before-packaging.md
  delivered_scope: Controlled and review evidence is scoped by sample, measured endpoint and storage system.
- id: ATLAS-078
  title: Revise canonical reference pages with cited context
  state: implemented
  paths:
  - styles/umqombothi.md
  - styles/burukutu.md
  - sensory/oxidative-aging.md
  delivered_scope: Eighteen existing subjects receive source-cited edition-1.11 sections; all canonical paths remain
    stable.
- id: ATLAS-079
  title: Publish 1.11 source ledger, navigation and checks
  state: implemented
  paths:
  - references/atlas-sources-1-11.md
  - navigation/edition-1-11-reading-trails.md
  - editorial/research-update-1-11.md
  - tests/test_research_quality_v111.py
  delivered_scope: Source-use backlinks, progress tracking, index, offline validation and site staging are reproducible;
    independent review remains unperformed.
- id: ATLAS-080
  title: Mahewu as a grain, process and microbe case
  state: implemented
  paths:
  - styles/mahewu.md
  - microbiology/mahewu-starter-cultures-2026.md
  - processes/mahewu-cooked-porridge-and-malt.md
  delivered_scope: Zimbabwean mahewu is described as a culturally situated cereal food-drink; 2019 community samples,
    2024 grain survey and 2026 model starters remain different studies.
- id: ATLAS-081
  title: Boza commerce, microbial ecology and Ottoman evidence
  state: implemented
  paths:
  - styles/boza.md
  - culture/istanbul-boza-sellers.md
  - microbiology/bulgarian-boza-pediococcus.md
  - history/ottoman-drink-restrictions-and-negotiation.md
  delivered_scope: One experimental boza, one Bulgarian microbial sample, Istanbul artisan service and a historical
    tavern-legal abstract remain distinct evidence.
- id: ATLAS-082
  title: Georgian Aludi, highland culture and seasons
  state: implemented
  paths:
  - styles/aludi-georgian-highland-beer.md
  - culture/georgian-highland-beer-and-blessings.md
  - calendar/aludi-summer-gatherings.md
  delivered_scope: Tourism-office documentation supports geographically scoped association, not a compulsory national
    recipe or UNESCO listing.
- id: ATLAS-083
  title: Paiwan cultural calendar versus unnamed sampled millet culture
  state: implemented
  paths:
  - styles/taiwan-indigenous-millet-ferment.md
  - culture/paiwan-millet-and-community-occasions.md
  - microbiology/taiwan-millet-starter-lab-study.md
  delivered_scope: Institutional Paiwan ceremony and a laboratory study without named originating community are
    expressly not equated, and no fixed Gregorian date is invented.
- id: ATLAS-084
  title: Japanese amazake and kvass as different starch systems
  state: implemented
  paths:
  - styles/amazake.md
  - processes/koji-amazake-saccharification.md
  - processes/kvass-bread-versus-malt.md
  delivered_scope: Different starter, substrate, food/drink and alcohol boundaries are documented; limited abstracts
    and producer affiliations remain identified.
- id: ATLAS-085
  title: Improve existing canonical profiles without duplicates
  state: implemented
  paths:
  - styles/boza.md
  - styles/kvass.md
  - styles/ikigage.md
  - ingredients/sorghum-and-millet.md
  delivered_scope: Eighteen existing subjects receive sourced edition-1.12 extensions; no existing profile is overwritten
    or falsely declared expert-reviewed.
- id: ATLAS-086
  title: Publish full provenance, subject index and automated checks
  state: implemented
  paths:
  - references/atlas-sources-1-12.md
  - editorial/research-update-1-12.md
  - editorial/validation-report-1-12.md
  - tests/test_research_quality_v112.py
  delivered_scope: Fifteen source records have actual access scopes and article backlinks, while the index, regression
    tests and staged website remain reproducible.
- id: ATLAS-087
  title: Jiahu 2004/2026 interdisciplinary reanalysis
  state: implemented
  paths:
  - styles/jiahu-fermented-beverage.md
  - history/jiahu-2004-to-2026-reinterpretation.md
  - processes/jiahu-starch-and-mould-inference.md
  delivered_scope: Separate chemical, starch and fungal evidence and chronological implications; do not invent
    an ancient recipe.
- id: ATLAS-088
  title: 'Benin and Ivorian sorghum beer: people and microbes'
  state: implemented
  paths:
  - culture/tchoukoutou-household-enterprises.md
  - microbiology/tchoukoutou-yeast-surveys-in-disagreement.md
  - microbiology/tchapalo-fermentation-versus-spoilage.md
  delivered_scope: Preserve local production context, study design and contradicting yeast reports without an all-Africa
    starter assumption.
- id: ATLAS-089
  title: Kenyan Muratina fermentation carrier and social context
  state: implemented
  paths:
  - styles/muratina.md
  - ingredients/kigelia-fruit-fibre.md
  - culture/muratina-and-agikuyu-marriage-negotiation.md
  - calendar/muratina-and-marriage-occasions.md
  delivered_scope: Distinguish a sugar fermentation carrier and a particular Sagana marital ethnography; no safety
    or universal ceremonial date claim.
- id: ATLAS-090
  title: Ugandan bushera and commercial opaque beer boundaries
  state: implemented
  paths:
  - styles/bushera.md
  - styles/chibuku.md
  - styles/malwa-ajon.md
  - categories/cereal-beer-versus-fermented-cereal-drink.md
  delivered_scope: Contrast household food-drinks, industrial brewing and secondary review terms without mislabelling
    alcohol status.
- id: ATLAS-091
  title: 'Beer flavor and environment: research methods over rankings'
  state: implemented
  paths:
  - sensory/beer-matrix-bound-aldehydes.md
  - environment/brewery-water-reuse-italy-portugal.md
  - environment/czech-brewery-scale-and-packaging-lca.md
  delivered_scope: Explain analytical matrix binding, pilot water reuse and life-cycle functional-unit limitations.
- id: ATLAS-092
  title: Cross-section navigation and canonical source-cited revisions
  state: implemented
  paths:
  - navigation/all-names.md
  - navigation/all-atlas-subjects.md
  - navigation/edition-1-13-reading-trails.md
  delivered_scope: Nineteen existing articles revised; names index expands to all 13 sections; historical profile
    paths preserved.
- id: ATLAS-093
  title: Release reproducibility, source review and regression checks
  state: implemented
  paths:
  - references/atlas-sources-1-13.md
  - editorial/research-update-1-13.md
  - editorial/validation-report-1-13.md
  - tests/test_research_quality_v113.py
  delivered_scope: Twenty-one source IDs remain linked to actual usages and explicit access limits; source hygiene
    is not human review.
- id: ATLAS-094
  title: Pilsen town brewery, 1842 historical evidence and exact date
  state: implemented
  paths:
  - culture/pilsen-burgher-brewing-rights.md
  - history/pilsen-1842-evidence-and-origin-myths.md
  - calendar/first-pilsen-batch-1842.md
  delivered_scope: Distinguish producer first-batch chronology from origin myths; archive access limits explicit
    and date cannot become a recurring festival.
- id: ATLAS-095
  title: Hop-growing work, drying infrastructure and seasonality
  state: implemented
  paths:
  - culture/kent-hop-farms-and-work.md
  - objects/english-hop-oast.md
  - processes/hop-drying-cooling-and-packing.md
  - calendar/english-hop-harvest-and-drying-season.md
  delivered_scope: Historic England full article used for regional material culture, with no fake universal annual
    harvest schedule.
- id: ATLAS-096
  title: Belgian heritage, Ethiopian tella and labor accounts
  state: implemented
  paths:
  - culture/belgian-beer-learning-networks.md
  - culture/tella-household-vessels-and-hospitality.md
  - history/american-beer-households-immigration-and-industry.md
  delivered_scope: Separate institutional heritage, household review synthesis and museum collection-level history
    from interviews and community endorsement.
- id: ATLAS-097
  title: Industrial yeast, draught systems and physical process
  state: implemented
  paths:
  - microbiology/industrial-lager-yeast-viability.md
  - processes/industrial-lager-aeration-and-filling.md
  - microbiology/draught-lines-as-a-different-microbial-habitat.md
  - objects/draught-lines-and-gas-balance.md
  delivered_scope: Technical study process parameters and BA guidance retain scope, do not establish brewing recipes
    or retail health claims.
- id: ATLAS-098
  title: Foam compounds, hop handling and sensory-service interpretation
  state: implemented
  paths:
  - ingredients/humulinones-and-aged-hops.md
  - sensory/protein-z-humulinone-foam.md
  - sensory/draught-service-vs-brewery-flavor.md
  delivered_scope: Distinguish isolated protein assay from flavor and population preference; preserve LTP1 differences.
- id: ATLAS-099
  title: Circular by-products and environmental model boundaries
  state: implemented
  paths:
  - environment/hot-trub-and-spent-yeast-valorization.md
  - environment/brewery-closed-loop-case-vs-general-rule.md
  - ingredients/surplus-brewers-yeast-as-material.md
  delivered_scope: Distinguish sample chemistry, technology reviews and industry modeled results from food safety
    and universal LCA.
- id: ATLAS-100
  title: Edition 1.14 integration, source provenance and maintenance tests
  state: implemented
  paths:
  - references/atlas-sources-1-14.md
  - editorial/research-update-1-14.md
  - editorial/validation-report-1-14.md
  - navigation/edition-1-14-reading-trails.md
  - tests/test_research_quality_v114.py
  delivered_scope: 29 new subjects, 18 source-backed original-article extensions, eight navigation trails, source-use
    backlinks, modern CI and regression checks.
- id: ATLAS-101
  title: Jurisdictional beer vocabulary, low-alcohol labels and an exact historical agency date
  state: implemented
  paths:
  - categories/jurisdictional-beer-names-vs-styles.md
  - categories/no-low-alcohol-descriptors-across-borders.md
  - history/us-beer-vs-malt-beverage-definitions.md
  - calendar/atf-nonalcoholic-marketing-circular-1991.md
  delivered_scope: Differentiate US tax/label law, BJCP judging categories and an archived 1991 marketing circular; English consultation proposals remain unverified as enacted law.
- id: ATLAS-102
  title: Carbon dioxide, glass surfaces, cleaning cues and model-bound sensory interpretation
  state: implemented
  paths:
  - ingredients/dissolved-carbon-dioxide-in-beer.md
  - processes/carbonation-from-bottle-to-glass.md
  - objects/beer-clean-glassware.md
  - objects/glass-surface-nucleation-sites.md
  - sensory/beer-bubbles-and-model-boundaries.md
  - sensory/foam-lacing-and-residues.md
  delivered_scope: Explain a studied lager CO2 nucleation model and service cues without inferring all-glass hygiene, sterility or universal sensory quality.
- id: ATLAS-103
  title: Water accounting, no-alcohol safety boundaries and canonical integration
  state: implemented
  paths:
  - environment/brewery-water-ratio-versus-water-footprint.md
  - environment/direct-and-indirect-water-in-brewing.md
  - microbiology/nolo-hurdles-are-not-label-rules.md
  - food/alcohol-descriptors-on-a-menu.md
  - categories/low-and-no-alcohol-beers.md
  delivered_scope: Separate site ratios, upstream supply-chain footprints, sample-specific microbial challenge and legal labels; 13 original articles extended with source-cited connections.
- id: ATLAS-104
  title: Edition 1.15 source provenance, navigation, reproducibility and review queue
  state: implemented
  paths:
  - references/atlas-sources-1-15.md
  - navigation/edition-1-15-reading-trails.md
  - navigation/all-names.md
  - navigation/all-atlas-subjects.md
  - editorial/research-update-1-15.md
  - editorial/validation-report-1-15.md
  - editorial/source-review-queue-1-15.md
  - tests/test_research_quality_v115.py
  delivered_scope: Nineteen new scoped subjects, thirteen sourced revisions, sixteen distinct works and seventy-six article-source placements, with independent review explicitly unperformed.

- id: ATLAS-105
  title: Standardized color, bitterness, malt and hop analytical interpretation
  state: implemented
  paths:
  - categories/beer-metrics-versus-beverage-identity.md
  - ingredients/hop-bitter-fractions-and-analytical-signals.md
  - processes/beer-colour-measurement.md
  - processes/bitterness-units-and-hop-chemistry.md
  - stories/two-beers-one-ibu.md
  delivered_scope: Distinguish analytical methods, sensory outcomes, predicted and measured quantities without treating IBUs or SRM as universal taste or cultural rankings.
- id: ATLAS-106
  title: Gravity, acidity, microbiological inference and sample-stage distinctions
  state: implemented
  paths:
  - objects/hydrometers-and-reading-conditions.md
  - processes/gravity-extract-and-estimated-alcohol.md
  - processes/ph-versus-titratable-acidity.md
  - microbiology/fermentation-timepoints-and-inference.md
  - categories/acidity-ph-ta-and-sourness.md
  delivered_scope: Clarify instrument stage, pH versus acidity, apparent extract versus alcohol and why process curves do not identify organisms or certify safety.
- id: ATLAS-107
  title: Richardson-era extract measurement, instruments and culturally situated authority
  state: implemented
  paths:
  - history/richardson-saccharometry-and-extract.md
  - objects/saccharometer-in-the-museum.md
  - culture/brewing-numbers-and-institutional-authority.md
  - history/from-lovibond-comparisons-to-srm.md
  delivered_scope: Use historical academic abstract, 1784 publication catalogue and circa-1830 museum object without inventing chronology, community consensus or an exact festival date.
- id: ATLAS-108
  title: Sensory discrimination, consumer preferences, appearance, environment and food
  state: implemented
  paths:
  - sensory/triangle-tests-for-beer.md
  - sensory/beer-colour-in-a-glass.md
  - categories/difference-tests-versus-quality-scores.md
  - food/difference-tests-do-not-rank-pairings.md
  - environment/analytical-consistency-is-not-a-life-cycle-footprint.md
  delivered_scope: Separate blinded detectability, colour expectation, quality scores, pairing preference and life-cycle functional units.
- id: ATLAS-109
  title: Edition 1.16 integration, source manifest consistency and reproducible release
  state: implemented
  paths:
  - references/atlas-source-manifest-1-16.json
  - references/atlas-sources-1-16.md
  - navigation/edition-1-16-reading-trails.md
  - editorial/research-update-1-16.md
  - editorial/validation-report-1-16.md
  - editorial/source-review-queue-1-16.md
  - tools/build_edition_sources.py
  - tests/test_research_quality_v116.py
  delivered_scope: Twenty-three new references, sixteen sourced canonical revisions, nineteen audited external works and ninety-four article-to-source placements with regression and continuous integration checks.

- id: ATLAS-110
  title: Barley pre-harvest physiology, malt enzymes and variable grain seasons
  state: implemented
  paths:
  - ingredients/preharvest-sprouted-barley.md
  - ingredients/malt-enzyme-readiness.md
  - processes/preharvest-sprouting-versus-malting.md
  - environment/barley-harvest-wet-weather-risks.md
  - calendar/barley-harvest-window-not-fixed.md
  delivered_scope: Separate crop dormancy, wet-weather sprouting, drought physiology and managed malting; no universal harvest event or agronomic operating plan.
- id: ATLAS-111
  title: Field-pathogen, modified mycotoxin, gushing and grain-to-beer evidence
  state: implemented
  paths:
  - microbiology/fusarium-strain-effects-in-barley.md
  - microbiology/plant-conjugated-don.md
  - microbiology/fungal-dna-versus-mycotoxin-measurement.md
  - ingredients/don-glucoside-as-modified-mycotoxin.md
  - processes/fusarium-malt-to-beer-transformation.md
  - sensory/gushing-hydrophobins-and-carbonation.md
  delivered_scope: Keep controlled inoculation, crop disease, DNA detection, toxin quantification and foam mechanisms distinct; no safe-use protocols.
- id: ATLAS-112
  title: Scottish Bere landrace continuity and Ethiopian regional malt-barley markets
  state: implemented
  paths:
  - ingredients/bere-six-row-barley.md
  - history/bere-introduction-date-uncertain.md
  - culture/orkney-bere-knowledge-and-revival.md
  - culture/arsi-malt-barley-farm-contracts.md
  - culture/estie-malt-barley-cooperatives.md
  - culture/malt-barley-and-household-food-security.md
  delivered_scope: Preserve local histories, research access and separate contract-study populations without claiming ancient recipe descent or universal household outcomes.
- id: ATLAS-113
  title: Malt sensory, storage objects, byproduct safety and resource comparisons
  state: implemented
  paths:
  - sensory/malt-hot-steep-experiments.md
  - objects/grain-stores-and-sample-provenance.md
  - food/spent-grain-and-food-safety-boundaries.md
  - food/bere-grain-food-and-brewing-boundaries.md
  - environment/bere-barley-crop-resilience.md
  delivered_scope: Distinguish malt-panel studies, current EU product categories and material resource evidence from finished-beer preference, food safety and life-cycle rankings.
- id: ATLAS-114
  title: Edition 1.17 source manifest, cross-reference integration, navigation and tests
  state: implemented
  paths:
  - references/atlas-source-manifest-1-17.json
  - references/atlas-sources-1-17.md
  - editorial/research-update-1-17.md
  - editorial/validation-report-1-17.md
  - editorial/source-review-queue-1-17.md
  - navigation/edition-1-17-reading-trails.md
  - navigation/all-atlas-subjects.md
  - navigation/all-names.md
  - tests/test_research_quality_v117.py
  delivered_scope: 28 new source-scoped articles and 18 cited revisions across all reference sections; 19 works, 95 actual article-source uses, nine trails and CI source/inventory checks.

- id: ATLAS-115
  title: Packaging format, beer aging and oxygen-phase distinctions
  state: implemented
  paths:
  - categories/packaging-material-is-not-shelf-life.md
  - processes/total-package-oxygen-has-two-phases.md
  - processes/cold-chain-experiment-is-not-a-universal-expiry.md
  - sensory/aldehyde-aging-begins-before-the-package.md
  - sensory/unpasteurized-ale-storage-case-2025.md
  delivered_scope: Keep 2025 beer-storage experiment, two-phase package oxygen and multiple aging mechanisms distinct from universal style expiry or safe handling instructions.
- id: ATLAS-116
  title: Comparative beer packaging LCAs, reuse systems and EU packaging rules
  state: implemented
  paths:
  - categories/why-packaging-lca-rankings-disagree.md
  - environment/seven-breweries-versus-pet-keg-case.md
  - environment/returnable-bottles-and-system-losses.md
  - environment/eu-packaging-reuse-law-scope.md
  - culture/deposit-and-return-as-beer-institutions.md
  delivered_scope: Compare seven-microbrewery and PET-keg LCAs with transport, loss and reuse assumptions; distinguish August 2026 application from later EU obligations.
- id: ATLAS-117
  title: Photochemical beer lightstruck science, refermentation and pressure-risk context
  state: implemented
  paths:
  - ingredients/riboflavin-hop-acids-light-reaction.md
  - sensory/lightstruck-vs-oxidative-staling.md
  - processes/pulsed-light-has-a-flavor-tradeoff.md
  - microbiology/lactobacillus-pulsed-light-case.md
  - microbiology/package-refermentation-pressure-vs-quality.md
  delivered_scope: Separate riboflavin-hop chemistry, measured lightstruck thiol, microbial experimental endpoints and manufacturer package-pressure safety.
- id: ATLAS-118
  title: Dated crown-cork history, handled-can object and food-contact materials
  state: implemented
  paths:
  - history/crown-cork-patent-vs-invention-myth.md
  - history/beer-cans-and-home-distribution.md
  - objects/crown-cork-and-sealing-liner.md
  - objects/baltimore-handled-beer-can.md
  - objects/metal-can-linings-and-food-contact.md
  - calendar/crown-cork-patent-1892.md
  - calendar/eu-ppwr-application-2026.md
  - food/can-liners-and-food-contact-evidence.md
  delivered_scope: Preserve exact archival days as historical, not recurring festivities; distinguish museum object, liner regulations, contact tests, community history and sensory evidence.
- id: ATLAS-119
  title: Edition 1.18 research, provenance, integration, navigation and CI
  state: implemented
  paths:
  - references/atlas-source-manifest-1-18.json
  - references/atlas-sources-1-18.md
  - editorial/research-update-1-18.md
  - editorial/validation-report-1-18.md
  - editorial/source-review-queue-1-18.md
  - navigation/edition-1-18-reading-trails.md
  - navigation/all-atlas-subjects.md
  - navigation/all-names.md
  - tests/test_research_quality_v118.py
  delivered_scope: 27 new subjects, 15 canonical sourced revisions, 22 external works and 101 actual article-source placements across thirteen sections with current navigation and negative-case regression tests.

---

# World Beer Atlas expansion specification

**Specification 1.13 · research deliverables tracked through edition 1.18 · 28 October 2026.** This is the scope and acceptance contract for extending World Beer Wiki beyond style descriptions. “Atlas” describes the connected reference model, not a compulsory project rename or a claim of complete geographical coverage.

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

## 12. Edition 1.6 — source-first geography, laboratory scope and explanation

The fifth research installment adds 30 bounded subject articles to the 372-article baseline, resulting in **402 subject articles**, including **170 named beer/tradition and related-ferment profiles**. It also adds research notes to 22 existing subjects. ATLAS-039 to ATLAS-045 define the finite work accomplished in this installment; they do not assert completion of any region or topic. The publication and its evidence limits are documented in [research update 1.6](research-update-1-6.md) and [source supplement](../references/atlas-sources-1-6.md).

### Evidence interpretation requirements

The five-community, 15-sample Southern Assam study is **not** a comprehensive account of Indigenous rice-beverage practices. Urugwa evidence currently comes from a secondary review, and the Ugandan Tonto chemistry study sampled two districts; retain those different access levels. Finnish producer accounts support named apprenticeship and celebrations, not a fixed date or the origin of the national tradition. Early-diverging kveik genomic lineages are not dates of beer invention. Measured fermentation organisms, predicted pathways, household culture and active causation are distinct claims. Peruvian and Chilean chicha sources retain their own communities and histories; similarities do not prove descent.

The edition's [quality checker](../tools/research_quality.py) adds reproducible tests for new-page source metadata, cited footnotes, local reading links and review status. A passing report means that the articles meet *local editorial hygiene*, not that external sources were exhaustively read or that communities approved the writing. The next priority is independent local-language and practitioner review, full original-text verification of abstract-only studies, and clear correction handling.

### Accessibility of research

The atlas remains readable as Markdown without network access or runtime dependencies. Automated exports and website navigation are optional derived layers. Historic reports retain the counts they actually measured; the new release records its own numbers instead of rewriting older editions.

## 13. Edition 1.7 — excavation context, work, mixed starters and modeled systems

This installment contributes **26** research articles and **16** sourced extensions, for **428** total subject articles. ATLAS-046 through ATLAS-053 record bounded deliverables. Each new article has claim-linked citations, actual access notes and related reading. Community/specialist review **ATLAS-012 remains planned**, not certified or automatically completed.

### Cross-domain acceptance gates

A fieldwork producer’s weekly service dates must not be projected into a present-day business opening schedule. A heritage inscription must not be treated as a scientific species inventory or a historical ownership grant. Microbial isolates must not become mandatory starter “recipes”; an organism detected or a marker gene identified need not demonstrate active spoilage in another system. Excavation-season descriptions and estimated production capacity must keep their separate labels. LCA comparisons require their functional unit, route assumptions and recovery scenario.

The [edition 1.7 source supplement](../references/atlas-sources-1-7.md), [research report](research-update-1-7.md), [review queue](source-review-queue-1-7.md), and [reading trails](../navigation/edition-1-7-reading-trails.md) document what was delivered and what has not been checked. The existing research quality audit should be usable for both edition 1.6 and 1.7 so new work does not erase earlier release coverage.

## 14. Edition 1.8 — living fermentation knowledge and analytical scope

This installment adds **29** bounded articles and **14** substantive, source-cited revisions. ATLAS-054 through ATLAS-059 cover Shawi cassava beverage field research, northeastern Tanzanian mbege, Ethiopian thick cereal ferments and Himalayan finger-millet ecology, beer foam/staling, hop aroma chemistry and reproducible evidence QA. Each new article has a scoped `source_checked_on`, explicit access limits and internal reading links.

### New acceptance boundaries

- Compare community-partnered photographs with commercial producer samples without declaring either one the universal masato process. Coliform counts **do not** certify drinking-water or fermented-beverage safety.
- Distinguish the named **nyalu** and **mso** preparations in mbege from one-pot brewing; keep its studied msesewe bark additive as *observation*, not a safety or botanical-collection recommendation.
- Treat thick fermented cereals such as borde and shamita as locally named food-drinks; keep sample stages, culture detection and actual function separate. A journal website posting date must not overwrite a print issue date.
- Attribute foam results to studied protein fractions, and hop/yeast aroma results to actual strains, chemical precursors, samples and time courses. No one cultivar, organism, or sensory word diagnoses an entire production process.
- The edition quality checker must recognize **1.6, 1.7 and 1.8** without losing historical reports; its source-use checks cannot establish external truth. The [review queue](source-review-queue-1-8.md) remains open.

**Editorial limits remain unchanged:** ATLAS-012 specialist and community review is still **planned**. Licensed media (ATLAS-013) and optional interactive/live discovery (ATLAS-014) remain deferred. Implemented means the named deliverable exists and passes structural checks, not that worldwide research is complete.

## 15. Edition 1.9 — archives, community vessels, rice starter ecology and civic law

This installment adds **31** source-scoped subject articles and **18** sourced revisions to existing pages. ATLAS-060 through ATLAS-066 represent finite, checkable files, not a claim of worldwide completeness. It preserves every existing canonical beer-profile path. The [1.9 source register](../references/atlas-sources-1-9.md), [research update](research-update-1-9.md) and [review queue](source-review-queue-1-9.md) identify what was and was not accessible.

### Specific evidence rules

- A Vietnam national heritage listing must not be silently called UNESCO heritage; Ma and S’Tieng accounts cannot be treated as interchangeable. Botanical starter materials are documented as reported, not proposed as foraging or ingestion guidance.
- Bhutanese *ara* can involve distillation and is included as a *related cultural tradition*, not a standardized grain beer. The phab isolate study is bacterial and does not establish the complete living starter.
- A cuneiform ration tablet is evidence for accounting and named products, not the taste or brewing recipe of Sumerian beer; the Hymn to Ninkasi requires translation and genre cautions.
- A parliamentary debate is a record of speakers’ claims, not proof of health benefits or downstream economic outcomes. City tourism accounts of an 1812 Munich decree are not independent inspection of the legal text.
- The comparison of manual and mechanized Huangjiu is specific to studied batches and measurements, not a universal flavor ranking. A survey of 42 nuruk starter samples cannot be equated with a makgeolli fermentation time course.
- Ancient Qasr Ibrim barley DNA is archaeological crop evidence, not direct evidence of brewing or a quantitative climate-change forecast.

The local **source-use audit for 1.9** must check every new source’s metadata and explanatory citation, and retain previous 1.6–1.8 checks. Calendar entries about ceremonies may not invent public dates. **ATLAS-012** independent community and specialist review remains planned, while licensed media and live discovery remain deferred.

## 15. Edition 1.10 — testimony, microbial evidence and modern process constraints

This eighth bounded research installment adds 27 articles and makes 15 substantive source-cited revisions, defined by ATLAS-067 through ATLAS-072. The original 488 subject articles remain accessible at their canonical paths. Implementation records files and tests, **not** proof of globally complete traditions or community approval.

### Sources and interpretation safeguards

- The Yaminahua masateada article is abstract-limited and is not a fixed annual holiday. Cusco chichería evidence and north-coast ethnoarchaeology describe distinct places and questions.
- The Wari Moquegua household-versus-specialist brewing hypothesis comes from a publisher abstract. An experimental fermentation trace is not an exact ancient recipe.
- Indonesian ragi and Thai lookpang demonstrate that mixed starters and locally named rice foods cannot be reduced to one yeast species or a universal beer style; the 1972 isolate model is not a community survey.
- A 2022 grist study with **40% alternative grain and 60% barley malt** must never be called a gluten-free beer result or interpreted as coeliac safety certification.
- Laboratory inoculation of low-alcohol products provides specific microbial-risk evidence, not retail contamination claims or a home food-preservation protocol. Photochemical mechanism does not diagnose every 'skunky' bottle or define a safe exposure threshold.

The new [source register](../references/atlas-sources-1-10.md), [release validation](validation-report-1-10.md) and [review queue](source-review-queue-1-10.md) preserve the access limitations. ATLAS-012 independent community/specialist review is **still planned**; media and live-calendar features remain deferred.


## 16. Edition 1.11 — identified voices, local ferments and chemical evidence

Edition 1.11 adds **34 source-scoped subjects and 18 sourced revisions**, recorded in ATLAS-073 through ATLAS-079. Existing pages and their canonical paths remain stable. This ledger says the named deliverable exists; it does not claim global coverage or independent expert approval. [The 1.11 research update](research-update-1-11.md) and [source supplement](../references/atlas-sources-1-11.md) identify the exact sources, access limitations and article backlinks.

**Method boundaries:** Colonial clerical and tax accounts are mediated records, not community-endorsed rituals; a sampled Brazilian preparation does not define another community’s recipe. Microbial sequencing and isolated culture counts do not certify safety, health benefits or metabolic function. Staling chemistry is sample-, time- and system-dependent. The [review queue](source-review-queue-1-11.md) retains the unperformed full-text, local-language and community checks. ATLAS-012 remains *planned*; media and live atlas features remain *deferred*.


## 17. Edition 1.12 — living cereal drinks, starter roles, seasonal knowledge and source scope

**30 new source-scoped articles and 18 sourced revisions** are tracked in ATLAS-080–086. Implementation means the named files and tests are present; it does not imply worldwide coverage, local consent, an exact historic recipe or microbial safety. See the [research report](research-update-1-12.md), [source access register](../references/atlas-sources-1-12.md), and [independent-review queue](source-review-queue-1-12.md).

**Research guardrails:** The experimental 1997 Turkish boza batch is not a standard 0.79% rule. The 2026 Zimbabwe mahewu starter study is not a field food-safety certification. The 2013 Taiwanese millet study does not identify its sampled group and must not be attributed to Paiwan ritual; governmental descriptions of a Five-Year Ritual do not supply a constant Gregorian date. A Georgian tourism account is not UNESCO inscription or independent highland-community review. Koji sweetening, sake-lees use, household rye kvass and laboratory barley kvass are separate transformations. Current and historical editions remain draft; ATLAS-012 review still awaits actual expert and community participation.

## 18. Edition 1.13 — archaeological re-evaluation, fermentation carriers and methods

This edition contributes **35** source-scoped articles and **19** sourced revisions. ATLAS-087 through ATLAS-093 track only their finite file and tooling deliverables. They neither certify all regional cultures nor override the still-open ATLAS-012 independent review. Historic releases retain their own validation figures.

### Special interpretation requirements

- The 2004 Jiahu chemical analysis and 2026 microfossil reassessment are two author interpretations of different evidence classes, not two exact prehistoric recipes. No lineage from Jiahu to living rice-ferment traditions is asserted.
- A 2007 Benin household study and multiple 2011–2025 yeast isolate surveys differ in location, timing, denominator and technique. An isolate percentage is not the proportion of all live fermenters in every batch, and social income figures are historical.
- Kenyan Muratina fruit fibres are described as yeast carriers in a 2003 university thesis; this does not justify an ingestion or isolation protocol. The 2026 Agikuyu Muslim Sagana ethnography is a bounded cultural account, not a universal marriage schedule.
- Ugandan bushera and malwa are related cereal food-drinks under differently sourced names, and industrial Chibuku is a commercial opaque beer. Review labels do not guarantee absolute alcohol content or consumer safety.
- Chemical aldehyde binding and antioxidant assays are not health benefits; pilot water-reclamation performance and environmental LCA results have different functional units and cannot certify every brewery.

[Edition 1.13 research update](research-update-1-13.md) · [Annotated 1.13 sources](../references/atlas-sources-1-13.md) · [Independent review queue](source-review-queue-1-13.md).

## 19. Edition 1.14 — fields, institutions, fermentation, serving and environmental evidence

**29 new bounded subject articles and 18 sourced revisions** extend the atlas to 643 subjects. ATLAS-094–100 track the finite delivered work, not a worldwide completeness score. The 1842 Pilsen batch is one producer-documented historical event, not the invention of bottom fermentation. English hop-oast evidence concerns regional agricultural handling and surviving buildings, not a sensory chemistry experiment or an annual event date. Belgian UNESCO heritage recognition is not a unified style or recipe; Smithsonian collection summaries do not substitute for reading oral interviews. Ethiopian tella vessel-smoking accounts are secondary synthesis, not validated sanitization protocols.

The 2025 industrial yeast experiment tests particular production-scale factor ranges; draught technical guidance describes maintenance and dispense, not sampled incidents at every bar. Humulinone/protein-Z assays and LTP1 heating experiments have different proteins, model systems and endpoints. Environmental comparisons retain functional units and distinguish a chemical screening, technology review and case-specific large brewery LCA. Every research article remains **draft**. [Edition report](research-update-1-14.md), [source uses](../references/atlas-sources-1-14.md), [review queue](source-review-queue-1-14.md), and [eight reading trails](../navigation/edition-1-14-reading-trails.md) document scope and open work. **ATLAS-012 independent review has not occurred**; media rights and interactive live event discovery remain deferred.

## 20. Edition 1.15 — legal terms, glass physics and resource-accounting boundaries

**19 new source-scoped subjects and 13 cited revisions** extend the atlas to 662 articles, tracked by ATLAS-101–104. This release compares TTB federal legal classes with independent BJCP judging terminology, archives a 20 August 1991 ATF marketing circular as an exact non-recurring historical event, and treats England's 2023 policy consultation as a proposal rather than present law. It separates package CO2 and a one-lager bubble model from glassware service cues, and distinguishes site water-use ratios from water-footprint accounting and product safety evidence.

The [release report](research-update-1-15.md), [16-work source register](../references/atlas-sources-1-15.md), [open review queue](source-review-queue-1-15.md), [seven trails](../navigation/edition-1-15-reading-trails.md) and [validation record](validation-report-1-15.md) describe the actual deliverables. **ATLAS-012 remains planned**, with external cultural, regulatory, brewing, historical and microbiological review not performed. Media and live event discovery remain deferred.

## 21. Edition 1.16 — evidence for what beer measurements can mean

**23 new articles and 16 source-backed revisions** extend the atlas to 685 subjects across 13 sections. ATLAS-105–109 track only finite research and tooling deliverables. These are not five new universal claims about brewing cultures or a count of officially defined beer styles. Modern ASBC colour/bitterness/pH/TA method summaries, indexed laboratory protocols and academic chemistry reviews are unlike a tasting-panel preference or a historical community description. A published IBU result is not a sensory score; a laboratory pH does not certify product safety; an SRM sample is not the entire glass appearance.

The 1784 Richardson source is a bibliographic year, the museum object is dated approximately 1825–1835, and the full historical article was not accessed. Neither record becomes a fabricated annual calendar event or local endorsement. ISO 4120:2021's public abstract, confirmed current in 2026, explains a forced-choice method but is not the complete paywalled normative procedure. Source limits and unperformed independent review remain explicit in the [source manifest](../references/atlas-sources-1-16.md), [review queue](source-review-queue-1-16.md), [research update](research-update-1-16.md) and [eight reading trails](../navigation/edition-1-16-reading-trails.md). ATLAS-012 is **planned**; media and live discovery remain **deferred**.

## 22. Edition 1.17 — agriculture, grain history, fungal evidence and research scope

**28 new research references and 18 substantive canonical revisions** extend the atlas to 713 subjects across 13 sections. ATLAS-110–114 track finite file-based deliverables rather than universal beer coverage. The new studies distinguish pre-harvest sprouting from managed malting, field-pathogen detection from named fermentation microbes, measured mycotoxin forms from consumer safety, and package gushing from glass/CO2 effects. The 2026 inoculated-barley experiment is a controlled study, not a procedure for rendering suspect grain safe.

Separate open farm surveys from Arsi, Oromia and Estie describe different contract models and household outcomes; they are not an all-Ethiopia causal estimate. Bere barley's regional cultivation and uncertain ancient introduction are not evidence of a fixed prehistoric beer recipe. EU contaminant rules require product-specific application and a dated consolidated text; a cereal threshold is not automatically a finished beer or spent-grain food limit. The [19-work source register](../references/atlas-sources-1-17.md), [research update](research-update-1-17.md), [nine trails](../navigation/edition-1-17-reading-trails.md) and [independent-review queue](source-review-queue-1-17.md) record what was actually consulted. **ATLAS-012 specialist/community review is still planned**, while licensed media and live event services remain deferred.

## 23. Edition 1.18 — packaging as physical, legal and social evidence

**27 source-scoped new subjects and 15 existing-page sourced revisions** extend the atlas to 740 subjects. ATLAS-115–119 track the finite content and tooling deliverables, not completeness of worldwide brewing knowledge. The two named 2022 and 2024 beer-packaging LCAs study different distributions and comparison formats; neither proves a universal best keg. The EU's 12 August 2026 packaging-law application is a historic legal date, not the completion of later reuse targets or an annual festival. The 1892 crown-cork patent date is exact archival evidence, not the invention of all bottled beer.

Technical work distinguishes liquid and headspace oxygen, multiple aldehyde pathways, specific light-triggered riboflavin chemistry and yeast effects in one unpasteurized-ale experiment. Packaging overpressure is a serious manufacturer safety matter; this wiki does not provide consumer interventions or production recipes. A Smithsonian handled-can object and EU bisphenol food-contact rules answer different questions; neither proves the taste or material composition of every beer can. See the [research update](research-update-1-18.md), [22-work annotated bibliography](../references/atlas-sources-1-18.md), [nine reading trails](../navigation/edition-1-18-reading-trails.md), and [independent-review queue](source-review-queue-1-18.md). **ATLAS-012 remains planned**, with licensed media and live calendar tools deferred.
