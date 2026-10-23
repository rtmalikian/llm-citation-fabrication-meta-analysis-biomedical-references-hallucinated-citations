# Appendix: search strings prepared, runs pending access

Every string in this file is marked: string prepared, run pending access. None of these databases was searched at protocol drafting on 22 October 2026, because the environment used for that pass holds no licensed or direct access to them. The review must not state or imply that they were searched. When access exists, run the string as written, add the date and hit count to the search log, and move the string from this file to the log as run. Any change to a string at run time is recorded as an amendment with a date and a reason.

This appendix covers Embase, Scopus and Web of Science only, as protocol section 5 provides. Strings for the sources the review will run directly (PubMed, Europe PMC, OpenAlex, Semantic Scholar, Crossref, arXiv, medRxiv) sit in the search log as run, with dates and hit counts, once each run exists. They do not sit here.

Core concept blocks used in each string below. Block M, models: large language model terms and named model families in general use for this literature. Block C, citations: citation, reference, bibliography and referencing terms. Block F, fabrication and accuracy: fabricated, fictitious, hallucinated, inaccurate, incorrect, accuracy and verification terms. Block A, audits: published literature, corpus and prevalence terms, used in a second combination so audits are found by design. Date limit: no start date limit, to search date. No language limit in any string.

Block M (plain text form): "large language model*" OR LLM OR LLMs OR ChatGPT OR "GPT-4" OR "GPT-3.5" OR GPT OR Claude OR Gemini OR Llama OR Mistral OR "generative AI" OR chatbot*
Block C (plain text form): citation* OR reference* OR bibliograph* OR referencing
Block F (plain text form): fabricat* OR fictitious OR hallucina* OR inaccura* OR incorrect OR accuracy OR verif*
Block A (plain text form): "published literature" OR "published paper*" OR "published article*" OR corpus OR prevalence OR audit

Main combination: M AND C AND F. Audit combination: (M OR "artificial intelligence") AND C AND F AND A, plus a standalone audit pass where Block A terms sit in the title, so audits that never name a model in title or abstract still surface. Each database string below writes these blocks out in full in that database syntax. No string is left as block letters alone.

## Embase, Elsevier, via Embase.com
String prepared, run pending access.

Main string:
('large language model':ti,ab OR 'large language models':ti,ab OR llm:ti,ab OR chatgpt:ti,ab OR 'gpt-4':ti,ab OR 'gpt-3.5':ti,ab OR gpt:ti,ab OR claude:ti,ab OR gemini:ti,ab OR llama:ti,ab OR mistral:ti,ab OR 'generative artificial intelligence':ti,ab OR chatbot:ti,ab OR chatbots:ti,ab) AND (citation:ti,ab OR citations:ti,ab OR reference:ti,ab OR references:ti,ab OR bibliography:ti,ab OR referencing:ti,ab) AND (fabricated:ti,ab OR fabrication:ti,ab OR fictitious:ti,ab OR hallucination:ti,ab OR hallucinations:ti,ab OR hallucinated:ti,ab OR inaccurate:ti,ab OR inaccuracy:ti,ab OR incorrect:ti,ab OR accuracy:ti,ab OR verification:ti,ab OR verified:ti,ab)

Audit string:
(('large language model':ti,ab OR llm:ti,ab OR chatgpt:ti,ab OR 'artificial intelligence':ti,ab) AND (citation:ti,ab OR citations:ti,ab OR reference:ti,ab OR references:ti,ab) AND (fabricated:ti,ab OR fabrication:ti,ab OR fictitious:ti,ab OR hallucination:ti,ab) AND ('published literature':ti,ab OR 'published papers':ti,ab OR corpus:ti,ab OR prevalence:ti,ab OR audit:ti,ab))

Limits at run time: no year limit, no language limit. Emtree checks at run time: check 'large language model', 'artificial intelligence', 'bibliography' and 'medical literature' as Emtree terms, add any confirmed term as an OR line in the relevant block, and record each addition as an amendment with the run date. Record the platform as Embase.com, the full string as run, the run date, and the hit count per string (main and audit kept apart) in the search log.

## Scopus, Elsevier
String prepared, run pending access.

Main string:
TITLE-ABS-KEY ( ( "large language model*" OR llm OR llms OR chatgpt OR "gpt-4" OR "gpt-3.5" OR gpt OR claude OR gemini OR llama OR mistral OR "generative AI" OR chatbot* ) AND ( citation* OR reference* OR bibliograph* OR referencing ) AND ( fabricat* OR fictitious OR hallucina* OR inaccura* OR incorrect OR accuracy OR verif* ) )

Audit string:
TITLE-ABS-KEY ( ( "large language model*" OR llm OR chatgpt OR "artificial intelligence" ) AND ( citation* OR reference* ) AND ( fabricat* OR fictitious OR hallucina* ) AND ( "published literature" OR "published paper*" OR corpus OR prevalence OR audit ) )

Limits at run time: no year limit (no PUBYEAR filter), no language limit. Record the full string as run, the run date, and the hit count per string (main and audit kept apart) in the search log. Note in the log that Scopus coverage of preprint servers is partial, so the Scopus audit string does not replace the preprint server searches in the main source set.

## Web of Science, Core Collection, Clarivate
String prepared, run pending access.

Main string:
TS=(("large language model*" OR LLM OR LLMs OR ChatGPT OR "GPT-4" OR "GPT-3.5" OR GPT OR Claude OR Gemini OR Llama OR Mistral OR "generative AI" OR chatbot*) AND (citation* OR reference* OR bibliograph* OR referencing) AND (fabricat* OR fictitious OR hallucina* OR inaccura* OR incorrect OR accuracy OR verif*))

Audit string:
TS=(("large language model*" OR LLM OR ChatGPT OR "artificial intelligence") AND (citation* OR reference*) AND (fabricat* OR fictitious OR hallucina*) AND ("published literature" OR "published paper*" OR corpus OR prevalence OR audit))

Limits at run time: timespan all years to search date, no language limit. Record editions searched (for example SCI-EXPANDED, SSCI, ESCI) by name in the log, with the full string as run, the run date, and the hit count per string (main and audit kept apart). If an edition is missing from the licence at run time, name the missing edition in the log. Do not report Web of Science as a whole as searched on a partial edition set without that note.
