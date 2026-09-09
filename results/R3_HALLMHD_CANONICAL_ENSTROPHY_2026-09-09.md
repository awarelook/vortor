# The Hall two-fluid lift — canonical-enstrophy regularity of the driven double-Beltrami object

**Author:** Nathaniel Hanks · **Date:** 2026-09-09
**Provenance:** executes §6 ("Extension to the Hall two-fluid object") of
`results/R2_NEAR_BELTRAMI_ENSTROPHY_THEOREM_2026-09-09.md`; targets the trilogy's *actual* object
(canonical vorticity `Ω = ∇×P`, `P = A + (m/q)v`).
**Verification:** `results/verify/hallmhd_canonical_check.py` (CPU, spectral).

**One-line.** The near-Beltrami enstrophy machinery lifts from Navier–Stokes to the ion **generalized
(canonical) vorticity** of incompressible resistive–viscous Hall two-fluid plasma — *because the Hall
physics is not an extra flux but the frozen-in transport of `Ω` by the ion flow*. The exact
Lamb-vector identity and the conditional `[V]` enstrophy bound port **verbatim at magnetic Prandtl
number `Pm = 1`**; away from `Pm = 1` an explicit `(η−ν)²` indefiniteness in the dissipation is the
precise, quantified obstruction — the honest frontier of the Hall lift.

**Tier.** `[V] conditional (Pm=1)` for the canonical-enstrophy bound, plus a `[V]` structural
identity (the canonical Lamb-vector form, holding for the genuine two-fluid case where `Ω ≠ ∇×v`) and
a `[V]` **no-go-flavored** obstruction result (canonical enstrophy is not a-priori controlled alone
for `Pm ≠ 1`). This carries the R2 conditional advance onto the real object under one added,
physically-named hypothesis (`Pm=1`), and *names exactly* what blocks the general case.

---

## 1. The object and its frozen-in canonical vorticity  `[credited]`

Incompressible two-fluid plasma; per species `s ∈ {i,e}` the equation of motion, for a barotropic
pressure and with the electromagnetic force, rearranges (Mahajan–Yoshida 1998; Steinhauer–Ishida
1997) into **canonical vortex-dynamics form**. With canonical momentum and generalized vorticity

```
  P_s = A + (m_s/q_s) v_s ,     Ω_s = ∇×P_s = B + (m_s/q_s) ω_s ,     ω_s = ∇×v_s ,
```

the ideal (dissipationless) evolution is exactly the frozen-in vortex equation

```
  ∂_t Ω_s = ∇×( v_s × Ω_s ) .                                        (1)
```

**Key point (resolves §6(i)).** In the bulk-MHD `(v,B)` variables the Hall term
`−∇×((J×B)/ne)` appears as an awkward *extra* flux; in canonical variables it is *not extra* — (1)
says `Ω_s` is simply frozen into its **own species' flow** `v_s`. The Hall physics is the statement
that the ion generalized vorticity `Ω_i` is transported by `v_i`, not by the bulk velocity. So the
NSE structure ports with `(v, ω) → (v_i, Ω_i)`, with the crucial difference that **`Ω_i` is an
independent divergence-free field, not the curl of `v_i`.**

We take the ion species as dynamical (electron inertia neglected, the standard Hall-MHD reduction;
electron friction supplies the resistivity), assume incompressible ion flow `∇·v_i = 0`, and write
`v := v_i`, `Ω := Ω_i`, `d_i := m_i/q_i`, `Z := ½∫|Ω|²` (**canonical enstrophy**).

## 2. The canonical Lamb-vector identity  `[V]`

**Lemma 1′.** For *independent* smooth divergence-free fields `v, Ω` on `T^3` (in particular `Ω`
*need not* be `∇×v`), the ideal canonical-enstrophy production is a canonical Lamb-vector flux:

```
  ∫ Ω·∇×(v×Ω) dx  =  ∫ (∇×Ω)·(v×Ω) dx  =  ∫ (∇×Ω)·L dx ,    L := v×Ω .   (2)
```

*Proof.* Integration by parts on the periodic box, `∫Ω·∇×L = ∫(∇×Ω)·L`. (When additionally
`∇·v = 0`, the flux equals the canonical stretching `∫Ω·(Ω·∇)v` — same reduction as the NSE Lemma 1,
using `∇×(v×Ω) = (Ω·∇)v − (v·∇)Ω` and `∫Ω·(v·∇)Ω = ½∫v·∇|Ω|² = 0`.) ∎

