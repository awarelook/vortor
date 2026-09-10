# MATH TOOLKIT BASE -- the shared foundational mathematics behind the FTGB toolkit

The foundation the eight advanced modules (M7-M14) rest on. Every advanced module cites this document
for its shared operators, its anchors, and its honesty discipline; those citations are load-bearing, so
the section identities below (`§1` Beltrami/CK, `§9` one-operator-three-readings + dual reading + K_PV +
topology, and the canonical-anchor block) are preserved verbatim in number and content. This is
**infrastructure documentation, one level below the papers** -- it carries the real mathematics the
toolkit imports, each claim tagged with what it is licensed to deliver, and it does not blur the line
between established physics, verified-in-project results, structural readings, and quarantined numerology.

## Tier legend (honesty discipline)
- **[V]** verified in-project by a named computation / a checked identity or dimensional reduction (script
  named where one exists), or a textbook identity checked here.
- **[credited]** established textbook / primary-source physics or mathematics we build on (cited).
- **[credited-convergence]** an established-physics reading the object *instantiates* (Madelung/Bohm/de
  Broglie) -- a convergence onto known physics, not a new claim.
- **[S]** structural / contingent: true given the stated frame (fixed geometry, a convention, a boundary
  condition, or a model), not a free-standing universal law.
- **[flag]** a numerical claim that does **not** follow from a clean closed-form (fit / full-numeric /
  numerical coincidence / open); named explicitly so it is **never** cited as derived.
- **[excised]** the `e^(-2/3)` screening factor and any kin -- kept **out** per the standing excision
  protocol (M11-4(v)).
- **No fabricated numbers.** Every value traces to the source, to a named in-project script, or to a
  standard credited constant.

> **Provenance.** Curated into the jewel from `03_paper/main_draft/MATH_TOOLKIT_BASE.md`; every claim
> carries its tier; numerology quarantined per the M11 / excision discipline.

> **The one firewall (read first).** This foundation carries **pure geometry / topology / field theory /
> plasma dynamics only**. No nuclear mechanism enters (no TGST/EVO/D4D content); **baryon number is
> conserved throughout**; the PV/`K_PV` polarizable-vacuum representation (§9c) is used **only** as a
> bookkeeping rewrite of the plasma's own Hall-MHD dielectric -- **no** vacuum-energy / gravity /
> propulsion mechanism is invoked (the PV-gravity levitation reading returned a clean NEGATIVE). Storti's
> EGM numerical outputs, `alpha`-from-geometry, particle radii, and `H0` are quarantined in the ledger
> below and in M11-4, never promoted here.

---

## Orientation -- one operator, three faces, one clock   [S / credited]

The whole object is **one Chandrasekhar-Kendall (Beltrami) curl eigenmode** (§1) read three ways and
breathing on one clock. The curl `∇×` on divergence-free fields is the single generator; `fields.py` /
`madelung.py` / `topology.py` are three faces of one object, not three objects (§9). The four axes it is
parameterized along -- nesting `N`, fold-number `f`, winding `(p,q)` with `Q_H = p·q`, and phase -- and
the beat clock `f_b = c_CK v_eff a / 2 pi R^2` are the program's organizing spine; only the *foundational*
operators, readings, anchors, and topological invariants are carried here. The cascade / triad / fold
machinery, the app layer, and the session-advance dynamics live in the parent tree and in M10-M14.

---

## §1 -- The Chandrasekhar-Kendall / Beltrami curl eigenproblem (force-free fields)   [credited / V]

**Governing equation.** `∇×B = λB`, with `B·n = 0` on the boundary -- the Chandrasekhar-Kendall
(force-free / Beltrami) eigenproblem `[credited: Chandrasekhar-Kendall 1957; Woltjer 1958]`. Force-free
means the current runs *parallel* to the field (`J = ∇×B = λB`, so `J×B = 0`, zero Lorentz force); the
field's own circulation is proportional to itself with the one scalar eigenvalue `λ`; `B·n = 0` = "no
field pierces the wall." This is the relaxed, minimum-energy magnetic state (§ helicity, below).

**Axisymmetric reduction.** Under axisymmetry the vector problem reduces to a scalar poloidal-flux equation
on the meridional cross-section (a disk of minor radius `a = eps·R` centred at `x = R` in cylindrical
`(x,y)`), `n` labelling the azimuthal twist:

```
n=0:   div( grad(psi) / x ) = -lambda^2 psi / x
n=1:   div( grad(psi) / x ) + psi / x^3 = -lambda^2 psi / x
```

with Dirichlet `psi = 0` on the boundary, discretized with P2 Lagrange elements and solved via FreeFEM's
`EigenValue()` (UMFPACK direct factorization, shift-invert Arnoldi). **Load-bearing convention [V].**
FreeFEM's own `ev[i]` returns `mu = lambda^2`, **not** `lambda` -- always recover the physical eigenvalue
as `lambda = sqrt(ev)`. Tier: operator + reduction **[credited]**; the `lambda = sqrt(ev)` convention
**[V]** (re-verified in `spectral_sweep.py` / `greenyer_frontier_cCK_general_eps_sweep.edp`).

**Toolkit module.** `toroidal_core/spectral_sweep.py` (`solve_point`, `sweep`, `mesh_convergence_check`,
`overlap_matrix`, `fit_power_law`, `solve_point_robin`). The near-degenerate doublet
`lambda_0(eps), lambda_1(eps)` this operator produces is the source of the Beat Law (§ anchors).

