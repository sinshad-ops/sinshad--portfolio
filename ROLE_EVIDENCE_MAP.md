# Recruiter evidence map

## Best three things to inspect first
1. **BANKING77 real-data experiment:** 13,083 public queries, 77 intents, 85.88% official-test classifier accuracy; leakage audit, source rights, actual error queue.
2. **HH-RLHF public preference study:** 200 human-preference pairs; why length alone cannot replace rubric-based judgment; transparent ties and sampling bias.
3. **Practical batch-QA case study:** measured query-length cohorts, high-confidence errors and an explicit proposed escalation workflow.

| Role direction | Most relevant evidence | What is not claimed |
|---|---|---|
| AI data annotator / quality analyst | BANKING77 schema, references, confusion matrix, review queue, QA case study | Personal annotation score or client delivery |
| AI / LLM evaluator | HH-RLHF preference study + synthetic rubric and disagreement cases | New production-model comparison or factual gold |
| Malayalam–English evaluator | Synthetic translation rubrics, Unicode checks and native-review forms | Completed linguistic validation |
| Multimodal evaluator | 120 rendered scenes, 240 answer records and RGB-pixel baseline | Natural-photo VLM expertise |
| Safety / content reviewer | Synthetic contextual policy cases and triage failures | Employer-specific policy qualification |
| Search evaluator | Fictional query relevance, NDCG/MRR and intent rationale | Live search-engine evaluation |

All implementation is AI-assisted and original datasets are attributed. Portfolio work is not employment history. Eligibility, language requirements and qualification tests remain role-specific.

## Five-minute review
Read the public-data README → inspect REPORT.md → open one prediction/error row → check the source/label origin → run a test suite. See QUALITY_REVIEW_PLAYBOOK.md for the review workflow.
