"""
R2 analytic-route verification (CPU, spectral, periodic box).

Verifies the load-bearing EXACT identity that makes the near-Beltrami
enstrophy closure work:

    P := integral omega . (omega . grad) v            (vortex stretching / enstrophy production)
       = integral (curl omega) . (v x omega)          (Lamb-vector form)

Consequences checked:
  (1) the two forms agree for an ARBITRARY smooth divergence-free field (to round-off);
  (2) both vanish for an exact Beltrami field (ABC flow, curl v = v), so production = 0;
  (3) the a-priori bound |P| <= ||grad omega||_2 * ||v x omega||_2 holds;
  (4) ||curl omega||_2 = ||grad omega||_2 for divergence-free omega (used in the bound).

All operators are spectral on T^3 = [0,2pi)^3, so derivatives are exact up to aliasing.
"""
import numpy as np

N = 48
L = 2*np.pi
x = np.linspace(0, L, N, endpoint=False)
X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
k1 = np.fft.fftfreq(N, d=L/N) * 2*np.pi          # integer wavenumbers
KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij')
K2 = KX**2 + KY**2 + KZ**2
K2s = K2.copy(); K2s[0,0,0] = 1.0                 # avoid /0 for the mean mode
dV = (L/N)**3

def fft(f):  return np.fft.fftn(f)
def ifft(F): return np.real(np.fft.ifftn(F))
def ddx(f, KI): return ifft(1j*KI*fft(f))

def grad(f):        return [ddx(f,KX), ddx(f,KY), ddx(f,KZ)]
def curl(a):
    ax,ay,az = a
    return [ddx(az,KY)-ddx(ay,KZ), ddx(ax,KZ)-ddx(az,KX), ddx(ay,KX)-ddx(ax,KY)]
def div(a):
    ax,ay,az = a
    return ddx(ax,KX)+ddx(ay,KY)+ddx(az,KZ)
