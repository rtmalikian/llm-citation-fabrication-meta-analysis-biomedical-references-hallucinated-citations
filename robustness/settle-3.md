# Settle-3 — Data-overlap investigation (Jędrzejczak_2024 × Pastucha_2026) + fully-accurate settlements

**Role:** Settlement Reader, Robustness Pass, Review 2 (LLM citation fabrication meta-analysis), 23 October 2026.
**Scope:** Data-overlap investigation plus settlements (a) and (b) as tasked. The manuscript and analysis files were **not** read.
**Sources read:** `fulltexts/R1232.pdf` (Jędrzejczak et al., medRxiv 2024, DOI 10.1101/2024.08.12.24311896), `fulltexts/R0696.xml` (Pastucha et al., Med Sci Monit 2026, DOI 10.12659/msm.950916), `extraction-passA.csv`, `extraction-passB.csv`, `extraction-form.md`.
**Machine-readable companion:** `robustness/settle-3.csv`.

---

## PART 1 — THE OVERLAP QUESTION

**Short answer: Pastucha_2026's ChatGPT-4 and Gemini 1.5 Pro arms are the Jędrzejczak_2024 experiment, carried over unchanged. They are the same underlying reference sets (duplicate data), not independent runs and not merely "overlapping" runs. The two reports must never both contribute these arms to a pool.**

### 1.1 Does Pastucha 2026 state that it reuses / extends / re-analyses the 2024 study?

**Not in those words — there is no reuse sentence anywhere in its Methods or Results.** A full-text search of R0696.xml for *reuse, re-used, extend(s), preprint, earlier, previous, replicate, duplicate, same data* finds exactly one link to the 2024 paper, and it is in the Acknowledgements, not in Methods/Results:

> "An earlier version of this manuscript was posted to the medRxiv preprint server https://doi.org/10.1101/2024.08.12.24311896 (accessed 13 August 2024)."
> — Pastucha_2026, Acknowledgements (R0696.xml, back matter)

That DOI is the Jędrzejczak_2024 preprint itself. In other words, Pastucha_2026 does not present itself as a *new* study that reuses an older one; it presents itself as the **journal version of the same manuscript**, extended with additional (2025) model arms. The preprint is not cited in the 2026 reference list, and the Introduction's otorhinolaryngology citations "[7,8]" are Frosolini et al. and Lechien et al., not the group's own preprint.

The Methods/Results text that bears on provenance, quoted verbatim:

> "The aim of this study was to evaluate the accuracy of references provided by 3 versions of ChatGPT and 3 versions of Gemini when used in the field of otorhinolaryngology. **We assessed 2024 and 2025 model releases** and tested whether enabling the newly introduced web-search option improved outcomes."
> — Pastucha_2026, Introduction (final paragraph)

> "In this study, we compared 3 versions of ChatGPT and 3 versions of Gemini by asking them to provide references about 25 highly cited topics in otorhinolaryngology (those with “guidelines” in the title). Answers were sought on 3 consecutive days to assess the variability and consistency of responses. **In total, the 6 chatbots returned 1947 references**, which were carefully checked against PubMed, Web of Science, and Google Scholar, and rated according to accuracy."
> — Pastucha_2026, Abstract

> "When the chatbots gave responses to each of the 25 questions … In total, across all the queries asked, the chatbots found **1947 references**. All these references were analyzed for correctness, and Table 4 shows the response accuracy across the 3 sessions for ChatGPT and Gemini."
> — Pastucha_2026, Results

The 1,947 total is the sum of all six arms as printed in Table 4 (231 + 396 + 296 + 193 + 530 + 301 = 1,947) — i.e. the 2026 paper counts the July 2024 references inside its own study total, with no separation of "previously reported" data. The testing schedule then dates the two arms in question to the 2024 data-collection window:

> Table 2 (Testing schedule), Pastucha_2026: "ChatGPT | 4.0 | **July 8–10, 2024**"; "Gemini | 1.5 Pro | **July 8–10, 2024**"; the other four arms are dated June 3–6, 2025.

### 1.2 Are the topics / prompts / sessions the same?

Yes — identical on every checkable dimension:

