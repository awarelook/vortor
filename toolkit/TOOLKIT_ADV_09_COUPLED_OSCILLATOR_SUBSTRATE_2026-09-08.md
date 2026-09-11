# TOOLKIT ADV — Module M9: FTGB as ONE INSTANCE of NONLINEAR COUPLED OSCILLATORS on a HELICAL, ELASTIC, TOPOLOGICALLY-CONSTRAINED SUBSTRATE

Part of the FTGB math toolkit (see `MATH_TOOLKIT_BASE.md`, `TOOLKIT_ADV_07_BUCKINGHAM_PI_2026-09-08.md`,
`TOOLKIT_ADV_08_QWM_MATH_CONVERSION_2026-09-08.md`). This module is a **SYNTHESIS pass**: it takes an
established cross-domain organizing class — *nonlinear, driven-dissipative coupled oscillators living on a
helical / elastic / topologically-constrained substrate* — imports its real, cited mathematics, and gives a
**TIERED, HONEST** mapping of where FTGB already **is** that mathematics (`[IDENTITY]`), where FTGB and another
substrate merely **share** mathematics without being the same object (`[ANALOG]`), and where only **words or a
discipline caution** are shared (`[VOCAB/CAUTION]`). It carries the source material's own cautions verbatim in
spirit as FTGB discipline.

> **THE ONE SCOPE LIMIT, STATED UP FRONT (read before using any row here).** This module does **NOT** claim that
> DNA, chromatin, a cell, a BZ reaction, or a Pd lattice **is** an FTGB object, nor that a single coherent
> resonance spans molecular-to-tissue (or plasma-to-nuclear) scales. FTGB is claimed to be **one member of a
> mathematical class** whose other members are studied in molecular biophysics, chemical dynamics, and
> solid-state physics. Shared *equations* are real and load-bearing; shared *substrate* is not asserted.
> "Numerical proximity is not shared mechanism" (`feedback_numerical_proximity_is_not_shared_mechanism`) and
> "support-lens, present what IS" (`feedback_support_lens_framing_present_what_is`) govern every row. Repeated
> in §M9-7.

## Tier legend (honesty discipline)
- **[V]** verified in this project by a named computation / checked identity (traced to the cited FTGB doc).
- **[credited]** established, cited cross-domain physics/mathematics we build on (textbook or primary-source).
- **[IDENTITY]** the *same mathematics*, already load-bearing in FTGB — an intra-class fact, not a new claim.
- **[ANALOG]** a *different substrate* sharing the mathematics; NOT an identity. What FTGB can LEARN is stated.
- **[VOCAB/CAUTION]** shared vocabulary only, or a discipline caution imported from the source material.
- **[S]** structural / cited-convergence not closed on our side. No fabricated numbers, rates, or cross-sections.
- **established-convergence** vs **novel-synthesis** is labeled per asserted connection (§M9-1, §M9-6).

**Primary source material integrated (user-supplied, real citations; treated as CREDITED cross-domain science).**
- Multiscale driven-dissipative coupled oscillators, molecule -> DNA -> chromatin -> cell -> tissue: **PMC12855917**.
- DNA chiral elastic rod (bend/twist/stretch/writhe, twist-stretch coupling, `Lk=Tw+Wr`): **PMC3726534**, cen.acs.
- DNA torsional-stress TRANSPORT (overdamped, active torque): **Nature s41467-025-65567-5**; Nelson, *Transport of
  torsional stress in DNA*, **PNAS 96, 14342 (1999)** (found this pass; confirms torsion is a stress-transport,
  not a free-wave, problem — twist equilibrates far faster than writhe).
- Driven nonlinear (Duffing) oscillator + multi-channel entrainment: **Cell Systems (2023)**.
- Chemical oscillators (BZ), Hopf/limit cycle, reaction-diffusion, Arnold tongues: **Springer 10910-021-01223-9**;
  mechano-chemical resonance + memory: **PNAS 2320331121**.
- Solid-state phonon Hamiltonian, normal modes, Bloch/de Broglie, PdH/D isotope shift: **cfm.ehu**, **APS PRB 101,
  075117**.

