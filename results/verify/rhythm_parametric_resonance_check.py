"""
Rhythm dynamics & parametric resonance (M16): the load-bearing relations, computed -- with the honest
frequency-matching constraint that disciplines the FTGB cross-scale claim.

Rhythm dynamics is how repeated motion organizes in time: Fourier components, harmonics, beats, resonance,
entrainment, parametric (Mathieu) subharmonics, nonlinear mixing. This script computes the FIVE relations
that are load-bearing for the FTGB coherent object -- four are the standard toolkit (grounding the CK comb,
the beat, the driven heartbeat, the comb-lock), and the fifth is an honest SETTLED-NEGATIVE that sharpens the
project's cross-scale fence.

  TEST 1 -- BEAT != FOURIER LINE [credited]. Two close lines A cos(w1 t)+A cos(w2 t) = 2A cos(w_b t/2)
            cos(w_c t), w_b=|w2-w1|. A LINEAR signal has NO spectral line at w_b; a QUADRATIC (energy/
            intensity/stress/torque) observable I ~ x^2 DOES contain a real line at w_b. So the FTGB kHz
            beat is a NONLINEAR/ENERGY observable, not a linear field line -- exactly how the resonator sim
            extracts it (FFT-Hilbert envelope) and how a physical detector would see it. [Feynman I-48.]
  TEST 2 -- PARAMETRIC (Mathieu) SUBHARMONIC [credited]. x'' + 2 gamma x' + w0^2[1+h cos(Omega t)]x = 0 has
            its principal instability tongue at Omega ~ 2 w0 (response ~ Omega/2), NOT at Omega ~ w0, with
            onset threshold h_th ~ 2/Q (Q = w0/2 gamma). Grounds the FTGB driven "heartbeat" / parametric
            drive and the M14 Floquet-Mathieu threshold eta_c = 2/Q. [Mathieu; Nayfeh multiple-scales.]
  TEST 3 -- ADLER ENTRAINMENT [credited]. dpsi/dt = Delta_w - K sin psi locks (psi -> const) iff
            |Delta_w| <= K (Arnold-tongue half-width K), and phase-slips outside. Grounds the FTGB
            Kuramoto/Adler comb-lock (M14). [Adler 1946; Pikovsky-Rosenblum-Kurths.]
  TEST 4 -- THE FREQUENCY-MATCHING CONSTRAINT [settled-NEGATIVE, sharpens the fence]. Parametric pumping of a
            mode needs a SUM-frequency match Omega ~ w_j + w_k (Omega ~ 2 w0 for a degenerate pair) -- a slow
            DIFFERENCE (beat) frequency w_b fails this. Computed: the FTGB kHz comb beat (w_b ~ 2 pi 87 kHz)
            is ~16 ORDERS too slow to parametrically pump a MeV nuclear mode (w_nuc ~ 1.5e21 rad/s). So the
            "cross-scale Delta identity (kHz detuning <-> MeV gap)" is a settled-negative FOR THE
            PARAMETRIC-PUMP MECHANISM: if any cross-scale link exists it must be a genuinely slow
            nuclear-adjacent collective mode or a different mechanism -- NOT the beat parametrically pumping
            the gap. (Does NOT touch the [V]/conserved d+d->4He energy ledger, which is separate.)
  TEST 5 -- THE CK COMB IS INHARMONIC [V]. Real resonators have w_n != n w_1; the CK comb (roots of tan x=x)
            gives ratios 1 : 1.719 : 2.427, NOT the harmonic 1:2:3 -- the FTGB spectral fingerprint (a
            harmonic 1:2:3 lock would falsify the Beltrami-carrier reading). [Chandrasekhar-Kendall 1957.]

numpy only, deterministic. Run: python results/verify/rhythm_parametric_resonance_check.py
"""
import numpy as np

ok = True


def banner(t):
    print("=" * 92); print(t); print("=" * 92)


def check(name, cond, detail=""):
    global ok
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, ("  -- " + detail) if detail else ""))
    ok = ok and cond


