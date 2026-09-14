# Handoff — the near-BPS field-theory run for the production Δ (execute-ready)

**Objective.** Compute the one remaining dimensionless unknown **ρ_eff** — hence the production branching gap
**Δ = 23.85 MeV × ρ_eff** — via a fitted near-BPS Skyrme field-theory run. Everything upstream of ρ_eff is
done and in-repo (Stages A–C, the scale bound, the breakthrough route, the falsifiability bridge); this run is
the single external computation left. It is **not** doable in a pure-CPU/numpy session (Stage 2 is a 3-D
topology-preserving relaxation, ~days on HPC/GPU, plus a fit) — this spec makes it execute-ready for a
collaborator with the compute. **No Δ is fabricated here.**

## Why this route (not the brute full-field HPC)

From `DELTA_BREAKTHROUGH_CONFIGURATIONS_2026-09-14.md`: the near-BPS model (i) fixes the ~9× standard-Skyrme
overbinding (`delta_b4_stageC_nearbps_check`), and (ii) makes Δ a **first-order perturbative matrix element**
on the analytically-known, degenerate BPS moduli space (`delta_bps_perturbative_structure_check`) — so the
barrier and Δ are O(perturbation), not O(1). The scale is already **data-calibrated**: the degeneracy-lifting
perturbation IS the measured `d+d→⁴He` release, 23.85 MeV (`delta_nearbps_scale_bound_check`). Only the
dimensionless crossing overlap ρ_eff ∈ [0,1] remains — target band ⟺ ρ_eff ≈ 0.07.

## The model

`L = c_0 L_0 + c_2 L_2 + c_4 L_4 + c_6 L_6`, with the **BPS part (`L_0 + L_6`) dominant** and `(L_2 + L_4)` the
small perturbation:

- `L_2 = -(f_π²/16) Tr(L_μ L^μ)` (Dirichlet), `L_4 = (1/32e²) Tr([L_μ,L_ν]²)` (Skyrme), `L_μ = U†∂_μU`;
- `L_6 = -(λ²/24) (ε^{μνρσ} Tr(L_ν L_ρ L_σ))²` (baryon-current², the BPS kinetic term);
- `L_0 = -μ² U(U)` (potential; e.g. the pion-mass form `U = ½Tr(1−U)` or a compacton form).

## Stages

1. **Fit** `(f_π, e, λ, μ, U)` to: pion data (`f_π`, `m_π`), the nucleon mass (`m_N`), and the light-nuclei
   binding energies (deuteron `B=2`, ⁴He `B=4`), reproducing the 23.85 MeV release. Standard near-BPS fitting
   (Adam–Naya–Sánchez-Guillén–Wereszczyński 2013, PRL 111, 232501). *Note:* the release scale is already
   anchored (scale bound), so the fit's job for this run is the *shapes* (the solitons and the barrier), not
   the overall energy scale.
2. **Solitons** `[HPC]`. Solve the `B=2` (deuteron, two-torus) and `B=4` (⁴He, cube) near-BPS solitons by
   topology-preserving 3-D relaxation (arrested Newton flow; baryon-density monitor). The BPS-dominated core
   is near-compacton and semi-analytic (Speight 2014) — exploit it to reduce cost; the `(L_2+L_4)` part needs
   the full second-order relaxation. This is the resource-limited stage (the ~15 h/sweep wall; needs a
   compiled/GPU minimizer, cf. the vendored `frontier_calcs/b4_two_diabatic_relaxation`).
3. **Reaction path + barrier.** Construct the moduli-space path from separated `2×B=2` (d+d entrance) to the
   compact `B=4` (⁴He), constrained by a merger coordinate `Q` (umbrella/constrained relaxation). Compute the
   `(L_2+L_4)` potential — the barrier — along it; identify the diabatic crossing `Q_c`.
4. **The overlap** `→ ρ_eff`. Compute the first-order off-diagonal coupling
   `Δ = ⟨⁴He | (L_2+L_4) | d+d⟩` as the crossing-region Franck–Condon overlap of the two baryon-density
   configurations at `Q_c`; normalize to `ρ_eff = Δ / 23.85 MeV ∈ [0,1]`. **This is the deliverable.**
5. **Falsify.** Plug `Δ = 23.85 MeV × ρ_eff` into the Landau–Zener bridge
   (`delta_b4_landau_zener_bridge_check`) → predict the ⁴He/neutron branching ratio → confront the LENR data
   (Miles He-4/heat; the aneutronic-vs-neutron record).

## Resources & outputs

- **Resources:** a compiled/GPU topology-preserving Skyrme minimizer (Stage 2); the near-BPS fitting code;
  ~days of wall-clock. Two-sided band from (2 resolutions × 2 constructions), per the project's honesty rule.
- **Outputs:** `ρ_eff` (dimensionless, with error band); `Δ` (MeV); the predicted ⁴He/neutron ratio; a
  pass/fail against the measured branching.

## What is already in-repo (so this run has everything but the compute)

- `delta_b4_stageA_rationalmap_check` — topology-exact machinery (validated).
- `delta_b4_stageB_endpoints_check` — the stable endpoint solver + the ~9× overbinding.
- `delta_b4_stageC_nearbps_check` — the near-BPS fix (overbinding → physical binding is near-BPS).
- `delta_bps_perturbative_structure_check` — Δ is perturbative (degenerate + integrable BPS core).
- `delta_nearbps_scale_bound_check` — Δ = 23.85 MeV × ρ_eff (scale calibrated to data; ρ_eff the one unknown).
- `delta_b4_landau_zener_bridge_check` — Δ → ⁴He/neutron ratio (falsifiable).
- Full-field alternative route: `HANDOFF_DELTA_B4_SKYRME_RELAXATION_2026-09-09.md`.

**Bottom line:** the LENR rate is reduced to one dimensionless number, ρ_eff, from this one specified run — a
data-anchored scale × one bounded factor, and falsifiable either way. Executing the run (or measuring the
⁴He/neutron ratio, which the LZ bridge makes decisive) is the honest next step; nothing here is fabricated.
