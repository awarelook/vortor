# The Coherent Object — FTGB modeler & synthesis bundle

**Author:** Nathaniel Hanks · **A self-contained package:** one interactive modeler + the two
manuscripts + the method toolkit + two execute-ready hand-off packages.

> One driven, force-free Beltrami–Hopf toroidal soliton, built up from a point → a string →
> a resonator → a knotted field → driven dynamics, and read at once as a *field* and a
> *matter wave*. Every claim carries an honest tier; the mathematics is shown with its
> plain-language translation and every symbol labelled.

---

## Open it (no install, any OS)

Every model is a single self-contained HTML file — **double-click it**. Each runs in any
modern browser on **Windows, macOS, Linux, iOS, or Android** with no server and no
dependencies (all CSS/JS inlined, all animation hand-rolled on `<canvas>`). Start with
`index.html`; the other three go deeper on one facet each.

- **`index.html`** — the coherent-object modeler. Five stages (point → string → resonator →
  knotted field → driven dynamics) animate the mathematics live; drag the sliders to drive
  the oscillator, tune the comb coupling, climb the eigenmode ladder, spin the torus, and
  raise the E·B drive.
- **`resonator_family.html`** — one driven resonator, the whole family. Sweep the drive
  frequency and watch the *same* object become vacuum, neutrino, electron, EVO, and nucleon,
  with the mass following live from `m = ħω/c²`.
- **`soliton3d.html`** — the Beltrami–Hopf soliton in three spatial axes plus a fourth axis
  of phase/time: the whirl clock and the √2 heartbeat made visible on the torus.
- **`dynamics_lab.html`** — a live nonlinear-dynamics bench: three of the theory's governing
  equations integrated in real time (Stuart–Landau heartbeat, Kuramoto/Adler comb-pull, and
  the driven current-leg scalar `S(t)` whose closure the object fails to select on its own).

Prefer a hosted view? Each model is also a shareable web artifact (see the links you were
given when they were published).

## What's in the bundle

| File | What it is |
|---|---|
| `index.html` | **the interactive modeler** — point → string → resonator → knotted field → dynamics (native-open, cross-OS) |
| `resonator_family.html` | the unified object at five resonance conditions (vacuum / neutrino / electron / EVO / nucleon) |
| `soliton3d.html` | the toroidal soliton in 3D + a phase/time axis |
| `dynamics_lab.html` | live fixed-step integration of the governing nonlinear equations (now incl. CH-04 vacuum beat spectrum) |
| `electron.html` | the electron rung as a torsion defect — precession = charge, whirl = 1/α, chirality → electron / positron / neutrino |
| `coherence.html` | the interactive coherence stack — the 8 layers and 5 shared-invariant threads of the one object, click-to-open |
| `FTGB_GRAND_SYNTHESIS_FULL_2026-09-09.pdf` | **the compiled jewel as one shareable paper** (~59 pp): synthesis + trilogy + the 2026-09-09 advances (R2/R3, LENR model, electron/α) + glossary/references. Built via `paper/` (pandoc → Chrome print) |
| `FTGB_GRAND_SYNTHESIS.{md,pdf}` | the full tiered synthesis manuscript (Parts A–G, ~16.8k words) — **the large text with all the math** |
| `FTGB_CURRENTLEG_TRILOGY.{md,pdf}` | the standalone lead result (a self-contained plasma / topological-fluid theorem) |
| `FTGB_LEAD_PAPER_2026-09-09.pdf` | **the journal-length lead paper** (6 pp): the current-leg no-go trilogy + the R2/R3 conditional enstrophy/BKM closure — the defensible `[V]` core, ready to submit. Source `paper/LEAD_PAPER_2026-09-09.md` |
| `FTGB_COHERENCE_MAP_2026-09-09.md` | the capstone: the 7-layer stack ordering all frameworks (Buckingham-Π, EGM, TUFT, Reed, Ginzburg) theory → reality → experiment |
| `MATH_TOOLKIT_BASE.md` | **the shared foundation** the eight modules rest on — Beltrami/CK curl eigenproblem (§1), helicity/Woltjer-Taylor (§4), the *one operator → three readings* (plasma ‖ Madelung matter-wave ‖ `K_PV` vacuum) + topology (§9); honesty-tiered, numerology quarantined |
| `foundation/30_CANONICAL_NUMBERS.md` | the single source of truth for the canonical anchors `{B, n_i, m_i, R}`, `c_CK`, and the {121, 208, 294} kHz comb (§A/§C/§I) — residuals flagged, excisions pointed to the ledger |
| `TOOLKIT_HANDBOOK.md` | plain-language + math handbook tying the eight method modules together (and to the base above) |
| `toolkit/` | the eight method modules: Buckingham-Π (M7), QWM conversion (M8), coupled-oscillator substrate (M9), topological-soliton methods (M10), EGM / polarizable-vacuum spectral methods (M11), Ginzburg spiral-field theory (M12), **Nielsen TUFT mass-tower (M13)**, **Greenyer beat-law & EVO cascade (M14)** — the last two folded from the corpus gap-scan, honestly flagged |
| `GLOSSARY.md`, `REFERENCES.md`, `LINEAGE.md` | consolidated, tiered knowledge base: shared vocabulary + citations across FTGB and the convergence frameworks (Reed, Storti, Nielsen, Ginzburg, Greenyer), plus the Bostick / Puthoff / Shoulders lineage note |
| `engine/` | **`ftgb_engine.py`** — the theory as one executable model: anchors {B,n,m_i,R} → static structure + dynamics + theorem verification, all tiered (`python engine/ftgb_engine.py`) |
| `handoffs/` | precise, execute-ready problem packages for the two hard open computations |
| `results/` | executed advances: R2 near-Beltrami enstrophy theorem, R3 Hall-MHD canonical lift, the matter-wave LENR interaction model, the electron torsion-defect explanation, the α dynamical reframe, + `verify/` scripts |

