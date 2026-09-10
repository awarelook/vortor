"""
The OAM ladder l -> l +/- N from DISCRETE SYMMETRY: is the mechanism real, computed in-repo?

The paper (sec.C.3) claims the object's orbital angular momentum "steps by the octahedral
order, l -> l +/- N." The analogue-prior-art-verifier established that the *mechanism* (a
discrete point-group symmetry of order N steps angular momentum by N) is credited physics
-- Finkelstein-Rubinstein (1968) + Braaten-Townsend-Carson (1990, Phys.Lett.B 235,147) for
the SAME B=4 octahedral Skyrmion (nuclear spin: ground J=0, first excited J=4), and
Ferrando (2005), Konishi (2014), Chen (2014) for electromagnetic OAM. This script COMPUTES
that mechanism from first-principles group theory, so it is [V] in-repo, not cited-only.
It does NOT validate the *application* to the driven Beltrami-Hopf plasmoid's EM-carried
OAM -- that stays [claimed synthesis]; what is proven here is the selection rule itself,
plus that the B=4 octahedral symmetry the FTGB LENR channel already adopts forces exactly
the l={0,4,6,...} ladder with fundamental step Delta l = 4.

  TEST A -- the ladder step is EXACTLY N (concrete, azimuthal Bloch selection). A field with
            C_N rotational symmetry has an azimuthal spectrum supported only on m = 0 mod N;
            hence an N-fold-symmetric coupling ladders any source mode m0 by multiples of N,
            i.e. m -> m +/- N and no other step. Shown to machine precision by FFT for N=4.
  TEST B -- the OCTAHEDRAL ladder l in {0,4,6,8,9,10,...} with first step Delta l = 4
            (full SO(3) -> O subduction via characters). n_A1(l) = # of octahedral-invariant
            states in the spin-l multiplet; the invariant l-channels are the allowed OAM rungs.
            l=1,2,3,5 carry NO invariant (forbidden); l=4 is the first excited rung.
  TEST C -- CONVERGENCE: the first two invariant rungs (0,4) reproduce Braaten-Townsend-Carson's
            B=4 Skyrmion rigid-rotor spectrum (ground J=0 -> first excited J=4) -- the credited
            nuclear-spin result equals the computed OAM selection ladder. Same object, same rule.

math-only, group theory + FFT, deterministic. Run: python results/verify/octahedral_oam_ladder_check.py
"""
import numpy as np

def banner(t): print("="*78); print(t); print("="*78)

ok = True

# ---------------------------------------------------------------------------
banner("A) ladder step is EXACTLY N: a C_N-symmetric coupling shifts m by multiples of N")
# Build an azimuthal grid and a DETERMINISTIC base "potential" g(phi); C_N-symmetrize it.
Nphi = 512
phi = np.linspace(0.0, 2*np.pi, Nphi, endpoint=False)
N = 4                                             # octahedral 4-fold (C4) axis
# a deterministic, generic base field (several modes, no randomness); it MUST carry some
# modes at multiples of N so the symmetrized potential is non-trivial and the ladder is exercised
g = (1.3*np.cos(phi) + 0.7*np.sin(2*phi) - 0.9*np.cos(3*phi)
     + 1.1*np.cos(5*phi) + 0.5*np.sin(7*phi) + 0.8
     + 1.0*np.cos(4*phi) + 0.6*np.cos(8*phi))
# C_N symmetrization: V(phi) = (1/N) sum_k g(phi + 2 pi k / N)
V = np.zeros_like(phi)
for k in range(N):
    V += np.interp((phi + 2*np.pi*k/N) % (2*np.pi), phi, g, period=2*np.pi)
V /= N
Vhat = np.fft.rfft(V)
m_axis = np.arange(Vhat.size)
power = np.abs(Vhat)
tol = 1e-9 * power.max()
surviving = m_axis[power > tol]
print("  C_%d-symmetrized potential: surviving azimuthal modes m = %s" % (N, list(surviving)))
print("  (all are multiples of N=%d; every non-multiple is killed to < 1e-9 of the peak)" % N)
ok_A1 = all(int(m) % N == 0 for m in surviving)
# now ladder a source mode m0=2 through the C_N potential: modes produced = m0 + {0,+-N,...}
m0 = 2
source = np.exp(1j*m0*phi)
coupled = V * source                              # product = convolution of spectra
Chat = np.fft.fft(coupled)
freqs = np.fft.fftfreq(Nphi, d=1.0/Nphi).astype(int)
cp = np.abs(Chat); ctol = 1e-9*cp.max()
produced = sorted(int(f) for f in freqs[cp > ctol])
print("  ladder a source mode m0=%d through it -> produced modes m = %s" % (m0, produced))
print("  -> every produced mode satisfies m == m0 (mod N): the step is EXACTLY N, none other.")
ok_A2 = all((m - m0) % N == 0 for m in produced) and len(produced) >= 3
ok = ok and ok_A1 and ok_A2

