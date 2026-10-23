# Extractor B — citation-chasing studies, ROBUSTNESS PASS (23 October 2026)

Extractor B, working independently. Sources read: `extraction-form.md` (definitions + mapping rules 1–8) and the two full texts only. I did **not** read `extraction.csv`, `extraction-passA.csv`, `extraction-passB.csv`, any Extractor A output for these studies, or any other extraction output.

Output: `robustness/search/extraction-chasingB.csv` — 4 data rows (1 arm for R16144, 3 arms for R16439) on the exact 25-column schema. Eligibility set to `include_generation` for every row, as instructed.

---

## R16144 — Mikus_2024

**Identity.** Gerd Mikus, "ChatGPT does make up scientific references: should it be currently renamed CheatGPT?", *European Journal of Clinical Pharmacology* 2024;80(12):1995–1996. DOI 10.1007/s00228-024-03758-7; PMID 39251431. Article type: letter. Single author, affiliation Heidelberg University Hospital, Germany → country = Germany. Specialty = pharmacology (clinical pharmacology / pharmacoepidemiology). Topic: yohimbine pharmacokinetics and the involvement of CYP2D6 in its clearance.

**Arm (one only).** "I used the free ChatGPT Version 1.2024.170 on a Mac, which is GPT-4o" (Par1). model_arm = ChatGPT GPT-4o; model_family = GPT; model_version recorded with the full printed string; model_year = 2024 (GPT-4o vendor release year, OpenAI 2024; consistent with the printed app version 1.2024.170). Retrieval = none — no browsing/search/tool use is reported; the links and PubMed IDs in the output were generated text, not retrieved records.

**Generation.** Prompts (printed): "What is the relationship between yohimbine and CYP2D6?", then "Are there specific scientific publications available regarding these 4 topics?" and "Is there more published on metabolism of yohimbine by CYP2D6?", then "Can you give these references with a link and a PubMed ID?" No number of references was requested → `refs_requested` left **blank** (not zero). "ChatGPT came up with 5 references" (Par12) → `refs_generated` = 5. The 5 references are reproduced in full (Par15–Par39) with authors, journal, year, PubMed ID and PubMed link each.

**Verification.** Verification source = PubMed (the supplied PubMed IDs/links are the records checked). Verifier = the sole author, who also posed the prompts → `verifier_independent` = no (same person). No blinding, duplicate verification or agreement statistic is reported (single-author letter).

**Definitions and mapping (rules 1–8).** The letter prints no formal definitions. Mapping rests on the narrative verification statement (Par40), quoted in substance: "The authors were not made up by ChatGPT; they really exist and publish in the area of drug metabolism. However, **all publication titles do not exist** whereas the journals are the target journals for this type of research. **All provided PubMed IDs exist; however, these are references which have different authors, different topics, and different journals.**"

- *Completely fabricated — exact in substance.* For every one of the 5 references, no single matching publication exists: the title does not exist, and the PubMed ID resolves to a different paper. This is exactly the review definition, including its explicit case of real authors attached to a title that does not exist. `n_fabricated` = 5 / 5.
- *Major inaccuracy (incl. fabricated) = 5.* All 5 references are fabricated, and fabricated is included in the review's major-inaccuracy definition, so the major count equals the fabricated count. No non-fabricated reference exists that could add to or complicate this count.
- *Fully accurate = 0 — FLAGGED for adjudication/author check.* Not printed as a count. It is logically entailed: 5 generated, all 5 fabricated, and a fabricated reference cannot be accurate on all checked fields (title fails). I recorded 0 rather than blank because the value is determined by the printed statements, not imputed; if the settled convention is "printed counts only", this cell should be blanked at adjudication without affecting the fabricated/major pools.
- *Minor error — blank.* No minor-error count is printed, and no reference survives as the same retrievable publication with a minor field error (all titles are non-existent), so no count is extractable under rule 2.
- *Bad DOI — blank.* The references carried PubMed IDs and PubMed links, not DOIs. The wrong-PubMed-ID phenomenon is captured by the fabricated count; it is not a DOI outcome and was not forced into `n_bad_doi`.

**Funding / conflicts.** Funding section: "Open Access funding enabled and organized by Projekt DEAL" (open-access funding only; no study funding stated). Competing interests: "The author declares no competing interests" → conflicts = none.

---

## R16439 — Jedrzejczak_2023

