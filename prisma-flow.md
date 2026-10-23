# PRISMA 2020 flow, Review 2 (corrected version, robustness pass 23 October 2026)

All counts from search-log.md, screening.csv, fulltext-screening.csv, stage3/prisma-counts.json and the robustness pass files under robustness/. The first version's counts are given at the end for comparison.

## Identification
- Records retrieved, database runs (22 Oct 2026): 16,497 (PubMed 372; Europe PMC 14,090; OpenAIRE 10; Crossref bibliographic 1,000 of a relevance match count; Crossref posted content 1,000 of a relevance match count; OpenAlex test page 25)
- Citation chasing candidates (robustness pass, 23 Oct 2026): 979 raw (Europe PMC references and citations, Crossref fallback; seeds = 25 first version generation studies + Yin 2026 audit + Basu and Huynh 2026 + Topaz 2026)
- Attempted and blocked, never counted as searched: arXiv (timeout, then HTTP 429; retried in the pass by two routes, timeout and HTTP 429), Semantic Scholar (HTTP 429 in v1; retried in the pass by two routes, HTTP 429 on both), OpenAlex full retrieval (attempted three times in the pass, HTTP 429, shared network budget exhausted; v1 test page of 25 records stands as its only retrieval)

## Deduplication
- Database set: 512 duplicates removed, 15,985 records screened
- Chasing set: 454 candidates already in the database set, 36 within-set duplicates, 489 genuinely new records screened

## Screening
- Records screened (title and abstract): 16,474 (15,985 + 489)
- Records excluded at screening after dual independent screening and adjudication by reading: 16,181 (database set: 15,863 excluded at screening in total, after the robustness pass re-adjudicated all 913 screener disagreements by reading and passed 190 to full text; chasing set: 445 excluded by both screeners, 54 adjudicated by reading, 47 excluded)
- Reports sought for retrieval: 293 (122 first pass + 161 re-adjudicated + 10 chasing)
- Reports not retrieved: 115 (46 + 66 + 3)
- Reports assessed for eligibility (full text): 178 (76 + 95 + 7)

## Included
- Reports excluded at full text, one reason each: 111 (48 + 58 + 5)
- Reports of generation experiments included: 66, reporting 63 unique studies (Jedrzejczak 2024 is the preprint of Pastucha 2026, merged at study level in the corrected version; the first version counted the two reports as two studies)
- Reports of published literature audits included, separate stratum: 1 (Yin 2026)
- Total studies included: 64 (63 generation experiments, 1 audit)

## First version (22 October 2026), for comparison
- 16,497 retrieved; 512 duplicates removed; 15,985 screened; 15,863 excluded at screening; 122 sought; 46 not retrieved; 76 assessed; 48 excluded at full text; 27 generation reports counted as 25 studies, plus 1 audit (26 total)

Diagram: prisma-flow-diagram.png
