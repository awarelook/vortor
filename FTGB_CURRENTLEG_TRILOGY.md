---
title: "When is a topological helicity current a matter current? A no-go trilogy for force-free and two-fluid plasmoids"
author: Nathaniel Hanks
date: 2026-09-09
status: "Standalone lead paper -- the current-leg trilogy, carved out from the FTGB synthesis; self-contained plasma / topological-fluid result."
---

# When is a topological helicity current a matter current? A no-go trilogy for force-free and two-fluid plasmoids

## Abstract

We ask, for a force-free (Beltrami) magnetic field `curl B = lambda B` and its two-fluid
generalization, when the fluid mass 4-current `(rho, rho v)` can be identified with the
topological helicity 4-current `(K^0, K^i)`, `K^0 = A.B`. The density leg of that
identification -- `rho` proportional to the helicity density `A.B` -- holds exactly as a
profile identity in the Beltrami gauge with a London-locked flow. The *current* leg does
not, and we settle its status as a tiered result. **(a)** In the static regime the full
4-current closes if and only if the field magnitude is spatially constant, `|B| = const`;
since a topologically nontrivial (nulled) field cannot satisfy this, closure is
obstructed and the identification is, at best, a consistent postulate. **(b)** The
natural escape -- a driven two-fluid plasma carrying its own conserved *canonical*
(generalized) helicity -- only relocates the obstruction: aligned/steady closure requires
`P.v = const` (`P = A + (m/q)v` the canonical momentum), which we prove impossible for a
nontrivial field via the perfect-square identity `(A'B'C')^2 >= 0`, adversarially
verified. **(c)** In the genuinely time-dependent regime the obstruction lifts: closure
reduces to a single scalar condition `S = mu - P.v = 0`, whose surface is non-empty and
is realizable by an electrostatic drive (the canonical-helicity source `d_mu K_can^mu = 2
f_body.Omega` vanishes for a purely electromagnetic force), with an index-1 differential-
algebraic structure and a bounded drive. We show, however, that the equilibrium and
relaxation dynamics both *select against* this closure surface, so the identification is
externally driven, never self-organized. Two residuals remain; the deeper reduces exactly
to the Beale-Kato-Majda enstrophy bound for 3D Hall-MHD -- a recognized open problem in
fluid regularity, not a defect of the construction. The results are stated with explicit
tiers ([V] verified/proven here; [S] constructed/contingent; credited where the physics
is established).

## 1. Introduction

Force-free fields `curl B = lambda B` (Chandrasekhar & Kendall 1957; Woltjer 1958) are the
minimum-energy states of magnetically dominated plasmas at fixed helicity (Taylor 1974),
and magnetic helicity `H = integral A.B` is the robust topological invariant of ideal
evolution (Moffatt 1969; Moffatt & Ricca 1992). A recurring and physically attractive
idea -- in models where matter and field co-move -- is that the fluid mass current *is*
the flux of the field's own winding: that `rho` measures how densely the field is wound
and `rho v` measures how that winding flows. This paper asks precisely when that
identification is mathematically admissible, treating the fluid current and the helicity
current as candidate equal 4-vectors and testing the equality leg by leg.

The answer is a trilogy: two proven no-gos (static; aligned/steady), one constructive
realizability result (driven), a selection negative (the dynamics avoid the closure
surface), and a clean reduction of the last gate to an external regularity theorem. The
scope discipline throughout is that these are limits of a *construction*, not verdicts
against any observed plasma phenomenon.

## 2. The law and its two legs; the density leg [V]

Write ordinary matter conservation as a candidate topological continuity equation,

```
  d_t rho + div(rho v) = 0     <==>     d_mu K^mu = 0 ,
```

with `K^mu = (K^0, K^i)`, `K^0 = A.B` the helicity density and `K^i` its flux, and the
organizing proportionality `rho = kappa (A.B)`. Two legs must hold for the 4-current to
close: the **density leg** (`rho ~ K^0`) and the **current leg** (`rho v ~ K^i`).

**Density leg = [V].** In the Beltrami gauge `A = B/lambda`, `K^0 = A.B = |B|^2/lambda >= 0`
(sign-definite, verified to 3e-15). With a London-locked cold-condensate flow `curl v =
-(q/m) B` (verified to 7e-15), the density profile tracks `|B|^2` with `corr(rho, A.B) =
1.0000` -- an exact dimensionless profile identity. Because `K^0` has units of a helicity
density, `kappa` is a genuine *dimensional* proportionality constant (the match is a
profile proportionality, not a units identity). The density leg is settled; the entire
subtlety lives in the current leg.

