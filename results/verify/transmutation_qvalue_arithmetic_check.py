"""
Transmutation Q-value arithmetic, HARNESSED. The 2026-09-14 resolution map carried the assigned transmutation
Q-values as "[V]-arithmetic (not in the 78/78 harness -- only 23.847 MeV is)" -- an honest but anomalous tag
(a [V]-family label with no named check, flagged by the jewel audit). This closes the exception: the same
mass-defect bookkeeping that fixes 23.847 MeV/4He is applied to the named baryon-conserving DeltaA=4n hops.

  TEST 1 -- ANCHOR: d+d -> 4He = 23.847 MeV from the SAME vendored AME2020 mass excesses (consistency with the
            in-repo canonical ledger; if this drifts, the vendored numbers are wrong, not the physics).
  TEST 2 -- Iwamura Cs->Pr: Cs-133 + 4d -> Pr-141, Q = 50.493 MeV (the map's printed value) with explicit
            baryon (133+8=141) and charge (55+4=59) conservation.
  TEST 3 -- Iwamura Sr->Mo: Sr-88 + 4d -> Mo-96, Q computed and conservation asserted (the map names the pair;
            the Q-value is printed here as the harnessed number).

  HONEST SCOPE (the fence, verbatim from the map): Q-value arithmetic is BOOKKEEPING [V]-arith -- it proves the
  assigned channels are exothermic and baryon/charge-conserving, and NOTHING about mechanism or rate (both stay
  [S]/open). Baryon-CONSERVING transmutation is kept strictly distinct from baryon decay. Mass excesses are
  vendored from AME2020 (Wang et al., Chin. Phys. C 45, 030003 (2021)); values in keV.

numpy only, deterministic. Run: python results/verify/transmutation_qvalue_arithmetic_check.py
"""
import numpy as np

ok = True

# AME2020 mass excesses, keV  (vendored; provenance: AME2020, Wang et al. 2021)
DELTA_KEV = {
    "d":     13135.72,     # 2H
    "he4":    2424.92,     # 4He
    "cs133": -88070.94,    # 133Cs (Z=55)
    "pr141": -86020.81,    # 141Pr (Z=59)
    "sr88":  -87921.62,    # 88Sr  (Z=38)
    "mo96":  -88790.87,    # 96Mo  (Z=42)
}
Z = {"d": 1, "he4": 2, "cs133": 55, "pr141": 59, "sr88": 38, "mo96": 42}
A = {"d": 2, "he4": 4, "cs133": 133, "pr141": 141, "sr88": 88, "mo96": 96}


def banner(t):
    print("=" * 98); print(t); print("=" * 98)


def check(name, cond, detail=""):
    global ok
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, ("  -- " + detail) if detail else ""))
    ok = ok and cond


def q_mev(reactants, products):
    return (sum(DELTA_KEV[r] for r in reactants) - sum(DELTA_KEV[p] for p in products)) / 1000.0


def conserved(reactants, products):
    return (sum(A[r] for r in reactants) == sum(A[p] for p in products),
            sum(Z[r] for r in reactants) == sum(Z[p] for p in products))


banner("TEST 1 -- anchor: d+d -> 4He from the SAME vendored masses reproduces the canonical 23.847 MeV")
q_dd = q_mev(["d", "d"], ["he4"])
print("   Q(d+d -> 4He) = %.4f MeV   (canonical in-repo ledger: 23.847)" % q_dd)
check("anchor matches the canonical number to <1 keV", abs(q_dd - 23.8465) < 0.001, "%.4f MeV" % q_dd)

banner("TEST 2 -- Iwamura Cs->Pr: Cs-133 + 4d -> Pr-141  (the map's printed 50.493 MeV)  [V]-arith")
q_cs = q_mev(["cs133", "d", "d", "d", "d"], ["pr141"])
bA, bZ = conserved(["cs133", "d", "d", "d", "d"], ["pr141"])
print("   Q = %.4f MeV;  baryon: 133+8 = 141 (%s);  charge: 55+4 = 59 = Pr (%s)" % (q_cs, bA, bZ))
check("Q(Cs-133+4d -> Pr-141) = 50.493 MeV (map value) to <2 keV", abs(q_cs - 50.493) < 0.002, "%.4f" % q_cs)
check("baryon AND charge conserved (Cs->Pr)", bA and bZ, "DeltaA=8=2x4n hop, baryon-CONSERVING")

banner("TEST 3 -- Iwamura Sr->Mo: Sr-88 + 4d -> Mo-96  [V]-arith")
q_sr = q_mev(["sr88", "d", "d", "d", "d"], ["mo96"])
bA, bZ = conserved(["sr88", "d", "d", "d", "d"], ["mo96"])
print("   Q = %.4f MeV;  baryon: 88+8 = 96 (%s);  charge: 38+4 = 42 = Mo (%s)" % (q_sr, bA, bZ))
check("Q(Sr-88+4d -> Mo-96) exothermic and O(50 MeV)", 40.0 < q_sr < 60.0, "%.3f MeV" % q_sr)
check("baryon AND charge conserved (Sr->Mo)", bA and bZ, "same DeltaA=4n class")

banner("VERDICT")
print("  The assigned transmutation channels are exact, exothermic, baryon/charge-conserving mass-defect")
print("  arithmetic on AME2020 -- now IN the harness (the map's '[V]-arithmetic, not harnessed' exception is")
print("  closed). This proves BOOKKEEPING ONLY: mechanism [S] and rate (open) are untouched, and baryon-")
print("  conserving transmutation stays strictly distinct from baryon decay.")
print("  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
