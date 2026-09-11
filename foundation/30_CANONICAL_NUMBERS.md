# 30 · Canonical Numbers — the single source of truth (foundation anchor table)

**Foundation tier · the load-bearing numbers the toolkit modules rest on.** This is the **one
authoritative place** for every load-bearing number, design point, and convention the FTGB theory uses.
The method modules (M7–M15) and the synthesis cite this file for their anchors — e.g. M7-2 reproduces the
carrier comb of §I "to the digit," M7-2 reads the `c_CK` conventions of §C, and M9 draws the comb from §I.

> **Provenance — now self-contained.** Values re-sourced from live `frontier_calcs/` scripts on 2026-08-11,
> not recalled. **Those provenance scripts are now VENDORED (frozen) into this repo under
> [`frontier_calcs/`](../frontier_calcs/)** (10 scripts + manifest), so every cited path resolves in-repo —
> the foundation no longer depends on the external corpus. The load-bearing *derived* numbers (`v_A`, `B`,
> `b_eff`, `ħ_eff`, `d_i`) are additionally **re-derived from the anchors, CI-gated**, by
> `results/verify/canonical_numbers_provenance_check.py` (≤0.1%). Reorganized here
> to the jewel's honesty discipline: a tier tag on every row, residual/ansatz labels preserved verbatim,
> and a note where a value is a self-consistency residual rather than a measurement. No number was changed
> in import. Excised numerology (the `e^(-2/3)` screening factor, the Storti radii/H₀/α "derivations") does
> **not** live here — see `results/EXCISION_LEDGER.md`; this ledger carries only anchors, residuals, and
> derived dimensionless ratios.

## Tier legend (honesty discipline — as in `TOOLKIT_HANDBOOK.md` §2)
- **[V]** — recomputed here / by a named `frontier_calcs` script, or a checked identity.
- **[credited]** — established physics or a literature-sourced measurement we build on.
- **[S]** — structural / contingent: a conditional identity or a value not closed on our side.
- **[residual]** — ⚠ a **self-consistency / algebraic residual, NOT an independent measurement**. Carries a
  labeled uncertainty band; anything scaling from it inherits that band (stated per row). Never quote a
  residual as a measured field/frequency.
- **[ansatz-band]** — value depends on the closure ansatz; quote the **band, ~1 digit**, not 6 figures.
- **[prediction]** — a calibration-free, falsifiable prediction (§G); no fit enters.
- **[flag]** — a coincidence held but **not** promoted (gated at the 0.5% anti-numerology bar).
- No fabricated numbers. Two-convention / two-design-point items are flagged — these are the traps; read
  the flag before quoting.

### Rules for using this file
1. **Cite here, don't re-derive.** If a doc quotes a number, it must match a row below.
2. **Verify at source before changing.** Each section names its source script. To change a value, re-run
   that source and update here first — never blind-`sed` a number across the corpus.
3. **Dimensionless ratios are robust; absolute fields/frequencies carry the `v_A` residual.** See §A.

---

## A. Plasmoid calibration constants (the medium)   [anchors]
Source: `frontier_calcs/ws5_hbar_b_eff_reduction_to_medium.py` (re-run 2026-08-11).

