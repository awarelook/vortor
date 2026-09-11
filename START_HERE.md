# START HERE — the FTGB coherent object

[![verify](https://github.com/awarelook/vortor/actions/workflows/verify.yml/badge.svg)](https://github.com/awarelook/vortor/actions/workflows/verify.yml)

One driven, force-free **Beltrami–Hopf toroidal soliton**, read at once as a *field* and a *matter wave*.
Every claim carries an **honest tier**, and the whole model reproduces from one command. This page routes you
by what you want, and — most importantly — shows you exactly **what is settled vs what is frontier**, because
the honest boundary is this project's most valuable feature.

## Route by intent

| I want to… | Go to |
|---|---|
| **Reproduce it from scratch** (46 checks, no network) | `pip install -r requirements.txt && python results/verify/verify_all.py` → exit 0. Map: [`results/verify/README.md`](results/verify/README.md). CI runs this on every push (badge above). **Full run-access for *every* derivation (incl. scipy/sympy provenance, FreeFEM torus eigensolves, HPC handoffs, doc build): [`REPRODUCE.md`](REPRODUCE.md).** |
| **Understand it in ~9 pages** | [`FTGB_PLAIN_LANGUAGE_BRIEF_2026-09-10.md`](FTGB_PLAIN_LANGUAGE_BRIEF_2026-09-10.md) (also PDF) — general-audience, honestly tiered. |
| **Read the full theory** | [`FTGB_GRAND_SYNTHESIS.md`](FTGB_GRAND_SYNTHESIS.md) (Parts A–G). The deep organizing principle is **§A.3** ("coherence *is* regularity"). |
| **Check what's actually proven** | the **settled vs frontier map** below, and [`results/TIER_LEDGER.md`](results/TIER_LEDGER.md) (the honest self-assessment). |
| **See it as one executable object** | `python engine/ftgb_synthesis_modeler.py` — the MATH ↔ PHYSICS ↔ EXPERIMENT isomorph with its honest seams. |
| **Try to kill it** | the **falsifiers** below. |
| **Cite an absolute number (Hz/T/eV)** | read [`V_A_RESIDUAL_AND_ABSOLUTE_MAGNITUDES.md`](V_A_RESIDUAL_AND_ABSOLUTE_MAGNITUDES.md) **first** — absolutes carry a band; ratios don't. |

## Settled vs frontier — the trust map

The single most important thing to understand: this object has a **rigorous `[V]`/`[credited]` core** and a
**disciplined `[S]`/frontier wrapper**, and they are never conflated. Judge each by its tier.

### ✅ SETTLED — the citable core (`[V]` verified in-repo / `[credited]` established)
- **CK/Beltrami carrier spectrum** — roots of `tan x = x`, ratios `1 : 1.719 : 2.427` `[V]`.
- **R2 / R3 fluid theorems** — the exact Lamb-vector identity; the near-Beltrami enstrophy/BKM bound `[V-cond]`; the Hall `Pm≠1` coupled-Lyapunov lift `[V-cond]`.
- **Exact-state global regularity** — the coherent object *as its force-free state* is an eternal smooth solution; the nonlinearity is null at coherence `[V]` (§A.3).
- **Topology** — Hopf charge `Q_H = 1` and wave-mode Chern `C = ±2`, both computed in-repo `[V]`; a credited convergence with the photon's helicity index.
- **Reeb / contact + Weinstein–Taubes** — the Beltrami field is a Reeb field; the coherent loop *exists* by topology `[credited]` (M15).
- **Chirality / C / Majorana** — chirality = `sign λ` = `sign H`; mirror = C; neutrino = self-dual `θ_χ=45°` `[V, computed]`.
- **Spectral geometry** — the `S³` curl spectral zeta `ζ′(−2) = −ζ(3)/4π²` (resolves the π-power anomaly) `[V]`.

### 🔬 FRONTIER — honestly speculative (`[S]` / open / settled-negative)
- **The matter-wave reading** (electron = this soliton; `m = ħω/c²`; charge = torsion defect) — `[S]`, the interpretive layer.
- **α's *value*** — **settled-negative**: the winding = 137 derivation fails (`ι ≈ 1`, not 137); α is correctly *typed* by several lenses but *not derived*, value open.
- **g = 2** — its *meaning* is derived (minimal-coupling limit); the `π₁/π₃` lock stays `[S]`.
- **LENR** — energy bookkeeping `[V]` (d+d→⁴He = 23.847 MeV, conserved, no over-unity); *mechanism* `[S]`; *rate* open.
- **Mass hierarchy** — the analytic-torsion dressing derives the *order* `[framework/S]`; exact ratios are a `[preprint-claim]`.
- **Absolute magnitudes** — carry the `v_A` residual band; only ratios are load-bearing.

## How to kill it (the sharp falsifiers)

A theory worth trusting says how to break it. These would:
- **He-4 / excess-heat correlation** off the 23.847 MeV/⁴He line → kills the LENR energy reading.
- **`0νββ` null** (KamLAND-Zen / LEGEND) → kills the Majorana-neutrino prediction (and favors TUFT's Dirac).
- **Neutron yield scaling with heat** → kills the aneutronic (E0-suppressed) channel.
- **The parameter-free scalar tests** (`30_CANONICAL_NUMBERS.md` §G) failing → kills the calibration-free predictions.
- **A harmonic (not inharmonic) carrier comb** → kills the CK-spectrum fingerprint.
- **`b_eff ≠` magnetic energy per ion** in a second plasmoid → kills the medium-reduction closed form.

## Reproduce & trust

```
pip install -r requirements.txt
python results/verify/verify_all.py      # 46/46 PASS, deterministic, no network
```

Everything load-bearing has a script; the foundation numbers are re-derived in-repo
(`canonical_numbers_provenance_check.py`) with the provenance scripts vendored under `frontier_calcs/`.
No claim exceeds its tier; no number is fabricated; settled-negatives are kept as wins.