---

## §2 -- The toroidal metric   [credited]

The exact induced metric on a torus surface, major radius `R`, minor (tube) radius `a`:

```
ds^2 = a^2 dtheta^2 + (R + a cos theta)^2 dphi^2
```

Used directly (not decoratively): in the Hellmann-Feynman coordinate substitution `x = R(1+eps u)`,
`y = R eps v` that turns the domain-shape dependence on `eps` into explicit coefficient dependence of a
fixed-domain operator, and in the Laplace-Beltrami operator on the surface. The circumferential factor
`R + a cos theta` is largest at the outer rim (`theta = 0`) and smallest at the inner rim (`theta = pi`) --
the asymmetry that makes a torus a torus (not a cylinder) and the geometric source of the doublet split
that drives the Beat Law. **[credited].**

---

## §3 -- CK / Beltrami spherical eigenmodes: roots of `tan x = x`, and the carrier index   [credited / V / S]

On a sphere the force-free eigenproblem `∇×B = λB` has the Chandrasekhar-Kendall solutions built from a
scalar generating field satisfying `(∇^2 + lambda^2)psi = 0`, i.e. a spherical Bessel times a spherical
harmonic, `chi = f_l(lambda r) Y_lm(theta,phi)` (`chi = r B_r`), with toroidal partner
`T = lambda r chi / [l(l+1)]`:

```
B_r     = chi / r
B_theta = (1 / (r l(l+1))) d^2(r chi)/(dr dtheta) + (1 / (r sin theta)) dT/dphi
B_phi   = (1 / (r l(l+1) sin theta)) d^2(r chi)/(dr dphi) - (1/r) dT/dtheta
```

Verified exactly in-project by direct symbolic `curl(B) - lambda B = 0` for `(l,m) = (1,0), (2,0), (2,2),
(4,4)` **[V]** (`fields.py` sphere-limit + the general-`(l,m)` construction). The Dirichlet condition
`B_r = 0` at `r = R` fixes `lambda R` to a zero of the spherical Bessel function `j_l`:

- **lowest mode `l=1`:** `lambda R` = first nonzero root of **`tan x = x` ≈ 4.4934** -- the CK/Beltrami
  eigenvalue of the ball (a spheromak) `[credited]`. First six roots — **reproduced from scratch (bisection +
  mpmath, cross-checking the engine) by `results/verify/ck_eigenvalues_check.py` `[V]`** — `4.493409,
  7.725252, 10.904122, 14.066194, 17.220755, 20.371303`, with **inharmonic** ratios `1, 1.719, 2.427,
  3.130, 3.832, 4.534`.
- **higher `l`** (first `j_l` zeros, `l = 0..4`): `[3.14, 4.49, 5.76, 6.99, 8.18]`; e.g. `Z_21 =
  5.76345919689455`, `Z_22 = 9.095011330476655` (zeros of `j_2`); `l=4`: `8.182561452571242,
  11.70490715457039` (zeros of `j_4`). `[credited]`.

`lambda_1 R = 4.4934` is the model's **carrier index** (the anchor block below): with the canonical medium
anchors `v_A = 2.033e4 m/s`, `R = 0.12 m`, the roots give the CK carrier comb `f_n = 121.2, 208.3, 294.0,
... kHz` (reproduces `foundation/30_CANONICAL_NUMBERS.md` §I to the digit, and is shared with M7-2 / M9).

> **CORRECTIVE, stated plainly [V/S] (carried from M7-2).** `lambda_1 R = 4.4934` is the eigenvalue of the
> **ball/sphere** boundary problem **only** -- it is **NOT a universal constant**. For the actual toroidal /
> conical FTGB object the eigenvalue becomes a *function* of the object's own Pi-groups,
> `Lambda_n = Lambda_n(a/R, d_i/R, beta, S, ...)`; the FreeFEM torus eigensolve finds a carrier *split*
> `Dlambda = 0.2806` at `eps = 0.697`, not a single sphere value. Quoting `4.4934` for the torus is a
> sphere-geometry approximation. Tier: ball eigenvalue **[credited]**; "geometry-dependent, not universal"
> **[V/S]**.

---

## §3a -- S^3 curl spectral zeta and the analytic-torsion pi-power   [V / credited]

The curl (Beltrami `*d`) operator restricted to **coexact 1-forms of `S^3`** has eigenvalue `(n+1) = m`
(`m >= 1`) with multiplicity `n(n+2) = m^2 - 1`, so its spectral zeta is **exactly**

```
zeta_B(s) = sum_{m>=1} (m^2 - 1) m^{-s} = zeta(s-2) - zeta(s).
```

