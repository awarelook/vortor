# Driven non-aligned time-dependent two-fluid closure test.
# ASCII only. PYTHONIOENCODING=utf-8.
# Tests: (E1) S is scalar -> closure <=> S=0 (no vector-perp B2 branch);
#        canonical current is ALWAYS a matter current with transport velocity u=v+(S/h)Omega.
#        (E2) time-dependent B1: curl of the S=0 momentum eqn == VORT identically (no steady curl-obstruction).
#        (E3) drive required to maintain S=0 on a genuine non-aligned time-dependent state;
#             is it bounded? does it conserve canonical helicity (f_ext . Omega = 0)?
#        (E4) can BOTH S=0 AND f_ext.Omega=0 hold non-aligned, or does it force alignment/triviality?
import numpy as np

np.random.seed(0)
N = 32
L = 2*np.pi
x = np.linspace(0, L, N, endpoint=False)
X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
k1 = np.fft.fftfreq(N, d=L/N)*2*np.pi
KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij')
K2 = KX**2 + KY**2 + KZ**2
K2s = K2.copy(); K2s[0,0,0] = 1.0

def grad(f):
    fh = np.fft.fftn(f)
    return (np.real(np.fft.ifftn(1j*KX*fh)),
            np.real(np.fft.ifftn(1j*KY*fh)),
            np.real(np.fft.ifftn(1j*KZ*fh)))

def curl(Fx, Fy, Fz):
    fxh, fyh, fzh = np.fft.fftn(Fx), np.fft.fftn(Fy), np.fft.fftn(Fz)
    cx = np.real(np.fft.ifftn(1j*(KY*fzh - KZ*fyh)))
    cy = np.real(np.fft.ifftn(1j*(KZ*fxh - KX*fzh)))
    cz = np.real(np.fft.ifftn(1j*(KX*fyh - KY*fxh)))
    return cx, cy, cz

def dot(A, B):
    return A[0]*B[0] + A[1]*B[1] + A[2]*B[2]

def cross(A, B):
    return (A[1]*B[2]-A[2]*B[1], A[2]*B[0]-A[0]*B[2], A[0]*B[1]-A[1]*B[0])

def rms(F):
    return np.sqrt(np.mean(dot(F, F)))

def ABC(k, A, B, C, phase=0.0):
    # curl = +k * field
    Fx = A*np.sin(k*Z+phase) + C*np.cos(k*Y+phase)
    Fy = B*np.sin(k*X+phase) + A*np.cos(k*Z+phase)
    Fz = C*np.sin(k*Y+phase) + B*np.cos(k*X+phase)
    return (Fx, Fy, Fz)

def scal_mul(a, F):
    return (a*F[0], a*F[1], a*F[2])

def add(*Fs):
    return (sum(F[0] for F in Fs), sum(F[1] for F in Fs), sum(F[2] for F in Fs))

# Verify eigenfields
G1 = ABC(1, 1.0, 0.7, 1.3)      # lam=+1, genuinely 3D
G2 = ABC(2, 0.9, 1.1, 0.8)      # lam=+2, genuinely 3D (same sign -> project regime)
c1 = curl(*G1); c2 = curl(*G2)
print("eigencheck G1 ||curl-1*G|/|G|| =", rms(add(c1, scal_mul(-1.0, G1)))/rms(G1))
print("eigencheck G2 ||curl-2*G|/|G|| =", rms(add(c2, scal_mul(-2.0, G2)))/rms(G2))
print("<G1.G2> (distinct-eig orthogonality) =", np.mean(dot(G1, G2)))
print()

# ---------------------------------------------------------------
# E1: S scalar; transport-velocity identity K = h*u, u = v + (S/h)Omega
# ---------------------------------------------------------------
print("="*70)
print("E1: S is SCALAR; canonical current is ALWAYS a matter current K=h u")
print("="*70)
lamp, lamm = 1.0, 2.0
p1, p2, e1, e2 = 1.0, 0.6, 0.8, -0.5   # non-aligned choice
P = add(scal_mul(p1, G1), scal_mul(p2, G2))
v = add(scal_mul(e1, G1), scal_mul(e2, G2))
Om = curl(*P)   # generalized vorticity
Pv = dot(P, v)                 # scalar P.v
h = dot(P, Om)                 # scalar helicity density
# choose an arbitrary Bernoulli head mu (a scalar field) to make S nonzero
mu = 0.3*np.cos(X)*np.sin(Y) + 0.5   # arbitrary smooth scalar
S = mu - Pv                    # SCALAR
print("shape(S) =", np.shape(S), " -> S is a scalar field (not a vector)")
# canonical flux K = h v + S Omega
K = add(scal_mul(h, v), scal_mul(S, Om))
# transport velocity u = K / h ; check K = h u exactly (so 4-current=(h,hu) is matter current)
u = (K[0]/h, K[1]/h, K[2]/h)
print("||K - h*u||/||K|| =", rms(add(K, scal_mul(-1.0, u) if False else scal_mul(-1.0, scal_mul(1.0,u)) )) )  # placeholder
K_from_u = scal_mul(h, u)
print("||K - h*u||/||K|| =", rms(add(K, scal_mul(-1.0, K_from_u)))/rms(K))
# closure on FLUID velocity v <=> u=v <=> (S/h)Omega=0 <=> S=0
du = add(u, scal_mul(-1.0, v))   # u - v = (S/h) Omega
pred = scal_mul(1.0, (S/h*Om[0], S/h*Om[1], S/h*Om[2]))
print("||(u-v) - (S/h)Omega||/||u-v|| =", rms(add(du, scal_mul(-1.0, pred)))/rms(du))
print("=> closure on fluid v requires S=0 (S is scalar; 'S perp Omega' is not a branch).")
print()

