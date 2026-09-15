# The Coincidence Ledger — compute every coincidence, log the outcome, keep it as a clue

**Author:** Nathaniel Hanks · **Date:** 2026-09-10
**Standing practice (core function).** Do **not** hand-wave "numerology." For **every** numerical
coincidence, near-miss, or flagged relation in the corpus: **compute it, record value / target /
deviation, run a genericity check where a hit is claimed, and log a verdict.** Coincidences are kept as
**clues** — reproducible, permanent, never promoted above their tier. This is ordinary science
(check → record → learn); a settled-negative that is *computed and logged* is a result, not a dead end.
**Reproduced by:** `results/verify/coincidence_ledger_check.py` (+ `egm_alpha_radii_H0_principle_calc.py`,
`alpha_genericity_check.py`, `egm_sense_checks.py`, `ck_winding_ratio_check.py`).

**Verdict tiers:** `DERIVED` (closed form/theorem — not a coincidence) · `RESTATEMENT` (exact, both sides
carry the same constants) · `GENERIC` (near-miss comparable to control-target hits) · `BACK-FIT` (the
"match" needs a factor solved *from* the answer) · `CIRCULAR` (inputs defined *through* the target) ·
`DEAD` (the proposed factor doesn't even produce the claimed correction) · `COINCIDENCE` (close, no
mechanism — logged as a clue, `[flag]`).

