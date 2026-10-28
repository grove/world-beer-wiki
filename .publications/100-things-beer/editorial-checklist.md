# Editorial and production checklist

**Edition:** 28 October 2026 · **Research foundation:** World Beer Wiki 1.19, commit `3b985c19a9dcccef8d334be54b5405e42093e812`.

This checklist consolidates the manuscript reviews, source-access records, automated validation, and rendered-page inspection. These are **AI-assisted editorial and technical checks, not independent scholarly peer review, community approval, or exhaustive verification of every factual statement**. The source corpus remains an evolving collection of AI-assisted research drafts.

**Release status:** the complete reading editions and publishing source are built and validated. All three final production confirmations below are complete. Paths are relative to the publication directory. Earlier research and polish reports retain their stage-specific counts; `research/validation.json` supplies the final release metrics.

## Edition metrics

| Measure | Recorded result | Final-build status |
|---|---:|---|
| Numbered lessons | 100 | Verified; no lessons added or removed by final corrections |
| Part allocation | 34 History / 33 Science / 33 Culture | Verified |
| Linked lesson notes | 100 | Verified; note 84 gained a supporting source |
| Lesson prose | 24,922 words; 232–263 words per lesson | Final corrections leave lesson prose unchanged |
| Complete reading edition | 34,911 readable words | Verified; includes contents, notes, and full license appendix |
| PDF | 142 pages | Verified; all 100 lessons occupy one page each |
| Source map | 188 wiki articles; 143 distinct underlying source URLs | Final source addition recorded in JSON and CSV |
| Manuscript external URLs | 323 | Earlier audit covers 322; supplemental PubMed source access covers the addition |

## Completed editorial reviews

### Structure and selection

- [x] Exactly 100 sequentially numbered lessons, three required parts, unique anchors, and one matching evidence note per lesson.
- [x] Pre-drafting matrices recorded each lesson's discovery, wider-world question, wiki articles, underlying sources, limitations, and overlap controls. The final source map preserves that editorial structure.
- [x] Related subjects address different questions: historical measurement and chemical meaning; ancient crop ancestry and present conservation; packaging calculations and collection institutions; yeast cultivation history and evolutionary mechanisms.
- [x] Title and edition pages, contents, introduction, part openings, afterword, acknowledgments, methodology, references, and correction/contribution guidance are present. The sequence moves from evidence and institutions through material processes to social relationships.

**Evidence:** `research/source-to-chapter.json`, `.csv`, the three section research reports, and `research/validation.json`.

### Facts, attribution, and source strength

- [x] Named studies, dates, places, mechanisms, and historical episodes were checked within the access actually recorded. The logs distinguish full-text sections, abstracts, indexed excerpts, translated primary texts, institutional accounts, and inherited references. A wiki article was not accepted as independent corroboration of itself.
- [x] Archaeological observations remain distinct from proposed recipes, ceremonies, and motivations. Experimental results remain tied to sampled organisms, products, conditions, and study designs. Models and associations are not presented as universal outcomes or established causation.
- [x] Specific corrections include Qasr Ibrim's location in Egyptian Nubia, differing Abydos excavation stages, malthouse operations, the limits of factory-scale inference from a laboratory reactor, and clarity about titratable acidity. The wiki itself was not edited.
- [x] **Lesson 84 citation gap resolved:** the rice–cassava study by Schwan and colleagues (2007; PMID 17697080) was checked through its original indexed abstract and added to note 84, both source maps, and the Culture access log. This supports the existing two-study wording; full-text inspection and data reanalysis are not claimed.
- [x] Prose was reviewed for invented dialogue, unsupported quotations, health promises, safety assurances, and operational brewing advice. No such material was intentionally introduced; the review is not a guarantee beyond the documented checks.

**Evidence:** `research/history-research.json`, `science-research.json`, `culture-research.json`, `review-history-by-science.json`, and `review-science-by-history.json`.

### Cultural framing

- [x] Named communities, beverages, narrators, translators, and places retain their identities. Sake, cauim, giroba, pulque, masato, and other preparations are not required to adopt a European commercial definition of beer.
- [x] Similar ingredients or techniques do not establish common ancestry. Small field studies, household samples, and selected interviews do not stand for entire peoples or national populations.
- [x] Colonial descriptions, tourism accounts, producer histories, heritage listings, and archival finding aids are attributed according to their perspectives. Heritage recognition is not treated as endorsement by every participant or as a ranking of traditions.
- [x] Acknowledgments do not imply approval by named communities or researchers. No community photographs, protected research figures, ceremonial instructions, or invented interview quotations are reproduced.

**Limit:** no community consultation or independent native-language review occurred. Publication should retain that disclosure, including when individual claims have strong documentary support.

### Style and reader experience

- [x] Structural, style, and concise-prose passes reduced repeated transitions and explanations while preserving concrete examples, distinctive openings, humor, and material qualifications.
- [x] Technical vocabulary is introduced in context. Cross-references connect relevant discoveries without making chapters dependent on prior reading. Readers are not assumed to drink beer or know brewing.
- [x] The introduction and afterword connect the hundred lessons into a shared inquiry. They acknowledge uneven geographic coverage and leave room for missing perspectives and future corrections.
- [x] Cross-review findings were addressed: malthouse wording, acidity terminology, laboratory scale, and the first expansion of Wine & Spirit Education Trust. Final layout editing shortened lesson 12 without removing its colonial-source limitations.

