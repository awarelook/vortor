"""
Real two-electron ring Madelung reduction.

Question being tested: DERIVATION_NOTE_1D_MADELUNG_RING.md's single-particle Madelung-ring
ansatz needed a phenomenological nonlinear self-interaction term (g*rho) with no first-principles
justification (FRONTIER_RESEARCH.md 8a/8b, sec 6.95/6.131) to generate a scalar beat channel.
That model also never included real fermion statistics or real electron-electron Coulomb repulsion
at all. This script asks: does a genuine, exact TWO-ELECTRON ring problem (real Coulomb repulsion,
real fermion antisymmetry, no phenomenological g) supply real physics the single-particle model
was missing, and if so, at what real energy/frequency scale, and how does that scale with ring
radius R across this project's own real six-level cascade (r_L = R*/4^L)?

Step 1 (symbolic, sympy): verify the COM/relative decoupling for two identical particles on a
homogeneous ring is exact (no approximation), and derive the real reduced mass.
Step 2 (analytic): fermion antisymmetry -> the relative-coordinate wavefunction must be ODD under
theta_- -> -theta_-, forcing real Dirichlet nodes at theta_-=0 (electron coincidence, the real
"Fermi hole") AND at theta_-=pi (a second node forced by periodicity + oddness together).
Step 3 (numerical, finite difference): solve the real relative-coordinate eigenvalue problem on
(0, pi) with Dirichlet BCs, real Coulomb repulsion V(theta)=k e^2/(2R sin(theta/2)), at each of
the six real cascade radii r_L = R*/4^L (R*=10nm), and report real eigenvalues, the fundamental
splitting, and how that splitting scales from level to level.
"""
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import sympy as sy

print("="*78)
print("STEP 1 -- symbolic verification of COM/relative decoupling (sympy)")
print("="*78)

theta1, theta2, thetap, thetam, m, R, hbar = sy.symbols(
    'theta1 theta2 theta_+ theta_- m R hbar', positive=True, real=True)

# theta_+ = (theta1+theta2)/2 , theta_- = theta1-theta2
thetap_expr = (theta1 + theta2) / 2
thetam_expr = theta1 - theta2

# Solve theta1, theta2 in terms of theta_+, theta_-
sol = sy.solve([sy.Eq(thetap, thetap_expr), sy.Eq(thetam, thetam_expr)], [theta1, theta2])
th1_of = sol[theta1]
th2_of = sol[theta2]
print(f"theta1(theta+,theta-) = {th1_of}")
print(f"theta2(theta+,theta-) = {th2_of}")

f = sy.Function('f')(theta1, theta2)
# chain rule: d/dtheta1 = dthetap/dtheta1 * d/dthetap + dthetam/dtheta1 * d/dthetam
dthetap_d1 = sy.diff(thetap_expr, theta1)
dthetam_d1 = sy.diff(thetam_expr, theta1)
dthetap_d2 = sy.diff(thetap_expr, theta2)
dthetam_d2 = sy.diff(thetam_expr, theta2)
print(f"d(theta+)/d(theta1)={dthetap_d1}, d(theta-)/d(theta1)={dthetam_d1}")
print(f"d(theta+)/d(theta2)={dthetap_d2}, d(theta-)/d(theta2)={dthetam_d2}")

# second derivative operator coefficients: d^2/dtheta1^2 + d^2/dtheta2^2
# = (dthetap_d1 d/dthetap + dthetam_d1 d/dthetam)^2 + (dthetap_d2 d/dthetap + dthetam_d2 d/dthetam)^2
# since dthetap_dX, dthetam_dX are constants (linear coordinate change), cross terms just add
a1, b1 = dthetap_d1, dthetam_d1
a2, b2 = dthetap_d2, dthetam_d2
coeff_p2 = a1**2 + a2**2          # coefficient of d^2/dtheta+^2
coeff_m2 = b1**2 + b2**2          # coefficient of d^2/dtheta-^2
coeff_cross = 2*(a1*b1 + a2*b2)   # coefficient of d^2/dtheta+ dtheta-
print(f"\nLaplacian in new coords: {coeff_p2}*d2/dtheta+^2 + {coeff_m2}*d2/dtheta-^2 + {coeff_cross}*d2/(dtheta+ dtheta-)")
print("(cross term vanishing confirms EXACT decoupling, no approximation)")

M_COM = sy.symbols('M_COM', positive=True)
mu = sy.symbols('mu', positive=True)
# kinetic operator: -hbar^2/(2 m R^2) * (coeff_p2 d2/dtheta+^2 + coeff_m2 d2/dtheta-^2)
# want this = -hbar^2/(2 M_COM R^2) d2/dtheta+^2 - hbar^2/(2 mu R^2) d2/dtheta-^2
M_COM_val = sy.simplify(m / coeff_p2)
mu_val = sy.simplify(m / coeff_m2)
print(f"\nEffective COM mass M_COM = m/{coeff_p2} = {M_COM_val}  (expect 2m, total mass)")
print(f"Effective reduced mass mu = m/{coeff_m2} = {mu_val}  (expect m/2, standard equal-mass reduced mass)")

