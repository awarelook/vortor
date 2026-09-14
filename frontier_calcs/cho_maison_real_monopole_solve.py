"""
Building the actual thing: numerically solve the REAL Cho-Maison electroweak monopole equations
(Cho & Maison 1997, Phys. Lett. B 391, 360), pure-monopole case (A=B=0), from scratch --
not testing whether this project's own field serves as a trial input (Stage 1/1b), but constructing
the genuine solution to the real Weinberg-Salam field equations on its own terms.

Dimensionless variable x = M_W r (M_W = g*rho0/2), following Cho-Maison's own convention.
Equations (their Eq. 5, A=B=0):
    f'' - f(f^2-1)/x^2 = (rho/rho0)^2 * f            [rescaled with g absorbed via x=M_W r]
    rho'' + (2/x)rho' - (1/2)(f^2/x^2)rho = (M_H/M_W)^2/2 * (rho^2-1) * rho    [rho in units of rho0]

Boundary conditions: f(0)=1, rho(0)=0, f(infinity)=0, rho(infinity)=1 (i.e. rho0 itself in these units).

This is a real two-point BVP on a semi-infinite domain, solved here by truncating to a large finite
x_max with the correct asymptotic conditions imposed there, using scipy's own BVP solver.
"""
import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

MH_over_MW = 1.0   # Cho-Maison's own illustrative choice (lambda/g^2 = 1/4)

def odes(x, y):
    f, fp, rho, rhop = y
    x_safe = np.where(x < 1e-6, 1e-6, x)
    fpp = f*(f**2-1)/x_safe**2 + rho**2*f
    rhopp = -(2/x_safe)*rhop + 0.5*(f**2/x_safe**2)*rho + (MH_over_MW**2/2)*(rho**2-1)*rho
    return np.vstack([fp, fpp, rhop, rhopp])

def bc(ya, yb):
    # at x=0: f=1, rho=0 ;  at x=x_max: f=0, rho=1
    return np.array([ya[0]-1, ya[2]-0, yb[0]-0, yb[2]-1])

x_max = 40.0
x_mesh = np.linspace(1e-3, x_max, 2000)

# initial guess: smooth interpolation between boundary values
f_guess = np.exp(-x_mesh/3)
rho_guess = 1 - np.exp(-x_mesh/3)
fp_guess = np.gradient(f_guess, x_mesh)
rhop_guess = np.gradient(rho_guess, x_mesh)
y_guess = np.vstack([f_guess, fp_guess, rho_guess, rhop_guess])

sol = solve_bvp(odes, bc, x_mesh, y_guess, max_nodes=200000, tol=1e-8, verbose=2)

print("\nSolve status:", sol.status, sol.message)
print("Success:", sol.success)

x_plot = np.linspace(0.001, x_max, 500)
y_plot = sol.sol(x_plot)
f_sol, rho_sol = y_plot[0], y_plot[2]

print("\nf(x) at selected x:")
for xv in [0, 0.5, 1, 2, 4, 8, 15, 25, 35]:
    idx = np.argmin(np.abs(x_plot - xv))
    print(f"  x={x_plot[idx]:6.2f}  f={f_sol[idx]: .6f}  rho={rho_sol[idx]: .6f}")

print(f"\nf(x_max={x_max}) = {f_sol[-1]:.6e}  (should be ~0)")
print(f"rho(x_max={x_max}) = {rho_sol[-1]:.6f}  (should be ~1)")
print(f"rho(0.001) = {rho_sol[0]:.6f}  (should be ~0)")

# core radius: where f drops to 1/e of its initial value
core_idx = np.argmin(np.abs(f_sol - f_sol[0]/np.e))
print(f"\nCore radius (f drops to 1/e): x_core = {x_plot[core_idx]:.3f}  (in units of 1/M_W)")

fig, ax = plt.subplots(figsize=(7,5))
ax.plot(x_plot, f_sol, label='f(x)  [SU(2) core profile]', color='#e0a93c', lw=2)
ax.plot(x_plot, rho_sol, label='rho(x)/rho0  [Higgs magnitude]', color='#8fb8e0', lw=2)
ax.set_xlabel('x = M_W r')
ax.set_ylabel('profile value')
ax.set_title('Real, numerically solved Cho-Maison electroweak monopole (A=B=0)')
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('../figures/greenyer/fig_cho_maison_real_monopole_solution.png', dpi=200)
print("\nSaved: figures/greenyer/fig_cho_maison_real_monopole_solution.png")
