# -*- coding: utf-8 -*-
"""
TOOLKIT ADV M7 - BUCKINGHAM PI THEORY as CLAIM-AUDIT + DIMENSIONLESS-SCALING MAP
Reproducible computation for MATH_TOOLKIT module ADV_07.

Run:  PYTHONIOENCODING=utf-8 python toolkit_adv07_buckingham_pi.py

What this script DOES (compute-before-assert; no fabrication):
  * Builds the three FTGB dimensional matrices D over base dims (M,L,T,I,Theta,N).
  * Uses sympy for EXACT integer/rational rank and null-space basis.
  * Reports n (variables), r (rank), N_Pi = n - r (independent dimensionless groups).
  * Verifies that each PROPOSED named Pi-group is actually dimensionless (D a = 0).
  * Demonstrates base-dimension-choice INVARIANCE: SI-with-current(I) vs the QWM
    'charge e ~ kg*rad/s' spin-angular-momentum base choice give the SAME Pi-groups.
  * Verifies Lambda_1 = 4.493409 as the first nonzero root of tan(x)=x (CK/Beltrami
    ball boundary problem) and reproduces the inharmonic carrier comb f_n.
  * Verifies the Kerker/Huygens first-condition group p/(eps0 Z0 m) is dimensionless.

What Pi theory does NOT do (stated in the doc, not derivable here): pick the
variables, name the mechanism, give the function f, fix the O(1) constant, or
establish stability. It gives ALLOWED SCALING ONLY.

Deps: numpy, sympy, scipy.  ASCII only.
"""
import numpy as np
import sympy as sp
from scipy.optimize import brentq

OUT = []
def log(s=""):
    print(s)
    OUT.append(s)

# base dimensions, fixed order
BASE = ["M", "L", "T", "I", "Theta", "N"]

def dimvec(**kw):
    """Return an exponent vector over BASE from keyword exponents."""
    return [sp.Rational(kw.get(b, 0)) for b in BASE]

def build_D(varnames, vardims):
    """D: rows = base dims, cols = variables. sympy Matrix (exact)."""
    return sp.Matrix([[vardims[v][i] for v in varnames] for i in range(len(BASE))])

def analyze(title, varnames, vardims, proposed=None):
    """Print D, rank, N_Pi, a null-space basis, and verify proposed Pi-groups."""
    D = build_D(varnames, vardims)
    n = len(varnames)
    r = D.rank()
    npi = n - r
    log("-" * 74)
    log(title)
    log("-" * 74)
    log("  variables (n=%d): %s" % (n, ", ".join(varnames)))
    # print the matrix compactly, only rows that are not all-zero (+ note which)
    log("  dimensional matrix D (rows = %s):" % ", ".join(BASE))
    for i, b in enumerate(BASE):
        row = [D[i, j] for j in range(n)]
        if any(v != 0 for v in row):
            log("    %-5s : [%s]" % (b, " ".join("%3s" % str(v) for v in row)))
        else:
            log("    %-5s : [%s]   (zero row - dim not used)" %
                (b, " ".join("%3s" % "0" for _ in row)))
    log("  rank r = %d   (base-dim symbols present but rank-independent do NOT add to r)" % r)
    log("  N_Pi = n - r = %d independent dimensionless groups" % npi)
    # exact null-space basis (each vector -> one Pi group Pi = prod q_j^{a_j})
    ns = D.nullspace()
    log("  null-space basis (each column vector a solves D a = 0 -> one Pi group):")
    for k, vv in enumerate(ns):
        # clear denominators for readability
        vv = sp.Matrix(vv)
        lcm = sp.ilcm(*[sp.fraction(sp.nsimplify(x))[1] for x in vv]) if any(
            sp.fraction(x)[1] != 1 for x in vv) else 1
        vvi = vv * lcm
        terms = []
        for name, e in zip(varnames, vvi):
            if e != 0:
                terms.append("%s^%s" % (name, sp.nsimplify(e)))
        log("    a%-2d = %-30s  ->  Pi = %s" %
            (k + 1, str([sp.nsimplify(x) for x in vvi]), " * ".join(terms)))
    # verify proposed named groups are dimensionless AND independent
    if proposed:
        log("  PROPOSED named Pi-groups (verify each is dimensionless: D a = 0):")
        vecs = []
        for pname, expo in proposed:
            a = sp.Matrix([sp.Rational(expo.get(v, 0)) for v in varnames])
            resid = D * a
            ok = all(x == 0 for x in resid)
            vecs.append(list(a))
            log("    %-14s exps=%s  dimensionless: %s" %
                (pname, {k: str(sp.nsimplify(expo[k])) for k in expo}, "YES" if ok else "NO -> BUG"))
        M = sp.Matrix(vecs).T  # columns = proposed groups
        rk = M.rank()
        log("    -> proposed set rank = %d (need %d for a complete independent basis): %s" %
            (rk, npi, "COMPLETE BASIS" if rk == npi and len(vecs) == npi else
             ("SPANS (extra/rank<count)" if rk == npi else "INCOMPLETE")))
    log("")
    return D, r, npi

