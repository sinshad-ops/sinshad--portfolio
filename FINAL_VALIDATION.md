# Final release verification

```json
{
  "status": "PASS",
  "test_count": 28,
  "python_verified": "3.14.6",
  "real_public_data_studies": 2,
  "banking77_test_queries": 3080,
  "hh_preference_pairs": 200,
  "deterministic_public_results": "PASS",
  "hh_notebook_actually_executed": true,
  "offline_hh_sample_reanalysis": "PASS",
  "synthetic_input_files_preserved": 156,
  "six_synthetic_metric_values_preserved": true,
  "github_actions_matrix_executed": false,
  "personal_human_annotation_performed": false,
  "employment_or_client_work_claimed": false
}
```

## Actual local logs
```text


{
  "dataset": "BANKING77",
  "source_revision": "57ec275d8078af65b7731c2a98be812d844a6d6b",
  "source_license": "CC-BY-4.0",
  "published_test_metrics": {
    "n": 3080,
    "correct": 2645,
    "accuracy": 0.8587662337662337,
    "macro_f1": 0.85792295772106,
    "top3_accuracy": 0.9516233766233766,
    "label_count": 77
  },
  "train_text_disjoint_test_metrics": {
    "n": 3073,
    "correct": 2638,
    "accuracy": 0.8584445167588676,
    "macro_f1": 0.8575329352055806,
    "top3_accuracy": 0.9515131793036121,
    "label_count": 77
  },
  "majority_baseline": {
    "n": 3080,
    "correct": 40,
    "accuracy": 0.012987012987012988,
    "macro_f1": 0.00033300033300033305,
    "top3_accuracy": 0.012987012987012988,
    "label_count": 77
  },
  "majority_intent": "card_payment_fee_charged",
  "source_qa": {
    "normalization": "NFKC + casefold + collapse whitespace",
    "rows": {
      "train": 10003,
      "test": 3080
    },
    "duplicate_extra_rows": {
      "train": 4,
      "test": 1
    },
    "train_test_overlap_unique_texts": 7,
    "test_rows_with_train_text": 7,
    "conflicting_label_groups": 0
  },
  "review_queue_rows": 535,
  "model_disagreements": 435,
  "vocabulary_size": 22266,
  "split_counts": {
    "train": 10003,
    "test": 3080
  },
  "labels_origin": "Published annotations from original dataset authors; no new human annotation performed",
  "claims_boundary": "Automatic classifier agreement with published benchmark labels; not personal annotator accuracy, production accuracy or model safety certification"
}


{
  "dataset": "Anthropic HH-RLHF helpful-base official test",
  "selection": {
    "eligible_rows": 304,
    "excluded": {
      "blocked_content_or_email": 94,
      "format_or_context_mismatch": 13,
      "non_target_topic": 1943,
      "oversized": 0
    },
    "manually_safety_reviewed": false,
    "official_source_rows": 2354,
    "sampling_bias": "curated educational/practical topics, NOT representative of all HH-RLHF",
    "selected_pairs": 200,
    "selection": "topic regex + broad risky-content/email exclusion + context match + size bounds; deterministic hash ordering; cap 200"
  },
  "baselines": [
    {
      "rule": "seeded_coin",
      "pairs": 200,
      "covered": 200,
      "ties": 0,
      "coverage": 1.0,
      "agreements": 101,
      "agreement_on_covered": 0.505,
      "agreement_all_pairs_ties_count_as_no_agreement": 0.505
    },
    {
      "rule": "longer_response",
      "pairs": 200,
      "covered": 195,
      "ties": 5,
      "coverage": 0.975,
      "agreements": 117,
      "agreement_on_covered": 0.6,
      "agreement_all_pairs_ties_count_as_no_agreement": 0.585
    },
    {
      "rule": "shorter_response",
      "pairs": 200,
      "covered": 195,
      "ties": 5,
      "coverage": 0.975,
      "agreements": 78,
      "agreement_on_covered": 0.4,
      "agreement_all_pairs_ties_count_as_no_agreement": 0.39
    }
  ],
  "by_topic": {
    "computing": [
      {
        "rule": "seeded_coin",
        "pairs": 23,
        "covered": 23,
        "ties": 0,
        "coverage": 1.0,
        "agreements": 14,
        "agreement_on_covered": 0.6086956521739131,
        "agreement_all_pairs_ties_count_as_no_agreement": 0.6086956521739131
      },
      {
        "rule": "longer_response",
        "pairs": 23,
        "covered": 21,
        "ties": 2,
        "coverage": 0.9130434782608695,
        "agreements": 15,
        "agreement_on_covered": 0.7142857142857143,
        "agreement_all_pairs_ties_count_as_no_agreement": 0.6521739130434783
      },
      {
        "rule": "shorter_response",
        "pairs": 23,
        "covered": 21,
        "ties": 2,
        "coverage": 0.9130434782608695,
        "agreements": 6,
        "agreement_on_covered": 0.2857142857142857,
        "agreement_all_pairs_ties_count_as_no_agreement": 0.2608695652173913
      }
    ],
    "everyday_tasks": [
      {
        "rule": "seeded_coin",
        "pairs": 160,
        "covered": 160,
        "ties": 0,
        "coverage": 1.0,
        "agreements": 79,
        "agreement_on_covered": 0.49375,
        "agreement_all_pairs_ties_count_as_no_agreement": 0.49375
      },
      {
        "rule": "longer_response",
        "pairs": 160,
        "covered": 157,
        "ties": 3,
        "coverage": 0.98125,
        "agreements": 93,
        "agreement_on_covered": 0.5923566878980892,
        "agreement_all_pairs_ties_count_as_no_agreement": 0.58125
      },
      {
        "rule": "shorter_response",
        "pairs": 160,
        "covered": 157,
        "ties": 3,
        "coverage": 0.98125,
        "agreements": 64,
        "agreement_on_covered": 0.40764331210191085,
        "agreement_all_pairs_ties_count_as_no_agreement": 0.4
      }
    ],
    "science": [
      {
        "rule": "seeded_coin",
        "pairs": 17,
        "covered": 17,
        "ties": 0,
        "coverage": 1.0,
        "agreements": 8,
        "agreement_on_covered": 0.47058823529411764,
        "agreement_all_pairs_ties_count_as_no_agreement": 0.47058823529411764
      },
      {
        "rule": "longer_response",
        "pairs": 17,
        "covered": 17,
        "ties": 0,
        "coverage": 1.0,
        "agreements": 9,
        "agreement_on_covered": 0.5294117647058824,
        "agreement_all_pairs_ties_count_as_no_agreement": 0.5294117647058824
      },
      {
        "rule": "shorter_response",
        "pairs": 17,
        "covered": 17,
        "ties": 0,
        "coverage": 1.0,
        "agreements": 8,
        "agreement_on_covered": 0.47058823529411764,
        "agreement_all_pairs_ties_count_as_no_agreement": 0.47058823529411764
      }
    ]
  },
  "interpretation": "Agreement with published human preferences, not factual correctness, personal annotator accuracy, model safety, or an evaluated production LLM.",
  "new_model_responses_generated": false,
  "personal_human_annotation_performed": false
}


{
  "dataset": "BANKING77",
  "source_revision": "57ec275d8078af65b7731c2a98be812d844a6d6b",
  "source_license": "CC-BY-4.0",
  "published_test_metrics": {
    "n": 3080,
    "correct": 2645,
    "accuracy": 0.8587662337662337,
    "macro_f1": 0.85792295772106,
    "top3_accuracy": 0.9516233766233766,
    "label_count": 77
  },
  "train_text_disjoint_test_metrics": {
    "n": 3073,
    "correct": 2638,
    "accuracy": 0.8584445167588676,
    "macro_f1": 0.8575329352055806,
    "top3_accuracy": 0.9515131793036121,
    "label_count": 77
  },
  "majority_baseline": {
    "n": 3080,
    "correct": 40,
    "accuracy": 0.012987012987012988,
    "macro_f1": 0.00033300033300033305,
    "top3_accuracy": 0.012987012987012988,
    "label_count": 77
  },
  "majority_intent": "card_payment_fee_charged",
  "source_qa": {
    "normalization": "NFKC + casefold + collapse whitespace",
    "rows": {
      "train": 10003,
      "test": 3080
    },
    "duplicate_extra_rows": {
      "train": 4,
      "test": 1
    },
    "train_test_overlap_unique_texts": 7,
    "test_rows_with_train_text": 7,
    "conflicting_label_groups": 0
  },
  "review_queue_rows": 535,
  "model_disagreements": 435,
  "vocabulary_size": 22266,
  "split_counts": {
    "train": 10003,
    "test": 3080
  },
  "labels_origin": "Published annotations from original dataset authors; no new human annotation performed",
  "claims_boundary": "Automatic classifier agreement with published benchmark labels; not personal annotator accuracy, production accuracy or model safety certification"
}


{
  "dataset": "Anthropic HH-RLHF helpful-base official test",
  "selection": {
    "eligible_rows": 304,
    "excluded": {
      "blocked_content_or_email": 94,
      "format_or_context_mismatch": 13,
      "non_target_topic": 1943,
      "oversized": 0
    },
    "manually_safety_reviewed": false,
    "official_source_rows": 2354,
    "sampling_bias": "curated educational/practical topics, NOT representative of all HH-RLHF",
    "selected_pairs": 200,
    "selection": "topic regex + broad risky-content/email exclusion + context match + size bounds; deterministic hash ordering; cap 200"
  },
  "baselines": [
    {
      "rule": "seeded_coin",
      "pairs": 200,
      "covered": 200,
      "ties": 0,
      "coverage": 1.0,
      "agreements": 101,
      "agreement_on_covered": 0.505,
      "agreement_all_pairs_ties_count_as_no_agreement": 0.505
    },
    {
      "rule": "longer_response",
      "pairs": 200,
      "covered": 195,
      "ties": 5,
      "coverage": 0.975,
      "agreements": 117,
      "agreement_on_covered": 0.6,
      "agreement_all_pairs_ties_count_as_no_agreement": 0.585
    },
    {
      "rule": "shorter_response",
      "pairs": 200,
      "covered": 195,
      "ties": 5,
      "coverage": 0.975,
      "agreements": 78,
      "agreement_on_covered": 0.4,
      "agreement_all_pairs_ties_count_as_no_agreement": 0.39
    }
  ],
  "by_topic": {
    "computing": [
      {
        "rule": "seeded_coin",
        "pairs": 23,
        "covered": 23,
        "ties": 0,
        "coverage": 1.0,
        "agreements": 14,
        "agreement_on_covered": 0.6086956521739131,
        "agreement_all_pairs_ties_count_as_no_agreement": 0.6086956521739131
      },
      {
        "rule": "longer_response",
        "pairs": 23,
        "covered": 21,
        "ties": 2,
        "coverage": 0.9130434782608695,
        "agreements": 15,
        "agreement_on_covered": 0.7142857142857143,
        "agreement_all_pairs_ties_count_as_no_agreement": 0.6521739130434783
      },
      {
        "rule": "shorter_response",
        "pairs": 23,
        "covered": 21,
        "ties": 2,
        "coverage": 0.9130434782608695,
        "agreements": 6,
        "agreement_on_covered": 0.2857142857142857,
        "agreement_all_pairs_ties_count_as_no_agreement": 0.2608695652173913
      }
    ],
    "everyday_tasks": [
      {
        "rule": "seeded_coin",
        "pairs": 160,
        "covered": 160,
        "ties": 0,
        "coverage": 1.0,
        "agreements": 79,
        "agreement_on_covered": 0.49375,
        "agreement_all_pairs_ties_count_as_no_agreement": 0.49375
      },
      {
        "rule": "longer_response",
        "pairs": 160,
        "covered": 157,
        "ties": 3,
        "coverage": 0.98125,
        "agreements": 93,
        "agreement_on_covered": 0.5923566878980892,
        "agreement_all_pairs_ties_count_as_no_agreement": 0.58125
      },
      {
        "rule": "shorter_response",
        "pairs": 160,
        "covered": 157,
        "ties": 3,
        "coverage": 0.98125,
        "agreements": 64,
        "agreement_on_covered": 0.40764331210191085,
        "agreement_all_pairs_ties_count_as_no_agreement": 0.4
      }
    ],
    "science": [
      {
        "rule": "seeded_coin",
        "pairs": 17,
        "covered": 17,
        "ties": 0,
        "coverage": 1.0,
        "agreements": 8,
        "agreement_on_covered": 0.47058823529411764,
        "agreement_all_pairs_ties_count_as_no_agreement": 0.47058823529411764
      },
      {
        "rule": "longer_response",
        "pairs": 17,
        "covered": 17,
        "ties": 0,
        "coverage": 1.0,
        "agreements": 9,
        "agreement_on_covered": 0.5294117647058824,
        "agreement_all_pairs_ties_count_as_no_agreement": 0.5294117647058824
      },
      {
        "rule": "shorter_response",
        "pairs": 17,
        "covered": 17,
        "ties": 0,
        "coverage": 1.0,
        "agreements": 8,
        "agreement_on_covered": 0.47058823529411764,
        "agreement_all_pairs_ties_count_as_no_agreement": 0.47058823529411764
      }
    ]
  },
  "interpretation": "Agreement with published human preferences, not factual correctness, personal annotator accuracy, model safety, or an evaluated production LLM.",
  "new_model_responses_generated": false,
  "personal_human_annotation_performed": false
}



test_annotation_labels_spans_and_counts (test_portfolio.PortfolioTests.test_annotation_labels_spans_and_counts) ... ok
test_deterministic_analysis (test_portfolio.PortfolioTests.test_deterministic_analysis) ... ok
test_image_pixels (test_portfolio.PortfolioTests.test_image_pixels) ... ok
test_judge_score_range (test_portfolio.PortfolioTests.test_judge_score_range) ... ok
test_manifest_hashes (test_portfolio.PortfolioTests.test_manifest_hashes) ... ok
test_output_consistency (test_portfolio.PortfolioTests.test_output_consistency) ... ok
test_schemas_ids_and_counts (test_portfolio.PortfolioTests.test_schemas_ids_and_counts) ... ok
test_all_notebooks_are_executed_outputs (test_regressions.RegressionTests.test_all_notebooks_are_executed_outputs) ... ok
test_baseline_does_not_depend_on_reference_labels (test_regressions.RegressionTests.test_baseline_does_not_depend_on_reference_labels) ... ok
test_metric_known_values (test_regressions.RegressionTests.test_metric_known_values) ... ok
test_multilingual_none_is_not_error (test_regressions.RegressionTests.test_multilingual_none_is_not_error) ... ok

----------------------------------------------------------------------
Ran 11 tests in 3.178s

OK


test_development_group_leakage (test_banking77.Banking77Tests.test_development_group_leakage) ... ok
test_features_keep_negation (test_banking77.Banking77Tests.test_features_keep_negation) ... ok
test_known_metric_values (test_banking77.Banking77Tests.test_known_metric_values) ... ok
test_metrics_recalculate (test_banking77.Banking77Tests.test_metrics_recalculate) ... ok
test_model_predictions_need_only_text (test_banking77.Banking77Tests.test_model_predictions_need_only_text) ... ok
test_official_counts_and_labels (test_banking77.Banking77Tests.test_official_counts_and_labels) ... ok
test_official_source_hashes (test_banking77.Banking77Tests.test_official_source_hashes) ... ok
test_official_test_matches_predictions (test_banking77.Banking77Tests.test_official_test_matches_predictions) ... ok
test_review_queue_has_no_invented_human_ratings (test_banking77.Banking77Tests.test_review_queue_has_no_invented_human_ratings) ... ok
test_validation_only_parameter_selection (test_banking77.Banking77Tests.test_validation_only_parameter_selection) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.141s

OK


test_balanced_display_order (test_hh_preference.PreferenceTests.test_balanced_display_order) ... ok
test_known_tie_and_accuracy (test_hh_preference.PreferenceTests.test_known_tie_and_accuracy) ... ok
test_metrics_recomputed (test_hh_preference.PreferenceTests.test_metrics_recomputed) ... ok
test_no_fake_human_review (test_hh_preference.PreferenceTests.test_no_fake_human_review) ... ok
test_no_label_used_in_prediction (test_hh_preference.PreferenceTests.test_no_label_used_in_prediction) ... ok
test_original_context_present (test_hh_preference.PreferenceTests.test_original_context_present) ... ok
test_sample_count_origin (test_hh_preference.PreferenceTests.test_sample_count_origin) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.023s

OK

{
  "banking_cohorts": [
    {
      "cohort": "01_short_1_to_7_words",
      "queries": 929,
      "correct": 766,
      "accuracy": 0.8245425188374597,
      "high_confidence_predictions": 806,
      "high_confidence_errors": 89
    },
    {
      "cohort": "02_medium_8_to_15_words",
      "queries": 1745,
      "correct": 1512,
      "accuracy": 0.8664756446991404,
      "high_confidence_predictions": 1625,
      "high_confidence_errors": 161
    },
    {
      "cohort": "03_long_16_plus_words",
      "queries": 406,
      "correct": 367,
      "accuracy": 0.9039408866995073,
      "high_confidence_predictions": 393,
      "high_confidence_errors": 29
    }
  ],
  "hh_pairs": 200,
  "real_data_studies": 2,
  "personal_review_claimed": false
}


```

Python versions in the GitHub Actions matrix are configured, not independently run here. Tests are quality checks, not proof of personal reviewer skill or a job guarantee.
