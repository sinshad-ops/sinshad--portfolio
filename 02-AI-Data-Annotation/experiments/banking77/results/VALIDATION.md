# Banking77 release validation

{
  "status": "PASS",
  "banking77_tests": 10,
  "preserved_suite_tests": 11,
  "notebook_executed_and_output_verified": true,
  "banking77_numeric_and_csv_byte_reproduction": "PASS",
  "synthetic_source_data_files_byte_preserved": 156,
  "all_six_synthetic_metric_values_preserved": true,
  "personal_human_annotation_performed": false,
  "run_date": "2026-10-09"
}

## Test logs
```text



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
Ran 11 tests in 3.173s

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
Ran 10 tests in 0.134s

OK

```

Original metric JSON may be serialized with different line endings on different platforms; numerical values are unchanged. New Banking77 predictions/metrics were identical on repeated same-environment execution.
