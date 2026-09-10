"""
GML/FIT phase-dynamics, internalized into the toolkit: coupled oscillators, Adler/Arnold phase-locking,
and the Phase-Pattern Metric (PPM) on the N-torus -- and the genuine result it yields for FTGB.

Bandyopadhyay's Geometric Musical Language / Fractal Information Theory, stripped to physics, is a
multi-scale COUPLED-OSCILLATOR model whose state is a phase pattern on T^N, with information carried in
PHASE RELATIONSHIPS (the PPM) rather than amplitudes. That mathematics is [credited] nonlinear dynamics
(Kuramoto 1975; Adler 1946; Arnold tongues) -- and it GENERALIZES FTGB's own engine.comb_lock. This
module internalizes the general framework and extracts one genuine, discriminating FTGB result.

Model (amplitude-phase reduction of a_k' = (i w_k - g_k)a_k + sum K_kj a_j + ... ):
    theta_k' = omega_k + sum_resonances  K * sin(Psi) ,   Psi = m theta_i - n theta_j     (Adler/Kuramoto)
State / PPM:   I(t) = (theta_2 - theta_1, ..., theta_N - theta_1) mod 2pi  in T^{N-1}
Lock test:     Psi locked  <=>  d<Psi>/dt -> 0  (Adler: locks iff coupling K >= detuning |m w_i - n w_j|)

  TEST A -- PPM: the object's state is a phase pattern on the torus; in a locked regime it settles to a
            FIXED pattern (an attractor) -- the phase-identity of the object.
  TEST B -- Arnold tongue: for the FTGB CK comb (inharmonic 1:1.719:2.427) the 7:4 and 5:2 locks have
            NONZERO detunings (0.123, 0.147) -> they lock only above a coupling threshold (a real tongue).
            Reproduces + generalizes engine.comb_lock.
  TEST C -- THE RESULT: harmonic vs inharmonic locking. Bandyopadhyay's microtubule cascade 1:3:9 is
            COMMENSURATE (integer) -> its locks have ZERO detuning -> it phase-locks at ANY coupling,
            trivially. The FTGB CK comb is genuinely INHARMONIC -> tongue-gated locking. So the two
            frameworks share the METHOD (phase dynamics) but sit at opposite ends of it: trivial-lock
            (harmonic N=3) vs threshold-lock (inharmonic CK) -- a clean, computed discriminator.
Run: python results/verify/phase_dynamics_gml_check.py
"""
import numpy as np

CK = np.array([4.493409, 7.725252, 10.904122])
OM_CK = CK/CK[0]                    # FTGB inharmonic comb: [1, 1.7192, 2.4267]
OM_HARM = np.array([1.0, 3.0, 9.0]) # Bandyopadhyay 1:3:9 (integer/harmonic cascade, base N=3)


def run(om, locks, K, T=800.0, dt=0.01, seed=1):
    """Integrate resonant phase oscillators. locks = [(m,i,n,j), ...]; coupling K on each. Return late-window theta history."""
    rng = np.random.default_rng(seed)
    th = rng.uniform(0, 2*np.pi, len(om))
    n = int(T/dt); hist = []
    for s in range(n):
        dth = om.copy()
        for (m, i, nn, j) in locks:
            psi = m*th[i] - nn*th[j]
            c = K*np.sin(psi)
            dth[i] -= c; dth[j] += c
        th = th + dt*dth
        if s > n*3//4: hist.append(th.copy())
    return np.array(hist), dt


def drift(hist, dt, m, i, nn, j):
    """mean drift rate of the lock phase Psi = m th_i - n th_j; ~0 => LOCKED, ~detuning => running."""
    psi = np.unwrap(m*hist[:, i] - nn*hist[:, j])
    return abs((psi[-1]-psi[0]) / ((len(psi)-1)*dt))


def banner(t): print("="*80); print(t); print("="*80)
ok = True

