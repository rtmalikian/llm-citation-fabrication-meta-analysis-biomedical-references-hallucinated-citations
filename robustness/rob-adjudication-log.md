# Risk-of-bias adjudication log — Review 2 robustness pass (23 October 2026)

Adjudicator: RoB Adjudicator agent, robustness pass. Tool: adapted 8-domain tool for citation-generation experiments (rob-forms.md) — an adapted tool, not RoB 2 and not QUADAS-2.

Method: for each of the 61 disagreement rows in `robustness/rob-disagreements.csv` (56 domain disagreements + 5 overall disagreements), the adjudicator read the relevant part of the study's full text (file mapping in `robustness/included-fulltexts.json`), weighed both assessors' normalised judgements and support summaries against what the paper actually reports, and recorded an independent judgement under the rob-forms.md domain guides. The v1 mechanical rule (take the more cautious judgement, rob_adjudicate.py) was not applied. Overall judgements for the 5 disputed overalls were derived from the settled domain judgements under the rob-forms.md overall rule. Agreed domains were carried over from stage4/rob-assessor1.csv / stage4/rob-assessor2.csv (assessor 2's 'moderate' normalised to 'some concerns', 'unclear' to 'no information'). Output sheet: `robustness/rob-assessments-v2.csv` (25 generation studies).

## Per-disagreement settlements

### 1. Mugaanyi_2024 (R0391) — d7_partial_match_handling

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: Methods (Data Collection and Validation) states the rule in advance of results: DOIs 'that did not exist or were matched to a different source were considered hallucinations', and Table 2 reports existence, accuracy, relevance, DOI existence, DOI accuracy and DOI hallucination as separate counts per discipline — partial cases are counted apart, satisfying D7 low. Assessor 2's concern is a reporting-completeness point, not a missing or uneven partial-match rule.

### 2. Mugaanyi_2024 (R0391) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: All 10 topics named in Methods/Appendix 1 and the single model (GPT-3.5) are carried into Results with counts per discipline in Table 2 (n=55 natural sciences, n=47 humanities, total 102); no arm, topic or prompt described in Methods is dropped. Nothing in the paper supports a selective-reporting concern beyond the absence of a registration, which the D8 guide caps at some concerns on 8.3 alone and does not convert an otherwise complete report.

### 3. Güneş_2026 (R2956) — d1_topic_prompt_sampling

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: Methods (Question preparation): subspecialties 'were selected to represent a broad range of clinical domains' and 'All questions were independently created by Radiologist 1 (Y.C.G.)', full list in Supplementary Material 1. That is exactly the guide's some-concerns case — author-chosen topics with the list printed in full and no external sampling frame; balance across 8 subspecialties does not create a frame, so low is not met.

### 4. Güneş_2026 (R2956) — overall

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: Derived under the rob-forms.md overall rule from the settled domains (D1 some concerns, D2–D8 low): low overall is available only where the single some-concerns domain 'cannot move the headline rates'. D1 can — the paper's own subspecialty analysis (Table 4) shows reference accuracy varying significantly by subspecialty — so the rule yields some concerns, not low.

### 5. Linardon_2025 (R3629) — d1_topic_prompt_sampling

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **low** (matches assessor 2)
- Support: Methods (Review Topics and Prompts): 3 disorders were selected to span pre-specified familiarity/maturity levels (major depressive = high, binge eating = moderate, body dysmorphic = low), crossed with general vs specialised prompts in a balanced 3×2 design, with classifications justified by publication volume, trial prevalence and population familiarity. Prompts were held constant with only the disorder substituted and 'we did not test these prompts within GPT-4o during development' — a stratified frame spanning difficulty in both directions with prompts fixed before outputs, meeting D1 low. The design deliberately varies difficulty and reports every cell; it does not favour one difficulty level.

### 6. Linardon_2025 (R3629) — d3_generation_settings

- Assessor 1: **no information**
- Assessor 2: **some concerns**
- Adjudicated judgement: **some concerns** (matches assessor 2)
- Support: The paper is not silent on generation handling: Methods states 'For each prompt, a new session was initiated, and chat history was cleared to eliminate any influence from previous interactions', and one literature review was generated per prompt. Temperature, browsing state and a retry rule are unreported, so low is not met; but because part of the D3 set (session handling, outputs per prompt) is reported, the guide's wording — no information only 'where the paper is silent in full' — gives some concerns.

### 7. Athaluri_2023 (R0094) — d1_topic_prompt_sampling

- Assessor 1: **some concerns**
- Assessor 2: **high**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: Methods: ChatGPT suggested the 50 topics and five reviewers checked them against FINER, and 'all agreed that the 50 topics adhered to the FINER criteria' — no re-prompting for more topics in fact occurred. Novelty is only one of five FINER criteria (with Feasible, Interesting, Ethical, Relevant), and the printed examples are broad undergraduate topics ('impact of technology on doctor-patient relationships', 'effect of exercise on cognitive function', green spaces and mental health), not a set that 'plainly leans' to sparse literature. Model-generated topics with no external frame bar low; a clear one-way difficulty lean, which the guide requires for high, is not shown.

### 8. Athaluri_2023 (R0094) — d2_prompt_model_reporting

- Assessor 1: **some concerns**
- Assessor 2: **high**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: The run is reported as ChatGPT (GPT-3) — a generation is named, not a bare family name — and the topic-suggestion prompt is printed verbatim ('Suggest 50 novel medical research topics that can be performed by undergraduate medical students in India...'). No generation date is stated, the second (protocol-writing) instruction is described rather than quoted, and 'GPT-3' is imprecise for the ChatGPT run. The guide's high case is 'family name only, with no version and no date'; a named generation plus a verbatim main prompt takes this out of that case, while the missing date caps it at some concerns.

### 9. Athaluri_2023 (R0094) — d3_generation_settings

- Assessor 1: **no information**
- Assessor 2: **some concerns**
- Adjudicated judgement: **no information** (matches assessor 1)
- Support: Unlike Linardon, this paper contains no generation-handling statement at all: no temperature or equivalent, no browsing/plugin state, no session rule, no statement of which output was verified beyond the structural fact of one protocol per topic, and no retry rule for outputs (the FINER passage contemplates re-prompting for topics only, and it was not used). On D3's signalling questions the paper is silent in full, which the guide judges no information.

### 10. Athaluri_2023 (R0094) — d7_partial_match_handling

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: Methods pre-specify two separate checks per reference (whether the DOI 'was functional and truly existed' and 'whether the reference article itself truly existed', via Scopus/PubMed/Google), and Results/Discussion apply them apart: of 69 references with a non-working DOI, 41 articles were found to exist and are explicitly labelled 'partial AI hallucination', against 28 that 'neither turned up on Google search nor had an existing DOI'. A stated rule, applied to the single arm, with partial cases counted apart (n=41 vs n=28) meets D7 low; that the label is spelt out in the Discussion does not undo the Methods-stated two-part check.

### 11. Athaluri_2023 (R0094) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: All 50 topics generated protocols and all 178 references from them were analysed and reported (Results; Table 3, Fleiss kappa 0.959); the study has a single model arm and no topic or prompt named in Methods is missing from Results. No dropped arm or unexplained subset is identifiable in the paper.

### 12. Athaluri_2023 (R0094) — overall

- Assessor 1: **some concerns**
- Assessor 2: **high**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: Derived under the overall rule from the settled domains (D1 some concerns, D2 some concerns, D3 no information, D4–D8 low): no domain is high. The combination route to high requires ≥3 domains at some concerns/no information 'where together they leave the verification or the arm set unchecked' — here verification is the study's strength (D4, D5, D6 all low; five independent checkers, kappa 0.959) and the single arm is fully reported, so the combination does not leave verification or the arm set unchecked. Overall is therefore some concerns.

### 13. Civelekler_2026 (R0125) — d6_duplicate_blinded_verification

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: Methods/Results (phase 2): 'Two ophthalmology experts independently classified each citation' as Fully Cited / Partially Cited / Not Cited, with Cohen's kappa = 0.74 reported. Duplicate independent verification of all citations with an agreement figure reported is the guide's stated route to D6 low. The phase-1 bibliographic screen does not dilute the duplicate expert verification of the citations themselves.

### 14. Civelekler_2026 (R0125) — d7_partial_match_handling

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **low** (matches assessor 2)
- Support: Methods state the rule in advance — 'predefined criteria': 1) Correct Publications (verifiable and relevant), 2) DOI Mismatches (correct journal, wrong DOI), 3) Incorrect Author/Journal Name, 4) Non-Correct Publications — and Table 1 counts each category apart per model, with the expert phase adding Fully/Partially/Not counts apart. The defined partial-match types (DOI mismatch, author/journal error) are therefore countable apart, meeting D7 low; the residual lump inside category 4 (unrelated vs unfindable) is a D4 coverage point already carried in the agreed D4 some concerns, not a folding of partial matches into the fabricated count.

