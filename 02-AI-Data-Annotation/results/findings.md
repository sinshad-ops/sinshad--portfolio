# Findings and decision implications

On the 30-record held-out partition, the frozen keyword baseline achieves topic accuracy 76.7%, sentiment accuracy 40.0%, and urgency accuracy 43.3%. This uneven performance shows why annotation requires meaning-level review rather than keyword matching.

Exact entity-span F1 is 0.000 on holdout. The extractor only recognizes limited order/date formats, not PRODUCT or ORG names; unsupported entity classes are not silently excluded from the denominator. The weak result is intentional evidence of baseline scope, not an annotation-quality claim.

29 records enter the structural/ambiguity review queue, and 2 records have span warnings. The simulated second-label exercise injects 13 known topic corruptions; its agreement statistic is a simulation, not human inter-annotator agreement. Calibration/holdout is a fixed order split, not random population sampling; no dictionaries were tuned on held-out labels during this run.

## Next validation step
Blind human review of the source evidence, followed by adjudication and a new unseen benchmark.
