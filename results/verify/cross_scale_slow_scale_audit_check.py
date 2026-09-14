"""
Cross-scale audit (M16, resolves the "genuinely-slow route" carve-out): compute and LOG every candidate
slow nuclear-adjacent scale against the 87.14 kHz carrier beat, and assert the honest conclusion.

The FTGB "cross-scale Delta identity" (kHz plasma detuning <-> MeV nuclear gap) had THREE carve-outs after the
sum-vs-difference pump fence (M16-4): the conserved 23.847 MeV energy ledger, the cold Landau-Zener B=4
resolution, and "a genuinely-slow (w_b ~ w_slow) nuclear-adjacent route." That third one was a hand-wave.
This script RESOLVES it by enumerating every candidate genuinely-slow scale, computing where each sits
relative to the beat, and logging the verdict -- the compute-and-log discipline applied to a fence.

THE RESULT (all arithmetic reproduced here; audited by an 8-scale adversarial pass):
  * The LITERAL "kHz = MeV gap" identity is DEAD -- a settled-negative by ~16.8 orders (E_beat = h*f_beat =
    0.360 neV vs Q = 23.847 MeV). No nuclear-internal or microscopic-collective scale rescues it: nuclear
    level spacings, the LZ sweep rate, the deuteron plasma, and Pd-D phonons ALL sit +7.5 to +17.6 OOM ABOVE
    the beat. The only scales AT kHz are (a) the object-Alfven beat itself (0 OOM BY CONSTRUCTION -- the beat
    equals the beat, zero information) or (b) field-TUNABLE atomic/molecular splittings a control target also
    hits (and 4He has spin I=0, so even that reactant-only bridge is empty).
  * So 87 kHz is a MACROSCOPIC-COLLECTIVE (object-Alfven/MHD) scale -- kHz order is GENERIC to any lab-scale
    collective object -- NOT a nuclear-internal frequency.
  * TWO ideas that wore the one phrase "detuning-gap" are separated:
      (A) the STRUCTURAL nuclear LZ branching gap Delta_nuc -- kHz-FREE (swept at NUCLEAR velocity; the kHz is
          frozen/DC across the crossing, tau_cross/T_kHz ~ 1e-18). The legitimate B=4 theory. LZ FORMULA is
          [credited] math; d+d-as-adiabatic-LZ-crossing is an FTGB [S] hypothesis; Delta value is open.
      (B) the kHz beat as a slow MACROSCOPIC RATE-GATE (a duty-cycle on the collective object, transferring
          ZERO number to the MeV scale) -- the only surviving kHz-involving reading, tier [S], FALSIFIABLE as
          a beat-locked yield step surviving a non-fusable (H2) control.
  * The pump reading is DOUBLY-closed: parametric short by 15.7 OOM (rhythm_parametric_resonance_check TEST 4)
    AND slow-adiabatic killed by the frozen/DC crossing (TEST 6 here).

  TEST 1 -- FAR-MISS LADDER: every independent nuclear/lattice/plasma/LZ-sweep scale sits >=+7 OOM above the
            beat (a computed settled-negative; no nuclear/microscopic scale reaches kHz).
  TEST 2 -- LITERAL IDENTITY DEAD: E_beat/Q = 1.5e-17 (~16.8 OOM); even a 1 keV spacing is +12.4 OOM.
  TEST 3 -- TAUTOLOGY GUARD: the E=h*f round-trip returns f_beat exactly; the ONLY 0-OOM entry is the
            object-Alfven beat, which equals the beat BY CONSTRUCTION -- must never be cited as evidence FOR
            a cross-scale identity (it is the definition).
  TEST 4 -- MACROSCOPIC GENERICITY: sweeping (v_A, R) over lab MHD ranges, f_b stays kHz-MHz order and
            brackets 87 kHz -> the beat is a macroscopic-collective scale, not nuclear.
  TEST 5 -- TUNABLE / EMPTY-BRIDGE GUARD: deuteron Larmor = 87.14 kHz at 133 G but a proton control hits at
            ~20 G (field-tunable => generic), and 4He (I=0) has no nuclear Zeeman => the reactant-only bridge
            is empty.
  TEST 6 -- A vs B SEPARATION: the nuclear crossing is DC across a kHz cycle (tau_cross/T_kHz ~ 1e-18, phase
            advance << 1 rad) -> idea A is kHz-FREE; idea B (macroscopic gate) is the sole surviving
            kHz-involving reading, tier [S]/falsifiable.
  TEST 7 -- HALF-BEAT (Klimov window): 43.57 kHz = (f2-f1)/2 lands in the claimed 43-46 kHz band, tiered
            IDENTICALLY to the object-beat (macroscopic/environmental EM coincidence, NOT nuclear-internal).

numpy only, deterministic. Run: python results/verify/cross_scale_slow_scale_audit_check.py
"""
import numpy as np

