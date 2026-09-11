# TOOLKIT ADV -- Module M10: TOPOLOGICAL-SOLITON + CONSERVED-CURRENT METHODS (canonical helicity, no-go template, moduli-geodesic, frequency-seesaw, RG-dielectric)

Part of the FTGB math toolkit (see `MATH_TOOLKIT_BASE.md`, `TOOLKIT_ADV_07_BUCKINGHAM_PI_2026-09-08.md`,
`TOOLKIT_ADV_08_QWM_MATH_CONVERSION_2026-09-08.md`, `TOOLKIT_ADV_09_COUPLED_OSCILLATOR_SUBSTRATE_2026-09-08.md`).
This module is a **METHODS-PRESERVATION pass**: it lifts the *reusable machinery* developed across the
2026-09 current-leg / Skyrme / neutrino / alpha sessions out of its one-off source docs and into a single,
tiered, cited place, so each method can be re-applied to a new problem without re-deriving it. It captures
**how to do a thing**, not a new claim. Every number quoted below is traced to the named source doc and its
reproducible script; nothing is fabricated.

> **SCOPE STATEMENT (read first).** These are **methods**, tiered by what they are licensed to deliver. Two
> of them (M10-1 canonical helicity, M10-3 moduli-geodesic) are **VALIDATED machinery** -- a proven Casimir
> and an exactly-lower-D-reproduced pipeline -- and are trustworthy at the stated precision. Three (M10-4
> frequency-seesaw, M10-5 RG-dielectric) are **reading/reduction** methods that reframe a problem in FTGB
> variables without solving it, and are tiered [A]/[S-mechanism] accordingly. **M10-3 carries a LOAD-BEARING
> usage warning (diagonal != off-diagonal; real relaxation required) -- stated in full in M10-3.0 before the
> method, because misusing it silently inflates a branching amplitude by orders of magnitude.** No nuclear
> rate, cross-section, branching magnitude, mass, or scale is invented here; `E_fm=2.5 MeV` stays retracted;
> baryon number is conserved throughout.

## Tier legend (honesty discipline)
- **[V]** verified in this project by a named computation / a checked identity or dimensional reduction.
- **[credited]** established physics/mathematics we build on (textbook or primary-source, cited).
- **[V-dim]** dimensionally verified (units close), value not derived.
- **[S]** structural / cited-convergence or numerically-supported, not closed on our side.
- **[S-mechanism]** the mechanism is well-posed (a category gap is dissolved), the value is NOT forced.
- **[A]** analytic / model-asserted or category-legitimate structural suggestion; not promotable as derived.
- **[VOCAB/framing]** shared morphology or organizing language only; no shared mechanism, no numbers cross.
- **[model / EXECUTED]** a genuine field integral / computation at MODEL precision (~10-30% + stated factor).
- **[flagged]** coincidence held, not promoted (`~137`).
- **[reject]** fabricated / refuted -- named so it is never resurrected.

**Primary FTGB source docs integrated (each with a reproducible ASCII script, traced per method).**
- `DRIVEN_CANONICAL_HELICITY_4CURRENT_2026-09-08` (+ `driven_canonical_aligned_2026-09-08.py`) -- M10-1, M10-2.
- `DRIVEN_NONALIGNED_CLOSURE_2026-09-08` (+ `driven_nonaligned_closure_2026-09-08.py`) -- M10-1, M10-2.
- `DRIVEN_PV_CONST_NOGO_PROOF_2026-09-08` (+ `..._VERIFY`, `driven_pv_const_nogo_2026-09-08.py`) -- M10-2.
- `CURRENTLEG_RESIDUAL_REDUCIBILITY_2026-09-08`, `CURRENTLEG_R1_CURRENTNULL_2026-09-08` -- M10-2.
- `SELF_UNIFIED_SKYRME_MULTIBODY_2026-09-08` (+ `..._DELTA_VERIFY`, `self_unified_skyrme_multibody_..py`) -- M10-3.
- `B4_MODULI_GEODESIC_EXECUTED_2026-09-08`, `B4_TWO_DIABATIC_RELAXATION_2026-09-08` -- M10-3 (the warning).
- `SEESAW_FTGB_DUALITY_BRIDGE_2026-09-08` (+ `seesaw_ftgb_duality_bridge.py`) -- M10-4.
- `ALPHA_KPV_RUNNING_BRIDGE_2026-09-08`, `ALPHA_IR_FIXED_POINT_HOLONOMY_2026-09-08` -- M10-5.

**Established literature cited (per method below):** Woltjer 1958; Steinhauer-Ishida 1997; Mahajan-Yoshida
1998; Bae-Kang-Shin 2025 (arXiv:2504.07629); Berger-Field 1984; Dombre et al. 1986; Manton 1982;
Battye-Sutcliffe 1997; Barnes-Baskerville-Turok 1997; Feist-Lau-Manton 2013; Dashen-Hasslacher-Neveu 1975;
Minkowski 1977 / Gell-Mann-Ramond-Slansky / Yanagida (type-I seesaw); Mohapatra-Senjanovic 1980; PDG 2024.

**In-repo verify —** `results/verify/octahedral_oam_ladder_check.py` `[V]` (the `Δl=4` OAM ladder =
credited B=4 Skyrmion spectrum, Braaten-Townsend-Carson `J=0→4`) and `results/verify/g2_skyrme_composite_check.py`
`[V]` (parameter-free `μ_p/μ_n=−3/2` via Skyrme collective quantization) — this module's B=4 / Skyrme
methods made computational. See also `topology_invariants_check.py` (`Q_H=1`, `C=±2`).

