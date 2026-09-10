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
| plasma-OAM order `N` vs the triad | 3 | 3 (CK lines, 3-6-9) | exact | **STRUCTURAL** `[clue]` — Stage 0 (`oam_stage0_pointgroup_check.py`) computes the plasma Beltrami point group = a 3-fold body-diagonal `C₃` (no `C₄`), so the EM-carried OAM ladders by `N=3`, coinciding with the native triad. Honest caveat: a 3-fold body diagonal is a generic feature of the `A=B=C` ABC field, so the match may be structural, not deep — logged as a clue, not promoted |

**Genericity gate (why `137` is not "special").** Sweeping `k·φ^a·π^b` (small integers, `k∈{½…6,20}`)
lands **0 hits within 0.5%** of `137.036` — the *same* as random control targets (0–1 hits). A number the
object's own constants cannot cleanly reach is, by this test, **generic**: the near-misses are what you
expect by chance, not a signal. (Full control-target denominator in `alpha_genericity_check.py`.)

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
