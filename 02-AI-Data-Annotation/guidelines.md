# Guidelines — Multi-task AI Data Annotation

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

## Label definitions

One primary topic: billing = charge/payment/invoice dispute; account = authentication or profile access; delivery = shipment status or arrival; technical = malfunction of an app/device/site; refund = explicit request to return money or reverse purchase; general = other or no actionable category. Multi-intent: prioritize the explicitly requested resolution, not the first keyword. When two requests have equal priority, flag ambiguity and record the chosen primary request.

Sentiment: positive = praise/satisfaction; negative = dissatisfaction/complaint; neutral = factual request without clear affect; mixed = substantive positive AND negative judgments. Courtesy words alone do not force positive. Negation must be read (not happy is negative).

Urgency: high = immediate time-critical loss/access/safety consequence, explicit immediate deadline; medium = a stated delay, issue or near-term dependency without immediate serious consequence; low = routine information or no urgency evidence. Do not infer high urgency from complaint intensity alone. Borderline cases need rationale.

Entity tags: ORDER_ID = order reference, PRODUCT = named product/service, DATE = date/time phrase, ORG = organization. Use exact Unicode substring offsets, start inclusive/end exclusive; no punctuation not part of the name. Annotate each occurrence separately. Repeated-text provisional references currently use the first occurrence and are flagged; this is a known pending adjudication issue. Unknown or absent substrings are quarantined. No inferred entities.

Blind the reviewer to provisional labels before independent annotation. Audit schemas/spans, compare decisions, document disagreements and adjudicate before establishing human gold. The controlled corruption exercise is not human IAA. The fixed 70/30 split was not randomized, and cannot establish population-level accuracy.
