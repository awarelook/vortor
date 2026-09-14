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

## Additional vendored provenance (2026-09-10 integrity pass)

To eliminate every phantom script reference, the toolkit-module / handoff provenance scripts cited across the
corpus were also vendored (frozen) here: `toolkit_adv07_buckingham_pi.py`, `toolkit_adv08_qwm_math_conversion.py`,
the current-leg no-go scripts (`driven_canonical_aligned_2026-09-08.py`, `driven_pv_const_nogo_2026-09-08.py`,
`driven_nonaligned_closure_2026-09-08.py` — the trilogy core is *also* reproduced in-repo by
`results/verify/currentleg_trilogy_check.py`), `self_unified_skyrme_multibody_2026-09-08.py`,
`b4_moduli_geodesic_executed_2026-09-08.py`, `b4_two_diabatic_relaxation_2026-09-08.py`,
`seesaw_ftgb_duality_bridge.py`, `nielsen_quark_assembly_verify.py`,
`benchtop_quadruplet_independent_circuit_crosscheck.py`, and the R2 exploration scripts
(`r2_grashof_threshold_*`, `r2_near_beltrami_enstrophy_*`, `r2_spectral_retry_*`). Deps vary (some need
scipy/sympy); each is cited by its toolkit module. These are a **frozen provenance record**, not part of the
CI gate — every *load-bearing* result is reproduced by an in-repo `results/verify/` script.

## Vendored citation stores & ark salvage (2026-09-13 corpus-salvage pass)

Frozen from the ckfreefem corpus so the jewel's **citation base and its verification tags** are
self-contained (sources: `03_paper/main_draft/` and `11_verified_ark/`):

| File | What | Source |
|---|---|---|
| `REFERENCES_VERIFIED_LEDGER_2026-08-28.md` | the corpus's full ~198-row citation ledger, every row tagged `[V]` live-verified / `[T]` textbook / `[P]` project | `03_paper/main_draft/` |
| `PAPER_PREP_CITATIONS_2026-09-01.md` | the paper-prep citation pass: 13 re-verified entries, **4 bibliographic corrections** (MoEDAL *Nature* **602**, 63; Gould & Rajantie PRL 119; Bartalucci–Vysotskii–Vysotskyy PRAB 22; Scamps & Simenel *Nature* 564, 382) + the do-not-cite list | `03_paper/main_draft/` |
| `greenyer_61_entry_catalog_slice.md` | the M14 (Greenyer beat/cascade) 61-entry per-citation verified catalog, every entry status-tagged | `11_verified_ark/greenyer_toroidal_beat/citations/` |
| `two_electron_ring_madelung.py` | the surviving iccf27 positive: two-electron ring Madelung reduction (×4 ratio from first-principles QHD) | `11_verified_ark/iccf27_evo_d4d/scripts/` |
| `cho_maison_real_monopole_solve.py` | from-scratch Cho–Maison electroweak-monopole BVP solve (Cho & Maison, *PLB* 391, 360 (1997)) — pairs with the settled-negative monopole-program closure (Hopf `π₃(S²)` ≠ monopole `π₂(S²)`) | `11_verified_ark/greenyer_toroidal_beat/scripts/` |
| `SECTOR_A_ENVIRONMENT_THEORY.md` | the helium-heat program's surviving Sector A: verified m=1 Beltrami eigenmode + solved Madelung ring + the exact closed-form OAM ratio `R = π m_e R_L² f_L / ħ` | `11_verified_ark/helium_heat_nuclear_extensions/verified_core/` |

Same rule as above: **frozen provenance, not CI-gated**. The curated fold of the absent citation clusters
into the jewel's own `REFERENCES.md` (§1e–§1h) is the load-bearing part; these files preserve the full
verification-tagged record they were curated from.
