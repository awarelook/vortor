"""
Stage 1 of the "framework vs. universal law" modeler app plan (2026-08-05): wraps the existing,
already-verified CK/Beltrami FEM sweep infrastructure (edp_solvers/greenyer_frontier_cCK_general_
eps_sweep.edp, greenyer_eigenvector_overlap_sample.edp, greenyer_frontier_cCK_robin_bc_sweep.edp)
so the editor_qt.py GUI can drive it interactively. This does NOT add new physics or a new solver --
every number here comes from the same FreeFEM solver already used and verified throughout
GREENYER_EXPANSION_PROGRAM_FINDINGS_LOG.md (Items 5-7). This module is scoped to the CK/Beltrami
operator family only (n=0/n=1, Dirichlet and, since Stage 2's boundary-condition-variation half,
Robin too -- see solve_point_robin). A genuinely different operator (Laplace-Beltrami on the actual
torus surface) is wrapped separately in toroidal_core.laplace_beltrami, since it needs its own
periodic-mesh machinery, not an extension of this module's disk-with-boundary solver.

c_CK is recomputed here in the CURRENT, correct normalization (Delta(lambda R)/eps, one power of
eps -- see FRACTAL_TOROIDAL_GEOMETRY_BEAT_DYNAMICS.tex sec:beatlaw), not the older
Delta(lambda R)/eps^2 convention the underlying .edp script's own cout line still prints (a pre-Pass-2
artifact in that older script, harmless since only the raw lam0/lam1 output is used here).
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

import numpy as np

from .freefem_locate import FreeFemNotFoundError, find_freefem

# Bundled locally so this package is self-contained (does not depend on the sibling frontier_calcs/
# tree, which is not part of a shared build) -- see edp_solvers/README.md for provenance.
_EDP_DIR = Path(__file__).resolve().parent / "edp_solvers"
SWEEP_EDP = _EDP_DIR / "greenyer_frontier_cCK_general_eps_sweep.edp"
OVERLAP_EDP = _EDP_DIR / "greenyer_eigenvector_overlap_sample.edp"
ROBIN_EDP = _EDP_DIR / "greenyer_frontier_cCK_robin_bc_sweep.edp"

_EIGVAL_RE = re.compile(r"lambda=([\-\d.eE+]+)")


def _run_edp(edp_path: Path, args: list[str], timeout: float = 120.0) -> str:
    freefem = find_freefem()
    if freefem is None:
        raise FreeFemNotFoundError()
    cmd = [freefem, "-nw", str(edp_path)] + args
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    return out.stdout


def solve_point(eps: float, Nm_override: int | None = None) -> dict:
    """One (lambda0, lambda1) point from the real n=0/n=1 CK/Beltrami solver. Nm_override lets the
    mesh-convergence check request a doubled mesh without editing the .edp file."""
    args = ["-eps", str(eps)]
    text = _run_edp(SWEEP_EDP, args)
    m = re.search(r"lam0=([\-\d.eE+]+)\s+lam1=([\-\d.eE+]+)", text)
    if not m:
        raise RuntimeError(f"solve_point({eps}) parse failure, raw output:\n{text}")
    lam0, lam1 = float(m.group(1)), float(m.group(2))
    cCK = (lam1 - lam0) / eps  # current, correct normalization (not the .edp's own printed value)
    return {"eps": eps, "lam0": lam0, "lam1": lam1, "cCK": cCK}


def sweep(eps_list: list[float]) -> list[dict]:
    return [solve_point(e) for e in eps_list]


def mesh_convergence_check(eps: float) -> dict:
    """Item 5's own mesh-doubling check (Nm 300->600), reused here as a live diagnostic. The shipped
    .edp hardcodes Nm=300; this check re-solves with a temporary Nm=600 copy of the same script rather
    than editing the original, so the published solver file is never touched by the app."""
    base = solve_point(eps)
    doubled_edp = SWEEP_EDP.parent / "_gui_tmp_cCK_Nm600.edp"
    text = SWEEP_EDP.read_text()
    text = text.replace("int  Nm  = 300;", "int  Nm  = 600;")
    doubled_edp.write_text(text)
    try:
        text_out = _run_edp(doubled_edp, ["-eps", str(eps)], timeout=180.0)
    finally:
        doubled_edp.unlink(missing_ok=True)
    m = re.search(r"lam0=([\-\d.eE+]+)\s+lam1=([\-\d.eE+]+)", text_out)
    if not m:
        raise RuntimeError(f"mesh_convergence_check({eps}) parse failure:\n{text_out}")
    lam0_2, lam1_2 = float(m.group(1)), float(m.group(2))
    cCK_2 = (lam1_2 - lam0_2) / eps
    rel_dev = abs(cCK_2 - base["cCK"]) / abs(base["cCK"]) if base["cCK"] else float("nan")
    return {"eps": eps, "cCK_Nm300": base["cCK"], "cCK_Nm600": cCK_2, "rel_dev_pct": rel_dev * 100}


def overlap_matrix(eps_a: float, eps_b: float, nSel: int, levels: list[int],
                    Ngrid: int = 25, rmax: float = 0.9) -> dict:
    """Item 6b's own eigenvector-overlap machinery: samples the requested levels of the n=nSel
    operator on a common normalized grid at two different eps values and returns the self/cross
    overlap matrix -- the real identity-exchange test, not just eigenvalue proximity."""
    def sample(eps):
        args = ["-eps", str(eps), "-n", str(nSel)]
        text = _run_edp(OVERLAP_EDP, args, timeout=120.0)
        blocks = {}
        cur_level, pts = None, []
        for line in text.splitlines():
            if line.startswith("EIGVEC_START"):
                cur_level = int(re.search(r"level=(\d+)", line).group(1))
                pts = []
            elif line.startswith("PT "):
                _, u, v, val = line.split()
                pts.append(float(val))
            elif line.startswith("EIGVEC_END"):
                if cur_level in levels:
                    blocks[cur_level] = np.array(pts)
                cur_level = None
        return blocks

    va = sample(eps_a)
    vb = sample(eps_b)
    n = len(levels)
    M = np.zeros((n, n))
    for i, li in enumerate(levels):
        for j, lj in enumerate(levels):
            if li not in va or lj not in vb:
                M[i, j] = float("nan")
                continue
            v1, v2 = va[li], vb[lj]
            denom = np.dot(v1, v1) * np.dot(v2, v2)
            M[i, j] = (np.dot(v1, v2) ** 2 / denom) if denom > 0 else float("nan")
    return {"eps_a": eps_a, "eps_b": eps_b, "levels": levels, "M": M}


def solve_point_robin(eps: float, kappa_wall: float) -> dict:
    """The Robin-boundary-condition variant of solve_point (Stage 2's boundary-condition-variation
    half, 2026-08-05): the SAME CK/Beltrami operator, with the strong Dirichlet constraint
    on(1,psi=0) replaced by a weak Robin condition, a finite "wall conductivity" kappa_wall added as
    a boundary integral. kappa_wall -> infinity recovers Dirichlet exactly (verified: matches
    solve_point() to 4-5 significant figures at kappa_wall=1e6-1e8); kappa_wall -> 0 recovers
    Neumann (not directly usable for n=0 -- psi=const lies in its kernel there, a real degeneracy,
    not a bug). Finding: c_CK(eps)'s shape does NOT survive this boundary-condition change -- under
    Dirichlet it has an interior MAXIMUM near eps~0.80 (Item 5); under Robin (kappa_wall=10) it has
    an interior MINIMUM near eps~0.35-0.40 instead, opposite curvature (GREENYER_EXPANSION_PROGRAM_
    FINDINGS_LOG.md, Stage 2 boundary-condition entry) -- the paper's own Dirichlet scoping was the
    right one, not an oversight."""
    args = ["-eps", str(eps), "-kappa", str(kappa_wall)]
    text = _run_edp(ROBIN_EDP, args)
    m = re.search(r"lam0=([\-\d.eE+]+)\s+lam1=([\-\d.eE+]+)", text)
    if not m:
        raise RuntimeError(f"solve_point_robin(eps={eps}, kappa={kappa_wall}) parse failure:\n{text}")
    lam0, lam1 = float(m.group(1)), float(m.group(2))
    cCK = (lam1 - lam0) / eps
    return {"eps": eps, "kappa_wall": kappa_wall, "lam0": lam0, "lam1": lam1, "cCK": cCK}


def fit_power_law(eps_arr: np.ndarray, y_arr: np.ndarray) -> dict:
    """Same fit already used for c_CK(eps)'s own published sensitivity slope: log-log linear fit,
    y ~ y0 * eps^p."""
    mask = (eps_arr > 0) & (y_arr > 0)
    log_e, log_y = np.log(eps_arr[mask]), np.log(y_arr[mask])
    p, log_y0 = np.polyfit(log_e, log_y, 1)
    y0 = np.exp(log_y0)
    pred = y0 * eps_arr[mask] ** p
    resid = y_arr[mask] - pred
    ss_res = np.sum(resid ** 2)
    ss_tot = np.sum((y_arr[mask] - np.mean(y_arr[mask])) ** 2)
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    return {"slope_p": p, "prefactor_y0": y0, "r_squared": r2}
