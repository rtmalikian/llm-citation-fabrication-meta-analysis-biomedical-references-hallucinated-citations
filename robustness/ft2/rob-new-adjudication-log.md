# Risk-of-bias adjudication log — NEW included studies, robustness pass (23 October 2026)

Adjudicator: Risk-of-Bias Adjudicator agent, robustness pass (re-run; files on disk are the deliverable). Tool: adapted 8-domain tool for citation-generation experiments (rob-forms.md) — an adapted tool, not RoB 2 and not QUADAS-2.

Method: for each of the 79 disagreement rows in `robustness/ft2/rob-new-disagreements.csv` (37 newly included studies) and the 3 disagreements between the two chasing assessor sheets (`robustness/search/rob-chasing-assessor1.csv` / `rob-chasing-assessor2.csv`, 2 studies), the adjudicator weighed both assessors' judgements and support summaries against the study's full text (mapping in `robustness/ft2/retrieved-files.json`; chasing full texts in `robustness/search/fulltexts3/`) and the rob-forms.md domain guides, and recorded an independent judgement. No mechanical rule was applied (the more cautious judgement did not automatically win: assessor 1 matched 59 settlements, assessor 2 matched 20, across the 79 FT2 rows). Reconciliation note (23 October 2026): two independent adjudication passes were run on this set; where they differed, each differing row was re-read against the full text and the better-supported judgement kept, so the settlements below and `rob-new-assessments-v2.csv` form one consistent pair. Agreed judgements were carried over unchanged. Overall judgements for the 6 disputed FT2 overalls and 1 disputed chasing overall were derived from the settled domains under the rob-forms.md overall rule. Outputs: `robustness/ft2/rob-new-assessments-v2.csv` (37 studies) and `robustness/search/rob-chasing-assessments-v2.csv` (2 studies).

Standing readings applied consistently, each grounded in the rob-forms.md guides: (i) D8 — absence of a registration/protocol alone does not make otherwise complete reporting selective (guide caps 8.3 at some concerns at most and low turns on all arms/topics being carried into results); a concrete unexplained gap or inconsistency in the reported counts does support some concerns (Ok_2026, Choi_2023, Suppadungsuk_2023). (ii) D3 — 'no information' only where the paper is silent in full; reported session/output handling with settings missing is some concerns; where settings/defaults, session handling and single-submission/all-outputs handling are all stated, low is met even without a sentence labelled a retry rule. (iii) D5/D6 — where the citation verifier is never identified, no information; where the text attributes verification/appraisal to the author team that generated the outputs, some concerns. (iv) Overall combination clause — high without a high domain only where the non-low domains together leave verification or the arm set unchecked (verification never performed/undescribed), not merely where many modest concerns accumulate over a described verification procedure.

## Per-disagreement settlements — FT2 new studies (79)

### 1. DiFebo_2026 (R0047) — d3_generation_settings

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: Defaults position stated (no advanced/paid/custom configuration), history cleared, each prompt submitted once with all outputs analysed — settings and output handling are as fully reported as a web-interface run allows.

### 2. DiFebo_2026 (R0047) — d7_partial_match_handling

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **some concerns** (matches assessor 2)
- Support: Methods rule separates locatable minor discrepancies from untraceable citations, but the minor-discrepancy count itself is never given apart (only 0 hallucinated main, 10/59 subanalysis), so 7.4 fails.

### 3. DiFebo_2026 (R0047) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: All five tools, four topics and the pre-specified subanalysis are reported with supplements; absence of a registration alone does not make complete reporting selective (D8 guide, 8.3 cap).

### 4. McLaughlin_2026 (R0112) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: All five models and both prompt types are reported with per-model counts (Table 3); no arm or prompt in Methods is missing from Results.

### 5. McCavitt_2026 (R0186) — d1_topic_prompt_sampling

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: All 19 recommendations of the AAOS hip-fracture CPG were queried in three perspectives — a complete enumerated frame with no selection step (cf. complete-exam frames judged low in this review).

### 6. McCavitt_2026 (R0186) — d3_generation_settings

- Assessor 1: **some concerns**
- Assessor 2: **no information**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: Paper is not silent in full: a newly opened private browsing window per prompt pair and asynchronous submission are reported, but no temperature/browsing/retry rule — part of the D3 set reported, so some concerns not no information.

