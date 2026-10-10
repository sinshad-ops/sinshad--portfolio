"""Public HH-RLHF preference study. Length is a proxy, not an LLM judge.
Original preference annotations belong to Anthropic; no personal human review claimed.
"""
from pathlib import Path
import argparse,csv,gzip,hashlib,json,re,urllib.request
ROOT=Path(__file__).resolve().parent
TOPICS={'computing':r'\b(python|javascript|programming|database|algorithm|html|css|computer science|software)\b',
 'science':r'\b(photosynthesis|solar system|astronomy|planet|gravity|electricity|mathematics|geometry|calculus|physics|biology)\b',
 'everyday_tasks':r'\b(baking|bread|gardening|garden|houseplant|recipe|cooking|knitting|sewing|photography|painting|piano|guitar)\b'}
BLOCK=r'\b(sex|sexual|porn|rape|nude|suicide|self.harm|kill|murder|weapon|bomb|explosive|drug|cocaine|meth|heroin|hack|malware|phishing|fraud|racist|slur|nazi|terrorist|abuse|torture|poison|stalk|ignore instructions|system prompt|password|credit card number|medical advice|diagnos\w*|prescri\w*)\b|[\w.+-]+@[\w.-]+\.[a-z]{2,}'

def dump(path,obj):
 path.parent.mkdir(parents=True,exist_ok=True)
 with path.open('w',encoding='utf-8',newline='\n') as f:json.dump(obj,f,ensure_ascii=False,indent=2,sort_keys=True);f.write('\n')
def csvout(path,rows):
 path.parent.mkdir(parents=True,exist_ok=True)
 with path.open('w',encoding='utf-8',newline='') as f:
  fields=list(rows[0]) if rows else ['id'];w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
def sha(data):return hashlib.sha256(data).hexdigest()
def answer(text):
 prefix,sep,last=text.rpartition('\n\nAssistant:')
 if not sep:raise ValueError('Conversation format unexpected')
 return prefix+sep,last.strip()
def build_sample(download=False):
 manifest=json.loads((ROOT/'source/source-manifest.json').read_text(encoding='utf-8'))
 cache=ROOT/'data/cache/test.jsonl.gz';sample=ROOT/'data/pairs.jsonl';ledger=ROOT/'source/sample-manifest.json'
 if not cache.exists() and not download:
  assert sample.exists(),'Use --download to build the sample'
  assert sha(sample.read_bytes())==json.loads(ledger.read_text())['sha256'],'Sample hash mismatch'
  return [json.loads(x) for x in sample.read_text(encoding='utf-8').splitlines()],json.loads(ledger.read_text())['selection']
 if not cache.exists():
  with urllib.request.urlopen(manifest['url'],timeout=60) as response:payload=response.read(4*1024*1024)
  assert sha(payload)==manifest['sha256'];cache.parent.mkdir(parents=True,exist_ok=True);cache.write_bytes(payload)
 assert sha(cache.read_bytes())==manifest['sha256'],'Official source hash mismatch'
 rows=[json.loads(x) for x in gzip.decompress(cache.read_bytes()).decode('utf-8').splitlines() if x.strip()]
 eligible=[];excluded={'format_or_context_mismatch':0,'blocked_content_or_email':0,'non_target_topic':0,'oversized':0}
 for i,row in enumerate(rows):
  try:ca,a=answer(row['chosen']);cb,b=answer(row['rejected'])
  except (ValueError,KeyError):excluded['format_or_context_mismatch']+=1;continue
  if ca!=cb or not a or not b:excluded['format_or_context_mismatch']+=1;continue
  if max(len(a),len(b))>8000 or len(ca)>12000:excluded['oversized']+=1;continue
  if re.search(BLOCK,ca+a+b,re.I):excluded['blocked_content_or_email']+=1;continue
  topic=next((t for t,pat in TOPICS.items() if re.search(pat,ca,re.I)),None)
  if topic is None:excluded['non_target_topic']+=1;continue
  eligible.append({'source_line':i+1,'context':ca,'chosen':a,'rejected':b,'topic':topic})
 eligible.sort(key=lambda r:sha(('20261009:'+str(r['source_line'])).encode()))
 selected=eligible[:200];out=[]
 for j,row in enumerate(selected):
  # Alternate display order, so preferred-answer position is not always A.
  a,b=(row['chosen'],row['rejected']) if j%2==0 else (row['rejected'],row['chosen'])
  out.append({'id':f"hh-helpful-test:{row['source_line']:04d}",'source_record_id':f"helpful-base/test.jsonl:line:{row['source_line']}",
   'source_revision':manifest['revision'],'label_origin':'published_human_preference','topic':row['topic'],
   'context':row['context'],'candidate_a':a,'candidate_b':b,'published_preference':'A' if j%2==0 else 'B'})
 assert len(out)>=50,'Insufficient eligible examples; do not fabricate records'
 sample.parent.mkdir(parents=True,exist_ok=True)
 with sample.open('w',encoding='utf-8',newline='\n') as f:
  for row in out:f.write(json.dumps(row,ensure_ascii=False)+'\n')
 selection={'official_source_rows':len(rows),'eligible_rows':len(eligible),'selected_pairs':len(out),'excluded':excluded,
  'selection':'topic regex + broad risky-content/email exclusion + context match + size bounds; deterministic hash ordering; cap 200',
  'sampling_bias':'curated educational/practical topics, NOT representative of all HH-RLHF','manually_safety_reviewed':False}
 dump(ledger,{'sha256':sha(sample.read_bytes()),'selection':selection})
 return out,selection

