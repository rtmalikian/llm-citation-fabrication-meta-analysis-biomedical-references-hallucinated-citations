# Extraction notes — Extractor A, Batch 3 (NEW included studies, Robustness Pass, 23 Oct 2026)

Extractor A worked independently from the full texts in `robustness/fulltexts2/` only. Output: `extraction-newA-batch3.csv` — 12 arm rows for 8 records, exact 25-column schema. All rows `eligibility = include_generation`. Mapping follows extraction-form.md rules 1–8: extract as printed; a study category maps to a review outcome only if definitions match exactly; percentages at a stated denominator converted only where they give whole counts with no rounding doubt, flagged DERIVED; blanks mean not extractable, never zero.

Conventions used across the batch: `model_year` is the vendor release year of the named version (GPT-3.5/ChatGPT-3.5 = 2022; GPT-4 = 2023; PaLM 2 = 2023), left blank where the platform's version/year is not identifiable from the paper (scite Assistant). `verifier_independent` = yes only where verification was by reviewers independent of generation; no where the study authors who prompted the model also verified; not reported where the paper does not say who verified.

---

## R6775 — Awosanya_2024 (Curr Osteoporos Rep 2024; DOI 10.1007/s11914-023-00855-x)

ChatGPT 4.0 used to draft review articles on COVID-19 and musculoskeletal health. Two arms extracted.

**AI-only arm (extractable).** 113 AI-cited references in the initial draft (Results text; Table 3). Printed breakdown: 19 (16.8%) "did not exist"; 31 (27.4%) existed but incorrect (authors, journal name, article title, publication year, volume/issue, page numbers, or DOIs); 30 (26.6%) misattributed (legitimate reference, text not reflective of it); total incorrect 80 (70.8%); correct 33.
- n_fabricated = 19 — EXACT. "Did not exist" matches review completely fabricated.
- n_fully_accurate = 33 — EXACT (strict). The three incorrect categories exhaustively cover nonexistence, any bibliographic field error, and misattribution, so "correct" requires existence + all checked fields correct + correct attribution.
- Major NOT mapped: 80 cannot be used. The 31 bibliographic-error references carry no severity split — a wrong page number or year can be a minor error under the review definition — so 80 is broader than review major inaccuracy.
- Verification source: none named in the paper (fact-checking by all co-authors); recorded as not reported. Verifiers = co-authors who wrote the queries → not independent.
- Funding (full, for the record): Hampton Roads Biomedical Research Consortium Collaboration Accelerator Fund; NIH F31AG077931, AR065971, UM1TR004402; VA Merit BX006399, RX003552; Indiana CTSI / Indiana Center for Musculoskeletal Health. Conflict: co-author Melissa Kacena is Editor-in-Chief of the journal.

**AI-assisted arm (no outcome extractable).** 89 AI-cited references; 71 correct, 18 (20.2%) incorrect "due to either the reference not matching what was stated in the associated text or plagiarism" (Results; Table 3).
- References were human-selected and supplied to ChatGPT (via the AskYourPDF plugin), so the model did not generate the bibliography: no fabricated count exists.
- The 18 incorrect mix misattribution with plagiarism; plagiarism is not a review outcome and the split is not given → major not mapped.
- 71 "correct" means only not-misattributed / not plagiarised; bibliographic accuracy was not the model's output and was not tested → fully accurate mapping unclear (rule 7), left blank.

## R6851 — Choi_2023 (BMC Med Educ 2023; DOI 10.1186/s12909-023-04832-x)

Single author, South Korea (Chungbuk National University). ChatGPT powered by GPT-3.5 (versions of 28–29 Jan 2023) answering 312 pharmacology MCQs; references were requested only in prompts 3–4 (156 MCQs), yielding **274 references** (Results, "References"; Table 4).

**No reference-level outcome was extractable**, despite the abstract headline "incorrect citations for 69.7% (191/274)":
- The 191 is Table 4 error type A only: "Reference URLs linked to a wrong page or a '404 page not available'". A URL-only criterion is *narrower* than review major inaccuracy (rule 4 — it cannot see title/author/journal errors in references whose URL happened to resolve) and it inseparably mixes nonexistent targets with links to a *different* real page, so it is neither major inaccuracy nor fabricated.
- The other error counts sit on incompatible denominators and cannot be combined into a reference-level count: authors not found 59/350 *authors*; incorrect titles 148/152 *titled items*.
- No fully accurate count is printed (274 − 191 = 83 would be "URL not wrong", not accuracy). n_bad_doi blank: URLs include PubMed/PMC links, not DOIs specifically.
- Verification: URLs followed; authors searched on PubMed, Amazon (books) and Google. Single-author evaluation → verifier not independent. Funding listed as N/A; no competing interests declared.

