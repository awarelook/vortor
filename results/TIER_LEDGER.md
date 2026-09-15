# Tier ledger — what is proven, what is honest-tier, and what would resolve each

**Date:** 2026-09-10, last updated **2026-09-14** (LENR disposal-chain convergence + the jewel-audit
capture pass: corridor sharpening, two-bar frontier, forgotten-batch checks). The project's honest self-assessment in one page: the solid `[V]`/`[credited]` core, and
for every `[S]`/`[flag]`/`open` item, **what would resolve it** and its **honest status**. "Seek to resolve to
proof" answered straight — resolving what is resolvable, and stating plainly what is *not* provable here (and
why fabricating it would violate the discipline). Every row cites a `results/verify/` script or a hand-off.

**Inclusion & validity policy (governance).** The jewel is a **new** theory, judged by its own
*reproducibility, prediction, internal consistency, and alignment with results* — **not** by consensus or
comparison to other theories. What the jewel carries: (1) **`[V]`/locked** promoted; (2) **hypothesis-to-test**
and **reasonable-frontier** kept at their tier (incl. the `[speculative frontier]` doc
`SPECULATIVE_FRONTIER_MICROTUBULE_HOLOGRAPHY_2026-09-10.md`, firewalled from the `[V]` core); (3)
**coincidences/numerology preserved as CLUES**, computed and logged in `COINCIDENCE_LEDGER.md` (everything is
connected — a clue may later lead somewhere). What is removed: **only superseded or inaccurate** content
(`e^(-2/3)`, `E_fm=2.5 MeV`, the α-winding-derivation). Nothing is excluded for lacking consensus; the bar is
*testable meaning + structure + reproducibility*.

---

## 1. The solid core — `[V]` proven here / `[credited]` established

- **The current-leg no-go trilogy** `[V]` — a self-contained plasma/topological-fluid theorem (static `|B|=const`
  and aligned `P·v=const` no-gos; driven `S=0` realizability; the reduction of the one gate to R2). Citable today.
- **R2 conditional enstrophy/BKM bound** `[V]cond` — exact Lamb-vector identity → Gronwall, bounded *if*
  `⟨η²⟩<ν²λ₁` (`r2_identity_check`, `r2_gronwall_check`). **R3 Hall lift at `Pm=1`** (`hallmhd_canonical_check`).
- **The DRIVEN coherent state** `[V]` — forcing the exact Beltrami field with `f=νλ²u_B` makes it an
  **exact time-independent solution** (the object *sustains itself*; the drive only replaces the viscous
  loss, the Lamb-null advection adds nothing), and it is a **stable attractor** — a 30% perturbation decays,
  a Taylor–Green base drifts (`r2_driven_beltrami_attractor_check`). **Now swept across Reynolds**
  (`r2_reynolds_sweep_check`): the attractor persists and the enstrophy stays bounded across **Re ≈ 126 → 628**
  (32³, confirmed at 48³), with the attraction not weakening as Re rises. Extends exact-state regularity from
  freely-decaying to driven/sustained, now on a robust Reynolds curve; the unconditional high-Re case stays
  open (needs the `S~10³–10⁴` GPU run).
- **The N-mode Woltjer theorem** `[V]` — fixed-helicity energy minimization over any `N` distinct-eigenvalue
  Beltrami modes is exactly a **linear program** whose minimum is always the single lowest-eigenvalue **pure**
  mode; no static multi-mode mixture is ever a critical point (`nmode_woltjer_lp_check`, corpus fold). So a
  beat-carrying structure survives only by **driven regeneration** against Taylor relaxation — "heartbeat, not
  flywheel" is *generic*, grounding the driven Stuart–Landau core. Companion `[V]`: integer **winding is
  protected away from field zeros and can slip only through them** — both the protection (7e-16) and its exact
  boundary observed (`fput_winding_conservation_check`).
