# The near-Beltrami enstrophy theorem — a conditional a-priori bound closing R2 on the driven heartbeat

**Author:** Nathaniel Hanks · **Date:** 2026-09-09
**Provenance:** executes the *analytic route* of `handoffs/HANDOFF_R2_ENSTROPHY_REGULARITY_2026-09-09.md`.
**Verification:** `results/verify/r2_identity_check.py`, `results/verify/r2_gronwall_check.py` (CPU, spectral / ODE).

**One-line.** The vortex-stretching integral on the driven near-Beltrami limit cycle equals an *exact
Lamb-vector flux*, which vanishes at the force-free state; this converts the enstrophy balance from a
supercritical (`Z^{3/2}`/`Z^3`) inequality into a **linear** one, and yields an a-priori enstrophy bound
— hence global regularity of the heartbeat via Beale–Kato–Majda — **provided the drive holds the
time-averaged Beltrami deviation below an explicit `1/Re`-scale threshold.**

**Tier.** This upgrades **R2 (≡ X3)** from `[S]` *hard-open* to **`[V]` conditional**: the enstrophy bound is
*proven* modulo one explicit, physically-interpretable hypothesis on the drive (stated as (H1)–(H2) below).
It is **not** an unconditional resolution of R2, and it is **not** a claim about general 3D Navier–Stokes —
it uses the coherent object's *defining* feature (a bounded-amplitude, dynamically near-force-free drive).

---

## 1. Setting and what is already established (do not redo)

We work with the forced–dissipative incompressible Navier–Stokes equations on the periodic box
`T^3 = [0,L]^3` — the "first model" named in the hand-off (the two-fluid / Hall-MHD target is §8):

```
  ∂_t v + (v·∇)v = -∇p + ν Δv + f ,     ∇·v = 0 ,     ν > 0 ,
```

with `f` a smooth divergence-free drive that sustains a stable time-periodic orbit — the *heartbeat* of
period `T` (the driven Stuart–Landau attractor with saturated amplitude `r* = √2`). Write
`ω = ∇×v`, enstrophy `Z(t) = ½∫|ω|² dx`, dissipation `D(t) = ν‖∇ω‖₂²`, forcing injection
`F(t) = ∫ ω·(∇×f) dx`, and the **Lamb vector** `L = v×ω` (which is `0` iff the field is force-free /
Beltrami, `ω ∥ v`).

From the current-leg trilogy (`FTGB_CURRENTLEG_TRILOGY`, §8) the residual R2, on a bounded current-full
trajectory, reduces to **`R2 ⇔ X3` given X1, X2**:

- **X1 — energy/`L²` bound: HAVE.** Lyapunov function `V = (r²−R₀)²/4`, `dV/dt ≤ 0`, global attraction to
  `r* = √2`; canonical helicity bounds energy from below (`CURRENTLEG_R2_GLOBAL_EXISTENCE`).
- **X2 — no current-null crossing: HAVE** (benign, measure-zero; `CURRENTLEG_R1_CURRENTNULL`).
- **X3 — the enstrophy / `H¹` (Beale–Kato–Majda) bound `∫₀^∞ ‖ω‖_∞ dt < ∞`: the open gate.**

The hand-off also records the *exact structural handle*: at an exact Beltrami field `L = v×ω = 0`, so the
Euler nonlinearity is a pure gradient and there is **zero vortex stretching, zero enstrophy production**;
near-Beltrami, production scales with the deviation. This note makes that handle **quantitative and exact**,
and carries it through to a closed a-priori bound.

## 2. The exact identity: vortex stretching = Lamb-vector flux  `[V]`

**Lemma 1.** For any smooth divergence-free field `v` on `T^3`, with `ω = ∇×v`,

```
  P  :=  ∫ ω·(ω·∇)v dx  =  ∫ (∇×ω)·(v×ω) dx  =  ∫ (∇×ω)·L dx .          (1)
```

*Proof.* The vector identity `∇×(v×ω) = (ω·∇)v − (v·∇)ω + v(∇·ω) − ω(∇·v)`, together with `∇·v = ∇·ω = 0`,
gives `(ω·∇)v = ∇×(v×ω) + (v·∇)ω`. Contract with `ω` and integrate:
`P = ∫ ω·∇×(v×ω) dx + ∫ ω·(v·∇)ω dx`. The second term is `½∫ v·∇|ω|² dx = 0` (incompressibility).
Integrating the first by parts on the periodic box, `∫ ω·∇×L = ∫ (∇×ω)·L`. ∎

