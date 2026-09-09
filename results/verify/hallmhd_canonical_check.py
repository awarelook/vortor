"""
Hall-MHD canonical-enstrophy extension: numerical verification (CPU, spectral, T^3).

Ports the R2 near-Beltrami machinery to the ION generalized (canonical) vorticity of
incompressible resistive-viscous Hall-MHD:

    Omega = B + d_i * omega ,   omega = curl(v) ,   d_i = m_i/(q_i)  (ion skin depth scale)
    ideal canonical vortex dynamics:  d_t Omega = curl(v x Omega)          (frozen into ION flow v)

Two things to establish:

  TEST A -- the canonical Lamb-vector identity for INDEPENDENT divergence-free fields
            (v and Omega are NOT related by Omega=curl v here, unlike NSE):
                P := int Omega . curl(v x Omega)  ==  int (curl Omega).(v x Omega)
            and P is bounded by ||grad Omega||_2 * ||v x Omega||_2, and VANISHES on the
            aligned / double-Beltrami state v || Omega (canonical Lamb vector L = v x Omega = 0),
            scaling LINEARLY in the deviation near alignment.

  TEST B -- the dissipation coercivity. Canonical-enstrophy dissipation is
                D = int [ eta * grad(Omega).grad(B) + d_i*nu * grad(Omega).grad(omega) ] .
            Claim: at eta=nu (magnetic Prandtl Pm=nu/eta=1) this is the PERFECT SQUARE
            D = eta*||grad Omega||_2^2 >= 0 (coercive -> the NSE theorem ports verbatim);
            for eta!=nu the quadratic form in (grad B, grad omega) is INDEFINITE
            (2x2 matrix determinant = -d_i^2 (eta-nu)^2 / 4 <= 0), so canonical enstrophy
            alone is NOT a-priori controlled -- the explicit obstruction to the Hall lift.
"""
import numpy as np

N = 48
L = 2*np.pi
x = np.linspace(0, L, N, endpoint=False)
X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
k1 = np.fft.fftfreq(N, d=L/N) * 2*np.pi
KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij')
K2 = KX**2 + KY**2 + KZ**2
K2s = K2.copy(); K2s[0,0,0] = 1.0
dV = (L/N)**3

def fft(f):  return np.fft.fftn(f)
def ifft(F): return np.real(np.fft.ifftn(F))
def ddx(f, KI): return ifft(1j*KI*fft(f))
def grad(f): return [ddx(f,KX), ddx(f,KY), ddx(f,KZ)]
def curl(a):
    ax,ay,az = a
    return [ddx(az,KY)-ddx(ay,KZ), ddx(ax,KZ)-ddx(az,KX), ddx(ay,KX)-ddx(ax,KY)]
def div(a):
    ax,ay,az = a
    return ddx(ax,KX)+ddx(ay,KY)+ddx(az,KZ)