Hence the analytic-torsion derivative `zeta_B'(0) = zeta'(-2) - zeta'(0) = -zeta(3)/(4 pi^2) + (1/2)
ln(2 pi)`, and the **quadratic (Casimir, `m^2`) coefficient is `zeta'(-2) = -zeta(3)/(4 pi^2)`** -- the
`pi^2` **structurally mandatory** via the functional-equation ladder `zeta'(-2n) = (-1)^n (2n)!
zeta(2n+1) / (2^{2n+1} pi^{2n})`. Therefore `omega_3 = zeta(3)/(4 pi^2)` is the genuine `S^3` `n^2`
analytic-torsion coefficient `[credited: Ray-Singer 1971]`, whereas the "pure" `zeta(3)/12 =
zeta(3)·(-zeta(-1))` is a **product of zeta VALUES** -- a categorically different object (the higher-shell
`n^2` derivatives are `zeta'(-4) ~ zeta(5)/pi^4`, `zeta'(-8) ~ zeta(9)/pi^8`, never `zeta(3)`). **[V]**
(`results/verify/curl_spectral_zeta_pi_power_check.py`, mpmath dps=40: identity checked at `s=4`;
`zeta'(-2)` matched to `1e-25`; full `zeta_B'(0)` to `1e-20`). This resolves the M13-10 "pi-power anomaly"
as a **category error** (not a normalization choice) in favor of the `pi^2` forms; it does **NOT** validate
the TUFT lepton-mass-tower fit, which stays **`[preprint-claim]`** at M13. **FIREWALL:** a spectral-geometry
identity only; no mass value is promoted here (the `zeta(3)/4pi^2` mass chain remains quarantined in the
ledger / M13).

---

## §4 -- Helicity, Woltjer-Taylor relaxation, and the force-free variational principle   [credited / V]

**Magnetic helicity.** `H = integral A·B dV` (`B = curl A`) -- the field-line linking / topological charge
of the magnetic field `[credited: Woltjer 1958; Moffatt 1969]`. For closed flux tubes `H = 2 Phi_1 Phi_2
Lk` with `Lk` the Gauss linking number; the ribbon decomposition `Lk = Tw + Wr` (twist + writhe) is the
Calugareanu-White-Fuller theorem `[credited]`.

**The force-free state is the constrained energy minimum.** Woltjer's variational principle: minimize the
magnetic energy `W` at fixed helicity `H`,

```
delta( W - (lambda/2) H ) = 0   ==>   curl B = lambda B
```

so the Beltrami/CK state is the minimum-energy field at fixed helicity and `lambda` is the Lagrange
multiplier `[credited: Woltjer 1958]`. **Taylor relaxation:** under small resistivity, energy decays
faster than helicity (selective decay), so a turbulent plasma relaxes to this single-`lambda` Beltrami
state while conserving total `H` -- the Woltjer-Taylor relaxed state `[credited: Taylor 1974]`.

**The helicity-eigenvalue identity [V, exact].** For a force-free field `A = B/lambda`, so `A·B = B^2 /
lambda` and

```
H = integral A·B dV = 2 W / lambda
```

tying the bulk linking to the single eigenvalue -- **VERIFIED exact in-project**; the CK state **saturates**
the corresponding helicity bound. Its gauge freedom is a **pure boundary term** `Delta H = closed-integral
chi (B·n) dS` (Berger-Field 1984): flux-closed => `Delta H = 0` (gauge-invariant), verified numerically on
an ABC field **[V]**.

---

## §4a -- Coupled-enstrophy Lyapunov functional for Hall-MHD at Pm != 1   [V / V-cond]

The canonical Hall enstrophy `Z = (1/2)‖Omega‖^2`, `Omega = B + d_i omega`, has an **indefinite**
dissipation away from `Pm = nu/eta = 1` (`det M = -d_i^2 (eta-nu)^2 / 4 <= 0`) -- but that obstruction is a
property of the **mixed canonical variable, not the physics**. In the natural coupled functional of the
*individual* curls,

```
L   = (1/2)‖omega‖^2 + kappa d_i^2 (1/2)‖J‖^2 ,     omega = curl v ,  J = curl B
D_L = nu‖grad omega‖^2 + kappa d_i^2 eta‖grad J‖^2   (DIAGONAL; det = nu·kappa d_i^2 eta > 0 at ANY Pm)
```

each field is diffused by its **own** coefficient, so the dissipation is diagonal and coercive at **every**
`Pm`; there is no cross term to make it indefinite. `L` strictly **controls** the canonical enstrophy `Z`
(via Poincare), while `Z` does **not** control `L` (take `B = -d_i omega => Omega ~ 0`, `Z ~ 0` while
`‖omega‖,‖J‖ = O(1)`) -- so `L` is the correct (`H^1`-of-the-pair) regularity functional. Near the
single-`lambda` **double-Beltrami** relaxed state (`v ‖ omega`, `J ‖ B`) `[credited: Mahajan-Yoshida 1998]`
the fluid Lamb production `S_om` and the Lorentz cross-term `Lambda` vanish **quadratically** (the Woltjer
constrained minimum is a variational critical point, §4). The one delicate top-order term, the Hall current
production `H_B = -d_i integral (curl J)·curl(J x B)`, vanishes **identically** on a constant-`lambda`
Beltrami field (`J x B = 0`) and is absorbed into `eta‖grad J‖^2` under a single explicit **Hall smallness
`d_i‖B‖_inf <~ eta`** (a Lundquist / small-data condition, matching Chae-Degond-Liu 2014 -- **NOT** a
Prandtl condition). **This removes `Pm = 1` as a hypothesis.** Tier: the three structural facts (coercivity
at any `Pm`; quadratic production suppression at the relaxed state; the linear `d_i‖B‖_inf/eta` Hall
absorbability) are **[V]** (`results/verify/hallmhd_coupled_lyapunov_check.py`, `Pm in {1/4,1/2,1,2,4}`); the
assembled regularity bound is **[V]-conditional** (a-priori deviation + Hall-smallness hypotheses, exactly as
the R2 / `Pm=1` theorems). **Unconditional large-data `Pm != 1` stays open** (= the open 3D Hall-MHD
problem). Full note: `results/R3_PM_NE_1_COUPLED_LYAPUNOV_2026-09-10.md`. This is the **same single-`lambda`
Woltjer-Taylor structure** (§4) that makes the carrier comb single-chirality -- the Hall lift and the
carrier coherence are one physics read twice.

