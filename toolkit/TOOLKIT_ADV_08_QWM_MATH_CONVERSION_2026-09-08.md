# TOOLKIT ADV — Module M8: QWM (Reed Quantum Wave Mechanics) MATH CONVERSION + DIMENSIONAL AUDIT

Part of the FTGB math toolkit (see `MATH_TOOLKIT_BASE.md`, `MATH_TOOLKIT_ADVANCED_2026-09-02.md`,
`TOOLKIT_ADV_07_BUCKINGHAM_PI_2026-09-08.md`). This module executes a **CONVERT-AND-CHECK** pass over the
mathematics of Larry Reed's *Quantum Wave Mechanics* (QWM, 4th ed., Booklocker 2022): each QWM expression is
**stated**, given its **physical meaning**, **mapped** to a toolkit module, expressed **real-unit ‖
dimensionless** side-by-side, **dimensionally checked** (the "check", per L's obsessive-units emphasis and the
M7 Buckingham-Pi backbone), and **tiered**. Every dimensional reduction, PASS/FAIL, and numeric anchor below is
**computed** (not restated) by `frontier_calcs/toolkit_adv08_qwm_math_conversion.py` →
`toolkit_adv08_qwm_math_conversion_OUT.txt` (sympy exact exponent bookkeeping + numpy CODATA-2018 arithmetic;
ASCII, `PYTHONIOENCODING=utf-8`).

> **SCOPE STATEMENT (read first).** QWM is a **FRAMEWORK**, not established physics. We tier **[QWM framework]**
> for its own ontological claims, **[credited]** for the standard pieces it builds on (Madelung 1927,
> de Broglie 1924, London 1935, standard EM/topology), and **[V]** *only* for what is verified here by the named
> computation or a checked identity. The QWM **gravity** chapters (Ch.33–47: Oldershaw discrete-scale-relativity,
> oscillator-sync-as-gravity, graviton = phase-conjugate photon) are **[unassessed external]** and are **not**
> converted — they are named and excluded. This module does **not** endorse QWM wholesale: it converts the math
> that checks out and flags the rest. Held corrections (D1 mass≠whirl-number, D2/D3 `A·B` is a helicity density
> not a matter density, D4 charge=spin angular momentum, K0 π₃(S²) helicity ≠ baryon B π₃(S³) ≠ Q_H linking) are
> honored throughout. No fabricated numbers; every near-miss coincidence-gated at 0.5% vs `phi^n`/`137^n`.

## Tier legend
- **[V]** verified here by the named computation / a checked identity or dimensional reduction.
- **[credited]** established physics QWM builds on (Madelung, de Broglie, London, Maxwell, Berry, Skyrme).
- **[QWM framework]** Reed/quantum-wave-mechanics ontology — internally-defined reading, used as a
  method/notation choice, attributed to Reed/QWM, **not** endorsed as established.
- **[A]** analytic / model-asserted (illustrative, internally consistent, not re-derived).
- **[S]** structural / spectral-geometric or cited-convergence, not closed on our side.
- **[flagged]** coincidence held, not promoted (`~137`).
- **[unassessed external]** QWM gravity chapters + Storti *Quinta Essentia* / Ginzburg — read critically,
  **do NOT cite as established**, method-borrow only where noted.

**Primary sources spot-read (this pass, Read tool `pages`, real rendered math):** Reed *QWM* Ch.3 (EM
4-potential), Ch.11 (Origin of Inertia), Ch.17 (Electron Model, Fig.17-2 parameter table), Ch.21 (Electric
Charge, Eqs.21-1…21-14 + Table 21-1), Ch.26 (Topological Charge, Eq.26-1 + Figs.26-1..6), Ch.36 (Mass Scaling).
Cross-checked against distilled `REED_QWM_MASS_EQUATIONS_BEYOND_QCD_2026-09-02.md`,
`REED_QWM_SALVAGE_2026-08-17.md`, `L_LETTER_CORRECTIONS_LEDGER_2026-09-03.md`, and the chapter catalog memory.

---

## M8-0 — The two unit systems the audit uses (the "check" apparatus)  [V]

The dimensional check reduces every RHS to base dimensions in **two** systems and asks whether it yields
**kg [M]**:

- **(A) SI-strict** — base `{M, L, T, I}`; **angle `rad` is dimensionless** (`A→0`); charge = Coulomb = `I·T`.
  This is the **rigorous referee check** (radians are formally dimensionless in SI).
