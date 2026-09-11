# INDEX — the complete map of the FTGB jewel

Every document and directory, by purpose. New here? → **[`START_HERE.md`](START_HERE.md)**. Reproduce? →
**[`REPRODUCE.md`](REPRODUCE.md)**. What's proven vs frontier? → START_HERE's map + **[`results/TIER_LEDGER.md`](results/TIER_LEDGER.md)**.

## Front door & navigation
| File | What |
|---|---|
| [`START_HERE.md`](START_HERE.md) | routes by intent; the **settled-vs-frontier** trust map; the falsifiers |
| [`README.md`](README.md) | package overview, CI badge, the bundle table |
| [`INDEX.md`](INDEX.md) | **this file** — the complete document map |
| [`REPRODUCE.md`](REPRODUCE.md) | run-access for every derivation (tiers A–D + doc build) |
| [`NOTATION.md`](NOTATION.md) | the symbol / notation reference (λ, `Q_H`, `C`, `v_A`, …) |
| [`GLOSSARY.md`](GLOSSARY.md) | terms & concepts, tier-tagged (incl. §8 Reeb/contact/regularity) |
| [`REFERENCES.md`](REFERENCES.md) | consolidated, tiered citations |

## The theory (readable)
| File | What |
|---|---|
| [`FTGB_PLAIN_LANGUAGE_BRIEF_2026-09-10.md`](FTGB_PLAIN_LANGUAGE_BRIEF_2026-09-10.md) (+PDF) | ~9-page general-audience tour |
| [`FTGB_GRAND_SYNTHESIS.md`](FTGB_GRAND_SYNTHESIS.md) (+PDF) | the full tiered synthesis (Parts A–G); **§A.3 = "coherence is regularity"** |
| `FTGB_GRAND_SYNTHESIS_FULL_2026-09-10.pdf` | the compiled jewel as one shareable paper |
| [`FTGB_CURRENTLEG_TRILOGY.md`](FTGB_CURRENTLEG_TRILOGY.md) (+PDF) | the self-contained `[V]` lead result |
| [`FTGB_COHERENCE_MAP_2026-09-09.md`](FTGB_COHERENCE_MAP_2026-09-09.md) | the layer stack ordering the frameworks |
| [`LINEAGE.md`](LINEAGE.md) | the Bostick / Puthoff / Shoulders lineage |

## Foundation & math
| File | What |
|---|---|
| [`MATH_TOOLKIT_BASE.md`](MATH_TOOLKIT_BASE.md) | the shared foundation (§1 CK/Beltrami … §9 topology, §4b R2); per-claim index B-1…B-30 |
| [`foundation/30_CANONICAL_NUMBERS.md`](foundation/30_CANONICAL_NUMBERS.md) | the single source of truth for the anchors & derived numbers |
| [`V_A_RESIDUAL_AND_ABSOLUTE_MAGNITUDES.md`](V_A_RESIDUAL_AND_ABSOLUTE_MAGNITUDES.md) | the one caveat for absolute magnitudes |

## Toolkit (method modules M7–M15)
| File | What |
|---|---|
| [`TOOLKIT_HANDBOOK.md`](TOOLKIT_HANDBOOK.md) | consolidated handbook (M7–M15) |
| [`toolkit/`](toolkit/) | the nine modules: M7 Buckingham-Π · M8 QWM · M9 coupled-oscillator · M10 topological-soliton · M11 EGM/PV · M12 Ginzburg · M13 TUFT mass-tower · M14 Greenyer beat/cascade · M15 Reeb & spectral geometry |

## Results, assessments & governance
| File | What |
|---|---|
| [`results/`](results/) | executed advances: R2/R3 theorems, LENR model, electron torsion-defect, α resolution, chirality/C/Majorana, R3 Hall-smallness, exact-state regularity |
| [`results/TIER_LEDGER.md`](results/TIER_LEDGER.md) | the honest self-assessment (every open item) |
| [`results/COINCIDENCE_LEDGER.md`](results/COINCIDENCE_LEDGER.md) | every coincidence computed & logged as a clue |

## Reproduction, harness & provenance
| File | What |
|---|---|
| [`results/verify/`](results/verify/) | **the reproducible model** — 45 theory scripts; map in [`results/verify/README.md`](results/verify/README.md) |
| [`results/verify/verify_all.py`](results/verify/verify_all.py) | the harness (**47/47**, CI-gated) |
| [`engine/`](engine/) | `ftgb_engine.py` (the object as one executable model) + `ftgb_synthesis_modeler.py` (the isomorph) |
| [`frontier_calcs/`](frontier_calcs/) | vendored (frozen) provenance scripts for the canonical numbers + toolkit-module methods |
| [`toroidal_core/`](toroidal_core/) | vendored (frozen) core-derivation package (`fields.py`, `madelung.py`, `topology.py`, …) |
| [`freefem/`](freefem/) | vendored (frozen) FreeFEM torus eigensolves (finite-ε `c_CK`, the doublet) |
| [`handoffs/`](handoffs/) | the two open heavy computes (R2-at-Reynolds solver + spec; Δ B=4 Skyrme spec) |
| [`paper/`](paper/) | the manuscript build (`assemble.py` → pandoc → Chrome; `BUILD.md`) |
| [`.github/workflows/verify.yml`](.github/workflows/verify.yml) | CI: runs `verify_all.py` on every push |
| [`requirements.txt`](requirements.txt) · [`CITATION.cff`](CITATION.cff) · [`RELEASE.md`](RELEASE.md) | deps · citation metadata · release/DOI checklist |

## Interactive models (double-click, any OS)
| File | What |
|---|---|
| `index.html` | the coherent-object modeler (point → string → resonator → knot → dynamics) |
| `resonator_family.html` | the one object at five resonance conditions |
| `soliton3d.html` · `dynamics_lab.html` · `electron.html` · `coherence.html` | facet views (torus, live dynamics, electron rung, the coherence stack) |

*Everything load-bearing has a script; every claim carries a tier; no number is fabricated; settled-negatives
are kept as wins. Reproduce: `pip install -r requirements.txt && python results/verify/verify_all.py`.*
