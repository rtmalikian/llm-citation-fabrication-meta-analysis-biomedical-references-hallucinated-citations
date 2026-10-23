# Risk of bias forms: adapted tool for citation accuracy studies

Status: pre-specified before extraction begins, as protocol section 8 requires. This tool is adapted for citation generation experiments and for audits of the published literature. It is reported as adapted at every mention, in the manuscript, in tables, and in any summary. It is never presented as RoB 2. It is never presented as QUADAS-2. Judgements from this tool are never merged with judgements from RoB 2 or QUADAS-2.

Why an adapted tool: RoB 2 covers randomised trials of interventions. QUADAS-2 covers diagnostic accuracy studies with an index test and a reference standard in patients. A citation generation experiment assigns prompts to models and checks generated references against bibliographic sources. The bias risks sit in topic choice, prompt and version reporting, generation settings, verification, and selective reporting of arms. No standard tool covers that set. This tool covers it, with domains fixed here, in advance.

Use: two independent assessor passes per study, working apart. One form per study, with per arm judgements added where a domain varies by arm. Agreements stand. A disagreement, with domain named, goes to the human author, whose settlement and reason are recorded on the form. Counts of disagreements go to the team log.

Judgement scale for every domain: low, some concerns, high, no information. No information is used where the paper gives too little to judge. It is a judgement in its own right. It is not merged with some concerns at extraction. Any merging for a sensitivity analysis follows protocol section 9.3 wording and is done at analysis, with the rule stated in the report.

Support rule: each judgement needs a support line on the form. A support line is a short quote from the paper or a page, table, figure, or supplement reference that shows the basis for the judgement. A judgement with no support line does not count and the form is returned to the assessor as incomplete.

Direction note: judge the method, never the result. A high fabrication rate is a finding. It is not evidence of bias. A low fabrication rate is not evidence of sound method.

Study ID. Stratum: generation experiment, audit, or split part named. Arms covered by this form, by arm number from the extraction form. Assessor pass: 1 or 2. Date of assessment.

## Domain 1: Topic and prompt sampling

Question: could the way topics and prompts were chosen have shifted the error rates away from the rates the same models would show on a fair sample of biomedical topics?

Signalling questions:
- 1.1 How many distinct topics were used, and how were they chosen (author choice, random sample from a named frame, a published topic set, topics from real manuscripts, other)?
- 1.2 Does the topic set favour settled, heavily referenced areas where accurate references are easy to produce, or narrow, recent, or sparse areas where fabrication is more likely? In which direction, and how strongly?
- 1.3 How many prompts were run per topic, and were prompts written in advance or adjusted after seeing outputs?
- 1.4 For split topic designs, were established and emerging topics balanced across models, or did models face different topic mixes?

Judgement: low, some concerns, high, no information.
Support line: quote or page reference.
Assessor note: likely direction of any bias (rates understated, rates overstated, direction unclear), in one sentence.

Guide: low needs a stated topic frame or a broad topic set with a selection method that does not favour one difficulty level, and prompts fixed before outputs were seen. High fits a small hand picked topic set with no frame, where the picks lean clearly to one difficulty level, or prompts tuned after outputs were seen with no log of changes. Author chosen topics alone, with the list printed in full, sit at some concerns unless the list plainly leans one way.

## Domain 2: Prompt and model version reporting

Question: is the generation run reported well enough for another team to repeat it and get a comparable set of references?

Signalling questions:
- 2.1 Is the full prompt, or each prompt, printed word for word in the paper or supplement, or is only a task summary given?
- 2.2 Is each model named with its exact version or release string, as the vendor names it, or only with a family name?
- 2.3 Is the generation date or period stated, so silent model updates can be taken into account?
- 2.4 Is the interface stated (chat interface, API, institutional deployment), where the interface changes what the model can do?

Judgement: low, some concerns, high, no information.
Support line: quote or page reference.
Assessor note: name the missing items, by signalling question number.

Guide: low needs full prompts available, exact versions, and a generation date. A missing generation date alone caps the judgement at some concerns, since models change without a name change. Family name only, with no version and no date, is high: the run cannot be repeated or placed in time.

## Domain 3: Generation settings

Question: could generation settings, or handling of outputs, have shifted the error rates in one arm against another or against real use?

