import json, time, urllib.request, urllib.parse, csv, os, re
meta=json.load(open("robustness/ft-retrieval-targets.json"))
MAIL="rtmalikian@gmail.com"
def get(url, timeout=30):
    req=urllib.request.Request(url, headers={"User-Agent":f"meta-analysis-retrieval/1.0 (mailto:{MAIL})"})
    with urllib.request.urlopen(req, timeout=timeout) as r: return r.read()
results={}
for rid,m in meta.items():
    doi=(m.get('doi') or '').strip()
    got=None; route=None
    if doi:
        try:
            q=urllib.parse.quote(f'DOI:"{doi}"')
            d=json.loads(get(f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={q}&format=json&resultType=core"))
            hits=d.get('resultList',{}).get('result',[])
            if hits:
                pmcid=hits[0].get('pmcid')
                if pmcid:
                    try:
                        xml=get(f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML")
                        if len(xml)>2000:
                            open(f"robustness/fulltexts2/{rid}.xml","wb").write(xml); got=f"robustness/fulltexts2/{rid}.xml"; route="europepmc_xml"
                    except Exception: pass
        except Exception as e: pass
    if not got and doi:
        try:
            u=json.loads(get(f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi,safe='')}?email={MAIL}"))
            loc=u.get('best_oa_location') or {}
            url=loc.get('url_for_pdf') or loc.get('url')
            if url:
                try:
                    data=get(url, timeout=60)
                    if data[:4]==b'%PDF':
                        open(f"robustness/fulltexts2/{rid}.pdf","wb").write(data); got=f"robustness/fulltexts2/{rid}.pdf"; route="unpaywall_pdf"
                    elif len(data)>5000 and b'<html' in data[:2000].lower():
                        open(f"robustness/fulltexts2/{rid}.html","wb").write(data); got=f"robustness/fulltexts2/{rid}.html"; route="unpaywall_html"
                except Exception: pass
        except Exception: pass
    results[rid]={"retrieved": bool(got), "file": got, "route": route}
    time.sleep(0.35)
json.dump(results, open("robustness/ft-retrieval-results.json","w"), indent=1)
n=sum(1 for v in results.values() if v['retrieved'])
print("retrieved", n, "of", len(results))
from collections import Counter
print(Counter(v['route'] for v in results.values()))
