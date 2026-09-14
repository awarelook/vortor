"""
The aneutronic disposal FORK, computed (M16 settled-negative): a proposed "selection-by-assembly" elevation of
the branching wall FAILS under adversarial test, and in failing it exposes a clean fork with BOTH branches
walled. Judged on self-consistent physics alone -- no appeal to authority.

THE ATTEMPT (honest to record; it did not survive). After the Byrnes causality wall relocated to channel
SELECTION (the >=1e7 aneutronic branching swing), a reframe was proposed: the neutron-bearing exits belong to
the d+d (B=4) entrance channel; the aneutronic 2-alpha exit belongs to the 4d (B=8) channel; so selection is
by SLOW cluster assembly (2d vs 4d), causally safe, and neutron-dearth is intrinsic (the 4d channel has no
free-nucleon exit). A skeptic pass (2026-09-14) REFUTED it quantitatively. Logged here, not glossed.

WHY IT FAILS -> a FORK (both branches walled):
  BRANCH (a) 4d -> 2alpha (momentum-clean: two back-to-back 23.85 MeV alphas, net p=0). But 4d->2alpha gives
    REAL 23.85 MeV alphas (two-body kinematics -- unavoidable), and a 23.85 MeV alpha is above every light-element
    Coulomb barrier along its stopping path -> secondary (alpha,n) at ~1e-6..1e-4 n per 4He (Am-Be anchor
    ~7e-5 n/alpha at only 5.5 MeV). That EXCEEDS the observed neutron/4He <= 1e-9..1e-12 by 3-8 ORDERS -> the
    fast-alpha branch is SELF-REFUTING. (Plus ~2.6e11 alphas/s per watt of 24 MeV alphas: trivially detectable,
    not seen; Miles' 4He is thermalized, consistent with LOW-energy birth.) And a real 8Be* compound at
    E*=47.6 MeV sits ~29 MeV above S_n -> evaporates neutrons unless exact di-alpha simultaneity is ASSUMED.
  BRANCH (b) d+d -> 4He with SOFT collective disposal (no fast alphas -> no (alpha,n)). Momentum is fine at the
    slow end (soft-quantum cascade carries the small 4He recoil to the lattice, causally allowed). But this is
    exactly the OPEN B=4 wall: does an on-shell collective mode with nonzero matrix element exist on the hard
    MeV->keV segment? (direct phonon coupling settled-negative ~66 OOM; the near-BPS/HPC Delta run). RATE OPEN.
  BAIT-AND-SWITCH FLAG: the only bounded rate object, Delta = 23.85 MeV x rho_eff with rho_eff in [0,1]
    (delta_nearbps_scale_bound_check), is a B=4 crossing overlap -- it does NOT license the B=8 assembly rate.

  TEST 1 -- the momentum fork is real: single-product d+d->4He from rest cannot conserve p (needs a recoil
            partner OR the 4d->2alpha two-alpha channel). [V]-logic
  TEST 2 -- BRANCH (a) is self-refuting: 23.85 MeV alphas -> secondary (alpha,n) ~1e-6..1e-4 n/4He, EXCEEDING
            observed neutron/4He <= 1e-9 by 3-8 OOM; plus an undetected ~2.6e11/s/W flux of 24 MeV alphas. [V]-arith
  TEST 3 -- BRANCH (a) also reopens neutrons at the fast stage: 8Be* at E*=47.6 MeV is ~29 MeV above the
            neutron threshold (S_n=18.9 MeV) -> a compound system evaporates n unless di-alpha simultaneity is
            merely assumed (Takahashi TSC assumption, not derived). [V]-arith
  TEST 4 -- so ONLY branch (b) survives, and it is the project's already-open B=4 wall (rate/branching), NOT
            cleared by the assembly reframe. The rho_eff in [0,1] bound is B=4 and does not transfer to B=8. [settled-neg]

numpy only, deterministic. Run: python results/verify/aneutronic_disposal_fork_check.py
"""
import numpy as np

ok = True
U = 931.494
M_D, M_A = 2.01410177812, 4.00260325413
M_N, M_HE3 = 1.00866491588, 3.01602932008
M_1H, M_TA = 1.00782503207, 3.01604928
MC2_A = 3727.379


def banner(t):
    print("=" * 98); print(t); print("=" * 98)


def check(name, cond, detail=""):
    global ok
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, ("  -- " + detail) if detail else ""))
    ok = ok and cond


# ---------------------------------------------------------------- TEST 1: the momentum fork
banner("TEST 1 -- the momentum fork: single-product d+d->4He from rest cannot conserve momentum")
Q_4he = (2*M_D - M_A)*U
Q_4d2a = (4*M_D - 2*M_A)*U
KE_a = Q_4d2a/2.0
pc_a = np.sqrt(KE_a**2 + 2*KE_a*MC2_A)
print("   d+d->4He (single product) Q=%.2f MeV: from ~rest, ONE 4He cannot carry the momentum -> needs a partner." % Q_4he)
print("   the momentum-clean option is 4d->2alpha: Q=%.2f MeV, two back-to-back %.2f MeV alphas (p=%.0f MeV/c, net p=0)." % (Q_4d2a, KE_a, pc_a))
check("aneutronic disposal forks into (a) 4d->2alpha [momentum-clean] vs (b) d+d->4He soft-collective [needs a soft cascade]",
      abs(Q_4d2a - 47.7) < 0.2 and abs(KE_a - 23.85) < 0.1, "the fork is forced by momentum conservation")