- **Exact identities** `[V]` — the CK carrier index `tan x=x` (`ck_eigenvalues_check`); **chirality = sign(λ) =
  sign(H)** and the carrier comb is **single-chirality** (`chirality_helicity_check`, `carrier_chirality_lock_check`);
  the Nielsen ζ-coefficients incl. `C₅/ω₃=π²/3` (`tuft_mass_tower_check`); the Greenyer cascade `N^L`, anapole `N⁴`,
  Fibonacci (`greenyer_beat_cascade_check`); the beat-from-detuning `f_b=v_A|Δλ|/2πR` (`delta_detuning_beat_check`);
  the EGM audit (numerology dead) (`egm_sense_checks`); **`α = Z₀/2R_K`** and the g−2 beat (`alpha_impedance_check`,
  `torque_beat_alpha_check`); the **nuclear energy accounting** `d+d→⁴He = 23.847 MeV`, conserved (`lenr_cop_nuclear_positive`).
- **`[credited]`** — Beltrami/CK, Woltjer–Taylor/Moffatt, Skyrme B=4, BKM/Chae–Degond–Liu, Puthoff PV, the ZPF
  spectrum, measured screening `U_s`, g=2 (Dirac), spin-½ from Hopf (Wilczek–Zee / Finkelstein–Rubinstein), the
  0νββ limits, the Miles He-4/heat correlation (as a *measurement*).

## 2. The resolution ledger — every open item, what would resolve it, honest status

