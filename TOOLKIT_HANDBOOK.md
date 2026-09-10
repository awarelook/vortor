---
title: "The FTGB Methods Toolkit: A Consolidated Handbook (Modules M7-M14)"
author: Nathaniel Hanks
date: 2026-09-09
status: "Consolidated reference handbook. Assembled from the eight canonical method modules TOOLKIT_ADV_07..14, resting on the shared foundation MATH_TOOLKIT_BASE.md; those modules remain the source of record. This is a clean, shareable single-file reference; no new claims are introduced here."
anchors: "Four measured anchors {B, n_i, m_i, R}; zero free structural parameters."
---

# The FTGB Methods Toolkit: A Consolidated Handbook (Modules M7-M14)

**Nathaniel Hanks -- 2026-09-09**

---

## 1. Introduction

This handbook consolidates the eight *method modules* of the Fractal-Toroidal-Beat (FTGB) program
into a single, tiered, citable reference. The toolkit is not the theory; it is the reusable
**analysis machinery** the theory is built with -- the dimensional bookkeeping, the conserved-current
constructions, the no-go templates, the synthesis mappings, and the anti-numerology controls that
one applies to a driven toroidal-Beltrami plasmoid, or more generally to any driven-dissipative
coupled-oscillator system on a helical, elastic, topologically-constrained substrate.

The object the toolkit serves is one driven, force-free Beltrami-Hopf standing wave -- a
Chandrasekhar-Kendall (CK) mode satisfying `curl B = lambda B`, read simultaneously as a plasma
configuration and as a Madelung / quantum-hydrodynamic matter wave, resting on four measured anchors
`{B, n_i, m_i, R}` with zero free structural parameters. But each method below is written to be
lifted out and re-applied to a fresh problem without re-deriving it. That is the point of a toolkit.

The eight modules are:

| Module | Subject | What it gives you |
|---|---|---|
| **M7** | Buckingham-Pi as claim-audit | which knobs a claim is *allowed* to depend on -> what a falsifier must vary |
| **M8** | QWM (Reed) math conversion + dimensional audit | a units referee for mass / charge / helicity readings, with the fake charge dimension dissolved |
| **M9** | Coupled-oscillator substrate | where FTGB *is* (vs merely *shares*) established cross-domain mathematics |
| **M10** | Topological-soliton + conserved-current methods | conserved currents, no-go templates, moduli-geodesic amplitudes, seesaw / RG readings |
| **M11** | EGM / polarizable-vacuum spectral methods | Storti's PV-refractive-index + ZPF harmonic-beat *representation* mapped onto M7/M9, with its numerology quarantined (method-only, no claim adopted) |
| **M12** | Ginzburg spiral-field theory (toryx / helyx) | a toroidal-spiral *structural analogy* (matter = self-inverting torus, radiation = double helix, discrete matter<->radiation ladder) mapped onto the Beltrami-Hopf object; analogy-only, no claim adopted |
| **M13** | Nielsen TUFT mass-tower & mixing methods | the ζ-valued exponent tower (`C₅=ζ(3)/12`, `β₅=ζ(5)/8π⁴`, …), knot/lens-space torsion, CKM/PMNS overlaps, Chern-Simons `M=ke²/4π`, Proca-Beltrami `λ=mc/ℏ` — coefficients `[V]`-checked, **π-power anomaly + preprint blind-fit flagged** |
| **M14** | Greenyer beat-law & EVO cascade methods | the Beat Law + shape-independent ladder `N^L`, the triad dichotomy (integer silence / golden resonance), two Manley-Rowe (Fibonacci) invariants, anapole `N⁴`, `9/8 μ_B`; nuclear layer a **pre-registered target** (`N_crit` prediction), **no over-unity** |

All eight modules rest on **`MATH_TOOLKIT_BASE.md`** — the shared foundation carrying the mathematics they
import: the Chandrasekhar-Kendall / Beltrami curl eigenproblem (`§1`), helicity / Woltjer-Taylor relaxation
(`§4`), the **one operator read three ways** (plasma ‖ Madelung matter-wave ‖ `K_PV` polarizable vacuum) and
the topology (`§9`), and the canonical anchors whose single source of truth is
**`foundation/30_CANONICAL_NUMBERS.md`** (`§A` anchors `{B,n_i,m_i,R}`, `§C` `c_CK`, `§I` the {121,208,294} kHz
comb). Every module header cites the base by section; those citations are load-bearing and resolve there.

Two consolidated knowledge-base files also accompany the modules: **`GLOSSARY.md`** (shared vocabulary across FTGB
and the five convergence frameworks — Reed, Storti, Nielsen, Ginzburg, Greenyer — tiered) and **`REFERENCES.md`**
(the credited literature + the framework primaries, with the do-not-cite / excision notes), plus **`LINEAGE.md`**
(the Bostick / Puthoff / Shoulders credited-lineage note).

**Provenance-citation convention.** Citations to `.md` documents *not* present in this bundle — the predecessor
toolkit (`MATH_TOOLKIT_ADVANCED`, `TOOLKIT_ADV_01`–`_06`), the distillation sources each convergence module was
folded from (`REED_QWM_*`, `KERNEL_NIELSEN_*` / `NIELSEN_TUFT_*`, `EVO_MATHEMATICAL_CORE`,
`TORUS_MATHEMATICS_APPENDIX`, `storti_egm_missing`, `excision-protocol-storti-factor`), and the `project_ftgb_*`
frame / open-problem notes — are **extended-corpus provenance**: the working notes a result was distilled from,
not in-jewel links. Every load-bearing claim they carry is re-stated and re-verified inside the jewel (the
modules + `results/verify/`). Quarantine-tooling outputs (`MANIFEST.md`, `candidates.csv`) live in
`F:\_QUARANTINE\`, not here.

Every module carries a scope limit at its head, stated before any result is used. Nothing here is
fabricated; every quoted number traces to a named reproducible script in its source module. No
over-unity, nuclear rate, cross-section, branching magnitude, mass, or scale is invented in this
document.

---

## 2. Tier and citation discipline (read before using any result)

This handbook uses **one clean tier convention** throughout. It deliberately does **not** use a bare
`[A]` for "established," because that symbol collided in review with the older "analytic / asserted"
sense. Established physics is always written `[credited]`.

**Core tiers**

- **[V]** -- computed / verified here by a named computation, a checked identity, or a dimensional
  reduction.
- **[credited]** -- established, peer-reviewed or textbook physics/mathematics we build on.
- **[S]** -- structural / contingent: cited-convergence or model-asserted reading, not closed on our
  side (includes what earlier notes called "analytic/model-asserted" readings).
- **open** -- a named external problem, not an internal crack.

**Compound and special-purpose labels** (each a refinement of the core tiers, used where it carries
real information)

- **[V-dim]** -- dimensionally verified (units close); the value is not derived.
- **[S-mechanism]** -- the mechanism is well-posed (a category gap is dissolved); the value is not
  forced.
- **[QWM framework]** -- a Reed / quantum-wave-mechanics ontological reading, used as a
  method/notation choice, attributed to Reed, **not** endorsed as established.
- **[IDENTITY] / [ANALOG] / [VOCAB/CAUTION]** -- the three synthesis tiers of M9 (same mathematics /
  shared mathematics on a different substrate / shared words or an imported caution only).
- **[flagged]** -- a coincidence held but not promoted (e.g. `~137`), gated at 0.5% against
  `phi^n` / `137^n`.
- **[unassessed external]** -- named and excluded (e.g. the QWM gravity chapters); read critically,
  do not cite as established.
- **[reject]** -- fabricated or refuted, named so it is never resurrected (e.g. `E_fm = 2.5 MeV`).

**Two standing citation notes**

1. **Bae-Kang-Shin, arXiv:2504.07629** ("On the double Beltrami states in Hall MHD"; Bae, Kang &
   Shin, 2025) is carried in M10-1 as a **VERIFIED real, on-topic** reference (confirm exact Prop.
   label at lock). It is **never presented as the sole support**. The
   canonical / generalized-helicity Casimir claim rests primarily on the two firmly-verified references
   **Steinhauer-Ishida 1997, PRL 79, 3423** and **Mahajan-Yoshida 1998, PRL 81, 4863** -- named as the
   load-bearing pair. Bae-Kang-Shin is a corroborating modern statement, not the foundation.
2. **TUFT (Nielsen) and QWM (Reed)** are tiered material: the Nielsen "toroidal unified field theory"
   is a preprint, and quantum-wave-mechanics ontology is `[QWM framework]`. Neither is presented as
   established. Load-bearing claims in the toolkit map to credited, peer-reviewed physics.

Notation is ASCII throughout: `Pi` = Buckingham dimensionless group, `N_Pi` = number of groups,
`->` maps to / reduces to, `!=` not equal, `<=` / `>=` inequalities, `.` a dot product, `x` a cross
product where context is clear.

---

## 3. Module M7 -- Buckingham-Pi as claim-audit and dimensionless-scaling map

> **Scope limit (stated first).** Buckingham's theorem gives the **allowed scaling only** -- the set
> of dimensionless groups a physical law *may* depend on. It does **not** give (i) which variables are
> relevant, (ii) the mechanism, (iii) the function relating the groups, (iv) the O(1) constant in
> front, (v) stability, or (vi) permission to extrapolate across a regime transition. A "clean
> four-anchor law" is a **scaling skeleton**, not a theory. Use Pi as a *claim-audit* tool -- it tells
> you exactly which knobs a claim is allowed to depend on, and therefore what a falsifier must vary --
> never as a theory generator.

### M7-1 -- The theorem, stated for the program   [credited] + [V]

**Statement.** Take `n` dimensional quantities `q_1..q_n` entering a relation `F(q_1..q_n) = 0`. Write
each `q_j` as a column of exponents over a chosen set of base dimensions (SI: `M` mass, `L` length,
`T` time, `I` current, `Theta` temperature, `N` amount) and stack them into the **dimensional matrix**
`D` (rows = base dims, columns = variables). Let `r = rank(D)`. Then the relation is equivalent to
`Phi(Pi_1 .. Pi_{N_Pi}) = 0` in

```
N_Pi = n - r          independent dimensionless groups.
```

**Key equations / the null-space construction.** A dimensionless monomial `Pi = prod_j q_j^{a_j}` has
zero net dimension iff its exponent vector `a` satisfies `D a = 0`. So the Pi-groups are exactly a
basis of the null space `ker D`, and there are `n - r` of them by rank-nullity
(`dim ker D = n - rank D`). Computing them is exact linear algebra (rational arithmetic).

**Two load-bearing subtleties.**
- **rank != symbol count.** `r` is the rank of `D`, not the number of distinct unit symbols that
  appear. Variable sets can lock two base dims together, dropping the rank and *raising* `N_Pi`. The
  metasurface matrix (M7-4) is the worked instance: only circuit/EM quantities appear, the current
  dimension satisfies `I = -2M` identically (a left-null vector of `D`), so four symbols `M,L,T,I`
  appear but `r = 3` and `N_Pi = 5`. Always compute `rank(D)`; never count symbols.
- **base-dimension invariance.** The theorem is invariant under any invertible change of base
  dimensions. SI-with-current-`I`, a reduced constant set, or the QWM charge-as-angular-momentum base
  all give the **same `N_Pi` and the same Pi-groups** -- only intermediate exponent labels differ.
  **[V] invariance check:** the force-free matrix rebuilt in an `(M,L,T,Q)` charge base (via the
  invertible map `I <-> Q/T`) gives `rank = 4` identically, and both groups stay dimensionless.

**Validity / tier.** Theorem **[credited]** (Buckingham 1914); rank/null-space computation and the
invariance check **[V]**.

**How to reuse.** Given a claim, (1) list every variable you think enters; (2) build `D`; (3) compute
`rank(D)` and `ker D` exactly; (4) read `N_Pi = n - r` as the number of independent knobs the claim is
*allowed* to depend on. Omitting a relevant variable is garbage-in -- the honest gap analysis (M7-3)
tells you what you dropped.

**Source.** TOOLKIT_ADV_07 sec M7-1. `frontier_calcs/toolkit_adv07_buckingham_pi.py`.

### M7-2 -- The force-free-object matrix, and why 4.4934 is NOT universal   [V] + [V/S]

Variables `{B, n_i, m_i, R, mu0, omega}` (the four canonical anchors plus `mu0` and the target
frequency). Computed:

```
          B    n_i   m_i    R    mu0  omega
   M  [   1     0     1     0     1     0 ]
   L  [   0    -3     0     1     1     0 ]
   T  [  -2     0     0     0    -2    -1 ]
   I  [  -1     0     0     0    -2     0 ]      (Theta, N rows zero)

   n = 6,  rank r = 4,  N_Pi = n - r = 2.
