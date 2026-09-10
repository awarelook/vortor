# TOOLKIT ADV — Module M13: NIELSEN TUFT MASS-TOWER & MIXING METHODS (Proca–Beltrami seed, ζ-valued exponent tower, knot/lens-space torsion, CKM/PMNS overlaps, Chern–Simons topological mass)

Part of the FTGB math toolkit (see `MATH_TOOLKIT_BASE.md`, `TOOLKIT_ADV_10_TOPOLOGICAL_SOLITON_METHODS_2026-09-08.md`).
This module is a **METHODS + COEFFICIENT-PRESERVATION pass** on Jennifer (Jenny Lorraine) Nielsen's Topological
Unified Field Theory (TUFT) mass-spectrum mathematics. It lifts the *reusable structure* — the mass-operator seed,
the ζ-valued exponent tower and every one of its coefficients, the knot/lens-space normalizations, the CKM/PMNS
overlap construction, and the Chern–Simons topological-mass machinery — out of the primary sources into one tiered,
cited place, so each piece can be re-applied without re-deriving it. It captures **how the tower is built and what
its numbers are**, quoting formulas verbatim. It does **not** endorse the preprint's fit-to-data claims; those are
tiered separately and honestly (M13-11). Every coefficient below is traced to a named source doc; nothing is fabricated.

**Primary sources integrated (read fully for this pass).**
- `NIELSEN_TUFT_MASS_COEFFICIENT_EXACT_FORM_2026-09-02.md` — the exact ζ-valued tower + all coefficients + π-power finding.
- `C9_MASS_TOWER_COEFFICIENT_VERIFICATION_2026-09-08.md` — the S⁹ coefficient C₉, arithmetic-verified to 30+ dps.
- `KERNEL_NIELSEN_MASS_MATRIX_ELEMENT_2026-09-02.md` — the `⋆d` mass operator (Thm 14), the (n+1) seed, the 6.1%/93.9% decomposition.
- `100pgCOMPLETE MATHEMATICAL COMPENDIUM FOR VORTEX TOPOLOGICAL UNIFICATION.md` — Proca–Beltrami axiom, Chern–Simons, CKM angles, neutrino suppression.
- `31newpgTopological Vortex Unified Field Theory … Framework.md` §II, §IX–XII — curl spectrum, popular mass formula, CKM `V_ij`/`J`, PMNS, CS₇.

**Established literature cited (per method):** Ray–Singer 1971; Nash–O'Connor 1995; Cheeger 1979 / Müller 1978
(analytic = Reidemeister torsion); Arnold–Khesin (curl spectrum); Atiyah–Patodi–Singer 1975 (η-invariant / spectral
asymmetry); Witten 1989 (Chern–Simons / Jones), Witten 1998 (AdS₇/CFT₆, hep-th/9812012); Cantarella–Kusner–Sullivan
2002 (ropelength); Woltjer 1958; PDG 2024. **The TUFT preprint itself** (Nielsen, PhilArchive 2024–2025; long
version `NielsenTUFT.pdf` 290 pp) is the *framework* source, **in peer review** — see the tier legend and M13-11.

> **THE ONE LIMIT, STATED UP FRONT.** Everything in this module is **[framework: Nielsen TUFT] / [S] scaffolding
> built on a bed of [credited] mathematics** — the Proca/Helmholtz correspondence, Ray–Singer analytic torsion,
> lens-space determinants, the curl/Beltrami spectrum, the Alexander polynomial `Δ(−1)`, and Chern–Simons theory are
> all genuine and cited; the *tower construction* that assembles them, and every *physical identification*
> (knot↔lepton, shell↔sector, overlap↔mixing), are the preprint's, not ours. **Only two classes of claim are
> [V]-in-project: (i) that the arithmetic reproduces** (given Nielsen's coefficients, the formula returns the numbers
> she states — the quark tower 6/6 to −0.000%, and the coefficient identities like `C₉=−0.15670774` and
> `ζ′(−2)=−ζ(3)/4π²` to 30+ dps); **and (ii) the internal-consistency findings below.** Two things are flagged
> PROMINENTLY and must travel with every use of this module: **(a) a documented π-power internal inconsistency** —
> the tower carries a *pure* `C₅=ζ(3)/12` (no π) for the n² term on S⁵/S⁹ but a π²-carrying `ω₃=ζ(3)/(4π²)`,
> `σ₅=ζ(3)/(16π²)`, `σ₉=ζ(3)/(8π²)` for the *same class* of Ray–Singer coefficient on S³ and in the torsion
> exponents — an **unresolved anomaly [anomaly]**, not a normalization choice; and **(b) the "zero-free-parameter,
> blind-fit-at-0.1σ, all-masses-recovered" claims are the PREPRINT's, in Round-2 review — [preprint-claim], NOT [V].**
> We fold the *structure and coefficients*; we mark the *fits* as unverified-here.

## Tier legend (honesty discipline)
- **[V]** verified in this project by a named computation / a checked identity (here: arithmetic reproduction of the
  formula and its coefficient identities ONLY — never the physical fit-to-data).
- **[credited]** established mathematics/physics we build on (textbook or primary-source, cited).
- **[framework: Nielsen TUFT]** the preprint's own construction, ansatz, or identification — asserted illustratively,
  standing on the TUFT-is-a-preprint caveat (Nielsen 2024–2025, in peer review); reproduced, not endorsed.
