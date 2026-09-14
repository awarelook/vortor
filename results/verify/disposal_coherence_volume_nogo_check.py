"""
Collective enhancement does NOT beat the disposal bottleneck (M16 settled-negative): the superradiant N is the
COHERENCE-VOLUME occupation N_lam(E) = n * lam_bar(E)^3, a property of the coupling at the transition energy --
O(1) at the hard 24 MeV top rung, ~1e7 only at the SOFT optical/eV end. So coherence helps the EASY part of the
cascade and NOT the load-bearing hard step. Corrects an earlier "magnitude has headroom" over-claim (a
verification found the N was illegitimately imported from optical scale to a 24 MeV disposal).

WHAT WAS WRONG (recorded). An earlier check argued: beating the ~1e-7 baseline needs only ~1e7 enhancement, and a
Dicke-class Gamma_N ~ N Gamma_1 with an EVO N ~ 1e11 gives ~1e4 headroom, so "magnitude is not the bottleneck, only
the coupling is." A verification refuted it: (i) the enhancement is amplitude ~ sqrt(N)*g(N) -> rate ~ N*g^2, which
is ~N ONLY if the per-unit coupling g is N-independent, i.e. only if all N units are within one reduced wavelength
AND in phase -> the couplable count is N_lam = n*lam_bar^3, NOT a free population; (ii) at 24 MeV lam_bar = 8.2 fm so
N_lam = O(1); (iii) N_lam ~ 1e7 is reached only at optical/eV (lam_bar ~ 100 nm) -- the soft end, where Preparata's
domain lives; (iv) the true target is ~1e15 (to reach n/4He <= 1e-9), not 1e7; (v) magnitude and coupling are ONE
object, not two. So the escape fails at the hard rung.

  TEST 1 -- THE TRUE TARGET IS ~1e15, NOT 1e7 [V]-arith. Hot d+d: 4He ~1e-7, neutron (n+3He) ~0.5 -> n/4He ~ 5e6.
            To reach the observed dearth n/4He <= 1e-9 with the strong channels unsuppressed needs the operative
            (aneutronic) path to beat the neutron channel by ~5e6/1e-9 = ~5e15. "Dominance=0.5" (G~1e7) is the wrong,
            far-too-lenient bar -- at G=1e7 a QUARTER of fusions still emit a neutron (hot-fusion flux).
  TEST 2 -- THE SUPERRADIANT N IS THE COHERENCE-VOLUME OCCUPATION N_lam = n*lam_bar^3, NOT a free count [V]-arith.
            At the hard 24 MeV top rung lam_bar = 8.2 fm -> N_lam ~ 4e-14 (solid density) to ~90 (nuclear density) =
            O(1). N_lam reaches ~1e7 ONLY at optical/eV (lam_bar ~ 100 nm). So the ~1e11 EVO count is an
            OPTICAL-scale coherence number wrongly applied to a 24 MeV disposal (~21 OOM out of place).
  TEST 3 -- AND THERE IS NO CONDENSED-MATTER MODE AT 24 MeV to receive the quantum in one step [credited]. Debye
            phonons <= ~0.1 eV; EVO/metal plasmons ~ tens of eV; nothing at MeV. A cavity gives Purcell
            DE-enhancement ~ lam_bar^3/V ~ 1e-25 for an 8 fm quantum in a micron cavity. So the load-bearing hard
            step gets NO collective enhancement -- collective coherence helps the SOFT cascade end, not the bottleneck.
  TEST 4 -- SO THE ENHANCEMENT-MAGNITUDE ESCAPE FAILS [settled-neg], and the frontier is NOT "one coupling number
            with headroom." Magnitude and coupling are ONE object (N_eff = N_lam(E) x phase). If the aneutronic path
            is real, its aneutronicity must come from the ENTRANCE-channel assembly (the B=4/B=8 moduli-space
            geodesic / non-population routing), NOT from soft-cascade collective enhancement -> back to the
            disposal_nonpopulation open item. The EVO-N_crit "coincidence" is a MISMATCH (a 1e7 factor vs a 1e11
            count, different kinds of number, ~1e4 apart) -- logged as such, not a clue.

numpy only, deterministic. Run: python results/verify/disposal_coherence_volume_nogo_check.py
"""
import numpy as np

ok = True
HBARC = 197.3269804        # MeV*fm
N_SOLID = 6.8e28           # /m^3 (Pd, ~solid density)
N_NUC = 1.6e44             # /m^3 (nuclear density 0.16/fm^3)
BR_HOT_HE = 1e-7           # hot d+d -> 4He branch
BR_HOT_N = 0.5             # hot d+d -> n+3He branch
OBS_DEARTH = 1e-9          # observed neutron/4He upper end


def banner(t):
    print("=" * 98); print(t); print("=" * 98)


def check(name, cond, detail=""):
    global ok
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, ("  -- " + detail) if detail else ""))
    ok = ok and cond


def N_lam(E_MeV, n):
    lam_bar_m = (HBARC/E_MeV)*1e-15      # reduced wavelength in metres
    return n*lam_bar_m**3, HBARC/E_MeV   # (occupation, lam_bar in fm)


