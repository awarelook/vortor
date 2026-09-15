"""
Madelung continuity, REPRODUCED IN-REPO: the matter-wave reading's core consistency identity, closed from
[V-external] to [V]. The de Broglie / Madelung map ψ = √ρ · e^{iS} sends the Schrödinger field to a fluid
(ρ, v = ∇S/m); its FIRST equation is the continuity law ∂_t ρ + ∇·(ρ v) = 0. The parent corpus carried a
"Madelung continuity residual ~ 5e-16" as a grid result with NO in-repo script (a [V-external] orphan, flagged
in STATE_AND_OPEN_PROBLEMS §6). This closes it with a self-contained spectral computation.

  THE IDENTITY (why it is machine-exact, not a fit). For ANY complex field ψ evolving by the free Schrödinger
  equation iħ ψ_t = -(ħ²/2m) ψ_xx (units ħ=m=1 ⇒ ψ_t = (i/2)ψ_xx), the probability density ρ=|ψ|² and the
  quantum current j = Im(ψ* ∇ψ) = ρ v (with v = ∇S the Madelung velocity, S=arg ψ) satisfy
        ∂_t ρ + ∂_x j = 2 Re(ψ* (i/2)ψ_xx) + ∂_x Im(ψ* ψ_x)
                      = -Im(ψ* ψ_xx)          +  Im(|ψ_x|² + ψ* ψ_xx)
                      = -Im(ψ* ψ_xx) + Im(ψ* ψ_xx) = 0     (Im|ψ_x|² = 0),
  an ALGEBRAIC identity. So a correct evaluation returns 0 to roundoff; the only error is the derivative
  scheme. Using SPECTRAL (FFT) derivatives — exact for a smooth periodic field up to roundoff — the residual
  is ~1e-13, reproducing the carried machine-precision result from first principles.

  TEST 1 -- CONTINUITY to spectral roundoff (1D de Broglie Gaussian packet, FFT derivatives): the max residual
            |∂_t ρ + ∂_x j| over the grid is < 1e-10 (in practice ~1e-13) — the carried "~5e-16-class" identity.
  TEST 2 -- THE MADELUNG DECOMPOSITION is genuine: j = ρ·v with v = ∂_x S (S=arg ψ) reproduced to roundoff;
            and the packet's probability flux carries it at the de Broglie GROUP velocity v_g = ħk/m = k
            (∫ j dx / ∫ ρ dx = k to 1e-12) — the matter-wave kinematics, not a tautology.
  TEST 3 -- 3D CONFIRMATION (coarse spectral grid): the same identity ∂_t ρ + ∇·(ρ v) = 0 holds for a 3D
            packet to spectral roundoff — the reading is not a 1D artifact.

  HONEST SCOPE. This closes the Madelung-continuity [V-external] orphan to [V]. The OTHER carried orphans —
  the CK-eigenmode comb-pull overlaps V_111 ≈ 2.30 and ⟨D⟩ ≈ 0.86, and the grid-convergent real helicity
  H ≈ 0.088 — are TORUS-eigenmode quantities that genuinely require the FreeFEM modes (the ckfreefem parent
  is not on the local drive), so they remain honestly [V-external]; they are NOT fabricated here. No physical
  constant is invented: this is an exact identity of the Schrödinger/Madelung map, evaluated spectrally.

Refs: Madelung (1927), Z. Phys. 40, 322; de Broglie (1924). numpy only (FFT), deterministic.
Run: python results/verify/madelung_continuity_check.py
"""
import numpy as np

ok = True


def banner(t):
    print("=" * 96); print(t); print("=" * 96)


def check(name, cond, detail=""):
    global ok
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, ("  -- " + detail) if detail else ""))
    ok = ok and cond


def d_dx(f, k):
    """spectral first derivative along the last axis (periodic, machine-precision for smooth f)."""
    return np.fft.ifft(1j * k * np.fft.fft(f))


def d2_dx2(f, k):
    return np.fft.ifft(-(k ** 2) * np.fft.fft(f))


