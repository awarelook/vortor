# Tension-resolution phase (2026-08-27): compute the honest numbers for T1 (beat convention/carrier)
# and T2 (b_eff square-law blast radius), from canonical inputs. No fabrication; report the band + the rigorous value.
import numpy as np

print("="*74)
print("T1  BEAT RATIO f_b/f_c  = (doublet splitting Delta-lambda) / (carrier lambda)")
print("="*74)
lam1R   = 4.4934          # sphere ground eigenvalue (CK, root of tan x = x)
eps     = 1/((1+5**0.5)/2)# 1/phi
dl_2D   = 0.138           # 2D Grad-Shafranov-reduced FEM doublet split (lam0=4.000, lam1=4.138)
dl_3D   = 0.2806          # RIGOROUS 3D vector H(curl) FEM (stage3_torus_doublet.edp), held across refinement
carr_sphere  = lam1R      # carrier = sphere ground 4.4934 (the locked convention)
carr_2Ddoub  = (4.000+4.138)/2   # carrier = 2D doublet mean 4.069
# For 3D we only have the split; use both the sphere ground and an estimated doublet mean near the same fractional offset
print(f"  inputs: lam1R={lam1R}, eps=1/phi={eps:.5f}, Delta-lambda 2D={dl_2D}, 3D(rigorous)={dl_3D}")
print(f"  ratio 3D/2D of the split = {dl_3D/dl_2D:.2f}x  (canonical quotes ~1.78-2.0x)")
print()
print("  f_b/f_c under each (model, carrier) choice:")
for name, dl in [("2D-reduced", dl_2D), ("3D H(curl) RIGOROUS", dl_3D)]:
    for cname, c in [("/sphere 4.4934", carr_sphere), ("/2D-doublet 4.069", carr_2Ddoub)]:
        print(f"    {name:22s} {cname:20s}: {100*dl/c:5.2f} %")
print()
band = sorted([100*dl_2D/carr_sphere, 100*dl_3D/carr_2Ddoub])
print(f"  => HONEST BAND: {band[0]:.2f}% (2D, /sphere)  to  {band[1]:.2f}% (3D, /doublet)")
print(f"  => RIGOROUS value (3D H(curl) / sphere carrier): {100*dl_3D/carr_sphere:.2f} %")
print(f"  => the locked headline 3.07% is the 2D-reduced value (dl=0.138 / 4.4934).")
print()
print("  T4 companion (the three 'heartbeat' frequencies are distinct, canonical E):")
print("     beat f_b ~ 3.7 kHz (n0/n1 doublet) ; carrier ~121 kHz (ion Alfven) ; onset 42.6 kHz (nonlinear breathing)")
print("     identity omega_0 = 2*pi*f_b FALSIFIED x11.5 (single-mode); the onset is NOT the beat.")

print()
print("="*74)
print("T2  b_eff / anapole BLAST RADIUS from the B/v_A residual  (b_eff ∝ v_A^2)")
print("="*74)
vA0   = 2.033e4          # current residual v_A (m/s)
beff0 = 65.04            # eV
anap0 = lam1R*beff0      # anapole E = lam1R * b_eff
print(f"  current: v_A={vA0:.3e} m/s, b_eff={beff0:.2f} eV, anapole E={anap0:.1f} eV")
print(f"  frequency comb scale ~ v_A (LINEAR);  b_eff, anapole ~ v_A^2 (SQUARE)")
print()
for label, fac in [("re-anchor B0=50mT,n_i=1.7e19 (v_A x2.41)", 2.41),
                   ("wider air-scaled range low (v_A x5)", 5.0),
                   ("wider air-scaled range high (v_A x13)", 13.0)]:
    print(f"  {label}:")
    print(f"     freq/hbar_eff (linear)  x{fac:.2f}  -> comb 121 kHz -> {121*fac:6.1f} kHz")
    print(f"     b_eff (square)  x{fac**2:.1f}  -> {beff0:.0f} eV -> {beff0*fac**2/1000:.2f} keV")
    print(f"     anapole (square) x{fac**2:.1f} -> {anap0:.0f} eV -> {anap0*fac**2/1000:.2f} keV")
print()
print(f"  => b_eff/anapole square-law span over v_A x2.4-13:  x{2.41**2:.1f} to x{13**2:.0f}  (i.e. 5.8x to 170x)")
print(f"  => canonical 'blast radius ~2.4x' is the LINEAR (freq) factor; b_eff/anapole is SQUARE (~5.8-170x).")
print(f"  => ALL dimensionless ratios/counts/mass-tower/octahedral remain ANCHOR-IMMUNE (unchanged).")
