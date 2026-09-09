# The 2.3% α gap, reframed dynamically — running / IR-fixed-point, not a static screening factor

**Author:** Nathaniel Hanks · **Date:** 2026-09-09
**Provenance:** reframes the toroidal-winding → α gap of `excision-protocol-storti-factor.md` /
`ELECTRON_TORSION_DEFECT_EXPLANATION`, using the toolkit's M10-5 RG dielectric-flow machinery.
**Verification:** `results/verify/alpha_running.py` (standard QED one-loop running; anti-numerology gate).

**One-line.** The geometric winding `q_geom ≈ 140.2` vs `α⁻¹ = 137.036` (a 2.3% gap) should be treated as a
**running / dynamical** effect, not the excised static `e^(-2/3)` screening factor — and when you actually run
the QED coupling, you find the standard flow goes the *wrong way*, so the honest reframe is a **magnetic-vacuum
(anti-screening) IR fixed point** — a principled, sign-distinctive hypothesis that still does **not** close the
value.

**Tier.** `[credited]` for the QED running; `[S-mechanism]` for the anti-screening IR-fixed-point reframe;
`[flag]` for the winding↔α coincidence (fails the 0.5% bar). `e^(-2/3)` remains `[excised]`.

---

## 1. Standard QED running goes the wrong way   `[V]` (ledger §1–2)

The fine-structure constant runs: `α⁻¹(μ) = α⁻¹(0)·(1 − Δα(μ))`, `Δα > 0` growing with energy (diamagnetic
vacuum polarization screens the charge). Computed (leptonic one-loop + hadronic estimate):

```
  α⁻¹(0)   = 137.036   ← Thomson / IR ceiling (MAXIMUM)
  α⁻¹(m_μ) = 136.08
  α⁻¹(m_τ) = 135.06
  α⁻¹(M_Z) = 128.94    (lep+had; matches the known ~128.9)
```

**`α⁻¹` decreases monotonically from 137.036 as energy rises — 137.036 is the ceiling.** The geometric winding
`140.2` is **+2.31% above** it: standard running can never reach it, and the direction is wrong. **So the 2.3%
gap is not a standard-running effect.** This is the first honest result — and it rules out the naive "just run
α" fix.

## 2. What a dynamical reframe actually requires   `[S-mechanism]`

To flow `q_geom = 140.2 → α⁻¹ = 137.036` requires `Δ(α⁻¹) = −3.16` — i.e. `α` must **increase** toward the IR.
That is **anti-screening**: the **paramagnetic / magnetic-dominated (non-Abelian-like)** sign of the vacuum
response, the *opposite* of QED's diamagnetic screening.

This sign is physically apt: the electron here is a **magnetically-structured toroidal object** (poloidal +
toroidal self-field, a Hopf-Beltrami knot), not a point charge in a diamagnetic vacuum. A magnetically
dominated self-field naturally gives a paramagnetic (anti-screening) contribution — the same sign that makes
non-Abelian couplings asymptotically free. The reframe:

> **`α⁻¹ = 137.036` is the IR fixed point of the object's self-consistent winding under a magnetic-vacuum
> (anti-screening) dielectric flow; `q_geom ≈ 140.2` is the bare/UV geometric winding; the 2.3% is the IR
> flow between them.**

This connects directly to **M10-5** (RG dielectric-flow / IR-fixed-point method). **Crucial honesty (M10-5's
own stated position):** the IR value is the **RG integration constant** — *framed*, not *predicted*; the 2.3%
flow amount is set by the scale window / boundary condition. So this is **not parameter-free** — it is a
principled hypothesis with a distinctive, falsifiable feature (the anti-screening sign), not a derivation.

## 3. The anti-numerology gate still holds the line   `[flag]`

The M10-5 discipline requires gating any `~137` coincidence at the **0.5%** bar against nearby values. The
winding estimate `140.2` (with its own ~2% uncertainty from the aspect ratio `A = 9.0 ± 1`):

```
  |140.2 − 137.036| / 137.036 = 2.31%   FAIL
  |140.2 − 138|     / 138     = 1.59%   FAIL
  |140.2 − 139|     / 139     = 0.86%   FAIL
  |140.2 − 140|     / 140     = 0.14%   PASS (!)
```

The raw winding is **closest to 140, not 137** — `137.036` is not specially picked at the 0.5% bar. So the
winding↔α match stays **`[flag]`, not promoted**. The dynamical reframe improves the *story* (a principled
anti-screening flow replaces an ad-hoc factor) but does not close the *number*.

## 4. Net — what this changes, and what would close it

- **Improved:** the 2.3% is no longer an unjustified static `e^(-2/3)` (excised); it is reframed as a
  **named dynamical hypothesis** — a magnetic-vacuum anti-screening IR flow toward a `137.036` fixed point —
  with a **distinctive, testable sign** (anti-screening, opposite to QED). That is a real gain in scientific
  content over "a factor that happens to fit."
- **Not closed:** the value is still an RG integration constant; the raw winding coincidence fails the 0.5%
  bar (closest to 140); `e^(-2/3)` stays out.
- **What would close it:** derive the object's β-function **sign and magnitude** from its magnetic self-field
  structure (M10-5), and show the IR fixed point lands at `137.036` **without tuning the scale window** — or,
  independently, tighten the geometric winding calc (true aspect ratio, knot-polynomial winding) and see
  whether it moves off `140` toward `137`. Either is a concrete frontier calc; neither is done here.

## References
QED running / vacuum polarization: standard (Jegerlehner, hadronic `Δα`; PDG). RG dielectric-flow /
IR-fixed-point + anti-numerology control: toolkit **M10-5** (`TOOLKIT_ADV_10_TOPOLOGICAL_SOLITON_METHODS`).
Winding↔α and the `e^(-2/3)` excision: `excision-protocol-storti-factor.md`,
`ELECTRON_TORSION_DEFECT_EXPLANATION_2026-09-09.md`. Verification: `results/verify/alpha_running.py`.

*No value is promoted; `α⁻¹ = 137.036` stays framed as an IR integration constant, and the winding coincidence
stays `[flag]`. `e^(-2/3)` remains excised. ASCII apart from standard math symbols.*
