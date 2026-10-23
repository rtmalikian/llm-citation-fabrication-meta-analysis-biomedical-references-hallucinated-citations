# Extractor B — Batch 1 notes (Robustness Pass, 23 October 2026)

Independent pass. Extracted from full texts alone (tables first, then methods, then text), without reading any prior extraction, analysis, stage3/stage4 or manuscript-results files. One row per model arm (model × retrieval condition); prompt-group conditions that are not retrieval conditions were pooled as printed. Blank = not printed / not extractable, never zero, except where a printed zero is explicitly noted.

Output: `extraction-passB-batch1.csv` — 26 rows.

## Adıgüzel_2026 (R0045, _v2 XML) — 2 arms

- Arms pooled across the 3 prompt groups (A simple, B PubMed-constrained, C persona). Table 3 gives the score distribution per model only (n=150/model); no per-prompt-group distribution of scores 0/1/2 is printed, so prompt-group arms could not be extracted.
- Could not extract: n_major_inaccuracy (score 1 "partially accurate", n=111 ChatGPT / 30 Claude, is any-severity and broader than review major); n_minor_error (no minor-only count); DOI resolve-vs-different-paper split (only correct/incorrect printed).
- Derived counts: none. All counts copied from Table 3 / Table 4.
- Contradiction flagged: abstract/text DOI accuracy (output-level mean proportions: ChatGPT 35.3%, Claude 90.0%) implies ≈97 and ≈15 DOI errors at reference level, whereas Table 4 prints reference-level DOI errors of 94 (62.7%) and 14 (9.3%). The two are different aggregations (output-level means vs reference-level counts) but do not reconcile exactly; Table 4 counts were extracted.
- Arithmetic check: score distributions reproduce the printed mean scores (ChatGPT (111+76)/150=1.25; Claude (30+238)/150=1.79).
- Model year: GPT-5 = 2025 and Claude Sonnet 4.6 = 2026 are vendor release years, not stated in the paper (paper states only that models were evaluated via web interfaces in April 2026).

## Aljamaan_2024 (R5083) — 5 arms (+ Bard, no arm)

- Bard was challenged but "failed to generate any references" to all 10 prompts — no arm row (denominator of generated references = 0).
- Could not extract for every arm: n_fabricated, n_major_inaccuracy, n_fully_accurate, n_minor_error. The study reports only a Reference Hallucination Score (0–11) and per-identifier erroneous counts (Table 2). No per-reference fabricated/accurate counts exist anywhere in the paper.
- refs_generated: ChatGPT 100, SciSpace 100, Elicit 100 read as complete (100 requested, no failures reported for them in the per-arm n). Perplexity 95 and Bing 70 taken from Table 3's parenthetical n values (z-test df: 100, 95, 100, 100, 70). These sum to 465 = 500 requested across 5 chatbots − 35 ungenerated references (7%, printed in Results), which corroborates them. Working: 100+95+100+100+70 = 465; 500−465 = 35 ✓. Bing's "210 failures" in the text is identifier-level (30 ungenerated refs × 7 items = 210), consistent with 70 generated.
- Derived counts: none for outcomes. n_bad_doi is the printed Table 2 DOI erroneous count per chatbot; its printed definition includes missing DOIs, so it is broader than the review bad-DOI definition (denominator = DOI-carrying references).
- Verifier independence / number of verifiers: not reported in the paper.
- Model versions for Perplexity, SciSpace, Elicit, Bing: not stated. Retrieval coded from the nature of the tools (Perplexity and Bing = live search/browsing; SciSpace and Elicit = reference-database/citation tools); the paper does not use retrieval terminology, and all prompts instructed the chatbots to begin by searching PubMed.

## Athaluri_2023 (R0094) — 1 arm

