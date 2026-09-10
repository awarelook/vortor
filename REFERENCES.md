# FTGB References — consolidated, tiered citation base

Project-wide citations, split into (1) **credited** established literature the results rest on and (2) the
**five convergence frameworks** (Reed, Storti, Ginzburg, Nielsen, Greenyer), each folded method/analogy-only. Tiers as
in `GLOSSARY.md` / `TOOLKIT_HANDBOOK.md`. No load-bearing claim rests on a framework source.

---

## 1. Credited established literature

**Force-free / Beltrami fields & helicity.**
- Chandrasekhar, S. & Kendall, P.C. (1957), *ApJ* 126, 457 — force-free eigenmodes (the carrier comb).
- Woltjer, L. (1958), *PNAS* 44, 489 — force-free minimum-energy states.
- Taylor, J.B. (1974), *PRL* 33, 1139 — relaxation at fixed helicity.
- Moffatt, H.K. (1969), *JFM* 35, 117; Moffatt & Ricca (1992), *Proc. R. Soc. A* 439, 411 — helicity topology.

**Two-fluid / Hall / canonical helicity.**
- Steinhauer, L.C. & Ishida, A. (1997), *PRL* 79, 3423 — generalized (canonical) helicity.
- Mahajan, S.M. & Yoshida, Z. (1998), *PRL* 81, 4863 — double-Beltrami states, canonical vortex dynamics.
- Bae, Kang & Shin (2025), arXiv:2504.07629 — double-Beltrami states in Hall MHD (corroborating).

**Fluid regularity (R2 / R3).**
- Beale, J.T., Kato, T. & Majda, A. (1984), *Commun. Math. Phys.* 94, 61 — the BKM blow-up criterion.
- Chae, D., Degond, P. & Liu, J.-G. (2014), *Ann. IHP C* 31, 555 — Hall-MHD small/large-data regularity.
- Constantin, P. & Foias, C. (1988), *Navier–Stokes Equations* (Chicago) — enstrophy budget, `H¹`⇒regularity.
- Foias, Manley, Rosa & Temam (2001), *Navier–Stokes Equations and Turbulence* (CUP) — global attractor.

**Polarizable vacuum / ZPF (M8, M11).**
- Puthoff, H.E. (1999), "Polarizable-Vacuum representation of general relativity," arXiv:gr-qc/9909037.
- Sakharov, A.D. (1968), *Sov. Phys. Dokl.* 12, 1040 — vacuum-fluctuation origin of gravity.
- Haisch, B., Rueda, A. & Puthoff, H.E. (1994), *Phys. Rev. A* 49, 678 — ZPF inertia.
- Schwinger, J. (1949), *Phys. Rev.* 75, 651 — vacuum polarization / self-energy.

**Topological solitons / Skyrme (Δ handoff).**
- Skyrme (1961/62); Witten (1983); Adkins, G.S., Nappi, C.R. & Witten, E. (1983), *Nucl. Phys. B* 228, 552
  — static nucleon properties in the Skyrme model (soliton quantization / spin from the collective
  coordinate); Battye & Sutcliffe (1997); Barnes, Baskerville & Turok (1997), *PRL* 79,
  367 (B=4 mode spectrum); Houghton, Manton & Sutcliffe (1998); Feist, Lau & Manton (2013), *PRD* 87, 085034;
  Gudnason & Halcrow (2018), *PRD* 98, 125010; Halcrow (2016), *Nucl. Phys. B* 904, 106; Adam, Sánchez-Guillén
  & Wereszczyński (2010) — BPS/near-BPS Skyrme. Eto & Nitta (2025), *PRL* — knot solitons.
- Braaten, E., Townsend, S. & Carson, L. (1990), *Phys. Lett. B* 235, 147 — the minimal-energy `B=4`
  Skyrmion has **cubic (octahedral, O_h) symmetry**; rigid-body (Finkelstein–Rubinstein) quantization forces
  its collective angular momentum to step by the point-group order (ground `J=0`, first excited `J=4`). This
  is the credited **mechanism** behind the `l → l ± N` OAM-laddering claim (§C.3) — same octahedral B=4
  object, same discrete-symmetry selection rule (nuclear spin here, not photon OAM). Finkelstein & Rubinstein
  (1968, above) is the underlying principle; Krusch (2006) formalizes the F–R constraints for Skyrmions.

