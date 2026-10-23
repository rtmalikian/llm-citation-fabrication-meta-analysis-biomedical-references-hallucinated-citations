# Extraction notes — Extractor A, batch 1 (robustness pass, new included studies)

Date: 23 October 2026 (run 2026-10-22 PT). Independent extraction: extraction.csv, extraction-passA/B.csv and analysis files were NOT read.
Output: `extraction-newA-batch1.csv` — 24 rows (one per model arm) for 8 records, exact 25-column schema.
Method: JATS XML stripped to text (python regex/html unescape); all counts taken as printed, with source_location per row.
Note: this file replaces a notes file timestamped 02:56 that described a different (21-row) extraction and did not match the CSV delivered with these notes.

## Per-study notes

### R0047 — DiFebo_2026 (Eur Heart J Digit Health 2026, cardiology literature-search tools)
- 5 tools evaluated; PubMed (conventional Boolean database, 105 articles) is NOT a model arm and has no row. AI arms: ChatGPT-5 (154), Elicit (140), Consensus (158), Scite (113) — main analysis (up to 10 refs/query; 4 prompts × 4 topics = 160 requested per AI tool).
- Main analysis: "no hallucinated citations occurred across any tool, topic, or prompt" → n_fabricated = 0 and n_major = 0 for all 4 AI arms (all other citations locatable despite minor discrepancies). Minor-error and fully-accurate counts not reported per tool → blank.
- Extra row: ChatGPT-5 clinical-studies subanalysis (larger lists requested): 59 ChatGPT citations (25 shared with SLRs + 34 ChatGPT-only), 10 hallucinated (17%). Kept as a separate row so it cannot be silently pooled with the main-analysis row — adjudicator to confirm convention.
- Country: lead team France; co-authors Italy/Switzerland (recorded as France). Funding: None. Conflicts: none declared.

### R0112 — McLaughlin_2026 (Neurosurg Pract 2026, spine surgery; 5 LLMs, clinician + patient prompts pooled, Table 3)
- Counts as printed: ChatGPT (n=98) fab 11, accurate 55; Gemini (65) fab 17, accurate 15; Claude (100) fab 11, accurate 78; Copilot (98) fab 13, accurate 31; OpenEvidence (120) fab 0, accurate 120 (major set to 0 for OpenEvidence only, since score-0 and score-1 are both 0).
- Fabricated (score 0) and fully accurate strict (score 2) map exactly. Score 1 "misrepresented" mixes minor/major errors and non-peer-reviewed websites → major and minor left blank for all arms.
- n_bad_doi blank: Table 4 reports incorrect DOI/PMID counts only inside the score-1 subset; no DOI-carrying denominator.
- refs_requested blank: prompt asked 3–5 references × 20 questions (range, no printed total).
- Versions as printed: ChatGPT 5.0, Gemini 2.5 Flash, Claude Sonnet 4.5, Copilot not stated, OpenEvidence 2.7.12; all with internet search enabled (Oct 2025). Verification: PubMed + publisher sites, 3 independent medical student reviewers (κ=0.918). No funding; no disclosures.

### R0186 — McCavitt_2026 (JBJS Open Access 2026, ChatGPT-4o mini, AAOS hip-fracture CPG)
- NO outcome counts mapped (all blank). Printed: 228 responses citing 2,556 publications, 7.9% fabricated (≈202 derived — recorded in definitions_note only).
- Why not exact: fabricated defined as "not indexed in PubMed" — broader than the review's "no matching publication exists" (a real paper absent from PubMed counts as fabricated). Inaccuracy definition (any field discrepancy vs the PubMed record) includes minor errors → major not exact. No fully-accurate count printed (1.1% is overlap with the CPG's own reference list, a different construct).
- CONTRADICTION flagged (not corrected): Table III means (7.53 total references and 0.59 fabricated per response × 228 ≈ 1,717 total / ≈135 fabricated) conflict with the text's 2,556 total at 7.9%.
- Funding not stated; conflicts via online disclosure forms only.

### R0264 — Knee_2025 (Cureus 2025, ChatGPT-4o mini, midshaft clavicle fractures; 31 Aug 2024)
- As printed (Reference analysis): 128 references — 1 correct (0.8%), 14 incorrect (10.9%), 113 fabricated (88.3%). Fabricated = "could not be located at all" (MEDLINE/Embase/Scopus) → exact; correct → fully accurate strict = 1. "Incorrect" mixes severities → major/minor blank.
- refs_requested blank (4 per patient question printed; clinical questions unspecified). No funding; no conflicts (ICMJE).

