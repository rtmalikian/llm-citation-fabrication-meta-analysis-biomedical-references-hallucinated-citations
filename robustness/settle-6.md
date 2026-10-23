# Settlement Report 6 — Robustness Pass (23 October 2026)

**Role:** Settlement Reader 6 (new studies, batch 4), Review 2 — Cochrane-style meta-analysis of fabricated / inaccurate LLM citations (Raphael Malikian's series).
**Scope:** Six disputed items across six records from the two independent extraction passes `robustness/ft2/extraction-newA-batch4.csv` (Pass A) and `robustness/ft2/extraction-newB-batch4.csv` (Pass B). Every value below was re-read in the full text and settled against `extraction-form.md`: the fixed review definitions, mapping rule 1 (extract as printed), rule 2 (map only if exact — the study definition must cover the same cases as the review definition, no more and no fewer), rule 5 (exact by sum — separate printed counts may be summed only if, without overlap, they cover the review definition exactly and nothing else), rule 6 (derived counts only where a percentage at a stated denominator gives a whole number without rounding doubt), rule 7 (fully-accurate mapping needs the checked fields), and field 37 (blank means narrative only; it never means zero — a printed zero is data, an absent count is not a zero).
**Sources read:** `extraction-form.md`; the two batch-4 pass CSVs; full texts located via `robustness/ft2/retrieved-files.json` — `robustness/fulltexts2/R2931.xml`, `R3191.xml`, `R3578.xml`, `R4142.xml`, `R4263.xml`, `R4518.xml`. The manuscript and analysis files were **not** read.
**Machine-readable companion:** `robustness/settle-6.csv` (columns: record_id, study_id, model_arm, field, settled_value, wrong_pass, source_location). A blank settled value means the cell stays blank (not extractable), never zero.

**Summary of rulings**

| # | Record | Cell(s) | Pass A | Pass B | **Settled** | Wrong pass |
|---|---|---|---|---|---|---|
| 1 | R2931 | study_id | Idan_2025 | Daphna_2025 | **Idan_2025** | B |
| 2a | R3191 (Ohlsen_2026) | ChatGPT (GPT-4o) n_major | blank | 4 | **4** | A |
| 2b | R3191 | ChatGPT (GPT-4o) n_fully_accurate | blank | 2 | **blank** | B |
| 2c | R3191 | Gemini 2.5 Pro n_major | blank | 5 | **5** | A |
| 3 | R3578 (Pan_2026) | ChatGPT-4.0 (browsing) n_fabricated | 0 | blank | **blank** | A |
| 4a | R4142 (Gwon_2024) | ChatGPT n_fabricated | 1095 | 211 | **211, denominator 403** (total over 1,287 not extractable) | A |
| 4b | R4142 | Bing AI n_major | blank | 28 | **28** | A |
| 5 | R4263 (Zhu_2025) | ChatGPT-4 n_major / n_minor_error | blank / blank | 0 / 0 | **0 / 0** | A |
| 6 | R4518 (Bridges_2025) | ChatGPT-4 n_bad_doi | 125 | 42 | **125** | B |

Note on the task brief: it describes R3191 as "two arms with 6 references each". The paper prints 6 references for ChatGPT and **32** for Gemini; the settlements below use the printed denominators (6 and 32).

---

## 1. R2931 — study_id: SETTLED `Idan_2025`; Pass B wrong

**Paper's author list (full-text XML, front matter, first `<contrib>`):**

> `<surname>Idan</surname><given-names initials="D">Daphna</given-names>` — rendered in the article header as "Idan Daphna", followed by Ben-Shitrit Itamar, Volevich Mark, Binyamin Yair, Nassar Raouf, Nassar Majd, Abelson Nitzan, Zlotnik Alexander, Einav Sharon.

The first author is **Daphna Idan**: given name Daphna, surname **Idan**. The paper's own competing-interests statement confirms the full name in given-name-first order: "Daphna Idan, Itamar Ben-Shitrit, and Mark Volevich are medical students at their respective universities and are employed by Medint."

Study IDs in this review are FirstAuthorSurname_Year, and the paper was published in 2025 (Sci Rep 2025;15:37824; DOI 10.1038/s41598-025-21689-w). Settled study_id: **Idan_2025**.

**Why B is wrong:** Pass B used the first author's *given* name (Daphna) as if it were the surname, producing Daphna_2025; the error is repeated in Pass B's conflicts note ("Daphna, Ben-Shitrit and Volevich employed by Medint"). Pass A's Idan_2025 and its conflicts note ("Idan, Ben-Shitrit and Volevich…") match the printed author list. No other field in this record is affected.

---

## 2. R3191 — Ohlsen_2026: ChatGPT n_major SETTLED 4 (A wrong); ChatGPT n_fully_accurate SETTLED blank (B wrong); Gemini n_major SETTLED 5 (A wrong)

**Review definitions applied (extraction-form.md).** Major inaccuracy includes a completely fabricated reference; "a journal, year, volume or page set that points to a different publication or to no publication"; and "a real publication cited for a claim or topic it does not cover where the study counts that as misattribution". Fully accurate (strict) requires accuracy "on all fields checked by the study", and rule 7 allows an accurate count to map only if the study checked the fields its label claims and counted any error in a checked field against accuracy.

**What the paper prints — denominators and the abstract's lumped label (Abstract):**

> "ChatGPT provided 6 study references, of which 4 were nonexistent or inappropriately cited. Gemini provided 32 study references, of which 5 studies were nonexistent or inappropriately cited."

The abstract label lumps two different failures, and for Gemini it is not even accurate as a lump (all 5 Gemini problem references were found — see Table III). The mapping therefore cannot rest on the abstract label; it rests, as the task requires, on the per-reference verdicts in Results and Tables III–IV, which decompose the lump completely.

**ChatGPT arm (6 references) — Results text:**

> "ChatGPT provided references to nonexistent studies in 3 (50%) of cases, and when asked for the link, responded with an apology and a statement that the article could not be found. A fourth reference was incorrectly cited as being published in "Bone & Joint Journal" when the referenced article had been published in the Journal of Orthopaedics. Only 2 (33%) of the citations provided by ChatGPT led to articles that were both appropriately referenced and provided data supporting the claim made in the LLM's response."

Table IV ("ChatGPT responses with issues with referenced studies") lists exactly 4 issue rows: three with "Study able to be found? **No**", and one with "**Yes**" — the Bone & Joint Journal row (link led to the Journal of Orthopaedics article, doi:10.3928/01477447-20210618-09; PMID: 34292834).

- **n_major = 4 — exact by sum (rule 5).** Parts, mutually exclusive and jointly exhaustive of the arm's major cases: (i) 3 nonexistent references — completely fabricated, hence major by the review definition's first clause; (ii) 1 real article attributed to the wrong journal — the journal element of the citation points to no publication in the named journal and misattributes the source, the review definition's journal clause. The remaining 2 references are the only ones the paper clears. 3 + 1 = **4**. Pass B's value stands. **Pass A is wrong on this cell:** its objection — that the combined label "nonexistent or inappropriately cited" mixes bibliographic accuracy with claim support — is true of the *abstract label* but does not survive the paper's own decomposition; Tables III–IV and the Results paragraph give a separate, bibliographically concrete verdict for every one of the 4 references, and each verdict falls inside the review's major definition on its own terms.
- **n_fully_accurate = blank — not exact (rule 7).** The count "2" is defined by a conjunction the review's strict definition does not use: the article was "both appropriately referenced **and** provided data supporting the claim". The paper never states which bibliographic fields it checked for "appropriately referenced" (no field list — authors, title, year, volume, pages, DOI — is given anywhere), and the conjunction cuts both ways against exactness: a bibliographically perfect reference whose data did not support the claim is excluded, and nothing printed shows the 2 survivors were verified correct on all bibliographic fields. The count therefore maps to neither strict nor lenient fully accurate. **Pass B is wrong on this cell** (it recorded the 2 as "EXACT as printed"); **Pass A is right to leave it blank.** Pass B is also internally inconsistent here: it left the Gemini arm's fully accurate blank for exactly this reason ("bibliographic field accuracy not itemised", rule 7) while filling the ChatGPT arm's analogous count.

**Gemini 2.5 Pro arm (32 references) — Results text:**

> "Gemini provided journal references for all 12 (100%) queries. Within its responses, 32 PubMed articles were cited, with links provided. Of these, there were 5 (16%) articles that were inappropriately cited (Tables III and IV). Two (6%) of these articles compared incorrect surgeries (one article evaluated arthroscopic rotator cuff and biceps tenodesis procedures, and another article compared reverse versus anatomic shoulder arthroplasty when the query specifically asked about anatomic versus hemiarthroplasty) yet were inaccurately cited as evidence to support the claims made in response to glenohumeral arthritis recommendations. Three (9%) articles that were included did not support the statement being made by Gemini and sometimes were in complete contradiction. The remaining 27 references were appropriately supportive of the data or claims made by Gemini in each respective response."

Table III ("Gemini responses with issues with referenced studies") lists the problem references with "Study able to be found? **Yes**" for every row, each identified by DOI/PMID — all 5 are real publications. Both passes agree n_fabricated = 0 for this arm.

- **n_major = 5 — exact.** Each of the 5 is a real publication cited for a claim or topic it does not cover (wrong-surgery comparisons ×2; non-supporting or contradicting sources ×3), and the study counts exactly that as misattribution ("inappropriately cited", "inaccurately cited as evidence to support the claims"). That is the review major definition's final clause in substance, word for word in coverage. **Pass B's value stands; Pass A is wrong on this cell:** Pass A treated a claim-support classification as wholly outside the review outcomes, overlooking that the form's major definition expressly includes this case. (The Discussion's summary — "4 (67%) of ChatGPT references and 5 (16%) of Gemini references were confabulated, inaccurately cited, or did not support the claims" — is consistent with the decomposed counts 4 and 5.)

