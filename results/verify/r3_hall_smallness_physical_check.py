"""
Does the PHYSICAL plasmoid sit inside the regime R3 proves globally regular? Plug the canonical
numbers into R3's Hall-smallness condition (iii)  d_i ‖B‖∞ < c3 η  and read the answer.

R3 (R3_PM_NE_1_COUPLED_LYAPUNOV) removed the Pm=1 restriction and proved the coupled-enstrophy
functional bounded at ANY magnetic Prandtl number, UNDER one residual hypothesis -- a Hall/Lundquist
smallness on the individual-curl production term:

    |H_B| / (η ‖∇J‖²)  ~  (d_i ‖B‖∞ / η) · c_spec ,   c_spec = O(1)   [R3 note, line 108]
    controlled  iff   d_i ‖B‖∞  <  c3 η        (condition (iii))

In Alfvén-normalized MHD (the R3 induction equation ∂_t B = ∇×(v×B) − d_i ∇×(J×B) + η ΔB), the field
‖B‖∞ carries velocity units → v_A, and η is the magnetic diffusivity [m²/s]. So the DIMENSIONLESS
Hall-smallness number is  S_di ≡ d_i v_A / η , which must be ≲ 1 for R3's sufficient condition to hold.

Canonical inputs (30_CANONICAL_NUMBERS): d_i = λ_L = 0.2963 m [V] (§B); v_A = 2.033e4 m/s [residual]
(§A, with a 5-13× band); R = 0.12 m [credited] (§A). η is NOT tabulated -> estimated from Spitzer
resistivity across an honest plasma-temperature band (T_e = 1-30 eV).

RESULT (this check): the object does NOT satisfy condition (iii). Two robust, discipline-honest facts:
  (a) structural: d_i = 0.296 m > R = 0.12 m (d_i/R ≈ 2.5) -- the ion skin depth EXCEEDS the object,
      the defining signature of a STRONGLY Hall-mediated (electron-MHD / whistler) regime;
  (b) quantitative: S_di = d_i v_A / η ≈ 15-2400 >> 1 across the entire (T_e, v_A) band.
So the physical plasmoid lives OUTSIDE the regime R3 proves regular. This does NOT refute R3 (a
CONDITIONAL theorem) -- it locates the object: global regularity for THIS object stays open (the open
3D Hall-MHD problem), and the R2/R3 conditional bounds are the honest current ceiling. The gap is now
named in physical units, not hand-waved.

numpy only, deterministic. Run: python results/verify/r3_hall_smallness_physical_check.py
"""
import numpy as np

def banner(t): print("="*82); print(t); print("="*82)

mu0 = 4e-7*np.pi
d_i = 0.2963        # ion skin depth = λ_L [m], 30_CANONICAL §B [V]
vA = 2.033e4        # Alfvén speed [m/s], §A [residual]
R = 0.12            # object radius [m], §A [credited]

ok = True

# ---------------------------------------------------------------------------
banner("1) STRUCTURAL: the ion skin depth exceeds the object -> strongly Hall-mediated")
print("   d_i = %.4f m ,  R = %.2f m  ->  d_i / R = %.2f" % (d_i, R, d_i/R))
print("   d_i > R: the ion skin depth is LARGER than the plasmoid. Hall/two-fluid physics is not a")
print("   small correction here -- it is the leading dynamics (electron-MHD / whistler regime).")
ok = ok and d_i/R > 1

# ---------------------------------------------------------------------------
banner("2) QUANTITATIVE: the Hall-smallness number S_di = d_i v_A / eta  (condition (iii): must be <~ 1)")
def eta_m(T_eV, Z=1, lnL=10.0):
    """Spitzer magnetic diffusivity [m^2/s] = eta_Spitzer/mu0, eta_Spitzer = 5.2e-5 Z lnL T^-1.5 Ohm.m."""
    return (5.2e-5*Z*lnL*T_eV**-1.5)/mu0
prod = d_i*vA
print("   d_i v_A = %.0f m^2/s  (base v_A; the v_A residual x5-x13 only makes S_di larger)" % prod)
Svals = []
for T in (1, 5, 10, 30):
    em = eta_m(T); S = prod/em; Svals.append(S)
    print("     T_e=%2d eV:  eta = %7.1f m^2/s   S_di = %8.1f   -> %s"
          % (T, em, S, "VIOLATED (>1)" if S > 1 else "ok"))
print("   -> S_di >> 1 across the whole (T_e, v_A) band: Hall-smallness (iii) is ROBUSTLY VIOLATED.")
print("      (even the most favourable corner -- lowest v_A, highest eta at T=1 eV -- gives S_di ~ 15.)")
ok = ok and min(Svals) > 1

# ---------------------------------------------------------------------------
banner("VERDICT -- the gap named in physical units")
print("  The physical plasmoid does NOT satisfy R3's Hall-smallness condition (iii): it is strongly")
print("  Hall-mediated (d_i > R; S_di = d_i v_A/eta ~ 15-2400 >> 1). It therefore lives OUTSIDE the")
print("  regime R3 proves globally regular. This does NOT refute R3 -- R3 is a CONDITIONAL theorem,")
print("  and its hypotheses are honestly stated -- it LOCATES the object: global regularity for this")
print("  specific object remains open (the open 3D Hall-MHD problem), and the R2/R3 conditional")
print("  enstrophy bounds are the current honest ceiling. The check ran; the answer is definite and")
print("  robust across the calibration band. status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
