# FTGB lineage — the toroidal-electron / polarizable-vacuum / EVO ancestors (Bostick · Puthoff · Shoulders)

**Status:** reference note (`[credited-lineage]` / `[framework]`) · **For:** FTGB project · **Date:** 2026-09-09
**Sources mined:** `Arc/Winston Bostick.md`, `Arc/Polarizable vacuum.md`, `Arc/Kenneth Shoulders.md`.

Three published lineages feed the FTGB "coherent object": a **toroidal-electron** model that
derives quantum results from a circulating electromagnetic vortex (Bostick), a **polarizable-vacuum**
model that reads gravity/inertia as a refractive-index property of the vacuum (Puthoff, with the
Penner/Kouki/Pais extensions the vault attaches to it), and an **EVO** (Exotic Vacuum Object)
program that produces self-organized toroidal charge clusters with nuclear-active behavior
(Shoulders). This note pulls the *equations* verbatim and tiers them honestly. It contains physics
only — no suppression/priority narrative.

**Tier key.** `[credited-lineage]` = the physicist's genuine, published contribution (a real figure
in the historical record). `[framework]` = a named fringe reading folded as method/analogy, not
endorsed. `[S]` = structural / contingent / speculative extension. Where a symbol is standard physics
independent of the framework, it is marked `[credited]`.

---

## 1. Winston Bostick (1916–1991) — the toroidal / "electromagnetic flywheel" electron

**WHAT.** Bostick coined "plasmoid" (1956) and photographed self-organized toroidal plasma. In
*"Toward Understanding the Nature of Fusion Energy"* (*Fusion Magazine*, May 1978), he modeled the
electron as charge `−e` circulating at `v = c` on a toroidal shell (an "electromagnetic flywheel"),
and derived the core quantum relations from classical vortex electrodynamics on that geometry rather
than postulating them. `[credited-lineage]`

**MATH.** (formulas verbatim from the Bostick note)

- **Fine-structure constant from geometry** — the ratio of major radius `R` to core radius `r₀` fixes
  `α` with no free parameter:
  `e²/ℏc = π/2 / ln(R/r₀)`   i.e.   `α = e²/ℏc = (π/2)/ln(R/r₀)`   `[credited-lineage]`
- **Flywheel (total electromagnetic) energy = rest energy:**
  `E ≈ (e²/πR)·ln(R/r₀) = mc²`   `[credited-lineage]`
- **Spin ½ from the geometry** — effective weighed mass `= 2m` (total energy `2E`), so angular
  momentum `mRc` gives
  `spin = mRc/(2m) = ½`   `[credited-lineage]`
- **Waveguide dispersion** — identical to an electromagnetic waveguide, with the Compton frequency as
  cutoff `ω_c = c/R`:
  `ω² = ω_c² + k²c²`   `[credited-lineage]`
- **Magnetic flux quantization** (toroidal topology), `Θ ≈ π` fluxons:
  `Θ ≈ πℏc/e`   `[credited-lineage]`
- **Force-free helical toroid** — "each segment exerts no force on the other segments," which is the
  Beltrami condition:
  `J × B = 0`   `[credited-lineage]` (Beltrami / force-free; `[credited]` as physics)

*Additional genuine results in the same paper (context, not core):* anomalous moment
`g ≈ 2(1 + α/2π)` (first-order QED / Schwinger term from torus geometry); de Broglie relation
`λ = h/(m_e·v_g)` from counter-rotating helical wavefunctions `ψ = R_v·exp[i(ωt−kz)]`,
`ψ* = R_v·exp[−i(ωt−kz)]`; `ΔxΔp ≥ ℏ` from the helical filament; `E = hν` from vortex energy storage.
All `[credited-lineage]` as his published derivations. **A particle is not a blob** is his governing
premise (a point charge would electrostatically explode; the torus stores the self-energy stably).

---

## 2. Harold Puthoff — the polarizable vacuum (PV), with its Penner / Kouki / Pais extensions

**WHAT.** PV treats gravity not as spacetime curvature but as a **refractive-index gradient** in the
quantum vacuum — a flat-space engineering model (Wilson 1921 → Dicke 1957 → Puthoff 2002). Reproduces
the weak-field GR tests (Shapiro delay, light deflection, perihelion precession). The vault attaches
three convergent extensions: Penner (vacuum polarization → galaxy dynamics without dark matter),
Kouki (single-potential force unification), and Pais (Superforce). `[credited-lineage]` for the core PV;
extensions tiered individually below.

