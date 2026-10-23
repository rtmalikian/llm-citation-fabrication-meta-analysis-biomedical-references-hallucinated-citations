# Settlement 2 — n_fully_accurate disputes: Civelekler_2026 and Pastucha_2026

Settlement Reader, Robustness Pass (23 October 2026). Review 2 (LLM citation fabrication / inaccuracy).

Sources re-read for this settlement only: `fulltexts/R0125.pdf` (Civelekler_2026), `fulltexts/R0696.xml` (Pastucha_2026), `extraction-passA.csv`, `extraction-passB.csv`, `extraction-form.md`. The manuscript and analysis files were not read.

## Rule applied

From `extraction-form.md`, Review definitions (fixed) and Mapping rules:

> "Fully accurate, strict: accurate on all fields checked by the study. Authors, title, journal or source, year, and volume, pages and DOI where the study checked them must all be correct. Any error in a checked field, major or minor, removes the reference from this count."

> "Major inaccuracy: any major inaccuracy, including completely fabricated. An error that prevents retrieval of the intended source, or that misattributes the source. It includes a completely fabricated reference; a fabricated element that forms part of the identity of the source, such as a fabricated title, fabricated first author, or fabricated DOI; a journal, year, volume or page set that points to a different publication or to no publication… Minor errors that leave the source findable and correctly credited do not count here."

> Mapping rule 2: "A printed count maps to a review outcome only if the study printed definition covers the same cases as the review definition, no more and no fewer."
> Mapping rule 5: a summed mapping is allowed only where the parts "sum, without overlap, to a review definition exactly… together they cover [the review definition] as defined and nothing else."
> Mapping rule 7: "A printed accurate count maps to strict only if the study checked all fields its accurate label claims and counted any error in a checked field against accuracy."

"Blank" below means **not extractable for the strict pool** (narrative use only, under the printed label). It never means zero. All printed counts that were rejected for pooling are retained in this file for narrative synthesis.

**Headline settlements**

- **Civelekler_2026, all 4 arms: n_fully_accurate = blank.** Neither pass maps exactly. Pass B counted the Phase-1 "verifiable and relevant" count; Pass A counted the expert "fully cited (exact match)" relevance count. Neither printed definition is strict bibliographic accuracy on all checked fields, and no printed cross-tabulation allows the strict count to be derived.
- **Pastucha_2026, all 6 arms: n_fully_accurate = Pass A** ("All correct" row of Table 4). Pass B counted the broader "Accurate references" total, which the paper explicitly defines to allow a missing DOI.
- **Pastucha_2026, all 6 arms: n_major_inaccuracy_incl_fabricated = blank.** Pass A's blank stands. Pass B's exact-by-sum is arithmetically correct but not exact in definition: its "partially accurate with some false information" component mixes misattributing errors with errors that, as printed, do not establish prevention of retrieval or misattribution, and the paper prints no sub-count to split them.

---

## 1. Civelekler_2026 (R0125) — n_fully_accurate

Paper as printed: 35 standardised clinical paragraphs on anterior segment (corneal, conjunctival and eyelid) disease from *The Review of Ophthalmology* (4th edition); each model was asked for an AMA 11-style reference relevant to each paragraph; 35 citations analysed per model. `refs_generated = 35` and `n_fabricated` are not in dispute.

### 1.1 Printed classifications (verbatim)

Phase 1 — Material and Methods, evaluation criteria (p. 2):

> "Generated citations were evaluated against predefined criteria: 1) Correct Publications (verifiable and relevant), 2) DOI Mismatches (correct journal, wrong DOI), 3) Incorrect Author/Journal Name, and 4) Non-Correct Publications (unrelated or unfindable). The primary outcome was the proportion of correctly generated citations per model."

Phase 2 (expert) — Material and Methods (p. 2):

> "Subsequently, all citations initially flagged as 'correct' underwent expert validation. Two ophthalmology experts independently classified each citation as: 'Fully Cited' (exact match), 'Partially Cited' (relevant but not the best or exact match), or 'Not Cited' (unrelated or fabricated). Discrepancies were resolved by discussion. Inter-rater reliability for this human evaluation was substantial (Cohen's kappa = 0.74)."

Summary (p. 1) states the same two results sets side by side:

