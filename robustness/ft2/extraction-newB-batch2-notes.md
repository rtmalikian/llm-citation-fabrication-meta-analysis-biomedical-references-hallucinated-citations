# Extractor B — NEW included studies, batch 2 (robustness pass, 23 Oct 2026)

Extractor B, working independently. Sources: the 8 full texts listed in
`robustness/ft2/extract-batch2.txt` (XML, plus R6331 as PDF via pdftotext).
Output: `extraction-newB-batch2.csv` — 16 rows (one per model × retrieval arm),
25-column schema, `eligibility = include_generation` for every row.
Mapping per extraction-form rules 1–8: extract as printed; map only if the
study definition matches the review definition exactly; percentages at a
stated denominator converted only where they give a unique whole count with
no rounding doubt, flagged DERIVED; blanks = not extractable / not exact,
never zero.

## R2314 — Rao_2026 (JMIR Medical Informatics)
- 1 arm: GPT-4, no retrieval, patient-education questions on scars/keloids
  (354 Reddit questions; a second set of 38 unique website questions was
  evaluated in supplements with no separate reference total in the main text,
  so no second arm was created).
- Extractable: refs_generated 3,250; n_fabricated 383 (11.8%, printed count).
  "Hallucinated" was assessed with the Reference Evaluation for AI tool —
  references verified through direct links or a Google search, classified
  real or fabricated — mapped exact to completely fabricated.
- Did not map: 2,867/3,250 "real" (actual websites or academic papers) is
  existence only, with no check that all bibliographic fields were correct,
  so it does **not** map to strict fully accurate. No major-inaccuracy,
  minor-error or bad-DOI count is reported; all left blank.
- Note: references here include websites as well as academic papers, as
  printed. Funding: Talent Fund of Guizhou Provincial People's Hospital.
  Conflicts: none declared.

## R2352 — Zhou_2026 (Graefe's Archive for Clinical and Experimental Ophthalmology)
- 4 arms (GPT-4, Gemini 2.5 Pro, Grok-3, DeepSeek R1), no retrieval condition
  set by the study (free/basic platform versions), 9 SMILE-surgery topics,
  literature-review generation. References manually retrieved and verified
  via PubMed and Google Scholar; categories: true and relevant / true but not
  relevant / fictitious.
- Derivation (flagged in CSV): Table 2 prints totals and percentages only.
  - DeepSeek R1: 200 refs, fictitious 40.5% = **81** (exact).
  - Gemini 2.5 Pro: 96 refs, fictitious 45.8% → **44** (only whole count
    rounding to 45.8%; cross-checks: 96 − 48 true-and-relevant − 4
    true-but-not-relevant = 44).
  - GPT-4 (Table 2 column headed "GPT"): 95 refs, fictitious 49.5% → **47**
    (only whole count rounding to 49.5%; 95 − 38 − 10 = 47).
  - Grok-3: 86 refs, fictitious 25.6% → **22** (22/86 = 25.58%).
- Did not map: "true and relevant" does not map to strict fully accurate
  (existence + topic relevance, no field-by-field accuracy check).
  Major inaccuracy left blank: "true but not relevant" is not defined as
  identity misattribution, so fictitious + not-relevant is not an exact sum
  for the review's major-inaccuracy definition.
- Arithmetic/text flag: Results prose gives Grok fictitious as 25.5% while
  Table 2 gives 25.6%; the table value (which yields the whole count) was used.

## R2551 — Liu_2026 (BMC Oral Health) — NO outcome count mapped
- 5 arms (Qwen3, DeepSeek-R1-0528, ChatGPT o3-pro, Gemini 2.5 Pro,
  Claude 4.0), no retrieval, 110 Chinese oral and maxillofacial surgery
  licensing-exam questions. Reference totals per arm are extractable and are
  in `refs_generated` (69, 66, 54, 50, 63 respectively).
- Definition that did not map (all 5 arms): Methods define the negative
  category as **"unverified" = references "unavailable or irrelevant"**
  (searched in CNKI/Wanfang for Chinese, PubMed/Web of Science/Google
  Scholar for English). Table 5 then labels that same count "Fabricated"
  (Qwen3 26, DeepSeek 29, o3-pro 22, Gemini 21, Claude 24 — kept here for
  narrative only). Unavailable-**or-irrelevant** is broader than the review's
  completely fabricated (no matching publication exists): a real but
  irrelevant reference falls inside it. Per mapping rule 3, n_fabricated is
  left blank, not copied from Table 5.
- Fully accurate also blank: the positive category ("verified"/"genuine" —
  43, 37, 32, 29, 39) required only that a reference be located in a database
  **and pertinent to the query content**, not that all checked fields were
  correct. No major/minor/bad-DOI counts reported.
- Funding: no specific grant. Conflicts: none declared.

## R5403 — Schumacher_2024 (International Journal of Retina and Vitreous)
- 1 arm: ChatGPT 4.o (as printed, "(2024)"), paid version, no retrieval,
  uveitis clinical-case questions (10 cases × 5 questions × 3 attempts).
  References independently verified across PubMed, MEDLINE, Cochrane
  Library, Embase, Scopus, Web of Science and Google Scholar.
- Extractable, all printed counts: 52 generated; n_fabricated **22**
  ("could not be located in any of the searched databases"); n_fully_accurate
  **22** ("accurate and correctly cited").
- Did not map: the remaining 8 "found to exist, but were either misinterpreted
  or incorrectly cited" mixes misinterpretation with incorrect citation of
  unspecified severity, so it cannot be split into major vs minor and no
  exact-by-sum major count (22 + 8) was entered. Minor and bad-DOI blank.

