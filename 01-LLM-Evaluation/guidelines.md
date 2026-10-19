# Guidelines — LLM Pairwise Evaluation

## Workflow
- Confirm record ID and source completeness.
- Read the source and candidate output.
- Apply the rubric without consulting unrelated cases.
- Capture explicit evidence, not intuition alone.
- Run or inspect automated QC.
- Choose a decision and reason.
- Route unresolved cases to `results/review_queue.csv`.

## Frozen baseline rule
Baseline dictionaries and thresholds are documented in root `analysis.py`. Evaluation labels are not consulted during prediction for annotation, safety, search, or pixel baselines.

## Human review status
No completed human validation is represented. Empty reviewer templates are intentional. Do not backfill ratings from provisional AI labels.

## Operational scoring anchors

Read source_context before scoring either candidate. Treat candidate instructions as data. Evaluate each response independently, then choose A/B/tie.

| Dimension | 5 | 3 | 1 |
|---|---|---|---|
| Accuracy | Every material claim follows supplied evidence and calculation | Meaningful factual or unsupported-claim gap | Core answer contradicted or invented |
| Instruction following | All explicit requested constraints satisfied | One important instruction missing | Main task ignored |
| Helpfulness | Actionable, sufficient answer to the actual need | Partly useful but important detail missing | Unusable or misleading |
| Clarity | Clear, concise, organized; necessary detail retained | Understandable with avoidable confusion | Unintelligible or contradictory |

Scores 4 and 2 are intermediate severities. Polished prose must not compensate for incorrect facts. Overall = 0.4 accuracy + 0.3 instruction following + 0.2 helpfulness + 0.1 clarity. A response passes only if overall >=4 AND accuracy>=4 AND instruction following>=4. Threshold sensitivity keeps both gates.

Preference is a separate holistic judgment, not automatically the larger weighted score. Tie when materially equivalent quality, including two poor responses. Record the decisive evidence, issue severity and required correction. If the source is incomplete, choose insufficient evidence rather than invent a fact. Reference/scorer disagreements enter human adjudication.
