# The Coherent Object

## A driven Beltrami–Hopf toroidal soliton read as field and matter wave: the complete presentation

**Nathaniel Hanks** · 2026-09-15 · version 1.2.0
Reproduce everything: `pip install -r requirements.txt && python results/verify/verify_all.py` → **90/90** PASS, deterministic, offline, CI-gated on every push.
Companions: ten-page version `paper/FTGB_TEN_PAGE_2026-09-15.md` · longform synthesis `FTGB_GRAND_SYNTHESIS.md` (+ Addendum H) · per-claim ledger `results/TIER_LEDGER.md` · visual gallery `gallery.html`.

---

## Abstract

We present a single geometric object — a driven, force-free **Beltrami eigenmode** `∇×B = λB` on a toroidal
domain, carrying Hopf-linked field lines and an inharmonic spectral comb — and read it simultaneously as a
*plasma structure* (the plasmoid / ball-lightning / EVO family) and, through the Madelung correspondence, as
a *matter wave*. Everything traces to four measured anchors `{B, n_i, m_i, R}` plus one structural selection
(`ε = a/R = 1/φ`), with zero fitted parameters. The theory is developed under an explicit honesty discipline
in which every claim carries a tier and every tiered claim is reproduced by a named script. The verified core
contains: an exact global-regularity statement for the coherent state ("coherence *is* regularity"); the same
state as an exact *driven* steady solution and stable attractor swept across Reynolds number 126→628; the
Chandrasekhar–Kendall inharmonic comb `1 : 1.719 : 2.427` as a falsifiable linear-limit fingerprint; a
one-mode "heartbeat" theorem (fixed-helicity minimization is a linear program — a beat-carrying object must
be driven); computed topology, chirality, charge-conjugation and Majorana structure; an exact spectral zeta
on S³; and a conserved nuclear energy ledger. Thirteen computed refutations are retained as results. The one
open nuclear problem is converged — by a chain of adversarially verified computations — to a single geometric
question, the **entrance-channel assembly corridor**, carrying two data bars, a derived constraint on the
crossing (`β·|dF| ≤ 0.874 MeV/fm`, under the structural hypothesis that d+d→⁴He-vs-breakup is an adiabatic
Landau–Zener crossing), a computed *exclusion* of density geometry as the source of that selectivity (leaving
orientation/phase structure, the moduli metric, and the boundary physics as the live candidates), and a new
experimentally accessible falsifier: **polarization-steered aneutronic yield**. The theory proves no
LENR, derives no COP, demonstrates no new nuclear mechanism, and fabricates no number: its contribution is
the conversion of a scattered anomaly landscape into one tiered, falsifiable, reproducible program.

---

## How to read this paper: the tier legend

Every claim below carries one of five labels, and the label is part of the claim:

- **[V]** — verified in this work by a named script in `results/verify/` that a reader can re-run;
- **[credited]** — established physics or mathematics we build on, cited, not re-derived;
- **[S]** — a structural hypothesis: falsifiable, labeled, never silently promoted;
- **[flag]** — a numerical observation logged as a clue (a coincidence ledger exists for exactly this);
- **settled-negative** — a computed refutation, kept and cited as a result.

*Plain language: the labels are the instrument. A reader who trusts nothing can re-run all 90 checks with one
command; a reader who trusts the labels can navigate the whole theory knowing precisely where the floor is.*

---

# Part I — Method

## 1. The honesty discipline as scientific instrument

The project operates under standing rules that are enforced mechanically, not aspirationally:

1. **Every load-bearing claim has a script.** The harness (`verify_all.py`) runs 87 theory scripts plus three
   engine programs; a failing assertion turns the public CI badge red. Nothing is asserted that a stranger
   cannot re-run, deterministically, offline.
2. **Settled-negatives are wins.** When a tempting idea fails the mathematics, the failure is *computed,
   logged, and kept* as a cited result (§9 lists thirteen). A theory's dead ends, honestly mapped, are part of
   its value.
3. **Coincidences are computed and logged, never promoted.** A dedicated ledger
   (`results/COINCIDENCE_LEDGER.md`) records every numerical near-miss with a verdict
   (DERIVED / RESTATEMENT / GENERIC / BACK-FIT / CIRCULAR / DEAD / COINCIDENCE), so nothing is silently
   dismissed *or* silently dressed up as a derivation.
4. **The discipline is symmetric.** Under-claiming is policed as hard as over-claiming. The recent record
   includes both directions: a "too defeatist" scoping corrected *upward*, and two of the project's own audit
   findings *refuted by computation* (§11.3).
5. **No number is fabricated.** Open quantities (`ρ_eff`, the corridor rate, the EMF magnitude) are named as
   open. Measured inputs are cited at the point of use; external data (AME2020 masses, TUNL levels, measured
   screening) is vendored with provenance.

*Plain language: most theories ask to be believed; this one asks to be re-run. The discipline is not
decoration — it is what makes the frontier claims meaningful, because the reader always knows which
statements are load-bearing and which are bets.*

## 2. Reproducibility architecture

Four access tiers cover every derivation: **A** — the CI harness (numpy + mpmath, no network); **B** — the
scipy/sympy provenance layer, vendored frozen under `frontier_calcs/`; **C** — FreeFEM finite-element torus
eigensolves, vendored with meshes; **D** — named external handoffs (a GPU pseudo-spectral run for
high-Reynolds regularity; the near-BPS nuclear run), each specified in `handoffs/` with honest scoping.
Canonical numbers are re-derived in-repo from cited anchors (`canonical_numbers_provenance_check`), and the
one absolute-magnitude caveat — the Alfvén-speed band — is *quarantined by proof*: scaling `v_A` over a 65×
band leaves every dimensionless observable invariant to 10⁻¹⁶ (`absolute_magnitude_invariance_check`).
Confronted artifacts from salvaged pre-project material are vendored *with their fence status* so the
project's own history is auditable.

---

# Part II — The object

## 3. The Beltrami state and its spectrum