- **[S]** structural / cited-convergence or numerically-supported, not closed on our side.
- **[anomaly]** an internal inconsistency in the source, documented and flagged, NOT silently smoothed.
- **[preprint-claim]** a data-recovery / significance / "zero-parameter" claim made by the preprint and currently
  under peer review — reproduced here for completeness, explicitly **NOT** independently validated by us. NOT `[V]`.
- **[reject]** fabricated / refuted — named so it is never resurrected.

---

## M13-1 — THE MASS OPERATOR (Proca–Beltrami seed + `⋆d`, Nielsen Thm 14)   [credited seed / framework identification]

**WHAT.** The tower's *linear* seed is a genuine, cited spectral fact: on a compact 3-manifold the curl operator is
self-adjoint with discrete spectrum, and on `S³` its eigenvalues are `±(n+1)/R`. Nielsen promotes `⋆d` (curl, Hodge
`⋆d` on 1-forms) to the "mass operator," and the Proca–Beltrami correspondence converts a Beltrami eigenvalue into a
mass. **The seed `(n+1)` is credited; calling its eigenvalue a particle mass is the framework's identification.**

**MATH.** Proca–Beltrami correspondence (100pg Axiom 3; 31pg abstract pt.4), verbatim structure:
```
Beltrami:            ∇×B = λB
take curl, ∇·B=0:    ∇×(∇×B) = −∇²B = λ²B     ⇒   ∇²B + λ²B = 0      (Helmholtz)
static Proca:        ∇²A − (mc/ℏ)²A = 0        ⇒   identification  λ = mc/ℏ   (equivalently  m = ℏλ/c)
```
> *"Mass IS the curvature of the vortex knot. The Beltrami eigenvalue equals the inverse Compton wavelength."* (100pg)

Curl / Beltrami spectrum (31pg §II.C, credited to Arnold–Khesin, *Topological Methods in Hydrodynamics* §I.5):
```
Thm 2.3 (self-adjointness):  ∇× on V(M) is self-adjoint w.r.t. the L² inner product.
Thm 2.5 (S³ spectrum):       λ_n = ±(n+1)/R ,   dim E_{λ_n} = n(n+2) ,   n ∈ ℤ_{≥0}.
```
The mass operator, verbatim from `KERNEL_NIELSEN_MASS_MATRIX_ELEMENT` §1c (Nielsen Thm 14):
> the **unique self-adjoint + elliptic + SO(4)-equivariant first-order operator on coexact 1-forms of S³** — "this
> part is her cleanest, cited result" — with eigenvalue seed `(n+1)`.

**LOAD-BEARING CONSEQUENCE (in-project [V], honest limit).** `⋆d` is **linear**, so on its own eigenbasis
`⟨ψ_f | ⋆d | ψ_i⟩ = λ_i · δ_{fi}` — **strictly diagonal, zero off-diagonal**. A linear mass operator therefore
supplies **masses (eigenvalues) but no transition matrix element**; MEs require a *nonlinear* interaction the tower
does not contain (this is the firewall result of `KERNEL_NIELSEN_MASS_MATRIX_ELEMENT`, and it bounds what the tower
can ever deliver). **[credited]** for the `(n+1)` curl spectrum + self-adjointness + Proca/Helmholtz map;
**[framework: Nielsen TUFT]** for `⋆d`-as-mass-operator and the eigenvalue→mass identification; the
diagonal-only/zero-ME fact is **[V] rigorous**.

---

## M13-2 — THE QUARK MASS-TOWER (S⁵), COMPLETE, WITH EVERY COEFFICIENT   [framework tower / [V] arithmetic]

**WHAT.** The full S⁵ quark tower: an `(n+1)` seed times an exponential whose exponent is a graded sum of a linear
helicity term, a quadratic "Casimir/Ray–Singer" term, a triangular ζ(5) term, and a knot-torsion term, times a small
compression factor. Fold the *whole* structure and *all* coefficients; the fit is tiered in M13-11.

