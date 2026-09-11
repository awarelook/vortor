# Nielsen TUFT — Exact Form of the ζ(3) Mass-Tower Coefficient (A1′ decision)

Date: 2026-09-02
Primary source: `C:\Users\natha\Downloads\NielsenTUFT.pdf` (290 pp, long version). Explicit
formulas are in the long version only; the short version (`TUFT Jenny Nielsen.pdf`, 180 pp)
states the structure qualitatively but not the numbered coefficient equations.
Method: pages read as images via Read tool; full text extracted with `pdftotext -layout`
(note: pdftotext drops the π and ζ glyphs, so `(3)/(42)` in extracted text = `ζ(3)/(4π²)`,
verified against page images and by numerics). All formulas below transcribed from the page
images, not the lossy text dump.

--------------------------------------------------------------------------------
## VERDICT (one line)

**Nielsen's mass tower contains BOTH forms, for DIFFERENT roles, and is internally
inconsistent in the π-power of the ζ(3) quadratic coefficient across shells:**

- The **S⁵ / S⁹ quadratic ("Casimir" / "Ray–Singer torsion") coefficient is PURE `ζ(3)/12`
  and `−ζ(3)/8` — NO π.** She writes `C₅ = ζ(3)/12 ≈ 0.100171` verbatim (eq 87, 99). This is
  exactly the spectral-geometrically anomalous form A1′ flags.
- The **S³ quadratic coefficient and the universal determinant prefactor DO carry 1/π²:
  `ω₃ = ζ_B′(0) = ζ(3)/(4π²)`** (p. 45, Sector Determinant Lemma). The knot torsion
  **exponents** also carry 1/π²: `σ₅ = ζ(3)/(16π²)`, `σ₉ = ζ(3)/(8π²)`.

So A1′'s claim — "in lens-space spectral geometry ζ(3) always carries 1/π²; a pure `ζ(3)/12`
is anomalous" — **matches Nielsen's own ζ_B′(0) = ζ(3)/(4π²)** and is **contradicted by her own
`C₅ = ζ(3)/12`**. The pure `ζ(3)/12` she writes for the n²-growth coefficient is inconsistent
with the π²-carrying determinant number she derives two sections earlier. A1′ is therefore
*correct in its diagnosis* and Nielsen's pure `ζ(3)/12` is the anomaly, not a legitimate
alternate normalization.

--------------------------------------------------------------------------------
## 1. THE MASS-TOWER FORMULA AND ITS ζ(3)/ζ(5) COEFFICIENTS (verbatim, with π-power)

### Quark tower, complete formula (p. 57, eq 96–103)

    m_{n,±} = Λ₅ (n+1) · exp( (a₅ ± λ_T(n)) n + C₅ n² + β₅ · n(n+1)/2 + σ₅ log τ(Kₙ) )
              × { 2/3, n=1 ; 1, n=2,3 }                                          (96)

with (all boxed equations, transcribed from the page image):

    C₅ = ζ(3)/12        ≈ 0.100171          (87 = 99)   ← PURE, NO π  [n² grading]
    β₅ = ζ(5)/(8π⁴)     ≈ 1.33064×10⁻³      (100)       ← ζ(5), carries π⁴  [n(n+1)/2]
    σ₅ = ζ(3)/(16π²)    ≈ 7.61211×10⁻³      (101)       ← carries π²  [log τ(Kₙ)]
    a₅ = exp(spectral₅/6) √3 (2 + ζ(3)/(4π²)) ≈ 3.564112 (98)  ← contains ζ(3)/(4π²)  [n]
    λ_T(n) = 2/π + (ζ(3)/(12π))(5/2 − n),  n=2,3        (90 = 103) ← ζ(3)/12 × (1/π contact)
    Λ₅ = (2π/√3) v κ₅³                                  (97)

Numerical proof that C₅ is pure (no π):
    ζ(3)/12       = 0.10017140859663…   → MATCHES 0.100171 exactly.
    ζ(3)/(12π²)   = 0.01014948…         → does NOT match.
Hence `C₅ = ζ(3)/12` is unambiguously the pure rational × ζ(3).

### Level grading (verbatim, eq 96)
- `C₅` (the pure `ζ(3)/12`) multiplies **n²** (quadratic Casimir growth).
- `β₅` (the `ζ(5)/(8π⁴)` term) multiplies **n(n+1)/2** (triangular).
- `a₅`, `λ_T` multiply **n** (linear).
- `σ₅` multiplies **log τ(Kₙ)** (knot-complement torsion, not a power of n).

