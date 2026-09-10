---
title: "When is a topological helicity current a matter current? A no-go trilogy and a conditional regularity closure for driven force-free plasmoids"
author: "Nathaniel Hanks"
date: "2026-09-09"
---

**Abstract.** For a force-free (Beltrami) field `∇×B = λB` and its two-fluid generalization we ask when the
fluid mass 4-current `(ρ, ρv)` may be identified with the topological helicity 4-current `(K⁰, Kⁱ)`,
`K⁰ = A·B`. The density leg `ρ ∝ A·B` holds exactly as a Beltrami-gauge profile identity. The *current* leg
is settled as a tiered result: **(i)** in the static regime the 4-current closes iff `|B| = const`, which a
topologically nontrivial (nulled) field cannot satisfy — a proven no-go; **(ii)** the two-fluid escape via a
conserved *canonical* helicity only relocates the obstruction to `P·v = const`, again impossible for a
nontrivial field via a perfect-square identity; **(iii)** in the genuinely driven regime closure reduces to a
single scalar condition `S = μ − P·v = 0`, whose surface is non-empty and realizable by an electrostatic
drive, while the equilibrium and relaxation dynamics *select against* it — closure is externally driven, never
emergent. The one remaining gate — a global enstrophy / Beale–Kato–Majda bound — we close **conditionally**:
an exact identity recasts the vortex-stretching integral as a Lamb-vector flux, converting the supercritical
enstrophy inequality into a *linear* one and yielding an a-priori bound on the driven near-Beltrami limit cycle
provided the time-averaged Beltrami deviation stays below an explicit `O(1/Re)` threshold. The result lifts to
resistive–viscous Hall two-fluid at unit magnetic Prandtl number, with an explicit `(η−ν)²` obstruction
otherwise. Tiers are stated throughout (`[V]` proven here; `[credited]` established); no over-unity is claimed.

---

## 1. Introduction

Force-free fields `∇×B = λB` (Chandrasekhar & Kendall 1957; Woltjer 1958) are the minimum-energy states of
magnetically dominated plasmas at fixed magnetic helicity `H = ∫A·B` (Taylor 1974; Moffatt 1969). A
recurrent and physically attractive idea — in models where matter and field co-move — is that the fluid mass
current *is* the flux of the field's own winding: that `ρ` measures how densely the field is wound and `ρv`
measures how that winding flows. This paper asks precisely when that identification is mathematically
admissible, treating the fluid current and the helicity current as candidate equal 4-vectors and testing the
equality leg by leg.

The answer is a trilogy — two proven no-gos (static; aligned/steady), one constructive realizability result
(driven), and a first-class selection negative — plus a clean reduction of the last gate to a recognized
regularity problem, which we then close under an explicit, falsifiable hypothesis on the drive. Throughout, the
scope discipline is that these are limits of a *construction*, not verdicts against any observed plasma
phenomenon.

## 2. The law, its two legs, and the density leg  `[V]`

Write ordinary matter conservation as a candidate topological continuity equation,
`∂_t ρ + ∇·(ρv) = 0 ⟺ ∂_μ K^μ = 0`, with `K^μ = (K⁰, Kⁱ)`, `K⁰ = A·B` the helicity density and `Kⁱ` its
flux, under the organizing proportionality `ρ = κ(A·B)`. Two legs must hold for the 4-current to close: the
**density leg** `ρ ~ K⁰` and the **current leg** `ρv ~ Kⁱ`.

In the Beltrami gauge `A = B/λ`, `K⁰ = A·B = |B|²/λ ≥ 0` (sign-definite, verified to `3×10⁻¹⁵`). With a
London-locked cold-condensate flow `∇×v = −(q/m)B` (verified to `7×10⁻¹⁵`), the density profile tracks `|B|²`
with `corr(ρ, A·B) = 1.0000` — an exact dimensionless profile identity; `κ` is a genuine dimensional constant.
**The density leg is settled**; the entire subtlety lives in the current leg.

