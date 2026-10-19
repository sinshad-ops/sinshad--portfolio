# Start here

This is a practice portfolio for remote AI generalist, response-evaluation, annotation, content-quality and search-evaluation work. It includes six AI-assisted synthetic demonstrations and two studies based on public datasets. It is not employment history.

## A short review path

1. Read the [main README](README.md) for scope and limitations.
2. Open the [BANKING77 study](02-AI-Data-Annotation/experiments/banking77/README.md) and its report.
3. Open the [HH-RLHF study](01-LLM-Evaluation/experiments/hh-preference/README.md) and check what the length baseline can and cannot tell us.
4. Pick one synthetic project and inspect its examples, rubric and review queue.
5. Run the relevant script and tests before discussing the implementation in an interview.

## Reproduce the portfolio checks

```bash
python -m pip install -r requirements.txt
python reproduce_all.py
python verify_final.py
```

The packaged validation report records the checks run when this version was assembled. That is not a substitute for running the code on your own machine. The GitHub Actions workflow has not been run on GitHub as part of this package.

## Before publishing

Check every link, read the files you plan to discuss, and complete the [personal review workbook](PERSONAL-WORKBOOK.md) with your real observations. Keep the synthetic-data and AI-assistance disclosures visible. Do not describe practice examples as client work or claim human validation that has not happened.