### 15. Gravel_2023 (R0210) — d4_verification_source

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: Methods states the verification procedure: 'To verify this, we searched Pubmed using the title and authors. If unsuccessful, we searched in the journal's website.' A named primary source plus a second-source look before a reference is treated as non-existent is the guide's stated route to D4 low ('a second look on a second source, or a stated rule with the same effect, before a reference is called fabricated'), and the primary outcome rests on existence, which this check covers.

### 16. Gravel_2023 (R0210) — d5_verifier_independence

- Assessor 1: **no information**
- Assessor 2: **some concerns**
- Adjudicated judgement: **no information** (matches assessor 1)
- Support: The paper never states who verified the 59 references: the 3 co-authors are described asking the questions 'on different computers and ChatGPT accounts', and the invited corresponding authors rated response quality, not reference existence. With the verifier for the citation outcome unidentified, independence from generation cannot be judged at all — the same basis on which both assessors recorded no information for D5 in Linardon, Pastucha and Jędrzejczak, where verifiers were likewise undescribed. Some concerns would require evidence that a known team did every step; here the actor is not reported.

### 17. Gravel_2023 (R0210) — d7_partial_match_handling

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **low** (matches assessor 2)
- Support: Table footnote and Results state the rule with counts apart: among the 18 real references, 11 were journal articles 'including 3 with minor citation errors (volume and pages) and 5 with major citation errors (wrong year, volume, and pages; or wrong authors)', the remaining real references are reported apart as 5 existing websites and 2 books, and fabricated references are counted apart (41/59). Minor/major partial matches and non-article real references are each countable, meeting D7 low.

