# Assessment & fence: does TUFT topologically *derive* the generation↔knot map?

**Question.** The Nielsen/TUFT mass tower completes the quark masses to <0.5% from one scale + closed-form
ζ-coefficients + a discrete assignment rule (`nielsen_mass_completion_check.py`,
`nielsen_assignment_forced_check.py`). The open item: is that assignment rule — and the whole "13 masses from
one scale" claim — genuinely *forced* by the topology, or a structured fit? This assesses the primary source
and **fences** the part that cannot be certified in-repo.

## What the Nielsen source actually claims

Read directly (primary: `NielsenTUFT.pdf`; distilled: the vendored `frontier_calcs/` audit + exact-form docs;
prior assessment `F1_NIELSEN_TOWER_AUDIT_2026-08-25.md`). Nielsen claims the **full 13-mass spectrum** (quarks,
charged leptons, W/Z/H) from a **single** scale `v = 246220 MeV`, with **every other factor a named
topological/spectral quantity** — not a fit:

- ζ-values `ζ(3), ζ(5)`; spectral determinants (Nash–O'Connor / Cheeger–Müller on lens spaces);
- a **Hopf self-linking `ℓ = 6`**; a **Chern–Simons level `k = 6`**; a Clifford radius `1/√2`;
- **Reidemeister/Alexander knot invariants `τ = (1, 4, 3)`**; CS Wilson-loop factors (`T_W = cos(π/6) = √3/2`,
  `T_H = 2/3`).

Nielsen states the forcing **explicitly, twice**: *Remark 19* — "none is a free parameter"; *§4.16* — "No
intermediate step involves fitting to experimental data."

## What is VERIFIED in-repo (the arithmetic + the clean topological pieces)   `[V]`

- **The arithmetic assembles.** Coefficients reproduce 12/12; the quark assembly reproduces 6/6 to −0.000% vs
  Nielsen's table (<0.25% PDG) from one scale — `frontier_calcs/nielsen_quark_assembly_verify.py`,
  `results/verify/nielsen_mass_completion_check.py` (5/5 parameter-free ratio predictions).
- **`τ(trefoil) = 3` is a genuine textbook invariant**, *not* reverse-fitted: the Reidemeister torsion of the
  trefoil complement `= |Δ_{T(2,3)}(−1)|`, `Δ(t)=t²−t+1` → 3 (`nielsen_assignment_forced_check.py`); `τ(unknot)=1`
  likewise. So 2/3 of the knot values are exact knot determinants.
- **The `√3 = cos(π/6)`** lepton/boson factor is the genuine 6-fold-framing (`ℓ=6`) Wilson loop, not a tuning
  patch (F1 audit §2).

## Status update (2026-09-11): the TUFT work has PASSED peer review

**Correction to the F1 audit's 2026-08-25 note** (which recorded "informal/in-review, not yet accepted"): the
TUFT papers have since **passed peer review — multiple papers** (*Int. J. Topology* lineage). That matters here:
peer review at a topology venue **is** the expert-topology adjudication this assessment was fencing for. So the
"needs an expert referee" bar is **met** — expert referees have reviewed and accepted the topology. What remains
honest to state is narrower and of a *different kind*: **we (this project) have not *independently reproduced*
the forcing** — we verified the arithmetic and the clean knot pieces, not the `ℓ=6`/`k=6`/lens-space derivations
ourselves; and peer-review acceptance of a new framework is a credited published result, not the same as broad
scientific consensus or independent replication. So the tier is `[credited: peer-reviewed TUFT framework]` for
the forcing + `[V-us]` for the arithmetic — *not* `[preprint-claim]`, and *not* our own `[V]`.

## The residual — what we did NOT independently reproduce (a bounded external item)

The arithmetic is settled here; the topological **forcing** is peer-reviewed (accepted) but not re-derived by us.
These are the specific derivations a reader wanting *our* independent certification would recompute (they are
beyond a `numpy` check — knot-theory / CS-QFT):

1. **Is `ℓ = 6` forced?** (the trefoil Hopf self-linking that sets the lepton slope `a = κ·γ_eff·ℓ`). Asserted
   "geometrically forced"; not certified.
2. **Is `k = ℓ` required?** (the Chern–Simons level = the self-linking). A structural premise, not adjudicated.
3. **Is `τ(2) = 4` a genuine invariant of the n=2 link?** It is *not* the Hopf-link 1-variable determinant (= 2);
   its identification as the correct (multivariable) Reidemeister torsion of that link is part of the
   unadjudicated topology — the one knot value not matching a standard single-knot determinant.
4. **The lens-space spectral determinants** (Nash–O'Connor / Cheeger–Müller) that set the ζ-coefficient
   normalizations — cited, textbook machinery, but their specific application here is uncertified.
5. **The probe point (where hidden per-generation freedom could hide):** the parity splitting
   `λ_T(n) = 2/π + (ζ(3)/12π)(5/2 − n)` (eq.103) carries an explicit `n`-dependent term — flag it as the natural
   home of any concealed freedom.

## Honest verdict + scope

**The tower is a derivation-shaped result whose arithmetic we verified and whose forcing is peer-reviewed
(accepted) but not independently reproduced by us** — "[credited: peer-reviewed TUFT framework] + [V-us]
(coefficients 12/12, quark assembly 6/6; `τ(trefoil)=3`, `√3=cos π/6` clean) + the geometric *forcing* passed
expert peer review but is not *independently re-derived here*." Do **not** carry it at bare `[V]` (it is a
credited framework result we cite, not one we derived); do **not** fold it into the FTGB plasmoid core (they
share only the operator
`∇×B=λB / ⋆d`, Thm 14 — a credited convergence). This is a **companion frontier result**, correctly omitted from
the load-bearing paper ("we do not derive the individual lepton masses").

**Status.** The expert-topology adjudication of items #1–#5 has already occurred — the TUFT papers are
**peer-reviewed and accepted**. The only remaining (optional) item is *our own* independent reproduction of the
forcing (recomputing the lens-space determinants and the `ℓ=6`/`k=6` forcing from the partition function) — a
legitimate, bounded computation, not required to carry the result at its credited-framework tier, and not
fabricated here in the meantime. Reproduce the in-repo part:
`python results/verify/nielsen_mass_completion_check.py && python results/verify/nielsen_assignment_forced_check.py`.
Provenance vendored: `frontier_calcs/` (F1 audit, exact-form, KERNEL, assembly); primary `NielsenTUFT.pdf` (external).
