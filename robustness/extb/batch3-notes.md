# Extractor B, batch 3 — notes (robustness pass, 23 October 2026)

Independent pass. Extracted from full texts alone (tables/outcome sections first, per Extractor B prompt). No extraction.csv, analysis files, stage3/stage4 files, or manuscript results were opened.

Output: `extraction-passB-batch3.csv` — 21 rows: Sawamura_2024 1, Seifi_2026 3, Shi_2026 7, Singh_2026 1, Tas_2026 3, UçarGündoğar_2026 2, Uçar_2026 3, Yin_2026 1 (audit).

## Sawamura_2024 (R6708, XML) — 1 arm
- Extracted: n_fabricated 15/37 as printed ("fictional paper" = not found after searching by title, PMIDs or DOIs — exact match to completely fabricated).
- Not extracted: n_major_inaccuracy (no major category; real-but-misinterpreted references described narratively, no count); n_fully_accurate (only PMID/DOI concordance 7/37 printed — identifier concordance, not all-fields accuracy, mapping not exact); n_minor_error, n_bad_doi (not reported); refs_requested (no number of references per question was prespecified; 15 clinical questions).
- Contradictions flagged (not fixed): per-section counts sum to 38 (16+11+11) vs overall denominators printed as 37; Table 2 prints internal-disorders fictitious rate as 36.7% (4/11) although 4/11 = 36.4%.
- Model version: only "ChatGPT (free version)" printed (data collected 3 April 2023); version number not stated, model_year left blank.

## Seifi_2026 (R0053_v2, XML) — 3 arms, 100 refs each
- Per-model results are printed ONLY as percentages at a printed denominator of 100 per model (10 topics × 10 references; "each model generated 10 references per topic, yielding 300 references").
- DERIVED counts (mapping rule 6, flagged DERIVED in definitions_note; all whole numbers, no rounding doubt):
  - Fabricated (score 3): GPT-5.3 27% × 100 = 27; DeepSeek-V3 8% × 100 = 8 (text confirms "its eight fabricated references"); Grok-4 50% × 100 = 50. Sum 85 = printed overall 85/300.
  - Major inaccuracy (score ≥2, exact by sum of score 2 + score 3): GPT-5.3 44; DeepSeek-V3 10; Grok-4 66.
  - Fully accurate (score 0, strict): GPT-5.3 100 − 69 = 31; DeepSeek-V3 100 − 23 = 77; Grok-4 100 − 73 = 27. Hallucinated total 69+23+73 = 165 = printed overall 165/300.
- Not extracted: n_minor_error (score-1 counts never printed separately; would require subtracting two percentage-derived counts — double derivation, refused); n_bad_doi (identifier-omission analysis printed, but no per-model bad-DOI count).
- Funding: no funding statement found in the full text — recorded "not reported". Conflicts: authors disclosed no potential conflicts of interest.
- model_year blank for GPT-5.3 and Grok-4 (release year not stated in paper); DeepSeek-V3 recorded 2024 (vendor release record).

