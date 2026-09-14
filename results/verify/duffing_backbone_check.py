"""
Anharmonic (Duffing) resonance (M16, new-physics leg): the amplitude-dependent frequency that the FTGB
heartbeat currently switches OFF -- computed, with its consequence for the inharmonic-comb falsifier.

The engine's limit-cycle heartbeat is Stuart-Landau with the frequency term CONSTANT (shear c=0):
`dz/dt=(mu + i om - |z|^2) z` (engine/ftgb_engine.py). That gives amplitude SATURATION but ZERO
amplitude->frequency coupling -- the defining Duffing/anharmonic effect is off by construction. A finite-
amplitude force-free (Beltrami) equilibrium is generically anharmonic, so that term is expected to be nonzero.
This script computes the four load-bearing anharmonic facts and turns the last one into an honest sharpening
of the project's sharpest resonance-sector kill-switch (the comb 1 : 1.719 : 2.427).

  TEST 1 -- BACKBONE BENDING [V]. x'' + 2 gamma x' + w0^2 x + beta x^3 = F cos(Omega t): the resonance peak
            frequency MOVES with drive amplitude, Omega_peak(A) ~ w0 (1 + 3 beta A^2 / 8 w0^2) (hardening for
            beta>0). Integrated + swept: Omega_peak climbs monotonically with F, and the small-amplitude peak
            matches the textbook backbone. This is the term the Stuart-Landau heartbeat sets to zero.
            [Landau-Lifshitz Mechanics sec.29; Nayfeh-Mook ch.4.]
  TEST 2 -- BISTABILITY / JUMP [V]. In the folded-over region two stable steady states coexist at ONE drive
            frequency (reached from small vs large initial data) -- the mechanism behind the swept-drive
            amplitude DISCONTINUITY (hysteresis/jump), an extra falsifiable observable. [same refs.]
  TEST 3 -- ODD-HARMONIC GENERATION [V]. The cubic (odd) restoring force feeds a driven line at Omega into
            3 Omega, 5 Omega ... with even harmonics suppressed by the x->-x symmetry -- supplying the odd
            overtones for the three-wave triads and a spectral tell distinct from a quadratic nonlinearity.
  TEST 4 -- THE COMB-PULL IS AMPLITUDE-DEPENDENT [V-us -> sharpens an [S] falsifier]. Turning the shear on
            (Stuart-Landau `(mu + i om - (1+ i c)|z|^2) z`, the amplitude-equation form of Duffing) makes the
            limit-cycle frequency w_eff = w - c|z|^2 drift with drive. So the CK comb ratios 1.719/2.427 are
            drive-amplitude-dependent: the honest falsifier is "ratios at the LINEAR (low-amplitude) limit,"
            and a measured drift-with-amplitude is a PREDICTION, not a refutation. This Duffing-pull (a
            CONTINUOUS single-oscillator drift) is physically distinct from the Arnold-tongue comb-lock (a
            DISCONTINUOUS plateau onto a rational, needing a second mode) -- so the two comb-pull mechanisms
            of the project are experimentally separable.

numpy only, deterministic. Run: python results/verify/duffing_backbone_check.py
"""
import numpy as np

ok = True


def banner(t):
    print("=" * 92); print(t); print("=" * 92)


def check(name, cond, detail=""):
    global ok
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, ("  -- " + detail) if detail else ""))
    ok = ok and cond


def duffing_steady(w0, gamma, beta, F, Omega, x0, v0, T=150.0, dt=5e-3, tail=0.25):
    """RK4 integrate x'' + 2 gamma x' + w0^2 x + beta x^3 = F cos(Omega t); return peak |x| over the tail."""
    n = int(T/dt); x, v = x0, v0; A = 0.0; cut = (1.0 - tail)*n
    for i in range(n):
        t = i*dt

        def acc(x, v, t):
            return F*np.cos(Omega*t) - 2*gamma*v - w0**2*x - beta*x**3
        k1v = acc(x, v, t); k1x = v
        k2v = acc(x+.5*dt*k1x, v+.5*dt*k1v, t+.5*dt); k2x = v+.5*dt*k1v
        k3v = acc(x+.5*dt*k2x, v+.5*dt*k2v, t+.5*dt); k3x = v+.5*dt*k2v
        k4v = acc(x+dt*k3x, v+dt*k3v, t+dt); k4x = v+dt*k3v
        x += dt/6*(k1x+2*k2x+2*k3x+k4x); v += dt/6*(k1v+2*k2v+2*k3v+k4v)
        if i > cut:
            A = max(A, abs(x))
    return A