| Symbol | Value | Tier | Meaning / source |
|---|---|---|---|
| `Γ_dim` | **≈ 1** (band 0.92–0.999) | **[ansatz-band]** | FPUT saturation growth rate `= Γ(k=2/R_dim)`, `Γ(k)=√(k²−k⁴/4)`; the genuine universal is the MI **max growth = 1 at k=√2** (eqn-defined, **[V]**). 0.998742 is where R_dim lands near that peak. Not a 6-fig universal. |
| `R_dim` | **≈ 1.4** (band 1.20–1.60) | **[ansatz-band]** | dimensionless breathing radius (log-normal 1.201 / Gaussian-O(w⁴) 1.380040 / shifted-exact 1.597 — bracket straddles √2). Quote the band, ~1 digit. Everything algebraic in R_dim (σ₀/R, κ₂, b_eff coeff) inherits this. |
| `m_i` | **29 AMU = 4.816×10⁻²⁶ kg** | **[credited]** | mean air-ion mass [US Standard Atmosphere 1976: M(air)=28.9647 g/mol]; ✓ sourced |
| `τ_alfvén` | **5.9039×10⁻⁶ s** | **[S/residual]** | Alfvén timescale `= R/v_A` (inherits the v_A residual below) |
| `R` (`r_ball`) | **0.12 m** | **[credited]** | object radius (diam. 0.24 m) [Stenhoff 1999, ~4587 reports: most-probable 10–50 cm, mean ~20 cm]; ✓ sourced (luminous diameter) |
| `v_A` | **2.033×10⁴ m/s** | **[residual]** | ⚠ **self-consistency residual, NOT independently measured** — originally computed from `B0=50 mT, n_e=10²⁰ m⁻³`, a density 6× the `n_i` below |
| `B` | **20.6 mT** | **[residual]** | ⚠ **algebraic residual** `= v_A √(μ₀ n_i m_i)` back-solved with `n_i=1.7×10¹⁹` — NOT a measurement; ~10–20× below SSPX edge field (0.2–0.4 T, Hill 2000) and BL near-channel (0.32–0.47 T, Uman) |
| `n_i` | **1.7×10¹⁹ m⁻³** | **[credited]** | ion density — SSPX-sourced [Hill et al., UCRL-JC-137828, 2000; range 1×10¹⁹–1.3×10²⁰]; assumes `n_i=n_e` (unstated) |
| **`b_eff`** | **1.0420×10⁻¹⁷ J = 65.04 eV** | **[V]/[residual]** | ⚠ recomputed from calibration (not 1.047e-17 / 65.4 eV — stale); inherits the v_A residual **square-law** (see blast-radius) |
| **`ħ_eff`** | **6.1594×10⁻²³ J·s** (5.84×10¹¹ × real ħ) | **[V]/[residual]** | ⚠ recomputed (not 6.175e-23 — stale); emergent/size-dependent, **not** a fundamental constant; inherits the v_A residual **linearly** |

**Closed forms (match calibration to 1.0000×)   [V].**
- `b_eff = (Γ_dim/R_dim)² · m_i · v_A²` — **object size R cancels → a pure MEDIUM property.** Physically
  `b_eff = 1.047 × (B²/2μ₀ n_i)` ≈ **the magnetic energy per ion** (derived, universal; not a fit).
- `ħ_eff = (Γ_dim/R_dim²) · m_i · v_A · R` — emergent action, **scales with object size R** (as it must).
- Honest scope: `ħ_eff` is emergent/size-dependent, **not** a fundamental constant.

**⚠ Blast-radius of the B/v_A residual (anchor audit 2026-08-23; ★ SQUARE-LAW corrected 2026-08-27 [T2],
`frontier_calcs/tension_T1_T2_resolution.py`).** Because `b_eff ∝ v_A²` and `ħ_eff ∝ v_A`, the two scale
**differently** and must be quoted separately:
- the **absolute frequency ladder `{27,121,4–8} kHz`** and `ħ_eff` inherit the residual **linearly**
  (~2.4× for the `B0=50 mT` re-anchor `v_A'≈4.9×10⁴`; ~5–13× for the wider air-scaled range);
- **`b_eff` (65 eV) and the anapole `≈293 eV` inherit it SQUARE-law → ~5.8× (re-anchor) to ~170× (wide
  range)** — i.e. `b_eff` could be ~0.4–11 keV and the anapole ~1.7–49 keV.

