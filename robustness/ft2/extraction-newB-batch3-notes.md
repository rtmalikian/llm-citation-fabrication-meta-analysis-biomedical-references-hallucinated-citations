# Extraction notes — Extractor B, batch 3 (NEW included studies, robustness pass, 23 Oct 2026)

Output file: `extraction-newB-batch3.csv` — 12 rows (one per model arm), 25 columns, schema as specified.
Worked independently from the full texts only; extraction.csv / pass A–B files / Extractor A outputs were not read.
All rows are `include_generation`. Blanks mean not extractable / not mappable under mapping rules 1–8, never zero.

---

## R6775 — Awosanya_2024 (Curr Osteoporos Rep 2024; ChatGPT-4 writing review articles on COVID-19 and musculoskeletal health, USA)

Two arms.

**AI-only arm** (113 AI-cited references in the abandoned first draft):
- Extractable: n_fabricated = **19** ("did not exist", 16.8%); n_fully_accurate = **33** ("Correct AI-cited references", Table 3 — the complement of incorrect, where incorrect covered nonexistence, wrong authors/journal/title/year/volume/issue/pages/DOI, and misattribution, so "correct" is a strict all-checked-fields pass).
- Not mapped: major inaccuracy. The paper prints a total incorrect of 80 (19 fabricated + 31 existed-but-incorrect on a bibliographic field + 30 misattributed). The 31 field-error references are not split by severity (a wrong page number alone could be a minor error), so no exact major count can be formed (rule 3).

**AI-assisted arm** (89 AI-cited references; human-selected references supplied to ChatGPT-4 via the AskYourPDF plugin — coded as document set supplied):
- Nothing mapped. No fabricated count (the model was given the references; the paper explicitly notes it "was not given the opportunity to fabricate references" — but no zero count is printed, so the cell is blank, not 0).
- The only error count, 18/89 (20.2%) "incorrect", mixes references not matching the associated text with **plagiarism**, which is not a reference-accuracy outcome; the complementary 71 "correct" (Table 3) was not field-checked, so it does not map to fully accurate either.

Verification source not reported (extensive co-author fact-checking, no database named); verifiers were the co-authors (not independent).

## R6851 — Choi_2023 (BMC Med Educ 2023; ChatGPT/GPT-3.5 answering Korean pharmacology MCQs, South Korea)

One arm, 274 references generated (prompts 3 and 4 of 156 MCQs; no number of references was requested per prompt, so refs_requested is blank).
**No outcome count is extractable** — the row is returned with all outcome cells blank:
- Reference errors are reported only by component, with three different denominators: URLs linked to an irrelevant or nonexistent site 191/274; authors not found on PubMed/Amazon/Google 59/350 authors; incorrect titles 148/152 titles given.
- The abstract's "incorrect citations for 69.7% (191/274)" is, per Table 4, the URL-error count only. A wrong/nonexistent URL is not the review's fabricated, major, or bad-DOI outcome (these were URLs, not DOIs, and a URL pointing to an irrelevant page does not establish that no matching publication exists).
- Overlap between the component errors is not given, so no fully accurate count can be derived either.

## R6938 — Citir_2025 (BMC Oral Health 2025; ChatGPT-3.5 answering 20 oral-cancer FAQs, Turkey)

One arm, 81 references cited in the answers.
**No outcome count is extractable** — row returned with all outcome cells blank:
- Printed split: only 13 of 81 references were scientific articles, 10 were "fake", the remainder were website data.
- "Fake" was defined operationally as a reference whose link gave a "page not found" error or led to an advertising page (manual search in Microsoft Edge). That link-based definition is narrower than and not equivalent to the review definition of completely fabricated (no matching publication exists on title/source identity), so the 10 does not map (rule 4). The denominator also mixes website references with articles.
- No field-checked accurate/major/minor/DOI counts are printed. (The 80 Likert ratings in the abstract are ratings of 20 answers by 4 specialists, not references.)

## R7018 — Woodrow_2025 (Arch Bone Jt Surg 2025; AI-written vs human review papers, foot & ankle orthopaedics, USA)

Two arms (ChatGPT-4 + ScholarAI plugin; Assistant by scite). Each model wrote two papers (ankle osteoarthritis; calcaneus fractures). Per the arm definition (model × retrieval condition), the two papers per model are summed into one arm row; the per-paper figures reconcile exactly, shown below.

**Derivation (flagged as derived in the CSV):** Table 2 prints, per paper, citation accuracy % and the number of incorrect citations. These recover each paper's citation denominator with no rounding doubt:
- ChatGPT osteoarthritis: 90% accurate, 3 incorrect → 27/30. ChatGPT calcaneus: 69.23%, 8 incorrect → 18/26. **Arm total: 56 generated, 11 incorrect.**
- Assistant osteoarthritis: 35.14%, 24 incorrect → 13/37. Assistant calcaneus: 39.68%, 38 incorrect → 25/63. **Arm total: 100 generated, 62 incorrect.**

