# Δ breakthrough configurations — the theory-level search for a tractable route

**The question.** Stepping back to theory: is there a *new model configuration* in which the production Δ
(the d+d→⁴He branching gap) can be computed for a breakthrough — ideally sidestepping the fitted-near-BPS
full-field HPC run? This is the honest roadmap of candidate routes, each assessed for what it computes, what
it sidesteps, and its residual. **No Δ is fabricated; this identifies routes, and demonstrates the structure
of the strongest one** (`delta_bps_perturbative_structure_check.py`).

## The recommended route — ★ BPS-perturbative (Δ becomes a perturbative matrix element)

This falls out of Stage C and is the genuine breakthrough-in-principle:

- **Standard Skyrme:** the compact B=4 (⁴He) and two separated B=2 (d+d) differ by an **O(1)** energy fraction
  (~6%) — the barrier and crossing are non-perturbative, so Δ needs the full nonlinear field relaxation (the
  HPC wall).
- **The BPS submodel (`L_6 + L_0`):** the energy is **exactly linear in B**, so those two configurations are
  **degenerate** (zero barrier), and the model is **integrable** — analytic soliton (compacton) solutions and
  a known moduli space (all volume-preserving diffeomorphisms) [Adam–Sánchez-Guillén–Wereszczyński 2010;
  Speight 2014].
- **The breakthrough:** turning on the small near-BPS perturbation (`L_2 + L_4`) lifts the degeneracy and
  creates the barrier, the physical release (23.85 MeV — a near-BPS quantity, Stage C), **and the off-diagonal
  Δ, all at first order.** So Δ is a **perturbative matrix element on the analytically-known BPS moduli space**
  — a semi-analytic computation, *not* a full-field relaxation.

**Why it's the recommended route:** it turns the non-perturbative full-field problem into a first-order
perturbation around an exactly-solvable core. **Residual (honest):** it still needs the near-BPS parameters
fitted to nuclei and the moduli-space matrix element evaluated — a real calculation, but qualitatively easier
(semi-analytic) than the HPC relaxation. Demonstrated structurally in-repo.

## The other candidate configurations (assessed)

- **Vibrational-mode / collective-coordinate.** Quantize the B=4 Skyrmion's *known* vibrational spectrum
  (Barnes–Baskerville–Turok 1997); the breakup channel is a specific mode, and Δ is its coupling to the
  ground state. **Sidesteps** full relaxation (finite mode basis); **residual:** the anharmonic coupling still
  needs the field theory, and the mode basis is a truncation. A credible reduced route, weaker than BPS-perturbative.
- **FTGB-native matter-wave / Franck–Condon overlap.** In FTGB's dual reading the nuclei *are* Madelung
  matter-wave configurations; the d+d→⁴He rearrangement's Δ factorizes (Born–Oppenheimer) into a nuclear
  matrix element × a **Franck–Condon overlap** of the initial/final matter-wave profiles. **Sidesteps** the
  relaxation for the overlap part (a computable integral, in-environment); **residual:** the nuclear matrix
  element still needs the field theory. Best combined with the BPS-perturbative core (compute the FC overlap
  on the BPS moduli space).
- **Coherent enhancement (anapole).** The FTGB active-site mechanism: the nonradiating anapole/coherent mode
  boosts the *effective* collective coupling. This is the `[S]` LENR mechanism (`LENR_ACTIVE_SITE_SYNTHESIS`),
  but the *direct* phonon-coupling rate is **settled-negative by ~66 orders** — so this is the physical
  mechanism, not a computational route to the bare nuclear Δ.

## A route considered and REJECTED (the discipline working)

- **"Slow lattice crossing → adiabatic → aneutronic."** Tempting: Landau–Zener adiabaticity `Γ ∝ 1/v`, so a
  slow crossing makes the *same* Δ adiabatic (aneutronic). **Rejected on physical grounds:** the LZ crossing
  happens at the *nuclear* (fm) scale, where the kinetic energy is ~MeV *regardless* of the lattice — the
  crossing is fast either way. The aneutronic channel is not explained by a slow crossing; it requires either
  a genuinely large Δ or the coherent-hold mechanism (above). Recorded so it is not re-attempted.

## The falsifiability bridge (already in-repo)

Independent of *computing* Δ, the two-level Landau–Zener bridge (`delta_b4_landau_zener_bridge_check.py`)
makes Δ **testable**: forward (Δ → ⁴He/neutron branching, a prediction) and inverse (measured ratio →
effective Δ). So the open number has a sharp experiment (the ⁴He/neutron ratio), sharpening the "neutron
yield ∝ heat" falsifier.

## Status & recommendation

The staged in-environment program is complete (A–C) and has now been extended at the theory level: the
**BPS-perturbative configuration is the recommended breakthrough route** — it makes Δ a semi-analytic
perturbative matrix element rather than a full-field HPC relaxation, and it is the same near-BPS model that
fixes the overbinding. The honest next run is: (1) fix a near-BPS lagrangian + fit its parameters to light
nuclei; (2) compute the first-order Δ as a Franck–Condon-weighted matrix element on the BPS moduli space;
(3) plug into the LZ bridge to predict the ⁴He/neutron ratio and confront the LENR data. Energy `[V]`,
mechanism `[S]`, rate `open` — with the route to the rate now identified and structurally demonstrated.
