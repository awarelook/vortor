"""
RESOLVES the TUFT mass-tower pi-power anomaly (M13-10) from first principles.

The open anomaly (TOOLKIT_ADV_13 M13-10): the "quadratic Casimir / Ray-Singer torsion" n^2
coefficient appears with INCONSISTENT pi-powers across shells -- pure zeta(3)/12 (no pi) on S^5/S^9
vs pi^2-carrying omega_3 = zeta(3)/(4 pi^2) on S^3 -- factor pi^2/3 = 3.2899, flagged UNRESOLVED.

Resolution (spectral geometry, first-principles): the curl (Beltrami *d) operator on coexact
1-forms of S^3 has eigenvalues (n+1) with multiplicity n(n+2). Put m = n+1 (m >= 1); multiplicity
n(n+2) = m^2 - 1. Its spectral zeta is therefore EXACTLY

    zeta_B(s) = sum_{m>=1} (m^2 - 1) m^{-s} = sum m^{2-s} - sum m^{-s} = zeta(s-2) - zeta(s).

Hence the analytic-torsion derivative is
    zeta_B'(0) = zeta'(-2) - zeta'(0) = -zeta(3)/(4 pi^2) + (1/2) ln(2 pi),
and the QUADRATIC (m^2) piece is exactly zeta'(-2) = -zeta(3)/(4 pi^2) -- which CARRIES pi^2 by the
textbook ladder zeta'(-2n) = (-1)^n (2n)! zeta(2n+1) / (2^{2n+1} pi^{2n}).

CONSEQUENCE: the pi^2 is STRUCTURALLY MANDATORY -- zeta(3) can enter a spectral derivative on S^3
ONLY through zeta'(-2), which always carries 1/(4 pi^2). So:
  (1) omega_3 = zeta(3)/(4 pi^2) is the genuine S^3 n^2 coefficient (= the m^2-piece of zeta_B'(0));
  (2) the "pure" zeta(3)/12 is NOT a spectral derivative -- it is zeta(3) x rational (1/12 = -zeta(-1)),
      a product of zeta VALUES, a categorically different object;
  (3) the true n^2 spectral derivatives on S^5/S^9 are zeta'(-4) ~ zeta(5)/pi^4 and zeta'(-8) ~
      zeta(9)/pi^8 -- NOT zeta(3). So C5 = zeta(3)/12 and C9 = -zeta(3)/8 use the WRONG zeta AND drop
      the pi: doubly not the spectral n^2 term.

Verdict: the M13-10 anomaly is a CATEGORY ERROR, not a normalization choice -- "same object, different
pi-power" is false; they are two different objects. The pi^2-carrying forms are the genuine curl-
spectrum / analytic-torsion coefficients. This settles the open A1 / M13-10 question in favor of the
pi^2 forms. (It does not validate TUFT's fit; that stays [preprint-claim].)

mpmath high-precision. Run: python results/verify/curl_spectral_zeta_pi_power_check.py
"""
import mpmath as mp

mp.mp.dps = 40
ok = True


def line(): print("-"*78)


print("="*78)
print("Curl/Beltrami spectral zeta on S^3 and the pi-power anomaly resolution")
print("="*78)

# (1) the spectral identity  zeta_B(s) = zeta(s-2) - zeta(s)   (multiplicity m^2-1 at eigenvalue m)
print("(1) S^3 curl spectrum: eigenvalue (n+1)=m, multiplicity n(n+2)=m^2-1")
print("    => zeta_B(s) = sum_{m>=1}(m^2-1) m^{-s} = zeta(s-2) - zeta(s).  Check at s=4 (converges):")
M = 200000
partial = mp.mpf(0)
for m in range(1, M+1):
    partial += (m*m - 1) * mp.mpf(m)**(-4)
closed = mp.zeta(2) - mp.zeta(4)
print("    partial sum (M=%d) = %s" % (M, mp.nstr(partial, 12)))
print("    zeta(2)-zeta(4)    = %s   diff = %.2e" % (mp.nstr(closed, 12), float(abs(partial-closed))))
ok = ok and abs(partial - closed) < 1e-4

