import json, time, urllib.request, urllib.parse, os
meta=json.load(open("robustness/search/chasing-ft-meta.json"))
MAIL="rtmalikian@gmail.com"
def get(url, timeout=30):
    req=urllib.request.Request(url, headers={"User-Agent":f"meta-analysis-retrieval/1.0 (mailto:{MAIL})"})
    with urllib.request.urlopen(req, timeout=timeout) as r: return r.read()
results={}
for rid,m in meta.items():
    doi=(m.get('doi') or '').strip(); got=None; route=None
    if doi:
        try:
            q=urllib.parse.quote(f'DOI:"{doi}"')
            d=json.loads(get(f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={q}&format=json&resultType=core"))
            hits=d.get('resultList',{}).get('result',[])
            if hits and hits[0].get('pmcid'):
                try:
                    xml=get(f"https://www.ebi.ac.uk/europepmc/webservices/rest/{hits[0]['pmcid']}/fullTextXML")
                    if len(xml)>2000:
                        open(f"robustness/search/fulltexts3/{rid}.xml","wb").write(xml); got=True; route="europepmc_xml"
                except Exception: pass
        except Exception: pass
    if not got and doi:
        try:
            u=json.loads(get(f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi,safe='')}?email={MAIL}"))
            loc=u.get('best_oa_location') or {}
            url=loc.get('url_for_pdf') or loc.get('url')
            if url:
                data=get(url, timeout=60)
                if data[:4]==b'%PDF':
                    open(f"robustness/search/fulltexts3/{rid}.pdf","wb").write(data); got=True; route="unpaywall_pdf"
                elif len(data)>5000 and b'<html' in data[:2000].lower():
                    open(f"robustness/search/fulltexts3/{rid}.html","wb").write(data); got=True; route="unpaywall_html"
        except Exception: pass
    if not got and not doi and m.get('title'):
        try:
            q=urllib.parse.quote('TITLE:"'+m['title'].replace('"','')[:200]+'"')
            d=json.loads(get(f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={q}&format=json&resultType=core"))
            hits=d.get('resultList',{}).get('result',[])
            if hits and hits[0].get('pmcid'):
                xml=get(f"https://www.ebi.ac.uk/europepmc/webservices/rest/{hits[0]['pmcid']}/fullTextXML")
                if len(xml)>2000:
                    open(f"robustness/search/fulltexts3/{rid}.xml","wb").write(xml); got=True; route="europepmc_xml_title"
        except Exception: pass
    results[rid]={"retrieved": bool(got), "route": route}
    print(rid, got, route, flush=True)
    time.sleep(0.35)
json.dump(results, open("robustness/search/chasing-ft-results.json","w"), indent=1)
print("retrieved", sum(1 for v in results.values() if v['retrieved']), "of", len(results), flush=True)
