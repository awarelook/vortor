"""
Ball-lightning sustaining-power closures -- corpus fold (dynamical_plasmoid), reproduced in-repo.

Salvaged from the ckfreefem ark (11_verified_ark/dynamical_plasmoid section 6 item 6; survey:
results/SALVAGE_SURVEY_ARK_2026-09-13.md). Two real, resolved closures + one honestly-open gap:

  TEST 1 -- THE IONIZATION ORDER PARAMETER [V-us]. Ball lightning's natural order parameter is the
            scalar electron density n(t) obeying the driven-dissipative equation
                dn/dt = S - alpha_DR n^2      (dissociative recombination, quadratic loss)
            with steady state n_ss = sqrt(S/alpha_DR). Sustaining the RF-relevant density
            n = 1.08e16 /m^3 against recombination (alpha_DR = 1e-13 m^3/s) over the CANON object
            volume (a sphere of R = 0.12 m -- the same canon radius) at the standard 34 eV/ion-pair
            air ionization cost requires ~0.46 W -- UNDER HALF A WATT -- and the steady state is
            reached in ~2.5 ms from a cold start (integrated here), far faster than the observed
            1-5 s lifetime. The energy BUDGET is not the obstacle. Stress test folded from the
            corpus: even a 38x-higher W-value (wall-loss-contaminated discharge data, not really
            applicable) gives ~17.6 W, still ~1800x below the combustion ceiling below.
  TEST 2 -- THE DELIVERY MECHANISM IS ALREADY PUBLISHED [credited + V-us arithmetic]. Abrahamson &
            Dinniss (Nature 403, 519 (2000)): lightning reduces soil silica to Si nanoparticles
            whose slow (diffusion-limited, oxide-shell) combustion releases energy over seconds --
            independently supported by the first natural-BL spectrum (Cen, Yuan & Xue, PRL 112,
            035001 (2014): Si/Fe/Ca soil lines for the whole event). Standard thermochemistry
            (Si + O2 -> SiO2, dH = 910.7 kJ/mol): the silicon mass needed to supply 0.46 W for the
            observed 1-5 s is ~14-71 MICROGRAMS -- 4+ orders of magnitude below the gram-scale
            nanoparticle inventory the published mechanism already treats as ordinary. The
            ionization-sustaining budget is overwhelmed with margin by real, published, spectrally
            supported physics. UNITS CORRECTION CAUGHT BY THIS REPRODUCTION: the corpus text says
            "tens of nanograms to ~70 nanograms" -- a 1000x unit slip; its OWN companion statement
            ("4-5 orders below the gram-scale inventory") is consistent with MICROGRAMS (1 g / 71 ug
            ~ 1.4e4), confirming the slip is in the unit word, not the physics. The closure stands
            at the corrected magnitude.
  THE HONEST OPEN GAP (printed, not glossed): sustaining the MAGNETIC (force-free/CK) structure
            against Ohmic decay is a SEPARATE question -- the corpus computed 2.3e5-2.6e7 W at an
            unverified ~5 eV placeholder temperature. The ionization closure does NOT close it;
            it stays open, named in physical units.

numpy only, deterministic. Run: python results/verify/ball_lightning_closures_check.py
"""
import numpy as np

ok = True


def check(name, cond, detail=""):
    global ok
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, ("  -- " + detail) if detail else ""))
    ok = ok and cond


print("=" * 92)
print("Ball-lightning sustaining power: the ionization budget closes; the magnetic one stays open")
print("=" * 92)

E_CH = 1.602176634e-19
R = 0.12                       # m -- the canon object radius
V = 4.0 / 3.0 * np.pi * R**3
n_ss = 1.08e16                 # /m^3 -- the RF-relevant electron density (corpus, sourced)
alpha_DR = 1e-13               # m^3/s -- dissociative recombination
W_ION = 34.0                   # eV per ion pair in air (standard)

print("TEST 1 -- the ionization order parameter  dn/dt = S - alpha_DR n^2:")
S = alpha_DR * n_ss**2                                  # required source rate /m^3/s
P_ion = S * V * W_ION * E_CH
print("  canon volume V = %.2e m^3 (R = %.2f m);  S = %.2e ionizations/m^3/s" % (V, R, S))
print("  required sustaining power P = S*V*34 eV = %.3f W" % P_ion)
check("the ionization budget is under half a watt (corpus: ~0.46 W)", 0.4 < P_ion < 0.5,
      "P = %.3f W" % P_ion)

# time to steady state from a cold start (RK4 on the ODE, deterministic)
n, t, dt = 1e10, 0.0, 1e-6
while n < 0.99 * n_ss and t < 0.1:
    f = lambda nn: S - alpha_DR * nn**2
    k1 = f(n); k2 = f(n + dt/2*k1); k3 = f(n + dt/2*k2); k4 = f(n + dt*k3)
    n += dt/6*(k1 + 2*k2 + 2*k3 + k4)
    t += dt
check("steady state reached in milliseconds (corpus: ~2.5 ms) << the observed 1-5 s lifetime",
      1e-4 < t < 1e-2, "99%% of n_ss at t = %.2f ms" % (t * 1e3))
P_stress = P_ion * 38.0
print("  stress test (38x W-value, wall-loss-contaminated -- not applicable, tested anyway): %.1f W" % P_stress)

print("TEST 2 -- the published delivery mechanism (Abrahamson-Dinniss Si combustion):")
DH = 910.7e3                   # J/mol, Si + O2 -> SiO2
M_SI = 28.09e-3                # kg/mol
e_per_kg = DH / M_SI           # J/kg
for tau in (1.0, 5.0):
    m_req = P_ion * tau / e_per_kg
    print("  lifetime %.0f s -> required Si mass = %.1f micrograms" % (tau, m_req * 1e9))
m5 = P_ion * 5.0 / e_per_kg
check("required Si is tens of micrograms (corpus said 'ng' -- a caught 1000x unit slip; its own "
      "'4-5 orders below gram-scale' companion figure matches MICROGRAMS)", 1e-8 < m5 < 1e-7,
      "%.1f ug for 5 s" % (m5 * 1e9))
inv_margin_g = 1e-3 / m5
check("margin vs the gram-scale nanoparticle inventory is > 1e4 (the corpus's own 4-5 orders)",
      inv_margin_g > 1e4, "1 g / m_req = %.1e" % inv_margin_g)
P_ceiling = e_per_kg * 1e-3    # 1 g/s combustion ceiling, W
check("even the 38x-stressed budget sits far below the combustion ceiling",
      P_ceiling / P_stress > 1000, "ceiling %.1f kW vs %.1f W (%.0fx)" % (P_ceiling/1e3, P_stress, P_ceiling/P_stress))

print("THE HONEST OPEN GAP (named, not glossed): the MAGNETIC (force-free) structure's own Ohmic")
print("sustaining power was computed in the corpus at 2.3e5-2.6e7 W (at an UNVERIFIED ~5 eV")
print("placeholder temperature) -- 5-8 orders above the ionization figure. The closure above answers")
print("the IONIZATION question only; a mechanism sustaining the magnetic structure of a free-floating")
print("object remains open. (The jewel's driven-object reading requires external drive for exactly")
print("this reason -- consistent, and consistent too with the N-mode Woltjer 'heartbeat' theorem.)")
print("Credited anchors: Abrahamson & Dinniss, Nature 403, 519 (2000); Cen-Yuan-Xue, PRL 112, 035001")
print("(2014); REFERENCES section 1f. Corpus provenance: 11_verified_ark/dynamical_plasmoid.")
print("status:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
