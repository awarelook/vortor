#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
ck_eigenvalues_check.py  --  reproduce the foundational Chandrasekhar-Kendall /
Beltrami carrier index FROM SCRATCH (the number the whole comb + ladder rest on).

WHAT THIS CLOSES
----------------
MATH_TOOLKIT_BASE.md §3, foundation/30_CANONICAL_NUMBERS.md §C, and M7-2 all quote
`lambda_1 R = 4.4934` (first root of `tan x = x`) and the convention-independent
`c_CK(eps->0) = 1/(2 j_0,1)` as "[V] (scipy brentq)" -- but no in-jewel script
actually SOLVED it, and engine/ftgb_engine.py only HARDCODES the roots. This script
solves them two independent ways (a self-contained bisection with NO scipy, and an
mpmath high-precision root find) and cross-checks the engine's hardcoded CK_ROOTS.

  1. roots of `tan x = x`  <=>  zeros of g(x) = sin x - x cos x  (pole-free)   [V]
  2. carrier comb ratios  x_n / x_1  =  1 : 1.719 : 2.427   [V]
  3. c_CK(eps->0) = 1/(2 j_0,1),  j_0,1 = first zero of J_0   [V]
  4. cross-check engine CK_ROOTS -- FLAG any hardcoded value that disagrees.

Deterministic; mpmath (already a project dep) for the authoritative roots; the
bisection uses math only. Run:  python results/verify/ck_eigenvalues_check.py
"""
import math
import os
import sys

import mpmath as mp

mp.mp.dps = 40  # authoritative precision


# ---- (1a) self-contained bisection: NO scipy, NO mpmath ----
def g(x):
    """tan x = x  <=>  sin x - x cos x = 0  (smooth, no poles: g'(x)=x sin x)."""
    return math.sin(x) - x * math.cos(x)


def bisect_root(a, b, tol=1e-15, itmax=200):
    fa, fb = g(a), g(b)
    if fa == 0.0:
        return a
    if fb == 0.0:
        return b
    assert fa * fb < 0.0, "no sign change in [%r, %r]" % (a, b)
    for _ in range(itmax):
        m = 0.5 * (a + b)
        fm = g(m)
        if fm == 0.0 or (b - a) < tol:
            return m
        if fa * fm < 0.0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return 0.5 * (a + b)


def roots_bisection(n):
    """First n nonzero positive roots: root k lies in (k*pi, (k+1/2)*pi)."""
    out = []
    for k in range(1, n + 1):
        a = k * math.pi + 1e-12
        b = (k + 0.5) * math.pi - 1e-12
        out.append(bisect_root(a, b))
    return out


# ---- (1b) authoritative mpmath roots ----
def roots_mpmath(n):
    out = []
    for k in range(1, n + 1):
        guess = (k + 0.5) * math.pi - 0.1  # just below the (k+1/2)pi asymptote
        r = mp.findroot(lambda x: mp.sin(x) - x * mp.cos(x), guess)
        out.append(r)
    return out


def banner(t):
    print("=" * 76)
    print(t)
    print("=" * 76)


def main():
    ok = True

    banner("1) ROOTS OF  tan x = x  (Chandrasekhar-Kendall / Beltrami eigenvalues)  [V]")
    bis = roots_bisection(6)
    mpr = roots_mpmath(6)
    print("   n |   bisection (float64)   |     mpmath (40 dps)                 | agree")
    print("  ---+-------------------------+-------------------------------------+------")
    for i in range(6):
        b = bis[i]
        m = float(mpr[i])
        agree = abs(b - m) < 1e-11
        ok = ok and agree
        print("   %d | %22.15f | %35.30f | %s"
              % (i + 1, b, float(mpr[i]), "OK" if agree else "FAIL"))
    lam1 = float(mpr[0])
    print("\n   lambda_1 R = %.13f  (base sec.3 / foundation sec.C 'ball carrier index 4.4934')  [V]" % lam1)
    ok = ok and abs(lam1 - 4.4934094579) < 1e-9

    banner("2) CARRIER COMB RATIOS  x_n / x_1  (the {121,208,294} kHz inharmonic comb)  [V]")
    ratios = [float(mpr[i] / mpr[0]) for i in range(3)]
    print("   1 : %.4f : %.4f   (quoted 1 : 1.719 : 2.427)" % (ratios[1], ratios[2]))
    ok = ok and abs(ratios[1] - 1.7192) < 1e-3 and abs(ratios[2] - 2.4265) < 1e-3
    # the physical comb {121,208,294} kHz is these ratios x a single anchor frequency
    f1 = 121.0
    print("   x f1=121 kHz  ->  %.1f : %.1f : %.1f kHz  (calibration {121,208,294})"
          % (f1, f1 * ratios[1], f1 * ratios[2]))

    banner("3) CONVENTION-INDEPENDENT c_CK LIMIT  c_CK(eps->0) = 1/(2 j_0,1)  [V]")
    j01 = mp.besseljzero(0, 1)      # first zero of Bessel J_0
    c_ck = 1.0 / (2.0 * float(j01))
    print("   j_0,1 (first zero of J_0) = %.12f   [credited]" % float(j01))
    print("   c_CK(eps->0) = 1/(2 j_0,1) = %.6f   (foundation sec.C '= 0.20792')  [V]" % c_ck)
    ok = ok and abs(c_ck - 0.20792) < 1e-4

    banner("4) CROSS-CHECK engine/ftgb_engine.py HARDCODED CK_ROOTS")
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)
    try:
        from engine.ftgb_engine import CK_ROOTS
        eng = [float(x) for x in CK_ROOTS]
        all_match = True
        for i in range(min(3, len(eng))):
            true_r = float(mpr[i])
            d = abs(eng[i] - true_r)
            status = "OK" if d < 1e-9 else ("!!! MISMATCH %.2e" % d)
            if d >= 1e-9:
                all_match = False
            print("   engine CK_ROOTS[%d] = %.15f   true = %.15f   %s"
                  % (i, eng[i], true_r, status))
        if all_match:
            print("   -> engine's hardcoded CK roots reproduce the solve  [V]")
        else:
            print("   -> engine has a hardcoded-constant error above; correct it to the true root.")
        ok = ok and all_match
    except Exception as e:
        print("   (could not import engine CK_ROOTS: %s -- solve above stands alone)" % e)

    banner("SUMMARY")
    print("  CK carrier index + comb ratios + c_CK reproduced from scratch (2 methods): %s"
          % ("ALL [V]" if ok else "A CHECK FAILED (see above)"))
    print("  This is the foundation everything rests on -- now reproducible, not asserted.")
    print("done.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
