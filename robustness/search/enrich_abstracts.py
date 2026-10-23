import csv, json, time, urllib.request, urllib.parse
MAIL="rtmalikian@gmail.com"
def get(url, timeout=30):
    req=urllib.request.Request(url, headers={"User-Agent":f"meta-analysis-enrich/1.0 (mailto:{MAIL})"})
    with urllib.request.urlopen(req, timeout=timeout) as r: return r.read()
rows=list(csv.DictReader(open("robustness/search/new-records.csv",encoding="utf-8")))
print("new records:", len(rows), "with abstract already:", sum(1 for r in rows if (r.get('abstract') or '').strip()))
enriched=0
for r in rows:
    if (r.get('abstract') or '').strip(): continue
    doi=(r.get('doi') or '').strip(); pmid=(r.get('pmid') or '').strip()
    q=None
    if doi: q=f'DOI:"{doi}"'
    elif pmid: q=f'EXT_ID:{pmid}'
    elif r.get('title'): q='TITLE:"'+r['title'].replace('"','')[:200]+'"'
    if not q: continue
    try:
        d=json.loads(get("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query="+urllib.parse.quote(q)+"&format=json&resultType=core&pageSize=1"))
        hits=d.get('resultList',{}).get('result',[])
        if hits and (hits[0].get('abstractText') or '').strip():
            r['abstract']=hits[0]['abstractText']; enriched+=1
            if not r.get('doi') and hits[0].get('doi'): r['doi']=hits[0]['doi']
            if not r.get('pmid') and hits[0].get('pmid'): r['pmid']=hits[0]['pmid']
            if not r.get('pmcid') and hits[0].get('pmcid'): r['pmcid']=hits[0]['pmcid']
    except Exception: pass
    time.sleep(0.3)
    if rows.index(r) % 50 == 49:
        with open("robustness/search/new-records-enriched.partial.csv","w",newline="",encoding="utf-8") as fh:
            w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
import os
_tmp="robustness/search/new-records-enriched.csv.tmp"
with open(_tmp,"w",newline="",encoding="utf-8") as fh:
    w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
os.replace(_tmp,"robustness/search/new-records-enriched.csv")
print("enriched:", enriched, "total with abstract now:", sum(1 for r in rows if (r.get('abstract') or '').strip()))