Signalling questions:
- 3.1 Are settings that change output reported (temperature or equivalent, system instructions, browsing or plugin state set by the study, other settings the paper names)?
- 3.2 Were settings held the same across arms, or are differences stated and accounted for?
- 3.3 How many outputs were generated per prompt, and which output was verified (first output, a selected output, all outputs)? Was selection based on quality or appearance in any way?
- 3.4 Were retries allowed after a refusal, an empty answer, or an obvious error, and are retried prompts counted and reported?

Judgement: low, some concerns, high, no information.
Support line: quote or page reference.
Assessor note: name any arm that ran under different settings, by arm number.

Guide: low needs settings reported, held fixed across arms or differences stated, the first or all outputs verified with no quality based selection, and a retry rule stated. Selecting the best looking output for verification is high. Settings unreported across the board is no information where the paper is silent in full, some concerns where part of the set is reported.

## Domain 4: Verification source

Question: was each reference checked against a source that can settle whether the reference exists and whether its fields are right?

Signalling questions:
- 4.1 Is the verification source named (PubMed, Crossref, Google Scholar, publisher record, journal record, library catalogue, other), per arm where sources differ?
- 4.2 Does the source cover the fields the outcomes rest on (authors, title, journal, year, volume, pages, DOI), or does the check cover only part of the reference while outcomes claim the whole?
- 4.3 Was DOI resolution tested directly where a DOI outcome is reported, or inferred from search results?
- 4.4 Could the source miss real references in a patterned way (for example, a single database with thin coverage of the journals, languages, or years in the topic set), and did the study check a second source for apparent fabrications?

Judgement: low, some concerns, high, no information.
Support line: quote or page reference.
Assessor note: name any outcome whose fields the stated check cannot settle.

Guide: low needs a named source fit for the topic set, a check that covers every field the outcomes rest on, and a second look on a second source, or a stated rule with the same effect, before a reference is called fabricated. Calling references fabricated after a single search on a single source with known coverage gaps is high. Verification against the model own output fails eligibility and is recorded here as high with that reason, for the log, even though such studies are excluded.

## Domain 5: Verifier independence

Question: were the people or tools that verified the references separate from the step that generated them, and free of an interest in the result?

Signalling questions:
- 5.1 Who verified the references, and did any verifier write the prompts, run the generation, or select the outputs?
- 5.2 Did vendor staff, or staff funded by a vendor whose model is tested, take part in verification, design, or analysis?
- 5.3 Where an automated checker did the verification, is the checker independent of the models under test (a checker built on a tested model, checking that model outputs, is not independent)?

Judgement: low, some concerns, high, no information.
Support line: quote or page reference.
Assessor note: name the overlap, by role, where one exists.

Guide: low needs verifiers with no part in generation or output selection, and no vendor role in verification for a vendor model under test. The same small team doing every step, with no separation stated, is some concerns. Vendor staff verifying their own model references, with counts entering the outcomes, is high.

## Domain 6: Duplicate or blinded verification

Question: was verification checked itself, by a second check or by blinding, well enough that one verifier errors or expectations cannot set the rates alone?

Signalling questions:
- 6.1 Was each reference, or a stated random sample of references, verified by two or more verifiers working apart?
- 6.2 Did verifiers know which model produced each reference while they checked it?
- 6.3 How were disagreements between verifiers settled (third verifier, discussion, rule based), and is an agreement figure reported?
- 6.4 Where verification was single and unblinded, does the study give a reason, and is the check mechanical enough (for example, DOI resolution plus exact title match on a named source) that judgement plays little part?

Judgement: low, some concerns, high, no information.
Support line: quote or page reference.
Assessor note: state sample size for any double checked sample, as printed.

Guide: low needs duplicate verification of all references or of a stated random sample with agreement reported, or blinded verification with model identity hidden, or both. Single unblinded verification where match calls need judgement, with no agreement check at all, is high. Single verification of a mechanical check under 6.4, with the rule printed, can sit at some concerns.

## Domain 7: Handling of partial matches

Question: were the hard cases, references that partly match a real publication, handled under rules set in a way that does not push counts toward fabrication or toward accuracy as the authors prefer?

Signalling questions:
- 7.1 Does the study state its rule for a near match (real title with wrong authors, real authors with a wrong title, right paper with wrong year or journal) before the results, in methods or in a registered plan, or does the rule appear only beside the results?
- 7.2 How were preprints that later appeared in journals, conference versions, and changed titles handled, and is the handling the same across arms?
- 7.3 Do the study rules for partial matches match the review definitions in substance, diverge from them, or stay unstated? Record the answer here in one sentence. The mapping itself lives on the extraction form. This question covers whether a rule exists and was applied evenly.
- 7.4 Are counts given for partial match cases apart from clean fabricated and clean accurate counts, so a reader can re-cut the totals under a different rule?