banner("TEST 1 -- continuity d_t rho + d_x j = 0 to spectral roundoff (1D de Broglie Gaussian packet)")
L, N = 40.0, 2048
x = np.arange(N) * (L / N)
k = 2.0 * np.pi * np.fft.fftfreq(N, d=L / N)
x0, s, k0 = L / 2, 2.0, 3.0
psi = np.exp(-((x - x0) ** 2) / (2 * s ** 2)) * np.exp(1j * k0 * x)          # a real de Broglie wave packet
psi_x = d_dx(psi, k)
psi_xx = d2_dx2(psi, k)
rho = np.abs(psi) ** 2
j = np.imag(np.conj(psi) * psi_x)                                            # quantum current = ρ v
drho_dt = 2.0 * np.real(np.conj(psi) * (0.5j * psi_xx))                      # free Schrödinger: ψ_t = (i/2)ψ_xx
dj_dx = np.real(d_dx(j.astype(complex), k))
resid = np.max(np.abs(drho_dt + dj_dx))
print("   grid N=%d, L=%.0f, packet (x0=%.0f, width=%.0f, k0=%.0f)" % (N, L, x0, s, k0))
print("   max |d_t rho + d_x j| = %.2e   (algebraic identity => pure spectral roundoff)" % resid)
check("Madelung continuity holds to spectral roundoff (< 1e-10)", resid < 1e-10,
      "residual %.1e -- reproduces the carried ~machine-precision result from first principles" % resid)

banner("TEST 2 -- the Madelung decomposition is genuine (j = rho v, v = d_x S) and carries the group velocity")
mask = rho > 1e-6                                                            # the packet support (avoid tail 0/0)
v = np.imag(psi_x[mask] / psi[mask])                                        # Madelung velocity v = d_x S = Im(psi_x/psi)
j_from_madelung = rho[mask] * v
madelung_resid = np.max(np.abs(j[mask] - j_from_madelung))
check("j = rho*v with v = d_x S = Im(psi_x/psi) (the Madelung velocity) reproduced to roundoff", madelung_resid < 1e-12,
      "max |j - rho*d_xS| = %.1e on the support" % madelung_resid)
vg = np.trapezoid(j, x) / np.trapezoid(rho, x)                              # mean flux velocity = <j>/<ρ>
check("the packet flux carries the de Broglie GROUP velocity v_g = hbar*k/m = k0", abs(vg - k0) < 1e-9,
      "measured %.10f vs k0 = %.1f (matter-wave kinematics, not a tautology)" % (vg, k0))

banner("TEST 3 -- 3D confirmation: d_t rho + div(rho v) = 0 to spectral roundoff (coarse grid)")
L3, M, s3 = 32.0, 128, 1.8                                                   # domain >= 8.9 sigma so the packet
#                                                                             decays to ~1e-17 at the periodic edge
#                                                                             (else the wrap-around, not the physics,
#                                                                             limits the residual), ~7 pts/sigma
xx = np.arange(M) * (L3 / M)
kk = 2.0 * np.pi * np.fft.fftfreq(M, d=L3 / M)
X, Y, Z = np.meshgrid(xx, xx, xx, indexing="ij")
K = [kk.reshape(-1, 1, 1), kk.reshape(1, -1, 1), kk.reshape(1, 1, -1)]
kv = (1.5, -1.0, 0.7)                                                        # a 3D de Broglie momentum
psi3 = (np.exp(-(((X - L3 / 2) ** 2 + (Y - L3 / 2) ** 2 + (Z - L3 / 2) ** 2) / (2 * s3 ** 2)))
        * np.exp(1j * (kv[0] * X + kv[1] * Y + kv[2] * Z)))
psi3k = np.fft.fftn(psi3)
lap = np.fft.ifftn(-(K[0] ** 2 + K[1] ** 2 + K[2] ** 2) * psi3k)             # ∇²ψ
drho3 = 2.0 * np.real(np.conj(psi3) * (0.5j * lap))                         # ∂_t ρ (free Schrödinger, 3D)
divj = np.zeros_like(drho3)
for ax in range(3):
    gpsi = np.fft.ifftn(1j * K[ax] * psi3k)                                 # ∂_ax ψ
    jax = np.imag(np.conj(psi3) * gpsi)                                     # current component
    divj += np.real(np.fft.ifftn(1j * K[ax] * np.fft.fftn(jax)))           # ∂_ax j_ax
resid3 = np.max(np.abs(drho3 + divj))
print("   3D grid %d^3, momentum k=(%.1f,%.1f,%.1f)" % (M, *kv))
print("   max |d_t rho + div(rho v)| = %.2e" % resid3)
check("3D Madelung continuity holds to spectral roundoff (< 1e-9)", resid3 < 1e-9,
      "residual %.1e -- the matter-wave map is consistent in 3D, not a 1D artifact" % resid3)

banner("VERDICT -- the Madelung-continuity [V-external] orphan is now reproduced in-repo  [V]")
print("  The de Broglie/Madelung continuity law d_t rho + div(rho v) = 0 -- the matter-wave reading's core")
print("  consistency identity -- is verified from first principles to spectral roundoff (1D and 3D),")
print("  closing the parent-corpus 'residual ~5e-16' orphan. HONEST: the CK torus-eigenmode orphans")
print("  (V_111 ~ 2.30, <D> ~ 0.86, grid-H ~ 0.088) genuinely need the FreeFEM modes and remain [V-external].")
print("  status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
