# Guidelines — Malayalam Translation Evaluation

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

## Native-speaker review rubric

Meaning preservation: verify every actor, action, negation, condition, time, number and obligation. Grammar: morphology, agreement and sentence formation. Naturalness: idiomatic Malayalam rather than literal English order. Register/context: audience-appropriate politeness and locally suitable terminology; accept legitimate regional variants.

Score each dimension 1–5: 5 no material issue; 4 minor localized problem; 3 important repair needed; 2 multiple major failures; 1 unusable or meaning reversed. Tag omission, meaning_shift, register, number_error or negation_error; none means no seeded defect, not independently verified correctness.

Review English source, both candidates, and reference Malayalam. Write rationale in English with the exact Malayalam span and proposed correction. Two fluent alternatives may tie. If neither preserves meaning, neither should be accepted merely because one sounds smoother. Escalate ambiguity in the source.

Script/NFC/digit checks are integrity flags only. Numbers spelled in Malayalam may legitimately lack ASCII digits. The first native review should hide provisional preferences; do not copy them into blank reviewer forms.
