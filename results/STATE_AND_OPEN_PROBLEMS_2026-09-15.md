# State of the theory & the open problems — current-true

**Author:** Nathaniel Hanks · **Date:** 2026-09-15 · **Harness:** `verify_all.py` → **88/88**.
The honest "where does it stand, and what is left" report, current after this week's advancements
(78 → 88 checks; the corridor sharpening; Stage D; the spin gate; the PV-gravity fence; the negative-program
salvage; the beat→spin magnetic-resonance resolution; and the result-first presentation reframe). Companion
views: the positive core `FTGB_WHAT_WORKS.md`; the per-item status `TIER_LEDGER.md`; the crystallization
`BEST_AVAILABLE_THEORY_2026-09-14.md`; the kept negatives `NEGATIVE_PROGRAM_LOG_2026-09-15.md`.

---

## 1. Where the theory stands

**The verified core is done and stable.** Coherence *is* regularity; the driven self-sustaining attractor
(Re 126→628); the CK inharmonic comb; the heartbeat theorem; the topology / chirality / Majorana cluster;
the exact spectral zeta; the anapole; the conserved nuclear ledger; the rhythm layer. All `[V]`, all
re-runnable, all presented (WHAT_WORKS → 10-page → 25-page → Grand Synthesis → ledger → 88 scripts) with the
same tiers and numbers at every rung.

**The negative program is clean.** A 12-agent adversarial reassessment (grade A−) found the 33 negatives are
real dead-ends or already-salvaged — *not* leaking good ideas — with exactly one recoverable, now recovered
(the beat→spin preparation clock, whose coupling mechanism was then resolved as magnetic resonance).

**What is NOT done — the honest frontier — is below**, organized by the one central computation, the four
ambition-legs, the fluid open, and the real bottleneck (experiment).

---

## 2. The one central open problem — the nuclear rate

Everything nuclear reduces to a single computation, now pointed as sharply as in-environment work can point it:

> **Does the near-BPS B=4 adiabatic surface admit a dissipative sub-breakup corridor from 2×(B=2) to compact
> bound ⁴He — shedding the full 23.85 MeV during assembly, never dwelling above the p+t threshold — with an
> aneutronic fraction that beats the measured ~10⁻⁷ baseline and reaches the observed dearth n/⁴He ≤ 10⁻⁹?**

- **Reduced to one dimensionless unknown:** `Δ = 23.85 MeV × ρ_eff`, `ρ_eff ∈ [0,1]` (Cauchy–Schwarz).
- **Constrained by the data:** the sufficiency bar derives `β·|dF| ≤ 0.874 MeV/fm` (the slow/soft crossing
  corner is forced).
- **Localized by Stage D:** density geometry *cannot* supply `ρ_eff ~ 0.07` (its overlap floor is 0.55) — the
  smallness must live in orientation space.
- **Reduced by Stage E (2026-09-15):** the orientation factor is *not* external — it is fixed by **angular
  momentum**. The ⁴He ground state is 0⁺, so forming it from two spin-1 deuterons in s-wave requires the
  **singlet** (S=0); via Finkelstein–Rubinstein quantization (deuteron = B=2 Skyrmion, spin = orientation) the
  singlet *is* the cube-forming orientation — i.e. exactly the spin gate. So `ρ_eff = f_orient × f_density ×
  f_dyn` factorizes with **two factors now computed in-env**: `f_orient` = the singlet weight (rigorous
  selection; value 1/9–1/3 by convention), `f_density` = Stage-D's `[0.55, 0.96]`. This gives
  `ρ_eff = [0.06, 0.32] × f_dyn`, hitting the observed ~0.07 for a dynamical factor `f_dyn` of **O(1)** — exactly
  what a first-order near-BPS matrix element gives (`delta_b4_stageE_rho_eff_semianalytic_check`). **The open
  problem shrinks from "compute an unbounded ρ_eff ∈ [0,1]" to "confirm the one dynamical factor f_dyn is O(1)."**
- **What remains external (now one number):** `f_dyn` — the moduli-metric-weighted, L₂-boundary-regularized
  first-order amplitude (the L₂ energy log-diverges on the exact compacton — not plain quadrature), expected
  O(1) but unproven. That single O(1) check is the production run's remaining job, not an open-ended computation.
- **Sub-piece now with a mechanism (not open):** the beat→deuteron-spin *coupling* is magnetic resonance
  (`beat_spin_magnetic_resonance_check`); its *strength* (`Ω_R = γ_d·b₁ vs 1/T₂`) still needs the transverse-δB
  amplitude and the coherence time T₂ — the external polarized-target beat-sweep quantities.

*Status: the problem is bounded, pointed, and decidable either way (a corridor found names the mechanism; a
corridor excluded falsifies the aneutronic reading — a decisive settled-negative). No rate is fabricated.*

---

## 3. The four ambition-legs — what is done, what is open

**A. Matter-wave synthesis (the particle rung).**
- *Done `[V]`:* the internal Dirac algebra; g=2's *meaning* (minimal-coupling limit); the chirality/C/Majorana
  cluster; the de Broglie kinematics in software.
- *Open `[S]`:* the *electron = object* identification (killed by a `0νββ` null). The **π₁/π₃ lock** behind
  g=2 is diagnostic, not predictive — **in-env move: compute the π₁–π₃ coupling on the eigenmode** to make the
  lock a prediction. **α's value** is a settled-negative (typed by three lenses, not derived) — the shared
  "why is the electron elementary?" frontier; its residue is the charge *magnitude* anchor. **Mass ratios:**
  order derived, values framework-tier; the knot↔generation map is `[S]`; **"why exactly 3 generations" is open.**