**Salvaged governance lessons (from the corpus ark's `BEST_LESSONS`/`cascade_vacuum_bridge`, folded
2026-09-13 — each earned by a caught error there):** (1) **two routes to the same number must be *proven
equivalent*, never assumed** — coincidence of outputs is not proof of identity (the corpus verified its
7/8-factor routes explicitly before trusting them); (2) **near-integers are documented, not promoted**
(already this ledger's practice — restated as a standing rule); (3) **self-consistency ≠ derivation** — a
loop that returns its own input (X → law → X) is labeled circular, not derived; (4) **run the cheap
topology/Stokes triviality check *before* building machinery** — a corpus AB-flux program built a full
Biot–Savart solve for a loop class that homotopy shows is trivial (`∮A·dl ≡ 0`); for a solid torus there is
exactly **one** AB flux class (the meridian). Check whether the target is already topologically determined
first.

---

## The log (computed 2026-09-10)

| Coincidence | value | target | dev | verdict |
|---|---|---|---|---|
| `α = Z₀/(2 R_K)` | 0.00729735 | α | 0.000% | **RESTATEMENT** — both sides carry `e, μ₀, c, h` |
| `1/(20 φ⁴)` vs `1/α` | 137.082 | 137.036 | 0.034% | **COINCIDENCE** `[flag]` — `20=C(6,3)` hand-chosen, no QED running |
| `140.2 · e^(−2/3)` vs `1/α` | 71.98 | 137.036 | 47% | **DEAD** `[excised]` — gives 72, not 137 |
| winding `ι` vs `1/α` | ~1.08 | 137.036 | 99% | **GENERIC** — Hopf ring `=Q_H`, not 137 |
| `c_CK(ε→0)=1/(2 j₀,₁)` | 0.207915 | 0.20792 | 0.002% | **DERIVED** — closed form (first zero of `J₀`) |
| `6 π⁵` vs `m_p/m_e` | 1836.12 | 1836.15 | **0.0019%** | **COINCIDENCE** `[flag]` — famous (Lenz 1951), **no mechanism** |
| `φ¹⁶` vs `m_p/m_e` | 2207 | 1836.15 | 20% | **GENERIC** — no clean `φⁿ` |
| `137²` vs `m_p/m_e` | 18779 | 1836.15 | 923% | **GENERIC** — no `137ⁿ` |
| EGM `r_π=(¾)λ_CP²/λ_Ce` | 8.6e−20 m | 8.41e−16 m | ~10⁴× | **BACK-FIT** — forward misses; `n_Ω≈25` solved from `r_p` |
| EGM `H₀=√(GM/R³)/H₀` | 0.7071 | 1 | — | **CIRCULAR** — `M,R` defined via `H₀` → `=1/√2` identically |
| EGM 2:1 harmonic `ω(e)/ω(p)` | 2 | 2 | 0.000% | **RESTATEMENT** — `ω_Ω(e)=ω_CP²/ω_Ce=2ω(p)` by definition |
| `π²/3` (TUFT `C₅/ω₃`) | 3.28987 | 3.2899 | 0.001% | **DERIVED** — RESOLVED: `ω₃=ζ′(−2)` genuine, pure form a category error |
| ~~ABC-proxy OAM order `N` vs the triad~~ | 3 | 3 (CK lines, 3-6-9) | exact | **SUPERSEDED** `[clue, retired]` — a point-group `N=3` from the space-filling **ABC proxy** (a 3-fold body diagonal, generic to the `A=B=C` field). Superseded: the theory's localized object is the fractal-toroidal **anapole** Reeb resonator (`oam_toroidal_resonator_resolution_check.py`), which has *no* point-group OAM ladder; the real ladder is the self-similar **cascade** `N` (`N^3`/`N^4` per level). The `3`-vs-triad match was a proxy coincidence, not the object's — kept as a retired clue |
| comb half-beat vs Klimov `43–46 kHz` window | 43.57 kHz | 43–46 kHz | inside | **COINCIDENCE** `[flag]` (Arc salvage 2026-09-13) — the canon comb's half-beat `(f₂−f₁)/2 = 43.57 kHz` lands inside the band Klimov claims optimal for anomalous effects (*JCMNS* 19, 67 (2016)); `(f₃−f₂)/2 = 42.86` sits just below. **Why it stays a clue:** absolutes carry the `v_A` band (5–13×), so the match dissolves off-anchor; Klimov's window is an unreplicated single-group claim (field journal); the source vault's "44.5 kHz from CK + Pd-D sound speed" is its author's own arithmetic, not independent convergence. Computed in `coincidence_ledger_check.py` |

**Genericity gate (why `137` is not "special").** Sweeping `k·φ^a·π^b` (small integers, `k∈{½…6,20}`)
lands **0 hits within 0.5%** of `137.036` — the *same* as random control targets (0–1 hits). A number the
object's own constants cannot cleanly reach is, by this test, **generic**: the near-misses are what you
expect by chance, not a signal. (Full control-target denominator in `alpha_genericity_check.py`.)

## M16 additions — rhythm dynamics (computed 2026-09-14)

Three entries from the M16 rhythm-dynamics fold (`rhythm_parametric_resonance_check.py`,
`duffing_backbone_check.py`). The first is a **settled-negative WIN** (a clue disciplined, not a dead end);
the second is a **pre-registered falsifier** (a prediction); the third a weak `[flag]` retired on arrival.

| Coincidence / relation | value | target | verdict |
|---|---|---|---|
| **sum-vs-difference no-go**: `ω_beat/(2ω_nuc)` | `1.80×10⁻¹⁶` | `≥1` for a pump | **SETTLED-NEGATIVE (win)** — the kHz carrier beat is a *difference* frequency, 15.7 OOM too slow to parametrically pump (`Ω≈2ω_nuc`) or drive a MeV mode; the only tongue it hits (`n≈5.6×10¹⁵`) has vanishing width. Retires the "beat pumps the nucleus" reading **only**; leaves the conserved 23.847 MeV ledger, the Landau-Zener B=4 route, and any genuinely-slow (`ω_b≈ω_slow`) route intact. Computed in `rhythm_parametric_resonance_check.py` TEST 4 |
| **Duffing comb-drift falsifier**: `d(1.719)` per unit drive `μ` (shear `c=0.10`) | `+0.016` (→`1.736`) | — | **PRE-REGISTERED FALSIFIER** — an anharmonic (finite-amplitude) equilibrium makes the CK ratios `1.719/2.427` drive-amplitude-dependent, so the comb falsifier must be quoted **at the linear-amplitude limit**; a measured drift is a *prediction* (Duffing-pull), distinct from the Arnold-tongue plateau-lock. Computed in `duffing_backbone_check.py` TEST 4. Not a coincidence — a sharpened falsifier |
| **2:1 octave ↔ chirality-doublet** `ℤ₂↔ℤ₂` | `ℤ₂` both sides | — | **GENERIC `[flag-weak]`** — the antiparticle involution `λ→−λ` (chirality `=sign λ`, `C=−λ`) is a `ℤ₂`, and the EGM `ω(e)/ω(p)=2` octave carries a `ℤ₂` doubling; the "match" is a shared `ℤ₂` label. **`ℤ₂` is the most generic group** (an involution is everywhere), so this carries near-zero information — logged for completeness, essentially retired on arrival, never promoted |

## Cross-scale audit additions — the "genuinely-slow route" resolved (computed 2026-09-14)

The 8-scale audit (`cross_scale_slow_scale_audit_check.py`) that resolves the third cross-scale carve-out
("a genuinely-slow nuclear-adjacent route"). Every candidate slow scale computed vs the 87.14 kHz beat and
logged. Net: **the LITERAL "kHz = MeV gap" identity is a settled-negative; the only kHz-scale things are the
beat itself (tautological) or field-tunable/generic environmental splittings.** 87 kHz is a macroscopic scale.

| Relation | value | target | verdict |
|---|---|---|---|
| LITERAL identity `E_beat` vs d+d `Q` | 0.360 neV vs 23.847 MeV (ratio `1.5×10⁻¹⁷`, `−16.82` dex) | equal (for a literal kHz=MeV identity) | **SETTLED-NEGATIVE (win)** — dead by 16.8 OOM; no nuclear-internal scale reaches kHz (all +7.5..+17.6 OOM). TEST 2 |
| object-Alfvén beat "MATCHES-kHz" | `f_b=v_A\|Δλ\|/2πR` = 87.0 kHz (0 OOM) | the 87.14 kHz beat | **RESTATEMENT / TAUTOLOGICAL** — the beat matching the beat carries ZERO information (macroscopic scale). GUARD: never quote as evidence FOR a cross-scale identity — it is the definition. TEST 3 |
| far-miss band (nuclear / lattice / plasma / LZ-sweep) | `+7.5 to +17.6` OOM ABOVE | 87.14 kHz | **SETTLED-NEGATIVE (far-miss)** — level spacing +15.3..+15.9, LZ sweep +16.9, plasma +8.65, phonon +7.5..+8.7; even 1 keV is +12.4 OOM. TEST 1 |
| D₂/H₂ molecular hyperfine straddle | 8 / 57.7 / 113.9 / 225 kHz | 87.14 kHz beat | **GENERIC** — the un-fusable H₂ control (p–p spin-spin 57.7 kHz=0.66×, proton spin-rotation 113.9 kHz=1.31×) straddles the beat as tightly as D₂ ⇒ a control hits it ⇒ not a signal. TEST 5 |
| deuteron Larmor = `f_beat` | 87.14 kHz at `B=133.3 G` (proton control at 20.5 G) | 87.14 kHz | **TUNABLE-COINCIDENCE** — field-tunable (a control nucleus also lands), AND connects only to the REACTANT; ⁴He `I=0` ⇒ no nuclear Zeeman ⇒ bridge empty even before tunability. TEST 5 |
| macroscopic kHz genericity band | `v_A∈[10⁴,10⁵], R∈[0.05,0.12]` → `f_b∈[4.3×10⁴, 1.0×10⁶] Hz` | 87.14 kHz | **GENERIC (macroscopic)** — kHz ORDER is generic to any lab-scale collective/MHD object; ties the object-beat and the Klimov half-beat (43.57 kHz, same class). 87 kHz sits at the macroscopic-collective, not nuclear, scale. TEST 4/7 |

**What survives (not a coincidence — the honest positive):** the Landau-Zener normal form as the correct
*description* of the B=4 branching (`[credited]` formula / `[S]` d+d identification / open rate, **kHz-free**),
and the macroscopic beat as a slow **rate-gate** (`[S]`, falsifiable — a beat-locked yield step surviving an
H₂ control). Neither transfers a number from kHz to MeV; the pump reading is a doubly-closed settled-negative.

## Beat-ladder prior-art non-match (computed 2026-09-14)

The novelty audit's one computable finding (`beat_ladder_nonmatch_check.py`): does the ONE published
beat-sweep excess-heat dataset already show — or already refute — FTGB's geometric yield-step ladder
`f_b(L)=N^L`?

| Relation | value | target | verdict |
|---|---|---|---|
| Hagelstein-Letts-Cravens 2010 THz steps vs the `f_b(L)=N^L` ladder | 8.2/15.1/20.8 THz (consecutive ratios 1.84, 1.38 — differ ~34%) | a geometric ladder (equal consecutive ratios) | **NON-MATCH (logged)** — the reported steps are not geometric for **any** base N, so the sole existing beat-sweep dataset neither confirms nor duplicates the FTGB ladder. The signature-CLASS ("sweep a beat, find a locked yield step") is credited prior art (HLC 2010, JCMNS 3, 59); the exact geometric `N^L` form stays a GENUINELY UNTESTED falsifier. Neither a hit nor a refutation — a clue on the record. |

## What the log teaches (the clues)

- **The two genuinely-close, mechanism-free coincidences to keep watching:** `6π⁵ ≈ m_p/m_e` (0.0019%) and
  `1/(20φ⁴) ≈ 1/α` (0.034%). Both are logged as `[flag]` — *close enough to record as a clue, not close
  enough (and with no derivation) to promote.* If a mechanism ever forces the `6` (or `20`) from the
  object's structure, they graduate; until then they are coincidences, on the record.
- **The "derivations" that dissolve on computation:** EGM `r_p` (back-fit `n_Ω`), `H₀` (circular in
  `H₀`), the 2:1 harmonic (definitional), `α` via `e^(-2/3)` (dead). Computing them **forward** is what
  exposes the back-fit — exactly why the discipline excises them, now *shown* rather than asserted.
- **The genuine closed forms** (`c_CK=1/2j₀,₁`, `π²/3=ζ′(−2)-ratio`) are **not** coincidences — they
  follow from a theorem, and the log keeps them cleanly separated from the flags.

## Why this is a core function

Every flag in the jewel now has a **computed number and a logged verdict**, reproducibly. This (a) stops
coincidences being silently dismissed *or* silently promoted, (b) keeps the near-misses as a searchable
record of clues, and (c) makes the excision decisions auditable. New coincidences get **computed and
appended here**, never hand-waved. *No number promoted; the genuinely-close ones are flagged and kept,
the derivations that back-fit are named, the closed forms are separated. ASCII apart from math symbols.*

## Appended 2026-09-14 (jewel audit -- the forgotten-batch sweep)

| Coincidence | value | target | dev | verdict |
|---|---|---|---|---|
| `omega_EVO` vs `2*pi*f_1` (121 kHz) | `7.603e5 rad/s` | `omega_EVO` (unvendored) | quoted 0.035% | **PROVENANCE-INCOMPLETE** `[flag]` -- the `2*pi*f_1` arithmetic is trivial; the *comparison target* `omega_EVO` (the macroscopic EVO whirl rate the synthesis matches against) has no vendored source in the repo, so the claimed 0.035% match cannot be recomputed. `[V]` stripped in `FTGB_GRAND_SYNTHESIS.md` D.1.4 pending a source; kept as a flag, not promoted. |
| gate x density-proxy vs the rho_eff target band | `1/9 x [0.55,0.96] = [0.061,0.107]` | `0.06-0.08` | overlapping | **CONSISTENCY** `[flag]` -- three independently-sourced pieces (textbook singlet statistics; the StageD density proxy; the LZ target band) meet at one decade (`spin_channel_gate_check.py` TEST 4, 2026-09-15). Wide bands, proxy has named omissions, the target band's provenance itself flagged -- logged as a clue, NOT a derivation of Delta. |
| `T_shed`-class near-misses (soft-cascade time vs beat period) | -- | -- | -- | **NOT LOGGED as a match** -- rates at different energy scales are different kinds of number (the coherence-volume lesson); no cross-scale identity is claimed. |
