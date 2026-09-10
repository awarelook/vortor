#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
r2_reference_solver.py -- execute-ready REFERENCE PIPELINE for the R2 numerical run.

Turns the prose hand-off (HANDOFF_R2_ENSTROPHY_REGULARITY) into working code: a pseudo-spectral
3D incompressible Navier-Stokes solver on a periodic box, driven toward a force-free Beltrami
(near-Beltrami) state, instrumented with the EXACT R2 diagnostics -- enstrophy Z(t), sup-vorticity
||omega||_inf(t), the Beltrami deviation delta(t) = <|v x omega|>/(<|v|><|omega|>), and the running
Beale-Kato-Majda integral BKM = int ||omega||_inf dt.

*** THIS IS A PIPELINE DEMONSTRATION, NOT THE PHYSICS RESULT. ***
At the tiny default resolution (N=32) and modest Reynolds number it is LAMINAR -- boundedness of Z
is trivial and expected there, and proves nothing about R2. The R2 question lives at the object's
Lundquist number S ~ 1e3-1e4 (N ~ 192-1024), which needs a GPU and long runs (see
R2_NUMERICAL_RUN_SPEC_2026-09-10.md). This script exists so a collaborator SCALES it (N, duration,
GPU FFT) rather than starts from scratch: the scheme, the near-Beltrami drive, and the success/
failure diagnostics are all here and verified to run.

