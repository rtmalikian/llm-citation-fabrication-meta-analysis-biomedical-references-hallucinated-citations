# Settlement 4a — Omission disputes: Mugaanyi_2024, Metze_2024, Nieves-Lopez_2026

**Role:** Settlement Reader 4a, Robustness Pass (23 October 2026), Review 2 (fabricated / inaccurate LLM citations), Cochrane-style meta-analysis series.
**Scope:** Three studies where Pass B filled outcome cells that Pass A left blank (Mugaanyi_2024, Metze_2024), plus the reverse omission in Mugaanyi_2024 (`n_fully_accurate`, filled by A only), and the Nieves-Lopez_2026 `n_major_inaccuracy_incl_fabricated` cells (filled by B only).
**Sources re-read for this settlement only:** `fulltexts/R0391.xml` (Mugaanyi_2024), `fulltexts/R0570.xml` (Metze_2024), `fulltexts/R1103.xml` (Nieves-Lopez_2026), `extraction-form.md`, `extraction-passA.csv`, `extraction-passB.csv`. The manuscript and analysis files were **not** read.
**Machine-readable companion:** `robustness/settle-4a.csv` (Pass-A arm names throughout; blank in the CSV = settled blank, i.e. not extractable for the pool — narrative use only under the printed label; blank never means zero).

## Rules applied (extraction-form.md)

Review definitions, fixed:

- **Completely fabricated:** "no matching publication exists. Verification against the named source finds no publication that matches on title and source identity in a way that could count as the same work. A reference that takes a real title and attaches wrong authors, or takes real authors and attaches a title that does not exist, counts here if no single matching publication exists."
- **Major inaccuracy:** "any major inaccuracy, including completely fabricated. An error that prevents retrieval of the intended source, or that misattributes the source… Minor errors that leave the source findable and correctly credited do not count here."
- **Fully accurate, strict:** "accurate on all fields checked by the study. Authors, title, journal or source, year, and volume, pages and DOI where the study checked them must all be correct. Any error in a checked field, major or minor, removes the reference from this count."
- **Minor error:** "an error in one field where the source remains the same publication, remains retrievable from the rest of the reference, and remains correctly credited in the main."

Mapping rules: Rule 2 — a printed count maps "only if the study printed definition covers the same cases as the review definition, no more and no fewer"; Rule 3 — a broader study definition maps to no review outcome; Rule 5 — a summed mapping is allowed only where the parts "sum, without overlap, to a review definition exactly"; Rule 6 — a count may be derived from a percentage with a denominator "only if the percentage and denominator give a whole number without rounding doubt"; Rule 7 — a printed accurate count maps to strict only if the study "checked all fields its accurate label claims and counted any error in a checked field against accuracy".

**Headline settlements**

