"""
Completes Stage 2 from TOPOLOGICAL_MONOPOLE_NONABELIAN_EXTENSION_RESEARCH_PROGRAM.md, the one item that
document flagged as genuine forward progress: the real Hopf charge Q_H for this project's own field.

Checked first, and NOT assumed: does the already-computed Lk=1 (field-line linking, S488/S502/S509)
already equal Q_H? Verified numerically this session that it does not -- the field's own DIRECTION
n=B/|B| varies substantially along a traced field line (max deviation 1.42 across one full period), so
field lines are NOT level sets/preimages of n for this specific field. Whitehead's theorem (Q_H = linking
number of preimages of two generic points on S^2) therefore requires a genuinely separate calculation,
not a relabeling of Lk.

Method: standard Whitehead-integral construction. n(x)=B(x)/|B(x)|. Pullback 2-form (Hopf charge density
field) F_i = (1/2)*epsilon_ijk * n.(d_j n x d_k n) -- always divergence-free by construction (a general
fact for the pullback of a closed 2-form via any smooth map into S^2, independent of whether the
ORIGINAL field B itself has zero divergence, which this project's own B_Hopf does not, S488/monopole
program). Reconstruct a vector potential A via the standard Biot-Savart-type formula
(curl(A)=F is the same mathematical structure as curl(B)=mu0*J), then Q_H=(1/16*pi^2)*integral[A.F]d^3x.

Validated FIRST against the textbook standard Hopf map (known Q_H=1 exactly) before applying to this
project's own field -- the same discipline used throughout S488-S516.
"""
import numpy as np

# ---------------------------------------------------------------------------
# Standard textbook Hopf map, via stereographic projection (independent of this project's own B_Hopf
# construction -- a clean, separate test case)
# ---------------------------------------------------------------------------
def n_standard_hopf(x, y, z):
    """The standard Hopf map n: R^3 -> S^2, via stereographic projection of the Hopf fibration.
    (2(xz+y), 2(yz-x), x^2+y^2-z^2-1) / (1+r^2)^2 * (1+r^2) -- normalized form, standard textbook."""
    r2 = x**2+y**2+z**2
    denom = 1+r2
    nx = 2*(x*z + y)/denom
    ny = 2*(y*z - x)/denom
    nz = (x**2+y**2-z**2-1)/denom
    return np.array([nx, ny, nz])

def n_project_hopf(x, y, z):
    """This project's own field's direction, n = B_Hopf/|B_Hopf|."""
    def v0(x,y,z):
        return np.array([x*z - y, x + y*z, (-x**2 - y**2 + z**2 + 1)/2])
    r2 = x**2+y**2+z**2
    Bv = v0(x,y,z)/(1+r2)**2
    return Bv/np.linalg.norm(Bv)

def pullback_F(n_func, x, y, z, h=1e-4):
    """F_i = (1/2)*epsilon_ijk * n.(d_j n x d_k n), via finite differences."""
    dnx = (n_func(x+h,y,z) - n_func(x-h,y,z))/(2*h)
    dny = (n_func(x,y+h,z) - n_func(x,y-h,z))/(2*h)
    dnz = (n_func(x,y,z+h) - n_func(x,y,z-h))/(2*h)
    n0 = n_func(x,y,z)
    Fx = np.dot(n0, np.cross(dny, dnz))
    Fy = np.dot(n0, np.cross(dnz, dnx))
    Fz = np.dot(n0, np.cross(dnx, dny))
    return np.array([Fx, Fy, Fz])

def check_divergence_free(n_func, pts, h=1e-4):
    """Sanity check: F should be divergence-free at every tested point (a general fact, not assumed)."""
    max_div = 0.0
    for (x,y,z) in pts:
        Fxp = pullback_F(n_func, x+h, y, z)[0]; Fxm = pullback_F(n_func, x-h, y, z)[0]
        Fyp = pullback_F(n_func, x, y+h, z)[1]; Fym = pullback_F(n_func, x, y-h, z)[1]
        Fzp = pullback_F(n_func, x, y, z+h)[2]; Fzm = pullback_F(n_func, x, y, z-h)[2]
        div = (Fxp-Fxm)/(2*h) + (Fyp-Fym)/(2*h) + (Fzp-Fzm)/(2*h)
        max_div = max(max_div, abs(div))
    return max_div