def cross(a,b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
def dot_int(a,b): return sum((a[i]*b[i]).sum() for i in range(3))*dV
def l2(a): return np.sqrt(sum((a[i]**2).sum() for i in range(3))*dV)
def leray(a):
    Ax,Ay,Az = fft(a[0]), fft(a[1]), fft(a[2])
    kdotA = (KX*Ax + KY*Ay + KZ*Az)/K2s
    return [ifft(Ax-KX*kdotA), ifft(Ay-KY*kdotA), ifft(Az-KZ*kdotA)]
def gradnorm2(a):  # ||grad a||_2^2 for a vector field a
    s = 0.0
    for i in range(3):
        for KI in (KX,KY,KZ):
            s += (ddx(a[i],KI)**2).sum()*dV
    return s
def grad_dot(a,b): # int grad(a):grad(b) = sum_i grad(a_i).grad(b_i)
    s = 0.0
    for i in range(3):
        for KI in (KX,KY,KZ):
            s += (ddx(a[i],KI)*ddx(b[i],KI)).sum()*dV
    return s

def rand_divfree(seed, width=4.0):
    rng = np.random.default_rng(seed)
    raw = []
    for _ in range(3):
        F = rng.standard_normal((N,N,N)) + 1j*rng.standard_normal((N,N,N))
        F *= np.exp(-K2/(2*width**2)); raw.append(ifft(F))
    return leray(raw)

def P_curlform(v, W):   return dot_int(W, curl(cross(v, W)))       # int Omega . curl(v x Omega)
def P_lambform(v, W):   return dot_int(curl(W), cross(v, W))       # int (curl Omega).(v x Omega)

print("="*78)
print("TEST A  canonical Lamb identity for INDEPENDENT div-free (v, Omega)")
print("        [v and Omega are NOT related by Omega=curl v -- the genuine 2-fluid case]")
print("="*78)
for s in range(3):
    v = rand_divfree(10+s); W = rand_divfree(200+s)   # independent fields
    Pc, Pl = P_curlform(v,W), P_lambform(v,W)
    rel = abs(Pc-Pl)/max(abs(Pc),1e-30)
    bound = np.sqrt(gradnorm2(W))*l2(cross(v,W))
    ok = abs(Pl) <= bound*(1+1e-9)
    print(f"  trial {s}:  P(curl)={Pc: .6e}  P(lamb)={Pl: .6e}  rel.diff={rel:.2e}  |P|<=bound: {ok}")

print()
print("  aligned state v || Omega  (Omega = c*v, both div-free)  -> P must be 0:")
v = rand_divfree(77)
W = [3.0*v[i] for i in range(3)]                      # Omega = 3 v : exactly aligned
print(f"     ||v x Omega||_2 = {l2(cross(v,W)):.2e}   P(lamb) = {P_lambform(v,W):.2e}")
print("  near-aligned  Omega = 3 v + eps * w_perp     -> P scales LINEARLY in eps:")
wp = rand_divfree(88)
for eps in [1e-1, 1e-2, 1e-3]:
    W = [3.0*v[i] + eps*wp[i] for i in range(3)]
    print(f"     eps={eps:.0e}:  ||v x Omega||={l2(cross(v,W)):.3e}   P={P_lambform(v,W): .3e}   P/eps={P_lambform(v,W)/eps: .3e}")

print()
print("="*78)
print("TEST B  canonical-enstrophy dissipation:  Pm=1 coercive vs (eta-nu)^2 obstruction")
print("        D(eta,nu) = int[ eta grad(Om).grad(B) + d_i nu grad(Om).grad(om) ],  Om=B+d_i om")
print("="*78)
d_i = 0.7
B  = rand_divfree(301)              # magnetic field (div-free)
om = rand_divfree(302)              # fluid vorticity (div-free)
Om = [B[i] + d_i*om[i] for i in range(3)]
def D(eta, nu):
    return eta*grad_dot(Om, B) + d_i*nu*grad_dot(Om, om)
gO2 = gradnorm2(Om)
print(f"  ||grad Omega||_2^2 = {gO2:.6e}")
for eta,nu in [(1.0,1.0),(1.0,0.5),(0.5,1.0),(1.0,2.0),(2.0,1.0)]:
    Dval = D(eta,nu)
    # at eta=nu the perfect-square prediction is eta*||grad Omega||^2:
    pred = eta*gO2
    print(f"  eta={eta:.2f} nu={nu:.2f} (Pm={nu/eta:.2f}):  D={Dval: .6e}   eta*||gradOm||^2={pred: .6e}"
          f"   match@Pm1: {abs(Dval-pred)/max(abs(pred),1e-30):.1e}" if eta==nu else
          f"  eta={eta:.2f} nu={nu:.2f} (Pm={nu/eta:.2f}):  D={Dval: .6e}   D/||gradOm||^2={Dval/gO2: .4f}")

print()
print("  Engineer the worst-case config B = -s* om (grad B anti-aligned with grad om) to")
print("  drive D NEGATIVE when eta!=nu -- canonical enstrophy PRODUCED by 'dissipation':")
for eta,nu in [(1.0,1.0),(1.0,0.25),(0.25,1.0),(1.0,4.0)]:
    s_star = d_i*(eta+nu)/(2*eta)                 # minimizer of the pointwise form
    B2  = [-s_star*om[i] for i in range(3)]
    Om2 = [B2[i] + d_i*om[i] for i in range(3)]   # = (d_i - s*) om  (nonzero -> legitimate Omega)
    Dmin = eta*grad_dot(Om2,B2) + d_i*nu*grad_dot(Om2,om)
    coeff = eta*s_star**2 - d_i*(eta+nu)*s_star + d_i**2*nu
    pred  = -d_i**2*(eta-nu)**2/(4*eta)           # predicted min coefficient
    print(f"     eta={eta:.2f} nu={nu:.2f}:  D_worst={Dmin: .4e}   min-coeff={coeff: .4e}  "
          f"predicted -d_i^2(eta-nu)^2/4eta={pred: .4e}")

print()
print("  2x2 form matrix M=[[eta, d_i(eta+nu)/2],[d_i(eta+nu)/2, d_i^2 nu]]  det = -d_i^2(eta-nu)^2/4:")
for eta,nu in [(1.0,1.0),(1.0,0.5),(2.0,0.5)]:
    det = eta*d_i**2*nu - (d_i*(eta+nu)/2)**2
    print(f"     eta={eta:.2f} nu={nu:.2f}:  det={det: .6e}   -d_i^2(eta-nu)^2/4={-d_i**2*(eta-nu)**2/4: .6e}")
print()
print("READING: at Pm=1 (eta=nu) dissipation is the perfect square eta*||grad Omega||^2 (coercive)")
print("-> NSE conditional theorem ports verbatim to canonical enstrophy. For Pm!=1 the form is")
print("indefinite (det<0), canonical enstrophy can be produced by dissipation, and the a-priori")
print("bound on Z_i alone fails -- the explicit, quantified obstruction to the unconditional lift.")
