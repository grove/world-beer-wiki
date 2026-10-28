# The Beer Detective

*Uncovering the Myths, Mysteries and Untold Stories of Beer*

A free, evidence-aware narrative nonfiction book grounded in the World Beer Wiki.

This directory contains the publishing project. The prose is newly written; the underlying wiki and its source references form a research map, **not an independent certificate of factual accuracy**.

## Contents and publishing status

- `the-beer-detective.md` — canonical manuscript with endnotes and reading list.
- `sources-and-chapters.md` — chapter-by-chapter source and claim register.
- `editorial-review.md` — corrections, limitations, and review status.
- `covers/` — original editable SVG cover concepts.
- `scripts/` — reproducible EPUB/PDF build and validation instructions.
- `publishing-copy.md` — back-cover copy and project description.

This submission is undergoing internal editorial and layout validation. Independent professional, scientific, and community-specific human review **has not occurred** and must not be inferred from editorial notes.

## Research baseline and attribution

Research map: [World Beer Wiki](https://github.com/grove/world-beer-wiki), baseline main commit `3b985c19a9dcccef8d334be54b5405e42093e812` (28 October 2026).

The parent wiki is Apache-2.0 licensed. Third-party sources retain their own rights. New original book prose and artwork are offered for free reading, but **no separate Creative Commons license is claimed without authorization from the rights holder**.

## Build

```bash
python3 -m pip install -r requirements.txt
python3 scripts/build.py
python3 scripts/validate.py
```

Publishing dependencies and format limitations are documented alongside the scripts. Do not describe unreleased editions as professionally fact-checked or independently endorsed.