```

A physically transparent complete basis (verified rank-2):

| Group | Definition | Physical role |
|---|---|---|
| `Pi_A = omega R / v_A` | `omega R sqrt(mu0 n_i m_i) / B` | Alfven-Mach: dimensionless drive frequency |
| `Pi_N = n_i R^3` | `n_i R^3` | number of ions in the object volume (geometric) |

**Derived natural scales.** The only velocity buildable from `{B, n_i, m_i, mu0}` is the Alfven speed
`v_A = B / sqrt(mu0 n_i m_i)`; the only frequency is the transit rate `f_A = v_A / (2 pi R)`. Every
frequency the object can have is therefore `f = Lambda * f_A` for a dimensionless `Lambda` -- this is
all Pi theory delivers.

**The modal eigenvalue Lambda_n.** The carrier law `f_n = Lambda_n * v_A / (2 pi R)` gives
`Lambda_n = 2 pi f_n R / v_A = (omega R / v_A)|_n` -- i.e. `Lambda_n` is the value the Alfven-Mach
group takes at resonance `n`. Pi theory says `f_n ~ v_A / R`; it says **nothing** about the number
`Lambda_n`. That number is an **eigenvalue fixed by geometry + boundary condition**, not by the
theorem.

**[V] `Lambda_1 = 4.493409`** is the first nonzero root of `tan x = x` -- the Chandrasekhar-Kendall /
Beltrami eigenvalue of the **BALL** (`curl B = lambda B`, PEC sphere). The first six roots
`4.493409, 7.725252, 10.904122, 14.066194, 17.220755, 20.371303` give the **inharmonic** ratios
`1, 1.719, 2.427, 3.130, 3.832, 4.534`. With canonical anchors `v_A = 2.033e4 m/s`, `R = 0.12 m` this
is the carrier comb `f_n = 121.2, 208.3, 294.0, 379.3, 464.3, 549.3 kHz`.

**Corrective, stated plainly [V/S].** `Lambda_1 = 4.4934` is the eigenvalue of the **ball/sphere**
boundary problem **only** -- it is **NOT a universal constant.** For the actual toroidal/conical FTGB
object the eigenvalue becomes a *function of the object's own Pi-groups*,
`Lambda_n = Lambda_n(r_minor/R_major, d_i/R, beta, S, ...)`. Quoting `4.4934` for the torus is a
sphere-geometry approximation; the true value is set by the aspect ratio and the two-fluid/loss groups
of M7-3. (Consistent with the project's own FreeFEM torus eigensolve, which finds a carrier *split*
`d(lambda) = 0.2806` at `eps = 0.697` rather than a single sphere value.)

**Validity / tier.** Matrix/rank/null-space and the `tan x = x` root **[V]**; `v_A`/Alfven and CK
identifications **[credited]** (Alfven 1942; Chandrasekhar-Kendall 1957); the "geometry-dependent, not
universal" corrective **[V/S]**.

**How to reuse.** When a "clean" scaling law hands you an O(1) constant, ask which boundary-value
problem set it, then treat that constant as a *function* of the geometry's own dimensionless groups,
not a transferable number.

**Source.** TOOLKIT_ADV_07 sec M7-2. Reproduces `30_CANONICAL_NUMBERS.md` sec I comb.

### M7-3 -- The plasma-resonator matrix and the control-parameter map   [V] + [credited]

Variables `{omega, B, n_e, R, m_i, T_e, e, eps0, mu0}` (`T_e` carried as thermal energy `k_B T_e`).
Computed: `n = 9, rank r = 4, N_Pi = 5`. The five groups map onto the mechanism-level control
parameters (verified complete basis):

| Group | Definition | Physical role |
|---|---|---|
| `beta` | `2 mu0 n_e k_B T_e / B^2` | plasma pressure / magnetic pressure |
| `omega/omega_ci` | `omega m_i / (e B)` | drive vs ion-cyclotron -> Hall / FLR / sideband onset |
| `d_i/R` | `sqrt(m_i/(mu0 n_e e^2)) / R` | ion skin depth / size -> two-fluid onset |
| `lambda_D/R` | `sqrt(eps0 k_B T_e/(n_e e^2)) / R` | Debye length / size -> quasineutrality |
| `n_e R^3` | `n_e R^3` | ions in the volume (geometric) |

**[V] key derived relation.** The Alfvenic drive group is **not** independent:
`omega R / v_A = (omega/omega_ci) * (R/d_i)`, because `v_A = omega_ci * d_i` exactly. The carrier is a
*product* of two basis groups, not a sixth degree of freedom -- a genuine, computed constraint on the
claim structure.

**Honest gaps (what these 9 variables cannot build).** `d_e/R` needs the electron mass `m_e` (adds the
pure ratio `m_e/m_i`); the collisional groups `nu_e/omega` and the **Lundquist number `S`** need a
collision frequency or resistivity; the Hall wavenumber group `k d_i` needs a wavenumber `k`. Note
`c = 1/sqrt(eps0 mu0)` is derived from the set and adds no new group. A model omitting `nu_e, eta, m_e`
is silently assuming they are irrelevant.

**Validity / tier.** Matrix/rank/null-space and the `v_A = omega_ci d_i` identity **[V]**; the named
plasma groups **[credited]**.

**How to reuse.** Use this as the checklist for "what did the four-anchor law drop?" -- the corrections
to `Lambda` live in exactly these plasma/loss groups.

**Source.** TOOLKIT_ADV_07 sec M7-3. (A fourth matrix, the metasurface/Huygens case `n=8, r=3, N_Pi=5`,
is the worked `rank != symbol count` demonstration and supplies the Kerker group `p/(eps0 Z0 m)`;
see TOOLKIT_ADV_07 sec M7-4.)

### M7-4 -- The claim-audit + falsifier table (the key deliverable)   [V]-structure / [S]-claims

For each FTGB claim: the relevant Pi-groups, which were held fixed, which were assumed small/large, and
the **direct experimental falsifier**. This is the program turned into a falsifiable scaling map. The
*groups* are [V]; whether each claim's assumed limit holds in the object is [S]/open.

| Claim | Relevant Pi-groups | Assumed small/large | Direct falsifier |
|---|---|---|---|
| CK/Alfven carrier `f_n = Lambda_n v_A/2piR` | `omegaR/v_A`, aspect, BC | -- | measure `f_1`; if `f_1 != Lambda_1 v_A/2piR` at the measured `v_A`, or the comb is harmonic (not `1:1.72:2.43`), the CK reading fails |
| single-fluid vs Hall | `k d_i`, `omega/omega_ci`, `nu/omega` | `k d_i << 1`, `omega/omega_ci << 1` | Hall/cyclotron sidebands at `omega_ci`, or spectrum scaling with `k d_i`, falsify single-fluid MHD |
| single-Beltrami-scale | `k d_i`, `k d_e` | `k d_i << 1` or `k d_e << 1` | if two-fluid skin terms shift `Lambda` with `d_i/R`, the single-scale closure breaks |
| Huygens reflection suppression | `a/lambda`, `Z_s/Z0`, `p/(eps0 Z0 m)` | `a/lambda << 1` | no `S11` minimum at the predicted `Pi_LC = 1`, or minimum absent when `p/(eps0 Z0 m) != 1`, falsifies Kerker balance |
| dark resonator | multipole-cancellation groups | radiative multipoles cancel | radiated power / Q far from the anapole floor `<~ (kR)^5` falsifies the dark-mode claim |
| plasma loading | `omega/omega_pe`, `nu/omega`, `lambda_D/R` | `lambda_D/R << 1`, `nu/omega << 1` | resonance shift vs measured `n_e` off the `omega_pe(n_e)` scaling falsifies the loading model |
| proposed beat | `d(omega)/omega`, aspect `eps`, drive | `d(omega)/omega << 1` | beat must scale linearly in aspect (`d(lambda) ~ eps`, `f_b/f_c ~ 7%`); different scaling falsifies the doublet-splitting origin |

**Headline falsifiers.** (1) the carrier comb must be **inharmonic `1:1.72:2.43`** (a harmonic comb
kills the CK ball-mode reading); (2) **cyclotron/Hall sidebands** at `omega_ci` would force the
two-fluid `d_i/R` correction; (3) the Huygens `S11` minimum must appear at `Pi_LC = 1` with
`p/(eps0 Z0 m) ~ 1`; (4) the beat must scale **linearly in aspect ratio** (`d(lambda) ~ eps`).

**How to reuse.** This is the template: **claim -> relevant Pi-groups -> what was held/assumed ->
which group a falsifier must vary.** Fill one row per claim; the falsifier column is the deliverable.

**Source.** TOOLKIT_ADV_07 sec M7-5.

### M7-5 -- The dimensional <-> dimensionless side-by-side format   [V/S per row]

The explanatory template for the whole program: **real-unit form | dimensionless-Pi form | named
group / tier**. Each right-hand column is a claim the experiment can test directly (an O(1) number or
a measured ratio); each dimensional prefactor (`kappa`, `mu_eff`, `c_CK`) is a constant Pi theory is
silent about -- it must come from the mechanism, a calibration, or measurement.

| FTGB relation | Real-unit form | Dimensionless-Pi form | Group / tier |
|---|---|---|---|
| density spine | `rho = kappa (A.B)` | `rho/rho0 = (A.B)/(A0.B0)` | helicity-density ratio; `kappa` a dimensional prefactor -- [S] |
| mass-whirl | `m = hbar omega_C / c^2` | `q = 1/alpha` (whirl number) | rest-frame closure; `q=1/alpha` [QWM framework] |
| force-free field | `curl B = lambda B` | `Lambda_1 = lambda_1 R = 4.4934` | [V] root, [V/S] geometry-dependent |
| carrier ladder | `f_n = Lambda_n v_A/(2piR)` | `Lambda_n = omega_n R/v_A = f_n/f_A` | [V] comb `121/208/294 kHz` |
| beat | `f_b = c_CK eps v_A/(2piR)` | `d(omega)/omega = f_b/f_c ~ 7%` | [V] (FreeFEM), linear in `eps` |
| swimmer / glide speed | `v = sqrt(2 U_s/mu_eff)` | `v/v_A = sqrt(2 U_s/(mu_eff v_A^2))` | energy-per-inertia ratio; [S] |

**Limits, restated [V].** Buckingham Pi does **not** pick the variables, identify the mechanism, derive
the function `Phi`, fix the O(1) constant (`Lambda_1 = 4.4934` comes from `tan x = x`, a boundary
problem, not from Pi), establish stability, or license extrapolation across a regime transition. The
four anchors fix the *scale* `v_A/R`; the *number* `Lambda` and its *corrections* live in the
plasma/loss groups of M7-3 and must be computed or measured, not assumed.

**Source.** TOOLKIT_ADV_07 sec M7-6, sec M7-7.

---

## 4. Module M8 -- QWM (Reed) math conversion and dimensional audit

> **Scope limit (stated first).** Quantum Wave Mechanics (Reed, *QWM* 4th ed., 2022) is a
> **framework**, not established physics. This module runs a **convert-and-check** pass: each QWM
> expression is stated, mapped to a toolkit module, written real-unit beside dimensionless,
> **dimensionally checked in two unit systems**, and tiered. We tier `[QWM framework]` for QWM's own
> ontology, `[credited]` for the standard pieces it builds on, and `[V]` only for what a named
> computation or checked identity verifies here. The QWM **gravity** chapters (Ch.33-47: Oldershaw
> discrete-scale-relativity, oscillator-sync-as-gravity, graviton = phase-conjugate photon) are
> `[unassessed external]` and are **not** converted -- named and excluded. Nothing is endorsed
> wholesale; the module converts the math that checks out and flags the rest.

### M8-1 -- The two unit systems: the SI-strict referee   [V]

The dimensional check reduces every right-hand side to base dimensions in **two** systems and asks
whether it yields mass `[M]`:

- **(A) SI-strict** -- base `{M, L, T, I}`; **angle `rad` is dimensionless**; charge = Coulomb = `I.T`.
  This is the **rigorous referee**.
- **(B) QWM (L's table)** -- base `{M, L, T, A}` with **angle `rad` = A a genuine base dimension** and
  **no current base**: charge `e ~ [kg.rad/s] = M.A.T^-1` (a spin angular momentum), `A_vec ~ L.A^-1`,
  `B ~ A^-1`, `E-field ~ L.T^-1.A^-1` (fixed so `E/B` is a velocity in both systems).

**Honest finding [V].** `E/B` reduces to velocity `L.T^-1` in both systems. The QWM angle-as-base
convention makes the load-bearing charge/helicity results transparent (`m = e/omega` and
`A.B = helicity density` both PASS), **but** it introduces spurious `A` residuals in `hbar omega`-type
relations (`m = hbar omega_C/c^2` shows a residual `2A` in the QWM base) because it double-counts a
formally-dimensionless radian in both `hbar` and `omega`. **Conclusion:** angle-as-dimension is a
useful *bookkeeping aid* for charge/helicity, **not** a rigorous replacement for SI. The SI-strict
column is the referee; the QWM column is the optional lens.

**How to reuse.** Run every dimensional check in the SI-strict base first (it is the referee). Use the
QWM angle-base only as a lens to expose where a "charge" or "helicity" quantity is secretly a
mechanical (angular-momentum) object.

**Source.** TOOLKIT_ADV_08 sec M8-0.

### M8-2 -- Mass = the Compton whirl; `m = hbar omega / c^2`   [V] + [QWM framework]

**Statement.** Mass is a confined-wave whirl frequency; the electron rest energy IS the Compton whirl:

```
m = hbar omega_C / c^2 ,    omega_C = m c^2 / hbar = c / R_C ,    omega_zbw = 2 omega_C.
```

The stationary matter wave `psi = sqrt(rho) exp(i S/hbar)`, `S = -E t`, rotates its phase at
`omega = E/hbar`; that rate divided by `c^2` is the inertial mass (de Broglie / zitterbewegung internal
clock). The radian is a dimensionless degrees-of-freedom marker that the mass identity turns into
kilograms via the dimensional carrier `omega_C`.

**Dimensional check [V].** `hbar omega_C / c^2 -> M` PASS (SI). Numeric: `omega_C = 7.7634e20 rad/s`,
`m = hbar omega_C/c^2 = 9.109384e-31 kg` (ratio to `m_e` = 1.000000), `hbar omega_C = 0.51100 MeV =
m_e c^2`.

**D1 held.** Mass `[kg]` **!=** the dimensionless whirl number `q = 1/alpha ~ 137.036`. The honest
schema is `m = f(q)` with the dimensional carrier `omega_C` supplying the units. `m = hbar omega_C/c^2`
is the dimensionally-correct identity; `q = 1/alpha` is a *separate* dimensionless quantity.

**The seven-form audit (the "check" earning its keep).** Of L's seven equivalent mass forms:
- five (`m = hbar k/v`, and L3 `m = (hbar k - qA)/(beta c)`, L5 `m = |Vq|/c^2`, L6 `m = -e E/a`,
  L7 `m = A e/v`) are standard-physics rearrangements -- Newton's second law, `E/c^2`,
  canonical-momentum -- and **PASS** the SI check. Tier **[credited]**.
- **Catch #1 (square restoration) [V]:** the ledger transcribed `m = E/(EE/B)` *without the square*.
  As written it is momentum (`M.L.T^-1`), not mass. The primary Ch.21 Table 21-1 has
  `m = E/(EE/B)^2 = 2L/(EE^2 - c^2 B^2)`, which reduces to `M`. **Restore the square.**
- **Catch #2 (L4 is a proportionality) [S]:** `m = 2L/(EE^2 - c^2 B^2)` cannot be a bare equality
  (the numerator `L` is not angular momentum for the ratio to be mass); it survives only as a
  proportionality `m ~ (field energy)/c^2` with a hidden `eps0`/volume constant -- the same D2 pattern
  as `rho = kappa(A.B)`.
- **Catch #3 (`m = e/omega` needs D4) [QWM framework]:** in SI, `e/omega = (I.T)/(T^-1) = I.T^2` -- NOT
  mass. In the QWM charge convention `e ~ [kg.rad/s]`, `e/omega = (M.A.T^-1)/(A.T^-1) = M` -- mass.
  Numeric `m = e/omega_C` returns `9.109384e-31 kg` (ratio 1.000000). This is *precisely why* D4 is
  load-bearing, not cosmetic: `m = e/omega` is only dimensionally coherent if charge carries
  spin-angular-momentum units.

**Validity / tier.** Anchor identity + arithmetic **[V]** (recovers `m_e`); de Broglie/zitterbewegung
**[credited]**; the "mass IS the whirl" ontology **[QWM framework]**.

**How to reuse.** Use `m = hbar omega/c^2` as the calibrated mass<->frequency map (it reappears in
M10-4). When auditing any mass relation, restore dropped exponents, separate bare equalities from
proportionalities-with-a-carried-constant, and check whether a "charge" term forces D4.

**Source.** TOOLKIT_ADV_08 sec M8-1.

### M8-3 -- Charge = spin angular momentum, `e ~ [kg.rad/s]`   [QWM framework] + [V]

**Statement.** Charge is read AS a rate -- a spin-precession angular momentum -- which dissolves the
fake independent `[Q]` dimension (Coulomb is merely a *count* of electrons):

```
e = m_e omega = m_e (omega_C + omega_p) = 7.0719e-10 kg.rad/s = 1.6022e-19 C   (Reed Eq.21-1/21-6)
omega_p = d(theta)/dt = e/m_e = 1.7588e11 rad/s                                (Eq.21-10)
d(theta) = 2 pi alpha = 0.04585 rad = 2.627 deg   per Compton turn             (Eq.21-2)
```

Physically, the Hopf-linked charge path does not close after one Compton revolution -- it **precesses**
by `2 pi alpha` each turn and re-synchronizes every `q = 1/alpha ~ 137.036` turns (a torsion
loop-closure defect). Charge sits on the whirl axis as a *rate*.

**Dimensional check [V].** `m = e/omega -> M` PASS in QWM units (M8-2 catch #3); `e = m_e omega_C =
7.0720e-10 kg.rad/s` (Reed 7.0719e-10, matches); `d(theta) = 2 pi alpha = 2.627 deg` (matches).

**`~137` coincidence-gate [flagged].** Reed's `q = 1/alpha` is measured `alpha` inserted by hand and
re-read as a synchronization ratio -- a definitional identity (a *mechanism*, torsion closure defect,
not a *prediction*). Distinct from `1/(20 phi^4) = 137.082` (a prediction claim, 0.034% off but with a
hand-chosen combinatorial factor and no QED running), held **[flagged]**. Neither derives `alpha` from
the object's own Beltrami-Hopf geometry.

**Validity / tier.** Charge-as-spin-angular-momentum (D4) and charge-as-torsion-defect **[QWM
framework]**; the arithmetic **[V]**; `~137` **[flagged]**; the recovered Schwinger term `a_e =
alpha/2pi` **[credited]** (recovers, does not predict).

**How to reuse.** When a "charge" appears in a dimensional relation and the SI check fails by exactly
`I.T^2`-type residuals, promote charge to `[kg.rad/s]` and re-check; the failure usually means the
relation is mechanical (angular-momentum) in disguise.

**Source.** TOOLKIT_ADV_08 sec M8-2.

### M8-4 -- Madelung / QHD and the helicity density: `K0 = A.B` is a helicity density, not `rho`   [credited] + [V]

**Statement.** The confined toroidal standing wave is the object. Madelung polar form
`psi = sqrt(rho) exp(i S/hbar)`, `rho = |psi|^2`, `v = grad S/m`; Bohm quantum potential
`Q = -(hbar^2/2m)(lap sqrt(rho))/sqrt(rho)`. Mass is an obstruction to energy flow, not a Higgs
coupling (ontology `[QWM framework]`).

**The units-table consistency check (D2) [V].** With `A_vec ~ m/rad`, `B ~ 1/rad`, the product
`A.B ~ m/rad^2` reduces (script) to exactly the tabulated **magnetic helicity density**
`L.A^-2 = m/rad^2` -- PASS, internally consistent. But matter density `rho ~ kg/m^3 = M.L^-3` is a
**different dimension**, so `rho = A.B` is dimensionally impossible. The surviving content is the
**proportionality**

```
rho = kappa (A.B) ,    kappa a fixed dimensional constant (D2).
```

Likewise winding density `m^-3` != matter density `kg/m^3` (D3). The `corr(rho, A.B) = 1.0000` result
is a dimensionless Pearson *profile* identity (shapes coincide), unaffected by the dimensional
distinction.

**Validity / tier.** Madelung/Bohm **[credited]** (Madelung 1927, de Broglie 1924, Bohm 1952); the
units-table check (`A.B` = helicity density) and the D2/D3 proportionality **[V]**; the
mass-as-obstruction ontology **[QWM framework]**.

**How to reuse.** Never write a density = helicity equality; write the profile proportionality
`rho = kappa(A.B)` and carry `kappa` as a dimensional constant. The identity is in the *shape*
(`corr = 1`), not the units.

**Source.** TOOLKIT_ADV_08 sec M8-3.

### M8-5 -- EM / topology, and the held distinction `K0 != B != Q_H`   [credited] + [V]

**Statement.** Reed Ch.3 is standard Maxwell (4-potential `A^mu = (phi/c, A)`, canonical momentum
`P = gamma m v + q A`, `B = curl A`); Ch.26 gives the winding number
`n = (1/2 pi) integral grad(phi).dr` (a dimensionless integer, the degree of the phase map). Ch.26
then *reads* electric charge as roots of unity and fractional quark charge via a hypocycloid /
Tusi-couple -- that identification is `[QWM framework]`, particle-scale.

**Held reconciliation (load-bearing) [V].** Reed's Ch.26 conflates several distinct topologies under
"topological charge." Keep the project's registry distinct:
- **K0 = A.B** -- real magnetic **helicity density** (pi_3(S^2), Moffatt/Woltjer): the object's own
  invariant, the density in the continuity/matter law.
- **baryon B** -- Skyrme **winding degree** (pi_3(S^3)),
  `B = (1/24 pi^2) integral eps^{ijk} Tr(L_i L_j L_k) d^3x`: a distinct, independently-conserved
  winding (nucleon leg).
- **Q_H** -- **Hopf linking number** (integer): the object's conserved charge, a *linking* not a
  *wind-up*.
- Reed's `n` (Eq.26-1) -- the degree of a phase map, = the project's own standing-wave mode number.

His identification of `n` with electric-charge quantization and SU(3) color is `[QWM framework]` and
must **not** be conflated with the `K0 / B / Q_H` triad.

**Excluded and gated material.** The QWM **gravity** chapters (33-47) and the Ch.36 Oldershaw
discrete-scale-relativity mass scaling `M_psi = Lambda^D M_{psi-1}` are `[unassessed external]`,
excluded (the DSR relation passes dimensionally only because `Lambda, D` are fitted -- empty of
mechanism, exactly the M7 caution). The polarizable-vacuum `K_PV` frame itself stays `[credited]` as a
weak-field-GR model; only Reed's gravity *extension* of it is walled. The `m_p/m_e = 1836.15`
placement fails the 0.5% `phi^n`/`137^n` gate -- ordering, not a law; `~137` stays `[flagged]`.

**Validity / tier.** Ch.3 Maxwell + Eq.26-1 winding **[credited]**; the roots-of-unity / hypocycloid
charge ontology **[QWM framework]**; the `K0 != B != Q_H` distinction **[V]** (held correction); the
gravity chapters and DSR scaling **[unassessed external, excluded]**; `E_fm = 2.5 MeV` **[reject]**.

**How to reuse.** Whenever a source says "topological charge," resolve *which* topology (helicity
density / Skyrme baryon degree / Hopf linking / phase-map degree) before importing any number; they
are four different invariants.

**Source.** TOOLKIT_ADV_08 sec M8-4, sec M8-5, sec M8-7.

---

## 5. Module M9 -- FTGB as one instance of nonlinear coupled oscillators on a helical, elastic, topologically-constrained substrate

> **Scope limit (stated first).** This module does **not** claim that DNA, chromatin, a cell, a
> Belousov-Zhabotinsky (BZ) reaction, or a Pd lattice **is** an FTGB object, nor that a single coherent
> resonance spans molecular-to-tissue (or plasma-to-nuclear) scales. FTGB is claimed to be **one member
> of a mathematical class** whose other members are studied in molecular biophysics, chemical dynamics,
> and solid-state physics. Shared *equations* are real and load-bearing; shared *substrate* is not
> asserted. "Numerical proximity is not shared mechanism." This is a **synthesis, not an identity**.

### M9-1 -- The class, and where FTGB sits in it   [S / synthesis]

A *nonlinear, driven-dissipative, coupled-oscillator system on a helical / elastic /
topologically-constrained substrate* is specified by four ingredients, each of which FTGB already
carries:

1. a local nonlinear oscillator with a driven limit cycle -- the **Stuart-Landau / Hopf normal form**;
2. coupling between many such oscillators -- **Kuramoto / Adler / Arnold** synchronization + rational
   locking;
3. a helical, elastic carrier with bend/twist/stretch/writhe mechanics and the topological law
   `Lk = Tw + Wr`;
4. a transport / conservation structure on that carrier (helicity / torsion current), driven and
   dissipative.

FTGB's object -- the driven toroidal-Beltrami plasmoid -- instantiates all four: the heartbeat
(Stuart-Landau limit cycle at `r* = sqrt(2)`, [V]); the multibody beat-rhythm organization of the
carrier comb / EVO cluster; the helicity/topology sector (`Lk = Tw + Wr`, four-torsion trichotomy);
and the current-leg helicity/torsion transport. FTGB is therefore **a member of** the class, with a
plasma substrate rather than a biopolymer or chemical one.

### M9-2 -- The tiered mapping table (core deliverable): 7 IDENTITY / 5 ANALOG / 4 CAUTION

Tiers: **[IDENTITY]** = the *same mathematics*, already load-bearing in FTGB (an intra-class fact, not
a new claim); **[ANALOG]** = a *different substrate* sharing the mathematics (what FTGB *learns* is
stated, not an identity); **[VOCAB/CAUTION]** = shared words only, or an imported discipline caution.

**IDENTITY rows (I1-I7) -- established-convergence.**

| # | FTGB structure | Framework element | Citation |
|---|---|---|---|
| I1 | driven heartbeat `dw/dt = (mu + i omega)w - beta|w|^2 w`, `mu=1, beta=1/2 -> r* = sqrt(2) = 1.414214` [V] | Stuart-Landau normal form (canonical supercritical-Hopf) | Stuart 1960 / Landau 1944 |
| I2 | multibody beat-rhythm organization of N family members | Kuramoto `theta_i' = omega_i + (K/N) sum sin(theta_j - theta_i)`, `K_c = 2/(pi g(0))` | Kuramoto 1975/1984; Strogatz 2000 |
| I3 | two-body locking of any FTGB pair | Adler `phi' = d(omega) - K sin phi` | Adler 1946 |
| I4 | inharmonic CK-comb `1:1.72:2.43` resists locking -> KAM 3-torus | Arnold tongues `p:q` mode-locking, width `~K^q` | Arnold 1961 |
| I5 | helicity/topology ledger, twist<->writhe heartbeat partition | `Lk = Tw + Wr` (Calugareanu-White-Fuller) | equation [IDENTITY]; substrate [ANALOG] |
| I6 | dual reading of the wave math (probability vs FLOW) | Madelung `psi = A exp(iS/hbar)`, `p = grad S` | Madelung 1927; de Broglie 1924 |
| I7 | driven-not-static ethos ("heartbeat, not flywheel") | driven-dissipative multiscale organizing principle | (methodological) |