| Item | Tier | What would resolve it → **honest status** |
|---|---|---|
| **Mass hierarchy** (`m_p/m_e=1836`, `m_e/m_ν~10⁷`) | `[V-us]` + `[credited: peer-reviewed TUFT]` | The Nielsen–TUFT mechanism (Proca–Beltrami `m=ħλ/c`) carries the hierarchy in an analytic-torsion exp-dressing. The quark tower completes 6/6 masses to <0.5% as **five parameter-free ratio predictions** from a single scale (the Higgs VEV): every coefficient is a closed-form ζ-value, so the ratios carry no continuous freedom (`nielsen_mass_completion_check`). Its **topological inputs are reproduced in-repo** `[V-us]` — `ℓ=6` (the trefoil `(2,3)`-torus-knot surface self-linking, Gauss integral), `√3/2=cos(π/6)`, and the `S³` Ray–Singer determinant `ζ'(-2)=-ζ(3)/4π²` (`nielsen_topology_forcing_check`). The one framework piece is the **physical identification map** (knot↔generation): a single natural ordering rule (generation = knot by crossing number), monotone with mass, predictive (gen-4=figure-8) — a peer-reviewed framework hypothesis (particle=knot), not a math theorem; open sub-question: **why exactly 3 generations** (`nielsen_identification_map_check`; full assessment `NIELSEN_MASS_MAP_ASSESSMENT_2026-09-11.md`). The **π-power question is resolved**: `ζ_B(s)=ζ(s−2)−ζ(s)` forces the `n²` coefficient to `ζ'(-2)=-ζ(3)/4π²` (`curl_spectral_zeta_pi_power_check`). **Neutrino: Majorana** (self-dual `H=0` = both suppressed mass and `C`-invariance; `0νββ` decides). `6π⁵≈m_p/m_e` (0.0019%) is a logged clue; numerology barred. |
| **α value** | `[flag]` / settled-neg | On the correct object — a standing-wave resonator in the medium + point defect, not a loop (`alpha_resonator_imbalance_check`) — the electro/magneto imbalance is **0** from the mode (equipartition), **0** from the medium (non-dispersive, canon §I), and **= α only via inserted `e`** (defect = `r_e/λ_C`, circular). And **α runs** — `1/137.036` is the IR endpoint, not a fixed target; the theory's `K_PV(q²)` dielectric flow *is* the running. **Frontier reduced to ONE quantity:** the running coupling's *anchor* = the charge MAGNITUDE `e`. Topology quantizes charge (integer winding/Hopf); the magnitude/scale is **unpinned** — the shared elementary-electron frontier. Winding `ι≈1` not 137; typed by beat/impedance/precession; never derived. Do **not** fabricate. |
| **g = 2** | `[S]`/open | Show the soliton's quantization is a minimally-coupled Dirac field (Hopf→spin-½ is credited; g=2 needs the full Dirac structure). From inside the theory (`g2_skyrme_composite_check`): FTGB's own B=1 Skyrmion (M10) *does* have a computed moment — Skyrme quantization gives `μ_p/μ_n=−3/2` (~3% of experiment), a **composite** g-factor (5.59), **not** g=2. So the extended soliton yields composite moments (correct for the nucleon); g=2 (electron) is the pointlike/elementary limit = the **same frontier as α**. The Dirac bispinor *algebra* is **internal** (`g2_dirac_structure`) — `±λ`=Weyl pair, `θ_χ`=`γ₅` chiral rotation, mirror=`C`, Hopf=spin-½ → g=2 is the *minimal-coupling limit* of this internal structure, reduced to one criterion: `π₁`(charge)/`π₃`(spin) locking (satisfied by the elementary lepton, broken by composites). **Derives g=2's meaning internally**; the lock itself stays `[S]`, and the α *value* stays the frontier. |
| **Matter-wave dictionary** (mass=whirl, charge=torsion-holonomy; C/Majorana) | `[S,computed]` | Contact with the QFT operators. **`[S]` by construction:** an *internal-consistency* check of FTGB's own dictionary — behaves *structurally like* C; not the QFT `C=iγ²γ⁰` (no Dirac spinor in the verified content). |
| **LENR mechanism** (active site enables the aneutronic channel) | `[S]` | A first-principles collective-rate calculation. `[S]` — the *energy* is `[V]`/conserved. **Refined (disposal chain, `LENR_EXPLANATORY_RESOLUTION_MAP` §6.2):** the γ-quiet `0⁺→0⁺` disposal *operator* is **E0**/collective `[credited-required]` (the toroidal *dipole*/anapole is a forbidden 0→0 double-zero); the anapole scaffold is the **active site** = slow confinement/coherence at *assembly* `[S]`, NOT the 24-MeV disposal operator. |
| **LENR rate / Δ** → the **entrance-channel assembly corridor** | `open` | **The one FTGB compute, now CONVERGED** (a 7-check disposal chain retired every escape route): the open problem is **not** "the disposal" and **not** one matrix element — it is whether coherent slow assembly raises the bound-⁴He fraction **above the measured ~10⁻⁷** aneutronic baseline (E1/isospin-forbidden; Wilkinson–Cecil PRC **31**, 2036 (1985)), steering the B=4/B=8 Skyrme trajectory to compact bound ⁴He — the moduli-space/HPC run (`HANDOFF_NEARBPS_DELTA_RUN`). **Sharpened 2026-09-14 (`entrance_corridor_survival_check`):** the "`≥3` open objects" **collapse to ONE corridor question** — ⁴He has no bound excited states (census) and supra-threshold dwell dies in zeptoseconds (survival), so the only route is a **dissipative sub-breakup corridor** shedding all 23.85 MeV during assembly. **Two data bars** (`delta_b4_landau_zener_bridge_check` TEST 2b): existence `>10⁻⁷`; sufficiency `n/⁴He ≤ 10⁻⁹` ⇒ `Δ_suff = 5.47×Δ_dom` ⇒ derived crossing fence `β·\|dF\| ≤ 0.874 MeV/fm`. `U_s` **measured**; COP *magnitude* (1.3–1.4) inherited, **not** FTGB-derived. |
| **A=4 corridor census + survival** | **`[V]`-arith / `[credited]`** | **NEW 2026-09-14** (`entrance_corridor_survival_check`): no bound excited ⁴He states (TUNL census — first excited 0⁺₂ 20.21 MeV > p+t 19.815) ⇒ no sub-threshold rung; supra-threshold half-life ~9×10⁻²² s ⇒ slow dwell settled-negative; corridor budget 4.03 MeV pre-compound / 23.85 MeV total. Forces the corridor formulation. |
| **Multibody sync capture** (Kuramoto onset, Aizawa λ_max) | **`[V]`** | **NEW 2026-09-14** (`multibody_sync_capture_check`): the Grand Synthesis Part-D orphan `[V]`s recomputed in-repo — Kuramoto N=800 Lorentzian onset P=1.20 (synthesis: ~1.2), r(2K_c)=0.69 (mean-field 0.71); Aizawa λ_max=0.094>0 by Benettin (lit. band 0.10–0.124). Identifications stay `[S]`/`[analogy]`. |
| **Transmutation Q-values** | **`[V]`-arith** | **NEW 2026-09-14** (`transmutation_qvalue_arithmetic_check`): Cs-133+4d→Pr-141 = 50.493 MeV, Sr-88+4d→Mo-96 = 53.412 MeV from vendored AME2020, baryon/charge conservation asserted; anchor reproduces 23.847. **Bookkeeping only** — mechanism `[S]`, rate open; baryon-conserving ≠ decay. |
| **StageD: BPS first-order ρ_eff structure** | **`[V]`-arith / proxy** | **NEW 2026-09-15** (`delta_b4_stageD_bps_overlap_check`): the audit's "first-order Δ is pure quadrature" scoping **half-refuted** — on the exact ASW compacton the L₂ piece **log-diverges at the boundary** (2·ln10/decade, computed) while L₄ is finite (11.886) → only c₄ is quadrature. Delivered: the density-geometry **proxy bracket [0.55, 0.96]** (CS-normalized Franck–Condon, 3 crossing geometries, grid-converged) ⇒ **new constraint: ρ_eff ~ 0.07 CANNOT come from density geometry — the suppression must live in orientation/FR-phase space**. Production ρ_eff stays the external run, now pointed at orientation structure first. |
| **Beat-modulated tunneling (GHz/THz)** | **`settled-neg`** | **NEW 2026-09-15** (`beat_modulated_tunneling_nogo_check`, torus_project_repo salvage): the pre-jewel campaign's "coherence gain 1.334" is fence-killed — beat frozen across any tunneling attempt (`τ/T_beat≈3e-7`), quanta 6.7–11.7 OOM short; the vendored artifact is also internally inconsistent (~82 OOM vs WKB-to-contact at its own barrier). The M16 kHz pump fence extends unchanged to GHz/THz. Screened tunneling (`U_s` measured) and the macroscopic rate-gate `[S]` untouched. Survey: `SALVAGE_SURVEY_TORUS_REPO_2026-09-15`. |
| **R2 unconditional / at-Reynolds** | `open` (driven case **advanced**) | **Reapproached in-environment**: the DRIVEN coherent state is an **exact steady solution** `[V]` and a **stable attractor** (`r2_driven_beltrami_attractor_check`), now **swept across Reynolds** (`r2_reynolds_sweep_check`) — the attractor persists and the enstrophy stays bounded across **Re ≈ 126 → 628** (32³, confirmed 48³), the attraction not weakening as Re rises. So exact-state regularity extends to the driven/sustained case on a robust Reynolds curve. What stays open is *unconditional* regularity at high Reynolds: the `S~10³–10⁴` GPU pseudo-spectral run (`R2_NUMERICAL_RUN_SPEC` + `r2_reference_solver`) — execution-limited, scoped, not principle-limited. (The Δ-Skyrme compute is genuinely NOT in-environment: ~15 h/sweep in pure numpy, unwinds at affordable `dx`; the near-BPS-perturbative route + `HANDOFF_NEARBPS_DELTA_RUN` is the recommended external run.) |
| **R3 at `Pm≠1`** | ~~open~~ **`[V]cond`** | The `(η−ν)²` obstruction is a *canonical-variable artifact* (`R3_PM_NE_1_COUPLED_LYAPUNOV` + `hallmhd_coupled_lyapunov_check`) — the coupled functional `L=½‖ω‖²+κd_i²½‖J‖²` has **diagonal coercive dissipation at every `Pm`** and controls `Z`; fluid+Lorentz productions vanish *quadratically* at the single-`λ` relaxed state (same Woltjer coherence as the carrier comb); the lone residual is a Hall smallness `d_i‖B‖∞≲η`. **`Pm=1` removed.** Unconditional large-data `Pm≠1` stays open (= open 3-D Hall-MHD). The plasmoid itself does **not** satisfy that smallness (`r3_hall_smallness_physical_check`) — `d_i=0.296 m > R=0.12 m`, `S_di=d_i v_A/η≈15–2400≫1` — it is **strongly Hall-mediated**, living *outside* the regime R3 proves regular; the gap is named in physical units (does not refute the conditional theorem). |
| **Cross-scale Δ identity** (kHz detuning ↔ MeV gap) | LITERAL identity **[settled-neg]** ; structural survivor = **shared-schema analogy** ; macroscopic gate **[S]/falsifiable** | **RESOLVED (M16 audit, `cross_scale_slow_scale_audit_check`, arithmetic `[V]`).** The **LITERAL "kHz = MeV gap" identity is DEAD** — a settled-negative by **~16.8 OOM** (`E_beat=h·f_beat=0.360 neV` vs `Q=23.847 MeV`). The full 8-scale audit shows every nuclear-internal / lattice / plasma / LZ-sweep scale sits **+7.5 to +17.6 OOM ABOVE** the beat; the only kHz hits are the object-Alfvén beat itself (0 OOM **by construction** — tautological, must never be cited as evidence) or **field-tunable** atomic/molecular splittings a control target also hits (⁴He has `I=0` → no nuclear Zeeman → that reactant-only bridge is empty). So **87 kHz is a MACROSCOPIC-COLLECTIVE (object-Alfvén/MHD) scale, not nuclear-internal.** The **PUMP reading is DOUBLY-closed [settled-neg]:** parametric short by 15.7 OOM (`rhythm_parametric_resonance_check` TEST 4) **AND** slow-adiabatic killed by `τ_cross/T_kHz≈10⁻¹⁸` (the nuclear crossing is frozen/DC across a kHz cycle). **Two ideas that wore the one phrase "detuning-gap" are now separated:** **(A)** the structural nuclear LZ branching gap `Δ_nuc` — **kHz-FREE** (swept at nuclear velocity), the legitimate B=4 theory: **LZ formula `[credited]` math / d+d identification `[S]` / rate open** (`delta_b4_landau_zener_bridge_check`); "detuning-gap" is a **shared-schema analogy** (von Neumann–Wigner codim-1, disjoint Π-groups, **zero transferred number**, explicitly **not** a forced law, **not** a pump). **(B)** the macroscopic 87 kHz (or half-beat 43.57 kHz) beat as a slow **yield-GATE / duty-cycle** on the collective object — **`[S]`, falsifiable** by a beat-locked yield step surviving an H₂ (non-fusable) control, and NOT touching the conserved 23.847 MeV **`[V]`** ledger. The conserved energy ledger and the cold LZ B=4 resolution stand unchanged. |
| **Same-sign-λ of the carrier comb** | ~~open~~ **`[V]`** | **RESOLVED (2026-09-10):** the three CK roots are all positive → single-chirality comb → the Woltjer–Taylor coherence argument is locked (`carrier_chirality_lock_check`). |
| **Experimental fingerprints** (comb pull, aspect ratio, transmutation-on-lattice) | prediction / `UNTESTED` | Do the measurement. **No data** — live targets. He-4/heat & aneutronic: *consistent with a contested anomaly* (Miles; ×5 scatter, contamination), accounted-for not confirmed (`EXPERIMENTAL_CONFRONTATION`). |
| **Storti radii/H₀, Ginzburg cosmology, TUFT mass values, Greenyer `N_crit`, "yin-yang universe"** | `[framework]` | Folded, **not adopted**; numerology/cosmology quarantined. `e^(-2/3)` and `E_fm=2.5 MeV` **excised**. |

