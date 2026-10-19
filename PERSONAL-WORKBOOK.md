# Personal review workbook — complete this yourself before publishing

This file is a working checklist, not a claim that the reviews have already happened. Add notes only after you have inspected the examples and run the code yourself. Keep the synthetic-data and AI-assistance disclosure in the public README.

## A repeatable review session

1. Run the project's analysis command from the repository root.
2. Open at least 10 examples, including several failures or review-queue entries.
3. Write down what the current label/rule says and what you think after inspecting the evidence.
4. If you disagree, record why. Do not overwrite the original reference silently.
5. If you change code or labels, rerun the analysis and tests and describe what changed.
6. Practise explaining one metric and one failure without reading the README.

## Record your actual work

Copy this section once per project after you have completed a review. Leave it blank until then.

### Project: [name]
- Date reviewed:
- Number of cases I personally inspected:
- One example I agreed with and why:
- One example I disagreed with and why:
- Error or limitation I discovered:
- Change I made (file and reason), if any:
- Test/analysis command rerun:
- What I can now explain confidently:
- What still needs an expert or native-speaker review:

## Project-specific review checklist

- [ ] **LLM pairwise:** inspect a tie, a disagreement, and a high-scoring response. Explain the rubric weights and why agreement is not accuracy.
- [ ] **Annotation:** inspect one topic error, one sentiment error, one urgency error, and one entity-span failure. Explain the fixed holdout split.
- [ ] **Malayalam:** ask a qualified native speaker to review examples if available. Do not treat Unicode checks as translation-quality judgments.
- [ ] **Visual:** inspect the PNG and corresponding question/answer. Explain what the pixel baseline supports and why it abstains on other tasks.
- [ ] **Safety triage:** inspect missed escalations and benign examples containing risk words. Explain false negatives and false positives.
- [ ] **Search relevance:** calculate one query's ranking by hand and inspect a misleading keyword-overlap case.

## Before adding this to a CV or LinkedIn

- [ ] I have run the project locally and can show it working.
- [ ] I can explain the important functions in the code I claim to understand.
- [ ] I can explain what each reported metric measures and what it does not measure.
- [ ] I have not described synthetic data as client or production data.
- [ ] I have not claimed human validation unless it actually happened and is documented.
- [ ] My public description reflects my real contribution and retains the AI-assistance disclosure.
