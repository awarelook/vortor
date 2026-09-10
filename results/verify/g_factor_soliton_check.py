#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
g_factor_soliton_check.py -- does the FTGB / Reed soliton give g = 2?  (honest: naive -> g = 1)

The forward program from ALPHA_RESOLUTION_ASSESSMENT sec.3c was "derive g=2 from the soliton [S]".
This runs it, and the result corrects an over-optimistic offer: the NAIVE circulating-charge /
Reed photon-ring picture gives g = 1, NOT 2. g = 2 is the Dirac value and needs spinor structure
the classical geometry does not automatically supply.

Model (Reed photon-ring / zitterbewegung, the FTGB electron reading): a charge q circulates on a
ring of radius R at speed v; the electron mass M is the circulating energy / c^2.
  magnetic moment  mu = (1/2) q v R           (current loop, mu = I*A)
  spin             S  = p R = (M v_gamma) R    (orbital ang. mom. of the circulating charge)
  g-factor         g  = 2 M mu / (q S)
For the relativistic ring (v = c, p = M c): g = 2M(qcR/2)/(q McR) = 1.  math-only.
Run: python results/verify/g_factor_soliton_check.py
"""
import math


def banner(t): print("=" * 78); print(t); print("=" * 78)


def g_ring(kind, R, q=1.0, M=1.0, c=1.0, v_over_c=0.6):
    """g of a charge circulating on radius R.
    kind='photon': massless charge at v=c, p=E/c=Mc (Reed/zitterbewegung).
    kind='rotor' : classical charge=mass co-distributed, non-rel, L=M v R."""
    if kind == 'photon':
        v = c; p = M * c
    else:
        v = v_over_c * c; p = M * v         # co-distributed: same distribution -> L = M v R
    mu = 0.5 * q * v * R                     # current loop mu = I*A
    S = p * R                               # orbital angular momentum of the circulating charge
    return 2 * M * mu / (q * S)


def main():
    banner("1) NAIVE FTGB / Reed photon-ring g-factor  -- COMPUTED")
    print("   charge circulating on a ring; g = 2 M mu /(q S), mu = q v R/2, S = p R\n")
    print("   model                                        R      g")
    print("   -------------------------------------------  -----  ------")
    for kind, R, label in [('photon', 0.5, "photon ring (v=c, p=Mc): Reed/zitterbewegung reading"),
                           ('photon', 1.0, "photon ring, different R (g is R-independent)   "),
                           ('rotor',  1.0, "classical rotor, charge=mass co-distributed     ")]:
        g = g_ring(kind, R)
        print("   %s  %.2f   %.4f" % (label, R, g))
    print("\n   -> g = 1 robustly (R-, v-, model-independent): mu ~ q v R and S ~ p R, ratio q/2M.")
    print("      A naive circulating charge / classical soliton current gives g = 1, NOT 2.")
    print("      (Relativistic 'hidden-momentum'/field treatments that claim g=2 are model-dependent")
    print("       and debated -- they are where a factor of 2 is argued in, not robustly derived.)")

    banner("2) g = 2 IS THE DIRAC VALUE -- it needs spinor structure, not geometry  [credited]")
    print("   Minimal coupling of a DIRAC field to EM gives g = 2 at tree level (from (sigma.p)^2).")
    print("   measured electron: g = 2.00231930436  =  2 (Dirac)  +  alpha/pi + ...  (the g-2 anomaly).")
    print("   The factor-of-2 over the classical g=1 is the signature of the first-order (spinor)")
    print("   Dirac equation -- a classical current loop / soliton current does not reproduce it.")

    banner("3) WHAT THE FTGB TOPOLOGY *DOES* DELIVER: spin-1/2, not g=2  [credited/S]")
    print("   A Hopf soliton with a Hopf/Wess-Zumino term at theta = pi is quantized as a SPIN-1/2")
    print("   FERMION (Wilczek-Zee 1983 fractional spin/statistics; Finkelstein-Rubinstein 1968).")
    print("   So FTGB can honestly carry 'the object is a spin-1/2 fermion' [credited/S] from its")
    print("   Hopf topology. BUT spin-1/2 =/= g=2: a spin-1/2 soliton/anyon can have g =/= 2; the")
    print("   g-factor is a separate dynamical quantity fixed by the coupling, not by the spin alone.")

    banner("VERDICT -- honest correction of the 'winnable' offer")
    print("  Does the FTGB soliton give g = 2?  NOT cleanly. The naive circulating-charge / photon-ring")
    print("  picture gives g = 1 (computed above). g = 2 is the Dirac value and requires the object's")
    print("  quantization to reproduce a minimally-coupled Dirac equation -- the same quantum/spinor")
    print("  structure, not classical soliton geometry. The Hopf term delivers SPIN-1/2 [credited], a")
    print("  real positive result to fold; but g = 2 specifically stays [S]/open -- the earlier framing")
    print("  ('g=2 winnable') was too optimistic. Same difficulty class as needing Dirac dynamics.")
    print("done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
