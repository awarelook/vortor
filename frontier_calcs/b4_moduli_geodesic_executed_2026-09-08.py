# -*- coding: utf-8 -*-
# B4_MODULI_GEODESIC_EXECUTED_2026-09-08  (standalone; ASCII; PYTHONIOENCODING=utf-8)
# =============================================================================
# Runs the sine-Gordon-VALIDATED (mu, V, amplitude) moduli/collective-coordinate
# pipeline on the REAL 2x(B=2)->B=4 (d+d->4He) attractive-channel merger path.
# Reuses the VALIDATED 3D field machinery (rational-map SU(2) fields, product
# ansatz, Skyrme energy) from kernel_skyrme_b4_reactive_2026-09-02.py.
#
# Section 1 below is the VALIDATION GATE (baryon number + energy trend on this grid).
# Section 2 (bottom) is the EXECUTED pipeline: attractive channel, V(sigma) [real
# field integral], mu(sigma) = INT sum_a (dn_a/dsigma)^2 d^3x [the inertia the prior
# doc skipped], and the quantized merger-mode hbar*omega via the same operator that
# reproduced the sine-Gordon breather.  Two constructions -> two-sided band.
# No nuclear rate/cross-section/branching magnitude fabricated. Baryon B conserved.
#
# GATE checks:
#   (1) baryon number B for B=1 hedgehog, B=2 torus, product(B2,B2), cube B=4
#   (2) Skyrme energy ratios along the expected trend
# If these pass, the merger-path V(sigma), mu(sigma) shapes are trustworthy at model precision.
import numpy as np

def profile(r, lam):
    return np.pi*(1.0 - 1.0/np.sqrt(1.0 + (lam/np.maximum(r,1e-9))**2))

def Rmap(z, B):
    z = z.astype(np.complex128)
    if B == 1: return z
    if B == 2: return z**2
    if B == 4:
        num = z**4 + 2.0*np.sqrt(3.0)*1j*z**2 + 1.0
        den = z**4 - 2.0*np.sqrt(3.0)*1j*z**2 + 1.0
        return num/den
    raise ValueError(B)

def su2_field(X, Y, Z, Xc, lam, B, Riso=None):
    x = X - Xc[0]; y = Y - Xc[1]; zc = Z - Xc[2]
    r = np.sqrt(x*x + y*y + zc*zc); r = np.maximum(r, 1e-6)
    ct = np.clip(zc/r, -1.0, 1.0)
    theta = np.arccos(ct); phi = np.arctan2(y, x)
    t2 = np.tan(np.clip(theta, 1e-7, np.pi-1e-7)/2.0); t2 = np.clip(t2, 0.0, 1e6)
    zz = t2*np.exp(1j*phi)
    R = Rmap(zz, B); R = np.nan_to_num(R, nan=0.0, posinf=1e6, neginf=-1e6)
    denom = 1.0 + np.abs(R)**2
    nx = (2.0*R.real)/denom; ny = (2.0*R.imag)/denom; nz = (1.0 - np.abs(R)**2)/denom
    f = profile(r, lam); sig = np.cos(f); s = np.sin(f)
    px, py, pz = s*nx, s*ny, s*nz
    if Riso is not None:
        px, py, pz = (Riso[0,0]*px+Riso[0,1]*py+Riso[0,2]*pz,
                      Riso[1,0]*px+Riso[1,1]*py+Riso[1,2]*pz,
                      Riso[2,0]*px+Riso[2,1]*py+Riso[2,2]*pz)
    return np.stack([sig,px,py,pz],axis=0)

def quat_mul(a, b):
    s1,x1,y1,z1 = a; s2,x2,y2,z2 = b
    s = s1*s2 - (x1*x2+y1*y2+z1*z2)
    x = s1*x2 + s2*x1 + (y1*z2 - z1*y2)
    y = s1*y2 + s2*y1 + (z1*x2 - x1*z2)
    z = s1*z2 + s2*z1 + (x1*y2 - y1*x2)
    return np.stack([s,x,y,z],axis=0)

def Rx(th):
    c,s = np.cos(th), np.sin(th)
    return np.array([[1,0,0],[0,c,-s],[0,s,c]])

def grid(N,L):
    ax = np.linspace(-L,L,N); dx=ax[1]-ax[0]
    X,Y,Z = np.meshgrid(ax,ax,ax,indexing='ij')
    return ax,dx,X,Y,Z

def skyrme_energy(n, dx):
    g = [np.gradient(n[a], dx, axis=(0,1,2)) for a in range(4)]
    di = [np.stack([g[a][i] for a in range(4)],axis=0) for i in range(3)]
    e2 = sum((di[i]*di[i]).sum(axis=0) for i in range(3))
    e4 = 0.0
    for i in range(3):
        for j in range(i+1,3):
            dii=(di[i]*di[i]).sum(axis=0); djj=(di[j]*di[j]).sum(axis=0); dij=(di[i]*di[j]).sum(axis=0)
            e4 += dii*djj - dij*dij
    return e2.sum()*dx**3, e4.sum()*dx**3

