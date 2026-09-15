"""
First render scenes -- the M16 rhythm content, drawn from the SAME numbers the verify checks validate.

  Scene A -- two-mode beat + torque spectrum  (animated GIF; the headline artifact)
             backed by delta_detuning_beat_check, rhythm_parametric_resonance_check           [V]/[credited]
  Scene B -- Duffing backbone bending (the anharmonic leg the heartbeat omits)
             backed by duffing_backbone_check                                                  [V]/[credited]
  Scene C -- the CK inharmonic comb fingerprint 1:1.719:2.427 vs harmonic 1:2:3
             backed by ck_eigenvalues_check, beat_law_across_scales_check                      [V]

Every number here is a closed form a passing check independently confirms; the metadata sidecar names it.
"""
import numpy as np

from .metadata import make_metadata


# ---- shared: the CK carrier comb (roots of tan x = x), the verified fingerprint ----
def ck_roots(n=3):
    g = lambda z: np.sin(z) - z*np.cos(z)
    brackets = [(4.0, 5.0), (7.0, 8.0), (10.5, 11.5), (14.0, 14.2), (17.0, 17.3), (20.3, 20.5)][:n]
    out = []
    for a, b in brackets:
        lo, hi = a, b
        for _ in range(90):
            m = 0.5*(lo+hi)
            if g(lo)*g(m) <= 0:
                hi = m
            else:
                lo = m
        out.append(0.5*(lo+hi))
    return np.array(out)


V_A, R = 2.033e4, 0.12                       # canon anchors (SI calibration; absolute_magnitude_invariance_check)
CK = ck_roots(3)
COMB_KHZ = V_A*CK/(2*np.pi*R)/1e3             # {121, 208, 294} kHz


