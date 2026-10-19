
from __future__ import annotations
import argparse, csv, json, math, re, sys, unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
PROJECTS = {
 "llm":"01-LLM-Evaluation","annotation":"02-AI-Data-Annotation",
 "multilingual":"03-Multilingual-AI-Evaluation","multimodal":"04-Multimodal-AI-Evaluation",
 "safety":"05-AI-Quality-Evaluation","search":"06-Search-Relevance"
}

def loadj(path):
 return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
def dump(path,obj):
 path.parent.mkdir(parents=True,exist_ok=True)
 with path.open("w",encoding="utf-8",newline="\n") as f:
  f.write(json.dumps(obj,ensure_ascii=False,indent=2,sort_keys=True)+"\n")
def csvout(path,rows):
 path.parent.mkdir(parents=True,exist_ok=True)
 fields=sorted({k for r in rows for k in r}) if rows else ["id"]
 with path.open("w",encoding="utf-8",newline="") as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
  for r in rows:w.writerow({k:json.dumps(v,ensure_ascii=False,sort_keys=True) if isinstance(v,(dict,list)) else v for k,v in r.items()})
def div(a,b): return a/b if b else 0.0
def confusion(gold,pred,labels):
 return {g:{p:sum(1 for a,b in zip(gold,pred) if a==g and b==p) for p in labels} for g in labels}
def class_metrics(gold,pred,labels):
 out={}
 for lab in labels:
  tp=sum(a==lab and b==lab for a,b in zip(gold,pred)); fp=sum(a!=lab and b==lab for a,b in zip(gold,pred)); fn=sum(a==lab and b!=lab for a,b in zip(gold,pred))
  pr=div(tp,tp+fp); rc=div(tp,tp+fn)
  out[lab]={"precision":pr,"recall":rc,"f1":div(2*pr*rc,pr+rc),"support":sum(a==lab for a in gold)}
 return out
def classification(gold,pred,labels):
 pc=class_metrics(gold,pred,labels)
 return {"accuracy":div(sum(a==b for a,b in zip(gold,pred)),len(gold)),"macro_f1":sum(x["f1"] for x in pc.values())/len(labels),"per_class":pc,"confusion":confusion(gold,pred,labels),"n":len(gold)}
def font(size,bold=False):
 for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf","C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"]:
  try:return ImageFont.truetype(p,size)
  except OSError:pass
 return ImageFont.load_default()
def chart(path,title,values):
 values=list(values.items())
 im=Image.new("RGB",(960,500),(9,22,38));d=ImageDraw.Draw(im)
 d.text((45,28),title,fill=(238,244,248),font=font(28,True))
 maxv=max([v for _,v in values]+[1])
 for i,(name,val) in enumerate(values):
  y=95+i*max(48,int(350/max(1,len(values))))
  d.text((45,y),str(name)[:28],fill=(207,220,230),font=font(17))
  x=290; w=int(590*val/maxv)
  d.rounded_rectangle((x,y,x+max(3,w),y+25),6,fill=(26,188,167))
  d.text((x+max(8,w)+10,y),f"{val:.3f}" if isinstance(val,float) else str(val),fill=(247,181,57),font=font(16,True))
 im.save(path)
def tokens(s): return re.findall(r"[a-z0-9]+",str(s).lower())
def flatten_conf(c): return [{"gold":g,"predicted":p,"count":n} for g,row in c.items() for p,n in row.items()]

