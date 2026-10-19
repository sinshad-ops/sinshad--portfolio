# Methodology — Search Relevance Evaluation

## Design
Rank each query’s four fictional results by TF-IDF-style lexical overlap over query, title, and snippet without using relevance labels.

## Computation
NDCG@4 uses gain 2^relevance−1 and log2 rank discount. MRR uses the first result with relevance ≥2.

## Reproducibility
The build uses seed `20261008`, stable ID order, local files, deterministic drawing, and JSON metrics. Re-running root `analysis.py` recreates metrics, queues, and charts.

## QA controls
Schema checks, unique-ID checks, label-range checks, image pixel checks, entity span validation, deterministic reproduction tests, and output-consistency tests are run automatically.

## Interpretation boundary
Judgments describe a fictional corpus, not live search. Lexical matching misses semantic, domain, locale, freshness, and local-intent nuance.
