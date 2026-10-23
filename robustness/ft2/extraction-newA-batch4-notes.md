# Extraction notes — Extractor A, batch 4 of 4 (NEW included studies, robustness pass, 23 Oct 2026)

Output: `extraction-newA-batch4.csv` — 30 rows (one per model arm), 13 records:
R2620, R2931, R3140, R3191, R3432, R3578, R4081, R4142, R4234, R4263, R4518, R5078, R5216.
All rows `eligibility = include_generation`. Worked independently from the full texts in
`robustness/fulltexts2/` only; extraction.csv / pass A / pass B / analysis files were not read.
Conventions: counts are as printed unless flagged DERIVED; a blank count means not extractable
under mapping rules 1–8 of `extraction-form.md`, never zero. Genuine printed zeros are entered
as 0 and justified per study below.

## R2620 — Ettien_2026 (JMLA, 2026; US librarian team)
Six chat tools, two prompts (Teach-Back at discharge; neutropenic diet), each repeated with
"additional" follow-ups by 4–7 librarian prompters per tool.
- Denominators are the printed totals across both prompts **including duplicates and repeat
  views by multiple prompters** (Results text): ChatGPT 125/177 hallucinated, Claude 37/138,
  Copilot 84/202, Gemini 97/153, Perplexity 10/334; OpenEvidence 0/163 (real total 94 + 69 from
  Table 1, no hallucinations). Unique-citation figures are also printed (e.g. ChatGPT 125/154)
  but were NOT used — flag for the author if the pool prefers unique denominators.
- "Hallucinated" = citation the team could not verify (searched PubMed, the journal if listed,
  and the web) → maps exactly to *completely fabricated*.
- "Real" = fully correct **or partially correct** (some missing/incorrect field, e.g. date or
  volume). Therefore the real count maps to neither fully-accurate strict nor lenient, and no
  major/minor/bad-DOI count is extractable. All such fields blank.
- Model versions were reported inconsistently by prompters (ChatGPT mostly 4o Mini/"auto";
  Claude some 3.5; Copilot Creative/Balanced on GPT-4/4o Mini; Gemini, OpenEvidence, Perplexity
  free/unspecified), so `model_version` records that wording and `model_year` is blank for all
  six arms. Retrieval condition not stated for any tool → "not reported".
- **Arithmetic flag:** the Gemini cells of Table 1 as printed do not sum to the Results-text
  total (97/153) used here; the text total is internally consistent with the reported 63% and
  with the other five tools' text totals matching their Table 1 sums. Not corrected, only flagged.
- Funding and conflicts: nothing stated in the paper → "Not reported".

## R2931 — Idan_2025 (Scientific Reports, 2025; Israel)
GPT-4o, Gemini 2.0, Claude Sonnet 3.5 vs human researchers on 20 complex clinical queries.
- Table 2 "Exist — No" is the fabricated count: GPT-4o 36/101, Gemini 8/26, Claude 1/64
  (sums reconcile with Table 1: 45 fabricated, 146/191 verified). Existence was checked on
  PubMed, Google Scholar, or direct URL for website sources, by an independent researcher
  blinded to report source → verifier_independent = yes.
- The paper's "Accurate/Faithful" outcome is **content faithfulness** (full text checked to see
  the citation supports the report), not bibliographic accuracy, and its denominators are
  inconsistent (Table 2: 49/70, 4/8, 62/63 vs verified 65/18/63; Table 1: 115/141 vs 146
  verified). It therefore maps to no review outcome; fully accurate / major / minor all blank.
  The 141 vs 146 and 70 vs 65 discrepancies are flagged, not resolved.
- Funding: Medint Medical Intelligence LTD. Conflicts: three authors employed by Medint;
  Einav is Medint CMO (paid); remainder none.

## R3140 — Hack_2026 (World J Otorhinolaryngol Head Neck Surg, 2026; Israel/Italy/USA)
GPT-4.0 and Gemini 2.0 writing narrative and PRISMA-style reviews on two otolaryngology topics.
No retrieval augmentation, plugins or browsing (explicit) → retrieval = none.
- Only percentages are printed, at stated denominators (GPT-4.0 n=77; Gemini 2.0 n=46).
  All conversions give whole counts with no rounding doubt and the parts sum to the totals:
  GPT-4.0 — fully accurate 89.6%→69, minor 9.1%→7, duplicate 1.3%→1, fabricated 0%→0 (sum 77).
  Gemini — fully accurate 71.7%→33, minor 4.3%→2, fabricated 23.9%→11 (sum 46).
  All flagged DERIVED in the CSV definitions_note.
