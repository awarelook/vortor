"""
Stage 0 of the EM-OAM derivation: WHAT IS N for the PLASMA object's electromagnetically
carried OAM ladder l -> l +/- N?  (decides whether sec.C.3's "octahedral order" is right)

Background. octahedral_oam_ladder_check.py proved the octahedral ladder (N=4, invariant
l in {0,4,6,8,9,10,...}, first step Delta l=4) for the B=4 NUCLEAR Skyrmion -- that is [V]
and correct AT THE NUCLEAR RUNG. Paper sec.C.3 then asserts the *plasma* object's EM-carried
OAM "steps by the octahedral order," silently transferring the B=4 nuclear point group to the
plasma Beltrami field. This script TESTS that transfer, and lets it decide N.

Key simplification. For a force-free object curl B = lam B => (Ampere) J = (lam/mu0) B, so the
radiating current is PARALLEL to the field: the point group that selects the radiated OAM
multipoles IS the Beltrami field's point group. The engine's explicit Beltrami field is the
A=B=C ABC field u = (sin z + cos y, sin x + cos z, sin y + cos x); its point group sets N.

  TEST A  -- POINT GROUP scan: over candidate centers, all 24 proper cubic rotations. The
             C4 (90deg) face-axis rotations are NEVER a point symmetry (max violation); the
             C3 body-diagonal axis always is. The field is NOT octahedral as a point group.
  TEST A2 -- the order-24 "octahedral" symmetry lives in the SPACE group: the C4/C2 rotations
             are symmetries only when paired with a half-period TRANSLATION (a roto-translation).
             Translations do not act on a LOCALIZED radiator, so they cannot protect its OAM
             ladder -- only the pure point rotations (E + C3) survive.
  TEST B  -- the ROBUST discrete symmetry is a 3-fold axis => the EM OAM ladder is N=3. The
             azimuthal spectrum of the field about the body-diagonal axis lives on m = 0 (mod 3)
             (off-3 power at machine zero), with GENUINE m=3 content (not axisymmetric), and
             m = 0 (mod 4) is violated. The OAM projection ladders by EXACTLY 3.
  VERDICT -- reframe N: 4 -> 3 for the EM-carried OAM (the plasma object's body-diagonal C3);
             the octahedral N=4 is correct only at the B=4 nuclear rung. N=3 coincides with the
             theory's native triad (three CK comb lines, 3-6-9). Honest caveat: the full discrete
             group is configuration-dependent (the theory has not pinned the localized EM
             configuration); only the 3-fold axis is center-robust.

math-only, group theory + FFT, deterministic. Run: python results/verify/oam_stage0_pointgroup_check.py
"""
import itertools
import numpy as np

def banner(t): print("="*80); print(t); print("="*80)

def u(P):
    """the engine's Beltrami field (A=B=C ABC); P shape (...,3). J = (lam/mu0) u, so this IS
    the point group that selects the radiated OAM."""
    x, y, z = P[..., 0], P[..., 1], P[..., 2]
    return np.stack([np.sin(z) + np.cos(y),
                     np.sin(x) + np.cos(z),
                     np.sin(y) + np.cos(x)], axis=-1)

# the 24 proper rotations of the cube = signed permutation matrices with det +1
ROTS = []
for perm in itertools.permutations((0, 1, 2)):
    for s in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3))
        for i in range(3):
            M[i, perm[i]] = s[i]
        if round(np.linalg.det(M)) == 1:
            ROTS.append(M)
assert len(ROTS) == 24

def cls(M):
    return {3: "E", 0: "C3", 1: "C4", -1: "C2"}[round(np.trace(M))]

# grid for the residual tests
ng = 24
tg = np.linspace(0, 2*np.pi, ng, endpoint=False)
G = np.stack(np.meshgrid(tg, tg, tg, indexing="ij"), axis=-1)   # (ng,ng,ng,3)
U = u(G); NRM = np.sqrt((U**2).sum())

def residual(M, center=(0., 0., 0.), t=(0., 0., 0.)):
    """|| (R,t).u - u || / ||u|| about a center; 0 => symmetry.  (R.u)(r)=M u(c + M^T(r-c-t))."""
    c = np.asarray(center); tv = np.asarray(t)
    Rr = c + (G - c - tv) @ M          # row-vector x@M = M^T x
    rot = u(Rr) @ M.T                  # apply M to the vector components
    return np.sqrt(((rot - U)**2).sum()) / NRM

ok = True

# ---------------------------------------------------------------------------
banner("A) POINT GROUP of the plasma Beltrami field: no C4 axis (=> not octahedral)")
centers = [(0., 0., 0.), (np.pi, np.pi, np.pi), (np.pi/2, np.pi/2, np.pi/2),
           (np.pi/2, 0., 0.)]