### 18. Gravel_2023 (R0210) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: All 20 questions and all 59 references from the single model are reported with counts (Table; Figure 2); no arm or topic in Methods is absent from Results. The mid-study outcome amendment (pertinence of 3 references per response → existence) is disclosed in the Methods itself with its reason ('we failed to find the first 6 articles'), so it is a reported amendment, not silent selective reporting.

### 19. Metze_2024 (R0570) — d2_prompt_model_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **some concerns** (matches assessor 2)
- Support: The prompt is printed verbatim and run dates are exact ('submitted the following prompt every day during a ten-days-period (16–25 October 2023)'), but the model is named only as 'ChatGPT-4' with no exact release string and the interface is never stated. D2 low requires full prompts, exact versions and a generation date together; the assessors likewise recorded some concerns for Linardon (GPT-4o, June 2025, appendix prompts). Verbatim prompt + dates with an imprecise version sits at some concerns.

### 20. Metze_2024 (R0570) — d7_partial_match_handling

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **some concerns** (matches assessor 2)
- Support: For references (as distinct from the response sketches, which have a stated consensus categorisation), the paper states no rule for a partly matching reference and reports results as percentages only: Table 1 gives 'Retrieved references' per professor (40, 35, 25, 35, 10, 25, 40, 50) and '% of references with hallucinations', with no inaccurate/partial counts apart. D7 low requires a stated rule plus partial counts available apart; neither is present for references. High requires partials folded silently into fabricated/accurate counts — the hallucination percentage may do this, but the paper does not say so, so the reading-based judgement is some concerns.

### 21. Pastucha_2026 (R0696) — d1_topic_prompt_sampling

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: Methods (Research Basis / Data Collection Procedure) states a reproducible frame — Web of Science search for 'guideline' in the title, ENT category, duplicates removed, 'Papers with at least 100 citations were selected', yielding the 25 topics listed in Table 1 — but the frame by construction favours one difficulty level: the authors' stated assumption is that guideline topics 'would be widely covered in the training space', i.e. settled, heavily referenced areas where accurate references are easiest to produce. A stated frame that leans clearly to the easy end bars low under the guide; the systematic, fully listed frame bars high.

### 22. Pastucha_2026 (R0696) — d2_prompt_model_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: All D2 items are present: the prompt is printed verbatim ('Please provide references to scientific papers on guidelines for [topic]. Only the bibliographic data of the papers is required'); every arm is versioned (ChatGPT 4.0, 4.1, 4.1 with browsing; Gemini 1.5 Pro, 2.5 Pro, 2.5 Pro with web search); Table 2 gives a per-version testing schedule with exact dates (8–10 July 2024; 3–6 June 2025); and prompts 'were entered separately, and the chatbots were reset to a new conversation after each question'. The functionally relevant interface difference — browsing on/off — is stated per arm.

### 23. Nieves-Lopez_2026 (R1103) — d1_topic_prompt_sampling

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: Methods (Data Set) uses a complete enumerated frame: OrthoBullets Foot and Ankle SAE forms D and E, all 200 questions (64 text-only, 128 image-based, 8 video). The only exclusion — the 8 video items 'because of Copilot's inability to interpret videos' — is format-based, stated in Methods, and applied identically to all three models, leaving 192 questions analysed. A full frame with a pre-stated, arm-even exclusion does not favour a citation-difficulty level, meeting D1 low.

### 24. Nieves-Lopez_2026 (R1103) — d8_selective_reporting

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **low** (matches assessor 2)
- Support: All three models and all 192 analysed questions are reported with counts (accuracy in Table 1; real / partially fabricated / completely fabricated comparisons in Tables 4–5 and text, e.g. fabrication 22.9% ChatGPT-5.4, 16.1% Gemini-3, 2.8% Copilot), and the only exclusion (8 video items) is explained in Methods before Results. No arm, question subset or cut in Methods is missing from Results. The complete absence of a verification source is a D4/D5/D6 matter (all agreed no information) and does not make complete reporting selective.