# ---------------------------------------------------------------------------
banner("B) the OCTAHEDRAL ladder l in {0,4,6,8,9,10,...}, first step Delta l = 4  (SO(3) -> O)")
# proper octahedral rotation group O (order 24): classes (angle, weight)
#   E:1@0 ; 8 C3 @ 2pi/3 ; 6 C4 @ pi/2 ; 3 C2 @ pi ; 6 C2' @ pi  (the two pi-classes merge: 9@pi)
CLASSES = [(0.0, 1), (2*np.pi/3, 8), (np.pi/2, 6), (np.pi, 9)]
ORDER = sum(w for _, w in CLASSES)                # = 24

def chi_l(l, theta):
    """SO(3) character of the spin-l irrep: sin((l+1/2) theta) / sin(theta/2), = 2l+1 at 0."""
    s = np.sin(theta/2.0)
    if abs(s) < 1e-14:
        return 2*l + 1
    return np.sin((l + 0.5)*theta) / s

def n_invariant(l):
    """# of O-invariant (trivial-irrep A1) states in the spin-l multiplet (integer)."""
    tot = sum(w * chi_l(l, th) for th, w in CLASSES) / ORDER
    r = round(tot)
    assert abs(tot - r) < 1e-9, "non-integer multiplicity at l=%d: %.6f" % (l, tot)
    return int(r)

mult = {l: n_invariant(l) for l in range(0, 13)}
ladder = [l for l in range(0, 13) if mult[l] > 0]
print("  n_invariant(l) for l=0..12:  %s" % {l: mult[l] for l in range(0, 13)})
print("  allowed OAM rungs (invariant l-channels): %s ..." % ladder)
print("  forbidden low channels: l=1,2,3,5 carry NO octahedral-invariant state.")
print("  first excited rung above the l=0 ground state:  Delta l = %d" % (ladder[1] - ladder[0]))
ok_B = (ladder[:4] == [0, 4, 6, 8]
        and mult[1] == 0 and mult[2] == 0 and mult[3] == 0 and mult[5] == 0
        and mult[0] == 1 and mult[4] == 1
        and (ladder[1] - ladder[0]) == 4)
ok = ok and ok_B

# ---------------------------------------------------------------------------
banner("C) CONVERGENCE: rungs (0,4) reproduce Braaten-Townsend-Carson B=4 Skyrmion (J=0 -> J=4)")
btc_ground, btc_first = 0, 4                       # credited: PLB 235,147 (1990) rigid-rotor spectrum
our_ground, our_first = ladder[0], ladder[1]
print("  Braaten-Townsend-Carson B=4 (nuclear spin):   ground J=%d , first excited J=%d" % (btc_ground, btc_first))
print("  this script's octahedral OAM selection ladder: ground l=%d , first excited l=%d" % (our_ground, our_first))
print("  -> identical: same octahedral object, same discrete-symmetry selection rule.")
ok_C = (our_ground == btc_ground and our_first == btc_first)
ok = ok and ok_C

# ---------------------------------------------------------------------------
banner("VERDICT")
print("  The MECHANISM l -> l +/- N is COMPUTED in-repo, not merely cited: a discrete symmetry of")
print("  order N shifts angular momentum by exactly N (TEST A, machine precision), and the octahedral")
print("  group forces the OAM ladder l in {0,4,6,8,9,10,...} with fundamental step Delta l = 4")
print("  (TEST B), reproducing the credited B=4 Skyrmion spectrum (TEST C). Since the FTGB LENR")
print("  channel ALREADY adopts the B=4 octahedral Skyrmion, this octahedral OAM ladder is inherited,")
print("  now [V] (group theory) / [credited] (BTC, Ferrara-... , Ferrando/Konishi/Chen).")
print("  STILL [claimed synthesis], NOT promoted here: that the driven Beltrami-Hopf plasmoid's")
print("  ELECTROMAGNETICALLY carried/emitted OAM follows this same ladder ('protected by the sheath")
print("  winding') -- the rule is proven, its application to the EM-emission channel is not.  status:",
      "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
