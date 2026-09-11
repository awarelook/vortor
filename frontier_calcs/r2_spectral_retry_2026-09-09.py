import numpy as np
N=32; nu=0.008; dt=0.002; nsteps=6000
k1=np.fft.fftfreq(N,1.0/N).astype(np.float64)
KX,KY,KZ=np.meshgrid(k1,k1,k1,indexing='ij')
K2=KX*KX+KY*KY+KZ*KZ; K2i=1.0/np.where(K2==0,1.0,K2)
dealias=(np.abs(KX)<N/3)&(np.abs(KY)<N/3)&(np.abs(KZ)<N/3)
visc=np.exp(-nu*K2*dt)
def proj(a,b,c):
    d=(KX*a+KY*b+KZ*c)*K2i; return a-KX*d,b-KY*d,c-KZ*d
def curl(a,b,c): return (1j*(KY*c-KZ*b),1j*(KZ*a-KX*c),1j*(KX*b-KY*a))
def nonlin(ux,uy,uz):
    wx,wy,wz=curl(ux,uy,uz)
    ur=[np.fft.ifftn(x).real for x in (ux,uy,uz)]; wr=[np.fft.ifftn(x).real for x in (wx,wy,wz)]
    cx=ur[1]*wr[2]-ur[2]*wr[1]; cy=ur[2]*wr[0]-ur[0]*wr[2]; cz=ur[0]*wr[1]-ur[1]*wr[0]
    return proj(np.fft.fftn(cx)*dealias,np.fft.fftn(cy)*dealias,np.fft.fftn(cz)*dealias)
def helical_basis(kx,ky,kz):
    k=np.array([kx,ky,kz],float); kn=np.linalg.norm(k)
    z=np.array([0,0,1.0]); 
    if abs(np.dot(k/kn,z))>0.9: z=np.array([0,1.0,0])
    e1=np.cross(z,k); e1/=np.linalg.norm(e1); e2=np.cross(k/kn,e1)
    hp=(e1+1j*e2)/np.sqrt(2); return hp  # positive-helicity eigenvector
def make_force(sign):  # sign=+1 single-helicity (Beltrami); sign=0 balanced (+/-, ~zero net helicity)
    fx=np.zeros((N,N,N),complex);fy=fx.copy();fz=fx.copy()
    F=3.0
    for (kx,ky,kz) in [(1,0,0),(0,1,0),(0,0,1)]:
        hp=helical_basis(kx,ky,kz)
        i=(np.array([kx,ky,kz])%N)
        vp=F*hp
        if sign==1: v=vp                       # + helicity only -> Beltrami
        else:       v=F*np.real(hp)+0j         # equal +/- mix -> ~zero net helicity, same energy
        fx[i[0],i[1],i[2]]+=v[0];fy[i[0],i[1],i[2]]+=v[1];fz[i[0],i[1],i[2]]+=v[2]
        j=((-np.array([kx,ky,kz]))%N)
        fx[j[0],j[1],j[2]]+=np.conj(v[0]);fy[j[0],j[1],j[2]]+=np.conj(v[1]);fz[j[0],j[1],j[2]]+=np.conj(v[2])
    return proj(fx,fy,fz)
def run(sign):
    rng=np.random.default_rng(3)
    ux=(rng.standard_normal((N,N,N))+1j*rng.standard_normal((N,N,N)))*0.02*dealias
    uy=ux.copy()*0.5; uz=ux.copy()*0.3; ux,uy,uz=proj(ux,uy,uz)
    fx,fy,fz=make_force(sign); Zs=[]
    Emax=0;Zmax=0;Hrel=0
    for s in range(nsteps):
        Nx,Ny,Nz=nonlin(ux,uy,uz)
        ux=visc*(ux+dt*(Nx+fx));uy=visc*(uy+dt*(Ny+fy));uz=visc*(uz+dt*(Nz+fz))
        if not np.isfinite(np.abs(ux).sum()): return None
        if s%200==0 and s>nsteps//3:
            E=0.5*np.sum(np.abs(ux)**2+np.abs(uy)**2+np.abs(uz)**2).real/N**3
            Z=0.5*np.sum(K2*(np.abs(ux)**2+np.abs(uy)**2+np.abs(uz)**2)).real/N**3
            wx,wy,wz=curl(ux,uy,uz); H=np.sum((ux.conj()*wx+uy.conj()*wy+uz.conj()*wz)).real/N**3
            Zs.append(Z); Emax=max(Emax,E);Zmax=max(Zmax,Z); Hrel=H/(2*E+1e-12)
    Zs=np.array(Zs)
    return dict(Emax=Emax,Zmean=Zs.mean(),Zmax=Zmax,Zstd=Zs.std(),Hrel=Hrel)
print("RETRY: sustained moderate-Re 3D spectral, single-helicity(Beltrami) vs balanced(non-helical)")
print(f"N={N} nu={nu} dt={dt} steps={nsteps}  (steady-state window = last 2/3)")
print("="*74)
for sign,tag in [(1,"Beltrami (single-helicity)"),(0,"non-helical (balanced)")]:
    r=run(sign)
    if r is None: print(f"{tag:28}: BLEW UP"); continue
    print(f"{tag:28}: <Z>={r['Zmean']:.3f}  Zmax={r['Zmax']:.3f}  Zstd={r['Zstd']:.3f}  E~{r['Emax']:.3f}  H_rel={r['Hrel']:+.3f}")
print("="*74)
print("Valid ONLY if H_rel clearly differs between the two (Beltrami ~ high |H_rel|, non-helical ~0).")
print("If so: lower/flatter <Z>,Zmax for Beltrami = 3D evidence for stretching-suppression (moderate Re).")
print("If H_rel does NOT differ, or Z ~ identical, the test is INCONCLUSIVE -- report as such, no spin.")
