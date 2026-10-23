# Settle-4b — Omission-direction disputes: cells filled by Pass A, left blank by Pass B

**Role:** Settlement Reader 4b, Robustness Pass, Review 2 (LLM citation fabrication meta-analysis), 23 October 2026.
**Scope:** Five studies, nine disputed cells. In every case Pass A filled a cell that Pass B left blank. Each cell was re-read in the full text and settled against `extraction-form.md` — the fixed review definitions, mapping rule 2 (map only if exact: the study definition must cover the same cases as the review definition, no more and no fewer), rule 5 (exact-by-sum: separate printed counts may be summed only if together they cover the review definition exactly and nothing else), rule 6 (a count may be derived from a percentage at a stated denominator only if it gives a whole number without rounding doubt), and rule 7 (fully-accurate mapping needs the checked fields). The manuscript and analysis files were **not** read.
**Sources read:** `extraction-form.md`; `extraction-passA.csv`; `extraction-passB.csv` (incl. `robustness/extb/` batches); full texts `fulltexts/R0094.xml`, `fulltexts/R2475.xml`, `fulltexts/R3629.xml`, `fulltexts/R0053_v2.xml`, `fulltexts/R0180_v2.xml`.
**Machine-readable companion:** `robustness/settle-4b.csv` (Pass-A arm names throughout; a blank settled value means the cell stays blank — narrative only, never zero, per form field 37).

**Summary of rulings**

| Study | Arm (Pass A) | Field | Pass A | Pass B | **Settled** | Wrong pass |
|---|---|---|---|---|---|---|
| Athaluri_2023 | ChatGPT | n_major_inaccuracy_incl_fabricated | 69 | blank | **blank** | A |
| Dhaimade_2026 | GPT-5.0 (Full Test) | n_major_inaccuracy_incl_fabricated | 135 | blank | **blank** | A |
| Dhaimade_2026 | GPT-5.0 (Individual Question) | n_major_inaccuracy_incl_fabricated | 105 | blank | **blank** | A |
| Dhaimade_2026 | Claude Sonnet 4.0 (Individual Question) | n_major_inaccuracy_incl_fabricated | 18 | blank | **blank** | A |
| Linardon_2025 | GPT-4o | n_bad_doi | 51 | blank | **blank** | A |
| Seifi_2026 | GPT-5.3 | n_minor_error | 25 | blank | **25** | B |
| Seifi_2026 | DeepSeek-V3 | n_minor_error | 13 | blank | **13** | B |
| Seifi_2026 | Grok-4 | n_minor_error | 7 | blank | **7** | B |
| Singh_2026 | GPT-5 | n_fully_accurate | 59 | blank | **blank** | A |

---

## 1. Athaluri_2023 (R0094.xml) — ChatGPT, `n_major_inaccuracy_incl_fabricated`: SETTLED BLANK; Pass A wrong

**What the paper prints.** Denominator 178 references. Table 3 ("Validity and accessibility of references"):

| Table 3 row | n |
|---|---|
| References with a valid DOI | 109 |
| References with an invalid DOI | 69 |
| References that turned up on Google search | 150 |
| References that did not turn up on Google search | 28 |

Results, verbatim:

> "Out of the 178 references cited by ChatGPT, 69 did not have a DOI. Upon extensive internet search, 41 out of these 69 reference articles were found to exist. However, 28 articles neither turned up on Google search nor had an existing DOI."

Abstract, verbatim:

> "Out of the 178 references analyzed, 69 references did not have a Digital Object Identifier (DOI), and 28 references neither turned up on Google search nor had an existing DOI."

