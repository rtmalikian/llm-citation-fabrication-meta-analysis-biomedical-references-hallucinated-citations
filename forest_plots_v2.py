"""Review 2 forest plots v2 (fix, 22 Oct 2026).
Changes from v1: (1) every plot now draws the random-effects summary as a
DIAMOND (centre = pooled proportion, tips = 95% CI) on its own row, with the
prediction interval as a capped line under it where available; (2) squares are
sized by arm size; (3) arm-level plots are split into panels of <=22 arms so no
panel is taller than a page when printed; (4) a study-level main plot per
outcome (one row per study) is produced for the manuscript body; (5) x axis is
fixed 0-1 and the axis label sits inside the figure.
All numbers come from stage4/analysis-results.json and the analysis-*.csv arm
datasets produced by analysis.py. No number is recomputed here except Wilson
intervals for display and per-study totals (sums of the arm rows)."""
import csv, math, json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import matplotlib.lines as mlines

base = "/home/hatch/workspace/publications/weekly-series/meta-analysis-llm-citation-fabrication/review2/"
res = json.load(open(base + "stage4/analysis-results.json"))
RED = "#b3001b"

def wilson(x, n):
    p = x / n; z = 1.96
    d = 1 + z * z / n; c = p + z * z / (2 * n)
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - m) / d, (c + m) / d

def draw(rows, pooled, ci, pi, title, outfile, diamond_label):
    """rows: list of (label, x, n) sorted as they should appear top->bottom."""
    k = len(rows)
    fig_h = max(3.2, (k + 3) * 0.30)
    fig, ax = plt.subplots(figsize=(10.5, fig_h))
    # data rows: y = k-1 .. 0 (first row at top)
    for i, (lab, x, n) in enumerate(rows):
        y = k - 1 - i
        p = x / n; lo, hi = wilson(x, n)
        ax.plot([lo, hi], [y, y], color="#444444", lw=1, zorder=2)
        ax.plot([p], [y], marker="s", color=RED, ms=max(3.5, min(9, math.sqrt(n) / 3.2)), zorder=3)
        ax.text(1.015, y, f"{x}/{n}  {p*100:.1f}%", va="center", ha="left", fontsize=7.5, transform=ax.get_yaxis_transform() if False else None) if False else None
    # use axes-fraction x for the right-hand text via blended transform
    from matplotlib.transforms import blended_transform_factory
    bt = blended_transform_factory(ax.transAxes, ax.transData)
    for i, (lab, x, n) in enumerate(rows):
        y = k - 1 - i
        p = x / n
        ax.text(1.01, y, f"{x}/{n}  {p*100:.1f}%", va="center", ha="left", fontsize=7.5, transform=bt)
    ax.text(1.01, k + 0.55, "events/total  %", va="center", ha="left", fontsize=7.5, fontweight="bold", transform=bt)
    # summary diamond row at y = -1.6, prediction interval at y = -2.6
    dy = -1.7
    diamond = Polygon([(ci[0], dy), (pooled, dy + 0.42), (ci[1], dy), (pooled, dy - 0.42)],
                      closed=True, facecolor=RED, edgecolor=RED, zorder=4)
    ax.add_patch(diamond)
    ax.text(1.01, dy, diamond_label, va="center", ha="left", fontsize=7.5, fontweight="bold", transform=bt)
    last = dy
    if pi:
        py = dy - 1.15
        ax.plot([pi[0], pi[1]], [py, py], color=RED, lw=2.2, zorder=3)
        ax.plot([pi[0], pi[0]], [py - 0.22, py + 0.22], color=RED, lw=2.2)
        ax.plot([pi[1], pi[1]], [py - 0.22, py + 0.22], color=RED, lw=2.2)
        ax.text(1.01, py, f"PI {pi[0]*100:.1f} to {pi[1]*100:.1f}%", va="center", ha="left", fontsize=7.5, transform=bt)
        last = py
    ax.set_yticks(list(range(k)))
    ax.set_yticklabels([r[0] for r in rows][::-1], fontsize=7.5)
    ax.set_ylim(last - 0.9, k + 0.4)
    ax.set_xlim(0, 1)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"], fontsize=8)
    ax.set_xlabel("Proportion of generated references (point estimate, 95% Wilson CI; diamond = random-effects pooled proportion)", fontsize=8.5)
    ax.set_title(title, fontsize=10.5, pad=24)
    ax.axvline(pooled, color=RED, ls="--", lw=0.8, zorder=1)
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.tick_params(axis="y", length=0)
    plt.tight_layout()
    plt.savefig(base + outfile, dpi=200)
    plt.close()
    print("saved", outfile)

OUTCOMES = [
    ("fabricated", "fabricated", "completely fabricated"),
    ("major_inaccuracy", "major inaccuracy", "with any major inaccuracy"),
    ("fully_accurate", "fully accurate", "fully accurate"),
]

for label, reskey, pretty in OUTCOMES:
    arms = list(csv.DictReader(open(base + f"analysis-{label}.csv")))
    pooled = res[label]["pooled"]; ci = res[label]["ci"]; pi = res[label].get("prediction_interval")
    dl = f"Pooled {pooled*100:.1f}% ({ci[0]*100:.1f} to {ci[1]*100:.1f})"
    # --- study-level main plot ---
    by = {}
    for a in arms:
        s = by.setdefault(a["study"], [0, 0]); s[0] += int(a["x"]); s[1] += int(a["n"])
    srows = sorted([(s, v[0], v[1]) for s, v in by.items()], key=lambda r: r[1] / r[2], reverse=True)
    draw(srows, pooled, ci, pi,
         f"Forest plot by study: {pretty} (diamond = arm-level pool, k={res[label]['k']} arms, I2={res[label]['I2']}%)",
         f"forest-{label}-bystudy.png", dl)
    # --- arm-level panels, <=22 arms each ---
    arows = sorted([(f"{a['study']} | {a['arm']}", int(a["x"]), int(a["n"])) for a in arms],
                   key=lambda r: r[1] / r[2], reverse=True)
    CH = 22
    panels = [arows[i:i + CH] for i in range(0, len(arows), CH)] or [arows]
    for pi_idx, panel in enumerate(panels):
        last_panel = pi_idx == len(panels) - 1
        rows = panel
        # diamond only on the final panel (it pools all arms); other panels get it too but labelled as overall
        draw(rows, pooled, ci, pi if last_panel else None,
             f"Forest plot by model arm ({pi_idx+1} of {len(panels)}): {pretty} (diamond = overall pool)",
             f"forest-{label}-arms-{pi_idx+1}.png", dl)
print("done")