---

## §9 -- One operator, three readings: the dual reading, K_PV, and the topology   [the load-bearing anchor]

*This is the section M9 cites as "§9 one operator, three readings" / the dual reading, M10 cites as "K_PV
polarizable vacuum, topology sec.9", and M14 cites as "Beltrami/helicity, topology sec." All three resolve
here.*

### §9a -- One curl operator, three readings   [credited / S]

The curl `∇×` on divergence-free fields is the common generator; three established wave theories are the
same operator read in three variables:

```
EM / photon :  i d_t F = c curl F ,   F = E + i c B    (Riemann-Silberstein; Bialynicki-Birula photon wavefn)
QM / matter :  psi = sqrt(rho) e^{iS/hbar} ,  v = grad S / m         (Madelung quantum hydrodynamics)
MHD / plasma:  curl B = lambda B                                     (force-free CK = Moffatt vortex)
```

Each reading is **[credited]** established physics. The claim that they **coincide on the toroidal Beltrami
eigenmode** is **[S]** -- a structural convergence, verified on the project's own eigenmode, not a new law.

### §9b -- The dual reading: probability vs flow; field <-> matter wave   [S / credited-convergence]

The single wave `psi = A e^{iS/hbar}` is read two ways:

- **probability:** `rho = |psi|^2 = A^2` is a probability density (Born rule), `S/hbar` the phase.
- **hydrodynamic flow:** `rho = A^2` is a fluid mass density and `p = grad S` the flow momentum
  (`v = grad S / m`) -- the Madelung/Bohm quantum-hydrodynamic form, with quantum potential
  `Q = -(hbar^2 / 2m) (nabla^2 A)/A`.

and the **field <-> matter-wave** duality: the same object read as a classical field and as a de Broglie
matter wave. **Tier: [S] / [credited-convergence].** Madelung (1927), Bohm (1952) and de Broglie (1924) are
established; the object *instantiates their convergence* -- an identity of readings, **not** a promoted
FTGB claim. (`madelung.py`, `quantum_hydrodynamics.py`, `quantum_ring.py` carry the `rho, S` decomposition,
the general 1D Madelung/Bohm quantum potential, and the genuine `hbar`-dependent particle-on-a-ring tie-in
kept deliberately separate from the classical field.)

**The medium the flow lives in.** Reducing the QHD gradient energy to a log-nonlinear Schrodinger closure
`i d_t psi = -(hbar^2/2m) nabla^2 psi - b ln(rho) psi` (Bialynicki-Birula-Mycielski) gives an acoustic
sound-speed `c_s^2 = -b < 0`, so the medium supports **breathing lumps (gaussons), not travelling waves** --
"heartbeat, not flywheel." Switch-on is the Stuart-Landau law `A-dot = (mu + i w_0) A - (b_r + i b_i)
|A|^2 A`, with onset frequency `w_0` = the linear Beat-Law eigenfrequency. `[credited]` for the log-NLS and
Stuart-Landau forms; **[S]** for the `c_s^2 < 0` breathing-medium reading.

### §9c -- K_PV polarizable-vacuum (Alfven-dielectric) representation   [credited / V] + firewall

The wave speed is read as the refractive index of a polarizable medium:

```
v_eff = c / sqrt(eps_r mu_r) = v_A ,   eps_r = c^2 / v_A^2 ,  mu_r ~ 1
n = sqrt(eps_r mu_r)  sets the beat frequency ;  Z = Z_0 sqrt(mu_r / eps_r)  sets the coupling
```

verified exactly in-project **[V]**. This is the same object as Puthoff's polarizable-vacuum index `K_PV`
(`c_eff = c / sqrt(K_PV)`) `[credited: Puthoff 1999, gr-qc/9909037]` -- **but here `K_PV` is used ONLY as a
bookkeeping rewrite of the plasma's own Hall-MHD dielectric.** **FIREWALL (load-bearing):** no vacuum-energy
/ gravity / propulsion mechanism is invoked; the PV-gravity levitation reading returned a clean **NEGATIVE**
(elliptic `c_s^2 < 0`, `K_PV -> Phi ~ 1e4 c^2` absurd). Any frequency/scale dependence of a vacuum index is
the running-coupling-as-dielectric duality `K_PV(q^2) = alpha(0)/alpha(q^2)` -- textbook QED, homed in the
RG dielectric-flow module (M10-5), where the IR value is an integration constant, **not** forced. Storti's
EGM numerical outputs are quarantined at M11-4. Tier: PV/Alfven-dielectric rewrite **[credited]/[V]**; any
`K_PV`-derived *value* **[flag]** (see ledger).

### §9d -- Topological charge: Hopf linking, Chern number, pi_1/pi_3   [V / credited]

- **Hopf linking `Q_H = p·q`** (poloidal (X) toroidal winding), computed via exact `S^3` Hopf fibers + the
  Gauss linking integral (`topology.py`); the object carries `Q_H = 1`. **[V].**
