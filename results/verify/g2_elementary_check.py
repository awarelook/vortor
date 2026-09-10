#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
g2_elementary_check.py -- resolving g=2 in principle: it means "effectively ELEMENTARY (Dirac)".

g_factor_soliton_check.py showed the naive extended soliton gives g=1, and g=2 is the Dirac value.
This closes the "resolution in principle": g=2 is not a geometry number to derive -- it is the value
FORCED for an ELEMENTARY (pointlike) charged spin-1/2 field by Lorentz invariance + minimal coupling
(Dirac; the "natural g=2" of Weinberg 1970 / Ferrara-Porrati-Telegdi 1992, from good high-energy
behaviour). COMPOSITE / extended spin-1/2 particles deviate: their structure shows up in g.

Evidence, by the data:
  elementary (pointlike Dirac): electron g=2.00232, muon g=2.00233  -> g = 2 + calculable QED loops
  composite (extended):         proton g=5.586,   neutron g=-3.826  -> big, structure-dependent
So the electron's g=2 (to 12 digits, matching QED) is a statement that the electron is EFFECTIVELY
POINTLIKE / ELEMENTARY. An FTGB extended soliton generically gives g != 2 (proton-like, g_factor gave
g=1); getting g=2 REQUIRES it to be in the effective elementary-Dirac (pointlike) limit -- its structure
must NOT appear in g. That is the SAME frontier as the electron's known pointlikeness (no substructure to
~1e-18 m) and as alpha's value: "why is the electron elementary?" math-only.
Run: python results/verify/g2_elementary_check.py
"""
import math

ALPHA = 1/137.035999084


def banner(t): print("="*78); print(t); print("="*78)


def main():
    banner("1) g = 2 is the ELEMENTARY (pointlike Dirac) value; composites DEVIATE  [credited]")
    # measured g-factors
    data = [
        ("electron", 2.00231930436, "elementary (lepton)"),
        ("muon",     2.00233184,    "elementary (lepton)"),
        ("proton",   5.5856946,     "COMPOSITE (uud)"),
        ("neutron", -3.82608545,    "COMPOSITE (udd), neutral yet has a moment = pure structure"),
    ]
    print("   particle   g            |g-2|       nature")
    print("   ---------  -----------  ---------  ------")
    for name, g, nat in data:
        print("   %-9s %+.6f    %7.4f    %s" % (name, g, abs(g-2), nat))
    print("\n   -> the ELEMENTARY leptons sit at g = 2 to 1e-3 (rest = calculable QED loops);")
    print("      the COMPOSITE nucleons are far from 2 (|g-2| ~ 3.6-5.8): structure shows up in g.")

    banner("2) the electron's g = 2 is the ELEMENTARY-Dirac value + QED, to 12 digits")
    g_dirac = 2.0
    a_e = ALPHA/(2*math.pi)                          # Schwinger leading anomaly
    g_pred = 2*(1 + a_e)
    print("   Dirac (elementary, tree)      : g = %.1f" % g_dirac)
    print("   + Schwinger loop 2(1+alpha/2pi): g = %.6f" % g_pred)
    print("   measured electron             : g = 2.00231930436  (agree to %.3f%%; rest = higher loops)"
          % (abs(g_pred-2.00231930436)/2.00231930436*100))
    print("   -> the electron is g=2 (elementary Dirac) + PERTURBATIVE QED -- the signature of a")
    print("      POINTLIKE particle, not an extended body with its own g-generating structure.")

    banner("3) RESOLUTION IN PRINCIPLE: g = 2  <=>  the soliton is effectively ELEMENTARY (pointlike Dirac)")
    print("   - g = 2 is not a shape/geometry number to compute; it is forced by (spin-1/2 + Lorentz +")
    print("     minimal coupling) for an ELEMENTARY field (Weinberg's natural g=2).")
    print("   - an EXTENDED soliton generically gives g != 2 (naive FTGB soliton -> g=1; proton -> 5.6).")
    print("   - so the electron's precise g=2 REQUIRES the FTGB object to be in the effective")
    print("     POINTLIKE / elementary-Dirac limit: its structure must not appear in g (or in scattering")
    print("     down to ~1e-18 m, where no electron substructure is seen).")
    print("   => g=2 is RESOLVED IN PRINCIPLE as a CONSTRAINT, not a derivation: the theory must reproduce")
    print("      effective pointlike-Dirac behaviour. This is the SAME open frontier as alpha's value --")
    print("      'why is the electron ELEMENTARY?' -- shared with all composite-electron models, not FTGB-")
    print("      specific, and not delivered by soliton geometry. The Hopf topology gives spin-1/2")
    print("      [credited]; elementary-Dirac behaviour (g=2 + alpha) is the frontier it must meet.")
    print("done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
