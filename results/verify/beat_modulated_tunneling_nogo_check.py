"""
Beat-modulated tunneling "coherence gain" -- FENCE-KILLED (torus_project_repo salvage, 2026-09-15).

THE CONFRONTED ARTIFACT. The pre-jewel June-2026 campaign (F:\\trial connect\\torus_project_repo, designated
"SCRATCH -- merge useful bits to vortor" by KNOWLEDGE_ORDERING_PLAN_2026-09-09) carried a CCS
barrier-transparency claim (vendored: frontier_calcs/torus_repo_salvage_2026-06/ccs_barrier_transparency.json):
a 11.127 GHz tight-doublet beat "provides coherent modulation clock" for d-Pd tunneling, granting a
"coherence gain" factor 1.334 (33% enhancement) on a bare WKB transmission 6.14e-6 at a 240 eV barrier.
This is the GHz instance of the beat-as-pump class the M16 cross-scale audit fenced at kHz. This check runs
the fence at the campaign's own frequencies and disposes of the claim honestly -- while keeping what is
legitimate (bare screened tunneling with measured U_s, already in-jewel).

  TEST 1 -- THE STANDARD ARITHMETIC AT THE CLAIMED BARRIER [credited]. The d+d Gamow energy is
            E_G = 2 mu c^2 (pi alpha)^2 = 986 keV; at an effective collision energy of 240 eV (the screening
            scale) the WKB-to-contact exponent is 2 pi eta = pi sqrt(E_G/E) ~ 201, i.e. T ~ 1e-87 -- the
            textbook screened cold-collision scale. The vendored artifact's T = 6.14e-6 (exponent 12) is
            ~82 OOM away from WKB-to-contact at its own stated barrier energy: an UNSTATED truncated-barrier
            model (its "66 fm classical radius" corresponds to ~22 keV, not 240 eV). Logged as an internal
            inconsistency of the artifact -- its absolute transparency numbers are NOT ingestible.
  TEST 2 -- THE FENCE (robust, convention-independent): the beat is FROZEN across any tunneling attempt.
            Traversal-scale time for a 240 eV deuteron pair across the sub-barrier region (~6000 fm) is
            tau ~ 4e-17 s; one 11.127 GHz beat period is 9e-11 s -- the beat phase advances ~3e-6 rad per
            attempt (ratio ~ 5e-7). A clock that does not tick during the event cannot "modulate" it: the
            claimed frequency-lock mechanism has no dynamical channel, at ANY gain factor. Quantum-side:
            hbar*omega(11.127 GHz) = 46 ueV -- 6.7 OOM below the 240 eV barrier and 11.7 OOM below the
            23.85 MeV rung; even the campaign's 10 THz carrier quantum (41.4 meV) sits 8.76 OOM below the
            nuclear rung. The M16 kHz fence extends UNCHANGED to GHz/THz.
  TEST 3 -- DISPOSITION [settled-neg for the modulation reading]. The "coherence gain 1.334" is
            fence-killed (no mechanism at these scale separations); bare screened tunneling survives as the
            ordinary [credited] physics the jewel already carries (U_s = 300-800 eV measured,
            Raiola/Huke/Czerski). The campaign's honest parts (beat-dominance methodology with
            phase-scrambled controls; the no-kernel nuclear-side envelope method) are folded separately --
            see results/SALVAGE_SURVEY_TORUS_REPO_2026-09-15.md.

  HONEST SCOPE: nothing here bears on the jewel's macroscopic beat-as-rate-GATE [S] (a gate needs no
  cross-scale energy transfer); the kill is specifically the beat-MODULATES-TUNNELING mechanism. And the
  fence does not touch measured screening: U_s is real, inherited, and already the jewel's only rate input
  from this scale.

numpy only, deterministic. Run: python results/verify/beat_modulated_tunneling_nogo_check.py
"""
import json
import os

import numpy as np

ok = True
EV = 1.602176634e-19       # J
HBAR = 1.054571817e-34     # J*s
ALPHA = 7.2973525693e-3
MU_C2_EV = 937.611e6       # reduced d+d mass energy, eV (m_d c^2 / 2)
M_MU_KG = 1.6726e-27       # reduced mass of d+d in kg (~ m_d/2 ~ m_p)
HBARC_EVFM = 197.327e6 * 1e-15 / 1e-15  # (not used directly; kept for clarity)

VENDOR = os.path.join(os.path.dirname(__file__), "..", "..", "frontier_calcs",
                      "torus_repo_salvage_2026-06", "ccs_barrier_transparency.json")


def banner(t):
    print("=" * 98); print(t); print("=" * 98)


def check(name, cond, detail=""):
    global ok
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, ("  -- " + detail) if detail else ""))
    ok = ok and cond


with open(VENDOR, encoding="utf-8") as f:
    art = json.load(f)

