# Recruiter Guide

## Suggested five-minute review
1. Start with the website’s six evidence cards.
2. Open one metrics JSON and its chart.
3. Inspect the corresponding review queue and three worked cases.
4. Review `analysis.py` for label-independent baseline logic.
5. Check tests and `VALIDATION.md`.
6. Read the limitations before interpreting any metric.

## What is demonstrated
Structured evaluation design, reproducible Python analysis, rubric writing, dataset QA, error queues, basic visual generation/pixel analysis, local documentation, and honest scope control.

## What is not demonstrated
Employment experience, production deployment, advanced machine learning, independently validated personal accuracy, natural-image VLM performance, or policy certification.









<!-- BANKING77:START -->
## Completed real-data experiment: BANKING77

The six original projects remain **synthetic baselines**. An additional real public-data experiment now evaluates a classifier on **10,003 official training queries / 3,080 test queries / 77 intents**. Original annotations are attributed to Casanueva et al. / PolyAI under CC BY 4.0; no personal annotation claim is made.

| Official test result | Value |
|---|---:|
| Multinomial Naive Bayes accuracy | 85.88% (2645/3080) |
| Macro-F1 (77 intents) | 0.8579 |
| Top-3 accuracy | 95.16% |
| Majority baseline accuracy | 1.30% |
| Accuracy after excluding 7 train-overlap test queries | 85.84% |
| Pending automated review queue | 535 cases |

Alpha=0.1 was selected using training-derived validation, not the test set. These are measured **classifier results against published labels**, not the portfolio owner's personal accuracy. All human-review fields remain blank.

- [Experiment and reproduction](02-AI-Data-Annotation/experiments/banking77/README.md)
- [Actual results, limitations and examples](02-AI-Data-Annotation/experiments/banking77/results/REPORT.md)
- [Source hashes and license](02-AI-Data-Annotation/experiments/banking77/source/source-manifest.json)
- [10 experiment tests](02-AI-Data-Annotation/experiments/banking77/tests/test_banking77.py)

```bash
python 02-AI-Data-Annotation/experiments/banking77/run_experiment.py
python -m unittest discover -s 02-AI-Data-Annotation/experiments/banking77/tests -v
```

<!-- BANKING77:END -->

<!-- REAL_EVIDENCE:START -->
# Recruiter evidence map

## Best three things to inspect first
1. **BANKING77 real-data experiment:** 13,083 public queries, 77 intents, 85.88% official-test classifier accuracy; leakage audit, source rights, actual error queue.
2. **HH-RLHF public preference study:** 200 human-preference pairs; why length alone cannot replace rubric-based judgment; transparent ties and sampling bias.
3. **Practical batch-QA case study:** measured query-length cohorts, high-confidence errors and an explicit proposed escalation workflow.

| Role direction | Most relevant evidence | What is not claimed |
|---|---|---|
| AI data annotator / quality analyst | BANKING77 schema, references, confusion matrix, review queue, QA case study | Personal annotation score or client delivery |
| AI / LLM evaluator | HH-RLHF preference study + synthetic rubric and disagreement cases | New production-model comparison or factual gold |
| Malayalam–English evaluator | Synthetic translation rubrics, Unicode checks and native-review forms | Completed linguistic validation |
| Multimodal evaluator | 120 rendered scenes, 240 answer records and RGB-pixel baseline | Natural-photo VLM expertise |
| Safety / content reviewer | Synthetic contextual policy cases and triage failures | Employer-specific policy qualification |
| Search evaluator | Fictional query relevance, NDCG/MRR and intent rationale | Live search-engine evaluation |

All implementation is AI-assisted and original datasets are attributed. Portfolio work is not employment history. Eligibility, language requirements and qualification tests remain role-specific.

## Five-minute review
Read the public-data README → inspect REPORT.md → open one prediction/error row → check the source/label origin → run a test suite. See QUALITY_REVIEW_PLAYBOOK.md for the review workflow.

<!-- REAL_EVIDENCE:END -->
