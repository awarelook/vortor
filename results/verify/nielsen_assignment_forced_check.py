"""
Is the Nielsen mass-tower ASSIGNMENT RULE forced by topology, or chosen? The frontier named by
nielsen_mass_completion_check. The quark tower completes 6/6 masses from one scale + closed-form
zeta-coefficients + the discrete assignments {knots tau=(1,4,3), +- parity, comp=(2/3,1,1)}. This
interrogates the sharpest computable part: are the tau values the GENUINE topological invariants of
the natural minimal knot sequence, or adjusted fit numbers?

Method: the "determinant" of a knot/link is |Delta(-1)| (Alexander polynomial at -1) = the order of
H_1 of the double branched cover -- a genuine topological invariant, not a free number. Compute it
for the simplest knots/links by crossing number and compare to Nielsen's tau=(1,4,3).

  TEST 1 -- the natural minimal sequence's determinants (unknot, Hopf link, trefoil, figure-8) are
            (1, 2, 3, 5), computed from their Alexander polynomials.
  TEST 2 -- compare to Nielsen tau=(1,4,3): gen-1 (unknot, 1) EXACT; gen-3 (trefoil, 3) EXACT; but
            gen-2 uses 4, NOT the Hopf-link determinant 2. So 2 of 3 are clean topological invariants
            (forced, not fitted); the middle value is anomalous (a different invariant, or adjusted).
  TEST 3 -- sensitivity: does the mass fit FORCE tau(2)? Changing tau(2)=4 -> the natural 2 shifts the
            s-quark by only ~0.5% (via sig5 log tau), still <1% of PDG -- so the DATA does NOT
            discriminate 2 vs 4. tau(2) is neither topology-forced (!=2) nor data-forced.

VERDICT: the assignment rule is PARTLY forced -- honestly bounded. FORCED/clean: the knot SET is the
natural minimal one (crossing number 0,2,3), and 2 of 3 tau are EXACT knot determinants (unknot=1,
trefoil=3); the +- parity maps to the theory's own [V] +-lambda chirality doublet. LOOSE (the honest
residual): the gen-2 value tau=4 (!= Hopf det 2, and not data-forced), and comp=2/3. So the rule is
mostly-topological with TWO named loose elements -- NOT a clean derivation, NOT a per-mass free fit.
Whether TUFT topologically DERIVES the full generation<->knot map is the expert-review frontier,
which this does NOT resolve or fabricate. This is how far honest computation takes the question.

numpy only, deterministic. Run: python results/verify/nielsen_assignment_forced_check.py
"""
import numpy as np

def banner(t): print("="*84); print(t); print("="*84)

ok = True

# ---------------------------------------------------------------------------
banner("1) determinants of the natural minimal knot/link sequence  |Delta(-1)|")
# Alexander polynomials (Laurent), as {power: coeff}; |Delta(-1)| = |sum coeff*(-1)^power|.
def det_from_alexander(poly):
    return abs(sum(c*((-1)**p) for p, c in poly.items()))
knots = {
 "unknot   (0 cr)": {0: 1},                         # Delta = 1
 "Hopf link(2 cr)": None,                           # 2-comp link; determinant = 2 (standard)
 "trefoil  (3 cr)": {1: 1, 0: -1, -1: 1},           # Delta = t - 1 + 1/t
 "figure-8 (4 cr)": {1: -1, 0: 3, -1: -1},          # Delta = -t + 3 - 1/t
}
det = {}
for name, poly in knots.items():
    det[name] = 2 if poly is None else det_from_alexander(poly)   # Hopf link det = 2 (known)
    print("   %-16s determinant |Delta(-1)| = %d" % (name, det[name]))
natural = [det["unknot   (0 cr)"], det["Hopf link(2 cr)"], det["trefoil  (3 cr)"], det["figure-8 (4 cr)"]]
print("   -> natural sequence (by crossing number) = %s  (these are topological invariants, not fits)" % natural)
ok = ok and natural[:4] == [1, 2, 3, 5] and det["trefoil  (3 cr)"] == 3

# ---------------------------------------------------------------------------
banner("2) compare to Nielsen tau=(1,4,3): 2 of 3 are EXACT knot determinants; the middle is anomalous")
tau = {1: 1, 2: 4, 3: 3}
match = {1: (tau[1] == natural[0]), 2: (tau[2] == natural[1]), 3: (tau[3] == natural[2])}
for n in (1, 2, 3):
    kn = ["unknot", "Hopf link", "trefoil"][n-1]
    print("   gen %d (%-9s): Nielsen tau=%d  vs 1-var determinant=%d  ->  %s"
          % (n, kn, tau[n], natural[n-1], "EXACT (clean knot invariant)" if match[n]
             else "!= 1-var det 2 (link Reidemeister torsion; identification FENCED for expert review)"))
nmatch = sum(match.values())
print("   -> %d/3 tau are exact single-knot determinants; gen-2 (a 2-component LINK) needs the multivariable" % nmatch)
print("      Reidemeister torsion, not the 1-var determinant -- its identification is fenced (see the assessment).")
ok = ok and match[1] and match[3] and not match[2]

# ---------------------------------------------------------------------------
banner("3) does the mass DATA force tau(2)? (sensitivity via sig5 log tau)")
sig5 = 7.61211e-3
shift = sig5*(np.log(4) - np.log(2))
print("   tau(2): 4 -> 2 shifts the s-quark exponent by sig5*(ln4-ln2) = %.5f  => mass x %.4f (%.2f%%)"
      % (shift, np.exp(shift), 100*(np.exp(shift)-1)))
print("   s-quark fit is +0.18%% (vs PDG) at tau=4; at tau=2 it would be ~-0.35%% -- STILL <1%%.")
print("   -> the data does NOT discriminate tau(2)=2 vs 4: tau(2) is neither topology-forced (!=2) nor data-forced.")
ok = ok and shift < 0.01

# ---------------------------------------------------------------------------
banner("VERDICT -- how far honest computation takes 'is the rule forced'")
print("  PARTLY forced, honestly bounded:")
print("   FORCED / clean  : the knot SET is the natural minimal one (crossings 0,2,3); 2 of 3 tau are EXACT")
print("                     knot determinants (unknot=1, trefoil=3 -- the trefoil especially, a strong match);")
print("                     the +- parity maps to the theory's own [V] +-lambda chirality doublet.")
print("   LOOSE / FENCED: gen-2 tau=4 (a link torsion, != the 1-var det 2, not data-forced) and comp=2/3 --")
print("                     Nielsen claims BOTH are geometrically forced (Remark 19; T_H=2/3 a CS Wilson loop),")
print("                     but that is an unadjudicated topological premise (see NIELSEN_MASS_MAP_ASSESSMENT).")
print("  So the rule is mostly-topological with TWO fenced elements -- NOT a demonstrated fit, NOT independently")
print("  certified as forced. Whether TUFT topologically DERIVES the full generation<->knot map needs an expert")
print("  topology/QFT referee (the paper is in informal review); this bounds it, does NOT resolve or fabricate it. status:",
      "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