## 3. The static no-go: closure requires `|B| = const`  `[V]`

Matching densities fixes the current *direction*: London flow gives `v ~ A ~ B`, so the matter current
`ρv ~ |B|²B` is **cubic** in the field while the helicity flux `K ~ B` is **linear**. Equality of a cubic and
a linear quantity demands `|B|² = const`:

> **The 4-current closes if and only if `|B|` is constant.**

The obstruction is basis-independent, measured by the residual of `B` from `range(L)` for
`L[φ] = ∇×((φB − ∇φ×B)/|B|²)` — dimensionless and `κ`-independent. For a genuine toroidal Beltrami field the
residual is `0.6053` (basis-converged); a four-move reducibility sweep (gauge, transverse `E`/sheath, norm,
multi-`λ`) never reaches the `< 0.2` bar, and a transverse non-force-free `E`-field leaves it unchanged. The
deciding control is the null-free constant-`|B|` Beltrami field `B = B₀(cos z, sin z, 0)`, which closes exactly
(residual `0.0000`). A topologically nontrivial closed-fibre field must have nulls and therefore cannot have
`|B| = const`. **In the static regime the current leg is over-determined by construction — a postulate, not a
theorem.**

## 4. Canonical helicity, and the aligned/steady no-go  `[V]`

A driven object may carry its own conserved current. For a two-fluid plasma the correct one is **canonical
(generalized) helicity**: with `P = A + (m/q)v` and `Ω = ∇×P = B + (m/q)∇×v`, the current from
`H = ∫P·Ω` is ideally conserved even when magnetic helicity is dissipated, because the canonical Ohm's law
`E_can = −v×Ω` gives `E_can·Ω = 0` (a Casimir invariant) (Steinhauer & Ishida 1997; Mahajan & Yoshida 1998).

Having the conserved current only *relocates* the obstruction. The canonical flux is
`K_can = h v + (μ − P·v) Ω` (`h` the canonical helicity density, `μ` the Bernoulli head), so closure requires
`(μ − P·v) Ω = 0`. On a double-Beltrami equilibrium `μ = const`, and this is the exact mirror of the static
theorem:

> **Aligned/steady closure requires `P·v = const`** (the analog of `|B| = const`).

Making the relevant cross-term vanish forces `λ₋ = −λ₊`; then `P·v = const` requires a positive ratio
`p₁²/p₂² > 0` between two helicity-fluctuation triples, which is impossible because
`(A'B')(B'C')(A'C') = (A'B'C')² ≥ 0` is a perfect square. Independent checks confirm it: the residual reaches
zero only at the forbidden-sign branch `c = −0.604 < 0`; distinct `λ` force a spectral band-gap and single-mode
collapse; and the field-magnitude inhomogeneity equals `std(P·v)/mean` to `~1%`. The two no-gos are thereby
unified — the same obstruction seen once in `B` and once in `P`.

## 5. The driven resolution, and the selection negative  `[S`→`V] / [V]`

The third leg differs in kind. Define the scalar `S = μ − P·v`. Since `S` is a scalar, `SΩ = 0` forces `S = 0`
pointwise (no "`S ⟂ Ω`" branch; verified false to `4×10⁻¹⁷`). The canonical current is then always a matter
current `(h, h u)`, `u = v + (S/h)Ω`, closing on `v` exactly when `S = 0`. Two facts make this a genuine
resolution. **(a)** The `S = 0` surface is non-empty and drive-compatible (jointly satisfiable to `~10⁻¹⁶`),
unlike the two no-gos whose surfaces are empty; a degree-of-freedom count is sharp (`8/8` isolated → `9/8`
over-determined for closure → the spare freedom supplied by a sustained drive). **(b)** No extra `f_ext ⟂ Ω`
constraint is needed: the exact identity `∂_μ K_can^μ = 2 f_body·Ω` vanishes for a purely electromagnetic
(Lorentz + barotropic) force, so the drive is simply the electrostatic potential
`φ = A·v + (m/2q)|v|² − w/q`; the differential-algebraic system is index-1 (`dS/dφ = 1 ≠ 0`), so `φ` is
algebraically slaved and bounded, with two-species Jacobian `det = −|v_e − v_i|²` (invertible iff current
flows). **Tier: `[S]` leaning `[V]`.**

