"""
The Eshelby zero-coupling theorem -- corpus fold, reproduced AND sharpened (its exact boundary found).

Salvaged from the ckfreefem corpus (TORUS_MATHEMATICS_APPENDIX sections 31.10-31.12; ark pointer:
11_verified_ark/dynamical_plasmoid; survey: results/SALVAGE_SURVEY_ARK_2026-09-13.md). The corpus's
closure: the dislocation loop's TORSIONAL (pure-shear) phonon mode has NO leading-order coupling to
the trapped-deuteron fusion rate via any volume-mediated deformation-potential channel
(dE_F/E_F = -(2/3) dV/V couples only to dilatation), because
  (a) the twist displacement field carries EXACTLY zero dilatation (div u = 0), and
  (b) the trap-site (Eshelby ellipsoidal-inclusion) response cannot "rectify" a shear eigenstrain
      into a volume change -- checked there for the aligned case, in-plane rotations, out-of-plane
      tilts, and triaxial shapes, all exactly zero.

We reproduce (a) and (b) in-repo with a from-scratch Eshelby S-tensor (numerical I-integrals,
validated against the exact textbook sphere closed form) -- AND, pressing the reproduction harder,
we compute the closed TRACE LAW the corpus did not state:

      trace(S : eps*) = nu/(1-nu) tr(eps*)  +  (1-2 nu)/(4 pi (1-nu)) * sum_j I_j eps*_jj

(a direct consequence of the ellipsoid's interior potential being quadratic). This law says the
corpus's zeros are SYMMETRY-PROTECTED, not universal: they hold exactly for (i) any eigenstrain
that is purely off-diagonal in the ellipsoid frame (aligned shears and all tilts of them -- every
configuration the corpus tested), and (ii) diagonal-traceless eigenstrains whose weights pair
across EQUAL-I axes (in-plane rotations on a spheroid, I_1 = I_2). But a shear whose principal
stretch axes SPAN the spheroid's short axis (eps* = diag(s, 0, -s)) gives a genuinely NONZERO
trace ~ (1-2 nu)(I_1 - I_3) s / (4 pi (1-nu)) -- order-unity in s for a strongly oblate trap. So:

  THE CLOSURE STANDS for the corpus's physically-motivated aligned geometry (the twist mode's shear
  is off-diagonal in the trap frame set by the same dislocation) -- reproduced exactly. THE
  GENERALIZATION "for any ellipsoidal shape AND ANY ORIENTATION" is CORRECTED: generic misalignment
  of the shear's principal axes across the short axis revives the coupling at O((1-2nu)(I_1-I_3)).
  Computed, logged, tiered -- the boundary of a theorem is part of the theorem.

  TEST 1 -- the torsional field's dilatation is exactly zero (numeric, ~1e-11)             [V]
  TEST 2 -- S-tensor machinery validated: sphere closed forms + standard I-identities      [V]
  TEST 3 -- the corpus's zeros reproduced: off-diagonal shears (all shapes/tilts) and
            in-plane-rotated shears (spheroid) give trace(S:eps*) = 0 to quadrature error  [V]
  TEST 4 -- the trace law verified + the boundary: diag(s,0,-s) on an oblate spheroid is
            NONZERO, matching the closed law; the corpus overreach is named               [V]

numpy only, deterministic. Run: python results/verify/eshelby_zero_coupling_check.py
"""
import numpy as np

ok = True


def banner(t):
    print("=" * 92)
    print(t)
    print("=" * 92)


def check(name, cond, detail=""):
    global ok
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, ("  -- " + detail) if detail else ""))
    ok = ok and cond


# ---------------------------------------------------------------- TEST 1: div u = 0 for the twist
banner("TEST 1 -- the torsional (twist) mode carries EXACTLY zero dilatation  [V]")
# torsional wave on the (locally straight) dislocation tube: u = u0 sin(k z) e_theta, cylindrical
# coords (rho, theta, z). Cartesian: u = u0 sin(kz) * (-y, x, 0)/rho. Dilatation div u -> 0 exactly.
h = 1e-6
pts = [(0.7, 0.3, 0.5), (1.2, -0.4, 2.0), (0.3, 0.9, -1.1)]


def u_twist(x, y, z, k=2.0):
    rho = np.sqrt(x * x + y * y)
    return np.sin(k * z) * np.array([-y / rho, x / rho, 0.0])