*Plain language: let a magnetized plasma relax while its "knottedness" (helicity) is conserved. It settles
into the one configuration whose current runs exactly along its own field — nothing pushes on anything. That
configuration is an eigenmode of the curl operator, and on a bounded domain the eigenvalues are quantized:
the object rings at specific tones, like a bell — but an* inharmonic *bell, and the specific inharmonicity is
the theory's fingerprint.*

**The state [credited].** At fixed magnetic helicity `H = ∫A·B`, the minimum-energy state of ideal MHD is the
force-free (Beltrami) field

```
∇×B = λB ,      J×B = 0        [Woltjer 1958; Taylor 1974; Moffatt 1969]
```

with a single eigenvalue λ. This is the relaxed state observed across laboratory and astrophysical plasmas
(spheromaks, reversed-field pinches). FTGB's move is to take it as a *driven physical object* — dissipative,
toroidal, knotted, breathing — and to follow the mathematics of that object wherever it goes.

**The spectrum [V]/[credited].** On the ball, the Chandrasekhar–Kendall construction reduces the vector
eigenproblem to a scalar one; the boundary condition `B·n = 0` quantizes the lowest (`l=1`) tower at the
roots of

```
tan x = x        →        x_n = 4.4934, 7.7253, 10.9041, 14.0662, …
```

reproduced in-repo two independent ways (bisection ‖ 40-digit mpmath; `ck_eigenvalues_check`). The ratios

```
x_n / x_1  =  1 : 1.719 : 2.427 : 3.130 : …
```

form an **inharmonic comb** — decisively different from a harmonic `1:2:3` overtone series — and are
*scale-invariant*: the same ratios apply from laboratory kHz to any other regime, because they are pure
boundary geometry. At the measured anchors (below) the comb lands at `{121, 208, 294}` kHz.

**Geometry honesty [V].** The `4.4934` is the *ball* eigenvalue, not a universal constant. The toroidal
eigenproblem (finite aspect `ε = a/R`) is solved in the vendored FreeFEM layer: the torus splits the
near-degenerate doublet by `Δλ = 0.2806` at the canonical aspect, with the raw gap *linear* in ε
(`Δλ = ε/(2j₀,₁)`, settled by a 14-point scan). Every comb-based falsifier states which geometry it assumes.

**Anchors and the one selection.** Everything numerical traces to four measured anchors `{B, n_i, m_i, R}`
(field, ion density, ion mass, major radius) plus **one [S] structural selection**: the aspect ratio
`ε = a/R = 1/φ = 0.618` — the most-irrational choice, selected for KAM protection of the multi-frequency
rhythm (§5.4), honestly labeled a selection, not a derivation. There are zero *fitted* structural parameters.

**The beat.** Two near-degenerate CK modes beat at

```
f_b  =  (v_A / 2πR) |Δλ|        [V: delta_detuning_beat_check]
```

— a slow (kHz-scale) *macroscopic* envelope rhythm. Part IV establishes what this beat is (an energy
observable of a driven system) and, just as importantly, what it is *not* (never a pump of any microscopic
channel — a settled-negative with 16.8 orders of margin).

## 4. Coherence is regularity

*Plain language: the deepest structural fact in the theory. The term in the fluid equations that causes
turbulence and blow-up — the nonlinear self-advection — is* identically zero *at the coherent state. The
object cannot tear itself apart, not because dissipation wins a fight, but because at coherence there is no
fight. And when you drive it to replace its losses, it does not merely persist: it attracts.*

**The exact statement [V].** For a velocity-Beltrami field, vorticity is parallel to velocity
(`ω = ∇×u = λu`), so the **Lamb vector vanishes pointwise**:

```
u×ω = λ(u×u) = 0        (verified to 3×10⁻¹⁵)
```

The advection term then collapses to a pure gradient, `u·∇u = ∇(½|u|²)`, absorbed into pressure — the
Navier–Stokes nonlinearity is *inert* on this state. Since a Beltrami field is a Stokes eigenfunction,

```
u(t) = e^{−νλ²t} u₀
```

