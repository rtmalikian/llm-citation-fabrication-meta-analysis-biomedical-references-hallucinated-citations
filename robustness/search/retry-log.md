# Retry log — arXiv and Semantic Scholar, plus OpenAlex full-retrieval attempts (Robustness Pass, 23 October 2026)

v1 outcomes: arXiv — timeout (60s) then HTTP 429, 0 retrieved, logged blocked. Semantic Scholar — HTTP 429 on one test call, 0 retrieved, logged blocked. OpenAlex — one test call succeeded, meta.count 1,773, only 25 retrieved (partial).

## OpenAlex full retrieval attempts (this pass)

- **2026-10-23T02:31:49+00:00** — attempt 1: HTTP 429: {"error":"Rate limit exceeded","message":"Insufficient budget. This request has no API key, so it counts against the free daily budget shared by everyone on your network's IP address, and that budget is used up ($0 remaining; resets at midnight UTC). Use your own key instead: add ?api_key=YOUR_KEY to the URL, or send it as an \"Authorization: Bearer YOUR_KEY\" header. Keys are free and have their own budget: https://help.openalex.org/api/authentication/ An AI agent can get one for its user in one call: POST https://api.openalex.org/api-keys with {\"email\": \"<your user's email>\"}; we email t
- **2026-10-23T02:32:19+00:00** — attempt 2: HTTP 429: {"error":"Rate limit exceeded","message":"Insufficient budget. This request has no API key, so it counts against the free daily budget shared by everyone on your network's IP address, and that budget is used up ($0 remaining; resets at midnight UTC). Use your own key instead: add ?api_key=YOUR_KEY to the URL, or send it as an \"Authorization: Bearer YOUR_KEY\" header. Keys are free and have their own budget: https://help.openalex.org/api/authentication/ An AI agent can get one for its user in one call: POST https://api.openalex.org/api-keys with {\"email\": \"<your user's email>\"}; we email t
- **2026-10-23T02:33:19+00:00** — attempt 3: HTTP 429: {"error":"Rate limit exceeded","message":"Insufficient budget. This request has no API key, so it counts against the free daily budget shared by everyone on your network's IP address, and that budget is used up ($0 remaining; resets at midnight UTC). Use your own key instead: add ?api_key=YOUR_KEY to the URL, or send it as an \"Authorization: Bearer YOUR_KEY\" header. Keys are free and have their own budget: https://help.openalex.org/api/authentication/ An AI agent can get one for its user in one call: POST https://api.openalex.org/api-keys with {\"email\": \"<your user's email>\"}; we email t

Outcome: **blocked**. Retrieved for export: 0. Meta count this pass: not obtained. The API error body stated the shared network IP's free daily budget was exhausted ($0 remaining, resets midnight UTC) and suggested obtaining a free per-user API key via an emailed activation link. That signup was NOT performed in this pass (account creation / external email step not named in the task); it is flagged for the coordinator/author. OpenAlex is therefore logged here as **blocked after retries** for the full retrieval, not as searched in full.

## arXiv and Semantic Scholar retry attempts (this pass)

At least two attempts per source, by separate routes, spaced with sleeps (15–20s) between calls.

- **2026-10-23T02:34:20+00:00** — arXiv — Route 1: export.arxiv.org API (https://export.arxiv.org/api/query)
  - Attempt: `https://export.arxiv.org/api/query?search_query=all:hallucinated AND all:citation AND all:"language model" AND submittedDate:[202301010000 TO 202610222359]&start=0&max_results=200`
  - Outcome: ERROR — ReadTimeout: HTTPSConnectionPool(host='export.arxiv.org', port=443): Read timed out. (read timeout=60)
  - Hit count: not obtained; Retrieved this attempt: not obtained
- **2026-10-23T02:34:36+00:00** — Semantic Scholar — Route 1: Graph API paper search (api.semanticscholar.org/graph/v1/paper/search)
  - Attempt: `https://api.semanticscholar.org/graph/v1/paper/search`
  - Outcome: HTTP 429 — {"message": "Too Many Requests. Please wait and try again or apply for a key for higher rate limits. https://www.semanticscholar.org/product/api#api-key-form", "code": "429"}
  - Hit count: not obtained; Retrieved this attempt: not obtained
- **2026-10-23T02:34:57+00:00** — arXiv — Route 2: arxiv.org API endpoint (https://arxiv.org/api/query)
  - Attempt: `https://arxiv.org/api/query?search_query=all:hallucinated AND all:citation AND all:"language model" AND submittedDate:[202301010000 TO 202610222359]&start=0&max_results=200`
  - Outcome: HTTP 429 — Rate exceeded.
  - Hit count: not obtained; Retrieved this attempt: not obtained
- **2026-10-23T02:35:18+00:00** — Semantic Scholar — Route 2: Bulk search endpoint (api.semanticscholar.org/graph/v1/paper/search/bulk)
  - Attempt: `https://api.semanticscholar.org/graph/v1/paper/search/bulk (bulk call 1)`
  - Outcome: HTTP 429 — {"message": "Too Many Requests. Please wait and try again or apply for a key for higher rate limits. https://www.semanticscholar.org/product/api#api-key-form", "code": "429"}
  - Hit count: not obtained; Retrieved this attempt: 0

## Summary

- arXiv: BLOCKED AFTER RETRIES — no records exported, no hit count invented.
- Semantic Scholar: BLOCKED AFTER RETRIES — no records exported, no hit count invented.
- OpenAlex full: blocked (see above).