# ============================================================ Scene A: two-mode beat + torque spectrum
class BeatTorqueScene:
    name = "m16_beat_torque"

    def __init__(self):
        # a near-degenerate CK doublet -> a clean slow beat (M16 "near-equal beats + small detuning")
        self.f1, self.f2 = 121.2e3, 124.92e3         # Hz
        self.A1, self.A2, self.K = 1.0, 0.9, 1.0
        self.fb = abs(self.f2 - self.f1)             # beat (difference) line
        self.fS = self.f1 + self.f2                  # sum line
        self.Tbeat = 1.0/self.fb

    def metadata(self):
        return make_metadata(
            model="two-mode beat + quadratic torque mixing (M16)",
            tier="[V]",
            verify_scripts=["delta_detuning_beat_check.py", "rhythm_parametric_resonance_check.py"],
            equations=["q_i = A_i cos(2 pi f_i t)",
                       "sum = 2A cos(pi df t) cos(2 pi f_c t)  [envelope beats at f_b=|f2-f1|]",
                       "tau = K q1 q2 = (K A1 A2/2)[cos(2pi f_b t)+cos(2pi f_Sigma t)]"],
            params={"f1_Hz": self.f1, "f2_Hz": self.f2, "f_beat_Hz": self.fb, "f_sum_Hz": self.fS,
                    "A1": self.A1, "A2": self.A2, "K": self.K},
            time_transform=("carrier ~121-125 kHz REAL; one beat period (%.0f us) shown; "
                            "GIF playback time-compressed (a GIF second is not a physical second)" % (self.Tbeat*1e6)),
            note="the beat is a nonlinear/energy (torque) line at f_b, not a linear field line -- see rhythm TEST 1.",
        )

    def _series(self, n=4000):
        t = np.linspace(0, self.Tbeat, n)
        q1 = self.A1*np.cos(2*np.pi*self.f1*t)
        q2 = self.A2*np.cos(2*np.pi*self.f2*t)
        env = np.sqrt(self.A1**2 + self.A2**2 + 2*self.A1*self.A2*np.cos(2*np.pi*self.fb*t))
        tau = self.K*q1*q2
        return t, q1, q2, env, tau

    def figure_static(self):
        import matplotlib.pyplot as plt
        t, q1, q2, env, tau = self._series()
        fig, ax = plt.subplots(3, 1, figsize=(8.2, 7.4))
        fig.subplots_adjust(hspace=0.42, bottom=0.09, top=0.93)
        fig.suptitle("Two-mode beat  ->  torque spectrum at $f_b$ and $f_\\Sigma$", color="#e6e6e6")
        tu = t*1e6
        ax[0].plot(tu, q1+q2, color="#4dd6d6", lw=1.0, alpha=0.9, label="$q_1+q_2$")
        ax[0].plot(tu, env, color="#ffcf5a", lw=2.2, label="envelope")
        ax[0].plot(tu, -env, color="#ffcf5a", lw=2.2)
        ax[0].set_ylabel("amplitude"); ax[0].set_title("superposition + beat envelope (carrier real, %.1f kHz)" % (self.f1/1e3), fontsize=11)
        ax[0].legend(loc="upper right", fontsize=8, framealpha=0.2)
        ax[1].plot(tu, tau, color="#e879b9", lw=1.0)
        ax[1].set_ylabel(r"$\tau = K q_1 q_2$"); ax[1].set_xlabel(r"time [$\mu$s]"); ax[1].set_title("nonlinear torque", fontsize=11)
        # FFT of tau -> the two spectral lines
        n = 1 << 15
        tt = np.linspace(0, 8*self.Tbeat, n, endpoint=False)
        ta = self.K*(self.A1*np.cos(2*np.pi*self.f1*tt))*(self.A2*np.cos(2*np.pi*self.f2*tt))
        frq = np.fft.rfftfreq(n, d=(tt[1]-tt[0]))/1e3
        S = np.abs(np.fft.rfft(ta*np.hanning(n))); S /= S.max()
        ax[2].plot(frq, S, color="#7ee787", lw=1.4)
        ax[2].set_xlim(0, (self.fS/1e3)*1.1); ax[2].set_ylabel("|FFT $\\tau$|"); ax[2].set_xlabel("frequency [kHz]")
        ax[2].set_title("torque spectrum: difference line $f_b$=%.1f kHz and sum line $f_\\Sigma$=%.0f kHz" % (self.fb/1e3, self.fS/1e3), fontsize=10)
        for f, lab, c in [(self.fb/1e3, "$f_b$", "#4dd6d6"), (self.fS/1e3, "$f_\\Sigma$", "#ffcf5a")]:
            ax[2].axvline(f, color=c, ls="--", alpha=0.6)
        return fig

    def animation(self, fig):
        import matplotlib.pyplot as plt
        from matplotlib.animation import FuncAnimation
        fig.clf()
        ax = fig.add_subplot(111)
        fig.subplots_adjust(bottom=0.16, top=0.9)
        ax.set_title("Two-mode beat (carrier real; playback time-compressed)", color="#e6e6e6")
        win = self.Tbeat*0.25
        t = np.linspace(0, win, 1400)
        (l_sum,) = ax.plot([], [], color="#4dd6d6", lw=1.1, label="$q_1+q_2$")
        (l_env,) = ax.plot([], [], color="#ffcf5a", lw=2.4)
        (l_env2,) = ax.plot([], [], color="#ffcf5a", lw=2.4)
        ax.set_xlim(0, win*1e6); ax.set_ylim(-(self.A1+self.A2)*1.1, (self.A1+self.A2)*1.1)
        ax.set_xlabel(r"time [$\mu$s]"); ax.set_ylabel("amplitude"); ax.legend(loc="upper right", fontsize=8, framealpha=0.2)
        frames = 90

        def update(k):
            t0 = k/frames*(self.Tbeat - win)
            tt = t0 + t
            s = self.A1*np.cos(2*np.pi*self.f1*tt) + self.A2*np.cos(2*np.pi*self.f2*tt)
            env = np.sqrt(self.A1**2 + self.A2**2 + 2*self.A1*self.A2*np.cos(2*np.pi*self.fb*tt))
            l_sum.set_data(t*1e6, s); l_env.set_data(t*1e6, env); l_env2.set_data(t*1e6, -env)
            return l_sum, l_env, l_env2
        return FuncAnimation(fig, update, frames=frames, interval=40, blit=True)