---

## M10-1 -- CANONICAL / GENERALIZED HELICITY conserved-current method   [V / credited]

**Statement.** A driven-dissipative ideal two-fluid (Yoshida-Mahajan double-Beltrami) object has its OWN
ideal conserved current -- the **canonical (generalized) helicity** -- even when the ordinary **magnetic**
helicity is NOT conserved (once `E.B != 0`). When you need a conserved topological charge for a driven,
non-force-free object, do NOT use magnetic helicity; use the canonical one. This is the "own conserved
current first" move: any driven-transport or closure construction should be built on the canonical current.

**Equations.** Per species `s` (charge `q_s`, mass `m_s`, flow `v_s`, inertial length `d_s = m_s/q_s`):

```
canonical momentum       P_s     = A + d_s v_s
generalized vorticity    Omega_s = curl P_s = B + d_s curl v_s
generalized helicity     H_s     = integral P_s . Omega_s dV        (a Casimir, dH_s/dt = 0 ideal)
helicity density         h       = P_s . Omega_s
canonical Ohm (ideal)    eps_s   = -d_t P_s - grad mu_s = -v_s x Omega_s
Bernoulli head (scalar)  mu_s    = phi + (m_s/2q_s)|v_s|^2 + enthalpy_s/q_s
```

The local conservation law and its flux (derived in the source):

```
d_t h + div[ mu_s Omega_s - (v_s x Omega_s) x P_s ] = -2 eps_s . Omega_s = 0
  =>  d_mu K^mu = 0 ,      K = h v_s + (mu_s - P_s.v_s) Omega_s
```

The current is divergence-free **because** `eps_s . Omega_s = -(v_s x Omega_s).Omega_s = 0` identically
(the canonical Ohm field is perpendicular to the generalized vorticity -- a Casimir/geometric fact). Contrast
the magnetic-helicity current, which is NOT conserved under drive:

```
d_mu K^mu_mag = -2 E.B  (!= 0 once driven)          [Berger-Field 1984]
```

**External drive extension** (from `DRIVEN_NONALIGNED_CLOSURE`): with an external body force `f_ext`, the
source becomes `d_mu K^mu = 2 f_ext . Omega`, so **conservation survives an external drive iff
`f_ext perp Omega`**. This one extra condition is the hinge of every driven-closure question.

**How to reuse.** (1) For any driven Beltrami/Hopf object, define `P_s, Omega_s, h` first; the canonical
helicity is the conserved charge to reason with. (2) The flux decomposition `K = h v + S Omega`,
`S := mu - P.v`, is the universal starting point for a medium<->matter closure test (M10-2). (3) The
`f_ext perp Omega` rule tells you exactly what an external drive must satisfy to preserve the invariant.
(4) The dimensional audit uses the M8 charge convention (`e ~ kg.rad/s`): `P ~ m/rad`, `Omega ~ 1/rad`,
`h = P.Omega ~ m/rad^2` = the magnetic-helicity-density dimension (identical to static `K0 = A.B`, D2 [V]).

**Validity / tier.** **[V] / [credited].** `dH_can/dt = 0` ideal is a proven Casimir (Bae-Kang-Shin 2025,
"On the double Beltrami states in Hall magnetohydrodynamics," arXiv:2504.07629, VERIFIED real and on-topic;
corroborates the canonical-helicity Casimir -- confirm exact Prop. label at lock; claim independently carried
by Steinhauer-Ishida + Mahajan-Yoshida; Steinhauer-Ishida 1997;
Mahajan-Yoshida 1998); the local
`d_mu K^mu = -2 eps.Omega = 0` is verified in-project (residuals `~1e-16` on genuine equilibria,
`driven_canonical_aligned_2026-09-08.py`). The `f_ext perp Omega` conservation condition is [V]
(`DRIVEN_NONALIGNED_CLOSURE` Sec.1).

**Source.** `DRIVEN_CANONICAL_HELICITY_4CURRENT_2026-09-08` (Secs.1-2); `DRIVEN_NONALIGNED_CLOSURE_2026-09-08`
(Sec.1). Cite Bae-Kang-Shin (2025) arXiv:2504.07629, "On the double Beltrami states in Hall
magnetohydrodynamics" (VERIFIED real; corroborates the Casimir -- confirm exact Prop. label at lock; claim
independently carried by Steinhauer-Ishida + Mahajan-Yoshida); Steinhauer-Ishida PRL 79, 3423 (1997);
Mahajan-Yoshida PRL 81, 4863 (1998); Woltjer PNAS 44, 489 (1958); Berger-Field JFM 147, 133 (1984).

---

## M10-2 -- NO-GO METHOD for magnitude-inhomogeneity obstructions (the `|B|=const` / `P.v=const` template)   [V]

**Statement.** A recurring, transferable proof pattern: a conserved-current or medium<->matter **closure
identity holds IFF some field magnitude is spatially constant**, which a topologically nontrivial
(nulled/knotted/Hopf) field provably cannot be. This is how three separate current-leg negatives were
proven; it is the standard tool for deciding whether a proposed closure is a theorem or a postulate.

**The template (four steps).**
1. **Reduce closure to a scalar constancy condition.** Write the matter 4-current as `(rho, rho v)` and the
   available conserved flux as `K = h v + S Omega`. Because `S` is a SCALAR, `S Omega = 0` forces `S = 0`
   pointwise (there is no "S perpendicular to Omega" vector branch -- a load-bearing subtlety, see below).
   Closure `<=>` a single scalar is constant:
   - static magnetic-helicity current: closes IFF `|B| = const`;
   - aligned-driven canonical current: closes IFF `P.v = const` (`|P| = const` in the aligned limit).