max_div = 0.0
for (x, y, z) in pts:
    div = ((u_twist(x + h, y, z)[0] - u_twist(x - h, y, z)[0])
           + (u_twist(x, y + h, z)[1] - u_twist(x, y - h, z)[1])
           + (u_twist(x, y, z + h)[2] - u_twist(x, y, z - h)[2])) / (2 * h)
    max_div = max(max_div, abs(div))
check("div u = 0 at every test point (finite difference)", max_div < 1e-9,
      "max |div u| = %.1e (field scale 1)" % max_div)
print("  -> a pure twist is deviatoric: the deformation potential dE_F/E_F = -(2/3) dV/V sees nothing")
print("     from the BULK field. The remaining question is trap-site (Eshelby) rectification.")

# ---------------------------------------------------------------- Eshelby machinery
banner("TEST 2 -- from-scratch Eshelby S-tensor, validated against the textbook sphere  [V]")
NU = 0.3


def I_integrals(a):
    """I_i and I_ij for a general ellipsoid, by numerical quadrature (Mura's definitions)."""
    a1, a2, a3 = a
    x = np.linspace(0.0, 1.0 - 1e-10, 2_000_001)
    s = x / (1.0 - x)
    w = 1.0 / (1.0 - x) ** 2                      # ds = w dx
    D = np.sqrt((a1**2 + s) * (a2**2 + s) * (a3**2 + s))
    pref = 2.0 * np.pi * a1 * a2 * a3
    I = [pref * np.trapezoid(w / ((a[i]**2 + s) * D), x) for i in range(3)]
    Iij = [[pref * np.trapezoid(w / ((a[i]**2 + s) * (a[j]**2 + s) * D), x) for j in range(3)]
           for i in range(3)]
    return np.array(I), np.array(Iij)


def S_tensor(a, nu=NU):
    """Isotropic interior Eshelby tensor (principal frame), Mura eq. 11.16 structure."""
    I, Iij = I_integrals(a)
    S = np.zeros((3, 3, 3, 3))
    c1 = 1.0 / (8.0 * np.pi * (1.0 - nu))
    c2 = (1.0 - 2.0 * nu) * c1
    for i in range(3):
        S[i, i, i, i] = 3.0 * c1 * a[i]**2 * Iij[i][i] + c2 * I[i]
        for j in range(3):
            if j != i:
                S[i, i, j, j] = c1 * a[j]**2 * Iij[i][j] - c2 * I[i]
                S[i, j, i, j] = S[i, j, j, i] = S[j, i, i, j] = S[j, i, j, i] = \
                    0.5 * c1 * (a[i]**2 + a[j]**2) * Iij[i][j] + 0.5 * c2 * (I[i] + I[j])
    return S, I, Iij


def apply_S(S, eps):
    return np.einsum("ijkl,kl->ij", S, eps)


# validation: sphere closed forms + the standard identities
S_sph, I_sph, Iij_sph = S_tensor((1.0, 1.0, 1.0))
s1111 = (7.0 - 5.0 * NU) / (15.0 * (1.0 - NU))
s1212 = (4.0 - 5.0 * NU) / (15.0 * (1.0 - NU))
check("sphere S_1111 = (7-5nu)/(15(1-nu))", abs(S_sph[0, 0, 0, 0] - s1111) < 1e-7,
      "%.8f vs %.8f" % (S_sph[0, 0, 0, 0], s1111))
check("sphere S_1212 = (4-5nu)/(15(1-nu))", abs(S_sph[0, 1, 0, 1] - s1212) < 1e-7,
      "%.8f vs %.8f" % (S_sph[0, 1, 0, 1], s1212))
_, I_ob, Iij_ob = S_tensor((1.0, 1.0, 0.2))
check("identity sum(I_i) = 4 pi (oblate 0.2)", abs(np.sum(I_ob) - 4 * np.pi) < 1e-6)
check("identity 3 I_11 + I_12 + I_13 = 4 pi / a1^2 (oblate 0.2)",
      abs(3 * Iij_ob[0][0] + Iij_ob[0][1] + Iij_ob[0][2] - 4 * np.pi) < 1e-6)

