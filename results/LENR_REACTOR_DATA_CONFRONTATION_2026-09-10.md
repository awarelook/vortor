# Reactor data → FTGB LENR layer: Klimov PVR, thorium-plasma framework, AUREON/SAFIRE

**Date:** 2026-09-10 · **Status:** honest experimental-data confrontation (no new experiment; no fabricated
numbers). Companion to `EXPERIMENTAL_CONFRONTATION_2026-09-10.md` (literature meta-check of the LENR layer's
own prediction table) — this file instead confronts the layer against **named reactor programs**: Anatoly
Klimov's Plasma Vortex Reactor (PVR), the thorium-plasma control-parameter framework, and AUREON
Energy/SAFIRE (Montgomery Childs). Tier legend: `[credited measurement]` = read directly off a peer-reviewed
primary source; `[S]` = structural/speculative connection; `[flag]` = an honesty/provenance problem surfaced
by this confrontation; `[V]` = verified by identity/computation in this repo. **Baryon number is conserved
throughout — nothing here proposes baryon decay.** COP>1, where real, is a nuclear-or-chemical energy
*ratio*, never free energy.

---

## Part I — Klimov PVR: extracted data (primary sources, directly fetched and read)

Three peer-reviewed Klimov papers were retrieved and read in full (PDF text extraction, not a secondary
summary):

- **[K1]** A. Klimov, "Energy Release and Transmutation of Chemical Elements in Cold Heterogeneous
  Plasmoids," *J. Condensed Matter Nucl. Sci.* **19** (2016) 155–163.
- **[K2]** A. Klimov, A. Grigorenko, A. Efimov, N. Evstigneev, O. Ryabkov, M. Sidorenko, A. Soloviev,
  B. Tolkunov, "High-energetic Nano-cluster Plasmoid and its Soft X-ray Radiation," *J. Condensed Matter
  Nucl. Sci.* **19** (2016) 145–154.
- **[K3]** A. Klimov, "Decay-Instability of Transmuted Chemical Elements Obtained in LENR Experiment,"
  *J. Condensed Matter Nucl. Sci.* **36** (2022) 305–311.

All three are ICCF/ISCMNS-proceedings-tier publications (self-published research reports, not
independently-replicated, peer-reviewed-adjacent but not mainstream-accepted). Treated here as
**[credited measurement]** in the narrow sense "this is what the paper reports it measured" — not as
adjudicated, confirmed physics.

### I.1 Reactor geometry `[credited measurement]`

| Parameter | Value | Source |
|---|---|---|
| PVR quartz tube | 60 mm diameter × 60 cm length | K2 §1 |
| Electrode (discharge) gap | 80 mm | K2 §2 |
| Water-cluster-plasmoid variant, tube inner diameter | 20–80 mm | K1 §2 |
| Water-cluster-plasmoid variant, tube height H | 50–200 mm | K1 §2 |
| Quartz wall thickness | 3–5 mm | K1 §2 |
| Metal droplet diameter (cathode erosion) | 0.01–0.1 mm | K2 §2 |
| Plasma halo diameter around droplets | ~10 mm | K2 §2 |
| Visible plasmoid diameter (water-cluster variant) | 2–6 cm | K1 §2.1 |
| Cathode diameter | 5 mm | K2 Fig.10 |

### I.2 Drive / operating conditions `[credited measurement]`

| Parameter | Value | Source |
|---|---|---|
| Discharge type | combined DC + HF (capacitively coupled) | K1–K3 |
| HF frequency (water-plasmoid variant) | 0.5 MHz | K1 §2 |
| HF power | 0.5–5 kW | K1 §2 |
| Output voltage (Tesla HF stage) | 40–60 kV | K1 §2 |
| Mean electric power input (PVR, swirl variant) | 0.1–3 kW (stated variously as "<1 kW", "0.2–3 kW", "0.1–1 kW" across K1–K3) | K1 §3, K2 §1, K3 §2 |
| Mean thermal/excess output power | 1–10 kW | K1 §3, K2 §5, K3 §2 |
| Discharge voltage U_d | 1–4.5 kV (varies by sub-experiment) | K2 §3, K3 §2 |
| Plasmoid/droplet electric potential | −(2–8) kV | K1 §2.1, K2 §2 |
| Gas mixture | Ar : H₂O steam, ratios 1:1 to 10:1 | K1–K3 |
| Mass gas flow rate | <10–30 g/s | K1 §3, K2 §1 |
| Swirl (tangential ≈ axial) velocity | ~30 m/s | K3 Fig.2 |
| Static pressure | ~1–2 bar | K1 §3, K3 Fig.2 |
| Erosion electrode mass rate | **<1 mg/s** | K1 §3 |