Mapped: n_major_inaccuracy_incl_fabricated = incorrect citations (11 and 62). A citation counted as accurate only if it (1) referenced a previously published journal paper and (2) contained the factually correct information from that paper, so an incorrect citation is either nonexistent or misattributed — both inside the review major definition.
Not mapped:
- n_fabricated: no fabricated-only count. For the Assistant arm the Discussion states all its citations referenced authentic papers (errors were tangential/misattributed content), but that is a narrative statement, not a printed count, so the cell is blank rather than 0.
- n_fully_accurate: the derived "correct" counts (45 and 38) do not map to strict — bibliographic fields (authors/journal/year/volume/pages/DOI) were never checked, only existence + content support (rule 7).
- "Missing citations" (ChatGPT 4+8; Assistant 26+12 statements needing but lacking a citation) are not references and are excluded from all denominators.

## R7279 — Ghanem_2024 (JBJS Open Access 2024; ChatGPT-4 references for the ABCDE trauma protocol, USA)

One arm; refs_requested = refs_generated = 30 (6 per category × 5 categories, requested explicitly).
Clean three-way grading by two independent reviewers against PubMed/Google Scholar/Cochrane/Embase/Scopus (κ = 0.89):
- n_fabricated = **4** (score 0, "nonexistent": title, authors, journal and year matched no existing reference and the publication could not be found in any of the five sources) — maps exact.
- n_major_inaccuracy_incl_fabricated = **17** (13 inaccurate, score 1 — false or incomplete information *requiring substantial modification*: missing author, wrong year/title/volume/pages/PMID — plus 4 nonexistent) — exact by sum.
- n_fully_accurate = **13** (score 2, "accurate", satisfactory in line with PubMed, no clarification required) — strict.
- No minor or DOI-specific count (wrong PMID sits inside the inaccurate category).

## R7335 — Schwartzman_2025 (Adv Orthop 2025; ChatGPT-3.5 sources for TKA/THA patient questions, USA)