## Where this credibly stands — the practical, positive value

This is a synthesis *hypothesis*, and its value is not "a finished theory of everything." It
is a set of concrete, field-useful deliverables, each at a stated tier:

1. **A rigorously-tiered result you can cite today: a `[V]` no-go core (static + aligned), a
   driven-realizability `[S]` leg, and one external open (R2).** The current-leg trilogy
   (`FTGB_CURRENTLEG_TRILOGY`) is a self-contained theorem about when a topological helicity
   current can equal a matter current in force-free / two-fluid plasmas — with an
   adversarially-verified no-go, a constructive driven realizability, and a clean reduction of
   its one gate to a recognised external regularity problem. It stands without the wider synthesis: a plasma /
   topological-fluid contribution ready for a journal.
2. **A reusable analysis toolkit.** M7–M10 give a coherent, dimensionally-audited machinery
   for driven toroidal plasmoids and coupled-oscillator systems — canonical-helicity
   currents, a magnitude-inhomogeneity no-go template, a sine-Gordon-validated
   moduli-geodesic method (with an explicit misuse warning), the seesaw frequency-downconversion,
   and an RG dielectric-flow control with a built-in anti-numerology test.
3. **Testable experimental fingerprints.** The inharmonic carrier comb {121, 208, 294} kHz
   (ratios 1 : 1.72 : 2.43, from the Chandrasekhar–Kendall roots) and its predicted
   strong-coupling pull toward 7/4 and 5/2 are concrete spectral discriminators for
   EVOs / plasmoids — a measurement, not a story.
4. **An honest LENR position for the field.** Scaffold-not-reaction: the *environment* is
   verified (the plasmoid-formation recipe — cold-seed condensation, the comb, the coherent
   collective mode), the experimental anomalies (aneutronic excess heat, He-4/heat, COP≈1.3–1.4)
   are structurally accounted for, and the *rate* reduces to exactly two named inputs — a
   branching amplitude Δ (FTGB-internal, open) and a screening energy U_s (host-lattice,
   inherited). No over-unity is claimed; FTGB derives no COP. This tells the CMNS field what
   is settled, what is inherited, and what one calculation would close.

The open problems are stated as **named external computations**, not internal cracks — the
`handoffs/` packages make them execute-ready for a PDE/analysis collaborator (R2 regularity)
and a Skyrme-HPC group (the Δ relaxation).

**Progress (2026-09-09):** the *analytic route* of the R2 hand-off has been partially executed —
see [`results/`](results/). For the Navier–Stokes first model, the driven near-Beltrami heartbeat
now has a **conditional `[V]` enstrophy bound** (a-priori bounded `Z`, hence Beale–Kato–Majda
global regularity) *provided* the drive keeps the time-averaged Beltrami deviation below an
explicit `⟨η²⟩ < ν²λ₁` (≈ RMS deviation `≲ 1/Re`) threshold — proven via an exact vortex-stretching
= Lamb-vector identity and reproduced numerically (`results/verify/`). This is a conditional
advance, not unconditional closure (the `1/Re` condition is stringent at the object's Lundquist
number and unproven). The **Hall two-fluid lift** onto the object's own canonical vorticity is now
also executed (`results/R3_HALLMHD_CANONICAL_ENSTROPHY_2026-09-09.md`): the identity ports verbatim
(the Hall term is frozen-in transport, not an extra flux) and the bound carries over at magnetic
Prandtl number `Pm = 1`, with an explicit `(η−ν)²` dissipation obstruction pinning down exactly what
blocks the general `Pm ≠ 1` case.

## Honest tier legend

`[V]` verified / proven here · `[credited]` established result · `[S]` structural /
contingent-open · `open` a named external problem. Load-bearing claims rest on peer-reviewed
physics; the Nielsen TUFT preprint and quantum-wave-mechanics readings are marked tiered and
are not presented as established.

## Publishing to GitHub (run these yourself, when ready)

This bundle is structured to drop straight into a repository. From the bundle folder:

```bash
git init
git add .
git commit -m "FTGB coherent-object modeler + tiered synthesis bundle"
git branch -M main
git remote add origin https://github.com/<YOUR-USERNAME>/<YOUR-REPO>.git
git push -u origin main
# for a PR from a feature branch instead:
#   git checkout -b ftgb-synthesis && git push -u origin ftgb-synthesis
#   then open the PR on GitHub, or:  gh pr create --fill
```

Replace `<YOUR-USERNAME>/<YOUR-REPO>` with **your** repository. (Note: `LuanRT/BgUtils` is a
third party's unrelated JavaScript library — not a destination for this content.) These
steps need your GitHub credentials and are an outward-facing publish, so they are left for
you to run and authorize.
