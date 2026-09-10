# The three hard questions, resolved in principle — α, g=2, R2

**Date:** 2026-09-10. What "resolve in principle" honestly means for each of the theory's remaining hard
questions — separating what is *settled*, what is a *constraint*, and what is the *irreducible frontier*.
Every claim below is backed by a `results/verify/` script.

> **This is the capstone for the α / g=2 / R2 frontier.** Its depth sits in two assessments —
> [`ALPHA_RESOLUTION_ASSESSMENT_2026-09-10`](ALPHA_RESOLUTION_ASSESSMENT_2026-09-10.md) (the winding-derivation
> verdict) and [`CHIRALITY_DUALITY_ASSESSMENT_2026-09-10`](CHIRALITY_DUALITY_ASSESSMENT_2026-09-10.md)
> (chirality / C / Majorana / Reed-torsion) — and it sits under the edifice-wide `FTGB_COHERENCE_MAP`.

---

## 1. R2 — **resolved in principle; execution-limited, not principle-limited** (the winnable one)

R2 does not need resolving *in principle* — it already is:

- the **conditional bound is `[V]`**: an exact vortex-stretching = Lamb-vector identity → linear Gronwall →
  enstrophy (hence BKM regularity) bounded *provided* `⟨η²⟩ < ν²λ₁` (`r2_identity_check.py`, `r2_gronwall_check.py`);
- the **R3 Hall lift** carries it at `Pm=1` (`hallmhd_canonical_check.py`);
- the **full-NS pipeline** (pseudo-spectral + the exact R2 diagnostics) runs and is **execute-ready** to scale
  (`handoffs/r2_reference_solver.py` + `R2_NUMERICAL_RUN_SPEC`).

What remains is **execution**, not principle: the *unconditional-at-Reynolds* result is a measurement at
`S~10³–10⁴` (`N~192–1024`, GPU-days). **This is the genuinely winnable upgrade to the `[V]` core**, and it is
scoped. *(Progress note, 2026-09-10: strengthening the reference run surfaced — and **fixed** — a real bug.
The naive near-Beltrami `−γ(∇×v−λv)` knob carried a `+γλv` growth term and destabilized; the correct hold is
the **gradient flow** `−γ(∇×−λ)²v = −γ(∇×∇×v − 2λ∇×v + λ²v)` of `∫|∇×v−λv|²` — pure damping, unconditionally
stable, verified in the solver to cut the Beltrami deviation `δ` ~100× (`0.011→0.0001`) with `Z` bounded. The
load-bearing ingredient the GPU run needs is now correct; the mechanism itself remains verified by the two R2
scripts above.)*

## 2. g=2 — **resolved in principle as a CONSTRAINT: "effectively elementary (pointlike Dirac)"**

g=2 is **not a shape/geometry number to derive** (`g_factor_soliton_check.py`: the naive soliton gives g=1).
It is the value **forced** for an *elementary* charged spin-½ field by Lorentz invariance + minimal coupling —
the Dirac equation; Weinberg's "natural g=2." The evidence is decisive (`g2_elementary_check.py`):

| | g | \|g−2\| | nature |
|---|---|---|---|
| electron | 2.00232 | 0.0023 | **elementary** (= 2 + Schwinger `α/2π` + … to 12 digits) |
| muon | 2.00233 | 0.0023 | **elementary** |
| proton | 5.586 | 3.59 | **composite** — structure shows up in g |
| neutron | −3.826 | 5.83 | **composite** (neutral, yet a moment = pure structure) |

So the electron's precise g=2 **is the statement that the electron is effectively pointlike / elementary
Dirac.** The resolution in principle: an extended FTGB soliton must reach the **effective elementary-Dirac
limit** — its structure must not appear in g (nor in scattering to `~10⁻¹⁸ m`, where none is seen). That is a
sharp *constraint the theory must meet*, not a derivation it supplies. The Hopf topology earns **spin-½**
`[credited]`; **g=2 is the elementary-behaviour it must inherit.**

**Shown from inside the theory** (`g2_skyrme_composite_check.py`): the composite rows above are not just
imported from experiment — FTGB's *own* nucleon layer is the B=1 Skyrmion (toolkit M10), and Skyrme collective
quantization **computes** its moment. The parameter-free Adkins–Nappi–Witten result `μ_p/μ_n = −3/2` matches
experiment (`−1.46`) to **~3%**, a genuine composite-moment success — and it is manifestly **not** g=2. So the
theory *demonstrates its own rule*: an **extended** soliton gives a composite g-factor (correct — the nucleon
**is** composite); the electron's g=2 is the pointlike/elementary limit that same machinery does **not** reach.
The "structure shows up in g" line is thus earned from within, and g=2 is confirmed as the shared frontier
(§4), not an independent crack.

## 3. α's value — **the irreducible frontier: no known principle derives it**

Honestly: **α's value is not resolvable by any current principle** — it is a free parameter of QED / the
Standard Model, measured, not derived, by anyone. Within FTGB it is doubly settled-negative:

