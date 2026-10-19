"""Download BANKING77 from a pinned official revision; verify bytes before use."""
from pathlib import Path
import argparse, hashlib, json, urllib.request
ROOT=Path(__file__).resolve().parent

def ingest(download=False):
    manifest=json.loads((ROOT/'source/source-manifest.json').read_text(encoding='utf-8'))
    statuses=[]
    for record in manifest['files']:
        destination=ROOT/record['path']
        if not destination.exists():
            if not download:
                raise FileNotFoundError(f'{destination}: rerun with --download')
            request=urllib.request.Request(record['url'],headers={'User-Agent':'Banking77-Portfolio-Reproduction/1.0'})
            with urllib.request.urlopen(request,timeout=60) as response:
                payload=response.read(4*1024*1024)
            if hashlib.sha256(payload).hexdigest()!=record['sha256']:
                raise ValueError('Source hash mismatch: '+record['path'])
            destination.parent.mkdir(parents=True,exist_ok=True)
            destination.write_bytes(payload)
        data=destination.read_bytes()
        if len(data)!=record['bytes'] or hashlib.sha256(data).hexdigest()!=record['sha256']:
            raise ValueError('Cached source is modified: '+record['path'])
        statuses.append({'path':record['path'],'status':'SHA256_VERIFIED','bytes':len(data)})
    return manifest,statuses

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--download',action='store_true')
    args=parser.parse_args();print(json.dumps(ingest(args.download)[1],indent=2))
