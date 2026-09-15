# Releasing & archiving (posterity)

This repo is set up to be a **fixed, citable, self-verifying artifact**. Cutting a release turns the
moving repo into a permanent, DOI-addressable snapshot.

## What is already in place
- **CI reproducibility gate** — `.github/workflows/verify.yml` runs `verify_all.py` (currently 90/90;
  58/58 at the v1.1.0 tag) on every push; the green badge is public proof the model reproduces from
  scratch on a clean machine.
- **Self-contained foundation** — provenance scripts + citation stores vendored under `frontier_calcs/`;
  canonical numbers re-derived in-repo (`canonical_numbers_provenance_check.py`).
- **Citation metadata** — `CITATION.cff` (v1.1.0), which GitHub and Zenodo read automatically.
- **Canonical snapshot PDF** — `FTGB_GRAND_SYNTHESIS_FULL_2026-09-10.pdf` (compiled from `paper/master.md`).

## Tags cut so far
- **v1.0.0** (2026-09-10) — the hardening milestone: CI gate, vendored provenance, START_HERE trust map,
  `v_A` proven-quarantined (46 checks).
- **v1.1.0** (2026-09-13) — the salvage + simulation milestone: the readability/current-true pass; the
  resonator simulation (`engine/ftgb_resonator_sim.py` — the theory running in software); the corpus
  salvage layer (history/people/EVO-CMNS record, REFERENCES §1e–1j, GLOSSARY §9, vendored citation
  stores, frozen survey digests); all twelve survey folds executed (N-mode Woltjer "heartbeat generic"
  theorem, Sector-A OAM identity, settled-negatives incl. the computed π₂ = 0 monopole closure, FPUT
  winding boundary, ball-lightning closures, Eshelby zero-coupling with corrected scope) — 58 checks.

## Cut a GitHub release for the current tag (~5 min)
1. Confirm CI is green on the default branch (the badge in `README.md` / `START_HERE.md`).
2. Push the tag if not yet pushed: `git push origin v1.1.0`.
3. On GitHub → **Releases → Draft a new release** → choose the tag → attach
   `FTGB_GRAND_SYNTHESIS_FULL_2026-09-10.pdf` → publish.

## Mint a DOI (make it citable forever, via Zenodo)
1. Sign in at **https://zenodo.org** with GitHub.
2. **Zenodo → GitHub settings** → flip the `awarelook/vortor` repo **ON**.
3. Publish (or re-publish) the GitHub Release above — Zenodo automatically archives the release and
   **mints a DOI**.
4. Add the DOI badge to the top of `README.md` and the `doi:` / `identifiers:` field to `CITATION.cff`.
   (Zenodo gives a "concept DOI" that always points at the latest version — use that in the badge.)

## Optional but recommended
- **Add a `LICENSE`** — choose reuse terms (e.g. CC-BY-4.0 for the text + MIT/Apache-2.0 for the code) so
  others can build on it. Add the SPDX id to `CITATION.cff` (`license:`).
- **Freeze the environment further** — the CI already pins `numpy==2.4.6`, `mpmath==1.3.0` on CPython 3.12.
  For maximal durability, note the exact `pip freeze` in a release asset.

## Version bumps
Each substantive advance: bump `version:` + `date-released:` in `CITATION.cff`, tag `vX.Y.Z`, cut a Release
→ Zenodo mints a new versioned DOI while the concept DOI keeps pointing at "latest."
