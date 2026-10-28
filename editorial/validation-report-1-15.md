---
type: Validation Report
title: Edition 1.15 validation and limits
description: Reproducible checks for 1.15, with pending CI status and independent-review boundaries.
tags: [wiki-documentation, edition-1.15, validation]
status: draft
generated:
  by: world-beer-wiki/1.15
  at: '2026-10-28T11:35:00Z'
sources:
- id: atlas-spec
  resource: /editorial/atlas-specification.md
  title: World Beer Atlas expansion specification
---

# Edition 1.15 validation and reproducibility

This report specifies what the PR checks are designed to verify. **At authoring time the full CI suite has not yet been confirmed passing**, and no live website or source URL check is claimed. Structural reproducibility is not independent cultural, historical, scientific, legal, food-safety or regulatory certification.

## Reproduction from the repository root

Install Python 3.11+ and PyYAML, then run:

```bash
python tools/validate_wiki.py --json
python tools/atlas.py check --json
python tools/atlas.py source-audit
python tools/research_quality.py --edition 1.15 --json
python tools/check_inventory.py --json
python tools/build_subject_index.py --check
python tools/build_names_index.py --check
python -m unittest discover -s tests -v
python tools/build_site.py
```

The GitHub Actions validation workflow also runs the earlier edition research checks, confirms provenance and generates reproducible output files. Edition 1.15 expects **19 new subjects, 13 source-cited revisions, 16 named external works, 76 article-source uses, and 662 subjects in 13 sections**. A source-use count is not a study count.

## Checks versus evidence

Offline checks cover local links, markdown metadata, source/footnote identifiers, source access description, generated directory membership, release counting and historical event semantics. They do **not** test current US or English legal compliance, official product labeling, beverage microbiological safety, consumer preferences, or environmental impact equivalence. A documented service procedure is not a venue hygiene inspection, and a modeled bubble count is not a sensory standard.

The [independent review queue](source-review-queue-1-15.md) remains open. Once CI checks actually run, their recorded run status should be attached to the pull request rather than inferred from this text.

[Research update](research-update-1-15.md) · [Annotated source register](../references/atlas-sources-1-15.md) · [Home](../index.md).
