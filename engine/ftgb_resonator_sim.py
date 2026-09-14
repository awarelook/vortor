"""
ftgb_resonator_sim.py -- SIMULATION software for the FTGB oscillating harmonic resonator matter wave.

Where ftgb_engine.py is the theory as one executable MODEL (anchors -> structure -> theorems), this file
is the theory as running SIMULATION: it time-integrates the object's dynamics in software and checks the
simulated behavior against the theory's exact laws. Five simulations, each with a hard PASS/FAIL:

  SIM 1 -- THE OBJECT (exact Beltrami eigenfield). Build a curl eigenfield (ABC flow, curl u = u) on a
           periodic 3-torus; verify the Beltrami property spectrally to machine precision and the
           self-interaction null (Lamb vector u x omega = 0 pointwise).                            [V]
  SIM 2 -- COHERENCE IS REGULARITY (full nonlinear evolution). Integrate the incompressible
           Navier-Stokes equations pseudo-spectrally (RK4, 2/3-dealiased, 32^3) from the Beltrami
           state: the nonlinearity self-cancels and the simulation must track the EXACT eternal
           solution u(t) = exp(-nu lambda^2 t) u0. Contrast: a Taylor-Green (non-Beltrami) start
           departs from pure decay -- proof the test has teeth.                                    [V]
           (Companion to results/verify/exact_beltrami_regularity_check.py: that script verifies the
            law's identities; this one RUNS the dynamics and shows the law emerge in software.)
  SIM 3 -- THE RESONATOR (CK comb). Re-derive the Chandrasekhar-Kendall boundary quantization
           tan x = x by bisection; comb ratios 1 : 1.719 : 2.427; SI calibration at the canon anchors
           (v_A = 2.033e4 m/s, R = 0.12 m -> {121, 208, 294} kHz) and the comb's beat structure
           (87.1 / 85.7 kHz, second-order detuning ~1.4 kHz -- the theory's kHz detuning).
                                                              [V] ratios / anchor-scaled absolutes
  SIM 4 -- HARMONIC OSCILLATION (driven-damped resonance + beat). Time-integrate the driven damped
           harmonic oscillator at the comb; simulated steady-state amplitudes must land on the analytic
           Lorentzian (Q factor recovered). Superpose comb modes 1+2 and EXTRACT the beat frequency
           from the simulated envelope (FFT-Hilbert): must equal x2 - x1.                          [V]
  SIM 5 -- THE MATTER WAVE (Proca packet). Evolve a wave packet under the theory's massive dispersion
           omega^2 = c^2 k^2 + omega_c^2 (Compton cutoff = the whirl mass, m = hbar omega_c / c^2).
           Measured envelope (group) velocity must equal c^2 k0 / omega0, the packet at rest must
           oscillate at exactly omega_c (the internal clock), and v_g * v_p = c^2 -- the de Broglie
           matter-wave relation, measured in software.       [V] math; the matter-wave reading [S/QWM]

Discipline: numpy only, deterministic (no RNG, no clock), ASCII output, exit 0 iff every check passes.
Run:  python engine/ftgb_resonator_sim.py       (auto-included in results/verify/verify_all.py)
"""
import numpy as np

# ---- canon anchors (foundation/30_CANONICAL_NUMBERS.md) ----
V_A_CANON = 2.033e4      # m/s  (ball-lightning calibration; absolute magnitudes carry the v_A band)
R_CANON   = 0.12         # m
CK_ROOTS_REF = np.array([4.493409457909064, 7.725251836937707, 10.904121659428899])

FAILS = []


def banner(t):
    print("=" * 86)
    print(t)
    print("=" * 86)


def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print("  [%s] %s%s" % (tag, name, ("  -- " + detail) if detail else ""))
    if not ok:
        FAILS.append(name)


# ================================================================================================
# SIM 1 + 2 -- the object and its nonlinear evolution (pseudo-spectral Navier-Stokes on T^3)
# ================================================================================================

def spectral_setup(N):
    k1 = np.fft.fftfreq(N, d=1.0 / N)                     # integer wavenumbers on [0, 2pi)^3
    KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing="ij")
    K2 = KX**2 + KY**2 + KZ**2
    K2n = np.where(K2 == 0, 1.0, K2)                      # safe divisor
    kmax = N // 2
    dealias = (np.abs(KX) <= (2.0/3.0)*kmax) & (np.abs(KY) <= (2.0/3.0)*kmax) & (np.abs(KZ) <= (2.0/3.0)*kmax)
    return (KX, KY, KZ), K2, K2n, dealias