### I.3 Plasma parameters `[credited measurement]`

| Parameter | Value | Source |
|---|---|---|
| Electron density N_e (PVR, swirl) | ~10¹⁴–10¹⁵ cm⁻³ | K2 §5 |
| Electron density N_e (water-plasmoid variant) | ~10¹³–10¹⁴ cm⁻³ | K1 §2.2 |
| Electron temperature T_e | ~6000–7000 K | K2 §5 |
| Metal-cluster/droplet temperature T_b | ~2000 K | K2 §5 |
| Rotation/gas temperature T_R | <2000–2300 K | K1 §2.2, K2 §5 |
| Vibration temperature T_V (from OH band) | ~4000 K | K1 §2.2 |
| Droplet propagation velocity | ~2–5 m/s | K2 §2 |

### I.4 COP claims — by measurement method `[credited measurement]`, tiered by method rigor

| Regime | COP | Method | Caveat |
|---|---|---|---|
| Shock-wave/WINP (ballistic, pulsed glow discharge) | **4–10** | gas-dynamics conservation laws (`q` from measured ρ₂/ρ₁, P₂/P₁ across shock) | assumes γ=1.4 constant, "chemical reactions are absent" — an *assumption*, not independently checked, for a plasma that elsewhere (K2) is shown to contain reactive metal nanoclusters + adsorbed H |
| Heterogeneous plasmoid, **swirl** flow (PVR) | **2–10** | calorimetry: outlet gas enthalpy vs electrical input, calibrated against a Ni–Cr wire heater in pure Ar | no stated uncertainty budget; no blinded/sham-reactor control; no third-party replication reported *in these papers* |
| Heterogeneous plasmoid, **non-swirl / straight** flow (PVR control) | **0.5–0.7** (i.e. **<1**) | same calorimetry | this is Klimov's own **negative control** — critical data point (§III below) |
| Energy release in swirl gas flow (separate report) | 2–4 | not detailed | K1 §3 |
| Specific energy release (self-estimated) | **q ≈ 1 keV/atom** | inferred from calorimetry ÷ estimated reacting-atom count | see §III.4 — this number is the sharpest confrontation point |

### I.5 Radiation `[credited measurement]`

- Soft X-ray spectrometer (X-123SDD), range 0.1–30 keV; main peaks at E₁≈1.3 keV (near Al Kα 1.487 keV /
  Mg Kα 1.254 keV — electrode-material lines) and E₂=4–4.6 keV (near Ti/V/Cr lines). K2 §3.
- X-ray line identity evolves with distance behind the nozzle (N at 50 mm → O at 75 mm → F at 120 mm →
  Na/Mg/Al at 150–200 mm); Klimov's *own* interpretation invokes "interaction of neutron-like particles with
  the atmospheric chemical elements" — his own speculative gloss, **not** an FTGB claim, **not** independently
  corroborated. K2 §3.
- A neutron detector is present in the K3 apparatus (Fig. 5, item 2) but **no neutron count/flux number is
  reported in the retrieved text** — an honest gap: neither a neutron excess nor a neutron null is
  documented in what was read. `[flag: unreported]`
- "Stimulated α-radioactivity of activated Bi-electrodes" is mentioned once (K1, Conclusions) with **no
  quantitative detail** in the retrieved text. `[flag: unelaborated]`

### I.6 Transmutation / isotope data `[credited measurement]`

- **Lithium isotope shift** (sharpest, most quantitative single number in the record): ⁷Li/⁶Li goes from
  **13.192 ± 0.004** (initial) to **18.996 ± 0.012** (activated water sample). K1 §2.3.
- Li, Ca concentration increase in water by factor 10²–10³. K1 §2.3, Table 1.
- Ni-cathode PVR erosion products (ion mass spec / EDS / ICP-MS): broad multi-element appearance —
  **P, S, Cl, Ca, Fe, Zn** (K2 §4); dusty-particle composition Ni~15%, Si~50%, Fe~9%, Cu~5% vs
  Ni-99.99% initial (K2 Table 1). This is a **broad elemental smear across many species**, not a clean
  discrete `ΔA` pattern.