- **Mugaanyi_2024:** `n_fabricated` = **15** (Pass B correct, Pass A wrong by omission); `n_fully_accurate` = **blank** (Pass B correct, Pass A's 37 wrong).
- **Metze_2024:** `refs_generated` = **260** (both passes agree); all four Pass B values settle as filled — `n_fabricated` = **194**, `n_major_inaccuracy_incl_fabricated` = **194**, `n_fully_accurate` = **30**, `n_minor_error` = **36** (Pass B correct, Pass A wrong by omission). One internal contradiction in the paper is flagged (Table 1 vs Results text, §2.4) — flagged only, not corrected.
- **Nieves-Lopez_2026, `n_major_inaccuracy_incl_fabricated`:** ChatGPT-5.4 = **blank**, Gemini-3 = **blank** (Pass A correct, Pass B's 161 / 128 wrong); Copilot = **26** (Pass B's value correct, Pass A wrong by omission — for a different reason than Pass B gave, §3.3).

---

## 1. Mugaanyi_2024 (R0391.xml) — natural-sciences subset only

Extraction is the biomedical subset only: 5 natural-sciences (clinical/biomedical) topics, **55 references**, one GPT-3.5 arm (Pass-A arm name: "ChatGPT (GPT-3.5) - natural sciences (clinical/biomedical) topics only"). The humanities subset (47 citations) is not extracted. `refs_generated` = 55 is agreed and matches the paper ("A total of 102 citations were generated, with 55 in the natural sciences and 47 in the humanities" — Results, Included Topics and Citations).

### 1.1 What the paper prints (verbatim)

Table 2, "Data analysis results", Natural sciences column (n=55):

> "Citation exists, n (%) — 40 (72.7)"; "Citation accurate, n (%) — 37 (67.3)"; "Relevant, n (%) — 39 (70.9)"; "DOI exists, n (%) — 39 (70.9)"; "DOI accurate, n (%) — 18 (32.7)"; "DOI hallucination, n (%) — 34 (61.8)".

Methods, Data Collection and Validation:

> "The researchers then independently validated the references by conducting searches on Google Scholar, PubMed, and Google Search for each cited reference. The primary objective was to confirm the existence and accuracy of the cited literature. DOI existence and validation were confirmed using the DOI Foundation website."

> "Two researchers independently prompted ChatGPT (GPT-3.5) to write sections of a manuscript while adhering to the American Psychological Association style for citations and including the DOI of each reference."

Results, Included Topics and Citations:

> "The existence, validity, and relevance of citations were examined irrespective of the corresponding DOIs."

Results, Citation Existence and Accuracy:

> "Of the 102 generated citations, 76 (74.5%) were found to be real and exist in the published literature, with 72.7% and 76.6% of the citations verified in the natural and humanities group, respectively."

Abstract, Results: "Among these, 40 citations (72.7%) in the natural sciences and 36 citations (76.6%) in the humanities were confirmed to exist".

### 1.2 `n_fabricated` — SETTLED: 15. Pass B correct; Pass A wrong (omission)

**Question set:** does the paper print a fabricated / non-existent count for the natural-sciences subset matching "no matching publication exists"? **Answer: yes, in substance — as the exact complement of a printed binary existence count on the same printed denominator.**

- Table 2 prints an existence verdict for every one of the 55 subset citations: 40 "confirmed to exist" / "found to be real and exist in the published literature", verified by search on the study's named sources (Google Scholar, PubMed, Google Search). Existence here is a yes/no verdict on the citation as cited, and the paper prints no third, indeterminate category. The non-existent remainder is therefore 55 − 40 = **15**, with no cases left over and none double-counted.
- That remainder is exactly the review's completely fabricated: a citation not found to be real and existing in the published literature on verification against the named sources is a citation for which no matching publication exists. Wording differs ("exists" vs "fabricated"); coverage does not, which is what Rule 2 tests.
- Pass A left the cell blank because "no fabricated count is printed as such". That demands a printed *label*, not a printed *count*: Rule 1 (extract as printed) is satisfied by the printed exists count and printed denominator, and the complement of a binary printed count on its own denominator is arithmetic on printed numbers of the same kind the review already accepts for pooled session sums — it introduces no case the paper did not classify. Pass A's blank was an omission error.
- Two things 15 does **not** rest on, stated to avoid confusion: (i) the paper's general hallucination sentence — "hallucination refers to instances where ChatGPT 3.5 generates DOIs and/or citations that do not correspond to actual, valid DOIs/citations" (Methods) — which mixes incorrect with nonexistent and is broader than the review definition; (ii) "DOI hallucination" 34/55, which is the bad-DOI outcome (a DOI that did not exist or was matched to a different source), a different field, already agreed by both passes. The settled 15 rests solely on the Citation-exists complement.

### 1.3 `n_fully_accurate` — SETTLED: blank. Pass B correct; Pass A's 37 wrong

**Question set:** does the paper print a strict fully-accurate count (no error in any checked field) for the subset? **Answer: no.**

- Pass A's 37 is Table 2's "Citation accurate". The paper states that citation existence, validity and relevance "were examined **irrespective of the corresponding DOIs**" (Results, quoted §1.1). DOI was a checked field in this study: the prompt required a DOI for each reference, DOI existence/accuracy were validated separately against the DOI Foundation website, and Table 2 reports them in separate rows.
- Strict fully accurate requires every checked field correct, DOI included, with any error in a checked field removing the reference. A count taken irrespective of DOIs cannot meet that definition, and the arithmetic proves the defect is real, not hypothetical: only 18/55 citations have an accurate DOI, so a citation-accurate count that also required DOI accuracy could be at most 18; the printed 37 necessarily includes at least 19 citations without an accurate DOI, each of which fails strict. The mapping is broader than strict and fails Rules 2, 3 and 7.
- The exact strict count cannot be derived either: the paper nowhere prints the overlap between the 37 citation-accurate citations and the 18 DOI-accurate citations. Settled value is therefore **blank** (37 retained for narrative synthesis under its printed label, "Citation accurate", assessed irrespective of DOIs). Pass B left the cell blank for exactly this reason and was correct; Pass A was wrong to fill it.

---

## 2. Metze_2024 (R0570.xml) — ChatGPT-4 arm

### 2.1 `refs_generated` — SETTLED: 260 (both passes agree; not a subset denominator)

Results text:

> "A total of 260 references were released (zero to five per reply), classified as follows: a) 11.54 % "Correct", b) 13.85 % "With incorrect data" and c) 74.62 % as "Hallucinations"."

Design, as printed: the prompt — "Please write a summary on the professional and scientific activities of (professor's full name) in the area of pathology or clinical pathology or hematology or neuropathology or microbiology or immunology or biochemistry or molecular mechanisms or cytology and add the most relevant literature, citing at least five references" — was submitted daily over a 10-day period (16‒25 October 2023) for 19 professors. Only 8 professors were ever recognised, and Table 1's per-professor "Retrieved references" row (40 + 35 + 25 + 35 + 10 + 25 + 40 + 50) sums to the same 260.

**Subset question, answered directly:** B's numbers do **not** come from a subset or a different denominator than the arm's full reference set. 260 is every reference the arm released; the 11 unrecognised professors contributed zero references (no reply, no references), so there is no released reference outside the 260 and no larger denominator the percentages could belong to. The 260 is subset-*generated* (recognised professors only) but it is the arm's complete generated set, exactly as Pass A also recorded it.

### 2.2 Printed categories and the Rule 6 derivation

Methods:

> "The quality of the replies was checked by two observers comparing them with data from PUBMED, Web of Science, Google Scholar as well as Lattes database, which is an official platform of curricula supported by CNPq (National Council of Research) of the Federal Government."

> "References were classified as: a) Correct, b) With incorrect data but possibility of recovering the publication, or c) Hallucination with non-existing titles or existing publications written by others, but erroneously attributed to the person under investigation."

Pass A extracted no outcome counts ("Counts not printed; percentages only (no back-calculation)"). Pass B derived counts from the printed percentages against the printed total of 260 under Rule 6. The derivation was re-checked for this settlement; each percentage determines **one** whole number with no rounding doubt:

| Category | Printed % | % × 260 | Settled count | Neighbour check (count/260, rounded to 2 dp) |
|---|---|---|---|---|
| (a) Correct | 11.54% | 30.004 | **30** | 29 → 11.15%; 31 → 11.92% |
| (b) With incorrect data | 13.85% | 36.01 | **36** | 35 → 13.46%; 37 → 14.23% |
| (c) Hallucinations | 74.62% | 194.012 | **194** | 193 → 74.23%; 195 → 75.00% |

Partition check: 30 + 36 + 194 = 260, the printed total. Rule 6 is satisfied for all three categories, so Pass A's refusal to derive was an omission error in method; whether each derived count *maps* is settled cell by cell in §2.3.

### 2.3 The four disputed cells — SETTLED: all four Pass B values stand; Pass A wrong on all four

| Field | Pass A | Pass B | **Settled** | Wrong pass |
|---|---|---|---|---|
| `n_fabricated` | blank | 194 | **194** | A |
| `n_major_inaccuracy_incl_fabricated` | blank | 194 | **194** | A |
| `n_fully_accurate` | blank | 30 | **30** | A |
| `n_minor_error` | blank | 36 | **36** | A |

- **`n_fabricated` = 194 — exact.** Category (c) has two limbs, and both are the review's completely fabricated. "Non-existing titles": no publication with that title exists, so no matching publication exists. "Existing publications written by others, but erroneously attributed to the person under investigation": as cited — that title under the investigated professor's authorship — no single matching publication exists, which is precisely the review's hybrid case ("takes a real title and attaches wrong authors… counts here if no single matching publication exists"). Neither limb admits a case in which the reference as cited matches an existing publication, and every no-matching-publication case in this study's design falls in (c): a reference whose publication exists and is the professor's own is (a) or (b) by construction. Coverage is the same, no more and no fewer (Rule 2).
- **`n_major_inaccuracy_incl_fabricated` = 194 — exact.** Major is fabricated plus any other error that prevents retrieval or misattributes the source. Category (c) is wholly major (above). Category (b) contributes nothing to major: its defining test is that the publication can be recovered despite the incorrect data, so retrieval is not prevented; and misattribution of a publication to a different person is, by the paper's own category definitions, a category-(c) case, not a (b) case — a (b) reference remains the investigated professor's own publication, correctly credited in the main, with incorrect data. Category (a) has no incorrect data at all. Major therefore equals (c) alone: **194**, a single-category mapping, not a sum. (Pass B recorded the same reasoning; it is confirmed.)
- **`n_fully_accurate` = 30 — exact (strict).** The three categories are an exhaustive partition of the 260, and the partition is drawn on incorrect data: any reference with incorrect data is (b) if the publication is recoverable or (c) if it is not a real, correctly attributed publication. Category (a) "Correct" is what remains — a reference with no incorrect data in the bibliographic data checked against PubMed, Web of Science, Google Scholar and the Lattes database. That is strict fully accurate as the review defines it: accurate on all fields checked by the study, with any error in a checked field (major or minor — both are captured by (b)/(c)) removing the reference. Rule 7 is met because the paper does state, through its category definitions, what "Correct" excludes: incorrect data of any kind.
- **`n_minor_error` = 36 — exact.** Category (b), "With incorrect data but possibility of recovering the publication", is the review's minor error in substance: the source remains the same publication (it is *the* publication that is recovered), remains retrievable (recoverability is the category's defining test), and remains correctly credited in the main (authorship misattribution to another person is a category-(c) case by definition, so no (b) reference is misattributed). The review's major definition expressly excludes such cases ("Minor errors that leave the source findable and correctly credited do not count here"), and (b) is the study's only category on the minor side of that line. Pass B's mapping is confirmed.

