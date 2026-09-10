# TOOLKIT ADV — Module M7: BUCKINGHAM PI as CLAIM-AUDIT + DIMENSIONLESS-SCALING MAP

Part of the FTGB math toolkit (see `MATH_TOOLKIT_BASE.md` and the consolidated `TOOLKIT_HANDBOOK.md`; its
predecessor advanced toolkit `MATH_TOOLKIT_ADVANCED_2026-09-02.md` and that toolkit's build plan
`FTGB_TOOLKIT_PROGRAM_PLAN_2026-09-02.md` are extended corpus, not in the jewel). This module supplies the **formal basis of the
dimensional↔dimensionless side-by-side format** and the **claim-audit / scaling-map tool** for the whole
program. Every dimensional matrix, rank, null-space, and Pi-group below is **computed** (not restated) by
`frontier_calcs/toolkit_adv07_buckingham_pi.py` → `toolkit_adv07_buckingham_pi_OUT.txt` (numpy + sympy exact
rational rank/null-space; scipy for the eigenvalue root). ASCII, `PYTHONIOENCODING=utf-8`.

> **THE ONE LIMIT, STATED UP FRONT (read before using any result here).** Buckingham's theorem gives the
> **ALLOWED SCALING ONLY** — the set of dimensionless groups any physical law *may* depend on. It does **NOT**
> give (i) which variables are relevant, (ii) the mechanism, (iii) the function `f` relating the groups,
> (iv) the O(1) constant in front, (v) stability, or (vi) permission to extrapolate across a regime transition
> (laminar→turbulent, collisionless→collisional). A "clean four-anchor law" is a **scaling skeleton**, not a
> theory. Use Pi as a *claim-audit* tool — it tells you exactly which knobs a claim is allowed to depend on and
> therefore what a falsifier must vary — never as a theory generator. This caveat is repeated in §7.

## Tier legend (honesty discipline)
- **[V]** verified here by the named computation / a checked identity.
- **[credited]** established physics we build on (Buckingham; Alfvén; Chandrasekhar–Kendall; Kerker).
- **[A]** analytic / asserted-from-model (standard result, not re-derived).
- **[S]** structural / spectral-geometric, or cited-convergence not fully closed on our side.
- **[QWM framework]** = Reed/quantum-whirl-mechanics reading, used as a *method/notation* choice only.
- **[UNASSESSED/fringe, method-only]** = Storti *Quinta Essentia* — dimensional bookkeeping method borrowed;
  none of its physical claims adopted or endorsed.
- No fabricated numbers/rates. `T_e` is carried as thermal **energy** `k_B T_e` [J] (standard plasma
  convention; `k_B` absorbed), and number density `n` as a pure count per volume `[L^-3]` — both are stated
  choices, not derivations.

---

## M7-1 — The theorem, stated for the project   [credited: Buckingham 1914]

- **WHAT.** Take `n` dimensional quantities `q_1,…,q_n` that enter a physical relation `F(q_1,…,q_n)=0`.
  Write each `q_j` as a column of exponents over a chosen set of **base dimensions** (here SI:
  `M` mass, `L` length, `T` time, `I` electric current, `Θ` temperature, `N` amount). Stack the columns into
  the **dimensional matrix** `D` (rows = base dims, columns = variables). Let `r = rank(D)`. Then the relation
  is equivalent to `Φ(Π_1,…,Π_{N_Π})=0` in **`N_Π = n − r`** independent dimensionless groups.
- **MATH (the null-space construction).** A dimensionless monomial `Π = ∏_j q_j^{a_j}` has zero net dimension
  iff the exponent vector `a` satisfies `D a = 0`. So **the Pi-groups are exactly a basis of the null space
  `ker D`**; there are `n − r` of them because `dim ker D = n − rank D` (rank–nullity). Computing them is a
  linear-algebra problem — done exactly (rational arithmetic) in the script via `sympy.Matrix.nullspace()`.
- **THE RANK SUBTLETY (load-bearing).** `r` is the **rank of `D`**, *not* the count of distinct unit symbols
  that appear. Two base dims can be locked together by the variable set, dropping the rank and *raising*
  `N_Π`. Matrix 3 below is a worked instance: with only circuit/EM quantities (no bare charge, no `ε₀`) the
  current dimension satisfies `I = −2M` identically (a left-null vector of `D`), so even though four unit
  symbols `M,L,T,I` appear, `r = 3` and `N_Π = 5`, not `4`. **Always compute `rank(D)`; never count symbols.**