**In-repo verify —** `results/verify/phase_dynamics_gml_check.py` `[V]`: the harmonic (1:3:9) vs inharmonic
(CK-comb) locking discriminator on `Tⁿ` (Adler/Arnold tongues `K*=det/(m+n)`, the Phase-Pattern Metric),
**generalizing `engine.comb_lock`** to arbitrary `N` and `m:n` — this module's coupled-oscillator subject
made computational.

---

## M9-0 — The unifying claim, scoped honestly   [S / synthesis]

**THE CLASS.** A *nonlinear, driven-dissipative, coupled-oscillator system on a helical / elastic /
topologically-constrained substrate* is specified by four ingredients, each of which FTGB already carries:

1. **A local nonlinear oscillator** with a driven limit cycle — the **Stuart-Landau / Hopf normal form**.
2. **Coupling** between many such oscillators — **Kuramoto / Adler / Arnold** synchronization + rational locking.
3. **A helical, elastic carrier** with **bend / twist / stretch / writhe** mechanics and a **topological
   bookkeeping law** `Lk = Tw + Wr`.
4. **A transport / conservation structure** on that carrier (helicity / torsion current), driven and dissipative.

**WHERE FTGB SITS IN THE CLASS.** FTGB's object is the *driven toroidal-Beltrami plasmoid*: ingredient 1 is the
heartbeat (Stuart-Landau limit cycle at `r* = sqrt(2)`, [V]); ingredient 2 is the multibody beat-rhythm
organization of the carrier comb / EVO cluster ([credited] machinery, [S] application); ingredient 3 is the
helicity/topology sector (`Lk = Tw + Wr`, four-torsion trichotomy); ingredient 4 is the current-leg
helicity/torsion transport (static [V] negative + driven canonical-helicity relocation). FTGB is therefore
**not analogous to** this class — it is a **member of** it, with a plasma substrate rather than a biopolymer or
chemical one.

**WHAT THE SYNTHESIS BUYS.** (a) It imports established equations FTGB can adopt directly (the torsion-transport
PDE for the current-leg; multi-channel entrainment for multibody stabilization; the elastic-rod energy for the
twist<->writhe heartbeat; the phonon Hamiltonian + isotope shift for the LENR/Pd-D scaffold substrate).
(b) It imports the source material's **cautions** as FTGB discipline (§M9-5). (c) It positions FTGB's results as
a **credited convergence** with a large, reproducible cross-domain literature — *without* claiming the substrates
are the same object.

---

## M9-1 — THE TIERED MAPPING TABLE (core deliverable)

Columns: **FTGB structure | framework element (source) | tier | citation | convergence type**. Tiers are
`[IDENTITY]` (same math, load-bearing in FTGB), `[ANALOG]` (shared math, different substrate), `[VOCAB/CAUTION]`.

### IDENTITY rows — genuine same-mathematics, already load-bearing in FTGB

