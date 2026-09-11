"""
Provenance closure: reproduce the DERIVED canonical numbers (30_CANONICAL §A/§B/§I) from the
cited ANCHORS, in-repo and CI-gated. Previously these numbers' provenance was the external
ckfreefem corpus; the full scripts are now vendored under `frontier_calcs/`, and this check
re-derives the load-bearing values from the anchors via the stated closed forms so a reader who
clones the repo can reproduce them from scratch (numpy only) -- no external tooling needed.

The ANCHORS are cited physical inputs (not derived; see 30_CANONICAL §A):
  R = 0.12 m           object radius            [ball-lightning stats, Stenhoff 1999]
  tau = 5.9039e-6 s    Alfven timescale R/v_A   [sets v_A; carries the residual band, see below]
  n_i = 1.7e19 m^-3    ion density              [SSPX, Hill 2000]
  m_i = 29 AMU         mean air-ion mass        [US Std Atmosphere 1976]
  Gamma_dim, R_dim     universal dimensionless   [theory dynamics, not fits: FPUT growth / breathing radius]

  TEST 1 -- v_A, B from the anchors:  v_A = R/tau ,  B = v_A sqrt(mu0 n_i m_i).
  TEST 2 -- b_eff, hbar_eff (medium) via the WS5 closed forms:
            b_eff = (Gamma/R_dim)^2 m_i v_A^2  (size cancels -> pure medium property, = magnetic energy/ion);
            hbar_eff = (Gamma/R_dim^2) m_i v_A R  (emergent action, scales with size).
  TEST 3 -- d_i (ion skin depth = penetration depth lambda_L) from the plasma formula d_i = c/omega_pi.
  Each is cross-checked against the tabulated 30_CANONICAL value.

Vendored provenance (full scripts, frozen from the ckfreefem corpus, `frontier_calcs/`):
  ws5_hbar_b_eff_reduction_to_medium.py (b_eff, hbar_eff), qhd_coherence_carrier_mass_resolution.py,
  greenyer_real_hopf_charge_whitehead_integral.py (Q_H), ws6_cCK_convergence_and_analytic_limit.py (c_CK),
  polarizable_medium_resonator_derivation.py, and 5 more (see frontier_calcs/README.md).

numpy only, deterministic. Run: python results/verify/canonical_numbers_provenance_check.py
"""
import numpy as np

def banner(t): print("="*84); print(t); print("="*84)

# physical constants
AMU = 1.66053906660e-27; mu0 = 4e-7*np.pi; e = 1.602176634e-19
eps0 = 8.8541878128e-12; c = 299792458.0
# anchors (cited inputs, 30_CANONICAL §A)
R = 0.12; tau = 5.9039e-6; n_i = 1.7e19; m_i = 29*AMU
GAMMA = 0.998742; RDIM = 1.380040
# tabulated canonical targets to reproduce
TARGET = dict(v_A=2.033e4, B_mT=20.6, b_eff_eV=65.04, hbar_eff=6.1594e-23, d_i=0.2963)

def close(name, got, want, rel=0.01):
    ok = abs(got - want) <= rel*abs(want)
    print("   %-14s computed = %-13.5g  tabulated = %-13.5g  (%.2f%%)  %s"
          % (name, got, want, 100*abs(got-want)/abs(want), "OK" if ok else "MISMATCH"))
    return ok

ok = True

banner("1) v_A and B from the anchors (R, tau, n_i, m_i)")
v_A = R/tau
B = v_A*np.sqrt(mu0*n_i*m_i)
ok &= close("v_A [m/s]", v_A, TARGET["v_A"])
ok &= close("B [mT]", B*1e3, TARGET["B_mT"])

banner("2) b_eff, hbar_eff (medium) via the WS5 closed forms")
b_eff = (GAMMA/RDIM)**2 * m_i * v_A**2
hbar_eff = (GAMMA/RDIM**2) * m_i * v_A * R
print("   closed forms: b_eff=(Gamma/R_dim)^2 m_i v_A^2 (size cancels); hbar_eff=(Gamma/R_dim^2) m_i v_A R")
ok &= close("b_eff [eV]", b_eff/e, TARGET["b_eff_eV"])
ok &= close("hbar_eff [J.s]", hbar_eff, TARGET["hbar_eff"])
mag_per_ion = B**2/(2*mu0*n_i)
print("   physical meaning: b_eff / (B^2/2mu0 n_i) = %.3f  -> b_eff ~ magnetic energy per ion [V]"
      % (b_eff/mag_per_ion))

banner("3) d_i = lambda_L (ion skin depth) from the plasma formula c/omega_pi")
omega_pi = np.sqrt(n_i*e**2/(eps0*m_i))
d_i = c/omega_pi
ok &= close("d_i [m]", d_i, TARGET["d_i"])

banner("VERDICT")
print("  The DERIVED canonical numbers (v_A, B, b_eff, hbar_eff, d_i) reproduce from the cited anchors")
print("  via closed forms, IN-REPO and CI-gated -- the provenance is no longer external-only. The full")
print("  provenance scripts are vendored (frozen) under frontier_calcs/. The anchors themselves are cited")
print("  physical inputs; note (30_CANONICAL §A) v_A/B carry a self-consistency RESIDUAL band (no")
print("  independent air-plasmoid (B,n) measurement) -> every ABSOLUTE magnitude inherits it (linear for")
print("  v_A/hbar_eff/frequencies, square-law for b_eff); only DIMENSIONLESS RATIOS are load-bearing.")
print("  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