# ---------------------------------------------------------------- TEST 1: beat != Fourier line
banner("TEST 1 -- the beat is a NONLINEAR/energy observable, not a linear Fourier line  [credited]")
f1, f2 = 120.0, 124.0
fb = abs(f2 - f1)
T, n = 8.0, 1 << 15
t = np.linspace(0, T, n, endpoint=False)
x = np.cos(2*np.pi*f1*t) + np.cos(2*np.pi*f2*t)
frq = np.fft.rfftfreq(n, d=T/n)


def amp_at(sig, f0):
    S = np.abs(np.fft.rfft(sig))
    return S[np.argmin(np.abs(frq - f0))] / np.max(S)


lin_fb = amp_at(x, fb)
quad_fb = amp_at(x**2, fb)
print("   linear x(t):   amp @ f_b = %.4f (~0)   amp @ f1 = %.3f" % (lin_fb, amp_at(x, f1)))
print("   quadratic x^2: amp @ f_b = %.4f (a REAL difference line)   amp @ 2f1 = %.3f" % (quad_fb, amp_at(x**2, 2*f1)))
check("the difference-frequency line is ABSENT in the linear field but PRESENT in the energy observable",
      lin_fb < 1e-3 and quad_fb > 0.1, "so the FTGB kHz beat lives in a quadratic/energy observable (detector/stress)")

# ---------------------------------------------------------------- TEST 2: Mathieu parametric tongue
banner("TEST 2 -- parametric (Mathieu) subharmonic: tongue at Omega ~ 2 w0, threshold ~ 2/Q  [credited]")
w0, gamma = 1.0, 0.02
Q = w0/(2*gamma)


def mathieu_tail(Omega, h, T=400.0, dt=2e-3):
    N = int(T/dt); xx, vv = 1e-3, 0.0; A = 0.0
    for i in range(N):
        a = -2*gamma*vv - w0**2*(1+h*np.cos(Omega*i*dt))*xx
        x2 = xx+0.5*dt*vv; v2 = vv+0.5*dt*a
        a2 = -2*gamma*v2 - w0**2*(1+h*np.cos(Omega*(i+0.5)*dt))*x2
        xx += dt*v2; vv += dt*a2
        if i > 0.7*N:
            A = max(A, abs(xx))
    return A


g_2w0 = mathieu_tail(2*w0, 0.15)
g_1w0 = mathieu_tail(1.0*w0, 0.15)
print("   Q = %.0f ,  threshold h_th ~ 2/Q = %.3f" % (Q, 2/Q))
print("   h=0.15:  Omega=2 w0 tail = %.2e (GROWS)   Omega=1 w0 tail = %.2e (decays)" % (g_2w0, g_1w0))
check("the principal parametric tongue is at Omega = 2 w0 (subharmonic), NOT Omega = w0",
      g_2w0 > 1e-2 and g_1w0 < 1e-3, "ratio %.0e -> half-frequency response, the hallmark of parametric drive" % (g_2w0/g_1w0))
g_below = mathieu_tail(2*w0, 0.05)
g_above = mathieu_tail(2*w0, 0.12)
check("onset threshold ~ 2/Q at exact tuning (h=0.05 below decays; h=0.12 above grows)",
      g_below < 1e-3 and g_above > 1e-2, "h_th ~ 2/Q = %.3f (Mathieu principal tongue)" % (2/Q))

# ---------------------------------------------------------------- TEST 3: Adler entrainment
banner("TEST 3 -- Adler entrainment: lock iff |Delta_w| <= K (Arnold tongue)  [credited]")
K = 1.0


def adler_drift(dw, T=200.0, dt=1e-2):
    N = int(T/dt); psi = 0.0
    for _ in range(N):
        psi += dt*(dw - K*np.sin(psi))
    p0 = psi
    for _ in range(int(20/dt)):
        psi += dt*(dw - K*np.sin(psi))
    return (psi - p0)/20.0