> "DeepSeek demonstrated the highest citation accuracy (78.6%, 22/35), followed by ChatGPT (51.4%, 18/35), and Copilot (51.4%, 18/35). Gemini showed the lowest accuracy (12.9%, 5/35). … Expert validation confirmed DeepSeek's relative advantage, with 42.9% (15/35) of its references classified as fully cited, compared with Copilot (20.0%, 7/35), ChatGPT (11.4%, 4/35), and Gemini (11.4%, 4/35)."

Results (p. 3), Phase 1 counts (see also Table 1, p. 3: "Correct Citations (%)" 78.6 / 51.4 / 51.4 / 12.9, with separate rows for DOI Mismatches and Journal/Author Name Mistakes):

> "DeepSeek achieved the highest proportion of correct citations at 78.6% (22/35). ChatGPT and Copilot demonstrated moderate and similar performance, with accuracy rates of 51.4% (18/35) and 51.4% (18/35), respectively. Gemini exhibited the lowest accuracy, at 12.9% (5/35)."

Results (p. 3), expert counts:

> "DeepSeek yielded the highest number of references classified as 'fully cited' by experts (15 out of 35, 42.9%). However, a notable portion of its output was still deemed only 'partially cited' (12 instances) or 'not cited' (5 instances). The other models had lower expert-validated fully-cited rates: Copilot (20.0%, 7/35), ChatGPT (11.4%, 4/35), and Gemini (11.4%, 4/35)."

Discussion (p. 4) — what the expert phase was measuring:

> "A key insight from the expert validation is the distinction between automated accuracy and expert-validated utility. Many citations initially deemed 'correct' were later judged by specialists to be only partially relevant or entirely wrong."

### 1.2 Disputed values and settlement

| model_arm (Pass A name) | Pass A — "Fully Cited" | Pass B — Phase-1 "Correct" | **Settled n_fully_accurate** |
|---|---|---|---|
| DeepSeek-R1 | 15 | 22 | **blank (not extractable)** |
| ChatGPT (GPT-5.1) | 4 | 18 | **blank (not extractable)** |
| Copilot (Microsoft Copilot 4.2) | 7 | 18 | **blank (not extractable)** |
| Gemini (Google Gemini Ultra 2.5) | 4 | 5 | **blank (not extractable)** |

Source locations for the rejected printed counts: Pass B counts — Summary (p. 1), Results text (p. 3) and Table 1 (p. 3). Pass A counts — Summary (p. 1) and Results text, expert-validation paragraph (p. 3). Table 1 contains no expert-phase counts.

### 1.3 Why Pass B is wrong

Pass B's values are the Phase-1 "Correct Publications" counts. On the parent note for DeepSeek: 22 is not merely `35 − 13` by coincidence — it is the printed "correct citations" count itself — but what B counted is **existence + relevance, not strict accuracy**:

1. The printed definition is only "(verifiable and relevant)". It does not state that authors, title, journal/source, year, volume/pages and DOI were all checked and all correct. Under mapping rules 2 and 7 it therefore does not cover the same cases as strict fully accurate.
2. The paper tracks bibliographic errors separately from, and not as a partition of, the correct count: Table 1 (p. 3) lists DOI Mismatches (DeepSeek 8, ChatGPT 3, Copilot 0, Gemini 2) and Journal/Author Name Mistakes (2, 2, 2, 0) alongside Correct Citations, and the tallies do not partition 35 (e.g. ChatGPT: 18 correct + 19 non-correct = 37; Gemini: 5 + 31 = 36). A "verifiable and relevant" citation is therefore not shown by the paper to be free of a checked-field error.
3. Pass B's own note concedes the point: its definition "does not state all bibliographic fields correct, mapping to strict fully accurate UNCLEAR." An unclear mapping enters neither pool (form, rule 7).

### 1.4 Why Pass A is also wrong

Pass A's values are the expert "Fully Cited" counts. "Exact match" in this paper is **not** a field-by-field bibliographic verdict:

