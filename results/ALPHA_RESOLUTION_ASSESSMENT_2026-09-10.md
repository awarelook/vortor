# α resolution assessment — is "winding = 1/α" derivable? (the test has been run: NO)

**Date:** 2026-09-10 · **Tier:** `[flag]`/**settled-negative**; nothing promoted; `e^(-2/3)` stays excised.
**Question (from the state-vs-ambition review):** α is the load-bearing pillar — if "whirl count = 1/α"
can't be made parameter-free, the matter-wave layer never rises above `[S]`.

> **Higher-level synthesis:** the frontier capstone
> [`OPEN_QUESTIONS_PRINCIPLED_RESOLUTION_2026-09-10`](OPEN_QUESTIONS_PRINCIPLED_RESOLUTION_2026-09-10.md) places
> this winding-derivation verdict alongside g=2 and R2 (and the multi-lens *typing* of α); read it for the whole
> frontier story, this doc for the depth behind the "NO."

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

## 3b. The continuous winding-to-spin ratio, computed directly — ι ≈ 1 (not 137)

The primality argument (§2–§3) refutes the *integer* invariants, but Reed's actual claim is the
*continuous* winding-to-spin ratio (rotational transform ι) and the loop-closure torsion holonomy —
non-integers the primality argument does not touch. So compute them directly from the l=1
Chandrasekhar–Kendall force-free field (`results/verify/ck_winding_ratio_check.py`, math-only field-line
tracing, no scipy):

- **Winding-to-spin ratio ι ≈ 1.05–1.11** (mean 1.08) across every flux surface — **≈ 1, not 137**
  (0.8% of 137; ~125× too small). The force-free electron is a **Hopf ring: one poloidal (whirl) turn per
  toroidal (orbital) circuit** — exactly the `Q_H = 1` the integer argument cited. The continuous and
  integer answers *agree*: the object's real winding is 1.
- **Loop-closure torsion holonomy** `∫τ ds ≈ −0.70 … +0.04` rad — O(0.1 rad), varies with flux surface and
  flips sign, **not** the fixed `2π/137 = 0.046` rad a torsion-defect-of-α would require.

So the continuous route is **computed-dead**, not merely asserted-dead — this closes the one gap the
primality argument left. To reach 137 you would need a 137-fold *nested/iterated* structure (not a single
CK eigenmode) or the tuned, theory-inconsistent `A = 9`.

## 3c. Reassessed — α as internal spin precession IS correctly-typed (g−2); the value stays open

An earlier draft called the internal route a "category error" (α a two-object coupling, not a one-object
count). That was too strong, and a sharper reading — pressing the *spin-precession* form of Reed's claim —
corrects it: the electron's **anomalous magnetic moment `a = (g−2)/2` is *exactly* an internal spin
precession**, generated by its coupling to the radiation field. The coupling *does* manifest internally, as a
precession. Grounded in `results/verify/g2_spin_precession_check.py`:

- **CONCEDED — α does live as an internal spin precession.** The anomalous precession per cyclotron orbit is
  `2π·a = α` rad (Schwinger leading `a = α/2π`, matching the measured `a_e` to 0.15%; the rest is higher QED
  loops). "Charge = spin precession, `dθ ∝ α` per cycle" (Reed) points at real, 12-digit-measured physics —
  **not** a category error.
- **BUT the anomaly gives 861, not 137.** The g−2 precession "resync" is `1/a = 2π/α ≈ 861`; Reed's whirl
  number `1/α = 137` is the **inverse coupling itself** (`= λ_C/r_e`, since `r_e = α λ_C`) — a *different*
  quantity that restates α by definition. The real internal-precession anomaly points at 861, not 137.
- **AND the value stays open.** `a = α/2π` is **α-proportional**: α is the *input* coupling, extracted from the
  measured anomaly via the QED loop coefficient `1/2π` — not derived. Soliton geometry can plausibly give the
  *leading* `g = 2` (the Reed photon-ring: charge circulating at `c` on the Compton ring gives `g=2`) `[S]`;
  the *anomaly*, and hence α's value, needs the quantized soliton⊗photon coupling loop.

**Net (reassessed):** the framing is **upgraded** — "α as internal spin precession" is correctly-typed and maps
onto real g−2 physics, a genuine gain over "category error." But the **value** of α is unchanged: it is the
coupling strength (the deep, shared, unsolved QED question), α-proportional in the anomaly, and `137 = 1/α`
restates it. FTGB's correctly-typed, honest program is to **derive `g = 2` from the soliton** `[S]`; α's
*value* stays `[flag]`. The winding-*count* route (§2–§3b) is separately settled-negative (`ι ≈ 1`).

## 3d. Attempted — does the soliton give g = 2? (offered as "winnable"; honestly it isn't)

§3c named "derive g = 2 from the soliton" as the correctly-typed forward step. Running it
(`results/verify/g_factor_soliton_check.py`) corrects that over-optimism:

- **The naive Reed photon-ring / circulating-charge picture gives `g = 1`, not 2** — robustly
  (R-, v-, model-independent): `μ = qvR/2` and `S = pR` share the same `q·v·R` scaling, so `μ/S = q/2M`
  and `g = 1`. Any classical soliton current with charge and mass co-distributed gives `g = 1`.
- **`g = 2` is the Dirac value** — it comes from minimal coupling of a *first-order spinor* (Dirac) field
  (the `(σ·p)²` structure), and the measured `g = 2.0023… = 2 + α/π + …` sits on top of it. A classical
  current loop does not reproduce the factor of 2; relativistic "hidden-momentum" treatments that argue for
  `g = 2` are model-dependent, not robust.
- **What the topology *does* deliver — spin-½ `[credited]`.** A Hopf soliton with a Hopf / Wess–Zumino term
  at `θ = π` is quantized as a **spin-½ fermion** (Wilczek–Zee 1983; Finkelstein–Rubinstein 1968). So FTGB can
  honestly carry "the object is a spin-½ fermion" from its Hopf topology — but **spin-½ ≠ g = 2**: a spin-½
  soliton/anyon can have `g ≠ 2`; the g-factor is a separate dynamical quantity fixed by the coupling.

**Verdict (updated 2026-09-10):** the naive soliton gives `g = 1`, and `g = 2` requires a minimally-coupled
Dirac structure. **That structure is now shown to be INTERNAL** (`g2_dirac_structure_check.py`,
`FRONTIER_INTERNAL_DERIVATION_2026-09-10.md` §1): the ±λ Beltrami branches are the two Weyl chiralities,
`θ_χ` is the `γ₅` chiral rotation, the mirror is `C`, and Hopf gives spin-½ — so **g=2's *meaning* is derived
internally** as the minimal-coupling limit, reduced to one criterion (the π₁/π₃ lock). ~~"g=2 stays [S]/open in
the same difficulty class as α"~~ is **superseded**: only the *lock itself* stays `[S]`, and it is *satisfied*
by the elementary lepton (broken by composites). α's *value* remains the frontier; g=2's *structure* does not.

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

- **α is SETTLED-OPEN — a well-posed NEGATIVE, not an untried "maybe."** The winding-*count* "1/α = 137" is an
  **asserted relabel / analogy**, not a computation: no invariant lands on 137.036 better than a generic
  near-miss; 137 is prime and the object's real levels are 1 and 2; the continuous winding-to-spin ratio is
  `ι ≈ 1` (§3b); and a static topological count is the wrong *type* for a running coupling. The *spin-precession*
  form is instead correctly-typed — it is the g−2 anomaly (§3c) — but there α is the *input* coupling, so the
  **value** stays open either way. This is the expected outcome for a famous open problem, reached with an
  anti-numerology control — a **success-criterion negative**, not a failed hunt.
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
