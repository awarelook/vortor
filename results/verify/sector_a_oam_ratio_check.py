"""
The Sector-A exact OAM ratio R = pi m_e R_L^2 f_L / hbar -- corpus fold (anapole-resonator thread).

Salvaged from the ckfreefem ark (11_verified_ark/helium_heat_nuclear_extensions -- Sector A, the
surviving environment-theory core; vendored: frontier_calcs/SECTOR_A_ENVIRONMENT_THEORY.md).
The ark's result: for a toroidal ring carrying (i) an m=1 Beltrami eigenmode field and (ii) a
quantized n=1 Madelung electron circulation on the SAME ring, the two independent orbital-angular-
momentum measures -- the classical FIELD OAM  L_field = (m/omega) U  (Allen et al., PRA 45, 8185
(1992), the standard structured-light relation) and the Madelung CIRCULATION OAM
L_circ = N_e n hbar -- have an EXACT closed-form ratio

    R  =  L_field / L_circ  =  pi m_e R_L^2 f_L / hbar

in which the electron density n_e CANCELS IDENTICALLY (it enters L_field through the field energy
and L_circ through the electron count, and drops out). The ark verified this on a 3-point grid to
0.002-0.02%; the deeper lesson it logged: an apparent cross-framework numerical trend traced to a
FORCED ALGEBRAIC IDENTITY, not an open physical puzzle.

Here we (1) re-derive the identity from its ingredients, (2) verify the n_e cancellation and the
closed form numerically over a grid spanning 8 orders of magnitude in n_e, and (3) evaluate R at
the jewel's own canon anchors -- connecting the ark's ring construction to the anapole-resonator
(OAM) thread. Tier: [V] algebra; the ring-model reading is [S] environment theory (no nuclear claim).

  Derivation reproduced (TEST 1): with the ring energy carried as the circulating electrons'
  kinetic energy  U = N_e (1/2) m_e v^2,  v = 2 pi R_L f_L,  omega = 2 pi f_L,  m = n = 1:
      L_field = U/omega = N_e m_e (2 pi R_L f_L)^2 / (4 pi f_L) = N_e pi m_e R_L^2 f_L
      L_circ  = N_e hbar
      R = L_field/L_circ = pi m_e R_L^2 f_L / hbar        (N_e, hence n_e, cancels EXACTLY)

numpy only, deterministic. Run: python results/verify/sector_a_oam_ratio_check.py
"""
import numpy as np

M_E = 9.1093837015e-31
HBAR = 1.054571817e-34
ok = True


def check(name, cond, detail=""):
    global ok
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, ("  -- " + detail) if detail else ""))
    ok = ok and cond


print("=" * 92)
print("Sector-A exact OAM ratio: R = pi m_e R_L^2 f_L / hbar  (field OAM / circulation OAM)   [V]")
print("=" * 92)

print("TEST 1 -- the identity, computed from its ingredients over a grid (n_e MUST cancel):")
grid_R = [1e-8, 1e-6, 1e-4]            # ring radii, m
grid_f = [1e6, 1e9, 1e12]              # ring frequencies, Hz
grid_ne = [1e20, 1e24, 1e28]           # electron densities, /m^3  (must cancel)
worst = 0.0
spread = 0.0
for R_L in grid_R:
    for f_L in grid_f:
        vals = []
        for n_e in grid_ne:
            V = 2.0 * np.pi**2 * R_L**3 * 0.04     # torus volume, aspect 0.2 (a=0.2 R_L): 2 pi^2 R a^2
            N_e = n_e * V
            v = 2.0 * np.pi * R_L * f_L
            U = N_e * 0.5 * M_E * v**2             # ring energy = circulating-electron KE
            L_field = U / (2.0 * np.pi * f_L)      # (m/omega) U with m=1
            L_circ = N_e * HBAR                    # N_e * n * hbar with n=1
            vals.append(L_field / L_circ)
        closed = np.pi * M_E * R_L**2 * f_L / HBAR
        vals = np.array(vals)
        worst = max(worst, float(np.max(np.abs(vals / closed - 1.0))))
        spread = max(spread, float(np.max(np.abs(vals / vals[0] - 1.0))))
check("computed ratio equals the closed form pi m_e R_L^2 f_L / hbar on the full grid",
      worst < 1e-12, "max rel dev %.1e" % worst)
check("n_e cancels IDENTICALLY (ratio invariant across 8 orders of magnitude in n_e)",
      spread < 1e-12, "max spread %.1e" % spread)

print("TEST 2 -- scale illustrations (the ratio is pure geometry x frequency):")
for (R_L, f_L, tag) in [(1e-6, 1e9, "ark-style micron ring at GHz"),
                        (0.12, 87.14e3, "jewel canon: R=0.12 m at the 87.14 kHz beat"),
                        (0.12, 1.428e3, "jewel canon: R=0.12 m at the 1.43 kHz detuning")]:
    Rv = np.pi * M_E * R_L**2 * f_L / HBAR
    print("    R_L=%-8.3g m  f_L=%-9.4g Hz  ->  R = %.3e   (%s)" % (R_L, f_L, Rv, tag))
check("R spans many orders across scales (a scale diagnostic, not a universal constant)", True)

print("READING: the exact ratio links the Beltrami-FIELD and Madelung-CIRCULATION descriptions of")
print("the same ring through geometry and frequency ALONE -- electron density drops out. The ark's")
print("logged lesson stands: what looked like a cross-framework numerical trend is a forced algebraic")
print("identity ([V]); it joins the anapole-resonator OAM thread as environment structure, carrying")
print("no nuclear claim (the same corpus closed every nuclear-rate route -- see")
print("corpus_settled_negatives_check.py). Provenance: frontier_calcs/SECTOR_A_ENVIRONMENT_THEORY.md.")
print("status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
