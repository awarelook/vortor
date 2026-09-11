# Does R2 close to [V] via the RIGOROUS small-Grashof global-regularity route?
# Rigorous fact (Foias-Manley-Rosa-Temam; Constantin-Foias): 3D Navier-Stokes/Hall-MHD has
# GLOBAL regularity + a bounded-enstrophy attractor when the Grashof number G (equiv. Reynolds
# Re) is below an O(1) threshold; ABOVE it, global regularity is the OPEN (Millennium-class)
# problem. So R2's easy route works ONLY if the FTGB heartbeat is LOW-Reynolds.
import math
mu0=4e-7*math.pi
# order-of-magnitude FTGB plasmoid anchors (locked-KB / arc-seed)
B=200.0            # T
n=1e28             # /m^3
R=1e-6             # m (micron plasmoid)
mi=3.34e-27        # kg (deuteron)
vA=B/math.sqrt(mu0*n*mi)
# effective transport: Spitzer-like resistivity eta and kinematic viscosity nu at a plasma T
def report(Te_eV):
    Te=Te_eV*11604.0
    # Spitzer resistivity eta ~ 5.2e-5 * Z lnLambda / Te^1.5  (Ohm m), lnLambda~10
    eta=5.2e-5*10.0/max(Te,1.0)**1.5
    # magnetic diffusivity etam = eta/mu0 (m^2/s); Lundquist S = R vA / etam
    etam=eta/mu0
    S=R*vA/etam
    # hydrodynamic: Braginskii ion viscosity is huge B-perp-suppressed; use kinematic nu ~ vth*mfp
    # crude: Re_mag = S is the governing large number for MHD enstrophy cascade
    return eta,etam,S
print("R2 rigorous-route check: is the FTGB heartbeat LOW-Grashof (easy [V]) or HIGH (hard/open)?")
print("="*74)
print(f"v_A = {vA:.3e} m/s   (B={B} T, n={n:.0e}, R={R:.0e} m)")
print(f"{'T_e (eV)':>9} {'eta (Ohm m)':>13} {'eta_m (m^2/s)':>14} {'Lundquist S':>13}  regime")
for Te in [1.0,10.0,100.0,1000.0]:
    eta,etam,S=report(Te)
    regime="HIGH-Re (super-critical: 3D regularity OPEN)" if S>10 else "low-Re (small-Grashof [V] applies)"
    print(f"{Te:9.0f} {eta:13.3e} {etam:14.3e} {S:13.3e}  {regime}")
print("="*74)
print("VERDICT (honest, corrects my earlier optimism):")
print(" - A coherent, long-lived plasmoid is HIGH-Lundquist/Reynolds by its very nature")
print("   (S >> 1 at every plasma temperature above ~1 eV) -- low dissipation is WHY it persists.")
print(" - High-Re => SUPER-critical => the rigorous small-Grashof global-regularity theorem does")
print("   NOT apply. The 'easy' route to upgrade R2 to [V] FAILS for this object.")
print(" - Worse, the CURRENTLEG_R2 'T=6000 stable' evidence is a LOW-MODE reduced ODE, which")
print("   CANNOT exhibit enstrophy blow-up (a small-scale/high-mode phenomenon) by construction")
print("   => it is weak evidence about the true PDE enstrophy, not a sub-criticality proof.")
print(" - So R2 does NOT resolve without either (a) a genuinely NEW a-priori bound that exploits")
print("   the Beltrami + Stuart-Landau limit-cycle structure (large-scale coherent forcing on a")
print("   stable periodic attractor -- a real but hard estimate), or (b) the general 3D result.")
print("HONEST TIER: R2 stays [S] conditional / hard-open. My earlier 'plausibly resolvable")
print("without the Millennium problem' was TOO OPTIMISTIC: the object is high-Re, the easy")
print("rigorous route is inapplicable. The limit-cycle route is the one genuine remaining hope,")
print("unproven. This is a REAL open problem (kept), now correctly tiered.")