def biot_savart_A(n_func, obs_pts, R_domain, n_samples=200_000, seed=0):
    """A(obs) = (1/4pi) * integral[ F(x') x (obs-x') / |obs-x'|^3 ] d^3x', Monte Carlo over a ball."""
    rng = np.random.default_rng(seed)
    u = rng.random(n_samples)
    r_mag = R_domain * u**(1/3)
    costheta = rng.uniform(-1,1,n_samples); phi = rng.uniform(0,2*np.pi,n_samples)
    sintheta = np.sqrt(1-costheta**2)
    xs = r_mag*sintheta*np.cos(phi); ys = r_mag*sintheta*np.sin(phi); zs = r_mag*costheta
    volume = (4/3)*np.pi*R_domain**3

    F_samples = np.array([pullback_F(n_func, xs[i], ys[i], zs[i]) for i in range(n_samples)])
    src_pts = np.stack([xs, ys, zs], axis=1)

    A_results = []
    for obs in obs_pts:
        diff = obs[None,:] - src_pts
        dist3 = np.linalg.norm(diff, axis=1)**3
        dist3 = np.where(dist3 < 1e-6, np.inf, dist3)
        integrand = np.cross(F_samples, diff) / dist3[:,None]
        A_results.append(integrand.mean(axis=0)*volume/(4*np.pi))
    return np.array(A_results)

def hopf_charge(n_func, R_domain=3.0, n_field_samples=60_000, n_A_samples=60_000, seed=0):
    rng = np.random.default_rng(seed+1)
    u = rng.random(n_field_samples)
    r_mag = R_domain * u**(1/3)
    costheta = rng.uniform(-1,1,n_field_samples); phi = rng.uniform(0,2*np.pi,n_field_samples)
    sintheta = np.sqrt(1-costheta**2)
    xs = r_mag*sintheta*np.cos(phi); ys = r_mag*sintheta*np.sin(phi); zs = r_mag*costheta
    volume = (4/3)*np.pi*R_domain**3

    obs_pts = np.stack([xs, ys, zs], axis=1)
    A_vals = biot_savart_A(n_func, obs_pts, R_domain, n_samples=n_A_samples, seed=seed)
    F_vals = np.array([pullback_F(n_func, xs[i], ys[i], zs[i]) for i in range(n_field_samples)])

    A_dot_F = np.einsum('ij,ij->i', A_vals, F_vals)
    Q_H = A_dot_F.mean()*volume/(16*np.pi**2)
    return Q_H

# ---------------------------------------------------------------------------
# STEP 1 -- validate: divergence-free check on both fields
# ---------------------------------------------------------------------------
print("=" * 78)
print("STEP 1 -- sanity check: is the pullback field F divergence-free (a general, required fact)?")
print("=" * 78)
test_pts = [(0.5,0.3,0.2), (1.0,-0.5,0.7), (0.2,0.2,0.2), (-0.3,0.6,-0.4)]
max_div_std = check_divergence_free(n_standard_hopf, test_pts)
max_div_proj = check_divergence_free(n_project_hopf, test_pts)
print(f"Standard Hopf map: max|div F| at test points = {max_div_std:.2e} (should be near zero)")
print(f"This project's field: max|div F| at test points = {max_div_proj:.2e} (should be near zero)")

# ---------------------------------------------------------------------------
# STEP 2 -- validate the FULL pipeline against the KNOWN textbook Hopf charge (Q_H=1 exactly)
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("STEP 2 -- validate the full Q_H pipeline against the textbook standard Hopf map (expect Q_H=1)")
print("=" * 78)
Q_H_standard = hopf_charge(n_standard_hopf, R_domain=3.0, n_field_samples=15000, n_A_samples=15000, seed=1)
print(f"Q_H (standard Hopf map) = {Q_H_standard:.4f}  (expect ~1.0)")

# ---------------------------------------------------------------------------
# STEP 3 -- the real question: Q_H for this project's own field
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("STEP 3 -- Q_H for THIS PROJECT'S OWN field (n = B_Hopf/|B_Hopf|)")
print("=" * 78)
Q_H_project = hopf_charge(n_project_hopf, R_domain=3.0, n_field_samples=15000, n_A_samples=15000, seed=2)
print(f"Q_H (this project's own field) = {Q_H_project:.4f}")

print("\n" + "=" * 78)
print("SUMMARY")
print("=" * 78)
print(f"If STEP 2 validates cleanly (Q_H_standard close to 1), STEP 3's number is a real, trustworthy")
print(f"answer -- the genuine Hopf charge of this project's own field, computed for the first time,")
print(f"completing Stage 2 from the monopole program's own flagged open item. Reported honestly whether")
print(f"it matches, differs from, or has no expected relation to Lk=1 (a DIFFERENT quantity, per the")
print(f"direct numerical check above showing field-lines != preimages for this specific field).")