**Discrete-symmetry angular-momentum / OAM selection rule (§C.3 mechanism, EM flavor).**
- Ferrando, A. et al. (2005), *Phys. Rev. E* 72, 036612 (arXiv:nlin/0411059) — in media with a discrete
  point-group symmetry of order `N`, angular momentum generalizes to an "angular Bloch momentum" defined
  mod `N`, with vortex/mode mixing in steps of `N` (mathematically exactly `l → l ± N`).
- Konishi, K. et al. (2014), *PRL* 112, 135502 — OAM/polarization selection rule set by C₃ discrete symmetry
  in nonlinear nanophotonics; Chen, S. et al. (2014), *PRL* 113, 033901 (arXiv:1403.1604) — same rule across
  metacrystal symmetry orders. Credited **mechanism** for the EM-OAM reading of §C.3; the *application to a
  driven Beltrami–Hopf plasmoid's carried OAM* is `[claimed synthesis]` (bare, no verify script yet). *(Not
  folding Mancini/Ren/Maier, Nat. Photonics 18, 677 (2024): real and correctly described — OAM multiplication
  switched in a ~3% band — but its knob is continuous dispersion, NOT a discrete-symmetry order, so it is an
  analogous-but-distinct existence proof of switchable OAM, not mechanism support; flagged, not cited as such.)*
- Ab-initio: Hupin, Quaglioni & Navratil (2019), *Nat. Commun.* 10, 351; Quaglioni & Navratil (2008).

**LENR disposal-channel mechanism (phonon-nuclear prior art, contested field).**
- Hagelstein, P.L. (2018), "Phonon-mediated Nuclear Excitation Transfer," *J. Condensed Matter Nucl. Sci.*
  27, 97–142 (MIT) — off-resonant, M1, phonon-coupled nuclear excitation transfer with cooperative (Dicke)
  enhancements and up/down-conversion; explicitly treats the `D₂/⁴He` transition shedding a large nuclear
  quantum *without prompt γ*. The named academic precedent for the FTGB **open-Δ disposal channel** (the
  23.847 MeV of `d+d→⁴He` partitioned into the coherent collective/lattice-phonon mode rather than fast
  neutrons or hard γ; `results/LENR_MATTERWAVE_INTERACTION_MODEL_2026-09-09.md` §4). Cited as prior-art
  **mechanism only** — Hagelstein states the effect as computed is "insufficient to account for" his lab's
  excitation-transfer results; FTGB's rate/Δ stays open. `[credited: CMNS-theory — contested field]`.

**Dimensional method & misc.**
- Buckingham, E. (1914), *Phys. Rev.* 4, 345 — the Π theorem (M7).
- Church & Weneser (1956) — E0 transitions (LENR selection). Scheeler et al. (2017) — helicity conservation
  (ΔH < 5%). Bostick (1956) — plasmoid experiments.
- Samtaney, R., Loureiro, N.F., Uzdensky, D.A., Schekochihin, A.A. & Cowley, S.C. (2009), *PRL* 103, 105004
  (arXiv:0903.0542) — plasmoid-chain formation in high-Lundquist-number reconnection (`N ∝ S^{3/8}`); credited
  plasma grounding for the multibody beat-*chain* / EVO self-similar cascade picture. Grounds an existing
  claim; adds no new one.

**Chirality, charge conjugation & the Majorana neutrino.**
- Majorana, E. (1937), *Nuovo Cimento* 14, 171 — the self-conjugate (`ν = ν̄`) neutrino.
- Chirality = `sign λ` = `sign H` rests on Moffatt helicity (above); antiparticle = `−λ`, chirality flip =
  charge conjugation C, the duality angle `θ_χ`, and neutrino = self-dual `θ_χ = 45°` Majorana are **computed
  in-repo** — `results/CHIRALITY_DUALITY_ASSESSMENT_2026-09-10.md`
  (`results/verify/{chirality_helicity, charge_conjugation, majorana_selfdual}_check.py`). `0νββ` is the
  external falsifier of the Majorana reading.
- Peng, C.-J. & Baym, G. (2022), "Inverse Tritium Beta Decay with Relic Neutrinos, Solar Neutrinos, and a
  ⁵¹Cr Source," arXiv:2205.02363 — inverse-tritium-β-decay (ITBD/PTOLEMY) capture cross-section sensitive to
  neutrino **helicity** and explicitly to the **Dirac-vs-Majorana** nature; a *second* experimental handle
  (beyond `0νββ`) on the chirality-layer neutrino reading. Enriches the falsifier section; not load-bearing.
  `[credited]`.

