# TOOLKIT ADV -- Module M14: GREENYER BEAT-LAW & EVO CASCADE METHODS (fractal-toroidal beat dynamics, triad dichotomy, anapole ledger, magnetic-tension fission)

Part of the FTGB math toolkit (see `MATH_TOOLKIT_BASE.md`, `TOOLKIT_ADV_09_COUPLED_OSCILLATOR_SUBSTRATE_2026-09-08.md`
(M9 Stuart-Landau/Kuramoto/Adler beat law), `TOOLKIT_ADV_10_TOPOLOGICAL_SOLITON_METHODS_2026-09-08.md`
(M10 canonical helicity, Woltjer/Taylor, no-go template)). This module is a **METHODS-PRESERVATION pass**
that lifts the *reusable mathematical machinery* of Bob Greenyer's fractal-toroidal / QHD / EVO synthesis --
as it was developed, checked, and tiered across three project source docs -- into one place so each result
can be re-applied without re-deriving. It captures **how a thing is proven** and **exactly what tier the
proof licenses**, not a new physical claim. Every formula is quoted verbatim from its source; every number
is traced; nothing is fabricated.

> **THE ONE LIMIT, STATED UP FRONT.** This module has **two layers with two different epistemic statuses,
> and they must never be quoted as one.** The **beat-dynamics layer (M14-1 through M14-8, M14-11 through
> M14-15)** is self-contained, checkable plasma/field mathematics -- symbolic proofs, mesh-converged
> eigensolves, and closed-form identities -- and stands **whether or not any nuclear claim is ever true.**
> The **nuclear/energetics layer (M14-9 magnetic-tension Rayleigh fission, M14-10 Gamow/ponderomotive
> ledger)** is a **pre-registered TARGET with a named open gap** (a mean Coulomb-explosion release
> `1.27x` *below* the free-proton threshold; a field anchor `B = 1000 T` the source itself flags as
> unconfirmed; a "one-in-three" figure that is a kinetic-energy fraction, **not** a shed fraction), built
> on **Greenyer's own baryon-decay (Callan-Rubakov monopole-catalysis) proposal, which this module tiers
> `[framework: Greenyer/MFMP]` -- a taken-as-given hypothesis, not a result of ours.** The falsifiable
> population band `N_crit ~ 1.7-3e11` is a **`[prediction]`**, never a finding. **No over-unity is claimed
> or implied anywhere** (the LENR ledger is a barrier-budget/selective-release bookkeeping, not an energy
> balance). And the load-bearing conflation to avoid: the **continuous** helicity functional scales as
> `N^(-4L)` and is NOT conserved across the cascade; only the **discrete integer** winding/linking number
> is exactly conserved -- the two are different objects and the sources flag every place the language slips.

## Tier legend (honesty discipline)
- **[V]** verified in-project by a named computation: a symbolic proof (SymPy), a mesh-converged FEM
  eigensolve, a checked identity, or an exact dimensional reduction. Trustworthy at the stated precision.
- **[credited]** established physics/mathematics we build on (textbook or primary-source, cited).
- **[V-dim]** dimensionally verified (units close), value not independently derived.
- **[S]** structural / numerically-supported / cited-convergence, not closed on our side.
- **[framework: Greenyer/MFMP]** the fractal-toroidal geometry, the EVO geometric anchors (Shoulders'
  `n_e, R, a, epsilon`), and the baryon-decay nuclear channel -- **taken as given from Greenyer/MFMP.**
  Our layer proves what the geometry *does*; it does **not** claim the geometry or the nuclear proposal.
- **[prediction]** a falsifiable, pre-registered number or band. **Explicitly NOT a result.**
- **[flagged]** a coincidence / near-match held for the record, not promoted.
- **[reject]** fabricated / refuted -- named so it is never resurrected.

**Primary source docs integrated (each traced per method).**
- `ICCF27_greenyer_beat_qhd_essentialized_v6e.pdf` -- Hanks, "Beat Dynamics and Quantum Hydrodynamics on
  Greenyer's Fractal Toroidal Geometry: First Results for Plasma Tori" (prepublication v6e, 2026). The
  proof layer: Secs. 2 (structural results), 3 (Beat Law / ladder / triplet algebra), 4 (Madelung bridge),
  5 (anchors), 6 (nuclear, on its own terms), 7 (pre-registered checks). **-- M14-1..M14-10.**
- `EVO_MATHEMATICAL_CORE.md` -- "EVO-Mediated Nuclear Phenomena: Mathematical Core" (v1.0, 2026-06-20). The
  concrete THz-cascade realization with numbers: Secs. 3 (Beltrami anchor), 5 (beat-law hierarchy / D-4D
  cascade), 7-8 (Gamow / ponderomotive), 9 (anapole sustaining). **-- M14-7, M14-9, M14-10.**
- `TORUS_MATHEMATICS_APPENDIX.md` -- "Torus Mathematics Appendix" (2026-07, Parts 1-45). The reusable
  Beltrami/helicity toolkit and its checked negatives: Part 5-7 (beat/three-wave/Adler), Part 25 (MRxMHD),
  Part 34 (Hopf), Part 35 (N-mode Woltjer), Part 39 (off-resonance), Parts 40-43 (l=1/l=2 closed forms,
  orthogonality). **-- M14-11..M14-15.**

**Established literature cited (per method below):** Chandrasekhar-Kendall 1957; Woltjer 1958; Taylor 1974;
Moffatt 1969; Madelung 1927 / Bohm 1952; Manley-Rowe 1956; Zel'dovich 1957; Rayleigh 1882 (fissility) /
Rayleigh 1878 (jet instability); Last-Levy-Jortner 2002; Brillouin 1945; Chandrasekhar-Fermi 1953 (virial);
Cantarella-DeTurck-Gluck-Teytel 2000 (CDG); Hudson-Hole-Dewar 2007 (MRxMHD); Arnold-Khesin 1998; Callan
1982 / Rubakov 1981 / Wilczek 1982; Hsu-Zhen-Stone-Joannopoulos-Soljacic 2016 (BIC); Nicolis-Prigogine 1977;
Fano 1961; Mathieu 1868. Full ledger reproduced at the end.

---

## M14-1 -- THE BEAT LAW and the CASCADE LADDER-INDEPENDENCE THEOREM   [V / credited]

**WHAT.** Two nested force-free (Chandrasekhar-Kendall) tori relaxed at fixed helicity carry two lowest
eigenmodes (a "doublet", `lambda_0, lambda_1`); their superposition beats at the difference frequency.
Bending the spherical doublet into a torus splits it by a shape-set amount, giving a beat frequency that
scales as `a^2/R^3`. The load-bearing theorem is not the beat law itself but its **cascade behaviour**: for
a self-similar stack `R_L = R_0/N^L` at fixed aspect ratio, the beat frequencies form an **exact geometric
ladder `N^L`, independent of the (unknown, shape-dependent) coefficient function** -- the one result the
whole spectral fingerprint rests on, and it needs no knowledge of the coefficient.

**MATH.** (verbatim, PDF Sec. 3.1, eqs. (1)-(2); torus appendix Part 5 CALC 3.)
```
splitting        Delta lambda  ~  C a^2 / R^3 ,     C ~ 0.2654
Beat Law (1)     f_b = C v_eff a^2 / (2 pi R^3)
shape function   c_CK(epsilon) = (lambda_1 - lambda_0) / epsilon^2      [10-pt mesh-converged sweep]
ladder thm (2)   f_b(L) / f_b(0) = N^L   exactly, for an ARBITRARY functional form of c_CK(epsilon)
```
Proof of (2) (verbatim): "the cascade's own scaling gives `epsilon_L = a_0/R_0` identically at every level,
so `c_CK` is always evaluated at the same argument and `f_b(L)/f_b(0) = N^L` exactly." I.e. **fixed aspect
ratio pins the coefficient to one fixed value at every rung, so it cancels in the ratio** -- this is the
"shape-factor independence" the task names. Condition (torus appendix Part 5 CALC 3): the ladder holds
"provided `v_eff` is scale-invariant across the cascade" -- a stated, named assumption.