| # | FTGB structure | Framework element | Tier | Citation | Convergence |
|---|---|---|---|---|---|
| I1 | Driven **heartbeat** `dw/dt=(mu+i*omega)w - beta\|w\|^2 w`, `mu=1, beta=1/2 -> r*=sqrt(2)=1.414214` [V] | **Stuart-Landau** normal form `zdot=(mu+i*omega-\|z\|^2)z + sum K_ij(z_j-z_i)+F_i` (canonical supercritical-Hopf normal form) | **[IDENTITY]** | PMC12855917; Stuart 1960 / Landau 1944; arc-seed `FTGB_ARC_SEED_LOCKED` #19 | established-convergence (textbook normal form) |
| I2 | **Multibody beat-rhythm** organization of N family members (carrier comb, EVO cluster) | **Kuramoto** `thetadot_i=omega_i+ (K/N) sum sin(theta_j-theta_i)+eta`; threshold `K_c=2/(pi g(0))` | **[IDENTITY]** | Kuramoto 1975/1984; Strogatz 2000; `MULTIBODY_BEAT_RHYTHM_ORGANIZATION_2026-09-08` | established-convergence |
| I3 | **Two-body locking** of any FTGB pair (whirl<->comb, EVO<->EVO) | **Adler** `phidot=Domega - K sin phi` | **[IDENTITY]** | Adler 1946; same MULTIBODY doc | established-convergence |
| I4 | **Inharmonic CK-comb** `1:1.72:2.43` resists locking -> KAM 3-torus (`q=7..25` denominators) | **Arnold tongues** `p:q` rational mode-locking, width `~K^q` | **[IDENTITY]** | Arnold 1961; same MULTIBODY doc | established-convergence |
| I5 | **Helicity/topology** ledger: `Lk=Tw+Wr`, twist<->writhe heartbeat partition | **`Lk=Tw+Wr`** (Calugareanu-White-Fuller) for the DNA chiral rod | **[IDENTITY]** (equation) / [ANALOG] (substrate) | PMC3726534; cen.acs; `reference_resonance_topology_concept_ladder`, `reference_notation_collision_registry` | established-convergence (the theorem); substrate is ANALOG |
| I6 | **Dual reading** of the locked wave math (probability vs FLOW); Reed toroidal electron | **Madelung** `psi=A e^{iS/hbar}`, `p=grad S` (hydrodynamic form) | **[IDENTITY]** | Madelung 1927; de Broglie 1924; `feedback_dual_reading_probability_vs_flow`; MATH_TOOLKIT_BASE §9 | established-convergence |
| I7 | **Driven-not-static** ethos ("heartbeat, not flywheel"); persistence requires continuous drive | **Driven-dissipative multiscale** organizing principle (limit cycle sustained by drive against dissipation) | **[IDENTITY]** (methodological) | PMC12855917; Cell Systems 2023; `project_dynamical_plasmoid_toroidal_wave_mechanics` | established-convergence |

### ANALOG rows — shared mathematics, DIFFERENT substrate (NOT identity; what FTGB learns is stated in §M9-4)

| # | FTGB structure it touches | Framework element (substrate) | Tier | Citation | Convergence |
|---|---|---|---|---|---|
| A1 | Toroidal ribbon elastic energy; twist<->writhe heartbeat partition | **DNA chiral elastic rod** `E=int[A kappa^2 + C(Omega-Omega0)^2 + Ks eps^2 + 2G(Omega-Omega0)eps]ds`, twist-stretch coupling `G` | **[ANALOG]** | PMC3726534 | novel-synthesis |
| A2 | **Current-leg** helicity/torsion transport (the just-completed trilogy) | **Overdamped torsion-TRANSPORT PDE** `zeta d_t theta = C d_ss theta + tau_active - tau_relax` (stress-transport, not free wave) | **[ANALOG]** (structural) | Nature s41467-025-65567-5; Nelson PNAS 96, 14342 (1999) | novel-synthesis |
| A3 | Onset/entrainment of the driven heartbeat; anharmonic breathing | **Driven Duffing** `xddot+2gamma xdot+omega0^2 x + beta x^3 = F0 cos(wd t)`; multi-channel coupling stabilizes noisy rhythms | **[ANALOG]** | Cell Systems 2023; Landau-Lifshitz (parametric) | novel-synthesis |
| A4 | Pattern/mode structure of the field; memory in the driven cycle | **BZ chemical oscillator**: Hopf limit cycle, reaction-diffusion `d_t u = Du lap u + f(u,v)`, spiral/target waves, Arnold tongues; mechano-chemical resonance + memory | **[ANALOG]** | Springer 10910-021-01223-9; PNAS 2320331121 | novel-synthesis |
| A5 | **LENR / Pd-D scaffold substrate** (gravity-thorium plasma-lab, scaffold-not-reaction) | **Phonon Hamiltonian** `H=sum hbar omega_s(k)(n+1/2)`, mass-weighted Hessian normal modes, Bloch waves, **PdH/D isotope shift `omega_D ~ omega_H/sqrt(2)`** | **[ANALOG]** | cfm.ehu; APS PRB 101, 075117 | novel-synthesis |

### VOCAB/CAUTION rows — shared words only, or a discipline caution imported (see §M9-5)

