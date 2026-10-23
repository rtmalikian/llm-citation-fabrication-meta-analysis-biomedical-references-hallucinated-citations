import csv, math, json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
base="/home/hatch/workspace/publications/weekly-series/meta-analysis-llm-citation-fabrication/review2/"
res=json.load(open(base+"stage4/analysis-results.json"))
for label,outcome in [('fabricated','fabricated'),('fully_accurate','fully accurate'),('major_inaccuracy','major inaccuracy')]:
    arms=list(csv.DictReader(open(base+f"analysis-{label}.csv")))
    arms.sort(key=lambda a: float(a['x'])/float(a['n']))
    fig_h=max(6, len(arms)*0.32)
    fig,ax=plt.subplots(figsize=(10,fig_h))
    ys=[]
    for i,a in enumerate(arms):
        n=int(a['n']); x=int(a['x']); p=x/n
        # Wilson CI
        z=1.96; d=1+z*z/n; c=p+z*z/(2*n); m=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))
        lo=(c-m)/d; hi=(c+m)/d
        ax.plot([lo,hi],[i,i],color="#444",lw=1); ax.plot([p],[i],marker='s',color="#b3001b",ms=4)
        ys.append(f"{a['study']} | {a['arm']}  {x}/{n}")
    pooled=res[label]['pooled']; ci=res[label]['ci']
    ax.axvline(pooled,color="#b3001b",ls="--",lw=1)
    ax.set_yticks(range(len(arms))); ax.set_yticklabels(ys,fontsize=7)
    ax.set_xlabel(f"Proportion {outcome} (point, 95% Wilson CI; dashed line = random-effects pooled {pooled:.3f}, {ci[0]:.3f} to {ci[1]:.3f})")
    ax.set_title(f"Forest plot: {outcome} per model arm (k={res[label]['k']} arms, {res[label]['studies']} studies, I2={res[label]['I2']}%)",fontsize=10)
    plt.tight_layout(); plt.savefig(base+f"forest-{label}.png",dpi=200); plt.close()
    print(label,"saved")
# totals hand-check
for label in ['fabricated','major_inaccuracy','fully_accurate']:
    arms=list(csv.DictReader(open(base+f"analysis-{label}.csv")))
    print(label, "total x", sum(int(a['x']) for a in arms), "total n", sum(int(a['n']) for a in arms), "crude", round(sum(int(a['x']) for a in arms)/sum(int(a['n']) for a in arms),4), "json crude", res[label]['crude'])