bestn = 0
for c in centers:
    inv = {"E": 0, "C3": 0, "C4": 0, "C2": 0}
    for M in ROTS:
        if residual(M, center=c) < 1e-9:
            inv[cls(M)] += 1
    tot = sum(inv.values())
    bestn = max(bestn, tot)
    print("  center (%.2f,%.2f,%.2f): invariant pure rotations E=%d C3=%d C4=%d C2=%d  (order %d)"
          % (c[0], c[1], c[2], inv["E"], inv["C3"], inv["C4"], inv["C2"], tot))
# across all tested centers, is a C4 EVER a pure point symmetry?
anyC4 = any(residual(M, center=c) < 1e-9 for M in ROTS if cls(M) == "C4" for c in centers)
# is the body-diagonal C3 a point symmetry about the origin?
c3_ok = any(residual(M, center=(0., 0., 0.)) < 1e-9 for M in ROTS if cls(M) == "C3")
print("  -> any C4 as a PURE point rotation?  %s      body-diagonal C3 present?  %s" %
      ("YES" if anyC4 else "NO", "YES" if c3_ok else "no"))
print("  the point group has a 3-fold axis and NO 4-fold axis: NOT octahedral.")
ok = ok and (not anyC4) and c3_ok

# ---------------------------------------------------------------------------
banner("A2) the order-24 symmetry lives in the SPACE group (roto-translations), not the point group")
shifts = [0, np.pi/2, np.pi, 3*np.pi/2]
for target in ("C4", "C2"):
    best = (1e9, None)
    for M in ROTS:
        if cls(M) != target:
            continue
        for t0 in itertools.product(shifts, repeat=3):
            r = residual(M, t=t0)
            if r < best[0]:
                best = (r, t0)
        if best[0] < 1e-9:
            break
    rr, t0 = best
    print("  %s rotation: min residual %.1e  with translation t=(%.2f,%.2f,%.2f)  -> %s"
          % (target, rr, t0[0], t0[1], t0[2],
             "roto-translation (needs the shift)" if rr < 1e-9 else "no symmetry"))
    ok = ok and rr < 1e-9
print("  translations do NOT act on a localized radiator => only E + C3 protect its OAM ladder.")

# ---------------------------------------------------------------------------
banner("B) the EM OAM ladder is N=3: azimuthal spectrum about the body-diagonal C3 axis")
n_ax = np.array([1, 1, 1.]) / np.sqrt(3)
e1 = np.array([1, -1, 0.]) / np.sqrt(2)
e2 = np.cross(n_ax, e1)
def azim_power(rho, h):
    Mphi = 720
    phi = np.linspace(0, 2*np.pi, Mphi, endpoint=False)
    ring = (h*n_ax[None, :] + rho*(np.cos(phi)[:, None]*e1[None, :]
                                   + np.sin(phi)[:, None]*e2[None, :]))
    s = u(ring) @ n_ax                              # axial field component on the ring
    S = np.abs(np.fft.rfft(s)); return S / S.max()
allok_B = True; m3_present = False
for (rho, h) in [(1.0, 0.0), (1.5, 0.6), (0.8, 1.2)]:
    S = azim_power(rho, h)
    modes = [m for m in range(1, 13) if S[m] > 1e-6]
    off3 = sum(S[m] for m in range(1, 13) if m % 3)
    on3 = sum(S[m] for m in range(1, 13) if m % 3 == 0)
    off4 = sum(S[m] for m in range(1, 13) if m % 4)
    print("  ring rho=%.1f h=%.1f: active m=%s | off-mult-3 power=%.1e | off-mult-4 power=%.3e"
          % (rho, h, modes, off3, off4))
    m3_present = m3_present or (S[3] > 1e-6)
    allok_B = allok_B and (off3 < 1e-9 * max(on3, 1e-30)) and (off4 > 1e-6)
print("  -> azimuthal (OAM) content lives on m = 0 (mod 3), genuine m=3 present (not axisymmetric),")
print("     and m = 0 (mod 4) is violated. The OAM projection ladders by EXACTLY N = 3.")
ok = ok and allok_B and m3_present

# ---------------------------------------------------------------------------
banner("VERDICT")
N_em, N_nuclear = 3, 4
print("  Stage 0 decides:  the PLASMA / EM Beltrami object's OAM ladder is  N = %d  (its robust" % N_em)
print("  body-diagonal C3 axis), NOT the octahedral N = %d.  The octahedral N=4 ladder is correct" % N_nuclear)
print("  ONLY at the B=4 NUCLEAR rung (octahedral_oam_ladder_check.py). sec.C.3's 'octahedral order'")
print("  for the EM-carried OAM was a symmetry BORROWED from the nucleus; the computed EM value is")
print("  N=3, which coincides with the theory's native triad (three CK comb lines, 3-6-9).")
print("  Honest caveat: the full discrete group is configuration-dependent (the theory has not")
print("  pinned WHICH localized mode-superposition the EM object is); only the 3-fold axis is")
print("  center-robust. Stages 1-3 (radiation multipoles, OAM/SAM split) build on THIS N, not 4.")
print("  reframe:  N: 4 -> 3 (EM object).   status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
