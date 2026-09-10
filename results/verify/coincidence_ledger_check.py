"""
COINCIDENCE LEDGER -- compute every numerical coincidence / flag in the corpus and LOG the outcome.

Standard-science practice (per project directive): do NOT hand-wave "numerology." COMPUTE each
coincidence, record its value / target / deviation, run a genericity check where a hit is claimed, and
LOG a verdict tier. Coincidences are kept as CLUES, not promoted. This makes the check reproducible and
the record permanent (results/COINCIDENCE_LEDGER.md presents the same log in prose).

Verdict tiers used here:
  DERIVED        -- follows from a closed form / theorem (not a coincidence).
  RESTATEMENT    -- exact, but both sides carry the same constants (no new content).
  GENERIC        -- the near-miss is comparable to hits on control targets (fails a genericity gate).
  BACK-FIT       -- the "match" needs a factor solved FROM the answer.
  CIRCULAR       -- the inputs are themselves defined through the target.
  DEAD           -- the proposed factor does not even produce the claimed correction.
  COINCIDENCE    -- close, no mechanism, no derivation (logged as a clue, [flag]).
Run: python results/verify/coincidence_ledger_check.py
"""
import numpy as np

hbar=1.054571817e-34; c=299792458.0; e=1.602176634e-19; eps0=8.8541878128e-12
m_e=9.1093837015e-31; m_p=1.67262192369e-27; h=2*np.pi*hbar
alpha=e*e/(4*np.pi*eps0*h/(2*np.pi)*c)  # = e^2/(4 pi eps0 hbar c)
alpha=e*e/(4*np.pi*eps0*hbar*c)
inv_a=1/alpha
mpme=m_p/m_e
phi=(1+np.sqrt(5))/2
j01=2.4048255577
Z0=np.sqrt(4e-7*np.pi/eps0); RK=h/(e*e)

rows=[]
def log(name, value, target, verdict, note):
    dev = abs(value-target)/abs(target)*100 if target else float('nan')
    rows.append((name, value, target, dev, verdict, note))

# --- alpha (1/alpha = 137.036) coincidences ---
log("alpha = Z0/(2 R_K)", Z0/(2*RK), alpha, "RESTATEMENT", "exact to ~1e-6; both sides carry e,mu0,c,h")
log("1/(20 phi^4) vs 1/alpha", 20*phi**4, inv_a, "COINCIDENCE", "0.034%; '20'=C(6,3) hand-chosen, no QED running [flag]")
log("140.2*e^(-2/3) vs 1/alpha", 140.2*np.exp(-2/3), inv_a, "DEAD", "gives 72, not 137; e^(-2/3) factor is dead [excised]")
log("winding iota vs 1/alpha", 1.08, inv_a, "GENERIC", "object winding-to-spin ~1 (Hopf ring=Q_H), not 137")
log("c_CK(eps->0)=1/(2 j01)", 1/(2*j01), 0.20792, "DERIVED", "closed form, first zero of J0; not a coincidence")

# --- proton/electron mass ratio (1836.153) coincidences ---
log("6 pi^5 vs m_p/m_e", 6*np.pi**5, mpme, "COINCIDENCE", "0.0019%! famous (Lenz 1951); NO mechanism [flag]")
log("phi^16 vs m_p/m_e", phi**16, mpme, "GENERIC", "20% off; no clean phi^n")
log("137^2 vs m_p/m_e", inv_a**2, mpme, "GENERIC", "off by ~10x; no 137^n")

# --- EGM alpha/radii/H0 (computed forward in egm_alpha_radii_H0_principle_calc.py) ---
lam_CP=hbar/(m_p*c); lam_Ce=hbar/(m_e*c)
log("EGM r_pi=(3/4)lamCP^2/lamCe", 0.75*lam_CP**2/lam_Ce, 0.8409e-15, "BACK-FIT", "forward off ~1e4; n_Omega~25 solved from r_p")
log("EGM H0 = sqrt(GM/R^3)/H0", 1/np.sqrt(2), 1.0, "CIRCULAR", "M,R defined via H0 -> ratio=1/sqrt2 identically")
log("EGM 2:1 harmonic w(e)/w(p)", 2.0, 2.0, "RESTATEMENT", "omega_Omega(e)=omega_CP^2/omega_Ce=2 w(p) by definition")

# --- resolved / genuine (logged for completeness) ---
log("pi^2/3 (TUFT C5/omega3)", np.pi**2/3, 3.2899, "DERIVED", "RESOLVED: category error; omega3=zeta'(-2) genuine")

print("="*94)
print("COINCIDENCE LEDGER -- computed, logged (clues kept, nothing promoted)")
print("="*94)
print("  %-34s %14s %14s %8s  %-11s" % ("coincidence","value","target","dev%","verdict"))
print("  "+"-"*90)
for name,val,tgt,dev,verd,note in rows:
    print("  %-34s %14.6g %14.6g %7.3f%%  %-11s" % (name,val,tgt,dev,verd))
    print("        -> %s" % note)

# --- genericity gate: is a hit on 137.036 special or generic? (compare to control targets) ---
print("\n  GENERICITY GATE (hits on 137.036 vs control targets from the object's own constants):")
consts=[phi, j01, np.pi, 4.493409, np.e]  # phi, j01, pi, lambda1 R, e
def count_hits(target, tol=0.005):
    n=0
    for a in range(-3,4):
        for b in range(-3,4):
            for k in (0.5,1,2,3,4,5,6,20):
                v=k*phi**a*np.pi**b
                if v>0 and abs(v-target)/target<tol: n+=1
    return n
for tgt in [137.036, 123.4, 150.7, 111.1, 160.0]:
    tag="  <- 137 (the claim)" if abs(tgt-137.036)<1 else "  (control)"
    print("     hits within 0.5%% of %8.3f : %3d%s" % (tgt, count_hits(tgt), tag))
print("  -> if 137's hit-count is COMPARABLE to the controls, the near-miss is GENERIC (not special).")

print("\n  READING: every coincidence is COMPUTED and LOGGED here as a clue (check-record-learn). None is")
print("  promoted: alpha=Z0/2R_K is a restatement; 1/(20phi^4) and 6 pi^5 are close-but-mechanism-free")
print("  coincidences [flag]; e^(-2/3) is dead; EGM radii/H0 are back-fit/circular; the winding is generic;")
print("  c_CK and pi^2/3 are genuinely DERIVED (not coincidences). Keeping the log is the science.")
print("done.")
raise SystemExit(0)
