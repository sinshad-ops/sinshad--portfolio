# Public preference benchmark — actual results

200 pairs / 400 responses selected from 2354 original test records; 304 passed the predeclared lexical/topic rules.

| Baseline | Covered pairs | Agreement on covered | Ties |
|---|---:|---:|---:|
| seeded_coin | 200 | 50.50% | 0 |
| longer_response | 195 | 60.00% | 5 |
| shorter_response | 195 | 40.00% | 5 |

## Conclusions and boundaries
- Longer is not necessarily more helpful. A response-length proxy ignores accuracy, instruction following, tone, omissions and context.
- Preferences were supplied by the original dataset, not personally labeled by Sinshad PS.
- The educational-topic and risk-word filters intentionally bias this sample. Do not generalize these rates to the full dataset.
- This benchmark does not produce new model outputs or validate a production LLM. It is a preference-analysis and evaluator-workflow demonstration.
- Equal-length ties are abstentions; covered and all-pair rates are both reported.
- Lexical filtering is not human safety certification. The full source can contain offensive material; it is not bundled.
- Review forms remain blank. Published preferences are subjective and are not factual-correctness gold.

## Reproduction
`python run_experiment.py` reanalyzes the hash-verified bundled sample offline. `python run_experiment.py --download` reconstructs it from the pinned official gzip source.

## Source
Anthropic HH-RLHF, MIT license. Original source and terms are retained under `source/`. See experiment README for attribution.