- Al-cathode PVR erosion: Si, P, S, Cl, Ca, Fe, Zn appear (K3 §3, Fig.7).
- **Decay-instability [flag — methodological]:** K3's central claim is that the *concentrations* of these
  transmuted elements (Fe, Cu, Ca...) measured by EDS/ICP-MS **decrease** over 1 week / 1 month / 6 months,
  and that further weak-plasma (WINP) exposure **accelerates this "decay" by factors of 10³–10⁶** (K3 §3,
  Conclusions). Read as ordinary nuclear decay this is physically anomalous: (a) Fe, Cu, Ca are stable
  elements — if genuinely nucleogenic, the *specific isotopes* produced would need to be unstable with
  half-lives compatible with week-to-month timescales, which is never demonstrated (no γ/β spectroscopy of
  the decaying species is reported); (b) "decay rate" measured purely as *elemental concentration by EDS/
  ICP-MS* cannot distinguish real nuclear decay from surface redistribution, leaching, oxidation, or
  diffusion of a contaminant — all of which are far more parsimonious explanations for a concentration that
  falls under further weak-plasma exposure. **This is flagged as a serious methodological weakness in
  Klimov's own data, independent of and prior to any FTGB confrontation** — it is exactly the class of
  measurement the AUREON/thorium discriminator in Part IV below is designed to exclude (isotope-ratio-level,
  not elemental-concentration-level, evidence is required to claim transmutation).
- Klimov's own proposed mechanism is a **"bi-nuclear atom" model** (Gurevich et al. 2009, cited K3 ref [4]) —
  a non-mainstream, unelaborated theoretical gloss that is **not** the FTGB Skyrme/O_h/E0 mechanism and is
  **not** adopted here; named only to keep Klimov's own interpretation clearly separate from FTGB's.

### I.7 Frequency data actually reported `[credited measurement]` — important negative finding

- The **only** frequency explicitly measured and reported across K1–K3 is the rate of **red luminescence
  flashes inside the water-cluster plasmoid: ~1–10 Hz** (K1 §2.3, Fig. 6 caption region).