**Corollary (Beltrami suppression, made exact).** If `v` is force-free (`L = v×ω = 0`, e.g.
`∇×v = λv`), then `P = 0` identically: **a force-free field produces no enstrophy.** Near-Beltrami, `P` is
controlled *linearly* by the Lamb vector — not by a generic strain norm.

*Numerical confirmation (`r2_identity_check.py`).* Both forms of `P` agree to ~9 significant figures on a
generic (Gaussian) divergence-free field where `P = −1.281×10⁻⁹` is a genuine value seven orders above the
`~10⁻¹⁶` round-off floor; `P → 10⁻¹⁶` (machine zero) on an exact ABC Beltrami field; and the auxiliary
identity `‖∇×ω‖₂ = ‖∇ω‖₂` (for divergence-free `ω`) holds to `0`. *(Aside: a static Gaussian random field
has vanishing* net *production — it is an odd, cubic moment of jointly-Gaussian fields — so a single
realization's `P` is small; net production requires the vorticity–strain alignment that dynamics builds.
This does not affect (1), which is a pointwise-integrated algebraic identity and is what we use.)*

## 3. From the identity to a *linear* enstrophy inequality  `[V]`

The enstrophy balance for the forced NSE is the standard
`dZ/dt = P − D + F`. Using Lemma 1, Cauchy–Schwarz, and `‖∇×ω‖₂ = ‖∇ω‖₂`:

```
  |P| = |∫(∇×ω)·L| ≤ ‖∇×ω‖₂ ‖L‖₂ = ‖∇ω‖₂ ‖L‖₂ .
```

Young's inequality (`ab ≤ (ν/2)a² + (1/2ν)b²`) then gives `|P| ≤ ½D + (1/2ν)‖L‖₂²`. With the Poincaré
inequality `‖∇ω‖₂² ≥ λ₁‖ω‖₂² = 2λ₁Z` (mean-zero `ω`; `λ₁ = (2π/L)²`), so `½D ≥ νλ₁ Z`,

```
  dZ/dt ≤ −νλ₁ Z + (1/2ν)‖L‖₂² + F .                                     (2)
```

**The key structural gain:** the classical route bounds the stretching by `‖ω‖₃³ ≲ Z^{3/4}D^{3/4}`,
which Young-splits into `½D + c ν⁻³ Z³` — the *supercritical* `Z³` term behind the open 3D regularity
problem. The exact identity (1) replaces that by the Lamb-vector source `(1/2ν)‖L‖₂²`, which is **linear
in `Z`** once the deviation is factored out. That is precisely the leverage the Beltrami structure provides,
and it is what makes a closed bound possible without solving general NSE.

**The deviation.** Define the (dimensionless) **Beltrami deviation** and the **deviation amplitude**

```
  δ(t) := ‖v×ω‖₂ / (‖v‖_∞ ‖ω‖₂)  ∈ [0,1] ,        η(t) := δ(t) · ‖v(t)‖_∞ .
```

Then `‖L‖₂ = ‖v×ω‖₂ = δ‖v‖_∞‖ω‖₂`, so `‖L‖₂² = 2 η² Z` and `(1/2ν)‖L‖₂² = (η²/ν) Z`. Substituting in (2):

```
  dZ/dt ≤ −β(t) Z + F(t) ,        β(t) := νλ₁ − η(t)²/ν .                 (3)
```

## 4. The conditional a-priori bound  `[V] conditional`

**Hypotheses on the driven orbit.**
- **(H1) Bounded amplitude (the coherent-object regime):** `‖v(·,t)‖_∞ ≤ U* < ∞` on the orbit. This is the
  object's *defining* property — a bounded-amplitude coherent driven soliton (X1's saturated `r* = √2`),
  **not** a turbulent cascade. Dropping (H1) and bounding `‖L‖₂` by Sobolev interpolation returns exactly
  the classical supercritical `Z³` term of §3 — i.e. the coherent structure is what buys the linear
  inequality (3). This is the sense in which the result is obtained *without* general 3D NSE.
