# Findings and decision implications

The lexical triage baseline achieves 42.0% agreement and macro-F1 0.250 against provisional project-owned safety decisions. There are 15 missed escalations and 0 unnecessary escalations.

Risk words in a prompt do not establish that a response is unsafe: refusals, education and benign requests require contextual judgment. Conversely, a harmful implication can avoid trigger words. The score is not a safety certification. Missed escalations get review priority; over-refusal and reviewer cost must also be tracked. A revised classifier needs a fresh held-out set, not tuning on all 100 cases.

## Next validation step
Blind human review of the source evidence, followed by adjudication and a new unseen benchmark.
