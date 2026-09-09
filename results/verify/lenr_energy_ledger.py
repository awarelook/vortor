"""
LENR theory<->experiment ledger: the CHECKABLE conservation-law arithmetic that grounds the
matter-wave interaction model. No rate or cross-section is fabricated here -- only exact
mass-energy bookkeeping, the matter-wave (m = hbar*omega/c^2) frequency ledger, and the
STRUCTURE of screening and branching (with U_s and Delta carried as named inputs, not derived).

Discipline (project excision protocol): baryon-conserving d+d only; no over-unity; Delta and
U_s are flagged as [open] / [inherited]; the neutron-suppression band is a TARGET, not a result.
"""
import numpy as np

u    = 931.49410242      # MeV / c^2  per atomic mass unit
hbar = 1.054571817e-34   # J s
MeV  = 1.602176634e-13   # J
c    = 299792458.0

# Atomic masses (u) -- electrons balance in these charge-conserving channels
m = {"n":1.00866491588, "1H":1.00782503207, "2H":2.01410177785,
     "3H":3.01604927767, "3He":3.01602932008, "4He":4.00260325413}

def Q(reactants, products):
    return (sum(m[r] for r in reactants) - sum(m[p] for p in products))*u

print("="*74)
print("1) d + d BRANCHING Q-VALUES  [credited: nuclear mass tables] -- exact")
print("="*74)
qHe = Q(["2H","2H"],["4He"])            # aneutronic fusion (the LENR-claimed channel)
qtp = Q(["2H","2H"],["3H","1H"])        # normal branch A (proton)
qhn = Q(["2H","2H"],["3He","n"])        # normal branch B (neutron)
print(f"  d + d -> 4He        Q = {qHe:7.3f} MeV   (ANEUTRONIC; hot-fusion branching ~1e-7)")
print(f"  d + d -> t + p      Q = {qtp:7.3f} MeV   (normal ~50%, charged)")
print(f"  d + d -> 3He + n    Q = {qhn:7.3f} MeV   (normal ~50%, NEUTRON channel)")
print("  -> The anomaly to explain: aneutronic 4He-dominant output. The branching to the")
print("     bound (4He) vs breakup (n) channel is set by the OFF-DIAGONAL gap Delta [open].")

print()
print("="*74)
print("2) He-4 / HEAT CORRELATION  [credited: Miles et al.] -- the experimental fingerprint")
print("="*74)
J_per_He = qHe*MeV
print(f"  Energy per 4He (if heat is d+d->4He) = {qHe:.2f} MeV = {J_per_He:.3e} J")
print(f"  Per mole of 4He                       = {J_per_He*6.02214076e23:.3e} J  ({J_per_He*6.02214076e23/1e6:.2e} MJ)")
print(f"  Observed correlation (Miles)          ~ 24 MeV / 4He atom  -> matches Q = {qHe:.1f} MeV")
print("  -> This is the load-bearing experimental hook: the ASH is 4He and the heat/4He ratio")
print("     equals the fusion Q. It says the heat is nuclear and aneutronic; it does NOT give a rate.")

print()
print("="*74)
print("3) MATTER-WAVE FREQUENCY LEDGER  m = hbar*omega/c^2  [V] identity")
print("   object interaction = matter-wave beat; conservation is  sum(hbar w_i) = sum(hbar w_f)")
print("="*74)
def wC(mass_u):   # Compton (whirl) angular frequency of a mass given in u
    return mass_u*u*MeV/hbar
wd, wHe = wC(m["2H"]), wC(m["4He"])
wQ = qHe*MeV/hbar
print(f"  omega_C(d)   = {wd:.4e} rad/s")
print(f"  omega_C(4He) = {wHe:.4e} rad/s")
print(f"  omega_Q (release) = {wQ:.4e} rad/s")
lhs, rhs = 2*wd, wHe + wQ
print(f"  2*omega_C(d)          = {lhs:.6e}")
print(f"  omega_C(4He)+omega_Q  = {rhs:.6e}   rel.diff = {abs(lhs-rhs)/lhs:.2e}")
print("  -> The matter-wave bookkeeping closes exactly (it IS mass-energy conservation restated).")
print("     The released hbar*omega_Q goes into the COHERENT collective mode (comb/EVO), not fast n/gamma.")

print()
print("="*74)
print("4) ANEUTRONIC PARTITION via E0  [S-mechanism]: where the 23.85 MeV goes")
print("="*74)
print("  The bound 4He forms through a COLLECTIVE monopole (E0) mode of the B=4 Skyrmion.")
print("  E0 forbids single-real-photon emission (0->0) -> gamma channel suppressed; de-excitation")
print("  is internal / collective -> energy sheds into the lattice+comb as HEAT, not hard radiation.")
print(f"  Budget: {qHe:.2f} MeV per event, partitioned to coherent phonon/comb modes (aneutronic).")
print("  [S] mechanism is well-posed (E0 selection is credited); the PARTITION fraction is not derived.")

print()
print("="*74)
print("5) SCREENING-ENHANCED TUNNELING  [inherited U_s]: order of magnitude, not a rate")
print("="*74)
# Sommerfeld/Gamow: P ~ exp(-2*pi*eta), eta = Z1 Z2 alpha c / v_rel ; screening: E -> E + U_s
alpha = 7.2973525693e-3
mu_dd = (m["2H"]/2)*u*MeV/c**2   # reduced mass (kg) for d-d
Z1=Z2=1
def penetration(E_eV, Us_eV=0.0):
    E = (E_eV+Us_eV)*1.602176634e-19        # J (screened energy)
    v = np.sqrt(2*E/mu_dd)                    # rel. velocity proxy
    eta = Z1*Z2*alpha*c/v
    return np.exp(-2*np.pi*eta), eta
for E_eV in [300.0, 1000.0]:
    p0,eta0 = penetration(E_eV, 0.0)
    for Us in [300.0, 800.0]:
        ps,_ = penetration(E_eV, Us)
        print(f"  E={E_eV:6.0f} eV, U_s={Us:4.0f} eV:  penetration enhancement P(E+U_s)/P(E) = {ps/p0:.3e}")
print("  -> Screening gives a LARGE but FINITE enhancement of barrier penetration (standard Gamow).")
print("     U_s ~ 300-800 eV is HOST-LATTICE INHERITED (accepted-not-adjudicated), NOT FTGB-derived.")
print("     This sets the reaction PROBABILITY scale; the branching (aneutronic vs n) is Delta's job.")

print()
print("="*74)
print("6) THE TWO OPEN/INHERITED RATE INPUTS (nothing below is claimed as derived)")
print("="*74)
print("  Delta  [OPEN, FTGB-internal]: off-diagonal B=4 Landau-Zener gap; TARGET band 1.4-1.9 MeV")
print("         (would suppress the neutron/breakup branch). HPC-only (pion-massive Skyrme).")
print("  U_s    [INHERITED]: host-lattice screening ~300-800 eV; sets penetration, not branching.")
print("  COP    [NOT DERIVED]: 1.3-1.4 is field positioning; NO over-unity; vacuum is a medium, not a source.")
print()
print("done.")