def predict(row,rule):
 a,b=(len(re.findall(r'\S+',row[x])) for x in ['candidate_a','candidate_b'])
 if rule=='seeded_coin':return 'A' if int(sha(row['id'].encode()),16)%2==0 else 'B'
 if a==b:return 'tie'
 long='A' if a>b else 'B'
 return long if rule=='longer_response' else ('B' if long=='A' else 'A')
def evaluate(rows,rule):
 pred=[predict(r,rule) for r in rows];covered=[(r,p) for r,p in zip(rows,pred) if p!='tie']
 agree=sum(r['published_preference']==p for r,p in covered)
 return {'rule':rule,'pairs':len(rows),'covered':len(covered),'ties':len(rows)-len(covered),'coverage':len(covered)/len(rows),
  'agreements':agree,'agreement_on_covered':agree/len(covered) if covered else None,
  'agreement_all_pairs_ties_count_as_no_agreement':agree/len(rows)}
def run(download=False):
 rows,selection=build_sample(download);rules=['seeded_coin','longer_response','shorter_response']
 metrics={'dataset':'Anthropic HH-RLHF helpful-base official test','selection':selection,
  'baselines':[evaluate(rows,rule) for rule in rules],
  'by_topic':{topic:[evaluate([r for r in rows if r['topic']==topic],rule) for rule in rules] for topic in sorted({r['topic'] for r in rows})},
  'interpretation':'Agreement with published human preferences, not factual correctness, personal annotator accuracy, model safety, or an evaluated production LLM.',
  'new_model_responses_generated':False,'personal_human_annotation_performed':False}
 results=ROOT/'results';dump(results/'metrics.json',metrics)
 predictions=[{'id':r['id'],'topic':r['topic'],'published_preference':r['published_preference'],
   **{rule:predict(r,rule) for rule in rules}} for r in rows]
 csvout(results/'baseline_predictions.csv',predictions)
 forms=[{'id':r['id'],'source_record_id':r['source_record_id'],'topic':r['topic'],'published_preference':r['published_preference'],
  'review_status':'not_reviewed','reviewer_preference':'','accuracy_notes':'','instruction_following_notes':'','evidence_and_rationale':'','review_date':''} for r in rows]
 csvout(results/'human_review_forms.csv',forms)
 misses=[p for p in predictions if p['longer_response']!=p['published_preference']]
 csvout(results/'length_proxy_failure_queue.csv',misses)
 lines=['# Public preference benchmark — actual results','',f"{len(rows)} pairs / {len(rows)*2} responses selected from {selection['official_source_rows']} original test records; {selection['eligible_rows']} passed the predeclared lexical/topic rules.",'',
  '| Baseline | Covered pairs | Agreement on covered | Ties |','|---|---:|---:|---:|']
 for r in metrics['baselines']:lines.append(f"| {r['rule']} | {r['covered']} | {r['agreement_on_covered']:.2%} | {r['ties']} |")
 lines+=['','## Conclusions and boundaries',
  '- Longer is not necessarily more helpful. A response-length proxy ignores accuracy, instruction following, tone, omissions and context.',
  '- Preferences were supplied by the original dataset, not personally labeled by Sinshad PS.',
  '- The educational-topic and risk-word filters intentionally bias this sample. Do not generalize these rates to the full dataset.',
  '- This benchmark does not produce new model outputs or validate a production LLM. It is a preference-analysis and evaluator-workflow demonstration.',
  '- Equal-length ties are abstentions; covered and all-pair rates are both reported.',
  '- Lexical filtering is not human safety certification. The full source can contain offensive material; it is not bundled.',
  '- Review forms remain blank. Published preferences are subjective and are not factual-correctness gold.','',
  '## Reproduction','`python run_experiment.py` reanalyzes the hash-verified bundled sample offline. `python run_experiment.py --download` reconstructs it from the pinned official gzip source.','',
  '## Source','Anthropic HH-RLHF, MIT license. Original source and terms are retained under `source/`. See experiment README for attribution.']
 (results/'REPORT.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
 from PIL import Image,ImageDraw
 im=Image.new('RGB',(950,330),'#071827');d=ImageDraw.Draw(im);d.text((25,25),'HH-RLHF: preference agreement of simple proxies (not model quality)',fill='#ffffff')
 for i,r in enumerate(metrics['baselines']):
  y=85+i*65;d.text((25,y),r['rule'],fill='#b5c7d0');end=260+int(600*r['agreement_on_covered']);d.rectangle((260,y,end,y+28),fill='#21c9b4');d.text((end+8,y),f"{r['agreement_on_covered']:.1%}",fill='#f9b83f')
 im.save(results/'benchmark.png')
 print(json.dumps(metrics,indent=2));return metrics
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--download',action='store_true');args=parser.parse_args();run(args.download)