# ============================================================ Scene B: Duffing backbone
class DuffingBackboneScene:
    name = "m16_duffing_backbone"

    def __init__(self):
        self.w0, self.beta = 1.0, 0.4
        # the in-repo measured peaks (duffing_backbone_check output): (F, Omega_peak, A_peak)
        self.peaks = [(0.05, 1.025, 0.482), (0.15, 1.150, 1.189), (0.30, 1.250, 1.564)]

    def metadata(self):
        return make_metadata(
            model="Duffing backbone bending (M16 anharmonic leg)",
            tier="[V]",
            verify_scripts=["duffing_backbone_check.py"],
            equations=["x'' + 2 gamma x' + w0^2 x + beta x^3 = F cos(Omega t)",
                       "backbone: Omega_peak(A) ~ w0 (1 + 3 beta A^2 / 8 w0^2)  [Landau-Lifshitz Mechanics sec.29]"],
            params={"w0": self.w0, "beta": self.beta, "measured_peaks_(F,Om,A)": self.peaks},
            time_transform="static parametric plot (no time axis) -- amplitude-response curves",
            note="the Stuart-Landau heartbeat has shear c=0, so it OMITS exactly this amplitude->frequency term.",
        )

    def figure_static(self):
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(8.0, 5.6))
        fig.subplots_adjust(bottom=0.16, top=0.9)
        fig.suptitle("Duffing backbone: the resonance peak climbs with drive amplitude", color="#e6e6e6")
        A = np.linspace(0, 1.8, 300)
        Om_bb = self.w0*(1 + 3*self.beta*A**2/(8*self.w0**2))     # credited backbone curve
        ax.plot(Om_bb, A, color="#ffcf5a", lw=2.4, label=r"backbone $\Omega_{peak}(A)=\omega_0(1+\frac{3\beta A^2}{8\omega_0^2})$")
        cols = ["#4dd6d6", "#e879b9", "#7ee787"]
        for (F, Om, Ap), c in zip(self.peaks, cols):
            ax.scatter([Om], [Ap], s=70, color=c, zorder=5, edgecolor="#0b0e14",
                       label="measured peak, F=%.2f  ($\\Omega$=%.3f)" % (F, Om))
        ax.axvline(self.w0, color="#33405a", ls=":", label=r"linear $\omega_0$")
        ax.set_xlabel(r"drive frequency $\Omega/\omega_0$"); ax.set_ylabel("steady amplitude $A$")
        ax.set_xlim(0.9, 1.4); ax.legend(loc="upper left", fontsize=8.5, framealpha=0.25)
        return fig


# ============================================================ Scene C: CK inharmonic comb fingerprint
class CKCombScene:
    name = "m16_ck_comb_fingerprint"

    def metadata(self):
        r = (CK/CK[0])
        return make_metadata(
            model="CK inharmonic carrier comb (the FTGB spectral fingerprint)",
            tier="[V]",
            verify_scripts=["ck_eigenvalues_check.py", "beat_law_across_scales_check.py"],
            equations=["boundary quantization tan x = x -> roots {4.4934, 7.7253, 10.9041}",
                       "comb ratios 1 : %.3f : %.3f  (vs harmonic 1:2:3)" % (r[1], r[2]),
                       "SI carrier f_n = v_A x_n / (2 pi R) -> {121, 208, 294} kHz",
                       "ratio is SCALE-INVARIANT: same comb from lab kHz to space mHz"],
            params={"ck_roots": list(np.round(CK, 4)), "ratios": list(np.round(r, 4)),
                    "comb_kHz": list(np.round(COMB_KHZ, 1)), "v_A": V_A, "R": R},
            time_transform="static spectrum (no time axis)",
            note="a harmonic 1:2:3 comb would FALSIFY the Beltrami-carrier reading -- the sharpest fingerprint.",
        )

    def figure_static(self):
        import matplotlib.pyplot as plt
        r = CK/CK[0]
        harm = np.array([1.0, 2.0, 3.0])
        fig, ax = plt.subplots(figsize=(8.0, 5.4))
        fig.subplots_adjust(bottom=0.16, top=0.9)
        fig.suptitle("The CK inharmonic fingerprint  1 : 1.719 : 2.427  (a bell, not a string)", color="#e6e6e6")
        ax.stem(r, np.ones_like(r), linefmt="#4dd6d6", markerfmt="o", basefmt=" ", label="CK comb (tan x = x)")
        ml, sl, bl = ax.stem(harm, 0.7*np.ones_like(harm), linefmt="#e879b9", markerfmt="s", basefmt=" ",
                             label="harmonic 1:2:3 (would falsify)")
        plt.setp(sl, alpha=0.6); plt.setp(ml, alpha=0.6)
        for x, f in zip(r, COMB_KHZ):
            ax.annotate("%.3f\n(%.0f kHz)" % (x, f), (x, 1.02), ha="center", fontsize=9, color="#cfd8e3")
        ax.set_xlim(0.5, 3.4); ax.set_ylim(0, 1.35); ax.set_yticks([])
        ax.set_xlabel(r"frequency ratio  $f_n / f_1$")
        ax.legend(loc="upper right", fontsize=9, framealpha=0.25)
        return fig


SCENES = [BeatTorqueScene(), DuffingBackboneScene(), CKCombScene()]