2. **Show the constancy is impossible for nontrivial topology.** Use the Beltrami identity
   `grad(|P|^2/2) = (P.grad)P` (since `curl P = lam P`): `|P| = const <=> (P.grad)P = 0 <=> straight field
   lines`, i.e. a laminar screw field with no nulls, no linking, zero Hopf index -- topologically trivial.
   Contrapositive: any field with nulls (required for Hopf/CK closed fibres) has spatially varying magnitude.
3. **The cross-term positivity obstruction (the two-mode crux).** For a two-mode double-Beltrami
   `P = p1 G+ + p2 G-`, constancy of `P.v` reduces to `p1^2 f+ = p2^2 f-` on the ABC self-fluctuations.
   Because `(A'B')(B'C')(A'C') = (A'B'C')^2 >= 0`, the three products cannot all carry the sign required --
   **positive-proportionality is algebraically impossible** unless both modes degenerate to single plane
   waves (trivial). This `(A'B'C')^2 >= 0` step is the reusable kill.
4. **Classify the residual obstruction set: measure-zero (benign) vs finite-volume (killer).** This is the
   decisive category test (`feedback_scale_invariant_assess_at_appropriate_scale`,
   `feedback_category_of_error_impossible_vs_misunderstood`):
   - **finite-volume obstruction = KILLER.** Static `|B|=const` fails *wherever `|B|` varies = everywhere*
     on a nontrivial object -> a genuine no-go.
   - **measure-zero obstruction = BENIGN.** The two-fluid current-null set `{v_e = v_i}` is 3 scalar
     equations in 3D = codim-3 isolated points (= the `B`-nulls, `J = lam B`), a thin set the object
     *crosses* without consequence: `E,B` stay bounded, the drive increment `dA ~ 1/r` is L1-integrable and
     `|dA|^2 ~ 1/r^2` is L2-integrable around isolated nulls, so no integral quantity sees the failure.
     Verdict: closure holds on the full-measure region; the null set is benign.

**Key results this template produced (all [V], traced).**
- Static: closes iff `|B|=const`; residual `0.605`, irreducible (`CURRENTLEG_RESIDUAL_REDUCIBILITY`).
- Aligned-driven: closes iff `P.v=const`; residual band `std(P.v)/mean ~ 0.46-0.66` on genuine equilibria;
  no-go proven [V] for single-mode, equal-`|lam|` opposite-helicity, and well-separated spheres; [S] in the
  close-same-sign-sphere project corner (floor `~0.58`) (`DRIVEN_PV_CONST_NOGO_PROOF` + `VERIFY`).
- Constant-`|P|` control closes EXACTLY (residual `~1e-16`) -- confirms the iff both directions.
- R1 current-null: GENUINE but BENIGN (measure-zero), so 3D realizability upgrades toward [V] on the
  current-full region (`CURRENTLEG_R1_CURRENTNULL`).

**The escape hatch this template also names.** The obstruction is a *pointwise* (steady/aligned) condition.
In the genuinely time-dependent, non-aligned regime the curl obstruction becomes an identity (VORT) and
vanishes: the closure surface is pointwise NON-EMPTY, realizable with a bounded drive satisfying `S=0` AND
`f_ext perp Omega`. That regime is **characterized-open, leaning conditional-theorem** -- DOF count 8/8
determined (not over-determined) once >=3 free drive functions are added -- with **sustained (all-time)
existence the single genuine open piece** (`DRIVEN_NONALIGNED_CLOSURE`). Use this to tell a real no-go from
a merely-un-demonstrated one.

**How to reuse.** Whenever a proposed conservation/closure "looks over-determined": (i) reduce it to a
scalar `S=0` via the `K = h v + S Omega` decomposition; (ii) test whether `S=0` forces a magnitude to be
constant; (iii) if so, apply steps 2-3 to show nontrivial topology forbids it; (iv) classify the failure set
as measure-zero (benign) or finite-volume (killer); (v) check whether time-dependence + a bounded
`f_ext perp Omega` drive reopens it. Note the scalar-vs-vector subtlety in step 1: presupposing a vector
"S perp Omega" branch is a category error -- `S` is a scalar.

**Validity / tier.** **[V]** for the template and the static/aligned no-gos; **[S]** in the project's
close-sphere corner; **characterized-open** for the driven non-aligned regime. The static [V] negative
stands untouched by every sequel.

**Source.** `CURRENTLEG_RESIDUAL_REDUCIBILITY_2026-09-08`; `DRIVEN_PV_CONST_NOGO_PROOF_2026-09-08` (+VERIFY);
`CURRENTLEG_R1_CURRENTNULL_2026-09-08`; `DRIVEN_NONALIGNED_CLOSURE_2026-09-08`. Cite Dombre et al. JFM 167,
353 (1986); Arnold-Khesin *Topological Methods in Hydrodynamics*; Bae-Kang-Shin (2025).

---

## M10-3 -- MODULI-GEODESIC transition-amplitude method   [S-model, sine-Gordon-VALIDATED]

### M10-3.0 -- CRITICAL USAGE WARNING (LOAD-BEARING -- read before using this method)

This method is genuinely validated, but it is **easy to misuse in two specific ways that inflate a result by
orders of magnitude.** Both are stated first, on purpose.