| Element | Jędrzejczak_2024 (R1232.pdf) | Pastucha_2026 (R0696.xml) |
|---|---|---|
| Authors | W. Wiktor Jędrzejczak, Małgorzata Pastucha, Henryk Skarżyński, Krzysztof Kochanek | Małgorzata Pastucha, Henryk Skarżyński, Krzysztof Kochanek, W. Wiktor Jedrzejczak (same four, reordered) |
| Topic selection | "The Web of Science was searched for papers with “guideline” in the title. Then the search was limited to the otorhinolaryngology category… Papers with at least 100 citations were then selected. This resulted in 25 papers…" (Method) | "(1) The Web of Science was searched for papers which had “guideline” in the title, limiting the search to the otorhinolaryngology category of Web of Science. (2) Repeating topics were removed… (3) Papers with at least 100 citations were selected. (4) This resulted in 25 papers…" (Data Collection Procedure) |
| Topics | Table 1: same 25 target guideline papers, same order, same derived topics | Table 1: same 25 target papers, same order, same topics. (Web of Science citation counts differ between the two Table 1 versions — e.g. refreshed counts in 2026 — consistent with a later lookup; the topic set is unchanged.) |
| Prompt (verbatim, both papers) | "Please provide references to scientific papers on guidelines for ['topic']. Only the bibliographic data of the papers is required." | "Please provide references to scientific papers on guidelines for ['topic']. Only the bibliographic data of the papers is required." |
| Administration | "The prompts were entered separately and the chatbots were reset to a new conversation after each question." | "The prompts were entered separately, and the chatbots were reset to a new conversation after each question." |
| Sessions / dates | "The responses of ChatGPT-4 and Gemini Advanced were collected on three consecutive days (**8–10.07.2024**)." (Method) | Table 2: ChatGPT 4.0 and Gemini 1.5 Pro — "**July 8–10, 2024**"; "Responses for each chatbot were collected over 3 consecutive days." |
| Verification | "verified with Pubmed, Web of Science, and Google Scholar" | "verified with PubMed, Web of Science, and Google Scholar" |
| Category scheme | "all were correct; all were accurate except that the Digital Object Identifier (DOI) was not given; all were accurate but the wrong DOI number was given; partially accurate but missing some information (but no false information); partially accurate but with some false information; and totally false information" (Method) | "correct (all information accurate); accurate, but DOI not given; accurate, but wrong DOI number; partially accurate, missing some information (but no false information); partially accurate, with some false information; and totally false" (Assessment of References) |

**Model-name caveat (flagged, not hidden):** the 2024 paper names its arms "ChatGPT-4" and "**Gemini Advanced**"; the 2026 paper names the corresponding arms "ChatGPT-4 / 4.0" and "**Gemini 1.5 Pro**". The 2026 paper nowhere states that "Gemini Advanced" = "Gemini 1.5 Pro", and nowhere uses the name "Gemini Advanced". The arm correspondence therefore rests on the dates and the counts (§1.3), not on a printed name equivalence. Nothing in either paper contradicts the correspondence.

### 1.3 The counts are identical cell-for-cell

Every cell of Jędrzejczak_2024 Table 2 for these two models reappears, unchanged, in Pastucha_2026 Table 4 (per-session *N*, percentages, and all six category rows):

**ChatGPT-4 — Sessions 1 / 2 / 3 (identical in R1232 Table 2 and R0696 Table 4A)**

| Row | S1 | S2 | S3 | Pooled |
|---|---|---|---|---|
| Number of references | 76 | 81 | 74 | **231** |
| Accurate references | 22 (29%) | 31 (38%) | 33 (45%) | **86** |
| — All correct | 10 | 17 | 19 | **46** |
| — Accurate but DOI number not given | 12 | 14 | 14 | **40** |
| Inaccurate references | 54 | 50 | 41 | 145 |
| — Accurate but wrong DOI number | 5 | 3 | 2 | **10** |
| — Partially accurate, missing some information | 24 | 20 | 23 | 67 |
| — Partially accurate but with some false information | 20 | 19 | 12 | 51 |
| — False reference | 5 | 8 | 4 | **17** |

**Gemini (Advanced in 2024 / 1.5 Pro in 2026) — Sessions 1 / 2 / 3 (identical in R1232 Table 2 and R0696 Table 4B)**

