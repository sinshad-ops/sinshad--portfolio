# Methodology — Multi-task AI Data Annotation

## Design
Frozen keyword dictionaries predict topic, sentiment, and urgency without reading reference labels. Regex extracts only high-confidence order/date entities. The first 70 IDs are calibration and final 30 are holdout.

## Computation
Accuracy and macro-F1 are computed separately per task. Entity precision/recall/F1 requires exact start, end, and label match.

## Reproducibility
The build uses seed `20261008`, stable ID order, local files, deterministic drawing, and JSON metrics. Re-running root `analysis.py` recreates metrics, queues, and charts.

## QA controls
Schema checks, unique-ID checks, label-range checks, image pixel checks, entity span validation, deterministic reproduction tests, and output-consistency tests are run automatically.

## Interpretation boundary
Keywords are brittle and entity coverage is intentionally narrow. The controlled second-label corruption is SIMULATION NOT HUMAN and cannot establish annotator agreement.