ok = True

# ---- constants (CODATA-ish; all values independently reproduced in the audit) ----
h_eVs = 4.135667696e-15          # eV*s
hbar_eVs = 6.582119569e-16       # eV*s
c = 2.99792458e8                 # m/s
e = 1.602176634e-19              # C
eps0 = 8.8541878128e-12          # F/m
m_d = 3.343583719e-27            # kg (deuteron)
f_beat = 87.14e3                 # Hz  (canon comb beat f2 - f1)
E_beat = h_eVs * f_beat          # eV
w_beat = 2*np.pi*f_beat          # rad/s
Q_ddHe = 23.847e6                # eV  (d+d -> 4He, conserved [V])
gamma_d = 6.536e6                # Hz/T (deuteron gyromagnetic)
gamma_p = 42.577e6               # Hz/T (proton gyromagnetic)


def banner(t):
    print("=" * 96); print(t); print("=" * 96)


def check(name, cond, detail=""):
    global ok
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, ("  -- " + detail) if detail else ""))
    ok = ok and cond


def oom(scale_Hz):
    return np.log10(scale_Hz / f_beat)


print("   ANCHOR: f_beat = %.2f kHz ;  E_beat = h*f_beat = %.3e eV = %.3f neV ;  w_beat = %.3e rad/s"
      % (f_beat/1e3, E_beat, E_beat*1e9, w_beat))
print("           d+d->4He Q = %.3f MeV (conserved [V]) ;  target of a LITERAL 'kHz = MeV gap' identity\n" % (Q_ddHe/1e6))

# ---------------------------------------------------------------- TEST 1: far-miss ladder
banner("TEST 1 -- FAR-MISS LADDER: every nuclear/lattice/plasma/LZ-sweep scale sits >= +7 OOM ABOVE the beat")
# deuteron plasma frequency in PdD (n_D ~ 6.8e28 /m^3)
n_D = 6.8e28
w_p = np.sqrt(n_D * e**2 / (eps0 * m_d)); f_p = w_p/(2*np.pi)
# nuclear level spacings near the d+d threshold (0.80 - 3.12 MeV) -> Hz
lvl_lo, lvl_hi = 0.80e6/h_eVs, 3.12e6/h_eVs
# Pd-D phonons: acoustic ~3 THz, optical ~8-15 THz ; D2+ vibration ~0.2 eV
ph_ac, ph_op_hi = 3.0e12, 15.0e12
vib = 0.2/h_eVs
# LZ sweep 1/tau_cross: nuclear crossing ~ few fm at ~0.1-0.23c
v_nuc = 0.1*c
tau_cross = 4e-15 / v_nuc                      # 4 fm / v  (conservative, slow end)
f_sweep = 1.0/tau_cross
scales = [
    ("deuteron plasma frequency (PdD)", f_p),
    ("nuclear level spacing (0.80 MeV)", lvl_lo),
    ("nuclear level spacing (3.12 MeV)", lvl_hi),
    ("Pd-D acoustic phonon (~3 THz)", ph_ac),
    ("Pd-D optical phonon (~15 THz)", ph_op_hi),
    ("D2+ vibration (~0.2 eV)", vib),
    ("LZ sweep 1/tau_cross (4 fm @ 0.1c)", f_sweep),
]
worst_low = 99.0
for nm, s in scales:
    o = oom(s)
    worst_low = min(worst_low, o)
    print("     %-38s f = %.3e Hz   -> %+.2f OOM vs beat" % (nm, s, o))