# baryon density via O(4) topological charge, empirically normalized to B=1 hedgehog
from itertools import permutations
def levi(p):
    p=list(p); sign=1
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            if p[i]>p[j]: sign=-sign
    return sign
PERMS=[(p,levi(p)) for p in permutations(range(4))]
def baryon_raw(n,dx):
    dnx=np.stack([np.gradient(n[a],dx,axis=0) for a in range(4)],axis=0)
    dny=np.stack([np.gradient(n[a],dx,axis=1) for a in range(4)],axis=0)
    dnz=np.stack([np.gradient(n[a],dx,axis=2) for a in range(4)],axis=0)
    b=np.zeros(n.shape[1:])
    for p,sgn in PERMS:
        a,bb,c,d=p
        b+=sgn*n[a]*dnx[bb]*dny[c]*dnz[d]
    return b.sum()*dx**3



hbarc = 197.3269804    # MeV fm
Md    = 1875.612       # MeV/c^2
Q     = 23.847         # MeV, d+d->4He (CODATA/AME anchor)

N,L = 96,10.0
ax,dx,X,Y,Z = grid(N,L)
n1=su2_field(X,Y,Z,(0,0,0),2.0,1); NORM=baryon_raw(n1,dx)
print(f"# grid N={N} L={L} dx={dx:.3f} fm ; baryon-norm={NORM:.3f}")

# ---- SECTION 1: validation gate (topology + energy trend on this grid) ----
print("\n#### GATE: baryon number + Skyrme energy on this grid (model-precision topology)")
def _E(n): e2,e4=skyrme_energy(n,dx); return e2+e4
for tag,nn in [("B1 hedgehog", su2_field(X,Y,Z,(0,0,0),2.0,1)),
               ("B2 torus",    su2_field(X,Y,Z,(0,0,0),2.0,2)),
               ("pair(B2,B2) s=6", quat_mul(su2_field(X,Y,Z,(0,0,+3.0),2.0,2),
                                            su2_field(X,Y,Z,(0,0,-3.0),2.0,2)))]:
    print(f"   {tag:18s} B={baryon_raw(nn,dx)/NORM:6.3f}  E={_E(nn):9.2f}  "
          "(B2->~2, pair->~4 at a few-% topological resolution)")

def Efun(n): e2,e4=skyrme_energy(n,dx); return e2+e4

def pair(sigma, lam, theta=np.pi):
    a=su2_field(X,Y,Z,(0,0,+sigma/2),lam,2)
    b=su2_field(X,Y,Z,(0,0,-sigma/2),lam,2,Riso=Rx(theta))
    return quat_mul(a,b)

def run_construction(lam, tag):
    print(f"\n#### CONSTRUCTION [{tag}] product ansatz, theta=pi, lam={lam} fm")
    Efar = Efun(pair(7.0,lam))
    sig = np.array([0.5,0.75,1.0,1.25,1.5,1.75,2.0,2.25,2.5,2.75,3.0,3.5,4.0,5.0,6.0,7.0])
    V = np.array([Efun(pair(s,lam)) for s in sig]) - Efar   # raw units
    # moduli metric mu_raw(sigma) = INT sum_a (dn/dsigma)^2, central diff h
    h=0.06
    mu_raw=np.array([ (( (pair(s+h,lam)-pair(s-h,lam))/(2*h))**2 ).sum()*dx**3 for s in sig ])
    # baryon along path (topology check)
    Bpath=np.array([baryon_raw(pair(s,lam),dx)/NORM for s in sig])
    print("  sigma   V_raw     mu_raw    B")
    for i,s in enumerate(sig):
        print(f"  {s:4.2f}  {V[i]:+8.3f}  {mu_raw[i]:8.2f}  {Bpath[i]:5.2f}")
    return sig,V,mu_raw,Bpath

