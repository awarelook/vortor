# Excision ledger — false / numerology items removed from or quarantined out of the jewel

**Author:** Nathaniel Hanks · **Date:** 2026-09-09
**Purpose.** Bin ⑤ of the knowledge-ordering plan: the scientific record of claims that were **false,
numerological, or fabricated** and have been **removed from the validated jewel** — logged here (not silently
dropped) so the reason is auditable and the item can never re-enter a citation by accident. Distinct from the
reversible *file* quarantine (`F:\_QUARANTINE\`); this ledger is about *claims*, and lives in the repo.

**Status key:** `EXCISED` = removed from the jewel as false/unjustified · `FLAGGED` = kept but demoted to
`[flag]`, may **not** be cited as derived · `DO-NOT-CITE` = external source barred as unreliable.

---

## EXCISED — false / unjustified, removed from the jewel

| Item | What it claimed | Why removed | Where it lived → now |
|---|---|---|---|
| **`e^(-2/3)` vacuum-screening factor** | maps toroidal winding 140.2 → 137.04, "deriving" α | unjustified numerology; `e^(-2/3)=0.513` actually maps 140.2→72, not 137 — it doesn't even give the needed correction | `excision-protocol-storti-factor.md`; verified dead in `verify/egm_sense_checks.py` §6, `verify/alpha_running.py` §4 |
| **`E_fm = 2.5 MeV` LENR rate/cross-section** | a specific fabricated reaction energy/rate | fabricated number with no derivation; retracted | retracted across the synthesis; barred by `LENR_MATTERWAVE_INTERACTION_MODEL` §6 |
| **Derived COP (1.3–1.4) / any over-unity** | a first-principles coefficient of performance | FTGB derives no COP; 1.3–1.4 is *inherited field positioning*; the vacuum is a medium, not a source | never in the jewel; explicitly barred (trilogy §6; LENR model §5) |
| **Storti "0.01%" particle-radii derivation** | proton radius etc. to 0.01% from a closed form | the clean closed-forms miss 0.84 fm by 10³–10⁴× (`verify/egm_sense_checks.py` §3); the match is a full-numeric fit, not a parameter-free derivation | folded as `[flag]` in M11-4, not as derived |

## FLAGGED — kept, demoted, may not be cited as derived

| Item | Status | Note |
|---|---|---|
| **α value via winding (140.2 vs 137.036, 2.3%)** | `[flag]` | raw winding is closest to **140**, fails the 0.5% bar for 137; reframed as a running/IR-fixed-point *question* (magnetic-vacuum anti-screening), **not** a derivation — `ALPHA_DYNAMICAL_REFRAME` |
| **Storti H₀ = 67.08 km/s/Mpc** | `[flag]` | `√(GM/R³)` gives ~9; reaching 67 needs an unmotivated ×7.8 (`verify/egm_sense_checks.py` §5); not derived; a separate historical-priority claim is left unassessed |
| **The "2:1 harmonic" ω_Ω(e)=2ω_Ω(p)** | `[flag]` | definitional (ratio = 2.000 by construction), not a prediction (M11-4) |
| **`~137` / `φ^n` coincidences** | `[flagged]` | held at the 0.5% anti-numerology bar (M10-5); none promoted |

## DO-NOT-CITE — external sources barred

- **Rossi (E-Cat), Mills (hydrino / BrLP), bio-transmutation** — barred as unreliable; never a source for any
  claim. Keep **baryon-conserving `d+d→⁴He` distinct from baryon decay**.

## Provenance / audit trail
`excision-protocol-storti-factor.md` (the original e^(-2/3) removal), `verify/egm_sense_checks.py`,
`verify/alpha_running.py`, `ALPHA_DYNAMICAL_REFRAME_2026-09-09.md`, `LENR_MATTERWAVE_INTERACTION_MODEL_2026-09-09.md`,
`FTGB_CURRENTLEG_TRILOGY.md` §6, `TOOLKIT_HANDBOOK.md` M10-5 / M11-4, `KNOWLEDGE_ORDERING_PLAN_2026-09-09.md`.

*Every item here was removed *because* the project's tier discipline caught it — this ledger is the receipt.
Nothing in the jewel cites an EXCISED or FLAGGED-as-derived item.*
