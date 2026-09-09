"""
Honest numerical sense-checks on Storti EGM claims, before folding into the FTGB toolkit.
Discipline (from the user's own excision protocol + FTGB tier legend): credit what holds,
flag what does not, keep the e^(-2/3) screening factor OUT.

CODATA-ish constants (EGM's own NIST values, Part 2 p.157, where they differ).
"""
import numpy as np

hbar = 1.05457168e-34      # J s   (EGM value)
h    = 6.6260693e-34
c    = 299792458.0
G    = 6.6742e-11
me   = 9.1093826e-31
mp   = 1.67262171e-27
mn   = 1.67492728e-27
alpha= 7.297352568e-3      # fine structure constant
rp_exp = 0.8750e-15        # EGM's "classical proton RMS charge radius" (p.157); modern CODATA ~0.8409 fm

def wC(m): return m*c**2/hbar          # Compton angular frequency  omega_C = m c^2 / hbar
def lC(m): return h/(m*c)              # Compton wavelength

print("="*76)
print("1) ZPF CUBIC SPECTRAL ENERGY DENSITY  rho_0(omega) = hbar omega^3 / (2 pi^2 c^3)")
print("   [CREDITED: stochastic electrodynamics / Haisch-Rueda-Puthoff; Storti 7.2.74]")
print("="*76)
# integrated ZPF energy density up to a cutoff W:  U(W) = hbar W^4 / (8 pi^2 c^3)
def U_ZPF(W): return hbar*W**4/(8*np.pi**2*c**3)
wPl = np.sqrt(c**5/(G*hbar))           # Planck angular frequency
print(f"   Planck angular frequency  omega_Pl = {wPl:.3e} rad/s")
print(f"   ZPF energy density to omega_Pl      = {U_ZPF(wPl):.3e} J/m^3  (~Planck energy density, as expected)")

print()
print("="*76)
print("2) THE '2:1 HARMONIC'  omega_Omega(e) = 2*omega_Omega(p) = omega_CP^2/omega_Ce ?")
print("   [claim in storti_egm_missing.md]. Test whether it is a PREDICTION or DEFINITIONAL.")
print("="*76)
wCe, wCp = wC(me), wC(mp)
ratio_def = (wCp**2/wCe)              # the asserted value of omega_Omega(e)
print(f"   omega_Ce = {wCe:.4e},  omega_Cp = {wCp:.4e}")
print(f"   omega_CP^2/omega_Ce = {ratio_def:.4e}")
print(f"   If omega_Omega(e):=omega_CP^2/omega_Ce and omega_Omega(p):=half of it, the 2:1 ratio is")
print(f"   TRUE BY CONSTRUCTION (a definition), not an independent prediction.  ratio = {ratio_def/(ratio_def/2):.3f}")
print(f"   (Note m_p/m_e = {mp/me:.3f}; the secondary doc's 'St_eta=m_p/m_e' is a mislabel:")
print(f"    Storti's St_eta [Part2 7.2.89] is the 5th sense-check relating proton cut-off to proton Compton freq.)")

print()
print("="*76)
print("3) PROTON RADIUS from the simple published closed-forms in storti_egm_missing.md")
print("   Does any simple form reproduce ~0.84 fm, or is the '0.01% agreement' a full-numeric/fit result?")
print("="*76)
forms = {
    "(3/4) lCP^2/lCe" : 0.75*lC(mp)**2/lC(me),
    "(5/4) lCP^2/lCe" : 1.25*lC(mp)**2/lC(me),
    "(5/4)(me/mp) lCP": 1.25*(me/mp)*lC(mp),
    "n_O * lCP/(2pi), n_O=25": 25*lC(mp)/(2*np.pi),
}
for name,val in forms.items():
    print(f"   r_pi ~ {name:26s} = {val:.3e} m   (ratio to 0.84 fm = {val/rp_exp:.2e})")
print("   -> The clean closed-forms miss 0.84 fm by ~1e3-1e4. The quoted 0.01% agreement does NOT")
print("      follow from a simple formula; it needs the full EGM numeric solution (or is fit). FLAG.")

print()
print("="*76)
print("4) EGM RADIUS as ZPF<->mass energy-equilibrium (Storti 7.2.65), honest reconstruction")
print("   set  mc^2/((4/3)pi r^3)  =  U_ZPF(omega_C)   and solve for r ; compare to charge radius")
print("="*76)
def r_equilibrium(m):
    U = U_ZPF(wC(m))                    # ZPF energy density at the particle Compton frequency
    # mass-energy density of a uniform sphere radius r = m c^2 / (4/3 pi r^3) = U  ->  r^3 = m c^2/((4/3)pi U)
    return (m*c**2/((4.0/3.0)*np.pi*U))**(1/3)
for nm,m in [("electron",me),("proton",mp),("neutron",mn)]:
    r = r_equilibrium(m)
    print(f"   {nm:8s}: r_eq = {r:.3e} m   (Compton lambda_C = {lC(m):.3e};  ratio r_eq/lC = {r/lC(m):.3e})")
print("   -> This naive equilibrium gives a Compton-scale length (order-of-magnitude only). The EGM")
print("      charge-radius match relies on the specific Fourier cut-off closure n_Omega, not this toy.")

print()
print("="*76)
print("5) H0 from a cosmic cut-off  omega_Omega,cosmic ~ sqrt(G M_u / R_u^3)  (missing-doc route)")
print("="*76)
M_u = 1e53; R_u = 4.4e26
w_cos = np.sqrt(G*M_u/R_u**3)
Mpc = 3.0857e22                          # m
H0_from_w = w_cos * Mpc/1000.0           # s^-1 -> km/s/Mpc
print(f"   omega_cos = {w_cos:.3e} 1/s  ->  H0 ~ {H0_from_w:.1f} km/s/Mpc")
print(f"   To reach Storti's quoted 67.08 needs x{67.08/H0_from_w:.2f} (the missing-doc's unmotivated ~1.82). FLAG.")

print()
print("="*76)
print("6) FINE STRUCTURE CONSTANT: geometric winding 140.2 vs alpha^-1 = 137.036")
print("="*76)
ainv = 1/alpha
print(f"   alpha^-1 = {ainv:.4f};  toroidal winding q ~ 140.2;  gap = {(140.2/ainv-1)*100:.2f}%")
print(f"   Storti e^(-2/3) = {np.exp(-2/3):.4f} would map 140.2 -> {140.2*np.exp(-2/3):.2f} (overshoots badly);")
print(f"   the *small* screening 140.2->137.04 is 1-137.04/140.2 = {(1-137.04/140.2)*100:.2f}% (NOT e^-2/3).")
print(f"   PER EXCISION PROTOCOL: e^(-2/3) is UNJUSTIFIED numerology -> keep OUT; 2.3% stays an open problem.")
print()
print("done.")
