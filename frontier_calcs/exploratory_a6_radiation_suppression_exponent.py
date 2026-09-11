"""
A6 RESOLUTION (isolated, NOT editing the locked preview) — is the preview §07 "(kR)^3" radiation-suppression
exponent right? Trace + independent multipole re-derivation.

PROVENANCE: preview §07 [V] traces to ws4_nearfield_vs_farfield_channel.py:45-50, where (kR)^3 is stated as the
"sub-wavelength radiation efficiency ~ (kR)^3 (electric-dipole-like floor)" and explicitly "an UPPER bound; the
anapole suppresses further." So (kR)^3 was ALWAYS meant as a conservative upper bound, not the anapole's own value.

INDEPENDENT CHECK (order-of-magnitude in kR, standard multipole radiation):
  eta ≡ P_rad / (omega * U_stored)  [radiated power per radian, = 1/Q_rad]
  (1) small ELECTRIC dipole: P_p=omega^4 p^2/(12 pi eps0 c^3), U~p^2/(4 pi eps0 R^3)
      -> eta_ed ~ (omega R/c)^3 = (kR)^3     [the Chu/Wheeler small-antenna floor]  <-- the preview's number
  (2) small TOROIDAL dipole (the anapole: m=0, p=0, T!=0): P_T=omega^6 T^2/(12 pi eps0 c^5);
      at the SAME stored energy, |T|/|p|~R -> P_T/P_ed ~ (kR)^2, so eta_anapole ~ (kR)^2 * (kR)^3 = (kR)^5
  => (kR)^3 is a VALID CONSERVATIVE UPPER BOUND; the anapole is ~(kR)^2 fainter still (eta~(kR)^5); a near-BIC
     condition can push it lower again. The preview UNDERSTATES the darkness -> correct, not an error.
"""
import sympy as sp

k, R = sp.symbols('k R', positive=True)
# --- symbolic (kR)-power bookkeeping via dimensional scaling of the standard multipole formulae ---
# electric dipole p ~ q R ; toroidal dipole T ~ (1/c) I R^3 ~ q*omega*R^3/c  => |T|/|p| ~ R (one extra length)
# P_p ∝ omega^4 |p|^2 ;  P_T ∝ omega^6 |T|^2 ;  ratio = (omega/c)^2 |T|^2/|p|^2 = k^2 R^2 = (kR)^2
ratio_TD_over_ED = (k**2) * (R**2)
print("P_toroidal / P_electric-dipole (same source scale) =", ratio_TD_over_ED, "= (kR)^2")
# radiation efficiency (radiated / reactive) of a small electric dipole = (kR)^3 (Chu floor)
eta_ed = (k*R)**3
eta_anapole = sp.simplify(ratio_TD_over_ED * eta_ed)
print("eta_electric-dipole (Chu floor)  =", eta_ed, "= (kR)^3   <-- preview §07 number (upper bound)")
print("eta_anapole (toroidal dipole)    =", eta_anapole, "= (kR)^5   <-- the object's actual, fainter, floor")

# --- numerics at the canonical electrical size ---
kR = 9.37e-6
print(f"\nAt kR = {kR:.2e} (canonical, beat-based):")
print(f"  (kR)^3 = {kR**3:.2e}   -> preview's '~10^-15' suppression (UPPER BOUND, electrically-small floor)")
print(f"  (kR)^2 = {kR**2:.2e}   -> extra toroidal-vs-electric-dipole factor")
print(f"  (kR)^5 = {kR**5:.2e}   -> anapole's own radiated fraction (per radian), far darker still")
print("\nVERDICT: preview §07 (kR)^3 is CORRECT as a conservative upper bound (the Chu small-antenna floor);")
print("  ws4 already labels it so. The anapole radiates ~(kR)^2 fainter (eta~(kR)^5). NO error; the doc")
print("  understates the darkness. OPTIONAL v1.4 clarification only: mark (kR)^3 'an upper bound' and note the")
print("  tighter ~(kR)^5 toroidal-dipole floor. Not lock-blocking; the number stands.")