One arm, 109 sources (56 TKA + 53 THA; no number requested per question).
- n_fully_accurate = **39** — maps exact to strict: a source was deemed accurate only if present on PubMed, Scopus, Cochrane or Google Scholar **and** all information provided matched (authors, title, journal name, year of publication, DOI). (14/56 TKA, 25/53 THA; the 39 include 7 duplicates — the paper's own denominator is all 109 cited sources, and extraction follows the paper.)
- Fabricated and major NOT mapped: the complementary 70 "inaccurate" sources are glossed in the Discussion as "not able to be traced back to an existing publication", but the Methods definition also fails a source for any single field mismatch, and the Discussion itself offers "correctly utilizing the peer-reviewed literature but unable to appropriately report authors, publication date, and DOI" as one mechanism. So 70 is broader than fabricated and broader than major; no fabricated-only count is printed (rule 3).

## R7442 — Aiumtrakul_2023 (J Pers Med 2023; ChatGPT-3.5, Bing Chat, Bard providing nephrology references, USA/Thailand)

Three arms. All counts are for **unique** references: 240 were requested per chatbot (20 per topic × 12 nephrology topics) and duplicates/absent responses were removed before analysis (ChatGPT 199, Bing 158, Bard 112 analysed). Category definitions (Methods 2.1): *fabricated* = could not be found in the databases (PubMed, Google Scholar, Web of Science; library/Google for books); *inaccurate* = existing but at least one of five components (author, title, journal, year/issue, DOI) incorrect; *accurate* = existing with all five components correct; *incomplete* = information inadequate to verify existence.

Per arm (accurate / inaccurate / fabricated / incomplete):
- **ChatGPT-3.5** (GPT-4.0 was tried first but "was unable to provide actual references", so only GPT-3.5 data exist): 76 / 82 / 32 / 9.
- **Bing Chat (GPT-4)**, coded retrieval = browsing/live search (Bing Chat): 47 / 77 / 21 / 13.
- **Bard AI (PaLM 2)**, retrieval not stated in the paper: 3 / 26 / 71 / 12.

Mapped per arm: n_fabricated (fabricated count) and n_fully_accurate (accurate count — all five checked components correct, strict).
Not mapped per arm:
- Major inaccuracy: fabricated + inaccurate would include existing references with a single incorrect component of unstated severity (e.g. one wrong field on an otherwise real, findable reference), which is broader than the review major definition (rule 3).
- Bad DOI: Table 2 counts inaccurate DOIs only *among the inaccurate references* (ChatGPT 74/82; Bing 68/77; Bard 18/26), not among all references carrying a DOI, so no arm-level bad-DOI count exists.
- Incomplete references map to no outcome.
- Bing Chat model_year left blank: the paper does not date Bing Chat itself (its GPT-4 base is not a version statement for the arm).

## R7837 — Suppadungsuk_2023 (J Clin Med 2023; ChatGPT-3.5 (03/23 version) identifying nephrology literature, USA/Thailand)

One arm, 610 references across the same 12 nephrology topics (no number specified in the prompt — "provide the references in Vancouver style and their links in recent literature on [topic]" — so refs_requested is blank; all results provided were taken, no deduplication step is reported).
Mutually exclusive split (Table 1, overall row; sums check: 40 + 192 + 122 + 256 = 610):
- n_fabricated = **192** (31%). Caveat recorded in the CSV: the Study Outcomes sentence defining fabrication ("fabricated or non-existent if all citation elements were forged or non-existent, respectively") is garbled, but operationally the fabricated category is the complement of the 378 references that existed (and of the 40 incomplete), i.e. references that did not exist — it maps to completely fabricated.
- n_fully_accurate = **122** ("existence with all correct" / "authentic": all six components — authors, title, journal, year, DOI, link — correct) — strict.
- Major NOT mapped: "existence with partial correct" (256) covers any single inaccurate component, dominated by incorrect links (68% of the 378 existing references) — links are not a review major-inaccuracy element, and single-field errors of unstated severity are included (rule 3).
- Bad DOI not entered: an inaccurate-DOI count of 206 is printed, but only against the 378 existing references (54%), not against references carrying a DOI.

## Judgement on the R7442 / R7837 relationship — same study reported twice?

**No — two separate data collections by the same team, not the same study reported twice. Both were extracted in full, on each paper's own numbers.**

Evidence they are related companion studies:
- Same research group (Mayo Clinic Division of Nephrology and Hypertension, with Mahidol/Thammasat co-authors): Suppadungsuk, Thongprayoon, Krisanapan, Miao and Cheungpasitporn appear on both papers.
- Same Mayo Clinic IRB number (23-005661, 30 June 2023) on both papers.
- Same 12 nephrology topics, same verification databases (PubMed, Google Scholar, Web of Science), near-identical category schemes (fabricated / incomplete / accurate vs inaccurate or partial-correct).

Evidence they are distinct studies with distinct data:
- Different scope: R7837 tests ChatGPT-3.5 only; R7442 compares ChatGPT-3.5, Bing Chat and Bard (and reports discarding GPT-4.0 for ChatGPT because it would not provide actual references).
- Different prompts: R7442 specified **20 references per topic** in Vancouver style (with per-chatbot prompt variants, run 1 August 2023); R7837 specified no number and additionally required **links**, and assessed six components (link included) against R7442's five.
- Different samples and irreconcilable numbers for the shared ChatGPT-3.5 condition: R7837 collected 610 references with 192 fabricated (31%) and 122 fully correct (20%); R7442 requested 240, analysed 199 unique after deduplication, with 32 fabricated (16.1%) and 76 accurate (38.2%). These cannot be the same reference set re-analysed — the denominators, fabrication rates and accuracy rates all differ in ways deduplication cannot explain (removing 41 duplicates from a 610-style set would not produce 199, and R7442's requested total was only 240 to begin with).
- Different journals and submission dates (R7837: J Clin Med, received 29 Jun 2023; R7442: J Pers Med, received Aug/Sep 2023).

Flag for the synthesis stage (not an extraction decision): because the same team ran near-identical protocols on the same 12 topics with the same model family within weeks of each other, the two ChatGPT-3.5 arms are **not fully independent evidence** in the way arms from unrelated groups would be; if the review team wants a sensitivity analysis, these two study_ids (Aiumtrakul_2023 ChatGPT arm; Suppadungsuk_2023) are the pair to examine. That concern does not change either paper's extracted counts.

---

### Cross-batch consistency notes
- Where a paper's "inaccurate/incorrect" category mixed minor field errors with major ones (R6775 AI-only total incorrect, R7335, R7442, R7837), major was left blank rather than approximated, per rules 3–4.
- Component-level error counts that could not form a review outcome (R6851 URL/title/author errors; R7442/R7837 DOI-error counts on restricted denominators) are documented above and in the CSV notes instead of being forced into n_bad_doi or n_minor_error.
- No study in this batch reported a separable minor-error count, so n_minor_error is blank on all 12 rows; no study reported a bad-DOI count on a "references carrying a DOI" denominator, so n_bad_doi is blank on all 12 rows.
