# Settlement Report 1 — Robustness Pass (23 October 2026)

**Role:** Settlement Reader, Review 2 (fabricated / inaccurate LLM citations), Cochrane-style meta-analysis series.
**Scope:** Shi_2026 (full text `fulltexts/R5289.pdf`, medRxiv preprint, April 2026 version) and Aljamaan_2024 (full text `fulltexts/R5083.xml`, JMIR Medical Informatics 2024;12:e54345).
**Method:** Every disputed value was re-read in the source full text and settled against the mapping rules in `extraction-form.md` — in particular Rule 1 (extract as printed), Rule 2 (map only if the study definition covers the same cases as the review definition, no more and no fewer), Rule 3 (a broader study definition maps to no review outcome), and Rule 5 (a summed mapping is allowed only if the parts sum, without overlap, to the review definition exactly). Review definition applied throughout: **completely fabricated = no matching publication exists**. The manuscript and analysis files were not read.

---

## Part 1 — Shi_2026

### 1.1 `n_fabricated` for all seven arms — SETTLED: Pass A is correct; Pass B is wrong on every arm

**The paper's categories and definitions (verbatim, Methods §3.2, PDF p. 4):**

> "Each reference in the manuscript was verified against CrossRef and PubMed APIs. References were classified as verified (confirmed by at least one database with consistent metadata), warning (found in a database but with field discrepancies such as mismatched years), failed (not found in either database), or corrupted (contains garbled or non-ASCII text)."

**The paper's hallucination definition (verbatim, §3.2, Eq. 2, PDF p. 4):**

> "The hallucination rate is defined separately as: h = (n_fail + n_corrupt) / N_ref × 100"

**Table 3: Citation Verification Results (PDF p. 11) — cells as printed** (footnote: "Hallucination rate = (failed + corrupted) / total references × 100%. Aggregated across 3 tasks."):

| System (Table 3 label) | References | Verified | Warning | Failed | Corrupted | Hallucination Rate |
|---|---|---|---|---|---|---|
| Army (pipeline) | 49 | 45 | 2 | 1 | 1 | 2.9% |
| AI Scientist | 43 | 26 | 14 | 2 | 1 | 4.8% |
| Army (single) | 64 | 34 | 25 | 3 | 2 | 7.2% |
| Baseline | 68 | 32 | 28 | 6 | 2 | 11.3% |
| AI-Researcher | 79 | 25 | 31 | 22 | 1 | 30.7% |
| Data-to-Paper | 83 | 22 | 30 | 30 | 1 | 33.3% |
| Agent Laboratory | 97 | 40 | 21 | 35 | 1 | 36.8% |

Each row sums exactly (Verified + Warning + Failed + Corrupted = References), so the four categories are a mutually exclusive partition. Verification method (§3.4, PDF pp. 6–7): "The CrossRef and PubMed API queries for citation verification used exact title matching with fuzzy fallback (Levenshtein distance ≤ 3)."

**Settled values (Pass-A arm names; `refs_generated` agreed in both passes and matches Table 3 "References"):**

| Model arm | Pass A | Pass B | **Settled `n_fabricated`** | Wrong pass |
|---|---|---|---|---|
| AI Research Army (pipeline) | 1 | 2 | **1** | B |
| AI Scientist | 2 | 3 | **2** | B |
| AI Research Army (single) | 3 | 5 | **3** | B |
| Baseline (GPT-4) | 6 | 8 | **6** | B |
| AI-Researcher | 22 | 23 | **22** | B |
| Data-to-Paper | 30 | 31 | **30** | B |
| Agent Laboratory | 35 | 36 | **35** | B |

**The extra subcategory Pass B counted is `Corrupted`.** Pass B's `n_fabricated` = Failed + Corrupted on every arm (the B−A difference is exactly the Table 3 Corrupted cell: +1, +1, +2, +2, +1, +1, +1). Pass B recorded this as an "exact by sum" mapping to the study's own hallucination numerator (Failed + Corrupted). Pass A recorded `n_fabricated` = Failed only.

