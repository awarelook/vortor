# The Coherent Object — FTGB modeler & synthesis bundle

**Author:** Nathaniel Hanks · **A self-contained package:** one interactive modeler + the two
manuscripts + the method toolkit + two execute-ready hand-off packages.

> One driven, force-free Beltrami–Hopf toroidal soliton, built up from a point → a string →
> a resonator → a knotted field → driven dynamics, and read at once as a *field* and a
> *matter wave*. Every claim carries an honest tier; the mathematics is shown with its
> plain-language translation and every symbol labelled.

---

## Open it (no install, any OS)

- **`index.html`** — double-click it. It runs in any modern browser on **Windows, macOS,
  Linux, iOS, or Android** with no server and no dependencies (all CSS/JS inlined). The five
  stages animate the mathematics live; drag the sliders to drive the oscillator, tune the
  comb coupling, climb the eigenmode ladder, spin the torus, and raise the E·B drive.
- Prefer a hosted view? The same modeler is a shareable web artifact (see the link you were
  given when it was published).

## What's in the bundle

| File | What it is |
|---|---|
| `index.html` | the interactive modeler (native-open, cross-OS) |
| `FTGB_GRAND_SYNTHESIS.{md,pdf}` | the full tiered synthesis manuscript (Parts A–G, ~16.7k words) — **the large text with all the math** |
| `FTGB_CURRENTLEG_TRILOGY.{md,pdf}` | the standalone lead result (a self-contained plasma / topological-fluid theorem) |
| `toolkit/` | the four method modules: Buckingham-Π (M7), QWM conversion (M8), coupled-oscillator substrate (M9), topological-soliton methods (M10) |
| `handoffs/` | precise, execute-ready problem packages for the two hard open computations |

## Where this credibly stands — the practical, positive value

This is a synthesis *hypothesis*, and its value is not "a finished theory of everything." It
is a set of concrete, field-useful deliverables, each at a stated tier:

1. **A proven result you can cite today `[V]`.** The current-leg trilogy (`FTGB_CURRENTLEG_TRILOGY`)
   is a self-contained theorem about when a topological helicity current can equal a matter
   current in force-free / two-fluid plasmas — with an adversarially-verified no-go, a
   constructive driven realizability, and a clean reduction of its one gate to a recognised
   external regularity problem. It stands without the wider synthesis: a plasma /
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

## Honest tier legend

`[V]` verified / proven here · `[A]` credited established result · `[S]` structural /
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
