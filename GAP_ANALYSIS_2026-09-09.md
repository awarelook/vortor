# Gap analysis — mathematics in the corpus not yet in the jewel

**Date:** 2026-09-09 · **Method:** three parallel scans of `C:\Users\natha\ckfreefem`,
`C:\Users\natha\Downloads`, and the `F:\conspire` / `F:\SYNTHESIS` vaults, each briefed on exactly what the
jewel (`F:\vortor`) already holds (toolkit M7–M14, R2/R3, the LENR model, the electron/α work, the engine) so
only genuine gaps are reported. Formulas below are quoted as found in the corpus; **inclusion here is a
candidate fold, not an endorsement** — each carries the tier it would enter at, and known problems are flagged.

## ✅ Status (2026-09-09): the top gaps are folded
- **G1 Nielsen TUFT → `toolkit/TOOLKIT_ADV_13_NIELSEN_TUFT_MASS_TOWER_2026-09-09.md` (M13)** + verify
  `results/verify/tuft_mass_tower_check.py` — coefficients `[V]`-reproduced, π-anomaly + blind-fit `[flag]`.
- **G2 Greenyer → `toolkit/TOOLKIT_ADV_14_GREENYER_BEAT_LAW_2026-09-09.md` (M14)** + verify
  `results/verify/greenyer_beat_cascade_check.py` — cascade/dichotomy/Fibonacci `[V]`, `N_crit` `[prediction]`,
  no over-unity.
- **G3–G5 lineage (Bostick/Puthoff/Shoulders) → `LINEAGE.md`** `[credited-lineage]`/`[framework]`.
- **Tier-3 Storti → `M11-6` (spectral mode-count closure) + `M11-7` (dispositions/quarantine ledger)** +
  verify `results/verify/egm_mode_count_closure.py` — folds the Debye/Nyquist mode-count method M11-1 left as a
  black box `[V]`; the 2:1 harmonic / radii / H₀ / α stay quarantined. Candidates K_PV(ω) & Buckingham-Π log
  found already-homed (M11-3 pt 2 / M7).
- **G6 Reed → verdict ALREADY COVERED (no append).** The `4.414e9 kg·rad/s` conversion is a restatement of
  M8-0/M8-2 (`e ~ [kg·rad/s]` + anchor `e = m_e ω_C`); the `dθ=2πα` closure defect is already in M8-2 and
  triple-covered by extended-corpus `TOOLKIT_ADV_05` M5.6 + in-jewel `electron.html` — folding either would only duplicate or requarantine.

