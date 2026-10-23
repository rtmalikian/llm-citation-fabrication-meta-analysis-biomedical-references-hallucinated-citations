"""Review 2 meta-analysis of proportions. Python 3, numpy/scipy/pandas.
Random effects, logit transformation, REML tau2 (Fisher scoring on logit scale),
Hartung-Knapp not used; CI from normal approx on pooled logit. Prediction interval
where k>=10 (t_{k-2}). Continuity correction 0.5 for zero/full cells.
"""
import csv, json, math
import numpy as np
from scipy import stats, optimize
base="/home/hatch/workspace/publications/weekly-series/meta-analysis-llm-citation-fabrication/review2/"
rows=list(csv.DictReader(open(base+"extraction.csv",encoding="utf-8")))
gen=[r for r in rows if r['eligibility']=='include_generation']
def num(v):
    try: return float(v)
    except: return None

def norm_retrieval(x):
    t=(x or '').strip().lower()
    if t.startswith('none'): return 'none'
    if 'browsing' in t or 'live search' in t or 'web search' in t or 'web-search' in t or t.startswith('retrieval') or 'database' in t or t=='rag': return 'retrieval'
    return 'not_reported'
def norm_family(x):
    t=(x or '').strip().lower()
    if 'gpt' in t: return 'GPT'
    if 'claude' in t: return 'Claude'
    if 'gemini' in t: return 'Gemini'
    if 'deepseek' in t: return 'DeepSeek'
    if 'grok' in t: return 'Grok'
    return 'other'
def norm_pub(x):
    t=(x or '').strip().lower()
    if 'preprint' in t: return 'preprint'
    if 'peer' in t or 'journal article' in t: return 'peer_reviewed'
    return t or 'nr'
def arms_for(outcome):
    out=[]
    for r in gen:
        n=num(r['refs_generated']); x=num(r[outcome])
        if n and n>0 and x is not None:
            out.append(dict(study=r['study_id'],record=r['record_id'],arm=r['model_arm'],family=norm_family(r['model_family']),retrieval=norm_retrieval(r['retrieval']),pub=norm_pub(r['pub_type']),year=r['model_year'],topic=r['topic_type'],specialty=r['specialty'],requested=num(r['refs_requested']),n=int(n),x=int(x)))
    return out
def pool(arms,label):
    if len(arms)<2: return dict(label=label,k=len(arms),note="too few to pool")
    y=[]; v=[]
    for a in arms:
        x=a['x']; n=a['n']
        xc=x+0.5 if x==0 or x==n else x; nc=n+1 if x==0 or x==n else n
        p=xc/nc; y.append(math.log(p/(1-p))); v.append(1/xc+1/(nc-xc))
    y=np.array(y); v=np.array(v)
    def reml(tau2):
        w=1/(v+tau2); mu=(w*y).sum()/w.sum()
        return -0.5*(np.log(v+tau2).sum()+ ((y-mu)**2/(v+tau2)).sum() + math.log(w.sum()))
    res=optimize.minimize_scalar(lambda t:-reml(t),bounds=(0,10),method='bounded')
    tau2=max(0.0,res.x)
    w=1/(v+tau2); mu=(w*y).sum()/w.sum(); se=math.sqrt(1/w.sum())
    Q=float(( (y- ( (1/v*y).sum()/(1/v).sum() ))**2 / v).sum()); df=len(y)-1
    I2=max(0.0,(Q-df)/Q*100) if Q>0 else 0.0
    p_pool=1/(1+math.exp(-mu)); lo=1/(1+math.exp(-(mu-1.96*se))); hi=1/(1+math.exp(-(mu+1.96*se)))
    pi=None
    if len(y)>=10:
        t=stats.t.ppf(0.975,len(y)-2); sd=math.sqrt(tau2+se*se)
        pi=[float(1/(1+math.exp(-(mu-t*sd)))), float(1/(1+math.exp(-(mu+t*sd))))]
    tot_n=sum(a['n'] for a in arms); tot_x=sum(a['x'] for a in arms)
    return dict(label=label,k=len(arms),studies=len(set(a['study'] for a in arms)),total_refs=int(tot_n),total_events=int(tot_x),crude=round(tot_x/tot_n,4),pooled=round(float(p_pool),4),ci=[round(float(lo),4),round(float(hi),4)],tau2=round(float(tau2),4),I2=round(float(I2),1),Q=round(Q,2),prediction_interval=pi)
results={}
datasets={}
for outcome,label in [('n_fabricated','fabricated'),('n_major_inaccuracy_incl_fabricated','major_inaccuracy'),('n_fully_accurate','fully_accurate')]:
    arms=arms_for(outcome); datasets[label]=arms
    with open(base+f"analysis-{label}.csv","w",newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(arms[0].keys())); w.writeheader(); w.writerows(arms)
    results[label]=pool(arms,label)
    # per-study sensitivity: sum arms within study
    by={}
    for a in arms: by.setdefault(a['study'],[]).append(a)
    sarms=[dict(study=s,n=sum(x['n'] for x in v),x=sum(x['x'] for x in v)) for s,v in by.items()]
    for a in sarms: a.update(family='',retrieval='',pub='',year='',topic='',specialty='',requested=None,arm='(study total)',record='')
    results[label+"_per_study"]=pool(sarms,label+"_per_study")
    # subgroups
    def sub(keyfn,name):
        groups={}
        for a in arms: groups.setdefault(keyfn(a),[]).append(a)
        results[f"{label}_sub_{name}"]={g:pool(v,f"{label}:{g}") for g,v in sorted(groups.items()) if len(v)>=2}
    sub(lambda a:(a['family'] or 'not_reported'),'family')
    sub(lambda a:a['retrieval'],'retrieval')
    sub(lambda a:('>10' if a['requested'] and a['requested']>10 else '<=10' if a['requested'] else 'not_reported'),'listlen_requested')
    sub(lambda a:(a['pub'] or 'nr'),'pubtype')
    sub(lambda a:('<=2023' if (a['year'] and a['year']<='2023') else '2024' if a['year']=='2024' else '2025+' if a['year'] and a['year']>='2025' else 'nr'),'modelyear')
# sensitivity: leave-one-model-family-out (fabricated + fully accurate), preprints removed
for label in ('fabricated','fully_accurate'):
    arms=datasets[label]
    fams=sorted(set(a['family'] for a in arms if a['family']))
    results[label+'_lofo']={f:pool([a for a in arms if a['family']!=f],label+' minus '+f) for f in fams}
    results[label+'_no_preprints']=pool([a for a in arms if a['pub']=='peer_reviewed'],label+' peer-reviewed only')
json.dump(results,open(base+"stage4/analysis-results.json","w"),indent=1)
for k,v in results.items():
    if isinstance(v,dict) and 'pooled' in v: print(k, "k=",v['k'],"studies=",v['studies'],"pooled=",v['pooled'],v['ci'],"I2=",v['I2'],"tau2=",v['tau2'],"PI=",v['prediction_interval'])
    elif isinstance(v,dict): print(k,{g:(x.get('pooled'),x.get('k')) for g,x in v.items()})
    else: print(k,v)
