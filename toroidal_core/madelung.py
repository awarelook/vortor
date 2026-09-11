"""
The Madelung (amplitude-phase) decomposition, applied at the one consistent level this project's own
theory uses throughout: to the complex coefficients of a superposition of fixed spatial eigenmodes,
never to the underlying Beltrami field itself (which cannot be a gradient field and remain a genuine
nontrivial curl-eigenfield -- an exact incompatibility).
"""
from __future__ import annotations

import numpy as np


def superposition(c0: complex, lam0: float, c1: complex, lam1: float, t: np.ndarray) -> np.ndarray:
    """Psi(t) = c0*e^{-i*lam0*t} + c1*e^{-i*lam1*t}, the two-mode case used throughout this theory."""
    return c0 * np.exp(-1j * lam0 * t) + c1 * np.exp(-1j * lam1 * t)


def rho(psi: np.ndarray) -> np.ndarray:
    """rho = |Psi|^2 -- the beat's own energy-exchange envelope."""
    return np.abs(psi) ** 2


def phase(psi: np.ndarray) -> np.ndarray:
    """S = arg(Psi) -- sets the corresponding Madelung flow direction, grad(S)."""
    return np.angle(psi)


def madelung_velocity_1d(psi: np.ndarray, dt: float) -> np.ndarray:
    """A simple finite-difference stand-in for grad(S) along the one parameter actually varying here
    (time, for a spatially-fixed-mode superposition) -- d(phase)/dt, unwrapped to avoid 2pi jumps."""
    s = np.unwrap(phase(psi))
    return np.gradient(s, dt)
