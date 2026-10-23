# Settle-5 — New-study disputes (Robustness Pass, Review 2)

**Role:** Settlement Reader 5 (new studies), Robustness Pass, Review 2 (LLM citation fabrication meta-analysis), 23 October 2026.
**Scope:** Six tasked items covering seven records from the two independent extraction passes on newly included studies (`robustness/ft2/extraction-newA-batch*.csv`, `extraction-newB-batch*.csv`): R0047, R11480, R7018, R7837, R0264, R0277, R0186. Each disputed cell was re-read in the full text (`robustness/fulltexts2/`, located via `robustness/ft2/retrieved-files.json`) and settled against `extraction-form.md` — the fixed review definitions, mapping rule 2 (map only if exact), rule 5 (exact by sum), rule 6 (derive a count from a percentage at a printed denominator only if it gives a whole number without rounding doubt) and rule 7 (fully-accurate mapping needs the checked fields). The manuscript and analysis files were **not** read.
**Conventions:** A blank settled value means the cell stays blank — narrative only, never zero (form field 37). `wrong_pass` = `neither` where both passes were right, `both` where both were wrong. Arm names are Pass A's, with Pass B's variant noted where it differs.
**Machine-readable companion:** `robustness/settle-5.csv` (record_id, study_id, model_arm, field, settled_value, wrong_pass, source_location).

**Summary of rulings**

| # | Record / study | Arm | Field | Pass A | Pass B | **Settled** | Wrong pass |
|---|---|---|---|---|---|---|---|
| 1a | R0047 DiFebo_2026 | ChatGPT-5 (clinical-studies subanalysis) | n_major_inaccuracy_incl_fabricated | 10 | blank | **10** | B |
| 1b | R0047 DiFebo_2026 | ChatGPT-5 / Elicit / Consensus / Scite | refs_requested (×4) | 160 | blank | **160** each | B |
| 2a | R11480 Moskatel_2023 | ChatGPT-3.5 | n_major_inaccuracy_incl_fabricated | blank | 82 | **82** | A |
| 2b | R11480 Moskatel_2023 | ChatGPT-3.5 | n_fully_accurate | blank | 33 | **33** | A |
| 3a | R7018 Woodrow_2025 | ChatGPT-4 with ScholarAI plugin | refs_generated | blank | 56 | **blank** | B |
| 3b | R7018 Woodrow_2025 | ChatGPT-4 with ScholarAI plugin | n_major_inaccuracy_incl_fabricated | blank | 11 | **blank** | B |
| 3c | R7018 Woodrow_2025 | Assistant by scite | refs_generated | blank | 100 | **blank** | B |
| 3d | R7018 Woodrow_2025 | Assistant by scite | n_major_inaccuracy_incl_fabricated | blank | 62 | **blank** | B |
| 4 | R7837 Suppadungsuk_2023 | ChatGPT-3.5 | n_fabricated | blank | 192 | **192** | A |
| 5a | R0277 | ChatGPT 3.5 | study_id | Knee_2025 | Knee_2025 | **Knee_2025a** | both |
| 5b | R0264 | ChatGPT-4o mini | study_id | Knee_2025 | Knee_2025 | **Knee_2025b** | both |
| 6 | R0186 McCavitt_2026 | ChatGPT-4o mini | n_fabricated | blank | blank | **blank** | neither |

---

## 1. R0047 — DiFebo_2026 (Eur Heart J Digit Health 2026), R0047.xml

### 1a. ChatGPT-5 (clinical-studies subanalysis), `n_major_inaccuracy_incl_fabricated`: SETTLED 10; Pass B wrong

**The paper's definitions, verbatim** (Methods, "Operationalization of retrieval tools"). The paper distinguishes exactly two categories of citation inaccuracy:

> "Citations containing minor bibliographic discrepancies (errors in title, authors, journal, or DOI) for which the intended source article could nonetheless be reliably identified and retrieved were considered locatable, corrected, and not classified as hallucinations, since the underlying evidence remains accessible to the clinician. Conversely, citations that could not be traced to any identifiable source after DOI and title searches were classified as hallucinated (fully fabricated), as the cited evidence does not exist and can neither be retrieved nor verified."

