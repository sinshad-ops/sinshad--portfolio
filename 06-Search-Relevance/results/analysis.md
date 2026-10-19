# Results Analysis

## Scope
These numbers are generated from the repository data by `analysis.py`; they are not manually entered.

## Primary interpretation
Rank each query’s four fictional results by TF-IDF-style lexical overlap over query, title, and snippet without using relevance labels.

## Important boundary
Judgments describe a fictional corpus, not live search. Lexical matching misses semantic, domain, locale, freshness, and local-intent nuance.

## Decision use
Metrics identify patterns and prioritize review. They do not replace human adjudication, prove production readiness, or establish the author’s personal accuracy.

## Machine-readable snapshot
```json
{
  "failure_queue": 1,
  "mrr_relevance_gte_2": 0.9833333333333333,
  "ndcg_at_4": 0.9615103376941129,
  "per_intent_ndcg": {
    "informational": 0.9722846845635256,
    "navigational": 0.9987699173624502,
    "transactional": 0.9284536115748047
  },
  "project": "search",
  "query_count": 30,
  "ranking": "TF-IDF-style lexical query/title/snippet overlap; gold relevance is not used for ranking",
  "result_count": 120,
  "scope": "Fictional corpus judgments, not live-search performance; locale and local intent require reviewer context."
}
```
