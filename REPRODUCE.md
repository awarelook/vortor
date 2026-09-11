# REPRODUCE — everything needed to re-run the FTGB jewel

The definitive run-access map: every math derivation, its script, its dependencies, and the exact command —
grouped by how much you need installed. **Tier A is the whole load-bearing core and needs nothing but Python
+ two pip packages.** The rest is provenance / refinement / heavy compute, each honestly labelled.

## Environment

- **CPython 3.12** (tested 3.12.10). Core deps **pinned**: `numpy==2.4.6`, `mpmath==1.3.0`.
- Everything in Tier A is **deterministic, offline, seconds-per-script**. The CI runs it on every push
  (`.github/workflows/verify.yml`) on a clean Ubuntu image — the green badge is your reproduction proof.

---

## Tier A — the CI-gated core (Python + numpy + mpmath) · **the whole `[V]` model**

```bash
pip install -r requirements.txt          # numpy, mpmath
python results/verify/verify_all.py      # 50/50 PASS, exit 0 iff all pass
```

`verify_all.py` globs every `results/verify/*.py` (48 theory scripts) + the two engine files
(`engine/ftgb_engine.py`, `engine/ftgb_synthesis_modeler.py`) = **50 checks**. This reproduces the entire
load-bearing model: the CK spectrum, R2/R3 fluid theorems, exact-state regularity, the topological
invariants `Q_H=1`/`C=±2`, the Reeb/contact + curl-spectrum results, the chirality/C/Majorana cluster, the
curl spectral zeta, the cascade, the α settled-negatives, the LENR energy ledger, and the canonical-number
provenance + v_A-invariance. Per-script map: **`results/verify/README.md`**. Run one script directly, e.g.:

```bash
python results/verify/exact_beltrami_regularity_check.py     # any single derivation, standalone
python engine/ftgb_engine.py                                 # the object as one executable model
python engine/ftgb_synthesis_modeler.py                      # the MATH<->PHYSICS<->EXPERIMENT isomorph
```

## Tier B — extended provenance (adds scipy / sympy) · frozen ckfreefem scripts

The full provenance derivations behind the canonical numbers are vendored (frozen) in **`frontier_calcs/`**
(manifest there). Seven run on the Tier-A stack; three need extra pip packages:

```bash
pip install scipy sympy
python frontier_calcs/polarizable_medium_resonator_derivation.py   # §I resonator spectrum (scipy)
python frontier_calcs/ws6_cCK_convergence_and_analytic_limit.py    # c_CK convergence (scipy)
python frontier_calcs/exploratory_a6_radiation_suppression_exponent.py  # anapole exponent (sympy)
```

The two most load-bearing of these (`Q_H` via the Whitehead integral; the `c_CK` CK limit) are *also*
reproduced inside the Tier-A gate (`topology_invariants_check.py`, `ck_eigenvalues_check.py`) — so the core
does not depend on scipy.

## Tier C — the FreeFEM torus eigensolves (needs the FreeFEM binary) · `[V, FE]` refinement

The finite-`ε` **toroidal** CK eigenvalues (the golden-aspect `c_CK(1/φ)=0.2234`, the Beat-Law doublet) are
computed with FreeFEM. Scripts vendored (frozen) in **`freefem/`** (manifest there); install FreeFEM
(<https://freefem.org>), then:

```bash
FreeFem++ freefem/stage3_torus_doublet.edp        # the doublet lambda_0(eps), lambda_1(eps)
FreeFem++ freefem/stage3_sphere_validate.edp      # sphere limit recovers tan x = x = 4.4934
FreeFem++ freefem/greenyer_frontier_cCK_general_eps_sweep.edp   # c_CK(eps) -> 0.2234 at eps=1/phi
```

**Not required for the core:** the load-bearing CK spectrum (`tan x = x`, `c_CK(ε→0)=0.20792`) is in Tier A.
FreeFEM is only for the finite-`ε` torus refinement.

## Tier D — heavy / open compute (HPC / GPU) · runnable references + specs

The two hardest open computations are **packaged, not asserted** (`handoffs/`):

- **R2 at Reynolds** — `handoffs/r2_reference_solver.py` is a runnable reference pseudo-spectral solver;
  `handoffs/R2_NUMERICAL_RUN_SPEC_2026-09-10.md` scopes the `N~192–1024` GPU run a collaborator scales up.
  Upgrades the R2 core from `[V]cond` toward `[V]` at-Reynolds.
- **Δ (B=4 branching)** — `handoffs/HANDOFF_DELTA_B4_SKYRME_RELAXATION_2026-09-09.md`: a topology-preserving
  Skyrme-HPC relaxation spec (closes the LENR rate). HPC-only; a spec, honestly not run here.

## Doc build — the manuscripts & PDFs (pandoc + headless Chrome)

The paper/brief PDFs are assembled and printed (details in **`paper/BUILD.md`**):

```bash
python paper/assemble.py                 # -> paper/master.md (concatenates the sources)
pandoc paper/master.md -s --toc --embed-resources -c paper/paper.css -o master.html
chrome --headless=new --print-to-pdf=out.pdf master.html    # any headless-Chromium
```

---

## Derivation → run map (at a glance)

| Derivation family | Where | Deps | Command |
|---|---|---|---|
| CK carrier spectrum, ratios | `ck_eigenvalues_check.py` | A | `verify_all.py` |
| R2 / R3 fluid theorems, exact-state regularity | `r2_*`, `hallmhd_*`, `exact_beltrami_*`, `r3_hall_*` | A | `verify_all.py` |
| Topology `Q_H=1`, `C=±2` | `topology_invariants_check.py` | A | `verify_all.py` |
| Reeb/contact + curl spectrum (M15) | `reeb_spectral_geometry_check.py` | A | `verify_all.py` |
| chirality / C / Majorana | `chirality_*`, `charge_conjugation_*`, `majorana_*` | A | `verify_all.py` |
| curl spectral zeta / mass tower | `curl_spectral_zeta_pi_power_check.py`, `tuft_mass_tower_check.py` | A | `verify_all.py` |
| cascade / beat / triad | `greenyer_beat_cascade_check.py` | A | `verify_all.py` |
| α settled-negatives | `alpha_*`, `ck_winding_ratio_check.py` | A | `verify_all.py` |
| LENR energy ledger | `lenr_*`, `delta_detuning_beat_check.py` | A | `verify_all.py` |
| canonical numbers + v_A invariance | `canonical_numbers_provenance_check.py`, `absolute_magnitude_invariance_check.py` | A | `verify_all.py` |
| full provenance derivations | `frontier_calcs/*.py` | A / B | per script |
| finite-`ε` torus eigenvalues | `freefem/*.edp` | C (FreeFEM) | `FreeFem++ …` |
| R2-at-Reynolds / Δ B=4 | `handoffs/` | D (GPU/HPC) | reference solver + spec |
| manuscripts / PDFs | `paper/` | pandoc+Chrome | `paper/BUILD.md` |

**Nothing load-bearing is out of reach:** the entire `[V]` core is Tier A (numpy+mpmath, CI-gated). Tiers
B–D are provenance, finite-element refinement, and honestly-open heavy compute — each vendored or scoped, none
hand-waved. See `START_HERE.md` for the settled-vs-frontier map and `results/TIER_LEDGER.md` for the honest
self-assessment.
