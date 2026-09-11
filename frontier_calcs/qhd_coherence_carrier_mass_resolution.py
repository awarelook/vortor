#!/usr/bin/env python3
r"""
qhd_coherence_carrier_mass_resolution.py
================================================================
RESOLVES the open question flagged in CONCEPT_EXPLORATION_FINDINGS (WS1 addendum):
which carrier mass m* belongs in the emergent-QHD coherence length
   sigma_0 = hbar_eff / (2 sqrt(b_eff * m*))
-- electron m_e, proton m_p, or the actual ion m_i? -- since it decides type-I vs
type-II (kappa = d_i/sigma_0 ~ m*).

ARGUMENT (physics, not fitting):
  The emergent Madelung fluid IS THE ION FLUID. Its density rho is the ion number
  density n_i; its flow v is the ion Alfven flow v_A; and BOTH emergent constants
  are per-ion: b_eff = (Gamma/R)^2 m_i v_A^2 (magnetic energy per ion) and
  hbar_eff = (Gamma/R^2) m_i v_A R (ion-fluid action). The mass in the quantum
  potential Q = -(hbar_eff^2/2 m*) lap(sqrt rho)/sqrt rho of THIS fluid is therefore
  the ion mass m_i, by construction. m_e/m_p would be the coherence of a DIFFERENT
  fluid, inconsistent with the hbar_eff/b_eff actually used.

DECISIVE CONSEQUENCE (computed below): with the self-consistent m*=m_i, the m_i
CANCELS and sigma_0/R becomes a pure geometric constant -- independent of gas
species, density, and field. So sigma_0 is ALWAYS the same fraction of the object
radius; it can never 'exceed the object', and the type-I single-fluxoid premise
cannot hold. The type-I result was an artifact of substituting m_p (=hydrogen, A=1),
which breaks the cancellation and inflates sigma_0 by sqrt(m_i/m_p)=sqrt(29)=5.4x.

Firewall: pure plasma/QHD length scales; no nuclear content.
"""
import numpy as np

m_u=1.66053907e-27; m_e=9.1093837e-31; m_p=1.67262192e-27
e=1.602176634e-19; mu0=4*np.pi*1e-7; eps0=8.8541878128e-12; cc=2.99792458e8

# canonical anchors
n_i0=1.7e19; B0=20.6e-3; R=0.12; A0=29.0
mi0=A0*m_u; vA0=B0/np.sqrt(mu0*n_i0*mi0)
# geometric constants (pure, from toroidal geometry) calibrated once on canonical
g2=1.0420e-17/(mi0*vA0**2)      # b_eff  = g2 * m_i * v_A^2
g1=6.1594e-23/(mi0*vA0*R)       # hbar_eff = g1 * m_i * v_A * R
print(__doc__)
print(f"geometric constants (species-independent): g1={g1:.5f}  g2={g2:.5f}")

def scales(A, n_i, B, mstar_choice):
    m_i=A*m_u; v_A=B/np.sqrt(mu0*n_i*m_i)
    b_eff=g2*m_i*v_A**2; hbar=g1*m_i*v_A*R
    mstar={'m_e':m_e,'m_p':m_p,'m_i':m_i}[mstar_choice]
    sig0=hbar/(2*np.sqrt(b_eff*mstar))
    d_i =cc/np.sqrt(n_i*e**2/(eps0*mstar))     # penetration depth uses the SAME carrier mass
    return dict(m_i=m_i,v_A=v_A,sig0=sig0,d_i=d_i,kap=d_i/sig0,ratio=sig0/R)

thr=1/np.sqrt(2)
print("="*72)
print("(A) The three mass choices at the canonical point (A=29):")
for ch in ('m_e','m_p','m_i'):
    s=scales(29,n_i0,B0,ch)
    typ='TYPE-I' if s['kap']<thr else 'TYPE-II'
    print(f"   m*={ch}: sigma0={s['sig0']:.4f} m ({s['sig0']/R:.2f} R)  d_i={s['d_i']*1e3:7.1f} mm"
          f"  kappa={s['kap']:7.3f}  -> {typ}")

print("="*72)
print("(B) DECISIVE self-consistency test: vary gas A, density n_i, field B --")
print("    with m*=m_i, sigma0/R must stay CONSTANT (m_i cancels):")
print(f"{'A':>5} {'n_i':>10} {'B(mT)':>7} {'sigma0/R (m_i)':>15} {'sigma0/R (m_p)':>15}")
for (A,n_i,B) in [(1,1.7e19,20.6e-3),(4,1.7e19,20.6e-3),(29,1.7e19,20.6e-3),
                  (29,5e18,20.6e-3),(29,1e20,20.6e-3),(29,1.7e19,5e-3),(29,1.7e19,60e-3),
                  (131,3e19,40e-3)]:
    si=scales(A,n_i,B,'m_i')['ratio']; sp=scales(A,n_i,B,'m_p')['ratio']
    print(f"{A:5d} {n_i:10.1e} {B*1e3:7.1f} {si:15.4f} {sp:15.4f}")

s_i=scales(29,n_i0,B0,'m_i')
print("="*72)
print("RESOLUTION:")
print(f" - Self-consistent carrier mass = m_i (ion). Then sigma0/R = g1/(2 sqrt(g2))")
print(f"   = {g1/(2*np.sqrt(g2)):.4f} = CONSTANT, independent of species/density/field (column B).")
print(f" - So sigma0 = {s_i['ratio']:.2f} R is ALWAYS below the object radius; the 'coherence")
print(f"   exceeds the object' (single-fluxoid) premise can NEVER hold self-consistently.")
print(f" - kappa = d_i/sigma0 = {s_i['kap']:.2f} > 1/sqrt2  ->  the object is TYPE-II.")
print(" - The canonical TYPE-I (kappa=0.237) used m_p (= hydrogen A=1), breaking the m_i")
print("   cancellation and inflating sigma0 by sqrt(29)=5.4x. That is an inconsistent")
print("   mass choice, not a physical result.")
print(" - m_e would require electron-borne coherence, but hbar_eff & b_eff are ION-fluid")
print("   constants (per-ion, Alfvenic); m_e is not self-consistent with them either.")
print("="*72)
print("WHAT SURVIVES: the winding is still protected -- by the Q_H=1 Hopf topology and")
print("the empirically observed 0 phase slips -- but the MECHANISM is type-II (vortices")
print("CAN fit; protection is topological + prospective flux-pinning at cascade defects),")
print("NOT the type-I single-fluxoid regime. Papers' type-I paragraphs need revision.")
