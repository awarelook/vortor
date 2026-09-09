# Hand-off package: R2 -- global regularity / enstrophy bound for the driven near-Beltrami heartbeat

**For:** a mathematical-fluid-dynamics / numerical-PDE collaborator or an HPC spectral run.
**Status:** `[S]` hard-open -> **analytic route PARTIALLY EXECUTED, 2026-09-09.** See
`results/R2_NEAR_BELTRAMI_ENSTROPHY_THEOREM_2026-09-09.md`: a **conditional `[V]`** enstrophy bound
now exists for the NSE first model (a-priori bounded `Z`, hence BKM-regular, provided the drive holds
the time-averaged Beltrami deviation below an explicit `O(1/Re)` threshold `<eta^2> < nu^2 lambda_1`).
The two routes below remain the way to make it UNCONDITIONAL / at-Reynolds and to lift it to Hall-MHD.
**One-line:** prove (or numerically evidence at the object's Reynolds) that the driven-dissipative
near-Beltrami limit cycle has an a-priori bounded enstrophy, upgrading the FTGB current-leg
trilogy's R2 from `[S] conditional` to `[V]` -- *without* requiring general 3D Navier-Stokes.

## 1. Problem statement (self-contained)
Consider incompressible two-fluid / Hall-MHD (or, as a first model, forced-dissipative 3D
Navier-Stokes) on a periodic box, driven so that the state settles onto a **stable time-periodic
limit cycle** (the "heartbeat"; a driven Stuart-Landau attractor with saturated amplitude
`r* = sqrt(2)`), and staying **near a force-free Beltrami state** `curl v ~ lambda v`. Question:

> Does the enstrophy `Z(t) = (1/2) integral |omega|^2` stay a-priori bounded for all time on
> this attractor -- equivalently, does the Beale-Kato-Majda integral `integral_0^inf
> ||omega(.,t)||_inf dt` stay finite?

If yes, the driven closure `S = mu - P.v = 0` of the FTGB medium-to-matter current leg holds
globally (R2 -> `[V]`), completing the trilogy for the object.

## 2. What is already established (do not redo)
- **X1 energy bound = HAVE.** A Lyapunov function `V = (r^2 - R0)^2/4` gives `dV/dt <= 0` with
  global attraction to `r* = sqrt(2)`; canonical helicity bounds energy from below (heartbeat
  persistence). `CURRENTLEG_R2_GLOBAL_EXISTENCE_2026-09-08`.
- **X2 no current-null crossing = HAVE** (benign, measure-zero). `CURRENTLEG_R1_CURRENTNULL_2026-09-08`.
- **Reduction: R2 <=> X3** (the enstrophy/BKM bound) given X1, X2 -- `[S]`, a worked chain
  (the slaved drive norm needs `||grad v||_2`).
- **The object is HIGH-Lundquist** `S ~ 1e2-1e6` (v_A ~ 3e4 m/s, B=200 T, n=1e28, R=1 um),
  so the small-Grashof rigorous global-regularity theorem does NOT apply (super-critical).
  `r2_grashof_threshold_2026-09-09.py`.
- **Structural handle (exact):** for a Beltrami field the Lamb vector `v x omega = 0`, so the
  Euler nonlinearity is a pure gradient -- ZERO vortex stretching, ZERO enstrophy production.
  Near-Beltrami, production ~ deviation `delta`. `r2_near_beltrami_enstrophy_2026-09-09.py`.

## 3. The precise target and the two routes
**The obstruction reduces to controlling intra-period gradient growth of a small-deviation
near-Beltrami periodic orbit** -- combining (i) Beltrami stretching-suppression [production
`O(delta)`] with (ii) limit-cycle mean-balance [`<production> = <dissipation>` over a period
if a smooth orbit exists]. Neither handle alone closes it at high Re + finite deviation.

- **Analytic route.** Establish an a-priori `H^1` (enstrophy) bound for the periodic orbit by
  exploiting the Lamb-vector suppression: bound the stretching term `integral omega.(omega.grad)v`
  by `C * delta(t) * Z^{3/2}` with `delta(t)` the (drive-controlled) deviation from Beltrami, and
  close a Gronwall/bootstrap using periodicity (`integral_period dZ/dt = 0`). Key sub-question:
  is the drive-maintained deviation `delta` compatible with dissipation over a full period, i.e.
  does the *time-integrated* production stay below the *time-integrated* dissipation on the orbit?
  A conditional theorem ("bounded provided `delta` obeys [explicit smallness-in-time integral]")
  is already a publishable advance.
- **Numerical route (HPC).** A resolved pseudo-spectral Hall-MHD / NS run *at the object's
  Reynolds*, measuring the enstrophy history over many heartbeat periods, with the flow
  dynamically pinned near force-free. Caution proven here: single-helicity *forcing* does NOT
  produce a near-Beltrami *flow* (`r2_spectral_retry_2026-09-09.py`: Z/E identical for helical vs
  non-helical at moderate Re) -- the flow must be *dynamically* held near Beltrami (relaxation
  toward the force-free state, or a helicity-constrained driving), not merely helically forced.

## 4. Resource spec (numerical route)
- Grid: dissipation scale ~ `S^{-3/4}` => `N ~ S^{3/4}` per dimension. At `S = 1e3`, `N ~ 180`;
  at `S = 1e4`, `N ~ 1000`; at `S = 1e6`, `N ~ 3e4` (out of reach -- target `S = 1e3-1e4` as the
  accessible high-Re window). GPU pseudo-spectral (dealiased 2/3), integrating-factor viscous step.
- Duration: >= 50-100 heartbeat periods to see whether Z is bounded/periodic vs secularly growing.
- Diagnostics: `Z(t)`, `||omega||_inf(t)`, the deviation `delta(t) = ||v x omega|| / (|v||omega|)`,
  and the running BKM integral. Success = `Z` and `integral ||omega||_inf dt` bounded across the run.
- Wall-time: GPU-hours to a few GPU-days at `N ~ 180-512`.

## 5. Success criterion / what closes R2
Analytic: a proof (even conditional on an explicit drive-deviation smallness) that `integral
||omega||_inf dt < inf` on the orbit. Numerical: bounded `Z(t)` and BKM integral at `S >= 1e3`
with the flow verified near-Beltrami (`delta` small, not just helical forcing). Either upgrades
R2 to `[V]` (or `[V]`-numerically-supported) and completes the current-leg trilogy for the object.

## 6. References
Beale-Kato-Majda 1984, CMP 94, 61 (blow-up criterion). Chae-Degond-Liu 2014, Ann. IHP C 31, 555
(Hall-MHD small/large data). Constantin-Foias, *Navier-Stokes Equations* (Grashof / attractor
enstrophy bounds). Foias-Manley-Rosa-Temam, *Navier-Stokes and Turbulence* (global attractor).
Standard Beltrami / force-free: Chandrasekhar-Kendall 1957; Woltjer 1958; Taylor 1974.
Provenance: `CURRENTLEG_R2_GLOBAL_EXISTENCE`, `r2_grashof_threshold_2026-09-09`,
`r2_near_beltrami_enstrophy_2026-09-09`, `r2_spectral_retry_2026-09-09` (all in frontier_calcs/).
