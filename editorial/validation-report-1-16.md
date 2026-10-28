---
type: "Validation Report"
title: "Edition 1.16 — validation checklist and explicit limits"
description: "Reproducible local and hosted integrity checks; factual verification is out of scope."
tags: [wiki-documentation, edition-1.16, validation]
status: draft
generated:
  by: world-beer-wiki/1.16
  at: "2026-10-28T13:00:00Z"
sources:
- id: atlas-spec
  resource: /editorial/atlas-specification.md
  title: World Beer Atlas expansion specification
---

# Edition 1.16 validation and research limits

The wiki's **offline** checks validate Markdown structure, local relationships, source metadata, citations, page counts and generated navigation. They do **not** verify truth by visiting every publisher, inspecting an unpublished method, replicating an experiment, evaluating a live beverage or obtaining community approval.

## Reproduce from repository root

```bash
python -m pip install PyYAML==6.0.2
python tools/validate_wiki.py --json
python tools/atlas.py check --json
python tools/research_quality.py --edition 1.16 --json
python tools/build_edition_sources.py --edition 1.16 --check --json
python tools/check_inventory.py --json
python tools/build_subject_index.py --check
python tools/build_names_index.py --check
python -m unittest discover -s tests -q
python tools/build_site.py
```

Expected edition manifest totals: **23 new articles, 16 revised articles, 19 external works and 94 distinct article-source placements**. The current directory should show **685 subject articles across 13 sections**. Source count is not independent study count. Previous release counts remain dated snapshots.

The new generator checks that each edition source ID, URL, title, author, type and actual access limit match the committed JSON manifest and that the generated Markdown register contains the article backlinks. Negative regression tests check that inconsistent source reuse is rejected. GitHub Actions runs the older editions' checks too.

## Verification status and limitations

Passing an offline validator does **not** imply that a copyrighted standard has been read in full, that a museum photograph can be reused, that an IBU predicts bitterness perception, or that an acidification measurement establishes food safety. Hosted GitHub Actions and the searchable site build are separate checks; see the PR's Checks tab for actual run outcomes rather than assuming they passed.

[Research update](research-update-1-16.md) · [Source-review queue](source-review-queue-1-16.md) · [Sources](../references/atlas-sources-1-16.md) · [Home](../index.md).