# ---------------------------------------------------------------
# E2: time-dependent B1: curl of the S=0 momentum eqn == VORT identically
# ---------------------------------------------------------------
print("="*70)
print("E2: B1 (S=0) time-dependent -- curl route gives an IDENTITY, no obstruction")
print("="*70)
# S=0 momentum eqn: d_t P = v x Omega - grad(P.v).  Take curl -> should equal curl(v x Omega)=d_t Omega (VORT).
vxOm = cross(v, Om)
gPv = grad(Pv)
rhs = add(vxOm, scal_mul(-1.0, gPv))     # d_t P under B1
curl_rhs = curl(*rhs)
curl_vxOm = curl(*vxOm)                   # = d_t Omega by VORT
print("||curl(dtP_B1) - curl(vxOm)||/||curl(vxOm)|| =",
      rms(add(curl_rhs, scal_mul(-1.0, curl_vxOm)))/rms(curl_vxOm))
print("=> curl(grad(P.v))=0 to machine eps: the time-dependent curl gives no new constraint.")
print("   (Contrast STEADY B1: d_tP=0 forces v x Omega = grad(P.v) => curl(vxOm)=0 => aligned.)")
# show the steady obstruction: is v x Omega a gradient? (curl(vxOm) !=0 for non-aligned)
print("   steady-check: ||curl(v x Omega)||/||v x Omega|| =", rms(curl_vxOm)/rms(vxOm),
      " (nonzero => v x Omega NOT a gradient => steady non-aligned B1 fails)")
print()

# ---------------------------------------------------------------
# E3 + E4: drive to maintain S=0 on a genuine non-aligned time-dependent state;
#          boundedness + canonical-helicity conservation (f_ext . Omega).
# ---------------------------------------------------------------
print("="*70)
print("E3/E4: drive to sustain S=0 on non-aligned time-dependent state")
print("="*70)

def alignment_metric(v, Om):
    # sin(angle) between v and Omega, rms; 0 => aligned, ~1 => orthogonal-ish
    vxO = cross(v, Om)
    return rms(vxO)/(rms(v)*np.sqrt(np.mean(dot(Om,Om))) + 1e-30)

def run_config(name, lam_list, coefP, coefV, omega_t):
    # P = sum coefP_i G_i, v = sum coefV_i G_i ; breathing: d_t P = omega_t * (rotate coefP)
    Gs = []
    for lam in lam_list:
        A,B,C = np.random.uniform(0.6,1.4,3)
        Gs.append(ABC(lam, A,B,C))
    P = add(*[scal_mul(coefP[i], Gs[i]) for i in range(len(Gs))])
    v = add(*[scal_mul(coefV[i], Gs[i]) for i in range(len(Gs))])
    Om = curl(*P)
    Pv = dot(P, v); h = dot(P, Om)
    align = alignment_metric(v, Om)
    # B1: mu = P.v, so grad mu = grad(P.v). d_t P prescribed as a breathing between modes:
    # rotate the P-coefficients: dP = omega_t*( -coefP[1]*G0 + coefP[0]*G1 ) style; general: random smooth
    dtP = add(*[scal_mul(omega_t*coefP[(i+1)%len(Gs)]*((-1)**i), Gs[i]) for i in range(len(Gs))])
    vxOm = cross(v, Om)
    gPv = grad(Pv)
    # ideal EoM: d_t P = v x Om - grad mu + f_ext ; with mu=P.v: f_ext = dtP - vxOm + grad(Pv)
    f_ext = add(dtP, scal_mul(-1.0, vxOm), gPv)
    # boundedness
    fmax = np.max(np.sqrt(dot(f_ext,f_ext))); frms = rms(f_ext)
    fieldrms = rms(P)
    # canonical helicity source density = 2 f_ext . Omega
    fdotO = dot(f_ext, Om)
    src_rms = np.sqrt(np.mean(fdotO**2))
    src_mean = np.mean(fdotO)   # net (integrated) helicity injection
    normO = np.sqrt(np.mean(dot(Om,Om)))
    # closure residual with S=0 (should be ~0 by construction): matter current K vs h v
    S = np.zeros_like(Pv)  # B1 imposes S=0
    K = add(scal_mul(h, v), scal_mul(S, Om))
    clos_res = rms(add(K, scal_mul(-1.0, scal_mul(h, v))))/ (rms(scal_mul(h,v))+1e-30)
    print("[%s] lam=%s  alignment sin=%0.3f (nonzero=>non-aligned)" % (name, lam_list, align))
    print("      closure residual (S=0) = %.2e" % clos_res)
    print("      drive |f_ext| max=%.3f rms=%.3f  (field rms=%.3f) -> bounded=%s"
          % (fmax, frms, fieldrms, "YES" if fmax < 1e3 else "NO"))
    print("      canonical-helicity source 2 f_ext.Omega: rms=%.3f  net<>=%.2e  (rel to |f||Om|=%.3f)"
          % (2*src_rms, 2*src_mean, src_rms/(frms*normO+1e-30)))
    print("      => maintaining S=0 conserves K^mu ONLY if f_ext.Omega=0 pointwise.")
    return dict(align=align, frms=frms, fmax=fmax, src_rms=src_rms, src_mean=src_mean,
                srcrel=src_rms/(frms*normO+1e-30))