- The HF **drive** frequency (an input, not an emergent resonance) is **0.5 MHz = 500 kHz** (K1 §2).
- **No 43–46 kHz spectral feature, resonance window, or "sharp resonance signature" appears anywhere in
  the three primary Klimov papers retrieved and read for this confrontation.** `[flag — provenance gap]`
  This number appears in secondary compilations (an Obsidian-vault note file supplied for this task states
  "resonance at 43 kHz window"; the user's own prior exploratory chat log — `Treating Klimov as a toroidal
  but non-slender...md`, 14458 lines — extensively engages a "Klimov 43–46 kHz" figure) but **could not be
  traced to a primary Klimov publication** in this pass. Two honest possibilities: (a) it is reported in a
  Klimov paper not retrieved here (there are further AIAA/Springer/RCCNT&BL proceedings papers in Klimov's
  reference lists not fetched), or (b) it is a garbled/conflated secondary-source figure. Given the
  measured luminescence-flash rate is 1–10 Hz — **3–4 orders of magnitude below** both the disputed
  43–46 kHz figure and the FTGB carrier comb {121, 208, 294} kHz — **neither figure is supported by the
  primary data actually retrieved.**
- The Obsidian-vault secondary note's "transmutation at 17–20 mg/s" also does **not** match the primary
  record: K1 §3 states the **erosion electrode mass rate is <1 mg/s**, roughly 20–2000× smaller. `[flag —
  provenance gap]` Neither of these two secondary-source numbers should be treated as sourced until traced
  to a specific Klimov publication with page number.

---

## Part II — Thorium-plasma framework and the pre-existing Π-group scaffold

The project's own prior work, `C:\Users\natha\ckfreefem\frontier_calcs\GRAVITY_AND_THORIUM_PLASMA_FRAMEWORK_2026-09-08.md`
(Part IV, lines 404–564), already builds the correct honest scaffold for confronting *any* driven-plasma
reactor claim against FTGB, via dimensionless Π-groups (`β`, `ω/ω_ci`, `d_i/R`, `λ_D/R`, `Λ=n_eR³`,
`Π_mag`), and already carries an AUREON/SAFIRE **prior-art ledger** entry (lines 431–455, 634–645) stating
their claims *as claims*, not adjudicating them, and naming the correct falsifier: **isotope-shift-resolved
+ RF-beat-correlated**, or the scaffold reading is falsified. That file's guardrails (no fabricated nuclear
numbers, scaffold-not-reaction, baryon `B∈π₃(S³)` strictly conserved) are inherited unchanged here; nothing
in this document supersedes it.

Applying that file's Π-set to Klimov's *measured* numbers (§I above) for the first time:

- `β = 2μ₀n_ek T_e/B²` — **cannot be computed**: Klimov reports no magnetic field strength anywhere in K1–K3
  (the PVR uses electric discharge + swirl, not an imposed confining B-field). This is itself informative:
  **Klimov's PVR has no reported magnetic-field diagnostics at all**, so the force-free-Beltrami (`∇×B=λB`)
  reading of the plasmoid — which is precisely the FTGB coherence claim (§III.3 below) — is **structurally
  unfalsifiable from Klimov's own published data**: there is no B-field measurement to check against.
  `[flag]`
- `Λ = n_e R³`: with `n_e~10¹⁴–10¹⁵ cm⁻³` and `R~1–3 cm` (visible plasmoid radius), `Λ~10¹⁴–10¹⁶` — large,
  consistent with a dense, collisional, non-ideal-MHD-marginal plasma; no tension with the framework's
  `β≲O(1)` requirement per se, but also not a discriminating test since `β` itself is unmeasured.
- `ω/ω_ci`: **cannot be computed** without B. The framework's own falsifier (IV.1: "comb-lock must persist
  across `ω/ω_ci` scan through carrier ratios and break off-comb") is **untestable against Klimov's
  published record** for the same reason.

**Honest conclusion of this section:** the thorium-framework's own Π-group scaffold, when actually applied
to Klimov's reported numbers, reveals that **the single most basic diagnostic the FTGB coherence claim
needs — a magnetic field measurement — is absent from Klimov's publications.** This is not a failure of
FTGB; it is a **named, specific data gap** in the reactor program being confronted. Any future confrontation
attempt should prioritize requesting/locating B-field (magnetic probe, Hall sensor, or Zeeman/Faraday
optical) data from Klimov or a replication.

---

## Part III — Confrontation: FTGB LENR predictions vs Klimov data

| # | FTGB prediction | Source | Klimov data | Verdict |
|---|---|---|---|---|
| 1 | Carrier comb {121,208,294} kHz, ratios 1:1.72:2.43 | `LENR_MATTERWAVE_INTERACTION_MODEL_2026-09-09.md:156` | measured: 1–10 Hz flash rate; drive: 500 kHz. **No spectral measurement in the comb's band at all.** | **UNTESTED, and the two numbers commonly associated with Klimov (43–46 kHz, 17–20 mg/s) are themselves unsourced in the primary record (§I.7).** No change to the prior UNTESTED verdict in `EXPERIMENTAL_CONFRONTATION_2026-09-10.md:19`. |
| 2 | Beat law `f_b=(v_A/2πR)\|Δλ\|` | `delta_detuning_beat_check.py` | no spectral data to invert against; the prior illustrative "nested-cavity" fit (R=0.4mm core) used **assumed, not measured**, geometry an order of magnitude below Klimov's actual droplet scale (0.01–0.1mm) and two orders below the reactor scale (60mm) — see `Treating Klimov...md:11481-11642` (already self-labeled "illustrative, not fitted" by the user's own prior exploration) | **UNTESTED.** The beat law has no Klimov data to confront; the one prior fit attempt was honestly non-empirical. |
| 3 | Single-λ Woltjer–Taylor force-free coherence = the LENR scaffold | `plasmoid_helicity_coherence_check.py`; `LENR_YINYANG_CONNECTIONS_2026-09-10.md:36-44` | **Klimov's own negative control is the sharpest data point in this entire confrontation:** COP collapses from 2–10 (**swirl** flow) to 0.5–0.7 / **<1** (non-swirl **straight** flow) — same reactor, same power, same chemistry, only the flow topology (swirl vs. straight) changed (K1 §3). | **STRUCTURALLY CONSISTENT (real, quantified, geometry-dependent signal), MECHANISM UNCONFIRMED.** Vortex/rotational organization is *causally necessary* for the anomalous-COP regime in Klimov's own data — exactly the qualitative shape the "coherent driven vortex scaffold matters" picture predicts. But because no B-field/helicity is measured (Part II), this cannot be elevated past a **structural analogue**: swirl-driven vortex flow ≠ demonstrated force-free single-λ Beltrami plasma. This is the **strongest genuine connection** in the whole confrontation, and it is honestly bounded. |
| 4 | Aneutronic selector (O_h/E0/isospin) ⇒ no hard γ, He-4 signature | `LENR_MATTERWAVE_INTERACTION_MODEL_2026-09-09.md:107-109` | **No helium measurement of any kind** in K1–K3. Soft X-ray only to 30 keV (consistent with "no hard γ" in the weak sense that nothing harder is reported, but this is silence, not a measured γ-null). Neutron detector present (K3 Fig.5) but **flux/count not reported** in retrieved text. | **UNTESTED** (no He-4 assay; γ/n data incomplete-as-reported, not a confirmed null). Cannot be elevated to CONSISTENT without a He-4 measurement Klimov does not report. |
| 5 | B=4 Landau–Zener Δ, target 1.4–1.9 MeV band | `LENR_MATTERWAVE_INTERACTION_MODEL_2026-09-09.md:61-65, 102-106` | no nuclear-spectroscopic data of the kind that could test a specific MeV-scale gap; this remains an internal, `handoffs/`-scoped HPC compute, not something reactor calorimetry/EDS data can test | **UNTESTED, and structurally cannot be tested by Klimov-class data** — a genuine scope mismatch to flag, not a failure of either side. |
| 6 | He-4/heat = 24 MeV signature | `LENR_MATTERWAVE_INTERACTION_MODEL_2026-09-09.md:138-139` | no He-4 measurement (see #4); Klimov's *own* self-estimated specific energy release is **q ≈ 1 keV/atom** (K2 Conclusions #4) — **not** 23.85 MeV/⁴He. These two numbers differ by a factor of **~24,000**, and no fraction-of-reacting-atoms figure is given to reconcile them. | **UNTESTED / not comparable as reported.** 1 keV/atom (bulk-averaged, Klimov's own number) sits in a physically ambiguous zone — far above ordinary chemical bond energies (~eV/atom) but ~4 orders below MeV-scale nuclear Q-values — and Klimov supplies no data (active-atom fraction, He yield) that would let this be checked against the FTGB signature either way. |
| 7 | Transmutation on a baryon-conserving Skyrme/Nielsen lattice, ΔA=4n favored | `LENR_MATTERWAVE_INTERACTION_MODEL_2026-09-09.md:69-72, 78-79` | Klimov's products (Fe, Cu, Zn, Si, P, S, Cl, Ca, Mg, Na, K from a Ni or Al cathode) are a **broad multi-element smear across many ΔZ/ΔA values**, not a discrete ΔA=4n pattern. This lands on the **CONSTRAINED (scattered, Mizuno/Miley-type)** side of the prior verdict in `EXPERIMENTAL_CONFRONTATION_2026-09-10.md:99-115`, not the CONSISTENT (Iwamura) side. | **CONSTRAINED — Klimov's data is a fresh instance of the field-wide "no clean lattice pattern" bucket**, reinforcing (not weakening or strengthening beyond) the prior verdict. Baryon conservation is guaranteed by ordinary nuclear physics regardless of mechanism, so it is not itself discriminating. The K3 "decay-instability" claim (§I.6) is additionally a methodological red flag independent of FTGB (elemental-concentration data cannot establish nuclear decay). |
| 8 | COP>1 = nuclear/chemical energy ratio (~10⁴–10⁵×), energy-conserving, not over-unity | `LENR_MATTERWAVE_INTERACTION_MODEL_2026-09-09.md:20-22`; `lenr_cop_nuclear_positive.py` | Klimov's measured COP values are **2–10**, not 10⁴–10⁵. | **The magnitude gap is the central honest finding of this confrontation (see §III.4 below): Klimov's COP is fully in the range explicable by ordinary exothermic plasma-chemistry (eV/atom-scale electrode-erosion/oxidation reactions) at a kW-scale input, with no need to invoke MeV-scale nuclear energy at all.** Klimov's data neither supports nor excludes FTGB's nuclear-source claim — it is simply **the wrong energy regime to test it**, because Klimov's own reported energy accounting (§I.4 caveats) never isolates or excludes a chemical term. |
| 9 | Plasmoid aspect ratio A ≈ φ ≈ 1.618 (corrected from erroneous A≈9) | `EXPERIMENTAL_CONFRONTATION_2026-09-10.md:139-144` | Plasmoid length ≈ electrode gap = 80 mm; plasmoid appears (from K2 Fig. 2/4 images) to roughly span the 60 mm tube diameter ⇒ **inferred aspect ratio ≈ 80/60 ≈ 1.33**. | **CONSISTENT-order-of-magnitude, tentative.** 1.33 sits between the real-spheromak range (1.1–1.4, already noted as a favorable SSPX near-miss) and FTGB's own `A≈φ=1.618` (~18% above 1.33). This is a **new, honest, favorable data point**, but it is an *inference* from a schematic description and photographs, not a number Klimov states as "plasmoid aspect ratio" — flagged `[S, inferred-from-published-geometry]`, not a direct measurement match. |

### III.4 The sharpest finding: COP magnitude, not mechanism, is the real test — and Klimov's data does not reach it

This is the single most important honest result of this confrontation. FTGB's positive core claim
(`lenr_cop_nuclear_positive.py`) is explicitly **quantitative**: a nuclear `d+d→⁴He` event releases 23.85 MeV
against a chemical/screening trigger of hundreds of eV, so **once such reactions occur, COP is automatically
~10⁴–10⁵**, not a modest 2–10. Klimov's PVR reports COP **2–10**, a range fully within reach of ordinary
plasma chemistry: metal-electrode erosion in an Ar–H₂O-steam discharge, subsequent oxidation of the exposed
metal droplets/nanoclusters, and recombination of dissociated H/OH radicals are all exothermic processes at
the **eV-per-atom** scale, and at kW-scale electrical input with gram/second-scale mass throughput these are
easily sufficient in magnitude to produce a factor-of-2-to-10 enthalpy excess **without any nuclear
contribution**. Klimov's own energy accounting (§I.4) never isolates a chemical term — no measurement rules
out ordinary combustion/oxidation chemistry of the eroding electrode as the source of the reported COP.

**This means Klimov's data is not evidence for the FTGB nuclear-source mechanism, but it is also not
evidence against it — it is simply the wrong magnitude regime to discriminate.** A COP of 2–10 is
*consistent with either* (a) no nuclear process at all (pure plasma-chemistry) or (b) a small fraction of
atoms undergoing genuine nuclear reactions, heavily diluted by non-reacting bulk (which is one reading of
Klimov's own "q≈1 keV/atom" estimate — small compared to 23.85 MeV/atom, large compared to eV/atom). Neither
Klimov's papers nor this confrontation can distinguish these without a **He-4 assay** (the one measurement
FTGB's own model names as decisive, §III row 6) or an **isotope-ratio-level** transmutation measurement
(the Li7/Li6 shift, §I.6, is the one number in Klimov's record that reaches this bar — and it is not
accompanied by any energy-balance correlation that would tie it to the reported COP).

---

## Part IV — AUREON Energy / SAFIRE: claims-as-read, gated by the rigorous discriminator

### IV.1 What is publicly claimed (claims-as-read, not adjudicated)

Per the coordinator's brief and confirmed by a targeted web search against aureon.ca and e-catworld coverage
(2026-09-10 pass):

- **Montgomery W. Childs** is the founder/chief scientist of Aureon Energy, Ltd. and creator/lead of the
  SAFIRE Project (an electrically-driven dense plasma sphere, originally built to test the "electric sun"
  solar model). All SAFIRE IP/hardware has been transferred to Aureon Energy.
- Associated figures named in the coordinator's brief: **Hal Puthoff** (IAS Austin — vacuum/EM theory,
  explicitly **not** the operational lead) and **David Nagel** (an independent LENR evaluator).
- **Claim (fall 2023, SAFIRE III):** a table-radio-sized reactor introduced a **liquid medium** (replacing
  gas) and, per the program's own public statements, "transmuted thorium into many stable non-radioactive
  daughter elements," described in program language as accelerating decay "from 14 billion years to
  minutes." The program states results were "validated by a third-party professional laboratory in the
  U.S." — **no report, methodology, or dataset from that validation was located in this pass.**
- **2025 development:** public statements describe a proposed "thorium-fueled, electrically initiated power
  cell" — an AUREON Micro Reactor / Elemental-Transmutation-Reactor concept for combined waste remediation
  and heat recovery.
- **No verifiable technical parameters** — geometry, input power, voltage, current, drive frequency,
  plasma density, magnetic field strength, isotope-ratio data, calorimetric uncertainty budget, or any raw
  measurement — were located in public sources during this pass. **This is stated plainly rather than
  invented:** the claims above are qualitative/promotional-language claims from the program's own public
  communications (aureon.ca, aureonenergy.com, e-catworld coverage), not a peer-reviewed dataset. This
  matches and does not update the project's own prior prior-art ledger entry, already on file at
  `C:\Users\natha\ckfreefem\frontier_calcs\GRAVITY_AND_THORIUM_PLASMA_FRAMEWORK_2026-09-08.md:433-440,
  636-638` — this confrontation adds no new numbers to that entry, only confirms it is still current.

### IV.2 The rigorous discriminator (per coordinator brief — applied here as the honest gate)

Any claim of thorium transmutation + excess heat, from AUREON or any other program including Klimov's,
should be gated by three **separable** measurement legs, each independently falsifiable:

1. **Isotopic change** — pre/post high-precision ICP-MS/TIMS **isotope ratios**, certified standards,
   blinded controls. (Klimov's Li7/Li6 shift, §I.6, is the one number in this whole confrontation that
   reaches *isotope-ratio* resolution — but it is a **lithium appearance/disappearance in water**, not a
   thorium decay-chain measurement, and carries no stated blinding or third-party replication.)
2. **Nuclear products** — calibrated, time-correlated radiation spectroscopy (α/β/γ/n) + product assay in
   an internally-consistent balance. (Klimov's soft-X-ray + unreported-neutron-count data, §I.5, does not
   reach this bar; AUREON's public claims supply no spectroscopy at all in what was located.)
3. **Net energy** — closed/calibrated flow calorimetry with full power accounting:
   `E_excess = E_thermal,out − E_electrical,in − E_chemical − E_stored`, uncertainty propagated per term.
   (Klimov's calorimetry, §I.4, omits the `E_chemical` term entirely — §III.4's central finding. AUREON's
   public claims supply no calorimetric data at all in what was located.)

**Additional requirement for a claim at the "days→minutes" scale AUREON makes:** because Th-232's half-life
is ~14 Gyr, any claimed transformation needs a **closed-system inventory balance** (isotope loss ↔
identified daughter products ↔ energy released, all mutually consistent), not merely a changed elemental
spectrum — this rules out precipitation, adsorption, incomplete recovery, isotopic fractionation, and
matrix/instrumental artifacts as alternative explanations. **Blinding** (active/sham reactors externally
indistinguishable, randomized labels held by a third party, samples split across ≥2 independent labs,
certified Th standards + matrix-matched blanks, spike-recovery tests, pre-registered success criteria) is
the standard that would make such a claim decisive.

### IV.3 Applying the discriminator evenhandedly

Neither Klimov's peer-reviewed-proceedings PVR data nor AUREON's public SAFIRE claims currently meet all
three legs at this rigor. This is stated **evenhandedly, not as a special standard invented for AUREON**:
Klimov's papers (§I) do not report blinding, sham controls, independent replication, or a closed isotope/
energy inventory either — his COP method (§III.4) and his "decay-instability" claim (§I.6) both fail the
same bar for the same structural reason (elemental/enthalpy measurements standing in for isotope-ratio/
energy-balance ones). **AUREON's public claims currently supply *less* raw data than Klimov's published
papers** (no geometry, no power numbers, no spectra located), so AUREON sits at a **lower** evidentiary tier
than Klimov in this specific comparison — "claims-as-read," gated, unconfirmed, with the specific missing
legs named above as the concrete, actionable request to the program (not a dismissal of it).

### IV.4 The conceptual bridge — where FTGB's geometry does and does not match

The coordinator's framing (input power → driven plasma/sheath/vortex → localized field & density structure
→ nuclear/isotopic change + heat) maps as follows onto the FTGB single-λ Woltjer–Taylor plasmoid + carrier-
comb picture:

- **Matches, structurally:** both SAFIRE (electrode-sheath double-layer geometry) and Klimov (vortex/
  recirculation geometry) are **driven, boundary-organized plasma structures**, smaller and more organized
  than the bulk discharge — exactly the "scaffold, not reaction" picture FTGB's own thorium framework
  already commits to (`GRAVITY_AND_THORIUM_PLASMA_FRAMEWORK_2026-09-08.md:40-44`). Klimov's swirl-vs-
  straight-flow COP contrast (§III row 3) is the best available *quantified* evidence that geometry/
  coherence, not raw power, drives the anomalous regime — consistent with (not proof of) that picture.
- **Does not match, or is untestable:** FTGB's *specific* carrier comb and beat-law numbers have no
  spectral data to confront in either program (§III rows 1–2); the force-free/helicity claim has no B-field
  data to confront in Klimov and no plasma diagnostics at all in AUREON's public materials (§II); the
  aneutronic/Δ/He-4 nuclear-mechanism claims have no He-4 or γ/n data to confront in either program
  (§III rows 4–6). SAFIRE's geometry (a driven plasma **sphere** with a liquid medium) is a genuinely
  **different topology class** from Klimov's **vortex/swirl tube** — both are read here as candidate
  driven Beltrami-Hopf plasmoids `[S]`, but they should not be conflated as "the same reactor" when
  confronting either against FTGB.

---

## Part V — The firewall, restated for this confrontation

- **Baryon-conserving transmutation/fusion** (Klimov's reported ΔZ/ΔA elemental shifts, AUREON's claimed
  Th-daughter products, FTGB's `d+d→⁴He`) is kept **strictly distinct** from any baryon-decay speculation.
  Nothing in this document, Klimov's papers, or AUREON's public claims proposes `ΔB≠0`; where FTGB's own
  `[S]` extensions touch baryon-adjacent speculation elsewhere in the project, they are walled off from this
  confrontation entirely (not engaged here).
- **`[V]` verified-core** results used in this confrontation (the mass-defect arithmetic in
  `lenr_cop_nuclear_positive.py`; the CK-eigenvalue comb structure in `delta_detuning_beat_check.py`; the
  Beltrami helicity identity in `plasmoid_helicity_coherence_check.py`) are **not challenged** by any
  reactor data here — they are internal-consistency computations, and no external measurement bears on
  their correctness as identities. What the reactor data *does* bear on is the **`[S]` application** of
  those identities to real devices, which is what §III scores.
- **COP>1**, wherever real in this confrontation (Klimov's 2–10), is explicitly **not** claimed here as
  free energy or as confirmed-nuclear; §III.4 states plainly that Klimov's own data cannot currently
  distinguish a chemical from a nuclear origin, and that FTGB's own ~10⁴–10⁵× claim is the sharp,
  falsifiable, currently-unmet target that would settle it.

---

## Bottom line

**Does the reactor data advance, constrain, or leave unchanged the FTGB LENR layer?** Mostly **leaves
unchanged with two genuine, specific movements** — one positive, one clarifying:

1. **Positive (real, bounded):** Klimov's own swirl-vs-straight-flow COP contrast (2–10 vs. <1) is the
   single most concrete piece of evidence in this whole confrontation that **coherent/vortex organization
   causally matters** to whatever anomalous-energy regime Klimov's PVR accesses — structurally consistent
   with (not proof of) FTGB's driven-coherent-scaffold picture, and honestly bounded by the total absence of
   any magnetic-field/helicity measurement in Klimov's published record (Part II) that would let the
   *specific* Woltjer–Taylor/single-λ claim be tested rather than merely analogized.
2. **Clarifying (a real negative, cleanly stated):** the widely-repeated "Klimov 43–46 kHz" and
   "17–20 mg/s" figures could **not** be traced to Klimov's own primary papers in this pass (§I.7) — the
   only frequency Klimov reports is 1–10 Hz, and the only mass rate is <1 mg/s, both far from the secondary-
   source numbers. This does not overturn the prior UNTESTED verdict on the carrier comb
   (`EXPERIMENTAL_CONFRONTATION_2026-09-10.md:19-30`), but it removes a specific pseudo-anchor and converges
   with the user's own earlier, independent exploration (`Treating Klimov...md`), which had already reached
   the same negative by a different route (the slender-torus beat law cannot honestly derive that band).
   Two independent honesty checks landing on the same negative is itself a small positive for the project's
   discipline.
3. **The sharpest open finding (§III.4):** Klimov's measured COP (2–10) is in the *wrong energy regime* to
   test FTGB's *specific* ~10⁴–10⁵× nuclear-to-chemical claim, because Klimov's own calorimetry never
   isolates a chemical (electrode-oxidation) energy term. **The decisive future measurement, for either
   program, is a He-4 assay correlated with excess heat** — the one number FTGB's own model names as
   decisive and that neither Klimov's papers nor AUREON's public claims currently supply.
4. **AUREON/SAFIRE** remains, as the project's own prior thorium framework already stated, a **claims-as-
   read, prior-art-ledger entry** — gated by the same three-leg discriminator (isotopic, nuclear-product,
   net-energy) applied here evenhandedly to Klimov as well, and currently supplying *less* raw public data
   than Klimov's peer-reviewed-proceedings papers.

No FTGB number was strengthened or weakened by this confrontation; two provenance errors were caught and
corrected (§I.7); one real, quantified, structurally-relevant experimental fact (the swirl/COP contrast) was
newly connected to the theory's own coherence claim, honestly bounded; and one sharp, actionable, falsifiable
future test (He-4 assay vs. excess heat, on either Klimov's or AUREON's apparatus) was identified as the
measurement that would actually discriminate FTGB's nuclear-source claim from ordinary plasma-chemistry.

*Provenance: Klimov papers K1/K2/K3 fetched directly from jcmns.org and read in full (PDF text extraction);
AUREON claims checked via targeted web search against aureon.ca / e-catworld (2026-09-10); thorium framework
cross-referenced at `C:\Users\natha\ckfreefem\frontier_calcs\GRAVITY_AND_THORIUM_PLASMA_FRAMEWORK_2026-09-08.md`;
FTGB LENR layer at `results/LENR_MATTERWAVE_INTERACTION_MODEL_2026-09-09.md`,
`results/LENR_YINYANG_CONNECTIONS_2026-09-10.md`, `results/EXPERIMENTAL_CONFRONTATION_2026-09-10.md`, and
`results/verify/{lenr_cop_nuclear_positive, delta_detuning_beat_check, plasmoid_helicity_coherence_check,
carrier_chirality_lock_check}.py`. No verify script, engine file, or TIER_LEDGER was modified. No number in
this document was fabricated; every quoted figure is either read directly from a cited primary source, a
direct FTGB-repo reference, or explicitly flagged as an inference/estimate.*
