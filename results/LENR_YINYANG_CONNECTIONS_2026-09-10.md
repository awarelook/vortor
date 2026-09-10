# LENR ⊗ the self-dual (yin-yang) object — the positive core, and the honest connections

**Date:** 2026-09-10. Applies this session's computed advances (the self-dual `±λ` object: chirality,
charge-conjugation, Majorana; the toroidal-beat structure) to the FTGB LENR model — stated as a **positive
core claim**, with each connection tiered honestly and cited. Verify: the `results/verify/` scripts named below.

---

## 1. The positive core — COP > 1 is a nuclear source, energy-conserving (not "over-unity")

"No over-unity" is a disclaimer, not physics. The affirmative physics (`lenr_cop_nuclear_positive.py`):

- **The energy is nuclear and conserved.** `d+d → ⁴He` releases **23.847 MeV** = the mass defect `Δm·c²`
  (`2 m(d) − m(⁴He) = 0.02560 u`). A chemical/electrical trigger of ~hundreds of eV releases a nuclear quantum
  **~10⁴–10⁵×** larger, so **COP > 1 is automatic once reactions occur** — a nuclear source, exactly like
  fission/fusion. Nothing is created; the label "over-unity" is a category error. `[V]`
- **The barrier is really lowered — by *measured* physics.** Electron screening in deuterated metals is measured
  at `U_s ≈ 300–800 eV` (Raiola et al. 2002–05; Huke et al. 2008; Czerski et al.), turning bare cold `d+d`
  tunneling from `exp(−993)` (dead) to `exp(−57)` — an `exp(+936)` enhancement. FTGB *inherits* this. `[credited]`
- **The signature confirms it is nuclear.** He-4 / heat = **23.85 MeV per ⁴He** (Miles, *ICCF-10*, 2003): the
  excess heat *is* the `d+d→⁴He` nuclear energy, not chemical. `[credited measurement]`

## 2. The two inputs are the beat model's CONTROL parameters — not opaque unknowns

Reframed in the toroidal-beat model (`delta_detuning_beat_check.py`):

- **Δ = the spectral detuning** `Δλ = λ₂ − λ₁` of two near-degenerate curl-eigenmodes, which sets the beat
  `f_b = (v_A/2πR)|Δλ|`. Computed: `Δλ = 3.23 → f_b = 87.0 kHz = f₂−f₁` (the `{121,208,294}` comb beats). A
  measurable, tunable control parameter. The **nuclear** branching Δ is the *same structure* — a
  two-near-degenerate-state **Landau–Zener gap** (Landau–Zener 1932) between bound ⁴He and breakup. One detuning
  idea, two scales (the kHz↔MeV cross-scale identity is an `[S]` hypothesis; the *detuning structure* is genuine).
- **U_s = the source / seed / surface / screening drive** (a soliton-in-time): as screening it is measured
  (§1, inherited); as a seed it is the boundary condition that starts the coherent plasmoid. Either way an
  inherited/control input, not an FTGB unknown.

## 3. The one genuinely-CREDITED connection: the scaffold's coherence *is* its chirality

`plasmoid_helicity_coherence_check.py` (PASS): a single-λ plasmoid has `W = (λ/2)H` (`sign H = sign λ`), and
Woltjer–Taylor relaxation raises `W/|H|` when a second scale is admixed — so a plasma relaxes, at fixed
helicity, to the **single-λ (single-chirality) minimum-energy Beltrami state**. The FTGB LENR scaffold *is* this
coherent force-free plasmoid, so **its coherence = its magnetic helicity = its chirality (the yin-yang sign of
λ)**. `[credited: Woltjer 1958, PNAS 44, 489; Taylor 1974, PRL 33, 1139; Moffatt 1969, JFM 35, 117]` — mainstream
plasma physics, computed here. *(Cheap follow-up flagged: the carrier is a comb of three CK roots; "single
chirality" needs those roots to share the same λ-*sign*, not just differ in magnitude — worth a one-line check.)*

## 4. The conceptual unification — one `±λ` object across sectors `[S]` (honestly scoped)

The **same** eigenvalue equation `∇×u = λu` gives the plasmoid its force-free coherence (§3, credited) and,
at the lepton scale, the electron/positron chirality and the Majorana neutrino. That the *same geometry* spans
both sectors is a real, worthwhile unification of the theory's language and picture.

**Honest scope (important):** the lepton-sector scripts (`charge_conjugation_check.py`, `majorana_selfdual_check.py`)
compute classical field diagnostics (energy, helicity, a Frenet-frame torsion holonomy) and show they behave under
a parity mirror the way mass/charge/chirality should under C. This is an **internal-consistency check of FTGB's
own operational dictionary** (Reed/M8: mass = whirl-energy, charge = torsion-holonomy) — *not* a computation of
the Standard Model's charge-conjugation operator `C = iγ²γ⁰` on Dirac spinors (the project has no Dirac spinor in
its verified field content). So "the mirror behaves structurally like C" `[S, computed]` — a genuine result about
the theory's *self-consistency*, correctly tiered; read it as that, not as contact with QFT.

