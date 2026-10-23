# Robustness pass discrepancy log, Review 2 (23 October 2026)

Every discrepancy between the two independent extraction passes, its settled value, the source location, and which pass was wrong. Pass A is the first version extraction (preserved as extraction-passA.csv). Pass B is the second, fully independent extraction (extraction-passB.csv plus the new study passes). Settlements were made by readers re-reading the source text; nothing was averaged and no value was silently changed. The corrected master is extraction.csv.

## Comparison statistics (by code)

Original studies, matched arms: 825 field cells compared where both passes had an entry; 487 (59 percent) differed at string level. Worst fields by string level difference rate: definitions_note, source_location, verifier_independent, model_version_as_printed, verification_source_named (all 80 to 100 percent; wording and formatting, not substance, in almost every case). Worst numeric field: n_fully_accurate (5 of 33 compared cells differed), then n_fabricated (4 of 51). On numeric inputs to the pools overall: 25 of 201 compared cells differed, of which 8 were arm pairing artefacts in Jedrzejczak 2024 (pass A pooled three sessions into one row per model; pass B split them), leaving 17 substantive numeric disagreements, all settled below or in the settle files.

New studies (37 from re-adjudication): batches 1 to 3, 51 arm pairs matched, 114 numeric cells compared, 16 discrepancies; batch 4, 12 further discrepancies. Citation chasing studies: Mikus 2024 counts adopted where the passes agreed after re-reading; Jedrzejczak 2023 outcome counts blank in both passes (the paper's analysis does not map to a printed count under the review definitions).

## Settled values that changed a pooled input

Blanked (printed category did not match the review definition exactly):
- Civelekler 2026, n_fully_accurate, all 4 arms (both passes' printed counts measured looser definitions; neither is strict field by field accuracy).
- Mugaanyi 2024, n_fully_accurate (pass A's 37 was an existence count).
- Singh 2026, n_fully_accurate (59, "correctly cited", not strict accuracy).
- Athaluri 2023, n_major_inaccuracy (69 rejected; the summed categories do not equal the review definition; the same 69 is, however, the paper's printed count of references with an invalid DOI, and is entered under n_bad_doi, whose definition it matches).
- Dhaimade 2026, n_major_inaccuracy, 3 arms (panel level agreement category, not reference counts).
- Pastucha 2026, n_major_inaccuracy stays blank (pass B's sums mix a partially false bucket that cannot be split).

Filled (printed count, or exactly one whole count reproducing the printed percentage, protocol rule 6):
- Metze 2024: n_fabricated 194, n_major_inaccuracy 194, n_fully_accurate 30 (of 260); n_bad_doi 12.
- Nieves-Lopez 2026, Copilot arm: n_major_inaccuracy 26 (exact sum of printed fabricated and fabricated detail counts).
- Moskatel 2023 (new): n_major_inaccuracy 82 (76 non-existent plus 6 real title with fabricated details).
- Suppadungsuk 2023 (new): n_fabricated 192.
- Ohlsen 2026 (new): ChatGPT arm n_major_inaccuracy 4, n_fully_accurate 2.

Corrected:
- Mugaanyi 2024, n_fabricated 15 (pass B). Coordinator re-read of the source (R0391, Europe PMC XML): natural sciences references exist 40 of 55, so non-existent = 15. The settlement reader's contrary value (a sum of the table's error margins) was not adopted: the margins count errors per field and are not a partition of the 230 references. The same reader's n_major_inaccuracy sum of 41 was not adopted for the same reason; the cell stays blank.
- Gwon 2024 (new), ChatGPT arm: n_fabricated 211 at refs_generated 403 (graded titles only; pass A had swept in 884 ungraded references).
- DiFebo 2026 (new), subanalysis arm: fabricated count removed from n_major_inaccuracy (misplaced by pass A); main arms refs_requested corrected to 160.

Removed rows:
- Aljamaan 2024, Bard arm (refs_generated 0, a model non-response, not an arm).
- Jedrzejczak 2024, all 6 arm rows: duplicate study. Pastucha 2026's acknowledgements name the medRxiv preprint DOI (10.1101/2024.10.15.24315549) as an earlier version of the same manuscript; topics, prompt, dates (8 to 10 July 2024) and the overlapping arms' data are identical cell for cell. Counted once, under Pastucha 2026.

Confirmed as printed (discrepancy was wording or pass error, value unchanged in the master):
- Shi 2026: pass A correct on all seven arms' n_fabricated; pass B had added a "Corrupted" error category.
- Pastucha 2026, n_fully_accurate: pass A correct on all arms.
- Pan 2026 (new): browsing arm n_fabricated 0 is a printed zero.
- Zhu 2025 (new): n_major_inaccuracy 0 and n_minor_error 0 are printed zeros.
- McCavitt 2026 (new): n_fabricated stays blank (7.9 percent of 2,556 is not a whole count and no count is printed).
- Liu 2026 and Woodrow 2025 (new): all outcome counts blank in both passes; their measures do not map to the review definitions. Narrative only.

## Settlement tables, original studies

### Shi 2026 (settlements in robustness/settle-1.csv; pass values and quotes in the matching .md)

| study | arm | field | settled value | wrong pass | source location |
|---|---|---|---|---|---|
| Shi_2026 | AI Research Army (pipeline) | n_fabricated | 1 | B | Table 3 (Failed=1, Corrupted=1, References=49), PDF p.11; category definitions §3.2, PDF p.4 |
| Shi_2026 | AI Scientist | n_fabricated | 2 | B | Table 3 (Failed=2, Corrupted=1, References=43), PDF p.11; category definitions §3.2, PDF p.4 |
| Shi_2026 | AI Research Army (single) | n_fabricated | 3 | B | Table 3 (Failed=3, Corrupted=2, References=64), PDF p.11; category definitions §3.2, PDF p.4 |
| Shi_2026 | Baseline (GPT-4) | n_fabricated | 6 | B | Table 3 (Failed=6, Corrupted=2, References=68), PDF p.11; category definitions §3.2, PDF p.4 |
| Shi_2026 | AI-Researcher | n_fabricated | 22 | B | Table 3 (Failed=22, Corrupted=1, References=79), PDF p.11; category definitions §3.2, PDF p.4 |
| Shi_2026 | Data-to-Paper | n_fabricated | 30 | B | Table 3 (Failed=30, Corrupted=1, References=83), PDF p.11; category definitions §3.2, PDF p.4 |
| Shi_2026 | Agent Laboratory | n_fabricated | 35 | B | Table 3 (Failed=35, Corrupted=1, References=97), PDF p.11; category definitions §3.2, PDF p.4 |
| Shi_2026 | AI Research Army (pipeline) | retrieval | reference database or citation tool access | A | §3.3 (pipeline = citation verification and repair), PDF p.6; §3.5 stages 2-3 (CrossRef and PubMed APIs), PDF p.7 |
| Aljamaan_2024 | ChatGPT 3.5 | n_fabricated | blank_not_printed | neither | Table 2 (per-identifier counts only); Table 1 + footnotes d/e (Methods > RHS Development); Table 3 (RHS medians only) |
| Aljamaan_2024 | Perplexity | n_fabricated | blank_not_printed | neither | Table 2 (per-identifier counts only); Table 1 + footnotes d/e (Methods > RHS Development); Table 3 (RHS medians only) |
| Aljamaan_2024 | SciSpace | n_fabricated | blank_not_printed | neither | Table 2 (per-identifier counts only); Table 1 + footnotes d/e (Methods > RHS Development); Table 3 (RHS medians only) |
| Aljamaan_2024 | Elicit | n_fabricated | blank_not_printed | neither | Table 2 (per-identifier counts only); Table 1 + footnotes d/e (Methods > RHS Development); Table 3 (RHS medians only) |
| Aljamaan_2024 | Bing | n_fabricated | blank_not_printed | neither | Table 2 (per-identifier counts only); Table 1 + footnotes d/e (Methods > RHS Development); Table 3 (RHS medians only) |
| Aljamaan_2024 | Bard | arm_inclusion | no_arm_refs_generated_0_no_extractable_data | A | Abstract Results; Results para 1 (Bard non-response quote; 500-reference denominator excludes Bard); Tables 2-3 (five chatbots onl |
| Aljamaan_2024 | ChatGPT 3.5 | retrieval | not_reported | B | Methods > Medical Prompts (uniform prompt format, all 6 chatbots); Methods > Testing AI Chatbots (authors' verification only); Int |
| Aljamaan_2024 | Perplexity | retrieval | not_reported | B | Methods > Medical Prompts (uniform prompt format, all 6 chatbots); Methods > Testing AI Chatbots (authors' verification only); ref |
| Aljamaan_2024 | SciSpace | retrieval | not_reported | B | Methods > Medical Prompts (uniform prompt format, all 6 chatbots); Discussion (Elicit/SciSpace 'dedicated to searching' general ch |
| Aljamaan_2024 | Elicit | retrieval | not_reported | B | Methods > Medical Prompts (uniform prompt format, all 6 chatbots); Discussion (Elicit/SciSpace 'dedicated to searching' general ch |
| Aljamaan_2024 | Bing | retrieval | not_reported | B | Methods > Medical Prompts (uniform prompt format, all 6 chatbots); Methods > Testing AI Chatbots (authors' verification only); ref |

### Aljamaan 2024 (settlements in robustness/settle-2.csv; pass values and quotes in the matching .md)

| study | arm | field | settled value | wrong pass | source location |
|---|---|---|---|---|---|
| Civelekler_2026 | DeepSeek-R1 | n_fully_accurate |  | A and B | Material and Methods evaluation criteria p.2 (Phase 1 'Correct Publications (verifiable and relevant)' and expert 'Fully Cited (ex |
| Civelekler_2026 | ChatGPT (GPT-5.1) | n_fully_accurate |  | A and B | Material and Methods evaluation criteria p.2 (Phase 1 'Correct Publications (verifiable and relevant)' and expert 'Fully Cited (ex |
| Civelekler_2026 | Copilot (Microsoft Copilot 4.2) | n_fully_accurate |  | A and B | Material and Methods evaluation criteria p.2 (Phase 1 'Correct Publications (verifiable and relevant)' and expert 'Fully Cited (ex |
| Civelekler_2026 | Gemini (Google Gemini Ultra 2.5) | n_fully_accurate |  | A and B | Material and Methods evaluation criteria p.2 (Phase 1 'Correct Publications (verifiable and relevant)' and expert 'Fully Cited (ex |
| Pastucha_2026 | ChatGPT-4 | n_fully_accurate | 46 | B | Table 4A row 'All correct' summed over 3 sessions (10+17+19); category definition 'correct (all information accurate)' in Assessme |
| Pastucha_2026 | ChatGPT-4.1 | n_fully_accurate | 1 | B | Table 4A row 'All correct' summed over 3 sessions (0+0+1); category definition 'correct (all information accurate)' in Assessment  |
| Pastucha_2026 | ChatGPT-4.1 (web search) | n_fully_accurate | 33 | B | Table 4A row 'All correct' summed over 3 sessions (12+12+9); category definition 'correct (all information accurate)' in Assessmen |
| Pastucha_2026 | Gemini 1.5 Pro | n_fully_accurate | 7 | B | Table 4B row 'All correct' summed over 3 sessions (4+1+2); category definition 'correct (all information accurate)' in Assessment  |
| Pastucha_2026 | Gemini 2.5 Pro | n_fully_accurate | 55 | B | Table 4B row 'All correct' summed over 3 sessions (10+11+34); category definition 'correct (all information accurate)' in Assessme |
| Pastucha_2026 | Gemini 2.5 Pro (web search) | n_fully_accurate | 71 | B | Table 4B row 'All correct' summed over 3 sessions (22+27+22); category definition 'correct (all information accurate)' in Assessme |
| Pastucha_2026 | ChatGPT-4 | n_major_inaccuracy_incl_fabricated |  | B | Assessment of References (Material and Methods) category list; Results text following Table 4 (wrong-DOI and partially-false descr |
| Pastucha_2026 | ChatGPT-4.1 | n_major_inaccuracy_incl_fabricated |  | B | Assessment of References (Material and Methods) category list; Results text following Table 4 (wrong-DOI and partially-false descr |
| Pastucha_2026 | ChatGPT-4.1 (web search) | n_major_inaccuracy_incl_fabricated |  | B | Assessment of References (Material and Methods) category list; Results text following Table 4 (wrong-DOI and partially-false descr |
| Pastucha_2026 | Gemini 1.5 Pro | n_major_inaccuracy_incl_fabricated |  | B | Assessment of References (Material and Methods) category list; Results text following Table 4 (wrong-DOI and partially-false descr |
| Pastucha_2026 | Gemini 2.5 Pro | n_major_inaccuracy_incl_fabricated |  | B | Assessment of References (Material and Methods) category list; Results text following Table 4 (wrong-DOI and partially-false descr |
| Pastucha_2026 | Gemini 2.5 Pro (web search) | n_major_inaccuracy_incl_fabricated |  | B | Assessment of References (Material and Methods) category list; Results text following Table 4 (wrong-DOI and partially-false descr |

### Pastucha 2026 and Civelekler 2026 (fully accurate) (settlements in robustness/settle-3.csv; pass values and quotes in the matching .md)

| study | arm | field | settled value | wrong pass | source location |
|---|---|---|---|---|---|
| Jędrzejczak_2024 | ChatGPT-4 | refs_generated | 231 | none | R1232.pdf Table 2 (Number of references: 76+81+74) |
| Jędrzejczak_2024 | ChatGPT-4 | n_fabricated | 17 | none | R1232.pdf Table 2 (False reference: 5+8+4) |
| Jędrzejczak_2024 | ChatGPT-4 | n_fully_accurate_strict | 46 | B | R1232.pdf Table 2 (All correct: 10+17+19); strict per extraction-form (paper Accurate references = 86 includes missing-DOI) |
| Jędrzejczak_2024 | ChatGPT-4 | accurate_references_paper_label_incl_missing_doi | 86 | none | R1232.pdf Table 2 (Accurate references: 22+31+33 = All correct 46 + DOI not given 40); Results definition: all correct information |
| Jędrzejczak_2024 | ChatGPT-4 | n_bad_doi_wrong_doi | 10 | none | R1232.pdf Table 2 (Accurate but wrong DOI number: 5+3+2) |
| Jędrzejczak_2024 | Gemini Advanced | refs_generated | 193 | none | R1232.pdf Table 2 (Number of references: 65+68+60) |
| Jędrzejczak_2024 | Gemini Advanced | n_fabricated | 30 | none | R1232.pdf Table 2 (False reference: 17+7+6) |
| Jędrzejczak_2024 | Gemini Advanced | n_fully_accurate_strict | 7 | B | R1232.pdf Table 2 (All correct: 4+1+2); strict per extraction-form (paper Accurate references = 26 includes missing-DOI) |
| Jędrzejczak_2024 | Gemini Advanced | accurate_references_paper_label_incl_missing_doi | 26 | none | R1232.pdf Table 2 (Accurate references: 9+7+10 = All correct 7 + DOI not given 19); Results definition: all correct information ex |
| Jędrzejczak_2024 | Gemini Advanced | n_bad_doi_wrong_doi | 1 | none | R1232.pdf Table 2 (Accurate but wrong DOI number: 0+0+1) |
| Pastucha_2026 | ChatGPT-4 | refs_generated | 231 | none | R0696.xml Table 4A (Number of references: 76+81+74); testing dates Table 2: July 8-10 2024 |
| Pastucha_2026 | ChatGPT-4 | n_fabricated | 17 | none | R0696.xml Table 4A (False reference: 5+8+4) |
| Pastucha_2026 | ChatGPT-4 | n_fully_accurate_strict | 46 | B | R0696.xml Table 4A (All correct: 10+17+19); strict per extraction-form (paper Accurate references = 86 includes missing-DOI) |
| Pastucha_2026 | ChatGPT-4 | accurate_references_paper_label_incl_missing_doi | 86 | none | R0696.xml Table 4A (Accurate references: 22+31+33 = All correct 46 + DOI not given 40); Results: deemed accurate except perhaps a  |
| Pastucha_2026 | ChatGPT-4 | n_bad_doi_wrong_doi | 10 | none | R0696.xml Table 4A (Accurate but wrong DOI number: 5+3+2) |
| Pastucha_2026 | Gemini 1.5 Pro | refs_generated | 193 | none | R0696.xml Table 4B (Number of references: 65+68+60); testing dates Table 2: July 8-10 2024 |
| Pastucha_2026 | Gemini 1.5 Pro | n_fabricated | 30 | none | R0696.xml Table 4B (False reference: 17+7+6) |
| Pastucha_2026 | Gemini 1.5 Pro | n_fully_accurate_strict | 7 | B | R0696.xml Table 4B (All correct: 4+1+2); strict per extraction-form (paper Accurate references = 26 includes missing-DOI) |
| Pastucha_2026 | Gemini 1.5 Pro | accurate_references_paper_label_incl_missing_doi | 26 | none | R0696.xml Table 4B (Accurate references: 9+7+10 = All correct 7 + DOI not given 19); Results: deemed accurate except perhaps a mis |
| Pastucha_2026 | Gemini 1.5 Pro | n_bad_doi_wrong_doi | 1 | none | R0696.xml Table 4B (Accurate but wrong DOI number: 0+0+1) |

### Remaining original studies, batch A (settlements in robustness/settle-4a.csv; pass values and quotes in the matching .md)

| study | arm | field | settled value | wrong pass | source location |
|---|---|---|---|---|---|
| Mugaanyi_2024 | ChatGPT (GPT-3.5) - natural sciences (clinical/biomedical) topics only | n_fabricated | 15 | A | Table 2, Natural sciences column (n=55): 'Citation exists' 40 (72.7%); settled as exact complement 55-40=15 (no matching publicati |
| Mugaanyi_2024 | ChatGPT (GPT-3.5) - natural sciences (clinical/biomedical) topics only | n_fully_accurate | blank | A | Table 2 ('Citation accurate' 37 (67.3%) vs 'DOI accurate' 18 (32.7%)); Results > Included Topics and Citations ('existence, validi |
| Metze_2024 | ChatGPT-4 | refs_generated | 260 | neither | Results text ('A total of 260 references were released (zero to five per reply)'); Table 1 'Retrieved references' row sums to 260  |
| Metze_2024 | ChatGPT-4 | n_fabricated | 194 | A | Results text classification of 260 references (74.62% 'Hallucinations' -> 194, unique whole number under Rule 6); category definit |
| Metze_2024 | ChatGPT-4 | n_major_inaccuracy_incl_fabricated | 194 | A | Results text (74.62% 'Hallucinations' -> 194); Methods category definitions - category (c) is wholly major and category (b) 'With  |
| Metze_2024 | ChatGPT-4 | n_fully_accurate | 30 | A | Results text (11.54% 'Correct' -> 30, unique whole number under Rule 6); Methods category definitions - exhaustive partition on in |
| Metze_2024 | ChatGPT-4 | n_minor_error | 36 | A | Results text (13.85% 'With incorrect data' -> 36, unique whole number under Rule 6); Methods category definition ('With incorrect  |
| Nieves-Lopez_2026 | ChatGPT-5.4 | n_major_inaccuracy_incl_fabricated | blank | B | Methods > Data Set classification paragraph ('some of the components were incorrect, non-compatible, or non-existent' = partial fa |
| Nieves-Lopez_2026 | Gemini-3 | n_major_inaccuracy_incl_fabricated | blank | B | Methods > Data Set classification paragraph ('some of the components were incorrect, non-compatible, or non-existent' = partial fa |
| Nieves-Lopez_2026 | Copilot | n_major_inaccuracy_incl_fabricated | 26 | A | Results > Reference Fabrication Rates ('903 (97.2%) were real and 26 (2.8%) were fabricated... 0.0% (0/26) were partially fabricat |

### Remaining original studies, batch B (settlements in robustness/settle-4b.csv; pass values and quotes in the matching .md)

| study | arm | field | settled value | wrong pass | source location |
|---|---|---|---|---|---|
| Athaluri_2023 | ChatGPT | n_major_inaccuracy_incl_fabricated |  | A | R0094.xml Results (69 did not have a DOI; 41 of 69 found to exist; 28 neither turned up nor had an existing DOI); Table 3 (valid D |
| Dhaimade_2026 | GPT-5.0 (Full Test) | n_major_inaccuracy_incl_fabricated |  | A | R2475.xml Methods, Human-in-the-loop citation validation (three-tier taxonomy: completely valid / partially correct incl. partial  |
| Dhaimade_2026 | GPT-5.0 (Individual Question) | n_major_inaccuracy_incl_fabricated |  | A | R2475.xml Methods, Human-in-the-loop citation validation (three-tier taxonomy); Results, Citation hallucination assessment (halluc |
| Dhaimade_2026 | Claude Sonnet 4.0 (Individual Question) | n_major_inaccuracy_incl_fabricated |  | A | R2475.xml Methods, Human-in-the-loop citation validation (three-tier taxonomy); Results, Citation hallucination assessment (halluc |
| Linardon_2025 | GPT-4o | n_bad_doi |  | A | R3629.xml Methods, Data Collection and Analysis (for nonfabricated sources, discrepancies/errors recorded in author list, year, ti |
| Seifi_2026 | GPT-5.3 | n_minor_error | 25 | B | R0053_v2.xml Methods (Hallucination Scale: 1 = minor error/typo; denominator 300 = 10 topics x 3 models x 10 references = 100 per  |
| Seifi_2026 | DeepSeek-V3 | n_minor_error | 13 | B | R0053_v2.xml Methods (Hallucination Scale: 1 = minor error/typo; denominator 100 per model); Results, Model-Level Performance (any |
| Seifi_2026 | Grok-4 | n_minor_error | 7 | B | R0053_v2.xml Methods (Hallucination Scale: 1 = minor error/typo; denominator 100 per model); Results, Model-Level Performance (any |
| Singh_2026 | GPT-5 | n_fully_accurate |  | A | R0180_v2.xml Methods, Reference Validation (accurate/supportive = reference found and directly supported the claim; no bibliograph |


## Settlement narratives, new studies

Full settlement records: robustness/settle-5.md (batches 1 to 3) and robustness/settle-6.md (batch 4), with the comparison files robustness/ft2/new-extraction-discrepancies.json and new-extraction-discrepancies-b4.json. Study identifier corrections made at settlement: R0264 is Knee_2026 and R0277 is Knee_2025 (first author "Knee A" in both papers; distinct studies, not a duplicate pair); R2931 is Idan_2025 (pass B had used a given name as the study identifier).
