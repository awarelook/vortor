"""
General-purpose Madelung/Bohm quantum-hydrodynamics utilities: the quantum potential and probability
current for an arbitrary 1D complex wavefunction on a grid.

Deliberately separate from `madelung.py`: that module applies the amplitude-phase decomposition only
to the complex coefficients of a superposition of fixed spatial eigenmodes (a beat's own time-domain
envelope), and its own docstring is explicit that it must never be applied to the underlying classical
Beltrami field itself -- a genuine curl-eigenfield cannot also be a gradient field, an exact
incompatibility. This module is for a different, genuinely spatial quantum-mechanical wavefunction
(see `quantum_ring.py` for the concrete case used in this toolkit); it does not generalize or replace
`madelung.py`.

`quantum_potential_scale` is ported verbatim (formula and default constants) from
frontier_calcs/madelung_quantum_hydrodynamics_scale_check.py, which already established, with real
numbers, that this quantum potential is negligible (Q/kT ~ 1e-14 to 1e-18) at every macroscopic scale
this project's own Greenyer-lineage work operates at, but significant (Q/kT ~ 147) at the atomic scale
relevant to the separate dislocation-core Coulomb-crystal project -- a scale-dependent verdict, not a
blanket one.
"""
from __future__ import annotations

import numpy as np

HBAR = 1.054571817e-34
M_ELECTRON = 9.1093837015e-31
K_B = 1.380649e-23


def quantum_potential(rho: np.ndarray, dx: float, hbar: float = HBAR, m: float = M_ELECTRON,
                       periodic: bool = True) -> np.ndarray:
    """Q = -(hbar^2 / 2m) * (Laplacian sqrt(rho)) / sqrt(rho), 1D finite-difference Laplacian.

    `periodic=True` uses np.roll for the Laplacian stencil (matching the periodic-ring use case in
    quantum_ring.py); `periodic=False` uses one-sided differences at the two endpoints.
    """
    sqrt_rho = np.sqrt(rho)
    if periodic:
        lap = (np.roll(sqrt_rho, -1) - 2 * sqrt_rho + np.roll(sqrt_rho, 1)) / dx**2
    else:
        lap = np.empty_like(sqrt_rho)
        lap[1:-1] = (sqrt_rho[2:] - 2 * sqrt_rho[1:-1] + sqrt_rho[:-2]) / dx**2
        lap[0] = (sqrt_rho[2] - 2 * sqrt_rho[1] + sqrt_rho[0]) / dx**2
        lap[-1] = (sqrt_rho[-1] - 2 * sqrt_rho[-2] + sqrt_rho[-3]) / dx**2
    safe_sqrt_rho = np.where(sqrt_rho < 1e-300, 1e-300, sqrt_rho)
    return -(hbar**2 / (2 * m)) * lap / safe_sqrt_rho


def probability_current(psi: np.ndarray, dx: float, hbar: float = HBAR, m: float = M_ELECTRON,
                         periodic: bool = True) -> np.ndarray:
    """j = (hbar/m) * Im(psi* dpsi/dx), the standard probability-current density."""
    if periodic:
        dpsi = (np.roll(psi, -1) - np.roll(psi, 1)) / (2 * dx)
    else:
        dpsi = np.empty_like(psi)
        dpsi[1:-1] = (psi[2:] - psi[:-2]) / (2 * dx)
        dpsi[0] = (psi[1] - psi[0]) / dx
        dpsi[-1] = (psi[-1] - psi[-2]) / dx
    return (hbar / m) * np.imag(np.conj(psi) * dpsi)


def quantum_potential_scale(L: float, m: float = M_ELECTRON, hbar: float = HBAR) -> float:
    """Dimensional estimate of the quantum potential's natural magnitude for a density field varying
    over length scale L: Q ~ hbar^2 / (2 m L^2). Ported from this project's own already-validated
    frontier_calcs/madelung_quantum_hydrodynamics_scale_check.py (S370)."""
    return hbar**2 / (2 * m * L**2)