## R6938 — Citir_2025 (BMC Oral Health 2025; DOI 10.1186/s12903-025-05479-4)

Turkey (Tokat Gaziosmanpasa University). ChatGPT-3.5 (queried 16 Oct 2023) answering 20 oral-cancer FAQs. **81 references** in the answers: 13 scientific articles, 10 "fake", the remainder website data (Abstract; Results; Discussion).

**No outcome extractable.** The 10 "fake" do **not** map to review completely fabricated: the printed definition (Methods, "Assessment of response") is "References with a 'page not found' error or links to advertising pages were considered fake" — a dead-link/ad-link test, not a test that no matching publication exists. A real paper can sit behind a broken link and a fabricated citation can carry a resolving link, so coverage differs from the review definition in both directions. The denominator also mixes articles with website sources. Verification was a manual search in the Microsoft Edge browser plus iThenticate similarity checking; all phases of the research were performed by the single author → not independent. No funding; no competing interests. (Answer-quality Likert scores are not reference outcomes and were not extracted.)

## R7018 — Woodrow_2025 (Arch Bone Jt Surg 2025; DOI 10.22038/ABJS.2024.80093.3669)

USA (Massachusetts General Hospital / Harvard). Two AI systems each wrote two review papers (ankle osteoarthritis; calcaneus fractures): ChatGPT-4 with the ScholarAI plugin, and Assistant by scite. Study authors (initially blinded) graded every citation true/false against published literature and UpToDate. A citation counted accurate only if it (1) referenced a previously published journal paper and (2) the paper contained the cited information; claims missing a required citation were graded incorrect (Methods, "Review Process").

**No outcome extractable for either arm.** Table 2 prints only citation-accuracy *percentages* with incorrect-citation and missing-citation counts — no denominator (number of citations per paper) is printed anywhere:
- ChatGPT: osteoarthritis 90% accurate, 3 incorrect, 4 missing; calcaneus 69.23%, 8 incorrect, 8 missing.
- scite Assistant: osteoarthritis 35.14%, 24 incorrect, 26 missing; calcaneus 39.68%, 38 incorrect, 12 missing.

Definitions also block mapping even if denominators were known: "accurate" checks existence + content support only — bibliographic fields (authors/title/journal/year/DOI) were never checked, so it is not review fully accurate (strict); "incorrect" lumps nonexistent citations with real papers that do not support the claim.

**DERIVED figures (for author check only — NOT entered in the CSV, because the denominators themselves are derived, not stated, so rule 6 is not met):** solving each percentage against its incorrect count gives whole-number citation totals with no rounding doubt — ChatGPT osteoarthritis 27/30 correct, calcaneus 18/26; scite osteoarthritis 13/37, calcaneus 25/63 — i.e. combined ChatGPT 45/56 citations correct, scite 38/100. The Discussion adds that the Assistant's citations "all referenced authentic scientific papers" (its errors were tangential/misattributed content), which would make its incorrect counts candidates for major inaccuracy (misattribution) *if* the author accepts the derived denominators. No funding; no conflicts declared.

## R7279 — Ghanem_2024 (JBJS Open Access 2024; DOI 10.2106/JBJS.OA.24.00099)

USA (Johns Hopkins). ChatGPT-4 generated **30 references** supporting the ABCDE trauma protocol (5 categories × 6). Two independent reviewers graded each against PubMed (Table 1 scale): 0 = nonexistent; 1 = inaccurate ("providing false or incomplete information and requiring substantial modification"); 2 = accurate ("requiring no modification").

