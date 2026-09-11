# F1 audit — re-derivation of the Nielsen QUARK mass ASSEMBLY (not just the coefficients).
# Closes the "full assembly is [cited], not re-derived" gap for the quark sector: plugs Nielsen's
# published coefficients (TUFT eq.96-103, p.57) + the topological torsions tau(K)=(1,4,3) + the SINGLE
# scale v into eq.96 and checks all 6 quark masses reproduce his Table (p.57) and PDG.
#   m_{n,+-} = Lam5 (n+1) exp[ (a5 +- lamT(n)) n + C5 n^2 + b5 n(n+1)/2 + sig5 log tau(Kn) ] * comp(n)
# This verifies the ARITHMETIC assembly (coefficients -> masses). It does NOT certify Nielsen's TOPOLOGY
# (whether a5, C5, tau, etc. are geometrically forced) — that needs expert review; see the audit doc.
import math, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# --- Nielsen coefficients, quoted verbatim from TUFT p.57 (eq.97-103) ---
Lam5 = 6.09144e-2        # MeV, eq.97 = 2pi/sqrt3 * v * kappa5^3
a5   = 3.564112          # eq.98
C5   = 0.100171          # eq.99 = zeta(3)/12
b5   = 1.33064e-3        # eq.100 = zeta(5)/8pi^4
sig5 = 7.61211e-3        # eq.101 = zeta(3)/16pi^2
def lamT(n):             # eq.102/103 (parity splitting)
    if n==1: return 2/(3*math.sqrt(3))                 # 0.384900
    return 2/math.pi + (1.2020569/(12*math.pi))*(2.5-n)  # zeta(3)=1.2020569
tau = {1:1, 2:4, 3:3}    # eq.94: unknot / Hopf-link / trefoil (Reidemeister = |Alexander(-1)|)
comp = {1:2/3, 2:1, 3:1} # eq.96 first-generation component factor

# Nielsen's own published quark table (p.57) and PDG
NIELSEN = {("u",1,"-"):2.160005, ("d",1,"+"):4.66418, ("s",2,"-"):93.5650,
           ("c",2,"+"):1272.714, ("b",3,"-"):4172.22, ("t",3,"+"):172864.95}
PDG = {"u":2.16,"d":4.67,"s":93.4,"c":1270,"b":4180,"t":172760}

def mass(n, sign):
    s = +1 if sign=="+" else -1
    expo = (a5 + s*lamT(n))*n + C5*n*n + b5*n*(n+1)/2 + sig5*math.log(tau[n])
    return Lam5*(n+1)*math.exp(expo)*comp[n]

print(f"{'quark':5s} {'n':>1s} {'sgn':>3s} {'re-derived':>12s} {'Nielsen tbl':>12s} {'PDG':>10s} {'vs Nielsen':>11s} {'vs PDG':>9s}")
okN=okP=0
for (q,n,sgn),mN in NIELSEN.items():
    m = mass(n,sgn); relN=(m-mN)/mN*100; relP=(m-PDG[q])/PDG[q]*100
    fN = "PASS" if abs(relN)<0.5 else "FAIL"; okN += fN=="PASS"
    fP = "ok" if abs(relP)<1.0 else "OFF"; okP += fP=="ok"
    print(f"{q:5s} {n:>1d} {sgn:>3s} {m:12.4f} {mN:12.4f} {PDG[q]:10.2f} {relN:+9.3f}% {fN} {relP:+7.3f}% {fP}")
print(f"\nQUARK ASSEMBLY: {okN}/6 reproduce Nielsen's table (<0.5%);  {okP}/6 within ~1% of PDG.")
print("Single scale: v = 246220 MeV (in Lam5); every other factor is a zeta-value or knot invariant.")
print("tau(K3)=3 = |Alexander_trefoil(-1)| = |t^2-t+1 at -1|; NOT fitted. See F1 audit for the topology caveat.")
