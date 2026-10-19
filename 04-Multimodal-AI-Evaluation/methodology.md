# Methodology — Synthetic Visual Evaluation

## Design
Render deterministic scenes, derive ground truth from geometry, create controlled correct/faulty answers, and evaluate eligible tasks with RGB connected-component or bar-pixel scanning.

## Computation
Pixel accuracy = correct eligible predictions / eligible predictions. Coverage = eligible predictions / all scenes; unsupported question types abstain.

## Reproducibility
The build uses seed `20261008`, stable ID order, local files, deterministic drawing, and JSON metrics. Re-running root `analysis.py` recreates metrics, queues, and charts.

## QA controls
Schema checks, unique-ID checks, label-range checks, image pixel checks, entity span validation, deterministic reproduction tests, and output-consistency tests are run automatically.

## Interpretation boundary
These are artificial images, not natural photos. Metadata is an oracle for data construction only and is not read by the pixel baseline. This is not a VLM evaluation.