### 2.4 Flagged contradiction (form field 45 — flag only, do not correct)

The Results-text partition settled above is internally consistent (percentages uniquely determine counts summing exactly to 260). Table 1, however, does not reconcile with it on the hallucination outcome: multiplying Table 1's per-professor "% of references with hallucinations" row by its "Retrieved references" row gives 27 (67.5% of 40) + 35 (100% of 35) + 25 (100% of 25) + 35 (100% of 35) + 1 (10% of 10) + 21 (84% of 25) + 26 (65% of 40) + 15 (30% of 50) = **185** hallucinated references, not 194 — a difference of 9. Each Table 1 product is a whole number, so the gap is not rounding. Neither pass noted this (Pass B's batch notes record "no internal contradictions", having checked only that the retrieved-references row sums to 260). **Settlement position:** the values in §2.3 stand on the Results classification sentence, which is the paper's only complete three-category classification of the full 260 and the source of the arm's denominator in both passes; the Table 1 conflict is unresolved within the paper and is flagged here for the author. It is not corrected, and no alternative count (185) is substituted, because Table 1 prints no per-professor split of Correct vs With-incorrect-data and cannot support a competing full partition.

---

## 3. Nieves-Lopez_2026 (R1103.xml) — `n_major_inaccuracy_incl_fabricated`, three arms

