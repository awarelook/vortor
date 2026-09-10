# `results/verify/` — the reproducible math model

Every load-bearing `[V]` claim in the FTGB jewel is reproduced by a script here.
Nothing is asserted that a reader cannot re-run.

## Reproduce everything (one command)

```bash
pip install -r requirements.txt          # mpmath, numpy
python results/verify/verify_all.py      # runs all checks + the engine; exit 0 iff all pass
```

`verify_all.py` runs each theory script plus `engine/ftgb_engine.py`, captures exit
codes, and prints a `PASS/FAIL` summary (it is also a CI gate — nonzero exit on any
failure). Deterministic, no network. Current status: **29 / 29 PASS** on CPython 3.12
(28 theory scripts + the engine).

## Claim → script coverage map

| Script | Reproduces (the `[V]` content) | Home in the jewel | Tier |
|---|---|---|---|
| `ck_eigenvalues_check.py` | roots of `tan x = x` (`λ₁R=4.4934`, first six) two ways (bisection ‖ mpmath); carrier comb ratios `1:1.719:2.427`; `c_CK(ε→0)=1/(2 j₀,₁)=0.20792`; cross-checks the engine's hardcoded `CK_ROOTS` | `MATH_TOOLKIT_BASE.md` §3, `foundation/30_CANONICAL_NUMBERS.md` §C/§H, M7-2 | `[V]` / `[credited]` |
| `r2_identity_check.py` | the exact vortex-stretching = Lamb-vector flux identity `∫ω·(ω·∇)v = ∫(∇×ω)·(v×ω)` (both forms agree ~9 sig figs) | `R2_NEAR_BELTRAMI_ENSTROPHY_THEOREM`, engine | `[V]` |
| `r2_gronwall_check.py` | the R2 enstrophy/BKM threshold `⟨η²⟩ < ν²λ₁` (time-integrated, sharp) — bounded below / blows up above | `R2_NEAR_BELTRAMI_ENSTROPHY_THEOREM` | `[V]`cond |
| `hallmhd_canonical_check.py` | the Hall two-fluid `Pm=1` coercivity and the `det = −d_i²(η−ν)²/4` obstruction to `Pm≠1` | `R3_HALLMHD_CANONICAL_ENSTROPHY`, M10 | `[V]` |
| `hallmhd_coupled_lyapunov_check.py` | **`Pm≠1` advance:** the `(η−ν)²` obstruction is a *canonical-variable artifact* — the coupled functional `L=½‖ω‖²+κd_i²½‖J‖²` has **diagonal coercive dissipation at every `Pm`** and controls `Z`; fluid+Lorentz productions vanish *quadratically* at the single-`λ` relaxed state; the Hall term is absorbed under `d_i‖B‖∞≲η` (linear law verified) → **removes `Pm=1`**, residual = one Hall smallness | `R3_PM_NE_1_COUPLED_LYAPUNOV` | `[V]` / `[V]cond` |
| `tuft_mass_tower_check.py` | Nielsen ζ-coefficients (`C₅=ζ(3)/12`, …), the exact `C₅/ω₃=π²/3`, lens-space `τ_R(L(n,1))=1/n`; blind-fit VALUES flagged | M13 | `[V]` core / `[flag]` values |
| `greenyer_beat_cascade_check.py` | cascade `N^L`, anapole `N⁴=256`, the golden-ratio three-wave dichotomy, Fibonacci Manley-Rowe; `N_crit` band flagged | M14 | `[V]` / `[prediction]` |
| `egm_sense_checks.py` | Storti EGM numerical audit — the 2:1 harmonic is definitional; radii/H₀ miss; `e^(-2/3)` is dead (`→72`, not 137) | M11-4 | `[V]` (audit) / `[flag]`/`[excised]` |
| `egm_mode_count_closure.py` | the Debye/Nyquist mode-count closure behind `ω_Ω`/`n_Ω`; `ℓ∝λ_C n_Ω^(-1/3)` scaling + weak-sensitivity | M11-6 | `[V]` |
| `alpha_running.py` | standard QED α running (and that it runs the *wrong way* for a geometric `~137`) — grounds the dynamical reframe | `ALPHA_DYNAMICAL_REFRAME`, M11-4(v) | `[V]` / `[flag]` |
| `alpha_scale_headroom_check.py` | bounds the α reframe's *magnitude*: zero running headroom at `m_e`, ~6 decades needed, natural window ~3× short → the 2.3% is a winding-**skeleton** error, not dynamical | `ALPHA_RESOLUTION_ASSESSMENT` | `[V]` / `[S]` |
| `alpha_genericity_check.py` | the anti-numerology denominator: hits near 137.036 from the object's real constants are *comparable to control targets* → generic; 137 is prime, object levels are `Q_H=1`/`C=±2` (not 137) → **"winding = 1/α" falsified as a derivation** | `ALPHA_RESOLUTION_ASSESSMENT` | settled-negative |
| `ck_winding_ratio_check.py` | traces the l=1 CK force-free field: the *continuous* winding-to-spin ratio is **ι ≈ 1.08 ≈ 1** (a Hopf ring, =`Q_H`), torsion holonomy O(0.1 rad) — **not 137 / not `2π/137`**; closes the continuous route the primality argument left | `ALPHA_RESOLUTION_ASSESSMENT` §3b | settled-negative |
| `g2_spin_precession_check.py` | reassess "α as internal spin precession": *conceded* — the g−2 anomaly `a=α/2π` **is** an internal precession (per orbit `2π·a = α`); but it gives `1/a≈861` not 137 (=`1/α`=`λ_C/r_e`), and is α-proportional → the framing is correctly-typed, the **value** stays open | `ALPHA_RESOLUTION_ASSESSMENT` §3c | `[credited]` / `[flag]` |
| `g_factor_soliton_check.py` | does the soliton give g=2? The naive Reed photon-ring / circulating-charge gives **g = 1** (robust); g=2 is the Dirac value (needs spinor structure). The Hopf term gives **spin-½** `[credited]` but **not** g=2 → g=2 stays `[S]`/open | `ALPHA_RESOLUTION_ASSESSMENT` §3d | `[credited]` / `[S]` |
| `g2_elementary_check.py` | g=2 resolved-in-principle: elementary leptons sit at g=2 (electron = Dirac + `α/2π`), composites deviate (proton 5.59, neutron −3.83) → **g=2 ⇔ effectively pointlike Dirac**, the *same frontier as α* ("why is the electron elementary?") | `OPEN_QUESTIONS_PRINCIPLED_RESOLUTION` §2 | `[credited]` |
| `g2_skyrme_composite_check.py` | g=2 from **FTGB's own soliton layer**: the B=1 Skyrmion (M10) is the nucleon, and Skyrme collective quantization **computes** its moment — parameter-free `μ_p/μ_n=−3/2` vs experiment −1.46 (~3%), a **composite** g-factor (`g_p=5.59`), manifestly **not** Dirac g=2 → extended solitons give composite moments; g=2 (electron) is the pointlike/elementary limit = the **same frontier as α**, shown from inside the theory | `TIER_LEDGER` §2, M10 | `[credited]` / `[S]`open |
| `g2_dirac_structure_check.py` | **g=2 re-derived from inside:** the `±λ` Beltrami doublet **is** the two Weyl chiralities (pure `P_±` eigenstates); the duality angle `θ_χ` **is** the `γ₅` chiral rotation (`H=H_max cos2θ`, Majorana at 45°); the mirror **is** `C`; with Hopf spin-½ the **Dirac algebra is internal** → g=2 is its *minimal-coupling limit*, reduced to one criterion — `π₁`(charge)/`π₃`(spin) locking (elementary lepton locked = g=2, composite decoupled) | `FRONTIER_INTERNAL_DERIVATION` | `[V]`/`[credited]`/`[S]` |
| `torque_beat_alpha_check.py` | the frontier through the theory's own lens: the g−2 anomaly **is** a beat (`ω_a=ω_s−ω_c=a·ω_c`), `α` = the spin⊗orbit beat-fraction (`2π·a=α`), the g−2 series = the harmonic/loop cascade (3-loop → measured to 5e-11), chirality = the beat's yin-yang handedness → it **types** the frontier, doesn't derive the value | `OPEN_QUESTIONS_PRINCIPLED_RESOLUTION` §5 | `[credited]` / `[S]` |
| `alpha_impedance_check.py` | the **medium** reading: `α = Z₀/(2R_K)` exactly (to 6e-15) — the vacuum's magnetic-to-electric impedance `Z₀=√(μ₀/ε₀)` over twice the quantum resistance `R_K=h/e²`; folds into the K_PV/M11 layer → types α as a medium-impedance ratio, but a restatement (both carry the constants) | `OPEN_QUESTIONS_PRINCIPLED_RESOLUTION` §5 | `[credited]` |
| `chirality_helicity_check.py` | chirality = `sign(λ)` = `sign(H)` of the Beltrami field (exact: `curl ABC=+u`, mirror `=−u`); antiparticle = `−λ` partner; the duality angle = computed helicity-mixing `θ_χ` (0°/90° = electron/positron) | `CHIRALITY_DUALITY_ASSESSMENT` | `[credited]` / `[S]` |
| `charge_conjugation_check.py` | the mirror `λ→−λ` keeps mass (`E`: +3→+3) but flips chirality (`H`: +3→−3) **and** the Reed torsion defect (`∫τ ds`: −96.7→+96.7, ratio −1.000) together → the chirality flip **is** charge conjugation C; chirality → C tied | `CHIRALITY_DUALITY_ASSESSMENT` §2b | `[S, computed]` |
| `majorana_selfdual_check.py` | the self-dual `u=(u₊+u₋)/√2`: `H=0`, `mirror(u)=u` to `0.0e+00` (C-invariant, `ν=ν̄`), `θ_χ=45°` → the neutrino rung is **Majorana**; resolves the repo's Majorana-vs-Dirac tension via the computed chirality layer | `CHIRALITY_DUALITY_ASSESSMENT` §3b | `[S, computed]` |
| `plasmoid_helicity_coherence_check.py` | the yin-yang → LENR connection: a single-λ plasmoid has `W=(λ/2)H` (`sign H = sign λ` = chirality), and Woltjer–Taylor raises `W/\|H\|` when a 2nd scale is added → relaxation selects **one λ = one chirality** = the coherent scaffold. The `±λ` object spans lepton-chirality *and* the plasmoid | LENR⊗yin-yang synthesis | `[credited, computed]` |
| `carrier_chirality_lock_check.py` | **resolves the flagged loose end:** the three CK carrier roots of `tan x=x` are all **positive** (same sign), and `sign H = sign λ` → the `{121,208,294}` kHz comb is **single-chirality**, locking the Woltjer–Taylor coherence argument (not undercut by mixed-sign content) | `TIER_LEDGER` §2 | `[V, resolved]` |
| `lenr_cop_nuclear_positive.py` | **positive core claim:** COP>1 is a **nuclear** energy release (d+d→⁴He = **23.85 MeV** mass defect, **conserved**), not over-unity — gain ~10⁴–10⁵/event; barrier lowered by **measured** screening `U_s≈300–800 eV` (enhances tunneling `exp(+936)`); the **He-4/heat = 24 MeV** signature (Miles) confirms the heat is nuclear; Δ is the one compute | LENR⊗yin-yang synthesis | `[V]`/`[credited]`/`[S]` |
| `delta_detuning_beat_check.py` | Δ reframed as the **spectral detuning** `Δλ=λ₂−λ₁` setting the beat `f_b=(v_A/2πR)\|Δλ\|` (`Δλ=3.23→f_b=87 kHz = f₂−f₁`, the comb beats); the nuclear Δ is the same **Landau–Zener gap** structure; `U_s` = source/seed/surface/screening drive → the two "inputs" are the beat model's **control parameters** | LENR⊗yin-yang synthesis | `[V]` beat / `[S]` |
| `lenr_energy_ledger.py` | the LENR energy accounting — `E_fm=2.5 MeV` retracted; rate reduces to exactly two named inputs (Δ, `U_s`); no over-unity | `LENR_MATTERWAVE_INTERACTION_MODEL` | `[V]` / `[S]` |
| `engine/ftgb_engine.py` | the whole object as one executable model: structure (`v_A`, `λ₁R`, comb, mass ladder) → dynamics (Stuart-Landau `r*=√2`, comb-lock, current-leg) → theorems (Lamb identity, R2 threshold, Hall coercivity) | consolidates the R2/R3 scripts | `[V]`/`[S]` |

## Not theory verification (excluded from `verify_all.py`)

- `dedup_scan.py` — content-hash duplicate scanner for the `F:\_QUARANTINE` knowledge-ordering tooling.
- `archive_mirror.ps1` — robocopy `/MIR` backup with a verification log (dry-run by default).

These are operational infrastructure (see `RUNBOOK.md`), not claims about the physics.

## Discipline

No fabricated numbers; every value traces to a named computation above or a credited
constant. Numerical coincidences and fits are **flagged/excised in-script**, never
promoted (`e^(-2/3)`, particle radii, H₀, blind-fit masses, the `N_crit` prediction).
No over-unity. Open items (unconditional R2/R3, the Δ LENR branching, the exact α)
are named, not hidden.