def llm(p):
 pairs=loadj(p/"data"/"pairs.jsonl"); judges=loadj(p/"data"/"judge-decisions.jsonl"); jm={str(x["id"]):x for x in judges}
 dims=["accuracy","instruction_following","helpfulness","clarity"]; weights={"accuracy":.4,"instruction_following":.3,"helpfulness":.2,"clarity":.1}
 gold=[];pred=[];cats=defaultdict(lambda:[0,0]);dimvals=defaultdict(list);passes=[];queue=[]
 for x in pairs:
  j=jm[str(x["id"])]; g=x["expected_preference"]; q=j["preference"];gold.append(g);pred.append(q);cats[x["category"]][1]+=1;cats[x["category"]][0]+=g==q
  for side in ["a","b"]:
   s=j["scores_"+side]
   for d in dims:dimvals[d].append(s[d])
   weighted=sum(weights[d]*s[d] for d in dims)
   passed=weighted>=4 and s["accuracy"]>=4 and s["instruction_following"]>=4
   passes.append({"id":x["id"],"response":side.upper(),"weighted_score":weighted,"accuracy":s["accuracy"],"instruction_following":s["instruction_following"],"pass":passed})
  if g!=q:queue.append({"id":x["id"],"category":x["category"],"provisional_preference":g,"judge_preference":q,"reason":"provisional author reference and AI judge disagree","status":"manual_review_pending"})
 labels=["A","B","tie"]; cl=classification(gold,pred,labels)
 sens={}
 for t in [3.5,4.0,4.5]:
  sens[str(t)]=div(sum(r["weighted_score"]>=t and r["accuracy"]>=4 and r["instruction_following"]>=4 for r in passes),len(passes))
 metrics={"project":"llm","case_count":50,"response_count":100,"provenance":{"author_reference":"Strawberry fast model, family/version unspecified","separate_scoring_pass":"Strawberry fast model, family/version unspecified","human_gold":False,"timestamp":"2026-10-08"},"agreement_rate":cl["accuracy"],"confusion":cl["confusion"],"ties":{"provisional":gold.count("tie"),"judge":pred.count("tie")},"per_category":{k:{"agreement":div(v[0],v[1]),"n":v[1]} for k,v in cats.items()},"mean_scores":{d:sum(v)/len(v) for d,v in dimvals.items()},"weighted_formula":"0.4*accuracy + 0.3*instruction_following + 0.2*helpfulness + 0.1*clarity","pass_rule":"weighted>=4 and accuracy>=4 and instruction_following>=4","pass_rate":div(sum(x["pass"] for x in passes),len(passes)),"threshold_sensitivity":sens,"disagreements":len(queue)}
 csvout(p/"results"/"review_queue.csv",queue);csvout(p/"results"/"response_scores.csv",passes)
 chart(p/"results"/"chart.png","Provisional reference vs AI judge",{"agreement":metrics["agreement_rate"],"pass_rate":metrics["pass_rate"],"disagreement_rate":1-metrics["agreement_rate"]})
 return metrics

TOPIC={
 "billing":["bill","charged","charge","invoice","payment","card","fee"],
 "account":["account","login","password","sign in","profile","locked"],
 "delivery":["delivery","delivered","shipping","shipment","parcel","courier","arrive","tracking"],
 "technical":["error","bug","app","website","crash","screen","connection","software"],
 "refund":["refund","money back","reimburse","return","cancel"]
}
SENT={"positive":["thanks","thank you","great","happy","excellent","love"],"negative":["angry","bad","terrible","failed","wrong","unhappy","frustrated","not working","late"]}
HIGH=["urgent","immediately","asap","emergency","today","now","locked out"]; MED=["soon","please help","waiting","delay","problem","issue"]
def choose_topic(text):
 t=text.lower();scores={k:sum(t.count(w) for w in ws) for k,ws in TOPIC.items()};m=max(scores.values())
 return "general" if m==0 else next(k for k in TOPIC if scores[k]==m)
def choose_sent(text):
 t=text.lower();p=sum(w in t for w in SENT["positive"]);n=sum(w in t for w in SENT["negative"])
 return "mixed" if p and n else "positive" if p else "negative" if n else "neutral"
def choose_urg(text):
 t=text.lower();return "high" if any(w in t for w in HIGH) else "medium" if any(w in t for w in MED) else "low"
def baseline_entities(text):
 pats=[("ORDER_ID",r"\b(?:ORD[- ]?\d{3,}|#[A-Z0-9]{4,})\b"),("DATE",r"\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2}(?:, \d{4})?)\b")]
 out=[]
 for lab,pat in pats:
  for m in re.finditer(pat,text,re.I):out.append({"text":m.group(),"label":lab,"start":m.start(),"end":m.end()})
 return out
