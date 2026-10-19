# Data Card — Search Relevance Evaluation

## Summary
30 queries with four judged fictional results each, for 120 result judgments.

## Intended use
Local portfolio demonstration of reproducible evaluation, QA queues, metric computation, and evidence review. It is not production training data, employer work, or a validated benchmark.

## Provenance
The supplied source arrays and generated artifacts are AI-assisted synthetic personal-project data authored for Sinshad PS. LLM, multilingual, safety, annotation, and search labels are provisional unless explicitly described as rendering-derived ground truth. No independent human validation has been completed.

## Size
Primary case count reported by the pipeline: **30**.

## Processing
Source arrays are normalized into UTF-8 JSONL and CSV. Nested values in CSV are JSON-encoded. Source IDs are preserved. Deterministic build seed: `20261008`.

## Risks and limitations
Synthetic composition can make patterns easier than real operations. Reviewer demographics, adjudication, inter-annotator agreement, natural distribution shift, and external validity are absent. Sensitive production deployment requires qualified human review.

## License
Code: MIT. Synthetic data: CC BY 4.0; see repository `DATA_LICENSE.md`.