1. **DIAGONAL (mu, V) vibrational quantum != OFF-DIAGONAL Landau-Zener gap.** The `(mu, V)` small-oscillation
   quantum `hbar*omega = hbar c sqrt(k/mu)` is a **diagonal** curvature/inertia quantum of ONE surface. The
   branching amplitude `Delta` is the **off-diagonal** coupling between TWO diabatic surfaces at a crossing.
   **They differ by ORDERS OF MAGNITUDE.** Executed on the real B=4 merger coordinate, the diagonal quantum
   was `hbar*omega_merger = 66-95 MeV` (= the primary-source BBT `Eg` "cube -> two donuts" mode ~20 MeV),
   while the LZ target `Delta` is `~1.4-1.9 MeV` -- a `~20-50x` gap. **Sanity gate:** set `Delta :=
   hbar*omega_merger` in `S = exp(delta)`, `delta = pi Delta^2 / (2 hbar v |dF|)`; you get `log10 S ~ 9600`
   (the absurd "freeze-BOTH-channels" pathology), which POSITIVELY PROVES the diagonal quantum is not the
   gap. Always run this freeze-both sanity check; if `S` is nonsensical you have computed the wrong object.
2. **Executing it needs REAL relaxation (arrested Newton flow), NOT a reduced ansatz.** Every tractable
   shortcut fails in the crossing region -- precisely where the off-diagonal coupling lives:
   - **product ansatz** -> hits a repulsive core wall, keeps `B ~ 3.8` but never reaches the fused basin;
   - **naive field blend** -> breaks topology mid-path (`B -> 2.4`, spurious barrier);
   - **free coarse/massless arrested-Newton-flow relaxation** -> UNWINDS the topology (`|B| -> 0` in
     ~50-150 steps) at any coarse grid; robust integer winding needs `dx <= 0.10 fm` (~5% needs
     `dx <= 0.06 fm`), i.e. the standard Battye-Sutcliffe/Feist production setup (compiled/GPU, N>=~150).
   So the off-diagonal `Delta` is a **named, quantified, thesis-scale blocker**, not something the reduced
   pipeline can deliver. Do not dress a static energy ratio (e.g. `(well/E4)*Q ~ 1.3 MeV`) as a
   "moduli-geodesic Delta" -- that was the exact error `SELF_UNIFIED_DELTA_VERIFY` caught and
   `B4_MODULI_GEODESIC_EXECUTED` corrected.

**Bottom line:** this method is trustworthy for FORM, SCALING, and ORDER-OF-MAGNITUDE BANDS (with a factor
~2.2 coefficient ceiling), and is NOT trustworthy for precision coefficients or for the off-diagonal
branching gap without a full relaxed two-surface solve.

### M10-3.1 -- The method

**Statement.** Reduce a soliton reaction/bound-state to a low-dimensional collective coordinate `sigma`,
compute the moduli-space metric `mu(sigma)` (inertia) and potential `V(sigma)` as genuine field integrals,
then quantize the reduced system to get a transition amplitude / bound-state spectrum via the geodesic
(Manton) approximation and a Landau-Zener form.

**Equations.**

```
moduli metric      mu(sigma) = integral sum_a (d n_a / d sigma)^2 d^3x        (reduced inertia)
potential          V(sigma)  = E_soliton[field(sigma)] - E(sigma -> infty)
reduced dynamics   (1/2) mu(sigma) sigma-dot^2 + V(sigma) = -binding          (geodesic on (mu,V))
diagonal quantum   hbar*omega = hbar c sqrt(k / mu(sigma*)) ,  k = V''(sigma*)
LZ branching       S = exp(delta) ,  delta = pi Delta^2 / (2 hbar v |dF|)     (Delta = off-diagonal gap)
```

**Validation (the crux -- why it is trustworthy at its tier).** Run on 1+1 sine-Gordon, where exact answers
exist (`self_unified_skyrme_multibody_2026-09-08.py`):
- **kink mass** `M = 7.999989` vs exact `8` -> rel.err `1.4e-6` (exact reproduction);
- **kink-antikink force** decay rate `= meson mass` to `0.9%` (fitted `0.991` vs exact `1`), amplitude to ~6%;
- **breather** near-threshold energy-frequency SCALING LAW `binding ~ w^p`: moduli `p = 1.93` vs exact
  `p = 2.0` (correct functional form) -- with an **HONEST O(1) coefficient ceiling of factor ~2.2 near
  threshold** (`w_cc/w_exact ~ 2.20-2.22`), growing in the deep/relativistic regime. Cause: a single rigid
  collective coordinate omits the breather's internal width mode; adding a second coordinate is the known
  tightening route.

So the pipeline gets mass EXACTLY, force decay-rate EXACTLY, bound-state scaling exponent right, and the
bound-state coefficient only to a factor ~2 -- hence trustworthy for form/scaling/bands, not precision.

