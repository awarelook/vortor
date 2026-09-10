# Tier ledger — what is proven, what is honest-tier, and what would resolve each

**Date:** 2026-09-10. The project's honest self-assessment in one page: the solid `[V]`/`[credited]` core, and
for every `[S]`/`[flag]`/`open` item, **what would resolve it** and its **honest status**. "Seek to resolve to
proof" answered straight — resolving what is resolvable, and stating plainly what is *not* provable here (and
why fabricating it would violate the discipline). Every row cites a `results/verify/` script or a hand-off.

---

## 1. The solid core — `[V]` proven here / `[credited]` established

- **The current-leg no-go trilogy** `[V]` — a self-contained plasma/topological-fluid theorem (static `|B|=const`
  and aligned `P·v=const` no-gos; driven `S=0` realizability; the reduction of the one gate to R2). Citable today.
- **R2 conditional enstrophy/BKM bound** `[V]cond` — exact Lamb-vector identity → Gronwall, bounded *if*
  `⟨η²⟩<ν²λ₁` (`r2_identity_check`, `r2_gronwall_check`). **R3 Hall lift at `Pm=1`** (`hallmhd_canonical_check`).
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
| **"One object across all scales"** (rungs vacuum→…→nucleon) | `[S]` | Derive the mass hierarchy (`m_e/m_ν~10⁷`, `m_p/m_e=1836`) from the geometry. **`[S]`-by-nature:** it is a *coherence* claim (shared invariants); the ratios are **not** the CK ladder (1.7, 2.4), and deriving 1836/137-type numbers is the same numerology graveyard as α. Not attempted — would fail the genericity bar. |
| **α value = 1/137.036** | `[flag]` | Derive it. **Settled-NEGATIVE** (`ALPHA_RESOLUTION_ASSESSMENT`): winding `ι≈1` not 137; typed by beat/impedance/precession but never derived. It is the **shared, non-FTGB QED frontier** ("why is the electron elementary?"). Do **not** re-attempt / fabricate. |
| **g = 2** | `[S]`/open | Show the soliton's quantization is a minimally-coupled Dirac field. **Hard field theory** (Hopf→spin-½ is credited; g=2 needs the full Dirac structure). **Shown from inside the theory** (`g2_skyrme_composite_check`): FTGB's own B=1 Skyrmion (M10) *does* have a computed moment — Skyrme quantization gives `μ_p/μ_n=−3/2` (~3% of experiment), a **composite** g-factor (5.59), **not** g=2. So the extended soliton yields composite moments (correct for the nucleon); g=2 (electron) is the pointlike/elementary limit = the **same frontier as α**. **FURTHER (2026-09-10, `g2_dirac_structure`):** the Dirac bispinor *algebra* is **internal** — `±λ`=Weyl pair, `θ_χ`=`γ₅` chiral rotation, mirror=`C`, Hopf=spin-½ → g=2 is the *minimal-coupling limit* of this internal structure, reduced to one criterion: `π₁`(charge)/`π₃`(spin) locking (satisfied by the elementary lepton, broken by composites). **Derives g=2's meaning internally**; the lock itself stays `[S]`, and the α *value* stays the frontier. |
| **Matter-wave dictionary** (mass=whirl, charge=torsion-holonomy; C/Majorana) | `[S,computed]` | Contact with the QFT operators. **`[S]` by construction:** an *internal-consistency* check of FTGB's own dictionary — behaves *structurally like* C; not the QFT `C=iγ²γ⁰` (no Dirac spinor in the verified content). |
| **LENR mechanism** (scaffold enables the aneutronic channel) | `[S]` | A first-principles collective-rate calculation. `[S]` — the *energy* is `[V]`/conserved; the *mechanism* is structural. |
| **LENR rate / Δ** (B=4 branching) | `open` | **The one FTGB compute** — a topology-preserving Skyrme-HPC run (`HANDOFF_DELTA_B4_SKYRME_RELAXATION`); test the 1.4–1.9 MeV band. `U_s` is **measured**; the COP *magnitude* (1.3–1.4) is inherited field positioning, **not** FTGB-derived. |
| **R2 unconditional / at-Reynolds** | `open` | **The genuinely winnable upgrade** — the `S~10³–10⁴` GPU pseudo-spectral run (`R2_NUMERICAL_RUN_SPEC` + `r2_reference_solver`). Execution-limited, scoped, not principle-limited. |
| **R3 at `Pm≠1`** | ~~open~~ **`[V]cond`** | **ADVANCED (2026-09-10, `R3_PM_NE_1_COUPLED_LYAPUNOV` + `hallmhd_coupled_lyapunov_check`):** the `(η−ν)²` obstruction is a *canonical-variable artifact* — the coupled functional `L=½‖ω‖²+κd_i²½‖J‖²` has **diagonal coercive dissipation at every `Pm`** and controls `Z`; fluid+Lorentz productions vanish *quadratically* at the single-`λ` relaxed state (same Woltjer coherence as the carrier comb); the lone residual is a Hall smallness `d_i‖B‖∞≲η`. **`Pm=1` removed.** Unconditional large-data `Pm≠1` stays open (= open 3-D Hall-MHD). |
| **Cross-scale Δ identity** (kHz detuning ↔ MeV gap) | `[S]` | Show the plasma detuning literally sets the nuclear gap. `[S]` hypothesis; only the plasma beat is `[V]`. |
| **Same-sign-λ of the carrier comb** | ~~open~~ **`[V]`** | **RESOLVED (2026-09-10):** the three CK roots are all positive → single-chirality comb → the Woltjer–Taylor coherence argument is locked (`carrier_chirality_lock_check`). |
| **Experimental fingerprints** (comb pull, aspect ratio, transmutation-on-lattice) | prediction / `UNTESTED` | Do the measurement. **No data** — live targets. He-4/heat & aneutronic: *consistent with a contested anomaly* (Miles; ×5 scatter, contamination), accounted-for not confirmed (`EXPERIMENTAL_CONFRONTATION`). |
| **Storti radii/H₀, Ginzburg cosmology, TUFT mass values, Greenyer `N_crit`, "yin-yang universe"** | `[framework]` | Folded, **not adopted**; numerology/cosmology quarantined. `e^(-2/3)` and `E_fm=2.5 MeV` **excised**. |

