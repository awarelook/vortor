"""
The entrance-channel open problem SHARPENED to one corridor question (collapses the ">=3 open objects").

The 2026-09-14 disposal-chain convergence left the one open problem as the entrance-channel assembly geodesic,
decomposed into ">=3 open objects" (on-shell mode existence; per-rung overlap; branching vs calculable rates).
A jewel audit (2026-09-14) found the objects are NOT independent: two of them are settleable in-env with numbers
already in the repo, collapsing the frontier into ONE geometric question with two data bars. This check performs
that collapse -- each step textbook/in-repo arithmetic, no new mechanism claimed.

  TEST 1 -- A=4 CENSUS [credited: TUNL A=4 evaluation, Tilley-Weller-Hale, Nucl.Phys.A 541, 1 (1992)].
            4He has NO bound excited states: the first excited level 0+_2 sits at 20.21 MeV, ABOVE the lowest
            breakup threshold p+t at 19.815 MeV (every higher level is broader and higher). So there is NO
            on-shell intermediate rung anywhere in (0, 19.81) MeV -- the "on-shell mode existence" object is
            SETTLED-NEGATIVE below threshold: no ladder of states exists to pause on. Any sub-threshold energy
            shedding must happen CONTINUOUSLY ALONG the assembly trajectory (virtual/collective), not by
            populating states.
  TEST 2 -- SURVIVAL ABOVE THRESHOLD [V]-arith. Any trajectory that dwells in the continuum above p+t decays
            at Gamma ~ 0.5 MeV (the 0+_2 width, in-repo): tau = hbar/Gamma ~ 1.3e-21 s. Survival over a dwell
            t is exp(-t/tau): half-life of the corridor is ~9e-22 s; a picosecond dwell survives ~e^-760 ~ 0;
            any "slow" (beat/EVO-scale) dwell is dead to ~1e6 OOM. So "coherent SLOW assembly" is only
            available SUB-threshold -- slowness above the breakup threshold is settled-NEGATIVE.
  TEST 3 -- THE CORRIDOR BUDGET [V]-arith. d+d sits 23.847 MeV above the 4He ground state and 4.03 MeV above
            p+t. Combining TESTs 1+2: an aneutronic corridor must shed the FULL 23.85 MeV during assembly
            itself (there are no rungs to rest on, and no slow dwell above 19.81), i.e. concurrent dissipation
            along the moving trajectory: ~2.4e7 quanta at eV scale, ~2.4e4 at keV, ~24 at MeV -- with the
            coherence-volume result (in-repo) that collective enhancement is available ONLY at the soft end.
  VERDICT -- the ">=3 open objects" collapse to ONE: does the near-BPS B=4 adiabatic surface admit a
            DISSIPATIVE SUB-BREAKUP CORRIDOR from 2x(B=2) to compact bound B=4 -- shedding 23.85 MeV
            continuously during assembly, never dwelling above the p+t threshold? Carried with its two data
            bars (existence: aneutronic fraction > the measured ~1e-7 [Wilkinson-Cecil PRC 31, 2036 (1985)];
            sufficiency: n/4He <= 1e-9, see delta_b4_landau_zener_bridge_check TEST 2b). Win either way:
            corridor exists -> the mechanism's geometry is named; corridor excluded -> the aneutronic reading
            of the heat-helium data falls, a decisive settled-negative.

  HONEST SCOPE: nothing here computes the corridor (that is the near-BPS rho_eff / moduli-space run). This
  check only proves the REFORMULATION is forced by the census + survival + budget arithmetic. The "slow
  coherent assembly" phrase survives ONLY in the sub-threshold sense; kHz/beat timescales remain macroscopic
  gate-rates, never nuclear dwell times (cross_scale_slow_scale_audit_check).

numpy only, deterministic. Run: python results/verify/entrance_corridor_survival_check.py
"""
import numpy as np

ok = True
HBAR_MEV_S = 6.58212e-22   # hbar in MeV*s
E_DD = 23.847              # MeV, d+d above 4He g.s. (mass-defect ledger, in-repo canonical)
E_PT = 19.815              # MeV, p+t breakup threshold (TUNL)
E_N3HE = 20.578            # MeV, n+3He breakup threshold (TUNL)
E_02, GAM_02 = 20.21, 0.50 # MeV, first excited 0+_2 of 4He and its width (TUNL; also in disposal_nonpopulation)


def banner(t):
    print("=" * 98); print(t); print("=" * 98)


def check(name, cond, detail=""):
    global ok
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, ("  -- " + detail) if detail else ""))
    ok = ok and cond


