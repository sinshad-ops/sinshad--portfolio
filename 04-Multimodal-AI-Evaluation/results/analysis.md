# Results Analysis

## Scope
These numbers are generated from the repository data by `analysis.py`; they are not manually entered.

## Primary interpretation
Render deterministic scenes, derive ground truth from geometry, create controlled correct/faulty answers, and evaluate eligible tasks with RGB connected-component or bar-pixel scanning.

## Important boundary
These are artificial images, not natural photos. Metadata is an oracle for data construction only and is not read by the pixel baseline. This is not a VLM evaluation.

## Decision use
Metrics identify patterns and prioritize review. They do not replace human adjudication, prove production readiness, or establish the author’s personal accuracy.

## Machine-readable snapshot
```json
{
  "answer_record_count": 240,
  "controlled_fault_records": 120,
  "ground_truth": "constructed from rendering geometry; metadata is an oracle only for dataset creation, never read by pixel baseline",
  "limitation": "Artificial geometric images are not evidence of performance on natural photos or a VLM.",
  "pixel_baseline": {
    "abstentions": 60,
    "accuracy": 0.9,
    "correct": 54,
    "coverage": 0.5,
    "eligible": 60,
    "per_type": {
      "count": {
        "accuracy": 1.0,
        "n": 20
      },
      "dominant_color": {
        "accuracy": 0.7,
        "n": 20
      },
      "tallest_bar": {
        "accuracy": 1.0,
        "n": 20
      }
    }
  },
  "project": "multimodal",
  "scene_count": 120,
  "synthetic_correct_records": 120
}
```
