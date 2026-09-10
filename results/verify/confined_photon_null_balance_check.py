"""
The confined photon (Hopf-Ranada EM knot) is a NULL field: exactly energy-balanced.
-> the "electrostatic/magnetostatic imbalance = alpha" route is computed-DEAD on the free photon.

QWM/FTGB picture (corrected framing): the electron is NOT a propagating loop -- it is a STANDING-WAVE
RESONATOR confined by the medium (the polarizable vacuum / Alfven-dielectric, v_eff = c/sqrt(eps_r mu_r)
= v_A), carrying a POINT charge defect (a localized torsion / "spark imbalance" point). Its charge and
alpha are said to arise from a slight ELECTROSTATIC vs MAGNETOSTATIC energy IMBALANCE, "unlike a
freely-propagating photon." This script checks the FREE-PHOTON end of that statement -- i.e. what the
electron is NOT -- on the canonical propagating object: the Hopf-Ranada electromagnetic knot (Bateman
construction, an exact null vacuum Maxwell solution, the literal "light chasing its own tail"). It
establishes the baseline the resonator must depart from.

Bateman (t=0):   F = E + iB = grad(alpha) x grad(beta),   c = 1,
   alpha = (r^2 - 1 + 2 i z)/(r^2 + 1),     beta = 2 (x - i y)/(r^2 + 1).

CLAIM (verified here): the field is NULL (E.B = 0, |E| = |B|), so the electric and magnetic energy
densities are equal POINTWISE, U_E/U_B = 1 exactly -- ZERO imbalance. Therefore the free confined
photon carries NO alpha-sized imbalance: any such imbalance must come entirely from the part that
BREAKS the null condition (the massive/bound, charge-carrying deviation). This closes the
"self-energy imbalance = alpha" route the same way ck_winding_ratio_check closed the winding route:
computed-dead, not asserted. It does NOT derive alpha; it pins down that the null photon cannot be
its source, and localizes the physics to the null-violating (charge) term.

math-only, spectral/FD. Run: python results/verify/confined_photon_null_balance_check.py
"""
import numpy as np

N = 64
Lbox = 4.0
x1 = np.linspace(-Lbox, Lbox, N)
dx = x1[1] - x1[0]
X, Y, Z = np.meshgrid(x1, x1, x1, indexing='ij')
r2 = X*X + Y*Y + Z*Z
D = r2 + 1.0

# complex Euler potentials (Bateman, t=0)
alpha = (r2 - 1.0 + 2j*Z) / D
beta = 2.0*(X - 1j*Y) / D


def grad(f):
    gx, gy, gz = np.gradient(f, dx, dx, dx, edge_order=2)
    return np.array([gx, gy, gz])


def cross(a, b):
    return np.array([a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]])


ga = grad(alpha)
gb = grad(beta)
F = cross(ga, gb)                     # Riemann-Silberstein F = E + iB  (c=1)
E = F.real
B = F.imag

# mask a margin to avoid the FD edge and keep the field's compact core
m = (np.abs(X) < 0.75*Lbox) & (np.abs(Y) < 0.75*Lbox) & (np.abs(Z) < 0.75*Lbox)

uE = np.sum(E*E, axis=0)               # electric energy density (c=1, eps0=1)
uB = np.sum(B*B, axis=0)               # magnetic energy density
U_E = uE[m].sum() * dx**3
U_B = uB[m].sum() * dx**3
imbalance = (U_E - U_B) / (U_E + U_B)

# nullness pointwise:  E.B = 0  and  |E| = |B|
EdotB = np.sum(E*B, axis=0)
Emag = np.sqrt(uE); Bmag = np.sqrt(uB)
core = m & (Emag > 0.05*Emag[m].max())      # where the field is non-negligible
cos_EB = np.abs(EdotB[core]) / (Emag[core]*Bmag[core])
null_mag = np.abs(Emag[core]-Bmag[core]) / (0.5*(Emag[core]+Bmag[core]))

print("="*78)
print("The Hopf-Ranada EM knot (confined photon 'chasing its tail'): NULL & energy-balanced")
print("="*78)
print("  total electric energy U_E = %.6e" % U_E)
print("  total magnetic energy U_B = %.6e" % U_B)
print("  U_E / U_B                 = %.6f" % (U_E/U_B))
print("  imbalance (U_E-U_B)/(U_E+U_B) = %+.4e   (-> 0: BALANCED)" % imbalance)
print("  pointwise nullness (field core):")
print("     mean |E.B|/(|E||B|)      = %.3e   (-> 0: E perp B)" % cos_EB.mean())
print("     mean ||E|-|B||/avg       = %.3e   (-> 0: |E| = |B|)" % null_mag.mean())
print("-"*78)
print("  READING: the FREE (propagating) photon is a NULL field -> U_E = U_B EXACTLY (zero electro/magneto")
print("  imbalance). So the 'imbalance = alpha' mechanism cannot draw alpha from a free photon. Per the")
print("  corrected model the electron is NOT this propagating knot but a STANDING-WAVE RESONATOR confined")
print("  by the medium with a POINT charge defect -- exactly the null-VIOLATING structure. 100%% of any")
print("  alpha-sized imbalance therefore lives in that resonator/medium/point-defect deviation from null,")
print("  NOT in the photon. This is a COMPUTED baseline (parallel to the winding route in")
print("  ck_winding_ratio_check): it localizes where charge/alpha must come from (the confined resonator's")
print("  departure from null), but does NOT derive the value 1/137 -- that requires computing the standing-")
print("  wave-in-medium imbalance from first principles (the open target), and stays inserted until then.")
print("  [V] (free-photon null balance = the baseline) / settled-negative (alpha value)")

# accept generous FD tolerances (numerical-gradient floor ~1e-2 at N=64)
ok = (abs(imbalance) < 0.02) and (cos_EB.mean() < 0.05) and (null_mag.mean() < 0.05)
print("done.  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