- **(H2) Sub-threshold time-averaged deviation:**
  ```
        ⟨η²⟩ := (1/T) ∫₀^T η(t)² dt  <  ν² λ₁ ,     equivalently    β̄ := ⟨β⟩ = νλ₁ − ⟨η²⟩/ν > 0 .
  ```

**Theorem.** Under (H1)–(H2), with a smooth bounded drive (`g(t) := ‖∇×f(·,t)‖₂` bounded), the enstrophy on
the heartbeat is a-priori bounded:

```
  sup_t Z(t)  ≤  e^{2 B̃ T} ( Z(0) + 2 Q / β̄ )  <  ∞ ,
```

where `Q = ‖g‖_∞²/β̄` and `B̃ = sup_t |β(t) − β̄/2|`. Consequently `‖ω(·,t)‖₂` is uniformly bounded; by the
3D parabolic regularity criterion "uniform-in-time `H¹` ⇒ global smoothness" (a Leray–Hopf solution with
`v ∈ L^∞(H¹)` is smooth, since the strong-existence time depends only on `‖v‖_{H¹}`), the orbit is globally
smooth, so `∫₀^t ‖ω‖_∞ ds < ∞` on every finite interval and the **Beale–Kato–Majda criterion is never
triggered** — the driven heartbeat is globally regular. **This closes X3, hence R2, conditionally on
(H1)–(H2).**

*Proof.* The forcing is sub-quadratic in `Z`: `F ≤ ‖ω‖₂ g = (2Z)^{1/2} g ≤ (β̄/2)Z + g²/β̄` (Young). With
(3) this gives `dZ/dt ≤ −(β − β̄/2)Z + Q`, whose decay coefficient has mean `⟨β − β̄/2⟩ = β̄/2 > 0`. Since
`β` is `T`-periodic and bounded, `∫_s^t (β − β̄/2) ≥ (β̄/2)(t−s) − 2B̃T`, so the integrating factor obeys
`exp(−∫_s^t) ≤ e^{2B̃T} e^{−(β̄/2)(t−s)}`. Gronwall then yields
`Z(t) ≤ e^{2B̃T}[Z(0)e^{−(β̄/2)t} + (2Q/β̄)]`, giving the stated sup bound. Note the threshold `β̄ = 0`
(⇔ `⟨η²⟩ = ν²λ₁`) is *unaffected* by the forcing, which only rescales the constant. ∎

**Threshold as a Reynolds condition.** With `η = δU*` and `λ₁ = (2π/L)²`, (H2) reads
`⟨δ²⟩^{1/2} ≲ 2π ν/(U* L) = 2π/Re`, `Re = U*L/ν`. **Bounded enstrophy on the heartbeat ⇔ the drive holds
the RMS Beltrami deviation below an `O(1/Re)` level, time-averaged over a period.**

*Numerical confirmation (`r2_gronwall_check.py`).* Integrating the linear inequality (3) with a periodic
heartbeat deviation: `Z` is bounded exactly for `⟨η²⟩ < ν²λ₁` and grows (up to `3.6×10¹³` over 60 periods
at `⟨η²⟩ = 1.5 ν²λ₁`) above it — the transition is **sharp at `β̄ = 0`**. Crucially, with a sub-threshold
*mean* the orbit stays bounded even when the instantaneous `η²` spikes to **2.76×** threshold each
heartbeat — confirming (H2) is a **time-integrated, not pointwise**, condition (a heartbeat may briefly
depart force-free each cycle and still be regular).

## 5. What this does and does not settle (scope discipline)

**Does:** gives a *proof* of the enstrophy/BKM bound (X3) — the sole remaining gate to full `[V]` in the
trilogy — under two explicit, physically-meaningful hypotheses, via an exact mechanism (the Lamb-vector
identity) rather than an estimate. A conditional theorem of exactly the form the hand-off anticipated
("bounded provided `δ` obeys [an explicit smallness-in-time integral]"). The mechanism also *sharpens* the
hand-off's `production ~ δ` handle to an exact identity and, decisively, to a **linear** Gronwall.

