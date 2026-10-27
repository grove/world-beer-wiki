---
type: Validation Report
title: Research edition 1.3 validation and reproduction
status: draft
description: Checked outputs, reproducibility commands and limits of structural validation.
tags: [wiki-documentation, validation, edition-1.3]
generated:
  by: world-beer-wiki/1.3
  at: '2026-10-27T22:50:00Z'
sources:
- id: atlas-spec
  resource: /editorial/atlas-specification.md
  title: World Beer Atlas expansion specification
---

# Validation report: edition 1.3

Run both validators and the negative-case regression suite from the repository root:

```bash
python tools/validate_wiki.py --json
python tools/atlas.py check --json
python -m unittest discover -s tests -v
python tools/atlas.py catalog > /tmp/atlas-catalog.json
python tools/atlas.py progress > /tmp/atlas-progress.json
python tools/atlas.py timeline > /tmp/atlas-timeline.json
python tools/build_site.py
```

The tools are offline and do not probe external source URLs. They verify frontmatter structure, claims-to-citation reference integrity, local Markdown links and anchors, comparison target links, source consistency, subject directory membership and root reachability. The atlas checker also verifies calendar metadata, evidence-qualified typed relationships and implementation work-item paths.

## Edition 1.3 observed results

Numbers below are populated from the actual test runs before PR review and should be compared with the CI workflow. The results do **not** assert independent scientific, historical, cultural, botanical or microbial-safety review.

<!--VALIDATION_RESULT_START-->

All checks completed locally with **zero structural errors** on the validated source tree:

| Check | Observed result |
|---|---:|
| Markdown files reachable from the wiki root | **334 / 334** |
| Subject articles across eleven layers | **295** |
| Canonical beer/tradition profiles retained | **166** |
| Resolved local Markdown link occurrences | **4,674** |
| Valid structured relations and linked targets | **1,014** |
| Evidence-bearing qualified relation records | **40** |
| Footnote references matched to definitions/source IDs | **1,136** |
| Distinct source IDs in metadata (includes internal sources) | **397** |
| Calendar records | **9** |
| Explicit dated event editions | **1** (the source-described 2026 Oktoberfest edition) |
| Work ledger items | **23** (20 implemented first-installment or extension deliverables; one planned independent review; two deferred) |
| Negative-case and integration regression tests | **30 passed** |
| Searchable-site Markdown pages staged | **334** |
| Structural errors | **0** |

Validation commands: `python tools/validate_wiki.py --json`, `python tools/atlas.py check --json`, `python -m unittest discover -s tests -v`, `python tools/atlas.py catalog`, `python tools/atlas.py progress`, `python tools/atlas.py timeline`, `python tools/build_site.py`, `git diff --check`. The last step detects whitespace problems in tracked changes; new files are staged for the final Git check. The catalog, progress and timeline exporters produce stable key order for equivalent source inputs. Both old and new historical-report pages remain in the corpus. Exact counts are for this checked branch, not the earlier editions.

The website staging command succeeded and included all 334 Markdown pages. A full HTML compilation requires MkDocs and must be validated by the repository's hosted website workflow; local staging alone is not an HTML-build claim.

<!--VALIDATION_RESULT_END-->

## Known scope limits

Historical papers consulted through abstracts are not presented as full archival analysis. A research source may support a particular location, period, organism or method rather than a whole category. The website compiler stages Markdown and public assets; successful staging is not the same as proving an HTML build unless an HTML build has actually passed. The data exports never infer an upcoming festival date.

[Specification](atlas-specification.md) · [Progress](atlas-progress.md) · [Research update](research-update-1-3.md)
