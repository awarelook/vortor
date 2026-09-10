# α resolution assessment — is "winding = 1/α" derivable? (the test has been run: NO)

**Date:** 2026-09-10 · **Tier:** `[flag]`/**settled-negative**; nothing promoted; `e^(-2/3)` stays excised.
**Question (from the state-vs-ambition review):** α is the load-bearing pillar — if "whirl count = 1/α"
can't be made parameter-free, the matter-wave layer never rises above `[S]`.

**Answer, corrected 2026-09-10:** the decisive test — *does a physics-selected winding/holonomy invariant
of the CK/Hopf object equal 137.036 without a tuned integer?* — **has already been run in the extended corpus,
more thoroughly than a single A-recompute, with a genericity control, and it returns a clean NEGATIVE.** An
earlier draft of this file proposed the test as still-open; that was wrong, and this version corrects it. The
running/scale analysis below (§1) still stands and complements the negative; the routes (§2) are annotated with
their actual results; the verdict (§4–5) is **settled-open**, not "open to try."

Grounded in: `results/verify/alpha_running.py` (direction), `results/verify/alpha_scale_headroom_check.py`
(magnitude), `results/verify/alpha_genericity_check.py` (the anti-numerology denominator, reproduced in-jewel),
and the extended-corpus `ALPHA_IR_FIXED_POINT_HOLONOMY_2026-09-08` / `_frontier_alpha_2026-09-08` (Derivation C).

---

## 1. The gap is a SKELETON error, not a dynamical one (still valid)

The "α as dynamical running" framing is quantitatively dead for this gap, two independent ways:

- **Direction** (`alpha_running.py`): QED *screens* — `α⁻¹` only decreases below its IR ceiling `137.036`;
  `140.2` sits *above* the ceiling, so no standard scale reaches it. Closing it needs exotic *anti-screening*.
- **Magnitude** (`alpha_scale_headroom_check.py`): zero running headroom at `m_e` (`α⁻¹(m_e)=137.036` exactly);
  covering 2.3% at QED-strength β needs **~6 decades**; the object's natural EM window supplies only 0.76%
  (~3× short).

So the 2.3% is not dynamics: `1/α = 137.036 = [137 integer skeleton] + [0.036 fraction]`, and the winding gives
140.2 — the whole error is in the **integer skeleton (140 vs 137)**. Resolution would mean the winding integer
coming out 137 from the geometry. §2–§3 test exactly that.

## 2. Route-by-route — with the actual test result on each

| Route | α would be | Result |
|---|---|---|
| **magnetic winding** | a linking / rotational-transform integer | **TESTED → NEGATIVE.** 137 is **prime**, so no nontrivial poloidal×toroidal winding `p·q` gives it at *any* aspect ratio; the object's real topological levels are **Hopf `Q_H=1`** and **Chern `C=±2`** — neither is 137. (`alpha_genericity_check.py` §2; HOLONOMY §2.) |
| **EM torsion** (Reed `dθ=2πα`) | `α = anholonomy/2π` (a Berry phase) | **TESTED → NEGATIVE.** The whirl/spin frequency ratio is `ω_C/ω_p ≈ 4.4×10⁹`, not 137; `dθ=2πα` has **α inserted by hand** — a relabel, not a holonomy computation. (Derivation C §3c; HOLONOMY §5 torque-harmonics.) |
| **ratio** | a dimensionless ratio of two invariants | **NEGATIVE by genericity.** ~5 sub-0.5% hits near 137.036 from the object's real constants — *comparable to control targets* (`alpha_genericity_check.py` §1; HOLONOMY §3: 18 vs 12). Any single hit is numerology. |
| **flux / Navier–Stokes (two-fluid)** | ratio of the canonical vorticity's `B` and `d_i ω` parts | **Not separately computed, but subsumed:** it is a ratio of the same plasma constants (frequencies ~`10⁹`, not 137) and falls under the genericity denominator. No reason to expect 137. |
| **vacuum / medium (`K_PV`)** | a dielectric renormalization | right home for the tiny `0.036`; **useless for the skeleton** (§1). And the flow has **no forced IR fixed point** — only the trivial Gaussian one; 137 is a threshold freeze-out (integration constant), not `β=0`. (HOLONOMY §1.) |
| **EM** (`α=r_e/λ_C`) / **resonator** | self-energy / mode ratios | **circular** — restate `r_e/λ_C = α`; the CK ladder gives O(1) roots, 137 only by tuning the free `n_Ω`. |

**Every route is negative or circular.** The two that looked most principled in the first draft — magnetic
winding and EM-torsion holonomy — are precisely the ones the corpus tested and refuted.

## 3. Why the "recompute at A = φ" move is moot

The first draft's headline test — "recompute the winding at the theory's own aspect ratio `A = φ` instead of the
flagged `A = 9`" — does **not** rescue it, for a reason independent of A: **137 is prime and the object's real
topological invariants are 1 and 2.** Changing A changes a continuous geometric factor; it cannot turn a
topological count of 1 or 2 into 137, and it cannot make a prime factor as a nontrivial `p·q` winding. The
genericity sweep already *includes* `ε = 1/φ` among the object's constants and finds nothing non-generic near
137. So the A=φ recompute would only add one more generic near-miss to a settled negative. (It was still right
to strip the tuned `A = 9` from the plasmoid-aspect row — see `EXPERIMENTAL_CONFRONTATION` §7 — but that is a
geometry-honesty fix, not a path to α.)

## 4. What would flip the negative to `[V]` — and why it is not expected

For "winding = 1/α" to become a derivation (per the corpus success-criteria), one would need **all** of:

1. **137 as an integer LEVEL the theory carries** (a genuine Chern–Simons level or linking the object
   possesses), reproduced in **≥2 independent routes** with **no post-hoc integer**. Present real levels are
   `C=±2`, `Q_H=1`; 137 is prime and absent.
2. A **derived bridge** explaining why a *static* topological count should equal the *q²→0 limit of a running
   renormalized coupling* (the category mismatch). None exists.
3. Either a **derived interacting IR fixed point** whose value is fixed by the object's topology with **zero
   free medium parameters** (currently any such FP value is a free ratio `a/c`), or an **RG limit cycle**
   (Efimov-like discrete scale invariance) that could single out a value (QED one-loop has none).

The corpus judges each "not expected from the current geometry," and the genericity denominator makes any
single numeric hit (e.g. Wyler `4π³+π²+π`, +2×10⁻⁴%) unpromotable — it is mechanism-free with three free
coefficients.

## 5. Honest bottom line

- **α is SETTLED-OPEN — a well-posed NEGATIVE, not an untried "maybe."** "Whirl count = 1/α" is an **asserted
  relabel / analogy**, not a computation: no invariant of the object lands on 137.036 better than a generic
  near-miss; 137 is prime and the object's real levels are 1 and 2; the whirl/spin ratio is ~10⁹; and it is a
  category error (topological count vs running coupling). This is the expected outcome for a famous open
  problem, reached cleanly with an anti-numerology control — a **success-criterion negative**, not a failed hunt.
- **Consequence for the theory:** the matter-wave layer's α-pillar stays `[flag]` — **permanently, absent a
  genuinely new mechanism** (§4). "α ≈ 137 as a winding number" survives only as a *suggestive analogy* (a
  layer of the coherence map, tier `[flag]`), never a load-bearing derivation.
- **What this does NOT touch:** the `[V]` plasma / topological-fluid core (the current-leg trilogy, R2/R3), the
  reproducible toolkit, and the falsifiable experimental program all stand independently of α. Honestly closing
  α as negative *strengthens* the jewel — it converts a tempting overclaim into a disciplined, cited, reproducible
  no.

*Provenance: `results/verify/{alpha_running, alpha_scale_headroom_check, alpha_genericity_check}.py`;
extended-corpus `ALPHA_IR_FIXED_POINT_HOLONOMY_2026-09-08.md`, `_frontier_alpha_2026-09-08.md` (Derivation C),
`COINCIDENCE_SWEEP_2026-09-08.md` (genericity methodology); `results/EXCISION_LEDGER.md` (`e^(-2/3)` excised),
`results/EXPERIMENTAL_CONFRONTATION_2026-09-10.md` §7 (the `A=9` vs `A=φ` flag). No value promoted.*