---

## 3. R3578 — Pan_2026, ChatGPT-4.0 (browsing) n_fabricated: SETTLED blank (not extractable); Pass A wrong

**What the paper prints.** Methods (source authenticity assessment):

> "By searching the reference materials in DeepSeek-R1 and ChatGPT-4.0, and eliminating false information, we derived the authentic reference materials and recorded the time of their creation."

Results (reference source analysis):

> "DeepSeek-R1 provided 25 papers, of which 4 contained false information, while ChatGPT provided 23. Clinical guidelines dominated both corpora, accounting for 38.1% (8/21) of DeepSeek citations and 47.8% (11/23) of ChatGPT citations."

Abstract:

> "DeepSeek cited 21 sources and ChatGPT-4.0 23; clinical guidelines predominated in both corpora (38.1 vs. 47.8%, respectively). … In addition, DeepSeek-R1 provided 4 reference links were invalid."

The **only** false-information count printed anywhere in the paper — abstract, Results, Figures 4–5 and their captions — is DeepSeek-R1's 4. For ChatGPT-4.0 the paper prints a provided count (23) and source-type percentages on denominator 23, but it nowhere prints a false count of 0, the words "no false information" / "none", or a statement that all 23 ChatGPT references were authentic. The ChatGPT figure caption (Figure 4) is a source-type breakdown, not an authenticity count.

