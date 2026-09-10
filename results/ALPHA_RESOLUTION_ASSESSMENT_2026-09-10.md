# α resolution assessment — can "winding = 1/α" be made parameter-free?

**Date:** 2026-09-10 · **Tier:** `[S]`/`[flag]` throughout; nothing promoted; `e^(-2/3)` stays excised.
**Question (from the state-vs-ambition review):** α is the load-bearing pillar — if "whirl count = 1/α"
can't be made parameter-free, the matter-wave layer never rises above `[S]`. This assesses the resolution
in principle across the theory's own layers — **ratio, EM, magnetic winding, EM torsion, vacuum/medium,
resonator, flux / Navier–Stokes** — and says honestly which routes are principled, which are numerology,
and where the real obstruction sits.

Grounded in `results/verify/alpha_running.py` (direction) and `results/verify/alpha_scale_headroom_check.py`
(magnitude), both reproducible.

---

## 1. The honest relocation: the gap is a SKELETON error, not a dynamical one

The current reframe (α's 2.3% miss as a *dynamical running / IR-fixed-point*) is **quantitatively dead for
this gap**, for two independent reasons now both computed:

- **Direction** (`alpha_running.py`): standard QED *screens* — `α⁻¹` decreases from its IR ceiling
  `137.036` as energy rises; `140.2` sits *above* the ceiling, so no standard scale reaches it. Closing the
  gap needs *anti-screening* (paramagnetic / non-Abelian sign).
- **Magnitude** (`alpha_scale_headroom_check.py`): even granting the anti-screening sign, the running has
  **zero headroom at the electron's own scale** (`α⁻¹(m_e) = 137.036` exactly — no charged particles below
  `m_e` to polarize the vacuum), and covering 2.3% at a QED-strength β needs **~6 decades** of running, while
  the object's *natural* EM window (`λ_C / r_e = 1/α`, ~2.1 decades) supplies only **0.76% — ~3× too short**.

So the 2.3% cannot come from dynamics at the electron scale. Decompose honestly:

> `1/α = 137.036 = [137: integer topological skeleton] + [0.036: a 0.026% fraction]`

The winding gives **140.2 → the whole error is in the integer skeleton (140 vs 137, 2.3%)**. The `0.036`
fraction is where a tiny vacuum/geometric correction legitimately lives; the skeleton error is ~90× larger
than that fraction and ∞× larger than the sub-`m_e` running (which is zero). **Resolution therefore means
making the winding integer come out 137, not 140, from the self-consistent geometry — not running it there.**

## 2. Route-by-route — principled vs numerology, and the obstruction in each

| Route (your list) | What α would be | Principled? | Obstruction / verdict |
|---|---|---|---|
| **ratio** | a dimensionless ratio of two energies/actions of the object | yes, but empty alone | α *is* a ratio (Coulomb/quantum energy); naming it a ratio restates, doesn't derive. Needs an independent invariant fixing the ratio to 137. |
| **EM** | `α = r_e/λ_C` (classical radius / Compton) | **circular** | `r_e ≡ α λ_C` *by definition* — the EM-self-energy ratio *is* α tautologically. No derivation without an independent scale law. |
| **magnetic winding** | a linking / rotational-transform / Hopf self-linking integer | **most principled skeleton** | a genuine integer topological invariant of the Beltrami–Hopf field — but generic Hopf linking is 1, not 137; must identify *why* the electron's self-linking is 137, from force-free closure, **without tuning the aspect ratio**. |
| **EM torsion** (Reed `dθ=2πα`) | `α = (anholonomy defect of the transport)/2π` | **cleanest calculation** | a well-defined geometric (Berry) phase of parallel transport around the whirl loop — no free knobs once geometry is fixed. But generic anholonomy is O(1); needs a *nearly-closed* transport with a `1/137` slip. No guarantee it lands there. |
| **vacuum / medium (`K_PV`)** | a dielectric renormalization of a bare coupling | right home for `0.036`, **not the skeleton** | §1: wrong direction + ~3× too short at the natural scale. A QCD-like *paramagnetic* magnetic vacuum is the correct *idea* for the tiny fraction, useless for 2.3%. |
| **resonator / mode-count** | a mode number `n_Ω` or eigenfrequency ratio | **tuned / circular** | the CK ladder gives O(1) roots, not 137; a mode-count hitting 137 requires tuning the free closure `n_Ω` (flagged in M11-6/M11-7). A 1-D count between `λ_C` and `r_e` gives `1/α` — but that is `r_e/λ_C=α` again. |
| **flux / Navier–Stokes (two-fluid)** | a ratio of quantized magnetic flux to mechanical circulation | **novel, worth computing** | the R3 canonical vorticity `Ω = B + d_i ω` literally couples magnetic flux (`h/e`) and mechanical circulation (`h/m`); the ratio of its two terms at the electron scale carries `e`. A candidate for α that ties it to machinery *already in the jewel* (R3). Uncomputed. |