### Charged-lepton tower, S³ (p. 26–48; extracted text lines 28, 3232, 3489)

    mₙ = Λ_shell (n+1) · exp( a n − ω₃ n² ) n ,   n = 1,2,3
    ω₃ = ζ(3)/(4π²)     ← the S³ quadratic Casimir coefficient CARRIES π²

The S³ "universal prefactor" is `ζ_B′(0) = ζ(3)/(4π²)` (p. 45): *"Step 2: The universal
prefactor ζ(3)/(4π²). The spectral zeta function of the Beltrami operator on S³ at s = 0
yields ζ_B′(0) = ζ(3)/(4π²). This is the analytic torsion of the shell with trivial twist."*

>>> The S³ quadratic coefficient ζ(3)/(4π²) and the S⁵ quadratic coefficient ζ(3)/12 are the
>>> SAME kind of object ("quadratic Casimir / Ray–Singer coefficient") but have DIFFERENT
>>> π-powers. This is the internal inconsistency that A1′ pins down.

### Neutrino tower, S⁹ (p. 282, FAQ 18; extracted lines 21084–21091, and line 4829)

    C₉ = −ζ(3)/8 · (1 + ζ(3)/28)        ← PURE, NO π  (quadratic-Casimir analogue)
    σ₉ = ζ(3)/(8π²)                     ← knot torsion exponent, CARRIES π²

Verbatim (FAQ 18, p. 282): *"C₉ = −ζ(3)/8·(1 + ζ(3)/28): the leading −ζ(3)/8 is the
lens-space determinant coefficient on S⁹ (rank(ξ)=8), from the same mechanism as ζ(3) on S³.
The correction ζ(3)/28 comes from the SO(8) triality automorphism of the S⁷ sub-shell
(dim SO(8)=28)."* And (line 4829): *"The torsion exponent σ₉ = ζ(3)/(8π²) differs from the
S⁵ value σ₅ = ζ(3)/(16π²)."*

### Summary table of every ζ(3)/ζ(5) coefficient found

| Coefficient | Shell | Value (verbatim) | π-power | Role / grading |
|---|---|---|---|---|
| C₅ | S⁵ | **ζ(3)/12** | **none** | quadratic n² ("Ray–Singer coeff") |
| C₉ (leading) | S⁹ | **−ζ(3)/8** | **none** | quadratic-Casimir analogue |
| ζ(3)/28 correction | S⁷ | **ζ(3)/28** | **none** | SO(8) triality |
| λ_T(n) coeff | S⁵ | ζ(3)/(12π) = C₅·(1/π) | π¹ (from contact 1/π) | splitting, linear n |
| ω₃ = ζ_B′(0) | S³ | **ζ(3)/(4π²)** | **π²** | quadratic n² + universal prefactor |
| σ₅ | S⁵ | **ζ(3)/(16π²)** | **π²** | knot torsion exponent (log τ) |
| σ₉ | S⁹ | **ζ(3)/(8π²)** | **π²** | knot torsion exponent (log τ) |
| a₅ term | S⁵ | 2 + ζ(3)/(4π²) | π² | linear helicity |
| β₅ | S⁵ | **ζ(5)/(8π⁴)** | π⁴ | ζ(5) shell term, n(n+1)/2 |
| spectral₅ | S⁵ | (3ζ(5) + 5π²ζ(3))/(8π⁴) | π⁴/π² | shell spectral input |

--------------------------------------------------------------------------------
## 2. HOW SHE DERIVES THE ζ(3): ANALYTIC Ray–Singer (Nash–O'Connor), NOT the sin-product

Route = **(b) analytic Ray–Singer / ζ-determinant**, via the Nash–O'Connor lens-space
determinant. It is explicitly NOT the algebraic Reidemeister sin-product for the ζ(3) itself.

Sector Determinant Lemma, §4.11 "Proof via Ray–Singer Torsion on Lens Spaces" (p. ~40–47):
- *"The nth fiber winding sector of S³ is naturally identified with the spectral theory on
  L(n,1) = S³/Zₙ. Nash and O'Connor [48] computed the determinant of the Laplacian on lens
  spaces explicitly."*
- The ζ(3) itself comes from a ζ-derivative of the spectral sum (extracted line 3172):
  *"Σ m²/(m+const)^{2s} whose derivative at s=0 yields Σ m⁻³ = ζ(3). This was first computed
  by Nash and O'Connor [47,48]."*
