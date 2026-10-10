"""BANKING77: published-label QA and a reproducible bag-of-words baseline.
No external model/API, no personal human annotations, no test-set tuning.
"""
from pathlib import Path
from collections import Counter,defaultdict
import argparse,csv,hashlib,json,math,random,re,subprocess,sys,unicodedata
from ingest import ingest
ROOT=Path(__file__).resolve().parent
SEED=20261009
ALPHAS=(0.1,0.5,1.0)
REVIEW_CONFIDENCE=0.8 # preregistered; uncalibrated probability, not a quality guarantee

def writej(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
def writecsv(path,rows,fields=None):
    path.parent.mkdir(parents=True,exist_ok=True)
    fields=fields or (list(rows[0]) if rows else ['id'])
    with path.open('w',encoding='utf-8',newline='') as handle:
        writer=csv.DictWriter(handle,fieldnames=fields);writer.writeheader()
        for row in rows:
            writer.writerow({key:json.dumps(row[key],ensure_ascii=False) if isinstance(row.get(key),(dict,list)) else row.get(key,'') for key in fields})
def norm(text):return ' '.join(unicodedata.normalize('NFKC',text).casefold().split())
def features(text):
    tokens=re.findall(r'[a-z]+|\d+',unicodedata.normalize('NFKC',text).casefold())
    # Prefix avoids unigram/bigram collisions. Keep negation and all stop words.
    return Counter(['u:'+x for x in tokens]+['b:'+a+' '+b for a,b in zip(tokens,tokens[1:])])
def load_data():
    categories=json.loads((ROOT/'data/raw/categories.json').read_text(encoding='utf-8'))
    data={};reject=[]
    for split,n in [('train',10003),('test',3080)]:
        with (ROOT/f'data/raw/{split}.csv').open(encoding='utf-8',newline='') as handle:
            rows=list(csv.DictReader(handle))
        assert len(rows)==n,(split,len(rows));out=[]
        for index,row in enumerate(rows):
            if not row.get('text','').strip() or row.get('category') not in categories:
                reject.append({'split':split,'row':index+2,'reason':'empty text or invalid category'});continue
            out.append({'id':f'banking77:{split}:{index:05d}','source_record_id':f'{split}.csv:record:{index+1}',
              'text':row['text'],'category':row['category'],'official_split':split,
              'label_origin':'published_annotation','source':'PolyAI BANKING77'})
        assert not reject,'Invalid rows detected; review before evaluating'
        data[split]=out
    assert len(categories)==77 and len(set(categories))==77
    return data,categories,reject

def audit(data):
    groups={}
    for split,rows in data.items():
        table=defaultdict(list)
        for row in rows:table[norm(row['text'])].append(row)
        groups[split]=table
    overlaps=set(groups['train'])&set(groups['test'])
    conflicts=[]
    for key,rows in groups['train'].items():
        labs={r['category'] for r in rows}
        if len(labs)>1:conflicts.append({'scope':'train','normalized_text':key,'labels':sorted(labs),'ids':[r['id'] for r in rows]})
    for key in overlaps:
        rows=groups['train'][key]+groups['test'][key]
        if len({r['category'] for r in rows})>1:
            conflicts.append({'scope':'train_test','normalized_text':key,'labels':sorted({r['category'] for r in rows}),'ids':[r['id'] for r in rows]})
    return {'normalization':'NFKC + casefold + collapse whitespace',
      'rows':{k:len(v) for k,v in data.items()},
      'duplicate_extra_rows':{k:sum(len(v)-1 for v in g.values()) for k,g in groups.items()},
      'train_test_overlap_unique_texts':len(overlaps),
      'test_rows_with_train_text':sum(norm(r['text']) in overlaps for r in data['test']),
      'conflicting_label_groups':len(conflicts)},overlaps,conflicts

def validation_split(train):
    # Split normalized-text groups, not rows. Never share text between fit/dev.
    table=defaultdict(list)
    for row in train:table[norm(row['text'])].append(row)
    per_label=defaultdict(list)
    for text,rows in sorted(table.items()):
        # Keep conflicting-label text groups together. First row assigns stratum only.
        per_label[rows[0]['category']].append(text)
    development=set()
    for label,texts in sorted(per_label.items()):
        rng=random.Random(str(SEED)+':'+label);rng.shuffle(texts)
        development.update(texts[:max(1,round(len(texts)*.15))])
    fit=[r for r in train if norm(r['text']) not in development]
    dev=[r for r in train if norm(r['text']) in development]
    assert not ({norm(r['text']) for r in fit}&{norm(r['text']) for r in dev})
    return fit,dev

class MultinomialNB:
    def __init__(self,labels,alpha):self.labels=labels;self.alpha=alpha
    def fit(self,rows):
        counts={label:Counter() for label in self.labels};docs=Counter()
        for r in rows:counts[r['category']].update(features(r['text']));docs[r['category']]+=1
        vocabulary=sorted(set().union(*(set(c) for c in counts.values())))
        totals={label:sum(counts[label].values()) for label in self.labels};n=len(rows);V=len(vocabulary)
        self.priors=[math.log(docs[label]/n) for label in self.labels]
        self.lookup={term:[math.log((counts[label][term]+self.alpha)/(totals[label]+self.alpha*V)) for label in self.labels] for term in vocabulary}
        self.vocabulary_size=V;self.train_rows=n
        return self
    def predict_one(self,text):
        scores=self.priors.copy();tokens=features(text)
        for term,count in tokens.items():
            weights=self.lookup.get(term)
            if weights is not None:
                scores=[s+count*w for s,w in zip(scores,weights)]
        order=sorted(range(len(scores)),key=lambda i:(-scores[i],i))
        peak=scores[order[0]];weights=[math.exp(x-peak) for x in scores];confidence=weights[order[0]]/sum(weights)
        known=sum(v for k,v in tokens.items() if k in self.lookup)
        return {'predicted_intent':self.labels[order[0]],'top3':[self.labels[i] for i in order[:3]],
          'uncalibrated_confidence':confidence,'log_score_margin':peak-scores[order[1]],
          'known_feature_fraction':known/sum(tokens.values()) if tokens else 0.0}
    def predict(self,rows):
        return [{'id':r['id'],'published_intent':r['category'],'text':r['text'],**self.predict_one(r['text'])} for r in rows]

def metrics(rows,labels):
    matrix={a:{b:0 for b in labels} for a in labels}
    for row in rows:matrix[row['published_intent']][row['predicted_intent']]+=1
    per=[]
    for label in labels:
        tp=matrix[label][label];support=sum(matrix[label].values());pred=sum(matrix[g][label] for g in labels)
        precision=tp/pred if pred else 0;recall=tp/support if support else 0
        per.append({'intent':label,'support':support,'precision':precision,'recall':recall,'f1':2*precision*recall/(precision+recall) if precision+recall else 0})
    total=len(rows);correct=sum(row['published_intent']==row['predicted_intent'] for row in rows)
    score={'n':total,'correct':correct,'accuracy':correct/total if total else 0,
      'macro_f1':sum(r['f1'] for r in per)/len(labels),
      'top3_accuracy':sum(r['published_intent'] in r.get('top3',[]) for r in rows)/total if total else 0,
      'label_count':len(labels)}
    return score,per,matrix

def chart(path,title,names,values,maximum=1.0):
    from PIL import Image,ImageDraw,ImageFont
    im=Image.new('RGB',(1100,460),'#071827');draw=ImageDraw.Draw(im)
    def font(size):
        for p in ['C:/Windows/Fonts/arial.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']:
            try:return ImageFont.truetype(p,size)
            except OSError:pass
        return ImageFont.load_default()
    draw.text((35,28),title,font=font(27),fill='#edf5f7')
    for i,(name,value) in enumerate(zip(names,values)):
        y=95+i*64;draw.text((35,y),name,font=font(18),fill='#a9bdc8')
        end=330+round(640*value/maximum)
        draw.rounded_rectangle((330,y,end if end>330 else 332,y+29),6,fill='#23c7b5')
        draw.text((end+8,y),f'{value:.1%}',font=font(17),fill='#f5b43c')
    path.parent.mkdir(parents=True,exist_ok=True);im.save(path)

def run(download=False):
    manifest,verified=ingest(download);data,labels,reject=load_data()
    qa,overlap,conflicts=audit(data);fit,dev=validation_split(data['train'])
    results=ROOT/'results';results.mkdir(exist_ok=True)
    tuning=[]
    for alpha in ALPHAS:
        model=MultinomialNB(labels,alpha).fit(fit);pred=model.predict(dev);score,_,_=metrics(pred,labels)
        tuning.append({'alpha':alpha,**score})
    best=sorted(tuning,key=lambda x:(-x['macro_f1'],-x['accuracy'],x['alpha']))[0]
    # Freeze selected settings before refitting on official training and touching test predictions.
    config={'model':'Multinomial Naive Bayes','features':'word unigrams + bigrams; NFKC/casefold; regex [a-z]+|digits; no stopword removal',
      'alpha_candidates':list(ALPHAS),'selected_alpha':best['alpha'],'selection':'development macro-F1; accuracy then smaller alpha tie-break',
      'seed':SEED,'fit_rows':len(fit),'validation_rows':len(dev),'refit_training_rows':len(data['train']),
      'test_rows':len(data['test']),'review_confidence_threshold':REVIEW_CONFIDENCE,'confidence_calibrated':False,
      'test_used_for_hyperparameter_selection':False,'labels_reannotated_by_portfolio_owner':False}
    writej(results/'config.json',config)
    model=MultinomialNB(labels,best['alpha']).fit(data['train']);predictions=model.predict(data['test'])
    primary,per,matrix=metrics(predictions,labels)
    clean=[p for p in predictions if norm(p['text']) not in overlap]
    clean_score,_,_=metrics(clean,labels)
    majority=Counter(r['category'] for r in data['train']).most_common(1)[0][0]
    simple=[{**r,'predicted_intent':majority,'top3':[majority]} for r in predictions]
    majority_score,_,_=metrics(simple,labels)
    cover=[]
    for threshold in [0.0,0.5,0.7,REVIEW_CONFIDENCE,0.9,0.95]:
        accepted=[r for r in predictions if r['uncalibrated_confidence']>=threshold]
        cover.append({'threshold':threshold,'retained':len(accepted),'coverage':len(accepted)/len(predictions),
          'accuracy_on_retained':sum(r['predicted_intent']==r['published_intent'] for r in accepted)/len(accepted) if accepted else None,
          'interpretation':'uncalibrated confidence sensitivity; thresholds not selected against test'})
    queue=[]
    for row in predictions:
        wrong=row['predicted_intent']!=row['published_intent'];low=row['uncalibrated_confidence']<REVIEW_CONFIDENCE
        if wrong or low:
            queue.append({**row,'reason':';'.join(x for x,condition in [('published_label_disagreement',wrong),('low_uncalibrated_confidence',low)] if condition),
              'human_review_status':'not_reviewed','reviewer_decision':'','reviewer_rationale':'','corrected_label':''})
    confusions=sorted([{'published_intent':a,'predicted_intent':b,'count':v} for a,row in matrix.items() for b,v in row.items() if a!=b and v],key=lambda x:(-x['count'],x['published_intent'],x['predicted_intent']))
    report={'dataset':'BANKING77','source_revision':manifest['revision'],'source_license':'CC-BY-4.0',
      'published_test_metrics':primary,'train_text_disjoint_test_metrics':clean_score,
      'majority_baseline':majority_score,'majority_intent':majority,
      'source_qa':qa,'review_queue_rows':len(queue),'model_disagreements':len(predictions)-primary['correct'],
      'vocabulary_size':model.vocabulary_size,'split_counts':{k:len(v) for k,v in data.items()},
      'labels_origin':'Published annotations from original dataset authors; no new human annotation performed',
      'claims_boundary':'Automatic classifier agreement with published benchmark labels; not personal annotator accuracy, production accuracy or model safety certification'}
    writej(results/'metrics.json',report);writej(results/'source-qa.json',qa)
    writej(results/'source-verification.json',verified);writej(results/'label-conflicts.json',conflicts)
    writej(results/'validation-selection.json',tuning)
    writecsv(results/'test_predictions.csv',predictions)
    writecsv(results/'per_intent.csv',per);writecsv(results/'top_confusions.csv',confusions,['published_intent','predicted_intent','count'])
    writecsv(results/'confidence_coverage.csv',cover)
    writecsv(results/'review_queue.csv',queue)
    writecsv(results/'confusion_matrix.csv',[{'published_intent':label,**row} for label,row in matrix.items()],['published_intent']+labels)
    writecsv(results/'split_assignments.csv',[{'id':r['id'],'split':split} for split,rs in [('fit',fit),('validation',dev),('official_test',data['test'])] for r in rs])
    derived=ROOT/'data/derived';derived.mkdir(exist_ok=True)
    for split,rows in data.items():
        with (derived/f'{split}.jsonl').open('w',encoding='utf-8') as handle:
            for row in rows:handle.write(json.dumps(row,ensure_ascii=False)+'\n')
    # One training example per intent provides a small attributed inspection sample.
    sample=[]
    for label in labels:sample.append(next(r for r in data['train'] if r['category']==label))
    writecsv(derived/'training_sample_77.csv',sample)
    chart(results/'benchmark.png','BANKING77: official test, classifier agreement',
      ['Majority accuracy','Naive Bayes accuracy','Naive Bayes macro-F1','Top-3 accuracy'],
      [majority_score['accuracy'],primary['accuracy'],primary['macro_f1'],primary['top3_accuracy']])
    weakest=sorted(per,key=lambda x:(x['f1'],x['intent']))[:5]
    lines=['# Actual BANKING77 results','',
      f"Official train/test: {len(data['train']):,}/{len(data['test']):,} queries; {len(labels)} published intents.",
      f"Training-only validation: {len(fit):,} fit / {len(dev):,} validation; alpha selected={best['alpha']}.",'',
      '| Model | Official-test accuracy | Macro-F1 |','|---|---:|---:|',
      f"| Majority (training frequency) | {majority_score['accuracy']:.2%} | {majority_score['macro_f1']:.4f} |",
      f"| Word unigram+bigram multinomial NB | {primary['accuracy']:.2%} | {primary['macro_f1']:.4f} |",'',
      f"Correct top-1 predictions: {primary['correct']}/{primary['n']}. Top-3 accuracy: {primary['top3_accuracy']:.2%}.",'',
      '## Duplicate/leakage audit',
      f"{qa['train_test_overlap_unique_texts']} normalized texts occur in both official splits, affecting {qa['test_rows_with_train_text']} test rows.",
      f"Secondary test excluding train-overlapping texts: {clean_score['n']} rows, accuracy {clean_score['accuracy']:.2%}, macro-F1 {clean_score['macro_f1']:.4f}. The official split remains intact.",
      f"Duplicate extra rows: {qa['duplicate_extra_rows']}. Conflicting-label groups flagged: {qa['conflicting_label_groups']}.",
      'No labels or rows were silently corrected or removed. The fit/validation split groups equal normalized text to prevent within-training leakage.','',
      '## Failure evidence',
      f"{report['model_disagreements']} prediction/reference disagreements; {len(queue)} cases require review because of disagreement or low uncalibrated confidence.",
      'Weakest intents by measured F1:',
      *[f"- `{r['intent']}`: F1 {r['f1']:.3f}; support {r['support']}" for r in weakest],'',
      'Largest measured confusion pairs:',
      *[f"- `{r['published_intent']}` → `{r['predicted_intent']}`: {r['count']} cases" for r in confusions[:5]],'',
      'The published label is a reference, not infallible gold. Incorrect predictions may reflect lexical overlap, subtle distinctions, out-of-vocabulary words or ambiguous labels. These are hypotheses for human review, not completed manual adjudications.','',
      '## Limits',
      '- Single banking domain, English only; no evidence for Malayalam, sentiment, entity spans, safety or multilingual generalization.',
      '- Simple lexical classifier; no transformer or production-service evaluation.',
      '- The probabilities are uncalibrated. Coverage tables describe a sensitivity analysis, not guaranteed precision.',
      '- A reused public test set does not demonstrate novelty or deployment readiness.',
      '- Data collection and original annotation were done by the published dataset authors, not the portfolio owner.',
      '- This implementation/documentation was AI-assisted. No personal human annotation score is claimed.','',
      '![Measured results](benchmark.png)','',
      '## Worked disagreement examples (not manually adjudicated)']
    for row in [r for r in predictions if r['predicted_intent']!=r['published_intent']][:5]:
        lines.extend(['',f"### {row['id']}",'> '+row['text'],f"Published: `{row['published_intent']}`; predicted: `{row['predicted_intent']}`.",f"Uncalibrated confidence: {row['uncalibrated_confidence']:.3f}. Human rationale and corrected-label fields remain blank."])
    (results/'REPORT.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    # Captured output from an actual computation, not a manually authored score.
    nb={'nbformat':4,'nbformat_minor':5,'metadata':{'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'}},
      'cells':[{'cell_type':'markdown','metadata':{},'source':['# BANKING77: public-data experiment\n','Original annotations credited to dataset authors; no personal human-labeling claim.']},
      {'cell_type':'code','metadata':{},'execution_count':1,'source':['import subprocess, sys, json\n','from pathlib import Path\n',"root = Path.cwd().parent if Path.cwd().name == 'notebooks' else Path.cwd()\n","subprocess.run([sys.executable, str(root/'run_experiment.py')], check=True, capture_output=True, text=True)\n","print((root/'results/metrics.json').read_text(encoding='utf-8'))\n"],
       'outputs':[{'name':'stdout','output_type':'stream','text':[json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True)+'\n']}]}]}
    writej(ROOT/'notebooks/analysis.ipynb',nb)
    print(json.dumps(report,indent=2))
    return report

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--download',action='store_true');args=parser.parse_args()
    run(args.download)
