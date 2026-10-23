# Search log

All searches run on 22 October 2026 by the information specialist role, through public APIs. Strings below are copied as run. Hit count is the count the source returned. Retrieved is the number of records exported from that run. Every retrieved record sits in search-results-full.json (working file, key `records_raw`, each record source-tagged and carrying its deduplicated `record_id`) and, after deduplication, in search-results.csv. No screening decisions were made in this pass: search and export only.

Date limit applied where the source supports it: 2023-01-01 to 2026-10-22 (PubMed form: 2023/01/01 to 2026/10/22).

## Runs

### PubMed, through NCBI E-utilities (MEDLINE) - core
- String as run: `((hallucinat*[Title/Abstract] OR fabricat*[Title/Abstract] OR fictitious[Title/Abstract] OR "false citation*"[Title/Abstract] OR "fake reference*"[Title/Abstract]) AND (citation*[Title/Abstract] OR reference*[Title/Abstract] OR bibliograph*[Title/Abstract]) AND ("large language model*"[Title/Abstract] OR LLM[Title/Abstract] OR ChatGPT[Title/Abstract] OR "GPT-3"[Title/Abstract] OR "GPT-4"[Title/Abstract] OR "GPT-5"[Title/Abstract] OR Bard[Title/Abstract] OR Gemini[Title/Abstract] OR Claude[Title/Abstract] OR "generative AI"[Title/Abstract]) AND ("2023/01/01"[Date - Publication] : "2026/10/22"[Date - Publication]))`
- Hit count: 372. Retrieved: 372.
- Retrieval: esearch for the full ID list, then efetch in batches of 100, XML.

### PubMed, broader variant - not run, trigger not met
- String prepared: `(ChatGPT[Title/Abstract]) AND (references[Title/Abstract]) AND (accuracy[Title/Abstract] OR fabricated[Title/Abstract]) AND ("2023/01/01"[Date - Publication] : "2026/10/22"[Date - Publication])`
- The broader variant was specified to run only if the core yielded fewer than 50 hits. The core yielded 372, so the broader variant was not run. Hit count: not obtained. Retrieved: 0.

### Europe PMC, REST API, result type core
- String as run: `(hallucinat* OR fabricat* OR fictitious OR "false citation*" OR "fake reference*") AND (citation* OR reference* OR bibliograph*) AND ("large language model*" OR LLM OR ChatGPT OR "GPT-4" OR Gemini OR Claude OR "generative AI") AND FIRST_PDATE:[2023-01-01 TO 2026-10-22]`
- Hit count: 14090. Retrieved: 14090.
- Retrieval: cursor paging, page size 100, until the cursor closed and retrieved equalled the hit count. Note on the run: a first pass stopped at 5100 retrieved because of a script safety cap; the complete set was then re-fetched with the identical string and that complete set is what is exported here. Europe PMC indexes PubMed records and preprints, including medRxiv and bioRxiv: preprint coverage for this review comes primarily from this run (see also the Crossref posted-content run below). Note on breadth: unlike the PubMed string, this string is not field-restricted to title/abstract, so its hit count is much larger and its result set much noisier. That is the count the source returned for the string as run; it has not been adjusted.

### OpenAIRE search API, keywords search
- String as run: keywords=hallucinated fabricated citations large language model ChatGPT references, fromDateAccepted=2023-01-01, toDateAccepted=2026-10-22, via the OpenAIRE publications search API (keywords/fulltext-style search), format json, size 100, paging.
- Hit count: 10. Retrieved: 10.
- OpenAIRE indexes Crossref and Europe PMC records, among other sources.

### Crossref, REST API, bibliographic query
- String as run: `query.bibliographic=hallucinated fabricated citations large language model ChatGPT references accuracy, filter=from-pub-date:2023-01-01,until-pub-date:2026-10-22, rows=1000`
- Hit count (total-results as returned): 1507235. Retrieved: 1000 (the first 1000 rows, as specified).
- Retrieval: REST API `query.bibliographic`, rows=1000. Caution on the hit count: Crossref `total-results` for a bibliographic query is a relevance match count, not a precise result set. It counts records matching any of the query terms under Crossref relevance matching and greatly overstates the number of records on this topic. It is logged here exactly as returned and must not be reported as 1.5 million relevant papers. Only the 1000 retrieved rows enter the record pool.

