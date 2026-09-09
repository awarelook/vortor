# Hand-off package: Delta -- the B=4 off-diagonal reactive overlap (LENR branching amplitude)

**For:** a Skyrme / nuclear-topological-soliton HPC group (compiled + GPU), or an ab-initio
NCSMC/RGM collaborator.
**Status:** `[A]` / open. This package specifies the one calculation that would give the LENR
kernel its quantitative branching amplitude (the other rate input, U_s, is host-lattice inherited).
**One-line:** compute the OFF-DIAGONAL Landau-Zener gap `Delta` between the bound B=4 (alpha)
configuration and the breakup channel along the 2x(B=2) -> B=4 merger coordinate, via a
topology-preserving relaxed two-diabatic-surface solve; test whether `Delta` lands in the
neutron-suppression band ~1.4-1.9 MeV.

## 1. Problem statement
The LENR branching amplitude in the FTGB kernel factorizes as `M_fi(theta) = sum_alpha C_alpha
A_alpha R_alpha S_alpha` with the selection skeleton `C_alpha, A_alpha` SETTLED `[V]` (O_h
symmetry, gerade sector, E0 gamma-suppression, aneutronic = dynamical) and `S_alpha` the
published B=4 collective-mode basis `[S]`. The open piece is the reduced radial overlaps `R_alpha`
and their phases -- concretely, the **off-diagonal reactive coupling** (a Landau-Zener gap
`Delta`) between two diabatic surfaces along the merger reaction coordinate:

> Surface 1: the bound B=4 alpha-Skyrmion (O_h cube). Surface 2: the breakup channel
> (B=3 + B=1, or the d + d entrance). `Delta` = the off-diagonal coupling at their avoided
> crossing = the branching amplitude that sets `Gamma = (2 pi/hbar) |M_fi|^2 rho_f`.

## 2. What is established (do not redo)
- **The DIAGONAL is NOT the gap.** The (mu, V) vibrational quantum was EXECUTED:
  `hbar omega_merger = 66-95 MeV` (= the BBT `Eg` "cube->two donuts" mode, ~20 MeV scale,
  cross-checked to the `4He 0+_2` level 20.21 MeV -- a SOFT/breakup-resonance caveat, not a clean
  bound state). Plugging it into `S = exp(delta)` freezes BOTH channels (`log10 S ~ 9600`),
  proving the diagonal is not the branching gap. `B4_MODULI_GEODESIC_EXECUTED_2026-09-08`.
- **The reduced ansaetze FAIL in the crossing region** (this is why it is HPC-only): product
  ansatz -> core wall (never fuses, keeps `B ~ 3.8`); naive field-blend -> topology breaks
  (`B -> 2.4`); free coarse-grid MASSLESS relaxation -> UNWINDS to `B = 0`.
  `B4_TWO_DIABATIC_RELAXATION_2026-09-08`.
- **Method validation:** the moduli-geodesic (mu, V, transition-amplitude) pipeline reproduces
  1+1 sine-Gordon (kink mass 1.4e-6, kink-antikink force 0.9%, breather scaling 1.93 vs 2.0) with
  an honest factor-~2.2 coefficient ceiling. `SELF_UNIFIED_SKYRME_MULTIBODY_2026-09-08`.

## 3. The precise calculation (the priced blocker, made executable)
A **topology-preserving, PION-MASSIVE** Skyrme relaxation of the two diabatic surfaces + their
off-diagonal coupling, with continuum matching for the breakup channel:
- **Interaction:** standard Skyrme term + a PION-MASS term (essential: the massless + coarse
  combination is what unwinds `B -> 0`; the mass raises the unwinding barrier).
- **Discretization:** topology-preserving (finite-difference with an exact-ish baryon-density
  monitor, or a spectral scheme) at `dx <= 0.06-0.10 fm`, `N >= 100-170` per dimension.
- **Minimizer:** arrested Newton flow / accelerated gradient descent, **compiled (C/Fortran)
  or GPU** -- NOT pure-numpy (which is ~15 h/sweep minimum, days at robust dx, and unstable).
- **Diabatic construction:** constrain the merger collective coordinate `sigma` (umbrella /
  reaction-path constraint), relax at each `sigma` on each branch (bound-cube vs breakup),
  extract `Delta` as the avoided-crossing gap; match the breakup branch to the continuum
  (R-matrix / boundary condition at large separation).
- **Cross-check option (ab-initio):** NCSMC/RGM for `d + d -> 4He` with SYMMETRIZED (bosonic)
  d+d cluster wavefunctions + a 3-channel R-matrix at few-percent precision + a collective-mode
  transition operator (not standard in NCSMC). Benchmark: Hupin-Quaglioni-Navratil 2019 (d+t).

## 4. Resource spec
- `N ~ 128-170`^3, pion-massive Skyrme, GPU arrested-Newton: ~GPU-hours to a GPU-day per branch;
  a full two-branch + avoided-crossing sweep ~ a few GPU-days. (Pure-numpy CPU is infeasible:
  ~15 h/sweep minimum and it unwinds -- do NOT attempt on CPU/numpy.)
- Baryon monitor: `B(sigma)` must hold ~4 throughout (the failure diagnostic).

## 5. Success criterion
`Delta` with a two-sided band (>= 2 ansaetze / resolutions), and the in-band test: is it in the
~1.4-1.9 MeV neutron-suppression window (`Delta ~ MeV` order)? Plus the `S = exp(delta)` sanity
(does THIS Delta give a sane, non-freeze branching, unlike the ~20 MeV diagonal?). A converged
`Delta` closes the LENR kernel's branching magnitude (one of its two rate inputs).

## 6. Scope discipline (carry into any write-up)
Baryon-conserving `d + d -> 4He` only (not baryon decay). No fabricated rate/cross-section
(`E_fm = 2.5 MeV` stays retracted). COP is NOT derived (1.3-1.4 is inherited field positioning;
no over-unity). The SECOND rate input, screening `U_s ~ 300-800 eV`, is host-lattice inherited
(accepted-not-adjudicated), NOT FTGB-derived -- so a converged `Delta` gives the branching, not
a full rate. Do-not-cite Rossi/Mills/bio-transmutation.

## 7. References
Skyrme 1961/1962; Witten 1983; Battye-Sutcliffe 1997; Barnes-Baskerville-Turok 1997, PRL 79, 367
(B=4 16-mode spectrum); Houghton-Manton-Sutcliffe 1998; Feist-Lau-Manton 2013, PRD 87, 085034;
Gudnason-Halcrow 2018, PRD 98, 125010; Halcrow 2016, Nucl. Phys. B 904, 106 (B=4 quantization);
Adam-Sanchez-Guillen-Wereszczynski 2010 (BPS Skyrme, near-BPS binding). Ab-initio: Hupin-Quaglioni-
Navratil 2019, Nat. Commun. 10, 351; Quaglioni-Navratil 2008; Navratil-Quaglioni 2012 (NOTE:
Navratil-Quaglioni 2011 d+4He is A=6 6Li, NOT A=4). E0: Church-Weneser 1956.
Provenance: `MFI_B4_REACTIVE_OVERLAP_COMPUTE`, `B4_MODULI_GEODESIC_EXECUTED`,
`B4_TWO_DIABATIC_RELAXATION`, `SELF_UNIFIED_SKYRME_MULTIBODY` (all in frontier_calcs/).