### 7. McCavitt_2026 (R0186) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: All 19 recommendations, three perspectives and strength strata are reported in Tables I–III and supplements; only a registration is missing.

### 8. Knee_2026 (R0264) — d3_generation_settings

- Assessor 1: **some concerns**
- Assessor 2: **no information**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: Session handling and output handling are reported (three same-day submissions in separate sessions, all 42 responses/128 references analysed) but no settings at all — part reported, so some concerns per the D3 guide.

### 9. Knee_2026 (R0264) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: All 14 questions and all three repeats are reported for the single model (Table 2); nothing in Methods is dropped.

### 10. Knee_2025 (R0277) — d3_generation_settings

- Assessor 1: **some concerns**
- Assessor 2: **no information**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: Each question entered twice as a distinct new chat with both runs assessed, but no temperature/system/browsing settings — part of the D3 set reported, so some concerns not no information.

### 11. Knee_2025 (R0277) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: All eight questions and both repeats are reported (Table 2) for the single model; only a registration is missing.

### 12. Moskatel_2023 (R11480) — d3_generation_settings

- Assessor 1: **some concerns**
- Assessor 2: **no information**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: One run per medication in a new session with history cleared and the methodology fixed before querying are reported; temperature/settings and a retry rule are not — part reported, so some concerns.

### 13. Moskatel_2023 (R11480) — d5_verifier_independence

- Assessor 1: **no information**
- Assessor 2: **some concerns**
- Adjudicated judgement: **no information** (matches assessor 1)
- Support: The paper never identifies who verified the 115 citations (queries by LSM; citations 'documented' and title-searched, no verifier named), so independence cannot be judged at all.

### 14. Moskatel_2023 (R11480) — d6_duplicate_blinded_verification

- Assessor 1: **no information**
- Assessor 2: **high**
- Adjudicated judgement: **no information** (matches assessor 1)
- Support: Duplication/blinding of verification is never stated and the verifier is unidentified; high would require evidence verification was single and unblinded, which the paper does not establish.

### 15. Moskatel_2023 (R11480) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: All 47 medications are reported with citation counts (Table 1) and the method was fixed before querying; no arm is dropped.

### 16. Teke_2026 (R2196) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: All five models and all 20 questions are reported including the per-model reference table (Table 3); only a registration/protocol is missing.

### 17. Kang_2026 (R2282) — d3_generation_settings

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: Access protocol in Multimedia Appendix 1 documents URLs, versions, browser environment, session management and configuration parameters; each question was a single-turn query in a separate window with all outputs analysed and boilerplate removed uniformly — no output was selected or discarded.

### 18. Kang_2026 (R2282) — d5_verifier_independence

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: Verifiers XH and WH are named, but author contributions give XH a supporting Investigation role alongside TK (lead), so generation/verification separation is not clean and cannot be confirmed as complete.

### 19. Kang_2026 (R2282) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: All five models and all 10 questions are reported with the full citation classification (Table 2, appendices); only a registration is missing.

### 20. Rao_2026 (R2314) — d3_generation_settings

- Assessor 1: **some concerns**
- Assessor 2: **no information**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: A new chat session per question, individual input and no appended instructions are reported; settings and retry handling are not — part of the D3 set reported, so some concerns.

### 21. Rao_2026 (R2314) — d7_partial_match_handling

- Assessor 1: **some concerns**
- Assessor 2: **high**
- Adjudicated judgement: **high** (matches assessor 2)
- Support: No partial-match rule is stated and results are a bare dichotomy (2,867 'actual sources' vs 383 hallucinated): real references with wrong fields are folded silently into 'actual', the D7 guide's high case.

### 22. Zhou_2026 (R2352) — d1_topic_prompt_sampling

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: Topic selection came first and classification second: the study "first identified nine core topics related to the management of SMILE surgery" to capture clinical priorities, trends and controversy, and only then had a three-expert panel classify the chosen topics as Researched / Controversial / Open. The 3/3/3 balance is a post-hoc labelling of a hand-picked set inside a single procedure, not a sampling frame; every model faced the same nine topics, barring high (compare DiFebo_2026, whose prospective 2×2 maturity/specificity design both assessors recorded as some concerns).

