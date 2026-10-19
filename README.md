# Sinshad P. S. — AI Training & Data Quality Portfolio

**[View my chosen one-page resume (PDF)](resume.pdf)** · [LinkedIn](https://www.linkedin.com/in/sinshad-ps-587677418/) · [Portfolio files](https://github.com/sinshad-ops/sinshad--portfolio)

B.Tech Computer Science student (expected 2027), Malayalam–English language-data contributor, and AI evaluation portfolio builder. This repository brings together practical examples of response evaluation, annotation QA, multilingual integrity checks, and reproducible error analysis.

## Quick evidence

- **BANKING77:** 10,003 official training queries, 3,080 test queries, 77 intents. A word uni/bi-gram Naive Bayes baseline reached **85.88% accuracy** and **0.8579 macro-F1** against the dataset’s published labels. Seven training-overlap test texts were identified; accuracy excluding them was **85.84%**. The 535-row queue is for follow-up review. These are classifier results, not a personal annotation-accuracy score. Labels and source data are attributed to Casanueva et al. / PolyAI, CC BY 4.0. [Method and results](02-AI-Data-Annotation/experiments/banking77/README.md).
- **HH-RLHF:** 200 curated preference pairs / 400 original answers with source-published preferences. A longer-answer proxy matched 117/195 non-tied preferences (60%); the result demonstrates the proxy’s limits, not model quality or personal evaluator accuracy. [Method and results](01-LLM-Evaluation/experiments/hh-preference/README.md).
- **Six synthetic demonstrations:** LLM response comparison, annotation QA, Malayalam checks, controlled-image evaluation, safety triage, and fictional search relevance. Their synthetic labels and limitations are disclosed in the project reports.

## Start here

1. Read [BANKING77 methodology](02-AI-Data-Annotation/experiments/banking77/README.md) and [measured report](02-AI-Data-Annotation/experiments/banking77/results/REPORT.md).
2. Review the [HH-RLHF study](01-LLM-Evaluation/experiments/hh-preference/README.md).
3. Browse the six clearly identified synthetic project READMEs.
4. See the [recruiter guide](recruiter-guide.md), [review playbook](QUALITY_REVIEW_PLAYBOOK.md), and [interview prep](INTERVIEW_PREP.md).

## Reproduce

Python 3.10+. From the repository root:

```bash
python -m pip install -r requirements.txt
python analysis.py --project all
python -m unittest discover -s tests -v
python 02-AI-Data-Annotation/experiments/banking77/run_experiment.py
python -m unittest discover -s 02-AI-Data-Annotation/experiments/banking77/tests -v
python 01-LLM-Evaluation/experiments/hh-preference/run_experiment.py
python -m unittest discover -s 01-LLM-Evaluation/experiments/hh-preference/tests -v
```

The public-data studies are source-pinned and reproducible. The CI workflow runs the three test suites on Python 3.10–3.13; check the repository’s **Actions** tab for live results.

## Scope and disclosure

The portfolio was developed with AI assistance. Two studies use public datasets and their authors’ labels; six demonstrations use synthetic data. Project metrics report the automated baselines documented in the corresponding experiment reports. Synthetic labels are not ground truth, Malayalam linguistic judgments still need qualified review, and no production certification or client deliverable is claimed. See [provenance](PROVENANCE.md), [data licenses](DATA_LICENSE.md), and [final validation](FINAL_VALIDATION.md).

The resume linked above is the user-selected PDF, published unchanged. The BANKING77 pipeline documents automated classification and retains blank reviewer fields; any claim of personal manual review in the resume is not independently evidenced by this repository.

## Contact

Email: [sinshadsirajudheenpriv@gmail.com](mailto:sinshadsirajudheenpriv@gmail.com) · [LinkedIn](https://www.linkedin.com/in/sinshad-ps-587677418/) · [GitHub](https://github.com/sinshad-ops)

See [LICENSE](LICENSE) and [DATA_LICENSE.md](DATA_LICENSE.md) for terms.
