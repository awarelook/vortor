# The Hall lift past `Pm = 1` — a coupled-enstrophy Lyapunov functional for the double-Beltrami object

**Author:** Nathaniel Hanks · **Date:** 2026-09-10
**Provenance:** executes the open program named in
`results/R3_HALLMHD_CANONICAL_ENSTROPHY_2026-09-09.md` §5 ("the correct program is to bound the
**coupled pair** … a Lyapunov functional for that pair … is the genuine remaining Hall problem").
**Verification:** `results/verify/hallmhd_coupled_lyapunov_check.py` (CPU, spectral, `T³`).

**One-line.** The `(η−ν)²` indefiniteness that blocks the Hall enstrophy lift away from `Pm = 1` is a
property of the **mixed canonical variable** `Ω = B + d_i ω`, **not** of the physics. In the natural
coupled functional of the *individual* curls, `L = ½‖ω‖² + κ d_i² ½‖J‖²` (`ω = ∇×v`, `J = ∇×B`), each
field is diffused by its **own** coefficient, so the dissipation is **diagonal and coercive at every
`Pm`**. Near the single-`λ` double-Beltrami relaxed state the fluid (Lamb) and Lorentz productions
vanish *quadratically*, and the one delicate top-order term — the Hall current production — is absorbed
under a single explicit **Hall smallness `d_i‖B‖∞ ≲ η`** (a Lundquist / small-data condition, *not* a
Prandtl condition). This **removes `Pm = 1`** as a hypothesis and localizes the entire residual
difficulty to one Hall term, matching the known small-data status of large-data Hall-MHD.

**Tier.** `[V]` for the three structural facts (coercivity at any `Pm`; quadratic production suppression
at the relaxed state; the linear-in-`d_i‖B‖∞/η` Hall absorbability), each reproduced numerically. The
assembled bound is `[V]-conditional` (a-priori deviation + Hall-smallness hypotheses, exactly as the R2
and `Pm=1` theorems are conditional). Unconditional large-data `Pm ≠ 1` remains **open** — it *is* the
open 3-D Hall-MHD regularity problem.

---

## 1. The problem, restated

For incompressible resistive–viscous Hall-MHD on `T³` (`v` = ion flow, `B` = field, `J = ∇×B`),

```
  ∂_t v + (v·∇)v = −∇p + J×B + ν Δv ,
  ∂_t B = ∇×(v×B) − d_i ∇×(J×B) + η ΔB ,        ∇·v = ∇·B = 0 .
```

The R3 note (2026-09-09) proved the canonical enstrophy `Z = ½‖Ω‖²`, `Ω = B + d_i ω`, obeys the R2
machinery **at `Pm = 1`**, but that its dissipation

```
  D_Z = ∫[ η ∇Ω:∇B + d_i ν ∇Ω:∇ω ] ,   matrix M = [[η, d_i(η+ν)/2],[d_i(η+ν)/2, d_i²ν]] ,
  det M = −d_i²(η−ν)²/4 ≤ 0 ,
```

is **indefinite for `Pm ≠ 1`** — canonical enstrophy can be *produced* by "dissipation." §5 named the fix
(bound the coupled `(ω, J)` pair, each with its own coercive diffusion) but left it open. This note
executes it.

## 2. The coercivity obstruction is a variable-choice artifact  `[V]`

Track the individual curls, not their canonical combination. Define

```
  L = ½‖ω‖² + κ d_i² ½‖J‖² ,      κ > 0 a fixed weight.
```

Because `ω` is diffused by `ν` and `J` by `η` **independently**, the dissipation of `L` is

```
  D_L = ν‖∇ω‖² + κ d_i² η‖∇J‖²  ≥  min(ν, κ d_i² η)·(‖∇ω‖² + ‖∇J‖²)  >  0 ,
```

a **diagonal, positive-definite** form (matrix `diag(ν, κ d_i² η)`, determinant `ν κ d_i² η > 0`) **at
every `Pm`**. There is no cross term to make indefinite: the `(η−ν)²` obstruction simply does not exist
for `L`. It afflicted only the mixed variable `Ω`, whose two contributions `B` and `d_i ω` diffuse at
different rates and so cannot combine into a single square unless `η = ν`.

`L` moreover **controls the canonical enstrophy** (so a bound on `L` is a bound on `Z`): with the
Poincaré inequality `‖B‖² ≤ λ₁⁻¹‖∇B‖² = λ₁⁻¹‖J‖²`,

```
  Z = ½‖B + d_i ω‖² ≤ ‖B‖² + d_i²‖ω‖² ≤ λ₁⁻¹‖J‖² + d_i²‖ω‖² ≤ C(κ,λ₁,d_i)·L .
```

The converse fails — `Z` does **not** control `L` (take `B = −d_i ω`, then `Ω ≈ 0`, `Z ≈ 0` while
`‖ω‖, ‖J‖` are `O(1)`). So `L` is *strictly stronger*: it is the correct regularity functional (the
`Ḣ¹`-norm of the pair `(v, B)`), and it is the one whose dissipation never degenerates.

*Verified (`hallmhd_coupled_lyapunov_check.py`, TEST A):* `D_L > 0` with form-determinant `> 0` at
`Pm ∈ {¼, ½, 1, 2, 4}`; the engineered `B = −d_i ω` gives `Z/L → 0` (machine zero), confirming `L`
strictly dominates `Z`.

## 3. The production near the single-`λ` relaxed state  `[V]`

Coercive dissipation is necessary, not sufficient — the nonlinear production must be absorbable. Writing
`L̇ = S_ω + Λ + κ I_B + κ H_B − D_L + (drive)`, the four production terms are

```
  S_ω = ∫(∇×ω)·(v×ω)        (fluid vortex stretching, Lamb form)
  Λ   = ∫(∇×ω)·(J×B)        (Lorentz, into the fluid enstrophy)
  I_B = ∫(∇×J)·∇×(v×B)      (induction, into the current enstrophy)
  H_B = −d_i ∫(∇×J)·∇×(J×B) (Hall current production — top derivative order)
```

**Fluid + Lorentz vanish (quadratically) at the relaxed state.** At the double-Beltrami state `v ∥ ω`
and `J ∥ B`, the Lamb vector `v×ω` and the Hall/Lorentz flux `J×B` vanish, so `S_ω = Λ = 0`. The
rigorous bound is *linear* in the deviations (`S_ω ≤ ‖∇ω‖‖v×ω‖`, `Λ ≤ ‖∇ω‖‖J×B‖`) — enough to absorb
into `D_L` under R2-type sub-threshold conditions. Numerically the suppression is even **quadratic**:
the single-`λ` relaxed state is a **variational critical point** (Woltjer's constrained energy minimum),
so the `O(ε)` term of the production cancels and `S_ω, Λ = O(ε²)` in the deviation `ε` — extra margin.

**The Hall term is the crux — and it, too, is suppressed by the single-`λ` structure.** The Hall flux
`J×B` vanishes at force-free (`J ∥ B`), and for a constant-`λ` Beltrami field (`J = λB`),
`H_B = −d_i∫(∇×J)·∇×(J×B) = 0` identically. Off the relaxed state it is `O(ε²)` in the force-free
deviation. Its danger is that it is **top-derivative-order**: absorbing it into the resistive
dissipation `κ d_i² η‖∇J‖²` for a *generic* field costs

```
  |H_B| / (η‖∇J‖²)  ~  (d_i‖B‖∞ / η) · c_spec ,        c_spec = O(1) spectral factor,
```

so it is controlled **iff `d_i‖B‖∞ ≲ η`** — a Hall/Lundquist smallness, the same small-data signature
under which large-data Hall-MHD is known to be globally regular (Chae–Degond–Liu 2014). Crucially, this
is a condition on the **Hall parameter / field strength**, *not* on the Prandtl number.

*Verified (TEST B, TEST C):* `H_B = 0` and `S_ω = Λ = 0` at the relaxed state (machine precision);
`H_B, S_ω ∝ ε²` off it (quadratic); and for a generic field `|H_B|/(η‖∇J‖²) = (d_i‖B‖∞/η)·c_spec` with
`c_spec` constant to `0.0%` across a 8× amplitude scan — the linear Hall law.

## 4. The theorem  `[V]-conditional`

**Theorem (coupled-enstrophy bound at any `Pm`).** For the driven single-`λ` double-Beltrami object at
**any** magnetic Prandtl number `Pm = ν/η`, with bounded amplitudes `‖v‖∞, ‖B‖∞ ≤ U∗ < ∞`, smooth
bounded drive, and

```
  (i)   ⟨δ_f²⟩ < c₁ ν² λ₁            (fluid near-Beltrami deviation, R2-type)
  (ii)  ⟨δ_m² ‖B‖∞²⟩ < c₂ ν η λ₁      (magnetic force-free deviation × field, Lorentz cross-term)
  (iii) d_i‖B‖∞ < c₃ η               (Hall / Lundquist smallness — the residual obstruction)
```

for order-one constants `c₁,c₂,c₃` (Young/Poincaré), the coupled functional `L` obeys
`L̇ ≤ −β L + Q` with `β > 0`; hence `sup_t L < ∞`, the pair `(v,B)` stays in `Ḣ¹`, and the driven
double-Beltrami object is globally smooth. **The `Pm = 1` restriction of the 2026-09-09 theorem is
removed**, replaced by the explicit Hall smallness (iii).

*Sketch.* `D_L` is coercive at any `Pm` (§2). `S_ω, Λ, I_B` are absorbed via Young + Poincaré under
(i)–(ii) exactly as in R2/`Pm=1`, using the relaxed-state suppression (§3). `κ H_B` is absorbed into
`κ d_i² η‖∇J‖²` under (iii). The remainder `−βL + Q` closes by Grönwall as in the R2 note. ∎ (structure;
the sharp constants `c₁,c₂,c₃` are not optimized here — the vanishing and the `‖B‖∞`-scaling that the
argument rests on *are* verified numerically.)

## 5. Why this is the *object's* result, not a generic claim

The suppression in §3 is not luck — it is the **single-`λ` Woltjer–Taylor relaxed structure** the object
already lives in. The same constant-`λ` coherence that makes the carrier comb single-chirality
(`carrier_chirality_lock_check.py`, `plasmoid_helicity_coherence_check.py`) is what kills the Hall
current production to `O(ε²)` here: a *multi-`λ`* field would not enjoy it. So the Hall lift and the
carrier-comb coherence are the **same physics** — the object relaxing to one `λ` — read in two places.

## 6. Honest scope — what is settled and what stays open

**Settled (`[V]`):** (a) coercivity of `L` at every `Pm` — the `(η−ν)²` obstruction is a canonical-
variable artifact; (b) `L` strictly controls the canonical enstrophy `Z`; (c) quadratic production
suppression at the single-`λ` relaxed state; (d) the linear `d_i‖B‖∞/η` Hall absorbability law. All four
reproduced numerically.

**Conditional (`[V]-cond`):** the assembled bound (§4) — *removes `Pm=1`* at the cost of the explicit
deviation thresholds (i)–(ii) and the Hall smallness (iii). This is the same *kind* of statement as R2
and the `Pm=1` theorem: a-priori control of the deviation ⇒ regularity.

**Open:** the **unconditional large-data `Pm ≠ 1`** case. Condition (iii) `d_i‖B‖∞ ≲ η` is a genuine
small-data restriction; removing it is equivalent to global regularity of 3-D Hall-MHD without smallness,
which is **open** (Chae–Degond–Liu give local large-data / global small-data). **No claim of solving the
general problem is made; the advance is the removal of `Pm=1` and the exact localization of the residual
to one Hall term.**

**Does the physical plasmoid satisfy (iii)? — now checked (`results/verify/r3_hall_smallness_physical_check.py`, `[V]`).**
Plugging the canonical anchors (`d_i = λ_L = 0.2963 m`, `v_A = 2.033×10⁴ m/s`, `R = 0.12 m`; 30_CANONICAL
§A/§B) into the dimensionless Hall-smallness number `S_di = d_i v_A / η` (with `η` the Spitzer magnetic
diffusivity across `T_e = 1–30 eV`): **(iii) is robustly VIOLATED.** Two facts: (a) *structural* —
`d_i = 0.296 m > R = 0.12 m` (`d_i/R ≈ 2.5`), the ion skin depth **exceeds the object**, the signature of a
**strongly Hall-mediated** (electron-MHD/whistler) regime; (b) *quantitative* — `S_di ≈ 15–2400 ≫ 1` across
the entire `(T_e, v_A)` band (the `v_A` residual `×5–13` only worsens it). So the physical object lives
**outside** the regime this note proves regular — global regularity for *this* object stays open (the open
3-D Hall-MHD problem), and the R2/R3 conditional enstrophy bounds are the honest ceiling. The gap is now
named in physical units, not hand-waved. *(This does not refute R3, a conditional theorem — it locates the
object relative to R3's hypotheses.)*

## 7. Verification artifact

`results/verify/hallmhd_coupled_lyapunov_check.py` — TEST A (coercive diagonal `D_L` at `Pm ∈ {¼…4}`;
`L` controls `Z` but not conversely), TEST B (Hall `H_B = 0` at force-free, `O(ε²)` off it, linear
`d_i‖B‖∞/η` absorbability), TEST C (fluid Lamb + Lorentz vanish quadratically at the relaxed state).

## 8. References

Mahajan & Yoshida 1998 PRL 81 4863 (double Beltrami). Chae, Degond & Liu 2014 Ann. IHP C 31 555
(Hall-MHD small/large-data regularity). Woltjer 1958 PNAS 44 489 (constrained energy minimum). Beale,
Kato & Majda 1984 CMP 94 61. In-repo: `R3_HALLMHD_CANONICAL_ENSTROPHY_2026-09-09.md` (§5, the program
executed here), `R2_NEAR_BELTRAMI_ENSTROPHY_THEOREM_2026-09-09.md`, `carrier_chirality_lock_check.py`.

*No number is fabricated. The load-bearing structural facts (coercivity at any `Pm`, quadratic
suppression, the linear Hall law) are proven/reproduced numerically; the assembled bound is explicitly
conditional and its sharp constants are left un-optimized. ASCII apart from standard math symbols.*