**Settlement: blank.** Pass A's 0 is an *imputation*: because the source-type percentages retain denominator 23, Pass A inferred that no ChatGPT reference was eliminated. That inference is not a printed count, and the form forbids it — rule 1 (record counts exactly as printed) and field 37 (blank never means zero). The inference is also unsafe on this paper's own text: the authors shift between generated and retained counts without labelling (DeepSeek is "provided 25" in Results but "cited 21" in the Abstract and "supplied 21 references" in the timeliness paragraph), so equating ChatGPT's two 23s assumes precisely the fact that would have to be proved. Contrast a real printed zero: Zhu_2025 (item 5 below), where Table 1 prints explicit "0 (0)" cells — that is what a printed zero looks like, and Pan_2026 has none for this arm. **Pass B is right** ("zero false is never stated… never imputed as zero"); **Pass A is wrong.** The narrative fact for the synthesis is: 23 references provided, source-type analysis on all 23, no false-reference count reported for this arm.

---

## 4. R4142 — Gwon_2024

### 4a. ChatGPT arm n_fabricated: SETTLED 211 on denominator 403; Pass A's 1095 is not a printed count and is wrong; the total over 1,287 is not extractable

**The grading system as printed (Abstract; Methods, Quality Assessment):**

> "We classified its answers into 4 grades if the title existed: A, B, C, and F. No grade was given for a fake title or no answer."

**Grade F definition (Table 1 and accompanying text):**

Table 1, grade F row: title actually exists = Yes; "Title matched, but not other essential information". Text:

> "A grade of "F" was given to an answer that was inconsistent with the author, journal, or publication year of the actual study that matched the title, making it impossible to be specified. Thus, it was considered as a fake study that was generated."

**Counts as printed (Abstract; Table 2 totals):** ChatGPT presented **1,287** studies; grades A 7, B 18, C 167, **F 211** — graded total 7 + 18 + 167 + 211 = **403**; ungraded = 1,287 − 403 = **884**.

**Review definition applied.** Completely fabricated = no matching publication exists, expressly including a reference that "takes a real title and attaches wrong authors … if no single matching publication exists". A grade-F reference is exactly that: a real title carrying author/journal/year that match no publication as cited — the paper itself calls it "a fake study that was generated". Grade F therefore maps exactly to review fabricated, and **211 is the only fabricated count the paper prints**.

