"""
The nuclear-frontier scenes -- the corridor and the gate, drawn from the SAME numbers the checks validate.

  Scene D -- THE CORRIDOR: the A=4 level scheme with no bound excited states, the zeptosecond
             supra-threshold wall, and the one open route (dissipative sub-breakup corridor).
             backed by entrance_corridor_survival_check, disposal_nonpopulation_check            [V]-arith/[credited]
  Scene E -- THE GATE: the d+d spin-channel arithmetic -- the singlet-only s-wave door and how
             coherent preparation steers it (1/9 -> 1/3 at m=0 -> 0 at m=+-1).
             backed by spin_channel_gate_check, delta_b4_stageD_bps_overlap_check                [credited]-arith/[S]

Every number is asserted by a passing check; the metadata sidecar names it. These are DIAGRAMS of computed
numbers, not simulations -- the tier travels with the pixel.
"""
import numpy as np

from .metadata import make_metadata

CY, MG, YE, GR, GRY = "#4dd6d6", "#e879b9", "#ffcf5a", "#7ee787", "#8b98ad"


# ============================================================ Scene D: the corridor
class CorridorScene:
    name = "lenr_corridor"

    E_DD, E_PT, E_N3HE = 23.847, 19.815, 20.578
    E_02, GAM_02 = 20.21, 0.50
    T_HALF = 9.1e-22

    def metadata(self):
        return make_metadata(
            model="the entrance-channel assembly corridor (the one open LENR problem, sharpened)",
            tier="[V]",
            verify_scripts=["entrance_corridor_survival_check.py", "disposal_nonpopulation_check.py",
                            "delta_b4_landau_zener_bridge_check.py"],
            equations=["4He: NO bound excited states (first excited 0+_2 at 20.21 MeV > p+t at 19.815)",
                       "supra-threshold half-life t_1/2 = hbar ln2 / Gamma ~ 9e-22 s (Gamma ~ 0.5 MeV)",
                       "=> the only aneutronic route: shed ALL 23.85 MeV DURING assembly, never pausing",
                       "two data bars: existence > 1e-7 (Wilkinson-Cecil 1985); sufficiency n/4He <= 1e-9",
                       "derived fence: beta*|dF| <= 0.874 MeV/fm (the dearth forces the slow/soft corner)"],
            params={"E_dd_MeV": self.E_DD, "E_pt_MeV": self.E_PT, "E_n3He_MeV": self.E_N3HE,
                    "E_02_MeV": self.E_02, "Gamma_02_MeV": self.GAM_02, "t_half_s": self.T_HALF},
            time_transform="static level scheme (no time axis)",
            outputs=[],
            note="no state ladder exists below breakup and no slow dwell exists above it -- the corridor "
                 "formulation is FORCED by census + survival arithmetic, not chosen.",
        )

    def figure_static(self):
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(8.6, 7.2))
        fig.subplots_adjust(left=0.12, right=0.7, bottom=0.14, top=0.9)
        fig.suptitle("The assembly corridor -- why the only aneutronic route never pauses", color="#e6e6e6")

        def level(E, c, lab, lab_y=None, lw=2.4):
            ax.hlines(E, 0.14, 0.62, color=c, lw=lw)
            ly = E if lab_y is None else lab_y
            ax.text(0.655, ly, lab, color=c, fontsize=9.5, va="center")
            if lab_y is not None:
                ax.plot([0.62, 0.648], [E, lab_y], color=c, lw=0.7, alpha=0.6)

        level(0.0, GR, "$^4$He ground state 0$^+$  (the only bound state)")
        level(self.E_PT, MG, "p+t breakup  19.815 MeV", lab_y=18.7)
        ax.axhspan(self.E_02 - self.GAM_02 / 2, self.E_02 + self.GAM_02 / 2, xmin=0.13, xmax=0.58,
                   color=YE, alpha=0.18)
        level(self.E_02, YE, "0$^+_2$ 20.21 MeV ($\\Gamma\\sim$0.5) -- ABOVE breakup", lab_y=20.3, lw=1.8)
        level(self.E_N3HE, MG, "n+$^3$He breakup  20.578 MeV", lab_y=21.8)
        level(self.E_DD, CY, "d+d entrance  23.847 MeV")

        ax.annotate("NO STATES\n(zero bound excited levels:\nno rung to pause on)",
                    xy=(0.38, 10.0), color=GRY, fontsize=10, ha="center", va="center", style="italic")
        ax.annotate("above p+t: dwell dies in $t_{1/2}\\approx 9\\times10^{-22}$ s",
                    xy=(0.38, 22.5), color=YE, fontsize=8.6, ha="center")
        ax.annotate("", xy=(0.09, 0.4), xytext=(0.09, self.E_DD - 0.3),
                    arrowprops=dict(arrowstyle="-|>", color=GR, lw=2.6))
        ax.text(0.055, 12.0, "THE CORRIDOR: shed all 23.85 MeV during assembly -- never pausing, never crossing p+t",
                color=GR, fontsize=9, rotation=90, va="center", ha="center")
        ax.text(0.655, 12.6, "two data bars:\n  existence  > 1e-7 (measured)\n  sufficiency n/$^4$He $\\leq$ 1e-9\nderived fence:\n  $\\beta\\,|dF| \\leq$ 0.874 MeV/fm",
                color="#cfd8e3", fontsize=9)
        ax.set_xlim(0, 1.12); ax.set_ylim(-1.2, 25.6)
        ax.set_ylabel("excitation above the $^4$He ground state [MeV]")
        ax.set_xticks([])
        for s in ("top", "right", "bottom"):
            ax.spines[s].set_visible(False)
        return fig


