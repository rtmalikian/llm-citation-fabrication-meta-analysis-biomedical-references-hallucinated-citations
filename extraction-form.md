# Data extraction form, piloted version 1

For use by extractor A and extractor B, working apart, on every study that passes full text screening. One form per study. Both sheets are compared field by field. Each mismatch is logged in the team log with the field name, settled against the source document, and counted in the extraction discrepancy rate. The human author checks every number that will enter a pool.

Pilot note: the form was drafted from protocol section 4 outcomes and section 8 bias concerns before screening ends. It gets its first live test on the first five included studies. Any field change after that test is logged here with a date, and forms already filled are rechecked on the changed field.

Stratum rule, read first: a study is extracted as a generation experiment, as an audit, or as both with a split. Generation experiment studies fill sections A to I. Audit studies fill sections A and J, and leave sections B to I outcome blocks empty with audit stratum written in field 39. A study with both parts fills all sections, with the generation part and the audit part recorded as separate units and the split described in field 39.

## Review definitions, fixed

Copy of protocol section 4. These definitions govern mapping. They do not replace the study printed definitions, which are extracted in section G.

- Completely fabricated: no matching publication exists. Verification against the named source finds no publication that matches on title and source identity in a way that could count as the same work. A reference that takes a real title and attaches wrong authors, or takes real authors and attaches a title that does not exist, counts here if no single matching publication exists.
- Major inaccuracy: any major inaccuracy, including completely fabricated. An error that prevents retrieval of the intended source, or that misattributes the source. It includes a completely fabricated reference; a fabricated element that forms part of the identity of the source, such as a fabricated title, fabricated first author, or fabricated DOI; a journal, year, volume or page set that points to a different publication or to no publication; and a real publication cited for a claim or topic it does not cover where the study counts that as misattribution. Minor errors that leave the source findable and correctly credited do not count here.
- Fully accurate, strict: accurate on all fields checked by the study. Authors, title, journal or source, year, and volume, pages and DOI where the study checked them must all be correct. Any error in a checked field, major or minor, removes the reference from this count.
- Fully accurate, lenient (sensitivity only): the source is real, correctly credited, and retrievable despite a minor field error.
- Minor error: an error in one field where the source remains the same publication, remains retrievable from the rest of the reference, and remains correctly credited in the main.
- Bad DOI: a DOI that does not resolve, or a DOI that resolves to a different paper. Denominator is references that carry a DOI.

## Mapping rules

These rules govern section G, field 36, and every pool entry. They apply in this order.

1. Extract as printed. Every count is first recorded exactly as the study prints it, under the study label for that count, with its printed denominator.
2. Map only if exact. A printed count maps to a review outcome only if the study printed definition covers the same cases as the review definition, no more and no fewer, in substance. Wording may differ. Coverage may not.
3. Where a study definition is broader than the review definition (for example, its inaccurate count includes minor errors), the count maps to no review outcome. Record mapping as not exact, give the difference in one sentence, and keep the count for narrative synthesis under its printed label.
4. Where a study definition is narrower (for example, its fabricated count requires failure on two sources where the review requires the named source the study used), the count maps to no review outcome on the same rule. Near enough is not exact.
5. Where a study prints separate counts that sum, without overlap, to a review definition exactly (for example, fabricated plus real but unretrievable, where together they cover major inaccuracy as defined and nothing else), the summed mapping is allowed. Record mapping as exact by sum, list the parts, and show the addition. The human author checks every exact by sum mapping before it enters a pool.
6. Where a study reports a percentage with a denominator and no count, derive the count only if the percentage and denominator give a whole number without rounding doubt. Record the count as derived, show the working, and flag it. A derived count with rounding doubt is recorded as not extractable, with the percentage kept for narrative use.
7. Fully accurate mapping needs the checked fields. A printed accurate count maps to strict only if the study checked all fields its accurate label claims and counted any error in a checked field against accuracy. It maps to lenient only if the study allowed minor field errors inside its accurate count while requiring a real, correctly credited, retrievable source. If the study does not state which errors its accurate count allows, mapping is unclear, and the count enters neither pool until the human author settles it from the full text.
8. Every mapping call (exact, exact by sum, not exact, unclear) is logged per outcome per arm in field 36, with a one sentence reason. The statistician pools only exact and exact by sum mappings in the main analysis.

