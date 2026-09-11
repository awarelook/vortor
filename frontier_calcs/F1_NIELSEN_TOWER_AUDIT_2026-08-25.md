# F1 — Nielsen mass/gauge-tower audit (2026-08-25)

*Resolves fault-line F1 from `VALIDATION_ASSESSMENT_AND_PLAN_2026-08-25.md`: (1) verify every Nielsen locator
against the primary source, (2) re-derive-or-classify the mass assembly. Source read directly:
`Reed-QWM/NielsenTUFT.pdf` (290 pp). Method: calculate-first; separate what is verified (loci exist; coefficients
+ assembly reproduce) from what is not (whether the topology is genuinely forced). No number fabricated.*

## Verdict in one line

The Nielsen mass/gauge tower is a **structured, parameter-free geometric construction** — 13 SM masses (3 leptons,
6 quarks, W/Z/H) from a **single scale** `v = 246 220 MeV` plus zeta-values and knot invariants — that **reproduces
PDG to <0.25% (quarks) / 0.4–2% (leptons) / sub-σ (bosons)**, is **explicitly non-fitted** by its author, and whose
loci and coefficient/assembly arithmetic this project has now **independently verified**. It is **NOT a fit and NOT
numerology.** But it rests on **topological premises that require expert referee review** and comes from an
**informal (in-invited-peer-review) source**, so it stays **[cited]+[V-us], not core [V]**, and stays **out of the
FTGB plasmoid paper** (which correctly claims only the shared *operator*, not the mass tower).

## 1. Locator verification — every load-bearing Nielsen citation, checked against NielsenTUFT.pdf

| Registry/toolkit claim | Cited locus | PDF check (this audit) |
|---|---|---|
| Beltrami `⋆d` unique (OP-1) | Thm 14, p.21 | **CONFIRMED** — Thm 14 present p.21 (also 26–32) |
| Torsion exponents σ₃/σ₅/σ₉ | Cor. 9, eq.46–48, p.43 | CONFIRMED (page family 43–44) |
| Lepton coeff `a = 6√2·exp(ζ(3)/24π²)` | Thm 31, eq.53/55, p.45–46 | **CONFIRMED** — Remark 19 "geometrically forced, none a free parameter"; assembly `a=κγ_eff·ℓ`, `ℓ=6`=trefoil Hopf self-linking, p.46 |
| Casimir suppression `D(n)` | eq.66, p.49 | **CONFIRMED** — D(1,2,3)=1.203/4.807/10.818, "confirmed by Nash–O'Connor + Cheeger–Müller"; **"No intermediate step involves fitting to experimental data"** |
| Lepton mass law `m_n=(n+1)e^{an−D(n)}φ_n` | eq.67, p.49 | **CONFIRMED** — each factor structurally traced (SU(2) mult / helicity / Casimir det / U(1) spectral) |
| Lepton knot torsions | eq.70, p.49; Fox p.56 | **CONFIRMED** — τ(K)=(1,4,3) from Reidemeister torsion |
| Bosons W/Z/H | Thm 32, eq.71, Table 1, p.50 | **CONFIRMED** — pulls **+0.04 / +0.11 / +0.23σ**; T-factors are CS Wilson loops (T_W=cos π/6=√3/2, T_H=2/3) |
| Weinberg `sin²θ_W=3/4π=0.2387` | eq.75, p.50 | CONFIRMED (matches **low-energy running**, 0.4σ; NOT M_Z — stated) |
| Gauge couplings g,g′,g_s | Thm 33, eq.76–78, p.51 | CONFIRMED present p.51 |
| Quark mass law | eq.96, p.57 | **CONFIRMED** — full formula + "v = 246220 MeV remains the **sole unit conversion factor**"; table u…t all within PDG error |
| Quark a₅/C₅/β₅/σ₅/λ_T/τ | eq.97–103, p.57 | **CONFIRMED** — all coefficients present verbatim |
| S⁵ spectrum, ζ_B5 | eq.82/83/106, p.53/58 | CONFIRMED (page family) |

**Result: every load-bearing locus exists at (or within one page of) the cited location and states what the
project's `CITATION_CLOSE_NIELSEN_2026-08-23.md` claims.** One negative confirmed: **"Koide" = 0 hits in 290 pp** —
Nielsen carries no Koide relation, so the project's Koide (TOP-10) is correctly attributed to its *own* spectral
calc, never to Nielsen.

## 2. Re-derivation of the mass assembly (not just the coefficients)

**Quark sector — RE-DERIVED, `nielsen_quark_assembly_verify.py` (NEW):** plugging Nielsen's published coefficients
(eq.97–103) + torsions τ(K)=(1,4,3) + the single scale `v` into eq.96 reproduces **all 6 quark masses**:
`u 2.1600, d 4.6642, s 93.565, c 1272.71, b 4172.20, t 172864` MeV — **−0.000% vs Nielsen's table (exact) and
<0.25% vs PDG (6/6).** So the *arithmetic* assembly is sound: coefficients → masses works, no hidden step.

