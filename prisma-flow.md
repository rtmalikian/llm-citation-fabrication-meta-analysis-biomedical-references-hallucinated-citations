# PRISMA 2020 flow, Review 2

All counts from search-log.md, screening.csv, fulltext-screening.csv and stage3/prisma-counts.json. They match the CSVs exactly.

## Identification
- Records retrieved, all runs: 16,497 (PubMed 372; Europe PMC 14,090; OpenAIRE 10; Crossref bibliographic 1,000 of a relevance match count; Crossref posted content 1,000 of a relevance match count; OpenAlex test page 25)
- Attempted and blocked, never counted as searched: arXiv (timeout, then HTTP 429), Semantic Scholar (HTTP 429)
- Duplicates removed before screening: 512
- Records screened (title and abstract): 15,985

## Screening
- Records excluded by dual screening plus adjudication: 15,863
- Reports sought for retrieval: 122
- Reports not retrieved: 46
- Reports assessed for eligibility (full text): 76

## Included
- Reports excluded at full text, one reason each: 48 (of these, 4 reports could not be assessed on their intended text because the retrieved file did not correspond to the record and the correct text could not be obtained: R0030, R0050, R0065, R0111)
- Reports of generation experiments included: 27, reporting 25 unique studies (2 reports were duplicate extractions of a study already included and were merged at study level: Aljamaan 2024 via R0115, Tas 2026 via R0100; Athaluri 2023 arrived twice and is counted once, via R0094)
- Reports of published literature audits included, separate stratum: 1 (Yin 2026)
- Total studies included: 26 (25 generation experiments, 1 audit)

Diagram: prisma-flow-diagram.png