**ANALOG rows (A1-A5) -- novel-synthesis (shared math, different substrate).**

| # | FTGB structure it touches | Framework element (substrate) | Citation |
|---|---|---|---|
| A1 | toroidal ribbon elastic energy; twist<->writhe partition | DNA chiral elastic rod `E = int[A kappa^2 + C(Om-Om0)^2 + Ks eps^2 + 2G(Om-Om0)eps] ds`, twist-stretch coupling `G` | PMC3726534 |
| A2 | current-leg helicity/torsion transport | overdamped torsion-TRANSPORT PDE `zeta d_t theta = C d_ss theta + tau_active - tau_relax` | Nelson PNAS 96,14342 (1999); Nat.Commun. s41467-025-65567-5 |
| A3 | onset/entrainment of the driven heartbeat | driven Duffing `x'' + 2gamma x' + omega0^2 x + beta x^3 = F0 cos(wd t)`; multi-channel coupling stabilizes noisy rhythms | Cell Systems 2023 |
| A4 | pattern/mode structure; memory in the driven cycle | BZ chemical oscillator: Hopf limit cycle, reaction-diffusion, Arnold tongues, mechano-chemical memory | Springer 10910-021-01223-9; PNAS 2320331121 |
| A5 | LENR / Pd-D scaffold substrate | phonon Hamiltonian `H = sum hbar omega_s(k)(n+1/2)`, mass-weighted Hessian normal modes, PdH/D isotope shift `omega_D ~ omega_H/sqrt(2)` | cfm.ehu; APS PRB 101,075117 |

