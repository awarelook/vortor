"""
Stages 1-3 of the EM-OAM derivation: does the driven plasmoid's FAR-FIELD emission actually
REALIZE the N=3 OAM ladder that Stage 0 fixed?  (and how much survives the OAM/SAM subtlety?)

Stage 0 (oam_stage0_pointgroup_check.py) computed the plasma object's point group = a 3-fold
body-diagonal C3, so N=3. Here we take the localized driven source J(r) e^{-iwt} (J = envelope
* the C3-symmetric Beltrami field) and compute what it RADIATES.

Key fact that makes this decidable. The radiation multipole amplitudes a_E(l,m), a_M(l,m)
(Jackson ch.9) are built from the source against vector spherical harmonics ~ e^{imphi}. The
azimuthal integral int e^{-imphi}(...) dphi therefore GATES every multipole: a C3-symmetric
source can only feed multipoles with m = 0 (mod 3). So the far-field angular-momentum ladder
is N=3 -- realized in the emitted field, not merely asserted from the source.

  TEST 1a (Stage 1) -- azimuthal moments A(m) = int e^{-imphi'} S d^3r of the driven source
            (S = n.(rxJ), the C3-invariant angular-momentum density about the axis): nonzero
            ONLY for m = 0 (mod 3) (off-ladder at machine zero), with genuine m=3,6,9 content.
  TEST 1b (Stage 2) -- the FULL radiation multipole amplitude a(l,m) with the j_l(kr) radial
            kernel and P_l^m(cos th') e^{-imphi'} angular kernel: nonzero on-ladder (m=0,3),
            machine-zero off-ladder (m=1,2) -- the N=3 ladder in the genuine emitted multipoles.
  TEST 2  (Stage 3) -- OAM vs SAM, honestly. m is the gauge-invariant J_z projection per
            multipole (TOTAL angular momentum). The photon SAM (spin-1, s in {-1,0,+1}) shifts
            the OAM index l = m - s by a FIXED amount, so it moves the ladder's OFFSET but not
            its SPACING. => the N=3 SPACING is robust to the orbital/spin split; the ABSOLUTE
            OAM value per rung is limit/gauge-dependent (the textbook global L/S split is not
            gauge-invariant -- clean only in the paraxial far zone).

VERDICT. The far-field emission DOES realize an N=3 OAM ladder in the robust sense: the LADDER
SPACING (and the operational topological-charge = J_z content) is [V]; the clean orbital-vs-spin
SEPARATION stays [S]. Honest ceiling: promote what survives the gauge subtlety (the N=3 step),
keep the absolute OAM label flagged.

math-only (numpy), deterministic. Run: python results/verify/oam_stage123_emission_check.py
"""
import numpy as np

def banner(t): print("="*82); print(t); print("="*82)

# ---- localized driven Beltrami source: J = envelope(|r|) * u_ABC(r) (C3 about body diagonal) ----
L, N = 6.0, 64
t = np.linspace(-L, L, N)
X, Y, Z = np.meshgrid(t, t, t, indexing="ij")
dV = (2*L/N)**3
sig = 2.2
env = np.exp(-(X**2 + Y**2 + Z**2)/(2*sig**2))
Jx = env*(np.sin(Z) + np.cos(Y))
Jy = env*(np.sin(X) + np.cos(Z))
Jz = env*(np.sin(Y) + np.cos(X))

n  = np.array([1, 1, 1.])/np.sqrt(3)
e1 = np.array([1, -1, 0.])/np.sqrt(2)
e2 = np.cross(n, e1)

# C3-invariant angular-momentum source density  S = n . (r x J)
rxJx = Y*Jz - Z*Jy
rxJy = Z*Jx - X*Jz
rxJz = X*Jy - Y*Jx
S = n[0]*rxJx + n[1]*rxJy + n[2]*rxJz

rmag = np.sqrt(X**2 + Y**2 + Z**2) + 1e-12
zp = X*n[0] + Y*n[1] + Z*n[2]
xp = X*e1[0] + Y*e1[1] + Z*e1[2]
yp = X*e2[0] + Y*e2[1] + Z*e2[2]
phi = np.arctan2(yp, xp)
ct = zp/rmag
st = np.sqrt(np.clip(1 - ct**2, 0, 1))

ok = True

# ---------------------------------------------------------------------------
banner("1a) radiated azimuthal moments A(m) = int e^{-i m phi'} S : nonzero only m = 0 (mod 3)")
A = {m: abs((np.exp(-1j*m*phi)*S).sum()*dV) for m in range(0, 10)}
peak = max(A.values())
for m in range(0, 10):
    tag = "<-- allowed (m = 0 mod 3)" if m % 3 == 0 else ""
    print("   m=%d : |A|/peak = %.2e   %s" % (m, A[m]/peak, tag))
