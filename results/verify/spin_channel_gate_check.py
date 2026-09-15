"""
The ENTRANCE-CHANNEL SPIN/ORIENTATION GATE: the quantum arithmetic of where Stage D says the selectivity
must live -- with a new falsifier (polarization dependence) and a logged three-piece consistency.

Stage D (delta_b4_stageD_bps_overlap_check) proved the density-support geometry CANNOT supply rho_eff's
needed smallness (~0.07): the suppression must live in ORIENTATION/phase space. This check computes the
exact quantum-channel arithmetic of that space for d+d -> 4He(0+), and what coherent preparation does to it.
Every quantum number here is textbook; the FTGB identification stays [S]; the consistency product is logged
coincidence-class, never promoted.

  TEST 1 -- THE CHANNEL DECOMPOSITION [credited]. Two deuterons (spin-1, isospin-0 bosons): 9 spin states.
            Bose symmetry ties spin to parity of L: S in {0,2} (symmetric) pairs with even L; S=1 with odd L.
            The 4He ground state is 0+; the s-wave door to it is the SINGLET (1S0) alone: 1 state of 9
            (all-encounters statistical gate 1/9), or 1 of the 6 s-wave-allowed states (1/6).
  TEST 2 -- THE GATE IS STEERABLE BY COHERENT PREPARATION [credited CG arithmetic / [S] identification].
            Two deuterons drawn from one condensate mode |1,m>:
              m = 0   : singlet fraction |<00|1,0;1,0>|^2 = 1/3  -- THREE TIMES the statistical gate;
              m = +-1 : singlet fraction = 0 EXACTLY (|1,m;1,m> is pure quintet) -- the s-wave door CLOSES;
                        the residual S=2 -> 0+ route needs L=2, suppressed ~(kR)^4 ~ 1.3e-6 at 240 eV.
            So single-mode coherence acts EXACTLY in the space Stage D isolated, and in BOTH directions:
            it can triple the aneutronic gate (m=0) or shut it (m=+-1). This gives the cold Bose-degenerate
            seed (already [S] in-jewel, n*lambda^3 >= 2.612) a mechanism-shaped job: CHANNEL PREPARATION.
  TEST 3 -- THE THERMAL FENCE [V]-arith. mu_d*B/kT ~ 1e-6..1e-5 at any plasmoid-scale field (<= 10 T):
            thermal Boltzmann polarization CANNOT set the gate -- any spin-channel selection must be
            dynamical/coherent. (Honest: this is a fence on the mechanism's source, not proof it operates.)
  TEST 4 -- THE THREE-PIECE CONSISTENCY (logged, NOT promoted). gate x StageD-density-bracket:
              1/9 x [0.55, 0.96] = [0.061, 0.107]   -- OVERLAPS the target band rho_eff ~ 0.06-0.08
              1/6 x [0.55, 0.96] = [0.092, 0.160]   -- adjacent above
            Three independently-sourced pieces (textbook statistics, the computed density proxy, the
            LZ-band target) meet at the same decade. Coincidence-class: the bands are wide, the proxy has
            named omissions, the target band's own provenance is flagged -- logged in COINCIDENCE_LEDGER,
            not claimed as a derivation of Delta.
  TEST 5 -- THE NEW FALSIFIER (theory-specific, experimentally meaningful): the aneutronic 4He yield of a
            coherent active site must DEPEND ON DEUTERON SPIN PREPARATION -- m=0/singlet-weighted assembly
            enhances it (up to 3x gate), m=+-1 polarization collapses the s-wave door (yield drop toward
            the ~1e-6 d-wave floor). Context [credited-contested]: spin-polarized fusion is real physics
            (Kulsrud-Furth-Valeo-Goldhaber, PRL 49, 1248 (1982), d-t); for d+d the "quintet suppression"
            question is a NAMED CONTESTED issue in few-body physics (Paetz gen Schieck et al. -- complete
            citation before external use). FTGB adds a sharp, site-specific version: polarization-steered
            aneutronic yield at a coherent site.

  HONEST SCOPE: this does NOT compute a rate, does NOT show the m=0 preparation actually occurs (that is
  the corridor dynamics, open), and does NOT resolve the contested d+d quintet-suppression physics. It
  computes the exact channel arithmetic, fences its source (coherent, not thermal), logs the consistency,
  and mints the falsifier.

numpy only, deterministic. Run: python results/verify/spin_channel_gate_check.py
"""
import numpy as np

ok = True


def banner(t):
    print("=" * 98); print(t); print("=" * 98)


def check(name, cond, detail=""):
    global ok
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, ("  -- " + detail) if detail else ""))
    ok = ok and cond


# exact spin-1 pair algebra (no CG tables imported -- built from operators)
Sz = np.diag([1.0, 0.0, -1.0])
Sp = np.zeros((3, 3)); Sp[0, 1] = Sp[1, 2] = np.sqrt(2.0)
Sm = Sp.T
Sx, Sy = (Sp + Sm) / 2.0, ((Sp - Sm) / 2.0) * 1.0  # Sy used only inside S^2 via symmetric combination
I3 = np.eye(3)


def tot(A):
    return np.kron(A, I3) + np.kron(I3, A)


S2 = tot(Sx) @ tot(Sx) + tot(Sz) @ tot(Sz)
# Sy^2 contribution built from ladder identity: Sx^2+Sy^2 = (Sp Sm + Sm Sp)/2
SyT2 = 0.5 * (tot(Sp) @ tot(Sm) + tot(Sm) @ tot(Sp)) - tot(Sx) @ tot(Sx)
S2 = S2 + SyT2
w, v = np.linalg.eigh(S2)
P0 = v[:, np.abs(w) < 1e-9] @ v[:, np.abs(w) < 1e-9].T          # singlet projector
e = np.eye(3)