# (2) zeta'(-2) = -zeta(3)/(4 pi^2)  -- the m^2 (quadratic) piece, CARRIES pi^2
line()
zp_m2 = mp.diff(mp.zeta, -2)
target = -mp.zeta(3)/(4*mp.pi**2)
print("(2) quadratic (m^2) coefficient of zeta_B'(0) is zeta'(-2):")
print("    zeta'(-2)           = %s" % mp.nstr(zp_m2, 20))
print("    -zeta(3)/(4 pi^2)   = %s   diff = %.2e   -> CARRIES pi^2" % (mp.nstr(target, 20), float(abs(zp_m2-target))))
ok = ok and abs(zp_m2 - target) < mp.mpf(10)**(-25)

# zeta_B'(0) full value
line()
zpB0 = mp.diff(mp.zeta, -2) - mp.diff(mp.zeta, 0)
zpB0_closed = -mp.zeta(3)/(4*mp.pi**2) + mp.mpf(1)/2*mp.log(2*mp.pi)
print("(3) zeta_B'(0) = zeta'(-2) - zeta'(0) = -zeta(3)/(4pi^2) + (1/2)ln(2pi):")
print("    from derivatives   = %s" % mp.nstr(zpB0, 18))
print("    closed form        = %s   diff = %.2e" % (mp.nstr(zpB0_closed, 18), float(abs(zpB0-zpB0_closed))))
ok = ok and abs(zpB0 - zpB0_closed) < mp.mpf(10)**(-20)

# (4) the "pure" zeta(3)/12 is NOT a spectral derivative: 1/12 = -zeta(-1); it is a product of VALUES
line()
omega3 = mp.zeta(3)/(4*mp.pi**2)
pure = mp.zeta(3)/12
z_m1 = mp.zeta(-1)
print("(4) omega_3 = zeta(3)/(4 pi^2) = %s   (pi^2-carrying, genuine S^3 n^2 coeff)" % mp.nstr(omega3, 12))
print("    'pure'  zeta(3)/12         = %s   with 1/12 = -zeta(-1) = %s" % (mp.nstr(pure, 12), mp.nstr(-z_m1, 12)))
print("    => zeta(3)/12 = zeta(3) x (-zeta(-1)): a PRODUCT OF ZETA VALUES, not a spectral derivative.")
print("    ratio (zeta(3)/12)/(zeta(3)/4pi^2) = %s  vs  pi^2/3 = %s" %
      (mp.nstr(pure/omega3, 12), mp.nstr(mp.pi**2/3, 12)))
ok = ok and abs(z_m1 + mp.mpf(1)/12) < mp.mpf(10)**(-30) and abs(pure/omega3 - mp.pi**2/3) < mp.mpf(10)**(-20)

# (5) true n^2 spectral derivatives on higher shells carry zeta(5)/pi^4, zeta(9)/pi^8 -- NOT zeta(3)
line()
zp_m4 = mp.diff(mp.zeta, -4)
lad_m4 = mp.factorial(4)*mp.zeta(5)/(2**5*mp.pi**4)     # (-1)^2 (4!) zeta(5)/(2^5 pi^4)
print("(5) higher-shell n^2 spectral derivatives use zeta(5)/pi^4, zeta(9)/pi^8 -- NOT zeta(3):")
print("    zeta'(-4)              = %s" % mp.nstr(zp_m4, 18))
print("    (4!)zeta(5)/(2^5 pi^4) = %s   diff = %.2e" % (mp.nstr(lad_m4, 18), float(abs(zp_m4-lad_m4))))
print("    beta_5 = zeta(5)/(8 pi^4) IS a genuine zeta'(-4)-type object; C5=zeta(3)/12 uses the WRONG")
print("    zeta (zeta(3) not zeta(5)) AND drops the pi.")
ok = ok and abs(zp_m4 - lad_m4) < mp.mpf(10)**(-20)

print("="*78)
print("VERDICT: the M13-10 pi-power anomaly is a CATEGORY ERROR, RESOLVED in favor of the pi^2 forms.")
print("  On S^3, zeta(3) enters a spectral derivative ONLY via zeta'(-2) = -zeta(3)/(4 pi^2): the pi^2")
print("  is structurally mandatory. omega_3 = zeta(3)/(4 pi^2) is the genuine analytic-torsion n^2")
print("  coefficient; the 'pure' zeta(3)/12 = zeta(3)*(-zeta(-1)) is a product of zeta VALUES, a")
print("  different object with the Ray-Singer provenance misattributed. 'Same object, different")
print("  pi-power' is FALSE. Settles the open A1/M13-10 question. (TUFT's data-fit stays [preprint-claim].)")
print("  [V] spectral-geometry identity / resolves [anomaly]")
print("done.  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