**What is UNAFFECTED (all dimensionless / ratios)   [V]:** `λ₁R=4.4934`, `ε=1/φ`, `c_CK`, `κ₂/κ₄`,
`σ₀/R=0.362`, GL `κ≈6.8`, the **beat ratio `f_b/f_c`** (anchor-immune — ★ DERIVED FROM GEOMETRY
2026-08-27 [T1], `frontier_calcs/tae_beat_from_geometry.py`: a rigorous FreeFEM `H(curl)` eigensolve at
ε=0.697 gives the convention-independent splitting `Δλ=0.2806`, i.e. `f_b/f_c ≈7%`, band 6–8%; a 14-point
small-ε scan (`frontier_calcs/beat_smalleps_scan.edp`) SETTLES the scaling: the **raw gap Δλ is LINEAR in
ε** — first-order toroidicity, `Δλ=0.208·ε = ε/(2j₀₁)`; the earlier `∝ε²` was a carrier-normalization
artifact. **Report the invariant Δλ, not a scaling label.**), the octahedral fold, the entire mass/gauge
tower, `sin²θ_W`. So the STRUCTURE and RATIOS are robust; only ABSOLUTE fields/frequencies carry the
residual.

**Search result (2026-08-23, primary sources read).** No independent AIR-object (B,n) pairing exists in
the literature: Versteegh 2008 (water plasmoid) has density but NO field; Uman is field-only/wrong-object;
Cen 2014 & Yuan 2025 have neither; force-free BL models are circular. The ONLY real single-system
(B,n,species) triple is **SSPX [Hill 2000]: B≈0.2–0.4 T, n≈1×10¹⁹–1.3×10²⁰ m⁻³, HYDROGEN (m_i=1 amu)**.
Mass-scaled to air (29 amu) this implies **v_A ≈ 1–2.6×10⁵ m/s — 5–13× the current 2.033×10⁴**.
**DECISION — HYBRID:** keep the residual label + the SSPX light-ion sanity bound (the re-anchor to SSPX
remains available as a bounded 5–13× shift in ALL absolute fields/frequencies — not a fit; dimensionless
ratios unchanged either way). FRC (FRX-C/LSX, C-2W) and DPF are candidate system-classes to *tighten* the
residual (open); the `>1000 T` EVO claim stays **EXCLUDED** (material-damage inference, do-not-cite). **Do
NOT invent a replacement value (= a new fit).**

---

## B. Topological protection — mesoscopic TYPE-II, winding held topologically
Source: `frontier_calcs/qhd_coherence_carrier_mass_resolution.py` (2026-08-12, RESOLVED).

**Carrier-mass resolution.** `ħ_eff` and `b_eff` are both *per-ion* quantities, so self-consistency fixes
the mass in the coherence length `ξ = ħ_eff/(2√(b_eff · m*))` to the **ion mass `m_i`**. With `m* = m_i`
the ion mass **cancels** and `σ₀/R = 1/(2 R_dim)` is invariant across gas species, density, and field —
BUT it is **[ansatz-band]**, not 6-figure: it inherits R_dim's ansatz spread → **σ₀/R ≈ 0.36 (band
0.31–0.42)** (Gaussian-O(w⁴) value 0.362). A dynamical-collective-coordinate ratio, not a pure geometric
number.

| Symbol | Value (self-consistent, `m_i`) | Tier | Meaning |
|---|---|---|---|
| `ξ = σ₀` | **0.0435 m** (43.5 mm) `= 0.362 R` | **[V]/[ansatz-band]** | coherence length `= ħ_eff/(2√(b_eff m_i))`; **< object** |
| `λ_L = d_i` | **0.2963 m** (296 mm) | **[V]** | penetration depth = ion skin depth `c/ω_pi` at `m_i` |
| **`κ = λ_L/ξ`** | **≈ 6.8** | **[V]** | Ginzburg–Landau parameter → **TYPE-II** (`> 1/√2 = 0.7071`) |

**Verdict [V]:** the object is a mesoscopic **type-II** condensate (`ξ ≈ 0.36 R` always sits inside it, for
any gas/density/field). Quantized vortices are geometrically admissible, **but the winding is still
conserved — held topologically** by the Hopf charge `Q_H = 1` and the conserved Madelung winding number
(0 observed phase slips across the driven runs are consistent with this).

