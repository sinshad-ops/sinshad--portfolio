from pathlib import Path
import csv,json,sys,unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from ingest import ingest
from run_experiment import load_data,validation_split,norm,features,metrics,MultinomialNB

class Banking77Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data,cls.labels,_=load_data()
        cls.report=json.loads((ROOT/'results/metrics.json').read_text(encoding='utf-8'))
        with (ROOT/'results/test_predictions.csv').open(encoding='utf-8',newline='') as f:
            cls.predictions=list(csv.DictReader(f))
        for row in cls.predictions:row['top3']=json.loads(row['top3'])
    def test_official_source_hashes(self):
        _,checks=ingest();self.assertEqual(len(checks),5)
        self.assertTrue(all(r['status']=='SHA256_VERIFIED' for r in checks))
    def test_official_counts_and_labels(self):
        self.assertEqual(len(self.labels),77);self.assertEqual(len(self.data['train']),10003);self.assertEqual(len(self.data['test']),3080)
        self.assertEqual(set(r['category'] for r in self.data['test']),set(self.labels))
        self.assertTrue(all(r['label_origin']=='published_annotation' for rs in self.data.values() for r in rs))
    def test_development_group_leakage(self):
        fit,dev=validation_split(self.data['train'])
        self.assertEqual(len(fit)+len(dev),10003)
        self.assertFalse({norm(r['text']) for r in fit}&{norm(r['text']) for r in dev})
        again=validation_split(self.data['train']);self.assertEqual([r['id'] for r in dev],[r['id'] for r in again[1]])
    def test_metrics_recalculate(self):
        score,_,matrix=metrics(self.predictions,self.labels)
        self.assertEqual(score,self.report['published_test_metrics'])
        self.assertEqual(sum(sum(v.values()) for v in matrix.values()),3080)
    def test_known_metric_values(self):
        score,_,_=metrics([{'published_intent':'a','predicted_intent':'a','top3':['a']},{'published_intent':'b','predicted_intent':'a','top3':['a','b']}],['a','b'])
        self.assertAlmostEqual(score['accuracy'],.5);self.assertAlmostEqual(score['macro_f1'],1/3);self.assertAlmostEqual(score['top3_accuracy'],1)
    def test_model_predictions_need_only_text(self):
        small=[{'text':'apple fruit','category':'a'},{'text':'orange fruit','category':'a'},{'text':'truck road','category':'b'},{'text':'car road','category':'b'}]
        model=MultinomialNB(['a','b'],.5).fit(small)
        self.assertEqual(model.predict_one('apple fruit')['predicted_intent'],'a')
        self.assertEqual(model.predict_one('truck road')['predicted_intent'],'b')
        self.assertTrue(0<=model.predict_one('unknown')['uncalibrated_confidence']<=1)
    def test_features_keep_negation(self):
        self.assertIn('u:not',features('My card is not working'))
        self.assertIn('b:not working',features('My card is not working'))
    def test_official_test_matches_predictions(self):
        lookup={r['id']:r for r in self.data['test']}
        self.assertEqual(len(self.predictions),3080)
        self.assertEqual(len(set(r['id'] for r in self.predictions)),3080)
        self.assertTrue(all(r['published_intent']==lookup[r['id']]['category'] and r['text']==lookup[r['id']]['text'] for r in self.predictions))
    def test_validation_only_parameter_selection(self):
        config=json.loads((ROOT/'results/config.json').read_text(encoding='utf-8'))
        tuning=json.loads((ROOT/'results/validation-selection.json').read_text(encoding='utf-8'))
        best=sorted(tuning,key=lambda x:(-x['macro_f1'],-x['accuracy'],x['alpha']))[0]
        self.assertEqual(config['selected_alpha'],best['alpha'])
        self.assertFalse(config['test_used_for_hyperparameter_selection'])
        self.assertFalse(config['labels_reannotated_by_portfolio_owner'])
    def test_review_queue_has_no_invented_human_ratings(self):
        with (ROOT/'results/review_queue.csv').open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
        self.assertEqual(len(rows),self.report['review_queue_rows'])
        self.assertTrue(all(r['human_review_status']=='not_reviewed' and not r['reviewer_rationale'] and not r['corrected_label'] for r in rows))

if __name__=='__main__':unittest.main()
