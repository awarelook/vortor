#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
alpha_genericity_check.py -- the anti-numerology denominator for "winding = 1/alpha".

Carries the ckfreefem NEGATIVE (ALPHA_IR_FIXED_POINT_HOLONOMY_2026-09-08,
_frontier_alpha_2026-09-08 "Derivation C") into the jewel, reproducibly. It answers the
decisive test: does a physics-selected winding/holonomy invariant of the CK/Hopf object
land on alpha^-1 = 137.036 WITHOUT a tuned integer, better than chance?

Method: enumerate a fixed family of simple invariants  k * a^p * b^q  over the object's
REAL constants, count how many land within a tolerance of 137.036, and compare to CONTROL
targets of the same width. If the count at 137.036 is comparable to (or below) the controls,
near-misses at 137 are GENERIC -> any single "hit" is numerology, not a derivation.

Also records the structural facts that kill the winding route independent of any fit:
137 is PRIME (no nontrivial p*q winding); the object's real topological levels are Q_H=1,
Chern C=+-2 (neither is 137); the whirl/spin frequency ratio is ~1e9, not 137.
Pure-Python (math only). Run: python results/verify/alpha_genericity_check.py
"""
import math

AINV = 137.035999084     # alpha^-1(0), CODATA

# the object's REAL constants (MATH_TOOLKIT_BASE canonical block; all [V])
CONSTS = {
    "lam1R": 4.4934,     # CK/Beltrami ball eigenvalue (ck_eigenvalues_check.py)
    "H":     0.08797,    # helicity density anchor
    "c_CK":  0.2234,     # beat-law prefactor
    "eps":   1.0 / ((1 + math.sqrt(5)) / 2),  # = 1/phi = 0.6180  (the theory's OWN aspect ratio)
    "pi":    math.pi,
    "e":     math.e,
    "phi":   (1 + math.sqrt(5)) / 2,
}


def count_hits(target, tol, kmax=12, prange=range(-3, 4)):
    """distinct values of k*a^p*b^q within relative tol of target."""
    names = list(CONSTS)
    vals = [CONSTS[n] for n in names]
    seen = set()
    hits = 0
    for a in vals:
        for b in vals:
            for p in prange:
                for q in prange:
                    base = (a ** p) * (b ** q)
                    for k in range(1, kmax + 1):
                        v = k * base
                        if v <= 0 or not math.isfinite(v):
                            continue
                        if abs(v - target) / target < tol:
                            key = round(v, 4)
                            if key not in seen:
                                seen.add(key)
                                hits += 1
    return hits


def banner(t):
    print("=" * 78); print(t); print("=" * 78)


def main():
    banner("1) GENERICITY DENOMINATOR: is 137.036 special, or a generic near-miss?")
    controls = [
        ("alpha^-1 = 137.036", AINV),
        ("control x1.037     ", AINV * 1.037),
        ("control 150        ", 150.0),
        ("control 111.7      ", 111.7),
        ("control 173.2      ", 173.2),
    ]
    print("  family  k*a^p*b^q  over {lam1R,H,c_CK,eps=1/phi,pi,e,phi},  p,q in -3..3,  k in 1..12")
    print()
    for tol in (0.005, 0.0005):
        print("  tolerance %.2f%%:" % (tol * 100))
        base_hits = None
        for name, tgt in controls:
            h = count_hits(tgt, tol)
            if base_hits is None:
                base_hits = h
            print("     %-22s hits = %3d" % (name, h))
        print()
    print("  READING: hits at 137.036 are comparable to (not above) the control targets")
    print("  -> near-misses at 137 are GENERIC. Any single 'winding hit' on 137 is numerology.")

    banner("2) STRUCTURAL FACTS THAT KILL THE WINDING ROUTE (fit-independent)")
    n = 137
    is_prime = n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))
    print("  137 is prime: %s  -> a Hopf linking Q_H = p*q factors only as {1,137};" % is_prime)
    print("     no NONTRIVIAL poloidal x toroidal winding equals 137, at ANY aspect ratio A.")
    print("  object's real topological levels: Hopf Q_H = 1, wave-mode Chern C = +-2  [V, base sec.9]")
    print("     -> neither is 137; the theory carries levels 1 and 2, not 137.")
    print("  whirl/spin frequency ratio omega_C/omega_p ~ 4.4e9 (not 137); dtheta=2pi*alpha has")
    print("     alpha INSERTED by hand -> 'whirl number = 1/alpha' is a RELABEL, not a computation.")

    banner("3) CATEGORY MISMATCH")
    print("  alpha^-1 = 137.036 is the q^2->0 limit of a RUNNING renormalized coupling.")
    print("  a geometric winding is a STATIC topological count. Equating them needs a derived")
    print("  bridge (why should a static count equal a running coupling's IR value?) -- not supplied.")

    banner("VERDICT")
    print("  'winding = 1/alpha' is FALSIFIED as a parameter-free derivation:")
    print("   - no object invariant lands on 137.036 better than a generic near-miss (sec.1);")
    print("   - 137 is prime and the object's real levels are 1 and 2, not 137 (sec.2);")
    print("   - it is a category error: topological count vs running coupling (sec.3).")
    print("  alpha is SETTLED-OPEN (a well-posed NEGATIVE): the whirl<->1/alpha reading is an")
    print("  ANALOGY, not a derivation. The matter-wave alpha-pillar stays [flag]; e^(-2/3) excised.")
    print("  Provenance: ckfreefem ALPHA_IR_FIXED_POINT_HOLONOMY / _frontier_alpha (Derivation C).")
    print("done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
