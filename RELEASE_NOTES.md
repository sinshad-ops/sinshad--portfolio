# Completed BANKING77 release

This is the completed real-data upgrade, not only a dataset roadmap. The six existing synthetic projects remain intact; the annotation project adds a separate public BANKING77 experiment.

- Official data: 10,003 train / 3,080 test queries; 77 intents.
- Naive Bayes: 85.88% accuracy; macro-F1 0.8579; top-3 accuracy 95.16%.
- Seven test texts overlap normalized training text; excluding them gives 85.84% accuracy.
- 535 cases await personal adjudication; review fields are intentionally blank.
- CC BY 4.0 verified from the original repository; full source license and attribution included.
- 21 automated tests pass; notebook actually executed; rerun predictions/metrics identical.
- 156 pre-existing source/data files verified byte-identical; all six synthetic metric values unchanged.
- Updated repository overview, website, LinkedIn/application drafts, one-page PDF and editable resume. Old PDF duplicates and caches omitted.

## Reproduce offline

From repository root, after installing requirements:

```bash
python reproduce_all.py
python validate_release.py
```

For just BANKING77:

```bash
python 02-AI-Data-Annotation/experiments/banking77/run_experiment.py
```

Existing `build_portfolio.py` reconstructs the original synthetic scaffolding. If you use it, run `reproduce_all.py` and `update_banking77_career.py` afterward to restore the upgrade integration; rerender the resume PDF if editing its content.

This release is AI-assisted. BANKING77 text and annotations belong to its cited original authors; classifier scores do not measure personal human annotation quality. No external publication has been performed. Only BANKING77 is upgraded to real public data; other proposed sources remain plans.

## Packaging polish

- JSON metrics are now written with explicit LF newlines for stable cross-platform regeneration.
- Removed a stale third-party portfolio URL from the HTML resume; the GitHub profile link remains.
- Added a recruiter shortcut and explicit local-site deployment note to the root README.
- No repository was published, no website was deployed, and no human review was fabricated.

## Final complete edition

Added a second real public-data study (HH-RLHF, 200 preference pairs), batch-QA cohort evidence and review playbook, role evidence map, executable notebook, seven new tests, and an offline website evidence reader. All 28 tests pass locally; two public-data studies rerun deterministically; 156 original synthetic input files and all six original synthetic metric values are preserved. Full release hashes are regenerated when packaging. Source caches and bytecode are excluded. No employment, clients, completed human review or external publication is invented.
