# Risk of bias summary

Adapted citation accuracy tool from rob-forms.md, applied by two assessors working apart to all 25 generation studies, then adjudicated by taking the more cautious judgement per domain (see llm-team-log.md). This tool is adapted for citation generation experiments. It is not RoB 2 and not QUADAS-2, and it is never named as either in this review.

## Adjudicated overall judgements

- Low: 0 studies
- Some concerns: 10 studies (Adiguzel 2026, Civelekler 2026, Gunes 2026, Kutluay 2026, Metze 2024, Mugaanyi 2024, Seifi 2026, Shi 2026, Tas 2026, UcarGundogar 2026)
- High: 15 studies

## Where the risk sits

Verification conduct was the weakest part of this literature. Domain 6 (duplicate or blinded verification) and domain 5 (verifier independence) carried the most no information judgements: many studies never say who checked the references, whether the checker knew which model produced them, or whether anyone checked the checking. Nieves-Lopez 2026 names no verification source at all. Dhaimade 2026 and Singh 2026 used a single evaluator with no inter-rater check.

Reporting of the generation setup was the second weakness. Several 2023 and 2024 studies used unversioned models with no generation date (Aljamaan 2024, Hasnain 2025, Sawamura 2024), so their results cannot be tied to a model that still exists in that form.

Two studies had a single domain that drove a high judgement on its own. Chelli 2024 retained a prompt version because it produced the largest number of results (domain 1). Bernstein 2026 verified against PubMed only and counted studies not indexed in PubMed as hallucinated (domain 4), which can push its fabricated count up for references to real work outside PubMed.

The strongest study on this tool was Seifi 2026: two blinded experts, kappa 0.91, browsing disabled on purpose, generation date printed. It still took some concerns overall, on topic sampling (ten topics chosen by one expert, a limit the authors state themselves). Gunes 2026 was split between the assessors (low from assessor 2, some concerns from assessor 1) and adjudicates to some concerns under the cautious rule.

Full per domain judgements, both assessors' originals and support lines: rob-assessments.csv, stage4/rob-assessor1.csv, stage4/rob-assessor2.csv.

## Robustness pass, 23 October 2026: adjudication by reading (supersedes the cautious rule above)

The first version adjudicated every disagreement by taking the more cautious judgement. The robustness pass replaced that rule: an adjudicator re-read the paper text and both assessors' rationales for every one of the 56 domain disagreements in the original study set, and for all disagreements in the 39 studies added by the pass, and settled each one on the printed evidence. The "more cautious wins" rule was not applied anywhere in the corrected version.

### Original 24 studies (after the Jedrzejczak 2024 / Pastucha 2026 study merge)
- 61 domain level disagreements settled by reading: the adjudicator matched assessor 1 on 34, assessor 2 on 27, neither on 0.
- Overall judgements, corrected: high 12, some concerns 12, low 0.
- Two studies changed overall category against the first version: Athaluri 2023 (high to some concerns; domains 5 and 6 rested on a misread of the form: the paper names a fourth author as reviewer and reports a kappa) and Sawamura 2024 (high to some concerns; domains 1 and 8 rested on fields the assessor had not read closely: the search date was printed and there was no selective reporting). The other first version studies kept their categories. Gunes 2026, which the cautious rule had pushed to some concerns from a low and some concerns split, stays at some concerns on the reading as well.
- Adjudicated sheet: robustness/rob-assessments-v2.csv; per domain support lines and the settlement of every disagreement: robustness/rob-adjudication-log.md.

### Studies added by the robustness pass (39)
- Assessed by two assessors working apart, then adjudicated by reading (79 domain level disagreements across the 37 re-adjudication studies, plus 18 across the 2 citation chasing studies, settled on the printed evidence; support lines in robustness/ft2/rob-new-adjudication-log.md and robustness/search/rob-chasing-adjudication-log.md).
- Overall judgements after adjudication, counted from the adjudicated sheets: combined with the original set below.

### All 63 generation studies, corrected version
- High: 30 studies
- Some concerns: 33 studies
- Low: 0 studies

Verification conduct remains the weakest part of this literature at the larger scale: domains 5 and 6 (verifier independence; duplicate or blinded verification) carry the most high and no information judgements in the new studies as well, and no study in either set reached low risk overall.
