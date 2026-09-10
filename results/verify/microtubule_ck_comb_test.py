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

banner("4) REFINED cascade test: do the bands scale by the FTGB base N (golden phi or 4)?")
phi = (1+np.sqrt(5))/2
# reported band structure (Ghosh/Sahu/Bandyopadhyay 2020): resonance bands at 1-40 Hz, 1-40 kHz,
# 1-40 MHz, 1-40 GHz -> band-to-band spacing = x1000 (decades); within each band a "triplet-of-triplet"
# with "equally spaced" (ARITHMETIC) sub-peaks; self-similar across ~12 orders of magnitude.
band_ratio = 1000.0
print("  reported band-to-band spacing (Hz->kHz->MHz->GHz) = x%.0f (decades)" % band_ratio)
print("  FTGB cascade base candidates: N=phi=%.4f, N=4. Does x1000 = N^k for integer k?" % phi)
print("     log_phi(1000) = %.2f  (not integer -> NOT a golden cascade step)" % (np.log(band_ratio)/np.log(phi)))
print("     log_4(1000)   = %.2f  (4^5=1024 is 2.4%% off 1000 -> fails the 0.5%% gate; and 1000=10^3 is a" %
      (np.log(band_ratio)/np.log(4)))
print("                    DECADE scan structure, not a power of 4) -> NOT a Nardi cascade step either")
print("  within-band sub-peaks are reported EQUALLY SPACED (arithmetic) -> neither CK-inharmonic nor phi/4-geometric")
print("  -> the microtubule spectrum is a DECADE-self-similar triplet-of-triplet: its OWN organizing")
print("     principle, matching neither the CK comb (sec.2) nor the FTGB phi/4 cascade base.")

banner("5) the triplet-of-triplet is 1:3:9 (base N=3) + the GML/FIT method IS FTGB's comb-lock")
N_mt = 3.0   # Bandyopadhyay GML: triplet-of-triplet = 1:3:9(:27), an integer/geometric cascade base 3
for base, name in [(phi,"phi (golden)"), (4.0,"4 (Nardi)"), (2.718281828,"e")]:
    print("  microtubule cascade base N=3  vs  FTGB base %-12s: %s" %
          (name, "MATCH" if abs(N_mt-base)/base < 0.005 else "no (%.1f%% off)" % (abs(N_mt-base)/base*100)))
print("  -> N=3 is a clean INTEGER cascade, distinct from CK-inharmonic and from the golden/4 FTGB bases.")
print("  M14 triad-dichotomy PREDICTION (Greenyer): phi (N^2=N+1) is the UNIQUE self-phase-matching base;")
print("  INTEGER bases (N=3) cannot phase-match (N^i - N^j != -1 mod N). So FTGB predicts the microtubule")
print("  1:3:9 is a DRIVEN/harmonic ternary hierarchy, NOT a self-organizing golden coherence -- testable.")
print("  METHOD CONVERGENCE (genuine, [S]): GML/FIT = multi-scale coupled oscillators with phase-locking")
print("  Psi = m*theta_i - n*theta_j on an N-torus. That IS FTGB's own dynamics layer -- engine.comb_lock")
print("  runs exactly this (Adler locks 7*th0-4*th1, 5*th0-2*th2; Arnold tongues). Same mathematics; the")
print("  frameworks converge at the phase-dynamics METHOD level even where the specific NUMBERS differ.")

banner("VERDICT (logged as a clue, [speculative frontier / contested data])")
print("  BOTH FTGB spectral signatures test NEGATIVE against the reported microtubule data:")
print("   (a) the single CK comb 1:1.719:2.427 (sec.2) -- mixed ratios, lone generic near-miss;")
print("   (b) the phi/4 cascade base (sec.4) -- bands scale by DECADES (x1000), within-band triplets")
print("       are ARITHMETIC ('equally spaced'), neither CK-inharmonic nor phi/4-geometric.")
print("  What DOES match is only the GENERAL PRINCIPLE: a self-similar, scale-free, near-field biological")
print("  resonance -- consistent with the theory's fractal-toroidal-beat idea at the level of KIND, not")
print("  NUMBER. The microtubule's own structure (decade-self-similar triplet-of-triplet) is a distinct")
print("  organizing principle -- a clean INTEGER cascade base N=3 (1:3:9), which FTGB's M14 triad-dichotomy")
print("  says CANNOT self-phase-match (only golden phi does) -> FTGB predicts it is driven/harmonic, testable.")
print("  THE GENUINE BRIDGE is at the METHOD level, not the numbers: GML/FIT (coupled oscillators + phase-")
print("  locking on an N-torus) IS FTGB's own dynamics layer (engine.comb_lock). Same mathematics.")
print("  Honest outcome: the specific-NUMBER predictions (CK comb, phi/4 base) do NOT confirm; the")
print("  phase-dynamics METHOD genuinely converges; the [V] core is scale-independent and untouched.")
print("  Computed, logged, contested-data frontier-check -- NOT [V], NOT a refutation. Remaining tests")
print("  (helicity/circular-dichroism, near-field 1/r falloff) need lab measurements, not available here.")
print("done.")
raise SystemExit(0)