**Evidence:** the three `*-polish.json` records, `front-back-polish.json`, `integration-edits.json`, `final-layout-edit.json`, and `review-front-by-culture.json`.

## Production and rights checks

- [x] Canonical Markdown, EPUB, PDF, original cover, publishing descriptions, rebuild scripts, source maps, and access records exist. The source bundle excludes downloaded research publications and temporary source caches.
- [x] The final EPUBCheck 5.4.0 run reported **zero fatal errors, errors, or warnings**. Automated checks also validated EPUB XML/resources, lesson anchors, internal destinations, note structure, and PDF link annotations. These tests do not certify identical behavior in every commercial reader application.
- [x] All 142 pages of the pre-correction PDF received contact-sheet review. **38 individual page PNGs** were opened across the three visual reviews, including front matter, long lessons, section transitions, notes, and appendix. Pages seen only in contact sheets were not represented as individually inspected. Supplied individual PNGs were 480 × 720 pixels, not high-resolution print proofs.
- [x] The visual pass found no narrative clipping, overlap, unintended blank pages, or tiny lesson continuations. Cover, title, and part-opening whitespace is intentional.
- [x] **Appendix numbering resolved in source:** literal Apache clauses 1–9 and subclauses (a)–(d) replaced automatic list numbering. The production editor reports normalized full-text agreement with the license in Markdown, EPUB, and PDF. Note 85 spacing was corrected; note 91's suspected missing heading space was checked and required no change. The corrected appendix and source-note pages passed follow-up visual inspection; the final validation script also compares the complete license text in all three editions.
- [x] The reference dependency environment produced identical final EPUB/PDF hashes on two consecutive builds after the appendix and source-note corrections.
- [x] Wiki and atlas checks passed before and after the addition, with identical canonical inventory counts. Book files remain separate from canonical wiki articles and tools.
- [x] Apache 2.0 attribution and license text are retained; no upstream `NOTICE` was present at the pinned snapshot. Third-party rights remain separate, and the bundled font license is included. Free reading is authorized; **no new Creative Commons grant is asserted**. CC BY 4.0 remains a rights-holder recommendation, not a completed licensing action.

**URL audit scope:** the bounded audit checked 178 wiki destinations locally, with seven successful live samples. Of 144 external URLs, 97 were reachable, 30 restricted, and 17 unavailable under the recorded request limits; no 404 or 410 response was observed. Those categories do not establish source validity or permanent availability, and failed requests were not retried. The audit's original 322 URLs match the manuscript apart from the subsequently added PubMed study, whose successful abstract access is recorded in its supplement.

**Evidence:** `research/epubcheck.txt`, `validation.json`, `reproducibility.json`, `external-link-audit.json`, baseline/final wiki and atlas reports, `final-license-edit.json`, and the visual-review records summarized in `research/visual-review.json`.

## Unresolved verification limits to retain

| Area | Remaining limitation and editorial treatment |
|---|---|
| Ancient history and archaeology | Process, ritual, and adaptation interpretations have not been independently replicated or specialist-reviewed. Several arguments remain abstract/excerpt-based; complete monographs and original archives were not all consulted. |
| Institutional histories | Lesson 24 uses attributed civic explanations rather than the original 1812 ordinance. Lessons 27 and 34 rely partly on Carlsberg retrospectives; laboratory notebooks and the original 1909 pH publication were not inspected. No exclusive priority or unrecorded motives are asserted. |
| Scientific literature | Several auxiliary references remain explicitly inherited, including material in lessons 48 and 56. Full proprietary ASBC methods and ISO standards were not accessed. Experiments, genomic assignments, statistical models, and environmental calculations were not reproduced or reanalyzed. |
| Language and community knowledge | German, Spanish, Turkish, and Norwegian material lacks independent language/community review. The Zao/Zou inconsistency in lesson 75 remains visible rather than silently resolved. |
| Source disagreement | The expert-pairing source's conflicting counts of principles are excluded from lesson 88; resolving the discrepancy needs comparison of the full paper and supplements. |
| Heritage and archives | Korea's designation chronology uses the recorded proposal and later institutional confirmation, with limited access to the latter. Lessons 94 and 99 use catalog/finding-aid descriptions; the interviews themselves were not heard or transcribed for this book. |
| Coverage and access | Some publisher content remains restricted or available only through abstracts/excerpts. Geographic and linguistic coverage is uneven. None of the checks establishes universal cultural authority or community endorsement. |

These are disclosed evidence boundaries, not requests to strengthen the claims. Future verification should update the manuscript, source map, and access record together.

## Final release confirmations

- [x] **Final metrics and hashes refreshed.** The canonical manuscript, EPUB, and PDF hashes in `research/validation.json` describe the final corrected files. The final book has 34,911 readable words, 100 lessons and 142 PDF pages.
- [x] **Final EPUB validation and reproducibility passed.** EPUBCheck 5.4.0 reported 0 fatals, 0 errors, 0 warnings and 0 informational messages. Two successive builds produced identical EPUB and PDF bytes; the report records both hash sets.
- [x] **Final PDF geometry and changed pages passed.** The refreshed geometry report records 142 pages, no text characters outside the page and consecutive lesson pages within each part. Only the intentional cover and title leaf have fewer than 60 extracted words. Corrected pages 135–137 and 139–142 received follow-up individual-page inspection. No visual findings remain in those pages; the earlier introduction and lesson spill pages have been eliminated.

The final reading files are complete. Independent expert review, community consultation and broader access to original archives remain the substantive limitations described above; these are not represented as completed production tasks.