## 3. Honest bottom line — where "breakthrough proof" can and cannot come from

- **Settled `[V]`:** the same-sign-λ lock — the carrier comb is genuinely single-chirality; the **R3 `Pm≠1`**
  result (`[V]cond`) — the coupled functional removes the `Pm=1` restriction, localizing the residual to one Hall
  smallness (the `(η−ν)²` obstruction is a variable-choice artifact); and the **TUFT π-power** form
  (`curl_spectral_zeta_pi_power_check`) — the S³ curl spectral zeta forces `ζ′(−2)=−ζ(3)/4π²`, so the π²-carrying
  forms are genuine and the "pure `ζ(3)/12`" is a mis-attributed different object.
- **Genuinely winnable (execution, not proof-by-thought):** **R2 at Reynolds** (the scoped GPU run) upgrades the
  `[V]` core; **Δ** (the Skyrme-HPC run) closes the LENR rate. Both are packaged execute-ready in `handoffs/`.
- **The frontier, at its sharpest:** **α's value** is settled-negative *and* reframed — α **runs** (1/137.036 is
  the IR endpoint), and on the correct object (resonator-in-medium + point defect) every imbalance channel is 0 or
  circular, so the frontier reduces to ONE quantity: the running coupling's *anchor* = the unpinned charge
  magnitude (topology quantizes charge but not its magnitude). **g=2's meaning is derived internally** (the ±λ
  Weyl / θ_χ=γ₅ / C / Hopf-spin-½ Dirac algebra; g=2 = its minimal-coupling limit, reduced to the π₁/π₃ lock — the
  lock itself stays `[S]`). The **mass hierarchy** is not numerology-circular: the **quark tower completes 6/6
  masses to <0.5% as FIVE parameter-free ratio predictions** from a *single* continuous scale (the Higgs VEV) +
  closed-form ζ-value coefficients + knot invariants (`nielsen_mass_completion_check.py`, `[V-us]` arithmetic), with
  the topological inputs (`ℓ=6`, `√3/2=cos π/6`, `ζ'(-2)=-ζ(3)/4π²`) reproduced in-repo `[V-us]`
  (`nielsen_topology_forcing_check.py`). The residual is the framework's **physical identification map**
  (knot↔generation) — a peer-reviewed hypothesis (particle=knot), not a math theorem; sharpest open sub-question:
  why exactly 3 generations. Claiming a *proof* of the α value or of the identification map would be fabrication —
  those remain the frontier; the theory supplies the *structure* of all three and names the single residual in
  each. The `6π⁵ ≈ m_p/m_e` (0.0019%) coincidence is kept as a computed `[flag]` clue
  (`nielsen_mass_completion_check.py` TEST 4, `COINCIDENCE_LEDGER`).
- **What the jewel *is*, precisely:** a citable `[V]` plasma/topological-fluid theorem + a reproducible toolkit +
  a set of exact identities, wrapped in a disciplined, falsifiable **`[S]` synthesis hypothesis** whose every
  tier is *labeled, reproducible, and honest*. The breakthroughs available are the two scoped external
  computations and the small locks; the rest is the honest frontier.

*Provenance: the 80 `results/verify/` scripts + engine + the synthesis modeler + the resonator simulation `engine/ftgb_resonator_sim.py` (`verify_all.py` → **83/83** PASS) + the `results/` and `handoffs/` docs
cited inline; every coincidence/flag is computed and logged in `COINCIDENCE_LEDGER.md`. No value promoted;
`e^(-2/3)`/`E_fm` excised; the α winding stays settled-negative.*