**MATH — core PV (Puthoff).** (verbatim)

- **Vacuum refractive-index parameter:** `K_PV = exp(2GM/rc²)` (`= 1` flat, `> 1` near mass-energy).
  `[credited-lineage]`
- **Gravity as a dielectrophoretic gradient force:** `F_g = −mc² ∇ ln K_PV`   `[credited-lineage]`
- **Locally variable speed of light:** `c(r) = c₀ / K_PV(r)`   `[credited-lineage]`
  *(Note: the FTGB `GLOSSARY.md` records the weak-field form with a square root, `c_eff = c/√K_PV`;
  the Arc note's `c₀/K_PV` is quoted here as given.)*

**MATH — Reed identity (speculative extension).**

- `K_PV ≡ γ = 1/√(1−v²/c²)` — the vacuum dielectric constant identified with the Lorentz factor
  ("Confinement of Light"), so that engineering `K_PV` engineers `γ`. `[framework]` / `[S]`

**MATH — Penner, vacuum polarization → dark-sector-free dynamics (published).**

- **Vacuum energy density** from an induced energy-dipole density `P_E` (dipole `p_E = E⟨x⟩_t`):
  `ε_V = −∇·P_E`   `[credited-lineage]`
- **Vacuum self-gravitation** (the vacuum energy itself gravitates):
  `g_V = (G/c²)∫ (ε_V dV'/(r−r')³)(r−r')`   `[credited-lineage]`
- **Baryonic Tully–Fisher relation** derived with zero free parameters (matches McGaugh's empirical
  `M_B = Av⁴`):
  `M_B = (3/5Gg₀)v⁴`,  with characteristic scale `g₀ = (9.6±1.2)×10⁻¹¹ m/s²`   `[credited-lineage]`

**MATH — Kouki, single-potential force unification (speculative extension).**

- One Yukawa-type potential parameterized by quantum number `n` — `n=0` strong → `n→∞` gravity:
  `V(r) = (K/r)·exp(−mr/√(n+1))`   `[framework]` / `[S]`
- Zero-point / rest-mass identity (vacuum-impedance model): `½ℏω₀ = mc²` — "mass IS vacuum coupling."
  `[framework]` / `[S]` (see §3, where FTGB uses this as the EVO vacuum-coupling rung).

**MATH — Pais, Superforce (speculative extension).**

- `S_F = c⁴/G` — the "Superforce" (numerically the Planck force, `~10⁴⁴ N`). The *quantity* `c⁴/G` is
  standard `[credited]`; the "Mother of All Forces" reading is `[framework]` / `[S]`.
- **PV bridge:** since `c = c₀/K_PV`, `S_F(r) = c₀⁴/(K_PV⁴·G)` — the Superforce varies wherever
  `K_PV ≠ 1`. `[framework]` / `[S]`

---

## 3. Kenneth Shoulders (1927–2013) — EVOs (Exotic Vacuum Objects) and their energetics

**WHAT.** Shoulders discovered and characterized **EVOs** — dense, self-organized charge clusters
(a.k.a. charge clusters; "ectons," "micro ball lightning" elsewhere) that self-confine as force-free
toroidal (Beltrami) eigenmodes and show excess energy, transmutation, and anomalous tunneling
(patents US 5018180 / 5123039 / 5148461). They are the microscale instance of the same toroidal
attractor as Bostick's plasmoids. `[credited-lineage]`

**MATH / quantitative claims.** (verbatim from the Shoulders note)

- **Transmutation energetics** — EVs carry `~10⁷ protons` with sufficient kinetic energy to overcome
  the **Coulomb barrier** → documented transmutation of palladium targets (micrographs + X-ray
  microanalysis, Shoulders & Shoulders 1996). `[credited-lineage]`
- **Stability model (Jin & Fox, 1996)** — EV stability from a **helical vortex ring** with
  "extraordinary poloidal circulation"; poloidal-filament energy density stated as `100×` higher than
  in a supernova; a spherical charge cluster is unstable and pinches into a toroid by force balance.
  `[credited-lineage]`
- **Formation mechanism (Ziolkowski, 1991)** — EV formation time set by a **vacuum-polarization
  displacement-current** term of the same order as the plasma-frequency period; the quantum potential
  compensates Coulomb repulsion. `[credited-lineage]`
- **Mass-as-vacuum-coupling rung** — `½ℏω₀ = mc²` (zero-point energy of the oscillator = rest energy):
  the EVO read as a vacuum-coupled object whose rest mass *is* its vacuum binding. `[framework]` / `[S]`
  *(Source note: in the vault this equation is Kouki's vacuum-impedance relation, carried into the EVO
  reading as the coupling principle; it is not Shoulders' own published formula.)*

---

## 4. How it connects to the FTGB object

**Bostick → the α reframe.** Bostick's `α = (π/2)/ln(R/r₀)` is the ancestral move of getting the
fine-structure constant out of one **torus aspect ratio** `R/r₀`, with the electron read as a
force-free (`J×B = 0`) toroidal vortex — exactly the FTGB coherent object (a driven Beltrami–Hopf
toroidal soliton) and its **whirl/winding number** `N_W = α⁻¹ ≈ 137`. FTGB does **not** inherit the
claim uncritically: the project's geometric winding lands at `q_geom ≈ 140.2`, a `+2.31%` miss of
`137.036`, and `ALPHA_DYNAMICAL_REFRAME` treats that gap **dynamically** — a magnetic-vacuum
(anti-screening) IR-fixed-point flow, not a static geometric or `e^(-2/3)` screening factor — while
holding the winding↔α coincidence at `[flag]` (it fails the 0.5% bar; closest to 140, not 137).
Bostick supplies the *geometry-fixes-α* intuition; FTGB keeps it honest as a framed IR fixed point.

**Puthoff → M11.** PV *is* the vacuum layer of FTGB. `K_PV(r) = exp(2GM/rc²)` and gravity as
`F_g = −mc²∇ln K_PV` are shared verbatim by Storti's **EGM / M11** reading (the PV energy-gradient of a
mass as a band-limited Fourier harmonic-beat spectrum) and by Reed's QWM. M11 is where FTGB folds
Puthoff's refractive-vacuum gravity as a *method* (a beat-spectrum representation of `K_PV`), tiered
`[framework: Storti]` over `[credited: Puthoff]`. The speculative extensions stay quarantined: the
`K_PV ≡ γ` identity, Kouki's `V(r)` force-unification potential, and Pais's Superforce
`S_F = c₀⁴/(K_PV⁴ G)` are `[framework]`/`[S]` and are **not** load-bearing; crucially, FTGB claims **no
net energy extracted from the ZPF** (the vacuum is a drive medium, not a source; `e^(-2/3)` excised).

**Shoulders → the resonator EVO rung + the LENR model.** Shoulders' EVO is the historical original of
FTGB's **resonator EVO rung** — the macroscopic resonance scaffold of the resonator family
(`resonator_family.html`), carrying the inharmonic Chandrasekhar–Kendall carrier comb {121, 208, 294}
kHz. In `LENR_MATTERWAVE_INTERACTION_MODEL`, the EVO is placed honestly as the *verified environment*,
not the reaction: it supplies (i) the screening `U_s` that lowers the Coulomb barrier — the modern
counterpart of Shoulders' `~10⁷ protons` crossing the barrier and transmuting Pd — (ii) the collective
mode basis, and (iii) the resonant beat channels that bridge the matter-wave frequency ledger
`Σ ħω_i = Σ ħω_f + ħω_release`. Jin & Fox's helical-vortex-ring stability and Ziolkowski's
vacuum-polarization formation are the ancestral form of the object's force-free toroidal topology and
its vacuum-coupled drive. FTGB adds the discipline: **baryon-conserving** `d+d → ⁴He` only, aneutronic
via an E0 collective mode, with the two missing numbers (branching Δ, screening `U_s`) named `[open]`
/ `[inherited]`, **not** fabricated, and **no over-unity** claimed.

---

*Draft only. Formulas quoted verbatim from the three Arc source notes; FTGB-internal anchors from
`GLOSSARY.md`, `results/ALPHA_DYNAMICAL_REFRAME_2026-09-09.md`, and
`results/LENR_MATTERWAVE_INTERACTION_MODEL_2026-09-09.md`. Nothing here is promoted beyond its tier.*