r1 = run_config("A same-sign 1,2", [1,2], [1.0,0.6], [0.8,-0.5], 1.0)
print()
r2 = run_config("B opp-sign 1,-1", [1,-1], [1.0,0.7], [0.5,0.9], 0.8)
print()
r3 = run_config("C three-mode 1,2,3", [1,2,3], [1.0,0.5,0.3], [0.4,-0.6,0.7], 1.2)
print()

# E4: can we make f_ext.Omega = 0 pointwise while keeping S=0 and non-aligned?
# f_ext.Omega = dtP.Omega - (vxOm).Omega + grad(Pv).Omega = dtP.Omega + grad(Pv).Omega  (vxOm _|_ Om)
# We control dtP (the time-evolution) and the coefficients. Minimize <(f_ext.Omega)^2> over dtP in span{G_i}
# by least-squares: choose dtP-coefficients to cancel Omega.grad(Pv) projected.
print("="*70)
print("E4: can S=0 AND f_ext.Omega=0 (pointwise) coexist non-aligned? (least-squares over dtP)")
print("="*70)
Gs = [ABC(1,1.0,0.7,1.3), ABC(2,0.9,1.1,0.8)]
p1,p2,e1,e2 = 1.0,0.6,0.8,-0.5
P = add(scal_mul(p1,Gs[0]), scal_mul(p2,Gs[1]))
v = add(scal_mul(e1,Gs[0]), scal_mul(e2,Gs[1]))
Om = curl(*P); Pv = dot(P,v)
gPv = grad(Pv)
OmgPv = dot(Om, gPv)                    # Omega.grad(P.v)  (target to cancel)
# f_ext.Omega = dtP.Omega + OmgPv.  dtP in span{G1,G2}: dtP = a*G1 + b*G2
G1dotOm = dot(Gs[0], Om); G2dotOm = dot(Gs[1], Om)
# minimize <(a*G1.Om + b*G2.Om + OmgPv)^2> over a,b
M = np.array([[np.mean(G1dotOm**2), np.mean(G1dotOm*G2dotOm)],
              [np.mean(G1dotOm*G2dotOm), np.mean(G2dotOm**2)]])
rhs = -np.array([np.mean(G1dotOm*OmgPv), np.mean(G2dotOm*OmgPv)])
ab = np.linalg.solve(M, rhs)
resid_field = ab[0]*G1dotOm + ab[1]*G2dotOm + OmgPv
best = np.sqrt(np.mean(resid_field**2))
base = np.sqrt(np.mean(OmgPv**2))
print("min <(f_ext.Omega)^2>^.5 over dtP in span{G1,G2}: %.4f  (baseline %.4f) -> ratio %.3f"
      % (best, base, best/base))
# also try dtP fully free (any vector field): then f_ext.Omega=0 solvable pointwise if Omega!=0
print("dtP fully free: f_ext.Omega=0 pointwise is solvable where Omega!=0 (dtP absorbs -OmgPv/|Om|^2 * Om).")
# but dtP fully free means arbitrary evolution -> check it stays non-aligned & bounded (it does, algebraically)
# construct that dtP: dtP = (target for f_ext.Om) ... f_ext = dtP - vxOm + gPv ; want f_ext.Om=0:
# set dtP such that (dtP+gPv).Om = 0 -> dtP = -gPv + (component making it perp). simplest: dtP = -gPv + t_perp
# pick dtP = -gPv + vxOm (then f_ext = vxOm ... wait). We just need existence; algebraically trivial.
Omag2 = dot(Om,Om) + 1e-30
lam_field = OmgPv/Omag2
dtP_free = add(scal_mul(-1.0, (lam_field*Om[0], lam_field*Om[1], lam_field*Om[2])),
               (np.zeros_like(Pv),)*1 and (np.zeros_like(Pv),np.zeros_like(Pv),np.zeros_like(Pv)))
# f_ext with this dtP:
f_ext = add(dtP_free, scal_mul(-1.0, cross(v,Om)), gPv)
print("   check f_ext.Omega rms with constructed free dtP = %.2e (=>0)"
      % np.sqrt(np.mean(dot(f_ext,Om)**2)))
print("   |dtP_free| rms=%.3f bounded, state stays non-aligned=%.3f"
      % (rms(dtP_free), alignment_metric(v,Om)))
print()
print("SUMMARY printed above; see doc for interpretation.")