> **Resolved 2026-08-12.** The earlier **TYPE-I** result (`σ₀ = 0.233 m`, `κ = 0.237`) used the **proton
> mass** in `ξ`/`d_i` — inconsistent with `m_i = 29 amu`; it broke the `m_i` cancellation and inflated `σ₀`
> by `√29 = 5.4×`. Superseded; the conserved-winding *observation* is unchanged — only the mechanism label.

---

## C. Beat-law prefactor `c_CK` — ⚠ TWO CONVENTIONS (notation collision)
Source: `frontier_calcs/ws6_cCK_convergence_and_analytic_limit.py`; the notation-collision registry;
`MATH_TOOLKIT_BASE.md` §10.

Beat law: `f_b = c_CK · ε · v_A / (2πR)`. The prefactor has **two live definitions — always state which:**

| Convention | Definition | Value | Tier | Used in |
|---|---|---|---|---|
| **Thesis / 2D** | `c_CK = (λ₁−λ₀)/ε` | **≈ 0.21** | **[V/convention]** | `TOROIDAL_SYNTHESIS_MASTER_THESIS`, Core Preview |
| **Cascade / 3D** | `c_CK = (λ₁−λ₀)/ε²` | **≈ 0.58** (range 0.58–1.16) | **[V/convention]** | `ICCF27_SELF_SIMILAR…`, `FRACTAL_TOROIDAL…` |

- The two differ by a factor `ε` (2D-vs-3D mode splitting). At `ε=0.697` they differ by 1.78×. **Not an
  error — a convention.** BOTH are canonical (user decision 2026-08-11): keep each self-consistent within
  the paper that depends on it. Do **not** "reconcile" by editing one to match the other.
- **Convention-independent anchor (the bridge)   [V]:** `c_CK(ε→0) = 1/(2·j₀,₁) = 0.20792` (`j₀,₁` = first
  zero of `J₀`; reproduced by `results/verify/ck_eigenvalues_check.py`). Matches the FreeFEM sweep `0.2080` at ε=0.05 to **0.04%**. Both conventions reduce to this
  limit — it is what makes either value "a coefficient with a derived limit," not a bare fit.
- **Cross-check rule:** in any single document, `c_CK` must appear in one convention throughout; verify the
  `ε`-power matches the paper's dimensional setup (2D vs 3D) before quoting a value.
- **✓ 3D value HARDENED (2026-08-13) — value unchanged, now ground-truth-validated + continuum-converged
  [V].** A full vector `H(curl)` FEM (`frontier_calcs/stage3_torus_doublet.edp` + `stage3_sphere_validate.edp`,
  FreeFEM 4.16) was **validated against the closed-form PEC-sphere spectrum** — the CK mode `kR=4.49341`
  recovered to **0.08%**, full TM/TE ladder (2.744, 3.870, 4.493, 4.973, 5.763) and degeneracies matched —
  then run at `ε=0.697` across a 3-mesh gmsh family (26k–89k DOF) with Richardson extrapolation:
  **`Δλ=0.2806`, `c_CK(÷ε²)=0.578±0.002`, `c_CK(÷ε)=0.403±0.002`**. Small-`ε` stays anchored by the exact
  limit `1/(2j₀,₁)=0.20792`. This is the deferred Stage-3 "3D closure" — now **closed**.

---

## D. Benchtop quadruplet — ⚠ TWO DESIGN POINTS
Source: `frontier_calcs/benchtop_quadruplet_decisive_neumann_crosscheck.py` (independent Neumann
double-integral), `benchtop_quadruplet_independent_circuit_crosscheck.py`.

Four tilted 5-cm rings, g-equivariant geometry, skip-one-dominant coupling. **The frequency spectrum
depends on the wire gauge + target f₀ — quoting the wrong design point is a known near-miss trap.**