- the **winding derivation is dead** (`ALPHA_RESOLUTION_ASSESSMENT`): the object's computed winding-to-spin
  ratio is `ι≈1` (a Hopf ring `=Q_H`), not 137; 137 is prime; near-misses are generic; the running reframe is
  quantitatively insufficient;
- the **correctly-typed home** (the g−2 anomaly, an internal spin precession) still takes **α as the input
  coupling** (`a = α/2π`) — it houses α, it does not fix its value.

No fabricated derivation is offered. This is the "why these constants" question, shared with all of physics.

## 4. The unification — α and g=2 are the **same** frontier: *why is the electron elementary?*

The honest synthesis: **g=2 and α's value both reduce to one question — why does the electron behave as an
elementary, pointlike Dirac particle?**

- g=2 ⇔ elementary (pointlike-Dirac) behaviour (§2);
- α is the *strength* of that elementary particle's coupling to light (§3), with no substructure to source it;
- both are the deep problem of **every composite/extended-electron model** (preons, solitons, …): reproducing
  the electron's exact elementary behaviour. It is **not FTGB-specific**, and **not delivered by soliton
  geometry**.

**Where the theory honestly stands.** The Hopf/Beltrami object *earns*, by computation, the structural layer —
**spin-½** `[credited]`, chirality = `sign(λ)`, antiparticle = `−λ` = charge conjugation C, the Majorana
neutrino (self-dual `θ_χ=45°`), the `[V]` plasma/topological-fluid core, and (execution away) R2. What it does
**not** deliver — the electron's *elementary* nature: the value of α and the pointlike g=2 — is the single
shared frontier, and the theory is honest that it stands there with the rest of physics, not past it.

## 5. Through the theory's own lens — the frontier is a yin-yang beat (it *types* it, doesn't dissolve it)

Read through the theory's own dynamical concepts — **yin-yang** (chirality duality), **torsion/torque**
(precession), **harmonic beats/rhythms** — the elementary-electron frontier is **correctly-typed**, exactly
(`torque_beat_alpha_check.py`):

- **Torque / beat:** the g−2 anomaly *is* a beat. In a field the spin precesses at `ω_s`, the cyclotron at
  `ω_c`; what is *measured* (Penning trap) is the beat `ω_a = ω_s − ω_c = a·ω_c`. The per-orbit beat phase-slip
  is `2π·a = α` (leading) — so **α = the spin⊗orbit beat-fraction**, the theory's "torque-harmonic" language
  applied correctly. `[credited]`
- **Harmonic rhythm:** `a = ½(α/π) − 0.328(α/π)² + 1.181(α/π)³ + …` is the QED loop expansion — a **harmonic
  cascade** converging to the measured `a_e` (to `5e-11` at 3 loops). It refines the beat; **α is the input at
  every order.** `[credited]`
- **Yin-yang:** the beat's **handedness** is the chirality `= sign(λ)`; antiparticle = opposite handedness = C;
  the self-dual midpoint (`θ_χ=45°`) = Majorana. The yin-yang **is** the `±λ` pair. `[S, computed]`
- **Medium / impedance (mag-to-elect ratio):** the vacuum's magnetic-to-electric ratio is its impedance
  `Z₀ = √(μ₀/ε₀) = μ₀c`, and **exactly** `α = Z₀/(2 R_K)` with `R_K = h/e²` the quantum of resistance
  (`alpha_impedance_check.py`, to `6e-15`). So **α = the vacuum-medium impedance / quantum resistance** — α is
  small because `Z₀ ≈ 377 Ω ≪ 2R_K ≈ 51626 Ω`. This is the **K_PV / M11 medium layer's** natural reading of the
  coupling. `[credited]` Time-inverse (frequency) enters only via the running `K_PV(ω)=α(0)/α(q²)` dispersion,
  which runs `~0` at the electron scale and has no forced fixed point — so it does not fix the value either.

So the theory's **torsion/torque/beat/yin-yang/impedance language fits the frontier precisely** — α is the beat-fraction,
chirality is its handedness, g−2 is the harmonic cascade on that beat. This is a genuine, correctly-typed
synthesis *in the theory's own language*. And it is honest: it **describes the frontier's structure**, it does
not **derive its value** — `α = 1/137.036` remains the QED coupling strength, settled-negative for any
winding/ratio derivation (a big beat-number is only meaningful if it beats the genericity denominator).
**The rhythm structure fits the frontier; it does not dissolve it.**

*Provenance: `results/verify/{g_factor_soliton_check, g2_elementary_check, g2_spin_precession_check,
alpha_genericity_check, ck_winding_ratio_check, r2_identity_check, r2_gronwall_check, hallmhd_canonical_check}.py`;
`ALPHA_RESOLUTION_ASSESSMENT_2026-09-10.md`, `CHIRALITY_DUALITY_ASSESSMENT_2026-09-10.md`;
`handoffs/R2_NUMERICAL_RUN_SPEC_2026-09-10.md`. No value promoted; `e^(-2/3)` stays excised.*