Judgement: low, some concerns, high, no information.
Support line: quote or page reference.
Assessor note: state where partial cases went in the printed counts (fabricated, inaccurate, accurate, apart), as printed.

Guide: low needs a stated rule, applied evenly across arms, with partial case counts available apart. No rule stated and partial cases folded silently into fabricated or accurate counts is high, since the fold direction moves the headline rates. A stated rule that diverges from the review definitions is not high on that ground alone. Divergence is a mapping matter. It is judged here only if the rule was applied unevenly or set after results were seen.

## Domain 8: Selective reporting

Question: does the report give counts for every model, topic and prompt the study ran, or does reporting pick the arms and cuts that suit a story?

Signalling questions:
- 8.1 Are all models named in methods reported with outcome counts, or are some models described and then dropped from results without a reason?
- 8.2 Are all topics and prompts named in methods reported, or only a subset, and is the subset choice explained before results?
- 8.3 Is there a registration, protocol, preprint, or supplement to check methods against results? What does the check show?
- 8.4 Are thresholds or category cuts (for example, what counts as major) reported as set in advance, or do cuts appear that favour one model or one claim, with no advance source?

Judgement: low, some concerns, high, no information.
Support line: quote or page reference. Where the support is an absence (a model in methods with no counts in results), cite the methods page and the results pages checked.
Assessor note: list each unreported arm, topic, or prompt by name.

Guide: low needs every arm and topic in methods carried into results with counts, or a stated reason for each gap that predates results. A model dropped from results with no reason is high where its methods presence is clear. No registration or preprint to check against, in a field where registration is rare, is some concerns at most on 8.3 alone, and no information on this domain needs more than a missing check source.

## Overall judgement

Set the overall judgement from the eight domains under this rule, and record it with the deciding domains named:
- Low overall: every domain low, with at most one domain at some concerns where that domain cannot move the headline rates (record why it cannot).
- Some concerns overall: any domain at some concerns, and no domain at high, or one domain at no information where the remaining domains cover the main risks.
- High overall: any domain at high, or three or more domains at some concerns or no information in combination where together they leave the verification or the arm set unchecked.
The rule is applied as written. An assessor who thinks the rule gives the wrong answer for a study records the rule based judgement, then adds a note naming the domain the rule mishandles, for the human author. The note does not change the recorded judgement until the author settles it.
Overall judgement: low, some concerns, high.
Deciding domains: list by number.
Support summary: one sentence, tied to the deciding domains.

## Per arm addition

Where any domain differs by arm (common for domains 3 and 4, where retrieval arms run under different settings or are checked on different sources), copy the domain block for that arm, head it with the arm number, and judge it apart. The overall judgement for the study then rests on the worst arm that enters a pool, and the form states which arm set it.

## Audit stratum notes

For audits of the published literature, use the same eight domains and the same support rule, with these readings substituted and recorded on the form:
- Domain 1 covers corpus sampling. Topics stand in for journals, fields, years, and paper types. The question is whether the corpus, or the sample drawn from it, favours parts of the literature where fabricated references are easier or harder to plant or to detect.
- Domain 2 covers reporting of the detection method and its version, plus the corpus extraction date, in place of prompt and model version. An unnamed or unversioned classifier, with no extraction date, is judged as a generation run with no version and no date would be.
- Domain 3 covers detection settings: thresholds, score cuts, and any selection among flagged papers before hand checking.
- Domains 4 to 6 cover validation. The verification source is the bibliographic source the audit checked against. Verifier independence covers the team that built the detector judging its own flags. Duplicate or blinded verification covers hand checking of flagged and unflagged samples by checkers who did not know the detector call. An audit with no hand checked sample of unflagged papers cannot show its miss rate, and domain 6 reflects that gap.
- Domain 7 covers the audit rule for partial matches in published references, read on the same terms.
- Domain 8 covers reporting of all corpora, years, and fields the audit ran, read on the same terms.
Audit overall judgements use the same rule as above and are reported in the audit table only. They never set the overall judgement of any generation experiment.

## Settlement block

Assessor 1 and Assessor 2 judgements compared by code on: date, script or step, domains in agreement (count of 8), domains in disagreement (list by number).
Human author settlement, per disagreed domain: final judgement, reason in one sentence, date. Author signature line for the form as a whole.