- **Wave-mode Chern number `C = +-2`** of the Beltrami eigenmode (Fukui-Hatsugai-Suzuki lattice Berry-flux,
  validated on the 2-level Weyl monopole `C = -+1`, grid-independent) **[V computed]** -- this is the
  **known** spin-1 photon-helicity value (Bliokh 2015; Palmerduca-Qin 2024): **recovered, not novel**
  `[credited]`.
- **pi_1 / pi_3 decoupling:** a Madelung phase slip changes the U(1) winding (`pi_1`, `Dw = -1`) but **not**
  the baryon/Hopf number (`pi_3`, `DB = 0`, a degree of the direction field). Classical topology, **not** a
  nuclear decay. **[V / credited]** (firewall-sharpening).
- **Topological persistence-protection:** the winding is conserved exactly (`1.000`, zero phase slips)
  through the deepest driven collapse (`min rho/rho_0 = 0.093`) -- topology protects the driven cycle's
  **existence** (not its period; the period follows Stuart-Landau). **[V].**

### §9e -- Holographic face: boundary encodes bulk   [S structural analogy only]

For fixed `lambda`, `curl B = lambda B` in a bounded domain has its entire interior determined by the
boundary normal flux `B·n` (Grad-Shafranov / Taylor state) -- "boundary encodes bulk" is a **theorem** here
`[credited]`. Independent force-free DOF are indexed by boundary surface harmonics `sum_{l=1}^{L}(2l+1) =
L(L+2) ~ L^2` (an area-law boundary count), not the volume `~L^3` **[V]**. **FIREWALL:** the holographic
principle is cited as a **STRUCTURAL analogy only** (the area-law of a boundary-value problem), **NOT**
AdS/CFT -- no gravity, no "entanglement-entropy = area". **[S].**

---

### §9f -- The Dirac bispinor structure is internal: Weyl pair, gamma_5 = theta_chi, C   [V / credited / S]

The `+/-lambda` Beltrami helicity branches **are the two Weyl chiralities.** The helical projectors
`P_+/- = (1/2)(u +/- curl u / |k|)` split any divergence-free field into the two chiralities, and a
single-`lambda` Beltrami is a **PURE** eigenstate (a `lambda>0` ABC field is 100% `P_+`, its mirror 100%
`P_-`; verified to `>0.999` energy fraction). The duality angle `theta_chi` acts as the **gamma_5 chiral
rotation**: for `u(theta) = cos theta·u_+ + sin theta·u_-` the helicity is `H(theta) = H_max cos 2theta`
(verified vs `cos 2theta` to `<2%`) -- zero at `45deg` (self-dual = **Majorana**), `+/-max` at `0/90deg`
(electron / positron). The `lambda -> -lambda` mirror swaps `P_+ <-> P_-` and flips helicity (`H_m/H_f = -1`
exact) -- **charge conjugation C**. With Hopf **spin-1/2** `[credited: Wilczek-Zee 1983; Finkelstein-
Rubinstein 1968]`, the Dirac bispinor structure is **INTERNAL** to the object, and `g = 2` is its
**minimal-coupling limit** `[credited: Ferrara-Porrati-Telegdi 1992; Weinberg natural-g]`: `g = 2 <=>` the
`U(1)` charge winding (`pi_1`) **locks** to the Hopf spin (`pi_3`) -- the "effectively elementary" limit (an
independent circulating charge gives `g = 1`; a composite such as the proton `g = 5.59` **breaks** the lock).
Since FTGB's `pi_1 / pi_3` are separately conserved (§9d), the locking is a **stated CONDITION**, not a fudge.
**[V]** the Weyl / gamma_5 / C algebra (`results/verify/g2_dirac_structure_check.py`); **[credited]** the
Hopf spin-1/2 and the FPT / Weinberg `g=2`-minimal-coupling theorem; **[S]** the `pi_1/pi_3` lock. This
**reduces the g=2 frontier to one internal criterion** (ties to the §9d chirality cluster and the computed
chirality / C / Majorana layer, `results/CHIRALITY_DUALITY_ASSESSMENT_2026-09-10.md`). It is a derivation of
what `g=2` **is** inside the theory and the exact residual condition -- **not** a proof of the lock.

---

## §11.0 -- Canonical anchors `{B, n_i, R, m_i}` and derived medium quantities   [measured / V / S]

*The anchor block M7 shares with `foundation/30_CANONICAL_NUMBERS.md` §A (anchors), §C (`c_CK`), §I (comb).
Four measured anchors + a fixed dimensionless geometry: zero free structural parameters, zero free scales.*

