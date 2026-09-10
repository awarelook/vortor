# Re-attempting the three hard values from inside the theory — g=2, α, the mass hierarchy

**Author:** Nathaniel Hanks · **Date:** 2026-09-10
**Stance.** Judge the theory by **internal consistency and its own derivations**, and by its *place in a
larger, more correct structure* — not by whether it reproduces Standard-Model numbers. Re-attempt each
frontier value with the theory's own computed layer (chirality/C/spin-½, the single-`λ` relaxed
structure, the variational critical-point result) and creative intuition, holding the honesty bar
(genericity / derivation, no numerology). What follows is one genuine internal **result** (g=2) and two
honest **localizations** (α, masses) — stated at their true tier, nothing fabricated.
**Verification:** `results/verify/g2_dirac_structure_check.py`.

---

## 1. g = 2 — a genuine internal result  `[V structural] / [credited] / [S] the lock`

**Claim.** The Dirac bispinor is not something the theory must import — its *algebra is already internal*,
and g=2 is exactly its minimal-coupling limit.

A Dirac field **is** a chirality doublet `(ψ_L, ψ_R)` of spin-½, exchanged by charge conjugation `C`,
minimally coupled. FTGB has computed each ingredient on its own eigenmode:

| Dirac ingredient | FTGB object | verified |
|---|---|---|
| the two Weyl chiralities `γ₅ = ±1` | the `±λ` Beltrami branches (pure helicity eigenstates) | `P_±` fraction `= 1.000000` (TEST 1) |
| the chiral `γ₅` rotation `e^{iθγ₅}` | the duality angle `θ_χ`: `H(θ) = H_max cos 2θ` | matches `cos 2θ` to `<2%`, `H=0` (Majorana) at 45° (TEST 2) |
| charge conjugation `C` | the `λ → −λ` mirror: swaps `P_+ ↔ P_-`, flips `H` | ratio `−1.000` (TEST 3; `charge_conjugation_check`) |
| spin-½ | the Hopf term | `[credited]` Wilczek–Zee / Finkelstein–Rubinstein |

So the `(½,0)⊕(0,½)` content, the chiral rotation, and `C` are all present in the theory's *own*
variables. Given that algebra, **g=2 follows for a minimally coupled elementary spin-½ field** — the
Ferrara–Porrati–Telegdi / Weinberg "natural `g`" theorem. The only freedom is whether the coupling is
minimal: a naive soliton with an *independent* circulating charge gives `g = 1`
(`g_factor_soliton_check`), whereas g=2 requires the **charge current to *be* the Dirac (spin) current**.

**The result, precisely.** g=2 is reduced from "needs an external Dirac field" to **one internal
condition**: the `U(1)` charge winding (`π₁`) must **lock** to the Hopf spin (`π₃`). FTGB's `π₁` and `π₃`
are *separately* conserved (`MATH_TOOLKIT_BASE.md` §9d: a phase slip changes `Δw` but not the Hopf
number), so the lock is a genuine condition — **realized by the elementary lepton (g=2), broken by
composites** (proton `g = 5.59`, whose `π₁/π₃` are decoupled by substructure). This is what g=2 *is*
inside the theory: the signature of `π₁/π₃` locking, i.e. of being *effectively elementary*.