| Design point | Wire | f₀ | Spectrum (MHz) | Span | `k13` | Tier / Status |
|---|---|---|---|---|---|---|
| **CANONICAL (papers)** | **6 AWG** | **5 MHz** | **4.743, 4.761, 5.251, 5.333** | 0.590 MHz (12.4%) | **−10.71%** | **[V]** — Neumann reproduces to the digit |
| earlier (design log) | 18 AWG | 2 MHz | 1.920, …, 2.083 | 8.2% | −7.52% | superseded; do **not** quote in papers |

- Skip-one coupling dominates: `k13 = −10.71% ≫ k12 = +0.90%`; the ratio `k13/k12 = −11.9` is
  normalization-independent (= the geometric `M13/M12`) — an independent confirmation of the coupling-
  topology claim **[V]**.
- ⚠ **CORRECTED 2026-08-13:** the earlier `k12 = +0.63%` was wrong (implied ratio −17.0, inconsistent with
  the geometric −11.9); re-verified `M13/M12 = −2.202e-8/1.850e-9 = −11.9`, so `k12 = +0.90%`.
- **Rule:** the papers quote the **6-AWG/5-MHz** spectrum. Never edit these toward the 2-MHz numbers.

---

## E. Driven / undriven heartbeat dynamics
Source: driven/undriven detached runs (`driven_R*.txt` logs).

| Quantity | Value | Tier | Meaning |
|---|---|---|---|
| Undriven troughs | 0.494 → 0.386 → 0.568 (ρ/ρ₀) | **[V]** | bounded damped spiral (saturating, not singular) — 3-trough decisive run |
| Undriven period | 3.0 → 4.4 | **[V]** | lengthening as it damps |
| Driven `R=1` | **sustained bounded heartbeat** | **[V]** | continuous dissipative time-crystal / Stuart–Landau limit cycle |
| **`R*` (onset)** | **≈ 1.0** (0.95 ± 0.05) | **[V]** | R≤0.9 damp, R=1.0 sustained; drive=dissipation balance. `≪ 31` → real drive suffices |
| **`ω₀` (onset freq)** | **1.579 ± 0.020 run-units = 42.6 kHz** | **[V]** | heartbeat period T₀=3.98; = 1.58× Alfvén rate (nonlinear breathing) |
| **`ω₀ = 2π f_b` ?** (single-mode) | **NO — fails ×11.5** | **[V]** | onset = single-mode breathing (42.6 kHz) ≠ n0/n1 beat (`f_b`≈4–8 kHz); beat needs 2-mode model |
| **`ω₀ = 2π f_b` ?** (two-mode) | **RECOVERED — conditional** | **[S]** | n₀/n₁ doublet with splitting Δ=c_CK·ε recovers the identity under coexistence / anapole phase-locking (β<1); FAILS under competition (β>1) |
| winding | **1.000** (zero phase slips) | **[V]** | conserved at every R to 2.2e-16, even at min `ρ/ρ₀ = 0.093` (R=1.0) |
| `N_THETA` | 19 | **[V]** | resolution-confirmed (trough 0.4936 vs 0.4941 at higher res, −0.1%) |