- Could not extract: refs_requested (no fixed number requested — ChatGPT wrote protocols for 50 self-suggested topics); n_fully_accurate (never printed; the 109 "valid DOI" count is not a fully accurate count); n_major_inaccuracy (no major label or sum printed; the 69 invalid DOIs mix 41 existing articles with 28 fabricated); n_minor_error (none printed).
- n_fabricated = 28 recorded as printed, but flagged NOT EXACT: the study's hallucination call requires both no Google-search hit AND no existing DOI, which is narrower than the review definition (mapping rule 4).
- n_bad_doi = 69 (Table 3, "References with an invalid DOI"; text: DOI non-existent or belonging to a different article).
- Model version: not stated. The paper describes ChatGPT as using "the third-generation generative pre-trained transformer (GPT-3)"; model_year left blank rather than inferred.
- Funding: no funding statement found in the full text — recorded as Not reported. Conflicts: "The authors have declared that no competing interests exist."

## Bernstein_2026 (R0043, _v2 XML) — 1 arm

- Could not extract: refs_requested (prompts requested supporting references, no number specified); n_major_inaccuracy (no combined count; references with any error = 2,736−1,350 would include minor errors and is broader than major — not recorded); n_minor_error (no minor-only count); n_bad_doi (no DOI outcome — PMID was checked instead; PMID incorrect n=1,020 is not entered as a DOI count).
- n_fabricated = 195 flagged as slightly broader than the review definition: printed hallucination includes studies "not indexed in PubMed" and PMIDs not associated with a published study, not only nonexistent studies.
- n_fully_accurate = 1,350 maps exact to strict (all 7 checked elements must match the PubMed record).
- Note on design: 5 graders each ran all 70 prompts on separate accounts (350 responses); each grader scored only their own responses, so there is no duplicate verification of a shared citation set and no inter-rater statistic — recorded in verifier_independent/source notes.
- Retrieval: web search was available and could be invoked automatically; investigators did not control or observe its use and no browsing-disabled condition was run. Coded as browsing available/uncontrolled, not as a clean retrieval arm.

## Chelli_2024 (R2136) — 3 arms

- Could not extract for every arm: n_fully_accurate (non-hallucinated counts 84/85/9 are NOT fully accurate — bibliographic accuracy of non-hallucinated papers was reported separately in Figure 4, e.g. DOI accurate in only 13/82 and 17/84); n_major_inaccuracy and n_minor_error (no such counts); n_bad_doi (DOI accuracy printed only within the non-hallucinated subset, with denominators 82/84 that exclude hallucinated papers and missing DOIs — not a whole-arm count); refs_requested (two prompt versions, with and without a minimum number, were run and the version returning most papers was retained; no single requested number).
- n_fabricated records the printed "hallucination" counts (55/34/95), flagged NOT EXACT: printed definition = any 2 of title, first author, year wrong. A real paper with 2 wrong fields counts as hallucinated, and a nonexistent paper with fewer than 2 of these fields wrong does not.
- Contradictions flagged (not fixed):
  1. Results text: "Overall, 471 references were included in this study and analyzed." The per-model returns in Table 2 sum to 139+119+104 = 362, and all hallucination/precision denominators are 139/119/104. 471 is unexplained by any table (109 original-review papers + 362 = 471 is a possible reading, but the paper does not say this).
  2. GPT-4 recall: Abstract and Results text give 13.7% (15/109), while Table 3 gives True positive = 16 for GPT-4 (16/109 = 14.7%, and precision 16/119 = 13.4% as printed). One of the 15/16 figures is inconsistent.
  3. Bard hallucination rate printed as 91.4% (95/104) in Abstract/Results and 91.3% in Discussion for the same count.
- Funding: no funding statement in the full text — Not reported. Conflicts: first author is co-founder/shareholder of EasyMedStat (the statistics software used).

## Civelekler_2026 (R0125, PDF) — 4 arms

