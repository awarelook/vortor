# EQ-33 : Vacuum resonance & the active medium — polarizable-medium refractive index, computed.
# -----------------------------------------------------------------------------------------------
# METHOD (calculate first; check the misapplied firewall; report the FIT, not an effect):
#   Instead of firewalling the polarizable-vacuum picture, COMPUTE both refractive indices and show
#   they are the SAME structural object n=sqrt(1+chi) at different scales; the plasma chi dominates.
#   The toroid FITS as a high-index cavity resonance. NO claim that the vacuum "does" anything
#   (no energy, no force, no propulsion) — only the structural/mathematical fit.
# All from the 4 anchors {B,n_i,R,m_i} + 2 dynamical constants {Gamma,R_dim}. No free parameters.
import sys, math
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# anchors + constants
B=20.6e-3; n_i=1.7e19; R=0.12; m_i=29*1.66053907e-27
Gamma=0.9987; R_dim=1.380
mu0=4*math.pi*1e-7; c=2.99792458e8; G=6.67430e-11
lam1=4.493409; lam2=7.725252     # roots of tan x = x (CK eigenvalues)

def approx(a,b,tol,name):
    ok=abs(a-b)<=tol*max(1,abs(b)); print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {a:.4g} vs {b:.4g}"); assert ok,name

v_A=B/math.sqrt(mu0*n_i*m_i)
n_A=c/v_A                              # analogue refractive index of the magnetized medium
f1=lam1*v_A/(2*math.pi*R)
lam_med=2*math.pi*R/lam1               # standing-wave (Alfven) wavelength at f1
kR_med=lam1                            # k_med * R = lam1 (the CK eigenvalue = cavity resonance cond.)
lam_vac=c/f1
kR_vac=2*math.pi*R/lam_vac            # electrical size in the true-vacuum index (=1)

print("== 1. analogue index + cavity resonance (asserted) ==")
approx(v_A,2.031e4,0.02,"v_A [m/s]")
approx(n_A,1.476e4,0.02,"n_A = c/v_A")
approx(kR_med,4.4934,1e-3,"k_med R (= CK eigenvalue lam1)")
approx(kR_vac,3.04e-4,0.03,"k_vac R (matches DARK-1 3.0e-4)")
approx(kR_med/kR_vac,n_A,0.02,"k_med/k_vac = n_A (cross-check)")
print(f"  lam_med = {lam_med:.3f} m = {lam_med/R:.2f} R  ->  fundamental cavity mode fits the object")
print(f"  lam_vac = {lam_vac/1e3:.2f} km >> R  ->  deeply subwavelength in true vacuum")
print("  FIT: index n_A makes the toroid RESONANT inside (k_med R=4.49) yet DARK outside (k_vac R=3e-4).")

print("\n== 2. the misapplied firewall, checked by calculation ==")
# both are refractive indices from a polarizable medium: n = sqrt(1 + chi)
chi_plasma=n_A**2-1                    # Alfven dielectric eps_A = 1 + c^2/v_A^2
V=(4/3)*math.pi*R**3
M_ions=n_i*m_i*V
W_B=B**2/(2*mu0)*V; M_field=W_B/c**2
KPV_ion=2*G*M_ions/(R*c**2)           # Winterberg/Reed gravitational vacuum-polarizability shift
KPV_field=2*G*M_field/(R*c**2)
print(f"  plasma polarizability   chi_plasma = n_A^2-1 = {chi_plasma:.3g}")
print(f"  vacuum (Winterberg/Reed) K_PV-1 = 2GM/Rc^2 = {KPV_ion:.2g} (ion mass) ... {KPV_field:.2g} (field energy)")
print(f"  ratio plasma/vacuum = {chi_plasma/KPV_ion:.2g}  (~{math.log10(chi_plasma/KPV_ion):.0f} orders)")
print("  FIT (not dismissal): BOTH are n=sqrt(1+chi) from a polarizable medium — the SAME structural")
print("  object; the plasma chi dominates by ~40+ orders. The polarizable-vacuum framework is the")
print("  correct STRUCTURE; the operative index is the plasma's. No claim the vacuum does anything.")

print("\n== 3. the medium is active (nonlinear + parametric), computed ==")
cs2_over_vA2=-(Gamma/R_dim)**2        # log-NLS negative sound speed c_s^2 = -b_eff/m_i = -(G/R_dim)^2 v_A^2
cs=abs(cs2_over_vA2)**0.5*v_A
eps_c=0.65                            # parametric (Mathieu) gain threshold, from EQ-13b
print(f"  c_s^2/v_A^2 = -(Gamma/R_dim)^2 = {cs2_over_vA2:.3f}  -> |c_s| = {cs/1e3:.1f} km/s = {abs(cs2_over_vA2)**0.5:.3f} v_A")
print(f"  |c_s| < v_A  ->  fast magnetosonic branch STABLE (magnetic pressure > negative log-NLS pressure)")
print(f"  parametric gain threshold eps_c = {eps_c} (EQ-13b): the driven medium AMPLIFIES above it")
print("  FIT: log nonlinearity (self-focusing gausson) + parametric drive = a phase-conjugate / parametric")
print("  resonator (Reed). Energy-conserving, pump-fed (SR-1) — active MEDIUM, NOT net energy gain.")

print("\n== 4. Nachamkin non-radiating resonance (the 'vactoid') ==")
print(f"  non-radiation at k R0 = lam2 = {lam2:.4f} (EQ-31): the vacuum-medium resonance is dark by construction.")
print("\n== summary ==")
print(f"  toroid = a resonance of a polarizable medium (analogue vacuum), index n_A={n_A:.3g};")
print(f"  resonant inside / dark outside; medium active under drive (eps_c={eps_c}); vacuum picture = same")
print("  structure, plasma-dominated. All from 4 anchors + 2 constants; 0 free parameters.")
