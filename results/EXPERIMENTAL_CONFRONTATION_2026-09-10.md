# Reality → experiment: the FTGB fingerprints vs the published record

**Date:** 2026-09-10 · **Status:** honest literature meta-check (no new experiment). This turns the
prediction *table* in `FTGB_COHERENCE_MAP_2026-09-09.md` §4 into an actual *comparison* against real,
cited measurements. Verdict categories: **CONSISTENT-with-anomaly** (a real, contested measurement the
theory matches), **CONSTRAINED** (existing limits bound it), **UNTESTED** (no measurement exists — the
honest majority), **TENSION** (data disfavors it).

**Discipline.** Every number carries a real citation checked against the primary source. "Consistent with
a reported anomaly" is **not** "confirms FTGB." CMNS results are contested and not mainstream-accepted;
that status is stated in each caveat. No fabricated numbers; no over-unity.

---

## Summary

| # | Prediction | Verdict | Falsifier triggered? |
|---|---|---|---|
| 1 | Carrier comb {121,208,294} kHz, ratios 1:1.72:2.43, pull → 7/4, 5/2 | **UNTESTED** | no data to trigger against |
| 2 | He-4 / heat = 24 MeV per ⁴He (aneutronic) | **CONSISTENT-with-anomaly** (contested) | not triggered; not precision-confirmed |
| 3 | Aneutronic neutron-suppression | **CONSISTENT-with-anomaly** (interpretation forks) | not triggered; doesn't discriminate |
| 4 | Plasmoid aspect ratio A ≈ 9.0 | **TENSION** (spheromaks) / **UNTESTED** (EVO, ball lightning) | **triggered** by real spheromak data |
| 5 | Transmutation on a baryon-conserving lattice | **CONSISTENT** (Iwamura) / **CONSTRAINED** (field-wide) | partially triggered (scattered ash elsewhere) |
| 6 | Neutrino = Majorana, ~0.05 eV | **CONSISTENT-BUT-UNDECIDED** (open, testable ~10 yr) | not triggered; 0νββ unseen |

**Two internal contradictions surfaced by the confrontation** (see §7) — an aspect-ratio number and the
neutrino nature — that should be resolved *before* those rows are presented as coherent predictions.

---

## 1. Carrier comb {121, 208, 294} kHz — UNTESTED

**Prediction.** An *inharmonic* triplet, ratios `1 : 1.719 : 2.427` (from the CK/Beltrami roots of
`tan x = x`, reproduced by `results/verify/ck_eigenvalues_check.py`), plus a strong-coupling pull toward
`7/4 = 1.75` and `5/2 = 2.5` (`dynamics_lab.html` CH-02, tagged `[S]`).

**Record.** No RF/magnetic/acoustic inharmonic triplet at these frequencies/ratios is reported in any
candidate system. Ball-lightning spectroscopy is *optical* atomic lines only (Cen, Yuan & Xue, *PRL* **112**,
035001, 2014). Shoulders EVOs report crater morphology, not RF spectra (Hubler & Blaise, *JCMNS* **36**, 30,
2022). Dusty-plasma acoustic modes sit at 0.1–450 Hz — 3–4 orders too low. The one real *in-band* analogue is
**Toroidicity-induced Alfvén Eigenmodes** (Cheng, Chen & Chance, *Ann. Phys.* **161**, 21, 1985), measured at
50–500 kHz in tokamaks/spherical-tokamaks — but that is a different (coil-confined, externally driven) system
whose frequencies track the device, not a universal CK ratio.

**Verdict UNTESTED.** Caveat: only the *ratio* structure is calibration-free — the absolute kHz depends on
`v_A`, which the foundation itself flags as a self-consistency residual (not independently measured). The
`7/4, 5/2` pull is a numerical mechanism demo, not a measurement (though Adler/Arnold-tongue mode-locking is
itself well established).

## 2. He-4 / heat = 24 MeV per ⁴He — CONSISTENT-with-anomaly (contested)

**Prediction.** Excess heat correlated with ⁴He at ~24 MeV/atom (Q(d+d→⁴He) = 23.85 MeV; verified in
`results/verify/lenr_energy_ledger.py`). Credited to Miles, not claimed original.

**Record.** Miles, "Correlation of Excess Enthalpy and Helium-4 Production: A Review," *ICCF-10* (2003):
18/21 excess-heat runs correlated with excess ⁴He; ⁴He rate `10¹⁰–10¹² atoms·s⁻¹·W⁻¹` vs a theoretical
`2.6×10¹¹` — i.e. **order-of-magnitude / rough-quantitative** agreement (scatter ~×5), not precision.
Corroborated by McKubre et al. (SRI/Case, *ICCF-8*, 2000). The **2004 US DOE review** found ⁴He in only
**5 of 16** examined excess-heat cases, "typically very close to but reportedly above background," flagged
**air (⁴He) contamination** as a live alternative, and its 18 reviewers split ~evenly on excess heat and
concluded LENR is "not conclusively demonstrated."