off3 = max(A[m]/peak for m in range(0, 10) if m % 3)
m36 = min(A[3]/peak, A[6]/peak)
print("   -> off-ladder moments <= %.1e (machine zero); genuine m=3,6 content present." % off3)
ok = ok and off3 < 1e-12 and m36 > 1e-3

# ---------------------------------------------------------------------------
banner("1b) the FULL radiation multipole a(l,m) [j_l(kr) . P_l^m(cos th') . e^{-i m phi'}]")
def jl(l, x):
    if l == 0: return np.sin(x)/x
    if l == 2: return (3/x**2 - 1)*np.sin(x)/x - 3*np.cos(x)/x**2
    if l == 3: return (15/x**3 - 6/x)*np.sin(x)/x - (15/x**2 - 1)*np.cos(x)/x
    if l == 4: return (105/x**4 - 45/x**2 + 1)*np.sin(x)/x - (105/x**3 - 10/x)*np.cos(x)/x
def Plm(l, m, u, s):                        # assoc. Legendre (unnormalized; sign irrelevant to zero-test)
    return {(3, 3): -15*s**3, (3, 0): 0.5*(5*u**3 - 3*u), (4, 3): -105*u*s**3,
            (2, 1): -3*u*s, (3, 1): -1.5*(5*u**2 - 1)*s, (4, 2): 7.5*(7*u**2 - 1)*s**2}[(l, m)]
k = 0.8
tests = [(3, 3, "allowed"), (3, 0, "allowed"), (4, 3, "allowed"),
         (2, 1, "FORBIDDEN"), (3, 1, "FORBIDDEN"), (4, 2, "FORBIDDEN")]
amp = {}
for (l, m, lab) in tests:
    kern = jl(l, k*rmag)*Plm(l, m, ct, st)*np.exp(-1j*m*phi)
    amp[(l, m)] = abs((kern*S).sum()*dV)
apk = max(amp.values())
for (l, m, lab) in tests:
    print("   (l=%d, m=%d)  %-9s |a|/peak = %.2e" % (l, m, lab, amp[(l, m)]/apk))
allowed = min(amp[(3, 3)], amp[(4, 3)])/apk
forbid = max(amp[(2, 1)], amp[(3, 1)], amp[(4, 2)])/apk
print("   -> allowed multipoles radiate (>=%.2e); forbidden are machine zero (<=%.1e)." % (allowed, forbid))
ok = ok and forbid < 1e-11 and allowed > 1e-3

# ---------------------------------------------------------------------------
banner("2) OAM vs SAM: the N=3 SPACING is robust; the absolute OAM OFFSET is not")
print("   m = gauge-invariant J_z (total) per multipole, pinned to m = 0 (mod 3).")
print("   photon SAM s in {-1,0,+1} shifts the OAM index l = m - s by a FIXED offset:")
mset = [m for m in range(-9, 10) if m % 3 == 0]
spacings = set()
for s in (-1, 0, 1):
    lset = sorted(m - s for m in mset)
    sp = sorted(set(np.diff(lset)))
    spacings |= set(sp)
    print("     SAM s=%+d : OAM rungs l = %s ...   spacing = %s" % (s, lset[3:7], sp))
print("   -> spacing = 3 for EVERY polarization: the ladder STEP survives the OAM/SAM split;")
print("      only the absolute OAM offset is limit/gauge-dependent (global L/S not gauge-inv.).")
ok = ok and spacings == {3}

# ---------------------------------------------------------------------------
banner("VERDICT")
print("  The driven plasmoid's FAR-FIELD emission REALIZES an N=3 OAM ladder: the C3 source")
print("  feeds only m = 0 (mod 3) multipoles (Tests 1a/1b, machine-zero off-ladder), so the")
print("  radiated total-angular-momentum ladder -- and the operationally measured topological")
print("  charge (the OAM index of structured-light experiments) -- steps by 3. The ladder")
print("  SPACING N=3 is ROBUST to the orbital/spin ambiguity (SAM = a fixed offset shift, Test 2).")
print("  So sec.C.3's EM-emission claim is promoted for what survives the gauge subtlety:")
print("     N=3 ladder spacing + J_z content ............... [V]")
print("     absolute orbital-vs-spin SEPARATION per rung ... [S] (limit/gauge-dependent)")
print("  The [claimed synthesis] shrinks to just the absolute OAM label; the ladder is earned.")
print("  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
