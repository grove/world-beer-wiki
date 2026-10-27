---
type: Validation Report
title: World Beer Atlas research edition 1.5 validation report
description: Reproducible validation and evidence boundaries for the edition 1.5 research expansion.
tags: [editorial, validation, research-edition-1.5]
status: draft
generated:
  by: world-beer-wiki/1.5
  at: '2026-10-27T23:15:00Z'
sources:
- id: atlas-spec
  resource: /editorial/atlas-specification.md
  title: World Beer Atlas expansion specification
- id: atlas-source-supplement
  resource: /references/atlas-sources-1-5.md
  title: Research edition 1.5 annotated source supplement
---

# Research edition 1.5: validation and limitations

Validation checks the **shape, navigability and stated provenance** of this research corpus, not the historical, archaeological, anthropological or microbiological truth of every claim. This edition adds source-bounded comparisons and keeps expert, community and original-language review outstanding. Source access differs by item: see the [annotated 1.5 supplement](../references/atlas-sources-1-5.md) and the [independent review queue](source-review-queue-1-5.md).

## Reproduce offline

From the repository root, with Python 3.9+ and PyYAML installed:

```bash
python tools/validate_wiki.py --json
python tools/atlas.py check --json
python -m unittest discover -s tests -v
python tools/build_subject_index.py --check
python tools/atlas.py catalog > catalog.json
python tools/atlas.py timeline > timeline.json
python tools/atlas.py progress > progress.json
python tools/atlas.py source-audit > audit.json
python tools/build_site.py
```

`git diff --cached --check` checks whitespace after staging. Export reproducibility can be checked by executing each export twice and byte-comparing outputs; exports do not fetch sources, conduct new research or consult event schedules.

## Results

| Validation target | Verified result |
|---|---:|
| Markdown files reachable from the root | 421 / 421 |
| Subject articles | 372 |
| Original beer/tradition profile paths preserved | 166 |
| Local Markdown link occurrences resolved | 5,873 |
| Structured comparison and qualified relations | 1,065 |
| Claim-linked footnote references | 1,427 |
| Calendar/event/season records | 12 |
| Stable implementation work items | 38 |
| Python regression tests | 38 passed |
| Unresolved structural errors | 0 |

The counts above are intentionally tied to this edition and should be regenerated if the PR changes. Site staging is not itself evidence that the full HTML site has been built; its GitHub workflow is reported separately in the PR. The generated [complete subject index](../navigation/all-atlas-subjects.md) can be validated with `--check` rather than maintained by hand.

## Evidence, ethics and reproducibility limits

A metadata footnote proves that a source record exists and the cited link resolves locally; it does **not** verify external URL permanence, the reliability of the cited interpretation, physical safety, linguistic accuracy, or community agreement. Inaccessible book chapters, repository metadata and indexed journal excerpts are explicitly scoped rather than treated as full texts. Corroboration is evaluated by independent evidence, not raw source-link counts. No restricted rituals, unlicensed photographs, unpublished interview recordings or full protected guidelines were bundled.

The [progress tracker](atlas-progress.md) reports implemented work at the scope of this edition; it is not a rating of scientific certainty, editorial independence or cultural representativeness.

[Specification](atlas-specification.md) · [Research update](research-update-1-5.md) · [Home](../index.md)