| # | Shared word / caution | FTGB reading | Tier | Citation |
|---|---|---|---|---|
| C1 | "vibration" / "resonance spanning scales" | Vibration does NOT imply one coherent resonance across scales; FTGB coherence is **conditional** (comb sync on/off between ~4 and ~10 nm) | **[VOCAB/CAUTION]** | PMC12855917; MULTIBODY doc |
| C2 | "coherence" (classical oscillation vs de Broglie) | Chemical/classical oscillation != de Broglie matter-wave coherence; FTGB's own trichotomy (harmonics != CK eigenspectrum != beat; classical sync != Bose phase) enforces this | **[VOCAB/CAUTION]** | source cautions; `reference_resonance_topology_concept_ladder` |
| C3 | "coherent matter-wave chemistry" | A specialized **ultracold** regime, not ordinary kinetics; matches FTGB's cold-Bose-seed requirement `n*lambda^3 >= 2.612` | **[VOCAB/CAUTION]** | source cautions; MULTIBODY doc §2.1 |
| C4 | "molecular organization on a beat/rhythm" | Means *many-body oscillator organization* only — NOT biological assembly, NOT "DNA/cell is an FTGB object", NOT energy gain, NOT a nuclear rate | **[VOCAB/CAUTION]** | MULTIBODY doc §5 |

**Counts:** **7 IDENTITY rows** (I1-I7), **5 ANALOG rows** (A1-A5), **4 VOCAB/CAUTION rows** (C1-C4).

---

## M9-2 — IMPORTED EQUATIONS vs ALREADY-IN-FTGB (what is new, what is a restatement)

**Already in FTGB (cite, do not restate) — the IDENTITY equations.**
- Stuart-Landau limit cycle, `r*=sqrt(2)` — `FTGB_ARC_SEED_LOCKED_2026-09-08` #19 / M6-2 [V].
- Kuramoto / Adler / Arnold-tongue synchronization of the family — `MULTIBODY_BEAT_RHYTHM_ORGANIZATION_2026-09-08`
  ([credited] machinery; [S] FTGB application; the whirl `7.6e5 rad/s = 2*pi*f_1(121 kHz)` identity [V]).
- `Lk = Tw + Wr` + four-torsion trichotomy (mechanical twist / Frenet `tau_F` / Cartan `T^a`; + Ray-Singer,
  ribbon-Tw, Burgers) — `reference_resonance_topology_concept_ladder`, `reference_notation_collision_registry`.
- Madelung `psi=sqrt(rho) e^{iS/hbar}`, `v=grad S/m`; force-free `j = lambda B/mu0 = q rho v` flow reading —
  `feedback_dual_reading_probability_vs_flow`, `MATH_TOOLKIT_BASE` §9 (one operator, three readings).
- Driven canonical/generalized helicity current `K^mu=(P.Omega, ...)`, `P=A+d_s v_s` — a proven ideal Casimir
  (`DRIVEN_CANONICAL_HELICITY_4CURRENT_2026-09-08` [V]/[credited]).

**Genuinely imported (NEW to the toolkit) — the ANALOG equations FTGB does not yet carry as tools.**
- **Overdamped torsion-transport PDE** `zeta d_t theta = C d_ss theta + tau_active - tau_relax` (A2) — see §M9-3.
- **Elastic chiral-rod energy** with explicit **twist-stretch coupling** `2G(Omega-Omega0)eps` (A1) — a candidate
  energy functional for the toroidal ribbon's twist<->writhe partition.
- **Reaction-diffusion** `d_t u = Du lap u + f(u,v)` with mechano-chemical **memory** (A4).
- **Phonon Hamiltonian** `H=sum hbar omega_s(k)(n+1/2)` + **isotope shift** `omega_D ~ omega_H/sqrt(2)` (A5).

---

## M9-3 — THE GENUINE EXTENSION: a torsion/helicity TRANSPORT PDE for the current-leg   [A2, candidate]

