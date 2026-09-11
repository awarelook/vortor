"""
Particle-on-a-ring quantum mechanics -- the genuine, textbook-exact quantum system this toolkit uses
to tie quantum wave mechanics to its own torus geometry, without touching the classical Beltrami field
(see quantum_hydrodynamics.py's own docstring for why that combination is deliberately avoided).

A ring of radius R is the theta-cross-section of the same torus geometry.py/beats.py already build for
the classical EM-coupling work; here it instead hosts a free quantum particle, eigenstates
psi_m(theta) = e^{i m theta} / sqrt(2 pi R), energies E_m = hbar^2 m^2 / (2 mass R^2), angular momentum
quantized by the integer winding number m -- exact, standard quantum mechanics (e.g. Griffiths,
Introduction to Quantum Mechanics, the particle-in-a-ring problem). Because Psi(theta,t) genuinely
varies over the spatial coordinate theta, this supports the real, full Madelung decomposition (spatial
density gradient, real quantum potential) that quantum_hydrodynamics.py's general functions compute.
"""
from __future__ import annotations

import numpy as np

from .quantum_hydrodynamics import HBAR, M_ELECTRON, probability_current, quantum_potential


def ring_eigenstate(m: int, theta: np.ndarray, R: float) -> np.ndarray:
    """psi_m(theta) = e^{i m theta} / sqrt(2 pi R), normalized so integral |psi_m|^2 R dtheta = 1."""
    return np.exp(1j * m * theta) / np.sqrt(2 * np.pi * R)


def ring_energy(m: int, R: float, mass: float = M_ELECTRON, hbar: float = HBAR) -> float:
    """E_m = hbar^2 m^2 / (2 mass R^2), the exact particle-on-a-ring energy spectrum."""
    return hbar**2 * m**2 / (2 * mass * R**2)


def ring_superposition(coeffs: dict, theta: np.ndarray, t: float, R: float,
                        mass: float = M_ELECTRON, hbar: float = HBAR) -> np.ndarray:
    """Psi(theta,t) = sum_m c_m * psi_m(theta) * e^{-i E_m t / hbar}, the general N-mode case."""
    psi = np.zeros(np.shape(theta), dtype=complex)
    for m, c in coeffs.items():
        E = ring_energy(m, R, mass=mass, hbar=hbar)
        psi = psi + c * ring_eigenstate(m, theta, R) * np.exp(-1j * E * t / hbar)
    return psi


def ring_density(psi: np.ndarray) -> np.ndarray:
    """rho(theta) = |Psi|^2."""
    return np.abs(psi) ** 2


def ring_phase(psi: np.ndarray) -> np.ndarray:
    """S(theta) = arg(Psi)."""
    return np.angle(psi)


def _dx(theta: np.ndarray, R: float) -> float:
    """Arclength grid spacing, assuming a uniform theta grid (np.linspace(0, 2pi, n, endpoint=False))."""
    return R * (theta[1] - theta[0])


def ring_velocity(psi: np.ndarray, theta: np.ndarray, R: float,
                   mass: float = M_ELECTRON, hbar: float = HBAR) -> np.ndarray:
    """v(theta) = j(theta) / rho(theta), the Madelung flow velocity along the ring's arclength."""
    dx = _dx(theta, R)
    rho = ring_density(psi)
    j = probability_current(psi, dx, hbar=hbar, m=mass, periodic=True)
    safe_rho = np.where(rho < 1e-300, 1e-300, rho)
    return j / safe_rho


def ring_quantum_potential(psi: np.ndarray, theta: np.ndarray, R: float,
                            mass: float = M_ELECTRON, hbar: float = HBAR) -> np.ndarray:
    """Q(theta) = -(hbar^2/2*mass) * (d^2 sqrt(rho)/dx^2) / sqrt(rho), arclength x = R*theta."""
    dx = _dx(theta, R)
    rho = ring_density(psi)
    return quantum_potential(rho, dx, hbar=hbar, m=mass, periodic=True)
