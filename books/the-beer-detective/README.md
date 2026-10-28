# The Beer Detective

## Uncovering the Myths, Mysteries and Untold Stories of Beer

**A World Beer Wiki book project · Free review edition · October 2026**

Twenty-four narrative investigations follow beer through archaeology,
chemistry, living traditions and the stories attached to familiar drinks.
The book begins with a prehistoric mortar and ends with the crops and practical
knowledge that future brewing will need. Its four parts are **What Survives**,
**Inside the Glass**, **A Living Trade** and **The Unfinished Case**.

This is a complete AI-assisted review edition. Internal editorial and
cross-reader passes are documented; independent human editorial, specialist
and community review has not occurred. No human author, reviewer, interview or
field visit is invented. Specific evidence restrictions appear in the notes.

## Read and download

| File | Purpose |
|---|---|
| [the-beer-detective.md](the-beer-detective.md) | Single authoritative release manuscript, including front matter, all chapters, closing sections, numbered endnotes and selected further reading |
| [the-beer-detective.epub](dist/the-beer-detective.epub) | Reflowable EPUB with final cover, embedded fonts, navigation, source links and individual return links from notes |
| [the-beer-detective.pdf](dist/the-beer-detective.pdf) | 6 × 9 inch reading edition, with embedded type, running heads, folios, clickable contents and PDF bookmarks |
| [editorial-review.md](editorial-review.md) | Actual editing passes, corrections, remaining limitations and questions for independent reviewers |
| [sources-and-chapters.md](sources-and-chapters.md) | Every chapter's wiki routes, independent sources, access status and claims requiring care |
| [publishing-materials.md](publishing-materials.md) | 176-word back-cover description, 50-word promotional description and truthful project biography |

The [manuscript manifest](research/manuscript-manifest.json) gives the exact
narrative word count, chapter counts and note/claim totals. Its word count
excludes references, headings, acknowledgments and the methodology note. The
[build manifest](research/build-manifest.json) records PDF pagination, artifact
hashes and the exact master used by each format.

## Cover and interior

The [three concepts](design/cover-concepts.png) explore distinct original vector
compositions. The selected orange, cream and dark-blue cover uses a small
schematic tablet and dominant typography. The marks are a graphic abstraction,
not a historical transcription. [Cover direction](design/cover-direction.md)
explains the selection.

Final assets: [editable SVG](design/cover.svg), [1800 × 2700 PNG](design/cover.png)
and [6 × 9 inch vector front-cover PDF](design/cover-print.pdf). The three
individual concept SVGs remain editable. A paperback wrap is not supplied:
spine width and bleed depend on the printer's stock and specification.

The interior uses EB Garamond for reading text and Bricolage Grotesque for
headings. The PDF has 10.7-point body type on 14.1-point leading, restrained
chapter openings and chapter-local notes. The EPUB keeps its text reflowable
and lets readers change size and reading preferences.

## Research foundation

