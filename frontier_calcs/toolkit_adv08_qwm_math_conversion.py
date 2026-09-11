#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TOOLKIT ADV M8 -- QWM (Reed Quantum Wave Mechanics) MATH CONVERSION + DIMENSIONAL AUDIT
=======================================================================================
CONVERT-AND-CHECK pass. For each QWM mass/charge expression this script performs the
"CHECK": it reduces the RHS to base dimensions in TWO unit systems and reports whether
it yields kg [mass]:

  (A) SI-strict    : base {M, L, T, I}; angle 'rad' is DIMENSIONLESS (A -> 0).
                     charge is Coulomb = I*T. This is the referee/standard check.
  (B) QWM (L's)    : base {M, L, T, A} with angle 'rad' = A a genuine base dimension,
                     NO current base. charge e ~ [kg*rad/s] = M*A*T^-1 (spin ang. mom.).
                     A(vec pot) ~ m/rad = L*A^-1 ; B ~ 1/rad = A^-1 ; E(field) ~ L*T^-1*A^-1.

Method backbone: TOOLKIT_ADV_07 Buckingham-Pi (sympy exact exponent bookkeeping).
Honors held corrections: D1 (mass != whirl-number), D2/D3 (A.B is helicity density
m/rad^2, NOT matter density kg/m^3 -> proportionality with carried constant kappa),
D4 (charge = spin ang. mom. kg*rad/s), K0(pi3 S2 helicity) != baryon B(pi3 S3) != Q_H(linking).

No fabrication: numbers are CODATA-2018 or arithmetic thereof. Coincidence-gate at 0.5%
vs phi^n and 137^n. ASCII only; PYTHONIOENCODING=utf-8.
"""
import sympy as sp
import numpy as np

# ---------------------------------------------------------------------------
# Base-dimension symbols. We carry all of {M,L,T,I,A}; each unit system zeroes
# the ones it does not use (SI: A=0 angle dimensionless; QWM: I absent).
# ---------------------------------------------------------------------------
M, L, T, I, A = sp.symbols('M L T I A')  # mass length time current angle(rad)
MASS_TARGET = M                          # we want RHS == M (kg)

def report(name, expr, target=MASS_TARGET):
    """Return (pass_bool, residual_expr) where residual = expr - target in log-exponent space."""
    diff = sp.simplify(expr - target)
    ok = (diff == 0)
    return ok, diff

# ===========================================================================
# (A) SI-STRICT dimensions (angle rad dimensionless -> A exponent 0)
# ===========================================================================
SI = {
    'hbar' : M + 2*L - T,          # J*s = kg m^2 / s
    'c'    : L - T,                # m/s
    'omega': -T,                   # rad/s -> 1/s  (rad dimensionless)
    'omega_C': -T,
    'k'    : -L,                   # 1/m
    'E'    : M + 2*L - 2*T,        # J = kg m^2/s^2
    'Erest': M + 2*L - 2*T,        # rest energy (E_s0+E_m0)
    'v'    : L - T,                # m/s
    'beta_c': L - T,               # beta*c = velocity
    'a'    : L - 2*T,              # m/s^2
    'Efield': M + L - 3*T - I,     # V/m = kg m /(s^3 A)
    'B'    : M - 2*T - I,          # Tesla = kg/(s^2 A)
    'Avec' : M + L - 2*T - I,      # vector potential Wb/m = T*m = kg m/(s^2 A)
    'q'    : I + T,                # charge Coulomb = A*s
    'V'    : M + 2*L - 3*T - I,    # volt = kg m^2/(s^3 A)
    'EoverB': (M + L - 3*T - I) - (M - 2*T - I),   # E/B  -> should be L - T (velocity)
}
# derived: E/B velocity check
assert sp.simplify(SI['EoverB'] - (L - T)) == 0, "E/B is not a velocity in SI!"

# ===========================================================================
# (B) QWM dimensions (L's table: angle A a base dim; charge = kg*rad/s; no I)
# ===========================================================================
QWM = {
    'hbar' : M + 2*L - T + A,      # rad*kg*m^2/s   (L's action row carries a rad)
    'c'    : L - T,
    'omega': A - T,                # rad/s
    'omega_C': A - T,
    'k'    : -L,
    'E'    : M + 2*L - 2*T,        # energy kg m^2/s^2 (angle-free)
    'Erest': M + 2*L - 2*T,
    'v'    : L - T,
    'beta_c': L - T,
    'a'    : L - 2*T,
    'Efield': L - T - A,           # QWM: E-field so that E/B is a velocity: (L-T-A)-(-A)=L-T
    'B'    : -A,                   # 1/rad
    'Avec' : L - A,                # m/rad
    'q'    : M + A - T,            # kg*rad/s = spin angular momentum
    'V'    : 2*L - T - A,          # QWM volt = m^2/(s*rad) (Table 21-1: V ~ L^2 T^-1 A^-1)
    'EoverB': (L - T - A) - (-A),  # = L - T velocity
}
assert sp.simplify(QWM['EoverB'] - (L - T)) == 0, "E/B is not a velocity in QWM!"

# ===========================================================================
# THE MASS FORMS.  Each defined as a callable of a dim-dict -> net dimension.
# We check L's 7 equivalent forms + the anchor identities.
# NOTE the KEY CATCH: primary Ch.21 Table 21-1 has m = E/(Escript/B)^2 (SQUARED);
# L's ledger transcribed it (and form 2) WITHOUT the square. We check BOTH.
# ===========================================================================
def forms(D):
    f = {}
    # --- anchor identity [V]: m = hbar*omega_C / c^2 ---
    f['ID  m = hbar*omega_C / c^2']          = D['hbar'] + D['omega_C'] - 2*D['c']
    # --- QWM lab-frame: m = e / omega  (D4) ---
    f['D4  m = e / omega']                   = D['q'] - D['omega']
    # --- another Reed/Mead form: m = hbar*k / v ---
    f['     m = hbar*k / v']                 = D['hbar'] + D['k'] - D['v']
    # --- L form 1 AS TRANSCRIBED (no square): m = E/(E/B) ---
    f['L1  m = E/(Ef/B)      [as written]']  = D['E'] - D['EoverB']
    # --- L form 1 CORRECTED to primary (squared): m = E/(E/B)^2 ---
    f['L1* m = E/(Ef/B)^2    [primary]']     = D['E'] - 2*D['EoverB']
    # --- L form 2 AS TRANSCRIBED: m = (Es0+Em0)/(E/B) ---
    f['L2  m = Erest/(Ef/B)  [as written]']  = D['Erest'] - D['EoverB']
    # --- L form 2 CORRECTED (squared, = E_rest/c^2 iff E/B=c): m = Erest/(E/B)^2 ---
    f['L2* m = Erest/(Ef/B)^2[primary]']     = D['Erest'] - 2*D['EoverB']
    # --- L form 3: m = (hbar*k - q*A)/(beta*c) ; kinetic momentum / velocity ---
    #     both terms hbar*k and q*Avec must be momentum; check the q*Avec term dim:
    f['L3  m=(hk-qA)/(beta c) [qA term]']    = (D['q'] + D['Avec']) - D['beta_c']
    f['L3  m=(hk-qA)/(beta c) [hk term]']    = (D['hbar'] + D['k']) - D['beta_c']
    # --- L form 5: m = |V*q| / c^2 ---
    f['L5  m = |V*q| / c^2']                 = D['V'] + D['q'] - 2*D['c']
    # --- L form 6: m = -e*Efield / a  (F=ma with F=eE) ---
    f['L6  m = e*Efield / a']                = D['q'] + D['Efield'] - D['a']
    # --- L form 7: m = A*e / v  (canonical qA = mv) ---
    f['L7  m = Avec*e / v']                  = D['Avec'] + D['q'] - D['v']
    return f

# --- L form 4 handled separately (needs a hidden constant / L is not ang.mom.) ---
def form4_diagnose(D):
    """m = 2L/(Ef^2 - c^2 B^2).  Field-invariant (Ef^2 - c^2 B^2) net dim, and what 'L' must be."""
    field_inv = 2*D['Efield']            # Ef^2 ; must equal (c B)^2
    cB2 = 2*(D['c'] + D['B'])
    same = sp.simplify(field_inv - cB2)  # 0 => Ef^2 and c^2B^2 share dim (subtractable)
    needed_L = MASS_TARGET + field_inv   # 'L' numerator dim required so ratio = M
    return same, field_inv, needed_L

# ---------------------------------------------------------------------------
def run_system(label, D):
    print("="*74)
    print("UNIT SYSTEM:", label)
    print("="*74)
    F = forms(D)
    allpass = True
    for name, dim in F.items():
        ok, resid = report(name, dim)
        tag = "PASS (kg)" if ok else "FAIL  residual=" + str(sp.simplify(dim - M))
        if not ok:
            allpass = False
        print(f"  {name:34s} : {tag}")
    # form 4
    same, finv, needL = form4_diagnose(D)
    print("  L4  m = 2L/(Ef^2 - c^2 B^2)        :")
    print(f"        Ef^2 vs (cB)^2 subtractable? {'YES (same dim)' if same==0 else 'NO diff='+str(same)}")
    print(f"        field-invariant net dim (Ef^2)   = {sp.simplify(finv)}")
    print(f"        'L' numerator must have dim       = {sp.simplify(needL)}")
    print(f"        (plain angular momentum L = M+2L-T = {sp.simplify(M+2*L-T)}) -> "
          f"{'MATCH' if sp.simplify(needL-(M+2*L-T))==0 else 'NO MATCH -> needs hidden const (eps0,V) => PROPORTIONALITY'}")
    print()
    return allpass

passA = run_system("(A) SI-STRICT  [rad dimensionless, charge=Coulomb=I*T]", SI)
passB = run_system("(B) QWM  [rad=base dim A, charge e=kg*rad/s=M*A/T]", QWM)

# ===========================================================================
# QWM UNITS-TABLE INTERNAL CONSISTENCY (D2): A.B = helicity density = m/rad^2
# ===========================================================================
print("="*74)
print("QWM UNITS-TABLE INTERNAL CONSISTENCY CHECK (D2/D3)")
print("="*74)
AB = QWM['Avec'] + QWM['B']            # A.B
heldens_expected = L - 2*A            # m/rad^2
print(f"  A.B net dim              = {sp.simplify(AB)}   (expected m/rad^2 = {heldens_expected})",
      "-> PASS" if sp.simplify(AB - heldens_expected)==0 else "-> FAIL")
rho = M - 3*L                          # kg/m^3
print(f"  matter density rho       = {rho}  (kg/m^3)")
print(f"  rho - (A.B)              = {sp.simplify(rho - AB)}  (nonzero => rho = kappa*(A.B), "
      "kappa carries dim) [D2 proportionality]")
# winding number n = (1/2pi) oint grad(phase).dr
gradphase = A - L                      # rad/m
winding = gradphase + L                # * dr (L) ; /2pi (rad=A) -> subtract A
winding_SI = (0 - L) + L               # SI: phase dimensionless
print(f"  winding n (QWM) grad(phase).dr = {sp.simplify(gradphase + L)}  (=N*rad = A, before /2pi)")
print(f"  winding n (SI)  = {sp.simplify(winding_SI)}  (dimensionless) [matches std mode number]")
wind_dens = -3*L                       # m^-3
print(f"  winding density {wind_dens} (m^-3) vs rho {rho} (kg/m^3): different -> D3 proportionality")
print()

# ===========================================================================
# NUMERIC ANCHORS (CODATA-2018) -- the [V] arithmetic
# ===========================================================================
print("="*74)
print("NUMERIC ANCHORS (CODATA-2018)")
print("="*74)
hbar = 1.054571817e-34      # J s
cc   = 299792458.0          # m/s
me   = 9.1093837015e-31     # kg
mp   = 1.67262192369e-27    # kg
e_C  = 1.602176634e-19      # C
alpha= 7.2973525693e-3      # fine structure
eV   = 1.602176634e-19      # J

omega_C = me*cc**2/hbar
m_from_whirl = hbar*omega_C/cc**2
e_qwm = me*omega_C          # kg*rad/s  (Reed Eq 21-6)
omega_p = e_C/me            # rad/s (Reed Eq 21-10 : e/m_e)
q_whirl = 1.0/alpha
dtheta  = 2*np.pi*alpha
print(f"  omega_C = m_e c^2/hbar          = {omega_C:.4e} rad/s   (Reed 7.7634e20)")
print(f"  m = hbar*omega_C/c^2            = {m_from_whirl:.6e} kg   (m_e ratio {m_from_whirl/me:.6f})")
print(f"  hbar*omega_C                    = {hbar*omega_C/eV/1e6:.5f} MeV  (=m_e c^2, 0.5110)")
print(f"  e = m_e*omega_C (QWM units)     = {e_qwm:.4e} kg*rad/s   (Reed 7.0719e-10)")
print(f"  omega_p = e/m_e                 = {omega_p:.4e} rad/s   (Reed 1.7588e11)")
print(f"  hbar*omega_p                    = {hbar*omega_p/eV:.3e} eV  (sub-meV precession quantum)")
print(f"  q = 1/alpha (whirl number)      = {q_whirl:.5f}   (dimensionless) [D1]")
print(f"  dtheta = 2*pi*alpha             = {dtheta:.6f} rad = {np.degrees(dtheta):.3f} deg (Reed 21-2)")
# m = e/omega with QWM charge -> returns m_e
m_from_eoveromega = e_qwm/omega_C
print(f"  m = e/omega_C (QWM, e in kg*rad/s) = {m_from_eoveromega:.6e} kg  (m_e ratio {m_from_eoveromega/me:.6f})")
print()

# ===========================================================================
# COINCIDENCE GATE (0.5%) : m_p/m_e vs phi^n and 137^n ; and whirl ratios
# ===========================================================================
print("="*74)
print("COINCIDENCE GATE (0.5%) -- ordering vs law")
print("="*74)
phi = (1+np.sqrt(5))/2
def gate(ratio, name):
    hits = []
    for base,bn in ((phi,'phi'),(1/alpha,'137')):
        n = np.log(ratio)/np.log(base)
        nearest = round(n)
        if nearest != 0:
            val = base**nearest
            dev = abs(val-ratio)/ratio
            hits.append(f"{bn}^{nearest}={val:.4g} dev={dev*100:.2f}%" + (" <=PASS" if dev<0.005 else ""))
    print(f"  {name} = {ratio:.6g}: " + " | ".join(hits))
gate(mp/me, "m_p/m_e")
gate(omega_C/(0.05*eV/cc**2/hbar*cc**2/hbar) if False else (mp*cc**2/hbar)/(me*cc**2/hbar), "omega_p/omega_e")
# 1/(20 phi^4) numerology (flagged)
val = 1/(20*phi**4)
print(f"  1/(20*phi^4) = {1/val:.3f}  vs 1/alpha = {1/alpha:.3f}  dev={abs(1/val-1/alpha)/(1/alpha)*100:.3f}% [FLAGGED numerology, not promoted]")
print()

print("="*74)
print("SUMMARY")
print("="*74)
print(f"  SI-strict: all standard forms PASS = {passA}")
print(f"  QWM      : all forms PASS          = {passB}")
print("  KEY CATCHES:")
print("   - L1/L2 as transcribed (E/(Ef/B), no square) => MOMENTUM not mass (FAIL).")
print("     Primary Ch.21 Table 21-1 has the SQUARE: m=E/(Ef/B)^2 => PASS. Transcription dropped it.")
print("   - m=e/omega PASSES only with QWM charge e=[kg*rad/s]; in SI (Coulomb) it FAILS (gives I*T^2).")
print("     -> this is exactly why D4 (charge=spin ang.mom.) is needed for m=e/omega to be dimensional.")
print("   - L4 m=2L/(Ef^2-c^2B^2): 'L' is NOT plain angular momentum; needs hidden eps0/V =>")
print("     survives only as a PROPORTIONALITY (energy-density/c^2), consistent with D2.")
print("   - m_p/m_e=1836.15: no phi^n/137^n within 0.5% => ordering, NOT a promoted law.")