def annotation(p):
 rows=loadj(p/"data"/"production_data.jsonl");preds=[];q=[]
 for r in rows:
  pred={"id":r["id"],"split":r["split"],"topic":choose_topic(r["text"]),"sentiment":choose_sent(r["text"]),"urgency":choose_urg(r["text"]),"entities":baseline_entities(r["text"])}
  preds.append(pred)
  if r.get("ambiguous") or r.get("qc_warnings"):q.append({"id":r["id"],"ambiguous":r.get("ambiguous"),"warnings":r.get("qc_warnings"),"status":"manual_review_pending"})
 csvout(p/"data"/"baseline_predictions.csv",preds)
 result={"project":"annotation","case_count":len(rows),"split":{"calibration":70,"holdout":30},"baseline":"frozen keyword dictionaries; labels are not consulted during prediction"}
 for split in ["all","holdout"]:
  ix=[i for i,r in enumerate(rows) if split=="all" or r["split"]=="holdout"]
  result[split]={}
  for field,labels in [("topic",["billing","account","delivery","technical","refund","general"]),("sentiment",["positive","neutral","negative","mixed"]),("urgency",["low","medium","high"])]:
   result[split][field]=classification([rows[i][field] for i in ix],[preds[i][field] for i in ix],labels)
  tp=fp=fn=0
  for i in ix:
   g={(e["start"],e["end"],e["label"]) for e in rows[i].get("entity_spans",[])}
   z={(e["start"],e["end"],e["label"]) for e in preds[i]["entities"]}
   tp+=len(g&z);fp+=len(z-g);fn+=len(g-z)
  result[split]["entity_span_exact"]={"precision":div(tp,tp+fp),"recall":div(tp,tp+fn),"f1":div(2*tp,2*tp+fp+fn),"tp":tp,"fp":fp,"fn":fn}
 corrupt=[];changed=0
 for i,r in enumerate(rows):
  lab=r["topic"]
  if i%8==0:
   labs=["billing","account","delivery","technical","refund","general"];lab=labs[(labs.index(lab)+1)%len(labs)];changed+=1
  corrupt.append({"id":r["id"],"reference_topic":r["topic"],"simulated_second_topic":lab,"is_controlled_error":lab!=r["topic"]})
 csvout(p/"results"/"simulated_second_labels.csv",corrupt)
 result["simulation_not_human"]={"controlled_errors":changed,"rate":changed/len(rows),"agreement":1-changed/len(rows),"warning":"SIMULATION NOT HUMAN; not annotator agreement"}
 result["qc"]={"manual_queue":len(q),"malformed_span_quarantine":sum(bool(r.get("qc_warnings")) for r in rows)}
 csvout(p/"results"/"review_queue.csv",q)
 chart(p/"results"/"chart.png","Holdout keyword baseline",{"topic_accuracy":result["holdout"]["topic"]["accuracy"],"sentiment_accuracy":result["holdout"]["sentiment"]["accuracy"],"urgency_accuracy":result["holdout"]["urgency"]["accuracy"],"entity_f1":result["holdout"]["entity_span_exact"]["f1"]})
 return result

def multilingual(p):
 rows=loadj(p/"data"/"pairs.jsonl");prefs=Counter();errors=Counter();domains=defaultdict(lambda:[0,0]);qc=[];total=0
 for r in rows:
  prefs[r["expected_preference"]]+=1
  for side in ["a","b"]:
   total+=1; txt=r[f"candidate_{side}_malayalam"]; flags=[]
   if unicodedata.normalize("NFC",txt)!=txt:flags.append("not_nfc")
   ratio=div(sum(0x0D00<=ord(c)<=0x0D7F for c in txt),sum(c.isalpha() for c in txt))
   if ratio<.5:flags.append("low_malayalam_script_ratio")
   engdigits=re.findall(r"\d+",r["english"])
   if engdigits and not all(x in txt for x in engdigits):flags.append("english_digit_not_preserved_review_spelled_or_local_digits")
   errs=r.get(f"error_{side}",[])
   if isinstance(errs,str):errs=[errs]
   errors.update(errs);domains[r["domain"]][1]+=1;domains[r["domain"]][0]+=any(e not in {"none", ""} for e in errs)
   qc.append({"id":r["id"],"candidate":side.upper(),"flags":";".join(flags),"script_ratio":ratio,"status":"manual_review_pending" if flags else "automatic_checks_passed_not_language_validated"})
 csvout(p/"results"/"review_queue.csv",[x for x in qc if x["flags"]])
 metrics={"project":"multilingual","pair_count":len(rows),"candidate_count":total,"benchmark_preference_counts":dict(prefs),"synthetic_error_distribution":dict(errors),"per_domain_composition_error_rate":{k:{"rate":div(v[0],v[1]),"candidate_n":v[1]} for k,v in domains.items()},"automatic_qc_flags":sum(bool(x["flags"]) for x in qc),"human_review":"Malayalam native human review required; no human scores or language accuracy reported","integrity_scope":"flag-only Unicode/script/digit checks, never definitive correctness"}
 chart(p/"results"/"chart.png","Benchmark composition: expected preference",dict(prefs))
 return metrics

