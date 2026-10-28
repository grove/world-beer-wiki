---
type: "Validation Report"
title: "Edition 1.17 — validation instructions and limits"
description: "Reproducible source, inventory and site checks, without claiming independent factual review."
tags: [wiki-documentation, edition-1.17, validation]
status: draft
generated:
  by: world-beer-wiki/1.17
  at: "2026-10-28T13:00:00Z"
sources:
- id: atlas-spec
  resource: /editorial/atlas-specification.md
  title: World Beer Atlas expansion specification
---

# Research edition 1.17 validation and evidence limits

The following checks validate Markdown structure, local links, evidence metadata, edition source consistency, navigation indexes and regression fixtures. **Passing these checks cannot certify the historical, agronomic, microbiological, regulatory, dietary or food-safety accuracy of every claim.** No external inspection or local farmer/community approval is claimed.

## Repeatable commands

```bash
python -m pip install PyYAML==6.0.2
python tools/validate_wiki.py --json
python tools/atlas.py check --json
python tools/research_quality.py --edition 1.17 --json
python tools/build_edition_sources.py --edition 1.17 --check --json
python tools/check_inventory.py --json
python tools/build_subject_index.py --check
python tools/build_names_index.py --check
python -m unittest discover -s tests -v
python tools/build_site.py
```

The [machine-readable source manifest](https://github.com/grove/world-beer-wiki/blob/research/world-beer-atlas-1-17/references/atlas-source-manifest-1-17.json) lists 19 researched source works; the [generated bibliography](../references/atlas-sources-1-17.md) maps 95 actual article-source references. The expected release comprises **28 new subject articles, 18 source-backed revisions, and 713 current subjects across 13 sections**. A repeated source on two pages is not a second independent study. Earlier edition numbers remain historical rather than being rewritten.

## Specific uncertainties

The 2026 controlled grain-inoculation result cannot prove a safe process or be generalized to every commercial beer. The EU consolidated food-contaminant regulation needs applicable product-category and legal review; a cereal value is not universally a finished-beer limit. Ethiopian contracts, Bere heritage and climatic crop traits are locally situated source populations, not universal lineages or economic guarantees. Local tests and hosted GitHub Actions check implementation, while a [review queue](source-review-queue-1-17.md) retains unperformed external specialist review.

[Research report](research-update-1-17.md) · [Reading trails](../navigation/edition-1-17-reading-trails.md) · [Home](../index.md).