def curl_hat(uh, K):
    KX, KY, KZ = K
    cx = 1j*(KY*uh[2] - KZ*uh[1])
    cy = 1j*(KZ*uh[0] - KX*uh[2])
    cz = 1j*(KX*uh[1] - KY*uh[0])
    return [cx, cy, cz]


def project_div_free(vh, K, K2n):
    KX, KY, KZ = K
    div = KX*vh[0] + KY*vh[1] + KZ*vh[2]
    return [vh[0] - KX*div/K2n, vh[1] - KY*div/K2n, vh[2] - KZ*div/K2n]


def nonlinear_hat(uh, K, K2n, dealias):
    """N(u) = P[ u x omega ]  (rotational form; the gradient part is removed by the projection)."""
    u = [np.fft.ifftn(c).real for c in uh]
    wh = curl_hat(uh, K)
    w = [np.fft.ifftn(c).real for c in wh]
    lamb = [u[1]*w[2] - u[2]*w[1], u[2]*w[0] - u[0]*w[2], u[0]*w[1] - u[1]*w[0]]
    lh = [np.fft.fftn(c) * dealias for c in lamb]
    return project_div_free(lh, K, K2n)


def rhs(uh, K, K2, K2n, dealias, nu):
    nl = nonlinear_hat(uh, K, K2n, dealias)
    return [nl[i] - nu*K2*uh[i] for i in range(3)]


def rk4_evolve(uh, K, K2, K2n, dealias, nu, dt, steps):
    for _ in range(steps):
        k1 = rhs(uh, K, K2, K2n, dealias, nu)
        u2 = [uh[i] + 0.5*dt*k1[i] for i in range(3)]
        k2 = rhs(u2, K, K2, K2n, dealias, nu)
        u3 = [uh[i] + 0.5*dt*k2[i] for i in range(3)]
        k3 = rhs(u3, K, K2, K2n, dealias, nu)
        u4 = [uh[i] + dt*k3[i] for i in range(3)]
        k4 = rhs(u4, K, K2, K2n, dealias, nu)
        uh = [uh[i] + (dt/6.0)*(k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) for i in range(3)]
    return uh


