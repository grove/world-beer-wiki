# 100 Things Beer Teaches Us About History, Science & Culture

**A world of discovery through fermentation**

A free e-book for curious general readers, including people who do not drink beer. Exactly 100 short lessons use fermentation to explore archaeology, technology, labor, evolution, chemistry, perception, cooperation, identity, and environmental systems.

The organization is fixed: **34 history lessons, 33 science lessons, and 33 culture lessons**. The collection is an original narrative synthesis, not a concatenation of wiki articles or a style directory.

## Reading and production files

- `100-things-beer-teaches-us.md` is the **single canonical manuscript**. Edit prose, section order, references, and publication metadata here.
- `100-things-beer-teaches-us.epub` is the reflowable EPUB 3 edition, with a cover, reader navigation, linked contents, internal cross-references, and external source links.
- `100-things-beer-teaches-us.pdf` is the 6 × 9 inch reading and printing edition, with embedded fonts, a clickable contents list, PDF bookmarks, and linked source notes.
- `assets/cover.png` is the original cover artwork.
- `publishing-materials.md` contains the subtitle, approximately 150-word back-cover description, approximately 50-word promotional description, and cover production record.
- `research/source-to-chapter.json` and `.csv` map every lesson to its discovery, wider-world question, wiki sources, underlying publications, evidence limits, and overlap controls.
- `research/*-research.json` record the section researchers' actual source access and editorial decisions. These distinguish new access from inherited wiki claims.
- `research/validation.json`, `research/epubcheck.txt`, and `editorial-checklist.md` record production and editorial checks, including unresolved issues.
- `LICENSE-APACHE-2.0.txt` preserves the source corpus license. The same terms appear in the manuscript's appendix and reading editions.

The source bundle includes all assets needed for an offline rebuild after dependencies are installed. Research caches, downloaded publications, temporary renders, and credentials are excluded.

## Research foundation and status

The source repository is [World Beer Wiki](https://github.com/grove/world-beer-wiki), with a [searchable public site](https://grove.github.io/world-beer-wiki/). This edition uses research edition **1.19**, pinned to commit `3b985c19a9dcccef8d334be54b5405e42093e812` of 28 October 2026.

The frozen corpus contains 766 subject articles in thirteen domains. The book research inspected the repository directly, including article metadata and relationships, reading trails, editorial methodology, source registers, review queues, and the catalog, timeline, source-audit, and progress exports of `tools/atlas.py`.

Underlying primary research, historical documents, institutional records, and public cultural accounts were consulted where accessible. A wiki draft was never treated as independent verification of itself. Some relevant publications remained accessible only as abstracts, records, or excerpts; those limits stay visible in the notes and research files.

The manuscript has received AI-assisted research, structural editing, factual-claim review, cultural-framing review, style editing, and production checks. **It has not received independent scholarly peer review or community approval.** The checklist describes the remaining work without representing it as completed.

## Why this directory is separate

All book material lives under `.publications/100-things-beer/`. The leading dot keeps the existing wiki scanners and automatic site staging from interpreting a 100-lesson manuscript and production documents as new canonical subject articles. No wiki article, root navigation, methodology file, validator, or site builder is changed by this book contribution.

This is a deliberate publishing boundary, not a change to the canonical wiki. To publish the book as a website download, a maintainer can separately choose where to expose the finished files. The requested pull request proposes the complete book without silently changing the wiki's public navigation.

## Rebuild the editions

Requirements: Python 3.10 or later, Pandoc 3.x on `PATH`, and the Python packages pinned in `requirements.txt`. The reference build used Pandoc 3.1.3. Source Serif 4 fonts and their SIL Open Font License are bundled; no proprietary fonts are required.

From this directory:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/build.py
python3 scripts/validate.py
```

To build one format:

```bash
python3 scripts/build.py --format epub
python3 scripts/build.py --format pdf
```

The builder reads only the canonical Markdown and bundled assets. It uses Pandoc for EPUB and the document's syntax tree, and ReportLab for the PDF layout. PDF creation is invariant and EPUB ZIP timestamps are fixed to the edition date for reproducible bytes. Build scripts do not fetch research sources or regenerate the cover.

Run the official EPUB validator separately. The reference production check used [EPUBCheck 5.4.0](https://github.com/w3c/epubcheck/releases/tag/v5.4.0):

```bash
mkdir -p .build/epubcheck-tmp
java -Djava.io.tmpdir=.build/epubcheck-tmp -jar /path/to/epubcheck-5.4.0/epubcheck.jar 100-things-beer-teaches-us.epub
```

For visual PDF inspection, use Poppler or another renderer, then inspect the actual page images. Text extraction and a successful build alone cannot establish good typography:

```bash
pdftoppm -r 100 -png 100-things-beer-teaches-us.pdf .build/page
```

The validation script checks lesson counts, numbering, references, source-map consistency, internal destinations, EPUB resources, PDF lesson labels and link annotations, complete source-license fidelity in all reading editions, and output hashes. It does **not** fact-check publications, establish cultural authority, or guarantee an external website will remain available.

Create a complete distribution archive with:

```bash
python3 scripts/package.py
```

## Updating the research

Edit the manuscript first, then update the matching row of the source map and the access record. If an underlying paper becomes available in full, record the actual new access and revise only claims supported by it. Preserve disagreement, study populations, experimental conditions, and the distinction between observation and interpretation.

Do not silently replace the frozen source commit when changing a sentence. A new book edition can select a new snapshot explicitly. Within a full wiki checkout, its source inventory can be reproduced with:

```bash
python tools/atlas.py catalog > atlas-catalog.json
python tools/atlas.py timeline > atlas-timeline.json
python tools/atlas.py source-audit > atlas-source-audit.json
python tools/atlas.py progress > atlas-progress.json
```

Run those commands from the repository root, not this publishing directory. Earlier source snapshots and their access limitations should remain traceable.

## Availability, rights, and attribution

The commissioning request authorizes free download and reading. World Beer Wiki and its contributors are credited, its Apache License 2.0 is preserved, and its source commit is recorded. No upstream `NOTICE` file was present at the pinned snapshot. This newly written adaptation changes the selection, narrative, organization, and editorial apparatus; it does not reproduce whole wiki articles or external publications.

Referenced third-party material retains its own rights. No research figures, cultural photographs, brewery logos, or substantial quoted passages are bundled. The cover is a newly generated conceptual illustration, not evidence or an archival reconstruction. The font files are distributed with their original license.

**No new Creative Commons license is asserted.** CC BY 4.0 is a recommendation for the book's new copyrightable material, subject to authorization by its rights holder. A publisher adopting that recommendation should update the rights statement in the canonical manuscript and rebuild both editions. Existing Apache-covered material and third-party rights must remain separately identified.

## Corrections

Use the [wiki issue tracker](https://github.com/grove/world-beer-wiki/issues) or a pull request. Supply the lesson number or wiki path, the disputed wording, a specific source locator, and the proposed correction. A source-to-chapter map and a list of unresolved questions are included so later editors can improve the work without reconstructing the research from scratch.