- Denominator problem (flagged, not fixed): all results are reported as n/35 per model (35 paragraphs). The prompt ("Please provide an AMA 11-style reference for sources relevant to the following clinical paragraph") does not state one reference per paragraph; the paper analyses the output as 35 citations per model.
- Could not extract: n_major_inaccuracy and n_minor_error (no severity counts printed in either phase).
- Phase mismatch (major internal contradiction): Phase 1 "correct citations" (DeepSeek 22, ChatGPT 18, Copilot 18, Gemini 5) do not reconcile with the expert validation phase, which was applied to "citations initially flagged as correct" yet reports fully + partially + not cited counts that exceed the Phase 1 correct counts — e.g. DeepSeek fully cited 15 + partially cited 12 + not cited 5 = 32 classifications against only 22 Phase 1-correct citations; Copilot fully cited is 7 against 18 Phase 1-correct. The expert fully-cited counts (DeepSeek 15/35, Copilot 7/35, ChatGPT 4/35, Gemini 4/35) are recorded here in the notes; the CSV n_fully_accurate uses the Phase 1 counts with mapping marked UNCLEAR (printed definition "verifiable and relevant" does not state all fields correct).
- Percentage contradictions (flagged): DeepSeek accuracy printed as 78.6% (22/35) — 22/35 = 62.9%, not 78.6%. Gemini printed as 12.9% (5/35) — 5/35 = 14.3%, not 12.9%. ChatGPT/Copilot 51.4% (18/35) is arithmetically correct.
- Category overlap (flagged): Phase 1 error categories are not mutually exclusive. Table 1 counts per model: DeepSeek DOI mismatches 8 + author/journal mistakes 2 + non-correct 13 = 23 error labels, plus 22 "correct" exceeds any single denominator; Gemini non-correct 31 + correct 5 = 36 > 35; ChatGPT non-correct 19 + correct 18 = 37 > 35. No sum mapping attempted.
- n_fabricated uses the printed "Non-Correct Publications (unrelated or unfindable)" counts (13/19/17/31), flagged broader than review fabricated because unrelated real references are included.
- n_bad_doi uses printed "DOI Mismatches (correct journal, wrong DOI)" counts (8/3/0/2). Copilot's 0 is a printed zero.
- Funding and conflicts: no statements anywhere in the PDF — Not reported for both.
- Model years: GPT-5.1 and DeepSeek-R1 coded 2025 (access period Nov–Dec 2025; release years from vendor records, not stated in the paper). Copilot 4.2 and Gemini Ultra 2.5 model_year left blank — no release year stated and the printed version names do not correspond to a dated release in the paper.

## Dhaimade_2026 (R2475) — 3 citation arms

- GPT-4.0 has NO citation arm: Abstract/Methods state only GPT-5.0 and Claude Sonnet 4.0 provided citations and that citation validity was tested only for those two. (GPT-4.0 FT/IQ answer-accuracy data exist but no citations — not extracted, eligibility is citation generation.)
- Could not extract for all 3 arms: n_fabricated, n_major_inaccuracy, n_fully_accurate, n_minor_error, n_bad_doi — all blank. The paper prints only a "hallucination rate" per arm (GPT-5.0 FT 51.53%, 135/262; GPT-5.0 IQ 32.01%, 105/328; Claude Sonnet 4.0 5.59%, 18/322) and never states which tier(s) of its three-tier taxonomy (completely valid / partially correct / critically wrong) the hallucination numerator counts. Per-tier counts appear only in a Figure 5 heatmap and supplementary files, not as printed numbers in text or tables. Recording any tier mapping would be a guess, so the rates are preserved verbatim in the CSV definitions_note instead.
- Contradiction flagged (not fixed): the Results sentence labels the 105/328 arm "GPT-4.0 IQ". This conflicts with the Methods (citation validity only for GPT-5.0 and Claude), the Abstract (citations only from GPT-5.0 and Claude), Table 5 (GPT-5.0 IQ n ≈ 328; GPT-5.0 FT n ≈ 264; Claude n ≈ 322) and the Figure 5 caption (arms = "5.0 FT, IQ5.0 IQ, and Claude Sonnet 4.0"). The row is filed under GPT-5.0 Individual Question as the only consistent reading, with the printed label quoted in the CSV note.
- refs_requested: blank — citations were requested per exam answer across 331 questions; no fixed number per answer is printed. refs_generated uses the denominators printed beside the hallucination rates (262/328/322); note the FT denominator is 262 in the Results sentence but ≈264 in Table 5.
- Verification was by a single evaluator (no duplicate verification, no inter-rater statistic — the paper lists this as a limitation).

