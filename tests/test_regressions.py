import importlib.util, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('portfolio_analysis',ROOT/'analysis.py')
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
class RegressionTests(unittest.TestCase):
 def test_multilingual_none_is_not_error(self):
  p=ROOT/'03-Multilingual-AI-Evaluation';rows=a.loadj(p/'data/pairs.jsonl');m=json.loads((p/'results/metrics.json').read_text(encoding='utf-8'))
  for domain,item in m['per_domain_composition_error_rate'].items():
   values=[r['error_'+side] for r in rows if r['domain']==domain for side in ['a','b']]
   count=sum(bool([v for v in (x if isinstance(x,list) else [x]) if v not in ['none','']]) for x in values)
   self.assertAlmostEqual(item['rate'],count/len(values))
 def test_metric_known_values(self):
  self.assertAlmostEqual(a.dcg([3,0]),7)
  result=a.classification(['x','x','y'],['x','y','y'],['x','y'])
  self.assertAlmostEqual(result['accuracy'],2/3)
  self.assertAlmostEqual(result['macro_f1'],2/3)
 def test_baseline_does_not_depend_on_reference_labels(self):
  text='Please refund the money for this return.'
  self.assertEqual(a.choose_topic(text),'refund')
  self.assertEqual(a.triage('Hello','Welcome.'),'accept')
 def test_all_notebooks_are_executed_outputs(self):
  paths=list(ROOT.glob('*/notebooks/*.ipynb'));self.assertEqual(len(paths),6)
  for p in paths:
   n=json.loads(p.read_text(encoding='utf-8'));cell=next(c for c in n['cells'] if c['cell_type']=='code')
   self.assertEqual(cell['execution_count'],1)
   output=json.loads(''.join(cell['outputs'][0]['text']))
   metrics=json.loads((p.parent.parent/'results/metrics.json').read_text(encoding='utf-8'))
   self.assertEqual(output,metrics)
