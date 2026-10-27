---
type: Reading Guide
title: 'World Beer Wiki: reading and maintenance guide'
description: 'World Beer Wiki: reading and maintenance guide'
tags:
- wiki-documentation
status: draft
generated:
  by: world-beer-wiki/1.1
  at: '2026-10-27T19:45:17Z'
sources:
- id: corpus
  resource: /styles/index.md
  title: Profile directory and linked article metadata
- id: ingredient-directory
  resource: /ingredients/index.md
  title: Ingredient reference directory
- id: category-directory
  resource: /categories/index.md
  title: Category guide directory
---

# Read this first

World Beer Wiki is a plain Markdown knowledge base. Open [index.md](index.md), browse on GitHub, or load the directory into an LLM retrieval system. Keep relative paths intact. Reading requires no application, database or build step.

## Browse the searchable website

The optional [World Beer Wiki website](https://grove.github.io/world-beer-wiki/) renders these same Markdown articles with full-text search, responsive navigation, dark mode and direct article links. New pages are discovered automatically during the site build; the original wiki remains readable without dependencies.

For a local preview, install Python 3.12 or later and run:

```bash
python -m pip install -r requirements-site.txt
python tools/build_site.py
python -m mkdocs serve -f .build/mkdocs.yml
```

The GitHub Actions workflow builds and validates pull requests, then publishes merges to `main` using GitHub Pages. In repository **Settings → Pages**, select **GitHub Actions** as the publishing source once. The live site will be available at the link above after the first successful deployment.

## What is included

| Section | Entries | Purpose |
|---|---:|---|
| [Beer and tradition profiles](styles/index.md) | 166 | Named styles, local traditions, specialty categories, historical accounts and related ferments. |
| [Ingredients and cultures](ingredients/index.md) | 38 | Materials, processing forms, enzymes and fermentation organisms. |
| [Category guides](categories/index.md) | 21 | Explanations and comparisons across families and classification axes. |
| [Culture](culture/index.md) | 26 | Situated institutions, work, exchange and knowledge. |
| [Calendar](calendar/index.md) | 12 | Seasons and edition-specific events. |
| [Microbiology](microbiology/index.md) | 24 | Organisms, cultures and ecological evidence. |
| [Processes](processes/index.md) | 21 | Transformations and production comparisons. |
| [Objects and service](objects/index.md) | 9 | Equipment and ways of presenting drinks. |
| [Sensory](sensory/index.md) | 13 | Flavor reasoning and evidence boundaries. |
| [Stories](stories/index.md) | 13 | Evidence-based narrative reading routes. |
| [History and archaeology](history/index.md) | 18 | Historical policies, industrialization and ancient material evidence. |
| [Environment](environment/index.md) | 7 | Climate, cultivation, energy, water and materials. |
| [Beer with food](food/index.md) | 4 | Evidence-based pairing context and consumer study designs. |

That is **372 subject articles**, not 240 standardized beer styles. The [atlas specification](editorial/atlas-specification.md), [progress ledger](editorial/atlas-progress.md) and [1.5 research update](editorial/research-update-1-5.md) document delivered and remaining scope.

The [navigation directory](navigation/index.md) offers names, regions, families, ingredients and historical scope. The [editorial directory](editorial/index.md) explains evidence handling and known gaps. The [reference directory](references/index.md) links to the [source register](references/source-register.md), which documents the 1.1 baseline. The [atlas source supplement](references/atlas-sources.md) traces the new layers and explicitly identifies inherited corpus evidence.

## Reading an article

Start with the definition, then its ingredients or process, comparisons and evidence note. A modern judging category, a community practice, an ingredient and an archaeological inference support different kinds of statements. The article's `type` and `scope` preserve that distinction. Footnote identifiers match its source metadata.

Use [How beer categories work](categories/beer-classification.md) before assuming that a family name is a genealogy. Ingredient pages describe roles, not mandatory recipes for every linked beer. Comparison links invite further reading; they do not establish descent.

## Using or extending the corpus

The [OKF 0.2 mapping](editorial/format.md) documents concept and metadata conventions. [Reading with an LLM](editorial/reading-with-an-llm.md) explains retrieval and evidence boundaries. [Coverage and gaps](editorial/coverage-and-gaps.md) states what this edition does and does not cover, and the [1.1 research note](editorial/research-update-1-1.md) describes the expansion.

Preserve canonical paths when revising an article. Cite specific factual claims, record actual source access, update the relevant directory and navigation, and keep the source register synchronized. Do not mark a document human-reviewed merely because an LLM expanded it.

## Optional maintenance check

The [base validator](tools/validate_wiki.py) checks the Markdown corpus. The [atlas utility](tools/atlas.py) adds section, evidence-edge, calendar and implementation-ledger checks, plus deterministic JSON exports. It performs offline checks of metadata, citation identifiers, local file and anchor links, relations, directory membership and reachability. It does not validate historical truth or probe external sites.

With Python 3.9 or later and PyYAML installed, run from the repository root:

```bash
python tools/validate_wiki.py
python tools/validate_wiki.py --json
python tools/atlas.py check --json
python -m unittest discover -s tests -v
python tools/atlas.py catalog > atlas-catalog.json
python tools/atlas.py progress > atlas-progress.json
python tools/atlas.py timeline > atlas-timeline.json
python tools/atlas.py source-audit > atlas-source-audit.json
python tools/build_subject_index.py --check
```

If needed, install its single dependency with `python -m pip install PyYAML`. No dependency is needed to read the wiki. The [1.5 validation report](editorial/validation-report-1-5.md) records checks actually run; earlier reports are retained as historical records. The validation workflow attaches a portable tracked-file snapshot and JSON results to pull-request runs.

## Sources and rights

The prose is newly written synthesis. Referenced publications, guideline texts, community knowledge, names and external sites retain their own rights and conditions. Citations do not grant rights to republish those sources; copies of source publications are not bundled. Guideline editions and producer claims remain identified in the relevant articles.

## New research in edition 1.4

Browse [environment](environment/index.md), [food and pairing](food/index.md) or the [research update](editorial/research-update-1-4.md). The [source supplement](references/atlas-sources-1-4.md) distinguishes fieldwork, primary experiments, institutional history and abstracts. The [scope ledger](editorial/atlas-progress.md) remains authoritative.

## Research edition 1.5

Use the [complete subject index](navigation/all-atlas-subjects.md) to find every entry across all sections, or follow [curated investigation routes](navigation/atlas.md). The [1.5 source supplement](references/atlas-sources-1-5.md) records access limitations; the [research review queue](editorial/source-review-queue-1-5.md) shows work that remains unverified. Regenerate the index with `python tools/build_subject_index.py`; continuous integration checks that committed navigation is current.
