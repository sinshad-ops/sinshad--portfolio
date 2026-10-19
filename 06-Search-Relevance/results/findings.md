# Findings and decision implications

Across 30 fictional query sets (120 judged results), lexical ranking achieves NDCG@4 0.962 and MRR 0.983. The review queue contains 1 cases below NDCG 0.8.

These scores are likely optimistic because the synthetic snippets often repeat query terms and each query has only four candidate results. They are not search-engine performance. Evaluate synonym-heavy queries, ambiguous intent, misleading keyword overlap, locale mismatch and stale-but-on-topic results on a new collection before making stronger claims. Intended local coverage must be checked from the actual intent counts, not assumed from the generation brief.

## Next validation step
Blind human review of the source evidence, followed by adjudication and a new unseen benchmark.