- **THE EM/PLASMA BASE-DIMENSION CHOICE.** For electromagnetics one may use **SI with current `I`** as an
  independent base dim (primary here, **[V]**), or a reduced constant set (`ε₀, μ₀, c, e`) that trades unit
  symbols for physical constants. A third option, offered by the **[QWM framework]**, treats charge `e` as a
  *spin angular momentum* `~ [kg·rad/s]` (i.e. promotes charge/angular-momentum to a base and demotes current).
  **The theorem is invariant under any invertible change of base dimensions**, so all three give the **same
  `N_Π` and the same Pi-groups** — only the intermediate exponent labels differ.
  **[V] INVARIANCE CHECK** (script): Matrix 1 rebuilt in an `(M,L,T,Q)` base with a charge dimension `Q` (the
  invertible map `I ↔ Q/T`) gives `rank = 4` identically, and both groups `ωR/v_A` and `nR³` remain
  dimensionless in the charge base. Same physics, different bookkeeping.
- **CITATION + TIER.** E. Buckingham, *Phys. Rev.* **4**, 345 (1914). **[credited].** Method-only borrow of
  dimensional-bookkeeping style noted from R. Storti, *Quinta Essentia* — **[UNASSESSED/fringe, method-only]**,
  no physical claim adopted.

---

## M7-2 — COMPUTED: the force-free-object matrix   [V]

Variables `{B, n_i, m_i, R, μ₀, ω}` (the 4 canonical anchors `{B, n_i, m_i, R}` plus `μ₀` and the target
frequency `ω`). **[V] computed** (`toolkit_adv07`):

```
          B    n_i   m_i    R    mu0  omega
   M  [   1     0     1     0     1     0 ]
   L  [   0    -3     0     1     1     0 ]
   T  [  -2     0     0     0    -2    -1 ]
   I  [  -1     0     0     0    -2     0 ]     (Theta, N rows all zero)
```
**`n = 6`, `rank r = 4`, `N_Π = n − r = 2`.** Null-space basis (exact, from the script):
`a₁ = (n_i¹ R³)` and `a₂ = (ω⁶ μ₀³ m_i³ n_i¹ B⁻⁶)`. A physically transparent **complete independent basis**
(rank 2, verified) is:

| Group | Definition | Physical role |
|---|---|---|
| `Π_A = ωR/v_A` | `ω R √(μ₀ n_i m_i) / B` | **Alfvén-Mach** — dimensionless drive frequency |
| `Π_N = n_i R³` | `n_i R³` | number of ions in the object volume (geometric) |

- **DERIVED NATURAL SCALES.** The **only** velocity buildable from `{B,n_i,m_i,μ₀}` is the **Alfvén speed**
  `v_A = B/√(μ₀ n_i m_i)`; the only frequency is the **transit rate** `f_A = v_A/(2πR)`. Every frequency the
  object can have is therefore `f = Λ · f_A` for some **dimensionless** `Λ` — this is all Pi theory delivers.
- **THE MODAL EIGENVALUE `Λ_n`.** The carrier law `f_n = Λ_n · v_A/(2πR)` is exactly `Λ_n = 2π f_n R/v_A =
  (ωR/v_A)|ₙ` — i.e. **`Λ_n` is the value the Alfvén-Mach group `Π_A` takes at resonance `n`.** Pi theory says
  `f_n ∝ v_A/R`; it says **nothing** about the number `Λ_n`. That number is an **eigenvalue** fixed by
  geometry + boundary condition, not by the theorem.
- **[V] `Λ_1 = 4.493409`** is the first nonzero root of **`tan x = x`** — the Chandrasekhar–Kendall / Beltrami
  eigenvalue of the **BALL** (`∇×B=λB`, PEC sphere). The in-jewel script `results/verify/ck_eigenvalues_check.py`
