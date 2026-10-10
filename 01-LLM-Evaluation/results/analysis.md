# Results Analysis

## Scope
These numbers are generated from the repository data by `analysis.py`; they are not manually entered.

## Primary interpretation
Compare the held-back provisional author preference with a separate AI scoring pass preference. Compute a three-class confusion matrix, agreement, category slices, score means, threshold sensitivity, and response-level pass rules.

## Important boundary
Neither the provisional author preference nor AI judge is human gold. Both calls use the Strawberry fast tier; underlying model identity/version and temperature were not supplied. Independence of model family is not established. Agreement is not model accuracy or human kappa.

## Decision use
Metrics identify patterns and prioritize review. They do not replace human adjudication, prove production readiness, or establish the author’s personal accuracy.

## Machine-readable snapshot
```json
{
  "agreement_rate": 0.9,
  "case_count": 50,
  "confusion": {
    "A": {
      "A": 22,
      "B": 0,
      "tie": 0
    },
    "B": {
      "A": 0,
      "B": 23,
      "tie": 0
    },
    "tie": {
      "A": 4,
      "B": 1,
      "tie": 0
    }
  },
  "disagreements": 5,
  "mean_scores": {
    "accuracy": 3.13,
    "clarity": 4.5,
    "helpfulness": 3.13,
    "instruction_following": 3.44
  },
  "pass_rate": 0.5,
  "pass_rule": "weighted>=4 and accuracy>=4 and instruction_following>=4",
  "per_category": {
    "arithmetic": {
      "agreement": 0.8,
      "n": 5
    },
    "coding": {
      "agreement": 0.8,
      "n": 5
    },
    "customer_support": {
      "agreement": 1.0,
      "n": 7
    },
    "extraction": {
      "agreement": 0.8333333333333334,
      "n": 6
    },
    "information_retrieval": {
      "agreement": 1.0,
      "n": 2
    },
    "instruction_following": {
      "agreement": 0.8333333333333334,
      "n": 6
    },
    "inventory": {
      "agreement": 1.0,
      "n": 1
    },
    "reasoning": {
      "agreement": 1.0,
      "n": 6
    },
    "scheduling": {
      "agreement": 1.0,
      "n": 1
    },
    "summarization": {
      "agreement": 0.75,
      "n": 4
    },
    "travel_policy": {
      "agreement": 1.0,
      "n": 2
    },
    "uncertainty": {
      "agreement": 1.0,
      "n": 5
    }
  },
  "project": "llm",
  "provenance": {
    "author_reference": "Strawberry fast model, family/version unspecified",
    "human_gold": false,
    "separate_scoring_pass": "Strawberry fast model, family/version unspecified",
    "timestamp": "2026-10-08"
  },
  "response_count": 100,
  "threshold_sensitivity": {
    "3.5": 0.5,
    "4.0": 0.5,
    "4.5": 0.5
  },
  "ties": {
    "judge": 0,
    "provisional": 5
  },
  "weighted_formula": "0.4*accuracy + 0.3*instruction_following + 0.2*helpfulness + 0.1*clarity"
}
```