### 25. Chelli_2024 (R2136) — d1_topic_prompt_sampling

- Assessor 1: **high**
- Assessor 2: **some concerns**
- Adjudicated judgement: **some concerns** (matches assessor 2)
- Support: Topics were not hand-picked: the 11 systematic reviews came from a stated PubMed search (27 July 2023; 2020; rotator-cuff systematic reviews of RCTs) screened by two independent reviewers, and the two prompt versions per request were written in advance to test prompt specificity. The frame is nevertheless very narrow — a single condition, a single publication year, 11 reviews — so the topic set is not a broad or difficulty-balanced sample of biomedical topics. That places D1 at some concerns; the output-dependent retention of one prompt version is a generation/output-selection matter, settled under D3.

### 26. Chelli_2024 (R2136) — d2_prompt_model_reporting

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: Models are named as GPT-3.5, GPT-4 and Bard and the prompt structure is described with a screenshot in Figure 1, and a fresh session per request is stated; but no LLM run dates are given (only the 27 July 2023 PubMed search date) and Bard carries no version at all. A missing generation date caps D2 at some concerns under the guide, and the prompt is exemplified rather than reproduced for all requests.

### 27. Chelli_2024 (R2136) — d3_generation_settings

- Assessor 1: **some concerns**
- Assessor 2: **high**
- Adjudicated judgement: **high** (matches assessor 2)
- Support: Methods: 'To assess the impact of the prompt's specificity... we tested 2 versions of the prompt for each request. The query that led to the largest number of results was retained for this study.' The analysed output set for every request was therefore selected after seeing both variants' outputs, on an output property (yield), and the discarded variant's results are nowhere reported. Selecting which generated output enters verification after seeing the outputs is the D3 guide's high case in substance ('selecting the best looking output for verification is high'); volume-based selection after generation is the same mechanism with a different criterion.

### 28. Chelli_2024 (R2136) — d4_verification_source

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **some concerns** (matches assessor 2)
- Support: Field coverage is broad — for each LLM paper the team collected existence/hallucination status plus accuracy of authors' list, journal, year and issue, title and DOI, against the original systematic reviews as ground truth — but the paper never names the bibliographic source used to verify the existence of LLM-supplied papers (PubMed appears for the review search and for first-author affiliation country only). D4 low requires a named source fit for the topic set; an unnamed existence check with broad field coverage sits at some concerns.

### 29. Chelli_2024 (R2136) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: All 3 LLMs × 11 systematic reviews are reported with recall/precision per model (Table 3), including Bard's failure to return any result for one review ('subacromial analgesia via continuous infusion catheter'), which is reported rather than dropped. No model, review or prompt version named in Methods is missing from Results without explanation; the retained-prompt analysis is a D3 matter.

### 30. Dhaimade_2026 (R2475) — d1_topic_prompt_sampling

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **low** (matches assessor 2)
- Support: Methods (Evaluation dataset): 'The 2024 American Academy of Periodontology (AAP) In-Service Examination, comprising 331 multiple-choice questions, was used as the evaluation instrument', in full, in both presentation formats (Full Test and Individual Question), with the exam's nine topical sections used for section analysis. A complete, enumerated examination frame with no selection step meets D1 low, on the same basis as the complete SAE frame in Nieves-Lopez.

### 31. Hasnain_2025 (R3074) — d1_topic_prompt_sampling

- Assessor 1: **some concerns**
- Assessor 2: **no information**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: Topic choice is fully reported, so no information is not available as a judgement: the study poses its questions on a single author-chosen condition, conjunctivitis (title; §3.4–3.5), with the sub-questions printed in the paper. A single hand-picked topic with no sampling frame is the guide's author-chosen case (some concerns). High would require a demonstrated clear lean to one difficulty level; a single common, literature-rich condition does not by itself demonstrate the direction or strength of lean the guide requires for high.

### 32. Hasnain_2025 (R3074) — d7_partial_match_handling

- Assessor 1: **some concerns**
- Assessor 2: **high**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: A rule is stated in Methods §3.5 before the results — 'Hallucination rate = No of fake or inaccurate references / Total references generated × 100', with verification 'by searching for its title in PubMed and Google Scholar' — so the fold of inaccurate into the headline rate is explicit, not silent, and the D7 high case ('no rule stated and partial cases folded silently') is not met. But partial-match counts are not given apart (further errors such as incomplete author lists and wrong issue/volume numbers are described in text without counts, and Table 3 counts 'Fake references'), so 7.4 fails and low is not met: some concerns.

### 33. Hasnain_2025 (R3074) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: For the citation outcome, both models named in Methods (ChatGPT 4.0 and DeepSeek) are reported with their reference counts and hallucination rates (Table 3; §3.5), and the conjunctivitis question set is reported in full. No citation arm or topic described in Methods is dropped from Results; the Claude image-classification task is a separate non-citation task, not a dropped citation arm.

