# The Δ program — an iterative, in-environment plan for the one HPC-limited item

**The question.** Can we plan an iterative, long-but-certain-to-complete process that reaches *reasonable
validity* on the LENR branching gap **Δ** — the small off-diagonal Landau–Zener gap between the compact B=4
(bound ⁴He) and the two-B=2-torus (d+d entrance) diabatic surfaces, target band **1.4–1.9 MeV** — here, in a
pure-numpy CPU environment, instead of the compiled/GPU run?

## Honest verdict (read this first)

**Two different things are being asked, and they have different answers:**

1. **Certain of *completion*? — YES.** The program below is a sequence of *finite, checkpointed* jobs, each of
   which completes and commits a durable result. It is certain to finish and to *deliver* — a bracketed
   reduced-model Δ with honest error bars, plus a sharpened statement of exactly what residual the full run
   must still resolve. Completion is guaranteed because we never depend on one un-terminating job.

2. **Certain of *reasonable validity*? — YES for a *reduced-model* tier; NO for the *production* number.**
   The honest ceiling is real and specific: Δ is a **small off-diagonal gap in the crossing (merger) region**,
   and that is precisely where reduced ansätze are known to fail (the vendored `b4_two_diabatic` /
   `b4_moduli_geodesic` runs recorded: product ansatz → repulsive core wall; naive blend → topology breaks,
   B→2.4). So the reduced program can nail the **endpoints, the Q-value, the barrier shape, and a Δ
   *bracket*** at a defensible `[V-us]` (reduced-model) tier — but the tight `1.4–1.9 MeV` production number,
   which turns on the crossing-region physics, **may remain HPC-limited even after staging.** We will not
   promise what only the full field can give.

**What "reasonable validity" therefore means here, concretely:** a reproducible `[V-us]` Δ estimate with a
stated two-sided band and a stated systematic-vs-full-field, that either (a) lands in the 1.4–1.9 MeV band
with an error small enough to be useful, or (b) *cannot* be tightened below some floor by reduced methods —
in which case the program has still *converted* "needs HPC, black box" into "here is the bracket and here is
the one crossing-region matrix element the HPC run must pin," which is genuine, valuable progress.

## The method that makes it feasible at all

Not brute-force full-field relaxation (the blocked route — ~15 h/sweep in numpy, topology unwinds at
affordable `dx`). Instead a **topology-exact reduced representation** — the Houghton–Manton–Sutcliffe
rational-map ansatz — which builds the baryon number in *exactly* by construction (degree = B, **no
unwinding**), reducing the 3-D field to a rational map (the shape/topology) × a 1-D radial profile (the
size). Two-cluster configurations use the moduli-space of B=2+B=2 (separation, relative orientation) with a
constrained/collective reaction coordinate `Q` — low-dimensional, numpy-tractable, and topology-safe.

## The stages (each a finite, committed checkpoint)

| Stage | Deliverable | Method (all numpy/CPU) | Tier | Exit criterion |
|---|---|---|---|---|
| **A ✅ DONE** | the reduced machinery is correct in-env | rational-map degrees (exact B) + Skyrme I-integrals vs the HMS table | `[V-us]` | degrees exact, I within ~1% — **met** (`delta_b4_stageA_rationalmap_check`: I = 1.000/5.808/20.650) |
| **B** | the two diabatic energy surfaces `E_bound(Q)`, `E_break(Q)` | stable 1-D profile BVP (semi-implicit / shooting) for endpoints; constrained reduced relaxation along `Q` on the B=2+B=2 moduli space | `[V-us]` | both branches converged + resolution-stable; Q-value matches the 23.85 MeV scale after `f_π,e` calibration |
| **C** | the diabatic crossing `Q_c` and a Δ **bracket** | avoided-crossing / two-level diabatic model at `Q_c`; two-sided band from (2 resolutions × 2 constructions) | `[V-us]` band | a reported Δ = X ± Y MeV with the systematic named |
| **D** | convergence + literature cross-check | refine moduli dimension & `dx`; check vs Feist (B=4 interactions), Halcrow (B=5 two-cluster), the known ⁴He\* level structure | `[V-us]` | band stops moving under refinement, OR the reduced-model floor is identified |
| **E** | the honest terminus | either a useful Δ band in 1.4–1.9 MeV, or a sharpened residual = the one crossing-region matrix element for the HPC run | `[V-us]` + named `[open]` | LENR-rate item either bracketed or precisely handed off |

## How completion is guaranteed (the "long process, certain finish" contract)

- **Each stage is a bounded job** with a fixed grid/step budget and a hard PASS/FAIL, committed as a verify
  script + a checkpoint note. No stage waits on an un-terminating computation.
- **Checkpointed & resumable:** intermediate surfaces (`E(Q)` tables) are written to disk; a later turn or a
  background run resumes from the last checkpoint, not from scratch.
- **Monotone information:** every stage *reduces* the open item (endpoints → surfaces → bracket → floor),
  so the program strictly converges toward either a useful number or a precisely-named residual. It cannot
  loop forever or come up empty — the worst case is stage E(b), which is itself a real result.
- **Honesty gate:** no Δ is reported without its band and its reduced-vs-full-field systematic. If the
  crossing-region floor exceeds the target-band width, that is stated as the finding — not hidden.

## Status

**Stage A is complete and validated** (`results/verify/delta_b4_stageA_rationalmap_check.py`, `[V-us]`): the
topology-exact reduced machinery runs correctly in pure numpy (degrees exact; Skyrme I-integrals match the
Houghton–Manton–Sutcliffe table to ~0.1%; the binding sign is right — ⁴He bound vs 2 d). The feasibility of
the whole staged program rests on that foundation, and it holds. Stages B–E are the iterative long process;
the honest ceiling (the crossing-region gap may stay HPC-limited) travels with every stage.

*Refs: Houghton, Manton & Sutcliffe (1998), Nucl. Phys. B510, 507; Manton & Sutcliffe, Topological Solitons
(CUP 2004) Ch.9; Battye & Sutcliffe (1997), PRL 79, 363; Feist (2012), arXiv:1112.2119; Halcrow (2017), NPB
904, 106; Landau–Zener (1932). Companion: `HANDOFF_DELTA_B4_SKYRME_RELAXATION_2026-09-09.md` (the full-field
route), `results/LENR_ACTIVE_SITE_SYNTHESIS_2026-09-14.md` (why Δ is the one open item).*