Both passes agree on `refs_generated` (703 / 796 / 929), `n_fabricated` (complete fabrication: 32 / 11 / 26) and `n_fully_accurate` (real: 542 / 668 / 903); none of those is in dispute here. The dispute is only whether Pass B's total-fabricated values (161 / 128 / 26) map to the review's major inaccuracy. Pass A left the field blank on all three arms.

### 3.1 Printed definitions and counts (verbatim)

Methods (Data Set), the complete classification paragraph:

> "A real reference consisted of accurately naming all parts of an existent reference, including the name of the authors, title, journal information, publication year, and the website link. If every component of the reference provided by the LLMs were non-existent, it was categorized as a complete fabricated reference. If some of the components of the reference were incorrect, non-compatible, or non-existent, it was categorized as a partial fabricated reference."

Results, Reference Fabrication Rates:

> "ChatGPT-5.4 provided 703 references in total… From these references, 542 (77.1%) were real and 161 (22.9%) were fabricated… From the 161 fabricated references, 80.1% (129/161) were partially fabricated and 19.9% (32/161) were completely fabricated."

> "Gemini-3 provided 796 references in total… From these references, 668 (83.9%) were real and 128 (16.1%) were fabricated… From the 128 fabricated references, 91.4% (117/128) were partially fabricated and 8.6% (11/128) were completely fabricated."

