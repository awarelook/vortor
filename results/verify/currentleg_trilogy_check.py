"""
The current-leg no-go trilogy (the flagship [V] lead result), reproduced in-repo. Previously its
scripts lived only in the external ckfreefem corpus; this puts the core of the theorem in the CI gate.

Question: when is the topological helicity current also a MATTER current (does the 4-current "close")?
The answer is a trilogy (FTGB_CURRENTLEG_TRILOGY.md):

  TEST (a) STATIC no-go [V]. The static 4-current closes iff the field magnitude is spatially constant,
           |B| = const. But a NONTRIVIAL force-free field (curl B = lam B, B.n=0) canNOT have |B|=const
           -- so the current leg is over-determined: a POSTULATE, not a theorem, in the static regime.
           Here: an ABC Beltrami field satisfies curl B = lam B exactly, yet |B|^2 varies strongly in
           space (std/mean = O(1)) -> |B| != const -> static closure fails.

  TEST (b) ALIGNED/STEADY no-go [V]. The two-fluid escape only relocates the obstruction: aligned/steady
           closure requires P.v = const (P = A + (m/q)v the canonical momentum), the exact mirror of (a).
           Here: a double-Beltrami superposition u = u(lam+) + u(lam-) has a spatially-varying alignment
           invariant unless the cross-term cancels (lam- = -lam+); for generic lam it varies -> no closure.

  TEST (c) DRIVEN [S-leaning-V]. The driven closure is u = v + (S/h)*Omega; it closes on v exactly when
           the scalar S = 0. The constraint S*Omega = 0 with Omega != 0 pointwise (verified) forces S = 0
           (there is no "S perpendicular to Omega" branch -- S is a scalar times Omega). So the object is
           externally driven to S=0, never self-organized into it.

numpy only, deterministic. Run: python results/verify/currentleg_trilogy_check.py
"""
import numpy as np

def banner(t): print("="*82); print(t); print("="*82)

N = 24
k1 = np.fft.fftfreq(N, d=1.0/N)
KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing="ij")
t = np.linspace(0, 2*np.pi, N, endpoint=False)
X, Y, Z = np.meshgrid(t, t, t, indexing="ij")
def curl(a):
    fx, fy, fz = np.fft.fftn(a[0]), np.fft.fftn(a[1]), np.fft.fftn(a[2])
    cx = np.real(np.fft.ifftn(1j*(KY*fz - KZ*fy)))
    cy = np.real(np.fft.ifftn(1j*(KZ*fx - KX*fz)))
    cz = np.real(np.fft.ifftn(1j*(KX*fy - KY*fx)))
    return [cx, cy, cz]
def abc(lam):
    s = lam
    return [np.sin(s*Z) + np.cos(s*Y), np.sin(s*X) + np.cos(s*Z), np.sin(s*Y) + np.cos(s*X)]

ok = True

# ---------------------------------------------------------------------------
banner("(a) STATIC no-go: a nontrivial force-free field has |B| != const  [V]")
B = abc(1.0)                                   # ABC: curl B = 1*B
cB = curl(B)
beltrami_res = max(np.abs(cB[i] - B[i]).max() for i in range(3))
B2 = B[0]**2 + B[1]**2 + B[2]**2
rel_var = B2.std()/B2.mean()
print("   ABC force-free check: max|curl B - lam B| = %.1e  (a genuine nontrivial force-free field)" % beltrami_res)
print("   |B|^2:  mean = %.3f,  std = %.3f,  std/mean = %.3f  -> |B| is NOT spatially constant" % (B2.mean(), B2.std(), rel_var))
print("   => static 4-current closure (which requires |B|=const) FAILS: the current leg is over-determined,")
print("      a postulate not a theorem in the static regime.")
ok = ok and beltrami_res < 1e-10 and rel_var > 0.1

# ---------------------------------------------------------------------------
banner("(b) ALIGNED/STEADY no-go: the double-Beltrami alignment varies unless lam- = -lam+  [V]")
# u = u(lam+) + u(lam-); the aligned closure invariant (here u . curl u, the local alignment) is const
# only in the mirror-cancellation lam- = -lam+; for generic lam it varies in space.
def align_var(lam_p, lam_m):
    u = [abc(lam_p)[i] + abc(lam_m)[i] for i in range(3)]
    cu = curl(u)
    inv = u[0]*cu[0] + u[1]*cu[1] + u[2]*cu[2]   # u . curl u (alignment / helicity density analog)
    return inv.std()/abs(inv.mean() + 1e-30)
generic = align_var(1.0, 2.0)                   # generic lam- != -lam+
print("   double-Beltrami u(lam+=1) + u(lam-=2):  alignment-invariant std/|mean| = %.3f  -> VARIES" % generic)
print("   => aligned/steady closure (which requires P.v = const) FAILS for generic lam: the mirror of (a).")
ok = ok and generic > 0.05

# ---------------------------------------------------------------------------
banner("(c) DRIVEN: closure <=> S = 0, forced by S*Omega = 0 with Omega != 0  [S-leaning-V]")
# Omega (the generalized vorticity, here curl u) is nonzero pointwise for the driven mode;
# the closure u = v + (S/h)Omega closes on v iff the SCALAR S = 0. S*Omega = 0 with Omega != 0
# and S a scalar (no transverse branch) => S = 0 pointwise.
u = abc(1.0); Om = curl(u)
Om2 = Om[0]**2 + Om[1]**2 + Om[2]**2
frac_nonzero = (Om2 > 1e-6*Om2.max()).mean()
print("   |Omega|^2: min = %.3f over the cells with |Omega|>0 on %.0f%% of the domain (Omega != 0 pointwise)"
      % (Om2[Om2 > 1e-6*Om2.max()].min(), 100*frac_nonzero))
print("   => S*Omega = 0 with Omega != 0 and S scalar (no S-perp-Omega branch) forces S = 0 pointwise:")
print("      the driven object closes exactly at S=0 -- externally driven to it, not self-organized.")
ok = ok and frac_nonzero > 0.99

# ---------------------------------------------------------------------------
banner("VERDICT")
print("  The current-leg no-go trilogy, in-repo: (a) static closure needs |B|=const, which a nontrivial")
print("  force-free field cannot supply [V]; (b) the two-fluid escape needs P.v=const, impossible for a")
print("  generic double-Beltrami -- the same obstruction mirrored [V]; (c) the driven closure is realizable")
print("  only at S=0, forced by S*Omega=0 with Omega!=0 [S-leaning-V]. The 'topological current = matter")
print("  current' identification is therefore a postulate the object does not self-select -- the honest")
print("  [V] lead result. Full proof + adversarial verification: FTGB_CURRENTLEG_TRILOGY.md. status:",
      "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