| symbol | value | role | tier |
|---|---|---|---|
| `B` | 20.6 mT | anchor -- field strength | measured |
| `n_i` | 1.7e19 m^-3 | anchor -- ion density | measured |
| `R` | 0.12 m | anchor -- object size | measured |
| `m_i` | 4.816e-26 kg (29 amu) | anchor -- ion mass | measured |
| `v_A = B/sqrt(mu_0 n_i m_i) = sqrt(2 b_eff/m_i)` | 2.033e4 m/s | Alfven / effective wave speed | **[V]** |
| `b_eff = 1.047 · B^2/(2 mu_0 n_i)` | 1.042e-17 J | magnetic energy per ion | **[V]** |
| `hbar_eff = kappa_2 m_i v_A R` | 6.16e-23 J·s (~5.84e11 hbar) | **emergent** action (`∝R`), NOT literal Planck hbar | **[V]** |
| `sigma_0 = hbar_eff/(2 sqrt(b_eff m_i))` | 0.0435 m = 0.362 R | coherence / gausson length | **[V]** |
| `u_0 = B^2/(2 mu_0)` | 169.1 J/m^3 | magnetic energy density | **[V]** |
| `U_mag = u_0 · (4/3) pi R^3` | 1.22 J | object magnetic energy | **[V]** |
| `lambda_1 R` | 4.4934 | eigenmode carrier index (§3, ball value) | **[credited]/[S]** |
| `c_CK = c_CK(1/phi)` | 0.2234 | Beat-Law coefficient at `eps = 1/phi` | **[V]** fixed geometry |
| `eps = 1/phi` | 0.618 | golden aspect `a/R` | **[S]** selection |
| `sigma_0/R` | 0.362 | coherence fraction | **[V]** fixed geometry |
| `kappa_2 = (Gamma_dim/R_dim)^2` | 0.524 | chi-field stiffness | **[V]** fixed geometry |
| `kappa_4 = kappa_2 · I_2/I_4` | 0.181 | Skyrme/quartic stiffness, `sigma_0`-regularized | **[V]** fixed geometry |

**Load-bearing reconciliations [V]:** `kappa_2 = b_eff/(m_i v_A^2) = (c_s/v_A)^2 = 0.524`; `f_b/f_Omega =
c_CK·eps = 0.138`; `f_c/f_Omega = lambda_1 R = 4.4934`; `f_b/f_c = c_CK eps / lambda_1 R = 3.1%`.

**The one frequency ladder [V].** One Alfvenic clock `Omega = v_A/R = 1.694e5 s^-1` sets three commensurate
rhythms:

```
{ f_Omega, f_c, f_b } = (v_A / 2 pi R) · { 1, lambda_1 R, c_CK eps } = { 27.0, 121, 3.7 } kHz
```

the winding/rotation rate, the eigenmode carrier (`= lambda_1 R x`), and the slow beat (`= c_CK eps x`); the
higher-mode CK carrier comb `{121, 208, 294} kHz` (ratios `1 : 1.72 : 2.43`) is catalogued in
`30_CANONICAL_NUMBERS.md` §I (shared with M7/M9).

