#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
chirality_helicity_check.py -- SHOW the math: chirality = sign of the Beltrami lambda.

Not an appeal to anybody's acceptance -- a computation. For a force-free (Beltrami) field
curl u = lambda u, the helicity H = int u . curl u = lambda int |u|^2, so sign(H) = sign(lambda)
EXACTLY: the two handednesses (+/- lambda) are the two chiralities, and the parity mirror swaps
them. FTGB reads antiparticle = opposite chirality = the -lambda partner. This script demonstrates
all of it on real fields, and gives the "duality angle" a concrete computed definition (the chiral
mixing angle of a superposition).

What this establishes [credited: Beltrami/Moffatt helicity] / [S: the antiparticle reading]:
  1. curl(ABC) = +ABC  -> H > 0  (right-handed / one chirality)
  2. parity mirror     -> curl = -u, H < 0  (left-handed / the other chirality = antiparticle)
  3. duality angle theta_chi = atan(||u_-||/||u_+||): pure particle 0, pure antiparticle pi/2,
     a mix in between -- the chiral angle TIED TO A COMPUTED QUANTITY, not left as analogy.

Separately (stated, not conflated): Reed's torsion is a FRAME-CLOSURE HOLONOMY defect (the Frenet
torsion holonomy computed in ck_winding_ratio_check.py, ~O(0.1 rad)) -- NOT Einstein-Cartan
spacetime torsion. Different objects; kept distinct. numpy-only.
Run: python results/verify/chirality_helicity_check.py
"""
import numpy as np


def grid(N, L=2*np.pi):
    k1 = np.fft.fftfreq(N, d=L/N) * 2*np.pi
    KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij')
    return (KX, KY, KZ)


def curl(u, K):
    KX, KY, KZ = K
    uh = [np.fft.fftn(u[i]) for i in range(3)]
    wx = np.fft.ifftn(1j*(KY*uh[2] - KZ*uh[1])).real
    wy = np.fft.ifftn(1j*(KZ*uh[0] - KX*uh[2])).real
    wz = np.fft.ifftn(1j*(KX*uh[1] - KY*uh[0])).real
    return np.array([wx, wy, wz])


def abc(N, L=2*np.pi):
    x = np.linspace(0, L, N, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    return np.array([np.sin(Z)+np.cos(Y), np.sin(X)+np.cos(Z), np.sin(Y)+np.cos(X)])  # curl u = u


def mirror_z(u):
    """parity reflection in the z=0 plane (improper, det=-1): flips helicity."""
    fz = lambda a: np.roll(a[:, :, ::-1], 1, axis=2)     # z_k -> -z_k on the periodic grid
    return np.array([fz(u[0]), fz(u[1]), -fz(u[2])])


def helicity(u, K):
    w = curl(u, K)
    H = np.mean(u[0]*w[0] + u[1]*w[1] + u[2]*w[2])
    E = np.mean(u[0]**2 + u[1]**2 + u[2]**2)
    return H, E


def helical_content(u, K):
    """||u_+||^2, ||u_-||^2 : energy in each helicity via the h_+/- basis per mode."""
    KX, KY, KZ = K
    uh = np.array([np.fft.fftn(u[i]) for i in range(3)])
    N = u.shape[1]
    Ep = Em = 0.0
    kk = np.stack([KX, KY, KZ], axis=-1)
    for idx in np.ndindex(N, N, N):
        k = kk[idx]; km = np.linalg.norm(k)
        if km < 1e-9:
            continue
        khat = k/km
        ref = np.array([0., 0., 1.]) if abs(khat[2]) < 0.9 else np.array([1., 0., 0.])
        e1 = np.cross(khat, ref); e1 /= np.linalg.norm(e1)
        e2 = np.cross(khat, e1)
        hp = (e1 + 1j*e2)/np.sqrt(2); hm = (e1 - 1j*e2)/np.sqrt(2)
        uvec = uh[(slice(None),)+idx]
        ap = np.vdot(hp, uvec); am = np.vdot(hm, uvec)      # projections
        Ep += abs(ap)**2; Em += abs(am)**2
    return Ep, Em


def banner(t): print("="*78); print(t); print("="*78)


def main():
    N = 16
    K = grid(N)

    banner("1) chirality = sign of the Beltrami lambda = sign of helicity  [credited, COMPUTED]")
    uR = abc(N)
    wR = curl(uR, K)
    lamR = np.mean(uR[0]*wR[0]+uR[1]*wR[1]+uR[2]*wR[2]) / np.mean(uR[0]**2+uR[1]**2+uR[2]**2)
    HR, ER = helicity(uR, K)
    resid = np.mean((wR - lamR*uR)**2)**0.5 / np.mean(uR**2)**0.5
    print("  ABC field:  curl u = lambda u  with lambda = %+.4f  (Beltrami residual %.1e)" % (lamR, resid))
    print("  helicity H = <u.curl u> = %+.4f = lambda * <|u|^2> (=%+.4f)  ->  sign(H)=sign(lambda)=+"
          % (HR, lamR*ER))

    banner("2) parity mirror -> opposite lambda -> the OTHER chirality = antiparticle  [S, COMPUTED]")
    uL = mirror_z(uR)
    wL = curl(uL, K)
    lamL = np.mean(uL[0]*wL[0]+uL[1]*wL[1]+uL[2]*wL[2]) / np.mean(uL[0]**2+uL[1]**2+uL[2]**2)
    HL, EL = helicity(uL, K)
    print("  mirror(ABC): curl u = lambda u  with lambda = %+.4f  ->  H = %+.4f  (sign flipped)" % (lamL, HL))
    print("  the +lambda and -lambda fields are mirror images = the two chiralities;")
    print("  FTGB reads antiparticle = opposite chirality = the -lambda partner  [S].")

    banner("3) the DUALITY ANGLE, tied to a computed quantity: chiral mixing theta_chi")
    print("  theta_chi = atan( ||u_-|| / ||u_+|| ) : pure particle 0, pure antiparticle pi/2.")
    for label, field in [("pure +lambda (ABC)      ", uR),
                         ("pure -lambda (mirror)   ", uL),
                         ("mix 0.8*(+) + 0.6*(-)   ", 0.8*uR + 0.6*mirror_z(uR))]:
        Ep, Em = helical_content(field, K)
        theta = np.degrees(np.arctan2(np.sqrt(Em), np.sqrt(Ep)))
        print("   %s  ||u_+||^2=%7.2f  ||u_-||^2=%7.2f  theta_chi = %5.1f deg" % (label, Ep, Em, theta))
    print("  -> the FTGB 'duality/chiral angle' is the helicity-content mixing angle -- COMPUTED,")
    print("     not analogy. Electron/positron are the theta_chi = 0 / 90 deg endpoints of one field.")

    banner("WHAT WORKS (math) vs WHAT DOESN'T -- by test, not by acceptance")
    print("  WORKS: chirality = sign(lambda) = sign(H)  [credited: Beltrami/Moffatt] -- exact identity above.")
    print("         antiparticle = -lambda mirror, duality angle = theta_chi  [S] -- computed above.")
    print("  DISTINCT (not conflated): Reed torsion = frame-closure HOLONOMY defect (Frenet holonomy")
    print("         ~O(0.1 rad), ck_winding_ratio_check.py) -- NOT Einstein-Cartan spacetime torsion.")
    print("  FAILS (a MATH test, genericity -- not 'unaccepted'): alpha from winding/large-number ratios")
    print("         -- alpha_genericity_check.py shows hits near 137 are as dense as at control targets.")
    print("  The large ratio omega_C/omega_p is a real SCALE HIERARCHY (a feature to explain), never a")
    print("  derivation of 137: a big number is only meaningful if it beats the genericity denominator.")
    print("done.")
    return 0 if (HR > 0 and HL < 0 and abs(lamR-1) < 0.05) else 1


if __name__ == "__main__":
    raise SystemExit(main())
