# Knowledge-ordering plan — cohering the local mind (PC → external → Obsidian → VS Code / GitHub)

**Author:** Nathaniel Hanks · **Date:** 2026-09-09
**Purpose.** One scheme to order the whole knowledge ecosystem: separate the **validated working jewel**
(`F:\vortor`) from **superseded drafts** (quarantine, not delete), from **framework readings** (kept with
tiers), and from **unverifiable assumptions / numerology** (separated or excised). Assign each store a single
role, and define the flow to sharing (GitHub) and archive (external / cloud). **Nothing is deleted by this
plan** — superseded material is *moved to quarantine* for the author to review.

> **Held for later (per instruction).** Two publication tracks — (T) a technical theory paper and (C) a
> readable companion (natural analogy, history, conceptual development) — are **not written now**. This plan
> only *orders the knowledge base so both can be drawn from valid, cited, reproducible sources* when the time
> comes. See §6.

---

## 1. The ecosystem as found (2026-09-09)

| Store | Drive | Role today | Role assigned |
|---|---|---|---|
| **`F:\vortor`** (git repo) | F: | the clean FTGB working project | **THE JEWEL** — single source of truth for validated physics/math/code → GitHub |
| **`F:\conspire`** (Obsidian) | F: | relation-maps: Puthoff, Shoulders, Bostick, physics concepts + suppression/network notes | **KNOWLEDGE / LINEAGE vault** — people, history, real connections **and** flagged speculation, kept apart from the jewel |
| **`F:\SYNTHESIS`** (Obsidian) | F: | vortex-paradigm synthesis + MOCs | **SYNTHESIS / narrative vault** — draft syntheses & maps-of-content |
| **`F:\trial connect`** (Obsidian) | F: | `torus_project_repo` trial | **SCRATCH** — merge useful bits to vortor, then quarantine |
| **`C:\…\OneDrive\Documents\Obsidian Vault`** | C: | general vault | personal; out of scope unless it holds project notes |
| **`C:\Users\natha\Downloads`** (~180+ files) | C: | raw dumping ground: TUFT/Reed/Nielsen primaries + many superseded drafts | **INBOX** — triage per §3, then route |
| **G:** (Google Drive) | G: | cloud sync | **ARCHIVE / SHARE-cloud** — backup of everything, incl. quarantine |

## 2. Single-source-of-truth (SSoT) — one home per artifact type

- **Validated physics, math, code, models** → **`F:\vortor` → GitHub.** Nothing validated lives only in
  Downloads or a vault. (Already: trilogy, R2/R3, toolkit M7–M12, LENR model, electron, α reframe, models.)
- **People / history / lineage / connections** → **`F:\conspire`** (and `F:\SYNTHESIS` for narrative). Real
  physics lineage (Puthoff PV, Shoulders EVOs, Bostick plasmoids, Nielsen, Reed, Storti, Ginzburg) lives here
  as relation-maps that *point to* the jewel — never duplicating its equations.
- **Raw / unsorted** → **Downloads (INBOX only)**; empty it by triage, don't accumulate.
- **Backups / archive** → **G: (cloud)** + one **physical external** (see §5); mirror `F:\vortor`,
  `_QUARANTINE`, and the vaults.

## 3. The triage taxonomy — five bins (the "cohere the mind" step)

Classify every file into exactly one bin. **Only JEWEL and TIERED enter the shareable repo.**

| Bin | What it is | Where it goes | Deletion? |
|---|---|---|---|
| **① JEWEL** | validated, tiered `[V]`/`[credited]`, reproducible (has a verify script or a proof) | `F:\vortor` (git) → GitHub | never |
| **② TIERED** | framework readings kept *with* their tier (`[framework]`/`[S]`) — Reed, Storti, Nielsen, Ginzburg | `F:\vortor/toolkit`, `/results`, `GLOSSARY`/`REFERENCES` | never |
| **③ QUARANTINE** | superseded drafts, near-duplicate iterations (e.g. `*Framework2/222/333`, `(1)(2)(3)` copies) | `F:\_QUARANTINE\` (kept, dated) | author-only, after review |
| **④ SEPARATE** | unverifiable **assumptions** (suppression chains, personnel/network conspiracy) | stays in the Obsidian vault, tagged `#speculation`, **never** merged into the jewel | never (but never promoted) |
| **⑤ EXCISED** | **false / numerology** — `e^(-2/3)`, fabricated rates/cross-sections, retracted numbers | recorded in an **excision ledger**; removed from the jewel | removed from jewel; ledger kept |