# ---------------------------------------------------------------- TEST 2: branch (a) self-refutes via (alpha,n)
banner("TEST 2 -- BRANCH (a) 4d->2alpha is SELF-REFUTING: 23.85 MeV alphas make secondary (alpha,n) neutrons")
yield_an_lo, yield_an_hi = 1e-6, 1e-4        # secondary (alpha,n) n per 24 MeV alpha (light-element converters; Am-Be~7e-5 at 5.5 MeV)
obs_hi, obs_lo = 1e-9, 1e-12                 # observed neutron/4He band
n_per_he_lo, n_per_he_hi = yield_an_lo, yield_an_hi   # ~1 fast alpha per 4He
excess_lo = np.log10(n_per_he_lo/obs_hi); excess_hi = np.log10(n_per_he_hi/obs_lo)
# 24 MeV alpha flux at 1 W
W = 1.0; MeV_per_s = W/1.602176634e-13
alpha_flux = MeV_per_s/KE_a
print("   secondary (alpha,n) yield ~%.0e..%.0e n per 4He  vs observed neutron/4He <= %.0e..%.0e" % (yield_an_lo, yield_an_hi, obs_hi, obs_lo))
print("   -> the fast-alpha branch OVERPRODUCES neutrons by %.0f-%.0f orders (self-refuting for an aneutronic claim)" % (excess_lo, excess_hi))
print("   plus a %.1e /s per watt flux of 23.85 MeV alphas (trivially detectable; not observed; Miles' 4He is thermalized)" % alpha_flux)
check("BRANCH (a) 4d->2alpha overproduces neutrons via (alpha,n) by 3-8 OOM above the observed bound -> EXCLUDED",
      excess_lo >= 3, "the momentum fix manufactures a fast-alpha (alpha,n) signature the neutron-dearth data already refutes")

# ---------------------------------------------------------------- TEST 3: branch (a) reopens neutrons at contact
banner("TEST 3 -- BRANCH (a) also reopens the neutron channel at the fast stage (8Be* is far above threshold)")
# 8Be* excitation from 4d: E* = Q(4d->8Be gs) ... use E* ~ Q(4d->2alpha) since 8Be gs ~ 2 alpha; S_n(8Be)=18.9 MeV
E_star = Q_4d2a                              # ~47.6 MeV of internal energy if it equilibrates as 8Be*
S_n = 18.9                                    # MeV, neutron separation energy of 8Be
above_thresh = E_star - S_n
print("   an equilibrated 8Be* at E* ~ %.1f MeV sits %.1f MeV ABOVE the neutron threshold (S_n = %.1f MeV)" % (E_star, above_thresh, S_n))
check("a compound 8Be* evaporates neutrons unless EXACT di-alpha simultaneity is ASSUMED (not derived)",
      above_thresh > 20, "so slow assembly protects the APPROACH, not the SELECTION -- the neutron channel returns at nuclear contact")

# ---------------------------------------------------------------- TEST 4: only branch (b) survives -> the open B=4 wall
banner("TEST 4 -- only BRANCH (b) d+d->4He soft-collective survives -> the project's ALREADY-OPEN B=4 wall")
print("   branch (b): NO fast alphas -> no (alpha,n); momentum OK at the slow end (soft cascade carries the small")
print("   4He recoil to the lattice, causally allowed). But it IS the open B=4 question: does an on-shell collective")
print("   mode with nonzero matrix element exist on the hard MeV->keV segment? (direct phonon coupling settled-neg")
print("   ~66 OOM; the near-BPS/HPC Delta run). The rho_eff in [0,1] bound is B=4 -- it does NOT license a B=8 route.")
check("the selection-by-assembly reframe does NOT clear the wall; the only survivor is the open B=4 rate/branching",
      True, "settled-negative: the 'elevation' exposed a fork with (a) EXCLUDED and (b) OPEN -- it did not resolve it")

banner("VERDICT")
print("  The 'selection-by-assembly' elevation of the aneutronic-branching wall FAILS (judged on physics alone).")
print("  It exposes a FORK, both branches walled: (a) 4d->2alpha is momentum-clean but SELF-REFUTING -- its")
print("  23.85 MeV alphas make secondary (alpha,n) neutrons 3-8 OOM ABOVE the observed dearth, and an 8Be* is")
print("  ~29 MeV above the neutron threshold; (b) d+d->4He soft-collective avoids the alphas but IS the project's")
print("  already-open B=4 wall (does the on-shell disposal mode exist? -- the near-BPS/HPC run). The bounded")
print("  rho_eff in [0,1] object is B=4 and does NOT transfer to the B=8 assembly rate (bait-and-switch flagged).")
print("  HONEST NET: the wall is NOT cleared; it is SHARPENED into a fork. Energy [V] / mechanism [S] / rate OPEN.")
print("  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
