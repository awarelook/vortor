"""
Storti-EGM "first-principles" calc of alpha, particle radii, and H0 -- computed FORWARD, honestly.

The user asked to COMPUTE alpha / radii / H0 "principle calc first." These three are in the FTGB
excised/flagged-numerology ledger (MATH_TOOLKIT quarantine; egm_sense_checks.py). Rather than cite the
excision, this runs the actual EGM forward derivations from `storti_egm_missing.md` (Storti-Desiato 2009;
Storti 2007 Quinta Essentia; Storti 2023 cosmology) and shows, with the arithmetic, whether each is a
DERIVATION or a BACK-FIT / CIRCULAR / dead-factor. Discipline: compute, show the math, tier honestly.
No result is promoted; a hit that needs an inserted/fitted factor is [flag], not derived.

Run: python results/verify/egm_alpha_radii_H0_principle_calc.py
"""
import numpy as np

# CODATA-2018
hbar = 1.054571817e-34; c = 299792458.0; G = 6.67430e-11
m_e = 9.1093837015e-31; m_p = 1.67262192369e-27
e = 1.602176634e-19; eps0 = 8.8541878128e-12
alpha = e*e/(4*np.pi*eps0*hbar*c)
phi = (1+np.sqrt(5))/2
def banner(t): print("="*78); print(t); print("="*78)

banner("1) PROTON RADIUS -- EGM forward formula r_pi = (3/4) lambda_CP^2 / lambda_Ce")
lam_CP = hbar/(m_p*c)          # proton Compton wavelength (reduced)
lam_Ce = hbar/(m_e*c)          # electron Compton wavelength (reduced)
r_pi_fwd = 0.75 * lam_CP**2 / lam_Ce
r_p_exp = 0.8409e-15           # CODATA-2018 proton rms charge radius
print("  lambda_CP = %.4e m ,  lambda_Ce = %.4e m" % (lam_CP, lam_Ce))
print("  FORWARD:  r_pi = (3/4) lambda_CP^2/lambda_Ce = %.4e m" % r_pi_fwd)
print("  EXPERIMENT: r_p = %.4e m   -> forward formula MISSES by factor %.1e" % (r_p_exp, r_p_exp/r_pi_fwd))
# the "0.01% agreement" comes from r_pi = n_Omega * lambda_CP/(2 pi) with n_Omega BACK-FIT to the answer:
n_Omega = 2*np.pi*r_p_exp/lam_CP
print("  The quoted 0.01%% match uses r_pi = n_Omega*lambda_CP/(2pi) with n_Omega solved FROM r_p:")
print("     n_Omega = 2 pi r_p / lambda_CP = %.2f  (chosen to reproduce r_p, not predicted)" % n_Omega)
print("  VERDICT: forward EGM misses by ~1e4; the precise value is a BACK-FIT of n_Omega. [flag] not derived.")

banner("2) H0 (Hubble) -- EGM  H0 ~ omega_Omega,cosmic = sqrt(G M_univ / R_univ^3)")
H0 = 67.08 * 1000 / (3.0857e22)          # 67.08 km/s/Mpc -> s^-1
R_hub = c/H0                              # Hubble radius (DEFINED by H0)
M_univ = c**3/(2*G*H0)                    # closure mass ~ c^3/(2 G H0) (DEFINED by H0)
omega_cosmic = np.sqrt(G*M_univ/R_hub**3)
print("  Using the standard cosmological inputs R_univ = c/H0 and M_univ ~ c^3/(2 G H0):")
print("  omega_Omega = sqrt(G M/R^3) = %.4e s^-1 ;  H0 = %.4e s^-1" % (omega_cosmic, H0))
print("  omega_Omega / H0 = %.4f  = 1/sqrt(2) = %.4f  <-- returns H0 up to an O(1) factor" % (omega_cosmic/H0, 1/np.sqrt(2)))
print("  Because M_univ and R_univ are THEMSELVES defined through H0, sqrt(GM/R^3) = H0/sqrt(2)")
print("  IDENTICALLY -- the 'prediction' is CIRCULAR; the doc's 'correction factor ~1.82' then rescales")
print("  the O(1) to hit 67. VERDICT: circular + fitted factor, NOT a first-principles derivation. [flag]")

banner("3) ALPHA -- the two EGM routes: e^(-2/3) screening, and 1/(20 phi^4)")
e_23 = np.exp(-2.0/3.0)
print("  measured alpha = %.6f  (1/alpha = %.4f)" % (alpha, 1/alpha))
print("  route (a) e^(-2/3) screening factor = %.4f -- invoked for the ~2.3%% winding gap (140.2 vs 137.036):" % e_23)
winding = 140.2
print("     140.2 * e^(-2/3) = %.2f   (target 137.036; gives %.1f -- MISSES, the factor is dead)" % (winding*e_23, winding*e_23))
print("     [egm_sense_checks: e^(-2/3) route -> ~72, not 137; does not even produce the 2.3%% correction]")
print("  route (b) 1/(20 phi^4):  20*phi^4 = %.3f  (vs 1/alpha = 137.036, %.3f%% off)" % (20*phi**4, abs(20*phi**4-1/alpha)/(1/alpha)*100))
print("     but the '20' = C(6,3) is HAND-CHOSEN and there is no QED running -> numerology [flag], not derived.")
print("  VERDICT: neither route DERIVES alpha; (a) is dead, (b) is a hand-picked coincidence. [flag]/[excised]")

banner("BOTTOM LINE -- computed forward, all three are fit/circular, not derivations")
print("  Ran the EGM 'first-principles' calcs FORWARD (per storti_egm_missing.md):")
print("   - proton radius: forward formula off by ~1e4; the 0.01%% match is a BACK-FIT of n_Omega~25;")
print("   - H0: sqrt(GM/R^3) is CIRCULAR (M,R are H0-defined -> = H0/sqrt2) + a fitted 1.82;")
print("   - alpha: e^(-2/3) is dead (->72), 1/(20 phi^4) uses a hand-chosen C(6,3)=20.")
print("  So the EGM alpha/radii/H0 'derivations' back-fit or rescale to known answers -- exactly why the")
print("  FTGB discipline EXCISES them. Computing them forward CONFIRMS the excision; it does not overturn")
print("  it. alpha's value, the radii, and H0 remain measured inputs / the honest frontier, not FTGB-derived.")
print("  (This is a settled-NEGATIVE audit, shown with the arithmetic -- no fabrication, nothing promoted.)")
print("done.")
raise SystemExit(0)