def components(im,colors):
 pix=im.load();w,h=im.size;target={tuple(v):k for k,v in colors.items()};seen=set();counts=Counter()
 for y in range(h):
  for x in range(w):
   rgb=pix[x,y]
   if rgb not in target or (x,y) in seen:continue
   stack=[(x,y)];seen.add((x,y));n=0
   while stack:
    a,b=stack.pop();n+=1
    for c,d in ((a-1,b),(a+1,b),(a,b-1),(a,b+1)):
     if 0<=c<w and 0<=d<h and (c,d) not in seen and pix[c,d]==rgb:seen.add((c,d));stack.append((c,d))
   if n>=100:counts[target[rgb]]+=1
 return counts
def visual_predict(r,p):
 typ=r["question_type"]; im=Image.open(p/"data"/r["image"]).convert("RGB"); cols=components(im,r["palette"])
 if typ=="count":return sum(cols.values())
 if typ=="dominant_color":
  if not cols:return None
  m=max(cols.values()); tied={c for c,n in cols.items() if n==m}
  pix=im.load()
  for x in range(im.width):
   for y in range(im.height):
    for c in tied:
     if pix[x,y]==tuple(r["palette"][c]):return c
 if typ=="tallest_bar":
  pix=im.load(); xs=[94,184,274,364]; tops=[]
  bg=(255,255,255)
  allowed={tuple(v) for v in r["palette"].values()}
  for x in xs:
   ys=[y for y in range(im.height) if pix[x,y] in allowed]
   tops.append(min(ys) if ys else 999)
  return ["A","B","C","D"][tops.index(min(tops))]
 return None
def multimodal(p):
 allrows=loadj(p/"data"/"visual_answers.jsonl");rows=[r for r in allrows if r["answer_variant"]=="correct"];evals=[];correct=0;eligible=0
 for r in rows:
  pred=visual_predict(r,p)
  if pred is not None:eligible+=1;ok=str(pred)==str(r["gold_answer"]);correct+=ok
  else:ok=False
  evals.append({"scene_id":r["scene_id"],"question_type":r["question_type"],"gold":r["gold_answer"],"pixel_prediction":pred if pred is not None else "ABSTAIN","correct":ok if pred is not None else "","status":"automatic_pixel_evaluation" if pred is not None else "abstained_requires_review"})
 csvout(p/"results"/"pixel_predictions.csv",evals);csvout(p/"results"/"review_queue.csv",[x for x in evals if x["pixel_prediction"]=="ABSTAIN" or x["correct"] is False])
 by=defaultdict(lambda:[0,0])
 for x in evals:
  if x["pixel_prediction"]!="ABSTAIN":by[x["question_type"]][1]+=1;by[x["question_type"]][0]+=bool(x["correct"])
 metrics={"project":"multimodal","scene_count":len(rows),"answer_record_count":len(allrows),"synthetic_correct_records":len(rows),"controlled_fault_records":len(allrows)-len(rows),"pixel_baseline":{"eligible":eligible,"correct":correct,"accuracy":div(correct,eligible),"coverage":div(eligible,len(rows)),"abstentions":len(rows)-eligible,"per_type":{k:{"accuracy":div(v[0],v[1]),"n":v[1]} for k,v in by.items()}},"ground_truth":"constructed from rendering geometry; metadata is an oracle only for dataset creation, never read by pixel baseline","limitation":"Artificial geometric images are not evidence of performance on natural photos or a VLM."}
 chart(p/"results"/"chart.png","Pixel baseline",{"accuracy_on_eligible":metrics["pixel_baseline"]["accuracy"],"coverage":metrics["pixel_baseline"]["coverage"],"abstention_rate":1-metrics["pixel_baseline"]["coverage"]})
 return metrics

ESC=["weapon","self-harm","suicide","explosive","malware","credential","bypass","dox","threat","violence","illegal"]
REV=["medical","legal","financial","guarantee","always","never","personal data","password","unsafe","unverified","harassment","hate"]
def triage(prompt,response):
 t=(str(prompt)+" "+str(response)).lower()
 if any(w in t for w in ESC):return "escalate"
 if any(w in t for w in REV):return "revise"
 return "accept"