Discussion, verbatim (note the paper's two framings of the same 69 sit side by side):

> "Out of the 69 references for which the DOI did not work at all (that is, the DOI provided by ChatGPT for that reference was non-existent in reality or belonged to a different article), 41 articles that turned up on on an internet search are considered a result of partial AI hallucination. These 41 articles cannot strictly be considered products of total AI hallucination because the articles did exist in reality and only the DOIs provided by ChatGPT in these cases were erroneous."

> "The 28 articles that neither turned up on an extensive internet search nor had a functional DOI are undoubtedly the product of AI hallucination."

Methods (verification rule), verbatim: "the appearance of any part of the article, abstract, or even the full text was considered as an indication of a true, non-AI-hallucinated reference." The study checked exactly two things per reference: whether the article itself existed (search) and whether its DOI was functional/existed. No other field was checked against the source.

**Pass A's construction** (its own note): 28 fabricated + 41 real articles with erroneous DOI = 69, i.e. the printed invalid-DOI total, entered as major inaccuracy. Pass A also entered the same 69 as `n_bad_doi`; Pass B agrees with `n_bad_doi` = 69 and that cell is not in dispute.

**Ruling.** No printed category and no exact sum in this paper equals the review's major inaccuracy. The 28 are completely fabricated and are a subset of major inaccuracy, but the disputed increment is the 41, and the 41 do not map:

1. **The paper's own characterisation of the 41 is the review's minor/field-error profile, not major.** Review major inaccuracy is an error that "prevents retrieval of the intended source, or that misattributes the source"; review minor error is "an error in one field where the source remains the same publication, remains retrievable from the rest of the reference, and remains correctly credited in the main." All 41 were in fact retrieved ("found to exist" / "turned up on an internet search"), are the intended articles, and carry — on the paper's own account — an error in one field only: the paper calls them "partial AI hallucination" precisely because "the articles did exist in reality and only the DOIs … were erroneous."
2. **The one route from a bad DOI to major inaccuracy is not established for these 41.** The review definition reaches a *fabricated* DOI (an invented identity element) and a DOI/set of fields that "points to a different publication". The Discussion's parenthesis covers two unsplit sub-cases — DOI "non-existent in reality" and DOI that "belonged to a different article" — with no counts for either, and a non-existent DOI is equally consistent with a mistyped DOI on a correctly identified source. Worse, the Abstract and Results twice describe the same 69 as references that "did not have a DOI" / "did not have an existing DOI": on that framing the 41 include references with no DOI element at all, and a missing DOI on a real, found, correctly identified article is not a major inaccuracy under the review definition. The paper contradicts itself on the exact property the mapping turns on, so exactness cannot be shown from the full text.
3. **Rule 5 therefore fails.** A sum is allowed only where the parts "cover major inaccuracy as defined and nothing else". The 28 + 41 sum demonstrably covers more than major inaccuracy (point 1) and rests on an unresolved internal contradiction (point 2). Pass B's stated ground — "the study prints no major label or sum" — is correct in substance: there is no major-inaccuracy label, and the only candidate sum is not exact.
4. **Bad DOI ≠ major inaccuracy.** The form keeps the field-level DOI count (field 35, extracted as printed under the study's resolution-based Discussion definition — both passes agree on 69 there) separate from the reference-level outcome (section G). Pass A's error was to carry the invalid-DOI total across into the outcome field by identity. A bad DOI attached to a real article that the verifiers themselves retrieved is exactly the case in which the two counts come apart in this review's definitions.

**Settled value: blank.** Pass A wrong; Pass B right.

---

## 2. Dhaimade_2026 (R2475.xml) — `n_major_inaccuracy_incl_fabricated`, three arms: SETTLED BLANK on all three; Pass A wrong

Arms (Pass-A names) and the values Pass A entered, which are the paper's printed "hallucination rate" numerators: GPT-5.0 (Full Test) 135 of 262; GPT-5.0 (Individual Question) 105 of 328; Claude Sonnet 4.0 (Individual Question) 18 of 322. Pass A mapped these to major inaccuracy on the stated basis that they are the paper's "critically wrong" counts. That identity is nowhere printed, and the paper's text contradicts it.

**The scoring/category definitions, verbatim.** Methods, "Human-in-the-loop citation validation":

> "For each citation, it was assessed whether the source could be located and whether bibliographic details were accurate (authors, year, journal/book title, volume, pages). Each citation was categorized using a three-tier taxonomy: Completely valid: existing and accessible citations accurately supporting the information provided, partially correct: real citations with minor inaccuracies or partial claim support, critically wrong: fabricated, inaccessible, or unrelated citations."

Results, "Citation hallucination assessment" (the only place the disputed numerators appear):

> "Claude Sonnet 4.0 demonstrated the lowest hallucination rate at 5.59% (18/322), GPT-4.0 IQ showed 32.01% (105/328), and GPT-5.0 FT exhibited the highest rate at 51.53% (135/262). Citations were systematically classified using a three-tier validation system: fully verifiable, partially correct (minor errors in volume/page numbers), and critically wrong (fabricated authors, studies, journals, or completely unrelated content)."

(The Results sentence labels the 105/328 arm "GPT-4.0 IQ"; both passes flagged this — Methods and the Abstract state citations were provided and validated only for GPT-5.0 and Claude Sonnet 4.0, and Table 5 lists GPT-5.0 IQ at n ~328. Per the tasking, the Pass-A arm name GPT-5.0 (Individual Question) is used; the labelling conflict does not affect the mapping ruling.)

**Why the hallucination numerator cannot be read as "critically wrong":**

1. **The paper never states which tier(s) the hallucination rate counts, and prints no per-tier count anywhere in the article.** No table gives a tier distribution: Table 5 is a logistic-regression table (n ~264 / ~328 / ~322, odds ratios) with no tier counts. The tier distribution exists only as the Figure 5 heatmap (and supplementary files, which are not part of R2475.xml beyond their captions). Figure 5's own panel scoring, verbatim from its Results paragraph, is a *four*-level scale that does not even match the Methods three-tier taxonomy: "color‐coded from red (0 = critically wrong) through orange (1 = partially correct, multiple errors) and yellow (2 = partially correct, fine errors) to green (3 = fully verified), with gray indicating missing responses."
2. **The paper's own summaries describe "hallucination" as spanning the tiers, with critical cases predominating — not as the critical tier alone.** Abstract, verbatim: "Citation analysis revealed frequent hallucinations, mostly critically erroneous, and citation validity was independent of answer accuracy." Discussion, verbatim: "Human-in-the-loop assessment demonstrated that hallucinated citations existed across a spectrum of severity." And: "The predominance of critically erroneous hallucinations, rather than minor bibliographic inaccuracies indicates that AI citation fabrication represents a qualitatively distinct problem from human citation errors…" "Mostly" and "predominance" are only meaningful if the hallucination count also contains non-critical (partially correct) cases. On the text as printed, the numerator is broader than the critical tier, which under rules 2–3 maps to no review outcome.
3. **Even taken on its own terms, the "critically wrong" tier is not an exact match for review major inaccuracy.** It includes "inaccessible" citations (Methods wording): a real, correctly credited source that the single evaluator could not access is not shown to have no matching publication, to prevent retrieval in general, or to misattribute — the review definition has no such case. Conversely, the neighbouring tier, "partially correct", includes "partial claim support" (Methods) — a real publication cited for a claim it only partly supports can fall inside the review's major-inaccuracy misattribution clause ("a real publication cited for a claim or topic it does not cover where the study counts that as misattribution"). Major-type cases therefore sit on both sides of the tier boundary Pass A drew, and no printed count separates them.

**Settled values: blank on all three arms** (GPT-5.0 (Full Test); GPT-5.0 (Individual Question); Claude Sonnet 4.0 (Individual Question)). Pass A wrong on all three — it asserted an unstated identity (hallucination rate = critically wrong count) that the Abstract and Discussion contradict; Pass B right to leave the cells blank.

---

## 3. Linardon_2025 (R3629.xml) — GPT-4o, `n_bad_doi`: SETTLED BLANK; Pass A wrong

Review definition (form, fixed definitions): "Bad DOI: a DOI that does not resolve, or a DOI that resolves to a different paper. Denominator is references that carry a DOI." Form field 35 extracts, as printed, a "DOI does not resolve count" and a "DOI resolves to a different paper count".

**What the paper prints.** The 51 that Pass A entered is Table 1's DOI *error* row for real citations: Total column "51/135 (37.8)", with Table 1 footnote b: "Error type was only relevant for actual references." The Results text ("Citation Errors") states the same numerator over the other denominator: "Combined, the highest error rate was observed for DOIs for journal articles (51/141, 36.2%)…" (Both passes flagged the 135-vs-141 denominator discrepancy; it is noted, not corrected.)

The Methods define what that row measures, verbatim:

> "We considered a citation to be genuine (not fabricated) if we could identify a real publication that closely matched both the title and the authors. In other words, inaccuracies in the citation were permitted if the cited work could be reliably traced to an actual source. For example, a GPT-4o citation that listed the correct authors and title but included an incorrect volume number, page range, or DOI was still considered a real (nonfabricated) source. For these nonfabricated sources, we then compared the GPT-4o citation to the actual citation and recorded whether there were any discrepancies and errors in the author list, year, title, journal, volume, issue, page range, and DOI."

**Ruling.** The paper prints no count of DOIs that do not resolve or resolve to a different paper for this arm, and 51 is not such a count:

1. **Different measurement.** The 51 is a bibliographic *discrepancy* count: the cited DOI string differed from the actual citation's DOI, recorded by comparison against the identified source. The paper nowhere reports resolution-testing these 51 DOIs, and nowhere splits them into does-not-resolve vs resolves-to-a-different-paper. A discrepancy against the true DOI and a resolution failure are not the same event under the form (a cited DOI can differ from the version-of-record DOI yet still resolve to the same publication, e.g. an alternate/earlier DOI for the same article), so rule 2 exactness fails: the study quantity is not the review quantity.
2. **Wrong coverage and denominator in any case.** The 51 covers *real (nonfabricated) citations only* (Table 1 footnote b; denominator 135 DOI-providing real citations in the table, 141 real citations in the text). The review's bad-DOI count runs over references that carry a DOI in the arm as a whole. The fabricated stratum is excluded from the 51 — and it is precisely there that the paper *does* print resolution-described DOI counts, verbatim (Results, "Fabrication Rates"): "When GPT-4o provided a DOI for a fabricated citation, 64% (21/33) of the DOIs were valid but linked to irrelevant and unrelated journal articles, whereas 36% (12/33) were completely invalid or nonfunctional." Those 21 + 12 are a different, partial quantity (fabricated citations only) and are not what Pass A extracted; and no printed total combines the two strata in resolution terms, so no exact arm-level bad-DOI count can be assembled from what is printed (rule 5 cannot rescue it: the real-stratum part is not printed in resolution terms at all).

**Settled value: blank** (`n_bad_doi` is not a pooled outcome; this settles the cell for the record, as tasked). Pass A wrong — it renamed a printed "DOI error" count as a bad-DOI count; Pass B right, for the reason its note gives.

---

## 4. Seifi_2026 (R0053_v2.xml) — `n_minor_error`, three arms: SETTLED 25 / 13 / 7; Pass B wrong

**Definitions and denominator, verbatim.** Methods (Hallucination Scale; also Figure 1 legend):

> "score 0 = fully accurate; 1 = minor error/citation inaccuracy (typo in author, title, volume, or page); 2 = major error/citation inaccuracy (wrong title, author, journal, or year); 3 = completely fabricated."

> "Throughout this article, 'hallucination' is used as the umbrella term for any citation with a score greater than or equal to 1." … "'fabrication' was reserved for references that could not be verified in PubMed, CrossRef, Google Scholar, or via DOI resolution and therefore did not exist as complete bibliographic entities."

Score 1 matches the review's minor error exactly in substance (a typo-level error in one field; the source is the same publication, retrievable and correctly credited in the main) — neither pass disputed the definition; the dispute is only about derivation. Denominator: 300 references = "10 topics × 3 models × 10 references", i.e. **100 per model**.

**What is printed per model — percentages only, no score-1 percentage and no score-1 count anywhere.** Results, "Model-Level Performance", verbatim:

> "DeepSeek demonstrated the lowest hallucination rate (23%; fabrication 8%), followed by GPT (69%; fabrication 27%) and Grok (73%; fabrication 50%). High-severity citation inaccuracies (score ≥ 2) occurred in 10% of DeepSeek outputs, 44% of GPT outputs, and 66% of Grok outputs (Table 1)."

Table 1's pooled rows repeat the any-hallucination rates (69 / 23 / 73) and fabrication rates (27 / 8 / 50). Printed pooled counts (Abstract and Results agree): "Of 300 references evaluated, 165 (55.0%) contained a verifiable citation inaccuracy (hallucination rate) and 85 (28.3%) corresponded to no existing publication (fabrication rate)."

**Classification of Pass A's counts.** Pass A's minor counts are **not printed**, and they are **not singly derived**: each is a difference of two rule-6 derived counts — (score ≥ 1 count) minus (score ≥ 2 count) — i.e. doubly derived in form, exactly as Pass B described. Pass B left the cells blank on that ground alone.

**Ruling — the values stand.** Rule 6 bars a derivation only where it carries *rounding doubt*: "derive the count only if the percentage and denominator give a whole number without rounding doubt. A derived count with rounding doubt is recorded as not extractable." Here there is no rounding doubt at either step, and none can arise:

- Every input is a whole-number percentage at a stated denominator of exactly 100, where a percentage and a count are the same number (69% of 100 = 69, with no interval of possible counts). Each threshold count (score ≥ 1: 69 / 23 / 73; score ≥ 2: 44 / 10 / 66) is therefore exact, not estimated.
- The scores are a partition of the same 100 references per arm, and score 1 is by construction the set difference (≥ 1) minus (≥ 2) over that identical denominator. Subtracting two exact counts over the same denominator yields an exact count: GPT-5.3: 69 − 44 = **25**; DeepSeek-V3: 23 − 10 = **13**; Grok-4: 73 − 66 = **7**.
- The results reconcile exactly against every printed pooled figure, which closes any residual doubt: minor total 25 + 13 + 7 = 45; total score ≥ 2 = 44 + 10 + 66 = 120, and printed any-hallucination total 165 − 120 = 45 ✓; per-arm partitions sum to the denominator (GPT-5.3: 31 fully accurate + 25 minor + 44 score ≥ 2 = 100; DeepSeek-V3: 77 + 13 + 10 = 100; Grok-4: 27 + 7 + 66 = 100); fabrication total 27 + 8 + 50 = 85 = printed 85 ✓.

Consistency note: a blanket "no subtraction of derived counts" rule would also invalidate this study's `n_fully_accurate` values, which **both** passes derived by subtraction at the same denominator (100 − any-hallucination count: 31 / 77 / 27) and which are not in dispute. The form contains no such blanket rule; its only derivation test is rounding doubt, and Pass B's objection does not survive it.

**Settled values: GPT-5.3 = 25; DeepSeek-V3 = 13; Grok-4 = 7** (derived, working shown above; denominator 100 per arm). Pass B wrong; Pass A right.

---

## 5. Singh_2026 (R0180_v2.xml) — GPT-5, `n_fully_accurate`: SETTLED BLANK; Pass A wrong

**What the paper prints.** Denominator for all reference outcomes is the validated subsample of 88 responses (44 correct + 44 incorrect answers, from 203 questions). Table 1 ("Reference reliability by answer correctness"): Total 88; Hallucinations 29; **Accurate citations 59**. Results, verbatim: "Across the subset of 88 responses, hallucinations (fabricated or misrepresented references) were observed in 29 cases (33%)."

The classification, verbatim (Methods, "Reference Validation"):

> "The first cited source for each answer was reviewed, and the claim made by GPT-5 was verified using PubMed, Google Scholar, and Google, with additional assistance from the hospital library to source textbooks when these were referenced. … If a reference could not be located on PubMed, on Google Scholar, or through librarian-assisted searches, it was deemed likely fabricated and documented as such. References were classified as misrepresented if they existed but either did not address the specific clinical topic cited or failed to directly support GPT-5's stated claim. If the reference was found and directly supported the claim made by GPT-5, it was classified as a supportive reference. For statistical analysis, fabricated and misrepresented references were collectively defined as hallucinations, while all others were considered accurate."

**Ruling.** The printed 59 is a count of *supportive* references — found, and directly supporting the claim. It is not a fully-accurate count under either review definition:

1. **Not strict.** Strict fully accurate requires accuracy "on all fields checked by the study", with any error in a checked field removing the reference (rule 7). This study checked no bibliographic field at all: its validation paragraph describes exactly two tests — could the source be located, and did it directly support the claim/topic. Authors, title, journal/source, year, volume, pages and DOI were never compared against the source record, so a citation with wrong authors, a garbled title or a wrong year counts among the 59 whenever the (intended) paper was found and supported the claim. The study's "accurate" label claims no field-level accuracy, and the count covers cases the strict definition excludes — broader than the review definition, so rules 2, 3 and 7 all bar the mapping.
2. **Not lenient either.** Lenient fully accurate requires a source that is "real, correctly credited, and retrievable despite a minor field error". The supportive count does not require correct crediting (crediting was never assessed) and places no minor-only limit on field errors (errors of any size in any bibliographic field are compatible with "supportive"). It therefore does not map to the lenient pool either. (Pass B's note makes exactly this argument from the v2 full text; it is confirmed here. Note the contrast with this study's major-inaccuracy cell, which is not in dispute: fabricated + misrepresented = 29 was settled by both passes as exact-by-sum, because the review's major definition expressly includes a real publication cited for a topic/claim it does not cover — the mirror image of why the residual "accurate" 59 fails: the review's fully-accurate definitions are field-based, and no fields were checked.)

**Settled value: blank.** Pass A wrong — it entered the paper's study-labelled "Accurate citations" total as review fully accurate; Pass B right.

---

## Caveats

1. All quotations are verbatim from the five XML full texts as provided, including the papers' own errors (e.g. Athaluri's "turned up on on an internet search"; Dhaimade's Results label "GPT-4.0 IQ" for the 105/328 arm). Internal discrepancies already flagged by one or both passes (Linardon Table 1 denominator 135 vs text 141; Dhaimade Table 5 n ~264 vs 262) are recorded, not corrected, and none of them changes a ruling above.
2. Dhaimade_2026 was settled from R2475.xml as provided. Its supplementary files (S1–S3 Text, S1–S2 Data) are present in the XML only as captions; if per-tier counts exist inside those files, they were outside the full text tasked for this settlement and outside both passes' extractions.
3. Seifi_2026 minor counts are derived, not printed; the derivation chain and the reconciliation checks are shown in full in §4 so the human author can verify them before the counts enter any pool, per the form's checking rule for derived/exact-by-sum mappings.
4. No number in this report was taken from the manuscript or the analysis files, which were not read.
