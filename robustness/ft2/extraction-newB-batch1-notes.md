# Extractor B — batch 1 (NEW included studies, robustness pass, 23 Oct 2026)

Independent extraction. I did not read extraction.csv, extraction-passA/B.csv, any Extractor A output, or any analysis file.
Output: `robustness/ft2/extraction-newB-batch1.csv` — 25 data rows (one per model arm), exact 25-column schema.
Records: R0047, R0112, R0186, R0264, R0277, R11480, R2196, R2282 (all XML full texts in `robustness/fulltexts2/`).
All rows carry eligibility = include_generation. Blanks mean not extractable / not mapped under mapping rules 1–8 — never zero.

## Per-study notes

### R0047 — Di Febo_2026 (Eur Heart J Digit Health 2026), cardiology literature-search tools, France/Italy/Switzerland
- 6 rows: 5 main-analysis tools (ChatGPT-5, Elicit, Consensus, Scite, PubMed) + 1 separate row for the ChatGPT-5 clinical-studies subanalysis. PubMed is a conventional database comparator, not an LLM — included as a study arm and labelled as such in model_family.
- Main analysis (≤10 references per condition): refs_generated per tool from Table 2 (154/140/158/113/105; total 670). Text states no hallucinated citations for any tool and only minor, correctable discrepancies (titles, DOIs, author names) with sources reliably located → n_fabricated = 0 and n_major = 0 for all 5. No minor-error count and no fully-accurate count is printed (the headline 90% etc. are relevance rates, not bibliographic accuracy) → those fields blank.
- refs_requested is DERIVED and flagged in definitions_note: 10 per query × 4 topics × 4 prompts = 160 per AI tool; 120 for PubMed (3 Boolean queries/topic).
- Subanalysis row: 10 hallucinated (17%), 9 in topic C, 1 in topic D, all beyond the 11th reference. Denominator 59 is DERIVED and flagged: 25 articles shared with human SLRs + 34 ChatGPT-5-only = 59; 10/59 = 16.9% ≈ printed 17%. n_major set = n_fabricated (no other major category reported for the subanalysis).
- Hallucinated definition (exact): citations that could not be traced to any identifiable source after DOI and title searches = fully fabricated. Minor discrepancies where the intended source could be reliably identified were explicitly NOT classified as hallucinations.
- Funding: None. Conflicts: None declared. Citation verification by the investigators (independence not reported); the 3 electrophysiology experts were blinded for relevance rating, not for citation verification.

### R0112 — McLaughlin_2026 (Neurosurg Pract 2026), spine surgery, USA
- 5 rows from Table 3 (total / Score-2 accurate / Score-0 fabricated): ChatGPT 5.0 98/55/11; Gemini 2.5 Flash 65/15/17; Claude Sonnet 4.5 100/78/11; Microsoft Copilot (version not stated) 98/31/13; OpenEvidence 2.7.12 120/120/0.
- Mapping: fabricated exact (Score 0 = could not be verified to exist in any available database or web search). Fully accurate exact/strict (Score 2 = real verifiable peer-reviewed article, all metadata correct). Major and minor BLANK: Score 1 (misrepresented) mixes any metadata error (major or minor) with non-peer-reviewed website citations, so Score 0+1 is broader than review major inaccuracy.
- n_bad_doi blank: Table 4 reports incorrect DOI only as a % of misrepresented citations (ChatGPT 56.3% of 32; Gemini 39.4% of 33; Claude 9.1% of 11; Copilot 20.4% of 54; OpenEvidence 0) — wrong denominator for the review bad-DOI outcome (references carrying a DOI).
- All models had internet search enabled, standard web interfaces, queried Oct 2025; prompts requested 3–5 references × 20 prompts, so no single printed total requested → refs_requested blank. Verification: 3 independent medical student reviewers, 95.4% agreement, κ = 0.918. Funding: none. Conflicts: none.

### R0186 — McCavitt_2026 (JBJS Open Access 2026), hip fracture / AAOS CPG, USA
- 1 row, ChatGPT-4o mini (model_year 2024 as stated in the paper: release 18 July 2024). refs_generated = 2,556 (228 responses).
- ALL outcome counts blank — deliberate, per mapping rules: (a) "fabricated" is defined as a reference not indexed in PubMed, which is broader than the review definition (a real, non-PubMed-indexed publication counts as fabricated); the printed figure is also only a percentage (7.9%), and 7.9% × 2,556 is not a whole number, so no derived count under rule 6. (b) "Inaccuracies" = any discrepancy in title/authors/journal/year/pages/volume/PMID among PubMed-indexed references — includes minor errors, so no exact major count. (c) No fully accurate citation count is printed; the 76.3% "accurate" figure rates the response recommendations against the CPG, not citations, and the 1.1% CPG overlap is not fully accurate.
- ARITHMETIC FLAG (flagged, not corrected): Table III's mean fabricated references per response (0.59) and mean total references per response (7.53) imply ≈1,717 total references over 228 responses, inconsistent with the printed total of 2,556 (≈11.2/response). The 7.9% figure is internally consistent with the per-response means (0.59/7.53 ≈ 7.8%) but not with the 2,556 total.
- Verifiers were the same 4 medical student graders who submitted the prompts → verifier_independent = No. Funding not stated; conflicts not stated in the full text (disclosure forms are with the online version only).

