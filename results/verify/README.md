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
failure). Deterministic, no network. Current status: **11 / 11 PASS** on CPython 3.12.

## Claim → script coverage map

| Script | Reproduces (the `[V]` content) | Home in the jewel | Tier |
|---|---|---|---|
| `ck_eigenvalues_check.py` | roots of `tan x = x` (`λ₁R=4.4934`, first six) two ways (bisection ‖ mpmath); carrier comb ratios `1:1.719:2.427`; `c_CK(ε→0)=1/(2 j₀,₁)=0.20792`; cross-checks the engine's hardcoded `CK_ROOTS` | `MATH_TOOLKIT_BASE.md` §3, `foundation/30_CANONICAL_NUMBERS.md` §C/§H, M7-2 | `[V]` / `[credited]` |
| `r2_identity_check.py` | the exact vortex-stretching = Lamb-vector flux identity `∫ω·(ω·∇)v = ∫(∇×ω)·(v×ω)` (both forms agree ~9 sig figs) | `R2_NEAR_BELTRAMI_ENSTROPHY_THEOREM`, engine | `[V]` |
| `r2_gronwall_check.py` | the R2 enstrophy/BKM threshold `⟨η²⟩ < ν²λ₁` (time-integrated, sharp) — bounded below / blows up above | `R2_NEAR_BELTRAMI_ENSTROPHY_THEOREM` | `[V]`cond |
| `hallmhd_canonical_check.py` | the Hall two-fluid `Pm=1` coercivity and the `det = −d_i²(η−ν)²/4` obstruction to `Pm≠1` | `R3_HALLMHD_CANONICAL_ENSTROPHY`, M10 | `[V]` |
| `tuft_mass_tower_check.py` | Nielsen ζ-coefficients (`C₅=ζ(3)/12`, …), the exact `C₅/ω₃=π²/3`, lens-space `τ_R(L(n,1))=1/n`; blind-fit VALUES flagged | M13 | `[V]` core / `[flag]` values |
| `greenyer_beat_cascade_check.py` | cascade `N^L`, anapole `N⁴=256`, the golden-ratio three-wave dichotomy, Fibonacci Manley-Rowe; `N_crit` band flagged | M14 | `[V]` / `[prediction]` |
| `egm_sense_checks.py` | Storti EGM numerical audit — the 2:1 harmonic is definitional; radii/H₀ miss; `e^(-2/3)` is dead (`→72`, not 137) | M11-4 | `[V]` (audit) / `[flag]`/`[excised]` |
| `egm_mode_count_closure.py` | the Debye/Nyquist mode-count closure behind `ω_Ω`/`n_Ω`; `ℓ∝λ_C n_Ω^(-1/3)` scaling + weak-sensitivity | M11-6 | `[V]` |
| `alpha_running.py` | standard QED α running (and that it runs the *wrong way* for a geometric `~137`) — grounds the dynamical reframe | `ALPHA_DYNAMICAL_REFRAME`, M11-4(v) | `[V]` / `[flag]` |
| `alpha_scale_headroom_check.py` | bounds the α reframe's *magnitude*: zero running headroom at `m_e`, ~6 decades needed, natural window ~3× short → the 2.3% is a winding-**skeleton** error, not dynamical | `ALPHA_RESOLUTION_ASSESSMENT` | `[V]` / `[S]` |
| `alpha_genericity_check.py` | the anti-numerology denominator: hits near 137.036 from the object's real constants are *comparable to control targets* → generic; 137 is prime, object levels are `Q_H=1`/`C=±2` (not 137) → **"winding = 1/α" falsified as a derivation** | `ALPHA_RESOLUTION_ASSESSMENT` | settled-negative |
| `ck_winding_ratio_check.py` | traces the l=1 CK force-free field: the *continuous* winding-to-spin ratio is **ι ≈ 1.08 ≈ 1** (a Hopf ring, =`Q_H`), torsion holonomy O(0.1 rad) — **not 137 / not `2π/137`**; closes the continuous route the primality argument left | `ALPHA_RESOLUTION_ASSESSMENT` §3b | settled-negative |
| `g2_spin_precession_check.py` | reassess "α as internal spin precession": *conceded* — the g−2 anomaly `a=α/2π` **is** an internal precession (per orbit `2π·a = α`); but it gives `1/a≈861` not 137 (=`1/α`=`λ_C/r_e`), and is α-proportional → the framing is correctly-typed, the **value** stays open | `ALPHA_RESOLUTION_ASSESSMENT` §3c | `[credited]` / `[flag]` |
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
