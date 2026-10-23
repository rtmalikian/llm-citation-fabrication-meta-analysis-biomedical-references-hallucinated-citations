# PROSPERO registration form, field by field

Prepared 22 October 2026 for submission at PROSPERO (University of York, Centre for Reviews and Dissemination) and, in parallel, for an Open Science Framework (OSF) registration record. Wording below matches protocol.md version 1.0, dated 22 October 2026. Paste each field as written. Fields that PROSPERO fills from an account, such as named contact address, are marked account field and left to the account holder.

Registration statement, to be read with every field below: no PROSPERO registration number exists at the time this form was prepared. No PROSPERO number was issued before analysis. No date in this form is backdated. If a number is issued after submission, the finished review will report the number with the date it was issued and will state how far the review had progressed by that date. If no number has been issued by publication, the finished review will state that plainly.

## 1. Review title
Fabricated citations from large language models: how often references are completely fabricated, how often they contain a major inaccuracy, and how often they are fully accurate. A systematic review and meta-analysis of citation generation experiments, with a separate stratum for audits of the published literature.

## 2. Original language title
English as above. No other language version.

## 3. Anticipated or actual start date
22 October 2026 (protocol date). No pooled result exists at this date.

## 4. Anticipated completion date
To be set at submission. Planned within 12 months of the protocol date so the search stays current.

## 5. Stage of review at time of submission
Preliminary searches: protocol stage, search strings in preparation at drafting. Piloting of the study selection process: not started at protocol drafting. Formal screening: not started at protocol drafting. Data extraction: not started at protocol drafting. Risk of bias assessment: not started at protocol drafting. Data synthesis: not started at protocol drafting. This stage statement will be updated to match the facts on the day the form is submitted, and any update will be dated. No stage will be described as earlier than it was.

## 6. Named contact
Raphael Malikian. ORCID: 0009-0008-4326-4205. Account field for email and address.

## 7. Named contact email
Account field.

## 8. Named contact address
Account field.

## 9. Named contact phone number
Account field. Optional on the form.

## 10. Organisational affiliation of the review
None. Independent researcher. No institutional affiliation claimed for this review.

## 11. Review team members and their organisational affiliations
Raphael Malikian, independent researcher. Sole named author and principal investigator at registration. Healthcare founder and operator, clinical AI builder.
In place of a human research team, the review uses a team of large language model roles, set out in the subsection below and in the protocol. The model roles are tools under the author direction. They are not team members in the PROSPERO sense, hold no authorship, and carry no accountability, which rests with the human author alone.

### LLM team in place of a human research team
A Cochrane author team has a search specialist, two screeners who work apart, two extractors, a risk of bias pair, a statistician, a GRADE assessor and a methods editor. This review maps each job to a named language model role: information specialist; screener A and screener B; adjudicator; extractor A and extractor B; risk of bias assessor pair; statistician; GRADE assessor; methods editor. Exact prompts sit in prompts.md.
Independence rules: screener A and screener B work in separate passes with separate prompts, and neither sees the other calls until both passes are complete. The same rule holds for the extractor pair and the risk of bias pair. A merge step done by code counts agreements and disagreements and makes no judgement. The adjudicator settles screener disagreements with a logged reason. Items it cannot settle go to the human author.
Human oversight: the author set the question and eligibility rules, settles flagged items and all risk of bias and GRADE disagreements, checks every pooled number against its source, and signs off the final numbers.
Disclosure, RAISE 2025: tool, version, dates, prompts and verification steps are logged in the review team log and reported in the finished review, in line with the 2025 RAISE statement on responsible AI use in evidence synthesis.
Mechanics reported as results: inter-screener agreement rate and Cohen kappa at title and abstract, count and type of disagreements, adjudication outcomes, and extraction discrepancy rate. These counts are reported in the review methods and results.

## 12. Funding sources and sponsors
None. No grant, no sponsor, no industry funding, no in kind product access.

## 13. Conflicts of interest
None. The author has no industry affiliation of any kind and is fully independent.

## 14. Collaborators
None at registration.

## 15. Review question
When large language models generate citations or reference lists for biomedical and clinical topics, what proportion of the generated references are (a) completely fabricated, (b) inaccurate in a way that prevents retrieval or misattributes the source, and (c) fully accurate, and how do those proportions vary by model and model generation, use of retrieval, browsing or a reference database, specialty or topic, number of references requested, and year?

Objectives, in one sentence form for the record: To estimate, from citation generation experiments, the proportions of large language model generated biomedical references that are completely fabricated, that contain a major inaccuracy, and that are fully accurate, and to examine how those proportions vary by model, retrieval, topic and list length, with audits of the published literature reported as a separate stratum.

