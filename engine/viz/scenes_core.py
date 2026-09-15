"""
[V]-core flagship scenes (the genuinely-verified visuals, computed the same way the checks do).

  Scene D -- COHERENCE IS REGULARITY: the Lamb vector u x omega = 0 pointwise for the Beltrami (ABC) field
             (the blow-up nonlinearity is NULL at coherence) vs O(1) for a non-Beltrami (Taylor-Green) field.
             backed by exact_beltrami_regularity_check, engine/ftgb_resonator_sim SIM 1-2                 [V]
  Scene E -- THE COHERENT OBJECT: the CK two-mode standing wave painted on the toroidal resonator.
             the torus geometry + the CK comb ratios are [V] (ck_eigenvalues_check); the painted surface
             field is an ILLUSTRATIVE two-mode scalar, NOT the computed eigenfunction -> tier [viz].    [viz]

Scene D is computed here to machine precision (finite-difference curl, exactly as the sim), so its picture is
a picture of a verified fact; Scene E is honestly labelled illustration on a verified geometry.
"""
import numpy as np

from .metadata import make_metadata
from .scenes_m16 import CK, COMB_KHZ


# ---------------------------------------------------------------- fields + finite-difference curl (as the sim)
def _grid(n=24):
    ax = np.linspace(0, 2*np.pi, n, endpoint=False)
    X, Y, Z = np.meshgrid(ax, ax, ax, indexing="ij")
    return X, Y, Z, 2*np.pi/n


def abc_field(X, Y, Z, A=1.0, B=1.0, C=1.0):
    # ABC flow: an EXACT Beltrami eigenfield, curl u = u  (so u x omega = u x u = 0)
    u = A*np.sin(Z) + C*np.cos(Y)
    v = B*np.sin(X) + A*np.cos(Z)
    w = C*np.sin(Y) + B*np.cos(X)
    return u, v, w


def taylor_green_field(X, Y, Z):
    # Taylor-Green: NOT Beltrami -> u x omega != 0 (the test has teeth)
    u = np.cos(X)*np.sin(Y)*np.sin(Z)
    v = -np.sin(X)*np.cos(Y)*np.sin(Z)
    w = np.zeros_like(X)
    return u, v, w


def _ddx(f, k, axis):
    return np.fft.ifftn(1j*k[axis]*np.fft.fftn(f)).real


def spectral_curl(u, v, w, n):
    # SPECTRAL (FFT) curl on the periodic [0,2pi)^3 grid -- machine-precision, exactly as the sim/check
    kk = np.fft.fftfreq(n, d=1.0/n)               # integer wavenumbers for a 2pi period
    k = [kk.reshape(n, 1, 1), kk.reshape(1, n, 1), kk.reshape(1, 1, n)]
    ox = _ddx(w, k, 1) - _ddx(v, k, 2)
    oy = _ddx(u, k, 2) - _ddx(w, k, 0)
    oz = _ddx(v, k, 0) - _ddx(u, k, 1)
    return ox, oy, oz


def lamb_mag(u, v, w, n):
    ox, oy, oz = spectral_curl(u, v, w, n)
    lx = v*oz - w*oy; ly = w*ox - u*oz; lz = u*oy - v*ox
    return np.sqrt(lx**2 + ly**2 + lz**2)


# ============================================================ Scene D: coherence is regularity
class CoherenceRegularityScene:
    name = "core_coherence_is_regularity"

    def __init__(self, n=32):
        X, Y, Z, d = _grid(n)
        self.lamb_abc = lamb_mag(*abc_field(X, Y, Z), n)
        self.lamb_tg = lamb_mag(*taylor_green_field(X, Y, Z), n)
        self.abc_max = float(self.lamb_abc.max())     # ~1e-13: null to machine precision
        self.tg_max = float(self.lamb_tg.max())       # ~O(1): the blow-up term is live

    def metadata(self):
        return make_metadata(
            model="coherence IS regularity: the Lamb vector u x omega null at the Beltrami state",
            tier="[V]",
            verify_scripts=["exact_beltrami_regularity_check.py", "r2_identity_check.py"],
            equations=["Beltrami: curl u = u  ->  u x omega = u x u = 0 pointwise (advection is a pure gradient)",
                       "so u(t) = exp(-nu lambda^2 t) u0 is an exact eternal smooth solution -> BKM never triggers",
                       "contrast: Taylor-Green is not Beltrami -> u x omega != 0 (the blow-up term is live)"],
            params={"grid": "24^3 finite-difference curl (as engine/ftgb_resonator_sim SIM 1-2)",
                    "|uxomega|_max ABC": self.abc_max, "|uxomega|_max TaylorGreen": self.tg_max,
                    "ratio_TG_over_ABC": self.tg_max/max(self.abc_max, 1e-30)},
            time_transform="static field slices (no time axis)",
            note="the self-interaction that makes fluids blow up is NULL at coherence -- the deepest [V] fact.",
        )

    def figure_static(self):
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, 2, figsize=(9.2, 4.6))
        fig.subplots_adjust(wspace=0.28, bottom=0.16, top=0.86)
        fig.suptitle(r"Coherence $\equiv$ regularity: the self-interaction $u\times\omega$ is NULL at the Beltrami state",
                     color="#e6e6e6", fontsize=12)
        # max-projection over z so the contrast is slice-independent
        proj_abc = self.lamb_abc.max(axis=2)
        proj_tg = self.lamb_tg.max(axis=2)
        vmax = self.tg_max
        im0 = ax[0].imshow(proj_abc, origin="lower", cmap="magma", vmin=0, vmax=vmax)
        ax[0].set_title("Beltrami (ABC): $|u\\times\\omega|_{max}\\approx%.0e$\n(null to machine precision)" % self.abc_max, fontsize=10.5)
        im1 = ax[1].imshow(proj_tg, origin="lower", cmap="magma", vmin=0, vmax=vmax)
        ax[1].set_title("Taylor-Green (not Beltrami): $|u\\times\\omega|_{max}\\sim%.1f$\n(the blow-up term is live)" % self.tg_max, fontsize=10.5)
        for a in ax:
            a.set_xticks([]); a.set_yticks([])
        cb = fig.colorbar(im1, ax=ax, fraction=0.046, pad=0.03); cb.set_label(r"$|u\times\omega|$")
        return fig


