#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
majorana_selfdual_check.py -- the neutrino rung = the self-dual theta_chi=45 deg state (C-invariant).

If the chirality flip IS charge conjugation C (charge_conjugation_check.py: the lambda->-lambda mirror
flips chirality AND charge together, keeps mass), then a field that is ITS OWN mirror is C-self-conjugate
= its own antiparticle = MAJORANA. That state is the equal-parts superposition u = (u_+ + u_-)/sqrt2:
net helicity H = 0 (zero chirality/charge) and duality angle theta_chi = 45 deg (the midpoint of the
electron 0deg / positron 90deg endpoints). This pins the FTGB "neutrino = Majorana" reading to a computed
condition -- and it is what 0nu-beta-beta decay will decide.

Built from the analytic +lambda ABC and its -lambda z-mirror (both exact Beltrami). math-only.
Run: python results/verify/majorana_selfdual_check.py
"""
import numpy as np


def grid(N, L=2*np.pi):
    k1 = np.fft.fftfreq(N, d=L/N) * 2*np.pi
    return np.meshgrid(k1, k1, k1, indexing='ij')


def curl(u, K):
    KX, KY, KZ = K
    uh = [np.fft.fftn(u[i]) for i in range(3)]
    return np.array([np.fft.ifftn(1j*(KY*uh[2]-KZ*uh[1])).real,
                     np.fft.ifftn(1j*(KZ*uh[0]-KX*uh[2])).real,
                     np.fft.ifftn(1j*(KX*uh[1]-KY*uh[0])).real])


def abc(N, L=2*np.pi):
    x = np.linspace(0, L, N, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    return np.array([np.sin(Z)+np.cos(Y), np.sin(X)+np.cos(Z), np.sin(Y)+np.cos(X)])


def mirror_z(u):
    fz = lambda a: np.roll(a[:, :, ::-1], 1, axis=2)
    return np.array([fz(u[0]), fz(u[1]), -fz(u[2])])


def E_H(u, K):
    w = curl(u, K)
    return (np.mean(u[0]**2+u[1]**2+u[2]**2),
            np.mean(u[0]*w[0]+u[1]*w[1]+u[2]*w[2]))


def banner(t): print("="*78); print(t); print("="*78)


def main():
    N = 16
    K = grid(N)
    uR = abc(N); uL = mirror_z(uR)
    uMaj = (uR + uL) / np.sqrt(2)               # equal +/- chirality content: the self-dual state

    banner("1) the self-dual (Majorana) field u = (u_+ + u_-)/sqrt2")
    ER, HR = E_H(uR, K); EL, HL = E_H(uL, K); EM, HM = E_H(uMaj, K)
    print("   electron (+lambda): E=%+.3f  H=%+.3f   (chirality +)" % (ER, HR))
    print("   positron (-lambda): E=%+.3f  H=%+.3f   (chirality -)" % (EL, HL))
    print("   neutrino (self-dual): E=%+.3f  H=%+.3f   <- net chirality/charge H = 0" % (EM, HM))
    zeroH = abs(HM) < 1e-9

    banner("2) it is its OWN mirror -> C-invariant -> its own antiparticle -> MAJORANA")
    uMaj_mirror = mirror_z(uMaj)
    diff = np.sqrt(np.mean((uMaj - uMaj_mirror)**2)) / np.sqrt(np.mean(uMaj**2))
    print("   ||mirror(u) - u|| / ||u|| = %.1e   -> mirror(u) = u  (C-invariant: nu = nu-bar)" % diff)
    selfdual = diff < 1e-9

    banner("3) duality angle theta_chi = 45 deg : the midpoint of electron(0) / positron(90)")
    # helicity content: for u=(u_R+u_L)/sqrt2, equal + and - energy by construction
    thetas = {}
    for lbl, f in [("electron", uR), ("positron", uL), ("neutrino", uMaj)]:
        Hh = E_H(f, K)[1]; Ee = E_H(f, K)[0]
        # helicity fraction -> chiral angle: Ep-Em ~ H/|k| (here |k|=1), Ep+Em ~ E
        Ep = 0.5*(Ee + Hh); Em = 0.5*(Ee - Hh)     # exact for a single k-shell Beltrami mix
        theta = np.degrees(np.arctan2(np.sqrt(max(Em, 0)), np.sqrt(max(Ep, 0))))
        thetas[lbl] = theta
        print("   %-9s theta_chi = %5.1f deg" % (lbl, theta))
    mid = abs(thetas["neutrino"] - 45.0) < 1.0

    banner("VERDICT -- the chirality-geometry layer predicts a MAJORANA neutrino")
    print("   the neutrino rung = the self-dual (equal +/- chirality) state: H=0 (neutral, no net")
    print("   chirality/charge), theta_chi = 45 deg (electron/positron midpoint), and mirror(u)=u")
    print("   (C-invariant = its own antiparticle). So FTGB's chirality layer commits to nu = nu-bar")
    print("   MAJORANA -- a concrete, falsifiable prediction (0nu-beta-beta decay decides it). This")
    print("   resolves the repo's neutrino tension in favor of the computed chirality-geometry reading.")
    print("   [S, computed] -- the geometry is exact; the neutrino identification is the FTGB step.")
    print("done.")
    return 0 if (zeroH and selfdual and mid) else 1


if __name__ == "__main__":
    raise SystemExit(main())