### Crossref, posted-content (preprint) check, including medRxiv / bioRxiv
- String as run: `query.bibliographic=hallucinated fabricated citations large language model ChatGPT references accuracy, filter=from-pub-date:2023-01-01,until-pub-date:2026-10-22,type:posted-content, rows=1000`
- Hit count (total-results as returned): 122445. Retrieved: 1000 (the first 1000 rows).
- Retrieval: REST API `query.bibliographic` with the posted-content type filter. This was run as a supplementary preprint check. The same Crossref match-count caution applies: 122445 is a bibliographic match count, not a count of relevant preprints. Primary preprint coverage is the Europe PMC run above, which indexes medRxiv and bioRxiv directly; no separate direct medRxiv/bioRxiv API run was made in this pass.

### OpenAlex, Works API - one test call
- String as run: `search=hallucinated fabricated citations large language model ChatGPT, filter=from_publication_date:2023-01-01,to_publication_date:2026-10-22, per-page=25`
- Hit count (meta.count on the test call): 1773. Retrieved: 25 (the test-call page only).
- Retrieval: ONE test call, as specified for this pass. The test call succeeded (HTTP 200), so OpenAlex is logged as searched for that test call, with the limit stated plainly: only 25 of the 1773 matching records were retrieved. A full OpenAlex retrieval was not run in this pass and must not be implied.

## Attempted and blocked

### arXiv, arXiv API
- String as run: `search_query=all:hallucinated AND all:citation AND all:"language model" AND submittedDate:[202301010000 TO 202610222359]`
- Result: BLOCKED / FAILED. The first attempt, via https://export.arxiv.org with max_results=200, timed out (read timeout, 60 seconds) with 0 records retrieved. A single retry via http://export.arxiv.org with max_results=100 returned HTTP 429. Hit count not obtained, records retrieved: 0. This source is logged as attempted and blocked, not as searched. No number has been filled in for it. A broader arXiv variant (all:hallucination AND all:reference AND all:ChatGPT, same date range) was prepared for use if the core total was under 20; it was not run, because the core run never returned a total.

### Semantic Scholar, Graph API paper search
- String as run: `query=hallucinated citations large language model ChatGPT fabricated references, year=2023-2026, limit=100, fields=title,authors,year,abstract,externalIds,journal,url`
- Result: BLOCKED. The ONE test call returned HTTP 429 ("Too Many Requests. Please wait and try again or apply for a key for higher rate limits."). Hit count not obtained, records retrieved: 0. This source is logged as attempted and blocked, not as searched, exactly as in Review 1. It was not retried persistently. A rerun needs an API key or a later date. No number has been filled in for it.

## Totals
- Records retrieved, all runs: 16497. By run: PubMed core 372; Europe PMC 14090; OpenAIRE 10; Crossref bibliographic 1000; Crossref posted-content 1000; OpenAlex test call 25; arXiv 0 (blocked); Semantic Scholar 0 (blocked).
- Duplicates removed: 512.
- Records after deduplication, taken to screening: 15985.
- Deduplication method: DOI first (normalised: lowercased, `https://doi.org/`, `http://doi.org/` and `doi:` prefixes stripped), then normalised title (lowercased, punctuation removed, whitespace collapsed) for records without a DOI. Where duplicates merged, the record with the longest abstract was kept for text fields, missing fields were filled from the duplicate records, and every contributing source was retained in the CSV `all_sources` column. Record IDs (R0001 to R15985) were assigned after deduplication, in deduplication order, in search-results.csv; the same IDs are carried on each raw record in search-results-full.json so any raw record can be traced to its deduplicated record.
- Caution for the PRISMA flow: the Europe PMC set (14090) is deliberately broad (no title/abstract field restriction) and the two Crossref runs contribute 2000 relevance-ranked rows whose source match counts (1507235 and 122445) are not usable result-set sizes. Screening load and the flow diagram must use the retrieved and deduplicated counts above, never the Crossref match counts.

## Not run in this pass
Embase, Scopus and Web of Science were not run. This environment holds no licensed access to them. Exact strings ready to run sit in search-appendix-pending.md, each marked string prepared, run pending access. The finished review must not claim those databases were searched until a dated run with a hit count is added to this log. Also not run: a full OpenAlex retrieval beyond the 25-record test call; a direct medRxiv/bioRxiv API run (preprints covered via Europe PMC and the Crossref posted-content check, as noted above); the PubMed broader variant (trigger not met, see above); the arXiv broader variant (core run blocked, see above); CINAHL, PsycINFO, Cochrane CENTRAL, ACM Digital Library and a Google Scholar pass were not part of the specified source set for this pass and were not run.