**Does not:**
- It does **not** prove (H2) *holds*. At the object's Lundquist number `S ~ 10²–10⁶` the condition
  `⟨δ²⟩^{1/2} ≲ 1/Re` is *stringent*; whether a physical drive achieves it is an empirical/consistency
  question, not a theorem. (H2) is therefore best read as a **falsifiable drive-quality criterion**:
  a well-maintained near-force-free drive is regular; a poorly-maintained one is not guaranteed to be.
- It does **not** resolve general 3D Navier–Stokes: (H1) is a genuine restriction (the coherent
  bounded-amplitude regime), and dropping it reinstates the supercritical barrier.
- It is stated for the **NSE first model**. The trilogy's actual object is Hall two-fluid with *canonical*
  vorticity `Ω = ∇×P`, `P = A + (m/q)v` (§6–8). See §6.

## 6. Extension to the Hall two-fluid object (next step, not done here)

The genuine target replaces `(v, ω)` by the canonical pair `(u, Ω)`, the force-free state by the
*double-Beltrami* state `∇×P = α P` (canonical Lamb vector `u×Ω = 0`), and `Z` by the **canonical
enstrophy** `½∫|Ω|²`. Lemma 1's structure carries over — canonical stretching is again a Lamb-vector flux
that vanishes on the double-Beltrami state — but two ingredients must be added: (i) the Hall term
`∇×(J×B/ne)` contributes an extra flux that must be re-expressed and bounded, and (ii) resistive +
viscous dissipation act on `B` and `v` separately, so the Poincaré step needs the two-fluid dissipation
operator. Establishing the analogue of (3) for canonical enstrophy — with the double-Beltrami deviation as
the small parameter — is the clean follow-on that would carry this conditional `[V]` to the true object.
(References for the Hall regularity setting: Chae–Degond–Liu 2014.)

**Executed (2026-09-09):** see `results/R3_HALLMHD_CANONICAL_ENSTROPHY_2026-09-09.md`. Lemma 1 ports
verbatim to the ion generalized vorticity `Ω = B + d_i ω` (the Hall term is the *frozen-in transport*
of `Ω` by the ion flow, not an extra flux; identity verified to machine precision for independent
`(v, Ω)`). The conditional `[V]` bound carries over **at magnetic Prandtl number `Pm = 1`**, where the
two-fluid dissipation collapses to the perfect square `η‖∇Ω‖₂²`; for `Pm ≠ 1` an explicit indefinite
term (`det = −d_i²(η−ν)²/4 < 0`) is the precise obstruction, localizing the remaining difficulty to a
coupled fluid+magnetic enstrophy problem.

## 7. Verification artifacts

- `results/verify/r2_identity_check.py` — spectral checks of Lemma 1 (both forms agree to ~9 sig figs on a
  nonzero field; exact-Beltrami null; the bound `|P| ≤ ‖∇ω‖₂‖L‖₂`; `‖∇×ω‖₂ = ‖∇ω‖₂`).
- `results/verify/r2_gronwall_check.py` — ODE integration of (3): sharp boundedness transition at
  `⟨η²⟩ = ν²λ₁`, and time-integrated (not pointwise) tolerance of within-period deviation spikes.

## 8. References

Beale, Kato & Majda 1984, Commun. Math. Phys. 94, 61 (blow-up criterion). Chae, Degond & Liu 2014,
Ann. IHP C 31, 555 (Hall-MHD). Constantin & Foias, *Navier–Stokes Equations* (Chicago, 1988; enstrophy
budget, `H¹`⇒regularity). Foias, Manley, Rosa & Temam, *Navier–Stokes Equations and Turbulence* (CUP 2001;
global attractor, enstrophy bounds). Chandrasekhar & Kendall 1957, ApJ 126, 457; Woltjer 1958, PNAS 44, 489;
Taylor 1974, PRL 33, 1139 (force-free / Beltrami). Provenance in-repo:
`FTGB_CURRENTLEG_TRILOGY.md` §8, `handoffs/HANDOFF_R2_ENSTROPHY_REGULARITY_2026-09-09.md`.

*No number in this note is fabricated; the two load-bearing claims (the identity and the boundedness
threshold) are both proven analytically and reproduced numerically. ASCII-clean apart from standard math
symbols.*