**MATH.** Verbatim (exact-form doc, TUFT p.57 eq 96–103; `× {2/3, n=1; 1, else}` in the task's shorthand):
```
m_{n,±} = Λ₅ (n+1) · exp( (a₅ ± λ_T(n)) n + C₅ n² + β₅ · n(n+1)/2 + σ₅ log τ(Kₙ) )
          × { 2/3, n=1 ; 1, n=2,3 }                                                  (eq 96)
```
with the boxed coefficients (transcribed from the page images), **quoted verbatim**:
```
C₅ = ζ(3)/12           ≈ 0.100171           (eq 87 = 99)   PURE, NO π      [grades n²]
β₅ = ζ(5)/(8π⁴)        ≈ 1.33064×10⁻³       (eq 100)       carries π⁴      [grades n(n+1)/2]
σ₅ = ζ(3)/(16π²)       ≈ 7.61211×10⁻³       (eq 101)       carries π²      [grades log τ(Kₙ)]
a₅ = exp(spectral₅/6)·√3·(2 + ζ(3)/(4π²)) ≈ 3.564112       (eq 98)         [grades n]
λ_T(n) = 2/π + (ζ(3)/(12π))(5/2 − n) ,  n=2,3              (eq 90 = 103)    [linear-n splitting]
Λ₅ = (2π/√3) v κ₅³                                          (eq 97)         [overall scale]
spectral₅ = (3ζ(5) + 5π²ζ(3))/(8π⁴)                                         [shell spectral input]
```
Level grading (verbatim, eq 96): `C₅` multiplies **n²** (quadratic Casimir growth); `β₅` multiplies
**n(n+1)/2** (triangular); `a₅, λ_T` multiply **n** (linear helicity ± splitting); `σ₅` multiplies **log τ(Kₙ)**
(knot-complement torsion). Numerical anchor (why `C₅` is *pure*, not π²-suppressed): `ζ(3)/12 = 0.10017140859…`
matches `0.100171`; `ζ(3)/(12π²) = 0.01014948…` does **not** — so `C₅ = ζ(3)/12` is unambiguously the pure rational×ζ(3).

**Decomposition (in-project [V], `KERNEL_…` §1a).** Across the tower u→t the mass spans **80,030×** (`log = 11.290`):
the `(n+1)` operator **seed = 0.693 = 6.1 %**, the `exp[ζ-values + knot]` **dressing = 10.597 = 93.9 %**. So ~94% of
the hierarchy lives in the number-theoretic exponent, ~6% in the operator eigenvalue. **[V]** that the formula
arithmetic reproduces (6/6 quark masses to −0.000% in `nielsen_quark_assembly_verify.py`); **[framework: Nielsen
TUFT]** for the tower ansatz and the ζ-value coefficient assignments; cross-checks `C₅=0.10017141`,
`β₅=0.00133064`, `σ₅` all reproduce.

---

## M13-3 — THE CHARGED-LEPTON TOWER (S³) AND ω₃   [framework tower / credited torsion prefactor]

**WHAT.** The S³ lepton tower has the same `(n+1)·exp(linear − quadratic)` shape, but its quadratic coefficient is the
**π²-carrying** universal analytic-torsion prefactor `ω₃ = ζ_B′(0)`, *not* the pure `ζ(3)/12`. This mismatch is the
seed of the π-power anomaly (M13-10).

**MATH.** Exact-form doc (TUFT p.26–48), verbatim:
```
mₙ = Λ_shell (n+1) · exp( a n − ω₃ n² ) n ,   n = 1,2,3
ω₃ = ζ_B′(0) = ζ(3)/(4π²)          ← S³ quadratic Casimir coefficient CARRIES π²
```
> *"Step 2: The universal prefactor ζ(3)/(4π²). The spectral zeta function of the Beltrami operator on S³ at s = 0
> yields ζ_B′(0) = ζ(3)/(4π²). This is the analytic torsion of the shell with trivial twist."* (TUFT p.45)

Underlying identity (in-project [V], C9 doc): `ζ′(−2) = −ζ(3)/(4π²) = −0.03044846`, holds to 30 dps.

**Popular / coarse presentation (compendia, for cross-reference — a DIFFERENT normalization).** Both compendium files
render the lepton sector with a simplified two-coefficient exponent, **not** the ζ-valued tower:
```
m_ℓ = (v / 2R) · exp(a λ_ℓ + b λ_ℓ²) · φ_ℓ           (31pg §IX.D, X.B; 100pg M.2.2)
a = 8.528175  (= β·ξ·Lk, β=1/39.28, ξ=55.8, Lk=6 trefoil linking)
b = −1.2006804  (curvature energy of the torsion field)
φ_ℓ = k₁ σ(K) + k₂ τ_RS(K) + k₃ μ(K) ,  k₁=0.0115, k₂=0.0089, k₃=0.0023
φ_e=1.00, φ_μ=1.66, φ_τ=1.01 ;  v=246.22 GeV, R=2.98×10⁻²² m
```
This `(a,b)` pair is a coarse rewrite, **distinct** from the exact ζ-valued tower of M13-2/M13-3; flag any attempt to
equate `a=8.528175` with `a₅≈3.564112` — they are different parameterizations of different shells. **[credited]** for
`ω₃=ζ_B′(0)=ζ(3)/(4π²)` as a Ray–Singer analytic-torsion value; **[framework: Nielsen TUFT]** for the lepton tower and
the `(a,b,φ)` popular coefficients.

---

## M13-4 — THE NEUTRINO TOWER (S⁹): C₉ AND σ₉   [framework tower / [V] arithmetic]

**WHAT.** The S⁹ neutrino shell's quadratic coefficient `C₉` is the S⁹ analogue of `C₅` — again written **pure (no π)**
by Nielsen — with a triality correction; its torsion exponent `σ₉` carries π². `C₉`'s arithmetic is [V] to 30+ dps.

**MATH.** Verbatim (TUFT p.282, FAQ 18; exact-form doc line 75; C9 doc):
```
C₉ = −ζ(3)/8 · (1 + ζ(3)/28)   = −0.15670774        ← PURE, NO π   (quadratic-Casimir analogue, grades n²)
σ₉ = ζ(3)/(8π²)                = 0.01522423          ← knot torsion exponent, CARRIES π²
```
Arithmetic (mpmath 50 dps, C9 doc — **[V]**):
```
−ζ(3)/8         = −0.15025711289494928567
 ζ(3)/28        =  0.042930603684271224479
(1 + ζ(3)/28)   =  1.0429306036842712245
C₉              = −0.15670774145938515279   → −0.15671
```
Provenance (verbatim, FAQ 18): *"the leading −ζ(3)/8 is the lens-space determinant coefficient on S⁹ (rank(ξ)=8),
from the same mechanism as ζ(3) on S³. The correction ζ(3)/28 comes from the SO(8) triality automorphism of the S⁷
sub-shell (dim SO(8)=28)."* So `1/8 = rank(ξ)` on S⁹ and `ζ(3)/28 = 1/dim SO(8)`. **[V]** arithmetic + the fact that
this exact form is Nielsen's verbatim coefficient (not an agent ansatz); **[framework: Nielsen TUFT]** for the S⁹
identification. (Housekeeping note: a stale `C₉ = −0.110` cited in one open-problems parenthetical is a **phantom** —
not a π-power/normalization pair of −0.15671, ratio `π^0.309`, coincidence-gate FAIL; do not reintroduce it.)

---

## M13-5 — KNOT & LENS-SPACE NORMALIZATIONS (τ(Kₙ), τ_R(L(n,1)), N₅/N₉/κ₅/κ₉)   [credited torsion / framework assignment]

**WHAT.** The tower's non-analytic inputs are integer knot invariants and a lens-space framing factor, plus contact
normalizations `N,κ`. These are the *algebraic* (Reidemeister) side — credited invariants; their *assignment* to
particles is the framework's.

**MATH.** Knot-complement torsions τ(Kₙ), verbatim (exact-form §2; TUFT eq 94–95, p.56):
```
τ(K₁) = 1   (unknot)
τ(K₂) = 4   (Hopf-link, regularized |1 − e^{iπ}|² )
τ(K₃) = 3   (trefoil, Alexander |Δ(−1)| )
```
Lens-space (Cheeger–Müller step `T_RS(L(n,1)) = τ_R(L(n,1))`), verbatim:
```
τ_R(L(n,1)) = ∏_{j=1}^{n−1} |1 − e^{2πij/n}|⁻¹ = 1/n      ← fixes the 1/n framing normalization only
```
Contact normalizations (exact-form §3):
```
N₅ = 8π³ ,   κ₅ = (1/8π³) · exp(…)
N₉ = 32π⁵ ,  κ₉ = (1/32π⁵) · exp( ζ′_{Δ2}(0)/16 )
```
The `τ(Kₙ) ∈ {1,4,3}` are pure integers (no ζ(3)); the trefoil value is the Alexander polynomial `|Δ(−1)| = 3`, the
Hopf-link value a regularized sin-product. **[credited]** for `Δ(−1)`, the Reidemeister sin-product, and
`τ_R(L(n,1))=1/n`; **[framework: Nielsen TUFT]** for the knot↔shell-index assignment `Kₙ` and the `N,κ` contact factors.

---

## M13-6 — THE ζ(3) PROVENANCE: RAY–SINGER / NASH–O'CONNOR LENS-SPACE DETERMINANT   [credited]

**WHAT.** Where the `ζ(3)` actually comes from: **not** the algebraic sin-product, but the *analytic* Ray–Singer
ζ-determinant of the Laplacian on lens-space quotients of the Hopf shells (Nash–O'Connor template). This is the
credited route, and it is the route that supplies a **π²** — the fact M13-10 turns on.

**MATH.** Sector Determinant Lemma, §4.11 "Proof via Ray–Singer Torsion on Lens Spaces" (TUFT p.~40–47), verbatim chain:
```
nth fiber-winding sector of S³   ≅   spectral theory on L(n,1) = S³/Zₙ     (Nash–O'Connor)
ζ-derivative of the spectral sum:  ∂_s[ Σ m²/(m+const)^{2s} ]|_{s=0}  =  Σ m⁻³  =  ζ(3)
normalize to the determinant:      ζ_B′(0) = ζ(3)/(4π²)   ("the analytic torsion of the shell")
Ray–Singer analytic torsion:       log τ_RS(M) = ½ Σ_p (−1)^p p ζ′_p(0) ,  ζ_p(s)=Σ_{λ>0} λ^{−s}   (31pg §IX.E)
Cheeger–Müller (1978–79):          analytic torsion = Reidemeister torsion (closed Riemannian M)
```
FAQ 7 (TUFT p.279), verbatim: *"torsion exponent zeta(3) from the lens-space determinant (Lemma 12), knot corrections
from Reidemeister torsion."* Citations Nielsen gives: **Ray–Singer [11]** (1971), **Nash–O'Connor [47,48]**
(lens-space determinants — the ζ(3) source), **Cheeger–Müller [18,19]**. No Millson citation for the mass ζ(3).
**[credited]** — this whole route is established spectral geometry; the ζ(3)=`Σm⁻³` and `ζ_B′(0)=ζ(3)/(4π²)`
(via `ζ′(−2)=−ζ(3)/4π²`) are textbook/checkable.

---

## M13-7 — CHERN–SIMONS TOPOLOGICAL MASS, 7D CS₇, η-INVARIANT / APS   [credited theory / framework 7D use]

**WHAT.** Chern–Simons gives a *topological* mass `M = ke²/4π` with no Higgs; its 3D form and the APS η-invariant
(spectral asymmetry) are credited; the 7D `CS₇` used to feed neutrino masses is the framework's extension.

**MATH.** 3D Chern–Simons action + topological mass (100pg M.2.6; also M.12.3), verbatim:
```
S_CS = (k/4π) ∫ Tr( A∧dA + (2/3) A∧A∧A )          ⇒   topological mass   M = k e² / 4π   (no Higgs)
Hopf-link embedding in S³:   CS₇(A_H) = 14.1914 ,   η-invariant  η(S³) = 0.0215
```
> *"The Atiyah–Patodi–Singer index theorem connects spectral asymmetry [η] to topological mass corrections."* (100pg)

7D Chern–Simons (31pg §XII.C), verbatim:
```
S_{CS7} = (k/4π) ∫_{M⁷} Tr( A∧dA∧dA∧dA + higher terms ) ,   ∫_{M⁷} CS₇(A) ∈ 2πℤ
```
> *"Witten's AdS₇/CFT₆ connection: the 7D Chern–Simons action is the holographic dual to the 6D (2,0) superconformal
> field theory, providing the mathematical structure for neutrino mass generation."* (Witten 1998, hep-th/9812012).
First Chern class of the bundle: `c₁(S¹→S⁹→CP⁴) = 1` (31pg §IX.A; 100pg M.12.3, `c₁ = (1/2π)∫F`). **[credited]** for the
CS action, `M=ke²/4π`, the η-invariant and APS; **[framework: Nielsen TUFT]** for the specific `CS₇=14.1914`,
`η(S³)=0.0215` values and the "CS₇ ⇒ neutrino mass" use (the 7D→ν identification is asserted, not derived here).

---

## M13-8 — CKM FROM CP⁴ OVERLAPS   [framework construction / [preprint-claim] fit]

**WHAT.** Quark mixing = topological overlap integrals of S⁵ eigenmodes on CP⁴. The *construction* (an overlap
`⟨ψ_i|ψ_j⟩`) is a legitimate framework move; the *agreement numbers* are the preprint's, under review (M13-11).

**MATH.** Definition + values (31pg §XII.A), verbatim:
```
V_{ij} = ⟨ψ_i | ψ_j⟩_{CP⁴}
|V_us| = 0.2252 ,  |V_cb| = 0.0412 ,  |V_ub| = 0.00358
J (Jarlskog) = 3.06×10⁻⁵    [exp 3.08×10⁻⁵ ± 0.13×10⁻⁵, 0.2σ]
```
Angle form (100pg M.2.9), verbatim [TUFT vs experiment]:
```
θ₁₂ (Cabibbo) 13.1° [13.04°±0.05°] ;  θ₂₃ 2.4° [2.38°±0.06°] ;  θ₁₃ 0.2° [0.201°±0.011°] ;  δ(CP) 69° [68°±5°]
```
Mechanism (framework): *small* CKM angles ⇐ **nearly disjoint** S⁵ modes (weak overlap). **[framework: Nielsen TUFT]**
for `V_ij=⟨ψ_i|ψ_j⟩` and the disjoint-mode mechanism; the "all 4 parameters, zero free parameters, `J` at 0.2σ" is
**[preprint-claim]** — reproduced, not [V].

---

## M13-9 — PMNS + NEUTRINO MASSES FROM S⁹ OVERLAPS   [framework construction / [preprint-claim] fit]

**WHAT.** Neutrinos = suppressed S⁹ Beltrami modes; large PMNS angles ⇐ **strongly overlapping** S⁹ modes (the
mirror of the small-CKM story); mass scale from a geometric S³/S⁹ radius ratio, no seesaw.

**MATH.** Geometric suppression (100pg M.2.7; 31pg §XII.B), verbatim:
```
m_ν ~ m_e · (R₃/R₉) = 0.511 MeV × 10⁻⁷ ≈ 50 meV        (100pg)
m_ν ~ (v · R₃)/R₉ ~ 246 GeV × (10⁻²² m / 10⁻¹⁸ m) ~ 0.001 eV     (31pg)
```
Spectrum + mixing (31pg §XII.B; 100pg M.2.7), verbatim:
```
m_ν1 ≈ 0.001 eV ,  m_ν2 ≈ 0.009 eV ,  m_ν3 ≈ 0.05 eV ,  Σm_ν ≈ 0.06 eV  (< 0.12 eV cosmo bound)
PMNS:  θ₁₂ ≈ 34° ,  θ₂₃ ≈ 45° ,  θ₁₃ ≈ 8.5°
Δm²₂₁ = 6.3×10⁻⁵ eV²  [exp 7.53×10⁻⁵, ~20%] ;  Δm²₃₁ = 2.5×10⁻³ eV²  [exp 2.453×10⁻³, ~2%]
```
Framework prediction: **Dirac** neutrinos (S⁹ spinor decomposition forbids a Majorana mass ⇒ 0νββ null), **normal
ordering**. **[framework: Nielsen TUFT]** for the suppressed-mode construction and no-seesaw geometric scale;
`m_ν ~ 50 meV` and the atmospheric `Δm²₃₁` at ~2% are **[preprint-claim]** (the solar `Δm²₂₁` is only ~20%, an honest
internal miss); cross-ref M10-4 (the seesaw-as-frequency-downconversion reading independently finds the ν rung at
0.05 eV to 0.04%, but locates the heavy scale **off-ladder** — FTGB does not itself derive `m_ν`).

---

## M13-10 — ⚑ THE π-POWER INTERNAL INCONSISTENCY (unresolved anomaly — flag on every use)   [anomaly]

**WHAT.** The single most important honesty flag for the whole tower. The **same class** of object — the "quadratic
Casimir / Ray–Singer torsion" coefficient — appears with **inconsistent π-powers across shells**: pure `ζ(3)/12` and
`−ζ(3)/8` on S⁵/S⁹ (no π), but `ζ(3)/(4π²)` on S³ and π²-carrying torsion exponents `σ₅, σ₉`. Nielsen's *own*
derivation (M13-6) supplies a π² (the lens-space determinant gives `ζ_B′(0)=ζ(3)/(4π²)`), so the **pure `ζ(3)/12` is
the anomaly — it drops the π² its own route supplies.** This is documented, not smoothed.

**MATH.** The full π-power ledger (exact-form doc §1, §3), verbatim:
```
π⁰ (pure) :  C₅ = ζ(3)/12 ;  C₉ = −ζ(3)/8 ;  ζ(3)/28 correction
π¹        :  λ_T splitting coeff ζ(3)/(12π)   (1/π from the S⁵ contact coupling λ_T⁽⁰⁾=2/π)
π²        :  ω₃ = ζ_B′(0) = ζ(3)/(4π²) ;  σ₅ = ζ(3)/(16π²) ;  σ₉ = ζ(3)/(8π²) ;  a₅'s (2 + ζ(3)/(4π²))
π⁴        :  β₅ = ζ(5)/(8π⁴) ;  spectral₅ = (3ζ(5)+5π²ζ(3))/(8π⁴)
```
The clash, verbatim: *"The S³ quadratic coefficient ζ(3)/(4π²) and the S⁵ quadratic coefficient ζ(3)/12 are the SAME
kind of object … but have DIFFERENT π-powers. This is the internal inconsistency."* The pure-vs-determinant factor is
`(ζ(3)/12)/(ζ(3)/(4π²)) = π²/3 = 3.2899`. **Status: OPEN.** Settling which of the pure or the π²-carrying form is
physically correct needs the lens-space η / coexact-p determinant computation (the "A1a/A1b" task) or a firmer TUFT
primary source — **not guessed here.** **[anomaly]** — carry this flag with any downstream use of `C₅`, `C₉`, `ω₃`,
`σ₅`, or `σ₉`.

---

## M13-11 — ⚑ HONESTY ON THE FITS: "blind-fit at 0.1σ / all-masses-recovered" is the PREPRINT's claim, in review   [preprint-claim — NOT [V]]

**WHAT.** The second prominent flag. The compendia advertise **sub-0.01% mass agreement, `χ²/dof ≈ 0`, "zero free
parameters," quark masses "within 0.1σ / 0.01σ," CKM "all four at 0.2σ."** These are **the preprint's own
data-recovery claims, currently in Round-2 peer review** — reproduced here for completeness and **NOT** independently
validated by this project.

**MATH / what is and isn't ours.**
```
[V] in-project (arithmetic only):  given Nielsen's coefficients, the formula returns the numbers she states —
    quark tower 6/6 to −0.000% (nielsen_quark_assembly_verify.py); C₉ = −0.15670774 and ζ′(−2)=−ζ(3)/4π² to 30 dps.
[preprint-claim] (NOT [V]):  that these are the correct particle masses; that it is a genuine zero-free-parameter
    blind fit; the "0.1σ / 0.01σ / sub-0.01%" significances; the CKM/PMNS/ν agreements as validations of TUFT.
```
Reproduced tables (label them **[preprint-claim]** wherever cited): leptons e/μ/τ "sub-0.01%"; quarks u,d,s,c,b,t
"within 0.5σ…0.01σ" (31pg §XI.B); CKM "all 4, `J` at 0.2σ" (M13-8); ν "`Δm²₃₁` at 2%" (M13-9). The honest reading:
the tower is **operator-seeded, linear, and formula-dressed** (M13-1, M13-2) with ~94% of the hierarchy in a
number-theoretic exponent whose coefficients carry the unresolved π-power anomaly (M13-10) — so its *structure* is
foldable and its *arithmetic* checks, but its *physical fit claims stand or fall with the preprint under review*,
not with anything verified here. Governing caveat: TUFT is a preprint (Nielsen 2024–2025, PhilArchive; in peer
review); everything framework-tagged is asserted **illustratively**. **NOT `[V]`.**

---

## M13-12 — THE COEFFICIENT / METHOD TABLE (core output)

| Object | Shell | Value (verbatim) | π-power | Role / grading | Tier |
|---|---|---|---|---|---|
| `(n+1)` seed | all | curl eigenvalue `±(n+1)/R` | — | linear operator seed (6.1% of u→t) | [credited] |
| `C₅` | S⁵ | **ζ(3)/12** ≈ 0.100171 | **π⁰** | quadratic `n²` (Ray–Singer) | [framework] + **[anomaly]** |
| `C₉` | S⁹ | **−ζ(3)/8·(1+ζ(3)/28)** = −0.15670774 | **π⁰** | quadratic `n²` analogue | [V] arith / [framework] + **[anomaly]** |
| `ζ(3)/28` | S⁷ | ζ(3)/28 = 0.0429306 | π⁰ | SO(8) triality (dim=28) | [framework] |
| `ω₃` | S³ | **ζ_B′(0) = ζ(3)/(4π²)** | **π²** | quadratic `n²` + universal prefactor | [credited] value / [framework] use + **[anomaly]** |
| `σ₅` | S⁵ | **ζ(3)/(16π²)** ≈ 0.0076121 | π² | knot torsion `log τ(Kₙ)` | [framework] |
| `σ₉` | S⁹ | **ζ(3)/(8π²)** = 0.0152242 | π² | knot torsion `log τ(Kₙ)` | [framework] |
| `λ_T(n)` | S⁵ | 2/π + (ζ(3)/12π)(5/2−n) | π¹ | linear-`n` splitting | [framework] |
| `a₅` | S⁵ | exp(spectral₅/6)√3(2+ζ(3)/4π²) ≈ 3.564112 | π² | linear helicity | [framework] |
| `β₅` | S⁵ | **ζ(5)/(8π⁴)** ≈ 1.33064×10⁻³ | π⁴ | triangular `n(n+1)/2` | [framework] |
| `spectral₅` | S⁵ | (3ζ(5)+5π²ζ(3))/(8π⁴) | π⁴/π² | shell spectral input | [framework] |
| `Λ₅` | S⁵ | (2π/√3) v κ₅³ | — | overall scale | [framework] |
| `τ(Kₙ)` | knot | {1, 4, 3} (unknot/Hopf/trefoil `\|Δ(−1)\|`) | — | knot-complement torsion | [credited] invariant / [framework] assignment |
| `τ_R(L(n,1))` | lens | `∏\|1−e^{2πij/n}\|⁻¹ = 1/n` | — | framing normalization | [credited] |
| `N₅, N₉` | contact | 8π³, 32π⁵ | π³, π⁵ | contact normalization | [framework] |
| `M=ke²/4π` | CS₃ | topological mass, no Higgs | — | Chern–Simons | [credited] |
| `CS₇(A_H)`, `η(S³)` | CS₇ | 14.1914, 0.0215 | — | 7D CS + APS η | [credited] theory / [framework] values |
| `V_ij=⟨ψ_i\|ψ_j⟩`, `J=3.06×10⁻⁵` | CP⁴ | CKM overlaps | — | quark mixing | [framework] / [preprint-claim] fit |
| PMNS `34°/45°/8.5°`, `m_ν~50 meV` | S⁹ | ν mixing + masses | — | lepton mixing | [framework] / [preprint-claim] fit |

---

## M13-13 — LIMITS (stated prominently)   [V]

This module does **NOT**:
1. **endorse the mass-recovery fit** — the "zero-parameter blind fit at 0.1σ / sub-0.01%" claims are the preprint's,
   in Round-2 review (**[preprint-claim]**, M13-11); only the arithmetic reproduction and the coefficient identities
   are **[V]**.
2. **resolve the π-power inconsistency** — pure `C₅=ζ(3)/12` vs π²-carrying `ω₃, σ₅, σ₉` is an **unresolved anomaly**
   (**[anomaly]**, M13-10); which form is physical is OPEN, needs the lens-space η / coexact-p determinant or a firmer
   TUFT source.
3. **supply a transition matrix element** — `⋆d` is linear ⇒ strictly diagonal, zero off-diagonal (M13-1); the tower
   has no nuclear sector and cannot hand over an ME (see `KERNEL_NIELSEN_MASS_MATRIX_ELEMENT`); MEs need a nonlinear
   interaction the tower lacks.
4. **derive a neutrino mass ab-initio** — the `m_ν~50 meV` is a geometric-ratio *ansatz*; the solar `Δm²₂₁` misses by
   ~20% (honest internal miss); cross-ref M10-4 (heavy scale is off-ladder).
5. **claim the compendium `(a=8.528175, b=−1.2006804)` popular formula equals the exact ζ-tower** — they are distinct
   parameterizations (M13-3); do not cross-substitute their coefficients.

**The two load-bearing flags, restated:** (a) the tower carries a **documented π-power internal inconsistency**
(`C₅=ζ(3)/12` pure vs `ω₃/σ₅/σ₉` π²-carrying) — **[anomaly]**, unresolved; (b) the **fit claims are the preprint's,
in review — [preprint-claim], NOT [V].** Fold the structure and coefficients; the fits are unverified-here.

---

## Per-claim index (M13)
| # | Claim | Tier | Repro / trace |
|---|---|---|---|
| M13-1 | Proca–Beltrami `λ=mc/ℏ`; curl `S³` spectrum `±(n+1)/R`; `⋆d` Thm 14 seed; linear ⇒ zero off-diagonal ME | [credited] seed / [framework] id / [V] diagonal-only | Arnold–Khesin §I.5; `KERNEL_NIELSEN…` §1c |
| M13-2 | Quark tower eq 96 + `C₅,β₅,σ₅,a₅,λ_T,Λ₅,spectral₅`; 6.1%/93.9% split | [framework] / [V] arith (6/6 −0.000%) | `NIELSEN_TUFT_MASS_COEFFICIENT_EXACT_FORM` §1; `nielsen_quark_assembly_verify.py` |
| M13-3 | Lepton tower `exp(a n − ω₃ n²)`, `ω₃=ζ(3)/(4π²)`; compendium `(a,b,φ)` popular form (distinct) | [credited] ω₃ / [framework] tower | exact-form p.45; 31pg §IX.D–X.B; `ζ′(−2)=−ζ(3)/4π²` [V] |
| M13-4 | `C₉=−ζ(3)/8(1+ζ(3)/28)=−0.15670774`; `σ₉=ζ(3)/(8π²)`; rank/triality provenance | [V] arith 30 dps / [framework] | `C9_MASS_TOWER_COEFFICIENT_VERIFICATION`; TUFT p.282 FAQ18 |
| M13-5 | `τ(Kₙ)={1,4,3}`; `τ_R(L(n,1))=1/n`; `N₅=8π³,N₉=32π⁵,κ₅,κ₉` | [credited] invariants / [framework] assignment | exact-form §2–3; TUFT eq 94–95 |
| M13-6 | ζ(3) = `Σm⁻³` from Nash–O'Connor lens determinant → `ζ_B′(0)=ζ(3)/(4π²)`; Cheeger–Müller | [credited] | exact-form §2; 31pg §IX.E; Ray–Singer/Nash–O'Connor/Cheeger–Müller |
| M13-7 | `S_CS=(k/4π)∫Tr(A∧dA+⅔A∧A∧A)`, `M=ke²/4π`; `CS₇`, `η(S³)=0.0215`, APS | [credited] theory / [framework] 7D values | 100pg M.2.6/M.12.3; 31pg §XII.C; Witten 1998 |
| M13-8 | CKM `V_ij=⟨ψ_i\|ψ_j⟩`; `J=3.06×10⁻⁵`; angles 13.1°/2.4°/0.2°/69° | [framework] / [preprint-claim] fit | 31pg §XII.A; 100pg M.2.9 |
| M13-9 | PMNS `34°/45°/8.5°`; `m_ν~50 meV`, spectrum, `Δm²`; Dirac/normal-ordering | [framework] / [preprint-claim] fit | 31pg §XII.B; 100pg M.2.7 |
| M13-10 | π-power inconsistency: pure `ζ(3)/12` vs π²-carrying `ω₃,σ₅,σ₉`; factor `π²/3` | **[anomaly]** unresolved | exact-form §1,§3 (verdict) |
| M13-11 | "blind-fit 0.1σ / zero-parameter / sub-0.01%" recovery | **[preprint-claim]** NOT [V] | compendia tables; TUFT in peer review |
| M13-13 | Limits + the two flags | [V] scope | statement |

## Verification coverage (M13)
- **In-repo verify — `results/verify/tuft_mass_tower_check.py` (run here):** reproduces the closed-form
  coefficients `C₅=ζ(3)/12`, `β₅=ζ(5)/(8π⁴)`, `σ₅=ζ(3)/(16π²)`, `ω₃=ζ(3)/(4π²)`, `C₉=−0.15670774` to their
  reported values; exhibits the **exact `C₅/ω₃ = π²/3 = 3.2899…` clash (M13-10, the π-power anomaly)**; and
  verifies `τ_R(L(n,1)) = 1/∏|1−e^{2πij/n}| = 1/n`. This is the checkable `[V]` core of the module; the
  fit-to-data recovery below stays `[preprint-claim]`.
- **[V] in-project (arithmetic / identities only):** quark tower reproduces 6/6 to −0.000%
  (`nielsen_quark_assembly_verify.py`, in `ckfreefem\frontier_calcs\`, external provenance);
  `C₉=−0.15670774` and `−ζ(3)/8, ζ(3)/28, (1+ζ(3)/28)` to 50 dps (`c9_mass_tower_coefficient_verification…py`);
  `ζ′(−2)=−ζ(3)/(4π²)=−0.03044846`; `C₅=ζ(3)/12=0.10017141`, `β₅=ζ(5)/(8π⁴)=0.00133064`, `σ₉=ζ(3)/(8π²)=0.01522423`;
  the pure-vs-π² clash and the `π²/3=3.2899` factor; the `⋆d`-linear ⇒ zero-off-diagonal theorem.
- **[anomaly] flagged, not smoothed:** the cross-shell π-power inconsistency (M13-10).
- **[preprint-claim], NOT validated here:** every mass-recovery, significance (`σ`), and "zero-parameter" statement (M13-11).
- **Numbers traced, not invented:** every coefficient quotes its source doc + equation number. No mass, rate, cross-section,
  or fit is fabricated; the compendium popular-`(a,b)` form is flagged as distinct from the exact ζ-tower.

**Citations.** Nielsen, J. L., *The Topological Unified Field Theory on S¹→S⁹→CP⁴* (PhilArchive 2024–2025; long
`NielsenTUFT.pdf` 290 pp), **in peer review** — eq 87/96–103 (quark tower), p.45 (`ω₃`), p.282 FAQ18 (`C₉,σ₉`), §XII
(CKM/PMNS/CS₇). Ray, D. B. & Singer, I. M., *Adv. Math.* **7**, 145 (1971). Nash, C. & O'Connor, D. J., *J. Math.
Phys.* **36**, 1462 (1995). Cheeger, J., *Ann. Math.* **109**, 259 (1979); Müller, W., *Adv. Math.* **28**, 233
(1978). Arnold, V. & Khesin, B., *Topological Methods in Hydrodynamics* (1998) §I.5. Atiyah, M., Patodi, V. & Singer,
I., *Math. Proc. Camb. Phil. Soc.* **77**, 43 (1975) (η-invariant). Witten, E., *Comm. Math. Phys.* **121**, 351
(1989) (CS/Jones); Witten, E., *JHEP* **9812**, 012 (1998), hep-th/9812012 (AdS₇/CFT₆). Cantarella, J., Kusner, R. &
Sullivan, J., *Invent. Math.* **150**, 257 (2002) (ropelength). Woltjer, L., *PNAS* **44**, 489 (1958). PDG 2024.

Cross-links: `NIELSEN_TUFT_MASS_COEFFICIENT_EXACT_FORM_2026-09-02`, `C9_MASS_TOWER_COEFFICIENT_VERIFICATION_2026-09-08`,
`KERNEL_NIELSEN_MASS_MATRIX_ELEMENT_2026-09-02`, `A1_ANALYTIC_TORSION_MASS_TOWER_2026-09-02` (the open π-power question),
`NEUTRINO_DM2_RATIO_MASS_TOWER_TEST_2026-09-08`, `TOOLKIT_ADV_10_TOPOLOGICAL_SOLITON_METHODS_2026-09-08` (M10-3 sector
split: Skyrme/baryon `π₃S³` moduli-geodesic vs lepton/ν `π₃S²` spectral; M10-4 seesaw/ν rung),
`reference_nielsen_tuft_assessment`, `project_ftgb_open_problems_and_negatives` (A1 / π-power entry).