The mesh-converged `c_CK(epsilon)` sweep (PDF Sec. 3.1), reproduced verbatim:
```
 epsilon   lambda_0   lambda_1   c_CK
 0.05      48.106     48.117     4.160
 0.10      24.065     24.086     2.084
 0.20      12.056     12.098     1.0486
 0.30       8.064      8.128     0.707
 0.697      3.577      3.735     0.3245
```
Shape sensitivity: `d(ln c_CK)/d(ln epsilon) = -0.969` (full fit) -- `c_CK` scales close to `1/epsilon`.

**Tier.** **[V]** for the ladder theorem `f_b(L)/f_b(0)=N^L` (symbolic, torus appendix Part 5 CALC 3; and
PDF proves it "for an arbitrary functional form", so it is a genuine algebraic identity, not a fit) and for
the mesh-converged `c_CK(epsilon)` sweep (single-method, convergence 0.003% at the spot-checked point).
**[credited]** for the Chandrasekhar-Kendall force-free eigenvalue basis `curl B = lambda B` the doublet
lives in (Chandrasekhar-Kendall 1957; Woltjer 1958).

**Flags / conflicts (stated, not papered over).**
1. **Coefficient normalization is internally ambiguous.** The `Delta lambda ~ C a^2/R^3` form (verbatim)
   implies a `~epsilon^2` splitting, but the same section's own sweep gives `c_CK(epsilon) ~ 1/epsilon`,
   i.e. the *dimensionless* split `c_CK * epsilon^2 ~ epsilon` (checked: `c_CK * epsilon = 0.208-0.226`
   across the table, near-constant, **not** equal to the stated `C = 0.2654`). The two normalizations are
   not explicitly reconciled in the source. **This does not touch the ladder theorem** (which holds for any
   `c_CK`), which is exactly why the theorem is the load-bearing result and `C` is not.
2. **A `2 pi^2` typo in the beat-law prefactor was caught and fixed** (torus appendix Part 5 CALC 3,
   2026-07-24); the canonical form is `2 pi R^3` as in eq. (1) above. Harmless to the ladder (any constant
   prefactor cancels in the ratio), but wrong as a standalone formula before the fix.

**Source.** PDF Secs. 3.1-3.2; `TORUS_MATHEMATICS_APPENDIX.md` Part 5 CALC 3, Part 12 (FEM eigensolve
cross-check vs slender-torus Bessel asymptotic `lambda_0 ~ j_01/epsilon`). Cite Chandrasekhar-Kendall
ApJ 126, 457 (1957); Woltjer PNAS 44, 489 (1958).

---

## M14-2 -- THE HEARTBEAT THEOREM: every persistent beat is DRIVEN, never static   [V / credited]

**WHAT.** A single-region multi-mode force-free object cannot host a *static* beat. Fixed-helicity energy
minimization over any set of distinct-eigenvalue Beltrami modes is a **linear program whose minimizer is a
vertex** -- a single pure lowest-`lambda` mode -- so **no genuine mixture is even a critical point.** Any
persistent inter-level beat is therefore a **driven/dissipative structure**, alive only while regeneration
outpaces Taylor relaxation. This is the reusable "you must feed it" theorem for the whole toolkit.

**MATH.** (verbatim, torus appendix Part 35, the N-mode generalization of the PDF Sec. 2.2 doublet result.)
```
N orthonormal Beltrami modes,  lambda_1 < ... < lambda_N ,   B = sum_i c_i A_i ,   x_i = c_i^2 >= 0
minimize   E = (1/2) sum_i x_i     subject to fixed helicity   h_1 = sum_i x_i / lambda_i
=> a linear program; stationarity  c_i (lambda_i - 2 mu) = 0  => minimum at a vertex (one nonzero x_i),
   necessarily the smallest lambda_i.
```
So "undisturbed Taylor relaxation always drives it to the single lowest-eigenvalue mode, discarding every
other mode present." A 50/50 doublet mixture sits above ground state by a computed excess (`7.9%` for the
locked doublet; `1.15%` for the 6-mode WIDE40 cluster).

**Tier.** **[V]** -- verified two independent ways (SymPy for `N=4`; `scipy.optimize.linprog` on the real
40-mode WIDE40 spectrum, reproducing the closed-form pure-lowest-mode energy exactly). **[credited]** for
the underlying Woltjer/Taylor minimum-energy relaxation principle (Woltjer 1958; Taylor 1974) and the
dissipative-structure reading (Nicolis-Prigogine 1977). Physically apposite modern family named in the PDF:
continuous/dissipative time crystals (cited to import injection-locking machinery, not to claim identity).

**Source.** PDF Sec. 2.2; `TORUS_MATHEMATICS_APPENDIX.md` Part 35 (promoted result), Part 25/Sec.196
(the `N=2` case). Ties directly to M10 (Woltjer invariant) and M9 (injection locking / Adler). Cite Taylor
PRL 33, 1139 (1974); Woltjer PNAS 44, 489 (1958); Nicolis-Prigogine, *Self-Organization in Nonequilibrium
Systems* (Wiley 1977).

---

## M14-3 -- THE TRIAD DICHOTOMY: integer silence vs golden-ratio resonance   [V / credited]

**WHAT.** Pairwise beats carry no energy; real transfer is three-wave (a triad `omega_n = omega_i +
omega_j`). Whether a self-similar cascade can triad *among its own levels* is decided by pure arithmetic and
is **exactly dichotomous**: an **integer** ratio `N` can **never** internally phase-match; the **golden
ratio** `phi` **always** does, because the golden-ratio identity **is** the matching condition. This is the
sharpest, most checkable structural result in the synthesis.

**MATH.** (verbatim, PDF Sec. 3.3.)
```
integer impossibility:   for integer N, phase matching requires   N^i - N^j == -1  (mod N)   -- UNSATISFIABLE
                         (an integer cascade can never triad among its own levels)
golden-ratio matching:   for N = phi,   phi^n = phi^(n-1) + phi^(n-2)   IS the matching condition,
                         so every consecutive level triple is exactly phase-matched.
```
Verbatim rider: "the golden-ratio cascade preserves every other theorem of this paper unchanged (checked
directly)." Concrete computed triplet on the geometry (verbatim): g-equivariant four-ring chain,
`M13 = M24 = -4.402e-7 H`, `kappa13 = 5.01%`, spectrum `omega/omega_0 = 0.9755, 1.0003, 1.0261`, whose
quasi-periodic envelope has structure at two independent gaps (ratio `1.0403`, not a simple rational) --
"the genuine fingerprint of a triplet, where a doublet gives one simple beat."

**Tier.** **[V]** -- both halves are elementary number theory over the cascade ratio, directly checkable
(the `mod N` non-residue statement and the Fibonacci/`phi` recursion). The concrete triplet is a computed
example. **[credited]** engineering precedent cited *to be distinguished, not conflated*: stellarators
choose noble (golden-mean-class) irrationals precisely to *avoid* low-order resonances (Hanson-Cary 1984) --
the same arithmetic run in reverse; and it is explicitly distinguished from Shenker-Kadanoff KAM locking
(external forcing, a different question).

**Source.** PDF Sec. 3.3. Cite Hanson-Cary, Phys. Fluids 27, 767 (1984); Shechtman et al. PRL 53, 1951
(1984) (quasicrystals, golden-ratio order made respectable, cited as cultural precedent). Feeds M9
(three-wave / parametric coupling).

---

## M14-4 -- THE TRIAD NETWORK: exactly two Manley-Rowe invariants, Fibonacci coefficients, two thresholds   [V / credited]

**WHAT.** Chaining the phase-matched triads (levels 0-8, seven triads) into a network gives three checkable
facts: (a) it conserves **exactly two** Manley-Rowe-class invariants for **any** chain length -- and the
count "2" is a *theorem* (a rank argument), not an observation; (b) the invariants' **basis coefficients are
literally the Fibonacci numbers** (the golden-ratio recursion of M14-3 reappearing inside the conservation
laws); (c) the onset is **two-staged with no exceptional point**.