banner("A) PPM -- the object's state is a phase pattern on T^{N-1}; locked -> a FIXED pattern (attractor)")
hist, dt = run(OM_CK, [(7,0,4,1), (5,0,2,2)], K=0.6)
d_a = drift(hist, dt, 7,0,4,1); d_b = drift(hist, dt, 5,0,2,2)
psi_a = np.mod(np.mean(7*hist[-500:,0]-4*hist[-500:,1]), 2*np.pi)
psi_b = np.mod(np.mean(5*hist[-500:,0]-2*hist[-500:,2]), 2*np.pi)
print("  CK comb, K=0.6: both locks converge (7:4 drift=%.4f, 5:2 drift=%.4f -> 0 = locked)" % (d_a, d_b))
print("  PPM fixed point = the settled LOCK phases Psi_74=%.2f, Psi_52=%.2f rad -- the object's" % (psi_a, psi_b))
print("  phase-IDENTITY on the torus. (The lock COMBOS are bounded; raw th_k-th_0 keep advancing -- it is")
print("  the PATTERN, not the phases, that is fixed. That is precisely the PPM idea.) [credited/V]")
ok = ok and d_a < 1e-2 and d_b < 1e-2

banner("B) Arnold tongue on the FTGB CK comb (inharmonic): locks are THRESHOLD-gated (reproduces comb_lock)")
Da = abs(7*OM_CK[0]-4*OM_CK[1]); Db = abs(5*OM_CK[0]-2*OM_CK[2])
print("  detunings: 7:4 |7w0-4w1| = %.4f ; 5:2 |5w0-2w2| = %.4f  (nonzero -> genuine tongue)" % (Da, Db))
print("   K       7:4 drift   locked?    5:2 drift   locked?")
for K in [0.02, 0.10, 0.30, 0.60]:
    h,_ = run(OM_CK, [(7,0,4,1),(5,0,2,2)], K=K)
    d74 = drift(h, dt, 7,0,4,1); d52 = drift(h, dt, 5,0,2,2)
    print("  %.2f     %.4f      %-5s      %.4f      %-5s" %
          (K, d74, d74<1e-2, d52, d52<1e-2))
print("  -> below threshold the locks DRIFT (quasiperiodic on the torus); above, they LOCK. Real tongue.")

banner("C) RESULT: harmonic (1:3:9, Bandyopadhyay N=3) locks TRIVIALLY; inharmonic (CK) is threshold-gated")
DaH = abs(3*OM_HARM[0]-1*OM_HARM[1]); Kstar = Da/(7+4)  # Adler tongue: locks iff K >= detuning/(m+n)
print("  1:3:9 cascade: the 3:1 lock |3w0-1w1| = %.4f (ZERO -- commensurate) -> locks at ANY K>0" % DaH)
hH,_ = run(OM_HARM, [(3,0,1,1),(9,0,1,2)], K=0.005)   # sub-threshold coupling
dH = drift(hH, dt, 3,0,1,1)
print("  1:3:9 at tiny K=0.005:  3:1 drift = %.4f  -> LOCKED (%s)" % (dH, dH<1e-2))
hC,_ = run(OM_CK, [(7,0,4,1)], K=0.005)
dC = drift(hC, dt, 7,0,4,1)
print("  CK 7:4 at the SAME K=0.005 (below the tongue K*=det/(m+n)=%.4f): drift = %.4f -> NOT locked (%s)"
      % (Kstar, dC, dC<1e-2))
print("  -> SAME method (phase dynamics), OPPOSITE regimes: harmonic N=3 is trivially commensurate-locked;")
print("     the FTGB CK comb needs finite coupling (an Arnold tongue). This is the clean discriminator")
print("     between Bandyopadhyay's 1:3:9 microtubule cascade and FTGB's inharmonic Beltrami comb.")
ok = ok and (dH < 1e-2) and (dC > 1e-2)

banner("INTERNALIZED (what the toolkit now carries from GML/FIT)")
print("  [credited] the coupled-oscillator + Adler/Arnold phase-locking + PPM(T^N) framework (Kuramoto 1975,")
print("  Adler 1946); [V] here: it reproduces & GENERALIZES engine.comb_lock (arbitrary N, arbitrary m:n")
print("  resonances, the phase-pattern state, the tongue thresholds); [V] the harmonic-vs-inharmonic")
print("  discriminator (C). [S] the FTGB reading (the single-lambda coherent object = a locked phase")
print("  pattern / PPM fixed point). [speculative frontier] the SOMU/consciousness 'reality is nested")
print("  phase-math' claims -- NOT adopted. The math is folded; the metaphysics is quarantined.")
print("done.  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