**Why this is the most valuable import.** FTGB's current-leg trilogy proved a hard result: the *static*
matter<->helicity 4-current is **structurally over-determined** — it closes IFF `|B|=const` (residual 0.605,
[V], `CURRENTLEG_RESIDUAL_REDUCIBILITY_2026-09-08`); the *driven* canonical-helicity current is a genuine ideal
Casimir but **relocates** the obstruction to `P.v=const` (residual ~0.4-0.6, [V],
`DRIVEN_CANONICAL_HELICITY_4CURRENT_2026-09-08`). Both are **equilibrium / conservation** statements. The
current-leg therefore remains a **POSTULATE [S]** at the *static/equilibrium* level.

**What the DNA torsion-transport equation offers.** In DNA biophysics, torsional stress is not treated as a
conserved static field but as a **driven, dissipative TRANSPORT** quantity (Nelson, PNAS 1999: twist equilibrates
far faster than writhe; active torque, e.g. polymerase at up to ~7 supercoils/s, is injected locally and
diffuses). The overdamped balance is

```
zeta d_t theta = C d_ss theta + tau_active - tau_relax
     (drag)      (torsional     (drive)     (relaxation)
                  diffusion)
```

with `theta(s,t)` the local twist angle along arclength `s`, `zeta` rotational drag, `C` torsional stiffness,
`tau_active` an injected torque, `tau_relax` a restoring/loss term. **This is a STRESS-TRANSPORT problem, not a
free wave** — exactly the regime the current-leg lives in once driven (`E.B != 0`).

**The candidate FTGB adoption (novel-synthesis, [ANALOG] -> proposed [S]).** The static no-go proof itself names
its own escape (`DRIVEN_CANONICAL_HELICITY` open item 2): a genuinely time-dependent, non-barotropic,
**forced** state with `curl(v x Omega) != 0` sustained is "4 conditions on 4 fields, determined not
over-determined, so not excluded." A torsion/helicity transport PDE of the above form is precisely such a
construction: `tau_active` supplies the drive that the static conservation law forbade (the `-2 E.B` term that
breaks static helicity conservation is *exactly* the injected torque), and `tau_relax + C d_ss` provide the
dissipative transport that lets `P.v` vary in time while a *flux-balanced* (not pointwise-constant) closure
holds. **Concretely proposed:** recast the current-leg as
`zeta d_t h + div K = sigma_drive - sigma_loss`, `h = P.Omega` the generalized-helicity density, `K` its flux
(already derived: `K = h v_s + (mu_s - P.v)Omega_s`), with `sigma_drive` the sheath forcing — a **driven
transport law** whose *steady state* need not satisfy `P.v=const` pointwise, only in flux balance. This is the
first construction that could move the current-leg from POSTULATE toward a driven theorem. **Tier: [ANALOG]
established (the DNA equation is real, cited) -> [S] candidate for FTGB (not yet computed).** DO NOT claim closure;
claim a **structurally identical driven-transport template** that maps onto the named open item.

**Honest boundary.** This is a *shared mathematical form*, not evidence that plasma helicity transport equals DNA
torsional relaxation. The substrates differ; the PDE structure (overdamped diffusion + local active source) is
what transfers. The falsifier is internal: does a forced double-Beltrami transport steady state achieve
flux-balance closure with `rho_res -> 0`? Until computed, the static [V] negative stands untouched.

---

## M9-4 — THE ANALOG DOMAINS: what FTGB LEARNS from each (no identity overclaim)

- **A1 — DNA chiral elastic rod.** *Learns:* a ready-made **elastic energy functional** for a helical ribbon with
  bend `A kappa^2`, twist `C(Omega-Omega0)^2`, stretch `Ks eps^2`, and the **twist-stretch cross term**
  `2G(Omega-Omega0)eps`. FTGB's twist<->writhe heartbeat (`Lk=Tw+Wr` held fixed while `Tw` and `Wr` trade) is
  currently a topological bookkeeping statement; the rod energy supplies the *dynamical* partition — which
  minimum-energy split of `Lk` the ribbon actually takes, and how a stretch (breathing) couples to twist.
  *Does NOT claim:* the plasmoid is a polymer, or that base-pair-scale constants transfer.