d_in1, d_in2, d_out = adler_drift(0.5), adler_drift(0.9), adler_drift(1.3)
print("   K = %.0f :  Delta_w=0.5 drift=%.3f ,  0.9 drift=%.3f ,  1.3 drift=%.3f" % (K, d_in1, d_in2, d_out))
check("locked (zero mean phase drift) inside |Delta_w| <= K, phase-slipping outside",
      abs(d_in1) < 1e-3 and abs(d_in2) < 1e-3 and abs(d_out) > 0.1,
      "the FTGB carrier comb-lock (Kuramoto/Adler, M14) realized: tongue half-width = K")

# ---------------------------------------------------------------- TEST 4: the frequency-matching constraint
banner("TEST 4 -- the honest constraint: a slow BEAT cannot parametrically pump a fast MODE  [settled-neg]")
hbar = 6.582119569e-22          # MeV*s
w_beat = 2*np.pi*87.14e3        # FTGB canon comb beat, rad/s
print("   parametric pumping needs a SUM-frequency match  Omega ~ w_j + w_k  (~ 2 w for a degenerate pair);")
print("   a slow DIFFERENCE (beat) frequency fails it. FTGB kHz beat w_b = %.2e rad/s vs:" % w_beat)
worst = 0
for E, lab in [(1.0, "MeV nuclear"), (1e-3, "keV"), (293e-6, "293 eV")]:
    w = E/hbar
    orders = np.log10(2*w/w_beat)
    worst = max(worst, orders)
    print("     %-11s w = %.2e rad/s   ->  w_b / (2 w) = %.1e   (~%.0f orders too slow)" % (lab, w, w_beat/(2*w), orders))
check("the kHz beat is >10 orders too slow to parametrically pump a MeV nuclear mode",
      worst > 12, "~%.0f orders short -> the beat CANNOT parametrically bridge kHz -> MeV" % worst)
print("   -> SETTLED-NEGATIVE for the PARAMETRIC-PUMP reading of the cross-scale 'kHz detuning <-> MeV gap'")
print("      [S] coincidence: if any cross-scale link exists it must be a genuinely slow nuclear-adjacent")
print("      collective mode (w_b ~ w_slow), or a different mechanism -- NOT the beat pumping the gap. This")
print("      does NOT touch the [V]/conserved d+d->4He energy ledger (separate). A clue disciplined, not a")
print("      mechanism promoted.")

# ---------------------------------------------------------------- TEST 5: the CK comb is inharmonic
banner("TEST 5 -- the CK carrier comb is INHARMONIC (the FTGB fingerprint)  [V]")
g = lambda z: np.sin(z) - z*np.cos(z)
roots = []
for a, b in [(4.0, 5.0), (7.0, 8.0), (10.5, 11.5)]:
    lo, hi = a, b
    for _ in range(90):
        m = 0.5*(lo+hi)
        if g(lo)*g(m) <= 0:
            hi = m
        else:
            lo = m
    roots.append(0.5*(lo+hi))
r = np.array(roots)/roots[0]
harm = np.array([1.0, 2.0, 3.0])
print("   CK comb ratios (roots of tan x = x):  1 : %.3f : %.3f" % (r[1], r[2]))
print("   harmonic series (a string):           1 : %.0f : %.0f" % (harm[1], harm[2]))
check("the CK comb is INHARMONIC (1:1.719:2.427), not the harmonic 1:2:3",
      abs(r[1]-1.719) < 0.01 and abs(r[2]-2.427) < 0.01 and abs(r[1]-2) > 0.2,
      "a harmonic 1:2:3 lock would FALSIFY the Beltrami-carrier reading -- the sharpest FTGB fingerprint")

banner("VERDICT")
print("  Rhythm dynamics grounds the FTGB core: the beat is a nonlinear/energy observable (TEST 1); the")
print("  driven 'heartbeat' is a parametric (Mathieu) drive with its tongue at 2 w0 and threshold 2/Q")
print("  (TEST 2); the carrier comb-lock is Adler/Arnold entrainment (TEST 3); the comb is inharmonic")
print("  (TEST 5, the fingerprint). AND the frequency-matching constraint disciplines the cross-scale")
print("  claim: a slow kHz beat cannot parametrically pump a MeV mode (TEST 4, settled-negative). Every")
print("  relation credited or computed; the one speculative bridge is fenced, not fabricated.")
print("  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