## A. Study identity
1. Record ID from the screening file.
2. First author, year, journal or source.
3. DOI, PMID, or preprint ID, as applicable.
4. Report type: peer reviewed journal article, preprint, conference paper with full methods report.
5. Country of the study team, as stated. If authors span countries, list each.
6. Registration, protocol, or preprint link for this study itself, if any, with registry or server named.
7. Stratum: generation experiment, audit, or both with split. Set at full text screening and confirmed here.

## B. Topic
8. Topic or topics as printed, word for word where the study lists them.
9. Specialty or topic type, review grouping: primary care and general medicine; medical specialty (name it); surgical specialty (name it); psychiatry and mental health; paediatrics; radiology and imaging; pathology and laboratory medicine; public health and epidemiology; pharmacology; nursing and allied health; dentistry; mixed biomedical; other biomedical (name it); mixed with non-biomedical (name the split if given).
10. Established against emerging call, per protocol section 3.6: established, emerging, unclear. Basis in one sentence, tied to what the study states or to the topic and its literature dates as given in the paper. If the study labels its own topics, record the study label here as printed, beside the review call.
11. Number of distinct topics or prompts topics: count as printed. If topics were sampled from a larger set, state the larger set and the sampling method as printed.

## C. Models and generation
One copy of fields 12 to 20 per arm. An arm is one model under one retrieval condition. Number arms A1, A2, and so on, and use the same arm numbers in sections G and H.
12. Model name and version as printed, word for word (for example, the full model string the study gives). If no version is stated, write not stated. Do not supply a version from outside the paper.
13. Model family, review grouping set from field 12: GPT family; Claude family; Gemini family; Llama family; Mistral family; other named family (name it); mixed models in one arm; unclear.
14. Model year: release year of the version in field 12, with source: as stated in the study, or vendor release record (name it), or unclear. This field feeds the model year subgroup and its source is always stated.
15. Generation date or period as printed: exact date, month and year, period, or not reported.
16. Generation settings as printed: temperature, system instructions, browsing or plugins state as set by the study, number of outputs generated per prompt, retries allowed, and whether the study selected among outputs or used the first output. Each item recorded as printed, not reported, or unclear. Write the settings as a list in the study terms.
17. Retrieval condition for this arm: none; browsing or live search; retrieval augmented generation over a named corpus (name it); reference database or citation tool access (name it); document set supplied in the prompt (describe it briefly); mixed; unclear. Record the tool or corpus name as printed.
18. Prompt as printed: full verbatim prompt where the study gives one, with page or supplement reference. Where the study gives no full prompt, summarise the prompt task in the study terms and write no verbatim prompt given. Record: number of references requested per prompt, whether claims or a passage were supplied for the references to support, and language of the prompt if stated.
19. References requested: total across the arm, as printed, and per prompt or per list where given. List length group for analysis: 10 or fewer requested per prompt or list, more than 10, varies within arm (give range), unclear.
20. References generated: total returned for this arm, as printed. References verified: total checked, as printed. If generated and verified differ, record both and copy the study reason for the gap, or write no reason given.

## D. Verification
21. Verification source or sources as printed: PubMed, Crossref, Google Scholar, publisher record, journal record, library catalogue, Scopus, Web of Science, other (name it). List each source the study used. If different references were checked on different sources, state the split.
22. Verification method as printed: what counted as a match, step by step in the study terms. Include: fields compared, whether DOI resolution was tested, whether the verifier opened the source record or relied on a search result, and the rule for a reference with no exact hit (for example, how many search attempts before calling it fabricated), each as printed or not reported.
23. Verifier: who or what verified the references (study authors, independent raters, librarians, an automated checker, vendor staff, other, not reported). Number of verifiers.
24. Verifier independence: whether any verifier took part in generating the references, in the study words where given. Review code: independent, partly involved, same people, automated only, not reported.
25. Blinding: whether verifiers knew which model produced each reference. Review code: blinded to model, not blinded, partly blinded (state how), not reported. Copy any study sentence on blinding into the notes if the code is in doubt.
26. Duplicate verification: whether each reference was checked by two or more verifiers, or once. How disagreements between verifiers were settled, as printed. Agreement statistic between verifiers, as printed, with its type (percent agreement, Cohen kappa, other).

## E. Definitions as printed
27. Definition of fabricated or equivalent study label, word for word, with page reference. If the study gives no definition, write no definition given.
28. Definition of inaccurate, incorrect, erroneous, or equivalent study labels, word for word, one line per label, with page references. Include any severity split the study uses (for example, major and minor) in its own terms.
29. Definition of accurate, correct, or equivalent study label, word for word, with page reference. Include the fields the study says it checked for accuracy, listed as printed.
30. Fields checked per reference, as printed: authors, title, journal or source, year, volume, pages, DOI, other (name it). List checked and not checked separately where the study allows it.
31. Partial match rule as printed: how the study handled near matches, changed titles, preprints that later appeared in journals, conference versions, and references mixing real and fabricated elements. As printed, or not reported, per case where the study splits them.

