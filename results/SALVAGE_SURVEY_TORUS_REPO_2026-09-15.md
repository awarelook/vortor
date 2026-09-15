# Salvage survey — `torus_project_repo` (the June-2026 THz-doublet campaign)

**Author:** Nathaniel Hanks · **Date:** 2026-09-15 · **Store:** `F:\trial connect\torus_project_repo`
(234 Python files, 1.2 GB; manifest dated 2026-06-10). **Mandate:** `KNOWLEDGE_ORDERING_PLAN_2026-09-09`
designated this store *"SCRATCH — merge useful bits to vortor, then quarantine."* This survey executes that
merge. Vendored provenance: `frontier_calcs/torus_repo_salvage_2026-06/`.

## 0. What the store is

A **pre-jewel campaign** (June 2026) on a *different parameter regime* than the jewel's object: a
**10 THz tight-doublet CK geometry** with `f_beat = 11.127 GHz`, necked/nested torus H(curl) FEM solves,
five calibrated reduced models (Galerkin v7 / plasmoid MHD / beat envelope / pressure-breathing / QHO),
Hagelstein-anchored quanta checks, and a nuclear-adjacent layer (CCS barrier transparency, Preparata QED
coherence, no-kernel nuclear-side envelope). It predates every M16/cross-scale fence and the 09-14
disposal-chain convergence — so its nuclear-adjacent readings required fence-confrontation, not ingestion.

## 1. FENCE-KILLED (computed, kept as wins)

- **Beat-modulated tunneling "coherence gain 1.334"** → **settled-negative**
  (`beat_modulated_tunneling_nogo_check.py`, NEW): the 11.127 GHz beat is *frozen* across any tunneling
  attempt (`τ_traversal/T_beat ≈ 3×10⁻⁷` — the beat is DC; no modulation channel), its quantum (46 µeV)
  is 6.7 OOM below its own 240 eV barrier and 11.7 OOM below the 23.85 MeV rung, and even the 10 THz
  *carrier* quantum (41.4 meV) sits **8.76 OOM** below the nuclear rung — the M16 kHz fence extends
  unchanged to GHz/THz. **Bonus catch:** the vendored artifact is internally inconsistent — its "66 fm
  classical radius" corresponds to ~21.7 keV, not its stated 240 eV barrier, and its transparency
  (6.14×10⁻⁶) sits ~82 OOM above standard WKB-to-contact at 240 eV (2πη = 201) — an unstated
  truncated-barrier model. Its **absolute transparency numbers are not ingestible**. What survives is what
  the jewel already carries: bare screened tunneling with *measured* `U_s` `[credited]`.
- **Preparata QED coherence conclusion** → **logged, demoted**: the vendored JSON's own numbers undercut
  its conclusion — `field_density_ratio = 6.0×10⁻¹⁰` (field energy density vs atomic binding density),
  yet it concludes "field density sufficient for QED processes." The coherence-length geometry
  (`L/λ = 3`, macroscopic-QED-accessible regime) is fine as *Preparata-class prior art context*
  (already credited in REFERENCES §1m); the "sufficient" clause is unsupported by its own ratio.
  Not promoted.

## 2. SALVAGED (folded into the jewel)

- **The phase-scrambled control protocol** (from the campaign's beat-dominance validation suite): any
  claimed beat-locked effect must (i) survive a ±10% drive perturbation with <30% variation AND
  (ii) **die under phase scrambling** (beat ratio < 0.2) — separating a coherent system property from an
  artifact. **Folded into the `f_b(L)=N^L` beat-gate falsifier** (MVP §5.7 + the resolution map's
  spectral-discriminators row): the jewel's sharpest theory-specific discriminator now has a stated
  control protocol. This is a genuine methodological catch — the gate prediction previously had no
  artifact control.
- **The no-kernel nuclear-side envelope method** (`output/nuclear_side_envelope.py` there): upper-bounds
  the supportable nuclear event rate from the coherent energy budget and coherence time *without assuming
  any nuclear kernel* — the same honest walls-first shape as the jewel's disposal chain. Method noted;
  its regime numbers stay in the store (campaign-specific).
- **The `f_beat(R₁)` fingerprint-tracked scan** (vendored summary): an honest *messy* result — effective
  scaling exponent ~0.5±0.3 with R² = 0.10 across a 6-point necked-geometry scan, i.e. **neither** clean
  `R⁻¹` nor `R⁻³`; mode hybridization and neck geometry contaminate simple beat-scaling laws. Kept as a
  **caution datum** for any `f_b(R)` falsifier design in coupled/necked geometries (the jewel's
  `f_b = v_A|Δλ|/2πR` is stated for the *single clean* resonator; this scan shows what necking does).
- **Methodology convergence** (no numbers moved): the campaign's "same CK-anchored calibration point via
  algebraic mapping, no fitting" bridge across five reduced models is the same no-fit discipline the
  jewel practices; noted as lineage.

## 3. CONFIRMED-ABSENT (the honest negative of the expedition)

The five `[V-external]` orphans the 09-14 audit backlogged — `V_111 = 2.30` / `⟨D⟩ ≈ 0.86` CK overlaps,
the Madelung continuity residual `5e-16`, the O_h/Tinkham–Koster gerade settlement, the grid-convergent
`H = 0.088`, and the `ω_EVO` provenance — are **not in this store** (all apparent grep hits were base64
false positives inside embedded images; targeted text search returned zero). Likewise absent: the MVVC
ledger / beat-ladder validity-boundary theorems, and the phantom "BLUE-SKY-annex" agent-report layer.
**Consequence:** the capture backlog still points at the ckfreefem parent corpus proper, which is *not on
the F: drive*. The in-repo *recompute* route (backlog ranking in `BEST_AVAILABLE_THEORY_2026-09-14.md` §3)
is therefore the realistic path for those five — not vendoring.

## 4. NOT INGESTED (fences held)

- Any absolute transparency/rate from the CCS layer (TEST 1 inconsistency; no-fabricated-rates rule).
- The Hagelstein-anchored `E_neck = 18.2 MV/m @ 1 pJ` calibration and campaign COP-adjacent material —
  campaign-internal, not confronted with the jewel's anchors; stays in the store.
- `F:\SYNTHESIS` (mixed science/Track-2 vault) and `F:\conspire` — out of scope per the standing
  science-only fence; not read beyond directory listing.
- The remaining ~220 scripts (solver/geometry/campaign orchestration for the necked THz object) — sound
  engineering for a *different object*; nothing there contradicts or extends the jewel's `[V]` core.
  Left in place; the store can now be quarantined per the ordering plan.

## 5. Ledger

| Item | Disposition | Tier |
|---|---|---|
| Beat-modulated tunneling gain 1.334 | fence-killed, check + vendored artifact | `settled-neg` |
| CCS absolute transparency 6.14e-6 | internally inconsistent (~82 OOM vs WKB-to-contact); logged | `[flag]` not ingestible |
| Preparata "sufficient for QED" | demoted by its own ratio 6e-10; prior-art context only | `[credited-context]` |
| Phase-scrambled control protocol | folded into the N^L beat-gate falsifier | method `[V-protocol]` |
| No-kernel envelope method | noted (walls-first methodology convergence) | method |
| f_beat(R₁) necked-scan scatter | caution datum for f_b(R) falsifier design | `[log]` vendored |
| The five [V-external] orphans + MVVC + phantom layer | **confirmed absent** from this store | recompute route stands |

*Harness after fold: 90/90 (with Stage D + the gate). The store's designation moves from SCRATCH to surveyed-and-quarantinable.*