# ---------------------------------------------------------------- TEST 3: the corpus's zeros
banner("TEST 3 -- the corpus closure reproduced: symmetry-protected zeros  [V]")
shear12 = np.zeros((3, 3)); shear12[0, 1] = shear12[1, 0] = 1.0
worst = 0.0
for ar in [(1.0, 1.0, 0.9), (1.0, 1.0, 0.5), (1.0, 1.0, 0.2), (1.0, 1.0, 0.05), (1.0, 0.7, 0.3)]:
    S, I, _ = S_tensor(ar)
    # (i) aligned shear + tilts of it about axis 1 (stays purely off-diagonal): all shapes incl. triaxial
    for t in (0.0, 0.3, 0.7, 1.2):
        c, s_ = np.cos(t), np.sin(t)
        Rt = np.array([[1, 0, 0], [0, c, -s_], [0, s_, c]])
        eps = Rt @ shear12 @ Rt.T
        worst = max(worst, abs(np.trace(apply_S(S, eps))))
    # (ii) in-plane rotation (generates diagonals, protected by I_1 = I_2) -- spheroids only
    if ar[0] == ar[1]:
        for t in (0.2, 0.5, np.pi / 4):
            c, s_ = np.cos(t), np.sin(t)
            Rz = np.array([[c, -s_, 0], [s_, c, 0], [0, 0, 1]])
            eps = Rz @ shear12 @ Rz.T
            worst = max(worst, abs(np.trace(apply_S(S, eps))))
check("trace(S:eps*) = 0 for every corpus-tested class (aligned/tilted/in-plane, all shapes)",
      worst < 1e-6, "max |trace| = %.1e" % worst)
print("  -> the ALIGNED geometry is the physically-motivated one (the trap spheroid's axes are set")
print("     by the same dislocation that defines the twist) -- the corpus closure STANDS there:")
print("     the torsional mode's fusion-rate coupling via any volume channel is exactly zero.")

# ---------------------------------------------------------------- TEST 4: the trace law + boundary
banner("TEST 4 -- the closed trace law + the corrected boundary (the corpus's overreach)  [V]")


def trace_law(I, eps, nu=NU):
    return (nu / (1.0 - nu)) * np.trace(eps) \
        + (1.0 - 2.0 * nu) / (4.0 * np.pi * (1.0 - nu)) * np.sum(I * np.diag(eps))


rng = np.random.default_rng(1)
worst_law = 0.0
for ar in [(1.0, 1.0, 0.5), (1.0, 1.0, 0.2), (1.0, 0.7, 0.3)]:
    S, I, _ = S_tensor(ar)
    for _ in range(5):
        eps = rng.standard_normal((3, 3)); eps = 0.5 * (eps + eps.T)
        worst_law = max(worst_law, abs(np.trace(apply_S(S, eps)) - trace_law(I, eps)))
check("trace(S:eps*) = nu/(1-nu) tr(eps*) + (1-2nu)/(4pi(1-nu)) sum I_j eps*_jj  (all shapes)",
      worst_law < 1e-6, "max law dev = %.1e (15 random eigenstrains x 3 shapes)" % worst_law)

# the boundary: a pure shear whose principal axes span the short axis: eps* = diag(s, 0, -s)
S_ob, I_ob, _ = S_tensor((1.0, 1.0, 0.2))
eps_b = np.diag([1.0, 0.0, -1.0])                      # a rotated pure shear (eigenvalues +1, -1, 0)
tr_b = np.trace(apply_S(S_ob, eps_b))
tr_b_law = trace_law(I_ob, eps_b)
coeff = (1.0 - 2.0 * NU) / (4.0 * np.pi * (1.0 - NU)) * (I_ob[0] - I_ob[2])
check("the BOUNDARY: diag(s,0,-s) on an oblate (c/a=0.2) trap gives NONZERO trace",
      abs(tr_b) > 0.05 and abs(tr_b - tr_b_law) < 1e-6,
      "trace = %.4f s  (law: %.4f s) -- order-unity, NOT small" % (tr_b, tr_b_law))
print("  -> CORRECTED SCOPE (our sharpening, computed not asserted): the corpus's zeros are")
print("     SYMMETRY-PROTECTED -- exact for every configuration it tested (off-diagonal shears at")
print("     any tilt, any shape incl. triaxial; in-plane rotations on a spheroid) -- but its")
print("     'any ellipsoidal shape AND ANY ORIENTATION' generalization overreaches: a shear whose")
print("     principal stretch axes span the short axis couples at O((1-2nu)(I_1-I_3)) ~ %.2f s." % coeff)
print("     The PHYSICAL closure (aligned twist mode vs dislocation-set trap axes) is unaffected;")
print("     a hypothetical strongly-MISALIGNED trap would reopen the channel -- now quantified.")
print("     The boundary of a theorem is part of the theorem (same discipline as the FPUT winding")
print("     boundary, fput_winding_conservation_check.py).")

banner("VERDICT")
print("  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
