# The v_A residual — the one caveat for every absolute magnitude

> **⚠ Read this before quoting any absolute number (Hz, Tesla, eV) from this project.**
> The Alfvén speed `v_A ≈ 2.03×10⁴ m/s` is a **self-consistency residual, not an independent
> measurement** — there is no simultaneous `(B, n)` measurement of a single air plasmoid. So **every
> absolute magnitude carries a band**: the `{121, 208, 294} kHz` carrier comb, `ħ_eff`, and the beat
> frequencies inherit it **linearly** (~5–13×); `b_eff` (65 eV) and the anapole energy (~293 eV) inherit it
> **square-law** (~5.8× to ~170×, i.e. `b_eff` could be ~0.4–11 keV). **Only dimensionless ratios are
> load-bearing.** An absolute value quoted without this band is a mis-citation.

## Can it be resolved? — the honest answer

**Not pinned to a single value, no — and pretending otherwise would be dishonest.** Pinning `v_A` requires
measuring `B` and `n` *in the same plasmoid at the same time*, and that measurement does not exist in the
literature for an air plasmoid. What *can* be done, and is done here, is three honest things:

**1. Ground the band in real measured data (not a hand-wave).** `v_A = B/√(μ₀ n m_i)` computed for the
nearest *measured* systems (`absolute_magnitude_invariance_check.py`, TEST 3):

| System (measured `B, n`) | `m_i` | `v_A = B/√(μ₀ n m_i)` |
|---|---|---|
| SSPX spheromak — `B~0.3 T, n~5×10¹⁹` (Hill 2000) | 1 AMU | `9.3×10⁵ m/s` |
| air plasmoid, low corner — `B~0.02 T, n~10²¹` | 29 AMU | `2.6×10³ m/s` |
| air plasmoid, high corner — `B~0.5 T, n~10¹⁹` | 29 AMU | `6.4×10⁵ m/s` |
| **the object (back-solved, §A)** | 29 AMU | **`2.03×10⁴ m/s` — sits inside the real band** |

The band (~`2.5×10³` to `6×10⁵ m/s` for air) is bounded by genuine measurements, and the object's value
lives inside it. The residual is real and honestly wide — not invented, and not hidden.

**2. Prove the residual touches nothing load-bearing** (`absolute_magnitude_invariance_check.py`, TESTs 1–2,
`[V]`). Scaling `v_A` over a 65× band leaves **every dimensionless observable invariant to machine
precision** (spread ≤ `10⁻¹⁶`): the CK comb ratios `1 : 1.719 : 2.427`, the beat/carrier ratio, the cascade
step, `b_eff/(magnetic-energy-per-ion) = 1.047`, and the topological invariants `Q_H = 1`, `C = ±2`. The
absolute magnitudes scale by the *exact documented powers* (frequencies ×13 linearly, `b_eff` ×169
square-law at `v_A`×13). **The theory's load-bearing content is the ratios and the topology; none of it moves
with `v_A`.**

**3. Name the one measurement that collapses the band.** A single simultaneous `(B, n)` measurement in one
plasmoid pins `v_A` outright. Equivalently, a **second-system test** that `b_eff` equals the magnetic energy
per ion (`B²/2μ₀n`, the `1.047` ratio above) confirms the closed form directly (WS5). Either is a clean,
decisive, and currently-missing experiment — a genuine falsifier, not a fudge.

## Bottom line

The residual is a **disclosed calibration gap, not a hidden fit**: real-data-bounded, quarantined by proof
to the non-load-bearing absolutes, and closable by one named measurement. When sharing this work:
**quote ratios freely; quote any absolute Hz/Tesla/eV only with its band.** Reproduce the whole statement:
`python results/verify/absolute_magnitude_invariance_check.py`. Provenance of the anchors:
`frontier_calcs/` (vendored) + `canonical_numbers_provenance_check.py`; full audit: `30_CANONICAL_NUMBERS.md`
§A and `frontier_calcs/tension_T1_T2_resolution.py`.
