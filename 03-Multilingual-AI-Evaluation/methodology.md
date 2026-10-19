# Methodology — Malayalam Translation Evaluation

## Design
Summarize benchmark preference/error composition, then run NFC, Malayalam-codepoint ratio, and digit-preservation flag checks.

## Computation
Composition error rate counts supplied synthetic error tags. Automatic QC flags are integrity indicators, not linguistic scores.

## Reproducibility
The build uses seed `20261008`, stable ID order, local files, deterministic drawing, and JSON metrics. Re-running root `analysis.py` recreates metrics, queues, and charts.

## QA controls
Schema checks, unique-ID checks, label-range checks, image pixel checks, entity span validation, deterministic reproduction tests, and output-consistency tests are run automatically.

## Interpretation boundary
Malayalam native human review is pending. Digit translation may legitimately use Malayalam digits or spelled numbers; flags are never definitive language correctness.
