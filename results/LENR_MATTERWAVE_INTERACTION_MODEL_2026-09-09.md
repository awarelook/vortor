# The matter-wave interaction model — a universal kernel for coherent-object interactions, transmutation, and the LENR anomalies

**Author:** Nathaniel Hanks · **Date:** 2026-09-09
**Provenance:** bridges `FTGB_CURRENTLEG_TRILOGY` (the object) + `handoffs/HANDOFF_DELTA_B4_SKYRME_RELAXATION`
(the Δ branching) + M8-2 (matter-wave `m = ħω/c²`) + M11/M12 (vacuum) + Nielsen TUFT (the lattice).
**Verification:** `results/verify/lenr_energy_ledger.py` (exact conservation arithmetic; no fabricated rate).

**One-line.** Every coherent-object interaction — fusion, transmutation, or an energy transform — is one
universal process: a **matter-wave beat** whose transition amplitude factorizes into a *settled selection
skeleton* times an *open radial overlap* (Δ), on a *discrete knot lattice*, with energy–mass conserved as a
matter-wave frequency ledger. The LENR anomalies are what this kernel predicts **structurally**; the two
missing numbers (Δ, U_s) are named, not fabricated.

**Tier.** `[S] synthesis` throughout, with `[V]` only for the conservation arithmetic, `[credited]` for the
established nuclear/plasma physics, and `[open]`/`[inherited]` for the two rate inputs. **No over-unity is
claimed; no rate or cross-section is derived; the `e^(-2/3)` factor stays excised.**

---

## 1. The universal interaction kernel   `[credited]` structure / `[S]` application

Each object is a matter wave `ψ = √ρ e^{iθ}` with whirl (Compton) frequency `ω_C = m c²/ħ` (M8-2). Two
objects interacting overlap their fields; the transition amplitude is `M_fi = ⟨f| Ĥ_int |i⟩`, and the rate is
**Fermi's golden rule**

```
  Γ = (2π/ħ) |M_fi|² ρ_f  .                                            (1)
```

The interaction is a **resonant beat**: it is strongest when the initial and final whirls are bridged by a
collective mode, `ω_i − ω_f = ω_release`. Energy–mass conservation is exactly the **matter-wave frequency
ledger**

```
  Σ_i ħω_i = Σ_f ħω_f + ħω_release       ⇔       Σ_i m_i c² = Σ_f m_f c² + Q .   (2)
```

**[V]** For `d + d → ⁴He`, `2 ω_C(d) = ω_C(⁴He) + ω_Q` holds to `0.00e+00` (ledger §3) — the bookkeeping is
mass–energy conservation restated. The released `ħω_release = Q` goes into the **coherent collective mode**
(the EVO comb / lattice phonons), *not* into fast neutrons or hard γ — that partition is §4.

## 2. The amplitude factorization — settled skeleton × open overlap   `[V]`/`[S]`/`[open]`

From the trilogy + the Δ hand-off, the branching amplitude factorizes as

```
  M_fi(θ) = Σ_α  C_α  A_α  R_α  S_α  .                                  (3)
```

| Factor | Meaning | Tier |
|---|---|---|
| `C_α` | geometric/topological selection (O_h symmetry, gerade sector) | **SETTLED `[V]`** |
| `A_α` | symmetry amplitudes — **E0 γ-suppression, aneutronic = dynamical** | **SETTLED `[V]`** |
| `S_α` | the B=4 collective-mode basis (published) | `[S]` |
| `R_α` | reduced **radial overlaps + phases** = the off-diagonal **Δ** gap | **`[open]`** |

So the amplitude's **selection skeleton is derived**; only its **magnitude** waits on the one open number Δ
(the Landau–Zener gap; target band 1.4–1.9 MeV; HPC-only, `handoffs/`). This is the crux: FTGB *owns* the
selection physics and *names* the single missing overlap.

## 3. The lattice and its selection rules   `[credited]`/`[framework: Nielsen]`