## Gravel_2023 (R0210) — 1 arm

- refs_requested: blank — no number was requested ("Do you have references for this?"); answers contained 2–7 references, all were counted, but only the first 3 per answer entered the primary analysis (59 references). refs_generated = 59 (the analysed/verified denominator, as printed: "A total of 59 references were included in the primary analysis"). The total number generated across all 20 answers is not printed as a single count.
- n_major_inaccuracy = 46 is EXACT BY SUM (mapping rule 5): 41 fabricated + 5 real articles with major citation errors (Table footnote a: "wrong year, volume, and pages; or wrong authors") = 46. Parts are disjoint (fabricated vs real articles). Working shown here and in the CSV note.
- n_minor_error = 3 (Table footnote a: minor citation errors, volume and pages, among real articles).
- n_fully_accurate: blank. Of the 18 real references, 11 were real article titles (3 minor-error, 5 major-error, leaving 3 without citation error by subtraction — a derived-by-subtraction figure, not printed, so NOT recorded), and 7 were websites/books whose citation-element accuracy is never classified. No whole-arm fully accurate count is printed.
- Table-vs-text check: Table gives "Title found on Pubmed 11" and "Article found on the journal/website 8"; text explains 11 real article titles, of which the article itself was located for 8 — recorded in definitions via the text account; no outcome count depends on the 8.
- n_bad_doi: blank (no DOI outcome assessed).

## Güneş_2026 (R2956) — 6 arms

- Could not extract: n_major_inaccuracy (RAS bands 1–3 mix minor and major errors; no severity count printed); n_minor_error (none); n_bad_doi (no DOI outcome — PMID checked instead; PMID accuracy counts in Table 1 were not entered as DOI counts).
- Contradiction flagged (not fixed): Results text states "A total of 480 references were analyzed to compare the performance of the six LLMs", but Tables 1 and 2 are headed "Reference (n = 480)" per model and every Table 2 row sums to 480 per model (e.g. Claude 3.5 Sonnet 15+7+4+66+388 = 480). The design (120 questions × 4 references) also gives 480 per model, 2,880 in total. Per-model denominator 480 extracted, per the tables and design.
- Fully accurate mapping note: RAS 4 requires final score 36 = all 9 bibliographic elements correct AND verification score 4 (content entirely pertinent). It is therefore the printed fully accurate count but carries a pertinence condition beyond the review's bibliographic strict definition; flagged in the CSV note.
- Fabricated mapping note: the study's fabricated definition (not locatable in Medline, Google Scholar, DOAJ or web search) matches the review definition; the extracted counts are the printed Table 2 RAS 0 (fabrication) row. RAS 0 is a composite-score band (final score = 0), which in practice requires verification score 0 (fabricated/not indexed) or zero correct elements.
- Verifier: Radiologist 1 evaluated all references blinded to model identity; the other two radiologists had run the models. Single evaluator — coded "partially" for independence.
- Funding: no funding statement in the full text — Not reported. Conflicts: "The authors declared no conflicts of interest."

## Cross-cutting

- Derived counts: only two places involve any derivation, both flagged in the CSV: (1) Gravel n_major = 46 by exact-by-sum of two printed, disjoint counts (41 + 5); (2) Aljamaan refs_generated for Perplexity (95) and Bing (70) read from Table 3's printed n values, corroborated by the printed total of 35 ungenerated references. No percentages were back-calculated into counts anywhere. Where percentages and printed counts conflicted (Civelekler), the printed counts were extracted and the percentages flagged.
- model_year is a vendor-release year for every arm where one is coded; it is never stated in the primary papers except Chelli (Bard PaLM 2.0 release date given) — flagged here once for all rows. Where no reliable release year could be tied to the printed version (Athaluri ChatGPT, Aljamaan Perplexity/SciSpace/Elicit/Bing, Civelekler Copilot 4.2 and Gemini Ultra 2.5), model_year is blank.
- topic_type uses the protocol §3.6 call: established for long-standing clinical topics with settled literatures; mixed where a study spans many unrelated fields/topics (Athaluri, Gravel).
