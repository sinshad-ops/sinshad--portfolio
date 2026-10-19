# Recruiter evidence brief

Six AI-assisted personal projects. No employment, certification, client or independently verified human performance is implied.

## 01-LLM-Evaluation

The separate AI scoring pass agrees with provisional author preferences on 45/50 pairs (90.0%). There are 5 disagreements, all retained in the review queue. The author and scorer use the same Strawberry tier; their underlying model identities are unavailable. This is not independent-human agreement.

The provisional references contain 5 ties; the scorer contains 0 ties. Inspect ties before interpreting aggregate agreement: a forced preference can hide equally useful alternatives. Pass rate across 100 synthetic candidate responses is 50.0% under the documented weighted rubric. It describes this constructed response set, not a real model or the candidate's personal accuracy.

[Source data and reproduction](01-LLM-Evaluation/README.md)

## 02-AI-Data-Annotation

On the 30-record held-out partition, the frozen keyword baseline achieves topic accuracy 76.7%, sentiment accuracy 40.0%, and urgency accuracy 43.3%. This uneven performance shows why annotation requires meaning-level review rather than keyword matching.

Exact entity-span F1 is 0.000 on holdout. The extractor only recognizes limited order/date formats, not PRODUCT or ORG names; unsupported entity classes are not silently excluded from the denominator. The weak result is intentional evidence of baseline scope, not an annotation-quality claim.

29 records enter the structural/ambiguity review queue, and 2 records have span warnings. The simulated second-label exercise injects 13 known topic corruptions; its agreement statistic is a simulation, not human inter-annotator agreement. Calibration/holdout is a fixed order split, not random population sampling; no dictionaries were tuned on held-out labels during this run.

[Source data and reproduction](02-AI-Data-Annotation/README.md)

## 03-Multilingual-AI-Evaluation

The benchmark contains 50 English prompts and 100 Malayalam candidate translations. Automatic integrity checks flag 5 candidates. Passing these checks cannot establish semantic fidelity, grammatical correctness or cultural appropriateness.

Error categories describe synthetic benchmark construction. The category 'none' is retained in the composition table but is excluded from per-domain error-rate numerators. Digit mismatches are review flags because Malayalam may express a number in words. Native-speaker judgments, rationale edits and adjudication remain pending; blank reviewer forms are supplied rather than fabricated ratings.

[Source data and reproduction](03-Multilingual-AI-Evaluation/README.md)

## 04-Multimodal-AI-Evaluation

The visual dataset contains 120 unique rendered PNGs and 240 synthetic answer records. The actual RGB-pixel baseline correctly answers 54/60 eligible questions (90.0%), with 50.0% coverage and 60 abstentions.

The baseline reads image pixels for counts, color frequency and bar height. Ground truth is generated from rendering geometry; scene metadata is not used to predict answers. Abstentions cover spatial/absence/UI tasks unsupported by this baseline. Performance on simple colored components says nothing about photographs, real charts, OCR or a vision-language model. Six color-order failures in the eligible subset expose limitations of the leftmost tie heuristic on multi-row layouts.

[Source data and reproduction](04-Multimodal-AI-Evaluation/README.md)

## 05-AI-Quality-Evaluation

The lexical triage baseline achieves 42.0% agreement and macro-F1 0.250 against provisional project-owned safety decisions. There are 15 missed escalations and 0 unnecessary escalations.

Risk words in a prompt do not establish that a response is unsafe: refusals, education and benign requests require contextual judgment. Conversely, a harmful implication can avoid trigger words. The score is not a safety certification. Missed escalations get review priority; over-refusal and reviewer cost must also be tracked. A revised classifier needs a fresh held-out set, not tuning on all 100 cases.

[Source data and reproduction](05-AI-Quality-Evaluation/README.md)

## 06-Search-Relevance

Across 30 fictional query sets (120 judged results), lexical ranking achieves NDCG@4 0.962 and MRR 0.983. The review queue contains 1 cases below NDCG 0.8.

These scores are likely optimistic because the synthetic snippets often repeat query terms and each query has only four candidate results. They are not search-engine performance. Evaluate synonym-heavy queries, ambiguous intent, misleading keyword overlap, locale mismatch and stale-but-on-topic results on a new collection before making stronger claims. Intended local coverage must be checked from the actual intent counts, not assumed from the generation brief.

[Source data and reproduction](06-Search-Relevance/README.md)









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

<!-- HH_STUDY:START -->
## Second completed public-data study: human preference analysis

**200 HH-RLHF pairs / 400 original candidate responses**, with source-published human preferences, a pinned official revision, MIT notice and documented sampling rules. A longer-response proxy agrees on **117/195 non-tied pairs (60%)**, with five ties. The deterministic coin baseline is **50.5%**. This shows the limits of superficial ranking proxies—not personal evaluator accuracy or production-model quality.

- [Source, methodology and reproduction](01-LLM-Evaluation/experiments/hh-preference/README.md)
- [Actual results and bias limits](01-LLM-Evaluation/experiments/hh-preference/results/REPORT.md)
- [Operational BANKING77 audit](02-AI-Data-Annotation/experiments/banking77/results/QA_CASE_STUDY.md)
- [Practical review playbook](QUALITY_REVIEW_PLAYBOOK.md)

The portfolio contains **two real public-data studies plus six synthetic baseline demonstrations**. The original authors supplied public labels; personal review fields remain blank.

<!-- HH_STUDY:END -->