**The subanalysis count, verbatim** (Results, "Citation accuracy and hallucinated references"):

> "In the main analysis (up to ten references per condition), no hallucinated citations occurred across any tool, topic, or prompt; only minor, correctable discrepancies in titles, DOIs, or author names arose, and their source articles were reliably located. Fabricated, untraceable citations were confined to the clinical-studies subanalysis, which requested larger lists: ChatGPT-5 produced ten (17%), nine of them in topic C, an emerging, broad topic requiring the longest list (22 articles), one in topic D, and none in the established topics, all beyond the 11th reference."

Figure 5 legend repeats the count: "Ten ChatGPT-5 citations (17%) were hallucinated." The denominator both passes use (59 ChatGPT-5 citations in the subanalysis: 25 retrieved by both ChatGPT-5 and the human SLRs + 34 retrieved only by ChatGPT-5, per the Figure 5 legend) is consistent with the printed percentage: 10/59 = 16.9% ≈ 17%.

**Ruling.** Yes to both parts of the tasked question. (i) The printed count is **10**: it is printed as a count ("produced ten (17%)"), not only as a percentage. (ii) The printed category maps to review major inaccuracy. The paper's "hallucinated (fully fabricated)" is defined as untraceable to any identifiable source after DOI and title searches — that is the review's *completely fabricated* ("no matching publication exists"), and the review's major inaccuracy expressly *includes* completely fabricated. The mapping is exact, not a lower bound, because of the paper's two-category scheme: the only other inaccuracy category is the locatable minor discrepancy, which the review definition expressly excludes from major ("Minor errors that leave the source findable and correctly credited do not count here"). Every subanalysis inaccuracy is therefore either major (hallucinated) or minor (locatable); the hallucinated count is the whole of major inaccuracy for this arm. This is the same logic both passes already applied to the main analysis, where no hallucinated citations and only locatable discrepancies were reported and both passes entered n_major = 0. **Settled: 10.** Pass A right; Pass B wrong to leave the cell blank.

### 1b. Four main arms, `refs_requested`: SETTLED 160 each; Pass B wrong (minor, for the record)

The design is printed, verbatim (Figure 1 legend; Methods, "Study design overview" / "Research queries and search quadrants"):

> "Each tool was queried with standardized queries (four natural-language prompts per AI-based tool; three Boolean queries of increasing complexity for PubMed), retrieving up to 10 top-ranked articles per tool and per query."

> "For each tool, topic, and prompt, we selected the top ten ranked articles whenever possible."

Four topics × four natural-language prompts × 10 references per query = **160 requested per AI tool** (ChatGPT-5, Elicit, Consensus, Scite). The total "160" is not printed as a single numeral anywhere in the paper; it is exact design arithmetic from three printed quantities, with no rounding doubt — the same basis on which Pass B's own notes flag its on-disk value as derived (see Caveat 1). PubMed, the non-AI comparator (3 Boolean queries per topic → 120), is not one of the four tasked arms and Pass A extracted no PubMed arm. **Settled: 160 for each of the four arms.** Pass A right; Pass B wrong (blank) on the tasked reading.

---

## 2. R11480 — Moskatel_2023 (Front Neurol 2023), R11480.xml — ChatGPT-3.5: SETTLED major 82 and fully accurate 33; Pass A wrong on both

Both passes agree on the denominator and the fabricated count: refs_generated = 115, n_fabricated = 76.

**The paper's categories as printed, verbatim.** Abstract:

> "only 33/115 (29%) of the papers ChatGPT cited were real, while 76/115 (66%) were "hallucinated" not real papers and 6/115 (5%) shared the names of real papers but had not real citations." [sic]

Results:

> "Of the 47 medications reviewed, ChatGPT generated supporting citations for 41. These 41 papers resulted in 123 cited papers which reduced to 115 papers when duplicates were removed. Of these 115 papers, only 33/115 (29%) were real papers that were correctly cited. Strikingly, 76/115 (66%) papers were ChatGPT "hallucinations" and did not exist. The other 6/115 (5%) papers had the names of real papers but the citation details, including author, journal, and year, were new creations."