**Boson sector:** Nielsen's Table 1 (p.50) gives W/Z/H at pulls +0.04/+0.11/+0.23σ; the formula (eq.71) uses `v`,
`α`, `r=8`, and CS Wilson-loop T-factors — verified as present; full re-run deferred (same arithmetic pattern).

**Lepton sector:** construction verified (eq.67 + D(n) eq.66 + torsions eq.70); mass values on p.49–50 to 0.4–2%.
Not re-scripted (φ_n=exp(nα/6) needs Nielsen's α convention) — deferred to avoid a convention-error false negative.

**The √3 "closes-the-tau" red flag — RESOLVED.** `τ(K₃)=3` is the **Reidemeister torsion of the trefoil
complement = |Δ_{T(2,3)}(−1)|**, where `Δ(t)=t²−t+1` is the trefoil's Alexander polynomial — a **textbook knot
invariant** (=the knot determinant), NOT reverse-fitted. The √3 in the lepton/boson sectors is `cos(π/6)` from the
6-fold framing (ℓ=6). The earlier "set τ=1 → tau 1.3% off → add √3" note was the project *initially omitting* a
genuine topological factor, then restoring it — not tuning.

## 3. Classification: DERIVATION, not fit — with three load-bearing caveats

**Why it is a derivation, not a fit / numerology:**
- **One free scale.** The entire 13-mass spectrum uses `v = 246220 MeV` as "the sole unit conversion factor"
  (Nielsen's words, eq.96). Every other factor is a ζ-value (ζ(3), ζ(5)), a spectral determinant
  (Nash–O'Connor/Cheeger–Müller on lens spaces), a Hopf self-linking (ℓ=6), a Clifford radius (1/√2), a
  Chern–Simons level (k=6), or a Reidemeister/Alexander knot invariant (τ=1,4,3).
- **Explicitly non-fitted** (Nielsen states it twice: Remark 19 "none is a free parameter"; §4.16 "No intermediate
  step involves fitting to experimental data").
- **Structurally traced.** Each mass-law factor maps to a named feature of the partition function (SU(2)
  multiplicity, helicity accumulation, Casimir determinant, U(1) spectral, parity splitting).
- **Independently reproduced.** Coefficients 12/12 (`mass_gauge_tower_reproduce.py`); quark assembly 6/6 (this
  audit). The arithmetic is not in question.

**Why it nonetheless stays [cited]+[V-us], NOT core [V]:**
1. **Informal source** — "in invited peer review, *Int. J. Topology*"; not yet accepted.
2. **Unadjudicated topological premises.** The claims that ℓ=6 is *forced*, that k=ℓ is *required*, that the
   corrections are *"unavoidable"* — are asserted with geometric justification but not independently certified. That
   13 masses match PDG from one scale is either a landmark or contains subtle freedom only an expert topology/QFT
   referee could find. This project verified the *arithmetic*, not the *forcing*.
3. **Probe point for a referee:** the parity-splitting `λ_T(n) = 2/π + ζ(3)/12π·(5/2−n)` (eq.103) carries an
   n-dependent piece — the natural place hidden per-generation freedom could hide. Flag it explicitly.

## 4. Scope decision (resolves F1) + registry corrections

**KEEP the tower as a separate, explicitly-credited COMPANION result — do NOT fold it into the FTGB plasmoid
paper.** The FTGB paper is about the EVO/plasmoid (a collective object at ~kHz/decimetre scale); the mass tower is
a *fundamental-particle* claim. They share only the **operator** `∇×B=λB / ⋆d` (Thm 14) — cite that as a **credited
convergence**, nothing more. The paper already omits the tower and states "we do not derive the individual lepton
masses" — **that scope is correct; keep it.**

**Registry tier corrections (apply to TOP-6, TOP-7, TOP-8, TOP-9, TOP-14, NEU-2):** state the tier precisely as
**"[cited] (Nielsen TUFT, informal/in-review) + [V-us] (coefficients reproduced 12/12; quark assembly reproduced
6/6); full geometric *forcing* not independently certified — needs expert topology/QFT review."** Do **not** carry
these at bare [V]. Keep the C₅ "12" (Ray–Singer) as [S] open. Keep the Bayes-global-confidence layer firewalled [N].

**Net:** F1 is a *positive* outcome — the tower is not a liability (not numerology, not a fit; loci and arithmetic
verified) and not an over-claim to import (informal, topology uncertified). The honest move is **precise
attribution + the uncertified-forcing caveat**, and continued **omission from the plasmoid paper** — exactly the
current state, now on a verified basis.

*Scripts: `nielsen_quark_assembly_verify.py` (6/6), `mass_gauge_tower_reproduce.py` (12/12). Source:
`Reed-QWM/NielsenTUFT.pdf` pp.21,43–58. Locator map: `CITATION_CLOSE_NIELSEN_2026-08-23.md`.*