log("=" * 74)
log("TOOLKIT ADV M7 - BUCKINGHAM PI : FTGB dimensional matrices + null-space groups")
log("Buckingham, Phys. Rev. 4, 345 (1914). Base dims (M,L,T,I,Theta,N), SI primary.")
log("=" * 74)
log("")

# ======================================================================
# SI dimensional dictionary (current I as an independent base dim)
# T_e is carried as THERMAL ENERGY (k_B*T_e) [M L^2 T^-2], so Theta does NOT
# appear (standard plasma convention; k_B absorbed). Number density n is a pure
# count per volume [L^-3] (amount N=0). Both choices are stated in the doc.
# ======================================================================
SI = {
    # force-free object
    "B":     dimvec(M=1, T=-2, I=-1),           # magnetic flux density (Tesla)
    "n_i":   dimvec(L=-3),                        # ion number density
    "m_i":   dimvec(M=1),                         # ion mass
    "R":     dimvec(L=1),                          # object radius
    "mu0":   dimvec(M=1, L=1, T=-2, I=-2),        # vacuum permeability (H/m)
    "omega": dimvec(T=-1),                         # angular frequency (rad/s)
    # plasma resonator extras
    "n_e":   dimvec(L=-3),
    "T_e":   dimvec(M=1, L=2, T=-2),               # thermal energy k_B T_e (J)
    "e":     dimvec(T=1, I=1),                      # elementary charge (C = A s)
    "eps0":  dimvec(M=-1, L=-3, T=4, I=2),         # vacuum permittivity (F/m)
    # metasurface
    "f0":    dimvec(T=-1),
    "Lind":  dimvec(M=1, L=2, T=-2, I=-2),         # inductance (Henry)
    "C":     dimvec(M=-1, L=-2, T=4, I=2),         # capacitance (Farad)
    "a":     dimvec(L=1),                           # cell size
    "t":     dimvec(L=1),                           # metal/dielectric thickness
    "sigma": dimvec(M=-1, L=-3, T=3, I=2),         # conductivity (S/m)
    "c":     dimvec(L=1, T=-1),                      # speed of light
    # Kerker check
    "p":     dimvec(L=1, T=1, I=1),                 # electric dipole moment (C m)
    "m_mag": dimvec(L=2, I=1),                       # magnetic dipole moment (A m^2)
    "Z0":    dimvec(M=1, L=2, T=-3, I=-2),          # wave impedance (Ohm)
}

# ======================================================================
# MATRIX 1 : FORCE-FREE OBJECT   {B, n_i, m_i, R, mu0, omega}
# ======================================================================
v1 = ["B", "n_i", "m_i", "R", "mu0", "omega"]
prop1 = [
    ("omegaR/v_A", {"omega": 1, "R": 1, "mu0": sp.Rational(1, 2),
                    "n_i": sp.Rational(1, 2), "m_i": sp.Rational(1, 2), "B": -1}),
    ("n R^3",      {"n_i": 1, "R": 3}),
]
analyze("MATRIX 1 - FORCE-FREE OBJECT  {B, n_i, m_i, R, mu0, omega}",
        v1, SI, prop1)

# natural groups + the modal eigenvalue Lambda_n
log("  NATURAL GROUPS of matrix 1:")
log("    v_A = B / sqrt(mu0 n_i m_i)     [the ONLY velocity buildable] -> Alfven speed")
log("    Pi_A = omega R / v_A            [dimensionless frequency = Alfven-Mach]")
log("    f_A = v_A / (2 pi R)            [Alfven transit frequency]")
log("    Pi_N = n_i R^3                  [# ions in the volume; a 2nd, geometric group]")
log("  The modal law  f_n = Lambda_n * v_A/(2 pi R)  <=>  Lambda_n = 2 pi f_n R / v_A = (omega_n R/v_A)")
log("    i.e. Lambda_n IS the value the Alfven-Mach Pi-group takes AT resonance n.")
log("    Pi theory gives the FORM f_n ~ v_A/R ; it does NOT give Lambda_n. Lambda_n is set")
log("    by the geometry + boundary condition (an eigenvalue), NOT by the theorem.")
log("")

