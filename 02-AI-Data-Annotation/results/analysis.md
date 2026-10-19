# Results Analysis

## Scope
These numbers are generated from the repository data by `analysis.py`; they are not manually entered.

## Primary interpretation
Frozen keyword dictionaries predict topic, sentiment, and urgency without reading reference labels. Regex extracts only high-confidence order/date entities. The first 70 IDs are calibration and final 30 are holdout.

## Important boundary
Keywords are brittle and entity coverage is intentionally narrow. The controlled second-label corruption is SIMULATION NOT HUMAN and cannot establish annotator agreement.

## Decision use
Metrics identify patterns and prioritize review. They do not replace human adjudication, prove production readiness, or establish the author’s personal accuracy.

## Machine-readable snapshot
```json
{
  "all": {
    "entity_span_exact": {
      "f1": 0.0,
      "fn": 58,
      "fp": 0,
      "precision": 0.0,
      "recall": 0.0,
      "tp": 0
    },
    "sentiment": {
      "accuracy": 0.34,
      "confusion": {
        "mixed": {
          "mixed": 1,
          "negative": 3,
          "neutral": 15,
          "positive": 3
        },
        "negative": {
          "mixed": 0,
          "negative": 6,
          "neutral": 42,
          "positive": 0
        },
        "neutral": {
          "mixed": 0,
          "negative": 3,
          "neutral": 27,
          "positive": 0
        },
        "positive": {
          "mixed": 0,
          "negative": 0,
          "neutral": 0,
          "positive": 0
        }
      },
      "macro_f1": 0.19016018306636157,
      "n": 100,
      "per_class": {
        "mixed": {
          "f1": 0.08695652173913045,
          "precision": 1.0,
          "recall": 0.045454545454545456,
          "support": 22
        },
        "negative": {
          "f1": 0.2,
          "precision": 0.5,
          "recall": 0.125,
          "support": 48
        },
        "neutral": {
          "f1": 0.4736842105263158,
          "precision": 0.32142857142857145,
          "recall": 0.9,
          "support": 30
        },
        "positive": {
          "f1": 0.0,
          "precision": 0.0,
          "recall": 0.0,
          "support": 0
        }
      }
    },
    "topic": {
      "accuracy": 0.74,
      "confusion": {
        "account": {
          "account": 12,
          "billing": 2,
          "delivery": 0,
          "general": 1,
          "refund": 0,
          "technical": 2
        },
        "billing": {
          "account": 0,
          "billing": 16,
          "delivery": 0,
          "general": 1,
          "refund": 0,
          "technical": 0
        },
        "delivery": {
          "account": 0,
          "billing": 1,
          "delivery": 16,
          "general": 0,
          "refund": 0,
          "technical": 0
        },
        "general": {
          "account": 4,
          "billing": 1,
          "delivery": 1,
          "general": 7,
          "refund": 1,
          "technical": 2
        },
        "refund": {
          "account": 0,
          "billing": 2,
          "delivery": 2,
          "general": 0,
          "refund": 10,
          "technical": 2
        },
        "technical": {
          "account": 1,
          "billing": 0,
          "delivery": 0,
          "general": 3,
          "refund": 0,
          "technical": 13
        }
      },
      "macro_f1": 0.7297078375509748,
      "n": 100,
      "per_class": {
        "account": {
          "f1": 0.7058823529411765,
          "precision": 0.7058823529411765,
          "recall": 0.7058823529411765,
          "support": 17
        },
        "billing": {
          "f1": 0.8205128205128205,
          "precision": 0.7272727272727273,
          "recall": 0.9411764705882353,
          "support": 17
        },
        "delivery": {
          "f1": 0.8888888888888888,
          "precision": 0.8421052631578947,
          "recall": 0.9411764705882353,
          "support": 17
        },
        "general": {
          "f1": 0.5,
          "precision": 0.5833333333333334,
          "recall": 0.4375,
          "support": 16
        },
        "refund": {
          "f1": 0.7407407407407406,
          "precision": 0.9090909090909091,
          "recall": 0.625,
          "support": 16
        },
        "technical": {
          "f1": 0.7222222222222222,
          "precision": 0.6842105263157895,
          "recall": 0.7647058823529411,
          "support": 17
        }
      }
    },
    "urgency": {
      "accuracy": 0.33,
      "confusion": {
        "high": {
          "high": 8,
          "low": 14,
          "medium": 0
        },
        "low": {
          "high": 6,
          "low": 14,
          "medium": 2
        },
        "medium": {
          "high": 14,
          "low": 31,
          "medium": 11
        }
      },
      "macro_f1": 0.3281731973519413,
      "n": 100,
      "per_class": {
        "high": {
          "f1": 0.32,
          "precision": 0.2857142857142857,
          "recall": 0.36363636363636365,
          "support": 22
        },
        "low": {
          "f1": 0.345679012345679,
          "precision": 0.23728813559322035,
          "recall": 0.6363636363636364,
          "support": 22
        },
        "medium": {
          "f1": 0.3188405797101449,
          "precision": 0.8461538461538461,
          "recall": 0.19642857142857142,
          "support": 56
        }
      }
    }
  },
  "baseline": "frozen keyword dictionaries; labels are not consulted during prediction",
  "case_count": 100,
  "holdout": {
    "entity_span_exact": {
      "f1": 0.0,
      "fn": 13,
      "fp": 0,
      "precision": 0.0,
      "recall": 0.0,
      "tp": 0
    },
    "sentiment": {
      "accuracy": 0.4,
      "confusion": {
        "mixed": {
          "mixed": 0,
          "negative": 2,
          "neutral": 3,
          "positive": 1
        },
        "negative": {
          "mixed": 0,
          "negative": 0,
          "neutral": 11,
          "positive": 0
        },
        "neutral": {
          "mixed": 0,
          "negative": 1,
          "neutral": 12,
          "positive": 0
        },
        "positive": {
          "mixed": 0,
          "negative": 0,
          "neutral": 0,
          "positive": 0
        }
      },
      "macro_f1": 0.15384615384615388,
      "n": 30,
      "per_class": {
        "mixed": {
          "f1": 0.0,
          "precision": 0.0,
          "recall": 0.0,
          "support": 6
        },
        "negative": {
          "f1": 0.0,
          "precision": 0.0,
          "recall": 0.0,
          "support": 11
        },
        "neutral": {
          "f1": 0.6153846153846155,
          "precision": 0.46153846153846156,
          "recall": 0.9230769230769231,
          "support": 13
        },
        "positive": {
          "f1": 0.0,
          "precision": 0.0,
          "recall": 0.0,
          "support": 0
        }
      }
    },
    "topic": {
      "accuracy": 0.7666666666666667,
      "confusion": {
        "account": {
          "account": 3,
          "billing": 1,
          "delivery": 0,
          "general": 0,
          "refund": 0,
          "technical": 1
        },
        "billing": {
          "account": 0,
          "billing": 5,
          "delivery": 0,
          "general": 0,
          "refund": 0,
          "technical": 0
        },
        "delivery": {
          "account": 0,
          "billing": 1,
          "delivery": 4,
          "general": 0,
          "refund": 0,
          "technical": 0
        },
        "general": {
          "account": 0,
          "billing": 0,
          "delivery": 0,
          "general": 3,
          "refund": 0,
          "technical": 2
        },
        "refund": {
          "account": 0,
          "billing": 1,
          "delivery": 0,
          "general": 0,
          "refund": 3,
          "technical": 1
        },
        "technical": {
          "account": 0,
          "billing": 0,
          "delivery": 0,
          "general": 0,
          "refund": 0,
          "technical": 5
        }
      },
      "macro_f1": 0.7704008954008953,
      "n": 30,
      "per_class": {
        "account": {
          "f1": 0.7499999999999999,
          "precision": 1.0,
          "recall": 0.6,
          "support": 5
        },
        "billing": {
          "f1": 0.7692307692307693,
          "precision": 0.625,
          "recall": 1.0,
          "support": 5
        },
        "delivery": {
          "f1": 0.888888888888889,
          "precision": 1.0,
          "recall": 0.8,
          "support": 5
        },
        "general": {
          "f1": 0.7499999999999999,
          "precision": 1.0,
          "recall": 0.6,
          "support": 5
        },
        "refund": {
          "f1": 0.7499999999999999,
          "precision": 1.0,
          "recall": 0.6,
          "support": 5
        },
        "technical": {
          "f1": 0.7142857142857143,
          "precision": 0.5555555555555556,
          "recall": 1.0,
          "support": 5
        }
      }
    },
    "urgency": {
      "accuracy": 0.43333333333333335,
      "confusion": {
        "high": {
          "high": 2,
          "low": 4,
          "medium": 0
        },
        "low": {
          "high": 1,
          "low": 5,
          "medium": 0
        },
        "medium": {
          "high": 3,
          "low": 9,
          "medium": 6
        }
      },
      "macro_f1": 0.4166666666666667,
      "n": 30,
      "per_class": {
        "high": {
          "f1": 0.3333333333333333,
          "precision": 0.3333333333333333,
          "recall": 0.3333333333333333,
          "support": 6
        },
        "low": {
          "f1": 0.4166666666666667,
          "precision": 0.2777777777777778,
          "recall": 0.8333333333333334,
          "support": 6
        },
        "medium": {
          "f1": 0.5,
          "precision": 1.0,
          "recall": 0.3333333333333333,
          "support": 18
        }
      }
    }
  },
  "project": "annotation",
  "qc": {
    "malformed_span_quarantine": 2,
    "manual_queue": 29
  },
  "simulation_not_human": {
    "agreement": 0.87,
    "controlled_errors": 13,
    "rate": 0.13,
    "warning": "SIMULATION NOT HUMAN; not annotator agreement"
  },
  "split": {
    "calibration": 70,
    "holdout": 30
  }
}
```
