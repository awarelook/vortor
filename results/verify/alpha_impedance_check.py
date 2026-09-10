#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
alpha_impedance_check.py -- the MEDIUM reading of alpha: mag/elect impedance to quantum resistance.

The user's angle: "mag to elect to medium ratio and time inverse." The vacuum's magnetic-to-electric
ratio is its IMPEDANCE Z0 = sqrt(mu0/eps0) = mu0*c (a MEDIUM property -- the K_PV / polarizable-vacuum
layer). There is an EXACT identity:

        alpha = Z0 / (2 R_K)     with   R_K = h/e^2  (von Klitzing quantum resistance)

i.e. alpha = (vacuum EM impedance) / (2 x quantum of resistance). This TYPES alpha as a
vacuum-MEDIUM-impedance ratio -- correctly-typed, and it folds into the M11 / K_PV medium layer. But it
is honest: it is a units RESTATEMENT (Z0 and R_K both carry {e,hbar,c,mu0}; their ratio is alpha by
construction), not a derivation of the value. Same status as the winding (dead) and the g-2 beat-fraction
(correctly-typed): the lens fits, the VALUE 1/137.036 stays the irreducible coupling. math-only (CODATA).
Run: python results/verify/alpha_impedance_check.py
"""
import math

# CODATA-2018
MU0 = 1.25663706212e-6      # H/m
EPS0 = 8.8541878128e-12     # F/m
C = 299792458.0            # m/s
H = 6.62607015e-34         # J s
E = 1.602176634e-19        # C
AINV = 137.035999084


def banner(t): print("="*78); print(t); print("="*78)


def main():
    banner("1) alpha = Z0 / (2 R_K)  EXACT: vacuum mag/elect impedance / (2 x quantum resistance)")
    Z0 = math.sqrt(MU0/EPS0)               # = mu0*c, the vacuum impedance (mag-to-elect ratio)
    RK = H/E**2                            # von Klitzing quantum resistance
    a_imp = Z0/(2*RK)
    print("  Z0 = sqrt(mu0/eps0) = mu0*c   = %.6f Ohm   (vacuum magnetic-to-electric impedance)" % Z0)
    print("  R_K = h/e^2                   = %.4f Ohm   (quantum of resistance, von Klitzing)" % RK)
    print("  alpha = Z0/(2 R_K)            = %.10f = 1/%.6f" % (a_imp, 1/a_imp))
    print("  measured alpha                = %.10f = 1/%.6f   (agree to %.1e)"
          % (1/AINV, AINV, abs(a_imp - 1/AINV)))
    ok = abs(a_imp - 1/AINV) < 1e-8

    banner("2) THE MEDIUM READING (folds into M11 / K_PV)  [credited typing]")
    print("  Z0 is the vacuum's magnetic-to-electric IMPEDANCE -- a MEDIUM property (the polarizable")
    print("  vacuum, K_PV: c_eff = c/sqrt(K_PV) rescales the effective impedance). R_K = h/e^2 is the")
    print("  quantum of resistance. So alpha = (vacuum medium impedance)/(2 x quantum resistance):")
    print("  alpha is SMALL because Z0 (~377 Ohm) << 2 R_K (~51626 Ohm). Correctly-typed as a")
    print("  vacuum-medium-impedance ratio -- the M11 layer's natural reading of the coupling.")

    banner("3) HONEST: exact but a RESTATEMENT -- it types the value, it does not derive it")
    # alpha = e^2 mu0 c / (4 pi hbar) : the identity, showing Z0/2RK is alpha rewritten
    hbar = H/(2*math.pi)
    a_id = E**2 * MU0 * C / (4*math.pi*hbar)
    print("  Z0/(2R_K) = (mu0 c)/(2 h/e^2) = e^2 mu0 c/(4 pi hbar) = alpha  (=%.10f) -- IDENTICALLY." % a_id)
    print("  Z0 and R_K both carry {e, hbar, c, mu0}; their ratio IS alpha by construction. The value")
    print("  1/137.036 still lives in e^2/(hbar c) -- the coupling. The impedance form RE-EXPRESSES")
    print("  alpha as a medium ratio; it does not fix its magnitude.")

    banner("4) TIME-INVERSE (frequency): where it enters, and why it still does not fix the value")
    print("  the STATIC vacuum impedance Z0 is frequency-INDEPENDENT. Time-inverse (omega) enters only")
    print("  via a running/dispersive medium K_PV(omega) = alpha(0)/alpha(q^2) -- the M11-3 RG dielectric")
    print("  flow -- which runs alpha ~0 at the electron scale (alpha_scale_headroom_check.py) and has no")
    print("  forced fixed point (ALPHA_IR_FIXED_POINT). And no object frequency RATIO lands on 137: the")
    print("  whirl/medium ratio omega_C/omega_p ~ 1e9 (torque-harmonics), generic (alpha_genericity_check).")

    banner("VERDICT -- the medium/impedance lens TYPES alpha (M11), does not derive it")
    print("  alpha = vacuum magnetic-to-electric IMPEDANCE / (2 x quantum resistance) -- an EXACT,")
    print("  correctly-typed MEDIUM reading that folds into the K_PV / M11 layer. Like the winding")
    print("  (settled-negative) and the g-2 beat-fraction (correctly-typed), it fits the frontier's")
    print("  structure but RESTATES the value: 1/137.036 stays the irreducible coupling strength.")
    print("done.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