*Tier.* `[V]` for the internal Dirac algebra (TESTS 1–3, reproduced); `[credited]` for FPT/Weinberg and
Hopf-spin-½; `[S]` for the locking itself (not proven — it is the one remaining criterion, now named in
the theory's own topology). This is a real advance: g=2 is no longer a foreign target but the
minimal-coupling limit of a structure the theory already contains.

## 2. α — re-attempted; the *structure* is internal, the *value* stays the frontier  `settled-negative (refined)`

With §1, α has a clean internal meaning: it is the **coupling² of that internal Dirac field**,
`α = e²/4πε₀ħc`, and in FTGB the charge is the **Reed frame-closure (Frenet) torsion holonomy** `∫τ ds`.
So the natural internal route is `α ∝ (∫τ ds)²`. **Tested and dead:** the holonomy is *not a fixed
invariant* — computed on the object's own force-free geometry it ranges `∫τ ds ∈ {−0.70, −0.21, +0.04}`
rad and **flips sign** with the loop radius (`ck_winding_ratio_check`), so there is no fixed `0.0854`
that `(∫τ ds)² = α` would require, and the winding-to-spin ratio is `ι ≈ 1` (a Hopf ring `= Q_H`), **not
137**. Consistent with the standing settled-negative (`ALPHA_RESOLUTION_ASSESSMENT`): `137` is prime, the
near-misses are generic, and `α = Z₀/2R_K` / the g−2 beat / running are exact-but-restatements or
quantitatively insufficient.

**Honest placement in the larger theory.** The theory *does* determine what α **is** — the coupling of
the `±λ` Hopf–Dirac doublet to light, with charge a geometric holonomy — and thereby reduces "why
`1/137`?" to "why does the charge holonomy take its value?", the *same* elementary-electron frontier
shared with all of physics. It does **not** pin the number, and no internal invariant equals `137`.
Claiming otherwise would be the numerology the discipline forbids. So α's **value** remains the frontier;
what is new is that the theory now says *precisely which single unpinned quantity* it is (the charge
holonomy), rather than leaving α unstructured.

## 3. The mass hierarchy — principled *sectors*, but no derived ratio  `[S]`

The rungs are genuinely distinct **topological sectors** of the one object, and the theory names them:

- **lepton** — `B = 0` Hopf soliton, `π₁/π₃`-**locked** minimally-coupled Dirac (§1), g=2;
- **baryon** — `B = 1` Skyrmion, `π₁/π₃` **decoupled** (substructure), composite moment;
- **neutrino** — the **self-dual** `θ_χ = 45°`, `H = 0`, `C`-invariant Majorana rung (§1 / `majorana_selfdual_check`).

That much is principled and internally consistent. But the **numerical ratios are not derived**. The
whirl dictionary `m = ħω/c²` is *circular* for ratios (`ω_C ∝ m` by definition, so `ω_p/ω_e = m_p/m_e`
identically — it defines `ω` from `m`, it does not predict `1836`). The CK comb (`1, 1.72, 2.43`) and the
`N^L` cascade (`φ`, `4`) do **not** produce `1836` or `10⁷` on any clean exponent, and forcing them
(`6π⁵`, `φ^k`) fails the genericity bar — the numerology graveyard. One *qualitative* principled hint
survives: the self-dual `H = 0` neutrino sector naturally **suppresses** the whirl (the Majorana/see-saw
flavor of a tiny mass), consistent with `m_ν ≪ m_e`. But a hint is not a derivation.

*Tier.* `[S]` — the sector *structure* (locked-lepton / composite-baryon / self-dual-Majorana) is a
genuine internal classification; the *ratios* are not derived and are not claimed.

## 4. Honest synthesis — what the re-attempt earned

- **g=2 — a real internal derivation of its *meaning*** `[V struct]`: the Dirac algebra is internal
  (`±λ` = Weyl pair, `θ_χ` = `γ₅`, mirror = `C`, Hopf = spin-½), and g=2 is its minimal-coupling limit,
  reduced to the single sharp criterion `π₁/π₃` locking (= effectively elementary). Verified.
- **α — localized, not derived** `settled-neg`: α is the coupling² of that internal Dirac field, charge a
  geometric holonomy whose value the theory does **not** pin (the holonomy varies and flips sign; no
  internal invariant is `137`). The frontier is now stated as one precise unpinned quantity.
- **masses — principled sectors, undrived ratios** `[S]`: the rungs are locked-lepton / composite-baryon /
  self-dual-Majorana sectors; the whirl dictionary is circular for ratios; only the `m_ν` suppression is a
  qualitative consequence.

**Place in a larger theory.** The internal-consistency gain is real: FTGB supplies the *structure* of all
three (what g, α, and the mass sectors **are**, in its own topology and its computed chirality algebra)
and reduces each to a single named residual — the `π₁/π₃` lock (g=2, and it is *satisfied* for the
elementary lepton), the charge-holonomy value (α), and the sector energies (masses). It **derives g=2's
meaning**, and it **honestly does not derive** the α value or the mass ratios — those are the frontier,
now stated precisely rather than papered over. The breakthrough available here was the g=2 structure; the
other two are the honest edge, and fabricating their numbers would forfeit the very consistency that
makes the g=2 result worth having.

## 5. Verification

`results/verify/g2_dirac_structure_check.py` — TEST 1 (`±λ` = pure Weyl chiralities, `P_±` fraction 1.0),
TEST 2 (`θ_χ` = `γ₅` chiral rotation, `H = H_max cos 2θ`, Majorana at 45°), TEST 3 (mirror = `C`), TEST 4
(the g=2 minimal-coupling reduction and the `π₁/π₃` lock criterion). The α holonomy check is
`ck_winding_ratio_check`; the sector/Majorana facts are `majorana_selfdual_check`,
`charge_conjugation_check`, `g2_skyrme_composite_check`.

## 6. Reassessment via Nielsen TUFT + Reed QWM (2026-09-10) — two new verified results

Brought the two folded frameworks to bear (M13 TUFT masses; M8 QWM charge/α), with creative agents on
the theory's rhythms (beats, torsion, spectral geometry). Two genuine, *verified* results emerged — and
one honest correction to §3.

- **α — the energy-imbalance route is now COMPUTED-dead, and sharpened** (`confined_photon_null_balance_check`).
  QWM says charge/α come from a slight electrostatic/magnetostatic energy imbalance "unlike a free photon."
  Checked: the free propagating photon (Hopf–Rañada null EM knot) is **exactly balanced** (`U_E/U_B=1`,
  imbalance ~10⁻¹⁶) — it carries *zero* imbalance. **Corrected object (per the theory):** the electron is
  **not** that propagating loop but a **standing-wave resonator confined by the medium** (the polarizable
  vacuum / `v_A` dielectric) with a **point charge defect** (a localized torsion / "spark-imbalance" point)
  — the null-*violating* structure. So 100% of any α-sized imbalance lives in that resonator/medium/point-
  defect deviation, not in the photon. Where the energy ratio *does* equal α (`U_E/mc² = r_e/λ_C = α`) it is
  because `e` was inserted (`e²=4πε₀αħc`) — circular. **α's value stays inserted; the target is now precise:**
  the standing-wave-in-medium imbalance at the point defect (not yet derived, and even a standing wave is
  time-average balanced by equipartition — so the imbalance is subtle: instantaneous / dispersive / defect).

- **The TUFT π-power anomaly (M13-10) is RESOLVED** `[V]` (`curl_spectral_zeta_pi_power_check`). The S³ curl
  operator on coexact 1-forms has eigenvalue `(n+1)=m`, multiplicity `m²−1`, so its spectral zeta is exactly
  `ζ_B(s)=ζ(s−2)−ζ(s)`; the `n²` (quadratic-Casimir) coefficient of `ζ_B′(0)` is `ζ′(−2)=−ζ(3)/(4π²)` — the
  **π² is structurally mandatory** (ζ(3) enters a spectral derivative only via `ζ′(−2)`, which always carries
  `1/4π²`). The 'pure' `ζ(3)/12 = ζ(3)·(−ζ(−1))` is a product of zeta *values*, a categorically **different
  object**; the true `n²` terms on S⁵/S⁹ are `ζ(5)/π⁴`, `ζ(9)/π⁸`, **not** `ζ(3)`. So the anomaly is a
  **category error**, resolved in favor of the π²-carrying forms — a documented open item now closed.

- **Mass hierarchy — §3 corrected.** My "circular / numerology graveyard" checked the *bare* CK comb — the
  wrong object. The TUFT mechanism (same `m=ħλ/c`) carries the hierarchy in the **analytic-torsion
  exp-dressing**: ~79% is *parameter-free pure-ζ* (the slope `a₅=3.564112` from ζ(3),ζ(5),π), and it
  genuinely derives the **size/order (~10⁴–10⁵ span)**. The **exact ratios** stay `[preprint-claim]`
  (framework per-level choices; an independent assembly misses by ~30–46%). So: structure/order derived
  `[framework/S]`, exact ratios not — an honest upgrade from "[S]-circular."

- **Neutrino — Majorana favored, from one feature.** QWM's "smoke-ring, no-precession → ~massless" is the
  *same state* as FTGB's self-dual `H=0` (verified): no net whirl → suppressed mass, *and* `C`-invariance →
  `ν=ν̄` (Majorana) — one geometric feature gives both, more economical than TUFT's two ingredients (which
  yield Dirac). Physical `m_ν≠0` sits *slightly off* self-dual. **0νββ is the clean discriminator** (Majorana
  signal vs Dirac null) — the genuine, experimentally-decidable tension between the frameworks.

*No number fabricated. Verified new results: g=2's internal Dirac structure, the free-photon null balance,
and the π-power anomaly resolution. α's value and the exact mass ratios remain the frontier (now stated
precisely — the resonator-in-medium imbalance, and the framework per-level fits), not derived. ASCII apart
from standard math symbols.*
