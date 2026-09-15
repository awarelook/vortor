# The Coherent Object — a minimum viable, reproducible theory

**FTGB (Fractal-Toroidal-Beat):** one driven Beltrami–Hopf toroidal soliton, read at once as a plasma field
and a matter wave. Author: Nathaniel Hanks · v1.1 · reproduce: `python results/verify/verify_all.py` (**81/81**,
CI-gated, no network). Full map: [`INDEX.md`](INDEX.md) · terms: [`GLOSSARY.md`](GLOSSARY.md) · citations:
[`REFERENCES.md`](REFERENCES.md) · honest self-assessment: [`results/TIER_LEDGER.md`](results/TIER_LEDGER.md).

---

> ## ✦ Apex summary (the whole theory in one breath)
> A force-free plasma relaxes, at fixed helicity, to a single-chirality **Beltrami eigenmode** `∇×B=λB`
> (Woltjer–Taylor). Read as an object it is a driven, nonradiating, topologically knotted **toroidal
> resonator**. **Proven `[V]` here:** its spectrum is the inharmonic Chandrasekhar–Kendall comb (`tan x=x`,
> ratios `1:1.719:2.427`); at coherence its self-interaction is *null* (`u×ω=0`), so it is an **exact,
> eternal, blow-up-free solution — and, driven, an exact steady state and a stable attractor**; it carries
> topological invariants (Hopf `Q_H=1`, Chern `C=±2`), an exact **anapole** (nonradiating) form, and a
> computed chirality/`C`/**Majorana** cluster. **Hypothesized `[S]` (to test):** *the object is the particle*
> — mass = trapped oscillation (`m=ħω/c²`, de Broglie `v_g·v_p=c²` shown in software), and the **LENR active
> site** is this object providing slow coherence at *assembly* (γ-quiet disposal is the credited **E0**
> collective channel, not the anapole; the one open problem is the entrance-channel **assembly geodesic** —
> beat the measured `~10⁻⁷` baseline). **Falsifiable now:** the comb fingerprint (at the linear-drive limit),
> the kHz beat, a `0νββ` null, He-4/heat at `24 MeV/⁴He`, and neutron-yield ∝ heat (the primary kill).
> **Never claimed:** α's value, exact mass ratios, any nuclear *rate*, energy from nothing. Every claim
> carries a tier; every result has a script.

---

## 1. The object

The **force-free / Beltrami** state `∇×B = λB` (current along field, `J×B=0`) is the minimum-energy state of
a plasma at fixed magnetic helicity `H=∫A·B` [Woltjer 1958; Taylor 1974; Moffatt 1969]. FTGB takes that state
as a physical *object* — a driven, dissipative, toroidal, Hopf-knotted standing wave — and reads it two ways
at once: as a **plasma structure** (the ball-lightning / plasmoid / EVO family) and, via the Madelung
identity (Schrödinger ⇔ a fluid) [Madelung 1927], as a **matter wave**. One object; the rest is forced.

## 2. Proven core — validated math & physics `[V]` / credited

| Result | Statement | Status · script |
|---|---|---|
| **CK carrier comb** | boundary quantization `tan x = x` → ratios `1 : 1.719 : 2.427`; near-equal beats + a kHz second-order detuning | `[V]` `ck_eigenvalues_check`, `delta_detuning_beat_check` |
| **Coherence *is* regularity** | at the Beltrami state the Lamb vector `u×ω=0`, so advection is a pure gradient → `u(t)=e^{−νλ²t}u₀` is an **exact eternal smooth solution** (BKM never triggers) [cf. Beale–Kato–Majda 1984] | `[V]` `exact_beltrami_regularity_check` |
| **Driven / sustained** | forcing `f=νλ²u_B` makes it an **exact steady solution** (self-sustaining) and a **stable attractor** — perturbations decay, enstrophy stays bounded, **swept across Re ≈ 126 → 628** (32³, confirmed 48³) with the attraction not weakening; a Taylor–Green base drifts | `[V]`@Re≤628 `r2_driven_beltrami_attractor_check`, `r2_reynolds_sweep_check` |
| **Heartbeat, not flywheel** | fixed-helicity energy minimization over N modes is a **linear program** whose minimum is the single lowest mode → a beat-carrying object is *never* static; it must be **driven** | `[V]` `nmode_woltjer_lp_check` |
| **Topology** | idealized-reference Hopf charge `Q_H=1` (Gauss linking of the closed-fibre reference pair) and wave-mode Chern `C=±2` (the photon helicity index), both reproduced in-repo; the *actual CK object* carries real helicity `H≈0.088`, not an integer charge (Grand Synthesis C.2) | `[V]` `topology_invariants_check` |
| **Current-leg trilogy** | static closure `ρv ~ K^i` ⇔ `\|B\\|=const` — impossible for nontrivial force-free fields; the driven closure is externally-driven, not emergent (the flagship structural theorem) | `[V]` `currentleg_trilogy_check` |
| **S³ curl spectral zeta** | exact closed form `ζ_B(s)=ζ(s−2)−ζ(s)` ⇒ `ζ′(−2)=−ζ(3)/4π²` (verified to 1e-25; resolves the π-power anomaly) | `[V]` `curl_spectral_zeta_pi_power_check` |
| **Reeb / contact** | the Beltrami field is a **Reeb field**; Weinstein–Taubes guarantees a closed field-line loop [Etnyre–Ghrist 2000; Taubes 2007] | `[credited]` `reeb_spectral_geometry_check` |
| **Anapole (nonradiating)** | the ordinary dipole cancels (`~1e-16`); a Zel'dovich toroidal-dipole resonator holds energy without radiating [Afanasiev–Stepanovsky 1995; Papasimakis 2016] | `[V]`/`[credited]` `oam_toroidal_resonator_resolution_check` |
| **Chirality / C / Majorana** | chirality `= sign λ = sign H`; antiparticle `= −λ = C`; the self-dual `θ_χ=45°` state is **Majorana** | `[V]` `majorana_selfdual_check` |
| **Winding protection** | integer winding is conserved through violent (FPUT) collapse away from field zeros; slips only through an exact zero (boundary observed) | `[V]` `fput_winding_conservation_check` |
| **Nuclear energy ledger** | `d+d→⁴He` releases `Q=23.847 MeV`, conserved; `2ω_C(d)=ω_C(⁴He)+ω_Q` exact | `[V]` `lenr_cop_nuclear_positive`, `lenr_energy_ledger` |

Credited inputs used, not re-derived: Beltrami/CK [Chandrasekhar–Kendall 1957]; spin-½ from Hopf
[Wilczek–Zee 1983; Finkelstein–Rubinstein 1968]; the mass-tower dressing [Nielsen TUFT, peer-reviewed —
`[credited]`, arithmetic + topological inputs reproduced in-repo `[V-us]`]; measured screening `U_s≈300–800 eV`.

## 3. Hypothesis to test — the `[S]` frontier

- **The matter-wave identification (the central bet):** *the electron is this object* — mass = trapped
  oscillation (`m=ħω/c²`), spin-½ = Hopf topology, charge = integer winding, de Broglie wave = the beat
  envelope. The **software simulation** reproduces the kinematics: measured `v_g=c²k/ω`, rest-clock `=ω_c`,
  and `v_g·v_p=c²` (`engine/ftgb_resonator_sim.py`). The *math* is `[V]`; the *identification* is `[S]`.
- **The LENR active site:** an **open-fed anapole dipole-balance resonance** holding charge/spin — the
  **active site** providing slow confinement/coherence at *assembly* (`[V]` object / `[S]` role). Crux
  (computed, credited): single-photon `0⁺→0⁺` is E0-forbidden [Church–Weneser 1956] **and** the E1 radiative
  channel is ΔT=0-forbidden (N=Z), so aneutronic ⁴He heat **must** shed **collectively** — the `0⁺→0⁺`
  disposal *operator* is **E0 (monopole)**, *not* the anapole toroidal *dipole* (a forbidden 0→0 double-zero).
  Energy `[V]`, disposal-requirement `[credited]`, mechanism `[S]`. **The one open problem has CONVERGED** (a
  7-check disposal chain, each adversarially verified): it is **not** "one matrix element" (that framing was
  refuted) and **not** the disposal — it is the **entrance-channel assembly corridor** *(sharpened
  2026-09-14 from "geodesic, ≥3 open objects" to ONE question: ⁴He has no bound excited states and
  supra-threshold dwell dies in zeptoseconds, so the only aneutronic route is a **dissipative sub-breakup
  corridor** that sheds the full 23.85 MeV during assembly — `entrance_corridor_survival_check`)*. It carries
  **two data bars**: *existence* — beat the measured `~10⁻⁷` baseline [Wilkinson–Cecil, PRC **31**, 2036
  (1985)]; *sufficiency* — the observed dearth `n/⁴He ≤ 10⁻⁹`, i.e. `Δ_suff = 5.47×Δ_dominance`, which with
  the Cauchy–Schwarz ceiling **derives** the crossing fence `β·|dF| ≤ 0.874 MeV/fm`
  (`delta_b4_landau_zener_bridge_check` TEST 2b) — the moduli-space/HPC run decides it. See the tiered
  [`results/LENR_EXPLANATORY_RESOLUTION_MAP_2026-09-14.md`](results/LENR_EXPLANATORY_RESOLUTION_MAP_2026-09-14.md)
  (disposal chain: `disposal_e0_pair_fork` / `disposal_nonpopulation` / `disposal_coherence_volume_nogo` / …);
  earlier synthesis `lenr_disposal_channel_check`, `results/LENR_ACTIVE_SITE_SYNTHESIS_2026-09-14.md`.

**Settled-negatives kept as wins:** α's value from winding (`ι≈1`, not 137); direct phonon-nuclear coupling
(dead by `~66` orders); phase conjugation / ponderomotive as *rate* levers; monopole catalysis (`π₃≠π₂`);
the scalar-EM free-energy extension.

## 4. Significance — cold fusion, transmutation, heat & electricity (Aureon-, SAFIRE-style)

FTGB gives the field's universally-invoked but rarely-defined **"active site"** a concrete, computable
referent: a driven, coherent, **nonradiating Beltrami/anapole resonator**. The corrected frame is physics,
not apology — **`COP>1` is nuclear-sourced and expected** (`d+d→⁴He` is `~1e4–1e5×` the eV trigger; the first
law holds); excess heat and transmutation are **data to explain**, weighted honestly against the null results
[Fleischmann–Pons 1989; Miles 1993/2000; McKubre; Iwamura 2002 (Cs→Pr); Storms 2010; the Berlinguette 2019
null].

- **Self-organized plasma programs (SAFIRE-style anode plasmoids; reverse-vortex reactors, Klimov):** the
  swirl-vs-straight `COP` contrast maps directly onto the Woltjer–Taylor single-λ coherence claim — testable,
  not just analogical, with a helicity diagnostic.
- **Direct heat *and* electricity (Aureon-style LEC / co-deposition):** the object's oscillating near-field
  **junction-pole EMF** (`V=ω_b ΔΦ ~ 0.1–1 V`, an `[S]` order-of-magnitude estimate — not yet derived or
  scripted) would be a real, reactive, load-driving voltage — the nuclear energy couples into the EM mode
  that drives current, rather than degrading to heat first. Honest limit: it is *fed*, never a net source;
  the energy is nuclear and conserved.
- **Transmutation:** hops on the discrete knot/Skyrme baryon lattice (baryon-conserving), plus a specific,
  falsifiable **bound-state β/EC trigger** (`¹⁶³Dy→¹⁶³Ho`, ionization-gated [Bosch 1996; Jung 1992]) — a
  heatless, ν-dominated ΔZ signature testable by X-ray charge-state spectroscopy against zero background.

## 5. Predict / test / falsify

1. **Comb fingerprint** — a driven plasmoid rings at `1 : 1.72 : 2.43` **in the linear/low-drive limit**; a
   *harmonic* `1:2:3` comb falsifies it. (M16: under hard drive the ratios pull anharmonically — the Duffing
   backbone bend, separable from the Arnold-tongue lock — so the fingerprint is a *linear-limit* statement.
   Geometry caveat: the ratios are the **spherical-boundary** CK values; the toroidal eigenvalues shift with
   aspect `a/R` — the FreeFEM torus solve gives a doublet split `Δλ=0.2806`, not sphere roots
   (`MATH_TOOLKIT_BASE.md` §3 CORRECTIVE) — so the experimental comparison must state which geometry it assumes.)
2. **kHz beat + detuning** — near-equal beats with a small second-order detuning (coil + FFT). (The kHz beat
   is a macroscopic rate-*gate*, **never** a pump of the MeV channel — settled-negative, M16.)
3. **Neutron yield ∝ heat** — **the primary, band-independent kill** of the aneutronic channel.
4. **He-4/heat = 24 MeV/⁴He** [Miles] — a large deviation kills the `d+d→⁴He` reading.
5. **~20 MeV e⁺e⁻ / 511 keV** — the E0 internal-pair *secondary* discriminator: if a localized hot ⁴He\* 0⁺
   compound forms it would appear; its non-observation is weak evidence for the entrance-assembly (b2) premise.
6. **`0νββ` null** [KamLAND-Zen / LEGEND] — kills the Majorana-neutrino prediction.
7. **Beat-locked yield steps** as drive sweeps the cascade `f_b(L)=N^L f_b(0)` — the sharpest theory-specific
   discriminator (no static LENR model predicts it; the one existing dataset, HLC 2010, fits neither N^L nor
   CK — but it is a Pd-D lattice, the wrong object).
8. **FWM sidebands** at `1.517 f₁`, `1.820 f₁` — decide the phase-conjugation role.

## 6. Reproduce & trust

```bash
pip install -r requirements.txt          # numpy, mpmath
python results/verify/verify_all.py      # 81/81 PASS, deterministic, no network, CI-gated
```

Everything load-bearing has a script; the foundation numbers are re-derived in-repo; no claim exceeds its
tier; no number is fabricated; settled-negatives are kept. Depth (scipy/sympy provenance, FreeFEM eigensolves,
HPC handoffs): [`REPRODUCE.md`](REPRODUCE.md). The one honest ceiling: unconditional high-Reynolds driven
regularity and the LENR *rate* (the entrance-channel assembly corridor / near-BPS `ρ_eff` run) need the
scoped GPU/HPC runs — named in `handoffs/`, not fudged.

*Citations here are compact; full, tier-tagged bibliography in [`REFERENCES.md`](REFERENCES.md) (§1 credited
core; §1e–1j corpus-salvage clusters; §1k LENR active-site physics). Vocabulary in [`GLOSSARY.md`](GLOSSARY.md)
(§1–8 core; §9 plasmoid/EVO/CMNS). Science history & lineage in
[`HISTORY_PEOPLE_EVO_CMNS.md`](HISTORY_PEOPLE_EVO_CMNS.md), [`LINEAGE.md`](LINEAGE.md).*
