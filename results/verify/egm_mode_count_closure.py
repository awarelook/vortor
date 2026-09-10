#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
egm_mode_count_closure.py  --  verify script for TOOLKIT module M11-6.

WHAT THIS CHECKS  (methods-only; NO adopted particle value is computed)
----------------------------------------------------------------------
M11-1 names Storti's harmonic cut-off (omega_Omega, n_Omega) but leaves the
CLOSURE -- how n_Omega is fixed -- a black box ("the physics content is entirely
in the choice of cut-off closure n_Omega").  M11-6 folds the reusable technique
behind it: the ordinary Debye-frequency / Nyquist 3-D mode-count band-limit.
This script reproduces ONLY the credited/[V] scaling content of that method:

  1. density of states  g(omega) = rho_0(omega)/(hbar*omega) = omega^2/(2 pi^2 c^3)
     -- the standard 3-D free-field DOS  [credited: SED spectrum / Debye]
  2. integrated mode count  N(Omega) = int_0^Omega g domega = Omega^3/(6 pi^2 c^3)
     -- numeric Riemann sum == closed form; N(2 Omega)/N(Omega) = 8   [V]
  3. closure scaling  omega_Omega / omega_C  ~  n_Omega^(1/3)          [V]
     hence characteristic length  ell ~ 2 pi c / omega_Omega  ~  lambda_C * n_Omega^(-1/3)
  4. WEAK SENSITIVITY  d ln ell = -(1/3) d ln n_Omega : the cube-root makes the
     COMPTON SCALE robust/predictive, but leaves the PRECISE value to the free
     integer n_Omega -- so any sub-0.01% "radius match" (M11-4(ii)) is a closure
     FIT, not a parameter-free derivation.  This strengthens the M11-4(ii) flag.

Every EGM particle radius / cut-off frequency / mass ratio remains QUARANTINED
at M11-4; none is adopted here.  ASCII only; run: python egm_mode_count_closure.py
"""
import math

C   = 299792458.0            # m/s        (exact)
HBAR = 1.054571817e-34       # J s        (CODATA; cancels in every ratio below)
PI  = math.pi


def rho0(w):
    """SED cubic zero-point spectral energy density  [credited]."""
    return HBAR * w**3 / (2.0 * PI**2 * C**3)


def dos(w):
    """3-D density of states = energy-density-per-mode-band / (hbar omega)."""
    return rho0(w) / (HBAR * w)          # = omega^2 / (2 pi^2 c^3)


def N_closed(W):
    """int_0^W dos domega, closed form = W^3 / (6 pi^2 c^3)  (per unit volume)."""
    return W**3 / (6.0 * PI**2 * C**3)


def N_riemann(W, steps=2_000_000):
    """Numeric mode count -- an honest 'computed', not a restated, check."""
    h = W / steps
    acc = 0.0
    for k in range(steps):
        w = (k + 0.5) * h                # midpoint rule
        acc += dos(w)
    return acc * h


def banner(t):
    print("=" * 74)
    print(t)
    print("=" * 74)


def main():
    banner("1) DENSITY OF STATES  g(omega) = rho_0/(hbar omega) = omega^2/(2 pi^2 c^3)  [credited]")
    ok = True
    for w in (1e18, 3e18, 7.7634e20):    # arbitrary probe frequencies (rad/s)
        lhs = dos(w)
        rhs = w**2 / (2.0 * PI**2 * C**3)
        rel = abs(lhs - rhs) / rhs
        ok = ok and rel < 1e-12
        print("  omega=%.4e :  g=%.6e   omega^2/(2pi^2 c^3)=%.6e   rel=%.1e" % (w, lhs, rhs, rel))
    # cubic-spectrum -> quadratic DOS: g(2w)/g(w) must be exactly 4
    r = dos(2e18) / dos(1e18)
    print("  g(2 omega)/g(omega) = %.6f   (exact 4 : DOS is quadratic)   %s" % (r, "[V]" if abs(r-4) < 1e-9 else "FAIL"))
    ok = ok and abs(r - 4) < 1e-9

    banner("2) MODE COUNT  N(Omega) = Omega^3/(6 pi^2 c^3)  (Debye/Nyquist band-limit)  [V]")
    W = 1.0e20
    nnum, ncl = N_riemann(W), N_closed(W)
    rel = abs(nnum - ncl) / ncl
    print("  Omega=%.3e :  N_riemann=%.6e   N_closed=%.6e   rel=%.1e" % (W, nnum, ncl, rel))
    r8 = N_closed(2 * W) / N_closed(W)
    print("  N(2 Omega)/N(Omega) = %.6f   (exact 8 : count ~ Omega^3)   %s" % (r8, "[V]" if abs(r8-8) < 1e-9 else "FAIL"))
    ok = ok and rel < 1e-4 and abs(r8 - 8) < 1e-9

    banner("3) CLOSURE SCALING  omega_Omega/omega_C ~ n_Omega^(1/3),  ell ~ lambda_C * n_Omega^(-1/3)  [V]")
    print("  Fix N = n_Omega (integer) in a Compton-scale region  ->  omega_Omega/omega_C = (n_Omega/n_ref)^(1/3).")
    print("  n_ref chosen so the smallest entry reads 1.  No adopted radius: dimensionless ratios only.")
    print("   n_Omega/n_ref |  omega_Omega/omega_C = cube-root  |  ell/lambda_C = n^(-1/3)")
    print("   --------------+-----------------------------------+------------------------")
    scale_ok = True
    for n in (1, 8, 27, 64, 1000):
        wr = n ** (1.0 / 3.0)
        lr = n ** (-1.0 / 3.0)
        exact = {1: 1.0, 8: 2.0, 27: 3.0, 64: 4.0, 1000: 10.0}[n]
        scale_ok = scale_ok and abs(wr - exact) < 1e-9
        print("   %11d   |   %8.4f  (exact %5.1f)          |   %8.5f" % (n, wr, exact, lr))
    print("  cube-root closure reproduces 1,2,3,4,10 exactly:  %s" % ("[V]" if scale_ok else "FAIL"))
    ok = ok and scale_ok

    banner("4) WEAK SENSITIVITY  d ln ell = -(1/3) d ln n_Omega  ->  precise value is a FREE-KNOB FIT")
    # a 10x change in the closure integer moves the length by only 10^(-1/3)
    factor = 10.0 ** (-1.0 / 3.0)
    print("  A 10x change in n_Omega moves ell by only %.4fx  (= 10^(-1/3)) -- the Compton SCALE is robust." % factor)
    print("  Inverse: to hit a target ell to 0.01%%, solve n_Omega = (k * lambda_C / ell)^3 for the free")
    print("  integer n_Omega -- a closure knob.  So the M11-4(ii) sub-0.01%% radius 'match' is a FIT, not a")
    print("  parameter-free derivation.  The SCALE (ell ~ lambda_C * n_Omega^(-1/3), Compton) is the only")
    print("  theorem-like, parameter-free content; the PRECISE value stays QUARANTINED at M11-4.  [V-structure]")
    # sanity: cube-root round-trips the free knob
    ell_target_ratio = 0.42                     # illustrative dimensionless ell/lambda_C (NOT an adopted radius)
    n_needed = (1.0 / ell_target_ratio) ** 3
    back = n_needed ** (-1.0 / 3.0)
    knob_ok = abs(back - ell_target_ratio) < 1e-12
    print("  round-trip: choose n=(1/0.42)^3=%.3f -> ell/lambda_C=%.5f  (free knob solves for any target)  %s"
          % (n_needed, back, "[V]" if knob_ok else "FAIL"))
    ok = ok and knob_ok

    banner("SUMMARY")
    print("  M11-6 method reproduced (DOS, Debye/Nyquist count, cube-root closure, weak sensitivity): %s"
          % ("ALL [V]" if ok else "SOME CHECKS FAILED"))
    print("  No EGM particle radius, cut-off frequency, or mass ratio is adopted -- all remain flagged at M11-4.")
    print("done.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
