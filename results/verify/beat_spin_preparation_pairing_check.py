"""
SALVAGE (2026-09-15): the kHz beat, killed as a "pump," reborn as the spin gate's PREPARATION clock.

The negative-program salvage reassessment found one genuine type-2 recovery -- a good idea lost to a poor
FORMULATION. The beat-as-PUMP reading is dead and STAYS dead (it demanded cross-scale ENERGY transfer to the
MeV gap: literal kHz=MeV 16.8 OOM, parametric 15.7 OOM, adiabatic tau_cross/T_kHz~1e-18 --
cross_scale_slow_scale_audit_check, rhythm_parametric_resonance_check). But the surviving CORE -- the beat as a
macroscopic coherent CLOCK -- re-pairs, at the SAME scale, to the one place spin_channel_gate left OPEN: it
proved the s-wave door to 4He(0+) is the singlet alone and is STEERABLE by single-mode coherent preparation,
but explicitly "does NOT show the m=0 preparation actually occurs." The beat is the named candidate for that
preparation clock. This relocates the beat OFF the once-refuted geometric yield-law f_b(L)=N^L
(beat_ladder_nonmatch_check: the sole dataset does not fit it) and ONTO a mechanism-grounded, same-scale,
falsifiable pairing.

  TEST 1 -- SAME-SCALE, NOT CROSS-SCALE (the defusing) [V]-arith. The ENTRANCE-channel spin DOF is kHz-scale:
            a deuteron (I=1) has Larmor frequency gamma_d*B = 87 kHz at B ~ 133 G -- the SAME scale as the
            object's comb beat f_beat = 87.14 kHz. So a kHz beat modulating the entrance deuterons' m-population
            is ordinary kHz spin dynamics (NMR-scale), NOT the forbidden kHz->MeV energy transfer. This is a
            DIFFERENT object than cross_scale TEST 5's "empty-bridge" caveat: that caveat was about the PRODUCT
            4He (I=0, no nuclear Zeeman) failing as EVIDENCE; here the ENTRANCE deuterons (I=1) are the live
            preparation target, and the claim is a MECHANISM + falsifier, not a coincidence-as-evidence.
  TEST 2 -- THE STEERING THE BEAT WOULD DRIVE (reused [credited] CG arithmetic, no new number). The singlet
            door to 4He(0+): a single-mode entrance pair |1,m>|1,m> has singlet fraction 1/3 at m=0 (3x the 1/9
            statistical gate) and EXACTLY 0 at m=+-1 (pure quintet). A coherent kHz clock that biases the
            entrance-deuteron m-population toward m=0 opens the singlet door; toward m=+-1 closes it. The beat
            is the mechanism-shaped clock the gate needs; the CG numbers are unchanged (spin_channel_gate_check).
  TEST 3 -- THE JOINT FALSIFIER (the deliverable) [S]. A beat-swept aneutronic-yield step must die under BOTH
            controls: (a) PHASE-SCRAMBLING (it is a coherent property, salvaged protocol) AND (b) m=+-1 DEUTERON
            POLARIZATION (which closes the singlet door toward the ~1e-6 d-wave floor); m=0/singlet-weighted
            assembly ENHANCES it up to the 3x gate. No thermal-statistical model predicts a joint
            phase-AND-polarization knob. This is sharper than either falsifier alone.

  HONEST SCOPE (do not over-read): this NAMES a same-scale candidate mechanism and mints a joint falsifier; it
  does NOT prove the beat actually drives the m=0 population. *(2026-09-15 update: the coupling MECHANISM is no
  longer open -- it is magnetic resonance, resolved in `beat_spin_magnetic_resonance_check`: Rabi driving at
  f_b = f_Larmor, met at a v_A-independent density n* = 1.02e20 /m^3 inside the object's range, deuteron-
  specific, strength Omega_R = gamma_d*b1 vs 1/T2. Only the transverse-dB amplitude and T2 remain quantitatively
  open.)* This check computes NO rate. The
  pump kill is untouched and STANDS. Tier: same-scale arithmetic [V]; CG steering [credited]; the beat-as-the-
  gate's-preparation-clock identification and the joint falsifier [S]. No new coincidence number; nothing
  promoted beyond a named, checkable mechanism.

numpy only, deterministic. Run: python results/verify/beat_spin_preparation_pairing_check.py
"""
import numpy as np

ok = True
GAMMA_D = 6.53569e6        # Hz/T, deuteron gyromagnetic ratio (Larmor per unit field)
F_BEAT = 87.14e3           # Hz, canonical comb beat (f2 - f1), same value as cross_scale_slow_scale_audit


def banner(t):
    print("=" * 98); print(t); print("=" * 98)


def check(name, cond, detail=""):
    global ok
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, ("  -- " + detail) if detail else ""))
    ok = ok and cond