**VOCAB/CAUTION rows (C1-C4)** -- see M9-4.

### M9-3 -- The genuine extension: a torsion/helicity TRANSPORT PDE for the current-leg   [ANALOG] -> [S] candidate

The most valuable import. FTGB's current-leg trilogy proved a hard result: the *static* matter<->helicity
4-current is structurally over-determined -- it closes iff a field magnitude is constant (residual
`0.605` static, `0.46-0.66` driven-aligned, both [V]) -- so the current-leg is a **postulate [S]** at
the static/equilibrium level. In DNA biophysics, torsional stress is not a conserved static field but a
driven, dissipative **transport** quantity (Nelson 1999: twist equilibrates far faster than writhe;
active torque is injected locally and diffuses):

```
zeta d_t theta = C d_ss theta + tau_active - tau_relax
     (drag)      (torsional      (drive)     (relaxation)
                  diffusion)
```

**Proposed FTGB adoption (novel-synthesis).** Recast the current-leg as a driven transport law
`zeta d_t h + div K = sigma_drive - sigma_loss`, with `h = P.Omega` the generalized-helicity density and
`K = h v_s + (mu_s - P.v)Omega_s` its (already-derived) flux; `sigma_drive` is the sheath forcing (the
`-2 E.B` term that breaks static helicity conservation is *exactly* the injected torque). The steady
state need not satisfy `P.v = const` pointwise, only in flux balance -- the first construction that
could move the current-leg from postulate toward a driven theorem.

**Tier.** [ANALOG] established (the DNA equation is real and cited) -> **[S] candidate** for FTGB (not
yet computed). **Do NOT claim closure**; claim a structurally identical driven-transport template that
maps onto the named open item. The substrates differ; the PDE *structure* (overdamped diffusion + local
active source) is what transfers. The static [V] negative stands untouched until a forced-transport
steady state is computed.

**Source.** TOOLKIT_ADV_09 sec M9-3.

### M9-4 -- The cautions, imported as FTGB discipline   [VOCAB/CAUTION]