(self-contained bisection, mpmath-cross-checked, and cross-checking the engine's hardcoded roots) returns the first six roots
  `4.493409, 7.725252, 10.904122, 14.066194, 17.220755, 20.371303`, with **inharmonic** ratios
  `1, 1.719, 2.427, 3.130, 3.832, 4.534`. With the canonical medium anchors `v_A = 2.033×10⁴ m/s`, `R = 0.12 m`
  these give the carrier comb `f_n = 121.2, 208.3, 294.0, 379.3, 464.3, 549.3 kHz` (reproduces
  `30_CANONICAL_NUMBERS.md` §I to the digit). Independent anchor check `v_A = B/√(μ₀ n_i m_i)` from
  `B=20.6 mT, n_i=1.7×10¹⁹ m⁻³, m_i=29 amu` returns `2.031×10⁴ m/s`, `f_A = 26.94 kHz`, `f_1 = 121.0 kHz`.
- **CORRECTIVE, STATED PLAINLY [V/S].** `Λ_1 = 4.4934` is the eigenvalue of the **ball/sphere** boundary
  problem **only** — it is **NOT a universal constant.** For the actual toroidal / conical FTGB object the
  eigenvalue becomes a **function of the object's own Pi-groups**,
  `Λ_n = Λ_n(r_minor/R_major, d_i/R, β, S, …)`. Quoting `4.4934` for the torus is a sphere-geometry
  approximation; the true value is set by the aspect ratio and the two-fluid/loss groups of §M7-3. (This is
  consistent with the project's own FreeFEM torus eigensolve, which finds the carrier *split* `Δλ=0.2806` at
  `ε=0.697` rather than a single sphere value — see `30_CANONICAL_NUMBERS.md` §C.)
- **TIER.** Matrix/rank/null-space **[V]**; `v_A`/Alfvén identification **[credited]** (Alfvén 1942;
  Chandrasekhar–Kendall 1957); the "`Λ` is geometry-dependent, not universal" corrective **[V/S]**.

---

## M7-3 — COMPUTED: the plasma-resonator matrix   [V]

Variables `{ω, B, n_e, R, m_i, T_e, e, ε₀, μ₀}` (`T_e` as thermal **energy** `k_B T_e`). **[V] computed:**

```
          omega  B   n_e   R   m_i  T_e   e   eps0  mu0
   M  [    0    1    0    0    1    1    0   -1    1 ]
   L  [    0    0   -3    1    0    2    0   -3    1 ]
   T  [   -1   -2    0    0    0   -2    1    4   -2 ]
   I  [    0   -1    0    0    0    0    1    2   -2 ]
```
**`n = 9`, `rank r = 4`, `N_Π = 5`.** The five groups can be mapped onto the **mechanism-level control
parameters** (this curated set is verified rank-5 = a complete independent basis):

| Group | Definition | Physical role |
|---|---|---|
| `β` | `2 μ₀ n_e k_BT_e / B²` | plasma pressure / magnetic pressure |
| `ω/ω_ci` | `ω m_i /(e B)` | drive vs ion-cyclotron → **Hall / FLR / sideband onset** |
| `d_i/R` | `√(m_i/(μ₀ n_e e²)) / R` | ion skin depth / size → **two-fluid onset** |
| `λ_D/R` | `√(ε₀ k_BT_e/(n_e e²)) / R` | Debye length / size → quasineutrality |
| `n_e R³` | `n_e R³` | ions in the volume (geometric) |

- **[V] KEY DERIVED RELATION (why the carrier is not an independent knob).** The Alfvénic drive group is
  **not** independent: the script's rank check shows `ωR/v_A = (ω/ω_ci)·(R/d_i)` because
  **`v_A = ω_ci · d_i` exactly**. So the carrier `ωR/v_A` is a *product* of two basis groups, not a sixth
  degree of freedom. This is a genuine, computed constraint on the claim structure.
- **HONEST GAPS (what these 9 variables CANNOT build).** `d_e/R` needs the electron mass `m_e` (adds the pure
  ratio `m_e/m_i`); the collisional groups `ν_e/ω` and the **Lundquist number `S`** need a collision frequency
  `ν_e` or resistivity `η`; the Hall wavenumber group `k d_i` and an independent `ω/ω_pe` need a wavenumber
  `k`. Note `c = 1/√(ε₀ μ₀)` is **derived** from the variable set, so it adds no new group. A model that omits
  `ν_e, η, m_e` is silently assuming they are irrelevant — exactly the kind of omission §7 warns about.
- **TIER.** Matrix/rank/null-space and the `v_A=ω_ci d_i` identity **[V]**; the named plasma groups
  **[credited]** (standard two-fluid / gyrokinetic dimensionless parameters).

---

## M7-4 — COMPUTED: the metasurface / Huygens matrix   [V]

Dimensional core `{f0, L, C, a, t, σ, μ₀, c}` (the relative constants `ε_r, μ_r` and all **angles**
`θ_inc, θ_out, α` are already dimensionless — each is *simultaneously* an independent variable **and** its own
trivial Pi-group). **[V] computed:**

```
          f0   L    C    a    t   sigma mu0   c
   M  [    0    1   -1    0    0   -1    1    0 ]
   L  [    0    2   -2    1    1   -3    1    1 ]
   T  [   -1   -2    4    0    0    3   -2   -1 ]
   I  [    0   -2    2    0    0    2   -2    0 ]
```
**`n = 8`, `rank r = 3`, `N_Π = 5`** — the rank drop is the `I = −2M` lock of §M7-1 (only circuit/EM
quantities, no bare charge or `ε₀`), a textbook demonstration that **rank ≠ symbol count.** Complete
independent basis (verified rank-5):

| Group | Definition | Physical role |
|---|---|---|
| `Π_LC` | `2π f0 √(LC)` | LC self-resonance tuning (`=1` at resonance) |
| `Π_cell` | `a/λ = a f0/c` | subwavelength unit cell — **Huygens needs `≪1`** |
| `Π_thick` | `t/a` (or `t f0/c`) | thickness/size, thin-sheet limit |
| `Π_skin` | `t/δ`, `δ=√(2/(ω μ₀ σ))` → `t√(f0 μ₀ σ)` | ohmic penetration / loss |
| `Π_Zind` | `ω L/Z₀ = f0 L/(μ₀ c)` | reactance vs free-space impedance (the `Z_s/Z₀` family) |

- **[V] KERKER / HUYGENS matching group.** The first Kerker (zero-backscatter) condition is the balance of
  electric and magnetic dipole responses. The group **`Π_Kerker = p/(ε₀ Z₀ m)`** (electric dipole `p`,
  magnetic dipole `m`) is **verified dimensionless** by the script; the Huygens condition is
  `Π_Kerker ≈ 1 + i0`, whose experimental signature is an **`S₁₁` (reflection) minimum**. (`p, m` are extra
  variables beyond the eight above; the impedance ratio `Z_s/Z₀` is the `Π_Zind` family.)
- **CONE geometry** `{α, R_apex, R_base, λ, θ_inc, θ_out}`: angles dimensionless; lengths give ratios
  `R_apex/λ`, `R_base/λ`, and the taper `R_base/R_apex`.
- **HONEST BREAKDOWN OF LENGTH-SCALING.** Exact Maxwell length-scale invariance (shrink the geometry, scale
  the frequency, same response) holds only for **frequency-independent, lossless** materials. Real metals and
  dielectrics have **dispersive `σ(ω)`, `ε_r(ω)`, and a skin depth `δ(ω)`** — so `Π_skin` and `Π_cell` do
  **not** co-scale, and a design cannot be freely rescaled in frequency. This is a real limit on any
  "just scale it" claim.
- **TIER.** Matrix/rank/null-space and the Kerker-group dimensionality **[V]**; Kerker condition itself
  **[credited]** (Kerker et al., *JOSA* **73**, 765 (1983); Huygens metasurface, Pfeiffer–Grbic 2013).

---

## M7-5 — THE CLAIM-AUDIT + FALSIFIER TABLE (the key deliverable)   [V-structure / S-claims]

For each FTGB claim: the relevant Pi-groups, which were **held fixed**, which were **assumed small/large**,
and the **direct experimental falsifier**. This is the program turned into a falsifiable scaling map. (The
*groups* are [V]; whether each claim's assumed limit actually holds in the object is [S]/open.)

| Claim | Relevant Pi-groups | Held fixed | Assumed small/large | Direct FALSIFIER |
|---|---|---|---|---|
| **CK/Alfvén carrier** `f_n=Λ_n v_A/2πR` | `ωR/v_A`, aspect `r_min/R`, BC | geometry, BC (`Λ_n`) | — | measure `f_1`; if `f_1 ≠ Λ_1 v_A/2πR` at the measured `v_A`, or the comb is harmonic (not `1:1.72:2.43`), the CK identification fails |
| **Single-fluid vs Hall** | `k d_i`, `ω/ω_ci`, `ν/ω` | β, geometry | `k d_i≪1`, `ω/ω_ci≪1` | look for **Hall/cyclotron sidebands**: if spectrum splits at `ω_ci` or scales with `k d_i`, single-fluid MHD is falsified |
| **Single-Beltrami-scale** | `k d_i`, `k d_e` | single `λ` | `k d_i≪1` **or** `k d_e≪1` | if two-fluid skin terms shift the eigenvalue (`Λ` moves with `d_i/R`), the single-scale Beltrami closure breaks |
| **Huygens reflection suppression** | `a/λ`, `Z_s/Z₀`, `p/(ε₀Z₀m)` | `Π_LC` (tuned) | `a/λ≪1` | scan frequency; **no `S₁₁` minimum** at the predicted `Π_LC=1`, or minimum absent when `p/(ε₀Z₀m)≠1`, falsifies Kerker balance |
| **Dark resonator** | multipole-cancellation groups (`p`, `m`, quadrupoles) | drive | radiative multipoles cancel | measured **radiated power / Q** far from the anapole floor `≲(kR)⁵` falsifies the dark-mode claim |
| **Plasma loading** | `ω/ω_pe`, `ν/ω`, `λ_D/R` | geometry | `λ_D/R≪1`, `ν/ω≪1` | **resonance shift vs measured `n_e`**: if the observed shift ≠ `ω_pe(n_e)` scaling, the loading model is wrong |
| **Proposed beat** | `Δω/ω`, aspect `ε`, drive | carrier `ωR/v_A` | `Δω/ω≪1` | beat must scale **linearly in aspect** (`Δλ ∝ ε`, `f_b/f_c≈7%`); a different scaling, or `Δω` independent of `ε`, falsifies the doublet-splitting origin |

**Headline falsifiers (one line each):** (1) the carrier comb must be **inharmonic `1:1.72:2.43`** (a
harmonic comb kills the CK ball-mode reading); (2) **cyclotron/Hall sidebands** at `ω_ci` would falsify
single-fluid MHD and force the two-fluid `d_i/R` correction; (3) the Huygens **`S₁₁` minimum** must appear at
`Π_LC=1` with `p/(ε₀Z₀m)≈1`; (4) the beat must scale **linearly in aspect ratio** (`Δλ∝ε`).

---

## M7-6 — Dimensional ↔ dimensionless SIDE-BY-SIDE (the explanatory format)   [V/S/A per row]

The template for the whole explanatory build: **real-unit form | dimensionless-Pi form | named group**.

| FTGB relation | Real-unit form | Dimensionless-Pi form | Pi-group / tier |
|---|---|---|---|
| density spine | `ρ = κ (A·B)` (`κ` carries units, `[κ]=kg·s/m⁵·…`) | `ρ/ρ₀ = (A·B)/(A₀·B₀)` | helicity-density ratio; `κ`=dimensional prefactor Pi cannot fix — **[S/A]** |
| mass–whirl | `m = ħ ω_C / c²` | `q = 1/α` (dimensionless whirl-number) | `ħω/mc²` (rest-frame closure); `q=1/α` **[QWM framework]** |
| force-free field | `∇×B = λ B` | `Λ_1 = λ₁R = 4.4934` (`tan x=x`) | Alfvén-Mach at resonance; **[V]** the root, **[V/S]** geometry-dep |
| carrier ladder | `f_n = Λ_n v_A/(2πR)` | `Λ_n = ω_n R/v_A = f_n/f_A` | `Π_A = ωR/v_A`; **[V]** comb `121/208/294 kHz` |
| beat | `f_b = c_CK ε v_A/(2πR)` | `Δω/ω = f_b/f_c ≈ 7%` (`Δλ=0.2806`) | `Δω/ω` + aspect `ε`; **[V]** (FreeFEM), linear in `ε` |
| swimmer / glide speed | `v = √(2 U_s/μ_eff)` | `v/v_A = √(2 U_s/(μ_eff v_A²))` | energy-per-inertia ratio; **[S]** |

Each right-hand column is a **claim the experiment can test directly** (a number of order 1 or a measured
ratio); each `κ`/`μ_eff`/`c_CK` prefactor is a **dimensional constant Pi theory is silent about** — it must
come from the mechanism (M2/M4/M6), a calibration, or measurement.

---

## M7-7 — LIMITS (stated prominently, again)   [V]

Buckingham Pi theory **does NOT**:
1. **pick the variables** — omit a relevant one and you get the wrong groups (garbage-in);
2. **identify the mechanism** — `ωR/v_A` says "Alfvénic," not "*because* of a Beltrami eigenmode";
3. **derive the function `f`** — it gives `Φ(Π_i)=0`, never the shape of `Φ`;
4. **fix the O(1) constant** — `Λ_1=4.4934` comes from `tan x=x` (a boundary problem), **not** from Pi;
5. **establish stability** — a group can be "allowed" and the state still be dynamically unstable;
6. **validate extrapolation** across a regime transition (laminar→turbulent, collisionless→collisional):
   the *same* `N_Π` can hide a change of governing `f`.

**Concrete FTGB caution.** A "clean four-anchor law" `{B, n, R, m_i}` giving `f = Λ v_A/2πR` is a genuine
scaling skeleton — but it is **incomplete** if the object actually depends on `T_e` (β), `ν_e`/`η` (Lundquist
`S`, resistive damping), `d_i/R` and `d_e/R` (two-fluid/Hall), `λ_D/R` (quasineutrality), or a sheath
thickness. Those are the very groups the four-anchor set **drops**. Pi theory's honest verdict: the four
anchors fix the *scale* `v_A/R`; the *number* `Λ` and its *corrections* live in the plasma/loss groups of
§M7-3 and must be computed or measured, not assumed. **Use Pi as a claim-audit tool, not a theory generator.**

---

## Per-claim index (M7)
| # | Claim | Tier | Repro check |
|---|---|---|---|
| M7-1 | Theorem: `N_Π=n−r` from `ker D`; rank≠symbol count; base-choice invariance | [credited]+[V] | invariance check (SI-`I` vs charge-`Q` bases → same rank, same groups) |
| M7-2 | Force-free matrix: `n=6,r=4,N_Π=2` → `{ωR/v_A, nR³}`; `Λ_1=4.4934` | [V] | rank/nullspace; `tan x=x` root; carrier comb |
| M7-3 | Plasma matrix: `n=9,r=4,N_Π=5`; control-param map; `v_A=ω_ci d_i` | [V]+[credited] | rank/nullspace; carrier = product of two groups |
| M7-4 | Metasurface matrix: `n=8,r=3,N_Π=5`; Kerker group dimensionless | [V]+[credited] | rank/nullspace; `p/(ε₀Z₀m)` dimensionality |
| M7-5 | Claim-audit + falsifier table | [V]-structure / [S]-claims | groups from M7-2..4; falsifiers = which group to vary |
| M7-6 | Dimensional↔dimensionless side-by-side format | [V/S/A] per row | each row's group from M7-2..4 |
| M7-7 | Limits: allowed scaling only (no `f`, constant, mechanism, stability) | [V] | — (statement of scope) |

## Reproducible-calculation coverage (M7)
- `frontier_calcs/toolkit_adv07_buckingham_pi.py` (numpy + sympy exact + scipy; ASCII, `PYTHONIOENCODING=utf-8`)
  → `toolkit_adv07_buckingham_pi_OUT.txt`. Ran clean; all checks resolved:
  - Matrix 1: `n=6, r=4, N_Π=2`; proposed `{ωR/v_A, nR³}` = **COMPLETE BASIS**.
  - Matrix 2: `n=9, r=4, N_Π=5`; proposed `{β, ω/ω_ci, d_i/R, λ_D/R, nR³}` = **COMPLETE BASIS**;
    `ωR/v_A=(ω/ω_ci)(R/d_i)` shown derived.
  - Matrix 3: `n=8, r=3, N_Π=5` (the `I=−2M` rank drop); proposed
    `{f0√(LC), a/λ, t/a, t/δ, ωL/Z₀}` = **COMPLETE BASIS**; Kerker `p/(ε₀Z₀m)` dimensionless.
  - Invariance: SI-`I` vs charge-`Q` base → rank 4 both; groups identical. **PASS.**
  - `Λ_1 = 4.493409` from `tan x=x` (first six roots; inharmonic ratios `1,1.719,2.427,…`). **PASS.**
  - Carrier comb `f_n = 121.2, 208.3, 294.0, … kHz` at `v_A=2.033×10⁴`, `R=0.12 m`; anchor `v_A` recompute
    `2.031×10⁴ m/s`. **PASS.**

Cross-links: `MATH_TOOLKIT_BASE.md`, `foundation/30_CANONICAL_NUMBERS.md` (§A anchors, §C `c_CK`, §I comb),
`project_ftgb_maximal_connected_theory_frame.md`, `project_ftgb_open_problems_and_negatives.md` (the open
plasma/loss groups this module exposes). Citation: Buckingham 1914. Method-only note: Storti *Quinta Essentia*
**[UNASSESSED/fringe]**.