**All three mapped counts are DERIVED** from the printed percentages at the stated denominator of 30 (Abstract; Results) — each gives a whole count with no rounding doubt, and they sum to 30:
- n_fabricated = 4 — grade 0, 13.3% × 30. EXACT definition (nonexistent vs PubMed).
- n_fully_accurate = 13 — grade 2, 43.3% × 30. EXACT (strict: no modification required).
- n_major_inaccuracy_incl_fabricated = 17 — EXACT BY SUM: grade 0 (4) + grade 1 (13, 43.3% × 30); also printed directly as 56.7% "false". Grade 1 required *substantial* modification, so no minor-error contamination; minor count therefore not reported (blank, not zero).
- Cross-check: counting the per-reference mean scores in Table 2 gives exactly four references scored 0, consistent with 4 nonexistent.
- Flag (paper's own inconsistency, extraction unaffected): the Discussion calls the whole 56.7% "false" group "fabricated citations (56.7%)", contradicting the Abstract/Results split (43.3% inaccurate + 13.3% nonexistent). The Abstract/Results grading was extracted.
- No funding, no financial relationships or conflicts disclosed. Verifiers independent (two independent reviewers; Cohen's kappa used).

## R7335 — Schwartzman_2025 (Adv Orthop 2025; DOI 10.1155/aort/5534704)

USA. ChatGPT-3.5 (queried 2 Nov 2023, prompted to use only peer-reviewed literature) answered 17 preoperative TKA and 16 THA questions, citing **109 sources** (TKA 56, THA 53 — one arm, one row; topics combined).

- n_fully_accurate = 39 — EXACT (strict). Methods: each source was queried on PubMed, Scopus, Cochrane and Google Scholar, and "Sources were only deemed accurate if all information provided by ChatGPT matched" (authors, title, journal name, year of publication, DOI). Split as printed: TKA 14/56, THA 25/53.
- Fabricated and major NOT mapped. The complement (70; printed as 64.22% inaccurate in the Conclusion) is glossed in the Discussion as sources "not able to be traced back to an existing publication", which would make it fabricated — but that gloss contradicts the Methods rule, under which a traceable paper with any single mismatched field is also "not accurate", and the Discussion itself lists this as possible process (ii) ("correctly utilizing the peer-reviewed literature but unable to appropriately report all relevant information including authors, publication date, and DOI"). Because the 70 inseparably mix nonexistent sources with real sources carrying field errors of unstated severity, it maps to neither fabricated nor major inaccuracy. This internal contradiction is flagged for the author rather than resolved by the extractor.
- Duplicates note: 39 accurate includes duplicates; 32 *unique* accurate sources were carried into the characterisation tables. The pooled denominator stays 109 / numerator 39 as printed.
- Verifiers were the (unblinded) study authors → not independent. No funding; no conflicts declared.

## R7442 — Aiumtrakul_2023 (J Pers Med 2023; DOI 10.3390/jpm13101457)

USA (Mayo Clinic, Rochester MN; University of Hawaii). Three chatbots, each prompted on 1 Aug 2023 for 20 Vancouver-style references on each of the same 12 nephrology topics (refs_requested = 240 per arm). Category definitions (Methods 2.1) are the cleanest in this batch: *incomplete* = information inadequate to verify existence; *fabricated* = "could not find the reference in the database"; *inaccurate* = identified in the database but ≥1 of 5 components (author, title, journal, year/issue, DOI) incorrect; *accurate* = identified and all 5 components correct. Verification: DOI search in PubMed first, then Google Scholar / Web of Science (library website / Google for books).

Per arm (Table 1; Results):
- **ChatGPT-3.5** (GPT-4.0 was tried and excluded — it returned only example references): 240 requested → 199 unique (41 duplicates). Accurate 76, inaccurate 82, fabricated 32, incomplete 9. n_fabricated = 32 EXACT; n_fully_accurate = 76 EXACT (strict).
- **Bing Chat (GPT-4.0)**: 240 → 158 unique (65 duplicates, 17 absent). Accurate 47, inaccurate 77, fabricated 21, incomplete 13. n_fabricated = 21; n_fully_accurate = 47. Retrieval recorded as platform-inherent browsing/live search — the paper does not separately state a retrieval condition, flagged here as an extractor judgement.
- **Bard AI (PaLM 2)**: 240 → 112 unique (39 duplicates, 89 absent). Accurate 3, inaccurate 26, fabricated 71, incomplete 12. n_fabricated = 71; n_fully_accurate = 3. Retrieval not stated in the paper → recorded as unclear (platform default).

Not mapped, all arms:
- Major: "inaccurate" requires only one wrong component with no severity split — a single wrong year/issue can be minor under the review definition — so fabricated + inaccurate would overstate major inaccuracy.
- Bad DOI: Table 2 counts refs *with an inaccurate DOI among the inaccurate refs only* (ChatGPT 74/82; Bing 68/77; Bard 18/26) and components overlap within a reference (ChatGPT component counts sum to 120 > 82). The schema denominator (references carrying a DOI) is never printed, so n_bad_doi is blank.
- Who verified is not reported → verifier_independent = not reported. No external funding; no conflicts declared.

## R7837 — Suppadungsuk_2023 (J Clin Med 2023; DOI 10.3390/jcm12175550)

USA (Mayo Clinic). ChatGPT-3.5 (03/23 version) prompted ("Please provide the references in Vancouver style and their links in recent literature on…") on the same 12 nephrology topics; no number of references was requested (refs_requested blank). **610 references** returned. Six components recorded per reference (authors, title, journal, year, DOI, link); verification via DOI in PubMed, then Google Scholar, then Web of Science (Methods 2.1). Categories (Methods 2.2; Results; Table 1): existed 378 (62%) = existence with all correct 122 + existence with partial correct 256; fabricated 192 (31%); incomplete 40 (7%).

- n_fully_accurate = 122 — EXACT (strict): "authentic" required all six components correct.
- n_fabricated NOT mapped — the batch's clearest rule-4 case. The printed definition requires *all* citation elements to be forged/non-existent before a reference counts as fabricated. A citation combining a real title with wrong authors therefore lands in "existing, partial correct" here, while the review definition counts it as completely fabricated (no single publication matches the citation as given). The study's 192 is thus *narrower* than the review outcome and cannot be pooled as fabricated.
- Major NOT mapped: partial-correct (256) mixes single-component errors of very different severity — inaccurate link 68% and inaccurate DOI 54% (percentages only, denominators unstated, so no bad-DOI count either) alongside author 3% and title 0.3% — with no split that isolates major errors; incomplete (40) is a separate non-outcome category.
- Who verified is not reported → not reported. No external funding; no conflicts declared.

## Judgement: R7442 vs R7837 — same study reported twice?

**No — two distinct (companion) studies, extracted separately on each paper's own numbers. They are not a duplicate report of one dataset.**

Evidence they are closely related:
- Overlapping senior team (Suppadungsuk, Thongprayoon, Krisanapan, Miao, Cheungpasitporn appear in both; R7837 is first-authored by Suppadungsuk, R7442 by Aiumtrakul with a partly different author set), same institution (Mayo Clinic Division of Nephrology and Hypertension).
- **Identical IRB approval in both papers: Mayo Clinic IRB 23-005661, 30 June 2023.**
- Same 12 nephrology topics, same Vancouver-style prompt family, same verification databases (PubMed → Google Scholar → Web of Science), same model (ChatGPT-3.5).

Evidence they are different experiments with different data:
- Different designs: R7837 tests ChatGPT alone with an open-ended "recent literature" prompt and no requested count, obtaining 610 references (≈50/topic); R7442 requests exactly 20 references × 12 topics from **three** chatbots (data collection dated 1 Aug 2023) and analyses deduplicated uniques (ChatGPT 199).
- Different measurement: R7837 scores **6** components including links, with categories existed/fabricated/incomplete and all-correct vs partial-correct; R7442 scores **5** components (no links) with accurate/inaccurate/fabricated/incomplete. Even the shared label "fabricated" is defined differently (all-elements-forged in R7837 vs not-found-in-database in R7442).
- Materially different results for the shared ChatGPT-3.5 arm: fabricated 31% (192/610) in R7837 vs 16.1% (32/199) in R7442; fully accurate/authentic 20% (122/610) vs 38.2% (76/199). One dataset re-reported could not produce both sets of numbers.

Residual caveat for the author: because the team, protocol and IRB are shared and both were run in mid-2023, partial overlap of prompts/sessions cannot be excluded from the published texts alone; if the review team wants to be conservative about non-independence, that is a sensitivity-analysis decision — it does not change extraction, and neither paper should be dropped as a duplicate on the published evidence.

## Batch summary

| Record | Arms | Pooled counts entered |
|---|---|---|
| R6775 Awosanya_2024 | 2 | AI-only: fabricated 19, fully accurate 33 (of 113). AI-assisted: none |
| R6851 Choi_2023 | 1 | None (URL-only error criterion) |
| R6938 Citir_2025 | 1 | None ("fake" = dead/ad link) |
| R7018 Woodrow_2025 | 2 | None (percentages only, denominators unprinted; derived totals flagged in notes) |
| R7279 Ghanem_2024 | 1 | Fabricated 4, major 17, fully accurate 13 (of 30) — all DERIVED from % at stated n=30 |
| R7335 Schwartzman_2025 | 1 | Fully accurate 39 (of 109) |
| R7442 Aiumtrakul_2023 | 3 | Fabricated 32/21/71; fully accurate 76/47/3 (ChatGPT/Bing/Bard) |
| R7837 Suppadungsuk_2023 | 1 | Fully accurate 122 (of 610); fabricated deliberately NOT pooled (narrower definition) |

Model years are vendor release years (see conventions above). No record in this batch reported a minor-error count or a bad-DOI count on the schema denominator (references carrying a DOI), so `n_minor_error` and `n_bad_doi` are blank on every row.