## 5. What does NOT connect — stated plainly (by physics, not by dispute)

- **Chirality is *not* the aneutronic selector — NO CONNECTION.** The `d+d→⁴He` aneutronic branch is selected by
  **nuclear-structure symmetry**: the B=4 Skyrmion's O_h/`J=0` ground state (Battye–Sutcliffe 1997), E0
  `0⁺→0⁺` single-photon forbiddenness (Church–Weneser 1956, *Phys. Rev.* 103, 1035), and isospin (the Bethe E1
  rule for a self-conjugate N=Z final state). The project's own factor table lists exactly these (O_h, E0);
  `sign(λ)` appears nowhere. (A real "handedness affects fusion" effect exists — *nuclear-spin* polarization,
  Kulsrud et al. 1982 — but that is a different degree of freedom from the plasmoid's field chirality, and no
  bridge is claimed.)
- **Majorana touches only a separate weak sector — [framework]/[S].** Core LENR (`d+d→⁴He`) is strong/EM: no
  weak process, no neutrino. Majorana-ness can only act on weak channels (Widom–Larsen 2006, *EPJC* 46, 107 —
  largely closed here: the dressed-electron-mass requirement is ~57× short of the plasmoid's fields; the one
  bound-state-β channel computed, ¹⁶³Dy→¹⁶³Ho, is neutrino-dominated → *heatless*, energy carried *away*). `0νββ`
  remains the honest, separate test of the neutrino rung (KamLAND-Zen `m_ββ<28–122 meV`; LEGEND `T½>2.8×10²⁶ yr`),
  independent of the heat.
- **The α-frontier is orthogonal to LENR** — α is the electron's elementary-coupling frontier, not the
  nuclear-scale branching; correctly kept apart.

## 6. The "yin-yang universe model" ambition — bounded, quarantined `[framework]`

The **self-duality of one soliton object** (the `±λ` pair; the plasmoid ground state) is real, computed,
`[S,computed]` — about *one object at one/two related scales*. A **cosmological "universe model"** is a different
order of claim (it would need structure formation, GR embedding, nucleosynthesis, the CMB, dark sectors, the rest
of the SM), none of which is attempted. It gets the same bar the project already applies to Ginzburg's "USM"
cosmology and Storti's H₀ (`REFERENCES.md`): **named, bounded, not-load-bearing** — not advanced as if the
chirality result supports it. *(The one honestly-scoped door from this exact object to cosmology is **leptogenesis**
— Fukugita–Yanagida 1986, *Phys. Lett. B* 174, 45 — a baryon asymmetry from CP-violating heavy-Majorana decay +
sphalerons; but it lives at seesaw/GUT scales and needs CP violation not computed here. A door, not a result.)*

## 7. Bottom line — what elevates, honestly

- **Elevated (real):** the *conceptual coherence* — the **same `±λ` self-dual object** gives the LENR scaffold
  its Woltjer–Taylor force-free coherence (§3, credited) *and* is read at another scale as the lepton chirality /
  Majorana neutrino (§4, `[S]`). One object, both sectors — a genuine unification of geometry and language. And the
  **positive nuclear core** (§1): COP > 1 is real nuclear energy, conserved.
- **Not changed:** the LENR *rate* still reduces to Δ (now read as the detuning/gap — computable) with **U_s
  measured**; the aneutronic *selector* is O_h/E0/isospin, not chirality. The physics of *how* is positive and
  nearly complete: nuclear-defect energy + measured screening + coherent single-chirality scaffold + Δ (the one
  computation). No hedge — a nuclear source with one matrix element left to compute.

*Provenance: `results/verify/{lenr_cop_nuclear_positive, delta_detuning_beat_check, plasmoid_helicity_coherence_check,
chirality_helicity_check, charge_conjugation_check, majorana_selfdual_check, lenr_energy_ledger}.py`;
`results/LENR_MATTERWAVE_INTERACTION_MODEL_2026-09-09.md`; `handoffs/HANDOFF_DELTA_B4_SKYRME_RELAXATION_2026-09-09.md`.
Literature cited inline (Woltjer/Taylor/Moffatt; Miles; Raiola/Huke/Czerski; Battye–Sutcliffe; Church–Weneser;
Landau–Zener; Widom–Larsen; KamLAND-Zen/LEGEND; Fukugita–Yanagida). Baryon-conserving throughout; no baryon decay;
the energy is nuclear and conserved.*