The source material's own cautions are adopted as standing FTGB discipline:

- **C1 -- "vibration" does not imply one coherent resonance across scales.** FTGB coherence is
  *conditional* (comb sync on/off between ~4 nm and ~10 nm); the electron internal whirl `7.76e20 rad/s`
  never phase-locks across a cluster. No cross-scale single-resonance claim.
- **C2 -- classical / chemical oscillation != de Broglie coherence.** FTGB's own trichotomy forbids
  conflating harmonics (`n omega`), the CK eigenspectrum (`1:1.72:2.43`), and the beat (`f1 - f2`).
- **C3 -- coherent matter-wave chemistry is a specialized ultracold regime, not ordinary kinetics.**
  The only route above the deuteron sync threshold is the cold Bose seed (`n lambda^3 >= 2.612`); warm
  classical gas is `n lambda^3 ~ 0.01`, hopelessly below.
- **C4 -- "molecular" means many-body oscillator organization, nothing more.** No biological/chemical
  assembly, no energy gain, no nuclear rate is claimed from any row.

**Note on the `sqrt(2)` recurrence.** `r* = sqrt(2)` (heartbeat radius, `sqrt(mu/beta)` with
`mu=1, beta=1/2`) and `omega_D ~ omega_H/sqrt(2)` (isotope shift, mass-ratio-2 square root) both feature
`sqrt(2)` but for **unrelated reasons** -- a VOCAB coincidence, not a shared mechanism. Not promoted.

**Limits [V].** This module does not claim substrate identity, cross-scale coherence, or any FTGB number
derived from the analogs; the A-rows are learning targets, not derivations; the torsion-transport recast
(M9-3) is a candidate [S], not a closure; no biological, chemical, or nuclear rate is asserted.

**Source.** TOOLKIT_ADV_09 sec M9-5, sec M9-7.

---

## 6. Module M10 -- Topological-soliton and conserved-current methods

> **Scope limit (stated first).** These are **methods**, tiered by what they are licensed to deliver.
> Two of them (M10-1 canonical helicity, M10-3 moduli-geodesic) are **validated machinery** -- a proven
> Casimir and an exactly-lower-dimension-reproduced pipeline -- trustworthy at the stated precision.
> Two (M10-4 seesaw, M10-5 RG-dielectric) are **reading/reduction** methods that reframe a problem in
> FTGB variables without solving it. **M10-3 carries a LOAD-BEARING usage warning (M10-3.0), stated in
> full before the method, because misusing it silently inflates a branching amplitude by orders of
> magnitude.** No nuclear rate, cross-section, branching magnitude, mass, or scale is invented here;
> `E_fm = 2.5 MeV` stays retracted; baryon number is conserved throughout.

### M10-1 -- Canonical / generalized helicity conserved-current method   [V] + [credited]

**Statement.** A driven-dissipative ideal two-fluid (Yoshida-Mahajan double-Beltrami) object has its
own ideal conserved current -- the **canonical (generalized) helicity** -- even when the ordinary
**magnetic** helicity is not conserved (once `E.B != 0`). When you need a conserved topological charge
for a driven, non-force-free object, do not use magnetic helicity; use the canonical one.

**Key equations.** Per species `s` (charge `q_s`, mass `m_s`, flow `v_s`, inertial length
`d_s = m_s/q_s`):

```
canonical momentum     P_s     = A + d_s v_s
generalized vorticity  Omega_s = curl P_s = B + d_s curl v_s
generalized helicity   H_s     = integral P_s . Omega_s dV        (Casimir, dH_s/dt = 0 ideal)
helicity density       h       = P_s . Omega_s
canonical Ohm (ideal)  eps_s   = -d_t P_s - grad mu_s = -v_s x Omega_s

local law:   d_t h + div[ mu_s Omega_s - (v_s x Omega_s) x P_s ] = -2 eps_s . Omega_s = 0
         =>  d_mu K^mu = 0 ,   K = h v_s + (mu_s - P_s.v_s) Omega_s
```

The current is divergence-free **because** `eps_s . Omega_s = -(v_s x Omega_s).Omega_s = 0` identically
(a Casimir/geometric fact). Contrast the magnetic-helicity current, which is not conserved under drive:
`d_mu K^mu_mag = -2 E.B != 0` (Berger-Field 1984). With an external body force,
`d_mu K^mu = 2 f_ext . Omega`, so **conservation survives an external drive iff `f_ext perp Omega`** --
the hinge of every driven-closure question.

**Validity / tier.** **[V] / [credited].** `dH_can/dt = 0` ideal is a proven Casimir; the local
`d_mu K^mu = -2 eps.Omega = 0` is verified in-project (residuals `~1e-16` on genuine equilibria); the
`f_ext perp Omega` condition is [V].

> **Citation note (load-bearing).** The Casimir claim rests primarily on the two firmly-verified
> references **Steinhauer-Ishida 1997, PRL 79, 3423** and **Mahajan-Yoshida 1998, PRL 81, 4863** (the
> primary load-bearing pair; Woltjer 1958 and Berger-Field 1984 underpin the magnetic-helicity
> contrast). The modern statement **Bae-Kang-Shin 2025, arXiv:2504.07629** (magneto-vorticity helicity,
> Prop. 2.1) is carried as a corroborating reference **(VERIFIED real and on-topic; confirm exact
> Prop. label at lock)**. Bae-Kang-Shin is **not** the sole support and
> should not be cited alone; the Steinhauer-Ishida + Mahajan-Yoshida pair carries the claim
> independently.

**How to reuse.** For any driven Beltrami/Hopf object, define `P_s, Omega_s, h` first; the canonical
helicity is the conserved charge to reason with. The flux decomposition `K = h v + S Omega`,
`S := mu - P.v`, is the universal starting point for a medium<->matter closure test (M10-2). The
`f_ext perp Omega` rule tells you exactly what an external drive must satisfy to preserve the invariant.

**Source.** TOOLKIT_ADV_10 sec M10-1 (`DRIVEN_CANONICAL_HELICITY_4CURRENT`, `DRIVEN_NONALIGNED_CLOSURE`).

### M10-2 -- No-go template for magnitude-inhomogeneity obstructions (the `|B| = const` / `P.v = const` template)   [V]

**Statement.** A recurring, transferable proof pattern: a conserved-current or medium<->matter closure
identity holds **iff some field magnitude is spatially constant**, which a topologically nontrivial
(nulled/knotted/Hopf) field provably cannot be. This is how three separate current-leg negatives were
proven; it is the standard tool for deciding whether a proposed closure is a theorem or a postulate.

**The template (four steps).**
1. **Reduce closure to a scalar constancy condition.** Write the matter 4-current as `(rho, rho v)`
   and the flux as `K = h v + S Omega`. Because `S` is a SCALAR, `S Omega = 0` forces `S = 0` pointwise
   -- there is no "S perpendicular to Omega" vector branch (a load-bearing subtlety; presupposing one is
   a category error). Closure `<=>` a single scalar is constant: static magnetic-helicity current closes
   iff `|B| = const`; aligned-driven canonical current closes iff `P.v = const`.
2. **Show the constancy is impossible for nontrivial topology.** The Beltrami identity
   `grad(|P|^2/2) = (P.grad)P` (since `curl P = lambda P`) gives `|P| = const <=> straight field lines`,
   a laminar screw field with no nulls, no linking, zero Hopf index -- topologically trivial. Any field
   with nulls (required for Hopf/CK closed fibres) has spatially varying magnitude.
3. **The cross-term positivity obstruction (the reusable kill).** For a two-mode double-Beltrami
   `P = p1 G+ + p2 G-`, constancy of `P.v` reduces to `p1^2 f+ = p2^2 f-` on the ABC self-fluctuations.
   Because `(A'B')(B'C')(A'C') = (A'B'C')^2 >= 0`, the three products cannot all carry the required
   sign -- positive-proportionality is algebraically impossible unless both modes degenerate to single
   plane waves (trivial). This `(A'B'C')^2 >= 0` step is the transferable kill.
4. **Classify the residual obstruction set: measure-zero (benign) vs finite-volume (killer).**
   - **finite-volume obstruction = KILLER:** static `|B| = const` fails wherever `|B|` varies =
     everywhere on a nontrivial object -> a genuine no-go.
   - **measure-zero obstruction = BENIGN:** the two-fluid current-null set `{v_e = v_i}` is codim-3
     isolated points (the `B`-nulls); the object crosses them without consequence -- `E,B` bounded,
     drive increment `dA ~ 1/r` is L1-integrable and `|dA|^2 ~ 1/r^2` is L2-integrable, so no integral
     quantity sees the failure. Closure holds on the full-measure region.

**Key results (all [V], traced).** Static: closes iff `|B| = const`, residual `0.605`, irreducible.
Aligned-driven: closes iff `P.v = const`, residual band `std(P.v)/mean ~ 0.46-0.66`; no-go proven [V]
for single-mode, equal-`|lambda|` opposite-helicity, and well-separated spheres ([S] in the
close-same-sign-sphere corner, floor `~0.58`). Constant-`|P|` control closes exactly (`~1e-16`) --
confirms the iff. R1 current-null: genuine but benign (measure-zero).

**The escape hatch this template also names.** The obstruction is *pointwise* (steady/aligned). In the
genuinely time-dependent, non-aligned regime the curl obstruction becomes an identity and vanishes: the
closure surface is pointwise non-empty, realizable with a bounded drive satisfying `S = 0` **and**
`f_ext perp Omega`. That regime is **characterized-open, leaning conditional-theorem** (DOF count 8/8
determined once >= 3 free drive functions are added), with **sustained (all-time) existence the single
open piece** -- category-identical to open large-data 3D Navier-Stokes / Hall-MHD regularity, not
FTGB-specific.

**Validity / tier.** **[V]** for the template and the static/aligned no-gos; **[S]** in the close-sphere
corner; **characterized-open** for the driven non-aligned regime. The static [V] negative stands
untouched by every sequel.

**How to reuse.** Whenever a proposed conservation/closure looks over-determined: (i) reduce it to a
scalar `S = 0` via `K = h v + S Omega`; (ii) test whether `S = 0` forces a magnitude constant; (iii) if
so, apply steps 2-3 to show nontrivial topology forbids it; (iv) classify the failure set (measure-zero
benign vs finite-volume killer); (v) check whether time-dependence + a bounded `f_ext perp Omega` drive
reopens it.

**Source.** TOOLKIT_ADV_10 sec M10-2 (`CURRENTLEG_RESIDUAL_REDUCIBILITY`, `DRIVEN_PV_CONST_NOGO_PROOF`
(+VERIFY), `CURRENTLEG_R1_CURRENTNULL`, `DRIVEN_NONALIGNED_CLOSURE`).

### M10-3 -- Moduli-geodesic transition-amplitude method (sine-Gordon-validated)   [S-model, validated]