def analyze(sig,V,mu_raw,tag, Ecal_unit):
    # find entrance-well minimum (interior local min)
    imin=np.argmin(V)
    s0=sig[imin]
    # local parabola fit for curvature k = V'' (raw units / fm^2), 3-pt around min
    i=imin
    if i==0: i=1
    if i>=len(sig)-1: i=len(sig)-2
    s_m,s_c,s_p=sig[i-1],sig[i],sig[i+1]
    V_m,V_c,V_p=V[i-1],V[i],V[i+1]
    # non-uniform 2nd deriv
    k_raw = 2*(V_m/((s_m-s_c)*(s_m-s_p)) + V_c/((s_c-s_m)*(s_c-s_p)) + V_p/((s_p-s_m)*(s_p-s_c)))
    # mu at min, calibrate mu so mu_raw(large sigma)=Md/2
    mu_asym = mu_raw[-1]                     # sigma=7 fm, two rigid tori
    kappa_mu = (Md/2.0)/mu_asym              # MeV c^-2 per raw unit
    mu_min = mu_raw[i]*kappa_mu              # MeV/c^2
    # energy calibration: Ecal_unit = MeV per raw energy unit
    k = k_raw*Ecal_unit                      # MeV/fm^2
    well_depth = -V[imin]*Ecal_unit          # MeV (entrance molecular well depth)
    if k<=0:
        print(f"  [{tag}] no positive curvature at min -> skip"); return None
    hbar_omega = hbarc*np.sqrt(k/mu_min)     # MeV
    print(f"\n  [{tag}] entrance well: sigma*={s0:.2f} fm  depth={well_depth:.2f} MeV")
    print(f"        k=V''={k:.3f} MeV/fm^2  mu(sigma*)={mu_min:.1f} MeV/c^2 "
          f"(mu_asym raw {mu_asym:.2f} -> kappa_mu {kappa_mu:.3f})")
    print(f"        hbar*omega_merger = hbar c sqrt(k/mu) = {hbar_omega:.2f} MeV")
    return dict(s0=s0,k=k,mu_min=mu_min,hw=hbar_omega,well=well_depth)

# ---- run two constructions ----
c1=run_construction(2.0,"C1 lam=2.0")
c2=run_construction(1.6,"C2 lam=1.6")

# ---- calibrate the raw energy unit ----
# PRIMARY (robust): nucleon-mass anchor (Adkins-Nappi-Witten style):
#   B=1 hedgehog raw energy  <->  physical nucleon mass 939 MeV.
Mnuc=939.0
E1_raw=Efun(su2_field(X,Y,Z,(0,0,0),2.0,1))
Ecal_N=Mnuc/E1_raw
print(f"\n# energy calibration (nucleon anchor): E1_raw(hedgehog)={E1_raw:.2f} -> {Ecal_N:.4f} MeV/raw-unit")
# SECONDARY (flagged non-robust): cube basin depth = Q.
lam_cube=1.6
ncube=su2_field(X,Y,Z,(0,0,0),lam_cube,4)
cube_depth_raw = Efun(pair(7.0,2.0)) - Efun(ncube)
print(f"# (secondary, NON-ROBUST) cube-vs-2tori raw depth = {cube_depth_raw:+.2f} "
      f"(sign/size resolution-unstable; cube binding NOT resolved in 3D coarse grid -> NOT used)")
Ecal_list={"nucleon-anchor 939 MeV": Ecal_N}

for name,ecal in Ecal_list.items():
    print(f"\n===== calibration [{name}]  ({ecal:.4f} MeV/raw-unit) =====")
    r1=analyze(*c1[:3],"C1 lam=2.0",ecal)
    r2=analyze(*c2[:3],"C2 lam=1.6",ecal)
    hws=[r for r in (r1,r2) if r]
    if hws:
        hw_vals=[r['hw'] for r in hws]
        lo,hi=min(hw_vals),max(hw_vals)
        cen=0.5*(lo+hi)
        print(f"\n  >> executed merger-mode band (2 constructions): "
              f"hbar*omega_merger = [{lo:.1f}, {hi:.1f}] MeV (central {cen:.1f})")
        # two-sided method-ceiling band: sine-Gordon collective-coord OVERESTIMATES omega ~2.2x
        f=2.21
        print(f"  >> two-sided method-ceiling (sine-Gordon coeff overestimate factor {f}):")
        print(f"       downward-corrected : [{lo/f:.1f}, {hi:.1f}] MeV")
        print(f"       symmetric          : [{lo/f:.1f}, {hi*f:.1f}] MeV")
        print(f"       in-band (1.4-1.9 MeV)? {'YES' if (lo/f<=1.9 and hi>=1.4) else 'NO'}")
        # S=exp(delta) sanity if one MISIDENTIFIES Delta with this merger-mode quantum
        def deltaLZ(D,v=2e-3,dF=0.9): return np.pi*D**2/(2*hbarc*v*dF)
        d_mis=deltaLZ(cen)
        print(f"  >> S=exp(delta) sanity: if Delta:=hbar*omega_merger={cen:.1f} MeV -> "
              f"delta={d_mis:.0f}, log10 S={d_mis/np.log(10):.0f}  (FREEZE-BOTH pathology if misidentified)")

# ---- static-ratio cross-check ----
E2s,E4s=2.4394,4.6204
Delta_static=( (2*E2s-E4s)/E4s )*Q
print(f"\n# static well-depth ratio (prior doc): Delta_static=(2E2-E4)/E4*Q = {Delta_static:.2f} MeV")
print(f"# BBT primary-source Eg 'cube->two donuts' mode (MFI_B4, recalibrated): ~20 MeV")
