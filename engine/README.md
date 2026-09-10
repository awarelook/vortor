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
