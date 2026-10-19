# Methodology — AI Safety and Quality Triage

## Design
Apply transparent escalation/revision lexical rules without consulting expected decisions; compare against provisional project-owned labels and route escalations or mismatches to human review.

## Computation
Report accuracy, macro-F1, confusion, category slices, and escalation false negatives/positives. Escalation false negatives receive review priority.

## Reproducibility
The build uses seed `20261008`, stable ID order, local files, deterministic drawing, and JSON metrics. Re-running root `analysis.py` recreates metrics, queues, and charts.

## QA controls
Schema checks, unique-ID checks, label-range checks, image pixel checks, entity span validation, deterministic reproduction tests, and output-consistency tests are run automatically.

## Interpretation boundary
The rubric is not an employer policy and the results are not a safety certification. Lexical matching can both miss risks and over-refuse benign content.
