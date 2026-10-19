# Results Analysis

## Scope
These numbers are generated from the repository data by `analysis.py`; they are not manually entered.

## Primary interpretation
Summarize benchmark preference/error composition, then run NFC, Malayalam-codepoint ratio, and digit-preservation flag checks.

## Important boundary
Malayalam native human review is pending. Digit translation may legitimately use Malayalam digits or spelled numbers; flags are never definitive language correctness.

## Decision use
Metrics identify patterns and prioritize review. They do not replace human adjudication, prove production readiness, or establish the author’s personal accuracy.

## Machine-readable snapshot
```json
{
  "automatic_qc_flags": 5,
  "benchmark_preference_counts": {
    "A": 18,
    "B": 21,
    "tie": 11
  },
  "candidate_count": 100,
  "human_review": "Malayalam native human review required; no human scores or language accuracy reported",
  "integrity_scope": "flag-only Unicode/script/digit checks, never definitive correctness",
  "pair_count": 50,
  "per_domain_composition_error_rate": {
    "culture": {
      "candidate_n": 12,
      "rate": 0.4166666666666667
    },
    "customer_support": {
      "candidate_n": 16,
      "rate": 0.375
    },
    "education": {
      "candidate_n": 16,
      "rate": 0.3125
    },
    "health_information": {
      "candidate_n": 14,
      "rate": 0.35714285714285715
    },
    "public_service": {
      "candidate_n": 16,
      "rate": 0.4375
    },
    "technology": {
      "candidate_n": 12,
      "rate": 0.4166666666666667
    },
    "travel": {
      "candidate_n": 14,
      "rate": 0.42857142857142855
    }
  },
  "project": "multilingual",
  "synthetic_error_distribution": {
    "meaning_shift": 14,
    "negation_error": 9,
    "none": 61,
    "number_error": 5,
    "omission": 10,
    "register": 1
  }
}
```
