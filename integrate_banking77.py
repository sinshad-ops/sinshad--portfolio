"""Integrate the real-data experiment without altering synthetic datasets or scores."""
from pathlib import Path
import base64,csv,html,json,re
ROOT=Path(__file__).resolve().parent
EXP=ROOT/'02-AI-Data-Annotation/experiments/banking77'
REL='02-AI-Data-Annotation/experiments/banking77'
START='<!-- BANKING77:START -->';END='<!-- BANKING77:END -->'
def add(path,block):
    text=path.read_text(encoding='utf-8') if path.exists() else ''
    text=re.sub(re.escape(START)+r'.*?'+re.escape(END),'',text,flags=re.S).rstrip()
    path.write_text(text+'\n\n'+START+'\n'+block+'\n'+END+'\n',encoding='utf-8')
def run():
    m=json.loads((EXP/'results/metrics.json').read_text(encoding='utf-8'))
    config=json.loads((EXP/'results/config.json').read_text(encoding='utf-8'))
    p=m['published_test_metrics'];clean=m['train_text_disjoint_test_metrics']
    brief=f'''## Completed real-data experiment: BANKING77

The six original projects remain **synthetic baselines**. An additional real public-data experiment now evaluates a classifier on **10,003 official training queries / 3,080 test queries / 77 intents**. Original annotations are attributed to Casanueva et al. / PolyAI under CC BY 4.0; no personal annotation claim is made.

| Official test result | Value |
|---|---:|
| Multinomial Naive Bayes accuracy | {p['accuracy']:.2%} ({p['correct']}/{p['n']}) |
| Macro-F1 (77 intents) | {p['macro_f1']:.4f} |
| Top-3 accuracy | {p['top3_accuracy']:.2%} |
| Majority baseline accuracy | {m['majority_baseline']['accuracy']:.2%} |
| Accuracy after excluding 7 train-overlap test queries | {clean['accuracy']:.2%} |
| Pending automated review queue | {m['review_queue_rows']} cases |

Alpha={config['selected_alpha']} was selected using training-derived validation, not the test set. These are measured **classifier results against published labels**, not the portfolio owner's personal accuracy. All human-review fields remain blank.

- [Experiment and reproduction]({REL}/README.md)
- [Actual results, limitations and examples]({REL}/results/REPORT.md)
- [Source hashes and license]({REL}/source/source-manifest.json)
- [10 experiment tests]({REL}/tests/test_banking77.py)

```bash
python {REL}/run_experiment.py
python -m unittest discover -s {REL}/tests -v
```
'''
    root=ROOT/'README.md';text=root.read_text(encoding='utf-8')
    text=text.replace('The datasets and reference labels are synthetic and the work was developed with AI assistance.','The six original baseline datasets and reference labels are synthetic. The added BANKING77 experiment uses public data and its original published annotations. The portfolio was developed with AI assistance.')
    root.write_text(text,encoding='utf-8');add(root,brief)
    overview = root.read_text(encoding="utf-8")
    block = re.search(re.escape(START) + r".*?" + re.escape(END), overview, flags=re.S)
    if block and "## Start here" in overview:
        featured = block.group(0)
        overview = overview[:block.start()] + overview[block.end():]
        overview = overview.replace("## Start here", featured + "\n\n## Start here", 1)
        root.write_text(overview.strip()+"\n", encoding="utf-8")
    project=ROOT/'02-AI-Data-Annotation/README.md'
    add(project,brief.replace(REL+'/','experiments/banking77/').replace('python '+REL,'python experiments/banking77'))
    for filename in ['EVIDENCE_BRIEF.md','recruiter-guide.md']:
        add(ROOT/filename,brief)
    add(ROOT/'PROVENANCE.md','''## BANKING77 exception to the synthetic-data scope

The additional BANKING77 experiment uses original public English banking queries and published annotations. Data creators: Iñigo Casanueva, Tadas Temcinas, Daniela Gerz, Matthew Henderson and Ivan Vulić / PolyAI, 2020. Official revision `57ec275d8078af65b7731c2a98be812d844a6d6b`; license CC BY 4.0. Source files, hashes, original README, full license and transformation details are retained in the experiment. Derived IDs and classifier outputs are new; source text and categories are unchanged. No personal human annotation or endorsement is claimed. The rest of the original benchmark suite remains synthetic.
''')
    add(ROOT/'DATA_LICENSE.md','''## Third-party BANKING77 data

`02-AI-Data-Annotation/experiments/banking77/data/raw/` and data-derived text/reference annotations are BANKING77 by Casanueva et al. / PolyAI, licensed CC BY 4.0, not original data created by Sinshad PS. Attribution, source, license and modifications are documented in the experiment README. Preserve these notices and upstream disclaimer when redistributing; no endorsement is implied. Newly written pipeline code is covered by the portfolio code license.
''')
    add(ROOT/'REAL_WORLD_DATA_UPGRADE.md','''## Implemented status

BANKING77 is now downloaded from a pinned original revision, hash-verified and evaluated. See `02-AI-Data-Annotation/experiments/banking77/README.md`. The other proposed datasets remain a roadmap and have not been imported or evaluated. Existing synthetic data/results are preserved; no synthetic example has been relabeled as real.
''')
    add(ROOT/'real_world_data/README.md',f'BANKING77 is implemented in [`../{REL}/README.md`](../{REL}/README.md). Raw/derived data are attributed to original authors and separated from synthetic examples. Other sources are proposals only.')
    registry=ROOT/'real_world_data_sources.json'
    reg=json.loads(registry.read_text(encoding='utf-8'))
    reg['note']='BANKING77 experiment is completed; other sources remain proposals. Original synthetic datasets/results remain separate.'
    for source in reg['sources']:
        if source['name']=='Banking77':source.update({'status':'downloaded_and_evaluated','revision':m['source_revision'],'verified_license':'CC-BY-4.0','experiment_path':REL})
    registry.write_text(json.dumps(reg,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    add(ROOT/'career/LinkedIn.md',f'''## Additional project draft: BANKING77 intent classification & label QA

AI-assisted public-data experiment using BANKING77: 10,003 training queries, 3,080 official test queries and 77 banking intents. Implemented a reproducible unigram/bigram Naive Bayes baseline with training-only alpha selection, hash-verified ingestion, confusion analysis and duplicate/leakage checks. Measured classifier accuracy {p['accuracy']:.2%} and macro-F1 {p['macro_f1']:.4f}; after excluding seven train-overlap test texts, accuracy {clean['accuracy']:.2%}. Original queries/annotations credited to Casanueva et al. / PolyAI (CC BY 4.0). No personal annotation-quality claim.

Draft only; not posted to LinkedIn.
''')
    add(ROOT/'career/application-kit.md',f'''## Updated evidence talking point

My AI-assisted portfolio now includes a real BANKING77 experiment alongside the synthetic baselines: pinned public-source ingestion, 77-intent classification, training-only parameter selection, {p['accuracy']:.2%} official-test classifier accuracy, per-intent errors and a review queue. The original dataset authors supplied the labels. I do not claim I personally annotated these queries. Use only when you can explain and reproduce this work yourself.
''')
    add(ROOT/'CHANGELOG.md','''## 2026-10-09 — Banking77 real-data release

Added official-source hash-verified ingestion; 77-intent NB experiment; group-aware training validation; majority baseline; official and train-text-disjoint test scores; source QA; confusion matrix; 535-case unadjudicated review queue; chart; notebook; 10 unit tests; source license and attribution. Kept original synthetic datasets and numerical results unchanged. No external publication.
''')
    (EXP/'source/ATTRIBUTION.md').write_text('''# Attribution and source license

BANKING77: Iñigo Casanueva, Tadas Temcinas, Daniela Gerz, Matthew Henderson and Ivan Vulić / PolyAI. *Efficient Intent Detection with Dual Sentence Encoders*, 2nd Workshop on NLP for ConvAI, ACL 2020.

Original: https://github.com/PolyAI-LDN/task-specific-datasets
Paper: https://arxiv.org/abs/2003.04807
License: CC BY 4.0, https://creativecommons.org/licenses/by/4.0/

No changes to source queries or categories. Derived JSONL adds record IDs/provenance; code normalizes input for features; predictions and metrics are new. Labels are not personally annotated by the portfolio owner. Upstream warranty disclaimer retained in BANKING77_LICENSE.txt. No PolyAI affiliation or endorsement is implied.
''',encoding='utf-8')
    (EXP/'source/CITATION.bib').write_text('''@inproceedings{Casanueva2020,
 author={Iñigo Casanueva and Tadas Temcinas and Daniela Gerz and Matthew Henderson and Ivan Vulić},
 title={Efficient Intent Detection with Dual Sentence Encoders},
 booktitle={Proceedings of the 2nd Workshop on NLP for ConvAI - ACL 2020},
 year={2020}, url={https://arxiv.org/abs/2003.04807},
 note={BANKING77 data: https://github.com/PolyAI-LDN/task-specific-datasets}
}
''',encoding='utf-8')
    page=ROOT/'website/index.html';text=page.read_text(encoding='utf-8')
    text=re.sub(re.escape(START)+r'.*?'+re.escape(END),'',text,flags=re.S)
    image='data:image/png;base64,'+base64.b64encode((EXP/'results/benchmark.png').read_bytes()).decode('ascii')
    section=f'''{START}<section><div class="eyebrow">Completed public-data experiment</div><h2>BANKING77: real queries, published labels.</h2><p class="lead">13,083 original queries · 77 English banking intents · CC BY 4.0 · Casanueva et al. / PolyAI. Separate from the six synthetic baselines below.</p><div class="grid"><article class="card"><span class="badge">Official 3,080-query test split</span><h2>Intent classification &amp; label QA</h2><p class="metric">{p['accuracy']:.2%} classifier accuracy · {p['macro_f1']:.4f} macro-F1</p><p>Training-only parameter selection. Seven overlapping test texts flagged; disjoint-test accuracy {clean['accuracy']:.2%}. {m['review_queue_rows']} cases await review. Original labels are not personal annotations.</p><a href="../{REL}/README.md">Source, license &amp; reproduction</a> · <a href="../{REL}/results/REPORT.md">Actual results</a><img src="{image}" alt="Computed BANKING77 results"></article><article class="card"><h2>What the evidence establishes</h2><p>Hash-verified public-source ingestion, published-label validation, simple lexical modeling, leakage audit, measured per-intent performance and explicit failure queues.</p><h2>What it does not establish</h2><p>Personal annotation accuracy, production readiness, financial expertise, Malayalam performance or completed human adjudication. This implementation is AI-assisted.</p></article></div></section>{END}'''
    text=text.replace('<main>','<main>'+section,1)
    text=text.replace('six AI-assisted synthetic personal projects with computed metrics','six AI-assisted synthetic baseline projects plus a completed public BANKING77 experiment, with computed metrics')
    text=text.replace('Provisional AI/synthetic labels are not human gold.','Original projects use provisional AI/synthetic labels; BANKING77 uses its published reference annotations. Neither is a personal human-performance claim.')
    page.write_text(text,encoding='utf-8')
    readme=(ROOT/'README.md').read_text(encoding='utf-8')
    assert 'BANKING77' in readme and '85.88%' in readme
    print('Integrated real-data evidence; synthetic data and original metric values not edited.')

if __name__=='__main__':run()
