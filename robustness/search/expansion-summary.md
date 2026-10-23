# Expansion summary — Robustness Pass search expansion (23 October 2026)

Information Specialist pass under Standard v2 item 2 (full retrieval, blocked-source retries, systematic citation chasing). All outputs in this folder (`robustness/search/`); the main search log was not edited — the coordinator merges. **No screening decisions were made.** The coded screeners were run on the new records as **triage only** (see §5).

Dates/times: runs on 23 October 2026 (UTC timestamps in `retry-log.md`; 22 October evening PDT).

## 1. Per-source retrieved counts

| Expansion source | Hit count | Retrieved | Status |
|---|---|---|---|
| OpenAlex full (`openalex_full`) | **not obtained this pass** (v1 test call, 22 Oct 2026: meta.count 1,773) | 0 | **BLOCKED after retries** — see §2 |
| arXiv retry (`arxiv_retry`) | not obtained | 0 | **BLOCKED AFTER RETRIES** — see §3 |
| Semantic Scholar retry (`semanticscholar_retry`) | not obtained | 0 | **BLOCKED AFTER RETRIES** — see §3 |
| Citation chasing, backward (`chasing_backward`) | — (per-seed, §4) | 534 raw candidates | Searched via Europe PMC + Crossref fallback |
| Citation chasing, forward (`chasing_forward`) | — (per-seed, §4) | 445 raw candidates | Searched via Europe PMC |
| **Total raw candidates entering dedup** | | **979** | all from chasing (the three database routes above returned 0 records) |

Files: `openalex-full.json` (blocked status, error body and attempt log recorded in the file; `records` is empty — nothing was retrieved and no records were invented), `chasing-raw.json` (979 records, each with `seed`, `seed_group`, `direction` and `chasing_source` per record). No `arxiv.json` / `semanticscholar.json` was written, because no route for either source succeeded — writing an empty export would risk it being read as a searched source.

## 2. OpenAlex full retrieval — BLOCKED (task a)

- String as specified from the v1 log: `search=hallucinated fabricated citations large language model ChatGPT`, `filter=from_publication_date:2023-01-01,to_publication_date:2026-10-22`, cursor paging at `per-page=200`, `mailto=rtmalikian@gmail.com` (polite pool).
- Three attempts (02:31, 02:32, 02:33 UTC, spaced 30s/60s) each returned **HTTP 429** on the first page. The API error body states the request has no API key and counts against a free daily budget **shared by everyone on this network's IP address**, that the budget is **$0 remaining**, and that it **resets at midnight UTC**.
- Therefore: meta.count this pass = **not obtained** (the 1,773 figure is v1's, from 22 October, and is reported only as v1's). Retrieved = **0**. OpenAlex full retrieval is logged as **blocked after retries, not searched in full**.
- The error body suggested obtaining a free per-user API key via a link emailed to the user, activated by a click. That signup was **not** performed in this pass: creating an account/API key and triggering an email to the author was not a step named in the task. **Flag for coordinator/author:** one free OpenAlex API key (author clicks the emailed activation link) or a rerun after the midnight-UTC budget reset would unblock the full 200-per-page cursor retrieval exactly as scripted.
- Downstream consequence, stated plainly: because OpenAlex was blocked, the OpenAlex `works` / `cited_by_api_url` route for citation chasing was also unavailable. Chasing (§4) was therefore run on the other free APIs the task allows — Europe PMC references/citations, with a Crossref references fallback — and is labelled with its actual API source per record in `chasing-raw.json`.

## 3. Retry outcomes — arXiv and Semantic Scholar (task b, full detail in `retry-log.md`)

Two attempts per source, by separate routes, spaced 15–20s apart, 23 October 2026:

- **arXiv — BLOCKED AFTER RETRIES.** Route 1, `export.arxiv.org` API (v1 query, `max_results=200`): **read timeout at 60s**, 0 retrieved (same failure mode as v1's first attempt). Route 2, `arxiv.org/api/query` (same query): **HTTP 429 "Rate exceeded."**, 0 retrieved. Hit count not obtained on either route; no count invented.
- **Semantic Scholar — BLOCKED AFTER RETRIES.** Route 1, Graph API paper search (v1 query, `limit=100`): **HTTP 429** ("Too Many Requests… apply for a key"). Route 2, bulk search endpoint (`/graph/v1/paper/search/bulk`, same query): **HTTP 429** on the first bulk call, 0 retrieved. Hit count not obtained on either route; no count invented.

Both sources remain **attempted and blocked after retries**, exactly as Standard v2 requires them to be logged — never as searched.

## 4. Citation chasing (task c)

**Seeds (28):** the 25 included generation studies + Yin 2026 audit (record IDs and full-text map in `robustness/included-studies.json` / `included-fulltexts.json`; seeds resolved by the DOI/PMID carried on their `search-results.csv` record) + the competing citation/hallucination reviews named in `manuscript.md`: **Basu & Huynh 2026** (mitigation systematic review) and **Topaz 2026** (Lancet fabricated-citations audit, named in the manuscript's Background/References). Zhao 2025 was **excluded** per instruction (different topic — ambient scribes). Chelli 2024 is an included generation seed, so its chasing is counted in the included group, not double-counted as a review seed.

**Method:** Europe PMC `/{source}/{id}/references` (backward) and `/{source}/{id}/citations` (forward), paging at 1,000 until the endpoint hitCount was reached (retrieved equalled hitCount for every resolved Europe PMC seed). Seeds resolved in Europe PMC: **26 of 28**. Crossref `works/{doi}` reference lists were then run as a backward fallback for every seed whose Europe PMC reference list was empty or which Europe PMC could not resolve, adding: Jędrzejczak 2024 +38, Kutluay 2026 +16, Shi 2026 +11, Topaz 2026 +10 (Topaz resolved by Crossref title search; DOI 10.1016/S0140-6736(26)00603-3 as returned by Crossref). Civelekler 2026 and Yin 2026 returned **0** reference entries via Crossref as well as Europe PMC — logged as zero metadata available via these free APIs, not as zero references in the papers. Topaz and Kutluay have no Europe PMC forward chasing (not resolved there); Yin, Shi and Civelekler forward counts in Europe PMC were 0.

**Raw yield (979 candidates in `chasing-raw.json`):**

| Seed group | Backward | Forward | Total |
|---|---|---|---|
| Included generation studies (25 seeds) | 513 | 444 | 957 |
| Yin 2026 audit (1 seed) | 0 | 0 | 0 |
| Competing reviews (Basu & Huynh 2026; Topaz 2026) | 21 | 1 | 22 |
| **Total** | **534** | **445** | **979** |

Largest per-seed yields: Chelli 2024 — backward 26, forward 198; Aljamaan 2024 — backward 31, forward 87; Gravel 2023 — backward 42, forward 69 (seed resolved via the DOI/PMID on its record R0210). Full per-seed table is derivable record-by-record from `chasing-raw.json` (`seed`, `direction` fields on every record).

**Known limits of this chasing pass:** Europe PMC reference/citation lists carry no abstracts and (for references) often no DOI — those fields are empty in `chasing-raw.json` rather than filled from elsewhere; Crossref fallback reference entries carry only the first author as printed by Crossref. Chasing is therefore a candidate-generation step, as the protocol specifies; nothing here is a screening decision.

## 5. Deduplication and new records (task d)

- Existing set: `search-results.csv` streamed (never loaded whole), **15,985 records** confirmed, IDs R0001–R15985.
- Method (v1): normalised DOI first (lowercase; `https://doi.org/`, `http://doi.org/`, `doi:` prefixes stripped), then normalised title (lowercase, punctuation removed, whitespace collapsed). A candidate counted as already-in-existing if its normalised DOI **or** its normalised title matched the existing set; within-candidate deduplication used the same two keys, with contributing expansion sources merged into `all_sources`.
- **Overlap with existing set: 454** (backward 172; forward 282).
- **Within-set duplicates: 36** (backward 32; forward 4).
- **Unkeyable candidates (no DOI and no title): 0.**
- **Genuinely new records: 489** — backward 330, forward 159. By seed group of first occurrence: included generation studies 475; competing reviews 14; Yin audit group 0.
- New IDs assigned continuing the sequence, **R15986–R16474**, in `new-records.csv`, whose columns match the `search-results.csv` header exactly (`record_id,title,authors,year,journal,doi,pmid,pmcid,abstract,url,source,all_sources`). `source` is the expansion source (`chasing_backward` / `chasing_forward`); no new records carry `openalex_full`, `arxiv_retry` or `semanticscholar_retry`, because those routes retrieved 0 records.
- Note on abstracts: most new records have an **empty abstract** — the Europe PMC references/citations endpoints and Crossref reference lists do not return abstracts. This directly limits the triage in §6 and must be remembered when the coordinator plans real screening of these 489 records (title-only material for most).

## 6. Triage of the new records (task e — TRIAGE ONLY, not screening decisions)

The v1 `screen_stage1.py` rules were re-run restricted to the 489 new records: Screener A (strict), Screener B (sensitive), and the v1 coded adjudication used **only as the triage call**, per Standard v2 item 4 (a coded rule may triage; it may not finally exclude or settle).

- Screener A include: **3**; Screener B include: **3**; triage include: **3** (R16012, R16143, R16145 — all backward-chasing records whose titles carry citation + LLM + fabrication terms).
- **A/B disagreements: 0** — so `new-disagreements.csv` contains only its header row. This is a real result of the rules on this material, not a missing file: with abstracts absent for most records, B's sensitive title+abstract rule collapses toward A's title-based rule.
- Outputs: `new-screening-triage.csv` (`record_id,screener_a,screener_b,triage_call`, 489 rows) and `new-disagreements.csv` (header + 0 disagreement rows, with `title` and `abstract` columns as specified).
- **Warning to the coordinator:** 0 triage disagreements does **not** mean the 486 triage-excluded records are screened out. Under Standard v2 they still require the real dual-screening/adjudication workstream, and the empty abstracts mean that workstream should consider abstract enrichment (e.g. Europe PMC search by PMID/DOI) before or during screening.

## 7. What remains blocked / flagged for the coordinator

1. **OpenAlex full retrieval** — rerun after midnight UTC (shared-IP budget reset) or with a free per-user API key activated by the author. Until a dated full run lands, OpenAlex must stay described as a 25-record test call (v1) plus a blocked full retrieval (this pass).
2. **arXiv and Semantic Scholar** — blocked after two routes each in this pass (and blocked in v1). A further retry on a later date, or a Semantic Scholar API key, are the remaining routes; neither source may be reported as searched.
3. **Forward chasing for Topaz 2026 and Kutluay 2026, and any chasing for Yin 2026** — no yield via the free APIs used here (Europe PMC unresolved/empty; Crossref carries no forward-citation data used here). An OpenAlex rerun (item 1) would close this gap via `cited_by_api_url`.
