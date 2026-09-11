"""
DRIVEN CANONICAL HELICITY 4-CURRENT -- RIGOROUS version on GENUINE double-Beltrami equilibria.

A true steady ideal two-fluid (double-Beltrami) equilibrium satisfies v_s x Omega_s = grad mu_s.
For a double-Beltrami state (B and v both in span{G+,G-}, curl G_pm = lam_pm G_pm) one has
      v x Omega = (e1 o2 - e2 o1) (G+ x G-)
which is a GRADIENT (equilibrium) only when the scalar coefficient (e1 o2 - e2 o1) = 0, i.e. v || Omega
everywhere. Then v x Omega == 0 EXACTLY, so mu_s = const (Bernoulli constant) -- the standard
double-Beltrami "Bernoulli-constant" state. This is the physical equilibrium; the arbitrary-coefficient
states used before had eq-defect ~ 1 (not equilibria) and are discarded.

On a genuine equilibrium (mu = const) the generalized-helicity flux
      K = h v + (mu - P.v) Omega ,   h = P.Omega
is a PURE matter current (h, h v)  IFF   S := mu - P.v = 0, i.e.  P.v = const = mu.
=> analog iff-condition:  the driven canonical 4-current closes  IFF  P.v is spatially constant.
(Static analog was: closes IFF |B| const, residual = std(|B|^2)/mean = 0.577.)

We enforce v || Omega exactly, verify v x Omega = 0, then measure the closure residual
   rho_res = ||S Omega|| / ||h v||    and    the direct iff-metric  std(P.v)/mean(P.v),
scanning the flow amplitude e1 and inertial length d, for two routes (single-fluid lam=1,sqrt2 and
the project near-degenerate lam+=3.85213, lam-=3.57038). Also the sub-limit v||P (single canonical
Beltrami) -> relocates to |P|=const, and the constant-|P| control that closes exactly.
"""
import numpy as np

np.random.seed(7)
N = 24
L = 2.0*np.pi
x = np.linspace(0, L, N, endpoint=False)
X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
k1 = np.fft.fftfreq(N, d=L/N)*2*np.pi
KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij')

def curl(Fx, Fy, Fz):
    fx, fy, fz = np.fft.fftn(Fx), np.fft.fftn(Fy), np.fft.fftn(Fz)
    cx = np.fft.ifftn(1j*(KY*fz - KZ*fy)).real
    cy = np.fft.ifftn(1j*(KZ*fx - KX*fz)).real
    cz = np.fft.ifftn(1j*(KX*fy - KY*fx)).real
    return cx, cy, cz

def beltrami_field(kvecs):
    Fx=np.zeros_like(X,dtype=complex); Fy=np.zeros_like(X,dtype=complex); Fz=np.zeros_like(X,dtype=complex)
    for k in kvecs:
        k=np.array(k,dtype=float); kn=np.linalg.norm(k); khat=k/kn
        ref=np.array([1.0,0,0]) if abs(khat[0])<0.9 else np.array([0,1.0,0])
        e1=ref-np.dot(ref,khat)*khat; e1/=np.linalg.norm(e1); e2=np.cross(khat,e1)
        hplus=(e1+1j*e2)/np.sqrt(2.0)
        amp=(np.random.randn()+1j*np.random.randn())
        ph=np.exp(1j*(k[0]*X+k[1]*Y+k[2]*Z))
        Fx+=amp*hplus[0]*ph; Fy+=amp*hplus[1]*ph; Fz+=amp*hplus[2]*ph
    Fx,Fy,Fz=Fx.real,Fy.real,Fz.real
    r=np.sqrt(np.mean(Fx**2+Fy**2+Fz**2)); return Fx/r,Fy/r,Fz/r

def dot(a,b,c,d,e,f): return a*d+b*e+c*f
def cross(a,b,c,d,e,f): return (b*f-c*e, c*d-a*f, a*e-b*d)
def rms(*cs): return np.sqrt(np.mean(sum(c**2 for c in cs)))

Gp=beltrami_field([(1,0,0),(0,1,0),(0,0,1)])
Gm=beltrami_field([(1,1,0),(0,1,1),(1,0,1)])
GpGm = dot(*Gp,*Gm)  # G+ . G-  (not orthogonal pointwise; volume-integral ~0)
print("volume <G+.G-> (should be ~0, distinct-eigenvalue orthogonality):", np.mean(GpGm))

def aligned_state(c1,c2,e1,d,lp,lm):
    """Return fields for the v||Omega equilibrium: e2 solved so (e1 o2 - e2 o1)=0."""
    # o1 = c1 + d e1 lp, o2 = c2 + d e2 lm ; enforce e1 o2 = e2 o1
    # e1(c2 + d e2 lm) = e2(c1 + d e1 lp) -> e2 = e1 c2 / (c1 + d e1 (lp - lm))
    denom = c1 + d*e1*(lp-lm)
    if abs(denom) < 1e-12: return None
    e2 = e1*c2/denom
    Bx=c1*Gp[0]+c2*Gm[0]; By=c1*Gp[1]+c2*Gm[1]; Bz=c1*Gp[2]+c2*Gm[2]
    Ax=c1/lp*Gp[0]+c2/lm*Gm[0]; Ay=c1/lp*Gp[1]+c2/lm*Gm[1]; Az=c1/lp*Gp[2]+c2/lm*Gm[2]
    vx=e1*Gp[0]+e2*Gm[0]; vy=e1*Gp[1]+e2*Gm[1]; vz=e1*Gp[2]+e2*Gm[2]
    wx=e1*lp*Gp[0]+e2*lm*Gm[0]; wy=e1*lp*Gp[1]+e2*lm*Gm[1]; wz=e1*lp*Gp[2]+e2*lm*Gm[2]
    Px,Py,Pz=Ax+d*vx,Ay+d*vy,Az+d*vz
    Ox,Oy,Oz=Bx+d*wx,By+d*wy,Bz+d*wz
    return (Px,Py,Pz),(Ox,Oy,Oz),(vx,vy,vz),e2