### 23. Zhou_2026 (R2352) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: All four models and all nine topics are reported (Tables 2–4); only a registration/preprint is missing.

### 24. Liu_2026 (R2551) — d3_generation_settings

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **some concerns** (matches assessor 2)
- Support: Parameters are fixed and reported for open-source models and sessions reset, but proprietary arms ran at unstated defaults and failed queries were 'put on hold' under a vague rule — output handling is ambiguous, barring low.

### 25. Liu_2026 (R2551) — d4_verification_source

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **some concerns** (matches assessor 2)
- Support: Sources are named and broad (CNKI/Wanfang; PubMed/Web of Science/Google Scholar), but 'verified' required only being located and pertinent to the query — no field-level accuracy or DOI check covers the fields the verification claim rests on (4.2).

### 26. Liu_2026 (R2551) — d6_duplicate_blinded_verification

- Assessor 1: **some concerns**
- Assessor 2: **no information**
- Adjudicated judgement: **no information** (matches assessor 2)
- Support: No duplicate, blinded or agreement-checked reference verification is described and who searched the references is not stated, so D6 cannot be judged beyond no information.

### 27. Liu_2026 (R2551) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: All five models are reported by question type, disease category and reference authenticity (Table 5); only a registration is missing.

### 28. Ettien_2026 (R2620) — d4_verification_source

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: Each citation was searched in PubMed, the journal if listed, and via web search before being called a hallucination — a named source plus a second look, the D4 guide's low route; no DOI outcome is reported, so 4.3 is not engaged.

### 29. Ettien_2026 (R2620) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: All six tools and both prompts are reported with real/hallucinated tallies and the OpenEvidence imputation is disclosed; only a registration is missing.

### 30. Idan_2025 (R2931) — d4_verification_source

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: Existence was verified through PubMed and Google Scholar (direct URL for websites) and citation accuracy by reviewing the full text of cited papers — named multi-source checking covering existence and accuracy.

### 31. Idan_2025 (R2931) — d7_partial_match_handling

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **some concerns** (matches assessor 2)
- Support: Hallucinated/unfaithful/irrelevant categories are defined and counted apart, but bibliographic partial matches (real paper, wrong metadata) have no category and no separate count, so the partial-match rule is incomplete.

### 32. Idan_2025 (R2931) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: Exclusions are reported with pre-specified reasons (27→20), all three models are compared, and reporting follows STROBE under an IRB-approved protocol; no arm is silently dropped.

### 33. Hack_2026 (R3140) — d2_prompt_model_reporting

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: Prompt templates are printed (Table 1), interface and April 2025 generation are stated, but models are named only as GPT-4.0 and Gemini 2.0 with no exact release strings — D2 low requires exact versions.

### 34. Hack_2026 (R3140) — d3_generation_settings

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: Fresh sessions, identical prompts, browsing/deep-research explicitly not enabled, no plugins, outputs unedited, and the first chronologically generated iteration pre-selected for evaluation — settings and output selection are stated and fixed across arms.

### 35. Hack_2026 (R3140) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: All 10 manuscripts (both models, topics and styles) plus the triplicate reproducibility generations are reported; the post hoc timing of the citation audit is a methods point, not a dropped arm.

### 36. Ohlsen_2026 (R3191) — d3_generation_settings

- Assessor 1: **some concerns**
- Assessor 2: **no information**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: Each query submitted once on a single day is reported (in one continuing session, a stated limitation), but no settings — part of the D3 set reported, so some concerns.

### 37. Ohlsen_2026 (R3191) — d5_verifier_independence

- Assessor 1: **some concerns**
- Assessor 2: **no information**
- Adjudicated judgement: **no information** (matches assessor 2)
- Support: Who checked the references is not stated: the two named independent reviewers (S.M.O., S.B.P.) are described only as classifying CPG concordance, so verifier independence for citations cannot be judged.

### 38. Ohlsen_2026 (R3191) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: All 12 recommendations and both models are reported (Tables I–II); the reference analysis lacking a methods basis is carried in D4, not D8.

### 39. Pan_2026 (R3578) — d5_verifier_independence

- Assessor 1: **some concerns**
- Assessor 2: **no information**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: Methods state in the first person that the team posed the questions, recorded responses and 'manually searched the sources' — the prompting team also verified, with no separation stated and no vendor role.

