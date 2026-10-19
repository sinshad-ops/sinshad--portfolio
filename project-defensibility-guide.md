# Project Defensibility Guide

## Core formulas
- Classification accuracy: correct predictions divided by total predictions.
- Per-class F1: harmonic mean of precision and recall; macro-F1 averages class F1 equally.
- Entity exact match: predicted and reference start, end, and label must all match.
- LLM weighted score: 0.4 accuracy + 0.3 instruction following + 0.2 helpfulness + 0.1 clarity.
- NDCG@4: DCG with gain `2^relevance−1` and `log2(rank+1)` discount, divided by ideal DCG.
- MRR: reciprocal rank of the first result with relevance at least 2.
- Pixel baseline coverage: eligible predictions divided by all visual questions.

## Defensible statements
Say “the pipeline measured X against provisional project references,” not “I achieved X% human accuracy.” Say “rendering-derived ground truth” only for visual geometry. Describe corruption labels as a controlled simulation, never human agreement.

## Known failures
Keyword rules miss paraphrases. Regex entities have narrow recall. Unicode checks cannot judge translation meaning. RGB components can merge or count UI pixels. Lexical safety rules over-trigger and miss context. Search overlap misses semantic intent.

## Replication
Run root analysis, inspect metrics and queues, execute tests, then compare data-file hashes with `DATA_MANIFEST.json`. Review code before trusting any metric.

## Honest ownership discussion
The repository is AI-assisted. A defensible interview explanation identifies which artifacts were generated, which computations can be explained and rerun, which labels remain provisional, and what the author still needs to learn.