> "Copilot provided 929 references in total… From these references, 903 (97.2%) were real and 26 (2.8%) were fabricated… From the 26 fabricated references, 0.0% (0/26) were partially fabricated and 100.0% (26/26) were completely fabricated."

Table 5, "Fabricated/total" row: ChatGPT-5.4 161/703; Gemini-3 128/796; Copilot 26/929; with Complete 32 / 11 / 26 and Partially 129 / 117 / 0. The three categories are exhaustive and mutually exclusive per arm (542 + 129 + 32 = 703; 668 + 117 + 11 = 796; 903 + 0 + 26 = 929).

Pass B's mapping claim, in its own words: major = the paper's total fabricated label (complete + partial), "because every partial has an incorrect, non-compatible or non-existent identity component (authors, title, journal, year or link)".

### 3.2 ChatGPT-5.4 and Gemini-3 — SETTLED: blank. Pass A correct; Pass B wrong (161, 128)

Pass B's claim over-reads the printed definition. The paper does **not** print that every partial has a fabricated *identity* component; it prints that a partial is a reference in which "**some** of the components… were **incorrect**, non-compatible, or non-existent". "Incorrect" alone, in any single component, is sufficient for the category. The components are authors, title, journal information, publication year and website link. A reference that names a real publication correctly on authors, title, journal and year but gives an incorrect website link is a partial fabrication under the printed definition — yet for the review it is a minor error: same publication, retrievable from the rest of the reference, correctly credited. A single incorrect publication year with everything else correct is in the same position. Neither prevents retrieval nor misattributes the source, so neither is major.

The partial bucket therefore mixes, in unknown proportions:

- major cases — e.g. a fabricated title or fabricated authors, where no matching publication exists as cited (these also belong inside major via fabricated); and
- minor cases — a single incorrect non-identity component (link, year) on an otherwise correctly named, retrievable, correctly credited real publication.