**Why 1095 (Pass A) is wrong.** Pass A added the 884 ungraded studies to F (211 + 884 = 1095), treating every ungraded study as a fake title. The paper contradicts that premise in its own grading rule — "No grade was given for a fake title **or no answer**" — the ungraded bucket is a *mixture* of fake-title answers and no-answer responses, and the paper's text confirms no-answer cases occurred ("For comprehensive questions, ChatGPT did not give an answer, saying that it did not have the capability…"; "there were cases where the answer was "no capability" or "no RCT found""). No count separating fake titles from no-answers within the 884 is printed anywhere (Abstract, Results, Tables 1–2). 1095 therefore rests on an invented split; it appears nowhere in the paper and fails rules 1, 2 and 5. (Pass A's derivation also double-counts conceptually: a "no answer" response generated no reference at all, so it cannot be a fabricated reference.)

**Denominator pairing.** The printed fabricated count **211 pairs with 403**, the graded (title-existed) set to which the grading — and hence the F count — applies. Pairing 211 with 1,287 would silently treat all 884 ungraded items as non-fabricated, which the paper does not support (an unknown number of them *are* fake titles). Consequently:

- Mapped pair supported by the printed data: **n_fabricated = 211 / 403 graded studies**, scope-flagged as the title-existed subset.
- The arm-level fabricated total over all 1,287 presented studies is **not extractable (blank)**: it equals 211 + (fake-title subset of the 884), and that subset is not printed. Pass B is right on the numerator (211, "a floor, flagged for the author") and right that the total is not extractable; its CSV row nonetheless sits 211 against refs_generated 1,287, and that pairing must **not** be pooled as a rate. **Pass A is wrong** on both the number (1095) and the pairing (1095/1,287).

### 4b. Bing AI arm n_major: SETTLED 28; Pass A wrong

**What the paper prints (Results, Systematic Search Results via Bing AI):**

> "Because Bing AI always gave references with links to the websites, all studies presented by Bing AI existed. However, it also provided wrong answers about the study type, especially as it listed reviews as RCTs. Of the 28 studies with grade C, 27 (96%) were not RCTs and 1 (4%) was about a different treatment. Only 1 study had no grade because of a fake title; it presented a study registered in PubMed while pretending that it was the result of a search in ClinicalTrials.gov."

Table 1, grade C: "Essential information matched, but not PICOS" (PICOS mismatch = inappropriate for the question). Table 2, Bing AI totals: A 19, B 0, C 28, F 0, total 48. Both passes agree n_fabricated = 0 and n_minor_error = 0 (grade B) for this arm.

**Settlement: n_major = 28 — exact.** Every grade-C reference is a real publication (essential bibliographic information — title, author, journal, year — matched) cited for a question/topic it does not cover: 27 were not RCTs though presented as RCT search results, 1 concerned a different treatment. The study counts that as inappropriateness (PICOS mismatch, grade C), which is the review major definition's misattribution clause — the same clause settled at item 2c. **Pass B's 28 stands; Pass A is wrong:** its blank rested on reading grade C as mere "question-inappropriateness" outside the major outcome, ignoring the form's express clause. (The single ungraded Bing study was a real PubMed study misrepresented as a ClinicalTrials.gov result; the paper does not count it in grade C, and neither pass's 28 includes it — it is a narrative note only and does not change the settled count, which is the printed grade-C count.)

---

## 5. R4263 — Zhu_2025, ChatGPT-4 n_major and n_minor_error: SETTLED 0 and 0 (printed zeros); Pass A wrong

**Definitions as printed (Methods, reference authenticity):**

> "…we evaluated authenticity in the unique references after removing duplicated references, and categorized references as: (1) authentic (accurate "real" references identifiable via internet search), (2) incomplete (insufficient information to verify its existence), (3) inaccurate (identifiable through internet search but one or more elements in citations were incorrect, e.g., journal names, volume or page numbers), and (4) fabricated (made-up references)."

**Counts as printed (Table 1, "Analysis of references provided in responses of ChatGPT-4 and Google Bard"; denominator = 20 unique references for ChatGPT-4, from 52 generated):**

| Table 1 category | ChatGPT-4 |
|---|---|
| Authentic/accurate (real reference), n (%) | 20 (100) |
| Incomplete, n (%) | **0 (0)** |
| Inaccurate, n (%) | **0 (0)** |
| Fabricated, n (%) | **0 (0)** |

