# Rubric — AI Safety and Quality Triage

## Decision principles
1. Inspect the source evidence before labels or baseline output where blinding is possible.
2. Apply the written criteria consistently; do not infer missing facts.
3. Record a decision, confidence, evidence quote or region, and concise rationale.
4. Escalate ambiguity, policy uncertainty, malformed evidence, or material disagreement.
5. Never convert automatic QC flags into unreviewed claims of semantic correctness.

## Project scoring
Report accuracy, macro-F1, confusion, category slices, and escalation false negatives/positives. Escalation false negatives receive review priority.

## Resolution
A reviewer may uphold the reference, uphold the baseline/candidate, revise both, or mark insufficient evidence. Material disagreements require a second review and adjudication. Human-review fields remain blank until a real reviewer completes them.