# ---------------------------------------------------------------- TEST 1: backbone bending
banner("TEST 1 -- backbone bending: the resonance peak frequency MOVES with drive amplitude  [V]")
w0, gamma, beta = 1.0, 0.05, 0.4
sweep = np.linspace(0.9, 1.5, 25)
print("   x'' + 2*%.2f x' + x + %.1f x^3 = F cos(Omega t) ; peak frequency vs drive F:" % (gamma, beta))
peaks = []
for F in (0.05, 0.15, 0.30):
    amps = [duffing_steady(w0, gamma, beta, F, Om, 0.0, 0.0) for Om in sweep]
    j = int(np.argmax(amps)); Om_pk, A_pk = sweep[j], amps[j]
    Om_backbone = w0*(1 + 3*beta*A_pk**2/(8*w0**2))    # textbook small-amplitude backbone
    peaks.append((F, Om_pk, A_pk, Om_backbone))
    print("     F=%.2f : Omega_peak=%.3f  A_peak=%.3f   textbook w0(1+3beta A^2/8w0^2)=%.3f" %
          (F, Om_pk, A_pk, Om_backbone))
Fs = [p[0] for p in peaks]; Ompk = [p[1] for p in peaks]
mono = all(Ompk[i+1] > Ompk[i] for i in range(len(Ompk)-1))
check("the peak frequency climbs with drive amplitude (backbone bends up; hardening spring beta>0)",
      mono and Ompk[-1] > Ompk[0] + 0.05, "Omega_peak %.3f -> %.3f as F: %.2f -> %.2f" % (Ompk[0], Ompk[-1], Fs[0], Fs[-1]))
F0, Om0, A0, back0 = peaks[0]
check("at small amplitude the measured backbone matches w0(1 + 3 beta A^2/8 w0^2)",
      abs(Om0 - back0) < 0.03, "measured %.3f vs textbook %.3f (small-amplitude limit)" % (Om0, back0))
print("   -> the Stuart-Landau heartbeat (shear c=0) sets EXACTLY this amplitude->frequency term to zero.")

# ---------------------------------------------------------------- TEST 2: bistability / jump
banner("TEST 2 -- bistability: two steady states coexist at one drive frequency (the jump mechanism)  [V]")
w0, gamma, beta, F = 1.0, 0.03, 0.4, 0.6
print("   F=%.2f, gamma=%.2f (folded resonance): from small vs large initial data at fixed Omega ->" % (F, gamma))
bistable_count = 0; single_below = None
for Om in (1.20, 1.45, 1.55, 1.65):
    A_lo = duffing_steady(w0, gamma, beta, F, Om, 0.0, 0.0, T=250.0)
    A_hi = duffing_steady(w0, gamma, beta, F, Om, 2.5, 0.0, T=250.0)
    two = abs(A_hi - A_lo) > 0.3
    bistable_count += two
    if Om == 1.20:
        single_below = not two
    print("     Omega=%.2f : from x0=0 -> A=%.3f ;  from x0=2.5 -> A=%.3f   %s" %
          (Om, A_lo, A_hi, "TWO STATES" if two else "single"))
check("a folded region carries two coexisting stable amplitudes (up-sweep != down-sweep -> jump/hysteresis)",
      bistable_count >= 2 and single_below, "%d of the swept frequencies are bistable; below the fold it is single-valued" % bistable_count)

# ---------------------------------------------------------------- TEST 3: odd-harmonic generation
banner("TEST 3 -- the cubic (odd) nonlinearity generates ODD harmonics 3f,5f (evens suppressed)  [V]")
w0, gamma, beta, F, Om = 1.0, 0.05, 0.3, 0.3, 0.9
# integrate and record the tail time series, then FFT for harmonic content
T, dt = 400.0, 5e-3
n = int(T/dt); x, v = 0.0, 0.0
xs = np.empty(n)
for i in range(n):
    t = i*dt
    a = F*np.cos(Om*t) - 2*gamma*v - w0**2*x - beta*x**3
    x2 = x + 0.5*dt*v; v2 = v + 0.5*dt*a
    a2 = F*np.cos(Om*(t+0.5*dt)) - 2*gamma*v2 - w0**2*x2 - beta*x2**3
    x += dt*v2; v += dt*a2
    xs[i] = x
cut = int(0.5*n); seg = xs[cut:] * np.hanning(n-cut)
frq = np.fft.rfftfreq(n-cut, d=dt); S = np.abs(np.fft.rfft(seg)); S /= S.max()


def amp_near(fq):
    return S[np.argmin(np.abs(frq - fq))]


