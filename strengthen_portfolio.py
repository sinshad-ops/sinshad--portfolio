from pathlib import Path
from collections import defaultdict
import base64,csv,html,json,re
ROOT=Path(__file__).resolve().parent
BANK=ROOT/'02-AI-Data-Annotation/experiments/banking77'
HH=ROOT/'01-LLM-Evaluation/experiments/hh-preference'

def write(path,text):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text,encoding='utf-8')
def block(path,name,text,first=False):
 s=path.read_text(encoding='utf-8') if path.exists() else ''
 begin=f'<!-- {name}:START -->';end=f'<!-- {name}:END -->'
 s=re.sub(re.escape(begin)+r'.*?'+re.escape(end),'',s,flags=re.S).strip()
 b=begin+'\n'+text+'\n'+end
 if first and '\n\n' in s:head,tail=s.split('\n\n',1);s=head+'\n\n'+b+'\n\n'+tail
 else:s+='\n\n'+b
 write(path,s+'\n')
def run():
 with (BANK/'results/test_predictions.csv').open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
 cohorts=defaultdict(list)
 for row in rows:
  n=len(row['text'].split());bucket='01_short_1_to_7_words' if n<=7 else '02_medium_8_to_15_words' if n<=15 else '03_long_16_plus_words'
  cohorts[bucket].append(row)
 stats=[]
 for key,rs in sorted(cohorts.items()):
  errors=sum(r['predicted_intent']!=r['published_intent'] for r in rs)
  high=sum(float(r['uncalibrated_confidence'])>=.8 for r in rs)
  high_wrong=sum(float(r['uncalibrated_confidence'])>=.8 and r['predicted_intent']!=r['published_intent'] for r in rs)
  stats.append({'cohort':key,'queries':len(rs),'correct':len(rs)-errors,'accuracy':(len(rs)-errors)/len(rs),'high_confidence_predictions':high,'high_confidence_errors':high_wrong})
 target=BANK/'results/cohort_audit.csv'
 with target.open('w',encoding='utf-8',newline='') as f:w=csv.DictWriter(f,fieldnames=list(stats[0]));w.writeheader();w.writerows(stats)
 assert sum(r['queries'] for r in stats)==3080
 audit=['# Reference-labelled batch QA audit','',
  'Actual analysis of the BANKING77 official-test predictions. This is a portfolio simulation of a labelled audit workflow, not client work or a released production batch.','',
  '| Query-length cohort | Queries | Accuracy | High-confidence errors |','|---|---:|---:|---:|']
 audit += [f"| {r['cohort']} | {r['queries']} | {r['accuracy']:.2%} | {r['high_confidence_errors']} |" for r in stats]
 audit+=['','## Operational interpretation',
  '- A schema pass is not a semantic quality pass. Published-label disagreement and confidence are distinct signals.',
  '- High-confidence errors occur; the Naive Bayes probability is not calibrated and must not be used as a quality guarantee.',
  '- Disagreement detection here requires published reference labels. For unseen production data, those labels may not exist; use independent sampled review rather than claiming this audit catches all errors.',
  '- Query length is a descriptive cohort, not a protected demographic attribute or proof of fairness.',
  '- The original 535-case queue is not adjudicated; no batch approval or personal review is claimed.','',
  '## Proposed workflow (not represented as previously performed)',
  '1. Verify source hashes and label schema. Quarantine invalid rows instead of guessing labels.',
  '2. Preserve published references and raw text; log new model outputs separately.',
  '3. Route labelled disagreements and low-confidence cases to review. Check high-confidence predictions by random sampling as well.',
  '4. Record reviewer decision, evidence and reason; escalate ambiguous cases to a second reviewer.',
  '5. Rerun metrics after adjudication while preserving the original benchmark for comparison.',
  '6. Use a clearly recorded owner approval before any hypothetical batch release.']
 write(BANK/'results/QA_CASE_STUDY.md','\n'.join(audit)+'\n')
 write(ROOT/'QUALITY_REVIEW_PLAYBOOK.md','''# Practical quality-review playbook

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
''')
 hh=json.loads((HH/'results/metrics.json').read_text(encoding='utf-8'))
 hhbrief='''## Second completed public-data study: human preference analysis

**200 HH-RLHF pairs / 400 original candidate responses**, with source-published human preferences, a pinned official revision, MIT notice and documented sampling rules. A longer-response proxy agrees on **117/195 non-tied pairs (60%)**, with five ties. The deterministic coin baseline is **50.5%**. This shows the limits of superficial ranking proxies—not personal evaluator accuracy or production-model quality.

- [Source, methodology and reproduction](01-LLM-Evaluation/experiments/hh-preference/README.md)
- [Actual results and bias limits](01-LLM-Evaluation/experiments/hh-preference/results/REPORT.md)
- [Operational BANKING77 audit](02-AI-Data-Annotation/experiments/banking77/results/QA_CASE_STUDY.md)
- [Practical review playbook](QUALITY_REVIEW_PLAYBOOK.md)

The portfolio contains **two real public-data studies plus six synthetic baseline demonstrations**. The original authors supplied public labels; personal review fields remain blank.
'''
 block(ROOT/'README.md','REAL_EVIDENCE',hhbrief,True)
 block(ROOT/'01-LLM-Evaluation/README.md','HH_STUDY',hhbrief.replace('01-LLM-Evaluation/','').replace('02-AI-Data-Annotation/','../02-AI-Data-Annotation/'))
 block(ROOT/'EVIDENCE_BRIEF.md','HH_STUDY',hhbrief)
 role='''# Recruiter evidence map

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
'''
 write(ROOT/'ROLE_EVIDENCE_MAP.md',role);block(ROOT/'recruiter-guide.md','REAL_EVIDENCE',role)
 block(ROOT/'PROVENANCE.md','HH_ORIGIN','HH-RLHF helpful-base test data are by Anthropic (2022), under the retained MIT license. This addition reorders original published chosen/rejected preferences into A/B pairs; original response text is not rewritten. Source hashes, line IDs and sample-selection exclusions are recorded. No personal human annotation, employment or Anthropic endorsement is claimed. The full source cache is not publicly bundled.')
 block(ROOT/'DATA_LICENSE.md','HH_LICENSE','Third-party HH-RLHF-derived sample text/preferences are by Anthropic under the original MIT notice in `01-LLM-Evaluation/experiments/hh-preference/source/UPSTREAM_LICENSE.txt`. Keep copyright and permission notices with redistribution. Original banking data remain CC BY 4.0. Neither dataset is original data collected or annotated by Sinshad PS.')
 block(ROOT/'career/LinkedIn.md','HH_PROJECT','## Additional project draft: public human-preference analysis\n\nAI-assisted analysis of 200 curated HH-RLHF test pairs (400 original responses), with source attribution, deterministic selection, preference-proxy comparisons, tie/coverage accounting and blank human-adjudication forms. The longer-answer proxy matches 60% of published preferences on non-tied cases, illustrating the need for contextual rubrics. Original preferences belong to the dataset authors; no personal annotation score is claimed. Draft only, not posted.')
 block(ROOT/'career/application-kit.md','REAL_DATA','## Updated portfolio introduction\n\nMy AI-assisted portfolio includes two public-data experiments—BANKING77 intent classification and HH-RLHF preference analysis—plus synthetic demonstrations for multilingual, visual, safety and search evaluation. It provides reproducible source checks, actual metrics, failure queues and a proposed QA workflow. Original published labels are credited; I do not claim these are personal human annotations or paid client work. Use this introduction only with an honest explanation of your contribution and understanding.')
 page=ROOT/'website/index.html';s=page.read_text(encoding='utf-8')
 start='<!-- HH_CARD:START -->';end='<!-- HH_CARD:END -->';s=re.sub(re.escape(start)+r'.*?'+re.escape(end),'',s,flags=re.S)
 chart='data:image/png;base64,'+base64.b64encode((HH/'results/benchmark.png').read_bytes()).decode('ascii')
 card=f'''{start}<section><div class="eyebrow">Public human-preference evidence</div><h2>Review quality—not just response length.</h2><div class="grid"><article class="card"><span class="badge">200 pairs · 400 source responses · original human preferences</span><h2>HH-RLHF preference study</h2><p class="metric">60% longer-response proxy agreement</p><p>117/195 non-tied pairs; five abstentions. Coin baseline: 50.5%. A curated educational-topic sample, not a production-model or personal accuracy score.</p><a href="../01-LLM-Evaluation/experiments/hh-preference/README.md">Source &amp; method</a> · <a href="../01-LLM-Evaluation/experiments/hh-preference/results/REPORT.md">Measured findings</a><img style="max-width:100%;height:auto" src="{chart}" alt="Actual proxy preference comparisons"></article><article class="card"><h2>Practical QA operations</h2><p>Inspect actual BANKING77 prediction errors by query length, including high-confidence mistakes. Follow an explicit proposed quarantine, review, adjudication and escalation workflow.</p><a href="../02-AI-Data-Annotation/experiments/banking77/results/QA_CASE_STUDY.md">Reference-labelled batch audit</a> · <a href="../QUALITY_REVIEW_PLAYBOOK.md">Review playbook</a><p>These are public-data portfolio experiments and simulations—not employment, clients or completed personal reviews.</p></article></div></section>{end}'''
 s=s.replace('<main>','<main>'+card,1);s=s.replace('a completed public BANKING77 experiment','two completed public-data studies: BANKING77 and HH-RLHF')
 write(page,s)
 ignore=ROOT/'.gitignore'
 old_ignore=ignore.read_text(encoding='utf-8')
 if '**/data/cache/' not in old_ignore:write(ignore,old_ignore.rstrip()+'\n\n# Public-source caches are not bundled\n**/data/cache/\n__pycache__/\n*.pyc\n')
 workflow=ROOT/'.github/workflows/tests.yml';w=workflow.read_text(encoding='utf-8')
 if 'Run HH preference tests' not in w:w+='\n      - name: Run HH preference tests\n        run: python -m unittest discover -s 01-LLM-Evaluation/experiments/hh-preference/tests -v\n'
 write(workflow,w)
 reproduction=ROOT/'reproduce_all.py';r=reproduction.read_text(encoding='utf-8')
 if "hh-preference" not in r:
  r=r.replace("    print('Synthetic", "    run([ROOT/'01-LLM-Evaluation/experiments/hh-preference/run_experiment.py'])\n    run([ROOT/'strengthen_portfolio.py'])\n    run(['-m','unittest','discover','-s',ROOT/'01-LLM-Evaluation/experiments/hh-preference/tests','-v'])\n    print('Synthetic")
 write(reproduction,r)
 print(json.dumps({'banking_cohorts':stats,'hh_pairs':200,'real_data_studies':2,'personal_review_claimed':False},indent=2))
if __name__=='__main__':run()
