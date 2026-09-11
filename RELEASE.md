# Releasing & archiving (posterity)

This repo is set up to be a **fixed, citable, self-verifying artifact**. Cutting a release turns the
moving repo into a permanent, DOI-addressable snapshot.

## What is already in place
- **CI reproducibility gate** — `.github/workflows/verify.yml` runs `verify_all.py` (46/46) on every push;
  the green badge is public proof the model reproduces from scratch on a clean machine.
- **Self-contained foundation** — provenance scripts vendored under `frontier_calcs/`; canonical numbers
  re-derived in-repo (`canonical_numbers_provenance_check.py`).
- **Citation metadata** — `CITATION.cff` (v1.0.0), which GitHub and Zenodo read automatically.
- **Canonical snapshot PDF** — `FTGB_GRAND_SYNTHESIS_FULL_2026-09-10.pdf` (compiled from `paper/master.md`).

## Cut the v1.0.0 release (one-time, ~5 min)
1. Confirm CI is green on the default branch (the badge in `README.md` / `START_HERE.md`).
2. The annotated tag `v1.0.0` is created in this commit. Push it: `git push origin v1.0.0`.
3. On GitHub → **Releases → Draft a new release** → choose tag `v1.0.0` → attach
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