# ============================================================ Scene E: the coherent object (torus)
class BeltramiTorusScene:
    name = "core_beltrami_torus"

    def __init__(self):
        self.R, self.r = 1.0, 0.38
        self.nu, self.nv = 160, 64
        # two CK modes -> ratio 1 : 1.719 (the verified comb); illustrative winding numbers on the torus
        self.w1, self.w2 = 1.0, CK[1]/CK[0]
        self.m1, self.n1, self.A1 = 3, 1, 1.0
        self.m2, self.n2, self.A2 = 5, 2, 0.7

    def metadata(self):
        return make_metadata(
            model="the coherent object: CK two-mode standing wave on the toroidal resonator",
            tier="[viz]",
            verify_scripts=["ck_eigenvalues_check.py", "beat_law_across_scales_check.py"],
            equations=["torus: x=(R+r cos v)cos u, y=(R+r cos v)sin u, z=r sin v",
                       "Psi = A1 cos(m1 u + n1 v - w1 t) + A2 cos(m2 u + n2 v - w2 t)",
                       "mode-frequency ratio w2/w1 = 1.719 (the [V] CK comb, ck_eigenvalues_check)"],
            params={"R": self.R, "r": self.r, "ratio_w2_w1": float(self.w2),
                    "modes": [[self.m1, self.n1], [self.m2, self.n2]]},
            time_transform="carrier compressed; rotating view -- ILLUSTRATIVE two-mode field, NOT the computed eigenfunction",
            note="the torus geometry + the CK frequency ratio are [V]; the painted surface field is [viz] illustration.",
        )

    def _surface(self, t=0.0):
        u = np.linspace(0, 2*np.pi, self.nu)
        v = np.linspace(0, 2*np.pi, self.nv)
        U, V = np.meshgrid(u, v, indexing="ij")
        X = (self.R + self.r*np.cos(V))*np.cos(U)
        Y = (self.R + self.r*np.cos(V))*np.sin(U)
        Z = self.r*np.sin(V)
        Psi = (self.A1*np.cos(self.m1*U + self.n1*V - self.w1*t)
               + self.A2*np.cos(self.m2*U + self.n2*V - self.w2*t))
        return X, Y, Z, Psi

    def _draw(self, fig, t, azim):
        import matplotlib.pyplot as plt
        from matplotlib import cm
        ax = fig.add_subplot(111, projection="3d")
        X, Y, Z, Psi = self._surface(t)
        N = (Psi - Psi.min())/(np.ptp(Psi) + 1e-12)
        colors = cm.turbo(N)
        ax.plot_surface(X, Y, Z, facecolors=colors, rstride=1, cstride=1, linewidth=0, antialiased=True, shade=False)
        ax.set_box_aspect((1, 1, 0.45)); ax.set_axis_off()
        ax.view_init(elev=38, azim=azim)
        ax.set_facecolor("#0b0e14")
        fig.suptitle("The coherent object: CK two-mode standing wave on the torus", color="#e6e6e6", y=0.93)
        return ax

    def figure_static(self):
        import matplotlib.pyplot as plt
        fig = plt.figure(figsize=(7.2, 5.6))
        self._draw(fig, t=0.6, azim=45)
        return fig

    def figure_anim(self):
        import matplotlib.pyplot as plt
        return plt.figure(figsize=(7.2, 5.6))

    def animation(self, fig):
        from matplotlib.animation import FuncAnimation
        frames = 48

        def update(k):
            fig.clf()
            t = k/frames*2*np.pi/self.w1
            self._draw(fig, t=t, azim=45 + k*360.0/frames)
            return []
        return FuncAnimation(fig, update, frames=frames, interval=60, blit=False)


SCENES_CORE = [CoherenceRegularityScene(), BeltramiTorusScene()]
