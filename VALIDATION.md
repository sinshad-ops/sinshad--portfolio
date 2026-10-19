# Validation Report

Generated automatically on 2026-10-09.

- Deterministic seed: `20261008`
- Test command: `python -m unittest discover -s tests -v`
- Status: **PASS**

## Covered checks
Schema counts, unique IDs, annotation labels, exact substring spans, judge score ranges, image dimensions and non-background pixels, unique image hashes, metric ranges, output consistency, manifest hashes, and deterministic analysis reproduction.

## Test output
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
Ran 11 tests in 26.769s

OK
```

<!-- BANKING77_VALIDATION -->
## Banking77 release

10 new experiment tests and 11 preserved-suite tests pass. Actual notebook execution and deterministic rerun are verified. See [`02-AI-Data-Annotation/experiments/banking77/results/VALIDATION.md`](02-AI-Data-Annotation/experiments/banking77/results/VALIDATION.md). Original synthetic metric values and source datasets were checked against the uploaded archive.