1. The printed contrast defines the scale topically: "Fully Cited" (exact match) vs "Partially Cited" (**"relevant but not the best or exact match"**) vs "Not Cited" (unrelated or fabricated). The dimension being graded is whether the citation is the exact/best source **for the paragraph**, not whether every bibliographic field is correct.
2. The Discussion confirms this reading: the expert phase is framed as "expert-validated **utility**" as distinct from "automated accuracy", and the drop from Phase-1 correct to fully cited is explained by citations being "only **partially relevant** or entirely wrong" — a relevance judgement.
3. Consequence for exactness, in both directions: (a) *narrower than strict* — a bibliographically perfect citation (every checked field correct) that is relevant but not the best/exact source for the paragraph is "Partially Cited" here, but is fully accurate (strict) for the review; (b) *not shown to exclude field errors* — no printed sentence states that a "Fully Cited" citation was re-checked and found correct on authors, title, journal, year, volume/pages and DOI. The definition therefore covers different cases from strict fully accurate, "no more and no fewer" fails, and rule 2 blocks the mapping.

### 1.5 Why the strict count cannot be derived from what is printed

No table or text cross-tabulates Phase-1 field-error status (DOI mismatch, author/journal mistake) against the expert Fully/Partially/Not classification, so the number that is simultaneously free of every checked-field error cannot be recovered exactly from the printed category counts. Two printed inconsistencies (flagged only, not corrected, per the form) reinforce that no derivation is safe:

- Methods says the expert phase was applied to "all citations initially flagged as 'correct'", yet for DeepSeek the expert counts printed in Results sum to 15 + 12 + 5 = 32 — more than the 22 Phase-1-correct citations, and not 35.
- Gemini Phase-1 accuracy is printed as "12.9% (5/35)" (Summary and Results); 5/35 is 14.3%, so the printed percentage and the printed count disagree.

**Settlement: blank for all four arms.** Use the Phase-1 counts (22 / 18 / 18 / 5) and the expert fully-cited counts (15 / 4 / 7 / 4) in narrative synthesis only, under their printed labels ("Correct Publications (verifiable and relevant)" and "Fully Cited (exact match)").

---

## 2. Pastucha_2026 (R0696) — n_fully_accurate

Paper as printed: 25 highly cited otorhinolaryngology "guideline" topics, 3 consecutive sessions per chatbot version, references checked against PubMed, Web of Science and Google Scholar. Per-arm `refs_generated` and `n_fabricated` are not in dispute. All Table 4 counts below are sums over the 3 sessions printed in Table 4, as both passes computed them; every sum was re-added for this settlement and reconciles exactly (Accurate = All correct + DOI not given; Accurate + Inaccurate = Number of references; the four Inaccurate sub-rows sum to Inaccurate).

### 2.1 Printed classifications (verbatim)

Abstract, Material/Methods:

> "In total, the 6 chatbots returned 1947 references, which were carefully checked against PubMed, Web of Science, and Google Scholar, and rated according to accuracy. Ratings were given based on correct authorship, complete bibliographic details, and proper DOI numbers."

Assessment of References (Material and Methods):

> "Each reference was assigned to one of the following categories: correct (all information accurate); accurate, but DOI not given; accurate, but wrong DOI number; partially accurate, missing some information (but no false information); partially accurate, with some false information; and totally false."

Results (definition of the Table 3 / Table 4 "Accurate references" row):

> "Accurate references were deemed to be those that had all the correct information (except perhaps a missing DOI)."

Table 4 (A: ChatGPT arms; B: Gemini arms) prints, per session, the parent row "Accurate references" with exactly two sub-rows: "All correct" and "Accurate but DOI number not given".

### 2.2 Disputed values and settlement

| model_arm (Pass A name) | refs_generated | Pass A — "All correct" (sessions) | Pass B — "Accurate references" (sessions) | DOI-not-given included in B (= B − A) | **Settled n_fully_accurate** |
|---|---|---|---|---|---|
| ChatGPT-4 | 231 | 46 (10+17+19) | 86 (22+31+33) | 40 | **46** |
| ChatGPT-4.1 | 396 | 1 (0+0+1) | 81 (28+23+30) | 80 | **1** |
| ChatGPT-4.1 (web search) | 296 | 33 (12+12+9) | 152 (53+57+42) | 119 | **33** |
| Gemini 1.5 Pro | 193 | 7 (4+1+2) | 26 (9+7+10) | 19 | **7** |
| Gemini 2.5 Pro | 530 | 55 (10+11+34) | 159 (47+46+66) | 104 | **55** |
| Gemini 2.5 Pro (web search) | 301 | 71 (22+27+22) | 124 (40+47+37) | 53 | **71** |