| Row | S1 | S2 | S3 | Pooled |
|---|---|---|---|---|
| Number of references | 65 | 68 | 60 | **193** |
| Accurate references | 9 (14%) | 7 (10%) | 10 (17%) | **26** |
| — All correct | 4 | 1 | 2 | **7** |
| — Accurate but DOI number not given | 5 | 6 | 8 | **19** |
| Inaccurate references | 56 | 61 | 50 | 167 |
| — Accurate but wrong DOI number | 0 | 0 | 1 | **1** |
| — Partially accurate, missing some information | 12 | 11 | 10 | 33 |
| — Partially accurate but with some false information | 27 | 43 | 33 | 103 |
| — False reference | 17 | 7 | 6 | **30** |

The identity extends beyond Table 2/Table 4. The core-reference analysis is also identical: Jędrzejczak_2024 Table 3 vs Pastucha_2026 Table 3 — ChatGPT accurate core references 5 (20%) / 7 (28%) / 12 (48%), consistent references 3 (12%), Fleiss kappa **0.32** in both; Gemini 6 (24%) / 5 (20%) / 6 (24%), consistent 1 (4%), kappa **0.16** in both.

Independent re-runs of stochastic chatbots on different days could not reproduce ~54 identical table cells plus identical kappa statistics. (Arithmetic inside each table also reconciles: e.g. ChatGPT 46 + 40 = 86; 86 + 145 = 231; Gemini 7 + 19 = 26; 26 + 167 = 193.)

### 1.4 Conclusion on overlap

**Same underlying reference sets — duplicate data.** Pastucha_2026 is the extended journal version of the Jędrzejczak_2024 preprint study: its ChatGPT-4 and Gemini arms *are* the July 8–10, 2024 dataset, reprinted unchanged, alongside four genuinely new arms collected 3–6 June 2025 (ChatGPT-4.1, ChatGPT-4.1-web, Gemini 2.5 Pro, Gemini 2.5 Pro-web), which appear only in Pastucha_2026.

**Pooling consequence:** the review may include the July 2024 data **once only**. Keeping both reports as separate studies and pooling both sets of arms would double-count **424 references** (231 + 193), including **47 fabricated events** (17 + 30) and **53 strict fully-accurate events** (46 + 7). Cleanest handling: one study record for the shared experiment (either report as the source), with Pastucha_2026 additionally contributing only its four 2025 arms.

---

## PART 2 — SETTLEMENT (a): Jędrzejczak_2024 arm structure and counts (from R1232.pdf itself)

### 2.1 What the 2024 paper prints, and under what definition

Jędrzejczak_2024 reports **per-session** counts only (Table 2, p. 5); it prints no pooled totals — pooled values below are sums of the printed session cells. Its category definitions, verbatim:

> "We checked whether: all were correct; all were accurate except that the Digital Object Identifier (DOI) was not given; all were accurate but the wrong DOI number was given; partially accurate but missing some information (but no false information); partially accurate but with some false information; and totally false information." — Method, R1232.pdf

> "As accurate references we included those that had all the correct information **except a missing DOI**." — Results, R1232.pdf

Table 2 therefore has a two-level structure: the headline row "**Accurate references**" = sub-row "**All correct**" + sub-row "**Accurate but DOI number not given**". The Abstract's accuracy ranges are the headline row (ChatGPT-4 "29–45%", Gemini Advanced "10–17%" = 22/76…33/74 and 7/68…10/60).

### 2.2 The dispute and the ruling

- **Pass A** extracted per-session rows and recorded `n_fully_accurate` = the "**All correct**" sub-row: ChatGPT-4 sessions 10 / 17 / 19 (pooled **46**); Gemini Advanced sessions 4 / 1 / 2 (pooled **7**).
- **Pass B** extracted pooled rows and recorded `n_fully_accurate` = the headline "**Accurate references**" row: ChatGPT-4 **86**, Gemini Advanced **26**.

Under the review's mapping rules (`extraction-form.md`), strict fully accurate = "accurate on all fields checked by the study… DOI where the study checked them must all be correct. **Any error in a checked field, major or minor, removes the reference from this count**", and mapping is allowed "only if the study printed definition covers the same cases as the review definition, no more and no fewer". DOI status *was* a checked field in this study (two of its six categories exist solely to grade DOI missing/wrong). A reference counted in "Accurate but DOI number not given" is, by the paper's own construction, **not** "all correct" — it is missing a checked field, which the Results definition explicitly tolerates ("except a missing DOI"). The headline "Accurate references" count is therefore **broader than** the review's strict definition and does **not** map to strict fully accurate (at most it is a lenient-type figure — real, correctly credited, retrievable despite the missing DOI — for narrative use). The "All correct" sub-row is the exact match.

