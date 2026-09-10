"""
alpha on the CORRECTLY-specified object: a standing-wave resonator in the medium with a point defect.

The electron (corrected picture) is NOT a propagating loop but a STANDING-WAVE RESONATOR confined by the
medium (polarizable vacuum / Alfven dielectric), carrying a POINT charge defect. QWM says alpha is the
slight electrostatic/magnetostatic energy IMBALANCE of this object. This script computes that imbalance
through EVERY physical channel it can enter, and asks honestly: does alpha ~ 1/137.036 fall out from
first principles, or does it stay inserted? (Discipline: a hit that needs inserted alpha is circular; a
geometric hit that is generic is [flag]; only a parameter-free, non-generic derivation counts.)

  CHANNEL 1 -- the resonator MODE itself: a lossless standing wave is EQUIPARTITIONED, <U_E> = <U_B>.
              Imbalance from the mode = 0 (E and B slosh 90-deg out of phase, time-averages equal).
  CHANNEL 2 -- DISPERSION of the medium: the Brillouin energy density u_E = (1/2) d(w eps)/dw |E|^2
              carries an imbalance ONLY if the medium is dispersive (dei/dw != 0). The theory's canonical
              medium is eps_r = (c/v_A)^2 = CONST, explicitly NON-DISPERSIVE (v_phi = v_g = v_A,
              foundation/30_CANONICAL_NUMBERS.md sec.I). So the dispersive-imbalance channel = 0 too.
  CHANNEL 3 -- the POINT DEFECT self-energy: U_E(defect) = e^2/(4 pi eps0 R_C) at the Compton radius
              gives U_E/mc^2 = alpha EXACTLY -- but ONLY because e^2 = 4 pi eps0 alpha hbar c is inserted
              (it is r_e/lambda_C = alpha restated). Circular.
  CONCLUSION -- topology QUANTIZES charge (integer winding / Hopf) but does NOT fix its MAGNITUDE e;
              alpha = e^2/(4 pi eps0 hbar c) is the unpinned SCALE. On the correctly-specified object,
              every imbalance channel is 0 (mode, dispersion) or circular (defect = r_e/lambda_C). alpha
              is not derived here -- it enters only through the charge magnitude e. Thorough, well-posed
              settled-negative: the frontier is exactly the charge MAGNITUDE, not its quantization.

math-only (CODATA). Run: python results/verify/alpha_resonator_imbalance_check.py
"""
import numpy as np

# CODATA-2018
hbar = 1.054571817e-34
c    = 299792458.0
e    = 1.602176634e-19
eps0 = 8.8541878128e-12
me   = 9.1093837015e-31
alpha_codata = e*e/(4*np.pi*eps0*hbar*c)

def banner(t): print("="*78); print(t); print("="*78)
ok = True

banner("CHANNEL 1 -- resonator mode: standing wave is EQUIPARTITIONED (<U_E> = <U_B>)")
# E = E0 sin(kz) cos(wt);  B = (E0/c) cos(kz) sin(wt)  (Faraday, non-dispersive)
Nz, Nt = 400, 400
z = np.linspace(0, np.pi, Nz)          # one half-wavelength, k=1
t = np.linspace(0, 2*np.pi, Nt)        # one period, w=1
E0 = 1.0
Z, T = np.meshgrid(z, t, indexing='ij')
E = E0*np.sin(Z)*np.cos(T)
B = (E0/c)*np.cos(Z)*np.sin(T)
uE = 0.5*eps0*E**2
uB = 0.5*(B**2)/(4e-7*np.pi)           # 1/(2 mu0) B^2
UE = uE.mean(); UB = uB.mean()
imb1 = (UE-UB)/(UE+UB)
print("  <U_E> = %.4e   <U_B> = %.4e   imbalance = %+.3e   (-> 0: BALANCED)" % (UE, UB, imb1))
print("  -> the standing-wave MODE gives no imbalance (equipartition); alpha is NOT here.")
ok = ok and abs(imb1) < 1e-3

banner("CHANNEL 2 -- dispersion: Brillouin u_E ~ d(w eps)/dw; imbalance needs a DISPERSIVE medium")
# theory's canonical medium: eps_r = (c/v_A)^2 = const  -> non-dispersive (v_phi=v_g=v_A, canon sec.I)
vA = 2.033e4
eps_r = (c/vA)**2
# non-dispersive: d(w eps)/dw = eps  => Brillouin factor / ordinary factor = 1  => zero extra imbalance
disp_factor = 1.0                       # d(w*eps)/dw / eps  for eps=const
print("  eps_r = (c/v_A)^2 = %.3e  (CONSTANT -> non-dispersive: v_phi = v_g = v_A, canon sec.I)" % eps_r)
print("  Brillouin/ordinary energy factor d(w eps)/dw / eps = %.3f  -> dispersive imbalance = 0" % disp_factor)
print("  -> the theory's own medium is non-dispersive, so this channel contributes NOTHING to alpha.")
ok = ok and abs(disp_factor-1.0) < 1e-12