### 40. Eminovic_2026 (R4081) — d3_generation_settings

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: Parameters are addressed directly (not user-configurable, left at provider defaults), with identical phrasing in fresh sessions, cache cleared, and one output per model–task (20 outputs) all scored — nothing was selected or regenerated.

### 41. Eminovic_2026 (R4081) — d6_duplicate_blinded_verification

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: Two radiologists blind-scored de-identified, randomised outputs independently with the blinding key held by a non-rating co-author — blinded duplicate verification is a stated D6 low route; the missing agreement figure for the binary reference classification does not remove the blinding.

### 42. Eminovic_2026 (R4081) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: Both models, all 10 tasks and essay-vs-Q&A strata are reported; only a registration/protocol is missing for an explicitly exploratory study.

### 43. Gwon_2024 (R4142) — d1_topic_prompt_sampling

- Assessor 1: **some concerns**
- Assessor 2: **high**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: A single benchmark topic with prompts adjusted after outputs were seen (find→show; added treatment questions) bars low, but the changes are reported in the text and no clear one-way difficulty lean is shown, so the guide's high case is not met.

### 44. Gwon_2024 (R4142) — d5_verifier_independence

- Assessor 1: **no information**
- Assessor 2: **some concerns**
- Adjudicated judgement: **some concerns** (matches assessor 2)
- Support: The paper repeatedly states 'we evaluated' existence/accuracy — grading was by the research team that designed and ran the prompts, with no separation or vendor role stated.

### 45. Gwon_2024 (R4142) — d7_partial_match_handling

- Assessor 1: **high**
- Assessor 2: **low**
- Adjudicated judgement: **low** (matches assessor 2)
- Support: Table 1 pre-defines grades A/B/C/F on title/essential/accessory matches with worked definitions, Table 2 counts every grade per flow and the ungraded (fake-title/no-answer) remainder reconciles to the 1,287 total (403 graded + 884 ungraded) — partial cases are counted apart.

### 46. Blasingame_2025 (R4234) — d1_topic_prompt_sampling

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: The database was queried for ALL clinician questions received since 2010, eligibility was determined per question against stated criteria, and only post-April-2023 requests were excluded (to match the GPT-4 cutoff) — a complete enumerated frame.

### 47. Blasingame_2025 (R4234) — d3_generation_settings

- Assessor 1: **no information**
- Assessor 2: **some concerns**
- Adjudicated judgement: **some concerns** (matches assessor 2)
- Support: aiChat used as provided and each question submitted once are reported, and a 5-question × 5-run variability test informed the single-submission decision — part of the D3 set is reported, so some concerns not no information.

### 48. Blasingame_2025 (R4234) — d7_partial_match_handling

- Assessor 1: **high**
- Assessor 2: **some concerns**
- Adjudicated judgement: **high** (matches assessor 1)
- Support: References were documented only as found or not found on PubMed/Google/Google Scholar/journal sites, with no rule for near matches — partial matches are folded silently into the 60/162 verified count, the D7 guide's high case.

### 49. Blasingame_2025 (R4234) — overall

- Assessor 1: **high**
- Assessor 2: **some concerns**
- Adjudicated judgement: **high** (matches assessor 1)
- Support: Derived under the overall rule: D7 is high, so overall is high regardless of the remaining domains.

### 50. Zhu_2025 (R4263) — d5_verifier_independence

- Assessor 1: **no information**
- Assessor 2: **some concerns**
- Adjudicated judgement: **no information** (matches assessor 1)
- Support: Who evaluated reference relevance/authenticity is never stated (passive voice); S.J.S. verified benchmark disease-occurrence answers only, and K.Z. input the questions — the citation verifier is unidentified.

### 51. Zhu_2025 (R4263) — overall

- Assessor 1: **high**
- Assessor 2: **some concerns**
- Adjudicated judgement: **high** (matches assessor 1)
- Support: Derived under the overall rule: D4 some concerns (authenticity by unnamed 'internet search') + D5 no information + D6 no information together leave verification unchecked, alongside D1–D3 at some concerns.

### 52. Bridges_2025 (R4518) — d1_topic_prompt_sampling

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: Cases were taken sequentially as published (165 NEJM cases plus 36 Friedman cases) — a stated sequential frame with no difficulty-based selection step.