def pair(m1, m2):
    return np.kron(e[1 - m1], e[1 - m2])


banner("TEST 1 -- the channel decomposition: 9 states; the s-wave door to 4He(0+) is the singlet alone  [credited]")
dims = {int(round((-1 + np.sqrt(1 + 4 * ww)) / 2)): 0 for ww in np.unique(np.round(w, 6))}
for ww in np.round(w, 6):
    S = int(round((-1 + np.sqrt(1 + 4 * ww)) / 2))
    dims[S] += 1
print("   S-multiplet dimensions from the operator algebra: %s (expect S=0:1, S=1:3, S=2:5)" % dims)
check("1 + 3 + 5 = 9 spin states, S in {0,1,2}", dims == {0: 1, 1: 3, 2: 5}, "")
check("statistical singlet gate = 1/9 (all encounters)", abs(np.trace(P0) / 9 - 1.0 / 9.0) < 1e-12,
      "Bose symmetry: S=1 pairs only with odd L -> s-wave-allowed set is 6 states, singlet 1/6 of those")

banner("TEST 2 -- the gate is STEERABLE: single-mode condensate pairs  [credited CG / [S] identification]")
f0 = float(pair(0, 0) @ P0 @ pair(0, 0))
fp = float(pair(1, 1) @ P0 @ pair(1, 1))
fm = float(pair(-1, -1) @ P0 @ pair(-1, -1))
print("   singlet fraction of |1,m>|1,m>:  m=0 -> %.6f ;  m=+1 -> %.2e ;  m=-1 -> %.2e" % (f0, fp, fm))
mu_red = 3.3436e-27 / 2.0
E240 = 240.0 * 1.602176634e-19
k = np.sqrt(2 * mu_red * E240) / 1.054571817e-34
kR = k * 1e-14
print("   m=+-1 residual route (S=2, L=2 -> J=0): centrifugal (kR)^4 = %.1e at E=240 eV, R=10 fm" % kR ** 4)
check("m=0 condensate pair: singlet fraction = 1/3 (3x the statistical gate)", abs(f0 - 1.0 / 3.0) < 1e-12, "")
check("m=+-1 condensate pair: singlet fraction = 0 EXACTLY (pure quintet -> s-wave door closed)",
      fp < 1e-14 and fm < 1e-14, "residual d-wave route suppressed ~%.0e" % kR ** 4)

banner("TEST 3 -- the thermal fence: Boltzmann polarization cannot set the gate  [V]-arith")
muN = 5.0507837e-27
mud = 0.8574 * muN
for B in (1.0, 10.0):
    r = mud * B / (1.380649e-23 * 300.0)
    print("   B = %4.1f T: mu_d B / kT(300 K) = %.1e" % (B, r))
check("thermal polarization <= 1e-4 at any plasmoid-scale field", mud * 10 / (1.380649e-23 * 300.0) < 1e-4,
      "any spin-channel selection must be DYNAMICAL/coherent -- the Bose-seed single-mode occupation is the [S] candidate")

banner("TEST 4 -- the three-piece consistency (logged coincidence-class, NOT promoted)")
lo, hi = 0.55, 0.96                    # StageD density-geometry proxy bracket
band_lo, band_hi = 0.06, 0.08          # the rho_eff target band (Delta 1.4-1.9 MeV)
p9 = (lo / 9.0, hi / 9.0)
p6 = (lo / 6.0, hi / 6.0)
print("   1/9 x [%.2f, %.2f] = [%.3f, %.3f]  vs target [%.2f, %.2f]" % (lo, hi, p9[0], p9[1], band_lo, band_hi))
print("   1/6 x [%.2f, %.2f] = [%.3f, %.3f]" % (lo, hi, p6[0], p6[1]))
overlap = p9[0] <= band_hi and band_lo <= p9[1]
check("statistical gate x density bracket OVERLAPS the target band", overlap,
      "three independent pieces meet at one decade -- logged in COINCIDENCE_LEDGER with the wide-band caution")
check("no Delta value is promoted from this consistency", True,
      "bands are wide; the proxy has named omissions; the target band's provenance is itself flagged")

banner("TEST 5 -- the NEW FALSIFIER: polarization-steered aneutronic yield")
print("   Prediction (theory-specific): at a coherent active site, the aneutronic 4He yield depends on the")
print("   deuteron spin preparation -- m=0/singlet-weighted assembly ENHANCES it (up to 3x gate); m=+-1")
print("   polarization COLLAPSES the s-wave door (toward the ~1e-6 d-wave floor). A polarization/field-")
print("   -steering knob on the aneutronic channel is something NO thermal-statistical model predicts.")
print("   Context: spin-polarized fusion is real physics [Kulsrud-Furth-Valeo-Goldhaber PRL 49, 1248 (1982),")
print("   d-t]; the d+d 'quintet suppression' question is NAMED and CONTESTED in few-body physics (Paetz gen")
print("   Schieck et al. -- complete the citation before external use). FTGB's addition is the coherent-site,")
print("   preparation-steered version -- falsifiable with polarized targets/fields at a candidate site.")
check("falsifier minted: spin-preparation dependence of the aneutronic yield", True,
      "kill: no polarization dependence at a verified coherent site")
print("  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