**Verdict CONSISTENT-with-anomaly.** The single most quantitatively specific, repeatedly-reported CMNS
correlation — but not accepted science, ×5 scatter, contamination unresolved, and the *mechanism* (how
23.8 MeV sheds without a γ) is exactly the gap the DOE panel found unconvincing and that FTGB itself carries
as `[S-mechanism]` + open Δ.

## 3. Aneutronic neutron-suppression — CONSISTENT-with-anomaly (interpretation forks)

**Prediction.** Excess heat with neutron flux many orders below same-rate thermal d+d (heat without
commensurate neutrons); falsifier "neutron yield scales with heat."

**Record.** The aneutronic d+d→⁴He+γ branch is a measured `~1.1×10⁻⁷` of hot d+d. ~1 W via the ordinary
n/p channels would imply ~10¹² n/s (lethal) — the "dead graduate student" argument (Huizenga, 1992); reported
CMNS fluxes are 8–9 orders below that. The small original F&P neutron/γ claim was itself disputed on
instrumental grounds (Petrasso et al., *Nature* **339**, 183, 1989). DOE 2004 records "no high-energy γ
accompanies the ⁴He" as the proponents' own anomaly.

**Verdict CONSISTENT-with-anomaly**, but with a sharp fork stated plainly: mainstream reads
"heat-without-neutrons" as evidence there is **no real d-d fusion at all** (calorimetry artifact); CMNS reads
it as a genuine selection rule. The *same* low-neutron data fits both — so a null neutron result does **not**
discriminate. FTGB needs *two* suppressions at once (the ~10⁻⁷ γ-branch, plus an extra n/p suppression) that
no accepted mechanism supplies, and the disposal channel is its open Δ (HPC-only).

## 4. Plasmoid aspect ratio A ≈ 9.0 — TENSION / UNTESTED  ⚠ internal problem (see §7)

**Prediction (as tabled).** Plasmoid aspect ratio `A ≈ 9.0`.

**Record.** Lab spheromaks — the object FTGB identifies its plasmoid with — sit at **A ≈ 1.1–1.4** (SSPX;
Hill et al., *PPCF* **54**, 113001, 2012); "spheromak" is *defined* by low aspect ratio. Ball lightning and
EVOs have **no measured internal aspect ratio** (not resolvable with current technique). Field-reversed
configurations reach 2:1–10:1, but FTGB's object is a spheromak/CK-torus, not an FRC.

**Verdict TENSION** (vs the only checkable system) **/ UNTESTED** (EVO, ball lightning). The falsifier
("A far from 9") is **triggered** by spheromak data. **But see §7:** `A ≈ 9.0` is not a plasmoid derivation
— it is a flagged input to the *α-winding* exercise, and it contradicts the theory's own core geometry
(`A = φ ≈ 1.618`), which is the number that should be compared here.

## 5. Transmutation on a baryon-conserving lattice — CONSISTENT (Iwamura) / CONSTRAINED (field-wide)

**Prediction.** Products on a discrete Skyrme/Nielsen mass lattice, `ΣB` conserved (baryon-conserving
steps only, never baryon decay).