## Shi_2026 (R5289, PDF, medRxiv preprint) — 7 system-configuration arms
- Table 3 gives complete printed counts per system (References / Verified / Warning / Failed / Corrupted). n_fabricated = Failed + Corrupted (exact by sum; the study's own hallucination numerator): Army pipeline 2/49, AI Scientist 3/43, Army single 5/64, Baseline GPT-4 8/68, AI-Researcher 23/79, Data-to-Paper 31/83, Agent Laboratory 36/97. n_fully_accurate = Verified (strict: confirmed by CrossRef/PubMed with consistent metadata; any discrepancy moves a reference out of Verified).
- Not extracted (all arms): n_major_inaccuracy (Warning category mixes field discrepancies of unstated severity — cannot form a major total exactly); n_minor_error and n_bad_doi (not reported); refs_requested (manuscript-generation task from a results package; no reference count was requested).
- CONTRADICTION flagged for every arm (not fixed): printed hallucination rates in Table 3 do not equal (Failed+Corrupted)/References from the same row (e.g., Army pipeline printed 2.9% vs 2/49 = 4.1%; Data-to-Paper printed 33.3% vs 31/83 = 37.3%). Rates may be unreported per-task means; the paper does not say. Counts were extracted as printed; printed rates were not used.
- Underlying LLM versions for the five multi-agent systems are not stated (only the Baseline is GPT-4); model_family coded unclear for those arms. The Army (pipeline) arm's citation verification/repair pipeline is coded as reference-database access in retrieval; all other arms none.

## Singh_2026 (R0180_v2, XML) — 1 arm (GPT-5)
- Denominator decision: 203 OITE questions × 1 reference = 203 generated; only an 88-response subsample (44 correct, 44 incorrect) was verified, so refs_generated = 88 (verified denominator, Table 1) with refs_requested = 203 and the split explained in definitions_note.
- Extracted: n_major_inaccuracy_incl_fabricated = 29/88 (exact by sum: study "hallucination" = fabricated + misrepresented, where misrepresented = real paper not addressing the topic / not supporting the claim, which the review major definition expressly includes).
- Not extracted: n_fabricated (fabricated vs misrepresented split never printed — only the combined 29); n_fully_accurate (printed "accurate" 59/88 requires only existence + direct support of the claim; bibliographic fields were not checked, so it maps to neither strict nor lenient — mapping not exact); n_minor_error, n_bad_doi (not reported).
- Retrieval: no retrieval/browsing condition stated — coded unclear.

## Tas_2026 (R3715, XML) — 3 arms, 1,050 refs each (3,150 total)
- ALL outcome counts blank = not extractable: the paper reports only Reference Hallucination Score (RHS) means (total 0–11 plus four subscales) in Tables 2–6. No fabricated/inaccurate/accurate counts and no percentages are printed, so no count can be extracted or derived under rule 6. This is the study's central extraction problem: a mean-score-only report.
- Model versions: expressly not trackable from the free-tier web interfaces (paper states this), so model_version "not stated" and model_year blank for all three arms. Retrieval coded unclear for all arms (no retrieval condition stated; Perplexity's search-grounded design is not stated in the paper and was not assumed).
- Verification: single investigator against PubMed/Google Scholar (95% intra-rater re-score agreement) — verifier_independent coded "not independent (single investigator…)".

## UçarGündoğar_2026 (R3820, XML) — 2 arms
- Extracted (Table 6, counts printed): ChatGPT-4o n_fabricated 61/114 (53 real); DeepSeek R1 n_fabricated 98/149 (51 real). "Fake = fabricated or unverifiable references not retrievable from scientific databases" — exact match to completely fabricated.
- Not extracted: n_fully_accurate ("real" = existence verified via PubMed/Google Scholar/Web of Science only; field accuracy of real references not checked — maps to neither strict nor lenient); n_major_inaccuracy (no severity split among real references, so a major total cannot be formed exactly); n_minor_error, n_bad_doi (not reported); refs_requested (references volunteered across 20 questions × 3 sessions; no number requested).
- Verifier independence: two reviewers verified independently, but one (DS) also generated prompts/collected data — coded "partly involved". Retrieval condition not stated — unclear.

## Uçar_2026 (R2250, XML, rosacea) — 3 arms
- Denominators printed (Methods 3.3): 298 references total — Claude Sonnet 4.5: 43; ChatGPT-5.2: 152; DeepSeek-V3.2: 103.
- ALL outcome counts blank = not extractable from the main full text: per-model hallucinated counts/percentages are never printed; only per-question ranges (ChatGPT-5.2 18.2%–50.0%; DeepSeek-V3.2 10.0%–58.3%). The "hallucinated" definition (no corresponding publication could be identified) would map exactly to completely fabricated if a count existed. Per-reference data are in Supplementary Materials, which were not part of the retrieved full text. n_major/n_minor also blank (the "inaccurate" category is severity-unsplit and also uncounted in the main text); n_fully_accurate and n_bad_doi not reported.
- CONTRADICTION flagged (Claude arm): "Of the six questions with cited references, one exhibited hallucination (12.5%)" — 1/6 = 16.7%, not 12.5% (which implies denominator 8); neither reconciles with the printed total of 43 Claude references. No count extracted from this sentence.
- Retrieval: expressly "web search or external retrieval functions were not enabled" — coded none for all arms. Verifier independence for the reference check: not reported (single designated expert per domain; dermatologist blinded for response scoring).

## Yin_2026 (R6358, PDF, Research Square preprint) — AUDIT STRATUM, 1 row
- eligibility = include_audit; every generation outcome cell left blank by design; no model arm.
- Audit values recorded in definitions_note: corpus = arXiv (1,465,145 papers; 44,107,529 citations) + bioRxiv (261,928; 21,183,111) + SSRN (421,698; 26,815,043) + PubMed Central 10% sample (374,807; 19,245,787), Jan 2020–Aug 2025; headline as printed "111 million references across 2.5 million papers" (per-corpus figures sum to 2,523,578 papers / 111,351,470 references). Detection: non-existent titles matched against an Elasticsearch index from Semantic Scholar + OpenAlex, GPT-4o-mini cleaning, Google Scholar API final check; "hallucinated" = estimated excess of unmatched citations above the pre-LLM baseline (regression estimate, not individual classification). Headline count as printed: conservative estimate of 146,932 hallucinated citations in 2025 alone; rates as of Aug 2025: arXiv 0.39%, bioRxiv 0.21%, SSRN 1.91%, PMC 0.27%; papers containing ≥1 hallucinated reference rose 2–23 percentage points across datasets (no single pooled paper-level count printed).
- Funding: no funding statement in the preprint text — "not reported". Conflicts: "There is NO Competing Interest" (Additional Declarations). Country recorded "USA; China" (Cornell/UC Berkeley/UCLA affiliations plus one Tsinghua co-affiliation).