Does the object select `S = 0` on its own? **No** — a tested negative. *Variationally*, minimizing energy at
fixed canonical helicities yields double-Beltrami equilibria with `μ = const`, hence `S = const − P·v ≠ 0`.
*Dynamically*, a driven-dissipative Hall two-fluid integration keeps `rms(S)/|P·v|` at `O(1)` and relaxes
*toward* the aligned `μ = const` state. **Closure is externally driven, never emergent** — and, as a corollary,
the two no-gos are the dynamical attractor of relaxation, reinforcing them.

## 6. The regularity gate, closed conditionally  `[V]` conditional

On a bounded, current-full trajectory the remaining residual reduces to a global existence question: given an
energy/`L²` bound (a Lyapunov function `V = (r² − R₀)²/4`, `dV/dt ≤ 0`, global attraction to the saturated
heartbeat amplitude `r* = √2`) and no current-null crossing (a measure-zero, benign set), does the driven
near-Beltrami limit cycle admit an a-priori **enstrophy / Beale–Kato–Majda** bound
`∫₀^∞ ‖ω‖_∞ dt < ∞`? This is category-identical to open large-data 3D regularity (Beale, Kato & Majda 1984;
Chae, Degond & Liu 2014). We close it **conditionally**, without solving general Navier–Stokes.

**Lemma (exact vortex-stretching = Lamb-vector flux).** For a smooth divergence-free field `v` on `𝕋³`,
`ω = ∇×v`,
```
   P := ∫ ω·(ω·∇)v dx = ∫ (∇×ω)·(v×ω) dx .                              (1)
```
*Proof.* The identity `(ω·∇)v = ∇×(v×ω) + (v·∇)ω` (both fields divergence-free) and
`∫ ω·(v·∇)ω = ½∫ v·∇|ω|² = 0` give `P = ∫ ω·∇×(v×ω)`; integrating by parts yields (1). ∎ Thus vortex
stretching is *exactly* a flux of the **Lamb vector** `L = v×ω`, and vanishes identically at a force-free state
(`L = 0`) — production is controlled *linearly* by the deviation, not by a generic strain norm. Both forms of
(1) agree to `~9` significant figures numerically on a generic field where `P ≠ 0`.

**Linear inequality.** The enstrophy balance `dZ/dt = P − ν‖∇ω‖₂² + F` (`Z = ½‖ω‖₂²`) with (1),
Cauchy–Schwarz `|P| ≤ ‖∇ω‖₂‖L‖₂`, Young, and Poincaré `‖∇ω‖₂² ≥ λ₁‖ω‖₂²` gives
```
   dZ/dt ≤ −β(t) Z + F(t),     β(t) = ν λ₁ − η(t)²/ν,                   (2)
```
where `η = δ‖v‖_∞` and `δ = ‖v×ω‖₂/(‖v‖_∞‖ω‖₂) ∈ [0,1]` is the Beltrami deviation. The classical route yields
instead a supercritical `Z³` term; the exact identity (1) is what makes (2) **linear**.

**Theorem (conditional a-priori enstrophy bound).** On the `T`-periodic driven orbit, if the amplitude is
bounded (`‖v‖_∞ ≤ U*`, the coherent-object regime) and the time-averaged deviation is sub-threshold,
```
   ⟨η²⟩ := (1/T)∫₀^T η² dt < ν² λ₁     ⟺     δ_rms ≲ 2π/Re,   Re = U*L/ν,   (3)
```
then `sup_t Z(t) < ∞`. Consequently `‖ω‖₂` is uniformly bounded; by the 3D `H¹`⇒regularity criterion the orbit
is globally smooth and the Beale–Kato–Majda integral stays finite — **the driven heartbeat is globally
regular**. *(Proof: forcing is absorbed by Young; `⟨β⟩ > 0` gives a Gronwall bound
`sup Z ≤ e^{2B̃T}(Z(0) + 2Q/⟨β⟩)`.)* Condition (3) is **time-integrated**, not pointwise: the deviation may
spike each heartbeat provided its average stays sub-threshold — verified numerically, with the boundedness
transition sharp at `⟨η²⟩ = ν²λ₁`.

