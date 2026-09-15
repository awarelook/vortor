# START HERE — the FTGB coherent object

[![verify](https://github.com/awarelook/vortor/actions/workflows/verify.yml/badge.svg)](https://github.com/awarelook/vortor/actions/workflows/verify.yml)

One driven, force-free **Beltrami–Hopf toroidal soliton**, read at once as a *field* and a *matter wave*.
Every claim carries an **honest tier**, and the whole model reproduces from one command. This page routes you
by what you want, and — most importantly — shows you exactly **what is settled vs what is frontier**, because
the honest boundary is this project's most valuable feature.

## Route by intent

| I want to… | Go to |
|---|---|
| **Reproduce it from scratch** (82 checks, no network) | `pip install -r requirements.txt && python results/verify/verify_all.py` → exit 0. Map: [`results/verify/README.md`](results/verify/README.md). CI runs this on every push (badge above). **Full run-access for *every* derivation (incl. scipy/sympy provenance, FreeFEM torus eigensolves, HPC handoffs, doc build): [`REPRODUCE.md`](REPRODUCE.md).** |
| **Read the whole theory in one page** | [`FTGB_MINIMUM_VIABLE_PAPER.md`](FTGB_MINIMUM_VIABLE_PAPER.md) — the capstone: apex summary + proven core + hypothesis-to-test + LENR significance + falsifiers, tight and citable. |
| **See what FTGB explains vs leaves open across the LENR anomaly landscape** | [`results/LENR_EXPLANATORY_RESOLUTION_MAP_2026-09-14.md`](results/LENR_EXPLANATORY_RESOLUTION_MAP_2026-09-14.md) — the tiered map (heat-helium, branching, transmutation, SAFIRE/EVO/Aureon), convergence ranking, novelty audit, and the disposal chain converging the one open problem to the entrance-channel assembly geodesic. The breakthrough stated honestly: a falsifiable *program*, not a proof. |
| **Understand it in ~9 pages** | [`FTGB_PLAIN_LANGUAGE_BRIEF_2026-09-10.md`](FTGB_PLAIN_LANGUAGE_BRIEF_2026-09-10.md) (also PDF) — general-audience, honestly tiered. |
| **Read the full theory** | [`FTGB_GRAND_SYNTHESIS.md`](FTGB_GRAND_SYNTHESIS.md) (Parts A–G). The deep organizing principle is **§A.3** ("coherence *is* regularity"). |
| **Check what's actually proven** | the **settled vs frontier map** below, and [`results/TIER_LEDGER.md`](results/TIER_LEDGER.md) (the honest self-assessment). |
| **See it as one executable object** | `python engine/ftgb_synthesis_modeler.py` — the MATH ↔ PHYSICS ↔ EXPERIMENT isomorph with its honest seams. |
| **Watch it run as a simulation** | `python engine/ftgb_resonator_sim.py` — the oscillating harmonic resonator matter wave in software: full nonlinear NS evolution of the eternal Beltrami state, the CK comb + kHz beats, the driven Lorentzian, the de Broglie packet. |
| **Try to kill it** | the **falsifiers** below. |
| **Cite an absolute number (Hz/T/eV)** | read [`V_A_RESIDUAL_AND_ABSOLUTE_MAGNITUDES.md`](V_A_RESIDUAL_AND_ABSOLUTE_MAGNITUDES.md) **first** — absolutes carry a band; ratios don't. |
| **Map every document** | [`INDEX.md`](INDEX.md) — the complete document map, by purpose. |
| **Look up a symbol or term** | [`NOTATION.md`](NOTATION.md) (symbols: λ, `Q_H`, `C`, `v_A`, …) · [`GLOSSARY.md`](GLOSSARY.md) (concepts, incl. §9 plasmoid/EVO/CMNS vocabulary) · [`REFERENCES.md`](REFERENCES.md) (citations, incl. §1e–1j salvage clusters). |
| **The history: plasmoids, EVOs, cold fusion** | [`HISTORY_PEOPLE_EVO_CMNS.md`](HISTORY_PEOPLE_EVO_CMNS.md) — the tiered science timeline + people roster + the record and its fences · deep-dives in [`LINEAGE.md`](LINEAGE.md). |

## Settled vs frontier — the trust map

The single most important thing to understand: this object has a **rigorous `[V]`/`[credited]` core** and a
**disciplined `[S]`/frontier wrapper**, and they are never conflated. Judge each by its tier.

### ✅ SETTLED — the citable core (`[V]` verified in-repo / `[credited]` established)
- **CK/Beltrami carrier spectrum** — roots of `tan x = x`, ratios `1 : 1.719 : 2.427` `[V]`.
- **R2 / R3 fluid theorems** — the exact Lamb-vector identity; the near-Beltrami enstrophy/BKM bound `[V-cond]`; the Hall `Pm≠1` coupled-Lyapunov lift `[V-cond]`.
- **Exact-state global regularity** — the coherent object *as its force-free state* is an eternal smooth solution; the nonlinearity is null at coherence `[V]` (§A.3).
- **Topology** — Hopf charge `Q_H = 1` (of the idealized closed-fibre *reference* field — the actual CK object carries real helicity `H≈0.088`, Grand Synthesis C.2) and wave-mode Chern `C = ±2`, both computed in-repo `[V]`; a credited convergence with the photon's helicity index.
- **Reeb / contact + Weinstein–Taubes** — the Beltrami field is a Reeb field; the coherent loop *exists* by topology `[credited]` (M15).
- **Chirality / C / Majorana** — chirality = `sign λ` = `sign H`; mirror = C; neutrino = self-dual `θ_χ=45°` — the *algebra* `[V, computed]`; the QFT-contact (the C/Majorana *dictionary*) `[S]` (TIER_LEDGER row: structurally like C, not the QFT `C=iγ²γ⁰`).
- **Spectral geometry** — the `S³` curl spectral zeta `ζ′(−2) = −ζ(3)/4π²` (resolves the π-power anomaly) `[V]`.

### 🔬 FRONTIER — honestly speculative (`[S]` / open / settled-negative)
- **The matter-wave reading** (electron = this soliton; `m = ħω/c²`; charge = torsion defect) — `[S]`, the interpretive layer.
- **α's *value*** — **settled-negative**: the winding = 137 derivation fails (`ι ≈ 1`, not 137); α is correctly *typed* by several lenses but *not derived*, value open.
- **g = 2** — its *meaning* is derived (minimal-coupling limit); the `π₁/π₃` lock stays `[S]`.
- **LENR** — energy bookkeeping `[V]` (d+d→⁴He = 23.847 MeV, conserved, no over-unity); the γ-quiet disposal *operator* is **E0**/collective `[credited]`; *mechanism* `[S]`. **The one open problem is now CONVERGED and narrow** (a 7-check disposal chain): the **entrance-channel assembly geodesic** — can coherent slow assembly beat the *measured* `~10⁻⁷` aneutronic baseline (steering the B=4/B=8 Skyrme trajectory to the compact bound ⁴He)? = the moduli-space/HPC run. *(Sharpened same day: ⁴He has **no bound excited states** and supra-threshold dwell dies in zeptoseconds, so the only route is a **dissipative sub-breakup corridor** shedding the full 23.85 MeV during assembly — `entrance_corridor_survival_check` — with **two data bars**: existence `>10⁻⁷`; sufficiency `n/⁴He ≤ 10⁻⁹`, deriving the crossing fence `β·|dF| ≤ 0.874 MeV/fm` — LZ bridge TEST 2b.)* The anapole is the **active site** (slow confinement/coherence at assembly), **not** the 24-MeV disposal operator. Full tiered map: [`results/LENR_EXPLANATORY_RESOLUTION_MAP_2026-09-14.md`](results/LENR_EXPLANATORY_RESOLUTION_MAP_2026-09-14.md).
- **The kHz-beat "pump" of the MeV channel** — **settled-negative** (M16): a slow kHz beat is 15.7–16.8 OOM too slow to parametrically pump a MeV mode; the literal `kHz = MeV gap` identity is **dead**, doubly-closed. The macroscopic beat survives only as a falsifiable rate-*gate* `[S]`, never an energy pump.
- **Mass hierarchy** — the analytic-torsion dressing derives the *order* `[framework/S]`; exact ratios are a `[preprint-claim]`.
- **Absolute magnitudes** — carry the `v_A` residual band; only ratios are load-bearing.

## How to kill it (the sharp falsifiers)

A theory worth trusting says how to break it. These would:
- **He-4 / excess-heat correlation** off the 23.847 MeV/⁴He line → kills the LENR energy reading.
- **`0νββ` null** (KamLAND-Zen / LEGEND) → kills the Majorana-neutrino prediction (and favors TUFT's Dirac).
- **Neutron yield scaling with heat** → **the primary, band-independent kill** of the aneutronic channel (its ~10⁻⁷→dominance suppression is the open entrance-channel-assembly question, not a symmetry).
- **The parameter-free scalar tests** (`30_CANONICAL_NUMBERS.md` §G) failing → kills the calibration-free predictions.
- **A harmonic (not inharmonic) carrier comb, *in the linear/low-drive limit*** → kills the CK-spectrum fingerprint (M16: under hard drive the ratios pull anharmonically — the Duffing backbone bend is separable from the Arnold-tongue lock, so the test is a linear-limit statement).
- **`b_eff ≠` magnetic energy per ion** in a second plasmoid → kills the medium-reduction closed form.
- Full numbered falsifier set — including the **E0 internal-pair secondary** (~20 MeV `e⁺e⁻` / 511 keV) and the **beat-locked yield step `f_b(L)=N^L`** (the sharpest theory-specific discriminator): [`FTGB_MINIMUM_VIABLE_PAPER.md`](FTGB_MINIMUM_VIABLE_PAPER.md) §5.

## Reproduce & trust

```
pip install -r requirements.txt
python results/verify/verify_all.py      # 82/82 PASS, deterministic, no network
```

Everything load-bearing has a script; the foundation numbers are re-derived in-repo
(`canonical_numbers_provenance_check.py`) with the provenance scripts vendored under `frontier_calcs/`.
No claim exceeds its tier; no number is fabricated; settled-negatives are kept as wins.