**How to reuse.** (1) Identify the collective coordinate and compute `mu(sigma)`, `V(sigma)` as REAL field
integrals -- never skip `mu` (the prior doc's error was labelling a static ratio as a geodesic result). (2)
Calibrate `mu(sigma -> infty)` to the physical reduced mass, `V` to a nucleon/energy anchor. (3) Report
outputs as a BAND with the factor-~2.2 method ceiling propagated two-sided (it points DOWN -- the method
OVERestimates the bound frequency). (4) For a branching amplitude, remember the M10-3.0 warning: the `(mu,V)`
quantum is diagonal; the off-diagonal `Delta` requires a relaxed two-diabatic-surface solve with continuum
matching. (5) Note the sector split: the moduli-geodesic method is native to the Skyrme/baryon sector
(`pi_3 S^3`); the lepton/EVO/neutrino sector (`pi_3 S^2`, Hopf/Beltrami) is a SPECTRAL (eigenvalue-difference)
computation, NOT moduli-geodesic -- one substrate, two topological sectors, two matched methods.

**Validity / tier.** **[S-model, sine-Gordon-VALIDATED]** -- trustworthy for FORM / SCALING /
order-of-magnitude bands with a factor-~2.2 coefficient ceiling; **[model / EXECUTED]** for genuine B=4
field integrals `mu(sigma), V(sigma), hbar*omega_merger` (~10-30% ansatz + factor ~2-3 Skyrme
over-stiffness); **[label / BLOCKED]** for the off-diagonal reactive `Delta` (named thesis-scale blocker,
NOT delivered). `[reject]`: any fabricated `Delta`/rate/branching magnitude; `E_fm=2.5 MeV`.

**Source.** `SELF_UNIFIED_SKYRME_MULTIBODY_2026-09-08` (Part 2 validation ladder); `B4_MODULI_GEODESIC_EXECUTED_2026-09-08`
(diagonal executed + the warning); `B4_TWO_DIABATIC_RELAXATION_2026-09-08` (the relaxation blocker,
dx-convergence of the O(4) baryon monitor). Cite Manton, *Phys. Lett. B* 110, 54 (1982) (geodesic
approximation); Manton-Sutcliffe *Topological Solitons* (CUP 2004) Ch.4,9-10; Battye-Sutcliffe PRL 79, 363
(1997); Barnes-Baskerville-Turok PRL 79, 367 (1997); Feist-Lau-Manton PRD 87, 085034 (2013);
Dashen-Hasslacher-Neveu PRD 11, 3424 (1975); Landau (1932) / Zener PRSA 137, 696 (1932).

---

## M10-4 -- SEESAW FREQUENCY-DOWNCONVERSION reading   [A / V-dim]

**Statement.** Under the calibrated mass<->frequency map `m = hbar*omega/c^2`, the type-I seesaw maps
term-by-term into frequency space and reads as a **parametric-beat downconversion**: a heavy whirl frequency
divides the square of a Dirac-coupling whirl down to a light whirl. This is the class of operation the M9
coupled-oscillator substrate already carries (Stuart-Landau + Adler/Kuramoto locking + beat law), so it is a
legitimate FTGB-native re-reading -- but it RESTATES, does not resolve, the neutrino-mass terminus.

**Equations.**

```
type-I seesaw   m_light ~ m_D^2 / M_R              [Minkowski 1977; GRS; Yanagida]
frequency read  omega_light ~ omega_D^2 / omega_R  (via m = hbar*omega/c^2)
dimensional     (hbar omega_D/c^2)^2 / (hbar omega_R/c^2) = hbar (omega_D^2/omega_R)/c^2 = a mass  [V-dim]
```

**What is [V-dim] (the calibration confirm).** The whirl ladder is a genuine, correctly-calibrated
mass<->frequency map (`seesaw_ftgb_duality_bridge.py`): the `nu` rung `omega = 7.6e13 rad/s` gives
`m = hbar*omega/c^2 = 0.05002 eV`, matching the atmospheric scale `sqrt(|Dm2_31|) ~ 0.05 eV` to **0.04%**;
e/p/d rungs reproduce their known masses to `<= 0.3%`. So the ladder is calibrated and the `nu` rung sits
where a 0.05 eV neutrino should.

**What is NEGATIVE (the honest limit).** Scanning all ordered ladder pairs, the ONLY on-ladder solution of
`omega_D^2/omega_R ~ omega_nu` is the **trivial no-op** `omega_D = omega_R = omega_nu` (`M_R = m_D`, no
seesaw gain). A genuine downconversion needs an **off-ladder** heavy scale (e.g. `omega_R = omega_e^2/omega_nu
~ 7.9e27 rad/s`, ~2800x the top rung) -- the external Majorana/LNV sector, exactly as the terminus states.

**How to reuse.** Use `m = hbar*omega/c^2` to move ANY mass relation into frequency space and check whether
FTGB's own whirl ladder can supply the needed levels. The pattern generalizes: if the required denominator
level lands OFF the ladder, the mapping *locates and names* an external ingredient rather than deriving it.
Companion mappings in the source (all held at their honest tier, do not over-promote): Majorana =
chargeless smoke-ring self-duality **[A]** (category match; self-duality asserted-not-shown; `0nubetabeta`
is the external falsifier); driven-heartbeat small parameter as inverse-seesaw `mu` **[A speculative]** (the
heartbeat is not shown to violate lepton number -- load-bearing caveat); LENR "frequency desert" as
seesaw-SHAPED suppression **[VOCAB/framing]** (shared morphology only; the direct nu-in-LENR channel STAYS
the known NULL, MSW `~10^-27`).

**Validity / tier.** **[A]** for the duality reading, **[V-dim]** for the ladder calibration confirm,
**NEGATIVE** for on-ladder closure. Claims the seesaw is a frequency-downconversion and the ladder is
calibrated; does NOT claim FTGB derives `m_nu` or contains the heavy scale.

**Source.** `SEESAW_FTGB_DUALITY_BRIDGE_2026-09-08` (Mapping 1). Cite Minkowski *Phys. Lett. B* 67, 421
(1977); Gell-Mann-Ramond-Slansky (1979); Yanagida (1979); Mohapatra-Senjanovic PRL 44, 912 (1980) (inverse
seesaw); Majorana *Nuovo Cimento* 14, 171 (1937); PDG 2024 (neutrino-mixing review); NuFIT 5.2 (2022).

---

## M10-5 -- RG DIELECTRIC-FLOW / IR-FIXED-POINT method   [S-mechanism / flagged]

**Statement.** Read a running coupling as a scale-dependent polarizable-medium dielectric, so that
"running-coupling" and "static-winding" are the SAME object at two scales (the category gap between "alpha
RUNS" and "the object gives a STATIC count" dissolves). The static/long-wavelength invariant is then
identified with the **IR (q^2 -> 0) endpoint**. This WELL-POSES the mechanism but does NOT force the value --
QED running supplies only the slope, and the IR value is the RG integration constant.

**Equations.**

```
dielectric map   K_PV(q^2) := alpha(0) / alpha(q^2) = 1 - Delta_alpha(q^2) ,   K_PV(0) = 1
one-loop run     alpha(Q^2) = alpha(0) / (1 - sum_l (alpha(0)/3pi)[ln(Q^2/m_l^2) - 5/3])
slope            d(1/alpha)/d ln Q^2 = -(alpha(0)/3pi) per lepton   (proportional to alpha => cannot source it)
beta function    beta_alpha = (2/3pi) alpha^2 * sum_f Q_f^2  -> only root is alpha* = 0 (Gaussian FP)
```

**What is established (the real win).** The coupling GROWS toward the UV (`137.036 -> ~132.7` leptonic at
M_Z), so **137.036 is the INFRARED endpoint** -- correct conceptually, since a *static* object is what you
see at zero momentum transfer / infinite wavelength. The running <-> polarizable-dielectric duality is exact
and textbook.

**What is NOT forced (the honest core).** The IR value is the integration constant of the flow: shifting the
IR boundary condition by hand just translates the whole curve (100 -> 95.7, 137.036 -> 132.73, 200 -> 195.7
at M_Z). The beta function has NO nontrivial fixed point (only Gaussian; physical `beta = 1.13e-5 != 0` is a
threshold freeze-out, not `beta = 0`). Any hypothetical interacting FP value `eps* = a/c` is a free medium
ratio = tuning. So the bridge REDUCES the problem (category gap -> "does the object's IR holonomy invariant
equal `1/alpha(0)`?") but does not solve it.

**Genericity-denominator anti-numerology control (reusable discipline).** Before promoting ANY near-miss to
a constant, enumerate a fixed family of simple invariants over the object's real constants and count hits
near the target vs a displaced control target -- if comparable, the near-miss is generic numerology:
- `ALPHA_KPV_RUNNING_BRIDGE`: near-misses at 137.036 are ordinary (`17/11200` vs `8/11200` control).
- `ALPHA_IR_FIXED_POINT_HOLONOMY`: `21,168`-combo family, at 0.5% tol `18` hits @ 137.036 vs `12` @ control
  (comparable); at 0.05% tol `4` vs `6` (control has MORE) -- 137 is not anomalously hard.
- 137 is PRIME (Hopf linking `Q_H = p*q` factors only {1,137}); the object's real levels are Chern `C = +-2`
  and Hopf `Q_H = 1`, neither of which is 137. The "integer level + running dressing" split is NOT clean.

Use the denominator (control-target count within the same tolerance) as the gate: promote only if the target
is anomalously dense relative to control.

**How to reuse.** (1) To bridge a "runs vs static" category mismatch, cast the running coupling as
`K_PV(q^2) = alpha(0)/alpha(q^2)` and pin the static invariant to the IR endpoint. (2) Do not expect the
running to source a value -- it fixes only the slope. (3) Apply the genericity-denominator control to any
proposed numerical coincidence before promotion. What would flip [S]->[V]: an IR fixed point of the object's
own dielectric flow whose q^2->0 holonomy/winding invariant equals `1/alpha(0)` ab-initio, zero tuned
integer, in >=2 independent routes.

**Validity / tier.** **[S-mechanism]** (category gap dissolved, mechanism well-posed) / **[flagged]** (value
NOT forced; `~137` stays flagged, `20*phi^4` and Wyler forms stay GENERIC). The IR-fixed-point closure test
returned a **clean, well-posed NEGATIVE** (a success-criterion negative for a famous open problem).

**Source.** `ALPHA_KPV_RUNNING_BRIDGE_2026-09-08`; `ALPHA_IR_FIXED_POINT_HOLONOMY_2026-09-08`. Cite standard
QED one-loop vacuum polarization; CODATA-2022 `alpha(0)^-1 = 137.035999206`; PDG 2024. Consistent with
`TOOLKIT_ADV_08` (`dtheta = 2pi*alpha`, `q = 1/alpha`, charge = torsion defect, `~137` [flagged]) and
`MATH_TOOLKIT_BASE` (`K_PV` polarizable vacuum). Coincidence register item 11.

---

## M10-6 -- THE METHODS TABLE (core output)

| # | Method | What it delivers | Tier | Source doc(s) | Literature |
|---|---|---|---|---|---|
| M10-1 | Canonical/generalized helicity conserved current `d_mu K^mu=0`; `f_ext perp Omega` rule | a driven object's OWN ideal invariant (Casimir) when magnetic helicity dissipates | **[V]/[credited]** | DRIVEN_CANONICAL_HELICITY_4CURRENT; DRIVEN_NONALIGNED_CLOSURE | Bae-Kang-Shin 2025; Steinhauer-Ishida 97; Mahajan-Yoshida 98; Berger-Field 84 |
| M10-2 | No-go template: closure iff a magnitude is const; `(A'B'C')^2>=0` obstruction; measure-zero vs finite-volume | decides theorem-vs-postulate for a closure; classifies the obstruction set | **[V]** (static/aligned); [S] project corner; char-open (driven) | CURRENTLEG_RESIDUAL_REDUCIBILITY; DRIVEN_PV_CONST_NOGO_PROOF+VERIFY; CURRENTLEG_R1_CURRENTNULL; DRIVEN_NONALIGNED_CLOSURE | Dombre 86; Arnold-Khesin |
| M10-3 | Moduli-geodesic `(mu, V)` -> quantum / LZ amplitude; sine-Gordon-VALIDATED | FORM/SCALING/bands (factor ~2.2 ceiling); diagonal quantum executed | **[S-model VALIDATED]**; [model EXECUTED]; [label/BLOCKED] off-diagonal | SELF_UNIFIED_SKYRME_MULTIBODY; B4_MODULI_GEODESIC_EXECUTED; B4_TWO_DIABATIC_RELAXATION | Manton 82; Battye-Sutcliffe 97; BBT 97; Feist-Lau-Manton 13; DHN 75 |
| M10-4 | Seesaw as frequency downconversion `omega_l ~ omega_D^2/omega_R` via `m=hbar*omega/c^2` | reframes mass relation; locates external ingredient (off-ladder scale) | **[A]** reading / **[V-dim]** calibration / NEG on-ladder | SEESAW_FTGB_DUALITY_BRIDGE | Minkowski 77; GRS; Yanagida; Mohapatra-Senjanovic 80; PDG 2024 |
| M10-5 | RG dielectric flow `K_PV(q^2)=alpha(0)/alpha(q^2)`; IR endpoint; genericity denominator | dissolves runs-vs-static category gap; anti-numerology control | **[S-mechanism]** / **[flagged]** value | ALPHA_KPV_RUNNING_BRIDGE; ALPHA_IR_FIXED_POINT_HOLONOMY | QED vac.pol. (textbook); CODATA-2022; PDG 2024 |

**Classification.**
- **VALIDATED machinery (trust at stated precision):** M10-1 (proven Casimir), M10-3 (exact lower-D
  reproduction with a named ceiling).
- **PROOF template (reusable, [V]):** M10-2.
- **Reading / reduction methods (reframe, do not solve):** M10-4 ([A]/[V-dim]), M10-5 ([S-mechanism]).

---

## M10-7 -- LIMITS (stated prominently)   [V]

This module does **NOT**:
1. **claim any current-leg closure** -- M10-1 supplies the object's conserved current; M10-2 shows the
   matter-current closure remains a POSTULATE (static [V] no-go untouched; driven non-aligned characterized-open,
   sustained existence the open piece);
2. **deliver the off-diagonal branching gap `Delta`** -- M10-3's `(mu,V)` quantum is DIAGONAL (tens of MeV, =
   BBT); the off-diagonal `Delta ~1.4-1.9 MeV` is a named, quantified, thesis-scale BLOCKER (needs a relaxed
   two-diabatic-surface solve at `dx<=0.06-0.10 fm`); the freeze-both sanity gate PROVES the diagonal is not
   the gap;
3. **derive any neutrino mass** -- M10-4 confirms only the ladder CALIBRATION (`nu` rung 0.05 eV, 0.04%) and
   locates the required OFF-ladder external Majorana/LNV scale; the nu-in-LENR channel stays NULL;
4. **force alpha** -- M10-5 dissolves the category gap and pins 137 to the IR, but the value is the RG
   integration constant; `~137` stays [flagged]; the genericity denominator shows near-misses are generic;
5. **assert any nuclear rate, cross-section, branching magnitude, mass, or scale** -- none is fabricated;
   `E_fm=2.5 MeV` stays retracted; baryon number is conserved.

**The one load-bearing warning, restated:** in M10-3, the DIAGONAL `(mu,V)` vibrational quantum is NOT the
OFF-DIAGONAL Landau-Zener branching gap (they differ by orders); executing the method for a branching
amplitude requires REAL 3D relaxation (arrested Newton flow at production resolution), not a reduced product
/ blend / coarse-massless ansatz (each fails in the crossing region: core-wall / topology-break / unwind to
B=0). Always run the `S = exp(delta)` freeze-both sanity check.

---

## Per-claim index (M10)
| # | Claim | Tier | Repro / trace |
|---|---|---|---|
| M10-1 | Canonical helicity `d_mu K^mu=0` ideal even when `d_mu K^mu_mag=-2E.B`; `f_ext perp Omega` conserves it | [V]/[credited] | `eps.Omega=0` Casimir; residual ~1e-16; Bae-Kang-Shin arXiv:2504.07629 VERIFIED real (confirm Prop. label at lock; carried by Steinhauer-Ishida + Mahajan-Yoshida) |
| M10-2 | Closure-iff-magnitude-const no-go template; `(A'B'C')^2>=0`; measure-zero vs finite-volume | [V] (+[S] corner) | static 0.605; `P.v` band 0.46-0.66; const-`|P|` closes ~1e-16; R1 codim-3 benign |
| M10-3 | Moduli-geodesic `(mu,V)` VALIDATED (kink 1.4e-6, force 0.99, breather p=1.93 vs 2.0, ceiling ~2.2) | [S-model VALIDATED] | `self_unified_skyrme_multibody_..py`; diagonal 66-95 MeV = BBT |
| M10-3-warn | Diagonal quantum != off-diagonal `Delta`; needs real relaxation; freeze-both gate | [V]/[label BLOCKED] | `log10 S ~ 9600`; product/blend/coarse all fail; `dx<=0.06-0.10 fm` |
| M10-4 | Seesaw = frequency downconversion; ladder calibrated (0.04%); genuine seesaw needs off-ladder scale | [A]/[V-dim]/NEG | `seesaw_ftgb_duality_bridge.py`; nu rung 0.05002 eV; only trivial on-ladder |
| M10-5 | RG dielectric `K_PV=alpha(0)/alpha(q^2)`; 137=IR endpoint; no forcing FP; genericity control | [S-mechanism]/[flagged] | `alpha_kpv_running.py`, `alpha_ir_fixed_point.py`; 18 vs 12 @0.5% |
| M10-7 | Limits + the load-bearing moduli warning | [V] | statement of scope |

## Verification coverage (M10)
- **Proven/verified in-project (traced):** canonical helicity Casimir + local `d_mu K^mu=0` (residual ~1e-16,
  `driven_canonical_aligned_..py`); static `|B|=const` [V] no-go (residual 0.605); aligned `P.v=const` [V]
  no-go (band 0.46-0.66; const-`|P|` control ~1e-16; `driven_pv_const_nogo_..py`); R1 current-null measure-zero
  benign (codim-3, `dA` L1/`|dA|^2` L2 integrable); sine-Gordon validation (kink 1.4e-6, force 0.9%, breather
  p=1.93 vs 2.0, ceiling ~2.2, `self_unified_skyrme_multibody_..py`); B4 diagonal `hbar*omega_merger=66-95 MeV`
  = BBT `Eg` ~20 MeV, freeze-both `log10 S~9600` (`b4_moduli_geodesic_executed_..py`); O(4) baryon-monitor
  dx-convergence (`b4_two_diabatic_relaxation_..py`); ladder calibration nu=0.05002 eV @0.04%, e/p/d <=0.3%
  (`seesaw_ftgb_duality_bridge.py`); alpha IR endpoint + genericity denominators (`alpha_kpv_running.py`,
  `alpha_ir_fixed_point.py`).
- **Numbers traced, not invented:** every value above quotes its source doc + script. No nuclear rate,
  cross-section, branching magnitude, mass, or scale is fabricated; `E_fm=2.5 MeV` retracted; baryon conserved.

**Citations.** Woltjer PNAS 44, 489 (1958); Steinhauer-Ishida PRL 79, 3423 (1997); Mahajan-Yoshida PRL 81,
4863 (1998); Yoshida-Mahajan PRL 88, 095001 (2002); Bae, Kang & Shin, "On the double Beltrami states in Hall magnetohydrodynamics" (2025) arXiv:2504.07629; Berger-Field
JFM 147, 133 (1984); Dombre et al. JFM 167, 353 (1986); Arnold-Khesin, *Topological Methods in
Hydrodynamics*; Skyrme *Nucl. Phys.* 31, 556 (1962); Manton *Phys. Lett. B* 110, 54 (1982); Manton-Sutcliffe,
*Topological Solitons* (CUP 2004); Battye-Sutcliffe PRL 79, 363 (1997); Barnes-Baskerville-Turok PRL 79, 367
(1997); Feist-Lau-Manton PRD 87, 085034 (2013); Dashen-Hasslacher-Neveu PRD 11, 3424 (1975); Landau (1932) /
Zener PRSA 137, 696 (1932); Minkowski *Phys. Lett. B* 67, 421 (1977); Gell-Mann-Ramond-Slansky (1979);
Yanagida (1979); Mohapatra-Senjanovic PRL 44, 912 (1980); Majorana *Nuovo Cimento* 14, 171 (1937); PDG 2024;
CODATA-2022 (`alpha(0)^-1 = 137.035999206`).

Cross-links: `MATH_TOOLKIT_BASE.md` (K_PV polarizable vacuum, topology sec.9), `TOOLKIT_ADV_08_QWM_MATH_CONVERSION`
(D2/D4 units, `m=hbar*omega/c^2`, `~137` flagged), `TOOLKIT_ADV_09_COUPLED_OSCILLATOR_SUBSTRATE` (M9
Stuart-Landau/Kuramoto/Adler beat law, feeding M10-4), `DRIVEN_CANONICAL_HELICITY_4CURRENT_2026-09-08`,
`DRIVEN_NONALIGNED_CLOSURE_2026-09-08`, `DRIVEN_PV_CONST_NOGO_PROOF_2026-09-08`,
`CURRENTLEG_RESIDUAL_REDUCIBILITY_2026-09-08`, `CURRENTLEG_R1_CURRENTNULL_2026-09-08`,
`SELF_UNIFIED_SKYRME_MULTIBODY_2026-09-08`, `B4_MODULI_GEODESIC_EXECUTED_2026-09-08`,
`B4_TWO_DIABATIC_RELAXATION_2026-09-08`, `SEESAW_FTGB_DUALITY_BRIDGE_2026-09-08`,
`ALPHA_KPV_RUNNING_BRIDGE_2026-09-08`, `ALPHA_IR_FIXED_POINT_HOLONOMY_2026-09-08`,
`project_ftgb_open_problems_and_negatives` (current-leg + nu-mass + alpha entries),
`reference_ftgb_coincidence_clues_register` (items 11, 13).