### R0277 — Knee_2025 (Cureus 2025, ChatGPT 3.5, Achilles tendon ruptures)
- As printed: 47 references — 16 correct (34%), 19 incorrect (40%), 12 fabricated (26%). Same mapping logic as R0264 (fabricated exact; correct = fully accurate 16; incorrect unmapped).
- model_year 2022 from vendor release record for GPT-3.5 (not stated in the paper; flagged in definitions_note). No funding; no conflicts (ICMJE).

### R11480 — Moskatel_2023 (Front Neurol 2023, ChatGPT-3.5, migraine-prevention medications)
- Prompt "Give 3 citations if they exist" × 47 medications → refs_requested 141; generated 115.
- As printed: 33/115 real, 76/115 "hallucinated" (not real papers; title searches in Google Scholar + PubMed) → n_fabricated = 76 (exact), 6/115 shared names of real papers but had not real citations.
- The 6 mixed cases were NOT added to fabricated (a publication with that title exists) and major was left blank: the paper assessed real papers for relevance, not all-field bibliographic accuracy, so major and fully accurate are not extractable. Flagged for human-author adjudication — if the author rules the 6 are major inaccuracies, major would be 82 by sum.
- Funding: Stanford Dept of Neurology paid the open-access fee. Conflicts: none declared.

### R2196 — Teke_2026 (BMC Oral Health 2026, restorative dentistry; queried 25 Dec 2025)
- Table 3 counts as printed: ChatGPT-5 (n=22) fab 1; DeepSeek V3.2 (9) fab 5; Claude Sonnet 4.5 (21) fab 1; Microsoft Copilot (10) fab 0; Google Gemini 3 Flash (19) fab 0. Fabricated = "could not be retrieved from any database" (PubMed/Google Scholar/Scopus/WoS) → exact.
- "Accurate and relevant" counts (15/3/18/6/16) NOT mapped to fully accurate (mapping rule 7 — category also requires supporting the statement; checked fields not stated). "Partially accurate" / "misleading-irrelevant" are content-alignment categories → major/minor blank.
- ARITHMETIC flagged: ChatGPT-5 category counts (15+3+1+1) sum to 20, not its printed total of 22; grand category totals sum to 79 of 81. All other rows sum correctly.
- Reference number was not specified in the prompt → refs_requested blank. No funding; no competing interests.

### R2282 — Kang_2026 (JMIR 2026, pediatric hypospadias; April 2025, China)
- Table 2 counts as printed: OpenEvidence (n=47) F 0; Gemini-2.5-Pro (40) F 0; DeepSeek (39) F 13; ChatGPT-4o (33) F 5; Zhipu Qingyan (17) F 4. F = unretrievable articles strictly coded Fabricated after canonical-source reverification (PubMed → Crossref DOI resolver → Google Scholar → CNKI) → exact.
- V (verifiable) counts NOT mapped to fully accurate: main text does not show V requires all-field accuracy (definitions sit in Multimedia Appendix 2, not in the extracted full text). PV mixes severities → major/minor blank.
- Denominator caveats (in definitions_note): printed totals include nonspecific guideline mentions (G: Gemini 34, DeepSeek 20, ChatGPT-4o 21, Zhipu 10) and no-reference (NR) units for Gemini (1) and Zhipu (2). Table 2 footnote reports κ over 157 paired records vs 176 citations tabulated — flagged.
- DeepSeek and Zhipu Qingyan versions not stated in main text (configuration in Multimedia Appendix 1) → model_version recorded as not stated, model_year blank. Funding: West China Hospital Postdoctoral Research Fund 2025HXBH053. Conflicts: none declared.

## General conventions used
- Blanks = not extractable / not mapped under mapping rules 1–8; never zero. Zero entered only where the paper prints zero (or, for R0112 OpenEvidence major, where both component categories print zero).
- model_year from the paper where stated or clearly implied by the printed version (GPT-4o mini 2024 — release date printed in R0186; GPT-3.5 2022 — vendor release record, flagged per row); left blank where the version itself is unstated.
- eligibility = include_generation for every row (all 8 are generation experiments; no audit-stratum records in this batch).