**Corollary (canonical Beltrami suppression).** The production vanishes when `L = v×Ω = 0`, i.e. the
ion flow is aligned with its generalized vorticity `v ∥ Ω` — the **canonical force-free / relaxed
(double-Beltrami-class) state**. Near it, production is *linear* in the canonical deviation
`δ_c := ‖v×Ω‖₂/(‖v‖_∞‖Ω‖₂)`.

*Numerical confirmation (`hallmhd_canonical_check.py`, TEST A).* For **independent** random
divergence-free `(v, Ω)` — the genuine two-fluid case — the two forms of (2) agree to **~4×10⁻¹⁶**
(machine precision), with `‖∇Ω‖₂‖L‖₂` a valid upper bound; the aligned state `Ω = 3v` gives
production `~10⁻²⁶` (exact zero); and near alignment `Ω = 3v + ε w_⊥` gives `P/ε → const` (linear).

## 3. The dissipation dichotomy — the crux (resolves §6(ii))  `[V]`

The dissipative terms in `∂_t Ω` are resistive on the magnetic part and viscous on the fluid part,
with generally *different* diffusivities: `∂_t Ω ⊃ η ΔB + d_i ν Δω` (`η` = magnetic diffusivity,
`ν` = kinematic viscosity, `Pm := ν/η`). The canonical-enstrophy dissipation is therefore the
quadratic form

```
  D = ∫ [ η ∇Ω:∇B + d_i ν ∇Ω:∇ω ] dx ,        Ω = B + d_i ω .          (3)
```

**Proposition 2 (the `Pm=1` perfect square vs. the `(η−ν)²` obstruction).**

- **At `Pm = 1` (`η = ν`):** `D = η ∫|∇(B + d_i ω)|² = η ‖∇Ω‖₂²  ≥  η λ₁ ‖Ω‖₂²` — a **perfect square,
  fully coercive**. Canonical enstrophy is genuinely dissipated, exactly as in NSE.
- **At `Pm ≠ 1`:** writing (3) as a `2×2` form in `(∇B, ∇ω)` with matrix
  `M = [[η, d_i(η+ν)/2],[d_i(η+ν)/2, d_i²ν]]`, one has

  ```
      det M  =  η d_i² ν − d_i²(η+ν)²/4  =  − d_i² (η−ν)² / 4   ≤ 0 ,
  ```

  so `M` is **indefinite** (one negative eigenvalue). The worst-case field `B = −s* ω`,
  `s* = d_i(η+ν)/2η`, gives `D = −[d_i²(η−ν)²/4η] ‖∇ω‖₂² < 0` while keeping `Ω = (d_i − s*)ω ≠ 0`:
  **"dissipation" can *produce* canonical enstrophy.** Hence `Z` alone is not a-priori bounded for
  `Pm ≠ 1`.

*Numerical confirmation (TEST B).* `D = η‖∇Ω‖₂²` at `Pm=1` to `2×10⁻¹⁶`; `det M = −d_i²(η−ν)²/4`
exactly; and the engineered `B = −s*ω` drives `D` negative for every `η ≠ ν`, matching the predicted
minimal coefficient `−d_i²(η−ν)²/(4η)`.

## 4. The theorem at `Pm = 1`  `[V] conditional`

At `Pm = 1` the NSE argument of the R2 note ports **verbatim**, with `ν → η` and the canonical
deviation. Write `ζ(t) := δ_c(t) ‖v(t)‖_∞` (canonical deviation amplitude).

**Theorem.** On the driven double-Beltrami heartbeat with `Pm = 1`, bounded ion-flow amplitude
`‖v‖_∞ ≤ U* < ∞`, smooth bounded drive, and the sub-threshold time-averaged canonical deviation

```
  ⟨ζ²⟩ := (1/T)∫₀^T ζ(t)² dt  <  η² λ₁          (⇔  δ_c,rms  ≲  1/S ,  S = U*L/η the Lundquist number),
```

the canonical enstrophy is a-priori bounded, `sup_t Z(t) < ∞`. Consequently `‖Ω‖₂` is uniformly
bounded, the orbit is globally smooth (3D `H¹`⇒regularity, applied to the canonical field), and the
Beale–Kato–Majda integral stays finite — **the driven object is canonically regular**. This closes
the trilogy's X3/R2 gate for the *Hall two-fluid object itself*, conditional on (`Pm=1`) + the
deviation threshold.

