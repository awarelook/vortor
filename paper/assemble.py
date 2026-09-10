import re, io, os
ROOT = r'f:/vortor'

def strip_yaml(t):
    return re.sub(r'^---\s*\n.*?\n---\s*\n', '', t, count=1, flags=re.S)

def demote(t, by=1):
    """Add `by` levels to every ATX heading, but never inside fenced code blocks."""
    out=[]; fence=None
    for line in t.split('\n'):
        s=line.lstrip()
        fm=re.match(r'^(```+|~~~+)', s)
        if fm:
            tok=fm.group(1)[0]
            if fence is None: fence=tok
            elif fence==tok: fence=None
            out.append(line); continue
        if fence is None:
            m=re.match(r'^(#{1,6})(\s)', line)
            if m:
                lvl=min(len(m.group(1))+by, 6)
                line='#'*lvl + line[len(m.group(1)):]
        out.append(line)
    return '\n'.join(out)

def load(path, by=1):
    t=io.open(os.path.join(ROOT,path), encoding='utf-8').read()
    return demote(strip_yaml(t), by).strip()

PREAMBLE = '''---
title: "The Coherent Object — Grand Synthesis (Full)"
subtitle: "A driven Beltrami–Hopf toroidal soliton across scales: field, matter wave, vacuum, dynamics, and the LENR anomalies — a tiered synthesis"
author: "Nathaniel Hanks"
date: "2026-09-10"
---

**Abstract & scope.** This is the compiled *validated jewel* of the FTGB program: one driven,
force-free Beltrami–Hopf toroidal soliton, read at once as a plasma **field** and a Madelung
**matter wave**, from which mass, spin, charge, topology, a living beat, and the low-energy-nuclear
(LENR/CMNS) anomaly follow under one organizing law. **Part I** is the tiered grand synthesis.
**Part II** is the standalone lead result — the current-leg trilogy (a self-contained plasma /
topological-fluid no-go theorem with a driven-realizability leg). **Part III** collects the
2026-09-09 advances: the R2 near-Beltrami enstrophy theorem (a conditional Beale–Kato–Majda closure
via an exact Lamb-vector identity), its R3 Hall two-fluid lift, the matter-wave LENR interaction
model, the electron-as-torsion-defect reading, and the dynamical reframe of the fine-structure gap.
**Part IV** is the shared glossary and consolidated references, and the four-framework convergence
(Reed QWM, Storti EGM/Quinta Essentia, Nielsen TUFT, Ginzburg spiral). Every claim carries an
explicit tier — `[V]` proven/verified here · `[credited]` established · `[S]` structural/contingent ·
`open` a named external problem · `[framework]` a folded reading. No over-unity is claimed; the
fine-structure value and the LENR branching amplitude are marked open; the `e^(-2/3)` factor is
excised. Load-bearing physics rests on peer-reviewed work.

**Compile note (2026-09-10 recompile).** Regenerated from the corrected sources. The charge/chirality
torsion is now one **frame-closure (Frenet) holonomy** read two ways — the earlier separate
"Cartan/Burgers charge torsion" split is **withdrawn**; it is a geometric phase, **not** a Cartan/Burgers
*connection* torsion nor Einstein–Cartan spacetime torsion. The neutrino rung is committed to **Majorana**
(self-dual `θ_χ = 45°`, `H = 0`, `C`-invariant). Supersedes the 2026-09-09 compile.
'''

PARTS = [
    ("# Part I — The Grand Synthesis", [("FTGB_GRAND_SYNTHESIS.md",1)]),
    ("# Part II — The Current-Leg Trilogy (lead result)", [("FTGB_CURRENTLEG_TRILOGY.md",1)]),
    ("# Part III — Advances (2026-09-09)", [
        ("results/R2_NEAR_BELTRAMI_ENSTROPHY_THEOREM_2026-09-09.md",1),
        ("results/R3_HALLMHD_CANONICAL_ENSTROPHY_2026-09-09.md",1),
        ("results/LENR_MATTERWAVE_INTERACTION_MODEL_2026-09-09.md",1),
        ("results/ELECTRON_TORSION_DEFECT_EXPLANATION_2026-09-09.md",1),
        ("results/ALPHA_DYNAMICAL_REFRAME_2026-09-09.md",1),
        ("FTGB_COHERENCE_MAP_2026-09-09.md",1),
    ]),
    ("# Part IV — Glossary, References, and the Four-Framework Convergence", [
        ("GLOSSARY.md",1),
        ("REFERENCES.md",1),
    ]),
]

chunks=[PREAMBLE]
for hdr, files in PARTS:
    chunks.append("\n"+hdr+"\n")
    for path, by in files:
        chunks.append(load(path, by)+"\n\n---\n")

out="\n".join(chunks)
io.open(os.path.join(ROOT,'paper','master.md'),'w',encoding='utf-8').write(out)
print("paper/master.md:", len(out), "chars,", out.count('\n#'), "headings-ish")