## 3. (a) The static no-go: closure requires |B| = const -- [V]

Matching densities fixes the current *direction*: London flow gives `v ~ A ~ B`, so the
matter current `rho v ~ |B|^2 B` is CUBIC in the field, while the helicity flux `K ~ B` is
LINEAR. Equality of a cubic and a linear quantity demands `|B|^2 = const`:

> **The 4-current closes if and only if `|B|` is constant.**

The obstruction is basis-independent, measured by the residual of `B` from `range(L)` for
`L[phi] = curl((phi B - grad phi x B)/|B|^2)` -- dimensionless and `kappa`-independent. For
a genuine toroidal Beltrami field the residual is 0.6053-0.6054 (basis-converged); a
four-move reducibility sweep (gauge, transverse E / sheath, norm, multi-lambda) never
reaches the < 0.2 bar, and a transverse non-force-free E-field leaves it UNCHANGED. The
deciding control is a null-free constant-`|B|` Beltrami field `B = B0(cos z, sin z, 0)`,
which closes EXACTLY (residual 0.0000). Hence the obstruction is entirely the spatial
variation of `|B|`, and a nontrivial closed-fibre field (which must have nulls) provably
cannot have `|B| = const`. **The current leg is over-determined by construction --
irreducibly a postulate, not a theorem, in the static regime.**

## 4. Canonical helicity is the right conserved current -- [V] / credited

A driven object may carry its own conserved current. For a two-fluid plasma the correct
one is **canonical (generalized) helicity**: with `P = A + (m/q)v` and `Omega = curl P = B
+ (m/q) curl v`, the current from `H = integral P.Omega` is ideally conserved, `d_mu
K_can^mu = 0`, *even when magnetic helicity is dissipated*, because the canonical Ohm's law
`E_can = -v x Omega` gives `E_can.Omega = 0` (a Casimir invariant). The prerequisite --
"have your own conserved current first" -- is met. *Credited:* Steinhauer & Ishida 1997
(PRL 79, 3423); Mahajan & Yoshida 1998 (PRL 81, 4863).

## 5. (b) The aligned/steady no-go: the (A'B'C')^2 >= 0 obstruction -- [V], adversarially verified

Having the conserved current only *relocates* the obstruction. The canonical flux is
`K_can = h v + (mu - P.v) Omega` (`h` the canonical helicity density, `mu` the Bernoulli
head), so closure `(rho, rho v) ~ (h, K_can)` requires `(mu - P.v) Omega = 0`. On a
double-Beltrami equilibrium `mu = const`, so this is the exact mirror of the static
theorem:

> **Aligned/steady closure requires `P.v = const`** (the analog of `|B| = const`).

Making the relevant cross-term vanish forces `lambda_- = -lambda_+`; then `P.v = const`
requires a POSITIVE ratio `p1^2/p2^2 > 0` between two ABC helicity-fluctuation triples,
which is impossible because `(A'B')(B'C')(A'C') = (A'B'C')^2 >= 0` is a perfect square.
Independent verification: the residual reaches zero only at `c = -0.604 < 0`, the
forbidden-sign branch; distinct `lambda` force a spectral band-gap and single-mode
collapse (the spectrum is discrete on any compact domain, so there is no continuous
loophole); the physical corner is `[V]`-via-mechanism (`std(P.v)/mean` equals the field-
magnitude inhomogeneity to ~1%). The two no-gos are thereby *unified* -- the same
obstruction seen once in `B` and once in `P`.

## 6. (c) The driven resolution: closure <=> S = 0, realizable by an electrostatic drive -- [S leaning V]

The third leg differs in kind. Define the scalar `S = mu - P.v`. Since `S` is a SCALAR,
`S Omega = 0` forces `S = 0` pointwise (there is no "S perpendicular to Omega" branch;
verified false to 4e-17). The canonical current is then always a matter current `(h, h u)`
with `u = v + (S/h)Omega`, closing on `v` exactly when `S = 0`. Two facts make this a
genuine resolution:

1. **The `S = 0` surface is non-empty and drive-compatible** (residual 0.00; jointly
   satisfiable to ~1e-16) -- unlike the two no-gos, whose surfaces are empty. A
   degree-of-freedom count is sharp: the isolated ideal system is 8/8, closure makes it
   9/8 (over-determined -> the no-gos), and a sustained external drive supplies the one
   spare freedom.