print("\n" + "="*78)
print("STEP 2 -- fermion antisymmetry -> Fermi-hole boundary condition")
print("="*78)
print("Exchange theta1<->theta2  =>  theta_+ -> theta_+ , theta_- -> -theta_-")
print("Real fermion requirement: Psi(theta2,theta1,t) = -Psi(theta1,theta2,t)")
print("For a decoupled product Psi = Phi(theta_+,t) * phi(theta_-,t):")
print("   Phi(theta_+) phi(-theta_-) = - Phi(theta_+) phi(theta_-)  for all theta_+")
print("   => phi(-theta_-) = -phi(theta_-)   (phi must be an ODD function of theta_-)")
print("Since theta_- also has period 2*pi (both original angles are 2pi-periodic):")
print("   oddness + periodicity together force phi(0)=0  AND  phi(pi)=0")
print("   (electron coincidence node forced twice over: Pauli AND the real 1/sin(theta/2)")
print("    Coulomb repulsion both independently push the wavefunction to zero there --")
print("    a real, mutually-consistent physical picture, not an arbitrary imposed BC.)")

print("\n" + "="*78)
print("STEP 3 -- real numerical eigenvalue solve, relative coordinate, six cascade radii")
print("="*78)

# real physical constants (SI)
hbar_v = 1.054571817e-34   # J.s
me_v   = 9.1093837015e-31  # kg
e_v    = 1.602176634e-19   # C
eps0_v = 8.8541878128e-12  # F/m
eV     = e_v                # J per eV

ke2 = e_v**2 / (4*np.pi*eps0_v)   # k*e^2, SI (J.m)
mu_v = me_v/2                      # real reduced mass, confirmed symbolically above

a_eff = hbar_v**2/(mu_v*ke2)       # real relative-motion "Bohr radius" analogue
print(f"k e^2            = {ke2:.6e} J.m  (= {ke2/eV*1e9:.4f} eV.nm)")
print(f"reduced mass mu  = {mu_v:.6e} kg  (m_e/2)")
print(f"a_eff = hbar^2/(mu k e^2) = {a_eff*1e12:.3f} pm  (twice the ordinary Bohr radius)")

Rstar = 10e-9  # 10 nm, this project's own established R* (SYNTHESIS_v1 Sec 1)
levels = list(range(6))
radii = [Rstar/4**L for L in levels]

# target cascade quanta this project's own Beat-Law ladder actually needs (SYNTHESIS_v1 Sec 2):
# omega_L = omega_0 * 4^L, omega_0 -> f_b=52.3THz -> hbar*omega_0 = 0.2163 eV; omega_5 = 221.2 eV
omega0_eV = 4.13567e-15 * 52.3e12   # h*f_b in eV (h in eV.s * Hz)
target_eV = [omega0_eV * 4**L for L in levels]

def solve_relative(R, N=4000):
    """Finite-difference solve of -hbar^2/(2 mu R^2) phi'' + V(theta) phi = eps phi
       on (0,pi), Dirichlet phi(0)=phi(pi)=0, V(theta)=k e^2/(2 R sin(theta/2))."""
    theta = np.linspace(0, np.pi, N+2)[1:-1]   # interior points only (Dirichlet at ends)
    dtheta = theta[1]-theta[0]
    V = ke2/(2*R*np.sin(theta/2))
    kin_coeff = hbar_v**2/(2*mu_v*R**2*dtheta**2)
    main = 2*kin_coeff + V
    off = -kin_coeff*np.ones(N-1)
    H = sp.diags([off, main, off], offsets=[-1,0,1], format='csc')
    # lowest few eigenvalues
    vals = spla.eigsh(H, k=6, which='SA', return_eigenvectors=False)
    return np.sort(vals)

print(f"\n{'L':>2} {'R (pm)':>10} {'R/a_eff':>9} {'eps1 (eV)':>12} {'eps2 (eV)':>12} "
      f"{'d_eps=e2-e1 (eV)':>17} {'target hbar*omega_L (eV)':>24}")
prev_deps = None
deps_list = []
for L, R in zip(levels, radii):
    vals = solve_relative(R)
    vals_eV = vals/eV
    deps = vals_eV[1]-vals_eV[0]
    deps_list.append(deps)
    ratio_str = ""
    if prev_deps is not None:
        ratio_str = f"  (ratio to prev level: {prev_deps/deps:.3f})"
    print(f"{L:>2} {R*1e12:>10.3f} {R/a_eff:>9.4f} {vals_eV[0]:>12.5e} {vals_eV[1]:>12.5e} "
          f"{deps:>17.5e} {target_eV[L]:>24.5e}{ratio_str}")
    prev_deps = deps

print("\nConsecutive-level scaling of the real, computed Delta-epsilon (need x4 per level to match cascade):")
for L in range(5):
    print(f"  L{L}->L{L+1}: computed ratio = {deps_list[L]/deps_list[L+1]:.4f}   (needed: 4.0000)")

print("\nHarmonic-well analytic check (valid only where R >> a_eff, i.e. small L):")
for L, R in zip(levels, radii):
    omega_osc = np.sqrt(ke2/(8*mu_v*R**3))
    print(f"  L{L}: hbar*omega_osc(harmonic estimate) = {hbar_v*omega_osc/eV:.5e} eV   "
          f"vs numeric d_eps = {deps_list[L]:.5e} eV")