- Definitions match the review's: fully accurate = correct authors, title, journal, year and
  pagination (strict); minor = metadata errors but verifiable publication; fabricated/corrupted
  = nonexistent, unverifiable or garbled author metadata. Major = fabricated only, **exact by
  partition** (remaining categories are minor errors or duplicates, neither a major inaccuracy).
- Ambiguity: the paper writes "GPT-4.0" throughout. `model_year` = 2023 (GPT-4) — if the tool
  actually used was GPT-4o the year would be 2024. Author to settle.
- Funding: Vaira only, e.INS/MUR-NRRP project (acknowledgments); others no specific funding.
  Conflicts: none declared.

## R3191 — Ohlsen_2026 (JSES Rev Rep Tech, 2026; USA)
GPT-4o and Gemini 2.5 Pro answering 12 patient-style questions from AAOS glenohumeral-arthritis
guideline recommendations (30 Apr 2025). References were not requested; they appeared in answers.
- ChatGPT: 6 references; 3 to nonexistent studies (fabricated, exact — on request for a link the
  model apologised and said the article could not be found). A 4th was a real article with the
  wrong journal named. The headline combined label "nonexistent or inappropriately cited" (4/6)
  and "only 2 appropriately referenced **and** supporting the claim" mix existence, bibliographic
  accuracy and claim support → no exact mapping to major / fully accurate / minor. Blank.
- Gemini: 32 references; **fabricated = 0** — the 5 problem references are all real papers
  (Table III gives DOIs/PMIDs; "study able to be found: Yes") that were misapplied to the claim
  (2 compared the wrong surgeries; 3 did not support or contradicted the statement); 27 were
  appropriately supportive. Because that classification is claim-support, not bibliographic,
  fully accurate / major / minor are blank and the 5 are recorded narratively in the CSV note.
  Note: review definition of major inaccuracy can include a real paper cited for a topic it
  does not cover — the author may wish to revisit whether these 5 should enter major; I did
  not map them because the paper did not check the other bibliographic fields for the 32.
- Verification source for the reference check is not named in the paper → "Not reported".
- Funding: none disclosed. Conflicts: Hsu personal fees from Enovis + ASES committee role.

## R3432 — Lin_2025 (Digital Health, 2025; Taiwan)
GPT-4, GPT-4o, Gemini 1.0 Ultra, PaLM 2 on 24 nephrology questions / biopsy reports.
- **Only the top-performing model was asked for references and only its references were
  verified.** That model (GPT-4): 131 references given, 30 duplicates removed, **101 unique
  verified, all valid and existing → fabricated 0/101**. Verification was existence-only
  (explicit: content correlation not assessed), so the paper's "100% accurate" does NOT map to
  fully accurate strict; fully accurate / major / minor / bad DOI blank.
- GPT-4o, Gemini 1.0 Ultra and PaLM 2 rows are returned with all counts blank: no references
  were requested or verified for them. This is the batch's clearest "row(s) with no extractable
  count" case.
- Funding: none. Conflicts: none declared.

## R3578 — Pan_2026 (Frontiers in Medicine, 2026; China)
DeepSeek-R1 vs ChatGPT-4.0 on 15 gout-nursing questions (Chinese). **Browsing was activated for
both** (DeepSeek Browser plugin; Browse with Bing) and built-in citation tools enabled →
retrieval = browsing for both arms (hence the arm labels carry "(browsing)").
- DeepSeek-R1: 25 papers provided, **4 with false information** → authentic denominator 21
  (all source-type percentages use 21). Abstract alternatively calls the 4 "invalid reference
  links". Mapped as fabricated = 4 (not authentic on manual search); the false-information vs
  invalid-link ambiguity is flagged for the author.
- ChatGPT-4.0: 23 references, none reported false → fabricated 0 as printed.
- No field-level bibliographic classification (mDISCERN scores answer quality, not references),
  so fully accurate / major / minor / bad DOI blank. Model labelled "ChatGPT-4.0 / version 4.0";
  model_year 2023 (GPT-4) — same 4.0-vs-4o ambiguity as R3140.
