"""
FRONTIER TEST (contested data): do measured microtubule resonances form the CK comb 1:1.719:2.427?

Tests prediction #1 of the [speculative frontier] doc SPECULATIVE_FRONTIER_MICROTUBULE_HOLOGRAPHY:
if microtubules were single-cavity CK/Beltrami resonators, their first resonances should sit at the
INHARMONIC comb (roots of tan x = x): 1 : 1.719 : 2.427 : 3.130 ..., NOT harmonic 1:2:3. This runs the
comparison against the published (contested) Sahu/Bandyopadhyay single-microtubule AC-resonance peaks and
LOGS the outcome honestly. Tier: [speculative frontier / contested external data] -- NOT a [V] claim;
this is a hypothesis-test, computed and logged (check-record-learn), not a verified result.

Data source (claims-as-read, contested): Sahu, Ghosh, Bandyopadhyay et al., single-microtubule AC
resonance peaks reported at ~9, 22, 113, 228 MHz; the fuller spectrum is described by the authors as
"fractal, scale-free" spanning kHz-MHz-GHz-THz (MDPI Fractals 4(2):11, 2020; DTIC ADA597480). Only the
four MHz peaks above were reliably extracted for this pass -> provenance-limited [flag].
Run: python results/verify/microtubule_ck_comb_test.py
"""
import numpy as np

# published microtubule MHz resonance peaks (claims-as-read; provenance-limited)
peaks = np.array([9.0, 22.0, 113.0, 228.0])   # MHz
CK = np.array([1.0, 1.719, 2.427, 3.130, 3.832, 4.534])   # roots of tan x = x, normalized

def banner(t): print("="*78); print(t); print("="*78)

banner("1) the CK-comb prediction vs the reported peaks")
print("  CK comb (tan x = x), ratios to fundamental: %s" % np.array2string(CK, precision=3))
print("  reported microtubule peaks (MHz): %s" % peaks.tolist())
r = peaks/peaks[0]
print("  peak ratios to first (9 MHz):     %s" % np.array2string(r, precision=3))
adj = peaks[1:]/peaks[:-1]
print("  adjacent ratios:                  %s" % np.array2string(adj, precision=3))

banner("2) does any consistent comb fit? (CK vs harmonic)")
# compare each peak-ratio to nearest CK entry and nearest integer (harmonic)
print("  ratio    nearest-CK  dev%%    nearest-int  dev%%")
mixed = False
for rr in r[1:]:
    ck_near = CK[np.argmin(np.abs(CK-rr))]; ck_dev = abs(rr-ck_near)/ck_near*100
    int_near = round(rr); int_dev = abs(rr-int_near)/int_near*100 if int_near else 99
    print("  %6.3f   %8.3f  %5.1f   %8d   %5.1f" % (rr, ck_near, ck_dev, int_near, int_dev))
# the ratios 2.44, 12.6, 25.3 -- huge gaps -> NOT one CK cavity comb
print("  -> the ratios (2.44, 12.6, 25.3) have huge gaps: these span SUB-BANDS, not one cavity comb.")
print("     22/9=2.44 is a lone near-miss to CK's 2.427 (0.7%%) but the OTHER ratios (5.14, 2.02) don't")
print("     line up -> no CONSISTENT CK comb. Prediction #1 (single CK comb) is NOT supported by this data.")

banner("3) the authors' own characterization: FRACTAL / SCALE-FREE -> the theory's N^L cascade, not the CK comb")
print("  Sahu/Bandyopadhyay describe the microtubule spectrum as 'fractal, scale-free' across kHz..THz")
print("  (self-similar bands), NOT a single inharmonic cavity comb. That maps onto FTGB's *cascade* layer")
print("  (N^L 'fractal-toroidal-beat', M14 Greenyer) -- a DIFFERENT structure from the single-cavity CK comb.")
print("  REFINED hypothesis (the real testable one): are the microtubule BANDS spaced by a cascade base")
print("  N (golden phi or N=4)?  Needs the full multi-band peak list (not reliably extracted here) [flag].")
band_span = peaks[-1]/peaks[0]
print("  within-band (MHz) span 9->228 = %.1fx ; ln(span)/ln(phi)=%.2f (not a clean integer) -- inconclusive"
      % (band_span, np.log(band_span)/np.log((1+np.sqrt(5))/2)))

banner("VERDICT (logged as a clue, [speculative frontier / contested data])")
print("  Prediction #1 CK-comb (1:1.719:2.427) is NOT borne out by the four reported microtubule MHz peaks")
print("  (mixed ratios; one generic near-miss). The authors' own 'fractal/scale-free' characterization")
print("  points instead to the theory's N^L CASCADE layer, not the single CK comb -- a refined, still-open")
print("  hypothesis needing the full multi-band peak list. Honest outcome: the sharpest microtubule")
print("  prediction, when tested against available data, does NOT confirm and REDIRECTS to the cascade.")
print("  This is a computed, logged frontier-check -- NOT a [V] result, NOT a refutation of the theory")
print("  (whose [V] core is scale-independent), and the data is contested + provenance-limited.")
print("done.")
raise SystemExit(0)