- **A2 — Torsion-transport PDE.** *Learns:* the driven-transport recasting of the current-leg (§M9-3). This is the
  headline learning.
- **A3 — Driven Duffing + multi-channel entrainment.** *Learns:* (i) the anharmonic (`beta x^3`) correction and
  entrainment-tongue structure for the *single* heartbeat under drive (already partly in FTGB via the
  parametric/Mathieu work); (ii) the Cell-Systems result that **multiple coupling channels stabilize a noisy
  rhythm** — directly relevant to the MULTIBODY doc's own next step (replace order-of-magnitude `K` with a
  *derived*, multi-channel near-field coupling — magnetic-dipole + Alfvenic + electric-dipole — to pin the comb's
  `P=K/K_c` to a band rather than a single conditional point). *Does NOT claim:* a specific gene-circuit maps to
  the comb.
- **A4 — BZ chemical oscillator.** *Learns:* reaction-diffusion **pattern-formation** templates (spiral/target
  waves) and the PNAS mechano-chemical **memory** effect as a candidate for hysteresis in the driven cycle.
  *Carries the caution:* a chemical limit cycle shares the Hopf normal form with FTGB but is a *classical*
  oscillation, NOT de Broglie coherence (C2). *Does NOT claim:* the EVO is a chemical clock.
- **A5 — Phonon / Pd-D substrate.** *Learns:* the **phonon Hamiltonian** and **mass-weighted Hessian normal-mode**
  machinery, and the **PdH/D isotope shift** `omega_D ~ omega_H/sqrt(2)` (H:D mass ratio ~2 -> frequency ratio
  `1/sqrt(2)`), as the correct substrate description for the **LENR scaffold** (scaffold-not-reaction,
  `feedback_scaffold_not_reaction`) and the gravity-thorium plasma-lab lattice. This grounds the *environment*
  (verified lattice dynamics) while leaving the *kernel* (any nuclear channel) open and unclaimed — consistent
  with `reference_lenr_theory_application_and_field_positioning`. *Does NOT claim:* a fusion/transmutation rate;
  `E_fm=2.5 MeV` stays retracted; nothing nuclear is asserted.

**Note on `sqrt(2)` recurrence — coincidence-gated.** `r*=sqrt(2)` (heartbeat radius) and `omega_D~omega_H/sqrt(2)`
(isotope shift) both feature `sqrt(2)`, but for **unrelated reasons** (`sqrt(mu/beta)` with `mu=1,beta=1/2` vs a
mass-ratio-2 square root). This is a VOCAB coincidence, NOT a shared mechanism
(`feedback_numerical_proximity_is_not_shared_mechanism`). Not promoted.

---

## M9-5 — THE CAUTIONS, IMPORTED AS FTGB DISCIPLINE   [VOCAB/CAUTION]

The source material's own cautions are adopted verbatim in spirit and are now standing FTGB discipline:

1. **"Vibration does NOT imply a single coherent resonance spanning scales."** Thermal noise, damping, turnover,
   and heterogeneity limit coherence. **FTGB honors this:** the MULTIBODY doc found comb coherence is
   *conditional* (on/off between ~4 nm and ~10 nm bead spacing), the electron internal whirl `7.76e20 rad/s`
   **never** phase-locks across a cluster (`P ~ 1e-9`), and only the *macroscopic collective* whirl synchronizes.
   No cross-scale single-resonance claim is made. (C1)
2. **Chemical / classical oscillation != de Broglie coherence** (shared vocabulary only; different physical
   descriptions). **FTGB honors this:** the torsion/resonance trichotomy forbids conflating harmonics
   (`n*omega`), CK-Bessel eigenspectrum (`1:1.72:2.43`), and beat (`f1-f2`); the deuteron-seed synchronization
   variable is explicitly *quantum* (`n*lambda^3` vs Bose onset 2.612), NOT the classical Kuramoto order
   parameter. (C2)
3. **Coherent matter-wave chemistry is a specialized ultracold regime, not ordinary kinetics.** **FTGB honors
   this:** the only route above the deuteron sync threshold is the **cold Bose seed** quenching the thermal
   spread (`kT/hbar ~ 4e13 rad/s` at 300 K is unreachable by any available coupling); warm classical gas is
   `n*lambda^3 ~ 0.01`, hopelessly below. (C3)