- Funding: NSFC + Guangzhou grants + hospital nursing fund (full list in CSV). Conflicts: none.

## R4081 — Eminovic_2026 (Digital Health, 2026; Germany)
DeepSeek-R1 vs ChatGPT-o1, 10 neuroradiology writing tasks. Per-reference classification:
(a) fully verifiable; (b) partially correct (real, ≥1 incorrect detail); (c) unverifiable
(not locatable via PubMed, Google Scholar or DOI lookup); (d) fully fabricated (DOI resolving
to a different publication).
- **Fabricated mapped exact-by-sum as (c)+(d)** — in both categories no single matching
  publication exists for the reference as cited. DeepSeek-R1 (n=49): (d) 36.7%→18, (c) derived
  49−27−18 = 4 → fabricated 22. ChatGPT-o1 (n=39): (d) 2.6%→1, (c) 64.1%→25 → fabricated 26.
  If the author instead wants the authors' "confirmed fabrication" category alone, those
  numbers are 18 and 1 (both stated in the CSV note).
- Fully accurate = (a), DERIVED from percentages (DeepSeek 22.4%→11/49; o1 20.5%→8/39; whole
  counts, no rounding doubt). (a) is mutually exclusive with (b) "≥1 incorrect detail", so it
  satisfies strict for the fields checked.
- Partially correct ((b): 16 and 5, derived as real − fully verifiable) is not severity-split →
  maps to neither minor nor major; major blank.
- Bad DOI = category (d) count (18 and 1): a DOI resolving to a different paper, exact as
  printed. Caveat: its denominator in the paper is all references; the DOI-carrying subset is
  not reported, so the review's bad-DOI denominator cannot be reproduced.
- "Real publications" percentages (55.1% of 49 = 27; 33.3% of 39 = 13) reconcile with the above.
- Funding: none. Conflicts: extensive disclosures for three authors, explicitly none relating
  to OpenAI, DeepSeek or the evaluated models' developers.