def closure(c1,c2,e1,d,lp,lm):
    st=aligned_state(c1,c2,e1,d,lp,lm)
    if st is None: return None
    (Px,Py,Pz),(Ox,Oy,Oz),(vx,vy,vz),e2=st
    # verify equilibrium: v x Omega should be ~0
    vxO=cross(vx,vy,vz,Ox,Oy,Oz); eqres=rms(*vxO)/(rms(vx,vy,vz)*rms(Ox,Oy,Oz)+1e-30)
    Pmag_rms=rms(Px,Py,Pz); Amag_rms=rms(c1/lp*Gp[0]+c2/lm*Gm[0],c1/lp*Gp[1]+c2/lm*Gm[1],c1/lp*Gp[2]+c2/lm*Gm[2])
    collapse = Pmag_rms < 0.05*Amag_rms   # guard: P ~ 0 (A + d v cancels) is trivial, not a closure
    h=dot(Px,Py,Pz,Ox,Oy,Oz)
    Pv=dot(Px,Py,Pz,vx,vy,vz)
    mu=np.mean(Pv)                     # Bernoulli constant (gauge: mean)
    S=mu-Pv
    rho_res=rms(S*Ox,S*Oy,S*Oz)/(rms(h*vx,h*vy,h*vz)+1e-30)
    Pv_spread=np.std(Pv)/(abs(np.mean(Pv))+1e-30)
    return dict(rho=rho_res,pvspread=Pv_spread,eqres=eqres,e2=e2,collapse=collapse,
                Pmag_spread=np.std(np.sqrt(dot(Px,Py,Pz,Px,Py,Pz)))/np.mean(np.sqrt(dot(Px,Py,Pz,Px,Py,Pz))))

print()
print("="*80)
print("GENUINE double-Beltrami equilibria (v||Omega, mu=const). eqres must be ~0.")
print("Closure iff-metric: std(P.v)/mean(P.v). rho_res = ||S Omega||/||h v||.")
print("="*80)
for lp,lm,tag in [(1.0,np.sqrt(2.0),"route a: lam 1, sqrt2"),
                  (3.85213,3.57038,"route b: project near-degen")]:
    print(f"\n--- {tag} ---")
    print(f"{'d':>6} {'e1':>7} | {'eqres':>9} {'rho_res':>9} {'std(P.v)/mean':>14} {'std|P|/mean':>12}")
    best=1e9; bestcfg=None
    for d in [0.2,0.5,1.0,2.0]:
        for e1 in [0.1,0.3,0.6,1.0,2.0,4.0,-0.3,-1.0,-3.0]:
            r=closure(1.0,1.0,e1,d,lp,lm)
            if r is None or r['collapse']: continue
            if r['pvspread']<best: best=r['pvspread']; bestcfg=(d,e1,r)
    # print a representative sweep at d=0.5
    for e1 in [0.1,0.3,0.6,1.0,2.0,4.0]:
        r=closure(1.0,1.0,e1,0.5,lp,lm)
        if r: print(f"{0.5:6.2f} {e1:7.2f} | {r['eqres']:9.2e} {r['rho']:9.4f} {r['pvspread']:14.4f} {r['Pmag_spread']:12.4f}")
    d,e1,r=bestcfg
    print(f"  BEST std(P.v)/mean over scan: {best:.4f} at d={d}, e1={e1} (rho_res={r['rho']:.4f}, eqres={r['eqres']:.1e})")

print()
print("="*80)
print("SUB-LIMIT v||P  (single canonical Beltrami, e proportional to canonical) -> |P|=const wall")
print("="*80)
# v || P means the flow is the canonical field itself: build P as single-mode canonical Beltrami.
# Take a single Beltrami mode for P: P = Gp (curl P = 1*Gp), Omega = Gp, v = xi Gp. Then P.v = xi|Gp|^2.
Pm=np.sqrt(dot(*Gp,*Gp))
print(f"  single-mode |P| std/mean = {np.std(Pm)/np.mean(Pm):.4f}  (P.v spread = same) -> the |P|=const wall")
print(f"  (this is the DIRECT analog of the static |B| std/mean; nontrivial Beltrami cannot be constant)")

print()
print("="*80)
print("CONTROL: constant-|P| Beltrami closes EXACTLY (analog of static constant-|B|)")
print("="*80)
# B0(cos z, sin z, 0): curl = -B ; |.|=const. Use as canonical field P.
Px=np.cos(Z); Py=np.sin(Z); Pz=np.zeros_like(Z)
Pmag=np.sqrt(Px**2+Py**2)
print(f"  constant-|P| field: std|P|/mean = {np.std(Pmag)/np.mean(Pmag):.2e}")
# v || Omega=P (Beltrami), v = xi P: P.v = xi|P|^2 = const -> S=0
Pv=Px*Px+Py*Py+Pz*Pz  # xi=1
print(f"  std(P.v)/mean = {np.std(Pv)/np.mean(Pv):.2e}  -> closes EXACTLY (residual 0)")

print()
print("DONE")