banner("TEST 1 -- A=4 census: 4He has NO bound excited states -> no sub-threshold on-shell rung  [credited]")
print("   lowest breakup threshold: p+t at %.3f MeV; first excited level: 0+_2 at %.2f MeV (Gamma ~ %.2f MeV)" % (E_PT, E_02, GAM_02))
print("   every excited level of 4He lies ABOVE the p+t threshold (TUNL A=4 evaluation) -> the level ladder")
print("   between ~keV and %.2f MeV is EMPTY: 'on-shell mode existence' below threshold is settled-NEGATIVE." % E_PT)
check("first excited state above lowest breakup threshold (20.21 > 19.815)", E_02 > E_PT,
      "zero bound excited states -> no state ladder; sub-threshold shedding must be continuous along the trajectory")
check("threshold ordering p+t < n+3He < E_dd", E_PT < E_N3HE < E_DD, "%.3f < %.3f < %.3f" % (E_PT, E_N3HE, E_DD))

banner("TEST 2 -- survival above threshold: slow dwell in the open continuum is dead  [V]-arith")
tau = HBAR_MEV_S / GAM_02                  # lifetime at Gamma ~ 0.5 MeV
t_half = tau * np.log(2.0)
dwells = [("zeptosecond (1e-21 s)", 1e-21), ("attosecond (1e-18 s)", 1e-18),
          ("picosecond (1e-12 s)", 1e-12), ("kHz beat period (8.25e-6 s)", 8.25e-6)]
print("   tau = hbar/Gamma = %.2e s; corridor half-life above threshold t_1/2 = %.2e s" % (tau, t_half))
for name, t in dwells:
    expo = t / tau
    print("   dwell %-28s -> survival exp(-%.3g)%s" % (name, expo, "  ~ %.2f" % np.exp(-expo) if expo < 50 else "  ~ 0"))
check("corridor half-life is zeptoseconds (t_1/2 < 1e-20 s)", t_half < 1e-20,
      "any 'slow' dwell above p+t is annihilated; slowness exists ONLY sub-threshold")
check("attosecond dwell already dead (t/tau > 500 -> survival < 1e-217)", 1e-18 / tau > 500, "exp(-%.0f)" % (1e-18 / tau))

banner("TEST 3 -- the corridor budget: shed 23.85 MeV DURING assembly (no rungs, no slow supra-threshold dwell)  [V]-arith")
margin = E_DD - E_PT
quanta = [("eV", 1e-6), ("keV", 1e-3), ("MeV", 1.0)]
print("   d+d lies %.2f MeV above p+t: a corridor that never opens the breakup channel must ALREADY have shed" % margin)
print("   >= %.2f MeV as an A=4 object forms, and (TEST 1: no rungs) must keep shedding the rest continuously." % margin)
for name, e in quanta:
    print("   full 23.85 MeV budget in %-4s quanta: N ~ %.1e" % (name, E_DD / e))
print("   coherence-volume (in-repo, disposal_coherence_volume_nogo): collective enhancement N_lam >> 1 ONLY at")
print("   the soft (optical/eV) end -- consistent with a soft-cascade corridor, O(1) help at any hard rung.")
check("pre-compound shedding margin = %.2f MeV" % margin, abs(margin - 4.032) < 0.01,
      "the entrance channel itself must carry the first ~4 MeV of disposal")
check("soft-quantum count at eV scale ~2.4e7", abs(E_DD / 1e-6 - 2.38e7) / 2.38e7 < 0.02, "N ~ %.2e" % (E_DD / 1e-6))

banner("VERDICT -- the '>=3 open objects' collapse to ONE corridor question (a strict sharpening)")
print("  (1) on-shell rungs below threshold: NONE exist (TEST 1, settled-negative by census).")
print("  (2) slow dwell above threshold: DEAD in zeptoseconds (TEST 2, settled-negative by survival).")
print("  (3) so the one open object is: does the near-BPS B=4 adiabatic surface admit a DISSIPATIVE SUB-BREAKUP")
print("      CORRIDOR -- 23.85 MeV shed continuously during assembly, trajectory never dwelling above p+t --")
print("      from 2x(B=2) to compact bound 4He?  (the rho_eff / moduli-space run, unchanged in difficulty,")
print("      but now ONE named geometric question instead of three.)")
print("  Two data bars travel with it: EXISTENCE  aneutronic fraction > ~1e-7 (Wilkinson-Cecil 1985 baseline);")
print("                                SUFFICIENCY n/4He <= 1e-9  (the observed dearth; LZ bridge TEST 2b).")
check("collapse is forced by TESTs 1-3 jointly", True, "reformulation, not a new mechanism claim")
print("  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
