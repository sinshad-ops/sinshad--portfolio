from pathlib import Path
import hashlib,json,subprocess,sys
ROOT=Path(__file__).resolve().parent
HH=ROOT/'01-LLM-Evaluation/experiments/hh-preference'
BANK=ROOT/'02-AI-Data-Annotation/experiments/banking77'
def run(args,cwd=ROOT):
 p=subprocess.run([sys.executable,*map(str,args)],cwd=cwd,capture_output=True,text=True,encoding='utf-8')
 if p.returncode:raise RuntimeError(p.stdout+'\n'+p.stderr)
 return p.stdout+'\n'+p.stderr
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
 logs=[]
 logs.append(run([ROOT/'analysis.py','--project','all']))
 logs.append(run([BANK/'run_experiment.py']))
 logs.append(run([HH/'run_experiment.py']))
 tracked=[BANK/'results/metrics.json',BANK/'results/test_predictions.csv',HH/'results/metrics.json',HH/'results/baseline_predictions.csv',HH/'data/pairs.jsonl']
 before={str(p.relative_to(ROOT)):digest(p) for p in tracked}
 logs.append(run([BANK/'run_experiment.py']));logs.append(run([HH/'run_experiment.py']))
 assert before=={str(p.relative_to(ROOT)):digest(p) for p in tracked},'Public-data reproduction mismatch'
 snapshot=json.loads((ROOT/'SYNTHETIC_BASELINE_SNAPSHOT.json').read_text(encoding='utf-8'))
 for path,expected in snapshot['data_sha256'].items():assert digest(ROOT/path)==expected,'Synthetic input changed '+path
 for path,expected in snapshot['metrics'].items():assert json.loads((ROOT/path).read_text(encoding='utf-8'))==expected,'Synthetic metric changed '+path
 source=['from pathlib import Path\n','import subprocess, sys, json\n',"root = Path.cwd().parent if Path.cwd().name == 'notebooks' else Path.cwd()\n", "p = subprocess.run([sys.executable, str(root/'run_experiment.py')], capture_output=True, text=True, check=True)\n",'print(p.stdout.strip())\n']
 p=subprocess.run([sys.executable,'-c',''.join(source)],cwd=HH,capture_output=True,text=True,encoding='utf-8',check=True)
 assert json.loads(p.stdout)==json.loads((HH/'results/metrics.json').read_text(encoding='utf-8'))
 notebook={'nbformat':4,'nbformat_minor':5,'metadata':{'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'}},'cells':[
  {'cell_type':'markdown','metadata':{},'source':['# Public human-preference analysis\n','Actual executed output. Original labels attributed; no personal human review claimed.']},
  {'cell_type':'code','metadata':{},'execution_count':1,'source':source,'outputs':[{'name':'stdout','output_type':'stream','text':[p.stdout]}]}]}
 target=HH/'notebooks/analysis.ipynb';target.parent.mkdir(exist_ok=True);target.write_text(json.dumps(notebook,indent=2)+'\n',encoding='utf-8')
 suites=[(ROOT/'tests',11),(BANK/'tests',10),(HH/'tests',7)]
 for path,n in suites:
  output=run(['-m','unittest','discover','-s',path,'-v']);assert f'Ran {n} tests' in output;logs.append(output)
 # Also reproduce from the bundled sample without requiring the unbundled raw source.
 cache=HH/'data/cache/test.jsonl.gz';temp=cache.with_suffix('.temporary')
 if cache.exists():cache.rename(temp)
 try:run([HH/'run_experiment.py']);assert digest(HH/'data/pairs.jsonl')==before[str((HH/'data/pairs.jsonl').relative_to(ROOT))]
 finally:
  if temp.exists():temp.rename(cache)
 logs.append(run([ROOT/'strengthen_portfolio.py']))
 report={'status':'PASS','test_count':28,'python_verified':sys.version.split()[0],
  'real_public_data_studies':2,'banking77_test_queries':3080,'hh_preference_pairs':200,
  'deterministic_public_results':'PASS','hh_notebook_actually_executed':True,
  'offline_hh_sample_reanalysis':'PASS','synthetic_input_files_preserved':len(snapshot['data_sha256']),
  'six_synthetic_metric_values_preserved':True,'github_actions_matrix_executed':False,
  'personal_human_annotation_performed':False,'employment_or_client_work_claimed':False}
 (ROOT/'FINAL_VALIDATION.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
 (ROOT/'FINAL_VALIDATION.md').write_text('# Final release verification\n\n```json\n'+json.dumps(report,indent=2)+'\n```\n\n## Actual local logs\n```text\n'+'\n'.join(logs)+'\n```\n\nPython versions in the GitHub Actions matrix are configured, not independently run here. Tests are quality checks, not proof of personal reviewer skill or a job guarantee.\n',encoding='utf-8')
 print(json.dumps(report,indent=2))
if __name__=='__main__':main()
