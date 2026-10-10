# Reference-labelled batch QA audit

Actual analysis of the BANKING77 official-test predictions. This is a portfolio simulation of a labelled audit workflow, not client work or a released production batch.

| Query-length cohort | Queries | Accuracy | High-confidence errors |
|---|---:|---:|---:|
| 01_short_1_to_7_words | 929 | 82.45% | 89 |
| 02_medium_8_to_15_words | 1745 | 86.65% | 161 |
| 03_long_16_plus_words | 406 | 90.39% | 29 |

## Operational interpretation
- A schema pass is not a semantic quality pass. Published-label disagreement and confidence are distinct signals.
- High-confidence errors occur; the Naive Bayes probability is not calibrated and must not be used as a quality guarantee.
- Disagreement detection here requires published reference labels. For unseen production data, those labels may not exist; use independent sampled review rather than claiming this audit catches all errors.
- Query length is a descriptive cohort, not a protected demographic attribute or proof of fairness.
- The original 535-case queue is not adjudicated; no batch approval or personal review is claimed.

## Proposed workflow (not represented as previously performed)
1. Verify source hashes and label schema. Quarantine invalid rows instead of guessing labels.
2. Preserve published references and raw text; log new model outputs separately.
3. Route labelled disagreements and low-confidence cases to review. Check high-confidence predictions by random sampling as well.
4. Record reviewer decision, evidence and reason; escalate ambiguous cases to a second reviewer.
5. Rerun metrics after adjudication while preserving the original benchmark for comparison.
6. Use a clearly recorded owner approval before any hypothetical batch release.
