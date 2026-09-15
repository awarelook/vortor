"""
The polarizable-vacuum (PV) gravity reading is GR-EQUIVALENT -> no propulsion, no levitation, no anti-gravity:
the project's central fence, harnessed. A computed settled-negative (M11/EGM thread).

The jewel carries a K_PV polarizable-vacuum representation (MATH_TOOLKIT_BASE §9c; TOOLKIT M11): the wave speed
of the medium is read as a variable refractive index K_PV, and for a static mass K_PV(r) = exp(2GM/rc^2)
[credited: Puthoff, PV representation of GR]. The firewall states plainly that "no vacuum-energy / gravity /
propulsion mechanism is invoked -- the PV-gravity levitation reading returned a clean NEGATIVE." This check
turns that prose negative into a re-runnable one, using only convention-robust statements (it does NOT depend
on the c/K vs c/sqrt(K) light-speed convention, so it cannot be tripped by that subtlety).

  TEST 1 -- THE REPRESENTATION IS GR AT WEAK FIELD [credited: Puthoff]. K_PV(r) = exp(2 GM / r c^2); its
            weak-field expansion is 1 + 2 GM/rc^2 (coefficient exactly 2). The gravitational REDSHIFT it
            predicts, Delta_nu/nu = GM/rc^2, reproduces the GR/measured value -- e.g. the solar surface
            redshift GM_sun/(R_sun c^2) = 2.12e-6 (measured ~2.12e-6). PV is a MECHANISM re-description of GR,
            not new physics: it adds no term GR does not have.
  TEST 2 -- THE INDEX WELL IS ALWAYS ATTRACTIVE FOR POSITIVE MASS [V]-arith (convention-robust). Near a
            positive mass K_PV > 1, so the optical index n (= K_PV or sqrt(K_PV), EITHER convention) is > 1
            and RISES toward the mass; a gradient-index gradient bends rays/deflects test bodies toward the
            higher index -- i.e. toward the mass. So the PV force is ATTRACTIVE for every positive M, at every
            radius. There is no positive-mass configuration whose K_PV gradient repels.
  TEST 3 -- THEREFORE LEVITATION / ANTI-GRAVITY / REACTIONLESS PROPULSION IS SETTLED-NEGATIVE. A repulsive
            (levitating) PV well requires K_PV < 1, i.e. exp(2 GM/rc^2) < 1, i.e. GM < 0 -- NEGATIVE
            mass-energy. Ordinary matter and the FTGB object's own POSITIVE field energy have GM > 0, hence
            attract normally. So the object gravitates like any energy; the PV representation licenses NO
            propulsion, NO levitation, NO anti-gravity, and NO over-unity -- exactly the firewall's fence,
            now computed. (Storti's "graviton = conjugate photon pair" propulsion interpretation is the
            [EGM method] piece the toolkit explicitly does NOT adopt.)

  HONEST SCOPE: this verifies the GR-EQUIVALENCE at weak field (redshift, convention-robust) and the
  attractive-sign no-go; it does NOT re-derive the light-bending factor (that is where the c/K vs c/sqrt(K)
  convention enters, and PV's reproduction of the 4GM/c^2b GR value is credited to Puthoff, not re-done here).
  The negative is structural: PV = GR, and GR has no reactionless propulsion for ordinary (positive) stress-
  energy. No new gravity physics is claimed.

numpy only, deterministic. Run: python results/verify/pv_gravity_no_propulsion_check.py
"""
import numpy as np

ok = True
G = 6.674e-11          # m^3 kg^-1 s^-2
C = 2.99792458e8       # m/s
M_SUN = 1.989e30       # kg
R_SUN = 6.957e8        # m
GM_SUN = G * M_SUN     # m^3/s^2


def banner(t):
    print("=" * 98); print(t); print("=" * 98)


def check(name, cond, detail=""):
    global ok
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, ("  -- " + detail) if detail else ""))
    ok = ok and cond


def K_PV(r, GM):
    return np.exp(2.0 * GM / (r * C ** 2))


