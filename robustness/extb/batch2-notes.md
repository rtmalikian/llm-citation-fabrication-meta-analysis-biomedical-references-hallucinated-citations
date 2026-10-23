# Extractor B — Batch 2 notes (Robustness Pass, 23 October 2026)

Independent pass, from full texts alone. Tables/outcome sections read first, methods second, per the Extractor B prompt in prompts.md. One row per model arm under one retrieval condition. Blank = not extractable as printed, never zero. `model_year` is blank on every row: no paper in this batch states a release year for the version tested (testing dates are given instead and are recorded in the definitions notes); a year was not supplied from outside the paper.

## Hasnain_2025 (R3074) — 2 arms (ChatGPT, DeepSeek)

- Extracted: refs requested 30 per arm (single prompt asking for 30 references); ChatGPT generated 15, DeepSeek 30; fake references 2 per arm (Table 3).
- Could not extract:
  - `n_major_inaccuracy_incl_fabricated` — the §3.5 hallucination-rate numerator is "fake or inaccurate" combined, and the inaccurate part is never counted (the text only mentions, without counts, incomplete author lists and incorrect issue/volume numbers for ChatGPT).
  - `n_fully_accurate` — no accurate count printed for either arm; deriving 15−2 or 30−2 would ignore the uncounted extra errors.
  - `n_minor_error`, `n_bad_doi` — no minor-error category; DOI not assessed.
  - `model_version` — not stated for either model in the citation experiment (versions appear only in cited literature about other tasks).
  - `verifier_independent` — annotators are mentioned ("human evaluations") but not identified.