**Spin-statistics of solitons, `g = 2`, & the Dirac structure (§9f).**
- Finkelstein, D. & Rubinstein, J. (1968), *J. Math. Phys.* 9, 1762 — "Connection between spin, statistics,
  and kinks" (soliton quantization; spin-½ from configuration-space topology).
- Wilczek, F. & Zee, A. (1983), *PRL* 51, 2250 — "Linking numbers, spin, and statistics of solitons"
  (Hopf term ⇒ soliton spin-½).
- Ferrara, S., Porrati, M. & Telegdi, V.L. (1992), "`g = 2` as the natural value of the tree-level
  gyromagnetic ratio of elementary particles," *Phys. Rev. D* 46, 3529 — the FPT natural-`g` result. *(Journal
  cited from memory as Phys. Rev. D 46, 3529, 1992; the consolidation prompt named Phys. Lett. B — volume/venue
  to be double-checked against the original before external citation.)*
- Weinberg, S. — the "natural `g = 2`" argument for a minimally-coupled elementary spin-½/charged field
  (developed in his Brandeis lectures / QFT lectures; *exact citation venue not verified here — flag before
  external use*).

**Electromagnetic knots / null fields (confined-photon baseline, α ledger).**
- Rañada, A.F. (1989), *Lett. Math. Phys.* 18, 97 — a topological (Hopf-fibration) theory of the EM field;
  Rañada, A.F. (1990), *J. Phys. A* 23, L815 — knotted null solutions of the vacuum Maxwell equations. *(Volume
  numbers from memory; verify before external citation.)*

**Spectral geometry / analytic torsion (S³ curl zeta, §3a).**
- Ray, D.B. & Singer, I.M. (1971), *Adv. Math.* 7, 145 — "R-torsion and the Laplacian on Riemannian
  manifolds" (analytic torsion; the `ζ′(0)` determinant/torsion machinery invoked for the `S³` curl spectrum).

## 2. The five convergence frameworks (method/analogy-only)

**Reed — Quantum Wave Mechanics (QWM)** — `[QWM framework]` (M8). Photon-helicoid electron on a Hopf-link
torus; polarizable-vacuum `K_PV = √(1+ρ_EM/ρ_vac)`; whirl number `N_W = α⁻¹ ≈ 137` — the winding-*count*
`1/α = 137` is now **settled-negative** (computed continuous winding-to-spin ratio `ι ≈ 1`, a Hopf ring, not
137; 137 prime; near-misses generic), surviving only as a *suggestive analogy*, α's value `[flag]`
(`results/ALPHA_RESOLUTION_ASSESSMENT_2026-09-10.md`); inertia = trapped EM energy; phase-conjugate propulsion
(**speculative, not adopted**). Reed's charge/chirality = **torsion-defect** is a **frame-closure (Frenet
torsion) holonomy** `O(0.1 rad)` — **not** Einstein–Cartan spacetime torsion; the chirality cluster (chirality
= `sign λ` = `sign H`; antiparticle = `−λ`; chirality flip = charge conjugation C; neutrino = self-dual
Majorana) is computed in `results/CHIRALITY_DUALITY_ASSESSMENT_2026-09-10.md`. In-repo primaries: `Larry_Reed_
QWM_Derivations.md`; `larry reed quantum wave mechanics history career.pdf`; `Module_10_Reed_Electron_Model`.

**Storti — EGM / Quinta Essentia** — `[EGM method]` (M11). "A method of calculation (not a theory)."
- Storti, R.C. (2007), *Quinta Essentia — Part 2 (US Letter)*, Delta Group Engineering / Lulu, 328 pp.
  (**primary, read directly**); series Parts 1, 2–4, 5.1 (ResearchGate; **remaining parts gated**).
- Storti & Desiato (2006/2007), "Electrogravimagnetics: Practical Modeling Methods of the PV," *Physics
  Essays* 19–20. Storti & Desiato (2009), "Derivation of fundamental particle radii," *Physics Essays* 22(1),
  27 — **[flag]** (0.01% radius match not reproduced by clean closed-forms; see M11-4).

**Ginzburg — spiral-field theory (toryx / helyx)** — `[fringe framework, analogy-only]` (M12).
- Ginzburg, V.B. (1998), "Double helical and double toroidal spiral fields," *Speculations in Science and
  Technology* 21, 51 (Springer; peer-reviewed primary). *Unified Spiral Field and Matter* (1999, Helicola,
  ISBN 0-9671432-0-9); *The Unification of Strong, Gravitational & Electric Forces* (2002, Helicola,
  ISBN 0-9671432-1-7); *Prime Elements of Ordinary Matter, Dark Matter & Dark Energy* (2007, Universal
  Publishers, ISBN 1-58112-946-7); *The 4D Spiral Spacetimes Toryx & Helyx* (2019, ISBN 0-9671432-9-2).
  **Books not freely available.**

