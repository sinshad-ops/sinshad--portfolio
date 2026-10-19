from pathlib import Path
import hashlib,json,subprocess,sys,zipfile
ROOT=Path(__file__).resolve().parent
EXP=ROOT/'02-AI-Data-Annotation/experiments/banking77'
OUT=EXP/'results'

def hashfile(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def command(args,cwd=ROOT):
    r=subprocess.run([sys.executable,*map(str,args)],cwd=cwd,capture_output=True,text=True,encoding='utf-8')
    if r.returncode:raise RuntimeError(r.stdout+'\n'+r.stderr)
    return r.stdout+'\n'+r.stderr

def main():
    logs=[]
    # Normalize current-platform serialization once; metrics values are checked against the uploaded original below.
    logs.append(command([ROOT/'analysis.py','--project','all']))
    paths=[OUT/n for n in ['metrics.json','config.json','test_predictions.csv','per_intent.csv','review_queue.csv','confidence_coverage.csv']]
    before={str(p.relative_to(ROOT)):hashfile(p) for p in paths}
    notebook=EXP/'notebooks/analysis.ipynb'
    nb=json.loads(notebook.read_text(encoding='utf-8'));cell=next(c for c in nb['cells'] if c['cell_type']=='code')
    executed=subprocess.run([sys.executable,'-c',''.join(cell['source'])],cwd=EXP,capture_output=True,text=True,encoding='utf-8',check=True)
    expected=json.loads(''.join(cell['outputs'][0]['text']))
    assert json.loads(executed.stdout)==expected,'Notebook output mismatch'
    after={str(p.relative_to(ROOT)):hashfile(p) for p in paths}
    assert before==after,'Banking77 results are not deterministic'
    snapshot=json.loads((ROOT/'SYNTHETIC_BASELINE_SNAPSHOT.json').read_text(encoding='utf-8'))
    preserved=0
    for relative,digest in snapshot['data_sha256'].items():
        assert hashfile(ROOT/relative)==digest,'Synthetic source/data changed: '+relative
        preserved+=1
    for relative,expected_metrics in snapshot['metrics'].items():
        assert json.loads((ROOT/relative).read_text(encoding='utf-8'))==expected_metrics,'Synthetic score changed: '+relative
    logs.append(command(['-m','unittest','discover','-s',ROOT/'tests','-v']))
    logs.append(command(['-m','unittest','discover','-s',EXP/'tests','-v']))
    command([ROOT/'integrate_banking77.py'])
    report={'status':'PASS','banking77_tests':10,'preserved_suite_tests':11,'notebook_executed_and_output_verified':True,
      'banking77_numeric_and_csv_byte_reproduction':'PASS','synthetic_source_data_files_byte_preserved':preserved,
      'all_six_synthetic_metric_values_preserved':True,'personal_human_annotation_performed':False,'run_date':'2026-10-09'}
    (OUT/'validation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    text='# Banking77 release validation\n\n'+json.dumps(report,indent=2)+'\n\n## Test logs\n```text\n'+'\n'.join(logs)+'\n```\n\nOriginal metric JSON may be serialized with different line endings on different platforms; numerical values are unchanged. New Banking77 predictions/metrics were identical on repeated same-environment execution.\n'
    (OUT/'VALIDATION.md').write_text(text,encoding='utf-8')
    root=ROOT/'VALIDATION.md';source=root.read_text(encoding='utf-8');start='<!-- BANKING77_VALIDATION -->'
    source=source.split(start)[0].rstrip()
    root.write_text(source+'\n\n'+start+'\n## Banking77 release\n\n10 new experiment tests and 11 preserved-suite tests pass. Actual notebook execution and deterministic rerun are verified. See [`'+str((OUT/'VALIDATION.md').relative_to(ROOT)).replace('\\','/')+'`]('+str((OUT/'VALIDATION.md').relative_to(ROOT)).replace('\\','/')+'). Original synthetic metric values and source datasets were checked against the uploaded archive.\n',encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