def sim_object_and_regularity():
    banner("SIM 1 -- THE OBJECT: exact Beltrami eigenfield (curl u = u) on the 3-torus   [V]")
    N = 32
    K, K2, K2n, dealias = spectral_setup(N)
    x = np.linspace(0.0, 2.0*np.pi, N, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")

    # ABC eigenfield (A=B=C=1): an exact curl eigenfield with lambda = 1
    u0 = [np.sin(Z) + np.cos(Y), np.sin(X) + np.cos(Z), np.sin(Y) + np.cos(X)]
    uh0 = [np.fft.fftn(c) for c in u0]

    wh0 = curl_hat(uh0, K)
    res = max(np.max(np.abs(np.fft.ifftn(wh0[i]).real - u0[i])) for i in range(3))
    scale = max(np.max(np.abs(c)) for c in u0)
    check("Beltrami property curl u = u (spectral, max residual)", res < 1e-12,
          "max|curl u - u| = %.2e  (field scale %.1f)" % (res, scale))

    w0 = [np.fft.ifftn(c).real for c in wh0]
    lamb0 = np.sqrt((u0[1]*w0[2] - u0[2]*w0[1])**2 + (u0[2]*w0[0] - u0[0]*w0[2])**2
                    + (u0[0]*w0[1] - u0[1]*w0[0])**2)
    check("self-interaction null: Lamb vector u x omega = 0 pointwise", np.max(lamb0) < 1e-12,
          "max|u x omega| = %.2e" % np.max(lamb0))

    banner("SIM 2 -- COHERENCE IS REGULARITY: full nonlinear Navier-Stokes evolution      [V]")
    nu, dt, steps = 0.1, 2.5e-3, 200
    T = dt * steps
    lam = 1.0

    uhT = rk4_evolve([c.copy() for c in uh0], K, K2, K2n, dealias, nu, dt, steps)
    uT = [np.fft.ifftn(c).real for c in uhT]
    decay = np.exp(-nu * lam**2 * T)
    err_b = max(np.max(np.abs(uT[i] - decay*u0[i])) for i in range(3)) / scale
    print("  nonlinear pseudo-spectral run: 32^3, RK4, 2/3-dealiased, nu=%.2f, T=%.2f (%d steps)"
          % (nu, T, steps))
    print("  exact eternal solution:  u(t) = exp(-nu lambda^2 t) u0   (Lamb null -> advection = pure gradient)")
    check("simulated field tracks the exact law", err_b < 1e-8,
          "rel departure from exp(-nu t) u0 = %.2e" % err_b)

    whT = curl_hat(uhT, K)
    wT = [np.fft.ifftn(c).real for c in whT]
    lambT = np.sqrt((uT[1]*wT[2] - uT[2]*wT[1])**2 + (uT[2]*wT[0] - uT[0]*wT[2])**2
                    + (uT[0]*wT[1] - uT[1]*wT[0])**2)
    check("Lamb null persists through the evolution", np.max(lambT) < 1e-10,
          "max|u x omega|(T) = %.2e" % np.max(lambT))

    # contrast: a NON-Beltrami start must depart from pure decay (the test has teeth)
    tg = [np.sin(X)*np.cos(Y)*np.cos(Z), -np.cos(X)*np.sin(Y)*np.cos(Z), np.zeros_like(X)]
    tgh = [np.fft.fftn(c) for c in tg]
    tghT = rk4_evolve([c.copy() for c in tgh], K, K2, K2n, dealias, nu, dt, steps)
    tgT = [np.fft.ifftn(c).real for c in tghT]
    decay_tg = np.exp(-nu * 3.0 * T)                      # TG modes have |k|^2 = 3
    err_tg = max(np.max(np.abs(tgT[i] - decay_tg*tg[i])) for i in range(3)) / 1.0
    check("contrast: Taylor-Green (non-Beltrami) departs from pure decay", err_tg > 1e-4 and err_tg > 1e4*err_b,
          "TG departure %.2e  vs Beltrami %.2e  (ratio %.1e)" % (err_tg, err_b, err_tg/max(err_b, 1e-300)))
    print("  -> the coherent (Beltrami) state is the one that evolves EXACTLY; generic states do not.")
    print("     (Exact-state result [V]; the driven/perturbed regime stays the open 3-D problem -- see TIER_LEDGER.)")


# ================================================================================================
# SIM 3 -- the resonator comb (CK boundary quantization) and its beat structure
# ================================================================================================

def sim_resonator_comb():
    banner("SIM 3 -- THE RESONATOR: Chandrasekhar-Kendall comb tan x = x and the kHz beats  [V]")
    g = lambda t: np.sin(t) - t*np.cos(t)                 # zeros of g <=> tan x = x (no poles)
    roots = []
    for a, b in [(4.0, 5.0), (7.0, 8.0), (10.5, 11.5)]:
        lo, hi = a, b
        for _ in range(90):
            mid = 0.5*(lo + hi)
            if g(lo)*g(mid) <= 0:
                hi = mid
            else:
                lo = mid
        roots.append(0.5*(lo + hi))
    roots = np.array(roots)
    err_roots = np.max(np.abs(roots - CK_ROOTS_REF))
    check("boundary quantization roots re-derived (bisection)", err_roots < 1e-12,
          "x = %.6f, %.6f, %.6f  (max dev %.1e)" % (roots[0], roots[1], roots[2], err_roots))

    ratios = roots / roots[0]
    check("comb ratios 1 : 1.719 : 2.427 (anchor-free)",
          abs(ratios[1] - 1.71925) < 1e-4 and abs(ratios[2] - 2.42670) < 1e-4,
          "1 : %.5f : %.5f" % (ratios[1], ratios[2]))

    f = V_A_CANON * roots / (2.0*np.pi*R_CANON)           # SI comb at the canon anchors
    beats = np.diff(f)
    detune = beats[0] - beats[1]
    print("  SI comb at canon anchors (v_A=%.4g m/s, R=%.2f m; absolutes carry the v_A band):" % (V_A_CANON, R_CANON))
    print("    f = {%.1f, %.1f, %.1f} kHz   (the {121, 208, 294} kHz calibration)" % tuple(f/1e3))
    print("    beats f2-f1 = %.2f kHz, f3-f2 = %.2f kHz;  second-order detuning = %.3f kHz" % (beats[0]/1e3, beats[1]/1e3, detune/1e3))
    check("comb lands on the {121, 208, 294} kHz calibration",
          np.all(np.abs(f/1e3 - np.array([121.2, 208.3, 294.0])) < 0.5),
          "|df| < 0.5 kHz each")
    check("the comb is INHARMONIC: near-equal beats with a nonzero kHz detuning",
          beats[0] > beats[1] and 1.0e3 < detune < 2.0e3,
          "detuning %.0f Hz (the theory's kHz detuning scale)" % detune)
    return roots


# ================================================================================================
# SIM 4 -- driven-damped harmonic oscillation at the comb + the simulated beat
# ================================================================================================

def sim_harmonic_oscillation(roots):
    banner("SIM 4 -- HARMONIC OSCILLATION: driven-damped resonance (Lorentzian) + simulated beat  [V]")
    Q = 25.0
    lorentz = lambda W: 1.0/np.sqrt((1.0 - W**2)**2 + (W/Q)**2)

    def drive(W, dt=0.005, T=400.0):
        n = int(T/dt)
        x, v = 0.0, 0.0
        acc = lambda t, x, v: np.cos(W*t) - (1.0/Q)*v - x
        amp = 0.0
        t = 0.0
        for i in range(n):
            k1v = acc(t, x, v);            k1x = v
            k2v = acc(t+dt/2, x+dt/2*k1x, v+dt/2*k1v); k2x = v + dt/2*k1v
            k3v = acc(t+dt/2, x+dt/2*k2x, v+dt/2*k2v); k3x = v + dt/2*k2v
            k4v = acc(t+dt, x+dt*k3x, v+dt*k3v);       k4x = v + dt*k3v
            x += (dt/6)*(k1x + 2*k2x + 2*k3x + k4x)
            v += (dt/6)*(k1v + 2*k2v + 2*k3v + k4v)
            t += dt
            if i > 0.8*n:
                amp = max(amp, abs(x))
        return amp

    ok_all = True
    for W in (0.90, 1.00, 1.10):
        a_sim, a_th = drive(W), lorentz(W)
        rel = abs(a_sim - a_th)/a_th
        ok = rel < 0.01
        ok_all = ok_all and ok
        print("    Omega/omega0 = %.2f :  simulated amplitude %.4f  vs Lorentzian %.4f  (rel dev %.1e)"
              % (W, a_sim, a_th, rel))
    check("driven-damped oscillator lands on the analytic Lorentzian (Q=%.0f recovered)" % Q, ok_all)

    # the BEAT: superpose comb modes 1+2, extract the envelope frequency from the simulation
    x1, x2 = roots[0], roots[1]
    T, n = 2000.0, 1 << 17
    t = np.linspace(0.0, T, n, endpoint=False)
    s = np.cos(x1*t) + np.cos(x2*t)
    S = np.fft.fft(s)
    S[n//2+1:] = 0.0                                       # analytic signal (FFT-Hilbert)
    S[1:n//2] *= 2.0
    env = np.abs(np.fft.ifft(S))
    E = np.abs(np.fft.rfft(env - np.mean(env)))
    freqs = np.fft.rfftfreq(n, d=T/n) * 2.0*np.pi          # angular
    j = np.argmax(E[1:]) + 1
    # parabolic peak refinement
    if 1 <= j < len(E) - 1:
        d = 0.5*(E[j-1] - E[j+1]) / (E[j-1] - 2*E[j] + E[j+1])
        beat_meas = freqs[j] + d*(freqs[1] - freqs[0])
    else:
        beat_meas = freqs[j]
    beat_th = x2 - x1
    rel = abs(beat_meas - beat_th)/beat_th
    check("simulated envelope beat = x2 - x1 (the matter-wave beat of the comb)", rel < 5e-3,
          "measured %.5f vs %.5f (rel dev %.1e)" % (beat_meas, beat_th, rel))
    print("  -> at the canon anchors this beat is the %.2f kHz line of SIM 3." % ((x2-x1)*V_A_CANON/(2*np.pi*R_CANON)/1e3))


# ================================================================================================
# SIM 5 -- the matter wave: Proca/Compton-cutoff dispersion packet (de Broglie in software)
# ================================================================================================

def sim_matter_wave():
    banner("SIM 5 -- THE MATTER WAVE: packet under omega^2 = c^2 k^2 + omega_c^2  (m = hbar omega_c/c^2)")
    c, wc = 1.0, 5.0                                       # natural units; omega_c = Compton cutoff
    L, N = 200.0, 4096
    x = np.linspace(0.0, L, N, endpoint=False)
    k = np.fft.fftfreq(N, d=L/N) * 2.0*np.pi
    omega = np.sqrt(c**2 * k**2 + wc**2)

    def evolve_centroid(k0, T=40.0, nt=41):
        x0, sig = 60.0, 5.0
        psi0 = np.exp(-0.5*((x - x0)/sig)**2) * np.exp(1j*k0*x)
        ph0 = np.fft.fft(psi0)
        ts = np.linspace(0.0, T, nt)
        cent = []
        for tt in ts:
            psi = np.fft.ifft(ph0 * np.exp(-1j*omega*tt))
            w = np.abs(psi)**2
            cent.append(np.sum(x*w)/np.sum(w))
        cent = np.array(cent)
        vg = np.polyfit(ts, cent, 1)[0]
        return vg

    k0 = 3.0
    w0 = np.sqrt(c**2*k0**2 + wc**2)
    vg_th = c**2 * k0 / w0
    vp_th = w0 / k0
    vg_sim = evolve_centroid(k0)
    rel = abs(vg_sim - vg_th)/vg_th
    print("  moving packet (k0 = %.1f):  measured group velocity %.5f  vs  c^2 k0/omega0 = %.5f" % (k0, vg_sim, vg_th))
    check("measured envelope velocity = group velocity c^2 k / omega", rel < 2e-3, "rel dev %.1e" % rel)

    prod = vg_sim * vp_th
    check("de Broglie relation v_g * v_p = c^2 (measured x analytic)", abs(prod - c**2) < 5e-3,
          "v_g*v_p = %.5f  (c^2 = 1)" % prod)

    # the packet AT REST: no drift; the internal clock ticks at exactly omega_c (de Broglie's phase harmony)
    x0, sig = 100.0, 5.0
    psi0 = np.exp(-0.5*((x - x0)/sig)**2).astype(complex)
    ph0 = np.fft.fft(psi0)
    ic = np.argmin(np.abs(x - x0))
    ts = np.linspace(0.0, 10.0, 1001)
    vals = np.array([np.fft.ifft(ph0 * np.exp(-1j*omega*tt))[ic] for tt in ts])
    phase = np.unwrap(np.angle(vals))
    w_clock = -np.polyfit(ts, phase, 1)[0]
    # narrow spectral width: clock = <omega(k)> ~= omega_c (1 + (sigma_k/wc)^2 c^2/2 correction)
    check("rest packet oscillates at the Compton clock omega_c (internal clock)",
          abs(w_clock - wc)/wc < 1e-3, "measured %.5f vs omega_c = %.1f" % (w_clock, wc))
    vg0 = evolve_centroid(0.0)
    check("rest packet does not translate (v_g = 0)", abs(vg0) < 1e-6, "v_g = %.1e" % vg0)
    print("  -> the resonator's oscillation IS the matter wave: mass = trapped oscillation (m = hbar omega_c/c^2),")
    print("     motion = the beat (group) envelope, v_g*v_p = c^2. Math [V]; the physical reading is the QWM/")
    print("     de Broglie identification carried at [S]/[framework] (see GLOSSARY / TIER_LEDGER).")


# ================================================================================================

def main():
    banner("FTGB RESONATOR SIMULATION -- the oscillating harmonic resonator matter wave, in software")
    print("  model: driven Beltrami-Hopf toroidal soliton; this run = object -> evolution -> comb ->")
    print("  oscillation/beat -> matter wave. Deterministic, numpy-only. Exit 0 iff all checks pass.")
    sim_object_and_regularity()
    roots = sim_resonator_comb()
    sim_harmonic_oscillation(roots)
    sim_matter_wave()
    banner("VERDICT")
    if FAILS:
        print("  status: FAIL  (%d failed: %s)" % (len(FAILS), "; ".join(FAILS)))
        return 1
    print("  All simulations reproduce the theory's exact laws: the Beltrami object evolves as the")
    print("  eternal coherent solution under the FULL nonlinear dynamics (and a generic state does not);")
    print("  the CK comb, its kHz beat, the Lorentzian resonance, and the de Broglie matter-wave")
    print("  kinematics all emerge from the simulated software model.  status: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
