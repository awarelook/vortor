"""
TUFT (Nielsen) mass-tower COEFFICIENT check -- verifies the closed-form zeta-coefficients that the
mass-tower is built from, exposes the documented pi-power internal inconsistency, and confirms the
knot/lens-space normalization -- WITHOUT claiming the fitted mass values (Lambda_5, a_5, the blinded
0.1-sigma fits are the preprint's [framework], not reproduced here).

Discipline: [V] here = a closed-form coefficient reproduced from its definition; [framework]/[flag] =
the tower's fit constants and the pi-power anomaly, carried honestly, not promoted.
"""
import numpy as np
from mpmath import zeta, mp
mp.dps = 30

z3 = float(zeta(3))     # 1.2020569...
z5 = float(zeta(5))     # 1.0369278...
pi = np.pi

print("="*74)
print("1) ZETA-COEFFICIENTS of the TUFT mass-tower  [V] (closed form vs reported)")
print("="*74)
coeffs = {
 "C5 = zeta(3)/12"          : (z3/12,            0.100171,   "quark n^2 term (pi-FREE)"),
 "beta5 = zeta(5)/(8 pi^4)" : (z5/(8*pi**4),     1.33064e-3, "quark n(n+1)/2 term"),
 "sigma5 = zeta(3)/(16 pi^2)":(z3/(16*pi**2),    7.61211e-3, "quark log-tau term"),
 "omega3 = zeta(3)/(4 pi^2)": (z3/(4*pi**2),     None,       "lepton n^2 term (universal S3 Ray-Singer)"),
 "sigma9 = zeta(3)/(8 pi^2)": (z3/(8*pi**2),     None,       "neutrino log-tau term"),
 "C9 = -zeta(3)/8 (1+zeta(3)/28)": (-z3/8*(1+z3/28), -0.15670774, "neutrino n^2 term (S9 lens det + SO(8))"),
}
for name,(val,rep,note) in coeffs.items():
    tag = "" if rep is None else ("  match=%.1e" % (abs(val-rep)/abs(rep)))
    print(f"  {name:34s} = {val:+.8e}{tag}   [{note}]")

print()
print("="*74)
print("2) THE pi-POWER INTERNAL INCONSISTENCY  [flag] (documented anomaly, carried not hidden)")
print("="*74)
print("  If all n^2 coefficients came from one Ray-Singer normalization zeta_B'(0)=zeta(3)/(4 pi^2),")
print("  every one should carry pi^2. But:")
print(f"     C5    = zeta(3)/12        = {z3/12:.6f}   -> pi-FREE  (1/12, no pi^2)")
print(f"     omega3= zeta(3)/(4 pi^2)  = {z3/(4*pi**2):.6f}   -> carries 1/pi^2")
print(f"     ratio C5 / omega3 = {(z3/12)/(z3/(4*pi**2)):.6f}  = pi^2/3 = {pi**2/3:.6f}")
print("  So C5 and omega3 differ by exactly pi^2/3 -- they cannot both be 'the' n^2 normalization.")
print("  This is the unresolved pi-power anomaly: fold the STRUCTURE, flag the coefficient origin.")

print()
print("="*74)
print("3) KNOT / LENS-SPACE NORMALIZATION  [V]/[credited]")
print("="*74)
# Reidemeister/lens torsion tau_R(L(n,1)) = 1 / prod_{j=1}^{n-1} |1 - e^{2 pi i j / n}| = 1/n
for n in (2,3,4,5,6):
    prod = np.prod([abs(1-np.exp(2j*np.pi*j/n)) for j in range(1,n)])
    print(f"  n={n}: prod_j |1-e^(2pi i j/n)| = {prod:.6f}  (= n)   ->  tau_R(L(n,1)) = 1/n = {1/n:.4f}   [V]")
print("  Alexander knot values: tau(unknot)=1, tau(Hopf)=4, tau(trefoil)=|Delta(-1)|=3  [credited]")
print("  N5 = 8 pi^3 = %.4f ,  N9 = 32 pi^5 = %.4f   [framework: TUFT normalization]" % (8*pi**3, 32*pi**5))

print()
print("="*74)
print("4) WHAT IS NOT REPRODUCED HERE (honest)")
print("="*74)
print("  Lambda_5=(2pi/sqrt3) v kappa_5^3, a_5~3.564112 (= exp(spectral_5/6) sqrt3 (2+omega3)), and the")
print("  full quark/lepton/neutrino mass VALUES depend on fit inputs (v, kappa, spectral_5) and are the")
print("  PREPRINT's blinded-fit result (Round-2 review) -- [framework: Nielsen TUFT], NOT [V] here.")
print("  The Proca-Beltrami seed lambda = m c / hbar (from curl B = lambda B -> Helmholtz vs Proca) is")
print("  [credited] structure; the identification of the mass operator with *d on coexact 1-forms is TUFT.")
print()
print("done.")