## R4142 — Gwon_2024 (JMIR Medical Informatics, 2024; Korea/USA)
ChatGPT (GPT-3.5, no browsing) and Bing AI (Prometheus incl. GPT-4, web search, "Precise" tone)
asked to show RCTs on Peyronie-disease treatments in named databases. Grading (Table 1):
A = PICOS + all bibliographic info matched; B = PICOS + essential info (title, author, journal,
year) matched, accessory info (issue, pages, DOI, PMID) mismatched; C = essential matched but
PICOS not (inappropriate for the question); F = title matched a real study but other essential
info did not — "considered as a fake study that was generated". No grade for a fake title.
- ChatGPT: 1287 studies presented; grades A7 B18 C167 F211 (sum 403). **Fabricated = 1095,
  DERIVED exact-by-sum** = F 211 + ungraded fake-title 884 (= 1287 − 403). This derivation is
  the batch's largest judgement call and is flagged in the CSV note: it rests on Table 2's
  denominator being studies presented (an ungraded presented study is a fake-title study, as
  Bing's single ungraded study confirms) and on the review definition counting a real title
  with wrong authors/journal/year (grade F) as fabricated. If the author rejects the subtraction,
  the printed-only fabricated count is 211 (grade F).
- Minor error = grade B = 18 (essential info intact, only accessory fields wrong → source
  remains the same, retrievable, correctly credited in the main). 
- Fully accurate NOT extractable: A also requires question-appropriateness, and C's accessory
  information was not assessed (N/A in Table 1), so the all-fields-correct total is not printed.
  Major NOT extractable: C is question-inappropriateness, not a bibliographic partition, and
  B's accessory errors are not severity-split. No separate DOI count.
- Bing AI: 48 studies, A19 B0 C28, ungraded 1. Authors state all presented studies existed and
  Bing "did not generate fake studies" → fabricated 0, minor (B) 0, both as printed.
  **Internal tension flagged:** the 1 ungraded study is described as having a fake title, yet
  also as a real PubMed-registered study misrepresented as a ClinicalTrials.gov result.
- Not extracted as an arm: a ChatGPT **plug-in (PubMed Research)** experiment discussed in the
  Discussion ("not a single case of hallucination"; 21 of the benchmark's 24 RCTs provided;
  service capped at 100 papers). No reference-level grade counts or clear denominator are
  printed for it, so no row was created; author may want a narrative mention.
- Funding: Soonchunhyang University Research Fund (no funder involvement). Conflicts: none.

## R4234 — Blasingame_2025 (JMLA, 2025; USA)
GPT-4 via the internal aiChat (Azure) answering 216 clinicians' evidence requests.
References were **not requested** in the prompt; they appeared in responses.
- Verification subsample: 66 randomly selected questions, 162 references; **60 confirmed
  nonfabricated / verified to exist**. `n_fabricated` = **102, DERIVED by subtraction**
  (162 − 60). Authors' wording for the remainder is "could not be independently verified /
  not found" (searched PubMed, Google, Google Scholar, journal websites) rather than a
  per-reference "fabricated" label; mapped as fabricated because verification was a search for
  a matching published source, and the paper's conclusions themselves frame the finding as
  reference fabrication. Flagged for the author.
- Detail accuracy / appropriateness of the verified references was explicitly not assessed →
  fully accurate / major / minor / bad DOI blank.
- Funding: NCATS CTSA UL1TR000445 (REDCap support). Conflicts: none declared.

## R4263 — Zhu_2025 (Pharmacoepidemiol Drug Saf, 2025; Sanofi authors, US/UK/Poland/Germany/France)
ChatGPT-3.5, ChatGPT-4 and Google Bard on 21 disease prevalence/incidence questions, asked twice.
Authenticity was analysed on **unique** references (duplicates removed); CSV denominators are
the unique sets, with totals in the notes.
- ChatGPT-4: 52 generated, 20 unique, all 20 authentic → fabricated 0, fully accurate 20.
- Google Bard: 109 generated, 65 unique — authentic 44 (67.7%), incomplete 5 (7.7%),
  inaccurate 7 (10.8%), **fabricated 9 (13.8%)**. (Abstract percentages are of the 65 unique,
  despite its "65/109" phrasing.)
- ChatGPT-3.5: **provided no references at all** → refs_generated = 0 (printed fact) and all
  outcome counts blank.
- Fully accurate = the "authentic" count: authentic is mutually exclusive with "inaccurate"
  (identifiable but ≥1 element incorrect — authors, journal, volume/pages, DOI, hyperlink),
  so authentic references had no incorrect element among those checked → strict, as mapped.
  "Inaccurate" is not severity-split → minor and major blank. "Incomplete" (insufficient
  information to verify existence) was not counted as fabricated, following the authors.
- Retrieval: Bard described as accessing real-time internet information (ChatGPT not
  connected) → Bard = browsing, ChatGPT arms = none. Bard's underlying model version is not
  stated in the paper → model_family "other (Google Bard)", model_year blank.
- Funding: Sanofi. Conflicts: all authors Sanofi employees/fellow, shareholdings possible.

## R4518 — Bridges_2025 (JAMIA Open, 2025; USA)
GPT-4 with a Tree-of-Thought prompt (expert panel of 2) on 201 diagnostic cases; the panel-of-2
prompt required a complete citation (authors, title, journal, page numbers, DOI) per diagnosis.
Other panel sizes were prompt variants for diagnostic accuracy only and produced no citation
data, so there is one arm.
- Printed counts: citations — 70 correct, 91 incorrect, **40 non-existent** (total 201;
  70/201 = 34.8%, matching the abstract). Fabricated = 40 (non-existent, exact; authors
  internet-searched each citation). Fully accurate = 70 (any field error → "incorrect").
- Incorrect (91) is not severity-split → major and minor blank.
- DOIs: 76 correct, 83 incorrect, 42 non-existent (total 201 — every citation carried a DOI).
  **Bad DOI = 125, exact by sum** (incorrect 83 + non-existent 42): an incorrect DOI either
  fails to resolve or resolves to a different paper, and a non-existent DOI does not resolve —
  together exactly the review's bad-DOI definition, on a denominator of 201 DOI-carrying
  references. If the author prefers only the explicitly non-resolving category, that count is 42.
- Funding: partly Microsoft AI for Good Azure credits (no role in the study). Conflicts: none.

## R5078 — Warren_2024 (Sexual Medicine, 2024; USA)
ChatGPT (GPT-3.5), Google Bard (PaLM 2), Bing AI (GPT-4) and DocsGPT (GPT-4) on Peyronie-disease
patient/preoperative questions. Citation review used four scenarios: (1) confirmed source
containing the cited information; (2) real source, cited information not in it; (3) hallucinated
source (cited source not where the hyperlink led) but information in the linked source;
(4) hallucinated source, not real, information not found.
- **Counts are reported pooled across all four chatbots, prompted cohort only: 254 cited
  sources — appropriate 108, scenario (2) 28, scenario (3) 16, scenario (4) 101.**
  The per-model breakdown is in Appendix A2, which is not part of the supplied full text, so a
  single mixed-models arm row is returned rather than four blank per-model rows. **Author
  decision needed** if per-model rows are required (would need Appendix A2).
- Fabricated = 101 as printed ("the cited source was not real"; the discussion likewise uses
  101/254 as the hallucinated-source count). Scenario (3)'s 16 are also labelled "hallucinated
  source" by the authors — if a cited source that does not match its hyperlink counts as
  fabricated, the total is 117. Flagged in the CSV note; 101 entered.
- Appropriately cited (108) requires the source to contain the cited information and is not an
  all-fields bibliographic count → fully accurate blank; major/minor/bad DOI not reported.
- **Arithmetic flag:** 108 + 28 + 16 + 101 = 253, one short of the stated 254 total. Flagged,
  not corrected.
- Funding: none declared. Conflicts: none declared.

## R5216 — Naldi_2024 (Dermatology Reports, 2024; Italy/Switzerland)
ChatGPT-4 (no plugins, no browsing — explicit) on a 23-item acne questionnaire; 3 references
requested per question. References were verified **for the first query session only**:
69 requested, 69 provided.
- 17 references were recorded as "AI hallucinations", defined as **any** error in quoting
  authors, title, journal, year, issue or pages (or a combination) against PubMed. That
  definition is broader than the review's *completely fabricated* (mapping rule 3) and gives no
  existence or severity split → fabricated, major and minor all **blank**, with the 17 recorded
  here and in the CSV note. This study therefore contributes a fully-accurate count only.
- **Fully accurate = 52, DERIVED by subtraction** (69 − 17): no error in any checked field
  (authors, title, journal, year, issue, pages; DOI not checked). Corroboration: the panel
  rated references on denominators of 52 references × 5 raters (260 judgments per criterion),
  i.e. the 52 non-hallucinated references were the ones taken forward.
- Funding: not reported. Conflicts: none (no competing interests declared).

## Cross-cutting flags for the author
1. Derived counts (all flagged in the CSV): R3140 (all counts, from percentages); R4081
   (fully accurate from percentages; unverifiable by subtraction; fabricated by sum); R4142
   ChatGPT fabricated 1095 (subtraction + sum — largest judgement call in this batch); R4234
   fabricated 102 (subtraction); R4518 bad DOI 125 (sum); R5216 fully accurate 52 (subtraction).
2. Exact-by-sum / partition mappings: R3140 major = fabricated; R4081 fabricated = unverifiable
   + fully fabricated; R4518 bad DOI = incorrect + non-existent DOIs.
3. Denominator choices where the paper prints two: R2620 total (incl. duplicates/repeat views)
   over unique; R3432 and R4263 unique verified sets over totals generated (totals in notes);
   R5078 pooled over per-model (per-model not in the supplied full text).
4. Studies contributing no fabricated count: R5216 (definition too broad) — contributes fully
   accurate only. Arms with no reference data at all: R3432 GPT-4o / Gemini 1.0 Ultra / PaLM 2;
   R4263 ChatGPT-3.5 generated zero references.
5. Arithmetic discrepancies flagged, never corrected: R2620 Gemini Table 1 vs text total;
   R2931 faithful-citation denominators (141 vs 146; 70 vs 65); R5078 category counts sum to
   253 vs stated 254.
6. `model_year` left blank where the version was not stated or was reported inconsistently
   (all R2620 arms; R4263 Bard; R5078 pooled arm). "GPT-4.0" papers (R3140, R3578) are dated
   2023 for GPT-4 with the 4o ambiguity noted.
7. `verifier_independent` uses the form's codes in words (yes / no / partly involved /
   not reported); generation in most of these studies was by the study team itself, so
   "partly involved" (R2620, R4234) means the verifying librarians were the prompters.