Source location (all settled values): Table 4A (ChatGPT arms) and Table 4B (Gemini arms), row "All correct", summed over Session 1 + Session 2 + Session 3; category definition in Assessment of References (Material and Methods).

### 2.3 Why Pass A is right and Pass B is wrong

- The printed category **"correct (all information accurate)"** — the Table 4 sub-row "All correct" — matches strict fully accurate exactly: the study checked authorship, complete bibliographic details and proper DOI numbers, and this category is the one with **all** information accurate, i.e. no error in any checked field. It is mutually exclusive with every error category in the Assessment list. Mapping: **exact**.
- Pass B instead took the parent row "Accurate references". The paper's own definition of that row carries an explicit exception — "(**except perhaps a missing DOI**)" — and the row is the sum of "All correct" **plus** "Accurate but DOI number not given". DOI was a checked field ("proper DOI numbers" were rated), and the paper itself separates DOI-not-given from "All correct". A reference with no DOI therefore cannot be counted under strict fully accurate in this study, however retrievable it may be on its other fields. Pass B's count is broader than strict by exactly the DOI-not-given sub-row (40 / 80 / 119 / 19 / 104 / 53 per arm, table above). Mapping of B's count to strict: **not exact (broader)**. Note this is the same error pattern as Civelekler Pass B: counting the paper's headline "accurate/correct" total (existence / essentially-correct) instead of the strict all-fields sub-category the paper also prints.

---

## 3. Pastucha_2026 (R0696) — n_major_inaccuracy_incl_fabricated (Pass B only)

Pass A left this field blank for every arm. Pass B filled it by exact-by-sum. The question set for settlement: does the paper print a category (or an exact-by-sum of categories) whose definition matches the review's major inaccuracy — an error that would mislead a reader or prevent retrieval of the intended source, **including** completely fabricated references — exactly, per arm?

**Answer: No. Settled value = blank for all six arms. Pass A's blank stands; Pass B's values must not enter the pool.**

### 3.1 What the paper prints

Table 4 prints a parent row "Inaccurate references" with four mutually exclusive sub-rows (per session): "Accurate but wrong DOI number"; "Partially accurate: missing some information (no false information)"; "Partially accurate but with some false information"; "False reference".

Results text following Table 4 (verbatim, in order):

> "First, there were errors only in the DOI number, which happened more often with ChatGPT. The change was often minor, such as just in the last digit, but it meant that a completely different paper was being referenced. Next, some references were partially correct, with only some missing information, but more significant were those with additional false information (for example, with added incorrect authors). When examined more closely, it seems these names appeared on the same page, and were often authors of other cited works. Sometimes there were correct names but the order of the authors was wrong, and occasionally, instead of the authors' names, the organization to which they belong was given. Finally, there were totally false references ('hallucinations') that occurred for 1% to 22% of those given by ChatGPT, and 0% to 26% for Gemini."

Discussion reinforces the wrong-DOI point:

> "Although the difference in a DOI number is often small, like a change in the last digit, the result is actually serious because the wrong DOI refers to a different paper."

Figure 4 legend glosses the four error types as: "correct authors/title but wrong DOI; missing bibliographic elements; extraneous information added; wholly incorrect citations."

### 3.2 Pass B's sum — arithmetic correct, mapping not exact

| model_arm (Pass A name) | Wrong DOI | + Partially false info | + False reference | = Pass B major | Missing-info (excluded by B) | Total "Inaccurate references" (= gen − Accurate) |
|---|---|---|---|---|---|---|
| ChatGPT-4 | 10 | 51 | 17 | 78 | 67 | 145 |
| ChatGPT-4.1 | 13 | 183 | 82 | 278 | 37 | 315 |
| ChatGPT-4.1 (web search) | 11 | 92 | 7 | 110 | 34 | 144 |
| Gemini 1.5 Pro | 1 | 103 | 30 | 134 | 33 | 167 |
| Gemini 2.5 Pro | 10 | 243 | 103 | 356 | 15 | 371 |
| Gemini 2.5 Pro (web search) | 0 | 39 | 4 | 43 | 134 | 177 |

All component counts are the Table 4A/4B session sums and were re-added for this settlement; Pass B's addition is correct. The failure is definitional, component by component:

1. **"Accurate but wrong DOI number" — does meet major, in isolation.** The paper states a wrong DOI meant "a completely different paper was being referenced" / "refers to a different paper". That is a DOI / identifier set pointing to a different publication, expressly included in the review's major definition.
2. **"False reference" — does meet major, in isolation.** Printed as "totally false" in the Assessment list and "totally false references ('hallucinations')" in Results: completely fabricated, expressly included in major.
3. **"Partially accurate but with some false information" — does NOT uniformly meet major, and cannot be split from what is printed.** The bucket is defined only by the presence of "some false information". The paper's own examples for this bucket span materially different cases: added incorrect authors (misattribution — major-like); "correct names but the order of the authors was wrong" (all correct authors present, same publication, retrievable and credited to the same authors — as printed this does not establish that retrieval is prevented or that the source is misattributed to a different work, and it falls on the review's minor side: an error where "the source remains the same publication, remains retrievable from the rest of the reference, and remains correctly credited in the main"); and the authors'/organisation substitution case. Figure 4's gloss for the bucket, "extraneous information added", likewise does not by itself establish prevention of retrieval or misattribution. The paper prints **no sub-count** separating the misattributing cases from the order-only / extraneous cases inside this bucket, in any arm.
4. Therefore the sum in the table above **covers more than** the review's major definition (it includes every partial-false case, major and non-major alike). Under mapping rules 2, 3 and 5 a broader count — including a broader exact-by-sum — maps to **no** review outcome. "Near enough is not exact" (rule 4).

### 3.3 Why no other printed mapping rescues a major count

- The parent row "Inaccurate references" (145 / 315 / 144 / 167 / 371 / 177) is broader still: it adds "Partially accurate: missing some information (**no false information**)" — missing-only cases, which the review counts as minor, not major. This is the reason Pass A gave for leaving the field blank, and it is correct as far as it goes; the present settlement adds that Pass B's attempt to repair it by summing the other three sub-rows also fails exactness, for the reason in §3.2(3).
- No single printed category is labelled or defined as major inaccuracy, and no severity split in the paper corresponds to the review's retrieval/misattribution threshold.

**Settlement: blank for all six arms.** Pass B's component counts and sums (table in §3.2) are retained for narrative synthesis under their printed labels only.

---

## 4. Summary of settled values

| study_id | model_arm (Pass A name) | field | settled value | wrong pass |
|---|---|---|---|---|
| Civelekler_2026 | DeepSeek-R1 | n_fully_accurate | blank | A and B |
| Civelekler_2026 | ChatGPT (GPT-5.1) | n_fully_accurate | blank | A and B |
| Civelekler_2026 | Copilot (Microsoft Copilot 4.2) | n_fully_accurate | blank | A and B |
| Civelekler_2026 | Gemini (Google Gemini Ultra 2.5) | n_fully_accurate | blank | A and B |
| Pastucha_2026 | ChatGPT-4 | n_fully_accurate | 46 | B |
| Pastucha_2026 | ChatGPT-4.1 | n_fully_accurate | 1 | B |
| Pastucha_2026 | ChatGPT-4.1 (web search) | n_fully_accurate | 33 | B |
| Pastucha_2026 | Gemini 1.5 Pro | n_fully_accurate | 7 | B |
| Pastucha_2026 | Gemini 2.5 Pro | n_fully_accurate | 55 | B |
| Pastucha_2026 | Gemini 2.5 Pro (web search) | n_fully_accurate | 71 | B |
| Pastucha_2026 | ChatGPT-4 | n_major_inaccuracy_incl_fabricated | blank | B (A's blank stands) |
| Pastucha_2026 | ChatGPT-4.1 | n_major_inaccuracy_incl_fabricated | blank | B (A's blank stands) |
| Pastucha_2026 | ChatGPT-4.1 (web search) | n_major_inaccuracy_incl_fabricated | blank | B (A's blank stands) |
| Pastucha_2026 | Gemini 1.5 Pro | n_major_inaccuracy_incl_fabricated | blank | B (A's blank stands) |
| Pastucha_2026 | Gemini 2.5 Pro | n_major_inaccuracy_incl_fabricated | blank | B (A's blank stands) |
| Pastucha_2026 | Gemini 2.5 Pro (web search) | n_major_inaccuracy_incl_fabricated | blank | B (A's blank stands) |

Machine-readable version: `robustness/settle-2.csv`.
