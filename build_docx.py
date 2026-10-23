import re, sys
from docx import Document
from docx.shared import Pt, Inches
base="/home/hatch/workspace/publications/weekly-series/meta-analysis-llm-citation-fabrication/review2/"
doc=Document()
for s in doc.sections: s.left_margin=Inches(0.9); s.right_margin=Inches(0.9)
lines=open(base+"manuscript.md",encoding="utf-8").read().splitlines()
i=0
def clean(t): return re.sub(r'\*\*(.*?)\*\*',r'\1',t).strip()
while i<len(lines):
    line=lines[i]
    if line.startswith("|") and i+1<len(lines) and lines[i+1].startswith("|---"):
        rows=[]
        while i<len(lines) and lines[i].startswith("|"):
            rows.append([clean(c) for c in lines[i].strip().strip('|').split('|')]); i+=1
        rows=[r for r in rows if not all(set(c)<=set('-: ') for c in r)]
        t=doc.add_table(rows=len(rows),cols=len(rows[0])); t.style='Table Grid'
        for ri,r in enumerate(rows):
            for ci,c in enumerate(r): t.cell(ri,ci).text=c
        continue
    if line.startswith("# "): doc.add_heading(clean(line[2:]),level=0)
    elif line.startswith("## "): doc.add_heading(clean(line[3:]),level=1)
    elif line.startswith("### "): doc.add_heading(clean(line[4:]),level=2)
    elif line.strip():
        p=doc.add_paragraph()
        # bold segments
        parts=re.split(r'(\*\*.*?\*\*)',line)
        for part in parts:
            run=p.add_run(part[2:-2] if part.startswith("**") else part)
            if part.startswith("**"): run.bold=True
            run.font.size=Pt(11)
    i+=1
from PIL import Image as PILImage
MAXW, MAXH = 6.7, 8.6
def add_fig(heading, filename, caption=None):
    h = doc.add_heading(heading, level=1)
    h.paragraph_format.keep_with_next = True
    path = base + filename
    iw, ih = PILImage.open(path).size
    scale = min(MAXW / (iw / 200), MAXH / (ih / 200))
    pic = doc.add_picture(path, width=Inches(iw / 200 * scale))
    if caption:
        p = doc.add_paragraph(caption)
        for r in p.runs: r.font.size = Pt(9)
    return pic

doc.add_page_break()
add_fig("Forest plot: completely fabricated, by study", "forest-fabricated-bystudy.png",
        "Figure 1. One row per study (study totals across its model arms). The diamond is the arm-level random-effects pooled proportion, 18.6% (95% CI 12.8 to 26.3); the capped line under it is the 95% prediction interval, 0.9 to 84.7%. The per-study sensitivity pool was 23.0%.")
add_fig("Forest plot: fully accurate, by study", "forest-fully_accurate-bystudy.png",
        "Figure 2. One row per study. Diamond: arm-level pooled proportion fully accurate, 29.4% (95% CI 19.5 to 41.7); capped line: 95% prediction interval. Per-study sensitivity pool 41.2%.")
add_fig("Forest plot: any major inaccuracy, by study", "forest-major_inaccuracy-bystudy.png",
        "Figure 3. One row per study. Diamond: pooled proportion with any major inaccuracy including fabricated, 36.0% (95% CI 19.8 to 56.3), from 9 arms in 5 studies. This figure was missing from the first build and is restored here.")
doc.add_page_break()
doc.add_heading("Appendix figures: forest plots by model arm", level=1)
for f, cap in [
    ("forest-fabricated-arms-1.png", "Fabricated, arms 1 of 3. The diamond on each panel is the overall arm-level pool."),
    ("forest-fabricated-arms-2.png", "Fabricated, arms 2 of 3."),
    ("forest-fabricated-arms-3.png", "Fabricated, arms 3 of 3, with the prediction interval."),
    ("forest-fully_accurate-arms-1.png", "Fully accurate, arms 1 of 2."),
    ("forest-fully_accurate-arms-2.png", "Fully accurate, arms 2 of 2, with the prediction interval."),
    ("forest-major_inaccuracy-arms-1.png", "Any major inaccuracy, all 9 arms."),
]:
    add_fig(cap.split(".")[0], f, cap)
add_fig("PRISMA flow diagram", "prisma-flow-diagram.png")
doc.save(base+"manuscript.docx")
print("docx built v2")