> ### M10-3.0 -- CRITICAL USAGE WARNING (LOAD-BEARING -- read before using this method)
>
> This method is genuinely validated, but it is **easy to misuse in two specific ways that inflate a
> result by orders of magnitude.** Both are stated first, on purpose.
>
> **1. The DIAGONAL `(mu, V)` vibrational quantum is NOT the OFF-DIAGONAL branching gap.** The
> `(mu, V)` small-oscillation quantum `hbar omega = hbar c sqrt(k/mu)` is a **diagonal**
> curvature/inertia quantum of ONE surface. The branching amplitude `Delta` is the **off-diagonal**
> coupling between TWO diabatic surfaces at a crossing. **They differ by ORDERS OF MAGNITUDE.** Executed
> on the real B=4 merger coordinate, the diagonal quantum was `hbar omega_merger = 66-95 MeV` (the
> Barnes-Baskerville-Turok "cube -> two donuts" mode, ~20 MeV scale), while the Landau-Zener target
> `Delta` is `~1.4-1.9 MeV` -- a `~20-50x` gap. **Do not dress a static energy ratio (e.g.
> `(well/E4)*Q ~ 1.3 MeV`) as a "moduli-geodesic Delta"** -- that was the exact error one verification
> caught and the executed calculation corrected.
>
> **Sanity gate:** set `Delta := hbar omega_merger` in `S = exp(delta)`,
> `delta = pi Delta^2 / (2 hbar v |dF|)`; you get `log10 S ~ 9600` (the absurd "freeze-BOTH-channels"
> pathology), which POSITIVELY PROVES the diagonal quantum is not the gap. Always run this freeze-both
> check; if `S` is nonsensical you have computed the wrong object.
>
> **2. Executing it needs REAL relaxation (arrested Newton flow), NOT a reduced ansatz.** Every
> tractable shortcut fails in the crossing region -- precisely where the off-diagonal coupling lives:
> a **product ansatz** hits a repulsive core wall (never reaches the fused basin); a **naive field
> blend** breaks topology mid-path (`B -> 2.4`, spurious barrier); **free coarse/massless
> arrested-Newton-flow** UNWINDS the topology (`|B| -> 0`) at any coarse grid. Robust integer winding
> needs `dx <= 0.10 fm` (~5% needs `dx <= 0.06 fm`), i.e. the standard Battye-Sutcliffe/Feist
> production setup (compiled/GPU, N >= ~150). So the off-diagonal `Delta` is a **named, quantified,
> thesis-scale blocker**, not something the reduced pipeline can deliver.
>
> **Bottom line:** this method is trustworthy for FORM, SCALING, and ORDER-OF-MAGNITUDE BANDS (with a
> factor-~2.2 coefficient ceiling), and is NOT trustworthy for precision coefficients or for the
> off-diagonal branching gap without a full relaxed two-surface solve.

**Statement.** Reduce a soliton reaction / bound-state to a low-dimensional collective coordinate
`sigma`, compute the moduli-space metric `mu(sigma)` (inertia) and potential `V(sigma)` as genuine
field integrals, then quantize the reduced system to get a transition amplitude / bound-state spectrum
via the geodesic (Manton) approximation and a Landau-Zener form.

**Key equations.**

```
moduli metric     mu(sigma) = integral sum_a (d n_a / d sigma)^2 d^3x        (reduced inertia)
potential         V(sigma)  = E_soliton[field(sigma)] - E(sigma -> infinity)
reduced dynamics  (1/2) mu(sigma) sigma_dot^2 + V(sigma) = -binding          (geodesic on (mu,V))
diagonal quantum  hbar omega = hbar c sqrt(k / mu(sigma*)) ,  k = V''(sigma*)
LZ branching      S = exp(delta) ,  delta = pi Delta^2 / (2 hbar v |dF|)     (Delta = off-diagonal gap)
```

**Validation (why it is trustworthy at its tier).** Run on 1+1 sine-Gordon, where exact answers exist:
kink mass `M = 7.999989` vs exact `8` (rel. err `1.4e-6`, exact reproduction); kink-antikink force decay
rate = meson mass to `0.9%`; breather near-threshold scaling law `binding ~ w^p` gives moduli `p = 1.93`
vs exact `p = 2.0` (correct functional form) with an **honest O(1) coefficient ceiling of factor ~2.2**
near threshold. So the pipeline gets mass exactly, force decay-rate exactly, bound-state scaling
exponent right, and the bound-state coefficient only to a factor ~2 -- trustworthy for form/scaling/
bands, not precision.

**Validity / tier.** **[S-model, sine-Gordon-validated]** for form/scaling/bands (factor-~2.2 ceiling);
**[model / EXECUTED]** for genuine B=4 field integrals (~10-30% ansatz + factor ~2-3 Skyrme
over-stiffness); **[label / BLOCKED]** for the off-diagonal reactive `Delta` (named thesis-scale
blocker, not delivered). **[reject]:** any fabricated `Delta` / rate / branching magnitude;
`E_fm = 2.5 MeV`.

**How to reuse.** (1) Compute `mu(sigma)` and `V(sigma)` as REAL field integrals -- never skip `mu`, and
never label a static ratio a geodesic result. (2) Calibrate `mu(sigma -> infinity)` to the physical
reduced mass, `V` to an energy anchor. (3) Report outputs as a BAND with the factor-~2.2 method ceiling
propagated (it points DOWN -- the method OVERestimates the bound frequency). (4) For a branching
amplitude, obey the M10-3.0 warning: the `(mu,V)` quantum is diagonal; the off-diagonal `Delta` needs a
relaxed two-diabatic-surface solve. (5) Note the sector split: the moduli-geodesic method is native to
the Skyrme/baryon sector (`pi_3 S^3`); the lepton/EVO/neutrino sector (`pi_3 S^2`, Hopf/Beltrami) is a
SPECTRAL (eigenvalue-difference) computation, not moduli-geodesic.

**Source.** TOOLKIT_ADV_10 sec M10-3 (`SELF_UNIFIED_SKYRME_MULTIBODY`, `B4_MODULI_GEODESIC_EXECUTED`,
`B4_TWO_DIABATIC_RELAXATION`).

### M10-4 -- Seesaw frequency-downconversion reading   [S] reading / [V-dim] calibration

**Statement.** Under the calibrated mass<->frequency map `m = hbar omega / c^2`, the type-I seesaw maps
term-by-term into frequency space and reads as a **parametric-beat downconversion**: a heavy whirl
frequency divides the square of a Dirac-coupling whirl down to a light whirl. This is the operation the
M9 coupled-oscillator substrate already carries, so it is a legitimate FTGB-native re-reading -- but it
**restates, does not resolve**, the neutrino-mass terminus.

**Key equations.**

```
type-I seesaw   m_light ~ m_D^2 / M_R              [Minkowski 1977; GRS; Yanagida]
frequency read  omega_light ~ omega_D^2 / omega_R  (via m = hbar omega/c^2)
dimensional     (hbar omega_D/c^2)^2 / (hbar omega_R/c^2) = hbar (omega_D^2/omega_R)/c^2 = a mass  [V-dim]
```

**What is [V-dim].** The whirl ladder is correctly calibrated: the `nu` rung `omega = 7.6e13 rad/s`
gives `m = hbar omega/c^2 = 0.05002 eV`, matching the atmospheric scale
`sqrt(|Dm2_31|) ~ 0.05 eV` to **0.04%**; e/p/d rungs reproduce their known masses to `<= 0.3%`.

**What is NEGATIVE (the honest limit).** The only on-ladder solution of
`omega_D^2/omega_R ~ omega_nu` is the trivial no-op `omega_D = omega_R = omega_nu` (`M_R = m_D`, no
seesaw gain). A genuine downconversion needs an **off-ladder** heavy scale (e.g.
`omega_R = omega_e^2/omega_nu ~ 7.9e27 rad/s`) -- the external Majorana/LNV sector, exactly as the
terminus states.

**Validity / tier.** **[S]** for the duality reading, **[V-dim]** for the ladder calibration confirm,
**NEGATIVE** for on-ladder closure. Claims the seesaw is a frequency-downconversion and the ladder is
calibrated; does NOT claim FTGB derives `m_nu` or contains the heavy scale.

**How to reuse.** Use `m = hbar omega/c^2` to move ANY mass relation into frequency space and check
whether FTGB's own whirl ladder can supply the needed levels; if the required denominator level lands
off-ladder, the mapping *locates and names* an external ingredient rather than deriving it.

**Source.** TOOLKIT_ADV_10 sec M10-4 (`SEESAW_FTGB_DUALITY_BRIDGE`).

### M10-5 -- RG dielectric-flow / IR-fixed-point method + the genericity-denominator anti-numerology control   [S-mechanism] / [flagged]

**Statement.** Read a running coupling as a scale-dependent polarizable-medium dielectric, so that
"running-coupling" and "static-winding" are the SAME object at two scales (the category gap between
"alpha RUNS" and "the object gives a STATIC count" dissolves). The static/long-wavelength invariant is
identified with the **IR (`q^2 -> 0`) endpoint**. This well-poses the mechanism but does not force the
value.

**Key equations.**

```
dielectric map   K_PV(q^2) := alpha(0) / alpha(q^2) = 1 - Delta_alpha(q^2) ,   K_PV(0) = 1
one-loop run     alpha(Q^2) = alpha(0) / (1 - sum_l (alpha(0)/3pi)[ln(Q^2/m_l^2) - 5/3])
slope            d(1/alpha)/d ln Q^2 = -(alpha(0)/3pi) per lepton   (proportional to alpha => cannot source it)
beta function    beta_alpha = (2/3pi) alpha^2 sum_f Q_f^2  -> only root alpha* = 0 (Gaussian FP)
```

**What is established.** The coupling grows toward the UV (`137.036 -> ~132.7` leptonic at `M_Z`), so
**137.036 is the INFRARED endpoint** -- correct conceptually, since a static object is what you see at
zero momentum transfer. The running <-> polarizable-dielectric duality is exact and textbook.

**What is NOT forced (the honest core).** The IR value is the integration constant of the flow: shifting
the IR boundary condition by hand just translates the whole curve. The beta function has no nontrivial
fixed point (only Gaussian). So the bridge REDUCES the problem but does not solve it.

**The genericity-denominator anti-numerology control (reusable discipline).** Before promoting ANY
near-miss to a constant, enumerate a fixed family of simple invariants over the object's real constants
and **count hits near the target vs a displaced control target** -- if comparable, the near-miss is
generic numerology:
- near-misses at 137.036 are ordinary (`17/11200` vs `8/11200` control);
- a `21,168`-combo family at 0.5% tol gives `18` hits @ 137.036 vs `12` @ control (comparable); at
  0.05% tol `4` vs `6` (control has MORE) -- 137 is not anomalously hard;
- 137 is PRIME (Hopf linking `Q_H = p*q` factors only {1,137}); the object's real levels are Chern
  `C = +-2` and Hopf `Q_H = 1`, neither of which is 137.

Use the denominator (control-target count within the same tolerance) as the gate: **promote only if the
target is anomalously dense relative to control.**