## 16. Searches
Sources to be searched, each run dated with string and hit count logged: PubMed (MEDLINE, NCBI E-utilities), Europe PMC, OpenAlex, Semantic Scholar, Crossref, and arXiv and medRxiv for preprints. No start date limit. Search end date is the run date per source. No language limit at search.
Strings are prepared, with runs pending access, for Embase, Scopus and Web of Science. Exact strings sit in search-appendix-pending.md, marked string prepared, run pending access. The review will report only databases actually run, each with a date and a count. A source blocked or rate limited at run time is logged as blocked, never as searched.
Citation follow up: reference lists of included studies and of existing reviews of language model hallucination, and forward citation chasing on the earliest systematic generation experiments identified at screening.
The search has blocks for model terms, citation and reference terms, and fabrication and accuracy terms, plus a second block set for audits of the published literature.

## 17. URL to search strategy
To be added when the review repository is posted. Search strings also reproduced in full in the search log file held with the protocol.

## 18. Condition or domain being studied
Accuracy of citations generated by large language models for biomedical and clinical topics, and research integrity in scholarly referencing. The domain covers generation experiments, where a model is asked for references and each reference is verified, and, as a separate stratum, audits that estimate fabricated citations in the published literature.

## 19. Participants and population
No human participants in the usual sense. The units are studies and, within studies, model arms and generated references. Include: primary studies that prompted one or more large language models to generate references on a defined biomedical, clinical or health topic, reported the number generated, and verified each reference against a named external source. Population of topics: biomedical, clinical and health topics as defined by each study, any country, any language of report at search.

## 20. Intervention, exposure
Exposure: generation of references or citations by a large language model in response to a prompt on a biomedical topic. Model name and version, generation date and settings, prompt, and any retrieval, browsing, search tool or reference database access are extracted per arm. Arms with retrieval and arms without retrieval are both eligible. Retrieval condition is a subgroup variable.

## 21. Comparator and control
No comparator in the intervention sense. Comparisons in the synthesis are between proportions: between model families and generations, between retrieval and no retrieval arms, between specialty or topic groups, between established and emerging topics, between list lengths (10 or fewer references requested against more than 10), between peer reviewed and preprint studies, and between model years (2023 or earlier, 2024, 2025 onward). Audit stratum studies have no comparator and are reported apart.

## 22. Types of study to be included
Generation experiments, main synthesis: primary studies meeting field 19, in peer reviewed journal articles, preprints with original data, or conference papers with a full methods report.
Audit stratum, never pooled with generation experiments: large scale audits of the published literature, journal corpora or preprint servers that state corpus, detection method and denominator in papers or published references.
Exclude: editorials, commentaries and reviews with no original experiment or audit; single reference anecdotes with no denominator; studies of hallucination with no citation outcome; studies verified only against the model own output; reports with no count and no extractable denominator; vendor marketing material.

## 23. Context
Any setting in which a large language model is asked to generate biomedical references: research writing support, manuscript drafting tests, benchmark evaluations, and journal or institutional integrity checks that run a defined generation experiment. Audit stratum context: published journal literature and preprint servers, any biomedical field covered by the audit corpus.

## 24. Main outcomes
Denominator: references generated and verified, per study arm.
1. Completely fabricated: proportion of generated references for which no matching publication exists.
2. Major inaccuracy: proportion with any major inaccuracy, including completely fabricated, where major means the error prevents retrieval or misattributes the source, including a fabricated element that forms part of the identity of the source.
3. Fully accurate: proportion accurate on all fields checked, strict definition in the main analysis. A lenient definition, where the source is real, correctly credited and retrievable despite a minor field error, is used only in a sensitivity analysis.
Definitions are fixed in the protocol and extraction form before screening ends. Study definitions are extracted as printed, mapped only where the mapping is exact, with the mapping logged per study, and otherwise kept in narrative synthesis.

## 25. Additional outcomes
Minor error rates by field: authors, title, journal or source, year, volume or pages, DOI. Bad DOI: proportion of references carrying a DOI where the DOI does not resolve, or resolves to a different paper. Error by position in the list, early against late references, per study split as printed. Verification method and verifier agreement where reported. Audit stratum outcomes, reported apart: proportion of published papers containing at least one fabricated reference, and proportion of published references fabricated, where the audit reports them.

## 26. Data extraction, selection and coding
Two stage screening, title and abstract then full text, against the criteria in fields 19 to 23. At full text each study is assigned to generation experiments, audit stratum, or exclude with one reason. Piloted extraction form covers study identity, country, specialty, established against emerging call with basis, models and versions, generation date and settings, retrieval condition, prompt, references requested and generated, verification source and method, verifier independence and blinding, outcome definitions as printed, counts with denominators per arm, funding and conflicts. Audit studies use a separate section of the same form.
Automation, LLM team: screening is done by two independent language model screener passes, A strict and B sensitive, with separate prompts and no sight of each other calls until both are done. An adjudicator pass settles disagreements with a logged reason, and items it cannot settle go to the human author. Extraction is done by two independent extractor passes and compared field by field, with each mismatch logged and settled against the source. The author checks every number that enters a pool. Tool, version, dates and prompts are logged in the team log. Inter-screener agreement, Cohen kappa, disagreement types, adjudication outcomes and extraction discrepancy rate are reported in the review. Full detail sits in the protocol, in the section titled LLM team in place of a human research team.

