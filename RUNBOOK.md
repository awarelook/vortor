# RUNBOOK — cohere the local knowledge base (one-glance operational reference)

The exact commands, in order, to order the corpus safely: **dedup → quarantine → archive → share**.
Every step is **dry-run first**, **nothing is deleted by tooling**, and the validated jewel (`F:\vortor` →
GitHub) is the single source of truth. Full rationale: `KNOWLEDGE_ORDERING_PLAN_2026-09-09.md`.

## Safety principles (read once)
- ✅ **Dry-run before every `-Execute`.** The dry-run changes nothing; read its output first.
- ✅ **Quarantine = move (reversible).** Restore by moving a file back to `Downloads`.
- ✅ **Delete nothing until archived.** Only *you* delete a quarantine batch, and only after the archive
  verifies in-sync (Step 5).
- ✅ **KEEP rows are never touched.** Protected primaries (Reed/Nielsen/Storti sources) are excluded.
- ⚠️ If any dry-run output looks wrong, **stop** and edit `candidates.csv` before executing.

---

## Step 0 — Share the jewel (DONE ✅)
The validated core is already offsite on GitHub. Future pushes are one command:
```bash
cd f:/vortor && git push
```
Repo: https://github.com/awarelook/vortor · branches `main` and `ftgb-coherent-object` at the same tip.

## Step 1 — Dedup scan (read-only; refresh the manifest)
```bash
python F:\vortor\results\verify\dedup_scan.py
```
→ Writes `F:\_QUARANTINE\2026-09-09\{candidates.csv, MANIFEST.md, quarantine_move.ps1}`. **Review**
`MANIFEST.md` (summary) and spot-check big clusters in `candidates.csv`. *(Changes no files in Downloads.)*
Current batch: **900 candidates / 6.75 GB** (A=99 version-series, B=755 `(n)`-copies, D=46 byte-identical);
Tier C auto-named files are **review-only**, never moved.

## Step 2 — Quarantine (safest tier first; dry-run → execute)
```powershell
cd 'F:\_QUARANTINE\2026-09-09'
.\quarantine_move.ps1 -Tier D              # DRY-RUN: byte-identical duplicates (zero info loss)
.\quarantine_move.ps1 -Tier D -Execute     # move exact dupes  ← safest, do first
.\quarantine_move.ps1 -Tier A              # DRY-RUN: explicit version series
.\quarantine_move.ps1 -Tier A -Execute     # move version-supersessions
.\quarantine_move.ps1 -Tier All            # DRY-RUN: + (n)-copy snapshots
.\quarantine_move.ps1 -Tier All -Execute   # move the rest
```
Each `-Execute` logs to `move-log_*.txt`. **Restore anything:** move it back from
`F:\_QUARANTINE\2026-09-09\` to `C:\Users\natha\Downloads`.

## Step 3 — Archive / backup (dry-run → execute; jewel first, then offsite)
```powershell
cd F:\vortor\results\verify
.\archive_mirror.ps1                                   # DRY-RUN to G:\My Drive\FTGB_ARCHIVE (cloud)
.\archive_mirror.ps1 -Sources 'F:\vortor' -Execute     # mirror the jewel first
.\archive_mirror.ps1 -Execute                          # mirror all 5 stores + verify (in-sync == verify exit 0)
.\archive_mirror.ps1 -Dest 'E:\Backup\FTGB' -Execute   # SECOND copy to a physical external (2 copies + offsite)
```
Each source mirrors into a **named subfolder** of the destination, so `/MIR` never purges anything else.
Check the SUMMARY table: every row should read `Verify = IN-SYNC (0)`.

## Step 4 — Vaults (Obsidian) — no tooling needed
`F:\conspire`, `F:\SYNTHESIS` stay local/cloud. The vault↔jewel pointer is
`F:\conspire\Relation_Map_FTGB_Coherent_Object.md`. Keep suppression/network notes tagged `#speculation`,
out of anything cited (see the plan §3, bins ④/⑤).

## Step 5 — Delete a quarantine batch (AUTHOR-ONLY, LAST)
Only after Step 3 shows the archive **in-sync** and you have spot-checked the batch:
```powershell
# you run this by hand, deliberately — tooling never deletes:
Remove-Item -LiteralPath 'F:\_QUARANTINE\2026-09-09' -Recurse -Force   # ← only when certain + archived
```

---

## Recommended cadence
1. **Now:** Step 2 `-Tier D -Execute` (exact dupes, zero risk), then Step 3 jewel mirror.
2. **After a skim of the manifest:** Step 2 `-Tier A`, then `-Tier All`.
3. **Weekly:** re-run Step 1 to catch new dupes, re-run Step 3 to keep the archive current.
4. **Only when sure + archived:** Step 5.

## Undo cheat-sheet
| Did | Undo |
|---|---|
| quarantine move | move the file back from `F:\_QUARANTINE\…` to `Downloads` |
| `main` fast-forward (local) | `git branch -f main <old-sha>` (history intact; nothing was rewritten) |
| archive mirror | delete the named subfolder under the archive dest (source untouched) |
| bad `candidates.csv` edit | re-run `dedup_scan.py` to regenerate |

## Provenance
`dedup_scan.py`, `archive_mirror.ps1` (in `results/verify/`); `quarantine_move.ps1`, `candidates.csv`,
`MANIFEST.md` (in `F:\_QUARANTINE\2026-09-09\`); `EXCISION_LEDGER.md`, `KNOWLEDGE_ORDERING_PLAN_2026-09-09.md`
(in the jewel). *Tooling is dry-run-by-default and never deletes; deletion is a deliberate manual act.*