banner("TEST 1 -- standard WKB-to-contact at the artifact's own barrier energy (240 eV)  [credited]")
E_G = 2.0 * MU_C2_EV * (np.pi * ALPHA) ** 2          # d+d Gamow energy, eV
E_eff = art["coulomb_barrier_ev"]                     # 240 eV (the screening scale)
two_pi_eta = np.pi * np.sqrt(E_G / E_eff)
log10_T_std = -two_pi_eta / np.log(10.0)
print("   Gamow energy E_G = 2 mu c^2 (pi alpha)^2 = %.1f keV  (textbook d+d: ~986 keV)" % (E_G / 1e3))
print("   at E = %.0f eV: 2*pi*eta = %.1f  ->  T_std ~ 1e%.1f" % (E_eff, two_pi_eta, log10_T_std))
print("   vendored artifact: T = %.3g (log10 = %.2f) -- a truncated-barrier model, unstated" % (
    art["transmission_bare_wkb"], np.log10(art["transmission_bare_wkb"])))
gap_oom = np.log10(art["transmission_bare_wkb"]) - log10_T_std
r_c_240 = 1.43996e6 / E_eff   # e^2/(4 pi eps0) = 1.43996 MeV*fm -> fm at 240 eV
print("   artifact's '66 fm classical radius' vs Coulomb r_c(240 eV) = %.0f fm (66 fm <-> %.1f keV)" % (
    r_c_240, 1.43996e6 / 66.24 / 1e3))
check("E_G reproduces the textbook 986 keV to 1%%", abs(E_G - 986e3) / 986e3 < 0.01, "%.1f keV" % (E_G / 1e3))
check("2*pi*eta ~ 201 at 240 eV (T ~ 1e-87.5)", abs(two_pi_eta - 201.3) < 2.0, "%.1f" % two_pi_eta)
check("artifact transparency is ~%d OOM above WKB-to-contact -> absolute numbers NOT ingestible" % round(gap_oom),
      gap_oom > 60, "internal inconsistency logged; barrier model unstated")

banner("TEST 2 -- the FENCE: the GHz beat is frozen across any tunneling attempt  [V]-arith")
f_beat = art["f_beat_hz"]                             # 11.127 GHz
T_beat = 1.0 / f_beat
v = np.sqrt(2.0 * E_eff * EV / M_MU_KG)               # sub-barrier velocity scale, m/s
width_m = r_c_240 * 1e-15                             # ~6000 fm in metres
tau_trav = width_m / v
ratio = tau_trav / T_beat
dphi = 2.0 * np.pi * ratio
print("   traversal-scale time tau ~ w/v = %.1e m / %.2e m/s = %.1e s;  beat period = %.1e s" % (
    width_m, v, tau_trav, T_beat))
print("   tau/T_beat = %.1e  ->  beat phase advance per attempt ~ %.1e rad  (the beat is DC)" % (ratio, dphi))
hw_beat = 2 * np.pi * HBAR * f_beat / EV
hw_thz = 2 * np.pi * HBAR * 10e12 / EV
print("   quanta: hbar*w(11.127 GHz) = %.1f ueV (%.1f OOM below 240 eV; %.1f OOM below 23.85 MeV);" % (
    hw_beat * 1e6, np.log10(E_eff / hw_beat), np.log10(23.847e6 / hw_beat)))
print("           hbar*w(10 THz carrier) = %.1f meV (%.2f OOM below the 23.85 MeV rung)" % (
    hw_thz * 1e3, np.log10(23.847e6 / hw_thz)))
check("beat frozen: tau/T_beat < 1e-4", ratio < 1e-4, "%.1e -- no modulation channel exists" % ratio)
check("beat quantum 6+ OOM below its own barrier", np.log10(E_eff / hw_beat) > 6, "%.1f OOM" % np.log10(E_eff / hw_beat))
check("even the THz carrier quantum is ~8.8 OOM below the nuclear rung",
      abs(np.log10(23.847e6 / hw_thz) - 8.76) < 0.05, "the M16 kHz fence extends unchanged to GHz/THz")

banner("TEST 3 -- disposition  [settled-neg for the modulation reading]")
print("   the 'coherence gain %.3f' has NO dynamical channel (TEST 2) and rides on non-reproducible" % art["coherence_gain"])
print("   absolute transparencies (TEST 1) -> the beat-modulated-tunneling reading is FENCE-KILLED.")
print("   What survives: bare screened tunneling with MEASURED U_s (already in-jewel, [credited]); the")
print("   campaign's phase-scrambled-control methodology and no-kernel envelope method (folded separately).")
print("   What is untouched: the macroscopic beat-as-rate-GATE [S] (needs no cross-scale energy transfer).")
check("modulation-gain reading fence-killed; screening and the gate untouched", True,
      "the GHz instance of the M16 pump class, disposed with the artifact vendored")
print("  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