### 34. Tas_2026 (R3715) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: Every arm and cut named in Methods is reported: all three chatbots (ChatGPT, Gemini, Perplexity) × both output formats, with total RHS and all four subcomponents in Tables 2–6, and 'the full dataset of AI-generated references and corresponding RHS scores is publicly available at Zenodo (doi:10.5281/zenodo.19390459)'. No model, format or subtopic is dropped. That outcomes are RHS means rather than fabricated/accurate counts is an outcome-format point already carried in the agreed D7 some concerns; D8 asks whether reporting picks among the arms the study ran, and it does not.

### 35. Sawamura_2024 (R6708) — d2_prompt_model_reporting

- Assessor 1: **high**
- Assessor 2: **some concerns**
- Adjudicated judgement: **some concerns** (matches assessor 2)
- Support: Assessor 1's premise is contradicted by the paper: Methods states 'Data were collected on April 3, 2023', and the verbatim prompt is printed ('I will now ask questions related to physical therapy. Please provide answers in Japanese, accompanied by references, such as PubMed IDs (PMIDs) or digital object identifiers (DOIs)'). What is missing is any version: the model is named only as 'ChatGPT (free version)'. The guide's high case is family name only with no version AND no date; with a verbatim prompt and an exact collection date the run is placed in time, so the judgement is some concerns — the unpinned free-tier version bars low.

### 36. Sawamura_2024 (R6708) — d3_generation_settings

- Assessor 1: **no information**
- Assessor 2: **some concerns**
- Adjudicated judgement: **no information** (matches assessor 1)
- Support: No D3 item is reported: no temperature or equivalent (temperature is raised only as a limitation), no browsing/plugin state, no session or output-selection rule, and no retry rule. Standardising the prompt wording is a D2 item; it is not a generation-settings report. Where the paper is silent in full on the D3 set, the guide judges no information — contrast Linardon, where a session rule is explicitly stated.

### 37. Sawamura_2024 (R6708) — d4_verification_source

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **low** (matches assessor 2)
- Support: Methods specifies the verification procedure in full: 'searches were performed using the appended PMIDs and DOIs'; 'in cases where the title of a referenced article differed from that of the search results using PMIDs or DOIs, another search was conducted using the article title'; and only 'if an article was not found even after searching by title, PMIDs, or DOIs, it was termed a fictional paper'. Identifier resolution (PMID resolution is by definition a PubMed check) plus a title-search second look, with fabrication called only after all three fail, is the guide's 'stated rule with the same effect' as a second source, meeting D4 low despite the database not being named in so many words — unlike Chelli, where no existence-check procedure is described at all.

### 38. Sawamura_2024 (R6708) — d7_partial_match_handling

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: The near-match rule is stated in Methods (title-mismatched records re-searched by title and evaluated on content before any 'fictional paper' call), and Table 2 counts the components apart per section: PMID/DOI concordance (6/16, 0/11, 1/11), fictitious-paper rates (6/16, 5/11, 4/11) and reference-accuracy scores with weighted kappa 0.93–0.98. A stated rule with partial cases counted apart meets D7 low; the 38-vs-37 denominator slip is a reporting-accuracy point carried in the agreed D8 some concerns, not a partial-match handling failure.

### 39. Sawamura_2024 (R6708) — overall

- Assessor 1: **high**
- Assessor 2: **some concerns**
- Adjudicated judgement: **some concerns** (matches assessor 2)
- Support: Derived under the overall rule from the settled domains (D1 low, D2 some concerns, D3 no information, D4 low, D5 some concerns, D6 low, D7 low, D8 some concerns): no domain is high — assessor 1's high rested on D2 high, which falls because the paper does state the 3 April 2023 collection date. The combination route to high requires ≥3 some/no-information domains leaving verification or the arm set unchecked; verification here is checked (D4 low; D6 low — two assessors per section, weighted kappa 0.93–0.98) and the single arm is fully reported, so overall is some concerns.