Research baseline: World Beer Wiki edition 1.19, commit
[`3b985c19a9dcccef8d334be54b5405e42093e812`](https://github.com/grove/world-beer-wiki/commit/3b985c19a9dcccef8d334be54b5405e42093e812).
Source checks closed on 28 October 2026.

The wiki supplied routes and evidence metadata, not automatic verification.
Original papers, historical texts, museum records and practitioner accounts
were checked where accessible. Notes distinguish full text, relevant passages,
abstracts, indexed excerpts and secondary descriptions. The
[claim register](research/claim-register.json) records the evidence and limits
for consequential claims. Part-level selection files and review records are in
research/; the [architecture](research/architecture.md) preserves the initial
selection decisions, including subjects deliberately excluded.

This book is maintained separately from the canonical subject articles. Wiki
ingestion tools exclude the books/ publication directory; regression tests
check that unrelated future wiki directories still remain eligible. The PR
does not revise canonical beer articles or publish a new wiki edition.

## Rebuild the reading editions

The build uses Python 3.12, Pandoc 3.1.3, the pinned Python packages in
requirements.txt, and CairoSVG's system Cairo library. The original fonts
are bundled with their licenses, so building requires no font download.
The production scripts do not fetch research sources or use a network service.
Pandoc and Cairo must be installed separately; on Ubuntu these are provided
by the pandoc and libcairo2 packages.

From this book directory:

```bash
python3 -m venv .build/venv
. .build/venv/bin/activate
python -m pip install -r requirements.txt
python tools/design_cover.py
python tools/build_book.py
python tools/validate_book.py
```

build_book.py reads **only the release master**. It does not silently regenerate
or overwrite the manuscript from working chapter files. Both final formats go
to dist/. Intermediate fonts, renderings and caches stay in the ignored .build/
directory. The cover script produces exact glyph outlines for vector exports
while retaining editable live text in the source SVG.

If editing the working chapters or research records, deliberately assemble a
new release master and inspect the diff before typesetting:

```bash
python tools/assemble.py
git diff -- the-beer-detective.md sources-and-chapters.md
python tools/build_book.py
python tools/validate_book.py
```

Assembly also regenerates the combined evidence map and manuscript manifest.
Reassembly checks wiki paths and should run inside a World Beer Wiki checkout;
typesetting the delivered master also works from a standalone book package.
The individual chapter files and front/back-matter files are editorial working
sources; the delivered master is the complete publication text. Direct edits
to the master are honored by the format builder. Preserve such changes in the
working sources before intentionally running assembly again.

To rebuild one format during layout work, use --format pdf or --format epub.
Each format records its own input-master hash; final validation rejects a stale
companion format after a manuscript change. Final validation requires both
formats to match the current master.

To package the complete book, including sources, designs, licenses and final
reading editions, run `python tools/package_book.py`. It creates the project
ZIP in dist/ and SHA256SUMS at the book root, excluding build caches and nested
archives.

## Validation and visual review

validate_book.py inspects the finished artifacts rather than just the build
code. It checks chapter and word counts, chapter-local numbering, every
internal EPUB target, individual note returns, navigation order, source-link
preservation, PDF bookmarks, page dimensions, actually used embedded fonts,
text completeness, the cover and artifact/master hash coherence. Its results
are written to [validation-report.json](research/validation-report.json).

The EPUB is also checked with the official
[EPUBCheck 5.4.0 release](https://github.com/w3c/epubcheck/releases/tag/v5.4.0).
Download its release ZIP, verify SHA-256
33350c61038e71dfb3d45a76aed04bf5481e6d5500cb780f6e98db8bbd15a28c, and extract
it outside the tracked project files. With Java installed:

```bash
mkdir -p .build/epubcheck-tmp
java -Djava.io.tmpdir="$PWD/.build/epubcheck-tmp" \
  -jar /absolute/path/to/epubcheck-5.4.0/epubcheck.jar \
  dist/the-beer-detective.epub --json research/epubcheck-report.json
```

The explicit temporary directory lets the validator inspect images in a
restricted workspace. The official validator is not bundled in this book's
release package. The [EPUBCheck report](research/epubcheck-report.json) records
the version and result for the delivered EPUB. Visual inspection of the PDF
is recorded in the editorial report; automated checks do not substitute for it.

The repository's existing wiki validator, Atlas checks and regression suite
remain separate gates. The scoped book workflow rebuilds the publication and
checks its artifacts without deploying a website or merging the branch.

## Attribution and rights

Project attribution is **The Beer Detective — a World Beer Wiki book project**.
The existing repository [Apache License 2.0](LICENSE) governs this submitted
original contribution; no separate Creative Commons grant is asserted.
[NOTICE.md](NOTICE.md) records attribution and distribution details. Cited
third-party works retain their rights. Source papers, photographs and archival
scans are not redistributed.

The original font files in design/fonts/ retain their SIL Open Font License
notices. Build-time static instances have distinct internal names and preserve
the font licenses. The PDF and EPUB carry the license and attribution notices
as embedded attachments/package resources as well as the readable edition
statement. The complete project package includes all license files.

## Contributing corrections

Identify the chapter, the disputed statement and the source that changes it.
For a source accessed only in part, a legitimate full-text version is especially
useful. Human reviewers should consult the concrete questions in the editorial
report; feedback should not be described as specialist or community approval
unless the reviewer has actually given it and agreed to that attribution.