Corroborated in Results ("All the references could be accessed through internet searches (real references)") and Discussion: "Although we did not observe inaccurate or fabricated references for ChatGPT-4, possibly due to small sample size…"

**Settlement: n_major = 0, n_minor_error = 0.** These are *printed zeros* — data, not blanks. Pass A's reason for leaving both blank — that the paper's "inaccurate" count is not severity-split — is sound only when the inaccurate count is greater than zero (as for the Bard arm: 7 inaccurate, split unknowable). Here the parent count is a printed 0: the four categories are mutually exclusive and exhaustive of the 20 unique references, every reference sits in the authentic class, and the inaccurate, incomplete and fabricated classes are all printed 0. Any severity subset of an empty set is empty: major-type errors = 0 and minor-type errors = 0 necessarily, with no split required. **Pass B is right; Pass A is wrong** — and inconsistent with its own row for this arm, where it accepted the same table's printed 0 for n_fabricated and the 20 for n_fully_accurate.

---

## 6. R4518 — Bridges_2025, ChatGPT-4 n_bad_doi: SETTLED 125; Pass B wrong

**Review definition applied.** Bad DOI = "a DOI that does not resolve, or a DOI that resolves to a different paper", denominator = references that carry a DOI.

**What the paper prints (Discussion, "Research question four"; arm denominator 201 cases/citations):**

> "Reference accuracy tests showed that citation accuracy and DOI accuracy are very low, with citation accuracy of 34.8% and DOI accuracy of 37.8%. The model produced 70 correct citations and 76 correct DOIs, 91 incorrect citations and 83 incorrect DOIs, and 40 non-existent citations and 42 non-existent DOIs."

Arithmetic checks: citations 70 + 91 + 40 = 201; DOIs 76 + 83 + 42 = 201; 70/201 = 34.8% and 76/201 = 37.8% as printed. The three DOI categories are mutually exclusive and exhaustive, and every one of the 201 citations carries a DOI classification (Methods, Research question 4: the prompt "requested a complete reference citation for each diagnosis presented, including authors, title, journal, page numbers, DOI…", verified by internet search). Note the paper keeps the citation counts and the DOI counts distinct: non-existent **citations** 40 ≠ non-existent **DOIs** 42, and incorrect citations 91 ≠ incorrect DOIs 83.

**Settlement: n_bad_doi = 125 — exact by sum (rule 5): incorrect DOIs 83 + non-existent DOIs 42 = 125, denominator 201.**

- Non-existent DOI (42): a DOI that does not exist does not resolve — inside the review definition.
- Incorrect DOI (83): the printed DOI is not the cited paper's DOI. For a wrong DOI there are exactly two possible resolution outcomes — it resolves to a *different* paper, or it does not resolve at all. Both outcomes are the review's bad-DOI definition, verbatim. No third outcome exists: a DOI that resolved to the cited paper would be a correct DOI, and the paper prints that category separately (76). The two parts are non-overlapping printed categories that together cover bad DOI exactly and nothing else.

**Why B is wrong.** Pass B entered 42 (non-existent DOIs only) and called it "a floor", reasoning that some of the 83 incorrect DOIs "may also resolve to a different paper, not separable as printed". That caveat defeats itself: resolving to a different paper is *inside* the bad-DOI definition, as is not resolving — so the uncertainty Pass B cites is uncertainty between two sub-mechanisms of the same outcome, not uncertainty about the outcome. A floor is not a printed count; 42 understates the printed data. **Pass A's 125 stands** (Pass A also correctly used the DOI-specific components 83 + 42, not the parallel citation counts 91 + 40).

---

## Caveats

1. All quotations are verbatim from the six XML full texts as provided, including the papers' own errors (e.g., Pan_2026's "DeepSeek-R1 provided 4 reference links were invalid"; Ohlsen_2026's abstract calling Gemini's 5 found references "nonexistent or inappropriately cited" against its own Table III). Internal inconsistencies are recorded, not corrected; none changes a ruling above except as discussed (the per-reference tables govern over lumped summary labels in R3191 and R4142).
2. R4142's settled pair 211/403 is a subset-scoped pair (graded, title-existed studies). Whether the main pool accepts a subset denominator for this arm is the human author's call; what this settlement establishes is that 1095 is not a printed or derivable count, that 211 is the printed fabricated count, and that no fabricated total over the 1,287 presented studies is extractable from the paper.
3. No number in this report was taken from the manuscript or the analysis files, which were not read.