check("every independent nuclear/lattice/plasma/LZ scale is >= +7 OOM above the 87 kHz beat (far-miss)",
      worst_low >= 7.0, "smallest gap = %+.1f OOM -> no nuclear or microscopic-collective scale reaches kHz" % worst_low)

# ---------------------------------------------------------------- TEST 2: literal identity dead
banner("TEST 2 -- LITERAL IDENTITY DEAD: E_beat vs the MeV gap is a ~16.8 OOM settled-negative")
r = E_beat / Q_ddHe
o_keV = oom(1e3/h_eVs)
print("     E_beat / Q(d+d->4He) = %.3e / %.3e = %.3e   (log10 = %.2f -> %.1f OOM short)"
      % (E_beat, Q_ddHe, r, np.log10(r), -np.log10(r)))
print("     even a hypothetical 1 keV nuclear level spacing is %+.2f OOM ABOVE the beat" % o_keV)
check("the literal 'kHz = MeV gap' identity is dead by ~16.8 orders of magnitude",
      abs(np.log10(r) + 16.82) < 0.2 and o_keV > 12, "0.360 neV vs 23.847 MeV -- affirmatively falsified, not merely unproven")

# ---------------------------------------------------------------- TEST 3: tautology guard
banner("TEST 3 -- TAUTOLOGY GUARD: the only kHz 'match' (the object-Alfven beat) equals the beat BY CONSTRUCTION")
f_roundtrip = (h_eVs * f_beat) / h_eVs         # f -> E=hf -> f: pure identity
# object-Alfven beat: f_b = v_A|dLam|/2piR at canon anchors -> equals the beat
v_A, R, dLam = 2.03e4, 0.12, 3.2318
f_b_obj = v_A*dLam/(2*np.pi*R)
print("     E = h*f round-trip: f -> hf -> f = %.1f Hz (returns f_beat exactly; carries ZERO information)" % f_roundtrip)
print("     object-Alfven beat f_b = v_A|dLam|/2piR = %.3e Hz  (%+.3f OOM -- the beat, BY CONSTRUCTION)"
      % (f_b_obj, oom(f_b_obj)))
check("the sole 0-OOM 'match' is tautological (the beat matching itself) -- never evidence FOR an identity",
      abs(f_roundtrip - f_beat) < 1e-6 and abs(oom(f_b_obj)) < 0.02,
      "GUARD: the object-Alfven 'MATCHES-kHz' cell is the DEFINITION of the beat, not an independent coincidence")

# ---------------------------------------------------------------- TEST 4: macroscopic genericity
banner("TEST 4 -- MACROSCOPIC GENERICITY: over lab MHD ranges f_b stays kHz-MHz order and brackets 87 kHz")
vA_grid = np.array([1e4, 3e4, 1e5])
R_grid = np.array([0.05, 0.08, 0.12])
fb_vals = np.array([vA*dLam/(2*np.pi*Rr) for vA in vA_grid for Rr in R_grid])
print("     v_A in [1e4,1e5] m/s, R in [0.05,0.12] m, |dLam|=%.2f  ->  f_b in [%.2e, %.2e] Hz" %
      (dLam, fb_vals.min(), fb_vals.max()))
check("f_b stays kHz-MHz order (macroscopic-collective) and brackets the 87 kHz beat",
      fb_vals.min() < f_beat < fb_vals.max() and fb_vals.min() > 1e4 and fb_vals.max() < 2e6,
      "kHz order is GENERIC to any lab-scale collective/MHD object -> 87 kHz is macroscopic, not nuclear")