## Two discoveries (independent of the math)
- **`ckfreefem\frontier_calcs\` exists on disk** — the provenance directory the R2 / Δ hand-offs reference
  (previously noted as "not in the repo"). The verification calcs are real and locatable there.
- The vortor jewel is a **curated subset of a larger `ckfreefem\ftgb_modeler\` project** (the full toolkit
  source, including M7/M8, lives there).

---

## Tier 1 — high value, big payload (fold first)

### G1. Nielsen TUFT — the actual mass spectrum (jewel only *mentions* the knot spectrum)  → new module **M13**
Would let the jewel **derive** the mass spectrum instead of asserting `m = ħω/c²`.
- **Quark mass-tower** (TUFT eqs 96–103): `m_{n,±} = Λ₅ (n+1)·exp( (a₅ ± λ_T(n)) n + C₅ n² + β₅ n(n+1)/2 +
  σ₅ log τ(Kₙ) ) × {2/3, n=1; 1, else}`, with `C₅ = ζ(3)/12`, `β₅ = ζ(5)/(8π⁴)`, `σ₅ = ζ(3)/(16π²)`,
  `a₅ ≈ 3.564112`, `λ_T(n) = 2/π + (ζ(3)/12π)(5/2−n)`.
- **Lepton (S³)** `ω₃ = ζ(3)/(4π²)` and **neutrino (S⁹)** `C₉ = −ζ(3)/8·(1+ζ(3)/28) = −0.15670774`,
  `σ₉ = ζ(3)/(8π²)` (arithmetic verified to 30 dps).
- **Knot normalizations:** `τ(unknot)=1, τ(Hopf)=4, τ(trefoil)=3`, `τ_R(L(n,1)) = 1/n`, `N₅=8π³`, `N₉=32π⁵`.
- **CKM** from CP⁴ overlaps `V_ij = ⟨ψ_i|ψ_j⟩` (`J = 3.06e-5`); **PMNS + ν-masses** from S⁹ overlaps, no
  seesaw (`m_ν ~ 50 meV`); **Chern–Simons action** `S_CS = (k/4π)∫Tr(A∧dA + A∧A∧A) → M = ke²/4π`.
- **Proca–Beltrami derivation:** `∇×B=λB → ∇²B+λ²B=0` vs static Proca ⇒ `λ = mc/ℏ`; mass operator `⋆d`.
- **Sources:** `ckfreefem\frontier_calcs\{NIELSEN_TUFT_MASS_COEFFICIENT_EXACT_FORM, C9_MASS_TOWER…,
  KERNEL_NIELSEN_MASS_MATRIX_ELEMENT}_2026-09-0*.md`; `Downloads\{100pg…COMPENDIUM, 31newpg…FRAMEWORK}.md`.
- **Fold tier `[framework: Nielsen TUFT]` / `[S]`.** Honesty flags: the π-power question (pure `C₅=ζ(3)/12`
  vs the π²-carrying `ω₃,σ₅,σ₉`) is **RESOLVED (2026-09-10, `curl_spectral_zeta_pi_power_check.py`)** in favor
  of the π²-carrying forms — the pure forms are a category error (`ζ_B(s)=ζ(s−2)−ζ(s)` → `ζ′(−2)=−ζ(3)/4π²`);
  the "blinded fit at 0.1σ" claims remain the preprint's, not `[V]` — fold the *structure*, mark the fits.

### G2. Greenyer — the beat law, the cascade, and the aneutronic energetics  → new module **M14**
Would let the jewel **derive** the {121,208,294} kHz comb and the LENR selective-release, not just state them.
- **Beat law** `f_b = C·v_eff·a²/(2πR³)` (`C ≈ 0.2654`, Greenyer's normalization; M14 flags it as
  convention-ambiguous and the jewel hardens to the FE cascade `c_CK(÷ε²)=0.578`, both reducing to the
  invariant limit `1/(2 j₀,₁)=0.208` — see `foundation/30_CANONICAL_NUMBERS.md` §C); **cascade theorem** `f_b(L)/f_b(0) = N^L`
  (shape-factor-independent, proven exact).
- **Triad dichotomy** — integer cascades cannot phase-match (`N^i − N^j ≡ −1 (mod N)`), the golden ratio
  always does (`φⁿ = φⁿ⁻¹+φⁿ⁻²` *is* the matching condition); the network conserves exactly **two
  Manley–Rowe invariants with Fibonacci-number basis coefficients**; growth threshold `κ/γ₀ = 22.8`.
- **Magnetic-tension Rayleigh fission** — fissility `X = Q²/(64π²γε₀R³)`, `γ_eff = (B²/2µ₀)R`, magnetic
  Rayleigh limit `N_R = 1.178e9`, **falsifiable critical population `N_crit ≈ 1.7–3×10¹¹` electrons**,
  `l=2` dispersion `ω²₂ = (8γ_eff/ρR³)(1−X)`.
- **Anapole/junction poles** `T = 8.4823 A·R³`, `T_L/T_{L+1} = 256 = N⁴`, helicity scales `N^{−4L}` while
  integer winding is conserved; **second (THz) cascade** `ω₀ = α_CK ε² ω_A` (`α_CK = ½`), `ω_L = ω₀·4^L`,
  `f_b = 52.286 THz`; **Gamow/ponderomotive** LENR ledger `δn/n = ½(ω_c/ω_5)²`, `G_total = 32.64`.
- **Sources:** `Downloads\ICCF27_greenyer_beat_qhd_essentialized_v6e.pdf`; `ckfreefem\EVO_MATHEMATICAL_CORE.md`
  (~50 eqs); **`conspire\Arc\cores\torus beat law\TORUS_MATHEMATICS_APPENDIX.md` (2069 lines** — MRxMHD
  nested-eigenvalue stacks, the Hopf-fibration Beltrami negative result, the `l=2` quadrupole mode, a
  self-similar off-resonance theorem).
- **Fold tier `[S]` / `[framework: Greenyer/MFMP]` with `[V]`-candidate sub-results** (the cascade theorem and
  the triad conservation algebra are provable; the falsifiable `N_crit` band is a genuine prediction). This is
  the biggest single missing *mathematical layer* and it directly strengthens the LENR model and the comb.

## Tier 2 — lineage math, credited/framework (fold into a "lineage" note or extend M8/M11)

### G3. Bostick — the toroidal electron  `[credited-lineage]`
`α = e²/ℏc = (π/2)/ln(R/r₀)`; flywheel `E ≈ (e²/πR)ln(R/r₀) = mc²`; spin `= ½`; waveguide dispersion
`ω² = ω_c² + k²c²` (`ω_c = c/R`); flux quantization `Θ ≈ πℏc/e`; force-free `J×B = 0`.
`conspire\Arc\Winston Bostick.md`. **New:** no Bostick math in the jewel; his `α ~ 1/ln(R/r₀)` is an
independent geometric route to the fine-structure gap (compare the α reframe).

### G4. Puthoff — PV consequences beyond `K_PV`  `[credited]`/`[framework]`
`F_g = −mc² ∇ln K_PV`; `c(r) = c₀/K_PV(r)`; `K_PV ≡ γ = 1/√(1−v²/c²)`; Baryonic Tully–Fisher
`M_B = (3/5Gg₀)v⁴` (`g₀ = (9.6±1.2)×10⁻¹¹`); force unification `V(r) = (K/r)exp(−mr/√(n+1))`; Pais Superforce
`S_F = c⁴/G`. `conspire\Arc\Polarizable vacuum.md`. **New:** the jewel has only static `K_PV = exp(2GM/rc²)`;
these are the force/optics/kinematic consequences — extend **M11**.

### G5. Shoulders — EVO energetics / transmutation  `[framework]`
EVs carry `~10⁷ protons` with Coulomb-barrier-crossing KE (documented Pd transmutation); Jin & Fox helical
vortex-ring stability; `½ℏω₀ = mc²` (mass-as-vacuum-coupling). `conspire\Arc\Kenneth Shoulders.md`. **New:**
the EVO rung is in the jewel; Shoulders' own energetics/transmutation relations are not — feed the LENR model.

### G6. Reed — the dimensional audit (extend **M8**)  `[QWM framework]`
Seven equivalent mass forms (`m = E/(𝓔/B)²`, `m = 2L/(𝓔²−c²B²)`, `m = |Vq|/c²`, `m = −e𝓔/a`, `m = Ae/v`);
confined-light rest mass `m = 4Vρ_m/3c²`, `c = c₀/√K_PV`; mechanical-unit table `1 C = 4.414e9 kg·rad/s`,
`ε₀ = 1.725e8 kg·rad²/m³`; closure defect `dθ = 2πα = 2.627°/turn`. `ckfreefem\…\TOOLKIT_ADV_08_QWM…md`.
**New:** the specific forms + unit table go beyond the jewel's `m = ħω/c²` and `charge = kg·rad/s`.

## Tier 3 — Storti EGM closed-forms (method-only; values stay flagged) → extend **M11**
All from `Downloads\storti_egm_missing.md` (a gap-analysis reconstructing Storti & Desiato 2009 / QE Part 2):
- ω_Ω 2:1 harmonic `ω_Ω(r_ε,m_e) = 2 ω_Ω(r_π,m_p) = ω_CP²/ω_Ce`.
- Spectral-density → radius **method** `m_p c² = ℏω₀ n_Ω`, `r_π = n_Ω λ_CP/(2π)`, `ρ(ω)=Σ A_n δ(ω−nω₀)`,
  `A_n ∝ 1/n`, `n_Ω,p ≈ 25` (the *method* is new; the 0.841 fm *value* stays jewel-flagged).
- **`K_PV(ω)` dispersion** `K_PV(ω) = 1 + ω_p²/(ω₀²−ω²−iγω)` and the harmonic-quantized form — the ω-dependent
  dielectric M11 flags as its natural home.
- Gravitational cutoff `ω_Ω ~ √(GM/r³)` (value-use → H₀ flagged; the frequency form is new).
- Buckingham-Π **log identity** `ln(ω_Ω,1/ω_Ω,2) ∝ ln(m₁/m₂)` (Eq. 9).
- ⚠ **Keep excised:** the radius closed-forms `r_π = (5/4)ℏm_e/(m_p²c)` (→ the flagged 0.01% radii), the
  `Λ_EGM = (8π/3)ℏω_Ω` H₀ route, and the "Storti symmetry equation" `∂_a Φ + ∇·(Φv) = ∇·(log ρ/ρ₀)` (already
  slated for excision alongside `e^(-2/3)`).

## Nulls (honest)
- **Ginzburg** — no spiral-field mathematics anywhere in the corpus; only book citations, tagged
  "[unassessed external, likely fringe] — geometry only." Every *other* "Ginzburg" hit is **Vitaly Ginzburg /
  Ginzburg–Landau** superconductivity (order parameter ψ, coherence length, flux vortices) — a different
  person. **M12's analogy-only fold is complete; nothing to add.**
- **Buckingham** — the corpus's Buckingham file *is* the jewel's M7 (same three matrices, `Λ₁=4.4934`); no
  independent Π-group / mass-ratio / LENR-scaling analysis exists to fold.

## Recommended fold order
1. **G2 Greenyer beat-law + cascade (M14)** — biggest missing *mathematical layer*; provable sub-results;
   directly derives the comb and the aneutronic energetics; carries a falsifiable prediction. Mine
   `TORUS_MATHEMATICS_APPENDIX.md` (2069 lines) + `EVO_MATHEMATICAL_CORE.md`.
2. **G1 Nielsen TUFT mass-tower (M13)** — lets the jewel derive the mass spectrum; fold the *structure*, carry
   the π-inconsistency and blinded-fit flags honestly.
3. **G3–G6** lineage/method extensions into M8/M11 + a short `[credited-lineage]` note (Bostick/Puthoff/Shoulders).
4. **G7/Tier 3** Storti closed-forms into M11 (methods only; values excised).

*Provenance: three scan transcripts (this session). Formulas quoted from the named corpus files; none are
promoted — this is a to-fold roadmap with tiers and flags attached, per the project's excision discipline.*