**Identity.** W. Wiktor Jedrzejczak & Krzysztof Kochanek, "Comparison of the audiological knowledge of three chatbots – ChatGPT, Bing Chat, and Bard", medRxiv preprint, posted 22 November 2023, doi 10.1101/2023.11.22.23298893 → pub_type = preprint. Affiliations: Institute of Physiology and Pathology of Hearing, Warsaw, and World Hearing Center, Kajetany, Poland → country = Poland. Specialty = medical specialty (audiology). Topic: 10 audiology questions (Table 1: Q1–3 basic, Q4–6 intermediate, Q7–10 specialised), posed to all three chatbots on 28.08.2023.

**Arms (three).**
- ChatGPT 3.5 — "OpenAI ChatGPT (version 3.5)"; Introduction: "ChatGPT utilizes the GPT-3.5 model, trained on information sources up to 2021" and, unlike the other two, no live Internet access → retrieval = none. model_family = GPT; model_year = 2022 (GPT-3.5/ChatGPT vendor release year).
- Bing Chat — Methods: "Microsoft Bing Chat (which is based on ChatGPT but with some modifications)"; Introduction: "Bing Chat uses the GPT-4 model". Both printed descriptions are carried in `model_version` because they differ in precision; family = GPT either way. Retrieval = browsing or live search ("both Bing Chat and Bard have access to live data on the Internet"). model_year = 2023 (GPT-4 vendor release year).
- Bard — Google Bard, "marked as an experimental version"; Introduction: "Bard employs the PaLM 2 model" → model_family = PaLM, model_version = PaLM 2. Retrieval = browsing or live search. model_year = 2023 (PaLM 2 vendor release year).

Standard publicly available versions were used for all three.

**Why every reference-outcome cell is blank (the central call on this study).** This is a knowledge-accuracy study, not a reference-generation study:

1. The prompts requested *answers* to 10 audiology questions. No references were requested → `refs_requested` blank for all arms (blank, not zero: no reference quota exists to count).
2. The study never enumerated the references/sources the chatbots produced, and never verified any reference against PubMed, Crossref or any other source. There is no verification source for references → `verification_source` records that no reference verification was performed (answers were rated by the two authors on a 1–5 Likert scale, twice, with agreed scores; the raters are the study authors → `verifier_independent` = no).
3. The only source-related count is at the *response* level (Table 2): "Number of responses in which sources were provided (max = 10)" — ChatGPT 0, Bing Chat 8, Bard 2. That is a count of responses, not of references: Bing "also usually provided several additional links" per response, so no per-arm reference total can be recovered → `refs_generated` blank for all arms.
4. The Discussion confirms the sources were not bibliographic references in the review's sense: "In our tests, only one of the responses contained a reference to a research paper. Only Bing Chat provided sources for its responses… However, the sources were typically links to webpages (usually unverified information) not scientific papers."
5. The printed error counts (Table 2 — errors: ChatGPT 2, Bing 1, Bard 6; inaccuracies: ChatGPT 4, Bing 4, Bard 2) are **answer-content** errors. The paper's own definition: "We decided to rate small mistakes as inaccuracies when the response was imprecise although not misleading." Worked examples are factual claims (ABR safety, AOAE terminology, audiogram shape, dB vs dB HL). They are not errors in reference identity, retrievability or attribution, so under mapping rules 2–4 they map to **no** review outcome — not to fabricated, not to major inaccuracy, and "inaccuracies" must not be entered as minor errors. Accordingly `n_fabricated`, `n_major_inaccuracy_incl_fabricated`, `n_fully_accurate`, `n_minor_error` and `n_bad_doi` are all blank (narrative only) for all three arms. The content counts are preserved in each row's `definitions_note`/`source_location` so nothing is lost at adjudication.
6. Narrative facts retained: ChatGPT provided no source information for any response; Bard failed to answer question 3 at all ("I'm unable to help you with that, as I'm only a language model…").

**Funding / conflicts.** The preprint contains no funding statement and no competing-interests statement (checked full text) → both = not reported for all arms.

---

## Cross-cutting notes for adjudication

- **Model years** are the only cells not printed in the papers: they use vendor release records as the extraction form's field 14 permits (GPT-4o 2024; GPT-3.5 2022; GPT-4 2023; PaLM 2 2023), and each is consistent with the version/date information the papers do print.
- **R16144 `n_fully_accurate` = 0** is an entailment from printed statements, flagged above — the one cell where Extractor A/B disagreement would be a convention question, not a reading question.
- **R16439 eligibility:** rows are coded `include_generation` as instructed. For the record: the generation in this study is answer generation with incidental, unverified source provision; it contributes no poolable reference outcome under the exact-match rules.
- No arithmetic contradictions found in either paper. R16439 Table 2 internal sums check (errors + inaccuracies = "together" row: 2+4=6, 1+4=5, 6+2=8).