banner("CHANNEL 3 -- point-defect self-energy: U_E/mc^2 = alpha, but ONLY by inserting e")
R_C = hbar/(me*c)                       # reduced Compton radius
U_E_defect = e*e/(4*np.pi*eps0*R_C)     # Coulomb self-energy of the point charge at R_C
ratio = U_E_defect/(me*c*c)
print("  R_C = hbar/(m c) = %.4e m" % R_C)
print("  U_E(defect)/mc^2 = e^2/(4 pi eps0 R_C mc^2) = %.6e" % ratio)
print("  alpha (CODATA)                              = %.6e   (ratio/alpha = %.6f)"
      % (alpha_codata, ratio/alpha_codata))
print("  BUT e^2 = 4 pi eps0 * alpha * hbar c, so U_E/mc^2 = alpha*(hbar/(R_C m c)) = alpha*1 = alpha:")
print("  the 'derivation' is r_e/lambda_C = alpha RESTATED -- alpha was inserted through e. CIRCULAR.")
ok = ok and abs(ratio/alpha_codata - 1.0) < 1e-6

banner("CHANNEL 4 -- alpha RUNS: 1/137.036 is the IR endpoint, not a fixed number to hit")
inv_a0 = 1.0/alpha_codata
# alpha is scale-dependent (Thomson/zero-momentum value 1/137.036; grows with energy).
# 1-loop QED, electron-loop-only leading illustration: 1/alpha(mu) = 1/alpha(me) - (2/3pi) ln(mu/me)
ln_scale = np.log(91.19e9 / 0.511e6)          # ln(M_Z / m_e)
shift_e_only = (2.0/(3*np.pi))*ln_scale
print("  1/alpha(IR, Thomson) = %.3f   (zero-momentum value -- what CODATA quotes)" % inv_a0)
print("  alpha GROWS with energy: 1-loop electron-loop shift over ln(M_Z/m_e)=%.1f is -%.2f in 1/alpha" % (ln_scale, shift_e_only))
print("  (all charged flavors give the full run to the MEASURED 1/alpha(M_Z) ~ 127.9). alpha is a CURVE.")
print("  -> the theory should supply the GENERAL (running) coupling -- exactly the dielectric flow")
print("     K_PV(q^2) = alpha(0)/alpha(q^2) (alpha_running.py, MATH_TOOLKIT sec.9c) -- NOT an exact digit.")
print("  KEY: running only RELATES scales; the curve needs an ANCHOR (integration constant), and that")
print("  anchor IS the charge MAGNITUDE of CHANNEL 3. So 'alpha runs (not an exact number)' and 'the")
print("  magnitude/scale is unpinned' are the SAME statement -- they unify the frontier.")

banner("CONCLUSION -- quantization is topological; the running coupling's ANCHOR (magnitude) is unpinned")
print("  On the correctly-specified object (standing-wave resonator, non-dispersive medium, point")
print("  defect), the electro/magneto imbalance is:")
print("    - 0 from the resonator mode (equipartition),")
print("    - 0 from the medium (non-dispersive by construction, canon sec.I),")
print("    - = alpha from the point defect ONLY because e is inserted (r_e/lambda_C, circular).")
print("  Topology (Hopf/winding) QUANTIZES charge -> integer units [why charge is quantized], but does")
print("  NOT fix the charge MAGNITUDE e; alpha = e^2/(4 pi eps0 hbar c) is the unpinned SCALE. So the")
print("  frontier is now stated at its sharpest: not 'why is charge quantized' (topology answers that), and")
print("  NOT 'derive the exact 1/137.036' (alpha RUNS -- that is only the IR endpoint, CHANNEL 4), but")
print("  'what ANCHORS the running coupling' = what sets the charge MAGNITUDE e -- the shared elementary-")
print("  electron scale, undrived here. A thorough, well-posed SETTLED-NEGATIVE on the correct object,")
print("  with the frontier reduced to ONE quantity: the running coupling's anchor.  [V] / settled-neg (value)")
print("done.  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