banner("TEST 1 -- the PV representation is GR at weak field: K_PV = exp(2GM/rc^2), redshift = GM/rc^2  [credited]")
# weak-field expansion coefficient
r = R_SUN
phi = GM_SUN / (r * C ** 2)                       # dimensionless potential
k = K_PV(r, GM_SUN)
coeff = (k - 1.0) / phi                            # -> 2 as phi -> 0
redshift = GM_SUN / (R_SUN * C ** 2)
print("   at the solar surface: GM/rc^2 = %.3e ;  K_PV = %.10f ;  (K_PV-1)/(GM/rc^2) = %.4f (-> 2)" % (phi, k, coeff))
print("   predicted gravitational redshift Delta_nu/nu = GM_sun/(R_sun c^2) = %.3e  (measured ~2.12e-6)" % redshift)
check("weak-field K_PV expansion coefficient = 2", abs(coeff - 2.0) < 1e-4, "%.5f" % coeff)
check("solar-surface redshift reproduces the measured 2.12e-6", abs(redshift - 2.12e-6) < 0.03e-6, "%.3e" % redshift)

banner("TEST 2 -- the index well is ALWAYS attractive for positive mass (convention-robust)  [V]-arith")
radii = R_SUN * np.array([1.0, 2.0, 5.0, 20.0, 100.0])
kv = K_PV(radii, GM_SUN)
# both conventions: n = K_PV or n = sqrt(K_PV); both are monotone in K_PV, so test K_PV's gradient sign
dK = np.diff(kv)                                   # K_PV vs increasing r
print("   K_PV at r/R_sun = [1,2,5,20,100]: %s" % np.array2string(kv, formatter={'float_kind': lambda v: '%.3e' % (v - 1) + '+1'}))
print("   d(K_PV)/dr < 0 at every step (index rises toward the mass -> deflection toward the mass):", bool(np.all(dK < 0)))
check("K_PV > 1 everywhere near a positive mass", bool(np.all(kv > 1.0)), "index exceeds 1 -> optically denser toward mass")
check("K_PV decreases monotonically outward (gradient points inward = ATTRACTIVE), both conventions",
      bool(np.all(dK < 0)), "n = K_PV or sqrt(K_PV): both monotone in K_PV, so the attractive sign is convention-free")

banner("TEST 3 -- levitation / anti-gravity / propulsion is SETTLED-NEGATIVE (needs negative mass)")
# a repulsive (levitating) well needs K_PV < 1 <=> GM < 0
GM_needed_sign = -1.0
k_neg = K_PV(R_SUN, GM_SUN * GM_needed_sign)       # what a "repulsive" well would require
print("   a repulsive/levitating PV well requires K_PV < 1 at the source, i.e. exp(2GM/rc^2) < 1, i.e. GM < 0.")
print("   with GM < 0 (negative mass) one would get K_PV = %.10f < 1; ordinary matter and the object's OWN" % k_neg)
print("   positive field energy have GM > 0 -> K_PV > 1 -> attractive. No positive-energy source levitates.")
check("repulsive well requires negative mass-energy (K_PV<1 <=> GM<0)", k_neg < 1.0, "%.10f" % k_neg)
check("the object's positive field energy gravitates attractively (no propulsion/over-unity from PV)",
      K_PV(R_SUN, GM_SUN) > 1.0, "PV-gravity = GR (credited); GR has no reactionless propulsion for positive stress-energy")

banner("VERDICT")
print("  The K_PV polarizable-vacuum representation is GR at weak field (TEST 1, redshift reproduced) and its")
print("  index well is attractive for every positive mass (TEST 2). Levitation/anti-gravity/reactionless")
print("  propulsion would require negative mass-energy (TEST 3), which ordinary matter and the object's own")
print("  positive field energy do not provide. So the PV-gravity/levitation reading is a computed")
print("  SETTLED-NEGATIVE -- the firewall's central fence (no propulsion, no levitation, no over-unity),")
print("  harnessed. PV re-describes GR's mechanism; it adds no new gravitational physics.")
print("  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
