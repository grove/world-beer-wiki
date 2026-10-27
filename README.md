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
| [Ingredients and cultures](ingredients/index.md) | 17 | Materials, processing forms, enzymes and fermentation organisms. |
| [Category guides](categories/index.md) | 13 | Explanations and comparisons across families and classification axes. |

The [navigation directory](navigation/index.md) offers names, regions, families, ingredients and historical scope. The [editorial directory](editorial/index.md) explains evidence handling and known gaps. The [reference directory](references/index.md) links to the [source register](references/source-register.md), which traces every external source record used by these three article sections to the pages citing it.

## Reading an article

Start with the definition, then its ingredients or process, comparisons and evidence note. A modern judging category, a community practice, an ingredient and an archaeological inference support different kinds of statements. The article's `type` and `scope` preserve that distinction. Footnote identifiers match its source metadata.

Use [How beer categories work](categories/beer-classification.md) before assuming that a family name is a genealogy. Ingredient pages describe roles, not mandatory recipes for every linked beer. Comparison links invite further reading; they do not establish descent.

## Using or extending the corpus

The [OKF 0.2 mapping](editorial/format.md) documents concept and metadata conventions. [Reading with an LLM](editorial/reading-with-an-llm.md) explains retrieval and evidence boundaries. [Coverage and gaps](editorial/coverage-and-gaps.md) states what this edition does and does not cover, and the [1.1 research note](editorial/research-update-1-1.md) describes the expansion.

Preserve canonical paths when revising an article. Cite specific factual claims, record actual source access, update the relevant directory and navigation, and keep the source register synchronized. Do not mark a document human-reviewed merely because an LLM expanded it.

## Optional maintenance check

The only supporting code is [tools/validate_wiki.py](tools/validate_wiki.py). It performs offline checks of metadata, citation identifiers, local file and anchor links, relations, directory membership and reachability. It does not validate historical truth or probe external sites.

With Python 3.9 or later and PyYAML installed, run from the repository root:

```bash
python tools/validate_wiki.py
python tools/validate_wiki.py --json
```

If needed, install its single dependency with `python -m pip install PyYAML`. No dependency is needed to read the wiki. The [validation report](editorial/validation-report.md) records the actual checks for this edition.

## Sources and rights

The prose is newly written synthesis. Referenced publications, guideline texts, community knowledge, names and external sites retain their own rights and conditions. Citations do not grant rights to republish those sources; copies of source publications are not bundled. Guideline editions and producer claims remain identified in the relevant articles.
