# Extraction — Extractor A, citation-chasing batch (Robustness Pass, 23 Oct 2026)

Pass: Extractor A, independent. I did not read `extraction.csv`, `extraction-passA/B.csv`, or any other extraction outputs.
Form read first: `review2/extraction-form.md` (definitions + mapping rules 1–8).
Output: `robustness/search/extraction-chasingA.csv` — exact 25-column schema given in the task, one row per model arm, 4 rows total.
Conventions applied: extract as printed (rule 1); map only on exact definition match (rules 2–4); rule-5 sums and rule-6 percentage derivations only where whole with no rounding doubt and flagged — **no rule-5 or rule-6 derivation was used in this batch**; blank = not extractable, never zero.
`study_id` = FirstAuthorLastName_Year as printed. `eligibility` = `include_generation` for both records, as instructed for this batch.
`topic_type` is coded here as the established/emerging call (protocol §3.6): both topics are established (see per-study basis below). If the parent dataset uses `topic_type` for a different grouping, remap from these notes.
`specialty` uses the extraction-form §B.9 review grouping wording.

---

## R16144 — Mikus_2024

**Identity (as printed):** Gerd Mikus (single author), "ChatGPT does make up scientific references: should it be currently renamed CheatGPT?", *European Journal of Clinical Pharmacology* 2024, 80(12):1995–1996. DOI 10.1007/s00228-024-03758-7; PMID 39251431; PMCID PMC11557680. Article type in the XML: letter. Affiliation: Heidelberg University Hospital, Department of Clinical Pharmacology and Pharmacoepidemiology, Heidelberg, Germany → country **Germany**.
**Pub type:** peer reviewed journal article (letter).