def safety(p):
 rows=loadj(p/"data"/"cases.jsonl");pred=[triage(r["prompt"],r["response"]) for r in rows];gold=[r["expected_decision"] for r in rows];labels=["accept","revise","escalate"];cl=classification(gold,pred,labels);q=[];cats=defaultdict(lambda:[0,0])
 for r,z in zip(rows,pred):
  cats[r["category"]][1]+=1;cats[r["category"]][0]+=z==r["expected_decision"]
  if z=="escalate" or z!=r["expected_decision"]:q.append({"id":r["id"],"category":r["category"],"expected":r["expected_decision"],"baseline":z,"severity":r["severity"],"reason":"escalation or provisional-label mismatch","status":"human_policy_review_pending"})
 fn=sum(g=="escalate" and z!="escalate" for g,z in zip(gold,pred));fp=sum(g!="escalate" and z=="escalate" for g,z in zip(gold,pred))
 csvout(p/"results"/"review_queue.csv",q)
 metrics={"project":"safety","case_count":len(rows),"baseline":"lexical heuristic; expected labels are not consulted","accuracy":cl["accuracy"],"macro_f1":cl["macro_f1"],"per_class":cl["per_class"],"confusion":cl["confusion"],"escalation_false_negatives":fn,"escalation_false_positives":fp,"category_breakdown":{k:{"accuracy":div(v[0],v[1]),"n":v[1]} for k,v in cats.items()},"risk_tradeoff":"Escalation false negatives receive priority; false positives expose over-refusal and reviewer cost.","scope":"Portfolio-owned provisional rubric, not employer policy and not a safety certification."}
 chart(p/"results"/"chart.png","Safety triage baseline",{"accuracy":cl["accuracy"],"macro_f1":cl["macro_f1"],"escalation_FN":fn,"escalation_FP":fp})
 return metrics

def dcg(rels):return sum((2**r-1)/math.log2(i+2) for i,r in enumerate(rels))
def search(p):
 qs=loadj(p/"data"/"queries.jsonl");nd=[];rr=[];intents=defaultdict(list);fails=[];rankrows=[]
 N=sum(len(q["results"]) for q in qs)
 df=Counter()
 for q in qs:
  for r in q["results"]:df.update(set(tokens(r["title"]+" "+r["snippet"])))
 for q in qs:
  qt=Counter(tokens(q["query"]));sc=[]
  for idx,r in enumerate(q["results"]):
   dt=Counter(tokens(r["title"]+" "+r["snippet"]))
   score=sum(qn*dt[t]*(math.log((N+1)/(df[t]+1))+1) for t,qn in qt.items())
   sc.append((score,idx,r))
  ranked=[x[2] for x in sorted(sc,key=lambda x:(-x[0],x[1]))];rels=[r["relevance"] for r in ranked];ideal=sorted([r["relevance"] for r in q["results"]],reverse=True)
  n=dcg(rels)/dcg(ideal) if dcg(ideal) else 0; m=next((1/(i+1) for i,r in enumerate(rels) if r>=2),0)
  nd.append(n);rr.append(m);intents[q["intent"]].append(n)
  for rank,r in enumerate(ranked,1):rankrows.append({"query_id":q["id"],"rank":rank,"result_id":r["id"],"relevance":r["relevance"],"query":q["query"]})
  if n<.8:fails.append({"id":q["id"],"query":q["query"],"intent":q["intent"],"locale":q["locale"],"ndcg_at_4":n,"status":"manual_relevance_review_pending"})
 csvout(p/"results"/"ranked_results.csv",rankrows);csvout(p/"results"/"review_queue.csv",fails)
 metrics={"project":"search","query_count":len(qs),"result_count":sum(len(q["results"]) for q in qs),"ndcg_at_4":sum(nd)/len(nd),"mrr_relevance_gte_2":sum(rr)/len(rr),"per_intent_ndcg":{k:sum(v)/len(v) for k,v in intents.items()},"failure_queue":len(fails),"ranking":"TF-IDF-style lexical query/title/snippet overlap; gold relevance is not used for ranking","scope":"Fictional corpus judgments, not live-search performance; locale and local intent require reviewer context."}
 chart(p/"results"/"chart.png","Search ranking quality",{"NDCG@4":metrics["ndcg_at_4"],"MRR":metrics["mrr_relevance_gte_2"],"failure_rate":len(fails)/len(qs)})
 return metrics

FUN={"llm":llm,"annotation":annotation,"multilingual":multilingual,"multimodal":multimodal,"safety":safety,"search":search}
def run(name):
 p=ROOT/PROJECTS[name];m=FUN[name](p);dump(p/"results"/"metrics.json",m);return m
if __name__=="__main__":
 a=argparse.ArgumentParser();a.add_argument("--project",choices=["all"]+list(PROJECTS),default="all");a.add_argument("--print",action="store_true");z=a.parse_args()
 out={k:run(k) for k in PROJECTS} if z.project=="all" else {z.project:run(z.project)}
 if z.print:print(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
