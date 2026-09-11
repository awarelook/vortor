# `frontier_calcs/` — vendored provenance scripts (frozen)

**What this is.** The `30_CANONICAL_NUMBERS.md` foundation table and `MATH_TOOLKIT_BASE.md` cite these
scripts as the provenance of several `[V]` anchor numbers. They originated in the external **ckfreefem**
corpus (`03_paper/main_draft/frontier_calcs/` and `ckfreefem/frontier_calcs/`). They are **vendored here as
frozen copies** so the jewel's foundation is *self-contained* — a reader who clones this repo can now see
exactly how every cited canonical number was produced, without needing the external corpus.

**Frozen, not maintained.** These are a provenance record, byte-for-byte as they produced the canonical
numbers. They are **not** part of the reproducibility gate (`verify_all.py`) — that gate is the curated,
`numpy`+`mpmath`-only theorem suite. Instead, the load-bearing *derived* numbers are re-derived from the
anchors, CI-gated, by **`results/verify/canonical_numbers_provenance_check.py`** (which reproduces `v_A`,
`B`, `b_eff`, `ħ_eff`, `d_i` from the closed forms to ≤0.1%). The scripts below are the full derivations
behind that summary.

## Manifest

| Script | Produces / checks | Deps | In CI stack? |
|---|---|---|---|
| `ws5_hbar_b_eff_reduction_to_medium.py` | `b_eff`, `ħ_eff` closed forms from anchors (§A); `b_eff` = magnetic energy/ion | numpy | ✓ runs |
| `qhd_coherence_carrier_mass_resolution.py` | type-II κ, winding protection, carrier-mass reduction (§B) | numpy | ✓ runs |
| `greenyer_real_hopf_charge_whitehead_integral.py` | `Q_H` via the Whitehead integral (§F) — also reproduced in-repo by `topology_invariants_check.py` | numpy | ✓ runs |
| `benchtop_quadruplet_decisive_neumann_crosscheck.py` | benchtop quadruplet `k=M/L` cross-check (§D) | numpy | ✓ runs |
| `polarizable_medium_resonator_derivation.py` | polarizable-medium resonator spectrum (§I) | numpy, **scipy** | needs scipy |
| `ws6_cCK_convergence_and_analytic_limit.py` | `c_CK` convergence / analytic limit (§C) — CK limit also in `ck_eigenvalues_check.py` | numpy, **scipy** | needs scipy |
| `exploratory_a6_radiation_suppression_exponent.py` | anapole radiation-suppression exponent (exploratory) | **sympy** | needs sympy |
| `tae_beat_from_geometry.py` | TAE beat frequency from geometry | numpy | ✓ runs |
| `tension_T1_T2_resolution.py` | the `v_A` residual blast-radius audit (T1/T2, square-law correction, §A) | numpy | ✓ runs |
| `vacuum_resonator_index.py` | vacuum/`K_PV` resonator index (§I) | numpy | ✓ runs |

**Dependency note.** Seven of the ten run under the CI stack (`numpy` only). Three need `scipy` or `sympy`
(not in the reproducibility gate's pinned deps by design); install `scipy sympy` to run those. The CK
eigenvalue limit (`ws6`) and the Hopf charge (`greenyer_…`) are *independently* reproduced inside the gate
by `ck_eigenvalues_check.py` and `topology_invariants_check.py` respectively — so the two most load-bearing
provenance results are covered by the CI gate even without scipy.

**The standing anchor caveat.** `v_A` (hence `B`, and every absolute magnitude) carries a self-consistency
**residual band** — there is no independent air-plasmoid `(B, n)` measurement — so absolute Hz/Tesla/eV
values travel with a 5–13× (linear) to ~170× (square-law, `b_eff`/anapole) band. Only **dimensionless
ratios** are load-bearing. See `V_A_RESIDUAL_AND_ABSOLUTE_MAGNITUDES.md` (root) and `tension_T1_T2_resolution.py`.