is an **exact, eternal, smooth solution** (the class is classical — Trkalian flows, Trkal 1919 [credited];
the in-repo verification and the coherence-is-regularity reading are this work's). Enstrophy decays
monotonically, the Beale–Kato–Majda integral is finite, blow-up never triggers
(`exact_beltrami_regularity_check`). *Honest scope:* this is regularity of the object **as** its coherent
state — the general large-data 3-D problem stays open and is not claimed.

**Driven and attracting [V].** Forcing with `f = νλ²u_B` (the drive replaces exactly the viscous loss) makes
the state an **exact time-independent solution** (steady to 6×10⁻¹⁶ under a full nonlinear pseudo-spectral
run) and a **stable attractor**: a 30%-amplitude broadband perturbation decays monotonically, while a
Taylor–Green control base drifts under the same protocol (contrast ratio 3×10¹⁴). Swept across viscosity,
the attractor persists from **Re ≈ 126 to 628** (32³ resolution, confirmed 48³) with the attraction *not
weakening* as Re rises (`r2_driven_beltrami_attractor_check`, `r2_reynolds_sweep_check`). The unconditional
high-Reynolds case (`S ~ 10³–10⁴`) is a named GPU handoff, not claimed.

**The conditional theorems [V-cond].** Around the coherent state, an exact vortex-stretching = Lamb-vector
flux identity yields a Grönwall enstrophy bound: global regularity *provided* the time-averaged Beltrami
deviation satisfies `⟨η²⟩ < ν²λ₁` (`r2_identity_check`, `r2_gronwall_check`). The Hall-MHD lift holds at
magnetic Prandtl `Pm = 1`, and the `Pm ≠ 1` obstruction was shown to be a canonical-variable artifact: a
coupled Lyapunov functional `L = ½‖ω‖² + κd_i²·½‖J‖²` has diagonal coercive dissipation at every `Pm`,
leaving one Hall-smallness residual (`hallmhd_coupled_lyapunov_check`). **The honest gap, computed:** the
physical plasmoid *violates* that smallness — its ion skin depth exceeds the object (`d_i/R ≈ 2.5`,
`S_di ≈ 15–2400 ≫ 1`) — so the real object lives *outside* the proven regime
(`r3_hall_smallness_physical_check`). The theory states this against itself, in physical units.

**The structural no-go [V].** The current-leg trilogy: a static identification of the topological 4-current
with the matter current requires `|B| = const`, which is *impossible* for a nontrivial force-free field
(computed `std/mean = 0.58`); the aligned variant fails on the alignment invariant; the driven closure
`S = 0` is realizable but externally driven, not emergent (`currentleg_trilogy_check`). The theory's own
flagship identification is thereby fenced by its own theorem — the discipline applied inward.

---

# Part III — The rhythm

## 5. The heartbeat theorem and the driven rhythm layer

*Plain language: the object's slow beat is not an accident — it is forced. A relaxed plasma always collapses
to a single tone; anything carrying TWO tones (and hence a beat) is being actively driven against that
collapse. The beat is therefore a diagnostic of drivenness — a heartbeat, not a flywheel. This section also
contains the discipline's sharpest self-limitation: what a slow beat can and cannot do.*

**5.1 The heartbeat theorem [V].** Fixed-helicity energy minimization over any N distinct-eigenvalue Beltrami
modes is exactly a **linear program** whose optimum is always the single lowest mode — no static multi-mode
mixture is ever a critical point (`nmode_woltjer_lp_check`). Corollary: a beat-carrying object must be
**driven**; remove the drive and Taylor relaxation kills the rhythm. The driven amplitude dynamics is the
Stuart–Landau normal form `z' = (μ + iω − |z|²)z` with its `r* = √2` limit cycle — the "heartbeat."

**5.2 What a beat is [V]/[credited].** The beat is a *nonlinear/energy observable* — a torque/intensity line
at `f_b = |f₂−f₁|` (plus a sum line at `f_Σ`), not a linear field line (`rhythm_parametric_resonance_check`).
Mathieu parametric resonance has its principal tongue at `Ω = 2ω₀` with threshold `2/Q`; Adler two-body
locking holds for `|Δω| ≤ K`; both are credited classical rhythm machinery, internalized with scripts.

**5.3 The anharmonic leg [V].** The Stuart–Landau heartbeat (shear `c = 0`) omits amplitude–frequency
coupling. The Duffing backbone restores it: `Ω_peak(A) ≈ ω₀(1 + 3βA²/8ω₀²)` — under hard drive the comb
ratios *pull* (`ω_eff = ω − c|z|²`), with bistability and odd harmonics (`duffing_backbone_check`).
**Consequence for falsification:** the CK comb fingerprint is a **linear-limit statement** — the Duffing
pull is separable from the Arnold-tongue lock, and the experimental protocol must operate (or extrapolate
to) low drive.

**5.4 The many-body layer [V]/[S].** A population of these driven oscillators synchronizes by the standard
machinery: the Kuramoto mean-field onset at `K_c = 2γ` (Lorentzian), reproduced in-repo with N = 800
(onset at `P = K/K_c = 1.20`, order parameter `r(2K_c) = 0.69` vs the mean-field `√½ = 0.71`); the chaotic
boundary of the forced-Hopf/Aizawa family carries a computed positive Lyapunov exponent
(`λ_max = 0.094 > 0`, Benettin) (`multibody_sync_capture_check`). The *identification* of specific FTGB
populations with this machinery stays [S]; the Aizawa branch is carried strictly as the disordered
*boundary* of the ordered heartbeat — an analogy with one load-bearing bit (the sign). The inharmonic comb
protects its own rhythm: the ratios are stubbornly irrational, Arnold tongues at those rationals are
astronomically thin, and the golden aspect `ε = 1/φ` is the extreme of that KAM protection — the one [S]
selection, now with its reason visible.

**5.5 The cross-scale fences (the discipline's sharpest instrument) [V]/settled-negative.** A slow beat is a
*macroscopic collective* scale. Computed, logged, and kept:

- the literal `kHz = MeV` identity is **dead by 16.8 orders of magnitude** (`E_beat = h·f_b = 0.36 neV` vs
  `Q = 23.847 MeV`);
- the beat-as-**pump** reading is **doubly closed**: parametrically short by 15.7 orders, *and* the nuclear
  crossing is frozen/DC across a kHz cycle (`τ_cross/T_kHz ~ 10⁻¹⁸`) (`cross_scale_slow_scale_audit_check`);
- the fence **extends unchanged to GHz/THz**: a salvaged pre-project claim of an 11.127 GHz "beat-modulated
  tunneling gain" was confronted and fence-killed — the beat is frozen across any tunneling attempt
  (`τ/T_beat ≈ 3×10⁻⁷`), and the artifact itself proved internally inconsistent by ~82 orders against
  standard WKB at its own stated barrier (`beat_modulated_tunneling_nogo_check`).

What survives for the beat is exactly one role: a slow macroscopic **rate-gate** (duty cycle) on the
collective object — [S], falsifiable via the yield-step protocol of §8.

---

# Part IV — Topology, chirality, and the matter wave

## 6. Topology and the chirality cluster

*Plain language: the object's knots and handedness are not decoration — they are computed, and they carry
the particle-like structure. One honest subtlety leads: the idealized reference field has a perfect integer
knot number, but the actual eigenmode does not, and the theory says so on its front page.*

**6.1 Invariants [V].** The idealized closed-fibre reference field carries Hopf charge `Q_H = 1` (Gauss
linking, computed) and the wave-mode Chern number `C = ±2` (Fukui–Hatsugai on the spin-1 photon band — the
photon helicity index, `|C| = 2Q_H`) (`topology_invariants_check`). The **actual CK eigenmode** carries a
*real* helicity `H ≈ 0.088`, not an integer — its Whitehead pull-back is 54% non-solenoidal — and every
front-door statement carries this qualifier. Integer *winding*, by contrast, is topologically protected
away from field zeros and can slip only through an exact zero — both the protection (to 7×10⁻¹⁶) and its
boundary are observed through violent FPUT collapse (`fput_winding_conservation_check`).

**6.2 The chirality algebra [V].** From one geometric fact — the sign of λ — a coherent particle-like
algebra follows, each step computed: chirality `= sign λ = sign H` (the `±λ` pair are pure Weyl projections,
purity 1.0); the mirror operation maps `λ → −λ` and behaves structurally as **charge conjugation**; the
chiral angle satisfies `H = H_max cos 2θ_χ` (to <2%) — the internal `γ₅` rotation; and the **self-dual
`θ_χ = 45°` state is its own conjugate: the Majorana state**
(`chirality_helicity_check`, `majorana_selfdual_check`, `g2_dirac_structure_check`). *Tier honesty:* the
algebra is [V]; the *dictionary* to the QFT operators (this C is not literally `iγ²γ⁰`) is [S], stated
identically everywhere.

**6.3 Geometric existence and spectral exactness [credited]/[V].** The Beltrami field is the **Reeb field**
of a contact structure (Etnyre–Ghrist), so Taubes' proof of the Weinstein conjecture *guarantees a closed
field-line loop* — the coherent loop exists by topology. On S³ the curl spectrum yields an exact zeta,

```
ζ_B(s) = ζ(s−2) − ζ(s)   ⇒   ζ′(−2) = −ζ(3)/4π²      (verified to 10⁻²⁵)
```

resolving a π-power anomaly in the credited mass-tower literature (`curl_spectral_zeta_pi_power_check`).
The object's electromagnetic form is an **anapole**: the ordinary radiating dipole cancels to ~10⁻¹⁶ — a
nonradiating toroidal resonator (Zel'dovich; Afanasiev–Stepanovsky; Papasimakis)
(`oam_toroidal_resonator_resolution_check`). This nonradiation is load-bearing twice: it is why the object
can *hold* energy, and (Part V) why its later nuclear role is *confinement*, never the 24-MeV antenna.

## 7. The matter-wave reading [S] — and what it honestly earns

*Plain language: here is the central bet, labeled as a bet: that this object, at another scale, IS the
elementary particle — mass as trapped oscillation, spin as the knot, the quantum wave as the beat envelope.
The mathematics earns real pieces (the Dirac algebra, the de Broglie kinematics); the identification itself
stays a hypothesis; and the two most famous numbers (α, g−2's value) are handled by refusing to fake them.*

**7.1 The correspondence [credited].** Madelung (1927): writing `ψ = √ρ e^{iS/ħ}` turns the Schrödinger
equation into a compressible-fluid system — continuity plus Euler with a quantum (Bohm) pressure. The
object's own class. The in-repo simulation evolves the full nonlinear system and *measures* the matter-wave
kinematics: group velocity `v_g = c²k/ω`, rest clock `= ω_c`, and the de Broglie relation `v_g·v_p = c²`
(`engine/ftgb_resonator_sim.py`, run by the harness). The math is [V]; *the electron is this object* is [S].

**7.2 g = 2: the meaning derived, the lock diagnostic [V]/[S].** The internal algebra of §6.2 assembles into
the Dirac bispinor structure, and `g = 2` is what minimal coupling of that structure gives — reduced to one
internal condition: the `π₁` charge winding must **lock** to the `π₃` Hopf spin. The theory's own extended
soliton computes *composite* moments correctly (Skyrme quantization gives `μ_p/μ_n = −3/2`, ~3% of
experiment; g ≈ 5.59 — the nucleon), so `g = 2` is precisely the *elementary/pointlike limit*. Honestly put:
the lock's realization is *inferred from* the measured g-values — diagnostic, not yet predictive; an
independent test would be a computed `π₁–π₃` coupling on the eigenmode (`g2_dirac_structure_check`,
`g2_skyrme_composite_check`).

**7.3 α: typed, not derived — a settled-negative kept in full.** The tempting derivation ("the winding count
is 137") was executed and **killed**: the computed continuous winding of the object is `ι ≈ 1` (a Hopf
ring), not 137; 137 is prime; the near-misses are generic against control targets (an anti-numerology
denominator was run); and the running of α points the wrong way for a geometric fixed value. Three lenses
*correctly type* α (the exact vacuum-impedance identity `α = Z₀/2R_K`, the g−2 precession beat, the QED
cascade) — each a restatement, none a derivation. The frontier is reduced to one named quantity: the anchor
of the charge magnitude — the same "why is the electron elementary?" question `g = 2` marks
(`alpha_genericity_check`, `alpha_running`, `alpha_resonator_imbalance_check`; full assessment in
`results/ALPHA_RESOLUTION_ASSESSMENT_2026-09-10.md`).

**7.4 Mass and the neutrino.** The credited TUFT analytic-torsion dressing carries the mass hierarchy's
*order*; its ζ-value coefficients are exact and reproduced ([V]-arith). Fixing the single scale from the up
quark alone, the remaining **five quark masses come out as parameter-free *ratio* predictions**, 5/5 within
~1% of PDG (all within 0.5% of Nielsen's table) — while the knot↔generation identification map stays a
framework hypothesis, stated as such (`tuft_mass_tower_check`, `nielsen_mass_completion_check`).
The neutrino: the self-dual `θ_χ = 45°` state predicts **Majorana** — in *disagreement* with the credited
TUFT preprint's Dirac reading; `0νββ` experiments decide between them. A theory that names an internal
disagreement and its judge is doing its job.

---

# Part V — The nuclear program

*Plain language for the whole Part: the cold-fusion-adjacent literature reports a strange pattern — heat
correlated with helium-4, almost no neutrons, almost no gamma rays — which contradicts textbook hot fusion,
where deuterium burns ~50/50 into neutron and proton channels. This Part neither believes nor dismisses that
pattern. It asks: IF the pattern is real, what does established nuclear physics FORCE the mechanism to look
like — and what single computation would decide it? The answer, built step by verified step, is one geometric
corridor with one measurable knob. Nothing here computes a rate, proves LENR, or invents a nuclear force.*

## 8. From anomaly landscape to one pointed question

**8.1 The ledger [V].** If the heat is nuclear it is `d+d → ⁴He` at **23.847 MeV per atom** — exact AME2020
mass-defect arithmetic, conserved (`lenr_energy_ledger`). A COP > 1 is then a *nuclear source* (a per-event
quantum ~10⁴–10⁵× the eV-scale trigger), never over-unity — the first law holds, and the theory derives no
COP. The same arithmetic, harnessed, covers the reported transmutation channels: `Cs-133 + 4d → Pr-141` =
50.493 MeV and `Sr-88 + 4d → Mo-96` = 53.412 MeV, exactly baryon- and charge-conserving
(`transmutation_qvalue_arithmetic_check`) — bookkeeping only; mechanism [S]; rate open; and
baryon-conserving transmutation is kept strictly distinct from baryon decay (the object is a Hopfion,
`π₂`-degree 0 — **no** monopole catalysis; settled-negative).

**8.2 The disposal chain — converged [credited]/[V].** The γ-quietness has a structural *why*: no single
photon can mediate a `0⁺ → 0⁺` transition (there is no `L = 0` photon — Church & Weneser 1956), and the E1
radiative channel is isospin-forbidden at N = Z; the *measured* radiative branch is `~10⁻⁷`
[Wilkinson & Cecil, PRC 31, 2036 (1985)]. Therefore an aneutronic, γ-quiet ⁴He channel **must shed its
23.847 MeV collectively** — the disposal operator is **E0/collective** [credited; shared prior art:
Hagelstein, Preparata, Takahashi — credited by name]. Every escape route was computed shut, adversarially:
the anapole toroidal *dipole* is double-forbidden between `J = 0` states (Wigner–Eckart zero AND parity) —
so the anapole is the **active site** (slow confinement at assembly), never the antenna
(`disposal_e0_pair_fork_check`); neutrino-pair disposal is dead (weak, and escapes)
(`neutrino_disposal_nogo_check`); the momentum-clean `4d → 2α` exit is **(α,n)-excluded** — its secondary
neutrons land 3–8 orders *above* the observed dearth, a computed refutation of the TSC-class exit channel
(`aneutronic_disposal_fork_check`); and collective/superradiant enhancement is bounded by the
coherence-volume occupation `N_λ = n·λ̄³(E)` — order ONE at the hard 24-MeV rung (λ̄ = 8.2 fm), ~10⁷ only at
the soft optical end — so coherence helps the easy part of any cascade and not the bottleneck
(`disposal_coherence_volume_nogo_check`). If a localized hot ⁴He* compound ever forms, E0 internal-pair
conversion makes it *detectable* (~20 MeV e⁺e⁻, a 511 keV line, rate ~5×10¹¹ s⁻¹) — quiet heat and a hot
compound are mutually exclusive, which is itself a falsifier (§10, #5).

**8.3 The corridor — the open problem, sharpened to one question [V]-arith.** Two census/survival facts
force the shape of any surviving mechanism (`entrance_corridor_survival_check`):

1. **There is no ladder.** ⁴He has **zero bound excited states** — its first excited level (0⁺₂, 20.21 MeV)
   sits *above* the lowest breakup threshold (p+t, 19.815 MeV). Below breakup there is no rung to pause on;
   energy shedding must ride the moving assembly trajectory continuously.
2. **There is no slow lane above threshold.** Any dwell in the continuum above p+t decays at Γ ~ 0.5 MeV:
   half-life `≈ 9×10⁻²² s`. An attosecond of "slow assembly" up there survives as `e^{−760}` (a picosecond, `e^{−7.6×10⁸}`). Slowness exists
   only *below* threshold.

Therefore the **only γ-quiet, collective-disposal aneutronic route** is a **dissipative sub-breakup corridor** (the measured ~10⁻⁷ radiative branch is itself aneutronic but is not this route): the assembly must shed
the full 23.85 MeV *while it happens* — never pausing (no rungs), never crossing p+t (no survival). The
question "does that corridor exist on the fitted near-BPS energy surface?" *is* the open problem — one
geometric question where there had been a fog, and decidable either way (corridor excluded → the aneutronic
reading falls: a decisive settled-negative, which the discipline also counts as a win).

**8.4 Two bars and a derived fence [V]-arith.** The corridor carries its own success criteria, both from
data: **existence** — beat the measured `10⁻⁷` baseline; **sufficiency** — reproduce the observed neutron
dearth `n/⁴He ≤ 10⁻⁹`, which in the Landau–Zener bridge means `Γ_LZ ≥ ln(10⁹)/2π = 3.30`, i.e.
`Δ_suff = 5.47 × Δ_dominance`. Combining the sufficiency bar with the Cauchy–Schwarz ceiling
(`Δ = 23.85 MeV × ρ_eff`, `ρ_eff ≤ 1`) **derives a constraint on the crossing itself**:

```
β·|dF|  ≤  2π (23.85 MeV)² / (ħc · ln 10⁹)  =  0.874 MeV/fm
```

— *the data forces the crossing into the slow/soft corner* (a conditional result: it presumes the `[S]`
identification of d+d→⁴He-vs-breakup **as** an adiabatic Landau–Zener crossing, which is an FTGB hypothesis,
not established nuclear physics — the measured ~10⁻⁷ suppression is standardly the E1/isospin-forbidden
radiative channel), independently converging with the corridor's own slowness requirement
(`delta_b4_landau_zener_bridge_check` TEST 2b). The bridge also makes any future
Δ testable in both directions (forward: Δ → ⁴He/neutron ratio; inverse: measured ratio → effective Δ).

**8.5 Stage D — where the smallness cannot come from [V]-arith.** In the near-BPS Skyrme model the BPS
submodel's energy is exactly linear in baryon number, so compact B=4 and separated 2×B=2 are *degenerate*
and the branching gap Δ is **first-order** in the near-BPS perturbation — evaluated on *analytic* BPS
compactons (`cos(ξ/2) = r/R`, derived and machine-validated in-check). Executing that route returned three
results (`delta_b4_stageD_bps_overlap_check`):

1. *A scoping correction (the audit audited):* the first-order **L₂ energy log-diverges at the compacton
   boundary** (cutoff increments ≈ `2·ln10` per decade (the analytic log-divergence slope)) while the L₄ energy is finite (11.886,
   compacton units) — only the quartic piece is plain quadrature; the quadratic piece needs a
   boundary-layer-regularized scheme. The earlier "pure quadrature" scoping was corrected in print.
2. *A proxy bracket:* the density-geometry Franck–Condon overlap of the B=4 ball with the 2×B=2 dumbbell is
   **[0.55, 0.96]** across every crossing geometry (Cauchy–Schwarz-normalized, grid-converged).
3. *A structural constraint (the payoff):* the target regime needs `ρ_eff ~ 0.07`, and density-support
   geometry **cannot** produce it (floor 0.55). The suppression — if the aneutronic reading is right —
   must therefore live in **what the density proxy omits** — three co-equal candidates the check does not
   rank: the relative orientation / Finkelstein–Rubinstein phase structure of the crossing, the moduli-space
   metric, and the regularized-boundary (L₂) physics. Of these, the orientation/phase structure is the one the
   spin gate (§8.6) next makes computable, so the external run is *pointed*: resolve orientation space first.

**8.6 The gate — the quantum arithmetic of that space [credited]/[S].** The orientation space's quantum
version is exactly solvable (`spin_channel_gate_check`, spin-1 pair algebra built from operators):

- **The door.** The s-wave route to ⁴He(0⁺) is the **spin singlet alone** — 1 of the 9 d+d spin states
  (statistical gate **1/9**; among Bose-symmetric s-wave-allowed states, 1/6). S = 1 pairs only with odd L.
- **The steering.** A deuteron pair drawn from a *single condensate mode* `|1,m⟩` has singlet fraction
  **1/3 at m = 0** (three times statistical) and **exactly 0 at m = ±1** (pure quintet; the residual
  S = 2, L = 2 route is centrifugally suppressed, `(kR)⁴ ~ 1.3×10⁻⁶` at 240 eV). Coherent preparation
  moves the gate in *both* directions.
- **The thermal fence.** `μ_d B/kT ~ 10⁻⁶` at any plasmoid-scale field: Boltzmann polarization cannot set
  the gate — any channel selection must be **dynamical/coherent**. The cold Bose-degenerate seed
  (`n·λ³ ≥ 2.612`, the theory's standing [S] condition) thereby acquires a mechanism-shaped job:
  **channel preparation**.
- **The logged consistency (never promoted).** `1/9 × [0.55, 0.96] = [0.061, 0.107]`, overlapping the
  `ρ_eff ~ 0.06–0.08` target band — three independently-sourced pieces (textbook statistics, the computed
  density proxy, the LZ band) meeting at one decade. Coincidence-class, logged in the ledger with the
  wide-band caution, because the proxy has named omissions and the band's own provenance is flagged.

**8.7 The chain, and what remains.** *Corridor* (where) → *fence* (how fast) → *gate* (what selects) →
*seed* (what prepares) → *knob* (how to test, §10 #9). Open, exactly: (i) the orientation-resolved
near-BPS crossing computation (external, now pointed, with the regularization requirement stated); (ii) the
laboratory polarization test. Everything else in the landscape is decided in-environment and tiered.

---

# Part VI — Confrontation, falsifiers, and limits

## 9. Settled-negatives — the results that are refutations

*Plain language: these are computations that killed attractive ideas. They are kept on purpose: each one
fences the theory against its own most tempting failure modes, and several are publishable results in
their own right.*

1. **α from winding** — computed `ι ≈ 1`, not 137; genericity control run; dead as a derivation.
2. **The literal kHz = MeV identity** — dead by 16.8 orders; every nuclear-internal scale sits 7.5–17.6
   orders above the beat.
3. **The beat as pump** — doubly closed (parametric 15.7 orders short; crossing frozen/DC, `10⁻¹⁸`).
4. **GHz/THz beat-modulated tunneling** — the salvaged campaign's "coherence gain 1.334" fence-killed; its
   artifact internally inconsistent by ~82 orders (a caught error, vendored with its confrontation).
5. **Direct phonon-nuclear coupling** — dead by ~66 orders.
6. **Monopole catalysis** — the object is a Hopfion (`π₂`-degree 0); no Callan–Rubakov channel.
7. **TSC-class 4d → 2α exits** — (α,n)-excluded, 3–8 orders above the neutron dearth; a named prior-art
   confrontation.
8. **Neutrino-pair disposal** — weak and escaping; dead.
9. **Coherence-volume enhancement at the hard rung** — `N_λ = O(1)` at 24 MeV; the enhancement lives only
   at the soft end.
10. **Supra-threshold slow dwell** — zeptosecond survival; slowness exists only sub-threshold.
11. **Sub-threshold state ladders** — ⁴He has no bound excited states; there is nothing to pause on.
12. **Static 4-current closure** — requires `|B| = const`, impossible for nontrivial force-free fields (the
    theory's own flagship identification, fenced by its own theorem).
13. **PV-gravity levitation / propulsion** — the polarizable-vacuum reading is GR-equivalent (solar redshift
    reproduced) and attractive for all positive mass; a levitating well requires negative mass-energy, so no
    propulsion/anti-gravity/over-unity follows (`pv_gravity_no_propulsion_check`).

## 10. The falsifier set (with protocols)

1. **Comb fingerprint** — inharmonic `1 : 1.72 : 2.43` in the linear-drive limit; harmonic `1:2:3` kills
   the Beltrami-carrier reading. Geometry stated (ball limit; torus doublet split computed).
2. **kHz beat + second-order detuning** (coil + FFT); the beat is a rate-gate, never a pump.
3. **Neutron yield ∝ heat** — the primary, band-independent kill of the aneutronic channel.
4. **He-4/heat ≠ 24 MeV/⁴He** — kills the energy-ledger reading (Miles' correlation is the confronting
   measurement, held as measurement, not authority).
5. **E0 internal-pair secondary** — ~20 MeV e⁺e⁻ / 511 keV if a localized hot compound forms; quiet heat
   and a hot compound are mutually exclusive.
6. **`0νββ` null** — kills the Majorana prediction (and decides the internal TUFT disagreement).
7. **Beat-locked yield steps** `f_b(L) = N^L` — with the salvaged control protocol: a real step survives
   ±10% drive (<30% variation) and **dies under phase scrambling** (else artifact). The one existing
   beat-sweep dataset (HLC 2010; a Pd-D lattice, the wrong object) fits neither `N^L` nor CK — logged.
8. **FWM sidebands** at `1.517 f₁`, `1.820 f₁` — decide the phase-conjugation role.
9. **Polarization-steered aneutronic yield** (new) — m=0/singlet-weighted assembly enhances up to 3×;
   m=±1 polarization collapses the s-wave door toward the ~10⁻⁶ d-wave floor. No thermal-statistical
   model predicts a spin knob. Context: spin-polarized fusion is real physics (Kulsrud et al. 1982); the
   d+d quintet-suppression question is named and contested — this theory adds the coherent-site,
   preparation-steered version.

## 11. Limits, threats to validity, and what is never claimed

**11.1 Never claimed.** No over-unity (COP > 1 is nuclear-sourced; no COP derived). No levitation, thrust, or
anti-gravity — and this is not a mere abstention: the polarizable-vacuum (`K_PV`) gravity reading the project
carries (M11; `K_PV = exp(2GM/rc²)` [credited: Puthoff]) was *computed* and returns a **settled-negative**
(`pv_gravity_no_propulsion_check`): it is GR-equivalent at weak field (it reproduces the solar redshift
`2.12×10⁻⁶`), its index well is attractive for every positive mass, and a repulsive/levitating well would
require negative mass-energy — so the object's own positive field energy gravitates normally and licenses no
propulsion. No new nuclear mechanism, rate, cross-section, or matrix element. Not α's value; not exact mass
ratios. Baryon-conserving ≠ baryon decay, always.

**11.2 Threats to validity, stated against ourselves.** (i) The central identifications (electron = object;
active site = object) are [S] and could simply be false — every downstream [S] falls with them, while the
[V] core stands independently as plasma mathematics. (ii) The physical plasmoid lives *outside* the
proven Hall-regularity regime (`d_i > R`, computed) — the regularity theorems cover the coherent state and
its driven neighborhood, not the full physical corner. (iii) The Stage-D bracket is a *proxy* with named
omissions (orientation structure, moduli metric, the divergent boundary piece); the three-piece consistency
is coincidence-class by construction. (iv) The confronting experimental record (Miles' correlation, the
neutron dearth, HLC) is contested, scattered, and partially anecdotal; the theory treats it as *data to
explain if real*, weighted against null results (Berlinguette 2019), never as authority. (v) Absolute
magnitudes carry the `v_A` band; only dimensionless ratios are load-bearing (proven invariant).

**11.3 The audit record (method as result).** The project audits itself with multi-lens adversarial passes,
and keeps the score: the 2026-09-14 six-dimension audit produced 49 findings, of which the load-bearing
ones were fixed, several were *refuted in the repository's favor* (including a citation accusation
disproven against the original paper), and two of the audit's own claims were later corrected *by
computation* (the Stage-D "pure quadrature" scoping; a "too defeatist" scoping corrected upward). The
discipline is symmetric or it is nothing.

---

# Part VII — The program, the convergence spine, and the one coherence

## 12. Where the theory meets data: the convergence ranking and the four legs

*Plain language: this Part steps back from the individual results to show the shape of the whole — an honest
ranking of where the theory is strong versus weak against real data, the four practical ambitions the
verified core actually organizes, and the single physical idea that runs through all of it.*

**12.1 The convergence ranking (strongest → weakest, stated against ourselves).** The theory's contact with
data is not uniform, and the project ranks it honestly (resolution map §2): **(1) strongest** — the conserved
`23.847 MeV` `d+d→⁴He` ledger `[V]` plus the `E0` collective-disposal requirement `[credited]`, which meets
the heat/helium and γ-quiet signatures structurally; **(2) strongest object, `[S]` interface** — the driven
Beltrami attractor (Re 126→628) and the N-mode Woltjer theorem, meeting the SAFIRE/plasmoid self-organization
as a re-description of Woltjer–Taylor; **(3) consistent but non-discriminating** — baryon-conserving `ΔA=4n`
transmutation, whose Q-values are exact `[V]`-arith but which any ⁴He-transfer would reproduce; **(4) strong
`[V]` fingerprint with zero data to meet** — the CK inharmonic comb, the cleanest falsifiable prediction, as
yet untested by an appropriate object; **(5) weakest, mostly re-description** — the anapole reactive-EMF ↔
Aureon/LEC heat-to-electricity thread, `[S]`/open, overlapping Preparata/Del Giudice coherent-domain prior
art. A theory that publishes its own strength gradient is easier to falsify at its weak points, which is the
intent.

**12.2 The four legs (the verified core mapped onto the project's ambitions).** The same object organizes
four practical programs, each carried at its earned tier:

- **A. Matter-wave synthesis** (the particle rung) — the internal Dirac algebra, g=2's meaning, and the
  chirality/C/Majorana cluster are `[V]`; the *electron = object* identification is `[S]`, killed by a `0νββ`
  null. The next in-env move is a computed `π₁–π₃` coupling to make the g=2 lock predictive.
- **B. Coherent energy transformation** (heat → collective EM) — the honest chain: nuclear-sourced energy
  `[V]` → must shed collectively (E0, `[credited]`) → *if* it couples into the anapole's nonradiating
  near-field mode, a reactive EMF `V = ω_b·ΔΦ` follows `[S]`, confronting the LEC 525 mV and Mizuno-2025 EMF
  data. The magnitude `V` is an untagged order-of-magnitude — the ranked in-env backlog item (an EM
  derivation needing one declared junction geometry). Kill: no drive/beat dependence of the EMF.
- **C. Transmutation** (baryon-conserving `ΔA=4n`) — arithmetic harnessed `[V]`; mechanism `[S]`; rate behind
  the same corridor as leg A's nuclear rung. Discriminator: ¹⁶³Dy→¹⁶³Ho ionization-gated β⁻.
- **D. EVO / SAFIRE / plasmoid engineering** — the strongest original `[V]` object (the driven Beltrami
  attractor) plus the two spectral discriminators (the CK comb; the `f_b(L)=N^L` beat-lock, with its
  phase-scramble control) — both with zero experimental convergence, live targets.

**12.3 The fences, computed.** No over-unity (COP nuclear-sourced; no COP derived). No new nuclear mechanism.
And no levitation/anti-gravity/propulsion — not by abstention but by **computation**: the polarizable-vacuum
gravity reading is GR-equivalent and its index well is attractive for all positive mass, so a levitating well
would require negative mass-energy (`pv_gravity_no_propulsion_check`, §11.1). The program is falsifiable
architecture — bars, fences, discriminators, one named external computation, one experimental knob — never a
claim of proven power.

## 13. The one coherence, and conclusion

*Plain language: the deepest unifying idea — one physical property, coherence, doing three different jobs at
three different scales, which is why a single object can be a stable plasma, a matter wave, and a nuclear
active site at once.*

**One coherence, three roles.** The organizing thread is that a single property — the object's *coherence* —
recurs, computed, at three scales. As the **force-free Beltrami state** it *is* regularity: the self-advection
nonlinearity is null, so the object cannot blow up (§4). As the **matter-wave** it is the phase coherence of
the Madelung fluid that lets the wave stand as a soliton (§7). And as the **nuclear active site** it is the
single-mode condensate coherence that prepares the spin channel — steering the singlet gate the corridor's
selectivity requires (§8.6). These are not three coincidences but one property read at plasma, particle, and
assembly scales; the chirality cluster (§6.2) is the same unification in the language of sign λ — one `±λ`
self-dual object giving both the Woltjer–Taylor plasmoid coherence and the lepton chirality/Majorana content.

**Conclusion.** One object, four measured anchors, one labeled selection. A verified mathematical core in
which coherence and regularity are the same fact; a driven heartbeat forced by a linear program; a computed
topology and chirality structure reaching to the edge of the Dirac algebra; and a nuclear anomaly landscape
converted — by census, survival, bridge, bracket, and gate arithmetic, every step re-runnable — into one
pointed geometric question with two data bars, one derived fence, and one experimental knob. The theory's
strongest property is not any single claim but the *auditability of the whole*: every claim wears its tier,
every tier has its script, every dead end is kept, and the reader is never asked to trust — only to run.

---

## References (key set; full tiered bibliography in `REFERENCES.md`)

**Foundations.** Chandrasekhar & Kendall, ApJ **126**, 457 (1957) · Woltjer, PNAS **44**, 489 (1958) ·
Taylor, PRL **33**, 1139 (1974) · Moffatt, JFM **35**, 117 (1969) · Trkal (1919; Trkalian exact flows) ·
Beale, Kato & Majda, CMP **94**, 61 (1984) · Etnyre & Ghrist, Nonlinearity **13**, 441 (2000) · Taubes
(Weinstein conjecture, 2007) · Zel'dovich (anapole); Afanasiev & Stepanovsky, J. Phys. A **28**, 4565
(1995) · Papasimakis et al., Nat. Mater. **15**, 263 (2016).

**Matter wave & topology.** Madelung, Z. Phys. **40**, 322 (1927) · Finkelstein & Rubinstein, JMP **9**,
1762 (1968) · Wilczek & Zee, PRL **51**, 2250 (1983) · Adkins, Nappi & Witten, NPB **228**, 552 (1983) ·
Battye & Sutcliffe, PRL **79**, 363 (1997) · Barnes, Baskerville & Turok, PRL **79**, 367 (1997) [B=4
normal modes; attribution verified against the original] · Houghton, Manton & Sutcliffe, NPB **510**, 507
(1998).

**Near-BPS and nuclear.** Adam, Sánchez-Guillén & Wereszczyński, Phys. Lett. B **691**, 105 (2010) [arXiv:1001.4544] · Adam, Naya,
Sánchez-Guillén & Wereszczyński, PRL **111**, 232501 (2013) · Speight, J. Geom. Phys. **92**, 30 (2015) [arXiv:1406.0966] · Church &
Weneser, Phys. Rev. **103**, 1035 (1956) · Wilkinson & Cecil, PRC **31**, 2036 (1985) · Tilley, Weller &
Hale, NPA **541**, 1 (1992) [A=4 evaluation] · AME2020: Wang et al., Chin. Phys. C **45**, 030003 (2021) ·
Kulsrud, Furth, Valeo & Goldhaber, PRL **49**, 1248 (1982) · Landau (1932); Zener (1932).

**Confronting measurements (held as measurements).** Miles et al. (He/heat correlation) · Hagelstein, Letts
& Cravens, JCMNS (2010) [THz beat sweep; logged non-match] · Berlinguette et al., Nature **570**, 45
(2019) [null result, weighted] · credited prior-art traditions: Hagelstein; Preparata; Takahashi; Kim;
Shoulders (EVO); each credited at its point of contact, none used as authority.

*No claim exceeds its tier; no number is fabricated; settled-negatives are kept as wins; the discipline is
symmetric. Everything above re-runs from one command: `python results/verify/verify_all.py` → 85/85.*
