from pathlib import Path
import json,re,urllib.parse
ROOT=Path(__file__).resolve().parent

def run():
 docs={}
 for p in ROOT.rglob('*.md'):
  if 'source' in p.parts or 'research' in p.parts or p.name=='FINAL_VALIDATION.md':continue
  docs['../'+p.relative_to(ROOT).as_posix()]=p.read_text(encoding='utf-8')
 for p in ROOT.rglob('metrics.json'):docs['../'+p.relative_to(ROOT).as_posix()]=p.read_text(encoding='utf-8')
 data=json.dumps(docs,ensure_ascii=False).replace('</','<\\/')
 page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Portfolio evidence — Sinshad PS</title><style>*{box-sizing:border-box}body{margin:0;background:#071827;color:#edf5f7;font:16px/1.65 system-ui,sans-serif}main{max-width:1000px;margin:auto;padding:35px 25px}a{color:#21c9b4}nav{display:flex;gap:20px;flex-wrap:wrap;margin-bottom:25px}.badge{color:#f4b844;font-size:12px;letter-spacing:.08em;text-transform:uppercase}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#102b3c;border:1px solid #294658;border-radius:14px;padding:25px;font:15px/1.7 ui-monospace,Consolas,monospace}select{max-width:100%;background:#102b3c;color:#fff;padding:12px;border:1px solid #23c7b5;border-radius:7px}h1{font-size:30px;overflow-wrap:anywhere}@media(max-width:600px){main{padding:20px 14px}pre{font-size:13px;padding:15px}h1{font-size:24px}}</style></head><body><main><nav><a href="index.html">Back to portfolio</a><a id="original">Open original evidence file</a></nav><div class="badge">Traceable portfolio evidence · no live service required</div><h1 id="title">Evidence reader</h1><label for="doc">Choose an evidence document</label><br><select id="doc"></select><pre id="content"></pre></main><script>const DOCS='''+data+r''';const select=document.getElementById('doc');for(const key of Object.keys(DOCS).sort()){const o=document.createElement('option');o.value=key;o.textContent=key.replace(/^\.\.\//,'');select.appendChild(o)}function show(key){if(!Object.prototype.hasOwnProperty.call(DOCS,key))key='../ROLE_EVIDENCE_MAP.md';select.value=key;document.getElementById('title').textContent=key.split('/').pop().replace(/[-_]/g,' ');document.getElementById('content').textContent=DOCS[key];document.getElementById('original').href=key;document.getElementById('original').download=key.split('/').pop()}select.addEventListener('change',()=>{show(select.value);history.replaceState(null,'','?doc='+encodeURIComponent(select.value))});show(new URLSearchParams(location.search).get('doc')); </script></body></html>'''
 (ROOT/'website/evidence.html').write_text(page,encoding='utf-8')
 path=ROOT/'website/index.html';site=path.read_text(encoding='utf-8')
 def replace(m):
  key=m.group(1)
  return 'href="evidence.html?doc='+urllib.parse.quote(key,safe='')+'"' if key in docs else m.group(0)
 site=re.sub(r'href="([^"\n]+)"',replace,site)
 site=site.replace('href="${c.folder}"','href="evidence.html?doc=${encodeURIComponent(c.folder+\'README.md\')}"')
 path.write_text(site,encoding='utf-8')
 print(json.dumps({'embedded_evidence_documents':len(docs),'offline_reader':True,'external_data_fetch_required':False}))
if __name__=='__main__':run()