## 3. Honest bottom line — where "breakthrough proof" can and cannot come from

- **Resolved this session:** the same-sign-λ lock (`[V]`) — the carrier comb is genuinely single-chirality; and
  the **R3 `Pm≠1` advance** (`[V]cond`) — the coupled functional removes the `Pm=1` restriction, localizing the
  residual to one Hall smallness (the `(η−ν)²` obstruction was a variable-choice artifact).
- **Genuinely winnable (execution, not proof-by-thought):** **R2 at Reynolds** (the scoped GPU run) upgrades the
  `[V]` core; **Δ** (the Skyrme-HPC run) closes the LENR rate. Both are packaged execute-ready in `handoffs/`.
- **Not provable here — and honestly so:** **α's value** (settled-negative; the shared QED frontier), **g=2**
  (needs Dirac quantization), and the **one-object mass hierarchy** ((`[S]`-by-nature; deriving 1836/137 is
  numerology). Claiming a "proof" of these would be exactly the fabrication the discipline forbids — the honest
  result is that they are the *frontier the theory stands at*, shared with all of physics, not a crack in it.
- **What the jewel *is*, precisely:** a citable `[V]` plasma/topological-fluid theorem + a reproducible toolkit +
  a set of exact identities, wrapped in a disciplined, falsifiable **`[S]` synthesis hypothesis** whose every
  tier is *labeled, reproducible, and honest*. The breakthroughs available are the two scoped external
  computations and the small locks; the rest is the honest frontier.

*Provenance: the 28 `results/verify/` scripts + engine (`verify_all.py` → **29/29** PASS) + the `results/` and `handoffs/` docs
cited inline. No value promoted; `e^(-2/3)`/`E_fm` excised; the α winding stays settled-negative.*
