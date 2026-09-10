#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
alpha_scale_headroom_check.py -- can the RUNNING/vacuum route EVER supply the 2.3% alpha gap?

alpha_running.py showed the DIRECTION is wrong (QED screens; 137.036 is the IR ceiling; 140.2
sits above it -> needs exotic anti-screening). This script bounds the MAGNITUDE, which is the
decisive point: even granting the anti-screening sign, how much scale-window would it take to
flow q_geom = 140.2 -> alpha^-1 = 137.036, and does the object's own natural EM window supply it?

Result (see SUMMARY): the running has ZERO headroom at/below the electron scale, and covering
2.3% at a QED-magnitude beta needs ~6 decades of running -- ~3x more than the object's natural
Compton->classical-radius window provides. So the 2.3% is a SKELETON (winding-integer) error the
dynamics cannot naturally supply; the resolution must fix the geometric winding (137, not 140),
not the running. Pure-Python (math only). Run: python results/verify/alpha_scale_headroom_check.py
"""
import math

AINV0 = 137.035999084          # alpha^-1(q^2 -> 0), CODATA
ALPHA0 = 1.0 / AINV0
Q_GEOM = 140.2                 # toroidal winding estimate (A=9.0), from the excision notes
ME = 0.5109989e-3              # GeV
PI = math.pi


def banner(t):
    print("=" * 78); print(t); print("=" * 78)


def dalpha_lep(mu, n_light=3):
    """Standard leptonic one-loop Delta-alpha up to scale mu (GeV)."""
    masses = [ME, 0.1056584, 1.77686][:n_light]
    return sum((ALPHA0 / (3 * PI)) * (math.log(mu**2 / m**2) - 5.0 / 3.0)
               for m in masses if mu > m)


def main():
    ok = True

    banner("1) HEADROOM AT THE ELECTRON'S OWN SCALE IS ZERO  [credited QED]")
    # below m_e there are NO charged particles to polarize the vacuum -> alpha is flat.
    ainv_me = AINV0 * (1 - dalpha_lep(ME))     # dalpha_lep(ME)=0 since mu not > m_e
    print("  alpha^-1(0)   = %.4f   (IR value / ceiling)" % AINV0)
    print("  alpha^-1(m_e) = %.4f   (running below m_e is structurally ZERO)" % ainv_me)
    print("  -> a winding that lives at the electron's geometry must EQUAL 137.036 there;")
    print("     there is no scale headroom to 'run' 140.2 into 137.036 at that scale.")
    ok = ok and abs(ainv_me - AINV0) < 1e-6

    banner("2) SCALE-WINDOW NEEDED to flow 140.2 -> 137.036 at a QED-MAGNITUDE beta")
    # need fractional flow d = (Q_GEOM - AINV0)/Q_GEOM, supplied by Delta-alpha = 2*(a/3pi)*n_eff*ln(R)
    d_need = (Q_GEOM - AINV0) / Q_GEOM
    print("  required Delta-alpha (fractional) = (140.2 - 137.036)/140.2 = %.4f  (%.2f%%)"
          % (d_need, 100 * d_need))
    coeff = 2.0 * (ALPHA0 / (3 * PI))          # per e-fold of scale, per unit n_eff
    for n_eff in (1, 2, 3):
        lnR = d_need / (coeff * n_eff)
        decades = lnR / math.log(10)
        print("  n_eff=%d anti-screening d.o.f.:  ln(Lambda_UV/Lambda_IR) = %5.1f  -> %.1f decades (x%.1e)"
              % (n_eff, lnR, decades, 10**decades))
    print("  -> even a single QED-strength anti-screening flavor needs ~6 DECADES of running.")

    banner("3) DOES THE OBJECT'S OWN NATURAL EM WINDOW SUPPLY IT?")
    # the electron's two natural EM scales: Compton wavelength and classical radius r_e = alpha * lambda_C
    ln_window = math.log(1.0 / ALPHA0)         # ln(lambda_C / r_e) = ln(1/alpha) = ln(137)
    decades_nat = ln_window / math.log(10)
    dalpha_nat = 2.0 * (ALPHA0 / (3 * PI)) * 1 * ln_window   # n_eff=1
    print("  natural window lambda_C / r_e = 1/alpha = %.1f  -> ln = %.2f  (%.1f decades)"
          % (AINV0, ln_window, decades_nat))
    print("  flow it supplies (n_eff=1, QED-magnitude) = %.4f  (%.2f%%)" % (dalpha_nat, 100 * dalpha_nat))
    shortfall = d_need / dalpha_nat
    print("  needed/supplied = %.1fx  -> the natural window is ~%.0fx too SHORT to cover 2.3%%."
          % (shortfall, shortfall))

    banner("4) DECOMPOSITION: where the 2.3% actually lives  [the honest relocation]")
    skeleton_err = (Q_GEOM - 137.0) / 137.0        # winding-integer error (140 vs 137)
    fraction = (AINV0 - 137.0)                      # the 0.036 non-integer part of alpha^-1
    print("  1/alpha = 137.036 = [137 integer skeleton] + [0.036 fraction]")
    print("  winding gives 140.2:  skeleton error 140 vs 137 = %.2f%%   <- the whole gap is HERE" % (100 * skeleton_err))
    print("  the fraction 0.036 is %.3f%% of alpha^-1  <- a tiny correction, NOT the problem" % (100 * fraction / AINV0))
    print("  max sub-m_e running available = 0.000%  <- cannot touch a 2.2% skeleton error")

    banner("SUMMARY")
    print("  The running/vacuum route is DIRECTION-wrong (alpha_running.py) AND MAGNITUDE-short")
    print("  (here): 0% headroom at the electron scale; ~6 decades or ~3x-enhanced beta needed;")
    print("  the object's natural window is ~3x too short. => the 2.3%% is a WINDING-INTEGER")
    print("  (skeleton) error, not a dynamical one. Resolution must make the winding 137, not 140,")
    print("  from the self-consistent geometry -- NOT from running. See ALPHA_RESOLUTION_ASSESSMENT.")
    print("  [S]/[flag] throughout; no value is promoted; e^(-2/3) stays excised.")
    print("done.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
