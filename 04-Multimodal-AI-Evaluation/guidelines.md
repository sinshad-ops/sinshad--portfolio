# Guidelines — Synthetic Visual Evaluation

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

## Visual evidence rules

Open the PNG and question, not only scene metadata. Count visible colored objects; exclude panels, outlines and labels. Color frequency means object count, not pixel area. For equal color counts, choose the color of the leftmost object; the current baseline's column-first scan has a documented tie limitation on multi-row scenes. Bar-height questions compare vertical extent, not color brightness. Spatial questions compare the specified object centers/positions. Absence requires inspecting the full central panel.

Check the answer against rendered evidence and classify count, color, spatial, chart, absence or grounding errors. The paired faulty response is deliberately constructed, not a captured VLM output.

Ground truth comes from rendering geometry. Pixel predictions read image pixels and fixed palette/coordinates only; abstain for unsupported question types. Report accuracy conditional on eligible questions AND coverage. Never count an abstention as a correct answer or claim natural-image performance. All 120 PNGs must have unique pixel content and correct dimensions.
