from pathlib import Path
import csv,hashlib,json,sys,unittest
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from run_experiment import build_sample,evaluate,predict
class PreferenceTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.rows,cls.selection=build_sample();cls.metrics=json.loads((ROOT/'results/metrics.json').read_text(encoding='utf-8'))
 def test_sample_count_origin(self):
  self.assertEqual(len(self.rows),200);self.assertEqual(len({r['id'] for r in self.rows}),200)
  self.assertTrue(all(r['label_origin']=='published_human_preference' for r in self.rows))
 def test_balanced_display_order(self):
  self.assertEqual(sum(r['published_preference']=='A' for r in self.rows),100)
  self.assertEqual(sum(r['published_preference']=='B' for r in self.rows),100)
 def test_original_context_present(self):self.assertTrue(all(r['context'].endswith('Assistant:') and r['candidate_a'] and r['candidate_b'] for r in self.rows))
 def test_no_label_used_in_prediction(self):
  r=self.rows[0].copy();before=predict(r,'longer_response');r['published_preference']='A' if r['published_preference']=='B' else 'B';self.assertEqual(before,predict(r,'longer_response'))
 def test_known_tie_and_accuracy(self):
  rows=[{'id':'1','candidate_a':'one two','candidate_b':'one','published_preference':'A'},{'id':'2','candidate_a':'one','candidate_b':'two','published_preference':'B'}]
  m=evaluate(rows,'longer_response');self.assertEqual(m['covered'],1);self.assertEqual(m['ties'],1);self.assertEqual(m['agreement_on_covered'],1);self.assertEqual(m['coverage'],.5)
 def test_metrics_recomputed(self):self.assertEqual([evaluate(self.rows,r) for r in ['seeded_coin','longer_response','shorter_response']],self.metrics['baselines'])
 def test_no_fake_human_review(self):
  with (ROOT/'results/human_review_forms.csv').open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
  self.assertEqual(len(rows),200);self.assertTrue(all(r['review_status']=='not_reviewed' and not r['reviewer_preference'] and not r['evidence_and_rationale'] for r in rows))
if __name__=='__main__':unittest.main()