# ============================================================ Scene E: the gate
class SpinGateScene:
    name = "lenr_spin_gate"

    GATES = [("unpolarized\n(statistical)", 1.0 / 9.0, GRY),
             ("s-wave\nallowed", 1.0 / 6.0, CY),
             ("m=0\ncondensate", 1.0 / 3.0, GR),
             ("m=$\\pm$1\ncondensate", 0.0, MG)]
    DW_FLOOR = 1.3e-6
    BRACKET = (0.55, 0.96)
    BAND = (0.06, 0.08)

    def metadata(self):
        return make_metadata(
            model="the spin/orientation gate: the singlet-only s-wave door and its coherent steering",
            tier="[credited]",
            verify_scripts=["spin_channel_gate_check.py", "delta_b4_stageD_bps_overlap_check.py"],
            equations=["s-wave door to 4He(0+) = the SINGLET alone: 1 of 9 spin states",
                       "condensate pair |1,m>x|1,m>: singlet fraction = 1/3 (m=0), 0 exactly (m=+-1)",
                       "m=+-1 residual (S=2,L=2) route: centrifugal (kR)^4 ~ 1.3e-6 at 240 eV",
                       "consistency (logged, not promoted): 1/9 x [0.55,0.96] = [0.061,0.107] ~ target 0.06-0.08"],
            params={"gate_unpolarized": 1 / 9, "gate_swave": 1 / 6, "gate_m0": 1 / 3, "gate_m1": 0.0,
                    "dwave_floor": self.DW_FLOOR, "stageD_bracket": list(self.BRACKET),
                    "target_band": list(self.BAND)},
            time_transform="static channel arithmetic (no time axis)",
            outputs=[],
            note="falsifier #9: the aneutronic yield of a coherent site must DEPEND on deuteron spin "
                 "preparation -- m=0 enhances up to 3x, m=+-1 closes the s-wave door. No thermal-statistical "
                 "model predicts a polarization knob.",
        )

    def figure_static(self):
        import matplotlib.pyplot as plt
        fig, (ax, ax2) = plt.subplots(1, 2, figsize=(9.4, 5.6), width_ratios=[1.25, 1.0])
        fig.subplots_adjust(left=0.09, right=0.97, bottom=0.2, top=0.86, wspace=0.3)
        fig.suptitle("The spin/orientation gate -- coherent preparation steers the aneutronic door", color="#e6e6e6")

        labels = [g[0] for g in self.GATES]
        vals = [max(g[1], self.DW_FLOOR) for g in self.GATES]
        cols = [g[2] for g in self.GATES]
        x = np.arange(4)
        ax.bar(x, vals, color=cols, width=0.62)
        ax.set_yscale("log"); ax.set_ylim(5e-7, 1.0)
        ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=8.4)
        ax.set_ylabel("singlet fraction (the s-wave door to $^4$He 0$^+$)")
        for xi, g in zip(x, self.GATES):
            v = g[1]
            ax.text(xi, max(v, self.DW_FLOOR) * 1.4, ("1/9" if xi == 0 else "1/6" if xi == 1 else "1/3" if xi == 2 else "0 (d-wave floor)"),
                    ha="center", color=g[2], fontsize=10)
        ax.axhline(self.DW_FLOOR, color=MG, ls=":", lw=1.0, alpha=0.7)
        ax.text(1.5, self.DW_FLOOR * 0.5, "residual d-wave route $(kR)^4\\sim 10^{-6}$", color=MG, fontsize=8, ha="center", va="top")
        ax.set_title("the gate, and how coherence moves it", fontsize=11)

        # right panel: the three-piece consistency (logged coincidence-class)
        lo, hi = self.BRACKET
        ax2.axhspan(self.BAND[0], self.BAND[1], color=YE, alpha=0.25, label="target band $\\rho_{eff}$ 0.06-0.08")
        for g, name, c in [(1 / 9, "1/9 gate", GRY), (1 / 6, "1/6 gate", CY)]:
            ax2.plot([name] * 2, [g * lo, g * hi], color=c, lw=7, solid_capstyle="round",
                     label="%s $\\times$ [0.55, 0.96]" % name)
        ax2.set_ylim(0, 0.2)
        ax2.set_ylabel("gate $\\times$ Stage-D density bracket")
        ax2.set_title("the logged consistency\n(coincidence-class, NOT a derivation)", fontsize=10)
        ax2.legend(loc="upper left", fontsize=7.5, framealpha=0.2)
        return fig


SCENES_LENR = [CorridorScene(), SpinGateScene()]
