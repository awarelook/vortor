# R2 numerical run — execute-ready specification

**Date:** 2026-09-10 · **For:** a fluid-dynamics / HPC collaborator (GPU pseudo-spectral).
**Goal:** upgrade the R2 enstrophy/BKM bound from **conditional `[V]`** to **`[V]`-numerically-supported**
by measuring the enstrophy history of the driven near-Beltrami heartbeat at the object's Reynolds number.
**Reference code:** `handoffs/r2_reference_solver.py` — a runnable numpy pseudo-spectral solver that
implements the *entire* scheme + diagnostics at demo resolution; the run is this code **scaled**.
Companion prose: `handoffs/HANDOFF_R2_ENSTROPHY_REGULARITY_2026-09-09.md`.

---

## 1. The one measurement that closes it

Integrate forced-dissipative incompressible 3D Navier–Stokes (first model; Hall-MHD is the lift),
with the flow **dynamically held near a force-free Beltrami state** `curl v ≈ λ v`, and answer:

> Over many heartbeat periods at the object's Lundquist/Reynolds number `S ~ 10³–10⁴`, does the
> enstrophy `Z(t) = ½∫|ω|²` stay on a **bounded plateau** (⇒ `∫₀^T ‖ω‖_∞ dt` finite ⇒ Beale–Kato–Majda
> regular), or does it grow **secularly**?

- **Bounded plateau + linear BKM + small δ** ⇒ R2 → `[V]`-numerically-supported at that Reynolds; the
  current-leg trilogy's regularity gate is closed numerically.
- **Secular Z growth / superlinear BKM** ⇒ the drive cannot hold near-Beltrami at Reynolds; the conditional
  bound's condition `⟨η²⟩ < ν²λ₁` fails dynamically — an honest, informative negative.

## 2. The scheme (as implemented in `r2_reference_solver.py`)

Periodic box `[0,2π]³`, rotational form so the Lamb vector is explicit (it *is* the enstrophy driver):

```
dv/dt = P[ v × ω ] − ν k² v + F ,   P = I − kk/k²  (Leray),   ω = ∇×v
```

- **Pseudo-spectral**, 2/3-dealiased; nonlinearity `v×ω` evaluated in physical space, projected in spectral.
- **Time step:** integrating-factor Heun (IF-RK2) — the exact viscous factor `e^{−νk²Δt}` removes viscous
  stiffness; verified stable in the reference at `Δt` set by the nonlinear CFL.
- **Near-Beltrami drive (the load-bearing subtlety):** ABC forcing (`curl F = k_f F`, a Beltrami field)
  holds large scales force-free; the reference exposes a **`γ` relaxation knob** (the near-Beltrami hold
  specified just below). **This is essential:** single-helicity *forcing* does **not** produce a
  near-Beltrami *flow* at high Re (proven in `r2_spectral_retry`) — the flow must be *dynamically pinned* near
  force-free. **The near-Beltrami hold (fixed 2026-09-10):** use `F_relax = −γ (∇×−λ)² v` — the **gradient
  flow** of `∫|∇×v−λv|²`, i.e. `−γ(∇×∇×v − 2λ∇×v + λ²v)`. This is **pure damping** (each helical mode by
  `γ(s|k|−λ)² ≥ 0`), so it is stable and drives the flow onto the single-λ Beltrami manifold — verified in the
  reference solver: `γ≈1` cuts the Beltrami deviation `δ` ~100× (0.011→0.0001) while `Z` stays bounded. (The
  *naive* `−γ(∇×v−λv)` was wrong — it carries a `+γλv` growth term; do not use it.) For **large** `γ` the
  `(∇×−λ)²` damping is stiff — fold it into the **integrating factor** (as with the viscous term), not an
  explicit step. **δ(t) must be monitored and kept small** —
  otherwise the run tests generic turbulence, not the
  near-Beltrami regime the theorem is about.

## 3. Diagnostics (all implemented; success/failure criteria)

| Diagnostic | Definition | Closes R2 (positive) | Negative |
|---|---|---|---|
| **Enstrophy** `Z(t)` | `½⟨|ω|²⟩` | bounded plateau over ≥50 periods | secular growth |
| **Sup-vorticity** `‖ω‖_∞(t)` | `max|ω|` | bounded | blows up |
| **BKM integral** | `∫₀^T ‖ω‖_∞ dt` | ~linear in `T` (finite) | superlinear / divergent |
| **Beltrami deviation** `δ(t)` | `⟨|v×ω|⟩ / (⟨|v|²⟩^½⟨|ω|²⟩^½)` | **stays small** (regime valid) | if large, run is off-regime |

A run is **conclusive only if δ stays small** (the flow really is near-Beltrami) **and** it reaches
`S ~ 10³–10⁴`. The reference demo (N=32, laminar) already shows the intended signature — Z plateau ≈ 1.5,
δ ≈ 0.005–0.016, BKM linear — but laminar boundedness is trivial and proves nothing; the physics is in the
same plot at Reynolds.

## 4. Parameter ladder (scale the reference)

Dissipation scale `~ S^{−3/4}` ⇒ grid `N ~ S^{3/4}` per dimension:

| `S` (Lundquist) | `N³` | regime | cost (GPU pseudo-spectral) |
|---|---|---|---|
| `10³` | ~192³ | **accessible entry** | GPU-hours |
| `10⁴` | ~1024³ | **the target** | GPU-days |
| `10⁶` | ~3·10⁴³ | out of reach | (not attempted) |

Per `S`: choose `ν` for the target Reynolds, `k_f=1` ABC drive, tune `γ` so `δ` sits small but the flow is
not frozen; `Δt` from the nonlinear CFL (`≈0.3 Δx/u_max`); run **≥50–100 heartbeat periods**.

## 5. How to scale `r2_reference_solver.py`

1. **Bigger `N`:** it is written N-agnostic; set `N=192`/`1024`.
2. **GPU FFT:** replace `numpy.fft` with `cupy.fft` or `jax.numpy.fft` — the array ops are drop-in; this is
   the only change needed for the 100–1000× throughput.
3. **Higher Re:** lower `ν`; raise `N` to keep the dissipation scale resolved; keep `2/3` dealiasing.
4. **Hold near-Beltrami:** raise `γ` until `δ(t)` plateaus small; if `γ` must be so large it freezes the
   dynamics, that itself is the informative negative (the flow *resists* being held near force-free at Re).
5. **Long runs / checkpointing:** dump `(Z, ‖ω‖_∞, δ, BKM)(t)` every period; the verdict is the `Z` trend
   over ≥50 periods.

## 6. What each outcome delivers

- **Positive (bounded, δ small, `S≥10³`):** R2 → `[V]`-numerically-supported. The current-leg trilogy's one
  external gate is closed numerically — a citable upgrade of the `[V]` core, independent of α or the wider
  synthesis.
- **Negative (secular growth, or `γ` must freeze the flow):** the near-Beltrami condition fails at Reynolds —
  the conditional bound stays conditional, and we learn *why* (the drive can't hold force-free against the
  cascade). Either way the result is publishable and sharpens the trilogy.

No over-unity, no new physics — this is a regularity measurement on a standard PDE, with the FTGB content
entirely in the near-Beltrami driving regime. Provenance: this spec + `r2_reference_solver.py`;
`HANDOFF_R2_ENSTROPHY_REGULARITY_2026-09-09`; `results/R2_NEAR_BELTRAMI_ENSTROPHY_THEOREM_2026-09-09`
(the conditional `[V]` bound this run would upgrade); `results/verify/r2_{identity,gronwall}_check.py`.
