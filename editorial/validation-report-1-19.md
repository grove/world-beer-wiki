---
type: "Validation Report"
title: "Edition 1.19 validation commands and evidence limits"
description: "Reproducible metadata, provenance, relationship, inventory and site checks."
tags: [wiki-documentation, edition-1.19, validation]
status: draft
generated:
  by: world-beer-wiki/1.19
  at: "2026-10-28T14:00:00Z"
sources:
- id: atlas-spec
  resource: /editorial/atlas-specification.md
  title: World Beer Atlas expansion specification
---

# Research edition 1.19 — validation and limitations

The checks below validate **local Markdown integrity and documented provenance**, not the truth of every source's experimental claims, physical engineering design, food-grade gas purity, sanitation or historical interpretation.

## Reproduce from the repository root

```bash
python -m pip install PyYAML==6.0.2
python tools/validate_wiki.py --json
python tools/atlas.py check --json
python tools/research_quality.py --edition 1.19 --json
python tools/build_edition_sources.py --edition 1.19 --check --json
python tools/check_inventory.py --json
python tools/build_subject_index.py --check
python tools/build_names_index.py --check
python -m unittest discover -s tests -v
python tools/build_site.py
```

The expected research counts are **26 new subject articles, 21 canonical revisions, 21 external works and 109 distinct article-source uses**. The current wiki inventory is **766 subject articles across 13 reference sections**. The new seasonal ice-harvest calendar entry has no invented fixed annual day. The [21-work manifest](https://github.com/grove/world-beer-wiki/blob/research/world-beer-atlas-1-19/references/atlas-source-manifest-1-19.json) and [generated reference register](../references/atlas-sources-1-19.md) must agree exactly on source IDs, titles, authors, URLs, access notes and linked articles.

## What remains separate from passing checks

An industrial heat-pump scenario is not verified savings at every brewery. A COD reduction in a reactor does not prove drinkable or legally reusable water. Recycling fermentation CO₂ does not necessarily permanently store it or confer whole-product net zero. Museum records are not personal testimony from all past brewers, and a company sustainability resource is not independently audited onsite data. [Independent review remains open](source-review-queue-1-19.md). Consult GitHub Actions on the pull request for the actual CI status, rather than inferring it from this documentation.

[Research](research-update-1-19.md) · [Reading trails](../navigation/edition-1-19-reading-trails.md) · [Home](../index.md).
