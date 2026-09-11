# R2 attempt: does the NEAR-BELTRAMI + LIMIT-CYCLE structure give an a-priori enstrophy bound
# at HIGH Reynolds, where small-Grashof fails? Honest -- identify the handle, then test if it closes.
import math

print("R2 a-priori enstrophy: the near-Beltrami vortex-stretching-suppression route")
print("="*76)
print("STRUCTURAL FACT (exact, not fitted):")
print("  For a Beltrami velocity field curl v = lambda v, the vorticity omega = lambda v is")
print("  PARALLEL to v, so the Lamb vector v x omega = 0 and (v.grad)v = grad(|v|^2/2).")
print("  => The Euler nonlinearity is a PURE GRADIENT: ZERO vortex stretching, ZERO enstrophy")
print("     production. An exact Beltrami flow is enstrophy-safe (dissipation only).")
print("  This is the object-specific handle generic 3D turbulence LACKS. [textbook: Beltrami]")
print()
print("NEAR-BELTRAMI inequality (schematic, honest scaling):")
print("  Write v = v_B + delta*v' (delta = fractional deviation from Beltrami).")
print("  Enstrophy production P ~ |v x omega| ~ delta (vanishes at delta=0).")
print("  dZ/dt  <=  C*delta*Z^{3/2}  -  nu*k^2*Z   (production vs viscous dissipation)")
print("  Bounded when production loses to dissipation: delta  <  delta_c ~ nu*k^2 / (C*sqrt(Z)).")
print("  At high Reynolds nu ~ 1/S is SMALL, so the threshold delta_c is SMALL.")
print("="*76)

# object: deviation-from-Beltrami is drive-set. FTGB beat depth delta_Phi/Phi ~ 5% (locked-KB).
delta_obj = 0.05
C=1.0; k=1.0; Zscale=1.0
print(f"{'S (Lundquist)':>13} {'nu~1/S':>10} {'delta_c ~ nu k^2/(C sqrtZ)':>26} {'delta_obj':>10}  closes?")
for S in [93.0, 2949.0, 9.3e4, 2.95e6]:
    nu=1.0/S
    delta_c=nu*k*k/(C*math.sqrt(Zscale))
    closes = "YES (bounded)" if delta_obj < delta_c else "NO (production wins)"
    print(f"{S:13.3g} {nu:10.3g} {delta_c:26.3g} {delta_obj:10.3f}  {closes}")
print("="*76)
print("READING (honest):")
print(" - The near-Beltrami handle is REAL and is the RIGHT structural mechanism (it is why a")
print("   force-free plasmoid is laminar/coherent, not turbulent) -- categorically distinct from")
print("   the small-Grashof route that just failed.")
print(" - BUT at the object's HIGH Lundquist (S~1e2-1e6) the threshold delta_c ~ 1/S is TINY")
print("   (1e-2 down to 3e-7), while the drive-set deviation delta_obj ~ 5% is far larger.")
print("   => the NAIVE near-Beltrami a-priori bound does NOT close: leading-order production")
print("      from the ~5% deviation can exceed the weak high-Re dissipation.")
print(" - The LIMIT-CYCLE periodicity adds a second handle: on a periodic orbit the time-mean")
print("   of dZ/dt is 0, so <production>=<dissipation> AUTOMATICALLY *if a smooth orbit exists*.")
print("   That reduces R2 to: does the near-Beltrami periodic orbit maintain bounded gradients")
print("   over one period (no intra-period small-scale blow-up)? -- a bootstrap, not yet closed.")
print("="*76)
print("HONEST VERDICT:")
print(" R2 stays [S] HARD-OPEN, but the obstruction is now PRECISELY LOCATED and the problem is")
print(" genuinely EASIER than general 3D Navier-Stokes: two exact structural handles (Beltrami")
print(" stretching-suppression O(delta); limit-cycle mean-balance) reduce it to controlling the")
print(" INTRA-PERIOD GRADIENT GROWTH of a near-Beltrami periodic orbit. Neither handle alone")
print(" closes it at high Re + 5% deviation; a proof needs their COMBINATION (small-deviation")
print(" periodic-orbit gradient control) -- a real, well-posed, hard estimate. NOT proven; NOT")
print(" Navier-Stokes. This ADVANCES the characterization (names the exact remaining estimate),")
print(" it does NOT resolve R2. No number fabricated (delta_obj=5% = drive beat-depth; delta_c")
print(" scaling is the standard enstrophy inequality).")