Methods (verification): the citations "were then documented and the titles searched on both Google Scholar and PubMed to determine if they were real literature or "hallucinations." Real papers were then assessed for relevance to the query."

Discussion confirms the partition: "Only 34% of the 115 citations produced in our study were real papers, including those with real titles but inaccurate citations, and the other 66% were not real publications." (33 + 6 = 39; 39/115 = 33.9% ≈ 34%.) The three categories are mutually exclusive and exhaustive: 33 + 76 + 6 = 115.

### 2a. `n_major_inaccuracy_incl_fabricated` = 82 (76 + 6), exact by sum (rule 5)

Yes — the sum is exact. The 76 are completely fabricated ("did not exist"), hence major. The 6 are major under the review definition's own words: major inaccuracy includes "a fabricated element that forms part of the identity of the source, such as a fabricated title, fabricated first author, or fabricated DOI" and "a journal, year, volume or page set that points to a different publication or to no publication". A citation that keeps a real paper's name but invents its author, journal and year points, as cited, to no publication: the real paper of that name is not the paper the citation describes. The parts are non-overlapping, and together with the 33 correctly cited they exhaust the 115, so the sum covers major inaccuracy and nothing else: no minor-error category exists anywhere in the paper, and the 33 are by definition not major. The 6 are correctly *not* in n_fabricated (a publication with that title exists — both passes agree, and §4 below applies the same boundary), which is exactly why they belong in major rather than in fabricated. **Settled: 82.** Pass B right (exact by sum, parts listed); Pass A wrong.

Pass A's stated ground for blanking — that the real papers "were assessed for relevance, not all-field accuracy" — misreads the paper's structure. The 33/76/6 classification is a *citation-correctness* classification; relevance was a separate, subsequent assessment with its own Table 1 columns ("Number of real studies cited" vs "Number of real and relevant studies cited"), and no citation was moved into or out of the 33 by relevance.

### 2b. `n_fully_accurate` = 33, strict, exact