**The discipline, in one line:** *valid, open, experimental, and real connections* (bins ①②, and the real
physics maps in ④) are cohered into the jewel and its lineage vault; *false assumptions and numerology* (⑤)
are logged-and-removed; *unverifiable speculation* (④) is quarantined in the vault, clearly labeled, and kept
out of anything cited. This is the same tier discipline the repo already runs, applied to the whole PC.

## 4. The flow (ASCII)

```
   Downloads (INBOX)                 F:\conspire / SYNTHESIS (vaults)
        │  triage (§3)                     │  relation-maps, MOCs
        ▼                                   │  (#speculation kept separate)
  ┌───────────────┐   ①JEWEL / ②TIERED   ┌──┴────────────┐
  │  classify 1-5 │ ───────────────────► │  F:\vortor    │ ──git push──► GitHub (share)
  └───────────────┘   ③ QUARANTINE       │  (the JEWEL)  │
        │            ─────────────────►  F:\_QUARANTINE   └──────┬────────┘
        │            ④ SEPARATE ───────►  vault #speculation      │ mirror
        │            ⑤ EXCISED  ───────►  results/EXCISION_LEDGER  ▼
        └───────────────────────────────────────────────►  G: cloud + physical external (ARCHIVE)
```

## 5. Concrete migration scheme (steps; author runs the moves)

1. **Freeze the jewel.** `F:\vortor` is authoritative and on GitHub once pushed (`git push -u origin
   ftgb-coherent-object`; repo `awarelook/vortor` must exist first).
2. **Make the bins.** `F:\_QUARANTINE\2026-09-09\` (dated) and `results/EXCISION_LEDGER.md` (already-excised
   items: `e^(-2/3)`, `E_fm=2.5 MeV`, fabricated COP/rates).
3. **Triage Downloads by pattern** (low-risk first): route obvious duplicates (`* (1).ext`, `*2/222/333`,
   `*LATER/LATEREST/shorter`) to QUARANTINE; keep the **primaries** already folded (`Larry_Reed_QWM_
   Derivations.md`, `TUFT Jenny Nielsen.pdf`, `Dtorti QE 2-4.pdf`) as source-of-record (copy into a
   `sources/` archive, cited by `REFERENCES.md`).
4. **Vault hygiene.** In `F:\conspire`, tag speculative network/suppression notes `#speculation`; keep the
   physics relation-maps (Puthoff/Shoulders/Bostick/poloidal-toroidal/43 kHz) linked to the jewel via a new
   index note (§ vault integration).
5. **Archive.** Mirror `F:\vortor`, `F:\_QUARANTINE`, and the vaults to **G: (cloud)** and a **physical
   external**; verify with a checksum/`robocopy /MIR` log. (Two copies + offsite = safe.)
6. **VS Code / GitHub.** Open `F:\vortor` as the VS Code workspace; GitHub is the share surface for the jewel
   only. Vaults stay local/cloud (not on the public repo) unless a curated export is intended.

*(I can generate the `_QUARANTINE` folder + a move-manifest of exact duplicate paths for your approval, and
scaffold `EXCISION_LEDGER.md` — but I will not delete or bulk-move files without your go-ahead.)*

## 6. Two publication tracks the ordered KB must feed (not written now)

- **(T) Technical theory** — draws only from ①JEWEL + ②TIERED: the trilogy, R2/R3, the toolkit, the LENR
  model, with `REFERENCES.md`. Every claim already carries a tier and (where `[V]`) a reproducible script.
- **(C) Readable companion** — natural analogy, history, conceptual development — draws from the Obsidian
  lineage/synthesis vaults (real figures & connections) + a future plain-language pass over the jewel. Keeps
  the same tier honesty in prose (what is proven vs. read vs. open).

Ordering now = both tracks later can cite valid, reproducible sources without re-litigating what is jewel vs.
quarantine vs. excised.

## 7. Invariants of the scheme (do-not-break rules)
- The **jewel never imports** SEPARATE (speculation) or EXCISED (numerology) content; it only *references*
  lineage via the vault.
- **Nothing is deleted** by automation; QUARANTINE is reversible; the EXCISION_LEDGER records *why* each false
  item left.
- **One SSoT per artifact type** (§2); no validated result lives only in Downloads or a vault.
- Every promoted number keeps its tier and, if `[V]`, a `results/verify/` script.

*Provenance: `FTGB_COHERENCE_MAP`, `TOOLKIT_HANDBOOK` (M7–M12), `GLOSSARY.md`, `REFERENCES.md`,
`excision-protocol-storti-factor.md`. This is an organizational plan; it moves no files on its own.*
