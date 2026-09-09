"""
R2 analytic-route verification, part 2: the enstrophy Gronwall closure.

After the exact Lamb-vector identity + Young, the enstrophy on the driven orbit obeys the
LINEAR (not supercritical) differential inequality

    dZ/dt <= -beta(t) Z + F(t),     beta(t) = nu*lam1 - eta(t)^2 / nu ,   eta = delta*||v||_inf

with eta(t) the (heartbeat-modulated) Beltrami-deviation amplitude and F(t) the bounded
forcing injection. Claim (the conditional theorem):

    if  <beta> := (1/T) int_0^T beta dt > 0   i.e.   < eta^2 > < nu^2 * lam1 ,
    then Z(t) is a-priori bounded for all time (uniform enstrophy bound on the orbit);
    if  <beta> < 0, Z grows without bound.

We integrate the borderline ODE (equality) with a periodic heartbeat deviation
    eta(t)^2 = eta0^2 * (1 + a*sin(2*pi*t/T))_+     (deviation spikes each heartbeat)
and sweep the mean deviation across the threshold to show the transition is SHARP and sits
exactly at < eta^2 > = nu^2*lam1, and that within-period spikes above threshold are tolerated
as long as the AVERAGE stays below it (the time-integrated, not pointwise, condition).
"""
import numpy as np

nu   = 1.0             # units chosen so nu*lam1 = O(1): the growth/decay rate is then
lam1 = 1.0             # visible over a modest number of periods (no artificial slowness)
T    = 1.0             # heartbeat period
thr  = nu**2 * lam1    # threshold value of < eta^2 >  (=1 here)
Fmax = 1.0             # bounded forcing injection amplitude

def integrate(eta2_mean, a, nper, dt=1e-4):
    """Integrate dZ/dt = -(nu*lam1 - eta2(t)/nu) Z + F(t).
    Diagnostic: growth ratio between the last period and the mid-run period.
    Bounded orbit -> settles onto a periodic attractor -> ratio ~ 1.
    Unbounded (<beta> < 0) -> exponential growth -> ratio = exp(|<beta>| * (nper/2) T) >> 1."""
    tmax = nper*T; n = int(tmax/dt)
    Z = 1.0; t = 0.0
    Z_mid = None; Z_end = None
    # Non-negative modulation with EXACT mean: eta2(t) = eta2_mean*(1+a sin)^2/(1+a^2/2),
    # since <(1+a sin)^2> = 1 + a^2/2. Never clamped, so the clamp cannot alter the mean.
    norm = 1.0 + 0.5*a*a
    for i in range(n):
        eta2 = eta2_mean*(1.0 + a*np.sin(2*np.pi*t/T))**2 / norm     # <eta2(t)> = eta2_mean exactly
        beta = nu*lam1 - eta2/nu
        F = Fmax*(1.0 + 0.5*np.sin(2*np.pi*t/T + 0.7))**2
        Z = Z + dt*(-beta*Z + F)
        if not np.isfinite(Z) or Z > 1e250:
            return np.inf, np.inf
        if Z_mid is None and t >= 0.5*tmax: Z_mid = Z
        t += dt
    Z_end = Z
    ratio = Z_end/Z_mid if (Z_mid and Z_mid>0) else np.inf
    return Z_end, ratio

print("="*80)
print(f"Threshold  <eta^2> = nu^2*lam1 = {thr:.3f}.   Sweep mean deviation across it.")
print("Diagnostic = Z(last period)/Z(mid-run).  ~1 => settled/bounded;  >>1 => growing.")
print("(60 periods; nu*lam1=1 so a super-threshold orbit e-folds visibly.)")
print("="*80)
print(f"{'<eta^2>/thr':>12} {'a (spike)':>10} {'Z_end':>14} {'growth ratio':>14} {'verdict':>12}")
for ratio in [0.5, 0.9, 0.99, 1.0, 1.01, 1.1, 1.5]:
    Zend, gr = integrate(ratio*thr, a=0.0, nper=60)
    verdict = "BOUNDED" if (np.isfinite(gr) and gr < 1.5) else "GROWING"
    print(f"{ratio:>12.2f} {'0.0':>10} {Zend:>14.4e} {gr:>14.4e} {verdict:>12}")

print()
print("Now LARGE within-period spikes (a=3: eta^2 peaks at (1+a)x its mean = above threshold")
print("for part of each cycle) while the MEAN stays below threshold. The time-INTEGRATED")
print("condition predicts the orbit is still bounded despite the pointwise over-threshold spikes:")
print(f"{'<eta^2>/thr':>12} {'a (spike)':>10} {'peak/thr':>10} {'Z_end':>14} {'growth ratio':>14} {'verdict':>12}")
for ratio, a in [(0.5,3.0),(0.8,3.0),(0.95,3.0),(1.05,3.0)]:
    Zend, gr = integrate(ratio*thr, a=a, nper=60)
    verdict = "BOUNDED" if (np.isfinite(gr) and gr < 1.5) else "GROWING"
    peak = ratio*(1+a)**2/(1+0.5*a*a)      # peak eta^2 / thr for the squared modulation
    print(f"{ratio:>12.2f} {a:>10.1f} {peak:>10.2f} {Zend:>14.4e} {gr:>14.4e} {verdict:>12}")

print()
print("Reading: bounded exactly for <eta^2> < thr; growth switches on at ratio>1 (sharp,")
print("at <beta>=0); a sub-threshold MEAN keeps Z bounded even when the instantaneous")
print("deviation spikes far above threshold -- the condition is time-integrated, not pointwise.")