**MATH.** (verbatim, PDF Sec. 3.4.)
```
invariant count (theorem):  each triad (n, n-1, n-2) contributes a strictly new pivot row to the
                            stoichiometric matrix S, so rank(S) = L identically, and the number of
                            conserved Manley-Rowe quantities = (L + 2) - L = 2   for every chain length
                            L >= 1   (swept to 128, no exception).
Fibonacci basis:            the two invariants' basis coefficients are literally Fibonacci numbers:
                            ( 21, 13, 8, 5, 3, 2, 1, 1, 0 )   and   ( 13, 8, 5, 3, 2, 1, 1, 0, 1 ),
                            with alternating sign  -- the triad recursion IS the Fibonacci recursion.
two thresholds, no EP:      discriminant  D = ((gamma_6 - gamma_7)/2)^2 + (kappa A_0)^2   -- a sum of
                            non-negative terms => NO exceptional point at any coupling
                            (proven over kappa/gamma_0 in [1e-1, 1e6]).
                            Exact linear growth threshold at  kappa/gamma_0 = 22.8 ;
                            full visible cascade onset at  kappa/gamma_0 ~ 300-1000.
```
The base three-wave amplitude equations and the two Manley-Rowe conservation laws are independently derived
and symbolically verified in the torus appendix (see M14-11).

**Tier.** **[V]** -- the invariant-count rank argument and the Fibonacci coefficient list are exact algebra;
the "no exceptional point" statement is a positive-discriminant proof plus a numerical Jacobian cross-check
(`kappa/gamma_0 = 1, 1e3, 1e5`). **[credited]** for the Manley-Rowe relations themselves (Manley-Rowe 1956)
and the coupled-mode / synchronization framing (Haus 1984; Kuramoto 1984; Strogatz 2000).

**Source.** PDF Sec. 3.4; `TORUS_MATHEMATICS_APPENDIX.md` Part 6 CALC 1 (exact Manley-Rowe conservation,
symbolic). Cite Manley-Rowe, Proc. IRE 44, 904 (1956).

---

## M14-5 -- THE LINKING / BIC SELECTION RULE: a symmetry-protected structural zero, linearly restored   [V / credited]

**WHAT.** Whether two doublet members can exchange energy is decided by a mirror. Their coupling is
proportional to a chirality/linking factor that **vanishes identically** when the two modes are related by a
current-reversing mirror symmetry -- a **structural zero** (confirmed to 50 decimals), i.e. a **bound state
in the continuum (BIC)**. Breaking the symmetry restores a real coupling, and the restoration law is
**measured, not assumed**: linear (`kappa ~ c_z`, exponent `p ~ 1.00`), the generic exponent for a single
protecting symmetry.

**MATH.** (verbatim, PDF Sec. 2.1.)
```
protected zero:   coupling ~ chirality/linking factor = 0 identically under current-reversing mirror
                  symmetry   -- structural zero to 50 decimal places (not a small number).
restoration:      sweeping the protecting parameter c_z (out-of-plane displacement of the 2nd loop center)
                  over 13 points across 5 decades,   kappa ~ c_z^p  with  p = 1.0000 (asymptotic windows;
                  0.9987 all points)  -- exactly linear, out to half the loop radius.
surveyed range:   kappa = 0.08% - 0.98%  across surveyed geometries;   kappa = 0.4215% at c_z = 0.3.
```

**Tier.** **[V]** -- a computed structural zero (50-digit) plus a 13-point power-law fit with a clean
generic exponent; the linear vanishing "rules out any hidden second protection." **[credited]** for the BIC
concept (Hsu-Zhen-Stone-Joannopoulos-Soljacic 2016).

**Source.** PDF Sec. 2.1 (and Fig. 2). Cite Hsu et al., Nat. Rev. Mater. 1, 16048 (2016).

---

## M14-6 -- THE ANAPOLE IDENTITY and the JUNCTION-POLE LAW (fractal-invariant multipoles)   [V / credited / framework]

**WHAT.** The structure is electromagnetically quiet outside **because of what it is**: the poloidal winding
realizes an **anapole (toroidal-dipole)** -- Zel'dovich's confined-field configuration -- with the ordinary
dipole cancelling exactly. Crucially, the multipole content is **invariant under fractal resolution** (a
torus, its six-sub-tori rebuild, and three recursion levels give the *same* multipoles), and the
toroidal-dipole strength falls by an exact `N^4` per cascade level. Where levels meet, a calculable
pole-phenomenology lives, governed exactly by the flux discontinuity.

**MATH.** (verbatim, PDF Secs. 2.4-2.5, 4.3.)
```
anapole construction:   wound toroidal sheet (I = 100 A, R = 1 m, a = 0.3 m) gives
                        T = 8.4823 A . R^3 ,   residual dipole |m| ~ 1e-15
fractal invariance:     identical multipoles on rebuild as 6 sub-tori and through 3 levels of recursion
                        -- "exactly invariant under fractal resolution"
cascade of the pole:    twin-core cascade gives m_L = 0 at machine precision at every level L = 0..4,
                        with   T_L / T_(L+1) = 256.0000 = N^4   exactly   (1024.0000 = N^5 alt. convention)
radiation silence:      omega R/c ~ 8.17e-4 ,  suppression (omega R/c)^2 ~ 6.7e-7 ,  n_poloidal ~ 0.49
junction-pole law:      effective pole strength of any junction = its magnetic-flux discontinuity  Delta Phi
                        (= 0 for the smooth closed structure; real & Biot-Savart-computable at gap defects)
field decay:            ideal closed anapole  p = 13.84  vs  real level junction  p = 2.20 (= ideal pole r^-2)
helicity vs winding:    continuous helicity functional  H(L)/H(0) = N^(-4L)   (shrinks fast);
                        integer winding/linking number  = EXACTLY conserved across the cascade
```

**Tier.** **[V]** for the explicit-construction multipoles (`T = 8.4823 A R^3`, `|m| ~ 1e-15`), the
fractal-invariance check, the exact ratio `T_L/T_(L+1) = N^4`, and the continuous-helicity scaling
`N^(-4L)` (also derived independently in torus appendix Part 5 CALC 4 from `lambda_L = lambda_0 N^L` and
`H = (1/lambda) integral |B|^2`). **[credited]** for the anapole/nonradiating-source physics (Zel'dovich
1957; Devaney-Wolf 1973; Radescu-Vaman 2002) and the `Lk = Tw + Wr` topology keeping winding-number and
continuous-helicity distinct (Arnold-Khesin 1998). **[framework: Greenyer/MFMP]** that this anapole IS the
active EVO structure.

**Flag (load-bearing, appears in both the PDF and the torus appendix).** The `N^(-4L)` **continuous**
helicity decay must **not** be quoted as "helicity is conserved across the cascade." That statement is true
**only** of the **discrete integer** winding/linking charge. This is the single most-repeated honesty flag
in the sources; carry it verbatim. The junction-pole law's named threshold for any genuinely topological
(interior-monopole) reading is `B >= 2.24e8 T at fermionic tube radii` -- stated in advance as the bar to
clear, not claimed met.

**Source.** PDF Secs. 2.4, 2.5, 4.3; `TORUS_MATHEMATICS_APPENDIX.md` Part 5 CALC 4. Cite Zel'dovich, JETP 6,
1184 (1958); Devaney-Wolf PRD 8, 1044 (1973); Radescu-Vaman PRE 65, 046609 (2002); Dubovik-Tugushev
Phys. Rep. 187, 145 (1990); Arnold-Khesin, *Topological Methods in Hydrodynamics* (Springer 1998).

---

## M14-7 -- THE THz-CASCADE REALIZATION: concrete numbers for the beat ladder   [S / framework / credited-coefficient]

**WHAT.** The EVO Mathematical Core instantiates the M14-1 beat law on Shoulders' measured EVO geometry,
giving concrete frequencies. The doublet splitting is written with an **analytically fixed** coefficient
`alpha_CK = 1/2` (the CDG helicity isoperimetric theorem for solid tori), producing a mid-infrared
fundamental and a base-4 cascade ladder. This is the "same law, actual numbers" companion to M14-1.