**SETTLED (strict fully accurate, Jędrzejczak_2024, pooled across the 3 printed sessions):**
- **ChatGPT-4: 46** (10 + 17 + 19) of 231
- **Gemini Advanced: 7** (4 + 1 + 2) of 193

**Pass A was right; Pass B was wrong** on `n_fully_accurate` for both arms. Pass B's 86 and 26 are genuine printed numbers, but they are the paper-labelled "Accurate references" totals (46 + 40 and 7 + 19), not strict fully-accurate counts.

On the remaining fields the passes **agree**, and both agree with Table 2 — no error in either pass:
- refs_generated: ChatGPT-4 **231** (76 + 81 + 74); Gemini Advanced **193** (65 + 68 + 60)
- n_fabricated ("False reference"): ChatGPT-4 **17** (5 + 8 + 4); Gemini Advanced **30** (17 + 7 + 6)
- n_bad_doi ("Accurate but wrong DOI number"): ChatGPT-4 **10** (5 + 3 + 2); Gemini Advanced **1** (0 + 0 + 1)

Arm-structure note: Pass A's six per-session rows and Pass B's two pooled rows describe the same Table 2; the CSV below uses the pooled model names ("ChatGPT-4", "Gemini Advanced") with the session sums documented here, per the tasking. Pass B's derived major/minor totals (78 / 134; 67 / 33) were outside this settlement's remit and are not ruled on here.

---

## PART 3 — SETTLEMENT (b): What Pastucha_2026 prints for the shared arms (cross-check report)

Because the arms are the shared dataset (Part 1), the 2026 paper prints for them exactly the counts in §1.3, in **Table 4A (ChatGPT-4)** and **Table 4B (Gemini 1.5 Pro)**, R0696.xml. Pooled across its 3 printed sessions:

| Pastucha_2026 printed row (Table 4) | ChatGPT-4 (pooled) | Gemini 1.5 Pro (pooled) |
|---|---|---|
| Number of references | 231 (76 + 81 + 74) | 193 (65 + 68 + 60) |
| Accurate references | 86 (22 + 31 + 33) | 26 (9 + 7 + 10) |
| — All correct | 46 (10 + 17 + 19) | 7 (4 + 1 + 2) |
| — Accurate but DOI number not given | 40 (12 + 14 + 14) | 19 (5 + 6 + 8) |
| Accurate but wrong DOI number | 10 (5 + 3 + 2) | 1 (0 + 0 + 1) |
| Partially accurate: missing some information | 67 (24 + 20 + 23) | 33 (12 + 11 + 10) |
| Partially accurate but with some false information | 51 (20 + 19 + 12) | 103 (27 + 43 + 33) |
| False reference | 17 (5 + 8 + 4) | 30 (17 + 7 + 6) |

Definitions printed in Pastucha_2026, verbatim:

> "Each reference was assigned to one of the following categories: correct (all information accurate); accurate, but DOI not given; accurate, but wrong DOI number; partially accurate, missing some information (but no false information); partially accurate, with some false information; and totally false." — Assessment of References, R0696.xml

> "Accurate references were deemed to be those that had all the correct information (except perhaps a missing DOI)." — Results, R0696.xml

> "Finally, there were totally false references ("hallucinations")…" — Results, R0696.xml (the "False reference" row)

Cross-check note for the parallel settle work: the definitional split found in (a) recurs identically in the 2026 paper — Pass A's Pastucha_2026 rows took `n_fully_accurate` = "All correct" (**46** / **7**), Pass B's took "Accurate references" (**86** / **26**). The 2026 paper prints both sub-counts, so the strict value (All correct: 46 / 7) is directly available from Table 4 without derivation. Testing dates for these arms (Table 2): July 8–10, 2024 — the Jędrzejczak_2024 collection window.

---

## Caveats

1. No pooled totals are printed in either paper for these arms; all pooled figures above are sums of printed per-session cells, with the addition shown. No other numbers were derived or invented.
2. The "Gemini Advanced" (2024) ↔ "Gemini 1.5 Pro" (2026) correspondence is established by identical dates and identical cell-for-cell counts plus the Acknowledgements preprint statement; neither paper prints a sentence equating the two names.
3. Table 1 citation counts differ between the two papers (refreshed Web of Science counts in 2026); the 25 target papers and topics are the same. This does not affect the overlap conclusion, which rests on the generated-reference data, not the target-paper metadata.
