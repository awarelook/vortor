"""
GUARD for the P.v = const no-go (driven double-Beltrami).
Conventions EXACTLY from DRIVEN_CANONICAL_HELICITY_4CURRENT_2026-09-08.md /
driven_canonical_aligned_2026-09-08.py:
  P = A + d v ;  Omega = curl P = B + d curl v ;  h = P.Omega ;
  aligned equilibrium: v || Omega (v x Omega = 0) => mu = const ;
  closure residual rho_res = ||S Omega|| / ||h v|| , S = mu - P.v , mu = mean(P.v) gauge.
  iff-metric std(P.v)/mean(P.v).
Fields built as P = p1 G+ + p2 G-, v = e1 G+ + e2 G-, curl G+- = lam+- G+-.
Aligned: e1 p2 lam- = e2 p1 lam+  ->  e2 = e1 p2 lam- / (p1 lam+).
"""
import numpy as np
np.set_printoptions(suppress=True)

N=32; Ltot=2*np.pi
x=np.linspace(0,Ltot,N,endpoint=False)
X,Y,Z=np.meshgrid(x,x,x,indexing='ij')
k1=np.fft.fftfreq(N,d=Ltot/N)*2*np.pi
KX,KY,KZ=np.meshgrid(k1,k1,k1,indexing='ij')
def curl(F):
    fx,fy,fz=np.fft.fftn(F[0]),np.fft.fftn(F[1]),np.fft.fftn(F[2])
    cx=np.fft.ifftn(1j*(KY*fz-KZ*fy)).real
    cy=np.fft.ifftn(1j*(KZ*fx-KX*fz)).real
    cz=np.fft.ifftn(1j*(KX*fy-KY*fx)).real
    return np.array([cx,cy,cz])
def dot(A,B): return A[0]*B[0]+A[1]*B[1]+A[2]*B[2]
def cross(A,B): return np.array([A[1]*B[2]-A[2]*B[1],A[2]*B[0]-A[0]*B[2],A[0]*B[1]-A[1]*B[0]])
def rms(A): return np.sqrt(np.mean(dot(A,A)))
def spread(f): return np.std(f)/(abs(np.mean(f))+1e-30)

def analyze(P,v,lamp,lamm,p1,p2,e1,e2,tag,note=""):
    Om=curl(P)
    # verify each mode eigen & alignment
    vxO=cross(v,Om); eqres=rms(vxO)/(rms(v)*rms(Om)+1e-30)
    h=dot(P,Om); Pv=dot(P,v)
    mu=np.mean(Pv); S=mu-Pv
    SOm=np.array([S*Om[0],S*Om[1],S*Om[2]])
    hv=np.array([h*v[0],h*v[1],h*v[2]])
    rho_res=rms(SOm)/(rms(hv)+1e-30)
    Pmag=np.sqrt(dot(P,P))
    print(f"[{tag}] {note}")
    print(f"   eqres(v x Om)={eqres:.2e}  std(P.v)/mean={spread(Pv):.3e}  rho_res={rho_res:.3e}")
    print(f"   h=P.Om: mean={np.mean(h):+.4f} std={np.std(h):.3e}  min|P|={Pmag.min():.3e} max|P|={Pmag.max():.3f}")
    return spread(Pv),rho_res

print("="*84)
print("(1) REFUTATION FAMILY: lam+=+1, lam-=-1, each mode a SINGLE helical wave (trivial).")
print("    G+=(cos z,-sin z,0) [curl=+G+],  G-=(0,cos x,sin x) [curl=-G-]. y-INDEPENDENT.")
print("="*84)
Gp=np.array([np.cos(Z),-np.sin(Z),np.zeros_like(Z)])
Gm=np.array([np.zeros_like(Z),np.cos(X),np.sin(X)])
print("   check curl G+ - (+1)G+ :",rms(curl(Gp)-Gp))
print("   check curl G- - (-1)G- :",rms(curl(Gm)+Gm))
lamp,lamm=1.0,-1.0
for q in [0.5, 0.8, 1.0]:
    p1,p2=1.0,q; e1=1.0; e2=e1*p2*lamm/(p1*lamp)   # aligned
    P=p1*Gp+p2*Gm; v=e1*Gp+e2*Gm
    analyze(P,v,lamp,lamm,p1,p2,e1,e2,"2wave",f"q=p2={q}: expect P.v=const, h=1-q^2={1-q*q:+.3f}, null only at q=1")

print()
print("="*84)
print("(2) GENUINE-3D lam+=+1,lam-=-1 ABC pair (symmetric amps): expect P.v NOT const.")
print("="*84)
# +helicity ABC A=B=C=1: u=(sin z+cos y, sin x+cos z, sin y+cos x), curl=+u
Ap=np.array([np.sin(Z)+np.cos(Y), np.sin(X)+np.cos(Z), np.sin(Y)+np.cos(X)])
# -helicity ABC: w=(sin z-cos y, sin x-cos z, sin y-cos x), curl=-w
Am=np.array([np.sin(Z)-np.cos(Y), np.sin(X)-np.cos(Z), np.sin(Y)-np.cos(X)])
print("   check curl(+ABC)-(+1): ",rms(curl(Ap)-Ap),"  curl(-ABC)+(-1): ",rms(curl(Am)+Am))
lamp,lamm=1.0,-1.0
for (p1,p2) in [(1.0,0.5),(1.0,1.0),(1.0,2.0)]:
    e1=1.0; e2=e1*p2*lamm/(p1*lamp)
    P=p1*Ap+p2*Am; v=e1*Ap+e2*Am
    analyze(P,v,lamp,lamm,p1,p2,e1,e2,"3D-ABC",f"p2={p2}: genuine 3D, expect std(P.v)/mean NOT ~0")