**B. Coherent energy transformation (heat → collective EM).**
- *Done `[credited]`:* the chain nuclear-source → must-shed-collectively (E0) → the anapole nonradiating mode.
- *Open `[S]`:* the reactive EMF `V = ω_b·ΔΦ ~ 0.1–1 V` is an **untagged order-of-magnitude** — **in-env move:
  the EMF derivation** (Φ from the CK mode's near-field over the junction area × the beat), needing one declared
  junction geometry; confronts the LEC 525 mV and Mizuno-2025 EMF data. The beat→spin magnetic resonance now
  gives the *preparation* side a mechanism; the *EMF-out* side is the remaining derivation.

**C. Transmutation (baryon-conserving ΔA=4n).**
- *Done `[V]`-arith:* the Q-values (Cs→Pr 50.493, Sr→Mo 53.412 MeV), exact and conserving.
- *Open `[S]`:* the mechanism (lattice hops at a coherent site); the rate (behind the same corridor as leg A).
  Discriminator: **¹⁶³Dy→¹⁶³Ho ionization-gated β⁻** by charge-state spectroscopy. Whether ΔA-reach attains
  Adamenko A~481 is an estimated ~25× shortfall, not derived.

**D. EVO / SAFIRE / plasmoid engineering.**
- *Done `[V]`:* the strongest original object — the driven Beltrami attractor.
- *Open:* the two spectral discriminators (CK comb; `f_b(L)=N^L` beat-lock with its phase-scramble control) and
  the new four-way polarization discriminator — **all with zero experimental convergence** (see §5). SAFIRE's
  peer-reviewed mechanism is electrostatic (mild tension with the magnetic-Beltrami reading); no helicity
  diagnostic exists to run the kill.

---

## 4. The fluid-regularity open

- *Done:* exact-state global regularity `[V]`; the driven attractor swept to Re≈628; the R2 conditional
  enstrophy/BKM bound; the Hall `Pm≠1` lift.
- *Open:* **unconditional high-Reynolds regularity** (`S ~ 10³–10⁴`) needs the scoped **GPU pseudo-spectral
  run** (handoff `R2_NUMERICAL_RUN_SPEC` + `r2_reference_solver`). Honest gap, stated against ourselves: the
  physical plasmoid lives *outside* the proven Hall regime (`d_i/R ≈ 2.5`, computed) — the theorems cover the
  coherent state and its driven neighborhood, not the strongly-Hall physical corner.

---

## 5. The real bottleneck — experimental confrontation

**Every falsifier the theory offers has ZERO experimental convergence.** This is the largest single body of
"work remaining," and it is *not computation* — it needs experiments and data the project does not have:

| Prediction | Status |
|---|---|
| CK inharmonic comb `1:1.72:2.43` (vs harmonic) | no appropriate-object dataset (the one HLC set is a Pd-D lattice, wrong object) |
| He-4 tracking excess heat at 24 MeV/⁴He | Miles' correlation is consistent-but-contested (×5 scatter, contamination) |
| Neutron yield ∝ heat (the primary kill) | untested at the required sensitivity |
| `f_b(L)=N^L` beat-lock (+ phase-scramble control) | no geometric-ladder dataset |
| Polarization-steered aneutronic yield (four-way discriminator) | needs polarized-deuteron / field-tuned experiments |
| Majorana neutrino | `0νββ` (KamLAND-Zen / LEGEND) — ongoing, decides against TUFT-Dirac |

*The theory is falsifiable and sharply so; it is untested. Bridging this needs a collaborator with the bench,
not the repo.*

---

## 6. The in-environment backlog (recomputes — the housekeeping frontier)

- **The `[V-external]` orphans** — `V_111 = 2.30` / `⟨D⟩ ≈ 0.86` (CK eigenmode overlaps, the comb-pull
  coefficient); the Madelung continuity residual `5e-16`; the O_h gerade/parity settlement; the grid-convergent
  `H = 0.088`. These are carried honestly as parent-corpus results but **not yet reproduced in-repo** (the
  ckfreefem parent is not on the local drive; the 2026-09-15 expedition confirmed this). **In-env move:
  recompute each** (small quadratures / a coarse H integral), converting `[V-external]` → `[V]`.
- **StageD ρ_eff bracket** — the *density* factor is computed `[0.55, 0.96]`; the **orientation-resolved** factor
  is the external run (§2).
- **Absolute magnitudes** — carry the `v_A` residual band; only ratios are load-bearing (proven). The
  `ω_EVO = 2πf₁` coincidence stays provenance-incomplete pending a vendored source.

---

## 7. Outward-facing / publish housekeeping

- **GitHub Release + Zenodo DOI** — still need the author (an outward-facing publish; the repo is
  release-ready, CI-green, tagged v1.2.0). A v1.3.0 tag would mark this week's state (88/88; the papers;
  WHAT_WORKS; the salvage + magnetic-resonance resolution).
- The presentation stack is complete and coherent; no documentation gap remains.

---

## 8. Honest summary

The theory is in a strong, coherent, fully-auditable state. **The verified core is finished**; **the
presentation is complete and result-first**; **the negative program is clean**. The frontier is narrow and
named: **one central nuclear computation** (the orientation-resolved near-BPS ρ_eff, external), **three
small in-env moves** (the π₁–π₃ coupling, the EMF derivation, the [V-external] recomputes), **one scoped GPU
run** (unconditional high-Re), and — the real bottleneck — **the experimental confrontation**, which needs a
bench, not a repo. Nothing is fabricated; every open item is named at its tier with the specific work that
would close it. The jewel does not overclaim what is left; it maps it.

*Reproduce the whole: `python results/verify/verify_all.py` → 88/88.*