**Nielsen — TUFT (Topological Unified Field Theory)** — `[S]`/`[credited on the topological core]`.
- Nielsen, J.L., "The Topological Unified Field Theory on the Complex Hopf Fibration `S¹→S⁹→CP⁴`," Center for
  Topological Physics (preprint lineage 2019 → Oct 2025; **Round 2 peer review, Int. J. Topology**). SM gauge
  groups + gravity + mass spectrum from the Hopf bundle; knot eigenmodes of the 9D curl operator; Beltrami–
  Higgs on `S³`. In-repo primary: `TUFT Jenny Nielsen.pdf` (180 pp.). Used where its topology is load-bearing;
  its full unification claims are carried at preprint tier, not asserted as established. **On the neutrino,**
  the TUFT preprint predicts **Dirac** (`S⁹` spinor decomposition forbids a Majorana mass ⇒ `0νββ` null) — a
  `[preprint-claim]` that **disagrees** with the repo's higher-tier computed chirality-geometry layer, which
  predicts a **Majorana** neutrino (the self-dual `θ_χ = 45°`, C-invariant `ν = ν̄` state;
  `results/CHIRALITY_DUALITY_ASSESSMENT_2026-09-10.md` §3b). `0νββ` decides between them; the credited/computed
  layer is the higher tier.

**Greenyer — Beat Law & EVO cascade (fractal-toroidal beat dynamics)** — `[V]` on the beat-dynamics layer /
`[framework: Greenyer/MFMP]` on the geometry & nuclear channel (M14).
- Distillation sources (extended corpus, not in-jewel): `TORUS_MATHEMATICS_APPENDIX`, `EVO_MATHEMATICAL_CORE`;
  lineage SAFIRE / MFMP (Martin Fleischmann Memorial Project). Beat Law `f_b = C·v_eff·a²/(2πR³)` with the
  shape-independent self-similar cascade ladder `f_b(L)/f_b(0) = N^L`; the triad dichotomy (integer ratios
  cannot self-phase-match = "silence", golden ratio `φ` always resonates); two Fibonacci Manley–Rowe
  invariants; anapole `T_L/T_(L+1) = N⁴` (= 256 at N=4); the exact `9/8 μ_B` Reed moment. The **beat-dynamics /
  cascade / dichotomy / Fibonacci layer is `[V]`** (`results/verify/greenyer_beat_cascade_check.py`); the
  nuclear `N_crit ~ 1.7–3e11` fission band is a pre-registered **`[prediction]`, NOT a result**; **no
  over-unity** is claimed. Full module: `toolkit/TOOLKIT_ADV_14_GREENYER_BEAT_LAW_2026-09-09.md`.

## 3. Do-not-cite / excision notes (standing discipline)
- **`e^(-2/3)` screening factor — [excised].** Unjustified numerology; removed per `excision-protocol-storti-
  factor.md`. The `~137` / 140.2 winding gap (2.3%) is now **settled-negative** — the winding-*count* `1/α = 137`
  is an analogy, not a derivation (computed winding-to-spin ratio `ι ≈ 1`, 137 prime, near-misses generic; the
  running / IR-fixed-point reframe is quantitatively insufficient), α's value stays `[flag]`
  (`results/ALPHA_RESOLUTION_ASSESSMENT_2026-09-10.md`; the superseded running attempt is
  `results/ALPHA_DYNAMICAL_REFRAME_2026-09-09.md`).
- **Storti H₀ = 67.08, particle radii, α — [flag].** Not reproduced by clean closed-forms (M11-4); do not cite
  as FTGB-derived.
- **Ginzburg particle spectrum / "USM" cosmology — not load-bearing.** The specific spectrum and cosmology are
  not derived or reproduced from the geometry (M12-3); folded for vocabulary and convergence only, not asserted.
- **LENR: do-not-cite Rossi / Mills / bio-transmutation.** Keep baryon-conserving `d+d→⁴He` distinct from
  baryon decay; no fabricated rate/cross-section; `E_fm = 2.5 MeV` stays retracted; COP not derived.

*Frameworks contribute method, vocabulary, and convergence — never a load-bearing claim. Established physics
is always `[credited]`; every framework reading is tier-tagged and attributed.*