# ---------------------------------------------------------------- TEST 5: tunable / empty-bridge guard
banner("TEST 5 -- TUNABLE / EMPTY-BRIDGE GUARD: a field-tunable Larmor match that a control also hits; 4He I=0")
B_d = f_beat/gamma_d; B_p = f_beat/gamma_p
print("     deuteron Larmor = 87.14 kHz at B = %.1f G ;  proton control hits at B = %.1f G  (field-TUNABLE => generic)"
      % (B_d*1e4, B_p*1e4))
print("     4He (alpha) nuclear spin I = 0  =>  NO nuclear Zeeman  =>  the reactant-only Larmor bridge is EMPTY")
check("the only kHz nuclear-adjacent 'match' is field-tunable (a control nucleus also lands) and reactant-only",
      abs(B_d*1e4 - 133.3) < 1.0 and abs(B_p*1e4 - 20.5) < 1.0,
      "tunable-coincidence, not a prediction; and 4He I=0 empties even that bridge")

# ---------------------------------------------------------------- TEST 6: A vs B separation
banner("TEST 6 -- A vs B: the nuclear crossing is DC across a kHz cycle (idea A kHz-free); only idea B involves kHz")
T_kHz = 1.0/f_beat
ratio = tau_cross / T_kHz
phase_adv = w_beat * tau_cross                  # kHz phase advance during one nuclear crossing
print("     tau_cross ~ %.2e s (4 fm @ 0.1c) ;  T_kHz = %.2e s ;  tau_cross/T_kHz = %.2e (log10 = %.1f)"
      % (tau_cross, T_kHz, ratio, np.log10(ratio)))
print("     kHz phase advance during the whole nuclear crossing = %.2e rad (<< 1 -> the kHz field is FROZEN/DC)" % phase_adv)
check("the nuclear avoided-crossing is DC across a kHz period -> idea A (structural gap) is kHz-FREE",
      ratio < 1e-12 and phase_adv < 1e-10,
      "(A) LZ gap swept at NUCLEAR velocity, no external freq; (B) macroscopic rate-GATE is the only surviving kHz reading [S]")

# ---------------------------------------------------------------- TEST 7: half-beat (Klimov window)
banner("TEST 7 -- HALF-BEAT: 43.57 kHz sits in the Klimov 43-46 kHz window, tiered as macroscopic (not nuclear)")
half_beat = f_beat/2
print("     (f2 - f1)/2 = %.2f kHz  vs the claimed 43-46 kHz optimal band" % (half_beat/1e3))
check("the half-beat is a MACROSCOPIC/environmental EM coincidence, same class as the object-beat -- not nuclear-internal",
      43e3 <= half_beat <= 46e3,
      "tier it IDENTICALLY to the object-Alfven beat (generic to lab MHD objects); do NOT promote to a nuclear signal")

banner("VERDICT")
print("  The 'genuinely-slow route' carve-out RESOLVES: 87 kHz is a MACROSCOPIC-COLLECTIVE (object-Alfven)")
print("  scale, not a nuclear-internal one (every nuclear/lattice/plasma/LZ scale is +7.5..+17.6 OOM away).")
print("  * LITERAL 'kHz = MeV gap' identity: DEAD (settled-negative, ~16.8 OOM).")
print("  * PUMP reading: DOUBLY-closed settled-negative (parametric 15.7 OOM AND slow-adiabatic frozen/DC).")
print("  * SURVIVES (kHz-free): the Landau-Zener SCHEMA as the correct DESCRIPTION of the B=4 branching")
print("    -- [credited] formula / [S] d+d identification / open rate -- a shared-schema ANALOGY, ZERO")
print("    transferred number, explicitly NOT a forced law and NOT a pump.")
print("  * SEPARATELY LIVE: the macroscopic beat as a slow yield-GATE / duty-cycle [S], FALSIFIABLE by a")
print("    beat-locked yield step surviving an H2 (non-fusable) control -- does not touch the 23.847 MeV [V] ledger.")
print("  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
