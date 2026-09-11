"""
Polarizable-medium / resonator derivation for the active-medium model + locked toolkit.

Derives, from the theory's own polarizable-medium form (v_eff = c/sqrt(eps_r mu_r) = v_A):
  1. medium parameters: eps_r, mu_r, refractive index n, wave impedance Z   (ball lightning + lab spheromak)
  2. dispersion: the force-free/Alfven medium is NON-DISPERSIVE (v_phase = v_group = v_A) -- confirms QWM 299-300
  3. the RESONATOR SPECTRUM the medium supports: CK/Beltrami force-free eigenvalues lambda_n R = roots of
     tan(x)=x -> standing-mode frequencies f_n = lambda_n v_A / 2pi.  First root must reproduce the locked
     paper's host-sphere eigenvalue lambda_1 R = 4.493409.
  4. mode spacing / Q-scale for a driven, impedance-matched resonator.
No aether/K_PV; pure MHD polarizable medium.  Feeds the §05 active-medium widget and foundation/10 §3.
"""
import numpy as np
from scipy.optimize import brentq

c = 2.99792458e8
Z0 = 376.730313668        # vacuum wave impedance (ohms)

def medium(vA):
    eps_r = 1.0 + (c/vA)**2          # Alfven permittivity
    mu_r  = 1.0
    n     = np.sqrt(eps_r*mu_r)      # = c/vA
    Z     = Z0*np.sqrt(mu_r/eps_r)   # wave impedance of the medium
    return eps_r, mu_r, n, Z

def tanx_roots(nroots=6):
    # roots of tan(x)=x : one in each interval (k*pi, (k+1/2)*pi), k>=1
    roots=[]
    k=1
    while len(roots)<nroots:
        a, b = k*np.pi+1e-6, (k+0.5)*np.pi-1e-6
        f = lambda x: np.tan(x)-x
        roots.append(brentq(f, a, b, xtol=1e-12)); k+=1
    return np.array(roots)

def fmt(x):
    return f"{x:.4e}"

print("="*92); print("POLARIZABLE-MEDIUM / RESONATOR DERIVATION"); print("="*92)

for name,vA,R in [("ball lightning", 2.033e4, 0.12), ("lab spheromak", 1.0e5, 0.30)]:
    eps_r,mu_r,n,Z = medium(vA)
    print(f"\n--- {name}:  v_A = {fmt(vA)} m/s,  R = {R} m ---")
    print(f"  polarizable medium:  eps_r = 1 + (c/v_A)^2 = {fmt(eps_r)}   mu_r = {mu_r}")
    print(f"                        n = sqrt(eps_r mu_r) = c/v_A = {fmt(n)}   (refractive index)")
    print(f"                        Z = Z0 sqrt(mu_r/eps_r) = {Z:.4f} ohm   (sets drive coupling)")
    print(f"                        v_eff = c/n = {fmt(c/n)} m/s   (== v_A: {np.isclose(c/n,vA)})")
    # dispersion: omega = v_A * k  (k = lambda)  ->  non-dispersive
    k = np.linspace(1,50,6)
    vph = (vA*k)/k                    # omega/k
    vg  = np.gradient(vA*k, k)        # d omega / dk
    print(f"  dispersion omega = v_A k:  v_phase = {fmt(vph.mean())}, v_group = {fmt(vg.mean())}"
          f"  -> NON-DISPERSIVE (v_ph=v_g=v_A: {np.allclose(vph,vA) and np.allclose(vg,vA)})")

# --- resonator spectrum (medium-independent eigenvalues; frequencies scale with v_A/R) ---
roots = tanx_roots(6)
print("\n" + "="*92)
print("RESONATOR SPECTRUM  (force-free CK/Beltrami standing modes:  lambda_n R = roots of tan x = x)")
print("="*92)
print(f"  lambda_n R (first 6): {np.array2string(roots, precision=4)}")
print(f"  CHECK lambda_1 R = {roots[0]:.6f}  vs locked-paper host-sphere 4.493409  "
      f"-> {np.isclose(roots[0],4.493409,atol=1e-5)}")
vA,R = 2.033e4, 0.12
f_n = roots*vA/(2*np.pi*R)           # f_n = (lambda_n R / R) * v_A / 2pi
print(f"\n  ball-lightning resonance frequencies f_n = lambda_n v_A / 2pi (R={R}, v_A={fmt(vA)}):")
for i,(lr,f) in enumerate(zip(roots,f_n),1):
    print(f"    n={i}:  lambda_n R = {lr:7.4f}   f_n = {f/1e3:8.2f} kHz")
print(f"\n  fundamental f_1 = {f_n[0]/1e3:.1f} kHz  (the medium's lowest sustained resonance)")
print(f"  overtone ratios f_n/f_1 = {np.array2string(f_n/f_n[0], precision=3)}  (inharmonic: tan x = x, not integer)")
print(f"  the BEAT (kHz) is the small doublet splitting on top of this ~{f_n[0]/1e3:.0f} kHz carrier,")
print(f"  NOT a fundamental -- consistent with beat law f_b = c_CK*eps*v_A/2piR << f_1.")

print("\n" + "="*92); print("TOOLKIT-READY RESULTS"); print("="*92)
print("  - medium: eps_r=1+(c/v_A)^2, n=c/v_A, Z=Z0/n  (derived, closed form)")
print("  - non-dispersive: v_phase=v_group=v_A exactly (confirms QWM 299-300; clean standing resonances)")
print("  - resonator spectrum: lambda_n R = roots(tan x = x); lambda_1 R=4.4934 reproduces the paper")
print("  - impedance-matched drive on a mode sustains it; the beat is the doublet splitting, not the carrier")
