---
type: Validation Report
title: Bundle integrity and validation report
description: Deterministic checks of the Markdown bundle, citations, metadata, and navigation.
tags:
- wiki-documentation
- validation
status: draft
generated:
  by: world-beer-wiki/1.1
  at: '2026-10-27T19:46:40Z'
sources:
- id: corpus
  resource: /styles/index.md
  title: Profile directory and linked article metadata
- id: format
  resource: /editorial/format.md
  title: OKF 0.2 mapping
- id: register
  resource: /references/source-register.md
  title: Source register
- id: wiki-validator
  resource: /tools/validate_wiki.py
  title: Optional offline wiki validator
---

# Bundle integrity and validation report

**Edition 1.1 · 27 October 2026**

The optional [offline validator](../tools/validate_wiki.py) checked the complete repository after the research expansion and navigation updates. These are structural checks, not a certification of historical truth or human review.

## Reproduce the check

With Python 3.9 or later and PyYAML installed, run from the repository root:

```bash
python tools/validate_wiki.py
python tools/validate_wiki.py --json
```

The checker makes no network requests and does not change files. It exits with a nonzero status if it finds an error. The wiki can be read without running it.

## Final measured results

| Check | Result |
|---|---:|
| UTF-8 Markdown files | 218 |
| Ordinary concept files | 210 |
| Beer and tradition profiles | 166 |
| Ingredient references | 17 |
| Category guides | 13 |
| Internal Markdown link occurrences resolved | 3521 |
| Structured comparison relations resolved and linked in the body | 705 |
| Footnote citation occurrences matched to definitions and source IDs | 872 |
| Source identifiers across subject and editorial concepts | 296 |
| Markdown files reachable from the root index | 218 |
| Validation errors | 0 |

The [subject-source register](../references/source-register.md) separately counts **260 external source records** used by profiles, ingredients and category guides. The larger source-identifier total above also includes internal document references used by navigation and editorial pages; it is not a count of independent publications.

## What passed

YAML parsed with duplicate keys rejected. Ordinary concepts have nonempty type, title and status fields and timezone-bearing generation timestamps. The root declares OKF 0.2; reserved directory indexes and the release log follow the bundle's frontmatter convention.

Local Markdown file and anchor targets, internal source paths and relation targets resolve. Structured relation targets are also linked in article bodies. Referenced footnotes have definitions and source metadata; definitions are not duplicated or left unused. Repeated source identifiers retain consistent resource URLs and titles. All subject articles appear in their corresponding directory index, and every Markdown file is reachable through links from the root.

The checker handles the Markdown link and heading forms used here, including balanced URL parentheses, reference links, Unicode heading anchors and fenced code blocks. Focused temporary fixtures exercised its positive and negative paths. It is a utility for this corpus, not a full Markdown renderer or complete OKF schema validator.

## Research review and limits

Independent AI editorial passes checked selected primary-source claims, including modern judging boundaries, regional process descriptions, microbial roles and archaeological interpretation. Resulting corrections are summarized in the [research update](research-update-1-1.md). All articles retain draft review status; no human historian, brewer, scientist or community approval is asserted.

External sources were consulted during research. This report does not claim a live health check of every existing URL, full-text access to every publication or continued future availability. Abstract-only, indexed and partial access remain identified in source metadata. See [methodology](methodology.md), [coverage](coverage-and-gaps.md) and [format conventions](format.md).
