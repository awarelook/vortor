"""
CAPTURE CHECK: the two Grand-Synthesis Part-D dynamics numbers that were computed in the parent corpus but
never harnessed in-repo -- recomputed here so their [V] tags are backed by a named, re-runnable script.
(A 2026-09-14 jewel audit found D.1.3/D.1.4 tagged 'numerical onset [V]' and '[V] positive-exponent detection'
with NO in-repo computation -- the 'forgotten batch' failure mode. This closes both.)

  TEST 1 -- KURAMOTO MEAN-FIELD ONSET (N=800, Lorentzian) [V]. theta_i' = omega_i + (K/N) sum_j sin(theta_j-theta_i)
            with omega_i ~ Lorentzian(gamma). Mean-field theory [credited: Kuramoto 1975/1984, Strogatz 2000]:
            K_c = 2*gamma exactly (Lorentzian), r = sqrt(1 - K_c/K) above onset. We simulate N=800 and assert:
            incoherence below onset (r small at K = 0.4 K_c), the onset within the finite-N band P = K*/K_c in
            [0.8, 1.6] (the synthesis quotes P ~ 1.2 at grid), and r at K = 2 K_c within a band around the
            mean-field sqrt(1/2) = 0.71 (the synthesis quotes r ~ 0.04 -> 0.38 -> 0.71).
  TEST 2 -- AIZAWA POSITIVE LYAPUNOV EXPONENT (Benettin) [V]. The Aizawa system (the forced-Hopf/Langford
            normal-form family the synthesis carries as [analogy]) at the standard parameters
            a=0.95 b=0.7 c=0.6 d=3.5 e=0.25 f=0.1. Benettin two-trajectory renormalization [credited:
            Benettin et al. 1980]. Literature/toolkit band lambda_max ~ 0.10-0.124; the synthesis carries
            0.107. The LOAD-BEARING claim is the SIGN (chaotic); we assert lambda_max > 0.03 (sign, with
            margin) and that our value lands in a generous [0.05, 0.20] band containing the literature band.

  HONEST SCOPE: these back the synthesis's [V] tags on the NUMERICS ONLY. The FTGB *identification* of
  multi-object synchronization with Kuramoto (D.1.4) stays [S], and the Aizawa reading stays [analogy] --
  exactly as the synthesis prints. Nothing here elevates an analogy.

numpy only, deterministic (seeded). Run: python results/verify/multibody_sync_capture_check.py
"""
import numpy as np

ok = True


def banner(t):
    print("=" * 98); print(t); print("=" * 98)


def check(name, cond, detail=""):
    global ok
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, ("  -- " + detail) if detail else ""))
    ok = ok and cond


banner("TEST 1 -- Kuramoto mean-field onset, N=800, Lorentzian(gamma=0.5) -> K_c = 2*gamma = 1.0  [V]")
rng = np.random.default_rng(0)
N, gamma_w = 800, 0.5
K_c = 2.0 * gamma_w
omega = gamma_w * rng.standard_cauchy(N)          # Lorentzian (Cauchy) natural frequencies
omega = np.clip(omega, -50, 50)                   # clip pathological tail draws (measure-zero, finite-N artifact)
dt, T_settle, T_avg = 0.05, 60.0, 40.0
n_settle, n_avg = int(T_settle / dt), int(T_avg / dt)


def order_param(K, theta0):
    th = theta0.copy()
    for _ in range(n_settle):
        z = np.exp(1j * th).mean()
        th += dt * (omega + K * np.abs(z) * np.sin(np.angle(z) - th))
    acc = 0.0
    for _ in range(n_avg):
        z = np.exp(1j * th).mean()
        th += dt * (omega + K * np.abs(z) * np.sin(np.angle(z) - th))
        acc += np.abs(z)
    return acc / n_avg


theta0 = rng.uniform(0, 2 * np.pi, N)
K_grid = [0.4, 0.8, 1.0, 1.2, 1.4, 1.6, 2.0, 3.0]
r_vals = {K: order_param(K, theta0) for K in K_grid}
for K in K_grid:
    mf = np.sqrt(max(0.0, 1.0 - K_c / K)) if K > K_c else 0.0
    print("   K = %.1f  ->  r = %.3f   (mean-field: %.3f)" % (K, r_vals[K], mf))
K_star = next((K for K in K_grid if r_vals[K] > 0.3), None)
P = (K_star / K_c) if K_star else np.inf
print("   numerical onset K* (first r > 0.3) = %s -> P = K*/K_c = %.2f  (synthesis: P ~ 1.2 at grid)" % (K_star, P))
check("incoherent below onset: r(K=0.4) < 0.2", r_vals[0.4] < 0.2, "r = %.3f" % r_vals[0.4])
check("onset in the finite-N band: P in [0.8, 1.6]", 0.8 <= P <= 1.6, "P = %.2f" % P)
check("r(K=2 K_c) near mean-field sqrt(1/2)=0.71: in [0.55, 0.85]", 0.55 <= r_vals[2.0] <= 0.85,
      "r = %.3f" % r_vals[2.0])
check("synchronized at strong coupling: r(K=3) > 0.6", r_vals[3.0] > 0.6, "r = %.3f" % r_vals[3.0])

banner("TEST 2 -- Aizawa lambda_max by Benettin renormalization; literature band 0.10-0.124, synthesis 0.107  [V]")
a, b, c, d, e, f = 0.95, 0.7, 0.6, 3.5, 0.25, 0.1


def aizawa(v):
    x, y, z = v
    return np.array([(z - b) * x - d * y,
                     d * x + (z - b) * y,
                     c + a * z - z ** 3 / 3.0 - (x * x + y * y) * (1.0 + e * z) + f * z * x ** 3])


def rk4(v, h):
    k1 = aizawa(v); k2 = aizawa(v + 0.5 * h * k1); k3 = aizawa(v + 0.5 * h * k2); k4 = aizawa(v + h * k3)
    return v + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)


h = 0.01
v = np.array([0.1, 0.0, 0.0])
for _ in range(20000):                      # transient: 200 time units
    v = rk4(v, h)
d0 = 1e-8
w = v + np.array([d0, 0.0, 0.0])
lyap_sum, n_ren, ren_every = 0.0, 0, 10
n_steps = 120000                            # 1200 time units
for i in range(n_steps):
    v = rk4(v, h); w = rk4(w, h)
    if (i + 1) % ren_every == 0:
        dv = w - v
        dist = np.linalg.norm(dv)
        lyap_sum += np.log(dist / d0)
        n_ren += 1
        w = v + dv * (d0 / dist)
lam = lyap_sum / (n_ren * ren_every * h)
print("   lambda_max (Benettin, T = %d units, renorm every %d steps) = %.4f" % (int(n_steps * h), ren_every, lam))
print("   literature/toolkit band: 0.10-0.124; synthesis value: 0.107")
check("SIGN (the load-bearing claim): lambda_max > 0.03", lam > 0.03, "chaotic: %.4f > 0" % lam)
check("value in the generous band [0.05, 0.20] containing the literature band", 0.05 <= lam <= 0.20,
      "%.4f" % lam)

banner("VERDICT")
print("  Both Part-D dynamics numbers are now computed IN-REPO: the Kuramoto N=800 Lorentzian onset (P ~ %.2f," % P)
print("  r(2K_c) = %.2f vs mean-field 0.71) and the Aizawa positive exponent (lambda_max = %.3f, band 0.10-0.124)." % (r_vals[2.0], lam))
print("  The [V] tags in FTGB_GRAND_SYNTHESIS.md D.1.3/D.1.4 are no longer orphans. Identifications stay [S]/[analogy].")
print("  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