**MATH.** (verbatim, `EVO_MATHEMATICAL_CORE.md` Secs. 3, 5.)
```
CK-doublet split (Law 1):   omega_0 = alpha_CK * epsilon^2 * omega_A ,     alpha_CK = 1/2
                            (alpha_CK = 1/2 is the CDG solid-torus helicity isoperimetric theorem, exact)
Alfven anchor:              omega_A = lambda_1 * v_A = (3.60 / R) v_A ,   v_A = sqrt(2/5)(1 + eps^2/2q^2) v_F
numerical fundamental:      omega_0 = (1/2)(0.20)^2 (8.226e15) = 1.645e14 rad/s = 0.2163 eV/hbar
                            => f_b = omega_0/2pi = 52.286 THz   (mid-IR, lambda = 5.734 um)
D-4D cascade ladder:        omega_L = omega_0 * 4^L ,        r_L = R / 4^L        (L = 0..5)
```
Geometric anchors (fixed inputs, Shoulders' morphology): `n_e = 1e33 m^-3`, `R = 10 nm`, `a = 2 nm`,
`epsilon = a/R = 0.20`, `lambda_tilde_1 = 3.60` (first CK mode). Derived: `E_F = 3646 eV`, `v_F = 0.1195 c`,
`v_A = 0.637 v_F = 2.282e7 m/s`, virial field cap `B_virial = sqrt((4/5) mu_0 n_e E_F) = 7.66e5 T`.

**Tier.** **[credited]** for `alpha_CK = 1/2` (Cantarella-DeTurck-Gluck-Teytel, J. Math. Phys. 41, 5615
(2000); project Calc #15 TVR-PASSED) and the CK/Alfven force-free machinery. **[S]** for the specific beat
frequency and cascade numbers, since they inherit the **[framework: Greenyer/MFMP]** geometric anchors
(`n_e, R, a` from Shoulders' measurements, only partially derived in the source: `n_e` to 0.81%, `epsilon`
to 0.15%, `R` accepted as an empirical input). The EUV cascade lines (`L=4: 55.4 eV`, `L=5: 221.4 eV`) are
**[prediction]** ("predicted spectral line", zero free parameters given the anchors).

**Conflict (stated).** The base rung differs between docs: `EVO_MATHEMATICAL_CORE.md` gives
`f_b(0) = 52.286 THz`; the PDF (Sec. 3.2) gives `f_b(0) ~ 477 THz` "from the network analysis of 3.4". The
ratio `477/52.286 = 9.12` is **not** a clean power of `N=4`; the two use different CK normalizations
(cylindrical `lambda_tilde_1 = 3.60` vs spherical `z_(1,1) = 4.4934`) and different `v_eff`/geometry. **The
ladder law `N^L` is the shared, robust object; the absolute base frequency is convention-dependent and the
two values should not be quoted interchangeably.**

**Source.** `EVO_MATHEMATICAL_CORE.md` Secs. 2, 3, 5. Cite Cantarella-DeTurck-Gluck-Teytel JMP 41, 5615
(2000); Chandrasekhar-Kendall 1957; Lundquist 1950.

---

## M14-8 -- THE MADELUNG (QHD) BRIDGE: beat = interference, and the exact Reed 9/8 mu_B theorem   [V / credited]

**WHAT.** The Madelung transform rewrites the field superposition as a fluid, `hbar`-independently, and
reproduces the direct electrodynamics to four decimals -- the precise, checked sense in which
"quantum-hydrodynamic" language is legitimate here with nothing smuggled in. Two exact riders: the beat
**is** wave interference; and Reed's precessing-charge electron moment collapses, from his own stated
geometry, to a closed-form `9/8 mu_B`.

**MATH.** (verbatim, PDF Secs. 4.1-4.3.)
```
transform:        psi = sqrt(rho) e^{iS}  ->  fluid (rho, grad S) ;  matches direct electrodynamics to 4 dp
beat = interference:   |e^{-i lambda_0 t} + e^{-i lambda_1 t}|^2 = 2 + 2 cos((lambda_1 - lambda_0) t)
                       -- |Psi|^2 beats at exactly  omega = lambda_1 - lambda_0
Reed theorem:     mu_avg = mu_B ( 1 + (1/2)(R_p/R_C)^2 ) = (9/8) mu_B   for  R_p/R_C = 1/2
                  key step:  R_C omega_C = c (def. of reduced Compton radius) collapses (e/2)R_C^2 omega_C
                  to exactly mu_B ; numerical trajectory integral agrees to 0.044%.
winding vs helicity:   smooth Madelung bulk flow can NEVER be a nontrivial Beltrami field
                       (curl grad S = 0); vorticity lives only on quantized vortex-line singularities.
```

**Tier.** **[V]** -- the interference identity is elementary and exact; the `9/8 mu_B` result is "a theorem,
derived symbolically, not a fit" (numerical check 0.044%); the four-decimal Madelung/electrodynamics match
is computed. The `curl grad S = 0` "never Beltrami" result is a standard vector identity, verified
symbolically (torus appendix Part 5 CALC 1); **its charged-flow correction** `curl v = -(q/m) B` (minimal
coupling) is also exact (Part 5 CALC 5) -- real bulk vorticity for a charged Madelung flow, though "not
automatically Beltrami" (needs `B || v`). **[credited]** Madelung 1927 / Bohm 1952; Onsager 1949 / Feynman
1955 (quantized circulation); the Reed cross-check cites Reed's *Quantum Wave Mechanics* Ch. 17.

**Source.** PDF Secs. 4.1-4.3; `TORUS_MATHEMATICS_APPENDIX.md` Part 5 CALC 1, CALC 5. Cite Madelung Z. Phys.
40, 322 (1927); Bohm Phys. Rev. 85, 166 (1952); Onsager (1949); Feynman (1955).

---

## M14-9 -- MAGNETIC-TENSION RAYLEIGH FISSION and the falsifiable N_crit band   [credited-mechanism / prediction / framework]

**WHAT.** The one missing nuclear-adjacent ingredient in Greenyer's channel -- *selective* release of net
charge rather than uniform Coulomb explosion -- is supplied by a **classical** mechanism: a charged drop
above the Rayleigh limit does not explode, it **fine-fissions** (ejects jets carrying ~30-40% of the charge,
~1% of the mass). The **one new step** is to use **magnetic confinement tension as the effective surface
tension**. This reduces the entire nuclear-energetics question to a single **falsifiable population band**.

**MATH.** (verbatim, PDF Sec. 6.3, eq. (3); Rayleigh 1882 / Last-Levy-Jortner 2002.)
```
fissility (credited):     X = Q^2 / (64 pi^2 gamma epsilon_0 R^3)          [Rayleigh 1882]
magnetic surface tension: gamma_eff = (B^2 / 2 mu_0) R                     [ "both halves textbook,
                                                                             their combination new" ]
magnetic Rayleigh limit:  N_R = 1.178e9 net electrons  (R ~ 2 um, f_net ~ 0.71%, B = 1000 T)
critical population (3):  N_total,crit ~ 1.66e11
falsifiable band:         persistent gentle fission requires  N_total in  1.7 - 3 e11 ;
                          1e12 - 1e13  predicts  83-98% shed = one catastrophic disruption, not persistence.
l=2 dispersion (rate):    omega_2^2 = (8 gamma_eff / rho R^3)(1 - X)
                          => tau = 67 fs (electron inertia) or 2.9 ps (proton-dominated),
                             factor sqrt(m_p/m_e) ~ 43 apart; both > light-crossing R/c ~ 6.7e-15 s;
                             omega_2 = 0 identically at X = 1  (required consistency check).
```

**Tier.** **[credited]** for the physics halves: the Rayleigh fissility `X` (Rayleigh, Phil. Mag. 14, 184
(1882)), the Rayleigh-Plateau / charged-drop fine-fission dichotomy (Last-Levy-Jortner, PNAS 99, 9107
(2002)), and magnetic surface tension `gamma = (B^2/2 mu_0) R` (standard magnetic-tension bookkeeping). The
**combination** (magnetic tension AS the drop's surface tension) is the source's own **[S] new step**. The
`l=2` dispersion is the standard Rayleigh capillary-instability quadrupole mode with `gamma -> gamma_eff`;
it passes the `omega_2=0 at X=1` and light-crossing consistency checks **[V-dim]**.
**The band `N_crit ~ 1.7-3e11` is a `[prediction]`, NOT a result** -- a pre-registered, falsifiable target
that "lands untuned at the low edge of the independently reported range" (Shoulders' `1e11-1e13`).

**Flags (the source's own, carried verbatim).** (1) `B = 1000 T` is "the program's general anchor, not
independently confirmed here." (2) The "one net electron in three clears the threshold" figure (Sec. 6.2) is
"a kinetic-energy fraction, not a shed fraction -- the two are not to be conflated." (3) The mean
Coulomb-explosion release stands `1.27x below` the free-proton capture threshold (782,332 eV) -- **a gap,
stated as a gap.** No over-unity anywhere.

**Source.** PDF Secs. 6.2-6.3. Cite Rayleigh Phil. Mag. 14, 184 (1882); Last-Levy-Jortner PNAS 99, 9107
(2002); Brillouin Phys. Rev. 67, 260 (1945); Chandrasekhar-Fermi ApJ 118, 116 (1953).

---

## M14-10 -- THE GAMOW / PONDEROMOTIVE LENR LEDGER (barrier budget, on the framework's own terms)   [S / framework]

**WHAT.** The EVO Mathematical Core keeps a term-by-term **Gamow-exponent budget** for the D+D channel and a
**ponderomotive density-enhancement** ledger. It is a barrier-penetration / density bookkeeping, **not** an
energy balance -- no over-unity is asserted. Preserved here as a method (how to tabulate a barrier budget),
tiered at framework level because the anchors are Greenyer/Shoulders inputs.

**MATH.** (verbatim, `EVO_MATHEMATICAL_CORE.md` Secs. 7-8.)
```
Gamow exponent:      G = integral_{r_turn}^{r_nucl} k(r) dr    (tunneling prob ~ exp(-2G))
bare / screened:     G_bare = 62.14 ;  G_Yukawa = 53.07 (Thomas-Fermi screening) ;  G_required <= 32.9
budget close:        G_total = G_Yukawa + dG_B + dG_ring = 53.07 - 8.17 - 12.26 = 32.64  <= 32.9
                     (P1 "closed" with margin 0.26 Gamow units)
ponderomotive:       delta n/n = (1/2)(omega_c / omega_5)^2 ;  chirp-up closure delta n/n(eta)
                     = delta n/n_0 (1/(1-eta))^4  -> 5.60% contraction closes 1.191% -> 1.50%
Floquet-Mathieu:     x'' + omega_5^2 (1 - eta_d cos 2 omega_5 t) x = 0 ,  threshold eta_c = 2/Q_5 = 0.1399
```

**Tier.** **[S] / [framework: Greenyer/MFMP]** throughout -- these are internal barrier-budget closures on
Shoulders-anchored geometry, using standard WKB/Thomas-Fermi/Mathieu machinery **[credited]** but
project-specific reduction terms (`dG_ring`, `dG_B`) that are model constructions. The "P1 CLOSED (margin
0.26)" statement is a **[framework]** internal bookkeeping result, explicitly **not** promoted to a rate or
a cross-section. The remaining external gate named in the source is an NCSM `4He*` resonance verification --
**[prediction]/pending**, not delivered.

**Source.** `EVO_MATHEMATICAL_CORE.md` Secs. 7-10. Cite standard WKB/Gamow; Thomas-Fermi screening; Mathieu
(1868); Pastore et al. (2013) (MEC). Baryon-conservation caveat: this ledger is baryon-agnostic D+D bookkeeping;
Greenyer's baryon-decay channel (M14-16 limits) is a separate **[framework]** proposal.

---

## M14-11 -- NONLINEAR THREE-WAVE DYNAMICS: amplitude Manley-Rowe + Adler phase-locking   [V / credited]

**WHAT.** The linear beat is the weak-coupling limit of a standard lossless three-wave system; turning on
coupling gives genuine pump-depletion energy transfer, a sharp parametric threshold, and (for the phases) an
Adler-class locking condition. This is the reusable nonlinear engine under M14-3/M14-4, with the coupling
constant `kappa` **derived** from the same eigenvalue splitting that sets the linear beat -- not a free
parameter.

**MATH.** (verbatim, torus appendix Parts 6-7.)
```
three-wave (lossless):   dot A_0 = -i kappa A_1 A_2* ,  dot A_1 = -i kappa A_0 A_2 ,  dot A_2 = -i kappa A_0* A_1
Manley-Rowe (exact):     N_0 + N_1 = const ,  N_1 + N_2 = const     (N_j = |A_j|^2 ; symbolic)
parametric threshold:    |A_1|^2_crit = gamma_0 gamma_2 / kappa^2
growth rate:             Gamma = -(gamma_0 + gamma_2)/2 + sqrt( ((gamma_0 - gamma_2)/2)^2 + kappa^2 |A_1|^2 )
coupling origin:         (J x B)_cross = (A_0 A_1/mu_0)(lambda_0 - lambda_1)(B_0 x B_1)
                         -- EXACTLY zero if lambda_0 = lambda_1 ; kappa ~ the same Delta lambda as the beat.
phase equation (Adler):  dot theta = -Delta + kappa cos theta [ sqrt(N_0 N_1/N_2) - sqrt(N_0 N_2/N_1)
                                                                 + sqrt(N_1 N_2/N_0) ]
locking condition:       fixed point (dot theta = 0) exists iff  |Delta| <= kappa K
```

**Tier.** **[V]** -- Manley-Rowe conservation verified symbolically; the threshold and growth rate are the
textbook parametric-decay forms, cross-validated numerically (sub- vs super-threshold, ~9 orders of growth
separation); the `kappa` origin is derived from the cross Lorentz force (`kappa` proportional to the
eigenvalue splitting is a genuine, non-free result). **A named self-correction** is logged in the source:
the phase-equation prefactor is `cos theta`, not the initially-expected `sin theta` (direct derivation beat
a "sounds-standard" recalled form) -- carry the `cos theta` form. **[credited]** Manley-Rowe 1956; the
Adler/injection-locking and tearing-mode-locking kinship (Adler; Fitzpatrick 1993, cited as same
mathematical *form*, not same physical origin).

**Source.** `TORUS_MATHEMATICS_APPENDIX.md` Parts 6 (CALC 1-5), 7 (CALC 1-3). Feeds M9. Cite Manley-Rowe
Proc. IRE 44, 904 (1956); Fitzpatrick, Nucl. Fusion 33, 1049 (1993).

---

## M14-12 -- MRxMHD NESTED-EIGENVALUE STACKS (multi-region relaxed MHD)   [S / credited]

**WHAT.** The single-region CK doublet generalizes to **multiple physically distinct nested regions**, each
its own Beltrami field and eigenvalue `lambda_i`, coupled only through an ideal-interface pressure-balance
condition -- the Hudson-Hole-Dewar MRxMHD construction. This is the machinery for a genuinely *stacked*
cascade (surface currents permitted between levels), as opposed to one continuous field.

**MATH.** (verbatim, torus appendix Part 25.)
```
region 1 (core):    B_z = A1 J_0(lambda_1 r) ,           B_theta = A1 J_1(lambda_1 r)
region 2 (shell):   B_z = A2 J_0(lambda_2 r) + C2 Y_0(lambda_2 r) ,
                    B_theta = A2 J_1(lambda_2 r) + C2 Y_1(lambda_2 r)
interface (p=0):    |B| continuity with direction free  (tangential jump = surface current permitted)
                    2x2 solve  [J0 Y0 ; J1 Y1] [A2;C2] = |B1| [cos psi ; sin psi] ,  det = -0.248
                    (Wronskian-type => always solvable; continuous family across interface twist psi)
```

**Tier.** **[credited]** for the MRxMHD framework (Hudson-Hole-Dewar, Phys. Plasmas 14, 052505 (2007);
citation content independently verified against the real abstract). **[S]** for use here: "this verifies the
MACHINERY is real and computationally tractable, not a new physical prediction." **Honest scope flag
(verbatim):** a genuine application needs 4 real numbers per region (toroidal flux `Psi_1, Psi_2` and
helicity `K_1, K_2`) that fix `lambda_1, lambda_2` via the true Taylor variational principle -- "any specific
`(lambda_1, lambda_2)` pairing used above is illustrative only." A follow-up (Part 25.5) found the
MST-doublet two-region construction **unstable** (energy extremum always a maximum), spherical ball-lightning
doublet qualitatively different (a real local -- but not global -- minimum). The M14-2 axisymmetric
`n=0/n=1` decoupling extends cleanly across MRxMHD interfaces (Part 25.3b).

**Source.** `TORUS_MATHEMATICS_APPENDIX.md` Part 25. Cite Hudson-Hole-Dewar, Phys. Plasmas 14, 052505 (2007).

---

## M14-13 -- THE HOPF-FIBRATION BELTRAMI NEGATIVE RESULT (a real reusable no-go)   [V / credited]

**WHAT.** The Hopf-fiber-generating field is an **exact** Beltrami eigenfield on the round `S^3` (its field
lines are the Hopf fibers, each pair linked once), but it does **NOT** transfer to this project's flat-`R^3`
setting under stereographic projection. A closed, checked negative -- recorded so the "Hopf constructor" is
not re-attempted as a free source of new flat-space modes.

**MATH.** (verbatim, torus appendix Part 34.)
```
on S^3:     V = d_xi1 + d_xi2  (U(1)-fiber Killing field) satisfies  *dV^flat = -2 V^flat  exactly,
            i.e.  curl_{S^3} V = lambda V ,  lambda = +-2 (unit sphere; +-2/R general).  A genuine
            exact Beltrami/force-free eigenfield -- the simplest one on S^3.
flat R^3:   stereographic pullback  V_R3 = (xz - y,  x + yz,  (1/2)(1 - x^2 - y^2 + z^2))
            has  curl(V_R3) = (-2y, 2x, 2)  -- NOT proportional to V_R3 anywhere.  (Ranada/Kedia
            null-EM-Hopfion route: div B = 0 but three different curl(B)_i/B_i ratios -- also not Beltrami.)
```
Why (verbatim): "curl is not conformally invariant, and stereographic projection is conformal, not
isometric -- there was never a general guarantee the `S^3` eigenfield property would survive the map."

**Tier.** **[V]** -- both the `S^3` eigenfield property (`*dV = -2V`, direct exterior-calculus computation)
and the two independent flat-space failures are exact symbolic checks. **[credited]** for the Hopf/Beltrami
and null-EM-Hopfion background (Arnold-Khesin 1998; Ranada; Kedia et al.). Reusable takeaway: the general
topological fact (any smooth map to the Riemann sphere pulls back a divergence-free `R^3` field with linked
lines) is real, but it is **not** a free source of new flat-space constant-`lambda` CK modes.

**Source.** `TORUS_MATHEMATICS_APPENDIX.md` Part 34. Cite Arnold-Khesin (1998); Rañada-Soler-Trueba (1998).

---

## M14-14 -- CLOSED-FORM FORCE-FREE MODES: the l=2 quadrupole, l=1 doublet, A=B/alpha, and the l=2 selection rule   [V / credited]

**WHAT.** A family of exact, symbolically-verified spherical force-free (CK) modes and identities that the
whole toolkit reuses: the `l=1` doublet in closed form, the vector-potential identity `A = B/alpha` (hence
helicity proportional to magnetic energy), a **new** `l=2` axisymmetric quadrupole mode, mode orthogonality,
and the exact rule that the `l=1` doublet's nonlinear self-interaction couples **only** to `l=2`.

**MATH.** (verbatim, torus appendix Parts 40-43.)
```
l=1 doublet (closed form):   psi = j_1(alpha r) cos theta ,   B_phi(r,theta) = j_1(alpha r) sin theta ,
                             curl B = alpha B verified exactly.
vector-potential identity:   A = B/alpha is already Coulomb-gauge:  curl(B/alpha) = B, div(B/alpha) = 0.
                             => H = integral A.B dV = (1/alpha) integral B^2 dV = (2 mu_0/alpha) E_mag
                                (helicity EXACTLY proportional to magnetic energy for any linear FF field)
l=2 quadrupole (new):        CK construction  B = T phi_hat + (1/alpha) curl(T phi_hat),  nabla^2 T + alpha^2 T = 0
                             T_2 = j_2(alpha r) * 3 sin theta cos theta  =>  curl B_2 = alpha B_2 EXACTLY
                             eigenvalue:  B_r(l=2) ~ (radial) x (3 cos^2 theta - 1) => j_2(alpha R) = 0
                             => alpha = z_(2,1)/R ,  z_(2,1) = 5.763459
orthogonality:               integral B_i . B_j dV = 0 for alpha_i != alpha_j (two independent numerical
                             methods + convergence study) => linear Maxwell forbids inter-mode energy exchange
                             (Poynting cross-term J.E ~ B_i.B_j -> 0); coupling MUST be nonlinear.
l=2 selection rule:          the l=1 doublet's (J x B) self-interaction phi-component factors EXACTLY as
                             sin theta cos theta ~ P_2^1(cos theta) -> couples exclusively to l=2.
```

**Tier.** **[V]** -- every one of these is a SymPy-verified exact identity or a convergence-checked numerical
integral (the `l=2` mode "verified by direct substitution into the defining PDE, not by analogy"; the `A =
B/alpha` and orthogonality identities symbolic; the `l=2` selection rule "confirmed symbolically (general)
and numerically"). **[credited]** for the general Chandrasekhar-Kendall toroidal-generating-function
construction and the Moffatt hydrodynamic-Beltrami identity (`lambda_0 a = 4.493409`, matching Moffatt's
swirled spherical vortex to six decimals -- PDF Sec. 2.3 / torus appendix Part 40).

**Source.** `TORUS_MATHEMATICS_APPENDIX.md` Parts 40, 41, 42, 43 (and Sec. 295 selection rule); PDF Sec. 2.3
(CK-Moffatt identity). Cite Chandrasekhar-Kendall 1957; Moffatt, JFM 35, 117 (1969).

---

## M14-15 -- THE SELF-SIMILAR OFF-RESONANCE THEOREM   [V]

**WHAT.** Adjacent levels of any self-similar frequency cascade are off-resonance by a **fixed,
scale-invariant ratio** set only by the branching ratio `N` and a common quality factor `Q` -- **independent
of which level pair you pick**. This is why a clean geometric comb does not accidentally self-resonate: the
detuning and the natural linewidth both scale as `N^L`, so their ratio is frozen.

**MATH.** (verbatim, torus appendix Part 39.)
```
given:   R_L = R_0/N^L ,  f_L = f_0 N^L  (the M14-1 ladder) ,  each level an oscillator of quality Q
theorem: Delta f / gamma_L = (f_{L+k} - f_L) / (f_L / Q) = Q (N^k - 1) ,   independent of L
         (verified symbolically before use)
```

**Tier.** **[V]** -- a one-line exact algebra, SymPy-checked, mechanism-independent. **Honest limit
(verbatim):** "at the gentlest possible self-similar branching (`N=2`), the ratio reduces to `Q` itself, so
the conclusion is NOT unconditional at the smallest possible step." Numerical content with project `Q`
values (`N=4`): e.g. `Q ~ 586.5` gives ratio `1759.5`; plasma-`Q` estimates (MST) give `~1e6-3e7`; ball
lightning's worst case still `135.8` -- decisively off-resonance in every case.

**Source.** `TORUS_MATHEMATICS_APPENDIX.md` Part 39. Reinforces the M14-3 "integer cascades stay quiet"
result from the resonance-width side.

---

## M14-16 -- THE METHODS TABLE (core output)

| # | Method | What it delivers | Tier | Source |
|---|---|---|---|---|
| M14-1 | Beat Law `f_b=C v_eff a^2/(2pi R^3)` + ladder `f_b(L)/f_b(0)=N^L` for arbitrary `c_CK` | shape-factor-independent geometric frequency comb | **[V]/[credited]** | PDF 3.1-3.2; TORUS Part 5/12 |
| M14-2 | Heartbeat theorem: fixed-helicity min = LP vertex = single pure mode | "every persistent beat is driven, never static" | **[V]/[credited]** | PDF 2.2; TORUS Part 35 |
| M14-3 | Triad dichotomy: `N^i-N^j!=-1 (mod N)` (integer) vs `phi^n=phi^{n-1}+phi^{n-2}` (golden) | exact integer-silence / golden-resonance rule | **[V]/[credited]** | PDF 3.3 |
| M14-4 | Triad network: exactly 2 Manley-Rowe invariants (rank thm), Fibonacci coeffs, no EP | conserved-quantity count + two-stage onset | **[V]/[credited]** | PDF 3.4; TORUS Part 6 |
| M14-5 | BIC linking selection rule: structural zero (50 dp), linear restoration `p~1.00` | symmetry-protected zero-coupling + its breaking law | **[V]/[credited]** | PDF 2.1 |
| M14-6 | Anapole `T=8.4823 A R^3`, fractal-invariant, `T_L/T_{L+1}=256=N^4`, helicity `N^{-4L}` | non-radiating identity + exact cascade multipole law | **[V]/[credited]/[framework]** | PDF 2.4-2.5,4.3; TORUS Part 5 |
| M14-7 | THz realization `omega_0=alpha_CK eps^2 omega_A` (`alpha_CK=1/2`), `omega_L=omega_0 4^L` | concrete beat + cascade numbers (52.3 THz, EUV lines) | **[S]/[framework]/[credited-coeff]** | EVO Secs. 3,5 |
| M14-8 | Madelung bridge: `|Psi|^2` beat identity; exact `mu_avg=(9/8)mu_B` Reed theorem | QHD reading legitimized to 4 dp; interference = beat | **[V]/[credited]** | PDF 4.1-4.3; TORUS Part 5 |
| M14-9 | Magnetic-tension Rayleigh fission: `X=Q^2/(64pi^2 gamma eps_0 R^3)`, `gamma_eff=(B^2/2mu_0)R` | selective-release mechanism + falsifiable `N_crit` band | **[credited]/[S new-step]/[prediction]** | PDF 6.3 |
| M14-10 | Gamow/ponderomotive barrier-budget ledger (`G_total<=G_required`) | how to tabulate a barrier budget (NOT a rate) | **[S]/[framework]** | EVO Secs. 7-8 |
| M14-11 | Three-wave `dot A` system + Manley-Rowe + `|A_1|^2_crit=gamma_0 gamma_2/kappa^2` + Adler | nonlinear engine; `kappa` derived from `Delta lambda` | **[V]/[credited]** | TORUS Parts 6-7 |
| M14-12 | MRxMHD nested stacks (J/Y-Bessel two-region, interface `|B|` continuity) | multi-region cascade machinery (illustrative `lambda`) | **[S]/[credited]** | TORUS Part 25 |
| M14-13 | Hopf negative: `*dV=-2V` on `S^3` but not Beltrami in flat `R^3` | closed no-go; curl not conformally invariant | **[V]/[credited]** | TORUS Part 34 |
| M14-14 | Closed-form `l=1`,`l=2` FF modes; `A=B/alpha`; orthogonality; `l=2` selection | exact reusable mode library + coupling-is-nonlinear | **[V]/[credited]** | TORUS Parts 40-43 |
| M14-15 | Off-resonance theorem `Delta f/gamma_L = Q(N^k-1)`, independent of `L` | why a self-similar comb never self-resonates | **[V]** | TORUS Part 39 |

**Classification.**
- **Checkable proof machinery (trust at stated precision):** M14-1 (ladder), M14-2, M14-3, M14-4, M14-5,
  M14-8, M14-11, M14-13, M14-14, M14-15 -- symbolic proofs, mesh-converged eigensolves, exact identities.
- **Established-physics application (credited mechanism, framework anchors):** M14-6, M14-7, M14-9, M14-10,
  M14-12.
- **Pre-registered prediction, NOT a result:** the `N_crit ~ 1.7-3e11` band (M14-9); the EUV cascade lines
  and NCSM gate (M14-7, M14-10).

---

## M14-17 -- LIMITS (stated prominently)   [V]

This module does **NOT**:
1. **claim any over-unity or any nuclear rate/cross-section/branching magnitude.** M14-9/M14-10 are a
   barrier-budget and a selective-release *bookkeeping*; the mean Coulomb-explosion release sits `1.27x`
   **below** the free-proton threshold -- a **gap**, pre-registered as a target, not closed.
2. **derive the EVO geometry or the nuclear channel.** The fractal-toroidal geometry, the Shoulders
   anchors, and the baryon-decay (Callan-Rubakov monopole-catalysis) channel are **[framework:
   Greenyer/MFMP]** -- taken as given. Our layer proves what the geometry *does* (Secs. 2-5 of the PDF),
   which "stand on their own, independent of the Section 6 gap." The PDF verifies only the *bookkeeping* of
   Greenyer's channel (the `J=0` precondition, charge and baryon-number accounting internal to the
   catalysis); it does **not** establish baryon decay, and this module does not either.
3. **conserve continuous helicity across the cascade.** The **continuous** functional scales as `N^{-4L}`
   (it shrinks); only the **discrete integer** winding/linking number is exactly conserved. Never quote the
   two as one -- the single most-repeated honesty flag in the sources.
4. **fix the beat-law coefficient or the absolute base frequency.** `C ~ 0.2654` (a `~eps^2` normalization)
   and the mesh `c_CK(eps) ~ 1/eps` sweep are not explicitly reconciled; the base rung differs `~9x`
   between docs (52.3 THz vs 477 THz, different CK normalizations). Only the **ladder `N^L`** (coefficient-
   independent) and the shape-*insensitivity* of the ladder are robust.
5. **deliver MRxMHD `(lambda_1, lambda_2)` or a saturated fission field.** The MRxMHD region eigenvalues are
   illustrative pending a real per-region flux/helicity dataset (M14-12); `B = 1000 T` in M14-9 is the
   program's unconfirmed anchor.

**The one load-bearing warning, restated:** the beat-dynamics layer is checkable and self-contained; the
nuclear layer is a pre-registered target on a taken-as-given framework. **Do not let the tier of the first
leak onto the second, and never conflate the continuous helicity `N^{-4L}` with the conserved integer winding
number.**

---

## Per-claim index (M14)
| # | Claim | Tier | Repro / trace |
|---|---|---|---|
| M14-1 | `f_b(L)/f_b(0)=N^L` exact for arbitrary `c_CK`; mesh `c_CK(eps)` sweep, sensitivity `-0.969` | [V]/[credited] | PDF 3.1 eqs (1)-(2); TORUS Part 5 CALC 3 (symbolic), Part 12 FEM |
| M14-2 | fixed-helicity min = LP vertex = pure lowest mode; doublet excess 7.9%, WIDE40 1.15% | [V]/[credited] | TORUS Part 35 (SymPy N=4 + linprog WIDE40) |
| M14-3 | `N^i-N^j != -1 (mod N)` integer no-triad; `phi^n=phi^{n-1}+phi^{n-2}` golden match | [V]/[credited] | PDF 3.3; concrete triad `omega/omega_0=0.9755/1.0003/1.0261` |
| M14-4 | rank(S)=L => exactly 2 Manley-Rowe invariants; Fibonacci coeffs; `D>=0` no EP; thresholds 22.8 / ~300-1000 | [V]/[credited] | PDF 3.4; TORUS Part 6 CALC 1 |
| M14-5 | linking coupling = 0 to 50 dp (BIC); restoration `kappa~c_z^p`, `p=1.0000`; `kappa=0.08-0.98%` | [V]/[credited] | PDF 2.1 (13-pt sweep, 5 decades) |
| M14-6 | `T=8.4823 A R^3`, `|m|~1e-15`; fractal-invariant; `T_L/T_{L+1}=256=N^4`; helicity `N^{-4L}` | [V]/[credited]/[framework] | PDF 2.4-2.5, 4.3; TORUS Part 5 CALC 4 |
| M14-7 | `omega_0=(1/2)eps^2 omega_A=52.286 THz`; `omega_L=omega_0 4^L`; EUV lines | [S]/[framework]/[credited coeff] | EVO Secs. 3,5; alpha_CK=1/2 CDG (Calc #15) |
| M14-8 | `|Psi|^2=2+2cos((lambda_1-lambda_0)t)`; `mu_avg=(9/8)mu_B` (0.044%); Madelung 4 dp | [V]/[credited] | PDF 4.1-4.3; TORUS Part 5 CALC 1/5 |
| M14-9 | `X=Q^2/(64pi^2 gamma eps_0 R^3)`, `gamma_eff=(B^2/2mu_0)R`, `N_R=1.178e9`, `N_crit~1.66e11` | [credited]/[S new-step]/**[prediction]** band 1.7-3e11 | PDF 6.3; `omega_2^2=(8 gamma_eff/rho R^3)(1-X)` |
| M14-10 | `G_total=32.64<=G_required=32.9`; ponderomotive `dn/n`, Floquet `eta_c=2/Q_5` | [S]/[framework] | EVO Secs. 7-8 |
| M14-11 | three-wave `dot A`; `N_0+N_1`,`N_1+N_2` const; `|A_1|^2_crit=gamma_0 gamma_2/kappa^2`; Adler `cos theta` | [V]/[credited] | TORUS Parts 6-7 (symbolic + numeric) |
| M14-12 | MRxMHD J/Y two-region, interface `|B|` cont., det `-0.248` | [S]/[credited] | TORUS Part 25 (Hudson-Hole-Dewar 2007) |
| M14-13 | `*dV=-2V` on S^3; flat pullback curl `(-2y,2x,2)` not `~V` | [V]/[credited] | TORUS Part 34 (exterior-calc + 2 flat routes) |
| M14-14 | `B_phi=j_1(alpha r)sin theta`; `A=B/alpha` => `H=(2mu_0/alpha)E_mag`; `T_2=j_2 3 sin cos`, `z_{2,1}=5.763459`; `l=2` selection | [V]/[credited] | TORUS Parts 40-43 (SymPy) |
| M14-15 | `Delta f/gamma_L=Q(N^k-1)` independent of L; N=2 -> Q limit | [V] | TORUS Part 39 (SymPy) |
| M14-17 | Limits + the continuous-vs-integer-helicity warning + no over-unity | [V] | statement of scope |

## Verification coverage (M14)
- **In-repo verify — `results/verify/greenyer_beat_cascade_check.py` (run here):** confirms the geometric
  ladder `N^L` and the anapole `T_L/T_(L+1)=N^4=256`; the **three-wave dichotomy** (integer cascades N=2,3,4
  have NO self-matching triad; the golden ratio matches `φ^(n-2)+φ^(n-1)=φ^n` to 7e-15) — the mathematical
  reason the FTGB carrier comb must be inharmonic; the Fibonacci/Manley-Rowe shadow (`F_n/F_(n-1) → φ`); and
  the dimensional consistency of the beat law and the fissility `X`. This is the checkable `[V]` core; the
  nuclear-layer numbers stay `[prediction]`/`[framework]`.
- **Proven/verified in-project (traced):** ladder `N^L` for arbitrary `c_CK` (symbolic, TORUS Part 5 CALC 3;
  PDF proves it for arbitrary functional form); N-mode Woltjer LP (SymPy N=4 + `scipy.linprog` on real
  WIDE40 spectrum, Part 35); triad `mod N` non-residue + `phi` recursion (PDF 3.3); Manley-Rowe invariant
  rank theorem + Fibonacci coefficients + `D>=0` no-EP (PDF 3.4; Part 6 CALC 1 symbolic); BIC 50-digit zero
  + 13-point `p=1.0000` restoration (PDF 2.1); anapole `T=8.4823 A R^3`, fractal invariance, `T_L/T_{L+1}=
  N^4`, continuous helicity `N^{-4L}` (PDF 2.4/4.3; Part 5 CALC 4); Reed `9/8 mu_B` symbolic (0.044% numeric,
  PDF 4.2); Madelung 4-dp match + `curl grad S=0` / charged `curl v=-(q/m)B` (Part 5 CALC 1/5); three-wave
  Manley-Rowe + threshold + Adler `cos theta` self-correction (Parts 6-7); Hopf `*dV=-2V` + 2 flat failures
  (Part 34); `l=1`/`l=2` closed forms, `A=B/alpha`, orthogonality, `l=2` selection (Parts 40-43); off-
  resonance `Q(N^k-1)` (Part 39, SymPy).
- **Numbers traced, not invented:** every value quotes its source doc + section/eq. **No over-unity, no
  nuclear rate/cross-section/branching magnitude is asserted.** The `N_crit` band is a **prediction**; the
  Gamow "P1 closed (margin 0.26)" is framework-internal bookkeeping; `B=1000 T` and the `1.27x` sub-threshold
  gap are flagged; baryon number is conserved in the beat-dynamics layer and the baryon-decay channel is held
  as **[framework: Greenyer/MFMP]**, not a result.
- **Cross-document conflicts flagged:** `C ~ 0.2654` vs `c_CK(eps) ~ 1/eps` normalization (M14-1 Flag 1);
  base rung 52.3 THz vs 477 THz (M14-7 Conflict); MRxMHD illustrative `lambda` (M14-12).

**Citations (full ledger).** Chandrasekhar-Kendall ApJ 126, 457 (1957); Woltjer PNAS 44, 489 (1958); Taylor
PRL 33, 1139 (1974); Moffatt JFM 35, 117 (1969); Madelung Z. Phys. 40, 322 (1927); Bohm Phys. Rev. 85, 166
(1952); Onsager Nuovo Cim. Suppl. 6, 279 (1949); Feynman, Prog. Low Temp. Phys. 1 (1955); Manley-Rowe Proc.
IRE 44, 904 (1956); Zel'dovich JETP 6, 1184 (1958); Devaney-Wolf PRD 8, 1044 (1973); Radescu-Vaman PRE 65,
046609 (2002); Dubovik-Tugushev Phys. Rep. 187, 145 (1990); Rayleigh Phil. Mag. 14, 184 (1882);
Last-Levy-Jortner PNAS 99, 9107 (2002); Brillouin Phys. Rev. 67, 260 (1945); Chandrasekhar-Fermi ApJ 118,
116 (1953); Cantarella-DeTurck-Gluck-Teytel JMP 41, 5615 (2000); Lundquist (1950); Hudson-Hole-Dewar Phys.
Plasmas 14, 052505 (2007); Arnold-Khesin, *Topological Methods in Hydrodynamics* (Springer 1998);
Rañada-Soler-Trueba (1998); Callan PRD 25, 2141 (1982) / Rubakov JETP Lett. 33, 644 (1981) / Wilczek PRL 48,
1146 (1982); Hsu-Zhen-Stone-Joannopoulos-Soljacic, Nat. Rev. Mater. 1, 16048 (2016); Nicolis-Prigogine,
*Self-Organization in Nonequilibrium Systems* (Wiley 1977); Hanson-Cary Phys. Fluids 27, 767 (1984);
Shechtman et al. PRL 53, 1951 (1984); Haus, *Waves and Fields in Optoelectronics* (1984); Kuramoto (1984);
Strogatz Physica D 143, 1 (2000); Fitzpatrick Nucl. Fusion 33, 1049 (1993); Fano Phys. Rev. 124, 1866 (1961);
Mathieu (1868); Shoulders, *EV: A Tale of Discovery* (1987); Reed, *Quantum Wave Mechanics* Ch. 17.

Cross-links: `TOOLKIT_ADV_09_COUPLED_OSCILLATOR_SUBSTRATE` (M9 Stuart-Landau/Kuramoto/Adler beat law --
feeds M14-3/4/11), `TOOLKIT_ADV_10_TOPOLOGICAL_SOLITON_METHODS` (M10 canonical helicity + Woltjer/Taylor +
no-go template -- feeds M14-2/6/14), `MATH_TOOLKIT_BASE` (Beltrami/helicity, topology sec.).
Source docs: `ICCF27_greenyer_beat_qhd_essentialized_v6e.pdf` (Hanks, prepublication v6e),
`EVO_MATHEMATICAL_CORE.md` (v1.0), `TORUS_MATHEMATICS_APPENDIX.md` (Parts 1-45).

---
*M14 -- folded from the Greenyer/EVO beat-QHD sources into FTGB toolkit house style. Tiers are
load-bearing: `[V]` = checked in-project, `[credited]` = established physics, `[framework: Greenyer/MFMP]` =
taken as given, `[prediction]` = falsifiable target not a result. No over-unity; formulas quoted verbatim;
cross-document conflicts flagged in place rather than reconciled by hand.*