**Honesty notes on the anchor block (preserved from the source's own corrections):**
- `hbar_eff` is an **emergent / effective** action (`∝R`, per-ion `m_i`), round-trip verified -- **explicitly
  NOT** a literal-Planck-`hbar` calibration (the source's own 2026-08-08 correction). **[V] emergent.**
- `b_eff = B^2/(2 mu_0 n_i)` and `hbar_eff` are **determined by physical scales, not two independent fits**
  (object size cancels); the falsifiable form is `b_eff = B^2/2 mu_0 n_i` on a second system. **[V].**
- `c_CK(1/phi) = 0.2234` is a **FreeFEM-computed** doublet coefficient at `eps = 1/phi` **[V, FE]**; the
  large-aspect closed-form limit `c_CK(eps -> 0) = 1/(2 j_{0,1}) = 0.20792` matches the sweep to 0.04%
  **[V, closed-form]**.
- `eps = 1/phi` is a **structural selection [S]**, over-determined three convergent ways -- resonance
  `N^2 = N+1 => N = phi` **[V]**, fold-packing `sin(pi/f) = 1/phi` **[V]**, and the KAM most-irrational
  (noble) torus **[credited]** -- **not** a fit; the Hall-regime operating aspect `eps ~ 0.77` is the flagged
  paired alternative **[flag/X]** (`(a/R, comb) = (0.77, phi)` resonance-locked vs `(0.618, phi^2)` rigid).

---

## Quarantine ledger -- numerology kept OUT / flagged   [flag / excised]

Per the M11-4 / M10-5 / M8 discipline, the following are **never** promoted here as derived. If a source
line states one as a "result", it is demoted exactly as M11-4 does.

- **`e^(-2/3)` screening factor and any kin** -- **[excised]** (standing excision protocol, M11-4(v)).
  `e^(-2/3) = 0.513` does not even produce the ~2.3% correction it was invoked for; it stays out.
- **`alpha` from toroidal winding (140.2) / `~137`** -- **[flag]**. The `140.2 vs 137.036` (2.3%) gap is an
  **open problem**, not a screening "derivation"; `~137` is a flagged coincidence (`137` is prime; genericity
  -denominator controls show the near-misses are generic, M10-5). Never cited as FTGB-derived.
- **`alpha` as an energy-imbalance of the confined object -- settled-negative (value), frontier reduced.**
  On the correctly-specified object the free photon (Hopf-Ranada **null** EM knot, Bateman construction) is
  **exactly energy-balanced** (`U_E/U_B = 1`, `E·B = 0`, `|E|=|B|`), so it carries no `alpha`-sized
  imbalance; the electron standing-wave **resonator** in the non-dispersive canonical medium (§9c,
  `eps_r = (c/v_A)^2 = const`) has zero mode imbalance (equipartition) and zero dispersive imbalance, and the
  point-defect self-energy gives `U_E/mc^2 = alpha` **only by inserting `e`** (`= r_e/lambda_C = alpha`
  restated -- circular). `alpha` moreover **runs** (`K_PV(q^2) = alpha(0)/alpha(q^2)`, §9c); `1/137.036` is
  only its IR / Thomson anchor. Topology quantizes charge (integer Hopf / winding) but **not** its magnitude;
  the frontier is thereby reduced to **one** quantity -- the running coupling's anchor = the charge
  **magnitude** `e`. **[V] baselines / settled-negative (value)** (`results/verify/confined_photon_null_
  balance_check.py`, `alpha_resonator_imbalance_check.py`) `[credited: Ranada 1989/1990, null EM knots]`.
- **Particle RMS charge radii to ~0.01%** -- **[flag]**, full-numeric / fit, not a clean closed form; the
  clean forms miss by 10^3-10^4 (M11-4(ii)). The honest Compton-scale energy-balance radius (`r_eq ~ 0.42
  lambda_C`) is the reasonable part; the *precision* claim is flagged.
- **`H0 = 67.08 km/s/Mpc` from a cosmic cut-off** -- **[flag]**, order-of-magnitude + unmotivated fudge
  (M11-4(iv)).
- **Lepton mass ratios (`m_mu/m_e`, `m_tau/m_e` to ~%) via `zeta(3)/4pi^2`** -- carried in **M13** (Nielsen
  TUFT mass tower) at its own `[V core] / [A,S sub-lemma]` tiers; **not** promoted into this foundation.

---

## What is deliberately NOT in this foundation

Kept out of the foundation (they live in the parent tree and the advanced modules), so promoting the base
never implies these are as settled as §§1-9:

- **Session-advance dynamics** -- rotational superradiance / black-hole-bomb gain, the two-mode swimmer
  (polarize / driven-glide), and the beat-clocked fissility cascade (source §11.5-11.8). Real, but
  dynamics-and-value-contingent (`[V]/[X]`), not foundation.
- **The division-algebra Hopf gauge tower and the lepton mass law** (source §12) -- M12 / M13 territory;
  charge-from-`Z_3`-winding, `Q = (1/3) sum n_i`, and the `zeta(3)/4pi^2` chain are tiered there.
- **The scale-discrimination table and domain transforms** (source §13) -- the `BR = const` scale-covariance
  and skin-depth / coherence-length disambiguation; an operating manual, not a foundational operator.
- **Maxwell cavity / vector H(curl) eigensolver, and the free-parameter reservoir-dynamics model** -- not
  built / deliberately exploratory (source §7).
- **Any retracted nuclear mechanism** (TGST/EVO/D4D) -- standing exclusion; `E_fm = 2.5 MeV` stays retracted.

---

## Per-claim tier index (base)

| # | Claim | Tier | Trace |
|---|---|---|---|
| B-1 | `curl B = lambda B`, `B·n=0`; axisymmetric poloidal-flux reduction (`n=0,1`) | [credited] | §1; CK 1957 / Woltjer 1958 |
| B-2 | FreeFEM `ev = lambda^2`, recover `lambda = sqrt(ev)` | [V] | §1; `spectral_sweep.py` |
| B-3 | Toroidal metric `ds^2 = a^2 dth^2 + (R+a cos th)^2 dph^2` | [credited] | §2 |
| B-4 | `l=1` ball CK eigenvalue = first root of `tan x = x` = 4.4934; `j_l` zeros; `(l,m)` curl-checked | [credited]/[V] | §3; M7-2 |
| B-5 | `lambda_1 R = 4.4934` is the BALL value only; torus `Lambda_n(a/R, d_i/R, beta, S)` | [V/S] | §3 corrective; M7-2 |
| B-6 | `H = integral A·B dV`; `Lk = Tw + Wr`; Woltjer `delta(W-(lambda/2)H)=0 => curl B=lambda B` | [credited] | §4; Woltjer 58 / Taylor 74 |
| B-7 | Force-free `H = 2W/lambda` (exact); CK saturates the bound; gauge `DH` a pure boundary term | [V] | §4; Berger-Field 84 |
| B-8 | One curl operator, three readings (RS photon / Madelung / force-free MHD) coincide on the eigenmode | [credited]/[S] | §9a |
| B-9 | Dual reading `psi = A e^{iS/hbar}`: probability vs flow; field <-> matter wave | [S]/[credited-convergence] | §9b; Madelung 27 / Bohm 52 / de Broglie 24 |
| B-10 | log-NLS closure; `c_s^2 = -b < 0` (breathing medium); Stuart-Landau onset `w_0` = beat | [credited]/[S] | §9b |
| B-11 | `K_PV` = Alfven dielectric `v_eff = c/sqrt(eps_r mu_r) = v_A`; plasma's own Hall-MHD index only | [credited]/[V] | §9c; Puthoff 99 |
| B-12 | PV-gravity / propulsion reading = NEGATIVE; `K_PV`-derived VALUES flagged | [V neg]/[flag] | §9c; ledger |
| B-13 | Hopf linking `Q_H = p·q = 1` (S^3 fibers + Gauss integral) | [V] | §9d; `topology.py` |
| B-14 | Wave-mode Chern `C = +-2` = known photon helicity (recovered, not novel) | [V]/[credited] | §9d; Bliokh 15 / Palmerduca-Qin 24 |
| B-15 | `pi_1/pi_3` decoupling (`Dw=-1`, `DB=0`); winding persistence through collapse | [V/credited] | §9d |
| B-16 | Holographic "boundary encodes bulk" area-law `L(L+2)~L^2`; STRUCTURAL analogy, not AdS/CFT | [credited]/[S] | §9e |
| B-17 | Anchors `{B, n_i, R, m_i}` + derived `v_A, b_eff, hbar_eff, sigma_0, u_0, U_mag`; ladder `{27,121,3.7} kHz` | measured/[V] | §11.0; `30_CANONICAL_NUMBERS.md` §A/§I |
| B-18 | `hbar_eff` EMERGENT (not literal Planck hbar); `b_eff` a medium property, not a fit | [V] | §11.0 (source corrections) |
| B-19 | `c_CK(1/phi)=0.2234` [FE]; `c_CK(eps->0)=1/(2 j_{0,1})=0.20792` [closed form] | [V] | §11.0 |
| B-20 | `eps = 1/phi` over-determined (resonance / packing / KAM); `eps~0.77` Hall alternative flagged | [S]/[flag] | §11.0 |
| B-21 | `e^(-2/3)` excised; `alpha`/`~137`, 0.01% radii, `H0` flagged; lepton-mass law -> M13 | [excised]/[flag] | ledger; M11-4 |
| B-22 | Dirac bispinor internal: `+/-lambda` = Weyl pair (`P_+/-` pure), `theta_chi = gamma_5` (`H=H_max cos2theta`), mirror = C; `g=2` = minimal-coupling limit <=> `pi_1` locks to `pi_3` | [V]/[credited]/[S] | §9f; `g2_dirac_structure_check.py`; WZ 83 / FR 68 / FPT 92 / Weinberg |
| B-23 | Coupled Hall Lyapunov `L=(1/2)‖om‖^2+kappa d_i^2(1/2)‖J‖^2`: diagonal coercive `D_L` at ANY `Pm` (removes `Pm=1`); prod. vanish quadratically at double-Beltrami; residual = Hall smallness `d_i‖B‖_inf<~eta` | [V]/[V-cond] | §4a; `hallmhd_coupled_lyapunov_check.py`; Mahajan-Yoshida 98 / Chae-Degond-Liu 14 |
| B-24 | `S^3` curl spectral zeta `zeta_B(s)=zeta(s-2)-zeta(s)`; `n^2` coeff `zeta'(-2)=-zeta(3)/4pi^2` (`pi^2` mandatory); `zeta(3)/12` a product of VALUES; resolves M13-10 (does NOT validate TUFT fit) | [V] | §3a; `curl_spectral_zeta_pi_power_check.py`; Ray-Singer 71 |
| B-25 | `alpha`: free photon null-balanced (`U_E/U_B=1`); resonator/medium imbalance = 0, defect = `r_e/lambda_C` (circular); `alpha` runs; frontier reduced to charge magnitude `e` | [V]/settled-neg (value) | ledger; `confined_photon_null_balance_check.py`, `alpha_resonator_imbalance_check.py`; Ranada 89/90 |

## References / provenance

Source (read in full): `03_paper/main_draft/MATH_TOOLKIT_BASE.md` (1119 lines; §§0-13). In-project traces:
`toroidal_core/` (`spectral_sweep.py`, `fields.py`, `madelung.py`, `topology.py`, `quantum_hydrodynamics.py`,
`quantum_ring.py`), `greenyer_frontier_cCK_general_eps_sweep.edp`, and the canonical block in
`foundation/30_CANONICAL_NUMBERS.md` (§A anchors, §C `c_CK`, §I comb). Established literature:
Chandrasekhar-Kendall 1957; Woltjer 1958; Taylor 1974; Moffatt 1969; Berger-Field 1984; Grad-Shafranov;
Calugareanu / White / Fuller (`Lk = Tw + Wr`); Madelung 1927; Bohm 1952; de Broglie 1924; Bialynicki-Birula
(Riemann-Silberstein photon wavefunction) and Bialynicki-Birula-Mycielski (log-NLS); Puthoff 1999
(gr-qc/9909037, PV representation of GR); Fukui-Hatsugai-Suzuki (lattice Chern number); Bliokh 2015;
Palmerduca-Qin 2024 (photon-helicity Chern `C = +-2`); Wilczek-Zee 1983 / Finkelstein-Rubinstein 1968
(soliton spin-statistics, §9f); Ferrara-Porrati-Telegdi 1992 & Weinberg (natural `g=2`, §9f); Mahajan-Yoshida
1998 (double-Beltrami, §4a); Chae-Degond-Liu 2014 (Hall-MHD small-data, §4a); Ray-Singer 1971 (analytic
torsion, §3a); Ranada 1989/1990 (null EM knots, ledger). Session-2026-09-10 verify scripts:
`results/verify/{g2_dirac_structure_check, hallmhd_coupled_lyapunov_check, curl_spectral_zeta_pi_power_check,
alpha_resonator_imbalance_check, confined_photon_null_balance_check}.py` and
`results/R3_PM_NE_1_COUPLED_LYAPUNOV_2026-09-10.md`. Cited by: M7 (anchors, `tan x = x`, comb),
M9 (§9 one-operator-three-readings / dual reading), M10 (`K_PV` polarizable vacuum, topology sec.9),
M11 (PV / excision protocol), M14 (Beltrami/helicity, topology sec.).

*Every number here traces to the source, a named in-project script, or a standard credited constant. No
FTGB physical claim is promoted above its tier; numerology is flagged or excised, never derived. ASCII apart
from standard math symbols.*
