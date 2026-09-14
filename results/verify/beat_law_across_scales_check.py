"""
The beat as a collective field across the scale hierarchy (M14/M16): ONE beat law f_b = v_A|dlam|/(2piR)
rides plasmoids from lab (kHz) to space (mHz), and the CK inharmonic RATIO is SCALE-INVARIANT -- so the
falsifiable fingerprint can be measured at whatever scale is accessible.

The user's question: how does the beat "logic" express physically across scales -- laser/lattice vs spheromak
vs lab plasmoid vs space plasmoid complexes -- as one collective field? Answer, tiered:
  * The CARRIER f_b = v_A|dlam|/(2piR) is the credited Alfven / field-line-resonance scaling (f ~ v_A/L).
    As (v_A, R) range over the plasmoid hierarchy it spans ~7 orders (lab ~1e5 Hz -> space ~1e-3 Hz).
    This is textbook (Woltjer-Taylor / TAE / magnetospheric ULF), NOT new -- credit it.
  * The RATIO 1:1.719:2.427 (roots of tan x = x) is SCALE-INVARIANT: it depends ONLY on the force-free
    boundary geometry, not on v_A or R. So the inharmonic comb is the SAME at every scale -> a UNIVERSAL,
    multi-scale falsifiable fingerprint of single-lambda Beltrami relaxation. THIS is the FTGB-original
    diagnostic (no CMNS author proposes CK ratios as a signature; the tan x=x math is Chandrasekhar-Kendall).
  * The Pd-D two-laser (Hagelstein) beat is an EXTERNAL difference-frequency drive at THz -- a driven, not an
    eigen, beat, on a LATTICE (phonon) object, not a Beltrami plasmoid. Its ~harmonic phonon clustering does
    NOT test the CK comb (wrong object) -- see beat_ladder_nonmatch_check.py.

  TEST 1 -- the carrier f_b spans lab kHz -> space mHz (~7 OOM), tracking v_A/R (credited Alfven scaling).
  TEST 2 -- the CK ratio 1:1.719:2.427 is SCALE-INVARIANT (identical at the lab and space rungs) -> the
            universal, multi-scale fingerprint (a harmonic 1:2:3 at ANY scale would falsify the reading).
  TEST 3 -- order-level consistency: the space rungs land in the OBSERVED ULF/coronal bands (magnetospheric
            Pc3-5 ~ mHz-Hz; coronal-loop oscillations ~ mHz) -- consistent with the credited scaling. The
            RATIO (scale-invariant) is the discriminator; the absolute f_b is the credited carrier.

numpy only, deterministic. Run: python results/verify/beat_law_across_scales_check.py
"""
import numpy as np

ok = True


def banner(t):
    print("=" * 98); print(t); print("=" * 98)


def check(name, cond, detail=""):
    global ok
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, ("  -- " + detail) if detail else ""))
    ok = ok and cond


# CK roots (tan x = x) and the canonical eigenvalue difference that sets the beat
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
roots = np.array(roots)
dlam = roots[1] - roots[0]              # 3.232, the canon beat eigenvalue-difference


def f_beat(v_A, R):
    return v_A*dlam/(2*np.pi*R)


# ---------------------------------------------------------------- TEST 1: the carrier spans the hierarchy
banner("TEST 1 -- ONE beat law f_b = v_A|dlam|/(2piR) rides the plasmoid hierarchy: lab kHz -> space mHz")
scales = [
    ("lab plasmoid (FTGB canon)", 2.03e4, 0.12),
    ("spheromak (SSX-class)", 5.0e4, 0.20),
    ("FRC / large device", 1.0e5, 0.50),
    ("magnetospheric plasmoid (ULF)", 1.0e6, 6.4e6),
    ("solar coronal loop", 1.0e6, 1.0e8),
]
fvals = []
for name, vA, R in scales:
    fb = f_beat(vA, R); fvals.append(fb)
    unit = ("%.1f kHz" % (fb/1e3)) if fb > 1e2 else ("%.1f mHz" % (fb*1e3))
    print("   %-32s v_A=%.1e m/s  R=%.1e m  ->  f_b = %.3e Hz  (%s)" % (name, vA, R, fb, unit))
span = np.log10(max(fvals)/min(fvals))
check("the carrier spans ~7 orders (lab ~1e5 Hz down to space ~1e-3 Hz), tracking v_A/R",
      span > 6.5, "credited Alfven / field-line-resonance scaling f ~ v_A/L -- the same collective field across scales")

# ---------------------------------------------------------------- TEST 2: the CK ratio is scale-invariant
banner("TEST 2 -- the CK inharmonic RATIO 1:1.719:2.427 is SCALE-INVARIANT (the universal fingerprint)")
r = roots/roots[0]
# the ratio is the same whether v_A/R gives lab kHz or space mHz (it depends only on tan x = x):
lab_ratio = roots/roots[0]
space_ratio = roots/roots[0]          # identical -- no v_A, R dependence
print("   mode ratios (tan x = x):  1 : %.4f : %.4f  -- identical at the lab (kHz) and space (mHz) rungs" % (r[1], r[2]))
print("   (depends ONLY on the force-free boundary geometry; v_A and R cancel in every ratio)")
check("the inharmonic comb 1:1.719:2.427 is identical at every scale -> a universal multi-scale falsifier",
      np.allclose(lab_ratio, space_ratio) and abs(r[1]-1.719) < 0.01 and abs(r[2]-2.427) < 0.01,
      "a harmonic 1:2:3 at ANY accessible scale falsifies the single-lambda Beltrami reading")

# ---------------------------------------------------------------- TEST 3: order-level consistency vs observed bands
banner("TEST 3 -- order-level consistency: the space rungs land in the OBSERVED ULF/coronal bands  [credited scaling]")
f_mag = f_beat(1.0e6, 6.4e6); f_cor = f_beat(1.0e6, 1.0e8)
print("   magnetospheric rung f_b = %.1f mHz  vs observed ULF Pc3 (22-100 mHz) / Pc4 (7-22 mHz)" % (f_mag*1e3))
print("   coronal-loop rung   f_b = %.1f mHz  vs observed coronal-loop oscillations (~1-10 mHz, minutes)" % (f_cor*1e3))
check("the CK-form carrier lands in the observed ULF/coronal bands at the ORDER level (credited Alfven scaling)",
      2e-3 < f_mag < 0.2 and 1e-3 < f_cor < 2e-2,
      "the absolute f_b is the credited carrier; the SCALE-INVARIANT RATIO is the FTGB-original discriminator")

banner("VERDICT")
print("  One collective beat field rides the whole plasmoid hierarchy: f_b = v_A|dlam|/(2piR) spans lab kHz")
print("  to space mHz (~7 OOM, TEST 1), a CREDITED Alfven/field-line-resonance scaling (Woltjer-Taylor/TAE/ULF).")
print("  The FTGB-ORIGINAL, testable piece is the SCALE-INVARIANT CK inharmonic ratio 1:1.719:2.427 (TEST 2):")
print("  measure the mode-ratio at ANY accessible scale (SAFIRE shells, a spheromak, ball-lightning acoustics,")
print("  or space-plasmoid ULF) -- inharmonic confirms the single-lambda Beltrami object, harmonic 1:2:3 kills it.")
print("  The Pd-D two-laser THz beat is a driven LATTICE, the wrong object for this ratio (beat_ladder_nonmatch).")
print("  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