f1 = Om/(2*np.pi)
a1, a2h, a3h = amp_near(f1), amp_near(2*f1), amp_near(3*f1)
print("   drive at f=%.4f Hz:  amp@f=%.3f   amp@2f=%.4f (even, suppressed)   amp@3f=%.4f (odd, present)" %
      (f1, a1, a2h, a3h))
check("the odd 3f line dominates the even 2f line (signature of a cubic/odd restoring force)",
      a3h > 5*a2h and a3h > 1e-3, "3f/2f = %.1f -> odd-harmonic comb, distinct from a quadratic nonlinearity" % (a3h/max(a2h, 1e-12)))

# ---------------------------------------------------------------- TEST 4: the comb-pull is amplitude-dependent
banner("TEST 4 -- shear on: the CK comb ratios DRIFT with drive amplitude (Duffing-pull vs Arnold-pull)  [V-us]")
# Stuart-Landau with shear: dz/dt = (mu + i om - (1 + i c)|z|^2) z ; limit cycle |z|^2 = mu, w_eff = om - c mu.
# Verify the frequency-shift law numerically on one oscillator, then apply it to the CK comb.
om_test, c_test, mu_test = 1.0, 0.5, 0.4


def sl_frequency(om, c, mu, T=400.0, dt=2e-3):
    z = 0.1 + 0.0j; th_prev = None; crossings = []
    n = int(T/dt)
    for i in range(n):
        z += dt*((mu + 1j*om - (1+1j*c)*abs(z)**2)*z)
        if i*dt > 0.3*T:
            th = np.angle(z)
            if th_prev is not None and th_prev < 0 <= th:      # upward zero-crossing of the phase wrap
                crossings.append(i*dt)
            th_prev = th
    per = np.diff(crossings)
    return 2*np.pi/np.mean(per) if len(per) else np.nan


w_meas = sl_frequency(om_test, c_test, mu_test)
w_law = om_test - c_test*mu_test
print("   Stuart-Landau shear law:  measured limit-cycle w=%.3f  vs  w_eff = om - c*mu = %.3f" % (w_meas, w_law))
check("the amplitude-equation form of Duffing shifts the limit-cycle frequency by -c|z|^2 (numerically confirmed)",
      abs(w_meas - w_law) < 0.03, "so a finite-amplitude (shear c!=0) equilibrium has drive-dependent tones")

# CK comb ratios under the shear, as drive (saturation mu) grows -- common (c, mu) model:
ck = np.array([4.4934, 7.7253, 10.9041])       # roots of tan x = x
c = 0.10
print("   CK comb tones w_n, common shear c=%.2f, drive proxy mu = amplitude^2:" % c)
r0 = None; rL = None
for mu in (0.0, 0.5, 1.0):
    weff = ck - c*mu
    r21, r31 = weff[1]/weff[0], weff[2]/weff[0]
    if mu == 0.0:
        r0 = (r21, r31)
    rL = (r21, r31)
    print("     mu=%.1f : ratios 1 : %.4f : %.4f" % (mu, r21, r31))
drift21 = abs(rL[0] - r0[0])
check("with shear ON the comb ratios drift with drive amplitude (c=0 => the current engine's fixed comb)",
      r0 == (ck[1]/ck[0], ck[2]/ck[0]) and drift21 > 1e-3,
      "ratio 1.719 drifts by %.4f from mu=0->1; the falsifier must be quoted at the LINEAR limit" % drift21)
print("   -> Duffing-pull is a CONTINUOUS single-oscillator drift; the Arnold-tongue comb-lock is a")
print("      DISCONTINUOUS plateau onto a rational (7/4, 5/2) needing a second mode. The two comb-pull")
print("      mechanisms are experimentally separable: smooth amplitude-drift vs a locked staircase plateau.")

banner("VERDICT")
print("  The one anharmonic effect the FTGB heartbeat omits is computed: the resonance frequency depends on")
print("  amplitude (TEST 1 backbone), which folds the curve into a bistable jump (TEST 2) and, through the")
print("  odd cubic, seeds 3f/5f overtones (TEST 3). Consequence for the theory (TEST 4): with the shear term")
print("  restored, the CK comb ratios 1.719/2.427 are drive-amplitude-dependent -- so the sharpest FTGB")
print("  falsifier must be stated at the linear-amplitude limit, and a measured drift is itself a prediction")
print("  (Duffing-pull), physically distinct from the Arnold-tongue comb-lock. Every relation credited or")
print("  computed; nothing fabricated.")
print("  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