## F. Counts as printed
One copy of fields 32 to 35 per arm, matching the arm numbers in section C.
32. Counts under study labels: for each label in section E, the count and its denominator, exactly as printed, with page or table reference. One line per label. Do not rename a study label here.
33. Completely fabricated count as printed, if the study prints one apart from a broader label, with denominator and page or table. Otherwise write covered by field 32 only.
34. Fully accurate count as printed, with denominator and page or table. Otherwise write covered by field 32 only.
35. Field level and DOI counts as printed: errors by field (authors, title, journal or source, year, volume or pages, DOI), each count with denominator; DOI carrying references count; DOI does not resolve count; DOI resolves to a different paper count. Each as printed, or not reported, per item.

## G. Mapped counts for synthesis
One copy of fields 36 to 38 per arm. Filled only under the mapping rules at the head of this form.
36. Mapping log: per review outcome (completely fabricated, major inaccuracy, fully accurate strict, fully accurate lenient), one line each: mapping call (exact, exact by sum with parts listed, not exact, unclear), the printed label or labels it rests on, and a one sentence reason.
37. Mapped counts: per review outcome with mapping exact or exact by sum, the numerator and denominator that will enter the dataset, with the field 32 line each rests on. Leave blank for outcomes mapped not exact or unclear. Blank means narrative only. It never means zero.
38. Position data: error counts or rates by position in the list, as printed, with the study split stated (for example, first five against rest). Where per position counts allow a first half against second half split, record that derived split here, marked derived, with the working shown. Otherwise write position not reported.

## H. Funding, conflicts, and reporting completeness
39. Extractor notes on stratum and splits: audit stratum written here for audit studies, split description for split studies, and anything that decides which sections apply.
40. Funding source in words, as stated.
41. Vendor role: whether any model vendor funded the study, supplied access, took part in design, verification, analysis, or writing, as stated per role. Write none stated where the paper is silent, none where the paper states none.
42. Author conflicts as stated in the paper, in short form, with page reference.
43. Reporting completeness, for the selective reporting domain: models run against models reported with counts; topics run against topics reported; prompts run against prompts reported. Each as printed, or not reported. Note any arm, topic or prompt mentioned in methods with no results count anywhere in the paper, by name.

## I. Extractor notes
44. Anything in the paper that does not fit a field above and bears on eligibility, bias, definitions, or an outcome.
45. Contradictions and arithmetic problems: text against table differences, denominators that do not sum, percentages that do not match counts, each with page references. Flag only. Do not correct.
46. Data the paper should have and does not give, by field number, for the author contact list.
47. Fields left as not reported or unclear on this form, listed by number. This list is part of the extraction record.

## J. Audit stratum section
Fill for audit studies instead of sections B to I outcome blocks. Section A still applies. One form per audit. Where an audit reports several corpora or years apart, copy fields 51 to 55 per corpus or period.
48. Corpus as printed: journals, publishers, preprint servers, or databases covered, with the sampling frame in the study terms.
49. Corpus years: period covered, as printed, and how papers entered the corpus (all papers, random sample, flagged sample, other).
50. Detection method as printed: how the audit decided a reference or paper was fabricated (hand verification, automated checks against named sources, a classifier, a score threshold, other). Name each source or tool.
51. Validation of the detection method: hand checked subsample size, agreement or accuracy figures as printed, or not reported.
52. Denominator in papers: papers in the corpus or sample, as printed. Papers containing at least one fabricated reference: count and proportion as printed, with page or table.
53. Denominator in published references: references checked, as printed. Fabricated published references: count and proportion as printed, with page or table.
54. Breakdowns as printed: by year, by field, by journal, or by paper type, each count with denominator where the audit gives one. One line per breakdown row.
55. Audit definitions as printed: definition of fabricated reference or fabricated paper used by the audit, word for word, with page reference. Mapping to review outcomes is never attempted for audit studies. This field exists so the audit table can quote the audit on its own terms.
56. Audit funding and conflicts: funding source in words, vendor or tool maker role as stated, author conflicts as stated.
57. Audit extractor notes: limits the audit itself states, corpus gaps, and anything that bears on how far the audit figures can be read, in the audit terms where given.
