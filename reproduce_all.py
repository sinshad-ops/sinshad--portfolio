"""Recompute both the preserved synthetic baselines and the real BANKING77 experiment."""
from pathlib import Path
import subprocess,sys
ROOT=Path(__file__).resolve().parent
EXPERIMENT=ROOT/'02-AI-Data-Annotation/experiments/banking77'

def run(args,cwd=ROOT):
    subprocess.run([sys.executable,*map(str,args)],cwd=cwd,check=True)

if __name__=='__main__':
    run([ROOT/'analysis.py','--project','all'])
    run([EXPERIMENT/'run_experiment.py'])
    run([ROOT/'integrate_banking77.py'])
    run(['-m','unittest','discover','-s',ROOT/'tests','-v'])
    run(['-m','unittest','discover','-s',EXPERIMENT/'tests','-v'])
    run([ROOT/'01-LLM-Evaluation/experiments/hh-preference/run_experiment.py'])
    run([ROOT/'strengthen_portfolio.py'])
    run(['-m','unittest','discover','-s',ROOT/'01-LLM-Evaluation/experiments/hh-preference/tests','-v'])
    run([ROOT/'build_evidence_reader.py'])
    print('Synthetic baselines + Banking77 recomputed; all tests passed. No network or personal human annotation claims.')