The accessible object states form a **discrete knot / mass lattice**:
- **Skyrme baryon sector** `π₃(S³)`: `B=1` nucleon, `B=2` deuteron, `B=3`, `B=4` α-cube (the `d+d` merger
  target). `[credited]`
- **Lepton / Hopf sector** `π₃(S²)`: the chargeless/neutrino and charged-lepton rungs. `[S]`
- **Nielsen TUFT tower** `[framework]`: stable eigenmodes of the 9D curl operator (unknot, Hopf, trefoil,
  figure-8) — a discrete topological spectrum setting *which* final nuclei are lattice-accessible and their
  spacing (hence the available Q). Beltrami/curl eigenmodes are the shared math with the FTGB carrier comb.

**Selection rules (what an interaction is allowed to do):**
1. **Topological charge conserved** — baryon `B` (Skyrme) or Hopf/lepton number (S²). Transmutation
   `A → B + C` conserves `Σ B`; this keeps **baryon-conserving fusion/transmutation distinct from baryon
   decay** (the standing scope discipline).
2. **Symmetry** — O_h, gerade, and **E0 (monopole)** de-excitation ⇒ the **aneutronic** channel (§4).
3. **Resonance** — the transition is favored when a collective mode (the comb) bridges `ω_i − ω_f`; the EVO
   supplies those channels.

**Transmutation** is a hop on this lattice; an **energy transform** is the released `ħω_release` shed into the
coherent mode.

## 4. The multibody energy–mass ledger   `[V]` arithmetic / `[S-mechanism]` partition

For an EVO-catalyzed multibody event:

```
  reactants (lattice knots)  +  EVO coherent mode  +  vacuum-coupled drive
        →  product knot (lower tower rung)  +  Q into the coherent mode  →  heat .
```

- **Barrier / probability** — screening `U_s` lowers the Coulomb barrier; the Gamow penetration enhancement
  `P(E+U_s)/P(E)` is **large but finite** (ledger §5: `~10⁷–10¹²` at `E~300 eV`, `U_s~300–800 eV`). `U_s` is
  **host-lattice inherited** `[inherited]`, not FTGB-derived; it sets the *probability scale*, not the branch.
- **Branching** — the aneutronic (bound `⁴He`) vs breakup (neutron) split is set by **Δ** `[open]`; a Δ in
  the 1.4–1.9 MeV band suppresses the neutron channel.
- **Aneutronic partition** — the `⁴He` forms through a **collective E0 mode**; E0 (`0⁺→0⁺`) forbids single
  real-photon emission, so the γ channel is suppressed and the `Q = 23.85 MeV` sheds into **lattice + comb
  phonons as heat** `[S-mechanism]` (mechanism credited; partition fraction not derived).

## 5. The three players, placed honestly

- **EVO — the coherent scaffold** `[V]` recipe / `[S]` catalysis. The macroscopic resonance rung
  (`resonator_family.html`; carrier comb {121, 208, 294} kHz). It provides (i) the screening environment
  `U_s`, (ii) the collective-mode basis `S_α`, and (iii) the **resonant beat channels** that bridge the
  frequency gap in (2). It is the *verified environment* of the LENR position — not the reaction itself.
- **Neutrinos — a separate rung, NOT the heat channel** `[S]`. The neutrino is the chargeless self-dual
  smoke-ring `π₃(S²)`. In the **baryon-conserving `d+d → ⁴He`** channel there is **no weak process**, hence
  **no neutrino** — the heat is aneutronic *and* neutrino-free (fusion, not weak-sector transmutation à la
  Widom–Larsen). If a weak channel operates in some systems, neutrinos would *carry energy away* (a loss, not
  a source). **`0νββ` is the honest external test of the neutrino rung**, independent of the heat.
- **Vacuum waves — the drive medium, not an energy source** `[S]`/`[excised]`. The polarizable vacuum
  (`K_PV`, ZPF `ω³`; M11) is the medium of the driving `E·B` term that makes the current-leg closure
  *realizable* (trilogy leg c). **CRUCIAL:** the vacuum is a reservoir at equilibrium — **no net energy is
  extracted from the ZPF** (no over-unity; the `e^(-2/3)` "vacuum gain" is excised). The measured gain is the
  nuclear `Q` released aneutronically; the drive only *organizes* it. **COP 1.3–1.4 is inherited field
  positioning, not derived, and is not over-unity.**

