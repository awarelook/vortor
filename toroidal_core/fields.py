"""
The CK eigenvalue (sphere limit) and the Hopf-Beltrami field.

`hopf_beltrami_field` ports the exact, already-validated formula from
frontier_calcs/greenyer_hopf_field_toroidal_dipole_T_computation.py (itself cross-validated across
S488/S502/S509 in this project's own history) -- not re-derived here.

Scope note: this module covers the field itself, its curl-eigenvalue property, and its self-similar
rescaling -- all directly, cheaply testable. It does NOT reimplement the full S^3/quaternion linking-
number (Lk, Q_H) machinery from the main paper's own frontier_calcs scripts; that apparatus is
substantial and already exists, tested, in frontier_calcs/greenyer_hopf_charge_exact_S3_fibers_resolved.py
and siblings. Reuse those directly for linking-number work rather than duplicating them here.
"""
from __future__ import annotations

import numpy as np
from scipy.optimize import brentq
from scipy.special import spherical_jn


def ck_lowest_eigenvalue_sphere() -> float:
    """The lowest Chandrasekhar-Kendall eigenvalue in the spherical limit, lambda_0 * a.

    This is a genuinely computed root, not a hardcoded constant: the lowest force-free spherical
    (spheromak) mode satisfies j_1(x) = 0 for the spherical Bessel function of order 1 (equivalently
    tan(x) = x), first nontrivial root near x = 4.4934 -- matching the paper's own CK-Moffatt identity
    to six decimals.
    """
    root = brentq(lambda x: spherical_jn(1, x), 4.0, 5.0)
    return root


def v0_hopf(x: float, y: float, z: float) -> np.ndarray:
    """The Hopf tangent field's numerator vector, exact closed form."""
    return np.array(
        [
            x * z - y,
            x + y * z,
            (-(x**2) - y**2 + z**2 + 1) / 2,
        ]
    )


def hopf_lambda(r2: float) -> float:
    """The Hopf-Beltrami field's own position-dependent curl-eigenvalue, lambda(r) = 4/(1+r^2)."""
    return 4.0 / (1 + r2)


def hopf_beltrami_field(x: float, y: float, z: float) -> np.ndarray:
    """The Hopf-Beltrami field, B_hopf = v0(x,y,z) / (1+r^2)^2 -- an exact curl-eigenfield."""
    r2 = x**2 + y**2 + z**2
    return v0_hopf(x, y, z) / (1 + r2) ** 2


def curl_numeric(field, point: np.ndarray, h: float = 1e-5) -> np.ndarray:
    """Numerical curl of `field` (a function R^3 -> R^3) at `point`, central differences."""
    x, y, z = point

    def d(axis_field, i):
        p_plus = point.copy()
        p_minus = point.copy()
        p_plus[i] += h
        p_minus[i] -= h
        return (axis_field(*p_plus) - axis_field(*p_minus)) / (2 * h)

    # curl_x = dFz/dy - dFy/dz, etc.
    dFz = d(lambda a, b, c: field(a, b, c)[2], 1) - d(lambda a, b, c: field(a, b, c)[1], 2)
    dFx = d(lambda a, b, c: field(a, b, c)[0], 2) - d(lambda a, b, c: field(a, b, c)[2], 0)
    dFy = d(lambda a, b, c: field(a, b, c)[1], 0) - d(lambda a, b, c: field(a, b, c)[0], 1)
    return np.array([dFz, dFx, dFy])


def rescaled_hopf_field(x: float, y: float, z: float, a: float) -> np.ndarray:
    """The self-similar rescaling w_a(r) = w(r/a) / a, exact at every scale a.

    The field's own amplitude falls as exactly 1/a under this rescaling -- the same
    "amplitude proportional to 1/size" law this project's own ampere-turns convention predicts from
    a completely different argument (see beats.ampere_turns_ratio).
    """
    return hopf_beltrami_field(x / a, y / a, z / a) / a
