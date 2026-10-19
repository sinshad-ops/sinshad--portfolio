# Real-world data upgrade plan

This portfolio currently includes a reproducible synthetic baseline. This file maps each project to a real public dataset or source that can be used for a stronger second experiment. **The current synthetic outputs have not been silently relabeled as real-world results.** Keep both experiments and compare them transparently.

## Dataset mapping

| Project | Suggested source | What it supports | Important caveat |
|---|---|---|---|
| 01 LLM Evaluation | Anthropic HH-RLHF (Hugging Face: `Anthropic/hh-rlhf`) | Human preference comparisons between assistant responses | This is human preference data, not your own customer dataset. Preserve source fields and license/terms. |
| 02 AI Data Annotation | Banking77 (Hugging Face: `PolyAI/banking77`) | Realistic customer-support utterances labelled by intent | Public research data; do not call it data you collected or data from your own customers. Check the dataset card before redistribution. |
| 03 Malayalam / multilingual | Chakravarthi et al., *A Sentiment Analysis Dataset for Code-Mixed Malayalam-English* | Human-labelled Malayalam-English social-media sentiment examples | This is code-mixed sentiment data, not translation quality. Keep it as a separate language QA experiment; do not present sentiment labels as translation judgments. |
| 04 Multimodal | Microsoft COCO captions (or FHIBE for permitted fairness evaluation) | Real images paired with human-written captions, or consented human-centric images for fairness evaluation | COCO usage terms apply. FHIBE requires registration and is evaluation-only; it must not be used for general training. |
| 05 Safety / quality | Civil Comments / Jigsaw toxicity dataset | Real online comments with crowd-labelled toxicity-related labels | Toxicity labels are imperfect and can encode annotator bias. Avoid claiming this is a complete safety policy benchmark. |
| 06 Search relevance | MS MARCO | Real search queries, passages, and relevance labels for ranking experiments | Use the official data and respect its terms; don't claim it represents a live commercial search engine. |

## Verified source links

- Anthropic HH-RLHF: https://huggingface.co/datasets/Anthropic/hh-rlhf
- Banking77: https://huggingface.co/datasets/PolyAI/banking77
- Malayalam-English code-mixed sentiment: https://zenodo.org/records/4015234
- Research overview for the Malayalam-English corpus: https://aclanthology.org/anthology-files/pdf/humeval/2024.humeval-1.pdf
- Microsoft COCO: https://cocodataset.org/
- Civil Comments: https://huggingface.co/datasets/google/civil_comments
- MS MARCO: https://microsoft.github.io/msmarco/
- FHIBE (consent-driven fairness evaluation images): https://fairnessbenchmark.ai.sony/

## How to make the upgrade defensible

1. Download each source from its official host and retain the dataset card, license, version/date, and original citation.
2. Keep an immutable copy of the raw source data separate from cleaned/derived files. Do not commit large or restricted datasets to GitHub; commit scripts and a small permitted sample instead.
3. Write a transformation script that maps source fields to the project schema. Log row counts before/after filtering and missing values.
4. Create a held-out split before developing heuristics. Avoid evaluating on examples used to tune rules.
5. Add a `source`, `source_record_id`, and `label_origin` field to every derived record. `label_origin` should distinguish `published_human_annotation`, `my_manual_review`, `model_output`, and `synthetic_example`.
6. Personally review a documented sample. Record the sample size, review date, decisions, disagreements, and limitations. Do not claim independent human validation unless it happened.
7. Recompute all metrics from the downloaded data. Replace the summary numbers only after the pipeline actually runs; never copy example or previous synthetic metrics into the real-data report.
8. Include a provenance note such as: “I used a publicly released dataset, built the preprocessing/evaluation pipeline, and independently analyzed the results. The original annotations were supplied by the dataset authors.”

## Recommended project order

Start with Banking77 (small and straightforward), then Malayalam-English sentiment, then HH-RLHF and Civil Comments. MS MARCO and COCO are larger and need more careful sampling/storage planning. Use FHIBE only if you specifically want fairness evaluation and agree to its access terms.

<!-- BANKING77:START -->
## Implemented status

BANKING77 is now downloaded from a pinned original revision, hash-verified and evaluated. See `02-AI-Data-Annotation/experiments/banking77/README.md`. The other proposed datasets remain a roadmap and have not been imported or evaluated. Existing synthetic data/results are preserved; no synthetic example has been relabeled as real.

<!-- BANKING77:END -->