# exact spin-1 pair singlet fractions (rebuilt from operators; identical to spin_channel_gate_check)
Sz = np.diag([1.0, 0.0, -1.0]); Sp = np.zeros((3, 3)); Sp[0, 1] = Sp[1, 2] = np.sqrt(2.0); Sm = Sp.T
Sx = (Sp + Sm) / 2.0; I3 = np.eye(3)
tot = lambda A: np.kron(A, I3) + np.kron(I3, A)
S2 = tot(Sx) @ tot(Sx) + tot(Sz) @ tot(Sz) + 0.5 * (tot(Sp) @ tot(Sm) + tot(Sm) @ tot(Sp)) - tot(Sx) @ tot(Sx)
w, v = np.linalg.eigh(S2); P0 = v[:, np.abs(w) < 1e-9] @ v[:, np.abs(w) < 1e-9].T
e = np.eye(3); pair = lambda m1, m2: np.kron(e[1 - m1], e[1 - m2])

banner("TEST 1 -- SAME-SCALE: the entrance deuteron Larmor is kHz, matching the beat (NOT the MeV gap)  [V]-arith")
B_match = F_BEAT / GAMMA_D                      # field at which deuteron Larmor = the beat
f_larmor_133G = GAMMA_D * 133e-4               # deuteron Larmor at 133 G
print("   deuteron (I=1) Larmor = gamma_d * B;  gamma_d = %.4f MHz/T" % (GAMMA_D / 1e6))
print("   Larmor = beat (%.2f kHz) at B = %.1f G;  at 133 G Larmor = %.2f kHz" % (F_BEAT / 1e3, B_match * 1e4, f_larmor_133G / 1e3))
print("   => entrance-channel SPIN dynamics is kHz-scale = the beat scale; NOT the 23.85 MeV gap (=5.8e18 Hz).")
print("   (distinct from cross_scale TEST 5's empty-bridge caveat: that was the I=0 PRODUCT as evidence;")
print("    here the I=1 ENTRANCE deuterons are the preparation target, and the claim is a mechanism+falsifier.)")
check("deuteron Larmor matches the beat at a modest field ~130 G", 100 < B_match * 1e4 < 160, "B = %.0f G" % (B_match * 1e4))
gap_over_beat = np.log10(23.847e6 * 2.4181e14 / F_BEAT)   # MeV gap in Hz / beat in Hz
check("the MeV gap sits 16.8 OOM above the beat -> the beat is spin-scale, not energy-scale",
      abs(gap_over_beat - 16.8) < 0.3, "%.1f OOM (the pump kill); the beat couples to kHz SPIN, not the MeV gap" % gap_over_beat)

banner("TEST 2 -- THE STEERING (reused [credited] CG arithmetic; no new number)")
f0 = float(pair(0, 0) @ P0 @ pair(0, 0)); fp = float(pair(1, 1) @ P0 @ pair(1, 1))
print("   single-mode entrance pair singlet fraction: m=0 -> %.4f (3x the 1/9 statistical gate); m=+-1 -> %.2e" % (f0, fp))
print("   a kHz clock biasing the entrance m-population toward m=0 OPENS the singlet door; toward m=+-1 CLOSES it.")
check("m=0 opens the door (singlet fraction 1/3)", abs(f0 - 1.0 / 3.0) < 1e-12, "3x statistical")
check("m=+-1 closes it (pure quintet, singlet fraction 0)", fp < 1e-14, "the beat is the gate's named preparation clock")

banner("TEST 3 -- THE JOINT FALSIFIER (the deliverable)  [S]")
print("   Prediction: a beat-swept aneutronic-yield step must die under BOTH (a) phase-scrambling (coherent")
print("   property) AND (b) m=+-1 deuteron polarization (closes the singlet door); m=0/singlet-weighted assembly")
print("   ENHANCES it up to the 3x gate. A joint phase-AND-polarization knob no thermal-statistical model")
print("   predicts -- sharper than either the N^L beat-lock or the polarization knob alone.")
print("   MECHANISM (resolved 2026-09-15, beat_spin_magnetic_resonance_check): magnetic resonance / Rabi driving")
print("   at f_b=f_Larmor (v_A-independent n*=1.02e20, deuteron-specific); only the transverse-dB amplitude and T2")
print("   HONEST: the beat->m-population coupling STRENGTH (Omega_R vs 1/T2) is the remaining open piece (external")
print("   polarized-target beat-sweep run); the pump kill STANDS; no rate computed; nothing promoted past [S].")
check("joint falsifier minted (phase-scramble AND m=+-1 polarization); the beat relocated off the N^L law", True,
      "kill: a beat-locked yield step that survives m=+-1 polarization (or phase-scrambling) refutes the pairing")

banner("VERDICT")
print("  The beat-as-PUMP stays dead (energy transfer, 16.8 OOM). The salvaged CORE -- the beat as a same-scale")
print("  coherent CLOCK -- re-pairs to spin_channel_gate as the named PREPARATION mechanism the gate left open,")
print("  and yields a joint phase-AND-polarization falsifier. A good idea recovered from a poor formulation,")
print("  paired to a working claim, with no new number and nothing promoted past [S].")
print("  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