Yes. The printed label is "real papers that were correctly cited", and the paper's own contrast in the same Results paragraph shows what "correctly cited" was tested against: the only citation-correctness failures the paper identifies among real-titled papers are the 6, excluded from the 33 *because* their author, journal and year were fabricated. The fields the study checked for this classification are the ones its method and its error category display — title (searched on Google Scholar and PubMed) and author, journal, year (compared against the real paper, as the description of the 6 proves). Under rule 7 and the form's strict definition ("accurate on all fields checked by the study… volume, pages and DOI *where the study checked them*"), a count maps to strict if any error in a checked field counted against accuracy — demonstrated here by the 6. The paper claims no volume/pages/DOI accuracy check for this count (DOI/PMID errors appear only in Table 2's examples of hallucinated references), so nothing unchecked is silently included. **Settled: 33.** Pass B right; Pass A wrong, for the same relevance conflation as in §2a.

---

## 3. R7018 — Woodrow_2025 (Arch Bone Jt Surg 2025), R7018.xml — both arms: SETTLED ALL BLANK; Pass B wrong on all four cells

Pass B's arms (Pass A used the same arm names): ChatGPT-4 with ScholarAI plugin (refs_generated 56, n_major 11) and Assistant by scite (refs_generated 100, n_major 62). Pass A left every outcome blank. Pass A is right; nothing in this paper maps.

**What "accurate" means in this paper, verbatim** (Materials and Methods, "Review Process"; the study authors graded the AI-generated papers):

> "For a citation to be considered accurate it must 1) reference a previously published journal paper and 2) contain factually correct information mentioned in said paper. Claims requiring but missing a citation were graded as incorrect."

**What the "incorrect" errors actually were, verbatim** (Discussion):

> "The two main citation errors the AI algorithms made were 1) omitting a citation when one would be required and 2) the referenced paper did not contain the claim intended to be cited."

> "While all of the citations referenced authentic scientific papers from peer-reviewed journals, sometimes the content was tangential at best." (of Assistant by scite)

Table 2 ("Sentence and citation accuracy for AI-generated papers") prints, per generated paper, only a citation-accuracy percentage, a "Number of Incorrect Citations" and a "Number of Missing Citations": Assistant by scite osteoarthritis 35.14% / 24 / 26; ChatGPT osteoarthritis 90% / 3 / 4; Assistant by scite calcaneus fracture 39.68% / 38 / 12; ChatGPT calcaneus fracture 69.23% / 8 / 8. No reference denominator is printed anywhere in the paper — no text, table or legend states how many references or citations any generated paper contained.

**Ruling — the "incorrect" counts do not map to major inaccuracy.**

1. **No bibliographic field was ever checked.** The accuracy test is (1) existence of a published paper plus (2) whether that paper contains the cited information. Authors, title, journal, year, volume, pages and DOI were never compared with the source record. A citation with perfect bibliographic details fails as "incorrect" whenever the paper does not contain the specific claim; a citation with garbled bibliographic details passes whenever the (intended) paper contains it. The counts grade *claim support inside generated manuscripts*, not the bibliographic accuracy of generated references.
2. **The counted error is broader than the review's one claim-related major case.** Review major reaches "a real publication cited for a claim or topic it does not cover where the study counts that as misattribution". This study counts any failure of its test 2 — including a paper that covers the topic but not the specific fact stated, which the paper itself describes as content "tangential at best". Partial/tangential coverage and wrong-detail quotation are claim-support failures outside the review clause, and they are not separated from whole-topic misattribution anywhere in the paper. Broader than the review definition → rule 3: maps to no review outcome.
3. **The lump cannot be split.** "Incorrect" mixes test-1 failures (no previously published paper — the fabricated-type case) with test-2 failures (support failures), with no printed split for the ChatGPT arm. For the Assistant arm the Discussion states all citations referenced authentic papers, so its 62 incorrect contain no fabricated references at all — they are support errors only, which confirms what the category measures. Rule 5 cannot rescue a sum whose parts are not printed separately.

**Ruling — 56 and 100 are not the paper's denominators.** They are Pass B's algebraic recovery: solving each paper's denominator from its printed percentage and incorrect count (27/30 = 90%, 18/26 = 69.23%; 13/37 = 35.14%, 25/63 = 39.68%), then summing across the two papers per tool. Three bars: (i) form fields 20/32 require denominators *as printed*; none is printed. (ii) Rule 6 authorises deriving a *count* from a percentage at a printed denominator; it does not authorise deriving the denominator itself from a percentage and a count. (iii) The recovery carries method doubt: it stands only if missing citations are excluded from the accuracy denominator, while the Methods state claims missing a citation "were graded as incorrect" — with the missing counts (4/8/26/12) in the graded set, the printed percentages yield no whole correct counts at all (e.g. ChatGPT osteoarthritis 27/34 = 79.4%, not the printed 90%). A denominator that requires silently overriding the paper's printed grading rule is a derived denominator with rounding/method doubt, not an extractable one.

**Settled: refs_generated and n_major_inaccuracy_incl_fabricated blank on both arms** (the Table 2 incorrect counts 11 and 62 remain available for narrative synthesis under their printed label). Pass B wrong on all four cells; Pass A right.

---

## 4. R7837 — Suppadungsuk_2023 (J Clin Med 2023), R7837.xml — ChatGPT-3.5: SETTLED n_fabricated 192; Pass A wrong

**The printed count and denominator, verbatim** (Results):

> "A total of 610 references were provided from the ChatGPT search in 12 topics of specific fields of nephrology. Of the references given by ChatGPT, we found that 378 (62%) existed, while 192 (31%) were fabricated, and 40 (7%) were incomplete (Figure 1)."

Table 1, Overall row (n = 610): Incomplete Reference 40 (7); Complete Reference Fabricated 192 (31); Existence with All Correct 122 (20); Existence with Partial Correct 256 (42). The four categories partition the denominator exactly: 40 + 192 + 122 + 256 = 610, and 122 + 256 = 378 = "existed".

**The definition, as the paper operates it.** Methods §2.1 (verification): references were checked first by DOI in PubMed; if PubMed yielded nothing, by title and author searches in Google Scholar, with Web of Science used to cross-reference — i.e. a reference "existed" if a matching publication could be located in the named sources, and the fabricated category is the complement of "existed" among complete references. Methods §2.2 states the category in compressed wording:

> "References were categorized as fabricated or non-existent if all citation elements were forged or non-existent, respectively. Existing references were deemed incorrect if at least one component was inaccurate. References with incomplete sets of six elements were classified as incomplete."

Figure 2 legend describes the fabricated references the same way: "for which all citation components were inaccurate, including authors, title, journal name, year of publication, digital object identifiers (DOI), and link."

**Ruling.** Yes: **192 is the printed fabricated count at denominator 610, under a definition that matches the review's "no matching publication exists".** Pass A read the §2.2 sentence ("all citation elements forged") as an extra necessary condition making the category *narrower* than the review definition (rule 4), on the ground that a real title with wrong authors sits in "existing, partial correct" (256) whereas — on Pass A's reading — the review would count it as fabricated. That reading fails twice:

1. **The operative classification is existence, and it is exhaustive.** "Existence with Partial Correct" requires, by its own heading, an *existing* publication that was located; a complete reference for which no publication could be located has nowhere else in the partition to go except the 192. The "all elements" wording describes what the fabricated references looked like (nothing about them matched — authors, title, journal, year, DOI and link all inaccurate, per Figure 2); it is not a second gate that demonstrably diverted any non-existent reference into another category, and Pass A identified no such case in the paper.
2. **Pass A's premise about the review definition is contradicted by this review's own settled practice.** The review's fabricated definition turns on whether a publication "that matches on title and source identity in a way that could count as the same work" exists. A real title carrying wrong authors is precisely Moskatel_2023's 6 (§2 above): both passes there — Pass A included — counted them as *not* fabricated (a publication with that title exists) and as major inaccuracy instead. Suppadungsuk's "existing, partial correct" is the same case on the same side of the boundary. The study's fabricated/existing boundary therefore coincides with the review boundary as applied: a matching publication located → not fabricated; none located → fabricated.

**Settled: n_fabricated = 192 (of 610).** Pass B right; Pass A wrong. (The two passes agree on the rest of this arm, including n_fully_accurate = 122, "existence with all correct" over all six components; that cell was not in dispute.)

---

## 5. R0264 and R0277 — first-author surname and study_id: SETTLED Knee_2025a (R0277) and Knee_2025b (R0264); both passes wrong (undifferentiated ID)

**Verified from each paper's title page (JATS author contrib-group in the XML full texts).** In both papers the first-listed author contrib is:

> `<surname>Knee</surname><given-names initials="CJ">Christopha J</given-names>`

The corresponding-author byline renders the name in given-names-first order as "Christopha J. Knee" (christophaknee@gmail.com), and both papers carry the copyright line "© 2025, Knee et al." **The first author's actual surname is Knee in both records** — the passes' surname was right. (Caution recorded for the file: both XML files also list Alexander Muacevic and John R Adler as `contrib-type="editor"` — in R0277 the editor group precedes the author group in raw XML order. They are the journal's editors, not authors, and are not the source of the first-author name.)

**They are two distinct studies**, by the same first author and overlapping co-authors (Campbell, Sivakumar, Symes; R0277 additionally Wines):

| | R0277 | R0264 |
|---|---|---|
| Title | "Investigating the Accuracy and Consistency of ChatGPT in the Management of Achilles Tendon Ruptures" | "An Assessment of the Accuracy and Consistency of ChatGPT in the Management of Midshaft Clavicle Fractures" |
| Journal / date | Cureus, published 3 Feb 2025 | Cureus, published 8 Apr 2025 |
| DOI | 10.7759/cureus.78433 | 10.7759/cureus.81906 |
| PMCID | PMC11882158 | PMC12059606 |
| Experiment | 8 questions × 2, 47 references (16 correct / 19 incorrect / 12 fabricated) | 14 questions × 3, 128 references (1 correct / 14 incorrect / 113 fabricated) |

**Correct study_ids.** Both passes used the bare `Knee_2025` for *both* records in batch 1, which collides. With the review's FirstAuthor_Year convention plus chronological disambiguation suffixes: the earlier paper, R0277 (Feb 2025), is **Knee_2025a**; the later paper, R0264 (Apr 2025), is **Knee_2025b**. Both passes wrong on the identifier (right surname, missing disambiguation).

---

## 6. R0186 — McCavitt_2026 (JBJS Open Access 2026), R0186.xml — ChatGPT-4o mini, `n_fabricated`: SETTLED BLANK; both passes right (neither wrong)

Both passes left the cell blank. A full-text search of R0186.xml for every occurrence of "fabricated/fabrication" confirms there is **no printed fabricated count for this arm anywhere in the paper**. Every occurrence is one of the following:

- Abstract: "ChatGPT-4o mini provided 228 responses citing 2,556 publications when prompted for supporting evidence, of which 1.1% overlapped with AAOS CPG references, and **7.9% were fabricated**."
- Results: "ChatGPT completely fabricated **7.9%** of references."; Results (totals): "228 responses to requests for supporting evidence, which yielded 2,556 references."
- Discussion: "Our finding of a **7.9%** reference fabrication rate **across 2,556 references** in ChatGPT suggests continued improvement in fabrication frequency."
- Methods (definition only): "A fabricated reference was defined as a reference cited by ChatGPT but not indexed in PubMed."
- Table III ("Mean Counts of Citation Characteristics Per Single ChatGPT Response"): "Fabricated references **0.59 ± 1.10**" per response, against "Total references 7.53 ± 2.28" — a per-response mean, not a count.

No integer fabricated count is printed in the text, tables, or figure/table legends; the numerals 201 and 202 do not occur anywhere in the full text.

**Ruling.** Rule 6 bars the derivation: 0.079 × 2,556 = 201.924, not a whole number, so the percentage carries rounding doubt and no count may be derived. Table III cannot rescue one: multiplying a rounded per-response mean (0.59 × 228 ≈ 135) is not a printed count, and the same table's total-references mean (7.53 × 228 ≈ 1,717) contradicts the printed total of 2,556, so the means and the total cannot both ground a count. **Settled: blank — the 7.9% is reported narratively only.** Both passes right; wrong pass: neither. (Recorded for completeness, not as the basis of this ruling: both passes also flagged that the study's fabricated definition — not indexed in PubMed — is broader than the review definition, so the cell would not have mapped even if a count had been printed.)

---

## Caveats

1. **R0047 provenance note.** In the CSV files as they stand on disk, Pass B's batch-1 rows also carry refs_requested = 160 (flagged in its notes as derived) and n_major = 10 for the subanalysis arm; the discrepancy list as tasked describes Pass B as blank on these cells. The mismatch appears to be an arm-matching artefact (Pass B spells the study_id "Di Febo_2026", adds a PubMed comparator row, and names the subanalysis arm "ChatGPT-5 (clinical-studies subanalysis, larger reference lists)"). The settled values in §1 are the same under either reading, and no change to Pass B's on-disk values is implied by the "wrong pass" labels there, which follow the tasked discrepancy list.
2. **R7837 residual gap (flagged, not barring).** The 40 "incomplete" references (missing one or more of the six elements) are classified by completeness before existence, and the paper does not print how many of the 40 also had no matching publication. No printed count splits them, and neither pass proposed adding any part of the 40 to fabricated; the gap is a field-46 item for the author-contact list. It does not change the ruling in §4, which concerns the printed fabricated category's definition and count.
3. All quotations are verbatim from the XML full texts as provided, including the papers' own errors (e.g. Moskatel's "had not real citations" [sic]; Suppadungsuk's compressed §2.2 wording). Internal discrepancies already flagged by one or both passes (e.g. R0186's Table III means vs its 2,556 total) are recorded, not corrected, and none changes a ruling above except as discussed in §6.
4. No number in this report was taken from the manuscript or the analysis files, which were not read.
