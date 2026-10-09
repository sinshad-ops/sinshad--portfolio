# AI Evaluation & Data Quality Portfolio — Sinshad PS

<!-- REAL_EVIDENCE:START -->
## Second completed public-data study: human preference analysis

**200 HH-RLHF pairs / 400 original candidate responses**, with source-published human preferences, a pinned official revision, MIT notice and documented sampling rules. A longer-response proxy agrees on **117/195 non-tied pairs (60%)**, with five ties. The deterministic coin baseline is **50.5%**. This shows the limits of superficial ranking proxies—not personal evaluator accuracy or production-model quality.

- [Source, methodology and reproduction](01-LLM-Evaluation/experiments/hh-preference/README.md)
- [Actual results and bias limits](01-LLM-Evaluation/experiments/hh-preference/results/REPORT.md)
- [Operational BANKING77 audit](02-AI-Data-Annotation/experiments/banking77/results/QA_CASE_STUDY.md)
- [Practical review playbook](QUALITY_REVIEW_PLAYBOOK.md)

The portfolio contains **two real public-data studies plus six synthetic baseline demonstrations**. The original authors supplied public labels; personal review fields remain blank.

<!-- REAL_EVIDENCE:END -->



I am a Computer Science Engineering student (expected graduation: 2027) exploring practical work in AI response evaluation, data annotation, multilingual QA, multimodal checks, content quality, and search relevance.

This repository is my **learning portfolio**. The six original baseline datasets and reference labels are synthetic. The added BANKING77 experiment uses public data and its original published annotations. The portfolio was developed with AI assistance. I have not presented it as client work or a production evaluation study. I am using it to practise building reproducible workflows, inspecting errors, and understanding where automated checks are not enough.

<!-- BANKING77:START -->
## Completed real-data experiment: BANKING77

The six original projects remain **synthetic baselines**. An additional real public-data experiment now evaluates a classifier on **10,003 official training queries / 3,080 test queries / 77 intents**. Original annotations are attributed to Casanueva et al. / PolyAI under CC BY 4.0; no personal annotation claim is made.

| Official test result | Value |
|---|---:|
| Multinomial Naive Bayes accuracy | 85.88% (2645/3080) |
| Macro-F1 (77 intents) | 0.8579 |
| Top-3 accuracy | 95.16% |
| Majority baseline accuracy | 1.30% |
| Accuracy after excluding 7 train-overlap test queries | 85.84% |
| Pending automated review queue | 535 cases |

Alpha=0.1 was selected using training-derived validation, not the test set. These are measured **classifier results against published labels**, not the portfolio owner's personal accuracy. All human-review fields remain blank.

- [Experiment and reproduction](02-AI-Data-Annotation/experiments/banking77/README.md)
- [Actual results, limitations and examples](02-AI-Data-Annotation/experiments/banking77/results/REPORT.md)
- [Source hashes and license](02-AI-Data-Annotation/experiments/banking77/source/source-manifest.json)
- [10 experiment tests](02-AI-Data-Annotation/experiments/banking77/tests/test_banking77.py)

```bash
python 02-AI-Data-Annotation/experiments/banking77/run_experiment.py
python -m unittest discover -s 02-AI-Data-Annotation/experiments/banking77/tests -v
```

<!-- BANKING77:END -->

## Start here

**Recruiter shortcut:** Begin with the [BANKING77 public-data experiment](02-AI-Data-Annotation/experiments/banking77/README.md), then choose one of the six clearly labelled synthetic demonstrations below. The [recruiter guide](recruiter-guide.md) provides a five-minute review path. The [website](website/index.html) is a static page. A root `index.html` is included for straightforward GitHub Pages setup; follow [`WEBSITE_DEPLOYMENT.md`](WEBSITE_DEPLOYMENT.md) after pushing the repository.


If you are reviewing this portfolio, I recommend starting with one project README, then opening its `results/analysis.md`, `results/review_queue.csv`, and `qa/worked-cases.md`. These show the method, the output, and the cases that still need human judgment.

| Project | What I practised | Current result (synthetic benchmark only) |
|---|---|---|
| [LLM Pairwise Evaluation](01-LLM-Evaluation/) | Comparing two responses with a rubric and retaining disagreements for review | 45/50 agreement with provisional AI-authored preferences; not human accuracy |
| [Data Annotation QA](02-AI-Data-Annotation/) | Topic, sentiment, urgency, entity spans, and a simple keyword baseline | 76.7% holdout topic accuracy; sentiment and urgency are weaker |
| [Malayalam Translation Checks](03-Multilingual-AI-Evaluation/) | Unicode/integrity checks and a review workflow for Malayalam candidates | 5 automatic QC flags; not a translation-quality score |
| [Synthetic Visual Evaluation](04-Multimodal-AI-Evaluation/) | Testing a pixel-based baseline on generated geometric images | 90% accuracy on eligible questions at 50% coverage; not a vision-language model evaluation |
| [AI Quality Triage](05-AI-Quality-Evaluation/) | Reviewing a transparent lexical safety-triage baseline and its misses | Macro-F1 0.250; not a safety certification |
| [Search Relevance](06-Search-Relevance/) | Ranking fictional results and calculating NDCG@4 and MRR | NDCG@4 0.962 on a small synthetic corpus; likely optimistic |

## Reproduce the work

Use Python 3.10 or newer. Install the pinned dependencies first:

```bash
python -m pip install -r requirements.txt
```


Requires Python and the dependencies listed in `requirements.txt`.

```bash
python analysis.py --project all
python -m unittest discover -s tests -v
```

The analysis runs locally; no network service is required. See `VALIDATION.md` for the recorded test coverage and `DATA_MANIFEST.json` for file hashes. The GitHub Actions workflow runs all three test suites on Python 3.10–3.13. For website publishing, follow [`WEBSITE_DEPLOYMENT.md`](WEBSITE_DEPLOYMENT.md); the site is not live until you deploy it.

## What the results do—and do not—show

The code computes metrics from the supplied datasets. That makes the calculations reproducible; it does **not** make the synthetic reference labels ground truth. Several labels were generated with AI assistance, the multilingual project still needs a qualified Malayalam review, and the visual project uses artificial scenes. No human inter-annotator study, employer-policy validation, or production certification is claimed.

## My next step

I am working through the review checklist in [`PERSONAL-WORKBOOK.md`](PERSONAL-WORKBOOK.md): checking examples myself, recording real corrections, and noting what I can explain confidently. Blank fields are intentional; I will fill them only after doing the work.

## Contact

- Email: [sinshadsirajudheenpriv@gmail.com](mailto:sinshadsirajudheenpriv@gmail.com)
- LinkedIn: [Sinshad PS](https://www.linkedin.com/in/sinshad-ps-587677418/)
- GitHub: [sinshad-ops](https://github.com/sinshad-ops)

## Licensing

See `LICENSE` and `DATA_LICENSE.md` for code and synthetic-data terms.