### 53. Bridges_2025 (R4518) — d2_prompt_model_reporting

- Assessor 1: **some concerns**
- Assessor 2: **high**
- Adjudicated judgement: **high** (matches assessor 2)
- Support: The model is named only as ChatGPT-4 with no version string and no generation date is stated anywhere, and prompts appear only as examples — the run cannot be repeated or placed in time, the D2 guide's high case.

### 54. Bridges_2025 (R4518) — d3_generation_settings

- Assessor 1: **no information**
- Assessor 2: **some concerns**
- Adjudicated judgement: **some concerns** (matches assessor 2)
- Support: Generation handling is partly described (several prompt designs and five sequential reproducibility runs, all reported) but no settings are reported and which run supplied the verified citations is unstated — part reported, so some concerns.

### 55. Warren_2024 (R5078) — d4_verification_source

- Assessor 1: **some concerns**
- Assessor 2: **no information**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: A verification procedure is described (following the cited source/hyperlink and classifying content presence), so the domain is judgeable, but no independent bibliographic source is named — some concerns, not no information.

### 56. Warren_2024 (R5078) — d7_partial_match_handling

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: Four scenarios are defined in Methods and all four counts are printed (108 appropriate; 28 confirmed source/hallucinated information; 16 hallucinated source/contains information; 101 hallucinated/hallucinated, of 254) — partial cases counted apart.

### 57. Naldi_2024 (R5216) — d5_verifier_independence

- Assessor 1: **no information**
- Assessor 2: **some concerns**
- Adjudicated judgement: **no information** (matches assessor 1)
- Support: Who performed the PubMed hallucination check is never stated; the five-dermatologist panel scored references only after hallucinations were excluded.

### 58. Naldi_2024 (R5216) — overall

- Assessor 1: **high**
- Assessor 2: **some concerns**
- Adjudicated judgement: **some concerns** (matches assessor 2)
- Support: Derived under the overall rule: no domain is high; verification was performed against a named source (PubMed, field-level quotation checks, first-session rule), so the D4/D5/D6 concerns do not together leave verification unchecked.

### 59. Schumacher_2024 (R5403) — d7_partial_match_handling

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **low** (matches assessor 2)
- Support: Accurate/correctly cited (22/52), not located in any database (22/52) and existing but misinterpreted or incorrectly cited (8/52) are counted apart under a stated classification applied evenly to the single model. That the definitions appear with the Results rather than in Methods does not bar low in this review's practice (Gravel_2023, first pass: rule stated in a table footnote and Results with counts apart, settled low).

### 60. Sina_2024 (R5556) — d2_prompt_model_reporting

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: The prompting-style texts are printed verbatim (Table 1) and the model is given as ChatGPT (February 3, 2024 version) on GPT-4 via the public website, but the 30 question wordings themselves are never printed. In this review's practice the questions are part of the prompt for D2 (Knee_2026/Knee_2025 recorded D2 low because the questions are printed verbatim in Table 1; McCavitt_2026's agreed some concerns rests partly on prompt wording not being printed), so the run cannot be repeated exactly as run, barring low.

### 61. Kaygisiz_2025 (R5577) — d4_verification_source

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **low** (matches assessor 2)
- Support: References were searched individually in Google Scholar, PubMed and Web of Science and labelled real only if found — named sources with a cross-source existence check covering the existence outcome the study reports.

### 62. Kaygisiz_2025 (R5577) — d5_verifier_independence

- Assessor 1: **no information**
- Assessor 2: **some concerns**
- Adjudicated judgement: **no information** (matches assessor 1)
- Support: Who searched the references is never stated; the blinding described covers only the 20 specialists scoring diagnoses, not citation verification.

### 63. Ok_2026 (R6331) — d8_selective_reporting

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: A concrete reporting gap: five references per section was pre-defined across a seven-section outline, yet the paper reports 'a total of 28 citations' (5 × 7 = 35) with no explanation of the shortfall in the main text.

### 64. Safrai_2024 (R6555) — d6_duplicate_blinded_verification

- Assessor 1: **some concerns**
- Assessor 2: **no information**
- Adjudicated judgement: **no information** (matches assessor 2)
- Support: Independent duplicate scoring is described only for relevance/depth/currentness ratings; whether reference authentication itself was duplicated or blinded is never stated, so D6 is no information.

