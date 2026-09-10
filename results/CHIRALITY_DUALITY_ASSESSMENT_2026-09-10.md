# Chirality, the duality angle, and torsion — what works in the math (by test, not by acceptance)

**Date:** 2026-09-10 · **Method rule (per instruction):** judge each claim by a **math/physics test**
(exact identity, computed quantity, or genericity), **never** by whether a community accepts it. "Not
accepted" is not an argument; "fails a genericity/derivation test" is. Everything below is computed —
`results/verify/chirality_helicity_check.py`.

---

## 1. Chirality = sign of the Beltrami λ = sign of helicity  — `[credited]`, an exact identity

For a force-free (Beltrami) field `curl u = λ u`, the helicity is
`H = ∫ u·(curl u) dV = λ ∫|u|² dV`, so **`sign(H) = sign(λ)` exactly**. Computed on the ABC field:

- `curl(ABC) = +1.0000·u` (Beltrami residual `1e-15`), `H = +3.0000 = λ⟨|u|²⟩` → right-handed.
- The parity **mirror** gives `curl u = −1.0000·u`, `H = −3.0000` → left-handed.

The `±λ` fields are mirror images — **the two chiralities**. This is not numerology and not a reading; it
is the geometry of force-free fields (Moffatt helicity). It is the theory's cleanest `[credited]` structural
fact, and it sits at coherence-map **layer 3**.

## 2. Antiparticle = the −λ partner — `[S]`, computed

FTGB reads **antiparticle = opposite chirality = the `−λ` mirror** — the left-handed partner of the same
object. Charge conjugation / parity flips `λ → −λ` and hence `H → −H`. This is a `[S]` structural reading
(the geometry gives the `±λ` pair; identifying `−λ` with the *antiparticle* is the FTGB step), and it is the
half-there content in `electron.html` made explicit and reproducible. It is falsifiable in principle: any
process that distinguishes the object's antiparticle from its `−λ` mirror would break it.

## 2b. The chirality flip **is** charge conjugation C — computed

Does flipping the chirality drag the *charge* with it? Tested on the same fields
(`results/verify/charge_conjugation_check.py`) by how three quantities behave under the mirror `λ → −λ`:

| under the mirror (λ → −λ) | quantity | behavior |
|---|---|---|
| **mass** | energy `E = ⟨\|u\|²⟩` (parity-even) | `+3.000 → +3.000` — **unchanged** |
| **chirality** | helicity `H = ⟨u·curl u⟩` (parity-odd) | `+3.000 → −3.000` — **flips** |
| **charge/precession** | Reed frame-closure torsion holonomy `∫τ ds` | `−96.73 → +96.73` (ratio **−1.000**) — **flips** |

So the mirror **keeps the mass but reverses chirality *and* the Reed torsion-defect/precession sign together**
— which is exactly **charge conjugation C** (same mass, opposite charge/handedness). The chirality `sign(λ)`
*drags* the charge/precession sign: **chirality → C, tied concretely** `[S, computed]`. This makes "antiparticle
= opposite chirality" and "antiparticle = opposite charge" the *same* statement for this object, not two
separate assertions — and it uses Reed's torsion as the frame-closure holonomy it is (§4), not as anything else.

## 3. The duality angle — now tied to a computed quantity, not analogy

Previously flagged `[framework]/analogy "until tied to something computed."` It is now tied: define the
**chiral mixing angle** `θ_χ = atan(‖u₋‖/‖u₊‖)` from the field's helicity content (`‖u±‖²` = energy in the
`h±` helical modes). Computed:

| field | `‖u₊‖²` | `‖u₋‖²` | `θ_χ` |
|---|---|---|---|
| pure `+λ` (electron end) | 1.0 | 0 | **0°** |
| pure `−λ` (positron end) | 0 | 1.0 | **90°** |
| mix `0.8(+) + 0.6(−)` | 0.64 | 0.36 | **36.9°** (`=atan 0.75`) |

So the "duality/yin–yang angle" is the **helicity-content mixing angle** of one field, with electron/positron
as its `0°`/`90°` endpoints — a computed quantity `[V-def]`, no longer imagery. (What it is *not*: a
derivation of the electroweak mixing angle — that would need the field's coupling, not just its helicity.)

## 4. Reed's torsion — a frame-closure holonomy, **NOT** Einstein–Cartan (correction)

Kept distinct, explicitly. Reed's "charge/chirality = torsion loop-closure defect" is a **frame-closure
holonomy** — the anholonomy of frame transport around the whirl loop, i.e. the **Frenet torsion holonomy**
`∫τ ds` computed in `ck_winding_ratio_check.py` (`~O(0.1 rad)`, varies, flips sign across flux surfaces). It
is **not** Einstein–Cartan *spacetime* torsion (the `torsion = spin-density source` of ECSK gravity) — a
different mathematical object in a different theory. An earlier note offered an EC bridge; that is withdrawn.
The honest status: Reed's torsion is a real, computed geometric-phase quantity of the field; Reed's *specific*
value `dθ = 2πα` is inserted (the computed CK holonomy is `O(0.1)`, not `2π/137 = 0.046`), so the *concept*
(torsion defect ↔ chirality/charge) is geometric and real, the *α-value* is not derived.

## 5. The scale hierarchy `ω_C/ω_p` — a feature to explain, marked high; not a derivation

The object carries a large internal-to-medium frequency ratio (Compton whirl `ω_C` vs a medium/plasma
frequency `ω_p`) — a genuine **scale hierarchy**, and a real feature worth explaining (like any hierarchy
problem), **not** to be dismissed. The discipline point is purely mathematical: a large ratio can only
*derive* a target (137, a mass, the CC) if it **beats the genericity denominator** — and it does not.
`alpha_genericity_check.py` shows near-misses to `137.036` from the object's constants are as dense as at
unrelated control targets. So: **mark the hierarchy as a feature/open question `[flag: feature]`; forbid using
it as a derivation** — on the math (genericity), not on anyone's approval.

## 6. What works vs what doesn't — the honest ledger, by test

- **WORKS `[credited]`:** chirality = `sign(λ)` = `sign(H)` (exact identity, §1).
- **WORKS `[S]`/`[V-def]`:** antiparticle = `−λ` mirror (§2); the chirality flip **is** charge conjugation C
  — mass fixed, chirality and the Reed torsion-defect flip together (§2b); duality angle = `θ_χ` (§3, computed).
- **REAL but distinct `[credited concept]`:** Reed torsion = frame-closure holonomy, `O(0.1 rad)` (§4) — not EC.
- **FEATURE `[flag]`:** the `ω_C/ω_p` hierarchy (§5) — explain, don't derive-from.
- **FAILS a math test:** α from winding / large-number ratios — beaten by the genericity denominator
  (`alpha_genericity_check.py`), and the winding-to-spin ratio is computed `ι ≈ 1` (`ck_winding_ratio_check.py`),
  not 137. This is a *result*, not a verdict of taste.

*Provenance: `results/verify/chirality_helicity_check.py` (§1–3), `ck_winding_ratio_check.py` (§4),
`alpha_genericity_check.py` (§5–6); coherence-map layer 3; `electron.html`. No value promoted; the discipline
is applied as mathematics, not as deference to consensus.*
