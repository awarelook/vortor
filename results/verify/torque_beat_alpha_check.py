#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
torque_beat_alpha_check.py -- the elementary frontier through the theory's OWN lens: a yin-yang beat.

The user's push: read the irreducible frontier (alpha + g=2, "why is the electron elementary?")
through the theory's own language -- yin-yang (chirality duality), torsion/torque (precession), and
harmonic beats/rhythms. This SHOWS that that language is exactly correctly-typed for the real g-2/alpha
physics -- and is honest that it TYPES the frontier, it does not derive the value.

1. TORQUE / BEAT: the g-2 anomaly IS a beat. In a field B the spin precesses at omega_s and the
   momentum (cyclotron) at omega_c; what is measured (Penning trap) is the BEAT omega_a = omega_s -
   omega_c = a * omega_c, with a=(g-2)/2. So the anomaly is literally the beat between two rhythms,
   and the per-orbit beat phase-slip is 2*pi*a = alpha (leading) -> alpha = the spin(x)orbit
   beat-fraction. [credited]
2. HARMONIC RHYTHM: a = alpha/2pi - 0.328(alpha/pi)^2 + ... is the QED loop expansion = a harmonic
   cascade; alpha is the INPUT at every order. [credited]
3. YIN-YANG: the beat's HANDEDNESS is the chirality = sign(lambda) (chirality_helicity_check.py);
   antiparticle = opposite handedness = C (charge_conjugation_check.py). [S, computed]
VERDICT: the theory's torsion/torque/beat/yin-yang language correctly TYPES the frontier (alpha = the
beat-fraction, chirality = its handedness, g-2 = the spin(x)orbit beat harmonic cascade) -- a genuine,
correctly-typed synthesis -- but the VALUE (1/137) is the QED coupling, the irreducible frontier: the
rhythm structure DESCRIBES the frontier, it does not dissolve it. math-only.
Run: python results/verify/torque_beat_alpha_check.py
"""
import math

AINV = 137.035999084
ALPHA = 1/AINV
PI = math.pi
A_MEAS = 1.15965218059e-3         # electron (g-2)/2, CODATA


def banner(t): print("="*78); print(t); print("="*78)


def main():
    banner("1) TORQUE/BEAT: the g-2 anomaly is a BEAT between spin and cyclotron rhythms  [credited]")
    a_lead = ALPHA/(2*PI)
    print("  in a field B: spin precesses at omega_s, cyclotron at omega_c;")
    print("  the MEASURED anomaly frequency is the BEAT  omega_a = omega_s - omega_c = a*omega_c")
    print("  a = (g-2)/2 = alpha/2pi = %.8f  (leading);  measured a_e = %.8f" % (a_lead, A_MEAS))
    print("  per-orbit beat phase-slip = 2*pi*a = %.7f rad = alpha (%.7f)" % (2*PI*a_lead, ALPHA))
    print("  -> alpha = the spin(x)orbit BEAT-FRACTION (the per-orbit phase slip). Correctly-typed.")

    banner("2) HARMONIC RHYTHM: the g-2 series is a loop/harmonic cascade; alpha is the INPUT  [credited]")
    x = ALPHA/PI
    C1, C2, C3 = 0.5, -0.328478965579, 1.181241456   # QED coefficients of (alpha/pi)^n
    a1 = C1*x
    a2 = a1 + C2*x**2
    a3 = a2 + C3*x**3
    print("  a = 0.5(a/pi) + (-0.3285)(a/pi)^2 + 1.181(a/pi)^3 + ...  (each order = a higher harmonic)")
    print("   1 loop: a = %.9f" % a1)
    print("   2 loop: a = %.9f" % a2)
    print("   3 loop: a = %.9f   (measured %.9f; agree to %.1e)" % (a3, A_MEAS, abs(a3-A_MEAS)))
    print("  -> the cascade CONVERGES to the measured value, but alpha enters as the INPUT at every")
    print("     order (the coefficients are QED integrals). It refines a, it does not fix alpha.")

    banner("3) YIN-YANG: the beat's HANDEDNESS is the chirality  [S, computed elsewhere]")
    print("  chirality = sign(lambda) = sign(H) (chirality_helicity_check.py): the +/- Beltrami")
    print("  handedness = the two chiralities = the beat's two senses. Antiparticle = opposite")
    print("  handedness = charge conjugation C (charge_conjugation_check.py); the self-dual midpoint")
    print("  (theta_chi=45 deg) = Majorana (majorana_selfdual_check.py). The yin-yang IS the +/-lambda pair.")

    banner("VERDICT -- the theory's lens TYPES the frontier; it does not dissolve it")
    print("  Through torsion/torque/beat/yin-yang, the elementary-electron frontier reads cleanly:")
    print("    * alpha = the spin(x)orbit BEAT-FRACTION (per-orbit phase slip) -- correctly-typed;")
    print("    * the g-2 series = the HARMONIC/loop cascade on that beat -- alpha the input;")
    print("    * chirality = the beat's HANDEDNESS (yin-yang +/-lambda), antiparticle = C.")
    print("  This is a genuine, correctly-typed synthesis in the theory's OWN language -- and it is")
    print("  honest: it DESCRIBES the frontier's structure precisely, but the VALUE alpha=1/137.036")
    print("  is the QED coupling strength, still the irreducible frontier (settled-negative for any")
    print("  winding/ratio derivation; a big beat-number is only meaningful if it beats genericity).")
    print("  The rhythm structure fits the frontier; it does not derive the electron's elementary value.")
    print("done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