**Reasoning (one line, tied to the mapping rules):** Failed — "not found in either database" (CrossRef + PubMed, the study's named verification sources) — matches the review definition of completely fabricated exactly, whereas Corrupted is defined only by a surface text property ("contains garbled or non-ASCII text") and says nothing about whether a matching publication exists, so adding it broadens the count beyond the review definition and fails Rules 2, 3 and 5; the study's composite hallucination rate `h` is a study label, not the review's completely-fabricated outcome.

Supporting points:

- Nowhere does the paper state that a corrupted reference was searched for and not found, or that corrupted references have no matching publication. The word "corrupted" appears only in the §3.2 category list, the two score/rate formulas, §3.5 ("References classified as failed or corrupted are flagged for replacement"), and Table 3 — always as a text-integrity category, never as a non-existence finding. A garbled/non-ASCII rendering of a real publication would be "corrupted" under the printed definition while a matching publication plainly exists; counting it as completely fabricated is an inference the text does not support.
- The printed hallucination percentages cannot rescue the sum: they do not reproduce from Table 3's own aggregated counts (e.g. pipeline (1+1)/49 = 4.1%, printed 2.9%; Agent Laboratory (35+1)/97 = 37.1%, printed 36.8%), so the rates are not the aggregated (Failed + Corrupted) proportions and provide no independent evidence about the Corrupted cells. Counts were settled as printed, per Rule 1 (both passes already flagged this discrepancy; it is noted here, not corrected).

### 1.2 Retrieval coding, AI Research Army (pipeline) arm — SETTLED: external database/tool access YES; canonical code = "reference database or citation tool access"; Pass B substantively correct, Pass A's code wrong/incomplete

**Evidence (verbatim):**

- §3.3 Evaluated Systems (PDF p. 6): "AI Research Army: Our multi-agent system, evaluated in two configurations: • Single-prompt: Single manuscript generation without quality assurance. • Pipeline: Full multi-agent pipeline with citation verification and repair."
- §3.5 AI Research Army Architecture (PDF p. 7), stage 2: "Citation Verification (Jing): Extracts all references and verifies each against CrossRef and PubMed APIs. References classified as failed or corrupted are flagged for replacement."
- §3.5, stage 3: "Reference Repair (Jing): For each flagged reference, searches for verified alternatives matching the same topic, retrieves metadata from CrossRef, and replaces the original entry with a verified reference."
- Abstract: "Adding a multi-agent citation verification and repair pipeline to the best-performing system improved its citation integrity score from 40.0 to 90.9…"

**Settled value:** `reference database or citation tool access` (tools as printed: CrossRef and PubMed APIs, used for citation verification and repair inside the pipeline). The pipeline arm **did** use external database/tool access: verification and repair are sequential stages of the pipeline that produces the final manuscript (Generation → Citation Verification → Reference Repair → Quality Check), i.e. the access occurs during production of the evaluated output, after the initial draft generation and before delivery. This is the retrieval condition of the arm as evaluated; it is not the separate evaluation-time verification applied to all systems' outputs in §3.2 (that verification is the study's outcome measurement, common to every arm).

**Wrong pass:** A. Pass A's code `database` is not one of the extraction form's field-17 codes and names no tool; Pass B's code (`reference database or citation tool access (multi-agent citation verification and repair pipeline)`) matches the form's category and the text. Pass A was right in direction (some database access) but wrong as a coded value.

**Reasoning (one line):** Field 17 requires the retrieval condition per arm with the tool/corpus named as printed, and §§3.3/3.5 print CrossRef/PubMed API verification-and-repair as a constitutive stage of this arm only — the single-prompt configuration is printed as "without quality assurance," so the database-access code belongs to the pipeline arm alone.

---

## Part 2 — Aljamaan_2024

### 2.1 `n_fabricated` (all arms) — SETTLED: blank / not printed is correct; NEITHER pass wrong

Both passes leave `n_fabricated` blank for every arm, with only `n_bad_doi` populated. Confirmed from the source: **the paper prints no whole-reference fabricated count for its own experiment, and none can be derived from what it prints.**

What the paper prints instead:

- Per-identifier erroneous counts only — Table 2, "Artificial intelligence chatbot hallucinating/erroneous reference identifiers' results" (Results): seven identifier rows (Title; Digit Object Identifier; Journal name; Authors' names; Publication date; Reference web link; Reference relevance to topic prompt) × five chatbots. Spot-check of the agreed `n_bad_doi` row against Table 2's "Digit Object Identifier" row, columns in table order ChatGPT / Perplexity / SciSpace / Elicit / Bing: **89 / 73 / 8 / 4 / 53** — exactly the values both passes carry.
- A Reference Hallucination Score (RHS, 0–11) per reference — Table 1 (Methods > RHS Development) and median RHS in Table 3. Table 1's footnotes define each identifier error as a bundle, e.g. footnote d (title): "The title provided by the artificial intelligence platform is misspelled, incomplete, or nonexistent"; footnote e (DOI): "Digital object identifier is missing, inaccurate, nonexistent, or directs to a different paper." Non-existence of one identifier is never separated from misspelling/incompleteness/missingness, and no reference-level "no matching publication exists" classification is reported anywhere.
- The word "fabricated/fabrication" in the paper's own voice appears only about prior literature (Introduction; Discussion's summary of Walters and Wilder [16], whose 55%/18% figures are that study's, not this study's results).

**Settled value:** `n_fabricated` = blank (not printed / not extractable) for ChatGPT 3.5, Perplexity, SciSpace, Elicit and Bing. Blank means narrative only; it never means zero (extraction form, field 37).

**Wrong pass:** Neither — both passes agree and both are correct.

**Reasoning (one line):** Under Rule 1/Rule 2 a completely-fabricated count can only be extracted as printed under a definition matching "no matching publication exists"; this paper operationalises hallucination only as per-identifier errors and an 11-point score, so no printed count maps to the review outcome.

### 2.2 Bard arm — SETTLED: no extractable Bard arm; Bard generated 0 references and was dropped from all results tables; Pass B's omission is the correct dataset treatment, Pass A's zero row must not persist as an arm

**Evidence (verbatim):**

- Abstract, Results: "Bard failed to generate any references."
- Results, first paragraph: "Bard was the only AI chatbot that failed to produce any response to all the 10 applied medical prompts. Bard's response to our prompts was, 'I'm a language model and don't have the capacity to understand and respond.'" Same paragraph: "The AI chatbots failed to generate any reference response for 35 (7%) of the 500 references." — the 500 denominator is 5 responding chatbots × 100 requested, i.e. Bard is already excluded from the results denominator.
- Discussion > Principal Findings: "Bard failed to generate any references for all the studied 10 prompts."
- Tables 2 and 3 contain five chatbot columns/rows only (ChatGPT, Perplexity, SciSpace, Elicit, Bing); every Kruskal–Wallis test in Results is reported with df = 4. Bard has no row, column, count, or score anywhere in the results.

**Settled value:** No Bard arm in the extraction dataset. The only extractable Bard facts are `refs_generated = 0` of 100 requested (10 prompts × 10 references) and total non-response, recorded as a methods/results note (cf. extraction form field 43: an arm mentioned in methods with no results count), with all outcome fields blank. Pass B (no Bard row, Bard's failure noted in every arm's definitions note) is the correct treatment for the dataset. Pass A's Bard row is factually accurate in its note and its `refs_generated = 0`, and is **not** numerically wrong — but it is wrong as a retained arm row, because a zero-denominator non-arm would enter arm counts while carrying no extractable outcome; if it is retained anywhere for audit, it must stay `refs_generated = 0` with every outcome blank (never 0 outcomes).

**Wrong pass:** A (arm retained), with the nuance above; B correct on inclusion, A and B in substantive agreement that Bard produced nothing.

**Reasoning (one line):** The paper itself drops Bard from every results table and denominator after total non-response, so there is no Bard arm with extractable data to extract — only a documented failure to generate.

### 2.3 Retrieval coding (all responding arms) — SETTLED: `not_reported` for every arm; Pass A correct, Pass B wrong on every arm it recoded