### 40. Kutluay_2026 (R0436) — d2_prompt_model_reporting

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **low** (matches assessor 2)
- Support: Every D2 item is present: exact model and tier ('ChatGPT-5.3 (Plus subscription)'), generation period ('queries were performed in March 2026, shortly after the model's release'), both prompts printed verbatim ('What is the management approach for open fractures in orthopedic trauma?...' and 'Please provide PubMed-indexed references to support each of the steps mentioned above. For every topic give three citations.'), and 'the complete prompt-response sequence... provided in Appendices A–C'. This meets D2 low.

### 41. Kutluay_2026 (R0436) — d3_generation_settings

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **low** (matches assessor 2)
- Support: Generation handling is reported and fixed: 'All queries were carried out in a single session, and each response was generated once', with 'the web search function enabled' stated, all references 'recorded without correction', and the complete sequence in Appendices A–C. Single generation with no regeneration or selection, and the browsing state stated, meets D3 low on the same basis as Seifi (single run, no regeneration, retrieval state stated), where both assessors agreed low.

### 42. Kutluay_2026 (R0436) — d5_verifier_independence

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **some concerns** (matches assessor 2)
- Support: Methods (Inter-rater evaluation process): 'All references were evaluated separately by two independent reviewers, who were the two authors of the present study' — the same two authors who designed and ran the single-session query process. Independence between the two reviewers (D6, agreed low, kappa 0.966) does not create separation from generation. The guide's some-concerns case — 'the same small team doing every step, with no separation stated' — applies, as both assessors held for UçarGündoğar, where a verifier also generated the prompts.

### 43. Hueber_2023 (R0712) — d2_prompt_model_reporting

- Assessor 1: **some concerns**
- Assessor 2: **high**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: No version is stated for the tested ChatGPT (ChatGPT-4 is mentioned only anecdotally at the end), which bars low. But the guide's high case requires no version AND no date: Figure 1 is captioned '(website retrieval 18 April 2023)', prompt fragments are quoted verbatim ('write a letter for the off-label use of ruxolitinib...', 'Please list respective literature sources') and full transcripts are in online supplemental document 1. With a date and transcript-level prompt reporting present, the judgement is some concerns.

### 44. Hueber_2023 (R0712) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: Every experiment the letter describes is reported with counts: topic 1, four references, none found; topic 2 (prodromal RA, supplement topic 2), 2 of 10 manuscripts false and five of six fictitious for the Kleyer literature request within the same topic; topic 3 (JAK inhibition), five of five references 'completely fabricated'. The closing remarks on ChatGPT-4 and perplexity.ai are commentary with no described run, prompts or methods presence, so they are not dropped arms under the D8 guide.

### 45. Jędrzejczak_2024 (R1232) — d1_topic_prompt_sampling

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: Identical frame to the later journal report (Pastucha_2026): Web of Science search for 'guideline' in the title, ENT category, duplicates removed, 'Papers with at least 100 citations were then selected', 25 topics in Table 1. The frame is stated and fully listed, but it selects only highly cited guideline topics, which the authors themselves assume 'would be widely covered in the training space' — a clear lean to the easiest difficulty level, barring low; the systematic frame bars high.

### 46. Jędrzejczak_2024 (R1232) — d2_prompt_model_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **some concerns** (matches assessor 2)
- Support: The prompt is printed verbatim, prompts 'were reset to a new conversation after each question', and 'responses... were collected on three consecutive days (8–10.07.2024)'. But the models are named only as 'ChatGPT-4' and 'Gemini Advanced' — a product tier with no version string for Gemini and no exact release for ChatGPT — so exact version reporting, which D2 low requires alongside prompt and date, is not met (compare Metze, settled some concerns on the same pattern; contrast Pastucha, where every arm carries a numbered version).

### 47. Uçar_2026 (R2250) — d2_prompt_model_reporting

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **low** (matches assessor 2)
- Support: D2 reporting is complete: exact versions (ChatGPT-5.2, Claude Sonnet 4.5, DeepSeek-V3.2), exact generation dates ('Responses were generated between 22 and 24 December 2025... through their official, publicly accessible web-based interfaces'; question retrieval 21 December 2025), the questions themselves printed (Table 1), and interface/configuration stated ('publicly available free web interfaces using the default user configuration'; 'web search or external retrieval functions were not enabled'). No D2 gap is identified in either assessor's support text.

### 48. Uçar_2026 (R2250) — d6_duplicate_blinded_verification

- Assessor 1: **low**
- Assessor 2: **high**
- Adjudicated judgement: **high** (matches assessor 2)
- Support: Assessor 1's low rests on the wrong evaluator: the blinded, anonymised assessment ('model identifiers were removed') is stated only for the dermatologist's mDISCERN/GQS/accuracy evaluations, whereas §3.3 reference verification was done by designated public-health experts, with no blinding stated for that task. The paper states 'each evaluation domain was performed by a single designated expert' and 'inter-rater reliability analyses were not applicable' — i.e. single, unblinded (as reported) verification of a judgement-based classification (verifiable / inaccurate / hallucinated, §3.3) with no agreement check at all, which is the D6 guide's high case verbatim. The check is not mechanical in the 6.4 sense: 'inaccurate' requires identifying the original publication and comparing its details.

### 49. Uçar_2026 (R2250) — d8_selective_reporting

- Assessor 1: **some concerns**
- Assessor 2: **high**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: No model or question is dropped: all three models and all 20 questions are carried into Results §4.1, reference totals per model are printed in §3.3 (43 Claude, 152 ChatGPT-5.2, 103 DeepSeek-V3.2; 298 total) and all outputs are in Supplementary Materials. What is missing is the per-model hallucinated count itself — §4.1 reports only per-question ranges (ChatGPT-5.2 18.2–50.0%; DeepSeek-V3.2 10.0–58.3%; Claude 1 of 6 citing questions). Incomplete outcome counts with nothing dropped is the some-concerns pattern (compare Metze, percentages only, agreed some concerns); D8 high requires an arm dropped with no reason, which did not occur.

### 50. Uçar_2026 (R2250) — overall

- Assessor 1: **some concerns**
- Assessor 2: **high**
- Adjudicated judgement: **high** (matches assessor 2)
- Support: Derived under the overall rule from the settled domains (D1–D5 low, D6 high, D7 some concerns, D8 some concerns): any domain at high gives high overall. The deciding domain is D6 (single designated expert, no duplicate or blinded check of reference verification). This matches assessor 2's overall, but by derivation from the settled domains, not by adoption.

### 51. UçarGündoğar_2026 (R3820) — d1_topic_prompt_sampling

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **some concerns** (matches assessor 1)
- Support: Methods (Question development): 'A total of 20 open-ended questions were developed by two pediatric dentists with more than 10 years of clinical experience in MIH', 'based on the most current clinical literature and the latest evidence-based guidelines published by the EAPD and the AAPD', organised evenly into four categories and printed in full. Guideline-anchored authorship is still author choice with no sampling frame — the questions were written by the investigators, not sampled from a stated frame — which is the guide's some-concerns case (compare Güneş, settled some concerns on the same basis). No clear difficulty lean is shown, so high is not met.

### 52. UçarGündoğar_2026 (R3820) — d6_duplicate_blinded_verification

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **low** (matches assessor 2)
- Support: Methods: responses were anonymised as 'Answer 1'/'Answer 2' to keep raters blind to chatbot identity, and (Reference verification) 'All references... were cross-checked independently by two reviewers using PubMed, Google Scholar, and Web of Science. Discrepancies... were resolved through discussion until full agreement was achieved.' The D6 guide gives low for 'duplicate verification of all references... OR blinded verification with model identity hidden, or both' — the blinded branch is met for the full reference set. The absence of a kappa figure, which assessor 1 relied on, is a requirement of the duplicate-with-agreement branch only.

### 53. Bernstein_2026 (R0043) — d2_prompt_model_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: D2 items are present: model pinned as 'ChatGPT-5 (December 2025)' and used 'from February 2026 to March 2026' via paid accounts; interface stated ('default settings of the user-facing ChatGPT interface'; 'Web search was available and could be invoked automatically'); 'All finalized prompts are provided in Appendix A', with the prompt-consensus process described (Figure 1). Version + date + interface + full prompts meets D2 low (compare Kutluay, settled low on the same completeness pattern).

### 54. Bernstein_2026 (R0043) — d7_partial_match_handling

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **low** (matches assessor 2)
- Support: The rule is stated in Methods ('Hallucination was defined as the citation of nonexistent studies, studies not indexed in PubMed, or with PMIDs not associated with a published study') and partial cases are counted apart in full: Appendix A Table 2 gives, per query, fabricated references and separate incorrect counts for title, author, journal, year, pages, volume and PMID, plus correct citations (e.g. query 1: 0 fabricated, title 1, author 1, journal 1, pages 2, volume 2, PMID 0, correct 3). A stated rule, applied evenly to the single arm, with every partial type countable apart, meets D7 low. The 'not indexed in PubMed' limb is a verification-source defect, already carried in the agreed D4 high; D7's guide states a diverging rule is not high on that ground alone and is judged here only for existence and even application.

### 55. Adıgüzel_2026 (R0045) — d3_generation_settings

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **some concerns** (matches assessor 2)
- Support: Part of the D3 set is reported: 'All prompts were predefined and applied identically across both models', 'Each prompt was entered in a separate, independent session to avoid contextual influence', and a fixed output size (5 references per query–prompt combination, 300 total, all included). Temperature/equivalent, browsing state and any retry rule are unreported, so low is not met; because session handling, cross-arm sameness and output handling are reported, the paper is not 'silent in full', giving some concerns — the same basis as Linardon D3.

### 56. Adıgüzel_2026 (R0045) — d8_selective_reporting

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **low** (matches assessor 2)
- Support: All arms in Methods are reported: both models × all three prompt groups appear in Table 1 (mean accuracy and DOI accuracy per model–prompt-group cell, n=10 outputs per cell), reference-level score distributions (0/1/2) per model in Table 3, error types per model and per prompt group in Tables 4–5, against three prespecified hypotheses. Prompt-group results are reported as means because the outcome is a 0–2 accuracy score analysed at output level — a granularity choice, not a dropped cut; no model, prompt group or query in Methods is absent from Results.

### 57. Seifi_2026 (R0053) — d2_prompt_model_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **some concerns** (matches assessor 2)
- Support: Versions, date and interface are exemplary (GPT-5.3, DeepSeek-V3, Grok-4; 'queried on March 10, 2026'; 'official paid web-based interfaces using Google Chrome; retrieval... explicitly disabled'), but the prompt itself is never reproduced word for word: Methods and the Figure 1 caption describe it ('an identical zero-shot prompt instructing the generation of 10 recent peer-reviewed references from training data only', Vancouver style, instruction to avoid fabrication) without quoting it. Signalling question 2.1 asks whether the full prompt is printed word for word or only a task summary is given; a detailed summary is still a summary, so D2 low — which requires full prompts available — is not met.

### 58. Singh_2026 (R0180) — d1_topic_prompt_sampling

- Assessor 1: **some concerns**
- Assessor 2: **low**
- Adjudicated judgement: **low** (matches assessor 2)
- Support: Generation sampling is a complete frame: 'The 2024 Orthopaedic In-Training Examination (OITE; 203 questions) was administered to GPT-5' — all 203 publicly available questions (Limitations disclose that the full examination is 275 questions and public items may differ) — with 'a standardised prompt... applied uniformly to all 203 questions', printed verbatim. No topic selection step favours a difficulty level. The correctness-stratified validation subsample (all 44 incorrect + 44 randomly selected correct) is a verification-stage sample, disclosed with strata counts apart in Table 1; its effect on the pooled rate is a reporting matter carried under D8/D7, not topic or prompt sampling.

### 59. Singh_2026 (R0180) — d6_duplicate_blinded_verification

- Assessor 1: **high**
- Assessor 2: **some concerns**
- Adjudicated judgement: **high** (matches assessor 1)
- Support: Methods (Subset validation): 'Each response was independently assessed for reasoning quality and reference reliability by a single reviewer', and Limitations: 'the use of a single reviewer... no inter-rater reliability statistics could be calculated, and some subjectivity cannot be excluded'. The classification is judgement-based in the strongest sense — 'misrepresented' requires judging whether an existing source 'did not address the specific clinical topic cited or failed to directly support GPT-5's stated claim' — and the reviewer cannot have been blind to answer correctness, since validation was stratified on it. Single, unblinded, judgement-based verification with no agreement check is the D6 guide's high case verbatim; the 6.4 mechanical-check mitigation does not apply.

### 60. Singh_2026 (R0180) — d8_selective_reporting

- Assessor 1: **low**
- Assessor 2: **some concerns**
- Adjudicated judgement: **low** (matches assessor 1)
- Support: Everything in Methods is carried into Results with counts: accuracy for all 203 questions (159/203, 78.3%); the validation subsample design (all 44 incorrect + 44 randomly selected correct) is stated in the Abstract and Methods before Results, with strata reported apart in Table 1 (correct 7/44 hallucinations, incorrect 22/44; total 29/88) and by reference type in Table 2 — a reader can re-weight the pooled 33% from the printed strata. No arm or topic is dropped silently. That fabricated and misrepresented counts are pooled within 'hallucinations' is the agreed D7 some concerns, not a D8 omission.

### 61. Singh_2026 (R0180) — overall

- Assessor 1: **high**
- Assessor 2: **some concerns**
- Adjudicated judgement: **high** (matches assessor 1)
- Support: Derived under the overall rule from the settled domains (D1 low, D2 low, D3 low, D4 low, D5 some concerns, D6 high, D7 some concerns, D8 low): any domain at high gives high overall; the deciding domain is D6. This matches assessor 1's overall, reached by derivation from the settled domains rather than by adoption.

## Summary of matches

- Disagreements settled: 61 (56 domain + 5 overall).
- Judgement matched assessor 1: 34.
- Judgement matched assessor 2: 27.
- Judgement matched neither assessor: 0.

Note on 'neither = 0': every dispute was between two points on the four-point scale and, on reading, the paper supported one assessor's point in each case — in several cases because one assessor's support line misstated the paper (e.g. Sawamura_2024 D2: the 3 April 2023 collection date is stated in Methods; Uçar_2026 D6: the blinding statement covers the dermatologist's quality/accuracy scoring, not the §3.3 reference verification). No settlement required a third value.

## Overall-category changes vs v1 (rob-assessments.csv)

**2 of 25 studies change overall category.**

- Athaluri_2023: high (v1) → some concerns (v2)
- Sawamura_2024: high (v1) → some concerns (v2)

All other 23 studies keep their v1 overall category. Domain-level judgements changed in additional studies without moving the overall (e.g. Uçar_2026 D2 some concerns → low and D8 high → some concerns, overall remaining high via D6; Bernstein_2026 D2/D7 settled low, overall remaining high via the agreed D4 high; Singh_2026 D1 some concerns → low and D8 some concerns → low in assessor 2's terms, overall remaining high via D6). Full domain-by-domain comparison is available by diffing robustness/rob-assessments-v2.csv against rob-assessments.csv.

Studies with no assessor disagreements (Aljamaan_2024, Shi_2026) are carried into the v2 sheet unchanged.
