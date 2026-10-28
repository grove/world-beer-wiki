---
type: "Validation Report"
title: "Edition 1.18 — reproducible integrity checks and scope"
description: "Expected inventory, source counts, validation commands and limitations."
tags: [wiki-documentation, edition-1.18, validation]
status: draft
generated:
  by: world-beer-wiki/1.18
  at: "2026-10-28T14:00:00Z"
sources:
- id: atlas-spec
  resource: /editorial/atlas-specification.md
  title: World Beer Atlas expansion specification
---

# Research edition 1.18 — validation and evidence limits

These checks evaluate **offline structure and provenance**, not the truth of every experimental or historical claim, legality of a specific package, operational pressure safety, hygiene of a venue or a consumer health outcome.

## Reproduce from the repository root

```bash
python -m pip install PyYAML==6.0.2
python tools/validate_wiki.py --json
python tools/atlas.py check --json
python tools/research_quality.py --edition 1.18 --json
python tools/build_edition_sources.py --edition 1.18 --check --json
python tools/check_inventory.py --json
python tools/build_subject_index.py --check
python tools/build_names_index.py --check
python -m unittest discover -s tests -v
python tools/build_site.py
```

Expected research scope is **27 newly sourced subjects, 15 canonical revisions, 22 external works and 101 article-to-source uses**. The current inventory should be **740 subjects in 13 sections**. The two historical calendar records must preserve exact single dates without invented annual observances. Source access may mean a full open paper, a publisher abstract, a partially indexed experiment, an official guidance landing page, a primary legal text or museum object metadata. These are different levels of confidence.

The source-manifest auditor verifies that reused edition IDs have consistent title, URL, credit, type and actual access scope, and that each source has real article backlinks. The CI workflow runs earlier editions' checks too, without rewriting their historical figures.

## What passing does not mean

No source citation proves that a specific beer was safe from excess pressure, free of regulated food-contact substances, compliant with the EU packaging laws, or the lowest-impact package. The method abstract for total package oxygen does not establish universal filling setpoints. A patent day does not establish the invention of all bottled beer, and one museum object is not a complete consumer history. The [independent-review queue](source-review-queue-1-18.md) lists unresolved full-text, technical, legal and cultural tasks. The PR Checks tab reports actual hosted run results; this report does not predeclare success.

[Research update](research-update-1-18.md) · [Sources](../references/atlas-sources-1-18.md) · [Home](../index.md).