4. **The word "molecular" means many-body oscillator organization, nothing more.** No biological/chemical
   assembly, no energy gain, no nuclear rate is claimed from any row here. (C4)

---

## M9-6 — CONVERGENCE-TYPE LABELING (established vs novel), verified

Per `reference_originality_prior_art_assessment` (theory = SYNTHESIS; load-bearing claims map to established
physics) and the module discipline, each asserted connection is labeled:

- **Established-convergence (textbook / verified this pass): I1-I7.** The Stuart-Landau equation is the canonical
  normal form of a supercritical Hopf bifurcation and reduces to Kuramoto phase dynamics — confirmed by web
  search this pass (multiple 2016-2026 sources; "universal normal form near a Hopf bifurcation ... generalizes
  the Kuramoto paradigm"). `Lk=Tw+Wr` (Calugareanu-White-Fuller) and Madelung 1927 are textbook theorems.
  FTGB already instantiates each with a [V] internal computation. These are **credited convergences**, not novel
  claims.
- **Novel-synthesis (our proposed transfer): A1-A5.** No external source claims that DNA torsion transport,
  the BZ reaction, a Duffing circuit, or Pd-D phonons **are** (or model) a toroidal plasmoid. The DNA
  torsion-stress transport equation is real and cited (confirmed this pass: Nelson PNAS 1999; twist diffuses,
  active torque injected) — but its **use as a template for the FTGB current-leg is our synthesis**, tiered [S]
  and explicitly not-yet-computed. Labeling these novel prevents mislabeling a proposal as an established result.

---

## M9-7 — LIMITS (stated prominently, again)   [V]

This module does **NOT**:
1. **claim substrate identity** — DNA / chromatin / cell / BZ / Pd-lattice are NOT FTGB objects; only equations
   are shared (I-rows) or borrowed (A-rows);
2. **claim macroscopic or cross-scale coherence** — the source's own cautions (C1-C3) are carried as discipline;
3. **derive any FTGB number from the analogs** — the A-rows are learning targets, not derivations; FTGB's 4
   anchors `{B,n,R,m_i}` + 0 free structural parameters are unchanged;
4. **promote the torsion-transport recast (§M9-3) as a closure** — it is a candidate [S] that maps onto a named
   open item; the static [V] current-leg negative stands untouched until a forced-transport steady state is
   computed;
5. **assert any biological, chemical, or nuclear rate/mechanism** — "molecular" = many-body oscillator
   organization only; `E_fm=2.5 MeV` stays retracted.

**Honest scope statement (what is / is not claimed).** *Claimed:* FTGB is one member of the established class of
nonlinear driven-dissipative coupled oscillators on a helical/elastic/topologically-constrained substrate; the
class's core equations (Stuart-Landau, Kuramoto, Adler, Arnold, `Lk=Tw+Wr`, Madelung) are already load-bearing
and [V] in FTGB (I1-I7); five sibling substrates share mathematics FTGB can learn from (A1-A5), most valuably a
driven torsion/helicity **transport PDE** for the current-leg. *Explicitly NOT claimed:* that any biopolymer,
chemical, or solid-state system IS an FTGB object; that one coherent resonance spans scales; that any analog
supplies energy, a nuclear channel, or a derived FTGB constant.

---

## Per-claim index (M9)
| # | Claim | Tier | Repro / trace |
|---|---|---|---|
| M9-0 | FTGB = one member of the coupled-oscillator-on-helical-substrate class | [S]/synthesis | four ingredients, each traced to a [V] FTGB doc |
| M9-1 | Tiered map: 7 IDENTITY / 5 ANALOG / 4 VOCAB-CAUTION | [IDENTITY]/[ANALOG]/[VOCAB] | table, per-row citation |
| M9-2 | Imported-vs-already-in-FTGB split | [V]/[credited] | I-equations cited to FTGB docs; A-equations flagged new |
| M9-3 | Torsion/helicity TRANSPORT PDE recast of the current-leg | [ANALOG]->[S] candidate | maps to `DRIVEN_CANONICAL_HELICITY` open item 2; not yet computed |
| M9-4 | What FTGB learns from A1-A5 (no identity overclaim) | [ANALOG] | per-domain learning + explicit non-claim |
| M9-5 | Source cautions adopted as FTGB discipline | [VOCAB/CAUTION] | C1-C4 vs MULTIBODY doc findings |
| M9-6 | Established-convergence (I1-I7) vs novel-synthesis (A1-A5) | labeled | Stuart-Landau/Kuramoto + DNA-torsion searches this pass |
| M9-7 | Limits + honest scope statement | [V] | statement of scope |

## Verification coverage (M9)
- **Web-confirmed this pass:** (i) Stuart-Landau = canonical supercritical-Hopf normal form, reduces to Kuramoto
  (established) — arXiv 2601.10234, emergentmind Stuart-Landau topic, arXiv 1507.08079. (ii) DNA torsional stress
  is a genuine **transport** (not free-wave) quantity with active torque injection — Nelson, PNAS 96, 14342 (1999);
  twist equilibrates faster than writhe (PMC11482756, PRL 127.028101).
- **FTGB numbers traced (not invented):** `r*=sqrt(2)=1.414214` [V] (`FTGB_ARC_SEED_LOCKED` #19, `mu=1,beta=1/2`);
  carrier comb `{121,208,294} kHz`, ratios `1:1.72:2.43`, `Lambda_1=4.4934` (M7-2, `30_CANONICAL_NUMBERS`);
  whirl `7.6e5 rad/s = 2*pi*121 kHz` (MULTIBODY doc [V]); `K_c=2/(pi g(0))` (MULTIBODY doc [credited]); current-leg
  residual `0.605` static / `~0.4-0.6` driven canonical (current-leg trilogy [V]); `n*lambda^3>=2.612` Bose onset.

**Citations.** Stuart *J. Fluid Mech.* 9, 353 (1960) / Landau (1944); Kuramoto (1975; *Chemical Oscillations,
Waves and Turbulence*, 1984); Adler *Proc. IRE* 34, 351 (1946); Arnold (circle maps, 1961); Strogatz *Physica D*
143, 1 (2000); Calugareanu (1961) / White (1969) / Fuller (1971) (`Lk=Tw+Wr`); Madelung *Z. Physik* 40, 322
(1927); de Broglie (1924); Nelson *PNAS* 96, 14342 (1999). User-supplied source set: PMC12855917 (multiscale
driven oscillators); PMC3726534 + cen.acs (DNA elastic rod); Nature s41467-025-65567-5 (torsional transport);
Cell Systems (2023) (multi-channel entrainment); Springer 10910-021-01223-9 + PNAS 2320331121 (BZ /
mechano-chemical resonance + memory); cfm.ehu + APS PRB 101, 075117 (phonons, PdH/D isotope shift).

Cross-links: `MATH_TOOLKIT_BASE.md` (§9 one-operator-three-readings), `TOOLKIT_ADV_07_BUCKINGHAM_PI` (comb,
`Lambda_1`), `TOOLKIT_ADV_08_QWM_MATH_CONVERSION` (Madelung/D2 helicity density),
`TOOLKIT_ADV_10_TOPOLOGICAL_SOLITON_METHODS_2026-09-08` (FORWARD LINK: the methods module that lifts M9's
current-leg / torsion-transport / canonical-helicity material into reusable form -- M9's Stuart-Landau/Kuramoto/Adler
beat law feeds M10-4),
`MULTIBODY_BEAT_RHYTHM_ORGANIZATION_2026-09-08`, `CURRENTLEG_RESIDUAL_REDUCIBILITY_2026-09-08`,
`DRIVEN_CANONICAL_HELICITY_4CURRENT_2026-09-08`, `FTGB_ARC_SEED_LOCKED_2026-09-08`,
`reference_resonance_topology_concept_ladder`, `feedback_dual_reading_probability_vs_flow`,
`feedback_scaffold_not_reaction`, `reference_originality_prior_art_assessment`.