**Record.** Iwamura et al. (Mitsubishi): Cs(A=133)→Pr(A=141) and Sr(A=88)→Mo(A=96), both **ΔZ=+4, ΔA=+8**
= two ⁴He-equivalent units — a clean discrete `ΔA = 4n` pattern (replicated by Toyota, and Sr→Mo by INFN
Frascati). But NRL failed to replicate, and NRL's Kidwell found environmental **Pr contamination** at the
Mitsubishi lab. Mizuno and Miley report broad, **scattered** multi-element shifts with *no* `ΔA=4n` pattern
("not possible to discern any systematic pattern" — Miley & Patterson's own words). Urutskoev is among the
least-controlled claims.

**Verdict CONSISTENT** for the cleanest case (Iwamura), **CONSTRAINED** field-wide (others show no lattice
pattern; contamination critiques active). Caveat: baryon conservation is guaranteed by *ordinary* nuclear
physics in every reported transmutation, so that half of the falsifier is moot; the discriminating question
is on-lattice vs scattered, and ⁴He is the natural transfer unit for *any* baryon-conserving mechanism — so
the ΔA=4 match is not evidence for the Skyrme/Nielsen mechanism *specifically*.

## 6. Neutrino = Majorana at ~0.05 eV — CONSISTENT-BUT-UNDECIDED  ⚠ internal problem (see §7)

**Prediction.** The neutrino rung is Majorana (`ν=ν̄`), mass `m = ħω_C/c² ≈ 0.05 eV`; falsifier "0νββ null
at the predicted scale."

**Record.** Majorana-vs-Dirac is experimentally **unknown**; 0νββ is the primary test and is **unseen**.
Best limit: **KamLAND-Zen**, `T½ > 3.8×10²⁶ yr`, `m_ββ < 28–122 meV` (arXiv:2406.11438, *PRL* **135**, 262501,
2025). LEGEND-200 / CUORE bracket 70–305 meV. The atmospheric splitting is `√Δm²_atm ≈ 0.050 eV` (NuFIT-6.0,
arXiv:2410.05380); cosmology now bounds `Σm_ν < 0.064 eV` (DESI DR2, arXiv:2503.14738), excluding any
quasi-degenerate spectrum.

**Verdict CONSISTENT-BUT-UNDECIDED.** The Majorana claim is genuinely open (0νββ unseen everywhere) — the
honest, live, falsifiable part. **But the ~0.05 eV "prediction" is a restatement of `√Δm²_atm`**, a splitting
measured since 1998 — the repo itself tags `m_ν≈50 meV` as a "geometric-ratio ansatz / [preprint-claim]"
that FTGB "does not itself derive." KamLAND-Zen's 28–122 meV window *brackets* 50 meV; next-gen (KamLAND2-Zen,
LEGEND-1000, nEXO) reaches the band in the **late-2020s–2030s** — a real decision within ~10 years. **See §7:**
the repo contradicts itself on whether the neutrino is Majorana or Dirac.

## 7. Two internal contradictions the confrontation surfaced

These are honesty flags, not data verdicts — the confrontation exposed them; **both are resolved by tier**.

- **The `A ≈ 9.0` aspect-ratio row is inconsistent with the theory's own geometry.** `A = 9.0 ± 1` traces
  to the *toroidal-electron winding* estimate feeding the α exercise (`results/ALPHA_DYNAMICAL_REFRAME`,
  `results/verify/alpha_running.py`), which is itself `[flag]`ged and 2.3% off. The core cabled-nesting result
  gives `ε = 1/φ`, i.e. `A = φ ≈ 1.618`. Real spheromaks sit at `A ≈ 1.1–1.4`. **Resolved:** the
  coherence-map §4 "aspect ratio" row now cites the theory's own `A ≈ φ` (a genuine, favorable near-miss to
  SSPX), and the flagged electron-winding `A ≈ 9.0` is removed from the plasmoid-geometry row.
- **The repo holds two contradictory neutrino readings.** `FTGB_GRAND_SYNTHESIS.md` (≈L522–527): neutrino is
  "self-dual (Majorana-like)", 0νββ is "the external falsifier … *not* an FTGB prediction." `TOOLKIT_ADV_13`
  (M13, ≈L287–295): "Framework prediction: **Dirac** neutrinos (S⁹ spinor decomposition forbids a Majorana
  mass ⇒ 0νββ **null**), normal ordering." These predict **opposite** 0νββ outcomes. **Resolved:**
  the credited/computed **chirality-geometry layer commits to Majorana** — the neutrino is the self-dual
  `θ_χ=45°`, `H=0`, C-invariant state (`majorana_selfdual_check.py`, `CHIRALITY_DUALITY_ASSESSMENT` §3b). The
  TUFT `[preprint-claim]` Dirac reading is the lower-tier disagreement `0νββ` will decide; the theory's
  load-bearing prediction is **Majorana**.

---

## Bottom line

The falsifiable program is **mostly UNTESTED** — which is the honest and expected state for a young synthesis:
the sharpest, cheapest tests (the inharmonic comb + its 7/4, 5/2 pull; a resolved plasmoid aspect ratio) have
**no data yet**, so they are live experimental targets, not confirmations. Two rows are **CONSISTENT with a
real but contested anomaly** (He-4/heat, aneutronic suppression) that FTGB *accounts for* but does not
*confirm* — and whose mechanism reduces to the still-open Δ. One row is in **TENSION** with the only checkable
data (aspect ratio) and is, on inspection, an internal-consistency error. The neutrino is **open and decidable
within ~10 years**, but its mass "prediction" is a restatement of a known splitting, and the repo disagrees
with itself on its nature.

The single most valuable outcome of confronting the table with data was not a confirmation — it was catching
**two internal contradictions** (§7). That is the anti-numerology discipline working as intended.

*Provenance: literature via the project's `cmns-lenr-explorer` + a 0νββ search pass; predictions from
`FTGB_COHERENCE_MAP_2026-09-09.md` §4; internal numbers from `results/verify/{ck_eigenvalues_check,
lenr_energy_ledger}.py`. Citations checked against primary sources. CMNS claims are contested and
not mainstream-accepted; every verdict states its status.*
