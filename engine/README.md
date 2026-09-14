# FTGB mathematical engine

`ftgb_engine.py` — the coherent-object theory as **one executable model**. From four physical anchors
`{B, n, m_i, R}` (zero free structural parameters) it derives the object's structure, integrates its
dynamics, and verifies its load-bearing theorems — every output tiered.

```bash
python engine/ftgb_engine.py         # full tiered report
```
```python
from engine.ftgb_engine import CoherentObject
obj = CoherentObject(B=200, n=1e28, m_i=1.6726e-27, R=1e-6)
obj.report()
obj.carrier_comb()          # (absolute Hz, CK-root ratios 1:1.719:2.427)
obj.heartbeat(mu=2.0)       # -> (settled amplitude, r* = sqrt(2))
obj.enstrophy_bounded(0.8, spike=3.0)   # R2 Gronwall: bounded iff <eta^2> < nu^2 lambda1
CoherentObject.verify_lamb_identity()   # exact stretching = Lamb-vector flux
```

**What it computes**
1. **Static structure** `[credited]/[V]` — Alfvén speed `v_A = B/√(μ₀ n m_i)`, Beltrami eigenvalue
   `λ₁R = 4.4934`, the inharmonic Chandrasekhar–Kendall carrier comb (ratios `1 : 1.719 : 2.427`, the EVO
   {121,208,294} kHz calibration), the whirl mass ladder `m = ħω_C/c²` (electron recovered to 0.04%),
   sign-definite helicity density.
2. **Dynamics** `[V]/[S]` — the Stuart–Landau heartbeat (`r* = √2`), Kuramoto/Adler comb entrainment (pull
   onto 7/4, 5/2), and the current-leg closure scalar `S(t)` (selects the `μ=const` no-go undriven; driven
   `→ 0`).
3. **Theorems** `[V]` — the exact vortex-stretching = Lamb-vector identity (both forms agree to ~9 sig figs),
   the R2 enstrophy/BKM threshold `⟨η²⟩ < ν²λ₁` (sharp; time-integrated), and the Hall `Pm=1` coercivity with
   the `det = −d_i²(η−ν)²/4` obstruction.

**Discipline.** numpy-only, reproducible, no fabricated numbers, no over-unity. Consolidates
`results/verify/{r2_identity_check, r2_gronwall_check, hallmhd_canonical_check}.py`; grounded in
`FTGB_CURRENTLEG_TRILOGY` and `FTGB_COHERENCE_MAP`. Open items (unconditional R2/R3, the Δ LENR branching,
the exact α value) are named in the report, not hidden.

---

`ftgb_resonator_sim.py` — the theory as running **simulation** (where the engine is the model, this is
the software that time-integrates it). Five simulations, each with hard PASS/FAIL:

```bash
python engine/ftgb_resonator_sim.py     # deterministic; auto-included in verify_all
```

1. **The object** `[V]` — exact Beltrami eigenfield (`curl u = u`) built on the 3-torus; Beltrami property
   and the self-interaction null (`u×ω = 0` pointwise) verified spectrally to ~1e-14.
2. **Coherence is regularity** `[V]` — the **full nonlinear Navier–Stokes equations** integrated
   pseudo-spectrally (32³, RK4, 2/3-dealiased) from the Beltrami state track the exact eternal solution
   `u(t)=e^{−νλ²t}u₀` to ~5e-16; a Taylor–Green (non-Beltrami) start departs at ~9e-2 — the coherent state
   is the one that evolves exactly, and the contrast proves the test has teeth. (Companion to
   `exact_beltrami_regularity_check.py`: that verifies the law's identities; this runs the dynamics.)
3. **The resonator** `[V]` — CK comb `tan x = x` re-derived by bisection; ratios `1:1.719:2.427`; the
   {121, 208, 294} kHz canon calibration and its beat structure (87.1/85.7 kHz, second-order detuning
   ≈ 1.43 kHz — the theory's kHz detuning scale).
4. **Harmonic oscillation** `[V]` — driven-damped oscillator lands on the analytic Lorentzian (Q recovered);
   the two-mode beat frequency is *extracted from the simulated envelope* (FFT-Hilbert) and equals `x₂−x₁`.
5. **The matter wave** `[V]` math / `[S,QWM]` reading — packet under the Proca/Compton-cutoff dispersion
   `ω²=c²k²+ω_c²`: measured group velocity `= c²k/ω`, rest packet ticks at exactly `ω_c` (the internal
   clock), and `v_g·v_p = c²` — the de Broglie matter-wave kinematics measured in software.
