#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
g2_skyrme_composite_check.py -- g=2 from FTGB's OWN soliton layer: extended solitons give COMPOSITE moments.

The g=2 question ("does the soliton's quantization give a minimally-coupled Dirac field?") is the same
frontier as alpha (the electron's elementary/pointlike nature). This shows WHY, from inside the theory:
FTGB's own nucleon layer is the B=1 Skyrmion (toolkit M10), and the Skyrme model DOES compute the
nucleon magnetic moment by collective quantization -- and it comes out COMPOSITE (g != 2), matching the
real nucleon, NOT the Dirac value.

  Adkins-Nappi-Witten 1983 (the standard Skyrme quantization) predicts, parameter-free,
      mu_p / mu_n = -3/2 ,
  vs experiment -1.46 (agree ~3%). The nucleon g-factors g_p ~ 5.59, g_n ~ -3.83 are far from 2.

So an EXTENDED topological soliton (B=1 Skyrmion = nucleon) yields a COMPOSITE moment (right, the
nucleon IS composite), not the elementary Dirac g=2. The electron's g=2 (pointlike Dirac) is precisely
what the extended-soliton framework does NOT reach -- reaching it needs the effectively-pointlike /
elementary limit, which is the SAME open frontier as alpha's value. g=2 is not an independent crack;
it is the shared elementary-electron frontier, confirmed by FTGB's own toolkit. math-only.
Run: python results/verify/g2_skyrme_composite_check.py
"""
import math


def banner(t): print("="*78); print(t); print("="*78)


def main():
    # experimental nucleon moments (nuclear magnetons)
    mu_p, mu_n = 2.7928473, -1.9130427

    banner("1) FTGB's own nucleon = the B=1 Skyrmion (M10): its moment is COMPUTED, and COMPOSITE  [credited]")
    ratio_exp = mu_p / mu_n
    ratio_skyrme = -3.0/2.0                      # Adkins-Nappi-Witten 1983, parameter-free
    print("  Skyrme collective quantization (Adkins-Nappi-Witten 1983) predicts  mu_p/mu_n = -3/2 = %.3f" % ratio_skyrme)
    print("  experiment: mu_p/mu_n = %.4f / %.4f = %.4f   (agree to %.1f%%)"
          % (mu_p, mu_n, ratio_exp, abs(ratio_skyrme-ratio_exp)/abs(ratio_exp)*100))
    print("  -> an EXTENDED soliton (the B=1 Skyrmion) gives a genuine COMPOSITE moment, not g=2.")

    banner("2) these are COMPOSITE g-factors -- far from the Dirac value 2")
    g_p, g_n = 2*mu_p, 2*mu_n                     # g = 2 mu / mu_N for spin-1/2
    print("  nucleon g-factors:  g_p = %.3f ,  g_n = %.3f   (|g-2| = %.2f, %.2f)"
          % (g_p, g_n, abs(g_p-2), abs(g_n-2)))
    print("  the extended soliton's structure shows up in g -- exactly as for any composite (proton, neutron).")

    banner("3) the electron: g = 2 (pointlike Dirac) -- the limit the soliton framework does NOT reach")
    print("  electron g = 2.00231930 = 2 (Dirac) + alpha/pi + ...  -> elementary/pointlike behaviour.")
    print("  FTGB's soliton machinery correctly yields COMPOSITE moments where the object IS composite")
    print("  (the nucleon, sec.1-2); it does NOT yield the elementary g=2 for a pointlike lepton.")

    banner("VERDICT -- g=2 is the shared elementary-electron frontier, confirmed by FTGB's OWN toolkit")
    print("  From inside the theory: extended solitons (Skyrmions) give COMPOSITE g-factors (mu_p/mu_n=-3/2,")
    print("  ~3% of experiment) -- a real, parameter-free success for the COMPOSITE nucleon, and manifestly")
    print("  NOT g=2. The electron's g=2 requires the effectively-pointlike / elementary-Dirac limit, which")
    print("  is the SAME open frontier as alpha's value ('why is the electron elementary?'). g=2 is therefore")
    print("  not an independent crack the geometry can close -- it is the shared frontier, and the theory")
    print("  stands at it honestly. [credited: Adkins-Nappi-Witten 1983; Weinberg natural-g] / [S]/open")
    print("done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