### R0264 — Knee_2025 (Cureus 2025), midshaft clavicle fractures, Australia
- 1 row, ChatGPT-4o mini, prompted 31 Aug 2024 ×3 with 14 questions. refs_generated = 128 (printed).
- Counts are percentages only in the paper; conversions give whole counts with no rounding doubt and are flagged DERIVED in definitions_note: fabricated 88.3% → 113 (could not be located at all in MEDLINE/Embase/Scopus — exact); correct 0.8% → 1 (located, no inaccuracies in checked fields title/authors/date/journal); incorrect 10.9% → 14 (not entered: no major/minor split → major and minor blank).
- refs_requested blank: patient questions requested 4 references each, clinical questions specified no number. Funding: no financial support. Conflicts: none declared.
- Note: R0264 and R0277 share study_id Knee_2025 by the FirstAuthor_Year rule (same first author, same year, different papers/topics).

### R0277 — Knee_2025 (Cureus 2025), Achilles tendon ruptures, Australia
- 1 row, ChatGPT — MODEL VERSION NOT STATED anywhere in the paper (queried 6 Feb 2024, 8 questions ×2, new chat per question). Version left as "not stated"; nothing supplied from outside the paper.
- Printed counts (47 references): correct 16, incorrect 19, fabricated 12. Fabricated exact (could not be found; MEDLINE/Embase/Scopus). Fully accurate = 16 (correct = no inaccurate details in checked fields title/authors/date/journal). Major/minor blank: "incorrect" has no severity split.
- Funding: no financial support. Conflicts: none declared.

### R11480 — Moskatel_2023 (Front Neurol 2023), migraine prevention, USA
- 1 row, ChatGPT-3.5. refs_generated = 115, the analysed denominator: the paper generated 123 citations (41 of 47 medications) and analysed 115 unique papers after deduplication — stated in definitions_note.
- Fabricated exact: 76/115 "hallucinated" papers that did not exist (titles searched on Google Scholar and PubMed). Fully accurate exact (strict): 33/115 real papers that were correctly cited.
- Major = 82, EXACT BY SUM and flagged: 76 hallucinated + 6 papers that shared the names of real papers but had author/journal/year details as new creations (fabricated identity elements = major under the review definition). The three printed categories partition all 115, so no minor category exists in the paper → minor blank. Bad DOI blank (DOI errors only in selected Table 2 examples).
- Funding: Stanford School of Medicine, Dept of Neurology (OA fee only). Conflicts: none. Verifier independence not reported.

### R2196 — Teke_2026 (BMC Oral Health 2026), restorative dentistry, Turkey
- 5 rows from Table 3 (total / fabricated): ChatGPT-5 22/1; DeepSeek V3.2 9/5; Claude Sonnet 4.5 21/1; Microsoft Copilot (version not stated) 10/0; Google Gemini 3 Flash 19/0.
- Fabricated exact: could not be retrieved from any database (searched PubMed, Google Scholar, Scopus, Web of Science; both authors independently, consensus).
- All other outcome fields blank: "accurate and relevant" is defined by retrievability + correctly supporting the statement, not by correctness of all checked bibliographic fields → fully accurate mapping unclear under rule 7. "Partially accurate" and "misleading/irrelevant" are content-alignment categories, not bibliographic minor/major errors.
- ARITHMETIC FLAG (in the ChatGPT-5 row's definitions_note and here): ChatGPT-5's four category counts sum to 20 (15+3+1+1), not the printed total of 22; study-wide categories sum to 79 vs grand total 81. Two references unaccounted for in the printed table. Flagged, not corrected.
- All models: free-tier web interfaces, web browsing enabled, accessed 25 Dec 2025; references requested by follow-up prompt with no number specified → refs_requested blank. Funding: none. Conflicts: no competing interests.

### R2282 — Kang_2026 (J Med Internet Res 2026), paediatric hypospadias perioperative consultation, China
- 5 rows from Table 2 (citations n / F = Fabricated): ChatGPT-4o 33/5; Gemini-2.5-Pro 40/0; OpenEvidence 47/0; Zhipu Qingyan (version not stated) 17/4; DeepSeek (version not stated) 39/13.
- Fabricated exact: unretrievable articles strictly coded F; verification hierarchy PubMed → Crossref DOI resolver → Google Scholar → CNKI; 2 independent reviewers, raw agreement 80.9%, κ = 0.702 pre-adjudication, consensus reported.
- Fully accurate blank (rule 7, unclear): V (Verifiable) counts are printed (47/3/5/0/4 respectively) but the V/PV definitions live only in Multimedia Appendix 2, which is not part of the supplied full text, so it cannot be confirmed that V required all checked fields correct. Major/minor blank: PV is not split by severity and G (guideline-based, nonspecific) records are not specific bibliographic references.
- DENOMINATOR FLAG: Table 2 "Citations, n" includes G and NR (no references) records, and the per-model n sum to 176 while the Table 2 footnote reports κ across 157 paired records — an unresolved discrepancy in the paper, flagged here, not corrected.
- Funding: Postdoctoral Research Fund of West China Hospital, Sichuan University (grant 2025HXBH053). Conflicts: none declared. Study conducted April 2025, free-tier interfaces; no number of references requested per question → refs_requested blank.

## Cross-cutting conventions used
- model_year left blank wherever the paper does not state a release year (only R0186 states one); no vendor/outside data used.
- retrieval uses the extraction-form vocabulary (none / browsing or live search / RAG / reference database or citation tool access / not reported) with the paper's own detail in parentheses.
- n_bad_doi is blank in every row of this batch: no study prints a bad-DOI count on the review denominator (DOIs that do not resolve or resolve to a different paper, out of references carrying a DOI).
- Derived counts (rule 6) and exact-by-sum mappings (rule 5) are flagged in-line in definitions_note wherever used: R0047 (refs_requested; subanalysis denominator), R0264 (fabricated, fully accurate), R11480 (major).