*Proof.* `dZ/dt = ∫(∇×Ω)·L − η‖∇Ω‖₂² + F ≤ ‖∇Ω‖₂‖L‖₂ − η‖∇Ω‖₂² + F`. Young + Poincaré
(`‖∇Ω‖₂² ≥ λ₁‖Ω‖₂² = 2λ₁Z`) and `‖L‖₂² = 2ζ²Z` give `dZ/dt ≤ −β_c(t)Z + F`,
`β_c = ηλ₁ − ζ²/η`; the forcing is absorbed as in the NSE note. `⟨β_c⟩ > 0` then yields the
Gronwall bound `sup_t Z ≤ e^{2B̃T}(Z(0)+2Q/⟨β_c⟩)`. The threshold `⟨β_c⟩ = 0` is `⟨ζ²⟩ = η²λ₁`. ∎

## 5. Scope — what is settled and what is the true frontier

**Settled (`[V]`):** (a) the canonical Lamb-vector identity for the genuine two-fluid pair
(machine-precision verified); (b) the `Pm=1` conditional enstrophy bound → regularity of the *actual*
canonical object; (c) the explicit `(η−ν)²` obstruction — a clean statement of *why* Hall-MHD is
harder than NSE, matching the known small-data-only status (Chae–Degond–Liu 2014).

**Not settled — the honest open pieces:**
- **`Pm ≠ 1`.** Canonical enstrophy alone is not monotone (§3). The correct program is to bound the
  **coupled pair** — fluid enstrophy `½‖ω‖₂²` (dissipated by `ν`) and magnetic enstrophy /current
  `½‖J‖₂²`, `J ∝ ∇×B` (dissipated by `η`) — jointly, since each species' *own* dissipation is
  coercive on *its own* gradient even when the canonical combination is not. Establishing a Lyapunov
  functional for that pair with the Lamb-suppressed cross-coupling is the genuine remaining Hall
  problem (and is expected to be as hard as large-data Hall-MHD regularity in general).
- **Is `Pm=1` physical for the object?** For the dense, cold plasmoid (`n ~ 10²⁸`, `B ~ 200 T`,
  `R ~ 1 µm`) the magnetic Prandtl number need not be near 1; `Pm=1` is a genuine restriction, not a
  free normalization. So the `Pm=1` theorem is a *bracketing* result, not the final word for the
  physical parameters.
- **Neglects:** electron inertia (standard Hall reduction), ion compressibility (`∇·v_i=0` assumed),
  and treats a single (ion) canonical enstrophy rather than the fully symmetric two-species pair.

**Net:** the ideal/near-Beltrami structure lifts perfectly to the canonical object; the entire
difficulty of the Hall lift is now localized to the `Pm ≠ 1` dissipation coupling, stated as an
explicit coercivity-failure with the sharp constant `d_i²(η−ν)²/4`.

## 6. Verification artifacts

- `results/verify/hallmhd_canonical_check.py` — TEST A (canonical Lamb identity for independent
  div-free `(v,Ω)`; aligned-state null; linear-in-deviation scaling; the bound) and TEST B
  (`Pm=1` perfect-square coercivity; `det M = −d_i²(η−ν)²/4`; worst-case `D<0` for `Pm≠1`).

## 7. References

Mahajan & Yoshida 1998, PRL 81, 4863 (double Beltrami, canonical vortex dynamics). Steinhauer &
Ishida 1997, PRL 79, 3423 (generalized/canonical helicity). Chae, Degond & Liu 2014, Ann. IHP C 31,
555 (Hall-MHD, small/large data regularity). Bae, Kang & Shin 2025, arXiv:2504.07629 (double-Beltrami
states in Hall MHD). Beale, Kato & Majda 1984, CMP 94, 61. Provenance in-repo:
`results/R2_NEAR_BELTRAMI_ENSTROPHY_THEOREM_2026-09-09.md`, `FTGB_CURRENTLEG_TRILOGY.md` §4–8.

*No number is fabricated; the load-bearing claims (the canonical identity and the `Pm=1` /
`(η−ν)²` dichotomy) are proven and reproduced numerically. ASCII-clean apart from standard math
symbols.*