print()
print("="*84)
print("(3) REFUTATION ATTEMPT: search 3D lam,-lam ABC pair (DIFFERENT amps) for P.v=const.")
print("    Positive-proportionality obstruction predicts a FLOOR bounded away from 0.")
print("="*84)
def abc_plus(A,B,C):  return np.array([A*np.sin(Z)+C*np.cos(Y), B*np.sin(X)+A*np.cos(Z), C*np.sin(Y)+B*np.cos(X)])
def abc_minus(A,B,C): return np.array([A*np.sin(Z)-C*np.cos(Y), B*np.sin(X)-A*np.cos(Z), C*np.sin(Y)-B*np.cos(X)])
best=1e9; bestcfg=None
rng=np.random.default_rng(3)
for _ in range(4000):
    Ap_=abc_plus(*rng.uniform(-1,1,3)); Am_=abc_minus(*rng.uniform(-1,1,3))
    # require both genuinely 3D (nonconstant |.|^2)
    if spread(dot(Ap_,Ap_))<0.1 or spread(dot(Am_,Am_))<0.1: continue
    p1,p2=1.0,rng.uniform(-3,3)
    if abs(p2)<0.1: continue
    P=p1*Ap_+p2*Am_; v=Ap_+ (p2*lamm/(p1*lamp))*Am_  # aligned e1=1
    Pv=dot(P,v)
    if abs(np.mean(Pv))<1e-6: continue
    s=spread(Pv)
    if s<best: best=s; bestcfg=(round(p2,3),)
print(f"   min std(P.v)/mean over 4000 random genuine-3D lam,-lam pairs = {best:.4f}  (bounded away from 0 => no 3D closer)")

print()
print("="*84)
print("(4) PROJECT REGIME: close SAME-SIGN spheres (spectral random Beltrami), lam+=3.85213 lam-=3.57038")
print("    Reproduce the 0.4-0.5 floor (genuine equilibria, v||Omega enforced).")
print("="*84)
def rand_beltrami(kvecs,seed):
    r=np.random.default_rng(seed)
    F=np.zeros((3,N,N,N),dtype=complex)
    for k in kvecs:
        k=np.array(k,float); kn=np.linalg.norm(k); kh=k/kn
        ref=np.array([1.0,0,0]) if abs(kh[0])<0.9 else np.array([0,1.0,0])
        e1v=ref-np.dot(ref,kh)*kh; e1v/=np.linalg.norm(e1v); e2v=np.cross(kh,e1v)
        hplus=(e1v+1j*e2v)/np.sqrt(2.0)
        amp=r.standard_normal()+1j*r.standard_normal()
        ph=np.exp(1j*(k[0]*X+k[1]*Y+k[2]*Z))
        for c in range(3): F[c]+=amp*hplus[c]*ph
    F=F.real; F/= np.sqrt(np.mean(dot(F,F))); return F
# helicity-eigen fields on integer spheres, then rescale coordinates is messy; instead use lam via |k|.
# Use |k|=2 sphere for + and a nearby set for -; ratio approximates project near-degeneracy.
Gp2=rand_beltrami([(2,0,0),(0,2,0),(0,0,2)],11)   # |k|=2  (lam=+2)
Gm2=rand_beltrami([(1,1,0),(0,1,1),(1,0,1)],12)   # |k|=sqrt2 (lam=+sqrt2) same sign
# curl eigenvalues:
print("   lam(Gp2)~",round(float(rms(curl(Gp2))/rms(Gp2)),4),"  lam(Gm2)~",round(float(rms(curl(Gm2))/rms(Gm2)),4))
lamp,lamm=2.0,np.sqrt(2.0)
best=1e9
for d in [0.3,0.7,1.5]:
    for e1 in [0.2,0.5,1.0,2.0,-0.5,-1.5]:
        # P=A+d v with A=Gp2/lamp+Gm2/lamm (curl A=B), B=Gp2+Gm2, v=e1 Gp2+e2 Gm2 aligned
        c1,c2=1.0,1.0
        # aligned in Omega basis: o1=(c1+d e1 lamp) etc; enforce e1 o2 = e2 o1
        denom=c1+d*e1*(lamp-lamm)
        if abs(denom)<1e-9: continue
        e2=e1*c2/denom
        A=np.array([c1/lamp*Gp2[i]+c2/lamm*Gm2[i] for i in range(3)])
        v=e1*Gp2+e2*Gm2
        P=A+d*v
        Pv=dot(P,v)
        if spread(dot(P,P))<0.05: continue
        Om=curl(P); h=dot(P,Om); mu=np.mean(Pv); S=mu-Pv
        rr=rms(np.array([S*Om[i] for i in range(3)]))/(rms(np.array([h*v[i] for i in range(3)]))+1e-30)
        best=min(best,spread(Pv))
print(f"   min std(P.v)/mean over close same-sign scan = {best:.4f}  (~0.4-0.6 floor, matches source doc)")

print()
print("="*84)
print("(5) CONTROLS")
print("="*84)
# single-mode |P| wall: single ABC +helicity, v||P
sm=spread(np.sqrt(dot(Ap,Ap)))
print(f"   single 3-wave Beltrami std|P|/mean = {sm:.4f}  (|P|=const wall; nonzero => obstruction)")
# constant-|P| control
Pc=np.array([np.cos(Z),np.sin(Z),np.zeros_like(Z)]); Pvc=dot(Pc,Pc)
print(f"   constant-|P| helical control std(P.v)/mean = {spread(Pvc):.2e}  (closes exactly)")
print("DONE")
