# Guidelines — Search Relevance Evaluation

## Workflow
- Confirm record ID and source completeness.
- Read the source and candidate output.
- Apply the rubric without consulting unrelated cases.
- Capture explicit evidence, not intuition alone.
- Run or inspect automated QC.
- Choose a decision and reason.
- Route unresolved cases to `results/review_queue.csv`.

## Frozen baseline rule
Baseline dictionaries and thresholds are documented in root `analysis.py`. Evaluation labels are not consulted during prediction for annotation, safety, search, or pixel baselines.

## Human review status
No completed human validation is represented. Empty reviewer templates are intentional. Do not backfill ratings from provisional AI labels.

## Query-intent and relevance rules

Determine intent and locale before reading scores. Navigational = reach a particular entity/resource; informational = answer a question; transactional = perform an action; local = find a location-constrained option. A generated brief does not guarantee that each intent is represented; inspect actual counts.

Relevance 3 = directly satisfies dominant intent and key locale/constraints; 2 = genuinely useful partial match; 1 = weak/tangential match or substantial constraint failure; 0 = irrelevant/misleading. Keyword overlap alone cannot justify 3. Inspect semantic match, entity ambiguity, freshness and location. Trustworthiness cannot be independently verified for this fictional corpus; do not assign real-domain credibility.

Rank without reference labels. NDCG@4 compares discounted gain 2^rel−1 to ideal ordering, discount log2(rank+1). MRR uses the first result with relevance>=2. Preserve ties with stable input-order tie-breaking. Review score<0.8 cases and inspect keyword-heavy false matches even if aggregate scores are high. The 4-result sets are simulations, not live search results.
