# `freefem/` — vendored torus-eigensolve provenance (frozen)

**What this is.** The `ε`-dependent **toroidal** Chandrasekhar–Kendall / Beltrami eigenvalues — the ones
`MATH_TOOLKIT_BASE.md` §1 and `30_CANONICAL_NUMBERS.md` §C cite as `[V, FE]` (e.g. the golden-aspect
`c_CK(1/φ) = 0.2234`, the near-degenerate doublet `λ₀(ε), λ₁(ε)` that drives the Beat Law) — are computed
with **FreeFEM** (a finite-element PDE solver), not with `numpy`. Those solver scripts originated in the
external ckfreefem corpus; they are **vendored here as frozen copies** so the provenance of every FreeFEM
number is in the repo.

**These need FreeFEM (an external binary), so they are NOT in the CI gate.** The `.edp` files are
self-contained FreeFEM programs — run standalone with:

```bash
FreeFem++ freefem/stage3_torus_doublet.edp      # the near-degenerate torus doublet lambda_0, lambda_1
FreeFem++ freefem/stage3_sphere_validate.edp    # sphere-limit validation (recovers tan x = x = 4.4934)
FreeFem++ freefem/greenyer_frontier_cCK_general_eps_sweep.edp   # c_CK(eps) sweep (-> 0.2234 at eps=1/phi)
FreeFem++ freefem/beat_smalleps_scan.edp        # small-eps beat-law scan
```

Install FreeFEM: <https://freefem.org> (or `apt install freefem++` / `brew install freefem`). `spectral_sweep.py`
is a Python *driver* that batch-runs these via FreeFEM; it additionally needs the ckfreefem `toroidal_core`
package (`freefem_locate`, mesh helpers) which is NOT vendored — use the `.edp` files directly for a clean
standalone run.

## What is covered by the CI gate WITHOUT FreeFEM

The **load-bearing** CK results are independently reproduced in the `numpy`+`mpmath` CI harness, so you do
**not** need FreeFEM to verify the core:
- the sphere / `l=1` eigenvalue **`tan x = x` roots** (`4.4934, …`) and the **`ε→0` limit `c_CK = 1/(2 j₀,₁)
  = 0.20792`** — `results/verify/ck_eigenvalues_check.py` `[V]`;
- the **carrier-comb ratios** `1 : 1.719 : 2.427` — same script.

FreeFEM is needed only to reproduce the **finite-`ε` torus** numbers (`0.2234`, the doublet split) — a
`[V, FE]` refinement, not part of the CI-gated core. `30_CANONICAL_NUMBERS.md` §C carries both conventions
with the `ε` flag.

## Manifest

| Script | Produces | Standalone? |
|---|---|---|
| `stage3_torus_doublet.edp` | near-degenerate doublet `λ₀(ε), λ₁(ε)` on the torus (Beat-Law source) | ✓ `FreeFem++` |
| `stage3_sphere_validate.edp` | sphere-limit validation (recovers `tan x = x`) | ✓ `FreeFem++` |
| `greenyer_frontier_cCK_general_eps_sweep.edp` | `c_CK(ε)` sweep → `0.2234` at `ε=1/φ` | ✓ `FreeFem++` |
| `beat_smalleps_scan.edp` | small-`ε` beat-law scan | ✓ `FreeFem++` |
| `spectral_sweep.py` | Python driver batching the above (needs `toroidal_core`, not vendored) | ✗ driver |