**Hall two-fluid lift.** The ion generalized vorticity `Ω = B + d_i ω` is frozen into the ion flow,
`∂_t Ω = ∇×(v×Ω) +` dissipation, so (1) ports verbatim to the *independent* divergence-free pair `(v, Ω)`
(verified to machine precision), and the canonical Lamb vector vanishes on the double-Beltrami state. The
conditional bound carries over at **unit magnetic Prandtl number** `Pm = ν/η = 1`, where the two-fluid
dissipation collapses to the perfect square `η‖∇Ω‖₂²`; for `Pm ≠ 1` the dissipation quadratic form is
indefinite (`det = −d_i²(η−ν)²/4 < 0`), the precise obstruction that localizes the remaining Hall difficulty.

## 7. Scope and discussion

The identification "matter is the flow of the knot" is admissible only for a knot that is being actively
driven; in a frozen or self-organizing field it is provably barred. The lead statement is a **`[V]` no-go /
well-founded postulate in the frozen regimes** (static and aligned/steady, both proven), a
**constructed-realizable closure `[S`→`V]` in the driven regime**, a **first-class selection negative** (it is
driven, not emergent), and a **conditional `[V]` closure of the regularity gate** under the explicit drive
hypothesis (3). What is *not* claimed: unconditional closure — at the object's Lundquist number `S ~ 10²–10⁶`
the `O(1/Re)` condition (3) is stringent and unproven, and the `Pm ≠ 1` Hall case requires a coupled
fluid+magnetic enstrophy functional. No over-unity is claimed; the density leg stays `[V]`; canonical helicity
is a genuine ideal conserved current `[V]/[credited]`. The results stand independently of any wider synthesis:
a self-contained plasma / topological-fluid contribution.

## 8. Conclusion

Whether a topological helicity current can be a matter current is decided leg by leg: the density leg holds; the
static and aligned/steady current legs are proven no-gos unified by a single magnitude-homogeneity obstruction;
the driven leg is constructively realizable but dynamically un-selected; and the sole regularity gate is closed
conditionally by an exact Lamb-vector identity that linearizes the enstrophy inequality, with an explicit,
falsifiable `O(1/Re)` drive criterion and a clean `Pm = 1` Hall lift. The open frontier is sharply named:
prove (3) at the object's Reynolds, and control the `Pm ≠ 1` coupled enstrophy.

## References

Beale, J.T., Kato, T. & Majda, A. (1984). *Commun. Math. Phys.* **94**, 61.
Chae, D., Degond, P. & Liu, J.-G. (2014). *Ann. IHP C* **31**, 555.
Chandrasekhar, S. & Kendall, P.C. (1957). *ApJ* **126**, 457.
Mahajan, S.M. & Yoshida, Z. (1998). *PRL* **81**, 4863.
Moffatt, H.K. (1969). *JFM* **35**, 117.
Steinhauer, L.C. & Ishida, A. (1997). *PRL* **79**, 3423.
Taylor, J.B. (1974). *PRL* **33**, 1139.
Woltjer, L. (1958). *PNAS* **44**, 489.
Bae, Kang & Shin (2025), arXiv:2504.07629 (double-Beltrami states in Hall MHD).

*Verification scripts (identity, Gronwall closure, Hall coercivity) and full derivations:
`results/verify/` in the project repository. No number in this paper is fabricated; ASCII apart from standard
math symbols.*
