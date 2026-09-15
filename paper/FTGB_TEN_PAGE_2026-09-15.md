# The Coherent Object: a driven Beltrami–Hopf toroidal soliton read as field and matter wave

**A reproducible, tiered theory — the ten-page presentation.**
Nathaniel Hanks · 2026-09-15 · reproduce: `pip install -r requirements.txt && python results/verify/verify_all.py` → **87/87**, deterministic, no network, CI-gated.
Complete 25-page version: `paper/FTGB_FULL_PAPER_25PG_2026-09-15.md` · longform: `FTGB_GRAND_SYNTHESIS.md` · per-claim ledger: `results/TIER_LEDGER.md` · visuals: `gallery.html`.

---

## Abstract

One geometric object — a driven, force-free **Beltrami eigenmode** `∇×B = λB` on a torus, carrying Hopf-linked
field lines — is read simultaneously as a *plasma structure* (the plasmoid / ball-lightning / EVO family) and,
through the Madelung correspondence, as a *matter wave*. Everything traces to four measured anchors
`{B, n_i, m_i, R}` plus one structural selection (`ε = a/R = 1/φ`), with zero fitted parameters. The theory is
presented under a strict honesty discipline: every claim carries a tier — **[V]** verified by a named,
re-runnable script; **[credited]** established physics built upon; **[S]** falsifiable structural hypothesis;
**settled-negative** a computed dead end kept as a result — and no number is ever fabricated. The verified core
contains an exact global-regularity statement ("coherence *is* regularity"), a driven stable attractor swept
across Reynolds number, an inharmonic spectral fingerprint, computed topology and chirality structure, and a
nuclear energy ledger. The one open nuclear problem has been converged, by a chain of adversarially verified
computations, to a single geometric question — the **entrance-channel assembly corridor** — carrying two data
bars, a derived constraint on the crossing, and a new experimentally accessible falsifier (polarization-steered
aneutronic yield). The theory does not prove LENR, derives no COP, and claims no new nuclear mechanism: it
converts a scattered anomaly landscape into one falsifiable program.

---

## 1. Method: the honesty discipline is the instrument

*Plain language: before any physics, the rule-set. Every claim in this theory wears a label saying exactly how
much it has earned, and every labeled claim can be re-run by a stranger with one command.*

Claims are tiered **[V]** / **[credited]** / **[S]** / **[flag]** / **settled-negative**, and the tier travels
with the claim into every document, interactive, and rendered figure. Three practices distinguish the project:
(i) **settled-negatives are wins** — a computed refutation is kept, cited, and celebrated (thirteen — fully enumerated in the 25-page paper §9);
(ii) **coincidences are computed and logged, never promoted** (`results/COINCIDENCE_LEDGER.md`); (iii) **the
discipline is symmetric** — under-claiming is policed as hard as over-claiming, and this week's record includes
corrections in both directions, including two of the project's own audit findings refuted by computation.

## 2. The object

*Plain language: take a magnetized plasma and let it relax. It settles into the one shape where the field's
own current runs exactly along the field — a "force-free" state. On a torus, that state rings like a bell,
holds its knots, and — the central claim — it cannot tear itself apart, because at that state the tearing
term in the equations is identically zero.*

The force-free (Beltrami) state `∇×B = λB` is the minimum-energy state of a plasma at fixed magnetic helicity
`H = ∫A·B` [Woltjer 1958; Taylor 1974; Moffatt 1969]. On the ball, its spectrum is fixed by the
Chandrasekhar–Kendall boundary quantization `tan x = x` [Chandrasekhar & Kendall 1957], with roots
`x_n = 4.4934, 7.7253, 10.9041…` — an **inharmonic comb** with ratios `1 : 1.719 : 2.427`, which at the
measured anchors lands at `{121, 208, 294}` kHz. FTGB takes this state as a *driven physical object*: a
dissipative, toroidal, Hopf-knotted standing wave with a beat rhythm (a "heartbeat," because a fixed-helicity
energy minimization over N modes is a linear program whose optimum is always one mode — a beat-carrying object
can never be static; it must be driven `[V]`).

## 3. The verified core

*Plain language: everything in this table is a mathematical statement a script checks every time the repository
is touched. If any line failed, the badge on the front page would turn red.*