## 6. What the model explains — and what it does not

**Explains, structurally `[S]`:**
- **Aneutronic excess heat** — E0 collective de-excitation + the coherent channel (§4).
- **He-4/heat = 24 MeV/He-4** — the ledger `[V]`; the ash is `⁴He`, the ratio is the fusion `Q` (Miles
  correlation, `[credited]`).
- **Absence of hard γ / n** — E0 γ-suppression + Δ neutron-branch suppression.
- **Requirement of a coherent host** — the EVO scaffold + screening (no coherent environment ⇒ no channel).
- **Transmutation spectra** — accessible final states are lattice hops on the Skyrme/Nielsen tower.

**Does NOT (honest):** derive any **rate or cross-section** (needs Δ × `U_s`); derive **COP**; claim
**over-unity**; predict specific **isotope yields** without the full lattice-amplitude calc.

## 7. Testable predictions / falsifiers

1. **He-4/heat ratio = fusion Q** (`≈ 24 MeV/⁴He`). Confirmed `[credited: Miles]`; a large systematic
   deviation would refute the `d+d → ⁴He` channel.
2. **Neutron flux ≪ heat-equivalent** — a hard falsifier: if neutron yield scaled with heat, the aneutronic
   (E0 + Δ) mechanism is wrong.
3. **The carrier comb {121, 208, 294} kHz** with the strong-coupling **7/4, 5/2 pull** — a spectral
   discriminator for the EVO scaffold (`dynamics_lab.html` CH-02); a lock at 12/7 = 1.714 refutes it.
4. **Δ in the 1.4–1.9 MeV band** — the HPC prediction; a Skyrme Δ outside the band falsifies the
   neutron-suppression mechanism.
5. **Transmutation products lattice-accessible** — observed ash should sit on the Skyrme/Nielsen tower with
   `Σ B` conserved; off-lattice or baryon-non-conserving products would refute the picture.

## 8. What closes each open piece

| Open | Closes it |
|---|---|
| **Δ (branching magnitude)** | the pion-massive B=4 Skyrme Landau–Zener relaxation (GPU-days; `handoffs/` Δ package) |
| **Driven-object stability** | the R2/R3 conditional enstrophy bounds → unconditional (at-Reynolds spectral run; Hall `Pm≠1` coupled Lyapunov functional) |
| **Rate (Δ × U_s)** | Δ closed **and** `U_s` measured/derived for the specific host lattice |
| **The one-object hypothesis** | stays `[S]`; `0νββ` tests the neutrino rung; the He-4/heat + neutron-null + comb correlations test the object reading |

## 9. References

Nuclear masses / Q-values: AME2020 (used in the ledger). He-4/heat correlation: Miles et al. (1990s).
E0 transitions: Church & Weneser 1956. Skyrme B=4: Battye–Sutcliffe 1997; Halcrow 2016. Ab-initio `d+d`:
Hupin–Quaglioni–Navratil 2019. Golden rule / screening: standard (Gamow; Assenbaum–Langanke–Rolfs 1987
screening). Canonical-helicity drive: Steinhauer–Ishida 1997; Mahajan–Yoshida 1998. Nielsen TUFT
(Hopf-fibration knot lattice): `REFERENCES.md`. In-repo: `FTGB_CURRENTLEG_TRILOGY.md`,
`handoffs/HANDOFF_DELTA_B4_SKYRME_RELAXATION_2026-09-09.md`, `results/verify/lenr_energy_ledger.py`,
`GLOSSARY.md` (§6 current-leg, LENR).

*Do-not-cite Rossi / Mills / bio-transmutation. Baryon-conserving `d+d → ⁴He` only; `E_fm = 2.5 MeV` stays
retracted. No number here is fabricated; every quoted value is either from a mass table, computed in the
ledger script, or explicitly flagged `[open]`/`[inherited]`. ASCII apart from standard math symbols.*