**Task / topic:** Author working on yohimbine pharmacokinetics and CYP2D6 involvement in its clearance asked ChatGPT about yohimbine–CYP2D6 (metabolism, genetic variability, drug interactions, clinical implications), then "Are there specific scientific publications available regarding these 4 topics?", "Is there more published on metabolism of yohimbine by CYP2D6?", then "Can you give these references with a link and a PubMed ID?" (Par9–Par14).
→ specialty **pharmacology**; topic_type **established** (long-standing drug-metabolism literature; author's own cited work is Vay et al. 2020, and the journals/authors invoked are established in the field).

**Arm (1 only):**
- model_arm `ChatGPT GPT-4o`; model_family `GPT family`; model_version `GPT-4o (ChatGPT Version 1.2024.170)` — Par1 verbatim: "I used the free ChatGPT Version 1.2024.170 on a Mac, which is GPT-4o."
- model_year **2024** — source: version string/year as printed in the paper (1.2024.170, paper 2024); consistent with the vendor release of GPT-4o in 2024. Flagged: the paper does not separately state a release date.
- retrieval **none** — no browsing, search tool, corpus or document set is stated; questions were put directly to the free ChatGPT. Coded none on what is printed, not "unclear", because the set-up is described as ordinary free ChatGPT use; adjudicator may prefer "unclear" — no retrieval condition is explicitly stated either way.
- refs_requested **blank** — no number of references was requested in any printed prompt; the model volunteered the list. Do not enter 5 here.
- refs_generated **5** — Par12: "ChatGPT came up with 5 references." The five are listed in full at Par15–Par39 (title, authors, journal/year, PubMed ID, link each).

**Counts and mapping:**
- n_fabricated **5** — mapping **exact**. Par40 verbatim substance: "The authors were not made up by ChatGPT; they really exist and publish in the area of drug metabolism. However, all publication titles do not exist whereas the journals are the target journals for this type of research. All provided PubMed IDs exist; however, these are references which have different authors, different topics, and different journals." Review definition of completely fabricated expressly covers real authors attached to a title that does not exist where no single matching publication exists — this is that case, for all 5/5.
- n_major_inaccuracy_incl_fabricated **blank** — no separate printed major-inaccuracy count/label. The 5 fabricated are by definition included in major inaccuracy, but I did not derive/copy the count across outcomes (no rule-5 sum was printed); blank ≠ zero, and the fabricated count is the poolable number. Flagged for the author/adjudicator if a derived major = 5 is wanted.
- n_fully_accurate **blank** — no printed accurate count. (Logically none of the 5 could be fully accurate, but no count is printed, so per instructions this is left blank, not entered as 0.)
- n_minor_error **blank** — no minor-error count/label printed; the errors described are identity-level (non-existent titles, mismatched PMIDs), not minor field errors.
- n_bad_doi **blank** — references carried **PubMed IDs, not DOIs**; no DOI outcome is reported. The PMID mismatch (PMID resolves to a different paper) is a PubMed-ID finding, not a bad-DOI finding, and was not mapped into n_bad_doi.

**Verification:** verification_source **PubMed** — the check reported is on the supplied PubMed IDs/links and on title existence; Par40 reports the PMID resolution result for every reference. Caveat: no formal step-by-step verification method, search-attempt rule, or fields-checked list is printed; verification is reported narratively by the author, who also knew the cited authors personally ("Since I know many of the authors, I was surprised…"). verifier_independent **no** — single author who both prompted ChatGPT and checked the output (same person; no second/independent verifier, no blinding reported).

**Funding / conflicts (as printed):** Funding section: "Open Access funding enabled and organized by Projekt DEAL." No other study funding stated. Competing interests: "The author declares no competing interests."

**Missing / not reported (form fields):** generation date/period (not printed, beyond the 2024 version string), generation settings/temperature/retries/selection, full verbatim prompt set is partial (questions quoted at Par2, Par10–Par11, Par13), verifier agreement, partial-match rule, position data. Arithmetic: no inconsistencies found; 5 listed references = the "5 references" at Par12.

---

## R16439 — Jedrzejczak_2023

**Identity (as printed):** W. Wiktor Jedrzejczak and Krzysztof Kochanek, "Comparison of the audiological knowledge of three chatbots – ChatGPT, Bing Chat, and Bard", medRxiv preprint, doi 10.1101/2023.11.22.23298893, version posted 22 November 2023 (not certified by peer review). Affiliations: Institute of Physiology and Pathology of Hearing, Warsaw, Poland, and World Hearing Center, Kajetany, Poland → country **Poland**. Text also confirms Poland directly ("problems with access in our country (Poland)").
**Pub type:** preprint.

**⚠ Headline extraction finding — no poolable reference outcome in this paper.** This is a question-answering accuracy study, not a reference-generation study in its reported outcomes:
- The models were **not asked for references**. They were presented with the same 10 audiology questions (Table 1: basic Q1–3, intermediate Q4–6, specialised Q7–10), presented on 28.08.2023, and the two authors rated each answer on a 1–5 Likert scale for correctness/completeness.
- No count of generated references is reported for any arm, and no generated reference was verified against PubMed/Crossref/Google Scholar/a publisher record or any other named external source. There is therefore **no denominator in generated references** and no fabricated / major / fully-accurate / minor / bad-DOI count to extract. **All reference-count columns are blank for all three arms (blank = not extractable, never zero).**
- Do **not** substitute the other counts in the paper (see "Counts as printed, not mapped" below) — each fails the exact-match test.

**Topic:** 10 questions "from a variety of topics in audiology" (audiometric testing, cochlear implant surgery, newborn hearing screening, air–bone gap, auditory neuropathy, stapedius reflex, conductive hearing loss, ABR vs MRI/CPA tumour, acoustic neuroma management, hidden hearing loss).
→ specialty **medical specialty (audiology)**; topic_type **established** (standard, long-standing audiology knowledge topics; no emerging/niche recent-literature topic is identified in the paper).

**Arms (3):**

1. **ChatGPT** — model_family `GPT family`; model_version `GPT-3.5` (Methods: "OpenAI ChatGPT (version 3.5)"; Introduction: "ChatGPT utilizes the GPT-3.5 model, trained on information sources up to 2021" — 2021 is the training cutoff as printed, **not** the release year). model_year **2022** — source: vendor release record (GPT-3.5/ChatGPT released 2022); not stated as a release year in the paper, flagged here per form field 14. retrieval **none** — Introduction: "Unlike ChatGPT, both Bing Chat and Bard have access to live data on the Internet."
2. **Bing Chat** — model_family `GPT family`; model_version `GPT-4` (Introduction: "Bing Chat uses the GPT-4 model"). Internal inconsistency flagged, not corrected: Methods describes Bing Chat only as "based on ChatGPT but with some modifications". model_year **2023** — vendor release record for GPT-4; not stated in the paper. retrieval **browsing or live search** (live Internet access, Introduction, quoted above).
3. **Bard** — model_family `PaLM family` (other named family in form terms); model_version `PaLM 2` (Introduction: "Bard employs the PaLM 2 model"); Methods note Bard "was marked as an experimental version". model_year **2023** — vendor release record for PaLM 2; not stated in the paper. retrieval **browsing or live search** (live Internet access, Introduction).

**Counts as printed, NOT mapped (narrative only, per mapping rules 2–3):**
- Table 2, per chatbot, over **10 responses** (denominator is responses, not references): errors — ChatGPT 2, Bing Chat 1, Bard 6; inaccuracies — ChatGPT 4, Bing Chat 4, Bard 2; errors+inaccuracies — 6 / 5 / 8. Definitions as printed (Methods): responses were rated for correctness/completeness; "we decided to rate small mistakes as inaccuracies when the response was imprecise although not misleading." These are factual errors/imprecisions **in answer text** (worked examples in Results: e.g. ChatGPT on ABR risks, Bing on newborn hearing test naming, Bard on the normal audiogram). They cover a different object (answer content) from the review outcomes (errors in a generated reference), so mapping to n_major_inaccuracy_incl_fabricated or n_minor_error is **not exact** — recorded here for narrative synthesis only.
- Table 2, "Number of responses in which sources were provided (max = 10)": ChatGPT **0**, Bing Chat **8**, Bard **2**. This is a per-response presence/absence count, **not** a count of references generated, and none of these sources was verified. Not entered in refs_generated. Discussion adds: "only one of the responses contained a reference to a research paper. Only Bing Chat provided sources for its responses… However, the sources were typically links to webpages (usually unverified information) not scientific papers (verified information)" and Bing's webpages "often provided references to scientific papers or books".
- Likert totals (Table 2, for context only): total score ChatGPT 45, Bing Chat 37, Bard 36 (min 10, max 50). Bard was the only chatbot unable to respond to a question (Q3, quoted in Discussion).

**Verification:** verification_source **not reported** — no external reference-verification source is named; answer evaluation was expert judgement by the two authors ("evaluated by two experts (the authors)… The experts went over all the responses twice and agreed on the scores"). verifier_independent **no** — the verifiers are the study authors themselves (same people who presented the questions); duplicate rating with consensus is reported, but no independence from the study/generation step and no blinding to model is reported (answers are discussed per named chatbot throughout).

**Funding / conflicts:** **not stated** — the preprint contains no funding statement and no competing-interests/conflict statement (searched full text; the only funding-adjacent text is the standard medRxiv copyright-holder boilerplate, which is not a study funding statement).

**Missing / not reported (form fields):** any reference request, reference count, reference verification, definitions of fabricated/accurate for references, DOI data, position data, generation settings (temperature etc.), funding, conflicts. Contradictions flagged: Bing Chat model description differs between Introduction (GPT-4) and Methods (based on ChatGPT with modifications) — GPT-4 used in the CSV per the Introduction, difference logged here.

---

## Verification of output

- `extraction-chasingA.csv`: header = the exact 25 columns in the task order; 4 data rows (R16144 × 1 arm; R16439 × 3 arms); both record IDs present.
- Only non-blank outcome count in the batch: R16144 / Mikus_2024 / GPT-4o — refs_generated 5, n_fabricated 5.
- Eligibility note for the author: R16439 is entered as `include_generation` as instructed for this batch, but on its printed content it reports no reference-generation outcome at all — if the adjudication stage applies protocol §3.1/§3.3 strictly (denominator in generated references; no citation outcome), this record is a candidate for author review on eligibility, and in any case it can contribute no pooled proportion.