# ======================================================================
# BASE-DIMENSION-CHOICE INVARIANCE (SI-with-I  vs  QWM spin base)
# QWM framework [UNASSESSED method-only]: treat charge e as an angular momentum
# [kg rad/s ~ kg/s], i.e. re-express the current dimension I via e. We MODEL this
# as a change of base from (M,L,T,I) to (M,L,T,Q) with Q the charge dimension
# (e ~ Q = A s). Buckingham's theorem is invariant under any invertible change of
# base dimensions -> SAME number of Pi-groups, SAME groups. Show it on matrix 1.
# ======================================================================
log("-" * 74)
log("INVARIANCE CHECK - base-dimension choice does not change the Pi-groups")
log("-" * 74)
# rebuild matrix 1 in a (M,L,T,Q) base where charge Q replaces current I (Q = I*T).
# The map I -> Q/T is invertible, so rank and null space are preserved.
BASE_Q = ["M", "L", "T", "Q"]
def to_Q(vec):
    """Convert an (M,L,T,I,Theta,N) exponent vector to (M,L,T,Q) with Q=I*T.
    A quantity with I^a * (time) contributions: since Q=I*T, we have I = Q/T,
    so an I^a factor becomes Q^a * T^-a . Theta,N assumed 0 here."""
    M_, L_, T_, I_, Th_, N_ = vec
    return [M_, L_, T_ - I_, I_]  # (M, L, T', Q) with T' = T - I, Q = I
SIQ = {k: to_Q(v) for k, v in SI.items()}
Dq = sp.Matrix([[SIQ[v][i] for v in v1] for i in range(len(BASE_Q))])
log("  matrix 1 re-expressed in base (M,L,T,Q), Q = charge dimension (e ~ Q):")
for i, b in enumerate(BASE_Q):
    log("    %-2s : [%s]" % (b, " ".join("%3s" % str(Dq[i, j]) for j in range(len(v1)))))
log("  rank(SI, current I) = %d ; rank(QWM base, charge Q) = %d  -> EQUAL: %s" %
    (build_D(v1, SI).rank(), Dq.rank(),
     "YES (invariant)" if build_D(v1, SI).rank() == Dq.rank() else "NO"))
# check the SAME named groups are still null
for pname, expo in prop1:
    a = sp.Matrix([sp.Rational(expo.get(v, 0)) for v in v1])
    ok = all(x == 0 for x in (Dq * a))
    log("    group %-12s still dimensionless in charge-base: %s" % (pname, "YES" if ok else "NO"))
log("  => the Pi-groups (omega R/v_A, n R^3) are IDENTICAL; only the base labels change.")
log("")

# ======================================================================
# MATRIX 2 : PLASMA RESONATOR
#   {omega, B, n_e, R, m_i, T_e, e, eps0, mu0}
# ======================================================================
v2 = ["omega", "B", "n_e", "R", "m_i", "T_e", "e", "eps0", "mu0"]
half = sp.Rational(1, 2)
prop2 = [
    ("beta",      {"mu0": 1, "n_e": 1, "T_e": 1, "B": -2}),           # 2 mu0 n kT / B^2
    ("omega/wci", {"omega": 1, "m_i": 1, "e": -1, "B": -1}),          # omega / omega_ci
    ("d_i/R",     {"m_i": half, "mu0": -half, "n_e": -half, "e": -1, "R": -1}),  # ion skin depth / R
    ("lam_D/R",   {"eps0": half, "T_e": half, "n_e": -half, "e": -1, "R": -1}),  # Debye / R
    ("n_e R^3",   {"n_e": 1, "R": 3}),                                # ions in the volume
]
analyze("MATRIX 2 - PLASMA RESONATOR  {omega,B,n_e,R,m_i,T_e,e,eps0,mu0}",
        v2, SI, prop2)
