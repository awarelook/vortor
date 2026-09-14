"""
The N-mode Woltjer theorem (LP form) + the Heuser dislocation-core Wigner crystal -- corpus fold.

Two results salvaged from the ckfreefem ark (11_verified_ark/dislocation_core, surveyed 2026-09-13;
frozen survey: results/SALVAGE_SURVEY_ARK_2026-09-13.md), here reproduced in-repo:

  TEST 1 -- THE N-MODE WOLTJER THEOREM [V]. For any collection of N distinct-eigenvalue Beltrami
            modes (curl B_k = lam_k B_k, lam_k > 0), each mode carries E_k = lam_k h_k / 2 where h_k
            is its helicity share. Fixed-helicity energy minimization is therefore EXACTLY a linear
            program:  min sum(lam_k h_k)/2  s.t.  h_k >= 0, sum h_k = H  -- whose minimum is always
            the SINGLE lowest-eigenvalue PURE mode (an LP attains its minimum at a vertex; every
            vertex is a pure mode; the lowest-lam vertex wins). No static multi-mode mixture is ever
            even a critical point. Verified here on the jewel's own spherical CK spectrum (40 modes,
            tan x = x re-derived), on a near-degenerate synthetic spectrum (the ark's WIDE40 regime),
            and by dense simplex sampling. The ark verified the same theorem symbolically (N=4) and
            by LP solve on its own real 40-mode spectrum (a genuine 6-mode mixture sat 1.15% above
            the pure ground state).
            CONSEQUENCE (the jewel's own reading): any BEAT-carrying (multi-mode) Beltrami structure
            is never a static energy minimum -- it must be continuously DRIVEN/regenerated against
            Taylor relaxation. "Heartbeat, not flywheel" is generic, not a special case -- exactly
            the driven Stuart-Landau core the jewel already carries. [V] math; the physical reading
            joins the existing [S] driven-object synthesis.

  TEST 2 -- THE WIGNER-CRYSTAL COUPLING [V-us on credited inputs]. Trapped deuterons at the measured
            Pd dislocation-core density (Heuser et al. 1991, Acta Metall. Mater. 39, 2815 -- the
            corpus's sourced trapping density n_D = 1.052e28 /m^3) have Wigner-Seitz radius
            a_WS = (3/4 pi n)^(1/3) = 2.83 Angstrom and one-component-plasma coupling
            Gamma = e^2/(4 pi eps0 a_WS k_B T) = 196.8 at 300 K -- above the OCP crystallization
            threshold Gamma ~ 172-175 (credited: Ichimaru 1982; Dubin & O'Neil 1999). The trapped
            population sits DEEP in the Wigner-crystallization regime -- the corpus's Gamma = 196.7,
            reproduced from the anchors.

numpy only, deterministic (fixed-seed sampling). Run: python results/verify/nmode_woltjer_lp_check.py
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


# ------------------------------------------------------------------ TEST 1: the LP theorem
banner("TEST 1 -- the N-mode Woltjer theorem: fixed-helicity minimum is ALWAYS the pure lowest mode  [V]")

# re-derive 40 spherical CK eigenvalues: roots of tan x = x  (g = sin x - x cos x, root n in (n pi, n pi + pi/2))
g = lambda t: np.sin(t) - t * np.cos(t)
lam = []
for n in range(1, 41):
    lo, hi = n * np.pi + 1e-6, n * np.pi + np.pi / 2 - 1e-9
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if g(lo) * g(mid) <= 0:
            hi = mid
        else:
            lo = mid
    lam.append(0.5 * (lo + hi))
lam = np.array(lam)
check("40-mode CK spectrum re-derived (x1..x3 match the canon roots)",
      abs(lam[0] - 4.493409457909064) < 1e-10 and abs(lam[1] - 7.725251836937707) < 1e-10
      and abs(lam[2] - 10.904121659428899) < 1e-10,
      "x1=%.6f x2=%.6f x3=%.6f ... x40=%.4f" % (lam[0], lam[1], lam[2], lam[39]))

# the LP structure: E(h) = sum lam_k h_k / 2 on the simplex {h >= 0, sum h = H}. Vertices = pure modes.
H = 1.0
E_pure = lam * H / 2.0
E_ground = E_pure[0]
print("  vertex (pure-mode) energies: the minimum vertex is mode 1 -- E = lam_1 H/2 = %.6f" % E_ground)
check("every other vertex sits strictly above the lowest pure mode",
      np.all(E_pure[1:] > E_ground * (1 + 1e-12)),
      "next-best vertex (mode 2) is %.1f%% above" % ((E_pure[1] / E_ground - 1) * 100))

# dense simplex sampling: no mixture beats (or ties) the pure ground state
rng = np.random.default_rng(0)
Hmix = rng.dirichlet(np.ones(40), 20000)          # 20000 helicity splittings over 40 modes
E_mix = Hmix @ (lam / 2.0)
check("20000 sampled mixtures ALL sit strictly above the pure ground state",
      np.min(E_mix) > E_ground * (1 + 1e-9),
      "closest sampled mixture: +%.2f%% above" % ((np.min(E_mix) / E_ground - 1) * 100))

# the ark's specific probe: an equal 6-mode mixture vs the pure ground state
E_6 = np.mean(lam[:6]) / 2.0
print("  equal 6-mode mixture on THIS (CK) spectrum: +%.1f%% above the pure ground state" % ((E_6 / E_ground - 1) * 100))

# near-degenerate synthetic spectrum (the ark's WIDE40 regime): the theorem still bites
lam_nd = 1.0 + 0.001 * np.arange(40)
E_nd_ground = lam_nd[0] / 2.0
E_nd_6 = np.mean(lam_nd[:6]) / 2.0
check("near-degenerate spectrum: 6-mode mixture STILL sits strictly above pure ground",
      E_nd_6 > E_nd_ground * (1 + 1e-9),
      "+%.3f%% (the ark measured +1.15%% on its own near-degenerate WIDE40)" % ((E_nd_6 / E_nd_ground - 1) * 100))

print("  -> THEOREM: an LP attains its minimum at a vertex; every vertex is a PURE mode; the lowest-")
print("     eigenvalue vertex wins. No static multi-mode Beltrami mixture is ever an energy minimum")
print("     at fixed helicity. CONSEQUENCE: a beat-carrying (multi-mode) structure can persist only by")
print("     continuous driven regeneration against Taylor relaxation -- 'heartbeat, not flywheel' is")
print("     GENERIC. This is the corpus's N-mode Woltjer theorem (11_verified_ark/dislocation_core),")
print("     reproduced on the jewel's own comb; it grounds the jewel's driven Stuart-Landau core.")

# ------------------------------------------------------------------ TEST 2: the Wigner crystal
banner("TEST 2 -- trapped D at the Heuser (1991) dislocation-core density is a Wigner crystal  [V-us]")

E_CH = 1.602176634e-19        # C
EPS0 = 8.8541878128e-12       # F/m
KB = 1.380649e-23             # J/K
n_D = 1.052e28                # /m^3  -- the corpus's Heuser-1991-derived trapped-D density
T = 300.0                     # K

a_WS = (3.0 / (4.0 * np.pi * n_D)) ** (1.0 / 3.0)
Gamma = E_CH**2 / (4.0 * np.pi * EPS0 * a_WS * KB * T)
print("  n_D = %.3e /m^3 (Heuser et al. 1991, credited)  ->  a_WS = %.3f Angstrom" % (n_D, a_WS * 1e10))
print("  Gamma = e^2/(4 pi eps0 a_WS k_B T) = %.1f  at T = 300 K" % Gamma)
check("Wigner-Seitz radius reproduces the corpus value 2.83 A", abs(a_WS * 1e10 - 2.83) < 0.01)
check("coupling reproduces the corpus Gamma = 196.7 (to <0.1%)", abs(Gamma - 196.7) / 196.7 < 1e-3,
      "Gamma = %.1f" % Gamma)
check("above the OCP crystallization threshold (Gamma ~ 172-175, Ichimaru/Dubin-O'Neil)", Gamma > 175.0,
      "deep Wigner-crystallization regime")
print("  -> the trapped-deuteron population at a REAL measured defect density is a strongly-coupled")
print("     one-component plasma past the crystallization threshold -- a credited-input, in-repo")
print("     arithmetic reproduction of the corpus's locked result. (Environment physics only -- no")
print("     nuclear-rate claim rides on this; see the corpus settled-negatives check.)")

banner("VERDICT")
print("  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