| Result `[V]` unless noted | Statement | Script |
|---|---|---|
| Coherence **is** regularity | at Beltrami the Lamb vector `u×ω = 0` pointwise → advection is a pure gradient → `u(t)=e^{−νλ²t}u₀` is an exact eternal smooth solution (class credited to Trkal 1919); Beale–Kato–Majda never triggers | `exact_beltrami_regularity_check` |
| Driven & attracting | forced with `f = νλ²u_B` it is an exact steady state AND a stable attractor, swept **Re 126→628** with attraction not weakening | `r2_driven_beltrami_attractor_check`, `r2_reynolds_sweep_check` |
| The CK comb | `tan x = x` ratios `1:1.719:2.427` (linear-drive limit; Duffing pull separable — M16); spherical-boundary geometry stated | `ck_eigenvalues_check`, `duffing_backbone_check` |
| Heartbeat theorem | N-mode fixed-helicity minimization = an LP with a single-mode optimum → driven or dead | `nmode_woltjer_lp_check` |
| Current-leg trilogy | static 4-current closure ⇔ `\|B\|=const` — impossible for nontrivial force-free fields (the flagship structural no-go) | `currentleg_trilogy_check` |
| Topology | idealized-reference Hopf `Q_H=1`, wave-mode Chern `C=±2`; the actual CK object carries real `H≈0.088` (honestly not an integer) | `topology_invariants_check` |
| Chirality cluster | chirality `= sign λ = sign H`; mirror = C-structure; self-dual `θ_χ=45°` = Majorana (algebra [V]; QFT dictionary [S]) | `majorana_selfdual_check`, `g2_dirac_structure_check` |
| Spectral zeta | exact `ζ_B(s) = ζ(s−2) − ζ(s)` on S³ ⇒ `ζ′(−2) = −ζ(3)/4π²` (to 1e-25) | `curl_spectral_zeta_pi_power_check` |
| Anapole form | the ordinary dipole cancels (~1e-16): a nonradiating toroidal resonator [Zel'dovich; Afanasiev–Stepanovsky 1995] | `oam_toroidal_resonator_resolution_check` |
| Nuclear ledger | `d+d→⁴He` = 23.847 MeV, conserved; transmutation Q-values (Cs→Pr 50.493, Sr→Mo 53.412 MeV) exact AME2020 arithmetic | `lenr_energy_ledger`, `transmutation_qvalue_arithmetic_check` |
| Rhythm layer | Kuramoto N=800 onset P=1.20; Aizawa λ_max=0.094>0 (chaotic boundary); beat = a nonlinear/energy observable | `multibody_sync_capture_check`, `rhythm_parametric_resonance_check` |

**The settled-negatives (kept as results):** α from winding (ι≈1, not 137); the literal kHz=MeV identity (dead
by 16.8 orders; the pump reading doubly closed); direct phonon-nuclear coupling (~66 orders); monopole
catalysis; GHz/THz beat-modulated tunneling (the pre-jewel campaign's claim, fence-killed with its artifact's
internal inconsistency caught); TSC-class 4d→2α exits ((α,n)-excluded — a named confrontation with prior art);
supra-threshold slow dwell (zeptosecond survival); sub-threshold state ladders (⁴He has no bound excited
states); neutrino disposal; coherence-volume enhancement at the hard rung; and PV-gravity levitation (the polarizable-vacuum reading is GR-equivalent, so a levitating well needs negative mass — no propulsion/over-unity).

## 4. The matter-wave reading `[S]`

*Plain language: the central bet — that this same object, at a different scale, IS the electron: its mass a
trapped oscillation, its spin the knot, its quantum wave the beat envelope. The math earns real pieces of this;
the identification itself remains a hypothesis and is labeled as one.*

Via Madelung [1927], `ψ = √ρ e^{iS/ħ}` reads Schrödinger as a fluid — the object's own class. The software
simulation reproduces the kinematics (`v_g v_p = c²`, rest clock `= ω_c`) `[V-sim]`. The internal algebra
delivers the Dirac structure: the `±λ` pair = Weyl chiralities, `θ_χ` = the `γ₅` rotation, mirror = C, Hopf =
spin-½ [Finkelstein–Rubinstein 1968; Wilczek–Zee 1983] — so **g = 2's meaning is derived internally**, reduced
to one condition (the `π₁/π₃` charge-spin lock), which itself remains `[S]` and diagnostic. α is correctly
*typed* by three independent lenses but its value is **not derived** (settled-negative kept); the mass
hierarchy's *order* is derived in the credited TUFT dressing with values at framework tier. The Majorana
prediction (`θ_χ = 45°` self-dual) is falsifiable by a `0νββ` null.

## 5. The nuclear program: from anomaly landscape to one pointed question

*Plain language: the LENR literature reports heat correlated with helium, almost no neutrons, and almost no
gamma rays — an apparent contradiction with textbook fusion. This section is the program that either explains
that pattern or kills the explanation. It claims no new nuclear force and computes no reaction rate. What it
has done is squeeze the entire question, step by verified step, into one geometric corridor with one
measurable knob.*

**The ledger and the operator `[V]`/`[credited]`.** If the heat is nuclear it is `d+d→⁴He` at 23.847 MeV per
atom, conserved — a nuclear *source*, never over-unity. No single photon can carry a `0⁺→0⁺` transition
(Church & Weneser 1956), and the E1 channel is isospin-forbidden (N=Z) — measured branching ~`1e-7`
[Wilkinson & Cecil, PRC **31**, 2036 (1985)]. So γ-quiet ⁴He heat **must shed collectively** (operator = E0 /
collective; shared prior art: Hagelstein, Preparata, Takahashi — credited). The anapole knot is the **active
site** (slow confinement at assembly), *not* the energy antenna — a toroidal dipole is double-forbidden
between `J=0` states.

**The corridor (the sharpened open problem).** ⁴He has **no bound excited states** (first excited 0⁺₂ at
20.21 MeV sits *above* the p+t threshold at 19.815), so no state-ladder exists below breakup; and any dwell
*above* threshold dies in `t_½ ≈ 9×10⁻²² s`. Therefore the only γ-quiet, collective-disposal aneutronic route is a **dissipative
sub-breakup corridor**: the assembly must shed the full 23.85 MeV *while it happens*, never pausing, never
crossing p+t (`entrance_corridor_survival_check`). Two data bars travel with it — *existence*: beat the
measured `1e-7`; *sufficiency*: the observed dearth `n/⁴He ≤ 1e-9`, which is `Δ_suff = 5.47×` the dominance
threshold and, with the Cauchy–Schwarz ceiling `Δ = 23.85 MeV × ρ_eff ≤ 23.85 MeV`, **derives a constraint**:
`β·|dF| ≤ 0.874 MeV/fm` — *the data itself forces the crossing into the slow/soft corner* (conditional on the
`[S]` identification of d+d→⁴He-vs-breakup as an adiabatic Landau–Zener crossing — an FTGB hypothesis, not
established nuclear physics).

**Stage D (where the smallness cannot come from).** On the analytic BPS compacton (`cos(ξ/2) = r/R`;
Adam–Sánchez-Guillén–Wereszczyński 2010), first-order perturbation theory is *half*-tractable — the L₂ piece
log-diverges at the compacton boundary (computed; a known near-BPS subtlety), the L₄ piece is finite — and the
density-geometry overlap of the B=4 ball with the 2×B=2 dumbbell is **[0.55, 0.96]** at every crossing
geometry. Since the target regime needs `ρ_eff ~ 0.07`, **density geometry cannot supply the suppression: it
must live in what the density proxy omits — orientation/phase structure, the moduli metric, and the
regularized L₂-boundary physics** (`delta_b4_stageD_bps_overlap_check`).

**The gate (the quantum arithmetic of that space).** The s-wave door to ⁴He(0⁺) is the **spin singlet alone**
— 1 of 9 d+d spin states (statistical gate 1/9). And the gate is **steerable**: a deuteron pair drawn from a
single condensate mode `|1,m⟩` has singlet fraction **1/3 at m=0** and **exactly 0 at m=±1** (pure quintet;
the d-wave residual is `(kR)⁴ ~ 1e-6`). Thermal polarization is `~1e-6` at any plasmoid-scale field, so
channel selection must be *dynamical/coherent* — giving the cold Bose-degenerate seed (`n·λ³ ≥ 2.612`, the
jewel's standing `[S]` condition) a mechanism-shaped job: **channel preparation** (`spin_channel_gate_check`).
Logged as coincidence-class, never promoted: `1/9 × [0.55, 0.96] = [0.061, 0.107]`, overlapping the
`ρ_eff ~ 0.06–0.08` target band — three independently-sourced pieces meeting at one decade.

**The chain, end to end:** *corridor* (where) → *β·|dF| fence* (how fast) → *orientation gate* (what selects)
→ *coherent seed* (what prepares) → *polarization knob* (how to test). What remains open is exactly two
things: the orientation-resolved near-BPS run (external, now pointed), and the laboratory knob below.

## 6. Falsifiers — how to kill it

*Plain language: a theory is only as good as the experiments that could break it. These are the nine, most
with no free parameters.*

1. **Comb fingerprint** — inharmonic `1:1.72:2.43` in the linear-drive limit; a harmonic `1:2:3` comb kills
   the Beltrami-carrier reading (spherical-boundary geometry stated; torus shifts computed).
2. **kHz beat + second-order detuning** (a rate-gate, never a pump).
3. **Neutron yield ∝ heat** — the primary, band-independent kill of the aneutronic channel.
4. **He-4/heat ≠ 24 MeV/⁴He** — kills the energy ledger reading [Miles].
5. **E0 internal-pair secondary** — ~20 MeV `e⁺e⁻` / 511 keV if a localized hot compound forms.
6. **`0νββ` null** — kills the Majorana prediction (and decides against the credited TUFT-Dirac reading).
7. **Beat-locked yield steps `f_b(L)=N^L`** — with the salvaged control protocol: a real step survives ±10%
   drive and **dies under phase scrambling**.
8. **FWM sidebands** at `1.517 f₁`, `1.820 f₁`.
9. **Polarization-steered aneutronic yield** (new): m=0/singlet-weighted assembly enhances up to 3×; m=±1
   polarization collapses the s-wave door. No thermal-statistical model predicts a spin knob
   [context: Kulsrud et al., PRL **49**, 1248 (1982); the contested d+d quintet-suppression question].

## 7. What is never claimed

No over-unity, ever — COP > 1 is nuclear-sourced and the first law holds; no COP is derived. No levitation or
thrust — no force balance is computed, so none is claimed. No new nuclear mechanism is demonstrated; no rate,
cross-section, or matrix element is fabricated — the open numbers (`ρ_eff`, the corridor, the EMF magnitude)
are *named as open*. α's value and the exact mass ratios are not derived. Baryon-conserving transmutation is
kept strictly distinct from baryon decay.

## 8. Reproducibility & provenance

One command reproduces the entire model (87 checks: 84 theory scripts + 3 engine runs), deterministic and
offline, gated by CI on every push. Canonical numbers are re-derived in-repo from cited anchors; external data
(AME2020 masses, TUNL levels, measured screening) is vendored with named provenance; the absolute-magnitude
caveat (`v_A` band) is quarantined by proof (dimensionless observables invariant to 1e-16). Confronted
artifacts from salvaged pre-jewel material are vendored with their fence status. The visual layer carries the
same discipline: every rendered figure has a `.meta.json` sidecar naming its tier and verify scripts — the
tier travels with the pixel.

## Key references

Chandrasekhar & Kendall, ApJ **126**, 457 (1957) · Woltjer, PNAS **44**, 489 (1958) · Taylor, PRL **33**, 1139
(1974) · Moffatt, JFM **35**, 117 (1969) · Beale–Kato–Majda, CMP **94**, 61 (1984) · Madelung, Z. Phys. **40**,
322 (1927) · Finkelstein & Rubinstein, JMP **9**, 1762 (1968) · Wilczek & Zee, PRL **51**, 2250 (1983) ·
Etnyre & Ghrist, Nonlinearity **13**, 441 (2000) · Church & Weneser, Phys. Rev. **103**, 1035 (1956) ·
Wilkinson & Cecil, PRC **31**, 2036 (1985) · Barnes, Baskerville & Turok, PRL **79**, 367 (1997) ·
Adam, Sánchez-Guillén & Wereszczyński, Phys. Lett. B **691**, 105 (2010) [arXiv:1001.4544] · Adam–Naya–Sánchez-Guillén–Wereszczyński,
PRL **111**, 232501 (2013) · Kulsrud, Furth, Valeo & Goldhaber, PRL **49**, 1248 (1982) · Miles et al.
(He/heat correlation, as measurement) · full tiered bibliography: `REFERENCES.md`.

*No claim exceeds its tier; no number is fabricated; settled-negatives are kept as wins; the discipline is
symmetric. Everything above re-runs from one command.*