log("  CONTROL-PARAMETER MAP (a complete independent basis of the 5 groups):")
log("    beta      = 2 mu0 n_e kT_e / B^2         plasma pressure / magnetic pressure")
log("    omega/wci = omega m_i /(e B)             drive vs ion-cyclotron (Hall/FLR onset)")
log("    d_i/R     = sqrt(m_i/(mu0 n e^2)) / R    ion skin depth / size (two-fluid onset)")
log("    lam_D/R   = sqrt(eps0 kT/(n e^2)) / R    Debye length / size (quasineutrality)")
log("    n_e R^3                                   # ions in the volume (geometric)")
log("  DERIVED (products of the basis, NOT new groups):")
log("    omegaR/vA = (omega/wci) * (R/d_i)        the CARRIER (v_A = omega_ci * d_i exactly)")
log("    omega/wpe, omega/wpi, S(Lundquist)       need m_e / a collision freq nu_e / eta")
log("  NOT buildable from THESE 9 variables (need extra variables - honest gaps):")
log("    d_e/R  needs electron mass m_e  (adds the pure ratio m_e/m_i)")
log("    nu/omega, Lundquist S  need a collision freq nu_e or resistivity eta")
log("    Hall k d_i, omega/omega_pe(as indep) need a wavenumber k / it reduces via c")
log("    (c = 1/sqrt(eps0 mu0) is DERIVED here, not independent -> no new group)")
log("")

# ======================================================================
# MATRIX 3 : METASURFACE / HUYGENS
#   dimensional core {f0, Lind, C, a, t, sigma, mu0, c}
#   (eps_r, mu_r, and all angles are ALREADY dimensionless -> each its own Pi)
# ======================================================================
v3 = ["f0", "Lind", "C", "a", "t", "sigma", "mu0", "c"]
prop3 = [
    ("Pi_LC = f0 sqrt(LC)", {"f0": 1, "Lind": half, "C": half}),
    ("Pi_cell = a f0/c",    {"a": 1, "f0": 1, "c": -1}),
    ("Pi_thick = t/a",      {"t": 1, "a": -1}),
    ("Pi_skin = t/delta",   {"t": 1, "f0": half, "mu0": half, "sigma": half}),  # delta=sqrt(2/(w mu sig))
    ("Pi_Zind = f0 L/(mu0 c)", {"f0": 1, "Lind": 1, "mu0": -1, "c": -1}),        # w L / Z0
]
analyze("MATRIX 3 - METASURFACE/HUYGENS  {f0,Lind,C,a,t,sigma,mu0,c}",
        v3, SI, prop3)
log("  NOTE: rank r=3 here (not 4): with only circuit/EM quantities and NO bare charge")
log("        or eps0, the current dim locks as I = -2M (a left-null of D) -> r drops,")
log("        N_Pi rises to 5. A textbook illustration that rank != count of unit symbols.")
log("  Pi_LC   = 2 pi f0 sqrt(L C)              LC self-resonance tuning")
log("  Pi_cell = a/lambda = a f0/c              subwavelength unit-cell (Huygens needs <<1)")
log("  Pi_thick= t/a  (or t f0/c)               thickness/size (thin-sheet limit)")
log("  Pi_skin = t/delta, delta=sqrt(2/(w mu0 sigma))   ohmic penetration")
log("  Pi_Zind = f0 L/(mu0 c) = omega L/Z_0     reactance vs free-space impedance (= Z_s/Z_0 family)")
log("  eps_r, mu_r, theta_inc, theta_out, cone-angle alpha : ALREADY dimensionless")
log("    -> each counts as an independent variable AND is itself a trivial Pi-group.")
log("  Cone {R_apex,R_base,lambda} -> length ratios R_apex/lambda, R_base/R_apex (taper).")
log("")

# Kerker / Huygens first condition : p / (eps0 Z0 m) ~ 1 (+ i0)  [zero backscatter]
log("  KERKER/HUYGENS matching group  Pi_Kerker = p / (eps0 Z0 m_mag) :")
vK = ["p", "eps0", "Z0", "m_mag"]
aK = sp.Matrix([1, -1, -1, -1])  # p^1 eps0^-1 Z0^-1 m_mag^-1
DK = build_D(vK, SI)
okK = all(x == 0 for x in (DK * aK))
log("    p/(eps0 Z0 m_mag) dimensionless: %s  (first Kerker condition -> S11 minimum)" %
    ("YES" if okK else "NO"))
log("    (p = electric dipole, m_mag = magnetic dipole; = 1 balances the two -> no back-scatter)")
log("")

# ======================================================================
# CHECK - Lambda_1 = 4.493409 from tan(x)=x  (CK/Beltrami BALL boundary problem)
# ======================================================================
log("-" * 74)
log("CHECK - CK/Beltrami eigenvalue Lambda_1 = lambda_1 R = 4.493409  (root of tan x = x)")
log("-" * 74)
def f(x):
    return np.tan(x) - x
roots = []
for k in range(1, 7):
    lo = k * np.pi + 0.05
    hi = (k + 0.5) * np.pi - 1e-6
    roots.append(brentq(f, lo, hi, xtol=1e-14, rtol=1e-15))