Method: rotational form dv/dt = P[v x omega] - nu k^2 v + F, Leray projector P = I - kk/k^2,
2/3 dealiasing, integrating-factor Heun (IF-RK2). ABC forcing (a Beltrami field, curl F = k_f F)
holds large scales near force-free; an optional relaxation term -gamma P[curl v - lambda v] is the
high-Re knob the spec calls for. numpy-only. Run: python handoffs/r2_reference_solver.py
"""
import numpy as np


def setup(N, L=2 * np.pi):
    k1 = np.fft.fftfreq(N, d=L / N) * 2 * np.pi
    KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij')
    K2 = KX**2 + KY**2 + KZ**2
    K2i = 1.0 / np.where(K2 == 0, 1.0, K2)
    kmax = np.max(np.abs(k1))
    dealias = ((np.abs(KX) <= 2/3 * kmax) & (np.abs(KY) <= 2/3 * kmax) & (np.abs(KZ) <= 2/3 * kmax))
    return (KX, KY, KZ), K2, K2i, dealias


def curl_hat(vh, K):
    KX, KY, KZ = K
    ux, uy, uz = vh
    wx = 1j * (KY * uz - KZ * uy)
    wy = 1j * (KZ * ux - KX * uz)
    wz = 1j * (KX * uy - KY * ux)
    return np.array([wx, wy, wz])


def leray(fh, K, K2i):
    KX, KY, KZ = K
    div = KX * fh[0] + KY * fh[1] + KZ * fh[2]
    return np.array([fh[i] - [KX, KY, KZ][i] * div * K2i for i in range(3)])


def abc_forcing(N, A=1.0, L=2*np.pi):
    x = np.linspace(0, L, N, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    fx = A * (np.sin(Z) + np.cos(Y))
    fy = A * (np.sin(X) + np.cos(Z))
    fz = A * (np.sin(Y) + np.cos(X))          # curl F = F : a k_f=1 Beltrami field
    return np.array([np.fft.fftn(fx), np.fft.fftn(fy), np.fft.fftn(fz)])


def rhs(vh, K, K2i, dealias, Fh, lam, gamma):
    # nonlinear rotational form: v x omega, dealiased, Leray-projected
    wh = curl_hat(vh, K)
    v = np.array([np.fft.ifftn(vh[i]).real for i in range(3)])
    w = np.array([np.fft.ifftn(wh[i]).real for i in range(3)])
    lamb = np.array([v[1]*w[2] - v[2]*w[1], v[2]*w[0] - v[0]*w[2], v[0]*w[1] - v[1]*w[0]])
    lh = np.array([np.fft.fftn(lamb[i]) * dealias for i in range(3)])
    N_ = leray(lh, K, K2i) + Fh
    if gamma > 0.0:                            # optional near-Beltrami relaxation (the high-Re knob)
        resid = wh - lam * vh                  # curl v - lambda v  (zero for Beltrami)
        N_ = N_ - gamma * leray(resid, K, K2i)
    return N_


def diagnostics(vh, K, N):
    wh = curl_hat(vh, K)
    v = np.array([np.fft.ifftn(vh[i]).real for i in range(3)])
    w = np.array([np.fft.ifftn(wh[i]).real for i in range(3)])
    E = 0.5 * np.mean(v[0]**2 + v[1]**2 + v[2]**2)
    Z = 0.5 * np.mean(w[0]**2 + w[1]**2 + w[2]**2)
    wmag = np.sqrt(w[0]**2 + w[1]**2 + w[2]**2)
    w_inf = np.max(wmag)
    lamb = np.array([v[1]*w[2]-v[2]*w[1], v[2]*w[0]-v[0]*w[2], v[0]*w[1]-v[1]*w[0]])
    lmag = np.sqrt(lamb[0]**2 + lamb[1]**2 + lamb[2]**2)
    vmag = np.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    delta = np.mean(lmag) / (np.sqrt(np.mean(vmag**2)) * np.sqrt(np.mean(wmag**2)) + 1e-30)
    return E, Z, w_inf, delta


def main():
    N, nu, lam, gamma = 32, 0.05, 1.0, 0.0     # laminar demo; gamma=0 (ABC forcing only)
    dt, T = 0.005, 20.0
    K, K2, K2i, dealias = setup(N)
    abc = abc_forcing(N, A=1.0)                 # the ABC/Beltrami field (k_f=1, curl u = u), spectral
    Fh = nu * abc                              # forcing that sustains ABC against viscous decay
    rng = np.random.default_rng(0)
    pert = leray(np.array([np.fft.fftn(0.1 * rng.standard_normal((N, N, N))) for _ in range(3)]), K, K2i)
    vh = abc + pert                            # start near-Beltrami, with a small perturbation
    Evisc = np.exp(-nu * K2 * dt)

    print("=" * 78)
    print("  R2 REFERENCE PIPELINE (N=%d, nu=%.3g, ABC k_f=1, gamma=%.2g) -- DEMO, not the run" % (N, nu, gamma))
    print("  laminar Re; watching: Z(t) bounded plateau? delta(t) small (near-Beltrami)? BKM ~ linear?")
    print("=" * 78)
    print("    t      E        Z(enstr)   ||w||_inf   delta(Beltrami dev)   BKM=int|w|inf dt")
    nsteps = int(T / dt); bkm = 0.0
    for n in range(nsteps + 1):
        E, Z, w_inf, delta = diagnostics(vh, K, N)
        if n % int(2.0/dt) == 0:
            print("  %5.1f  %.4f   %8.3f   %8.3f      %.4f              %8.3f"
                  % (n*dt, E, Z, w_inf, delta, bkm))
        bkm += w_inf * dt
        # IF-RK2 (Heun with integrating factor)
        a1 = rhs(vh, K, K2i, dealias, Fh, lam, gamma)
        vstar = Evisc * (vh + dt * a1)
        a2 = rhs(vstar, K, K2i, dealias, Fh, lam, gamma)
        vh = Evisc * vh + 0.5 * dt * (Evisc * a1 + a2)

    print("=" * 78)
    print("  READING (demo): if Z(t) settles to a bounded plateau, delta stays small (flow held")
    print("  near-Beltrami), and BKM grows ~linearly (bounded ||w||_inf), the pipeline + diagnostics")
    print("  are working and ready to SCALE. Boundedness HERE is laminar-trivial and proves nothing")
    print("  about R2 -- the test is the same plateau vs secular growth at S~1e3-1e4 (see RUN_SPEC).")
    print("done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