- Then normalized to the determinant value: *"ζ_B′(0) = ζ(3)/(4π²) … the analytic torsion of
  the shell."*
- FAQ 7 (p. 279) states the provenance directly: *"torsion exponent zeta(3) from the
  lens-space determinant (Lemma 12), knot corrections from Reidemeister torsion."*

The algebraic Reidemeister sin-product DOES appear, but only for the (integer/algebraic)
knot-complement normalizations, NOT for ζ(3):
- Cheeger–Müller step (line 3144): `T_RS(L(n,1)) = τ_R(L(n,1))`, with
  `τ_R(L(n,1)) = ∏_{j=1}^{n−1} |1 − e^{2πij/n}|⁻¹ = 1/n`. This fixes the *1/n* framing
  normalization only.
- Knot corrections τ(Kₙ): τ(K₁)=1 (unknot), τ(K₃)=3 (trefoil Alexander |Δ(−1)|), τ(K₂)=4
  (Hopf-link, regularized |1−e^{iπ}|² ) (eq 94–95, p. 56). Pure integers; no ζ(3).

Citations she gives: **Ray–Singer [11]** (analytic torsion, 1971), **Nash–O'Connor [47,48]**
(lens-space determinants, 1995-era — the ζ(3) source), **Cheeger–Müller [18,19]**
(analytic = Reidemeister). No Millson citation for the mass ζ(3).

--------------------------------------------------------------------------------
## 3. EXPLICIT π-POWERS IN THE TOWER (as written)

- π⁰ (pure): C₅ = ζ(3)/12; C₉ = −ζ(3)/8; ζ(3)/28 correction.
- π¹: λ_T splitting coefficient ζ(3)/(12π) (the 1/π is the S⁵ contact coupling λ_T⁽⁰⁾=2/π,
  the ζ(3)/12 factor itself is pure).
- π²: ω₃ = ζ_B′(0) = ζ(3)/(4π²); σ₅ = ζ(3)/(16π²); σ₉ = ζ(3)/(8π²); a₅'s (2 + ζ(3)/(4π²)).
- π⁴: β₅ = ζ(5)/(8π⁴); spectral₅ = (3ζ(5)+5π²ζ(3))/(8π⁴).
- π³, π⁵ (non-ζ, contact normalizations): N₅ = 8π³, κ₅ = (1/8π³)exp(…); N₉ = 32π⁵,
  κ₉ = (1/32π⁵)exp(ζ′_{Δ2}(0)/16).

--------------------------------------------------------------------------------
## 4. ANSWER TO A1′ (200-word summary)

Nielsen writes the ζ(3) mass-tower coefficient in BOTH forms, and the two are mutually
inconsistent — which is precisely what A1′ needs to know. For the quadratic (n²) growth
coefficient on the S⁵ quark shell she writes, verbatim and boxed, `C₅ = ζ(3)/12 ≈ 0.100171`
(eqs 87, 99) — a PURE rational times ζ(3) with NO π, numerically confirmed (ζ(3)/12 =
0.1001714; ζ(3)/(12π²) = 0.01015, ruled out). The S⁹ neutrino analogue is likewise pure,
`C₉ = −ζ(3)/8·(1+ζ(3)/28)` (p. 282). Yet the SAME "quadratic Casimir / Ray–Singer" coefficient
on the S³ lepton shell is `ω₃ = ζ_B′(0) = ζ(3)/(4π²)` (p. 45), and the knot torsion exponents
are `σ₅ = ζ(3)/(16π²)`, `σ₉ = ζ(3)/(8π²)` — all carrying 1/π². Her derivation is the analytic
Ray–Singer / Nash–O'Connor lens-space determinant (ζ(3) from `Σ m⁻³`, normalized to
`ζ_B′(0)=ζ(3)/(4π²)`), citing Ray–Singer [11], Nash–O'Connor [47,48], Cheeger–Müller [18,19];
the algebraic Reidemeister sin-product only fixes the integer knot normalizations τ(Kₙ),
never the ζ(3). Conclusion: A1′ is right that a legitimate lens-space determinant ζ(3) carries
1/π² (Nielsen's own ζ_B′(0) does). Her pure `ζ(3)/12` for the n² coefficient is the anomaly —
it drops the π² that her own determinant derivation supplies.