**Validity / tier.** **[S-mechanism]** (category gap dissolved, mechanism well-posed) / **[flagged]**
(value not forced; `~137` stays flagged, `20 phi^4` and Wyler forms stay generic). The IR-fixed-point
closure test returned a clean, well-posed NEGATIVE. What would flip [S] -> [V]: an IR fixed point of the
object's own dielectric flow whose `q^2 -> 0` holonomy/winding invariant equals `1/alpha(0)` ab-initio,
zero tuned integer, in >= 2 independent routes.

**How to reuse.** (1) To bridge a "runs vs static" category mismatch, cast the running coupling as
`K_PV(q^2) = alpha(0)/alpha(q^2)` and pin the static invariant to the IR endpoint. (2) Do not expect the
running to source a value -- it fixes only the slope. (3) Apply the genericity-denominator control to any
proposed numerical coincidence before promotion.

**Source.** TOOLKIT_ADV_10 sec M10-5 (`ALPHA_KPV_RUNNING_BRIDGE`, `ALPHA_IR_FIXED_POINT_HOLONOMY`).

### M10-6 -- The methods table (summary)

| # | Method | What it delivers | Tier |
|---|---|---|---|
| M10-1 | canonical/generalized helicity current `d_mu K^mu = 0`; `f_ext perp Omega` rule | a driven object's OWN ideal invariant (Casimir) when magnetic helicity dissipates | [V] / [credited] |
| M10-2 | no-go template: closure iff a magnitude is const; `(A'B'C')^2 >= 0`; measure-zero vs finite-volume | decides theorem-vs-postulate for a closure; classifies the obstruction set | [V] (static/aligned); [S] corner; char-open (driven) |
| M10-3 | moduli-geodesic `(mu,V) -> quantum / LZ amplitude`; sine-Gordon-validated | FORM/SCALING/bands (factor-~2.2 ceiling); diagonal quantum executed | [S-model validated]; [model EXECUTED]; off-diagonal [label/BLOCKED] |
| M10-4 | seesaw as frequency downconversion `omega_l ~ omega_D^2/omega_R` via `m = hbar omega/c^2` | reframes mass relation; locates external ingredient (off-ladder scale) | [S] reading / [V-dim] calibration / NEG on-ladder |
| M10-5 | RG dielectric flow `K_PV(q^2) = alpha(0)/alpha(q^2)`; IR endpoint; genericity denominator | dissolves runs-vs-static category gap; anti-numerology control | [S-mechanism] / [flagged] value |

**Classification.** VALIDATED machinery (trust at stated precision): M10-1 (proven Casimir), M10-3
(exact lower-D reproduction with a named ceiling). PROOF template (reusable, [V]): M10-2. Reading /
reduction methods (reframe, do not solve): M10-4, M10-5.

**Limits [V] and the one load-bearing warning, restated.** This module does not claim any current-leg
closure (M10-1 supplies the object's conserved current; M10-2 shows the matter-current closure remains a
POSTULATE, static [V] no-go untouched); does not deliver the off-diagonal branching gap `Delta`
(M10-3's `(mu,V)` quantum is DIAGONAL, tens of MeV; the off-diagonal `Delta ~ 1.4-1.9 MeV` is a named,
quantified, thesis-scale BLOCKER needing a relaxed two-diabatic-surface solve at `dx <= 0.06-0.10 fm`;
the freeze-both sanity gate PROVES the diagonal is not the gap); does not derive any neutrino mass (M10-4
confirms only the ladder CALIBRATION and locates the required off-ladder external scale); does not force
alpha (M10-5 pins 137 to the IR, but the value is the RG integration constant); asserts no nuclear rate,
cross-section, branching magnitude, mass, or scale.

---

## 7. Module M11 -- EGM / polarizable-vacuum spectral methods (representation-map, not theory)

Full module: `toolkit/TOOLKIT_ADV_11_EGM_POLARIZABLE_VACUUM_2026-09-09.md`. Verification:
`results/verify/egm_sense_checks.py`, `results/verify/egm_mode_count_closure.py`.

**The one limit (Storti's own framing).** EGM is -- Part 2 §7.2.24 -- *"a method of calculation (not a
theory) based upon energy density."* M11 folds in its **mathematical representation** and **credits its
foundations**, while **adopting none of its numerical predictions**. This extends the M7 Storti tier
`[UNASSESSED/fringe, method-only]` and keeps the standing **excision** of the `e^(-2/3)` factor.

**What is credited.** The polarizable-vacuum refractive index `K_PV`, `c_eff = c/sqrt(K_PV)` (Puthoff 1999);
the ZPF cubic spectral energy density `rho_0(omega) = hbar omega^3 / (2 pi^2 c^3)` (SED; Sakharov;
Haisch-Rueda-Puthoff) -- **[V]** its Planck-cutoff integral returns a Planck-scale energy density.

**The cut-off closure, folded (M11-6).** M11-1 left "how `n_Omega` is fixed" a black box; M11-6 folds the
reusable technique behind it -- the ordinary **Debye/Nyquist 3-D mode-count** band-limit: `g(omega) =
rho_0/(hbar omega) ~ omega^2/c^3`, count `N(Omega) ~ (Omega/c)^3`, terminate at integer `n_Omega` -> cut-off
`omega_Omega ~ n_Omega^(1/3) omega_C`, length `ell ~ lambda_C n_Omega^(-1/3)` (Compton-scale). **[V]**
`egm_mode_count_closure.py`. The cube-root makes the *scale* robust but leaves the *precise* value to the free
integer `n_Omega` -- a structural reason the 0.01% radius "match" is a closure fit, not parameter-free
(reinforcing the M11-4(ii) flag). Method folded; every value stays quarantined.

**The four maps into the toolkit** (why it is worth folding in -- each pillar is math a module already carries):
1. EGM's band-limited harmonic-beat spectrum (fundamental `omega_PV(1,r,M)` -> cut-off `omega_Omega`/`n_Omega`)
   <-> **M9** coupled-oscillator comb + the {121,208,294} kHz carrier comb + the **M10-4** seesaw down-conversion.
2. `K_PV` vacuum dielectric / refractive index <-> the **M10-5** RG dielectric-flow method (with its
   anti-numerology control) and the resonator `m = hbar omega / c^2` (M8-2) mass-from-frequency reading.
3. ZPF cubic spectrum <-> the "field = matter-wave" vacuum-energy backdrop (credited, accounting only).
4. Storti "sense checks" `St_beta...St_theta` <-> **M7** Buckingham-Pi claim-audit (the M7 ONE LIMIT applies).

**What is quarantined [flag]/[excised], per `egm_sense_checks.py`.** The "2:1 harmonic"
`omega_Omega(e)=2 omega_Omega(p)` is definitional (ratio = 2.000 by construction), not a prediction; the
proton-radius 0.01% match does not follow from the clean closed-forms (they miss 0.84 fm by 1e3-1e4x); the
energy-equilibrium radius is Compton-scale only (`r_eq = 0.42 lambda_C`); H0 = 67.08 needs an unmotivated
large factor over `sqrt(GM/R^3)`; and `e^(-2/3)` (=0.513, maps 140.2->72, not 137) stays excised with the
2.3% alpha gap carried as an open problem. Also corrected here: the secondary note's `St_eta = m_p/m_e` is a
mislabel of Storti's 5th sense-check.

---

## 8. Module M12 -- Ginzburg spiral-field theory (toryx / helyx) as structural analogy

Full module: `toolkit/TOOLKIT_ADV_12_GINZBURG_SPIRAL_FIELD_2026-09-09.md`.

**The one limit.** Ginzburg's spiral-field theory is an **ontological/geometric picture**, not a predictive
calculation like M7-M11. It is folded **[fringe framework, analogy-only]** -- a vocabulary and imagery for the
FTGB torus, its resonance ladder, and the field<->matter duality -- with **no physical claim adopted** (no
particle spectrum, no "Unified Spacetime Multiverse," no cosmology).

**The two prime elements, mapped.** The **toryx** (a self-inverting 4D *double-toroidal* spiral element =
prime element of *matter*) maps to the Beltrami-Hopf soliton read as matter and the torus inversion of
`soliton3d.html`; the **helyx** (a *double-helical* element = prime element of *radiation*) maps to the same
object read as a field / photon-helicoid (cf. Reed M8). Ginzburg's **discrete energy levels** map to the
resonator eigenmode ladder (M7-2 carrier comb), and his **matter<->radiation transformation** to the
`m = hbar omega / c^2` field<->matter duality (M8-2).

**The five-framework convergence.** Ginzburg joins Reed (QWM, M8), Storti (EGM, M11), Nielsen (TUFT --
Hopf-fibration `S1->S9->CP4` curl-eigenmode knot spectrum; Beltrami-Higgs on `S3`), and Greenyer (Beat Law /
EVO cascade, M14 -- the shape-independent `N^L` beat ladder + golden-ratio triad dichotomy the object realizes
at its high-drive/EVO rung) as independent fringe frameworks -- **five in all** -- each folded
method/analogy-only, all converging on the **same toroidal, Beltrami/Hopf, resonance-quantized object**. The shared invariants (toroidal/Hopf topology; Beltrami/curl eigenmodes; a
polarizable-vacuum reading; `m = hbar omega/c^2`; an `alpha ~ 137` winding number) are collected in
`GLOSSARY.md` and `REFERENCES.md`, each thread `[credited]` where established, `[framework]` where a reading.

---

## 9. Module M13 -- Nielsen TUFT mass-tower & mixing methods

Full module: `toolkit/TOOLKIT_ADV_13_NIELSEN_TUFT_MASS_TOWER_2026-09-09.md`. Verify:
`results/verify/tuft_mass_tower_check.py`.

**The one limit.** Everything here is `[framework: Nielsen TUFT]` / `[S]` scaffolding on a bed of `[credited]`
mathematics (Proca/Helmholtz, Ray-Singer torsion, lens-space determinants, the curl/Beltrami spectrum,
Chern-Simons). Only two classes are `[V]`: (i) the coefficients reproduce their closed forms, and (ii) the
internal-consistency findings. **Two flags travel with every use:** (a) the **π-power anomaly** -- pure
`C₅=ζ(3)/12` (no π) vs π²-carrying `ω₃=ζ(3)/4π²`, `σ₅`, `σ₉` for the same class of coefficient; the clash is
exactly `C₅/ω₃ = π²/3` `[anomaly]`; and (b) the **blind-fit-at-0.1σ / zero-parameter / sub-0.01%
mass-recovery claims are the PREPRINT's, in Round-2 review -- `[preprint-claim]`, NOT `[V]`.**

**What it folds.** The mass operator (Proca-Beltrami `λ=mc/ℏ`, curl S³ spectrum `±(n+1)/R`, `⋆d` -- linear,
so zero off-diagonal ME); the full quark tower `m_{n,±}=Λ₅(n+1)exp((a₅±λ_T)n + C₅n² + β₅n(n+1)/2 +
σ₅logτ(Kₙ))` with every ζ-coefficient; lepton `ω₃=ζ(3)/4π²`, neutrino `C₉=−0.15670774`; knot/lens norms
`τ(Kₙ)={1,4,3}`, `τ_R(L(n,1))=1/n`; the Ray-Singer/Nash-O'Connor ζ(3) provenance; Chern-Simons `M=ke²/4π`;
CKM `V_ij=⟨ψ_i|ψ_j⟩`; PMNS + ν-masses (`~50 meV`, no seesaw). In-repo verify reproduces `C₅,β₅,σ₅,ω₃,C₉`,
the exact `C₅/ω₃=π²/3` clash, and `τ_R=1/n`.