### 65. Awosanya_2024 (R6775) — d4_verification_source

- Assessor 1: **some concerns**
- Assessor 2: **no information**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: Fact-checking is described with error fields enumerated (authors, journal, title, year, volume/issue, pages, DOIs), so the domain is judgeable, but no bibliographic source used for checking is named — some concerns.

### 66. Awosanya_2024 (R6775) — d6_duplicate_blinded_verification

- Assessor 1: **some concerns**
- Assessor 2: **no information**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: Checking by all co-authors is stated, so verification was multi-author, but no independent duplicate process, blinding or agreement figure for citation checking is reported — some concerns, not no information.

### 67. Awosanya_2024 (R6775) — d7_partial_match_handling

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: AI-only arm counts are apart (19 non-existent / 31 incorrect-field / 30 misattributed of 113), but the AI-assisted arm's 18/89 'incorrect' folds misattribution and plagiarism together with no split, so partial counts are not apart for every arm.

### 68. Awosanya_2024 (R6775) — overall

- Assessor 1: **some concerns**
- Assessor 2: **high**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: Derived under the overall rule: no domain is high, and verification — though its source is unnamed — was performed by all co-authors against enumerated fields with counts apart, so the combined concerns do not leave verification or the arm set unchecked.

### 69. Choi_2023 (R6851) — d4_verification_source

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: Components were checked on named sources matching the fields the prompts requested (URLs followed; authors searched on PubMed, Amazon and Google; titles compared on PubMed) — the check covers the fields the outcomes rest on.

### 70. Choi_2023 (R6851) — d8_selective_reporting

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: All four prompts and 78 items are reported, but the additional textbook-only prompt modification's reference results are reported only as 'data not shown' — a run subset withheld without counts.

### 71. Citir_2025 (R6938) — d5_verifier_independence

- Assessor 1: **some concerns**
- Assessor 2: **no information**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: Author contributions state 'All phases of the research were performed by M.C.' — the single operator who ran the questions also verified the references, the guide's same-team case.

### 72. Citir_2025 (R6938) — d6_duplicate_blinded_verification

