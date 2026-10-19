
import csv, hashlib, json, subprocess, sys, unittest
from pathlib import Path
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
def jl(path):
 return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
class PortfolioTests(unittest.TestCase):
 def test_schemas_ids_and_counts(self):
  cases={
   "01-LLM-Evaluation/data/pairs.jsonl":50,
   "01-LLM-Evaluation/data/judge-decisions.jsonl":50,
   "02-AI-Data-Annotation/data/production_data.jsonl":100,
   "03-Multilingual-AI-Evaluation/data/pairs.jsonl":50,
   "04-Multimodal-AI-Evaluation/data/visual_answers.jsonl":240,
   "05-AI-Quality-Evaluation/data/cases.jsonl":100,
   "06-Search-Relevance/data/queries.jsonl":30}
  for name,n in cases.items():
   rows=jl(ROOT/name);self.assertEqual(len(rows),n,name)
   key="record_id" if "visual_answers" in name else "id"
   self.assertEqual(len({str(x[key]) for x in rows}),n,name)
 def test_annotation_labels_spans_and_counts(self):
  rows=jl(ROOT/"02-AI-Data-Annotation/data/production_data.jsonl")
  self.assertEqual(CounterLike(rows,"split"),{"calibration":70,"holdout":30})
  for r in rows:
   self.assertIn(r["topic"],{"billing","account","delivery","technical","refund","general"})
   self.assertIn(r["sentiment"],{"positive","neutral","negative","mixed"})
   self.assertIn(r["urgency"],{"low","medium","high"})
   for e in r["entity_spans"]:
    self.assertEqual(r["text"][e["start"]:e["end"]],e["text"])
    self.assertIn(e["label"],{"ORDER_ID","PRODUCT","DATE","ORG"})
 def test_judge_score_range(self):
  for r in jl(ROOT/"01-LLM-Evaluation/data/judge-decisions.jsonl"):
   for side in ("scores_a","scores_b"):
    for key in ("accuracy","instruction_following","helpfulness","clarity"):
     self.assertIsInstance(r[side][key],int);self.assertTrue(1<=r[side][key]<=5)
 def test_image_pixels(self):
  files=sorted((ROOT/"04-Multimodal-AI-Evaluation/data/images").glob("*.png"))
  self.assertEqual(len(files),120)
  hashes=set()
  for p in files:
   im=Image.open(p).convert("RGB");self.assertEqual(im.size,(480,300))
   self.assertGreater(len(im.getcolors(maxcolors=1000000)),2)
   hashes.add(hashlib.sha256(p.read_bytes()).hexdigest())
  self.assertEqual(len(hashes),120)
 def test_output_consistency(self):
  m=json.loads((ROOT/"04-Multimodal-AI-Evaluation/results/metrics.json").read_text())
  self.assertEqual(m["scene_count"],120);self.assertEqual(m["answer_record_count"],240)
  s=json.loads((ROOT/"06-Search-Relevance/results/metrics.json").read_text())
  self.assertEqual(s["query_count"],30);self.assertEqual(s["result_count"],120)
  self.assertTrue(0<=s["ndcg_at_4"]<=1 and 0<=s["mrr_relevance_gte_2"]<=1)
  a=json.loads((ROOT/"02-AI-Data-Annotation/results/metrics.json").read_text())
  for split in ("all","holdout"):
   for field in ("topic","sentiment","urgency"):
    self.assertTrue(0<=a[split][field]["accuracy"]<=1)
    self.assertTrue(0<=a[split][field]["macro_f1"]<=1)
 def test_deterministic_analysis(self):
  paths=[ROOT/d/"results/metrics.json" for d in [
   "01-LLM-Evaluation","02-AI-Data-Annotation","03-Multilingual-AI-Evaluation",
   "04-Multimodal-AI-Evaluation","05-AI-Quality-Evaluation","06-Search-Relevance"]]
  before=[p.read_bytes() for p in paths]
  subprocess.run([sys.executable,str(ROOT/"analysis.py"),"--project","all"],cwd=ROOT,check=True,stdout=subprocess.DEVNULL)
  self.assertEqual(before,[p.read_bytes() for p in paths])
 def test_manifest_hashes(self):
  man=json.loads((ROOT/"DATA_MANIFEST.json").read_text())
  for item in man["files"]:
   p=ROOT/item["path"];self.assertTrue(p.is_file())
   self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),item["sha256"])
def CounterLike(rows,key):
 out={}
 for r in rows:out[r[key]]=out.get(r[key],0)+1
 return out
if __name__=="__main__":unittest.main()