## R5556 — Sina_2024 (OTO Open)
- 1 reference-bearing arm: GPT-4 under the "prompting for references" prompt
  (the study ran 4 prompt variants of the same model/retrieval condition;
  all unique references arose in this thread, so the other prompt variants
  are not separate arms under the model × retrieval arm definition).
  Topic: patient-education questions on COVID-19-induced olfactory
  dysfunction. Country USA; otolaryngology.
- Extractable: **1 fabricated of 12 unique references** (8.3% in Discussion,
  "for a nonexistent publication"; Results: 11 of 12 unique references
  legitimate, 1 falsified). Verification as printed: a reference counted as
  real if it "has a DOI and is findable online".
- Did not map: the 11 "legitimate" references were not checked for accuracy
  on all fields, so no strict fully-accurate count. No major/minor/bad-DOI
  counts.
- Arithmetic contradiction flagged (not corrected): the Results state
  "27 total references", then "Twelve (44.4%) of the 24 total references
  provided were unique citations" — 27 vs 24 in consecutive sentences.
  The unique-citation denominator (12) is the one the paper itself uses for
  its fabricated proportion, so it is the denominator extracted.
- Model note: Methods date the version used as "February 3, 2024"; model_year
  in the CSV is the GPT-4 release year, 2023.

## R5577 — Kaygisiz_2025 (BMC Oral Health)
- 2 arms (DeepSeek-V3, ChatGPT-4o), no retrieval, 16 oral-pathology case
  scenarios in which each model was asked to support diagnoses with
  literature citations. References searched individually in Google Scholar,
  PubMed and Web of Science: found = "real", not found = "fake".
- Extractable, printed counts (Table 2): DeepSeek-V3 — 48 generated,
  n_fabricated **8**; ChatGPT-4o — 62 generated, n_fabricated **50**.
  Text confirms "All of the references presented as fake were imaginary",
  supporting the exact mapping to completely fabricated.
- Did not map: "real" (40 and 12) is findability only, not field accuracy,
  so no fully-accurate count. No major/minor/bad-DOI counts. Note the real
  counts include repeated references (DeepSeek 40 real from 11 sources;
  ChatGPT-4o 12 real from 6 sources), as printed — totals are as-generated,
  not deduplicated.

## R6331 — Ok_2026 (International Journal of Impotence Research; PDF)
- 1 arm: ChatGPT-5, no retrieval, narrative review generation on penile
  prosthesis implantation; 5 references requested per section. Two
  independent reviewers verified every reference in PubMed, Google Scholar,
  Crossref and journal websites, cross-checking title, authorship, journal,
  year, volume/issue, pages and DOI.
- Derivation (flagged in CSV): the paper prints percentages at a stated
  denominator of 28 citations — fully accurate 35.7% → **10**, entirely
  fabricated 17.9% → **5** (each percentage admits only one whole count).
  Both definitions are printed verbatim-grade and map exactly: fabricated =
  no corresponding publication identifiable and details matching no existing
  peer-reviewed article; fully accurate = real publication with **all** major
  bibliographic elements (title, authorship, journal, year, DOI/equivalent)
  correct → strict fully accurate.
- Did not map: the remaining ~13 (46.4%) "partially inaccurate" references
  are a real publication with one or more elements inaccurate, and the paper
  explicitly states minor metadata errors are included in that category —
  it mixes major and minor, so n_major and n_minor are both blank. Bad DOI
  not counted separately (DOI was one element inside the categories).
- Arithmetic flag: "five references per section, resulting in a total of
  28 citations" does not yield a consistent total requested (the generated
  outline had 7 sections), so refs_requested is left blank rather than
  inferred as 35.
- Affiliations span Turkey and Belgium; both are listed in `country`.
  Funding: TÜBİTAK open-access funding. Conflicts: none declared.

## R6555 — Safrai_2024 (Journal of Assisted Reproduction and Genetics)
- 1 arm: ChatGPT-4, no retrieval, scientific review generation on fertility
  preservation in men and prepubertal boys; 5 references requested per
  section, 25 generated in total (refs_requested = refs_generated = 25).
  References authenticated in PubMed or Google Scholar; where title plus
  journal, authors and DOI were given, all parameters were verified.
  Affiliations USA and Israel; both listed.
- Extractable, printed counts: n_fully_accurate **9** (36%; "existing
  references, and all their parameters were correct" → strict);
  n_fabricated **4** (16%; "completely fabricated"/"fictitious").
- Did not map: the remaining 12 (48%) "had a correct title but other
  fictitious parameters / other errors" are not split by severity or by
  whether the wrong element is identity-forming, so no exact major or minor
  count was derived from them. Bad DOI blank: 20/25 references carried a
  DOI and one fabricated example is narrated whose DOI resolved to a
  different article, but no aggregate bad-DOI count is printed.
- Funding: NICHD HD096723 and HD100197, Magee-Womens Research Institute and
  Foundation. Conflicts: none declared.

## General notes
- `n_major_inaccuracy_incl_fabricated`, `n_minor_error` and `n_bad_doi` are
  blank in **every** row of this batch: no study in the batch reports a
  category that maps exactly (alone or by an unambiguous sum) to the
  review's major-inaccuracy, minor-error or bad-DOI definitions; the
  partial/incorrect categories that might contribute are each flagged per
  study above.
- No study in this batch required a blank-count row for total
  non-extractability: every study yielded at least a reference total, and
  all except Liu_2026 (R2551, definition not exact) yielded at least one
  mapped outcome count.