## 10. Module M14 -- Greenyer beat-law & EVO cascade methods

Full module: `toolkit/TOOLKIT_ADV_14_GREENYER_BEAT_LAW_2026-09-09.md`. Verify:
`results/verify/greenyer_beat_cascade_check.py`.

**The one limit.** Two layers, two statuses. The **beat-dynamics layer** (M14-1..8, 11..15) is self-contained
checkable field mathematics -- symbolic proofs, mesh eigensolves, closed-form identities -- and stands
whether or not any nuclear claim is true. The **nuclear layer** (M14-9/10) is a **pre-registered target** on
Greenyer's `[framework]` baryon-decay channel, with a stated `1.27×` sub-threshold gap; `N_crit ~ 1.7-3e11`
is a `[prediction]`, never a finding. **No over-unity.** Never conflate the continuous helicity `N^(−4L)`
(shrinks) with the exactly-conserved integer winding number.

**What it folds.** The Beat Law `f_b=C v_eff a²/(2πR³)` + the **shape-independent ladder theorem
`f_b(L)/f_b(0)=N^L`** `[V]`; the heartbeat theorem (fixed-helicity min = a single pure mode ⇒ every persistent
beat is driven) `[V]`; the **triad dichotomy** (integer cascades cannot self-phase-match; the golden ratio
always does) `[V]`; two Manley-Rowe invariants with **Fibonacci** coefficients `[V]`; the BIC linking rule;
the anapole `T_L/T_(L+1)=N⁴` and helicity `N^(−4L)`; the THz cascade `ω₀=α_CK ε²ω_A` (`α_CK=½`); the Madelung
bridge + exact **`9/8 μ_B`** Reed theorem `[V]`; magnetic-tension Rayleigh fission + the `N_crit`
`[prediction]`; the Gamow ledger `[framework]`; MRxMHD; the Hopf-Beltrami no-go; the `l=2` mode
`z_(2,1)=5.763459`; the off-resonance theorem `Q(N^k−1)`. In-repo verify confirms the ladder, `N⁴=256`, the
three-wave dichotomy (integer NONE vs golden to 7e-15), and the Fibonacci→φ shadow.

## 11. Consolidated reference list

Established, credited literature underpinning the toolkit (per module). Primary load-bearing references
are named in full; tiers are as used above. See `REFERENCES.md` for the full project-wide citation base,
the convergence-framework primaries (Reed, Storti, **Nielsen TUFT**, Ginzburg, **Greenyer/MFMP**), and the
Bostick / Puthoff / Shoulders ancestors (`LINEAGE.md`).

**Dimensional method (M7).**
- E. Buckingham, *Phys. Rev.* **4**, 345 (1914) -- the Pi theorem. [credited]
- H. Alfven, *Nature* **150**, 405 (1942) -- Alfven waves / speed. [credited]
- S. Chandrasekhar & P. C. Kendall, *Astrophys. J.* **126**, 457 (1957) -- force-free CK fields. [credited]
- M. Kerker, D.-S. Wang & C. L. Giles, *J. Opt. Soc. Am.* **73**, 765 (1983); C. Pfeiffer & A. Grbic,
  *Phys. Rev. Lett.* **110**, 197401 (2013) -- Kerker / Huygens metasurface. [credited]

**QWM conversion + dimensional audit (M8).**
- E. Madelung, *Z. Physik* **40**, 322 (1927) -- hydrodynamic (Madelung) form. [credited]
- L. de Broglie (1924) -- matter wave / internal clock. [credited]
- D. Bohm, *Phys. Rev.* **85**, 166 (1952) -- quantum potential. [credited]
- F. London, *Proc. R. Soc.* A **149**, 71 (1935) -- superconducting response. [credited]
- L. Reed, *Quantum Wave Mechanics* (4th ed., Booklocker 2022), Ch.3/11/17/21/26/36 -- source
  framework. [QWM framework]

**Coupled-oscillator substrate (M9).**
- J. T. Stuart, *J. Fluid Mech.* **9**, 353 (1960) / L. D. Landau (1944) -- Stuart-Landau normal form.
  [credited]
- Y. Kuramoto (1975; *Chemical Oscillations, Waves and Turbulence*, 1984); S. H. Strogatz, *Physica D*
  **143**, 1 (2000) -- Kuramoto synchronization. [credited]
- R. Adler, *Proc. IRE* **34**, 351 (1946) -- Adler locking. [credited]
- V. I. Arnold (circle maps, 1961) -- Arnold tongues. [credited]
- G. Calugareanu (1961) / J. White (1969) / F. B. Fuller (1971) -- `Lk = Tw + Wr`. [credited]
- P. Nelson, *PNAS* **96**, 14342 (1999); *Nat. Commun.* **16**, 10543 (2025)
  (s41467-025-65567-5) -- DNA torsional stress as transport. [credited]
- User-supplied cross-domain source set (treated as credited cross-domain science): PMC12855917
  (multiscale driven oscillators); PMC3726534 + cen.acs (DNA elastic rod); Cell Systems (2023)
  (multi-channel entrainment); Springer 10910-021-01223-9 + PNAS 2320331121 (BZ / mechano-chemical
  memory); cfm.ehu + APS PRB **101**, 075117 (phonons, PdH/D isotope shift).

**Topological-soliton + conserved-current methods (M10).**
- L. Woltjer, *PNAS* **44**, 489 (1958) -- force-free / helicity minimum. [credited]
- **J. B. Steinhauer & A. Ishida, *Phys. Rev. Lett.* **79**, 3423 (1997)** -- canonical-helicity
  Casimir (primary load-bearing pair). [credited]
- **S. M. Mahajan & Z. Yoshida, *Phys. Rev. Lett.* **81**, 4863 (1998)** -- double-Beltrami /
  generalized helicity (primary load-bearing pair). [credited]
- Z. Yoshida & S. M. Mahajan, *Phys. Rev. Lett.* **88**, 095001 (2002). [credited]
- Bae, Kang & Shin (2025), **arXiv:2504.07629** ("On the double Beltrami states in Hall MHD") --
  corroborating modern statement, **VERIFIED real and on-topic** (confirm exact Prop. label at
  lock); not the sole support. [credited]
- M. A. Berger & G. B. Field, *J. Fluid Mech.* **147**, 133 (1984) -- `d_mu K^mu_mag = -2 E.B`.
  [credited]
- T. Dombre et al., *J. Fluid Mech.* **167**, 353 (1986); V. I. Arnold & B. Khesin, *Topological
  Methods in Hydrodynamics* -- ABC / topological fluid dynamics. [credited]
- T. H. R. Skyrme, *Nucl. Phys.* **31**, 556 (1962). [credited]
- N. S. Manton, *Phys. Lett. B* **110**, 54 (1982) -- geodesic approximation; N. Manton & P. Sutcliffe,
  *Topological Solitons* (CUP 2004). [credited]
- R. A. Battye & P. M. Sutcliffe, *Phys. Rev. Lett.* **79**, 363 (1997); C. Barnes, W. K. Baskerville &
  N. Turok, *Phys. Rev. Lett.* **79**, 367 (1997); J. Feist, P. H. C. Lau & N. S. Manton, *Phys. Rev.
  D* **87**, 085034 (2013) -- B=4 Skyrme machinery. [credited]
- R. F. Dashen, B. Hasslacher & A. Neveu, *Phys. Rev. D* **11**, 3424 (1975) -- soliton quantization.
  [credited]
- L. Landau (1932) / C. Zener, *Proc. R. Soc. A* **137**, 696 (1932) -- Landau-Zener. [credited]
- P. Minkowski, *Phys. Lett. B* **67**, 421 (1977); Gell-Mann, Ramond & Slansky (1979); T. Yanagida
  (1979); R. N. Mohapatra & G. Senjanovic, *Phys. Rev. Lett.* **44**, 912 (1980); E. Majorana, *Nuovo
  Cimento* **14**, 171 (1937) -- type-I / inverse seesaw. [credited]
- PDG 2024 (neutrino-mixing review); NuFIT 5.2 (2022); CODATA-2022 (`alpha(0)^-1 = 137.035999206`);
  standard QED one-loop vacuum polarization. [credited]

---

## 12. Do-not-cite note

The following are named so they are never cited as established, and never resurrected:

- **QWM gravity chapters** (Reed, *QWM* Ch.33-47: Oldershaw discrete-scale-relativity, oscillator-sync-
  as-gravity, graviton = phase-conjugate photon; the Ch.36 cosmological mass scaling
  `M_psi = Lambda^D M_{psi-1}`) -- **[unassessed external, EXCLUDED]**. Read critically; not converted;
  not endorsed. (The polarizable-vacuum `K_PV` frame itself stays [credited] as a weak-field-GR model;
  only Reed's gravity extension of it is walled.)
- **R. Storti, *Quinta Essentia*** and **Ginzburg, *Unified Spiral Field*** -- **[unassessed/fringe,
  method-only]**; a dimensional-bookkeeping / geometry borrow at most, no physical claim adopted.
- **Nielsen TUFT** -- a **preprint**, not peer-reviewed; the octahedral tower is ours. Cite as tiered
  material, not as established.
- **Reed QWM ontology** (mass IS the whirl; charge IS spin angular momentum; roots-of-unity /
  hypocycloid charge quantization) -- **[QWM framework]**: a method/notation choice attributed to Reed,
  not established physics. The underlying *equations* (`E = hbar omega`, `m = E/c^2`, the winding
  integral) are textbook and credited; the ontology is not.
- **Bae-Kang-Shin arXiv:2504.07629** -- now VERIFIED real and on-topic (confirm exact Prop. label at
  lock); carry alongside Steinhauer-Ishida 1997 + Mahajan-Yoshida 1998, which remain the primary
  load-bearing pair; not the sole support for the canonical-helicity Casimir.
- **Fabricated / retracted numbers** -- `E_fm = 2.5 MeV` (**[reject]**, retracted); any fabricated
  branching amplitude `Delta`, nuclear rate, cross-section, or `COP` excess. FTGB derives no COP; the
  `COP ~ 1.3-1.4` figure is inherited field positioning, never an over-unity claim. The `~137`
  coincidences (`1/(20 phi^4)`, Wyler forms) stay **[flagged]**, not promoted.
- **Do-not-cite people/programs (field discipline)** -- Rossi, Mills, and bio-transmutation claims are
  not cited as verified.

---

*This handbook is a consolidation of TOOLKIT_ADV_07 (M7), _08 (M8), _09 (M9), and _10 (M10), which
remain the canonical source-of-record modules with their reproducible ASCII scripts in
`frontier_calcs/`. No new claim is introduced here; every quoted number traces to its source module.*
