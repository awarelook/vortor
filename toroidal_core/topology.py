"""
Topological charge (Hopf linking number Q_H), ported verbatim from
frontier_calcs/greenyer_hopf_charge_exact_S3_fibers_resolved.py -- the resolution of the S517-S529
Hopf-charge investigation: trace the field's S^3 fibers in their own exact closed form (a U(1) orbit,
no ODE integration, no risk of numerical "escape" since S^3 is compact by construction), stereographically
project to R^3 from a pole chosen to avoid both fibers, then compute the ordinary Gauss linking integral
on the resulting genuinely bounded curves. Result there: Q_H=1.000000, robust from n_pts=500 to 8000,
for both the textbook Hopf map and this project's own v0/|v0| field.

n_pts default here is dropped to 400 (vs. the source script's 8000) for interactive use --
gauss_linking_number is O(n_pts^2) in both time and memory ((n_pts,n_pts,3) float64), and the source
script's own convergence sweep shows Q_H already rounds to the same integer at n_pts=500.
"""
from __future__ import annotations

import numpy as np


def fiber_S4_standard(n0, n_pts: int = 400):
    """n_standard_hopf convention: n_z = |z2|^2 - |z1|^2 (the textbook Hopf map, for validation)."""
    nx0, ny0, nz0 = n0
    A0 = np.sqrt((1 - nz0) / 2)
    B0 = (nx0 + 1j * ny0) / (2 * A0)
    thetas = np.linspace(0, 2 * np.pi, n_pts, endpoint=False)
    z1 = np.exp(1j * thetas) * A0
    z2 = np.exp(1j * thetas) * B0
    return np.stack([z1.real, z1.imag, z2.real, z2.imag], axis=1)


def fiber_S4_project(n0, n_pts: int = 400):
    """n_project_hopf (=v0/|v0|, this project's own actual field) convention: n_z = |z1|^2 - |z2|^2."""
    nx0, ny0, nz0 = n0
    A0 = np.sqrt((1 + nz0) / 2)
    B0 = (nx0 + 1j * ny0) / (2 * A0)
    thetas = np.linspace(0, 2 * np.pi, n_pts, endpoint=False)
    z1 = np.exp(1j * thetas) * A0
    z2 = np.exp(1j * thetas) * B0
    return np.stack([z1.real, z1.imag, z2.real, z2.imag], axis=1)


def stereographic_from_pole(P4pts: np.ndarray, pole: np.ndarray):
    """Project R^4 points on S^3 to R^3 stereographically from an arbitrary given pole."""
    p = pole / np.linalg.norm(pole)
    basis = []
    for cand in [np.array([1., 0, 0, 0]), np.array([0., 1, 0, 0]),
                 np.array([0., 0, 1, 0]), np.array([0., 0, 0, 1])]:
        v = cand - np.dot(cand, p) * p
        for b in basis:
            v = v - np.dot(v, b) * b
        n = np.linalg.norm(v)
        if n > 1e-8:
            basis.append(v / n)
        if len(basis) == 3:
            break
    B = np.stack(basis, axis=1)
    dot = P4pts @ p
    denom = 1 - dot
    coords_in_plane = (P4pts - dot[:, None] * p[None, :]) @ B
    return coords_in_plane / denom[:, None], denom


def gauss_linking_number(curve1: np.ndarray, curve2: np.ndarray) -> float:
    """The ordinary Gauss linking integral -- O(n^2) in both time and memory; keep n_pts modest for
    interactive use (see module docstring)."""
    r1, r2 = curve1, curve2
    dr1 = np.roll(r1, -1, axis=0) - r1
    dr2 = np.roll(r2, -1, axis=0) - r2
    m1 = r1 + 0.5 * dr1
    m2 = r2 + 0.5 * dr2
    diff = m1[:, None, :] - m2[None, :, :]
    dist3 = np.linalg.norm(diff, axis=-1) ** 3
    dist3[dist3 < 1e-12] = 1e-12
    cross = np.cross(dr1[:, None, :], dr2[None, :, :])
    integrand = np.einsum('ijk,ijk->ij', diff, cross) / dist3
    return integrand.sum() / (4 * np.pi)


def compute_Q_H(fiber_func, target1, target2, pole: np.ndarray = None, n_pts: int = 400):
    """Q_H (the Hopf linking number) between two field-line fibers over target1/target2 on S^2.

    Returns (Q_H, min_dist_from_pole) -- the second value is the source script's own sanity check that
    the chosen pole genuinely avoids both fiber circles (small values would mean the projection is
    numerically unreliable near that fiber).
    """
    if pole is None:
        pole = np.array([0., 0., 0., 1.])
    c1 = fiber_func(target1, n_pts)
    c2 = fiber_func(target2, n_pts)
    curve1, d1 = stereographic_from_pole(c1, pole)
    curve2, d2 = stereographic_from_pole(c2, pole)
    min_dist = min(np.abs(d1).min(), np.abs(d2).min())
    Lk = gauss_linking_number(curve1, curve2)
    return Lk, min_dist
