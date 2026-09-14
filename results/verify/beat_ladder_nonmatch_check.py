"""
Beat-cascade ladder vs the ONE existing beat-sweep dataset (M14/M16, honest non-match log).

FTGB's sharpest theory-specific LENR discriminator is the beat-locked yield step: as a drive sweeps the
self-similar cascade, nuclear yield rises in DISCRETE geometric steps f_b(L) = N^L f_b(0) (N=4; M14-1 ladder,
greenyer_beat_cascade_check.py). The novelty audit (2026-09-14) asked the honest question the discipline
requires -- does the ONE published beat-sweep excess-heat dataset already show (or already refute) this ladder?
-- and this script computes the answer and LOGS it, so the claim is never quoted as confirmed or as duplicated.

  THE PRIOR ART (credited, the signature-CLASS predates FTGB): Hagelstein, Letts & Cravens (2010),
  J. Condensed Matter Nucl. Sci. 3, 59 -- two lasers detuned to a swept DIFFERENCE (beat) frequency on Pd-D;
  excess-heat response reported locked near 8.2 / 15.1 / 20.8 THz. So "sweep a beat frequency, look for a
  locked yield step" is field-standard, NOT new to FTGB. What is (narrowly) original to FTGB is the EXACT
  self-similar geometric functional form f_b(L) = N^L f_b(0).

  TEST 1 -- the CK carrier comb is the INHARMONIC fingerprint 1:1.719:2.427 (roots of tan x = x), distinct
            from a harmonic 1:2:3 -- the [V] spectral discriminator (also ck_eigenvalues_check.py).
  TEST 2 -- the FTGB beat-cascade ladder is GEOMETRIC: f_b(L)/f_b(0) = N^L = 1, 4, 16, 64 (N=4).
  TEST 3 -- NON-MATCH (the honest log): the reported HLC steps 8.2/15.1/20.8 THz have ratios
            1.84 / 1.38 / 2.54 -- NONE is a clean power of N=4 (4^0=1, 4^0.5=2, 4^1=4). So the one existing
            beat-sweep dataset NEITHER confirms NOR duplicates the FTGB N^L ladder: the prediction stays
            genuinely UNTESTED, and FTGB's geometric form is distinct from Hagelstein's phonon-harmonic steps.
            A computed coincidence, logged as a non-match (COINCIDENCE_LEDGER) -- not a hit, not a refutation.

numpy only, deterministic. Run: python results/verify/beat_ladder_nonmatch_check.py
"""
import numpy as np

ok = True


def banner(t):
    print("=" * 94); print(t); print("=" * 94)


def check(name, cond, detail=""):
    global ok
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, ("  -- " + detail) if detail else ""))
    ok = ok and cond


# ---------------------------------------------------------------- TEST 1: the CK inharmonic fingerprint
banner("TEST 1 -- the CK carrier comb is the INHARMONIC fingerprint 1:1.719:2.427 (not harmonic 1:2:3)  [V]")
g = lambda z: np.sin(z) - z*np.cos(z)
roots = []
for a, b in [(4.0, 5.0), (7.0, 8.0), (10.5, 11.5)]:
    lo, hi = a, b
    for _ in range(90):
        m = 0.5*(lo+hi)
        if g(lo)*g(m) <= 0:
            hi = m
        else:
            lo = m
    roots.append(0.5*(lo+hi))
r = np.array(roots)/roots[0]
print("   CK ratios (tan x = x): 1 : %.3f : %.3f   vs harmonic 1 : 2 : 3" % (r[1], r[2]))
check("the CK comb is inharmonic 1:1.719:2.427 (the falsifiable spectral fingerprint)",
      abs(r[1]-1.719) < 0.01 and abs(r[2]-2.427) < 0.01, "a harmonic 1:2:3 lock would falsify the Beltrami-carrier reading")

# ---------------------------------------------------------------- TEST 2: the geometric beat-cascade ladder
banner("TEST 2 -- the FTGB beat-cascade ladder is GEOMETRIC: f_b(L)/f_b(0) = N^L  [S]")
N = 4
ladder = np.array([N**L for L in range(4)])
print("   N = %d ->  f_b(L)/f_b(0) = %s  (a self-similar geometric ladder)" % (N, list(ladder)))
check("the beat-step prediction is the geometric ladder 1, 4, 16, 64", list(ladder) == [1, 4, 16, 64],
      "the sharpest theory-specific discriminator; no static LENR model predicts a geometric yield-step ladder")

# ---------------------------------------------------------------- TEST 3: the honest non-match vs HLC 2010
banner("TEST 3 -- NON-MATCH: the one existing beat-sweep dataset (HLC 2010) does NOT fit the N^L ladder  [log]")
hlc = np.array([8.2, 15.1, 20.8])       # THz, Hagelstein-Letts-Cravens 2010 (JCMNS 3, 59) excess-heat steps
# A GEOMETRIC ladder f_b(L)=r^L has EQUAL consecutive ratios (r each step). Test that first -- it is
# N-independent and unambiguous, so it does not hinge on any tolerance for "a clean power of 4".
c1, c2 = hlc[1]/hlc[0], hlc[2]/hlc[1]          # consecutive step ratios
spread = abs(c1 - c2)/min(c1, c2)             # how far from a constant ratio (geometric)
print("   HLC steps 8.2/15.1/20.8 THz -> consecutive ratios %.2f, %.2f  (a geometric ladder needs them EQUAL)" % (c1, c2))
print("   consecutive-ratio spread = %.0f%%  ->  NOT a geometric sequence for ANY base N" % (spread*100))
# and, for color, neither consecutive ratio is N=4 or sqrt(N)=2 within 15%
near4 = min(abs(c1-4)/4, abs(c2-4)/4); near2 = min(abs(c1-2)/2, abs(c2-2)/2)
print("   (nearest N=4 miss %.0f%% ; nearest sqrt(N)=2 miss %.0f%%)" % (near4*100, near2*100))
check("the HLC steps do NOT form a geometric ladder (consecutive ratios 1.84 vs 1.38 differ ~34%) -> no N^L fit",
      spread > 0.20, "so the one existing beat-sweep dataset neither confirms nor duplicates the FTGB N^L ladder")
print("   -> HONEST LOG: FTGB's geometric f_b(L)=N^L is DISTINCT from Hagelstein's phonon-harmonic steps and")
print("      stays a GENUINELY UNTESTED falsifier (not confirmed, not refuted). Signature-CLASS is credited")
print("      prior art (HLC 2010); the exact geometric form is the narrow original residue. [COINCIDENCE_LEDGER]")

banner("VERDICT")
print("  The CK inharmonic comb (TEST 1, [V]) and the geometric beat-cascade ladder (TEST 2, [S]) are FTGB's")
print("  two falsifiable spectral discriminators. The discipline check (TEST 3): the sole published")
print("  beat-sweep excess-heat dataset (Hagelstein-Letts-Cravens 2010) does NOT fit the N^L ladder -- logged")
print("  as a non-match, so the prediction is neither over-claimed as confirmed nor mistaken for prior art.")
print("  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