- Contradiction found: Results text after Table 3 states "Based on the titles, DeepSeek provided 30 correct references", which contradicts Table 3 (2 of DeepSeek's 30 references are fake, so at most 28 could be correct). The same paragraph notes duplicate titles in the DeepSeek list. Flagged, not fixed; Table 3 counts were extracted.

## Hueber_2023 (R0712) — 1 arm (ChatGPT, version not stated)

- Extracted: one arm aggregating the 4 literature requests reported in the text (same model, same condition): generated 4 + 10 + 6 + 5 = 25; fabricated 4 + 2 + 5 + 5 = 16. Per-request figures are printed in sentences, not a table: eosinophilic fasciitis/ruxolitinib 4 references that "cannot be found"; prodromal RA 2 of 10 false; Kleyer-specific request 5 of 6 fictitious; JAK-inhibition risks 5 of 5 completely fabricated.
- Could not extract:
  - `n_fully_accurate`, `n_major_inaccuracy_incl_fabricated`, `n_minor_error`, `n_bad_doi` — the paper reports only false vs not false per request; the non-false references were not assessed field by field, so 16 is a floor for major inaccuracy, not a printed total.
  - `refs_requested` — no number of references was specified in the requests.
  - `verification_source` — verification is described only as an "independent literature search"; no database is named for the check (PubMed/Scopus/Web of Science are named only inside the chatbot's own false claim, not as the authors' method).
  - `model_version` — not stated; ChatGPT-4 is mentioned as also producing false citations but with no counts, so no second arm exists to extract.

## Jędrzejczak_2024 (R1232, medRxiv preprint) — 2 arms (ChatGPT-4, Gemini Advanced)

- Extracted from Table 2 (preprint p.5), summing the 3 printed sessions per arm. All sub-rows reconcile: accurate + wrong-DOI + partial-missing + partial-false-information + false = total, for both arms.
  - ChatGPT-4: 76+81+74 = 231 generated; accurate 86 (all correct 46 + DOI not given 40); false 17; wrong DOI 10; partial missing 67; partial false information 51; major (exact by sum) 10+51+17 = 78; minor 67.
  - Gemini Advanced: 65+68+60 = 193; accurate 26 (7 + 19); false 30; wrong DOI 1; partial missing 33; partial false information 103; major 1+103+30 = 134; minor 33.
- Could not extract: `refs_requested` (prompt specifies no number); `verifier_independent` (who verified, and whether verification was duplicated/blinded, is not stated); funding and conflicts (no statements in the preprint).
- Overlap flag for the author: this preprint is the earlier report of the same experiment that Pastucha_2026 (also in this batch) later published in extended form — the ChatGPT-4 and Gemini arms here have identical session counts to the ChatGPT-4 and Gemini 1.5 Pro arms in Pastucha_2026 Table 4. Both were extracted as instructed; the duplicate-report overlap needs a decision at synthesis, not at extraction.

## Kutluay_2026 (R0436, PDF) — 1 arm (ChatGPT-5.3, web search enabled)

- Extracted: 45 requested (3 per topic × 15 topics) and 45 generated; fully accurate 11 (score 2/2, exact strict); unverifiable 15 (score 0/2) mapped to fabricated with the caution recorded in the CSV — the printed 0/2 category also covers real non-article sources (books/guidelines) and inaccessible sources, so it is broader than pure non-existence and the mapping is not exact.
- Could not extract:
  - `n_major_inaccuracy_incl_fabricated` and `n_minor_error` — the 19 references scoring 1/2 ("existed but contained a clear error in the PMID, year, journal, title, author information, or other bibliographic details") are not split by severity; some are plainly major (a PMID belonging to a completely different article) but no split is printed.
  - `n_bad_doi` — DOI was not assessed; PMID was used as the identifier.
- Contradictions/oddities flagged (not fixed):
  - Abstract: "The overall bibliographic accuracy rate was 11 (45.6%)" conflates the fully-accurate count (11) with the normalised score rate (41/90 = 45.6%, explained in the Results/Table 3). The 24.4% proportion of fully accurate references is the consistent figure.
  - Discussion reports a descriptive comparison as "9 of 32 versus 16 of 42" for topic categories with/without the reused review article; those denominators are score fractions, not reference counts, and cannot be reconciled with the 45 references as counts.
  - Retrieval caveat in the paper's own words: web search was enabled, but "the recorded output did not indicate whether retrieval was actually invoked for this response".
  - Redundancy: the 45 references are only 36 unique sources; one review article accounts for 8 of the 11 fully accurate references. Primary analysis (per generated reference) was extracted, as in the other studies; the unique-source sensitivity figures (4 fully accurate of 36) are not a separate arm.

## Linardon_2025 (R3629) — 1 arm (GPT-4o)

- Extracted: 176 generated; fabricated 35 (exact: no identifiable source after the stated multi-database search; genuine required a close match on both title and authors); fully accurate 77 (exact strict: no errors in any checked field, DOI included). The printed accurate rate's denominator is the 141 real citations (Table 1, footnote a), not the 176 generated; the count 77 is what is extracted.
- Could not extract:
  - `n_major_inaccuracy_incl_fabricated` and `n_minor_error` — the 64 real citations with errors are reported only by error field (author, year, title, journal, volume, issue, page, DOI), never split into major vs minor, and field errors overlap within a citation, so no severity total can be formed.
  - `n_bad_doi` — the DOI error row (51) counts DOI field errors among real citations, not a printed "does not resolve / resolves to a different paper" count; fabricated citations carried a further 33 DOIs (21 valid but linked to unrelated articles, 12 invalid) already inside the fabricated count. No single printed bad-DOI total exists.
  - `refs_requested` — the prompt asked for at least 20 citations per review across 6 reviews (a minimum of 120), which is not an exact requested total.
  - Funding — not stated in the article.
- Contradiction found: Table 1 gives the combined DOI error rate as 51/135 (37.8%), while the Citation Errors text gives the same count as 51/141 (36.2%). Flagged, not fixed.

## Metze_2024 (R0570) — 1 arm (ChatGPT-4)

- Derived counts (mapping rule 6 — the paper prints only percentages against a stated total of 260; each percentage gives one unambiguous whole number):
  - Fully accurate ("Correct"): 11.54% × 260 = 30.004 → 30. Check: 30/260 = 11.538% → rounds to 11.54%; neighbouring counts give 11.15% (29) and 11.92% (31), so 30 is unique.
  - Minor ("With incorrect data but possibility of recovering the publication"): 13.85% × 260 = 36.01 → 36. Check: 36/260 = 13.846% → 13.85%; 35 → 13.46%, 37 → 14.23%, so 36 is unique.
  - Fabricated ("Hallucinations"): 74.62% × 260 = 194.012 → 194. Check: 194/260 = 74.615% → 74.62%; 193 → 74.23%, 195 → 75.00%, so 194 is unique.
  - Partition check: 30 + 36 + 194 = 260. ✓ Major inaccuracy = 194 (hallucinations only; the incorrect-but-recoverable category is minor by the review definition, since the publication can be recovered).
- Could not extract: `n_bad_doi` (DOI not assessed); `refs_requested` (prompt asked for "at least five references" per professor per day; no total requested is printed — 60 sketches were released over 10 days for 19 professors, of whom only 8 were ever recognised, and the 260 references cover only recognised professors).
- No internal contradictions found; Table 1's per-professor "Retrieved references" row (40+35+25+35+10+25+40+50) sums to the same 260.

## Mugaanyi_2024 (R0391) — 1 arm (ChatGPT GPT-3.5), natural sciences subset only

- Subset extracted, as instructed: natural sciences (clinical/biomedical topics), n = 55 generated. Humanities counts (n = 47) were not extracted. The 5 natural-science topics are listed only in Multimedia Appendix 1, which is not part of the full text supplied, so `topic_type` is coded unclear and `specialty` as mixed biomedical.
- Extracted: fabricated 15, derived by subtraction from printed counts (55 generated − 40 "Citation exists"); bad DOI 34 (printed "DOI hallucination", defined as a DOI that did not exist or was matched to a different source).
- Could not extract:
  - `n_fully_accurate` — "Citation accurate" (37/55) was assessed "irrespective of the corresponding DOIs", so it can include citations whose DOI was hallucinated; it does not map to strict fully accurate, and the fields checked for citation accuracy are not stated.
  - `n_major_inaccuracy_incl_fabricated` and `n_minor_error` — no severity partition is printed, and the overlap between the 34 DOI hallucinations and the citation-level categories is not given, so no sum is exact.
  - `refs_requested` — the prompt (write a manuscript introduction in APA style, including the DOI of each reference) specifies no number.
- Contradictions found:
  - Abstract reports the humanities DOI hallucination as "(42/55, 89.4%)" — the denominator should be 47 (42/47 = 89.4%; 42/55 = 76.4%). Table 2 itself gives 42 (89.4%) under the humanities column (n = 47). This affects only the unextracted humanities subset but is flagged as printed.
  - Abstract describes the 18/55 vs 4/47 contrast as a difference in "accuracy between the two disciplines"; in Table 2 those are the DOI-accurate counts, while citation accuracy (37/55 vs 29/47) is explicitly non-significant. Flagged, not fixed.
  - Internal tension (noted, not resolved): DOI exists 39 + DOI hallucination 34 exceeds 55 if read as disjoint sets, and DOI accurate (18) + DOI hallucination (34) = 52, leaving 3 citations unaccounted for (presumably carrying no DOI). The paper does not state the DOI-carrier denominator, which is why bad DOI is extracted as the printed hallucination count only.

## Nieves-Lopez_2026 (R1103) — 3 arms (ChatGPT-5.4, Gemini-3, Copilot)

- Extracted per arm from the Results text and Table 5; partitions reconcile (real + fabricated = total for each arm):
  - ChatGPT-5.4: 703 total, 542 real (= fully accurate, strict: all parts accurately named, including authors, title, journal, year and website link), 161 fabricated (129 partial + 32 complete).
  - Gemini-3: 796 total, 668 real, 128 fabricated (117 partial + 11 complete).
  - Copilot: 929 total, 903 real, 26 fabricated (0 partial + 26 complete).
  - `n_fabricated` = complete count; `n_major_inaccuracy_incl_fabricated` = complete + partial (every partial has an incorrect, non-compatible or non-existent identity component).
- Could not extract:
  - `n_minor_error` — partial fabrication is not a minor-error category and no minor count exists.
  - `n_bad_doi` — DOI not assessed (a website link forms part of the "real" definition, but no link/DOI error counts are printed).
  - `refs_requested` — references were volunteered or obtained with a follow-up prompt that specifies no number.
  - `verification_source` and `verifier_independent` — the paper never names the external source(s) used to judge references real or fabricated, nor who classified them. This is the batch's largest reporting gap: eligibility-relevant verification detail is simply absent from the full text.
  - `retrieval` coded unclear for all 3 arms: the paper does not state whether browsing/search was on or off for any model.
  - `model_version` for Copilot — not stated beyond the product name.
- No internal contradictions found in the reference counts (means in Table 4 are consistent with the totals in the text).

## Pastucha_2026 (R0696) — 6 arms (ChatGPT-4; ChatGPT-4.1; ChatGPT-4.1-web; Gemini 1.5 Pro; Gemini 2.5 Pro; Gemini 2.5 Pro-web)

- Retrieval vs no-retrieval conditions are separate arms, as instructed (Table 2 testing schedule; Table 4 counts). All counts summed across the 3 printed sessions per arm. Cross-checks: session sub-rows reconcile within every arm (accurate + wrong-DOI + partial-missing + partial-false-information + false = number of references), and the six arm totals sum to 231+396+296+193+530+301 = 1,947, matching the paper's stated total of 1,947 references.
  - ChatGPT-4 (no browsing, Jul 2024): 231; accurate 86; false 17; wrong DOI 10; partial missing 67; partial false info 51; major 78; minor 67.
  - ChatGPT-4.1 (no browsing, Jun 2025): 396; accurate 81; false 82; wrong DOI 13; partial missing 37; partial false info 183; major 278; minor 37.
  - ChatGPT-4.1-web (browsing, Jun 2025): 296; accurate 152; false 7; wrong DOI 11; partial missing 34; partial false info 92; major 110; minor 34.
  - Gemini 1.5 Pro (no browsing, Jul 2024): 193; accurate 26; false 30; wrong DOI 1; partial missing 33; partial false info 103; major 134; minor 33.
  - Gemini 2.5 Pro (no browsing, Jun 2025): 530; accurate 159; false 103; wrong DOI 10; partial missing 15; partial false info 243; major 356; minor 15.
  - Gemini 2.5 Pro-web (browsing, Jun 2025): 301; accurate 124; false 4; wrong DOI 0 (printed as 0 in all three sessions — extracted as a printed zero, not left blank); partial missing 134; partial false info 39; major 43; minor 134.
- Mapping note: "fully accurate" here is the paper's printed accurate row, whose definition allows a missing DOI ("all the correct information (except perhaps a missing DOI)"); the stricter "All correct" sub-row is smaller (e.g. 46 of the 86 for ChatGPT-4) and is recorded in the CSV definitions notes so the author can re-cut if the strict definition is enforced.
- Could not extract: `refs_requested` (prompt specifies no number of references); `verifier_independent` (verifiers, duplicate checking and blinding not stated).
- Inconsistencies flagged (not fixed):
  - Model naming varies inside the paper: "ChatGPT 4.0" (Table 2), "ChatGPT-4" (Table 4), "ChatGPT-4.0" and "oldest version of ChatGPT (ie, ChatGPT-4.0)" in text. Extracted as printed in Table 4 ("4").
  - Abstract states ChatGPT-4.1 with web search "achieved the best accuracy, with a score of 51%" and Gemini 2.5 Pro was "second at 41%" — 51% matches the pooled Table 4 accurate proportion for ChatGPT-4.1-web (152/296 = 51.4%), but 41% matches Gemini 2.5 Pro-WEB (124/301 = 41.2%), not the non-web Gemini 2.5 Pro named in the sentence (159/530 = 30.0%). Flagged as a probable arm-labelling slip in the abstract.
  - Overlap with Jędrzejczak_2024: see the note under that study — the ChatGPT-4 and Gemini 1.5 Pro arms here are the journal version of the preprint's experiment.