- **(B) QWM (L's table)** — base `{M, L, T, A}` with **angle `rad` = A a genuine base dimension**, **no current
  base**; charge `e ~ [kg·rad/s] = M·A·T⁻¹` (spin angular momentum), `A_vec ~ m/rad = L·A⁻¹`, `B ~ 1/rad = A⁻¹`,
  `E-field ~ m/(s·rad) = L·T⁻¹·A⁻¹` (fixed so `E/B` is a velocity in **both** systems — [V] asserted in script).

**Verified up front (script):** `E/B` reduces to velocity `L·T⁻¹` in both systems. **Honest finding [V]:** the
QWM angle-as-base convention makes the *load-bearing* QWM results transparent — `m=e/ω` and `A·B`=helicity-density
both PASS — but it introduces **spurious `A` residuals** in `ħω`-type relations (`m=ħω_C/c²` shows residual `2A`
in the QWM base) because it double-counts a formally-dimensionless radian in both `ħ` and `ω`. **Conclusion:**
angle-as-dimension is a useful *bookkeeping aid* for charge/helicity, **not** a rigorous replacement for SI. The
SI-strict column is the referee; the QWM column is L's optional lens. This is itself an obsessive-units result.

---

## M8-1 — MASS: the whirl/Compton identity + the whirl NUMBER + L's seven equivalent forms

### The anchor identity (the one thing that is [V], not just framework)
- **QWM statement (Reed Ch.11/17; Fig.17-2 table).** Mass is a confined-wave **whirl frequency**; the electron
  rest energy IS the Compton whirl. **`m = ħ·ω_C / c²`**, `ω_C = m c²/ħ = c/R_C`, `ω_zbw = 2ω_C`.
- **Physical meaning.** The stationary matter wave `ψ=√ρ e^{iS/ħ}`, `S=−Et`, rotates its phase at `ω=E/ħ`; that
  rotation rate, divided by `c²`, is the inertial mass (de Broglie/zitterbewegung internal clock).
- **Toolkit map.** L2 (QHD/Madelung spine) + M5 (charge/whirl) + M7-6 row "mass–whirl".
- **Real-unit ‖ dimensionless.** `m = ħω_C/c²` [kg]  ‖  whirl NUMBER `q = 1/α ≈ 137.036` [dimensionless].
- **Dimensional check [V].** `ħω_C/c² → M` **PASS (SI)**. Numeric: `ω_C=7.7634e20 rad/s`,
  `m=ħω_C/c²=9.109384e-31 kg` (ratio to `m_e` = 1.000000), `ħω_C=0.51100 MeV=m_e c²`.
- **D1 held.** Mass [kg] **≠** the dimensionless whirl number `q=1/α`. `m=ħω_C/c²` is the dimensionally-correct
  identity; `q=1/α` is a *separate* dimensionless quantity ("one orbital whirl per ~137 spin revolutions").
  Per **D1′**, the honest schema is `m = f(q)` with the dimensional carrier `ω_C` supplying the units.
- **TIER.** **[V]** the identity + arithmetic (recovers `m_e` exactly); **[credited]** de Broglie/zitterbewegung;
  **[QWM framework]** the "mass IS the whirl" ontology and the whirl-number reading. **Standard-physics-equivalent:**
  `E=ħω`, `m=E/c²` are textbook; QWM's contribution is the *ontology*, not the equation.

### L's seven equivalent mass forms — DIMENSIONAL AUDIT (the core "check")
All from Reed Ch.21 Table 21-1 / Ch.17 Fig.17-2 (verified against primary). Each is a *different bookkeeping of
the same spin-precession mass*. Verdicts computed by the script (SI-strict = referee):

| # | Form (L's ledger) | Primary source form | SI check | Verdict |
|---|---|---|---|---|
| — | `m = ħ ω_C / c²` (anchor) | Ch.17 Fig.17-2 | `→ M` | **PASS [V]** — recovers `m_e` |
| — | `m = ħk / v` (Mead/Ch.11) | Ch.11 Tab.11-1 | `→ M` | **PASS** — kinetic momentum / velocity |
| L1 | `m = E/(𝓔/B)` *(as transcribed)* | `m = E/(𝓔/B)²` **[squared]** | `→ M·L·T⁻¹` | **FAIL as written → MOMENTUM.** Transcription dropped the square |
| L1\* | `m = E/(𝓔/B)²` (primary) | Ch.21 Tab.21-1 | `→ M` | **PASS** — energy / velocity² |
| L2 | `m = (E_s0+E_m0)/(𝓔/B)` *(as transcribed)* | `/(𝓔/B)²` **[squared]** | `→ M·L·T⁻¹` | **FAIL as written → MOMENTUM** |
| L2\* | `m = (E_s0+E_m0)/(𝓔/B)²` (primary) | Ch.21 Tab.21-1 | `→ M` | **PASS** iff `𝓔/B=c` (rest energy /c²) |
| L3 | `m = (ħk − qA)/(βc)` | Ch.11/Ch.3 (P=γmv+qA) | both terms `→ M` | **PASS** — canonical momentum / velocity |
| L4 | `m = L/[½(𝓔²−c²B²)]` | `m = 2L/(𝓔²−c²B²)` | see below | **CONDITIONAL — proportionality, not equality** |
| L5 | `m = \|V·q\|/c²` | Ch.21 Tab.21-1 (`=W/g`) | `→ M` | **PASS** — `qV=energy`, `/c²` |
| L6 | `m = −e𝓔/a` | Ch.21 (F=ma, F=e𝓔) | `→ M` | **PASS** — Newton's 2nd law |
| L7 | `m = A·e/v` | Ch.3/Ch.17 (`qA=mv`) | `→ M` | **PASS** — potential momentum / velocity |
| D4 | `m = e/ω` | Ch.17 Fig.17-2 | SI: `→ I·T²` ; QWM: `→ M` | **FAIL in SI, PASS in QWM** (needs D4 charge units) |

- **KEY CATCH #1 (L1/L2).** As transcribed in the ledger, `m=E/(𝓔/B)` gives **momentum** (`M·L·T⁻¹`), not mass —
  because `𝓔/B` is a *velocity* and energy/velocity = momentum. The **primary Ch.21 Table 21-1 has the SQUARE**:
  `m = E/(𝓔/B)² = 2L/(𝓔²−c²B²)`, which reduces to `M` (energy/velocity²). **The ledger transcription dropped the
  exponent.** Corrected forms L1\*/L2\* PASS. This is a genuine dimensional-audit finding — fold the square back in
  wherever the ledger's short form is quoted.
- **KEY CATCH #2 (L4).** `m = 2L/(𝓔²−c²B²)`: the field invariant `𝓔²−c²B²` is dimensionally consistent to
  subtract (script confirms `𝓔²` and `c²B²` share dimension `M²L²T⁻⁶I⁻²`), but for the ratio to be mass the
  numerator `L` would need dimension `M³L²T⁻⁶I⁻²` — **NOT** plain angular momentum (`M L² T⁻¹`). So `m=2L/(𝓔²−c²B²)`
  **cannot be a bare dimensional equality**; it survives only as a **proportionality** `m ∝ (field energy)/c²` with
  a hidden `ε₀`/volume constant. This is exactly the **D2 pattern** (equalities that are really
  proportionalities-with-a-carried-constant). Flag it as such.
- **KEY CATCH #3 (D4, `m=e/ω`).** In SI, `e/ω = (I·T)/(T⁻¹) = I·T²` — **not mass**. In the QWM charge convention
  `e~[kg·rad/s]=M·A·T⁻¹`, `e/ω = (M·A·T⁻¹)/(A·T⁻¹) = M` — **mass**. Numeric: `m=e/ω_C` with `e=7.0720e-10 kg·rad/s`
  returns `9.109384e-31 kg` (ratio 1.000000). **This is precisely why D4 is needed:** `m=e/ω` is only dimensionally
  coherent if charge carries mechanical (spin-angular-momentum) units. Standard SI hides this.
- **TIER.** The five standard forms (L3, L5, L6, L7, `ħk/v`) are **standard-physics-equivalent [V-check /
  credited]** — Newton's 2nd law, `E/c²`, and canonical-momentum rearrangements. L1\*/L2\* are **[V-check]** with
  the square restored. L4 is **[QWM framework, proportionality]**. `m=e/ω` is **[QWM framework]** (needs D4).

---

## M8-2 — CHARGE: `e ~ [kg·rad/s]` = spin(-precession) angular momentum; charge = torsion loop-closure defect

- **QWM statement (Reed Ch.21 Eqs.21-1..21-14; Ch.26).** Charge is read **AS a rate**:
  `e = m_e·ω = m_e(ω_C + ω_p) = 7.0719e-10 kg·rad/s = 1.6022e-19 C` (Eq.21-1/21-6); `ω_p = dθ/dt = e/m_e =
  1.7588e11 rad/s` (Eq.21-10); the loop-closure defect `dθ = 2πα = 0.04585 rad = 2.627°` per Compton turn
  (Eq.21-2), re-synchronizing every `q = 1/α ≈ 137.036` turns (Eq.21-2). Reed's Table 21-1 gives the full
  mechanical unit set: `1 C = 4.414e9 kg·rad/s`, `ε₀ = 1.725e8 kg·rad²/m³`, `μ₀ = 6.449e-26 m·s²/(kg·rad²)`.
- **Physical meaning.** The Hopf-linked charge path does not close after one Compton revolution — it **precesses**
  by `2πα` each turn ("spin torsion defect — topological charge", Ch.26 Fig.26-4). Charge sits on the **whirl axis**
  (a rate), the dynamical partner of the winding LABEL. Coulomb `[Q]` is merely a **count** of electrons (amount),
  concealing its nature (D4).
- **Toolkit map.** **L7 / M5** (origin of charge; torsion/holonomy) — `charge ~ b^a(C) = ∮ e^a = ∫ T^a`
  (translational torsion holonomy). Duplicates the extended-corpus `TOOLKIT_ADV_05_ORIGIN_OF_CHARGE.md` M5.6
  (origin-of-charge; not in the jewel — its result is folded here at M8-2 and in
  `results/ELECTRON_TORSION_DEFECT_EXPLANATION_2026-09-09.md`).
- **Real-unit ‖ dimensionless.** `e = m_e ω_C` [kg·rad/s]  ‖  `q = 1/α ≈ 137.036` [dimensionless] +
  `dθ = 2πα` [rad].
- **Dimensional check [V].** `m = e/ω → M` **PASS in QWM units** (M8-1 catch #3); `e = m_e·ω_C` numeric =
  `7.0720e-10 kg·rad/s` (Reed 7.0719e-10, matches). `dθ = 2πα = 0.045851 rad` (Reed 21-2, matches).
- **`~137` coincidence-gate [flagged, NOT promoted].** Reed's `q ≡ 1/α` is measured `α` **inserted by hand** and
  re-read as a synchronization ratio — a definitional identity (0.00% deviation, no second number). It is a
  **mechanism** (torsion closure defect), not a **prediction**. Distinct from `1/(20φ⁴)=137.082` (a prediction
  claim, 0.034% from 137.036, but hand-chosen `C(6,3)=20`, no QED running) — held **[flagged]**. Neither derives
  `α` from the object's own Beltrami–Hopf geometry.
- **TIER.** **[QWM framework]** the charge-as-spin-angular-momentum reading (D4) and charge-as-torsion-defect
  mechanism; **[V]** the arithmetic; **[flagged]** the `~137`; **[credited]** the `a_e=α/2π` Schwinger term the
  precession reproduces (recovers, does not predict).

---

## M8-3 — STANDING WAVE / QHD: Madelung, Bohm, and the QWM units-table consistency

- **QWM/credited statement.** The confined toroidal **standing wave = the object**. Madelung polar form
  `ψ = √ρ e^{iS/ħ}`, `ρ=|ψ|²`, `v = ∇S/m`; the Bohm quantum potential
  `Q = −(ħ²/2m)(∇²√ρ)/√ρ`. Reed Ch.11 (Origin of Inertia): confined light acquires rest mass
  `m = 4Vρ_m/3c²`, `c = c₀/√K_PV` (index slowdown), `ħk = q₀A + mv`, `v_p = c²/v_g = ω/k` (non-dispersive limit).
- **Physical meaning.** Amplitude `√ρ` is inert (standing); the phase rhythm carries the energy. Mass is an
  **obstruction to energy flow** (inductive analogy), not a Higgs coupling (D1 ontology note, [QWM framework]).
- **Toolkit map.** **L2** — the spine's QHD leg (Madelung ‖ RS-photon ‖ force-free MHD, the "one operator, three
  readings"). `TOOLKIT_ADV_03` (QHD/PV/solitons).
- **Real-unit ‖ dimensionless.** `ρ = |ψ|²` [kg/m³ via a carried constant]  ‖  `ρ/ρ₀ = |ψ|²/|ψ₀|²` [dimensionless].
- **QWM units-table internal consistency check (D2) [V].** L's table: `A_vec ~ m/rad`, `B ~ 1/rad`, so
  `A·B ~ m/rad²`. **Script confirms** `A·B` reduces to `L·A⁻²` = exactly the tabulated **magnetic helicity density
  m/rad²** — **PASS, internally consistent**. Matter density `ρ ~ kg/m³ = M·L⁻³` is a **different** dimension, so
  `ρ = A·B` is dimensionally impossible; the surviving content is the **proportionality** `ρ = κ·(A·B)` with a
  dimensional constant `κ` (D2). Likewise winding density `m⁻³` ≠ matter density `kg/m³` (D3). The
  `corr(ρ,A·B)=1.0000` result is a **dimensionless Pearson profile identity** (shapes coincide), unaffected.
- **TIER.** **[credited]** Madelung 1927, de Broglie 1924, Bohm 1952; **[V]** the units-table consistency check
  (`A·B`=helicity density) and the D2/D3 proportionality; **[QWM framework]** the "mass=obstruction-to-flow"
  ontology.

---

## M8-4 — EM / TOPOLOGY: Ch.3 4-potential + Ch.26 topological charge; the K0 ≠ B ≠ Q_H reconciliation

- **QWM statement (Reed Ch.3, standard).** EM 4-potential `A^μ = (φ/c, A)` (Eq.3-4); potential momentum
  `p_pd = qA` (Eq.3-7); canonical momentum `P = γmv + qA` (Eq.3-8); Lorentz force `F = q(E + v×B)` (Eq.3-16);
  fields `E = −∇φ − ∂A/∂t`, `B = ∇×A` (Eqs.3-10/3-11); Lorenz gauge `∇·A + (1/c²)∂φ/∂t = 0`. All **standard
  Maxwell** — Ch.3 adds an extra "dielectric force `F = q∇K_PV`" (Eq.3-17) which routes into the PV frame.
- **QWM statement (Reed Ch.26, topological charge).** Winding number **`n = (1/2π) ∮_C ∇φ·dr`** (Eq.26-1),
  `φ` = phase of `ψ = |ψ|e^{iφ}`; topological charge = degree of the phase map, a **dimensionless integer**; Reed
  reads electric charge as roots of unity on the unit circle (leptons: `n=2`, square roots `q±`) and **fractional
  quark charge** as cubic roots of unity via a **Tusi-couple / hypocycloid** (3-cusp deltoid ↔ SU(3)); "electric
  charge `Q = 2π` radians integer; `Q` is a spin precession effect (torsion defect)."
- **Physical meaning + toolkit map.** Ch.3 → **L1/L2** (fields/potentials, standard); the potential-momentum
  `qA=mv` underwrites mass form L7. Ch.26 Eq.26-1 → **L7 / M1** (winding/topology); it is the **exact standard
  formula** the project's §305 standing-wave mode number uses independently.
- **Real-unit ‖ dimensionless.** `n = (1/2π)∮∇φ·dr` [dimensionless integer]  ‖  itself (already a Pi-group);
  `A·B` [T·m·... = helicity density]  ‖  `K0/K0₀` [dimensionless].
- **Dimensional check [V].** Ch.26 winding: `∇φ·dr` = (rad/m)·m = rad, `/2π` → **dimensionless** in SI (script);
  in QWM it carries `A` ("N turns × rad", winding = `N·rad`) — consistent with L's table.
- **HELD RECONCILIATION (load-bearing).** Reed's Ch.26 conflates several distinct topologies under "topological
  charge." Keep the project's registry distinct:
  - **K0 = A·B** = real magnetic **helicity density** (**π₃(S²)**, Moffatt/Woltjer) — the object's *own* invariant,
    the density in the continuity/matter law. **[V] density leg** (`corr(ρ,A·B)=1`).
  - **baryon B** = Skyrme **winding degree** (**π₃(S³)**), `B=(1/24π²)∫ε^{ijk}Tr(L_iL_jL_k)d³x` — a *distinct,
    independently-conserved* winding (nucleon leg).
  - **Q_H** = **Hopf linking number** (integer, S517) — the object's conserved charge, a *linking* not a *wind-up*.
  - Reed's Eq.26-1 `n` is the **degree of a phase map** (π₁-type winding around a loop) = our §305 mode number.
    His *identification* of `n` with electric-charge quantization and SU(3) color charge is **[QWM framework]**,
    particle-scale, and must **NOT** be conflated with the K0/B/Q_H triad. Reed's Ch.26 "Q=2π integer / torsion
    defect" is the charge mechanism of M8-2, not a fourth topology.
- **TIER.** **[credited]** Ch.3 Maxwell + Eq.26-1 winding formula (standard, consonant with §305); **[QWM
  framework]** the roots-of-unity / hypocycloid charge-quantization ontology; the K0≠B≠Q_H distinction is **[V]**
  (held correction).

---

## M8-5 — MASS SCALING (Ch.36) / beyond-QCD: quark trefoil, `α_s=1`, and the DSR scaling law

- **QWM statement (Reed Ch.36 + L Q6).** (i) **[L Q6, QWM framework]** up/down quarks = **shrunken
  electrons/positrons**, magnetically coupled end-to-end with the flux loop (gluon) as a **trefoil knot**;
  `α_s = 1` = whirl/spin ratio; nucleon **mass** = spin-precession whirl energy of the confined e± (`m≃ħω/c²`),
  **baryon number** = topological winding (trefoil/Skyrme, Witten) — MASS-not-BARYON, distinct axes.
  (ii) **[Ch.36, unassessed external]** cosmological **discrete-scale-relativity** (Oldershaw): `L_ψ=Λ L_{ψ−1}`,
  `T_ψ=Λ T_{ψ−1}`, `M_ψ=Λ^D M_{ψ−1}` (Eqs.36-1/2/3), `Λ=5.2e17`, `D=3.174`, `Λ^D=1.7e56`; Schwarzschild
  `K_PV=e^{2GM/rc²}`, Sternglass e± cosmology; masses "follow a logarithmic progression."
- **Physical meaning + toolkit map.** The Q6 micro-picture → **M8-1/M8-2** + `REED_QWM_MASS_EQUATIONS §2.3`
  (nucleon = higher-WOUND toroidal wave; Skyrme `M_soliton = C(f_π/e) → ~939 MeV`, order-of-magnitude [S]). The
  Ch.36 **DSR/gravity** scaling → **NOT converted** (depends on Oldershaw DSR + oscillator-sync-as-gravity, both
  unverified; gravity-tied via Schwarzschild `K_PV`).
- **Dimensional check.** `M_ψ = Λ^D M_{ψ−1}`: `Λ` is an "empirically derived dimensionless constant" so the
  relation is dimensionally trivial (`M=M`) — it **passes dimensionally but is empty of mechanism** (a fitted
  self-similar re-scaling, exactly the M7-7 caution). The only **credited** piece is the **Regge trajectory**
  `J ∝ α M²` (real hadron spectroscopy), which Ch.36 cites.
- **Coincidence-gate `m_p/m_e = 1836.15` [V, gate].** Script: nearest `phi^16=2207` (dev **20.2%**, FAIL),
  nearest `137^2=1.88e4` (dev **923%**, FAIL). **No `phi^n`/`137^n` within 0.5%** → the proton/electron placement
  is **consistent ordering, NOT a promoted numerical law** (`log_137≈1.53`, `log_φ≈15.6`, neither clean). Matches
  the distilled verdict.
- **TIER.** **[QWM framework]** quark=shrunken-e± trefoil + `α_s=1`; **[S]** the Skyrme order-of-magnitude
  re-grounding (no locked number changes; `m_i` stays measured); **[credited]** Regge `J∝αM²`; **[unassessed
  external, EXCLUDED]** the Oldershaw DSR / Schwarzschild-`K_PV` cosmological scaling.

---

## M8-6 — THE MAPPING TABLE (core output): one row per QWM expression

`RU` = real-unit form; `Π` = dimensionless form; `dim` = SI-strict check. Toolkit modules: L1 fields/potentials,
L2 QHD spine, L7 charge/torsion, M1 topology, M5 origin-of-charge, M7 Buckingham-Pi, M8 (this) new items.

| QWM expression | Physical meaning | Module | Real-unit form | Dimensionless Π-form | dim check | Tier |
|---|---|---|---|---|---|---|
| `m = ħω_C/c²` | mass = Compton whirl | L2/M5/M7-6 | kg | `q=1/α` | `→M` **PASS** | **[V]** (arith)+[QWM] ontology |
| `ω_C=mc²/ħ`, `ω_zbw=2ω_C` | internal clock | L2 | rad/s | `ω_zbw/ω_C=2` | `→T⁻¹` PASS | [credited]+[V] |
| `R_C=ħ/mc`, `λ_C=h/mc` | toroid radius | L2 | m | `R_C/λ_C=1/2π` | `→L` PASS | [V] |
| `s=½ħ`, `μ_B=eħ/2m` | spin, moment | L2 | J·s, J/T | `ω_C/ω_zbw=½` | PASS | [V] numbers |
| `m=ħk/v` | Mead inertial mass | L2 | kg | — | `→M` PASS | [credited] |
| `m=E/(𝓔/B)²` (L1\*) | energy/velocity² | M8/M5 | kg | — | `→M` PASS | **[V-check]** (square restored) |
| `m=(E_s0+E_m0)/(𝓔/B)²` (L2\*) | rest-E/c² @ 𝓔/B=c | M8 | kg | — | `→M` (cond.) | [QWM framework] |
| `m=(ħk−qA)/(βc)` (L3) | canon. momentum/v | L1/L7 | kg | — | `→M` PASS | [credited] |
| `m=2L/(𝓔²−c²B²)` (L4) | field-energy/c² | M8 | kg (∝) | — | **proportionality** | [QWM framework] |
| `m=\|Vq\|/c²` (L5) | `qV=E`, `/c²` | L1 | kg | — | `→M` PASS | [credited] |
| `m=−e𝓔/a` (L6) | Newton `F=ma` | — | kg | — | `→M` PASS | [credited] |
| `m=Ae/v` (L7) | `qA=mv` | L1/L7 | kg | — | `→M` PASS | [credited] |
| `e=m_eω=m_e(ω_C+ω_p)` | charge AS a rate | M5/L7 | kg·rad/s | `q=1/α`, `dθ=2πα` | `→M·A·T⁻¹` | **[QWM framework]**+[V] |
| `m=e/ω` (D4) | mass from charge/whirl | M5 | kg | — | SI FAIL / QWM `→M` | **[QWM framework]** (needs D4) |
| `dθ=2πα`, `q=1/α` | closure defect / re-sync | M5 | rad / — | `q=1/α` | rad / dimensionless | **[flagged]** (~137) |
| `charge~∮e^a=∫T^a` | torsion holonomy defect | L7 | m (Burgers) | — | `→L` | [A/hyp]+[credited] geom |
| `ψ=√ρ e^{iS/ħ}`, `v=∇S/m` | Madelung standing wave | L2 | — | `ρ/ρ₀` | consistent | [credited] |
| `A·B` (helicity density) | winding/whirl density | L2/M1 | m/rad² | `K0/K0₀` | `→L·A⁻²` **PASS** | **[V]** (D2 units check) |
| `ρ=κ(A·B)` | matter ∝ helicity | L2 | kg/m³ | `ρ/ρ₀=(A·B)/(A·B)₀` | proportionality | **[V]** density leg + [S] |
| `A^μ=(φ/c,A)`, `P=γmv+qA` | EM 4-potential | L1 | standard | — | PASS | [credited] |
| `E=q(E+v×B)`, `B=∇×A` | Maxwell/Lorentz | L1 | standard | — | PASS | [credited] |
| `n=(1/2π)∮∇φ·dr` (26-1) | winding = phase-map degree | M1/L7 | — | integer `n` | `→` dimensionless | [credited] (=§305) |
| quark charge = roots of unity / hypocycloid | fractional charge (SU(3)) | M1 | — | `Q=±1/3,±2/3` | dimensionless | [QWM framework] |
| quark=shrunken e± trefoil, `α_s=1` | nucleon micro-picture | M8/§2.3 | — | `α_s=1` | dimensionless | [QWM framework] |
| `M_soliton=C(f_π/e)→939 MeV` | Skyrme nucleon | §2.3 | MeV | `C≈40`, `B` degree | `→` energy | [S] order-of-mag |
| `M_ψ=Λ^D M_{ψ−1}` (Ch.36) | Oldershaw DSR cosmo scaling | — | kg | `Λ`,`D` fitted | trivially PASS | **[unassessed], EXCLUDED** |
| `K_PV=e^{2GM/rc²}` (Ch.36) | Schwarzschild PV scaling | — | — | dimensionless | — | [credited PV frame] / gravity-ext EXCLUDED |
| Ch.33–47 gravity | osc-sync gravity, graviton=PC photon | — | — | — | — | **[unassessed external], EXCLUDED** |

### Classification of the converted math
- **NEW to the toolkit (add as M8 items):** the **dimensional AUDIT itself** (L1/L2 square-restoration catch;
  L4-is-a-proportionality; `m=e/ω` needs D4); the explicit **QWM units-table consistency check** (`A·B`=helicity
  density m/rad², D2/D3 as computed proportionalities); the **`m = f(q)` schema** (D1′, mass a function of the
  whirl number with `ω_C` the carrier). These did not previously live in one place with the units machinery.
- **DUPLICATES existing modules (cite, don't restate):** `m=ħω_C/c²` and the electron parameter table (M5 /
  `REED_QWM_MASS_EQUATIONS §1`); charge-as-torsion-defect + `q=1/α` (extended-corpus `TOOLKIT_ADV_05_ORIGIN_OF_CHARGE.md` M5.6, not in the jewel; folded here at M8-2 + `results/ELECTRON_TORSION_DEFECT_EXPLANATION_2026-09-09.md`); Madelung/RS/MHD spine
  (L2 / `TOOLKIT_ADV_02`, `_03`); winding formula 26-1 (§305); Skyrme nucleon (`REED_QWM_MASS_EQUATIONS §2.3`);
  the standard EM 4-potential (L1). Ch.3 Maxwell, Berry phase, coupled-mode all already credited elsewhere.
- **[unassessed/fringe] EXCLUDED:** all QWM **gravity** content (Ch.33–47: Oldershaw DSR, oscillator-sync-as-
  gravity, graviton=phase-conjugate-photon, Ch.36 cosmological mass scaling); Storti *Quinta Essentia* and
  Ginzburg *Unified Spiral Field* (method/geometry-borrow at most, no claim adopted). The PV representation `K_PV`
  itself remains **[credited]** as a weak-field-GR modeling frame (reproduces Eddington bending) — only Reed's
  gravity *extension* of it is excluded.

---

## M8-7 — VERDICT (≈350 words)

**What converts cleanly (dimensionally checked, tiered).** The QWM mass foundation transfers into the toolkit
with its units intact. The anchor identity `m = ħω_C/c²` is **[V]** — it recovers `m_e` to 1.000000 and
`ħω_C = 0.511 MeV = m_e c²`. Of L's seven equivalent mass forms, five (`m=ħk/v`, L3, L5, L6, L7) are
**standard-physics-equivalent** and PASS the SI dimensional check outright — they are Newton's second law, `E/c²`,
and canonical-momentum (`qA=mv`) rearrangements. The charge mechanism converts as **[QWM framework]**: `e=m_eω`,
`dθ=2πα`, `q=1/α` reproduce Reed's `7.0719e-10 kg·rad/s` and `2.627°`, and the winding formula `n=(1/2π)∮∇φ·dr`
is the standard degree already used at §305 (**[credited]**). The QWM units table is **internally consistent**
where it matters: `A·B` reduces exactly to the tabulated helicity density `m/rad²` (**[V]**).

**Standard-equivalent vs genuinely-QWM-framework.** The *equations* for mass and the internal clock are textbook
(`E=ħω`, `m=E/c²`); QWM's genuine contribution is **ontological** — mass IS the whirl, charge IS a spin-precession
angular momentum (`[kg·rad/s]`), winding IS the address. These are **[QWM framework]**, attributed to Reed, not
endorsed as established.

**What FAILS / needs correction (the "check" earning its keep).** Three catches. (1) L's ledger transcribed
`m=E/(𝓔/B)` **without the square** — as written it is momentum, not mass; the primary Ch.21 Table 21-1 has
`m=E/(𝓔/B)²`, which PASSES. Restore the square. (2) `m=e/ω` FAILS in SI (`→I·T²`) and PASSES only with the D4
charge unit `[kg·rad/s]` — which is *precisely why* D4 is load-bearing, not cosmetic. (3) `m=2L/(𝓔²−c²B²)` cannot
be a bare equality (`L` is not angular momentum); it survives only as a **proportionality** with a hidden `ε₀`,
the same D2 pattern as `ρ=κ(A·B)`. The `m_p/m_e=1836` placement fails the 0.5% `phi^n`/`137^n` gate — ordering,
not a law. `~137` stays **[flagged]**.

**What stays [unassessed].** All QWM gravity chapters (33–47: Oldershaw DSR, oscillator-sync-as-gravity,
graviton=phase-conjugate photon, Ch.36 cosmological scaling) are excluded — gravity-tied and dependent on
unverified named ingredients. `K_PV` itself remains [credited]; only Reed's gravity extension of it is walled.

**Cite:** Reed *QWM* Ch.3/11/17/21/26/36; Madelung, *Z. Physik* **40**, 322 (1927); de Broglie (1924); London,
*Proc. R. Soc.* A **149**, 71 (1935); Buckingham, *Phys. Rev.* **4**, 345 (1914).

---

## Per-claim index (M8)
| # | Item | Tier | Repro check |
|---|---|---|---|
| M8-0 | Two unit systems; angle-base is bookkeeping-aid not rigorous | [V] | `E/B`→velocity both; QWM `ħω` picks up spurious `A` |
| M8-1 | Mass identity `ħω_C/c²` + 7 forms dimensional audit | [V]/[QWM] | recovers `m_e`; L1/L2 square catch; L4 proportionality; `m=e/ω` D4 |
| M8-2 | Charge = `[kg·rad/s]` spin ang.mom.; torsion defect; `q=1/α` | [QWM]/[V]/[flagged] | `e=m_eω_C=7.072e-10`; `dθ=2πα=2.627°` |
| M8-3 | Madelung/Bohm QHD; QWM units-table `A·B`=helicity density | [credited]/[V] | `A·B→L·A⁻²=m/rad²`; D2/D3 proportionality |
| M8-4 | EM 4-potential (Ch.3) + winding 26-1; K0≠B≠Q_H held | [credited]/[V] | winding dimensionless; triad kept distinct |
| M8-5 | Quark trefoil/`α_s=1` [QWM]; DSR scaling [unassessed EXCL]; `1836` gate | [QWM]/[S]/[unassessed] | `m_p/m_e` no `phi^n`/`137^n` <0.5% |
| M8-6 | The mapping table (core output) + NEW/DUP/EXCLUDED split | [V]-structure | per-row dim check |
| M8-7 | Verdict | — | — |

## Reproducible-calculation coverage (M8)
- `frontier_calcs/toolkit_adv08_qwm_math_conversion.py` (sympy exact + numpy CODATA-2018; ASCII,
  `PYTHONIOENCODING=utf-8`) → `toolkit_adv08_qwm_math_conversion_OUT.txt`. Ran clean; all checks resolved:
  - Mass forms SI: `ħω_C/c²`, `ħk/v`, L1\*, L2\*, L3, L5, L6, L7 = **PASS (→M)**; L1/L2 as-written = **FAIL
    (→momentum)**; `m=e/ω` = **FAIL in SI** (`→I·T²`), **PASS in QWM** (`→M`). L4 = **proportionality** (numerator
    not angular momentum).
  - QWM units: `A·B → L·A⁻²` = helicity density m/rad² **PASS**; `ρ−(A·B)≠0` ⇒ D2 proportionality; winding density
    `m⁻³` ≠ `ρ` `kg/m³` ⇒ D3.
  - Numeric anchors: `ω_C=7.7634e20`, `m=ħω_C/c²` ratio `1.000000`, `ħω_C=0.51100 MeV`, `e=m_eω_C=7.0720e-10
    kg·rad/s`, `ω_p=1.7588e11`, `q=1/α=137.036`, `dθ=2πα=2.627°`, `m=e/ω_C` ratio `1.000000`.
  - Coincidence gate: `m_p/m_e=1836.15` no `phi^n`/`137^n` <0.5%; `1/(20φ⁴)=137.082` dev 0.034% **[flagged]**.

Cross-links: `TOOLKIT_ADV_07_BUCKINGHAM_PI_2026-09-08.md` (dimensional method backbone),
`REED_QWM_MASS_EQUATIONS_BEYOND_QCD_2026-09-02.md` (mass equations source),
`REED_QWM_SALVAGE_2026-08-17.md`, `L_LETTER_CORRECTIONS_LEDGER_2026-09-03.md` (D1–D4/Q5–Q7 corrections),
`TOOLKIT_ADV_05_ORIGIN_OF_CHARGE.md` (M5 charge — extended corpus, not in the jewel; folded here at M8-2), `MATH_TOOLKIT_BASE.md`. Citations: Reed *QWM* Ch.3/11/17/21/26/36;
Madelung 1927; de Broglie 1924; London 1935; Buckingham 1914.