✓ *Resolved 2026-08-18:* 6-point R-scan onset fit. **Identity `ω₀=2πf_b` FALSIFIED ×11.5 in the single
mode** (the driven heartbeat is the Madelung ring's nonlinear breathing, not the two-CK-mode beat).
Time-crystal *existence* supported; *beat=heartbeat frequency* identity recovered only in the two-mode
n₀/n₁ doublet, conditional on coexistence / anapole phase-locking (β<1).

---

## F. Topological invariants
| Symbol | Value | Tier | Note / source |
|---|---|---|---|
| `Q_H` (Hopf) | **1.000000** | **[V]** | Hopf charge = linking number of two preimage fibres (Whitehead). **Reproduced in-repo:** `results/verify/topology_invariants_check.py` (Gauss linking of a Hopf-linked pair `= 1`, unlinked control `= 0`). External provenance: `frontier_calcs/greenyer_real_hopf_charge_whitehead_integral.py` |
| Chern `C` | **±2** | **[V]/[credited]** | wave-mode Chern of the CK/Beltrami beat eigenmode = spin-1 photon-helicity value `2s` (Bliokh 2015 *Science* 348:1448; Palmerduca–Qin 2024 *PRD* 109:085005). **Reproduced in-repo:** `results/verify/topology_invariants_check.py` (Fukui-Hatsugai over `S²`, `C = +2` exact). A **credited convergence** — the object's eigenmode carries the photon's helicity index (`|C| = 2 Q_H`), corroborating the confined-photon reading — not a concession |

**Structural backbone (existence & spectral unification — M15, `reeb_spectral_geometry_check.py`)   [V]/[credited]**
- **Closed-orbit existence (the standing-wave loop is a theorem).** The Beltrami field is the **Reeb field of a
  contact structure** (`α∧dα = λ‖B‖²vol`, `curl B×B=0`; Etnyre–Ghrist 2000), so Weinstein/**Taubes 2007**
  *guarantees* a closed field line — the resonator's fundamental loop **exists by topology, not assumption**.
  Enciso–Peralta-Salas 2012 strengthens this: force-free fields realize *any* knot/link.
- **Curl-spectrum unification (one operator, three geometries).** The `curl` (Beltrami/Reeb) operator's single
  spectrum is the CK carrier comb (bounded, `tan x = x`), the self-similar cascade (`λ_L = λ_0 N^L`, §I/M14),
  and the `S³` Ray-Singer torsion coefficient (`ζ′(−2) = −ζ(3)/4π²`, §3a/M13) — not three coincidences.

---

## G. Parameter-free scalar test (the sharpest falsifiable predictions)   [prediction]
**Calibration-free — no `ħ_eff`, `b_eff`, `v_A`, or fit enters.** A direct discriminator: measure the
ladder ratio and it selects the structure (or falsifies both).

| Prediction | Golden (`N=φ`) | Nardi (`N=4`) |
|---|---|---|
| frequency ladder `f(L+1)/f(L) = N` | **1.6180** | 4 |
| toroidal-moment ratio `T(L)/T(L+1) = N⁴` | **6.854** | 256.0000 |
| second-system test `b_eff = B²/(2μ₀ n_i)` | (magnetic energy per ion — testable on any second plasmoid/spheromak) |

The golden branch is not a fitted coincidence: `N=φ` is the **adjacent-triad phase-matching** root
(§H, `N²=N+1`) — the golden ratio is the unique cascade base that phase-matches (integer bases cannot;
carried at [V]-candidate in the M14 beat-law / triad-dichotomy result). Which branch the object realizes is
**open — measure it.**

---

## H. Convention register
| Symbol | Value | Tier | Note |
|---|---|---|---|
| `N = φ` | **1.6180339887** | **[V]** | unique real root of `N²=N+1` (adjacent-triad phase-matching) — **derived, not fit** |
| `N⁴` (golden) | 6.854 | **[V]** | `φ⁴` |
| `ln φ` | 0.4812 | **[V]** | temperature/scale ratio = `ln N` (structural consequence, not an independent coincidence) |
| type-I/II boundary | `1/√2 = 0.7071` | **[credited]** | GL κ threshold |
| `j₀,₁` | 2.404826 | **[credited]** | first zero of `J₀`; `1/(2 j₀,₁) = 0.20792` (the §C convention-independent `c_CK` limit) |
| `ε` (aspect / nesting) | 0.697 (FreeFEM geometric) ‖ `1/φ = 0.618` (golden nesting) | **[V]/convention** | ⚠ two-convention symbol — §A/§C use the FreeFEM aspect 0.697; §G/§H/§I use the golden nesting `1/φ`. State which. |

## I. Polarizable medium & resonator spectrum (derived)   [V]
Source: `frontier_calcs/polarizable_medium_resonator_derivation.py` (2026-08-11). Medium form
`v_eff = c/√(ε_rμ_r) = v_A`.

| Quantity | Ball lightning | Lab spheromak | Tier |
|---|---|---|---|
| `ε_r = 1+(c/v_A)²` | **2.17×10⁸** | 8.99×10⁶ | **[V]** |
| `n = √(ε_rμ_r) = c/v_A` | **1.47×10⁴** | 2.998×10³ | **[V]** |
| `Z = Z_0/n` | **0.0255 Ω** | 0.126 Ω | **[V]** |
| dispersion | **non-dispersive** — `v_φ = v_g = v_A` (exact) | same | **[V]** |

- **Resonator (CK/Beltrami) eigenvalues [V]:** `λ_n R =` roots of `tan x = x` `= 4.4934, 7.7253, 10.9041,
  14.0662, 17.2208, 20.3713` — `λ₁R = 4.493409` = the locked-paper host-sphere value (exact cross-check).
- **Ball-lightning resonance frequencies [V]** `f_n = λ_n v_A/2πR`: **121.2, 208.3, 294.0, 379.3, 464.3,
  549.3 kHz** — **inharmonic** (ratios 1, 1.719, 2.427, 3.13, 3.83, 4.53 — bell-like, since `tan x = x`).
  *(This is the `{121,208,294} kHz` carrier comb M7-2 reproduces "to the digit"; the absolute frequencies
  carry the §A `v_A` residual, the ratios do not.)*
- The **beat** (~kHz) is the doublet splitting on the ~121 kHz carrier, **not** a fundamental (`f_b ≪ f₁`).
- **Electrical size [V]** `kR = ω_b R/c ≈ 9.4×10⁻⁶` (beat-frequency, at `ε=1/φ`: `f_b(0)≈4–8 kHz`,
  `R=0.12 m`) → far-field radiation `≲(kR)³ ≈ 8×10⁻¹⁶` (Chu electrically-small floor = conservative upper
  bound; the anapole radiates `~(kR)²` fainter as a toroidal dipole, efficiency `~(kR)⁵`, near-BIC further
  — so `≲10⁻¹⁵`; `frontier_calcs/exploratory_a6_radiation_suppression_exponent.py`). SUPERSEDES the earlier
  non-golden `2.5–5×10⁻⁶` (which used `f_b≈1 kHz`, `ε=0.3`).
- `Z_0 = 376.730 Ω` **[credited]** (vacuum wave impedance).

**⚠ K_PV convention — PINNED (P5 reconciliation, 2026-08-25)   [S/convention].** The polarizable-vacuum
*gravitational* index shift had been quoted three ways (10⁻³⁵ / 10⁻²⁷ / 1.8×10⁻⁴³) — different mass/length
conventions read as one number. **Canonical: `K_PV − 1 = 2GM/Rc²`, with `M` = the object's ION REST MASS**
`M = n_i m_i·(4/3)πR³ ≈ 5.9×10⁻⁹ kg` → **`K_PV − 1 ≈ 7×10⁻³⁵`** (gravity-dominant;
`frontier_calcs/vacuum_resonator_index.py` `KPV_ion`). The EM-only/field-energy version (`M = W_B/c² ≈
1.4×10⁻¹⁷ kg`) gives `1.8×10⁻⁴³` — a *lower bound*, not the headline. **Quote `7×10⁻³⁵` with the rest-mass
convention; the plasma analogue index `n_A = c/v_A ≈ 1.5×10⁴` dominates the vacuum term by >40 orders
regardless.** (Consistent with `MATH_TOOLKIT_BASE.md` `K_PV` and the M11 polarizable-vacuum treatment.)

---

*Foundation anchor table. Every value traces to the named `frontier_calcs/` script (extended-corpus
provenance directory). Residuals and ansatz-bands are labeled, not hidden; dimensionless ratios are the
robust, anchor-immune core. Excised numerology is logged in `results/EXCISION_LEDGER.md`, not here.
ASCII apart from standard math symbols.*
