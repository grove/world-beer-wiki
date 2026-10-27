---
type: Format Reference
title: OKF 0.2 mapping
description: Editorial documentation and navigation for the World Beer Wiki.
tags:
- wiki-documentation
status: draft
generated:
  by: world-beer-wiki/1.0
  at: '2026-10-27T19:09:58Z'
sources:
- id: okf-spec
  resource: https://raw.githubusercontent.com/GoogleCloudPlatform/open-knowledge-format/main/SPEC.md
  title: Open Knowledge Format specification, version 0.2
  author: team:googlecloudplatform-open-knowledge-format-contributors
  source_kind: official-format-specification
  access_scope: version 0.2 specification consulted 2026-10-27
  author_label: GoogleCloudPlatform/open-knowledge-format contributors
---

# OKF 0.2 mapping

This bundle targets Open Knowledge Format version 0.2. Ordinary concept files have YAML frontmatter with a non-empty `type`. A concept identifier is its bundle-relative path without `.md`. The root `index.md` declares `okf_version: "0.2"`; other index files and `log.md` do not carry concept frontmatter.[^okf-spec]

Provenance uses `sources`, with footnotes matching source identifiers. `generated` records the producer and an offset-bearing timestamp. `status: draft` records the document lifecycle. No `verified` field is asserted, so consumers should not infer independent verification.[^okf-spec]

## Corpus-specific extensions

This corpus adds `aliases`, `regions`, optional `countries`, `tradition_status`, `scope`, `evidence_basis`, `source_checked_on`, `review_note`, and comparison `relations`. Source metadata also records `source_kind`, `access_scope`, and the bibliographical display name `author_label`. These extensions preserve context; they do not change the standard's required fields.

## Reference

[^okf-spec]: [Open Knowledge Format specification, version 0.2](https://raw.githubusercontent.com/GoogleCloudPlatform/open-knowledge-format/main/SPEC.md), consulted 27 October 2026.

[Validation report](validation-report.md) · [Reading guide](../README.md)