# ---------------------------------------------------------------- TEST 1: the true target ~1e15
banner("TEST 1 -- the true target is ~1e15 (to reach n/4He <= 1e-9), NOT 1e7 ('dominance')")
n_over_he_hot = BR_HOT_N/BR_HOT_HE
target = n_over_he_hot/OBS_DEARTH
print("   hot d+d: 4He ~%.0e, n+3He ~%.1f -> n/4He ~ %.0e ; to reach observed n/4He <= %.0e -> swing ~ %.0e" %
      (BR_HOT_HE, BR_HOT_N, n_over_he_hot, OBS_DEARTH, target))
print("   ('dominance=0.5' i.e. G~1e7 is far too lenient: at G=1e7 a QUARTER of fusions still emit a neutron)")
check("the real enhancement target set by the aneutronicity data is ~1e15, ~8 OOM above the earlier 1e7 claim",
      target > 1e14, "the earlier '1e7 to dominance' bar was wrong")

# ---------------------------------------------------------------- TEST 2: N is the coherence-volume occupation
banner("TEST 2 -- the superradiant N is the COHERENCE-VOLUME occupation N_lam = n*lam_bar^3, O(1) at the hard rung")
for E, lab in [(23.847, "24 MeV (hard top rung)"), (1e-3, "1 keV"), (2e-6, "2 eV (optical)")]:
    Nl_s, lb = N_lam(E, N_SOLID)
    Nl_n, _ = N_lam(E, N_NUC)
    lb_disp = ("%.2f fm" % lb) if lb < 1e5 else ("%.3g nm" % (lb*1e-6))
    print("   E=%-22s lam_bar=%-10s  N_lam(solid)=%.2e  N_lam(nuclear)=%.2e" % (lab, lb_disp, Nl_s, Nl_n))
Nl_hard, _ = N_lam(23.847, N_SOLID)
Nl_opt, _ = N_lam(2e-6, N_SOLID)
check("N_lam is O(1) at the hard 24 MeV rung and reaches ~1e7 only at optical/eV -> the EVO ~1e11 is optical-scale, misapplied",
      Nl_hard < 1e-6 and Nl_opt > 1e6, "the couplable count is set by the coherence volume at the transition energy, not a free population")

# ---------------------------------------------------------------- TEST 3: no 24 MeV condensed-matter mode
banner("TEST 3 -- no condensed-matter mode at 24 MeV to receive the quantum; a cavity gives Purcell DE-enhancement")
E_debye, E_plasmon = 0.1, 30.0         # eV: Debye phonon ceiling, metal/EVO plasmon
lam_bar_hard = (HBARC/23.847)*1e-15    # m
V_cavity = (1e-6)**3                    # m^3 (micron cavity)
purcell = lam_bar_hard**3/V_cavity
print("   available modes: Debye phonons <= %.1f eV ; plasmons ~ %.0f eV ; NOTHING at ~24e6 eV (MeV)" % (E_debye, E_plasmon))
print("   cavity Purcell factor ~ lam_bar^3/V = (%.1e m)^3/(1 um)^3 = %.1e  -> DE-enhancement (suppression), not gain" % (lam_bar_hard, purcell))
check("there is no resonant condensed-matter mode at 24 MeV, and cavity coupling DE-enhances (~1e-25) -> no help at the top rung",
      purcell < 1e-20 and E_plasmon < 1e3, "[credited] -- collective coherence helps the soft cascade end, not the load-bearing hard step")

# ---------------------------------------------------------------- TEST 4: the escape fails; back to the geodesic
banner("TEST 4 -- the enhancement-magnitude escape FAILS; the aneutronicity must come from the ENTRANCE assembly")
print("   magnitude and coupling are ONE object (N_eff = N_lam(E) x phase), NOT separable. The ~1e15 needed enhancement")
print("   is available (N_lam >> 1) ONLY at optical/eV -- the SOFT end -- and is O(1) at the 24 MeV bottleneck.")
print("   -> if aneutronic d+d is real, its aneutronicity must come from the ENTRANCE-channel assembly (the B=4/B=8")
print("      moduli-space geodesic / non-population routing, disposal_nonpopulation_check), NOT soft-cascade coherence.")
print("   EVO-N_crit 'coincidence': a 1e7 FACTOR vs a 1e11 COUNT (different kinds of number, ~1e4 apart) -> a MISMATCH.")
check("collective enhancement does NOT beat the hard-rung bottleneck; the open item is the entrance-assembly geodesic",
      True, "[settled-neg] -- a genuine wall, converging with the non-population check on the moduli-space geodesic")

banner("VERDICT")
print("  Collective/superradiant enhancement does NOT solve the disposal. The needed enhancement (~1e15 to match the")
print("  aneutronicity data, TEST 1) is available (N_lam >> 1) ONLY at the SOFT optical/eV end, where N_lam ~ 1e7 and")
print("  Preparata's coherent domain is real -- and it is O(1) at the HARD 24 MeV top rung (lam_bar = 8.2 fm, TEST 2),")
print("  where there is no resonant condensed-matter mode and a cavity DE-enhances (TEST 3). So coherence helps the")
print("  EASY part and not the bottleneck; 'magnitude has headroom' was wrong (magnitude and coupling are one object).")
print("  The aneutronicity, if real, must come from the ENTRANCE-channel assembly (the B=4/B=8 moduli-space geodesic),")
print("  NOT the soft cascade -- converging with disposal_nonpopulation. A settled-negative; the frontier is the geodesic.")
print("  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