## 27. Risk of bias assessment
Adapted tool pre-specified in rob-forms.md before extraction. No standard tool fits citation generation experiments cleanly, so the tool is reported as adapted at every mention and is never presented as RoB 2 or QUADAS-2. Domains: topic and prompt sampling; prompt and model version reporting; generation settings; verification source; verifier independence; duplicate or blinded verification; handling of partial matches; selective reporting. Each judgement is low, some concerns, high, or no information, and needs a support line quoted or referenced from the paper. Two independent assessor passes per study, per arm where a domain varies by arm. Disagreements go to the human author and are counted in the team log.

## 28. Strategy for data synthesis
Random effects meta-analysis of proportions. Logit transformation as primary. Tau squared, I squared and, at ten or more studies or arms, a prediction interval reported for each pool. Software: R with meta or metafor as primary. Where R is unavailable, Python with an equivalent random effects model for proportions will be used, and the finished review will state which software ran the final numbers, with package and version.
Unit of analysis: the model arm, with study as a clustering level where the data allow. A per study pool, where each study contributes one combined proportion, is shown as a sensitivity check for every critical outcome pool. Completely fabricated, major inaccuracy and fully accurate are pooled apart and never added together. Minor errors, bad DOI rates and position results are pooled only where definitions and denominators match. Where definitions do not map, SWiM style structured narrative synthesis is used. Audit stratum studies are never pooled with generation experiments. Audits are pooled with each other only if at least three share a denominator type, corpus type and detection method, and any such pool is labelled as an audit pool at every mention.

## 29. Analysis of subgroups or subsets
Subgroups set in advance, and no others presented as pre-specified: model family and generation; retrieval, browsing or RAG against no retrieval; specialty or topic type; established against emerging topic; references requested, 10 or fewer against more than 10; peer reviewed against preprint; model year, 2023 or earlier against 2024 against 2025 onward. Subgroup claims rest on a test for interaction or an equivalent between group test.
Sensitivity analyses set in advance: fully accurate definition strict against lenient; studies at low or moderate overall risk of bias only, using the wording set in rob-forms.md; leave one model family out in turn; preprints removed; per study pool; mapping sensitivity with studies whose definitions mapped with any doubt removed.

## 30. Type and method of review
Systematic review with meta-analysis of proportions. Methods follow the Cochrane Handbook version 6.5 in spirit and structure. Reporting follows PRISMA 2020, with the search reported to PRISMA-S. Not a Cochrane review. Narrative synthesis used only where pooling is not sound or definitions do not map.

## 31. Language
English. Searches have no language limit. Non-English reports are translated where a checked translation is possible and otherwise listed as awaiting classification.

## 32. Country
United States (author base). Studies from any country are eligible.

## 33. Other registration details
An OSF registration record is prepared in parallel with the same protocol text, so a dated public record exists even if PROSPERO review takes time or PROSPERO judges the question out of scope for its register. The finished review will cite whichever numbers have actually been issued by publication, with issue dates, and will state plainly if a number is still pending. No registration number is claimed in advance. This is Review 2 in the author series. Review 1 covered ambient AI scribes for clinical documentation. The two reviews cover different questions, different study types and different denominators.

## 34. Reference or bibliographic details for protocol publications
Protocol file held with the review, version 1.0, 22 October 2026, author Raphael Malikian, ORCID 0009-0008-4326-4205. Preprint of the protocol to be posted free of charge with the review repository.

## 35. Dissemination plans
Preprint free of charge on Zenodo with a DOI and on medRxiv if the framing is accepted. Public GitHub repository with PDF first README, manuscript, protocol, search log, screening and extraction files, risk of bias assessments, analysis code and data, CC BY 4.0. Journal submission by a no fee subscription route only, to a journal that has not received Review 1 in this series. Conference abstract submission to a fitting venue, with paid presenting opportunities considered first. No funder reporting duties, since there is no funder.

## 36. Keywords
Large language models; citation fabrication; fabricated references; hallucination; reference accuracy; biomedical literature; research integrity; meta-analysis of proportions.

## 37. Details of any existing review of the same topic by the same authors
None on this question. Review 1 in the series, by the same author, covers ambient AI scribes and shares no studies, outcomes or denominators with this review.

## 38. Current review status
Protocol stage. Protocol version 1.0 dated 22 October 2026. Registration prepared for PROSPERO and OSF, no number issued at preparation. Screening, extraction, risk of bias assessment and synthesis stages will be reported with their actual start dates in the finished review.

## Author note for the form, not a PROSPERO field
Evidence synthesis and research integrity discussion only. This review makes no clinical recommendation and no medication recommendation. The author writes as a healthcare founder and operator and clinical AI builder, and as an independent researcher. Subtle AI assistance note, factual, will sit in the manuscript declarations area, per the author academic disclosure rule: a team of language model roles carried out team tasks under the separations described in field 11 and in the protocol, and the named human author is accountable for every judgement.
