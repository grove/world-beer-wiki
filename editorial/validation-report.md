---
type: Validation Report
title: Bundle validation report
description: Deterministic checks of the Markdown bundle, citations, metadata, and navigation.
tags:
- wiki-documentation
- validation
status: draft
generated:
  by: world-beer-wiki/1.0
  at: '2026-10-27T19:13:06Z'
sources:
- id: corpus
  resource: /styles/index.md
  title: Profile directory and linked files
- id: format
  resource: /editorial/format.md
  title: OKF 0.2 mapping
- id: register
  resource: /references/source-register.md
  title: Source register
---

# Bundle validation report

**Edition 1.0 · 27 October 2026**

This report records mechanical checks of the downloadable bundle. It does **not** certify historical accuracy, replace independent expert review, or elevate the articles' trust tier.

## Checked successfully

| Check | Result |
|---|---:|
| UTF-8 Markdown files | 171 |
| Canonical profile files | 153 |
| Ordinary concept files with valid YAML and a non-empty type | 165 |
| Internal Markdown link occurrences resolved | 2275 |
| Comparison relations resolved | 495 |
| Footnote citations matched to definitions and source identifiers | 622 |
| Files reachable from the root index | 171 |
| Broken internal links | 0 |
| Unresolved footnote references | 0 |
| Duplicate concept identifiers | 0 |

The checks also confirm the root version declaration, reserved index and log conventions, timezone-bearing generation timestamps, lifecycle values, nonempty source references, internal source paths, and source metadata on every profile. Each profile's comparison targets exist and are also linked in its body. All files in the archive are Markdown; the ZIP was reopened and checked for CRC errors after writing.

## Scope and limits

External references were consulted during research, but this report is not a live-health test of every external URL or a promise of continued availability. Source titles and links are not evidence that every historical interpretation is settled. The [source register](../references/source-register.md) records what was used; individual articles record access and scope limitations.

The corpus remains an AI-generated, source-checked research edition with `status: draft`. No `verified` metadata is asserted. Formatting validation is deliberately not represented as human verification of the contents.

## References

Results refer to the [profile corpus](../styles/index.md) and [OKF mapping](format.md). Read the [methodology](methodology.md) and [coverage limitations](coverage-and-gaps.md) alongside these results.