log("  first 6 nonzero roots of tan x = x (Lambda_n):")
log("    " + ", ".join("%.6f" % r for r in roots))
log("  Lambda_1 = %.6f   (canonical 4.493409)  -> match: %s" %
    (roots[0], "PASS" if abs(roots[0] - 4.493409) < 1e-5 else "FAIL"))
log("  inharmonic ratios Lambda_n/Lambda_1 : " +
    ", ".join("%.3f" % (r / roots[0]) for r in roots))
log("  (canonical 1, 1.719, 2.427, 3.13, 3.83, 4.53 -- bell-like, since tan x = x)")

# reproduce the carrier comb f_n = Lambda_n v_A/(2 pi R)  (canonical medium anchors)
v_A = 2.033e4      # m/s   (canonical residual, 30_CANONICAL_NUMBERS.md A)
R   = 0.12         # m
f_n = [r * v_A / (2 * np.pi * R) for r in roots]
log("  carrier comb f_n = Lambda_n v_A/(2 pi R)  with v_A=2.033e4 m/s, R=0.12 m:")
log("    " + ", ".join("%.1f kHz" % (fn / 1e3) for fn in f_n))
log("    (canonical 121.2, 208.3, 294.0, 379.3, 464.3, 549.3 kHz) -> match f_1: %s" %
    ("PASS" if abs(f_n[0] / 1e3 - 121.2) < 0.5 else "FAIL"))
log("  CORRECTIVE [V/S]: Lambda_1=4.4934 is the BALL(sphere) eigenvalue ONLY. For the")
log("  actual toroidal/conical object Lambda_n = Lambda_n(r_minor/R_major, d_i/R, beta, S, ...)")
log("  -- a FUNCTION of the Pi-groups above, NOT a universal constant.")
log("")

# ======================================================================
# CHECK - v_A, f_A, beta numeric sanity from canonical anchors
# ======================================================================
log("-" * 74)
log("CHECK - natural-group numeric values from the 4 canonical anchors {B,n_i,m_i,R}")
log("-" * 74)
mu0 = 4e-7 * np.pi
B = 20.6e-3        # T
n_i = 1.7e19       # m^-3
m_i = 29 * 1.66053906660e-27  # kg (29 amu)
vA_calc = B / np.sqrt(mu0 * n_i * m_i)
fA = vA_calc / (2 * np.pi * R)
log("  B=20.6 mT, n_i=1.7e19 /m^3, m_i=29 amu, R=0.12 m")
log("  v_A = B/sqrt(mu0 n_i m_i) = %.4e m/s   (canonical 2.033e4)" % vA_calc)
log("  f_A = v_A/(2 pi R)        = %.3f kHz" % (fA / 1e3))
log("  f_1 = Lambda_1 f_A        = %.1f kHz   (carrier)" % (roots[0] * fA / 1e3))
# example beta (needs a T_e; use a plausible 2 eV just to show the group evaluates)
kTe = 2 * 1.602176634e-19  # 2 eV in J (ILLUSTRATIVE ONLY - not a canonical anchor)
beta = 2 * mu0 * n_i * kTe / B**2
log("  beta = 2 mu0 n kT/B^2 = %.3f  (ILLUSTRATIVE kT_e=2 eV; T_e is NOT a canonical anchor)" % beta)
log("  n_i R^3 = %.3e  (# ions in the volume, the 2nd geometric group)" % (n_i * R**3))
log("")

log("=" * 74)
log("SUMMARY")
log("  Matrix 1 (force-free object) : n=6, r=4, N_Pi=2  -> {omega R/v_A, n R^3}")
log("  Matrix 2 (plasma resonator)  : n=9, r=4, N_Pi=5  -> {beta, omega/wci, d_i/R, lam_D/R, n R^3}")
log("  Matrix 3 (metasurface)       : n=8, r=3, N_Pi=5  -> {f0 sqrt(LC), a/lambda, t/a, t/delta, wL/Z0}")
log("  Lambda_1 = %.6f from tan x = x (BALL eigenvalue; geometry-dependent, NOT universal)" % roots[0])
log("  Base-dim choice (SI-I vs QWM charge-Q) : SAME rank, SAME Pi-groups (invariance).")
log("  Pi theory = ALLOWED SCALING ONLY : no mechanism, no f, no constant, no stability.")
log("=" * 74)

with open("toolkit_adv07_buckingham_pi_OUT.txt", "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT) + "\n")