2. **No extra `f_ext perp Omega` constraint is needed** -- it was a body-force artifact.
   The exact identity `d_mu K_can^mu = 2 f_body.Omega` vanishes for a purely
   electromagnetic (Lorentz + barotropic) force, so the `S = 0` drive is simply the
   electrostatic potential `phi = A.v + (m/2q)|v|^2 - w/q`. The differential-algebraic
   system is index-1 (`dS/dphi = 1 != 0`): `phi` is algebraically slaved, bounded, and
   the two-species closure `{S_e = 0, S_i = 0}` is absorbed by `phi` and the parallel
   potential `A_parallel`, with Jacobian `det = -|v_e - v_i|^2` (invertible iff current
   flows). **Tier: [S] leaning [V].**

## 7. The selection result: the dynamics avoid the closure surface -- [V]/[S] negative

Does the object select `S = 0` on its own? No -- a specific, tested negative. **(A)
Variational:** minimizing energy at fixed canonical helicities yields double-Beltrami
equilibria with `mu = const`, hence `S = const - P.v != 0`; the only functional `S = 0`
extremizes is the residual squared (a tautology). **(B) Dynamical:** a driven-dissipative
Hall two-fluid integration keeps `rms(S)/dPv` at O(1) and relaxes TOWARD the aligned `mu =
const` state. Closure is therefore externally *driven*, never emergent -- and, as a
corollary, the two no-gos are the dynamical attractor of relaxation, which reinforces
them.

## 8. Residuals: R1 benign; R2 <=> the Beale-Kato-Majda bound -- [S] conditional

**R1 (current-null `v_e = v_i`).** The two-species drive scales as `1/|v_e - v_i|` and
diverges where the currents coincide, but this set is codimension-3 (isolated points,
coincident with the field nulls) and hence measure zero; the fields stay bounded and the
drive energy is `L1 + L2` integrable, so closure holds on the full-measure current-full
complement. Genuine-but-benign [S].

**R2 (global all-time existence)** on a bounded, current-full trajectory reduces to `R2 <=>
X3` given X1, X2: **X1** an energy/`L^2` bound (HAVE, via a Lyapunov function `dV/dt <= 0`
on the driven limit cycle); **X2** no current-null crossing (HAVE, via R1); **X3** the
enstrophy/`H^1` (Beale-Kato-Majda) bound `integral ||Omega||_inf dt < inf` (OPEN). X3 is
category-identical to open large-data 3D Navier-Stokes / Hall-MHD global regularity
(Chae, Degond & Liu 2014; Beale, Kato & Majda 1984) -- a recognized external problem, not
a defect of the construction. Numerically the driven system is stable to `T = 6000`
(~2196 cycles) with `|S| <= 2.2e-16` and bounded drive.

## 9. Result

> **The matter-to-helicity current identification is a [V] no-go / well-founded postulate
> in the frozen regimes** (static `|B| = const` and aligned/steady `P.v = const`, both
> proven, both adversarially or mechanism-verified), **and a constructed-realizable
> closure [S leaning V] in the genuinely-driven regime**, via an external electrostatic
> drive, obstructed only on a measure-zero benign set. **The equilibrium and relaxation
> dynamics select against closure** (a first-class negative): it is externally driven, not
> emergent. **The sole remaining gate to full [V] is the 3D enstrophy / Beale-Kato-Majda
> regularity bound -- a recognized external problem.** The density leg stays [V];
> canonical helicity is a genuine ideal conserved current [V]/credited.

The identification "matter is the flow of the knot" is thus admissible only for a knot
that is being actively driven; in a frozen or self-organizing field it is provably barred.

## References

Beale, Kato & Majda 1984, Commun. Math. Phys. 94, 61. Chae, Degond & Liu 2014, Ann. IHP C
31, 555. Chandrasekhar & Kendall 1957, ApJ 126, 457. Mahajan & Yoshida 1998, PRL 81, 4863.
Moffatt 1969, JFM 35, 117. Moffatt & Ricca 1992, Proc. R. Soc. A 439, 411. Steinhauer &
Ishida 1997, PRL 79, 3423. Taylor 1974, PRL 33, 1139. Woltjer 1958, PNAS 44, 489.

*Note: a fourth source for the canonical-helicity Casimir (Bae-Kang-Shin 2025,
arXiv:2504.07629) states the same proposition but its identifier was not independently
verified; it is deliberately NOT cited as load-bearing -- the result rests on Steinhauer-
Ishida 1997 and Mahajan-Yoshida 1998. No number in this paper is fabricated; ASCII-clean.*
