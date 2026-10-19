# Practical quality-review playbook

This is a proposed/simulated workflow backed by reproducible public-data analyses. It is not a claim of employment or client delivery.

## Daily workflow
Source/version check → schema check → read prompt/context → evaluate output against rubric → label or rank → explain evidence → queue ambiguity → independent sampling → adjudicate → report limitations → owner approval.

## Issue taxonomy
- **Critical:** potential privacy/safety issue or source/identity mismatch. Quarantine and escalate; do not invent a replacement.
- **Major:** wrong intent, unsupported factual assertion, missing required content, meaning-changing translation or visual mismatch.
- **Minor:** readability, formatting or style problem that does not change the core meaning.
- **Ambiguous:** evidence or rubric cannot resolve the choice. Record uncertainty rather than force a confident label.

These are suggested review definitions, not an employer's policy. Company instructions always determine the real task's rules.

## Evidence rules
Reference-label disagreement is not automatically a bad reference label. Human preference is not factual-correctness gold. Unicode validation is not translation quality. Confidence is not accuracy. A procedural image benchmark is not natural-image model performance. A synthetic corruption test is not inter-annotator agreement.

## Audit packet included
- BANKING77 source hashes, official split, 77-label schema, model/reference predictions, confusion matrix and per-intent scores.
- Query-length cohort audit and high-confidence-error counts in the BANKING77 QA case study.
- 535 pending BANKING77 review cases and 200 HH-RLHF review forms.
- HH-RLHF selected human-preference pairs with IDs and original-source attribution; length-proxy failure cases.
- Original synthetic worked cases covering Malayalam, images, safety and search intent.

## Personal reviewer practice — not completed by AI on your behalf
For each case record: source ID, rubric dimension, your decision, supporting evidence, confidence/uncertainty, escalation reason and date. Keep original labels intact. Only mark a review completed after actually doing it. Never claim clients, paid contracts, calibration sessions or production approvals that did not occur.
