# Methodology — LLM Pairwise Evaluation

## Design
Compare the held-back provisional author preference with a separate AI scoring pass preference. Compute a three-class confusion matrix, agreement, category slices, score means, threshold sensitivity, and response-level pass rules.

## Computation
Weighted score = 0.4×accuracy + 0.3×instruction following + 0.2×helpfulness + 0.1×clarity. Pass requires weighted score ≥4, accuracy ≥4, and instruction following ≥4.

## Reproducibility
The build uses seed `20261008`, stable ID order, local files, deterministic drawing, and JSON metrics. Re-running root `analysis.py` recreates metrics, queues, and charts.

## QA controls
Schema checks, unique-ID checks, label-range checks, image pixel checks, entity span validation, deterministic reproduction tests, and output-consistency tests are run automatically.

## Interpretation boundary
Neither the provisional author preference nor AI judge is human gold. Both calls use the Strawberry fast tier; underlying model identity/version and temperature were not supplied. Independence of model family is not established. Agreement is not model accuracy or human kappa.