**Reading the table.** Four routes collapse on inspection: **EM** and **resonator** are circular (they restate
`r_e/λ_C = α`); **ratio** is empty without an invariant; **vacuum/medium** is the wrong magnitude and direction
for the skeleton (though it is the correct, tiny home for the `0.036`). Three are genuinely open and principled:
**magnetic winding** (a topological integer), **EM torsion** (a geometric-phase defect), and **flux/two-fluid**
(a canonical-vorticity ratio). These are the only routes that could, in principle, make α parameter-free.

## 3. The one concrete, cheap falsification test available now

The current `q_geom = 140.2` uses **aspect ratio `A = 9.0`** — but that `A` is itself a *flagged, tuned* input
from the α exercise, and it **contradicts the theory's own core geometry** (`ε = 1/φ`, i.e. `A ≈ 1.618`, from the
cabled-nesting result; the FreeFEM solve gives `ε ≈ 0.697`). The winding is `A`-dependent, so the honest test is:

> Compute the Beltrami–Hopf **rotational transform / self-linking at the theory's OWN self-consistent aspect
> ratio** (`A = φ` or the force-free-closure value), with `A` **not** free. Whatever integer it yields is the
> parameter-free prediction. If it is 137 → the winding pillar is vindicated. If it is 140, or 3, or anything
> else → the winding picture is **falsified**, honestly, and "winding = 1/α" drops to analogy.

This needs the actual `q_geom(A, λ)` winding formula (it lives in the extended-corpus excision notes, not the
jewel) — a small, reproducible calculation, no HPC. It is the single highest-value α step: it either resolves
the skeleton or kills the claim, and it removes the tuned `A = 9` that the experimental confrontation already
flagged (`results/EXPERIMENTAL_CONFRONTATION_2026-09-10.md` §7).

## 4. The resolution program (what parameter-free α would actually require)

1. **Fix the electron's geometry with no free knob** — aspect ratio from force-free closure + a quantization
   condition (the theory's own `ε = 1/φ`, or a Beltrami self-linking quantization), *not* `A = 9`.
2. **Compute the topological winding integer** (rotational transform / Hopf self-linking) at that geometry →
   it must be **137** (an integer), by one of {magnetic winding, EM-torsion holonomy}.
3. **Account for `0.036`** as the small geometric/vacuum correction (here the `K_PV` paramagnetic-vacuum idea
   is legitimate — it is a 0.026% effect, the right size).
4. **The flux/two-fluid route** (`Ω = B + d_i ω`) is the most novel cross-check: derive α from the ratio of the
   canonical vorticity's magnetic and mechanical parts, tying it to R3.

If steps 1–2 give 137 without tuning, α is resolved to the skeleton and the matter-wave layer can rise to
`[V-structure]`. If they do not, the honest outcome is that "winding ≈ 1/α" is a **suggestive analogy, not a
derivation**, and the layer stays `[S]` permanently — which the theory must be willing to accept.

## 5. Honest bottom line / risk

- **`137.036` is a measured IR coupling with a non-integer part**, not obviously a geometric integer. The
  history of "geometric 137" (Eddington `136→137`, Wyler) is a graveyard of numerology; the project's own
  anti-numerology bar (0.5% promotion gate, the genericity denominator, the `e^(-2/3)` excision) is the correct
  guard and it currently, correctly, keeps α at `[flag]` (139 and 140 are as "close" to `q_geom` as 137).
- **The reframe was aimed at the wrong target.** "Dynamical running" cannot supply a 2.3% *skeleton* error;
  the assessment relocates the whole problem to the **topological winding integer**, and identifies the three
  routes (magnetic winding, EM-torsion holonomy, flux/two-fluid) that could in principle deliver it.
- **The cheapest decisive move is §3**: recompute the winding at the theory's *own* aspect ratio, with `A` not
  free. It is a falsification test, not a fitting exercise — and it retires the tuned `A = 9`.
- **α may remain open.** That is an acceptable, honest outcome; it would fix the matter-wave layer at `[S]`
  without discrediting the `[V]` plasma core, the toolkit, or the falsifiable program.

*Provenance: `results/verify/alpha_running.py` (direction), `results/verify/alpha_scale_headroom_check.py`
(magnitude), `results/ALPHA_DYNAMICAL_REFRAME_2026-09-09.md`, `results/EXCISION_LEDGER.md` (the `e^(-2/3)`
excision), `results/EXPERIMENTAL_CONFRONTATION_2026-09-10.md` §7 (the `A=9` vs `A=φ` flag). No value promoted;
`e^(-2/3)` stays excised; every route carries its tier.*
