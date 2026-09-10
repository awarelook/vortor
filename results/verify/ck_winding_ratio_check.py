#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
ck_winding_ratio_check.py -- the CONTINUOUS winding-to-spin ratio of the force-free electron.

Closes the one gap the primality argument left. The alpha-winding negative
(alpha_genericity_check.py, ckfreefem HOLONOMY) refuted the INTEGER invariants (Q_H=1, C=+-2;
137 prime) and a FREQUENCY ratio (omega_C/omega_p ~ 4.4e9). But Reed's actual claim is the
CONTINUOUS winding-to-spin ratio (rotational transform iota) and the loop-closure TORSION
holonomy -- non-integers, immune to the primality argument. So compute them directly from the
l=1 Chandrasekhar-Kendall force-free field and report the numbers.

RESULT: iota ~ 1.05-1.11 across all flux surfaces (~1, a Hopf ring: one poloidal turn per
toroidal circuit = the Q_H=1 the corpus cited), and the per-orbit torsion holonomy is O(0.1 rad),
not 2pi/137 = 0.046 rad. The continuous route is computed-dead: the winding-to-spin ratio of the
force-free electron is ~1, NOT 137. math-only, no scipy. Run: python results/verify/ck_winding_ratio_check.py
"""
import math

LAM = 4.493409457909064     # lambda*R, first root of tan x = x (ck_eigenvalues_check.py)
AINV = 137.035999084


def j0(x): return math.sin(x) / x
def j1(x): return math.sin(x) / x**2 - math.cos(x) / x


def Bfield(r, th):
    # axisymmetric l=1 CK spheromak (curl B = lam B), R=1
    s, c = math.sin(th), math.cos(th)
    Br = 2 * j1(LAM * r) / r * c
    Bth = -s * (LAM * j0(LAM * r) - j1(LAM * r) / r)
    Bph = LAM * j1(LAM * r) * s
    return Br, Bth, Bph


def iota(r0, th0=math.pi/2, ds=3e-4, max_steps=3_000_000):
    """toroidal turns per poloidal circuit = winding-to-spin ratio (rotational transform)."""
    r, th, phi = r0, th0, 0.0
    x0, y0 = r0 * math.sin(th0), r0 * math.cos(th0)
    left = False

    def deriv(r_, th_):
        br, bth, bph = Bfield(r_, th_)
        bp = math.hypot(br, r_ * bth)
        return br / bp, bth / bp, bph / (r_ * math.sin(th_) * bp)

    for n in range(1, max_steps + 1):
        dr1, dth1, dphi1 = deriv(r, th)
        rm, thm = r + 0.5 * ds * dr1, th + 0.5 * ds * dth1
        dr2, dth2, dphi2 = deriv(rm, thm)
        r += ds * dr2; th += ds * dth2; phi += ds * dphi2
        x, y = r * math.sin(th), r * math.cos(th)
        d0 = math.hypot(x - x0, y - y0)
        if not left and d0 > 20 * ds:
            left = True
        if left and d0 < 2 * ds:
            return abs(phi / (2 * math.pi))
    return None


def torsion_holonomy(r0, th0=math.pi/2, ds=1e-3, max_steps=1_500_000):
    """per-toroidal-orbit integrated Frenet torsion (the loop-closure geometric defect)."""
    def B_cart(x, y, z):
        rho = math.hypot(x, y); r = math.hypot(rho, z)
        th = math.acos(max(-1, min(1, z / r))); ph = math.atan2(y, x)
        Br, Bth, Bph = Bfield(r, th)
        s, c, sp, cp = math.sin(th), math.cos(th), math.sin(ph), math.cos(ph)
        return (Br*s*cp + Bth*c*cp - Bph*sp,
                Br*s*sp + Bth*c*sp + Bph*cp,
                Br*c - Bth*s)
    x, y, z = r0*math.sin(th0), 0.0, r0*math.cos(th0)
    ph_tot, ph_prev, tau_int = 0.0, math.atan2(y, x), 0.0
    hist = []
    for n in range(max_steps):
        Bx, By, Bz = B_cart(x, y, z); b = math.sqrt(Bx*Bx+By*By+Bz*Bz)
        if b < 1e-14: break
        hist.append((x, y, z))
        if len(hist) > 4: hist.pop(0)
        x += ds*Bx/b; y += ds*By/b; z += ds*Bz/b
        ph = math.atan2(y, x); dph = ph - ph_prev
        dph = (dph + math.pi) % (2*math.pi) - math.pi
        ph_tot += dph; ph_prev = ph
        if len(hist) == 4:
            p0, p1, p2, p3 = hist
            d1 = tuple(p1[i]-p0[i] for i in range(3))
            a1 = tuple((p2[i]-p1[i])-d1[i] for i in range(3))
            jj = tuple(((p3[i]-p2[i])-(p2[i]-p1[i]))-a1[i] for i in range(3))
            cr = (d1[1]*a1[2]-d1[2]*a1[1], d1[2]*a1[0]-d1[0]*a1[2], d1[0]*a1[1]-d1[1]*a1[0])
            den = cr[0]**2+cr[1]**2+cr[2]**2
            if den > 1e-30:
                tau_int += (cr[0]*jj[0]+cr[1]*jj[1]+cr[2]*jj[2])/den*ds
        if abs(ph_tot) >= 2*math.pi:
            return tau_int
    return tau_int


def banner(t): print("="*76); print(t); print("="*76)


def main():
    banner("1) WINDING-TO-SPIN RATIO iota of the l=1 CK force-free field  (Reed's claim)")
    print("  lambda*R = %.6f ; iota = toroidal turns per poloidal circuit (rotational transform)\n" % LAM)
    vals = []
    for r0 in (0.30, 0.45, 0.60, 0.75):
        it = iota(r0)
        if it is None:
            print("   r0=%.2f : (degenerate)" % r0); continue
        vals.append(it)
        print("   r0=%.2f :  iota = %7.4f    (%.3f%% of 137.036 -- ~%.0fx too small)"
              % (r0, it, 100*it/AINV, AINV/it))
    mean = sum(vals)/len(vals)
    print("\n   mean iota = %.3f  ~ 1  (a Hopf ring: ONE poloidal turn per toroidal circuit = Q_H=1)" % mean)
    ok = 0.8 < mean < 1.5

    banner("2) LOOP-CLOSURE TORSION HOLONOMY per toroidal orbit  (int tau ds)")
    print("   a torsion-defect = 2 pi alpha would need a FIXED %.5f rad per loop:" % (2*math.pi/AINV))
    for r0 in (0.35, 0.50, 0.65):
        th = torsion_holonomy(r0)
        print("   r0=%.2f :  int tau ds = %+8.4f rad   (%.1fx of 2pi/137; varies+flips sign)"
              % (r0, th, abs(th)/(2*math.pi/AINV)))

    banner("VERDICT")
    print("  The CONTINUOUS winding-to-spin ratio is iota ~ 1 (not 137), and the torsion holonomy")
    print("  is O(0.1 rad), not the fixed 2pi/137. So Reed's whirl-per-orbit / torsion-defect route")
    print("  is COMPUTED-dead at the object's own force-free geometry -- closing the gap the integer")
    print("  (primality) argument left. The object's real winding is 1 = Q_H, which the theory carries.")
    print("  'winding = 1/alpha' stays a suggestive ANALOGY, not a derivation. See ALPHA_RESOLUTION_ASSESSMENT.")
    print("done.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