def cross(a,b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
def dot_int(a,b):   # integral a.b dV
    return sum((a[i]*b[i]).sum() for i in range(3))*dV
def l2(a):
    return np.sqrt(sum((a[i]**2).sum() for i in range(3))*dV)

def leray(a):
    """Project onto divergence-free part (Leray / Helmholtz)."""
    Ax,Ay,Az = fft(a[0]), fft(a[1]), fft(a[2])
    kdotA = (KX*Ax + KY*Ay + KZ*Az)/K2s
    return [ifft(Ax-KX*kdotA), ifft(Ay-KY*kdotA), ifft(Az-KZ*kdotA)]

def stretching_direct(v, omega):
    # integral omega . (omega . grad) v
    gvx, gvy, gvz = grad(v[0]), grad(v[1]), grad(v[2])
    adv = [ omega[0]*gvx[0]+omega[1]*gvx[1]+omega[2]*gvx[2],
            omega[0]*gvy[0]+omega[1]*gvy[1]+omega[2]*gvy[2],
            omega[0]*gvz[0]+omega[1]*gvz[1]+omega[2]*gvz[2] ]
    return dot_int(omega, adv)

def stretching_lamb(v, omega):
    # integral (curl omega) . (v x omega)
    return dot_int(curl(omega), cross(v, omega))

rng = np.random.default_rng(0)

print("="*74)
print("TEST 1  fields with GENUINELY nonzero stretching: two forms of P must agree")
print("        (NB: a Gaussian random field has ~0 net stretching -- it is an odd/")
print("         cubic moment of jointly-Gaussian fields -- so we use non-Gaussian")
print("         fields here, where P is O(1) and the identity is actually exercised.)")
print("="*74)

def report(name, v):
    v = leray(v)
    omega = curl(v)
    P1 = stretching_direct(v, omega)
    P2 = stretching_lamb(v, omega)
    rel = abs(P1-P2)/max(abs(P1), 1e-30)
    scale = l2(omega)**2 * l2(v)              # ~ typical size of a cubic-in-field integral
    relscale = abs(P1)/max(scale,1e-30)
    print(f"  {name:26s} P_direct={P1: .5e}  P_lamb={P2: .5e}  rel.diff(forms)={rel:.2e}  |P|/scale={relscale:.2e}")

# Fields with ENGINEERED vorticity-strain alignment -> |P| genuinely O(scale).
# Take a Gaussian field, advance vorticity by one small Euler step of the Euler
# equation (omega += dt*(omega.grad)v); this builds the omega/strain alignment that
# a static random field lacks, giving a sizable net production, and reconstruct v
# from the stretched omega via Biot-Savart (v = curl(-Delta^-1 omega)).
def biot_savart(omega):
    Ox,Oy,Oz = fft(omega[0]),fft(omega[1]),fft(omega[2])
    Ax,Ay,Az = Ox/K2s, Oy/K2s, Oz/K2s        # A = (-Delta)^-1 omega  (vector potential)
    A = [ifft(Ax),ifft(Ay),ifft(Az)]
    return leray(curl(A))                     # v = curl A, div-free
for trial in range(3):
    raw = []
    for _ in range(3):
        F = (rng.standard_normal((N,N,N)) + 1j*rng.standard_normal((N,N,N)))
        F *= np.exp(-K2/(2*5.0**2)); raw.append(ifft(F))
    v = leray(raw); omega = curl(v)
    for _ in range(6):                        # a few Euler steps to build alignment
        gvx,gvy,gvz = grad(v[0]),grad(v[1]),grad(v[2])
        stretch = [omega[0]*gvx[0]+omega[1]*gvx[1]+omega[2]*gvx[2],
                   omega[0]*gvy[0]+omega[1]*gvy[1]+omega[2]*gvy[2],
                   omega[0]*gvz[0]+omega[1]*gvz[1]+omega[2]*gvz[2]]
        adv = [ (v[0]*grad(omega[i])[0]+v[1]*grad(omega[i])[1]+v[2]*grad(omega[i])[2]) for i in range(3)]
        omega = [omega[i] + 0.02*(stretch[i]-adv[i]) for i in range(3)]
        omega = leray(omega)
        v = biot_savart(omega)
    report(f"aligned (Euler-evolved) #{trial}", v)
# For contrast: a raw Gaussian random field (net stretching ~ 0, an odd Gaussian moment)
raw = []
for _ in range(3):
    F = (rng.standard_normal((N,N,N)) + 1j*rng.standard_normal((N,N,N)))
    F *= np.exp(-K2/(2*4.0**2)); raw.append(ifft(F))
report("raw Gaussian (P~0 expected)", raw)

print()
print("="*74)
print("TEST 2  exact Beltrami (ABC flow, curl v = v): production must be ~0")
print("="*74)
A,B,C = 1.0, 0.7, 0.5
vB = [A*np.sin(Z)+C*np.cos(Y), B*np.sin(X)+A*np.cos(Z), C*np.sin(Y)+B*np.cos(X)]
oB = curl(vB)
beltrami_resid = l2([oB[i]-vB[i] for i in range(3)])/l2(vB)   # ||curl v - v||/||v||
P1 = stretching_direct(vB, oB); P2 = stretching_lamb(vB, oB)
lamb = l2(cross(vB, oB))
print(f"  Beltrami residual ||curl v - v||/||v|| = {beltrami_resid:.2e}   (0 => exact Beltrami)")
print(f"  Lamb vector ||v x omega||_2            = {lamb:.2e}   (0 => force-free)")
print(f"  P_direct = {P1:.3e}   P_lamb = {P2:.3e}   (both -> 0)")

print()
print("="*74)
print("TEST 3  a-priori bound  |P| <= ||grad omega||_2 * ||v x omega||_2")
print("        and identity    ||curl omega||_2 == ||grad omega||_2  (div-free omega)")
print("="*74)
raw = []
for _ in range(3):
    F = (rng.standard_normal((N,N,N)) + 1j*rng.standard_normal((N,N,N)))
    F *= np.exp(-K2/(2*5.0**2)); raw.append(ifft(F))
v = leray(raw); omega = curl(v)
P = stretching_lamb(v, omega)
# ||grad omega||_2^2 = sum over components of |grad omega_i|^2
grad_omega_sq = 0.0
for i in range(3):
    for KI in (KX,KY,KZ):
        grad_omega_sq += (ddx(omega[i],KI)**2).sum()*dV
grad_omega = np.sqrt(grad_omega_sq)
curl_omega = l2(curl(omega))
lamb = l2(cross(v, omega))
rhs = grad_omega*lamb
print(f"  |P|                       = {abs(P):.6e}")
print(f"  ||grad omega||_2*||L||_2  = {rhs:.6e}   -> bound holds: {abs(P) <= rhs*(1+1e-9)}")
print(f"  ||curl omega||_2          = {curl_omega:.6e}")
print(f"  ||grad omega||_2          = {grad_omega:.6e}   rel.diff={abs(curl_omega-grad_omega)/grad_omega:.2e}")
print()
print("ALL CHECKS DONE.")