The paper prints no sub-count splitting the 129 (ChatGPT-5.4) or 117 (Gemini-3) partials by which component was wrong, by severity, or by retrievability — not in the Results text, not in Table 4 (means per question only) and not in Table 5 (complete/partial split only). The sum complete + partial is consequently **broader** than the review's major inaccuracy, and under Rules 2, 3 and 5 a broader count — including a broader exact-by-sum — maps to no review outcome. No other printed category or sum in the paper isolates major, so the settled value is **blank** for both arms (the 161 / 128 totals and the 129 / 117 partial counts are retained for narrative synthesis under their printed label, "fabricated" / "partially fabricated"). This is the same failure pattern settled in settle-2 for Pastucha_2026's "partially accurate with some false information" bucket: a mixed bucket with no printed split cannot be summed into major.

### 3.3 Copilot — SETTLED: 26. Pass B's value correct; Pass A wrong (omission)

Copilot is the exception, and it turns on the printed zero. For this arm the partial category is empty: Partially 0 (Table 5; Results: "0.0% (0/26) were partially fabricated and 100.0% (26/26) were completely fabricated"). The exhaustive trichotomy therefore leaves only two populated categories: real (903), defined as accurately naming **all** parts of an existent reference — no inaccuracy of any degree — and completely fabricated (26), which is inside major by the review definition's express inclusion. There is no partial/minor residue in which a non-major error could hide, and no other error category in the paper. Major inaccuracy including fabricated is therefore exactly the completely fabricated count: **26**. Pass B's number is right, though not for Pass B's stated reason: the value settles because the partial bucket B summed is empty for this arm, so the sum collapses to the complete count alone. Pass A's blank, correct for the other two arms, was an omission here.

| Model arm | Pass A | Pass B | **Settled `n_major_inaccuracy_incl_fabricated`** | Wrong pass |
|---|---|---|---|---|
| ChatGPT-5.4 | blank | 161 | **blank** | B |
| Gemini-3 | blank | 128 | **blank** | B |
| Copilot | blank | 26 | **26** | A |

---

## 4. Summary of settled values

| study_id | model_arm (Pass A name) | field | settled value | wrong pass |
|---|---|---|---|---|
| Mugaanyi_2024 | ChatGPT (GPT-3.5) - natural sciences (clinical/biomedical) topics only | n_fabricated | 15 | A |
| Mugaanyi_2024 | ChatGPT (GPT-3.5) - natural sciences (clinical/biomedical) topics only | n_fully_accurate | blank | A |
| Metze_2024 | ChatGPT-4 | refs_generated | 260 | neither |
| Metze_2024 | ChatGPT-4 | n_fabricated | 194 | A |
| Metze_2024 | ChatGPT-4 | n_major_inaccuracy_incl_fabricated | 194 | A |
| Metze_2024 | ChatGPT-4 | n_fully_accurate | 30 | A |
| Metze_2024 | ChatGPT-4 | n_minor_error | 36 | A |
| Nieves-Lopez_2026 | ChatGPT-5.4 | n_major_inaccuracy_incl_fabricated | blank | B |
| Nieves-Lopez_2026 | Gemini-3 | n_major_inaccuracy_incl_fabricated | blank | B |
| Nieves-Lopez_2026 | Copilot | n_major_inaccuracy_incl_fabricated | 26 | A |

## 5. Actions implied for the merged dataset

1. **Mugaanyi_2024:** set `n_fabricated` = 15 (complement of Table 2 "Citation exists" 40/55, natural-sciences subset); set `n_fully_accurate` = blank (remove Pass A's 37; keep 37 in narrative as "Citation accurate", assessed irrespective of DOIs).
2. **Metze_2024:** fill all four outcomes from Pass B (194 / 194 / 30 / 36 on 260 generated), derived under Rule 6 from the Results-text percentages; carry the §2.4 Table 1 flag (weighted hallucination total 185 vs text 194) in the study's contradictions record for the author.
3. **Nieves-Lopez_2026:** keep `n_major_inaccuracy_incl_fabricated` blank for ChatGPT-5.4 and Gemini-3 (do not pool Pass B's 161 / 128; narrative only as total "fabricated"); set Copilot `n_major_inaccuracy_incl_fabricated` = 26.

Machine-readable version: `robustness/settle-4a.csv`.