- Assessor 1: **high**
- Assessor 2: **no information**
- Adjudicated judgement: **high** (matches assessor 1)
- Support: Verification was single and unblinded by that sole operator with judgement-based calls and no duplicate check or agreement figure for references (reported kappas cover specialists' answer scores only) — the D6 guide's high case.

### 73. Citir_2025 (R6938) — d7_partial_match_handling

- Assessor 1: **some concerns**
- Assessor 2: **high**
- Adjudicated judgement: **high** (matches assessor 2)
- Support: No partial-match rule is stated and bibliographic field errors were not assessed; of 81 references only 13 scientific articles / 10 fake / rest website data are distinguished — partial cases are folded into a link-based fake/not-fake split with no separate counts.

### 74. Woodrow_2025 (R7018) — d1_topic_prompt_sampling

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **some concerns** (matches assessor 2)
- Support: Two author-chosen topics (broad ankle osteoarthritis; niche calcaneal fractures) with no sampling frame — a deliberate contrast pair does not create a frame, and the guide places author-chosen topics with the list printed at some concerns.

### 75. Ghanem_2024 (R7279) — d2_prompt_model_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: The citation prompt is printed verbatim, the model is ChatGPT version 4.0 (ChatGPT Plus) at chat.openai.com and the date is exact (27 November 2023); the initial prompt shown in Figure 1 is still available to the reader — all four D2 items are substantively present.

### 76. Schwartzman_2025 (R7335) — d5_verifier_independence

- Assessor 1: **some concerns**
- Assessor 2: **no information**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: Level-of-evidence and validity appraisals are attributed to 'the authors' who formulated and posed the questions, with no separation stated — the guide's same-team case; the attribution to the author team makes this judgeable, barring no information.

### 77. Aiumtrakul_2023 (R7442) — overall

- Assessor 1: **high**
- Assessor 2: **some concerns**
- Adjudicated judgement: **some concerns** (matches assessor 2)
- Support: Derived under the overall rule: no domain is high, and verification rests on a low-rated sequential multi-source check (DOI→PubMed, then Google Scholar/Web of Science), so the combined some-concerns/no-information domains do not leave verification unchecked.

### 78. Suppadungsuk_2023 (R7837) — d8_selective_reporting

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: All 12 topics and all 610 references are reported and Table 1's counts sum exactly to its overall row (40 incomplete + 192 fabricated + 122 all-correct + 256 partial = 610), so nothing is dropped. The concern is narrower than assessor 1's summary states: the text accompanying Figure 3 gives per-topic fabricated shares "ranged from 1% in acute kidney injury and general nephrology to 18% in the electrolyte domain", which Table 1 contradicts (acute kidney injury 2/51 = 4%, general nephrology 2/50 = 4%, glomerular disease 11/50 = 22%) — a figure-versus-table inconsistency in the reported counts, unexplained in the paper. (Assessor 1's other limb — general nephrology at 62% all-correct against 20% overall — is not an inconsistency: a best subgroup can exceed the overall rate, and Table 1 presents it as such.)

### 79. Suppadungsuk_2023 (R7837) — overall

- Assessor 1: **high**
- Assessor 2: **some concerns**
- Adjudicated judgement: **some concerns** (matches assessor 2)
- Support: Derived under the overall rule: no domain is high (settled D8 is some concerns), and verification was performed under a low-rated sequential multi-source procedure, so the combination does not leave verification unchecked.

## Per-disagreement settlements — citation-chasing studies (3)

### 80. Mikus_2024 (R16144) — d1_topic_prompt_sampling

- Assessor 1: **some concerns**
- Assessor 2: **high**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: One author-chosen topic from the author's own research area pursued in a single printed conversation; follow-up prompts are the letter's stated method and are printed verbatim, and no clear one-way difficulty lean is demonstrated, so the guide's high case is not met.

### 81. Jedrzejczak_2023 (R16439) — d7_partial_match_handling

- Assessor 1: **some concerns**
- Assessor 2: **no information**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: The paper's reference handling is reported (provision of sources counted per model; correctness judged by the two expert authors) with no partial-match rule or partial counts — a judgeable gap, so some concerns rather than no information.

### 82. Jedrzejczak_2023 (R16439) — overall

- Assessor 1: **some concerns**
- Assessor 2: **high**
- Adjudicated judgement: **high** (matches assessor 2)
- Support: Derived under the overall rule: no bibliographic verification was performed or described at all (D4 no information — no source named, existence never checked), with D5 and D6 at some concerns, so together the domains leave verification unchecked.

## Summary of overall counts

- FT2 new studies (`rob-new-assessments-v2.csv`, n=37): low 0, some concerns 20, high 17.
- Assessor overalls for comparison (same 37 studies): assessor 1 — low 0, some concerns 16, high 21; assessor 2 — low 0, some concerns 20, high 17. The adjudicated totals match assessor 2's totals but not its composition: the adjudicated sheet differs from assessor 1's overall on 4 studies (Gwon_2024, Naldi_2024, Aiumtrakul_2023, Suppadungsuk_2023 — all high → some concerns) and from assessor 2's overall on 4 studies (Blasingame_2025 and Zhu_2025 — some concerns → high; Awosanya_2024 and Gwon_2024 — high → some concerns).
- Chasing studies (`rob-chasing-assessments-v2.csv`, n=2): low 0, some concerns 0, high 2 (Mikus_2024 high on agreed D6; Jedrzejczak_2023 high under the combination clause — see settlement 82).
- Settlements: 82 total (79 FT2 + 3 chasing). FT2 matches: assessor 1 in 59, assessor 2 in 20, neither in 0. Chasing matches: assessor 1 in 2, assessor 2 in 1.
- Note on Gwon_2024 (R4142): the assessors agreed on overall high, but that agreement rested on the two domain judgements settled down here (assessor 1's D7 high → low on Table 1/Table 2; assessor 2's D1 high → some concerns). With settled domains D1 some concerns, D2 some concerns, D3 some concerns, D4 low, D5 some concerns, D6 no information, D7 low, D8 some concerns, no domain is high and the combination clause is not met (verification source is low and partial cases are counted apart), so the sheet records the rule-derived overall **some concerns**. Flagged for the author: this is the one study where adjudication of disagreed domains changes an agreed overall.