Pass A coded all arms `not_reported`. Pass B coded Perplexity and Bing as `browsing or live search`, SciSpace and Elicit as `reference database or citation tool`, and ChatGPT 3.5 as `none`. The paper supports none of Pass B's per-arm codings:

**What the paper actually prints about retrieval/generation conditions:**

- The only "searching" instruction is in the prompt, identical for all six chatbots — Methods > Medical Prompts: "All the prompts were formulated according to the following format: (1) begin by searching PubMed for papers related to the topic; (2) review the search results and select 10 relevant and recent papers; (3) ensure that all information is accurate and up-to-date…" and "The same 10 prompts were applied to each of the 6 AI chatbots." A prompt instruction is not a report that any chatbot had, enabled, or used PubMed/web access — Bard received the same instruction and produced nothing.
- No Methods passage reports any arm's browsing/plugin/database state as set by the study (extraction form field 16/17 information). Methods > Testing AI Chatbots describes the **authors' verification**, not the chatbots' generation: "Our methodology of judging the hallucinations depended on using a systematic verification process based on PubMed and Google Scholar to ensure legitimacy, accuracy, and transparency."
- The chatbot citations (refs 19–24) give only a name and a URL per chatbot — no function description. The text contains no sentence describing Perplexity or Bing as browsing/live-search tools (the word "browse/browsing" does not occur in the paper).
- The single tool-function sentence in the paper — Discussion: "Our observations align with those of others who investigated AI platforms for writing and research objectives, as they found that Elicit and SciSpace are far more dedicated to searching for scientific papers and summarizing references [40]." — is a general characterisation attributed to other investigators, names no database or corpus accessed in this experiment, and appears in the Discussion, not in the generation methods. It describes what those tools are generally dedicated to; it does not report the retrieval condition under which they were run here.
- For ChatGPT 3.5, Pass B's positive code `none` is equally unprinted: the Introduction's only relevant sentence is generic history — "Initially, ChatGPT stored data in its database without access to continually updated human literature. It later evolved to employ internet access." — which states no setting for the version/run used in this study.

**Settled values:**

| Model arm | Pass A | Pass B | **Settled `retrieval`** | Wrong pass |
|---|---|---|---|---|
| ChatGPT 3.5 | not_reported | none | **not_reported** | B |
| Perplexity | not_reported | browsing or live search | **not_reported** | B |
| SciSpace | not_reported | reference database or citation tool | **not_reported** | B |
| Elicit | not_reported | reference database or citation tool | **not_reported** | B |
| Bing | not_reported | browsing or live search | **not_reported** | B |

**Reasoning (one line):** Field 17 records the retrieval condition of the arm as run, with the tool/corpus named as printed; this paper prints no per-arm browsing/database condition at all (only a uniform prompt instruction to search PubMed and the authors' own PubMed/Google Scholar verification), so Pass B's codings rest on outside knowledge of the products rather than on the text, and `not_reported` is the only text-supported code — including for SciSpace/Elicit, where the Discussion's "dedicated to searching for scientific papers" characterisation, quoted above, is the closest text and still reports no retrieval condition for this experiment.

---

## Actions implied for the merged dataset

1. Shi_2026: use Pass A `n_fabricated` (Failed only) for all seven arms: 1, 2, 3, 6, 22, 30, 35. Discard Pass B's Failed + Corrupted sums as `n_fabricated`; if the study's hallucination composite is wanted, it belongs in narrative under its printed label, not in the fabricated pool.
2. Shi_2026, AI Research Army (pipeline): set `retrieval` = `reference database or citation tool access` (CrossRef/PubMed verification-and-repair pipeline).
3. Aljamaan_2024: keep `n_fabricated` blank on all arms (neither pass changes); keep agreed `n_bad_doi` (89 / 73 / 8 / 4 / 53).
4. Aljamaan_2024: drop the Bard arm row (Pass B treatment); retain Bard's total non-response as a note (`refs_generated = 0`, no extractable outcomes).
5. Aljamaan_2024: set `retrieval` = `not_reported` on all five responding arms (Pass A treatment), including reverting Pass B's ChatGPT 3.5 `none`.

Machine-readable version: `robustness/settle-1.csv` (Pass-A arm names used throughout).
