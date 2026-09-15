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
  & Wereszczyński (2010) — BPS/near-BPS Skyrme. Eto & Nitta (2025), *PRL* — knot solitons
  `[incomplete: vol/page missing — complete before external use]`.
  *(Audit note 2026-09-14: the PRL 79, 367 attribution for the B=4 mode spectrum was CHALLENGED by an
  audit pass (proposing a swap with the B=2 deuteron paper) and VERIFIED CORRECT against the original —
  hep-th/9704012 "Normal Modes of the B=4 Skyrme Soliton" IS PRL 79, 367 (1997). Kept; challenge logged.)*
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
  metacrystal symmetry orders. This point-group mechanism is computed in-repo — `results/verify/
  octahedral_oam_ladder_check.py` (`[V]`): the ladder step is *exactly* `N`, and the `SO(3)→O` subduction
  forces `l ∈ {0,4,6,8,9,10,…}`, `Δl=4`, reproducing the credited B=4 Skyrmion spectrum. **This applies at
  the composite B=4 *nuclear* rung only** (`N=4`, a genuinely octahedral 4-baryon Skyrmion). It does **not**
  describe the theory's localized **EM object** — see the resolution below. *(Not folding Mancini/Ren/Maier,
  Nat. Photonics 18, 677 (2024): real and correctly described — OAM multiplication switched in a ~3% band —
  but its knob is continuous dispersion, NOT a discrete-symmetry order; flagged, not cited as mechanism support.)*

**The EM matter resonator's angular momentum: anapole + fractal cascade, via Reeb & spectral geometry (§C.3).**
- **Resolution (`results/verify/oam_toroidal_resonator_resolution_check.py`).** The theory's localized EM
  object is the fractal-toroidal matter resonator (electron/neutrino/EVO), **not** a spheromak — and it has
  **no** point-group OAM ladder `l→l±N`. It is (i) an **anapole** (Zel'dovich toroidal dipole; ordinary
  radiating dipole cancels to `~1e-16`, so it is nonradiating — the "OAM ladder" question is ill-posed);
  (ii) a **self-similar fractal cascade** (anapole *type* fractal-invariant; strength `~N^p` per level —
  `N^3` fixed-current / `N^4` twin-core, M14-6); (iii) topologically protected — spectrum `λ_L = λ_0 N^L`,
  continuous helicity `~N^{-4L}`, integer winding (Hopf/Reeb-orbit linking) exactly conserved (`Lk=Tw+Wr`).
  *(This supersedes an earlier point-group analysis — the space-filling ABC field and the spherical spheromak
  as proxies gave `N=3`/axisymmetric; both were the wrong geometry for the localized toroidal object.)*
- Etnyre, J.B. & Ghrist, R. (2000), *Nonlinearity* 13, 441 — a Beltrami field is (up to reparametrization)
  the **Reeb field of a contact structure**; the correct geometric frame for the toroidal resonator (already
  `[credited]` in the synthesis §A). Spectral-geometry side: the CK spectrum + cascade `λ_L = λ_0 N^L`
  (§3, M14) and the `S³` curl spectral zeta / Ray-Singer torsion (M13, `curl_spectral_zeta_pi_power_check.py`).
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
- Rañada, A.F. (1989), *Lett. Math. Phys.* **18**, 97–106 (DOI 10.1007/BF00401864) — a topological
  (Hopf-fibration) theory of the EM field; Rañada, A.F. (1990), *J. Phys. A: Math. Gen.* **23**, L815–L820
  (DOI 10.1088/0305-4470/23/16/007) — knotted null solutions of the vacuum Maxwell equations. *(Volumes/pages
  verified 2026-09-10.)*

**Spectral geometry / analytic torsion (S³ curl zeta, §3a).**
- Ray, D.B. & Singer, I.M. (1971), *Adv. Math.* 7, 145 — "R-torsion and the Laplacian on Riemannian
  manifolds" (analytic torsion; the `ζ′(0)` determinant/torsion machinery invoked for the `S³` curl spectrum).

**Anapole / toroidal-dipole electrodynamics (§C.3 nonradiating resonator).**
- Kaelberer, T., Fedotov, V.A., Papasimakis, N., Tsai, D.P. & Zheludev, N.I. (2010), *Science* **330**, 1510
  (DOI 10.1126/science.1197172) — first direct observation of a resonant **toroidal dipole**, a multipole
  family distinct from electric/magnetic. Papasimakis, N., Fedotov, V.A., Savinov, V., Raybould, T.A. &
  Zheludev, N.I. (2016), *Nat. Mater.* **15**, 263 (DOI 10.1038/nmat4563) — the authoritative **anapole**
  review (nonradiating electric+toroidal-dipole interference). The modern experimental anchor for the §C.3
  anapole reading (ordinary dipole cancels ~1e-16); complements Zel'dovich 1957. `[credited]`.

**Beltrami fields carry knots/links (topology core, M15/M14-6).**
- Enciso, A. & Peralta-Salas, D. (2012), *Ann. of Math.* **175**, 345 (arXiv:1003.3122) — *any* link is realized
  by closed field lines of a Beltrami field: knottedness of force-free fields is a theorem. The stronger
  companion to Taubes' single-orbit existence, underpinning the Hopf-linking / `Lk=Tw+Wr` core. `[credited]`.
- Cardona, R., Miranda, E., Peralta-Salas, D. & Presas, F. (2021), *PNAS* **118**, e2026818118; (2023),
  *Adv. Math.* **428**, 109142 — Etnyre-Ghrist-based universality of Beltrami/Reeb flows (Turing-complete
  Euler flows; flexible Reeb embeddings). Deepen the §A.2.1/M15 contact frame. `[credited]` / `[S]` relevance.
  *(UNVERIFIED vol/page — verify before external use: Enciso-Peralta-Salas (2015), *Acta Math.* **214**, 61
  (knotted vortex tubes); Cieliebak & Volkov (2015), *JEMS* **17**, 321 (stable Hamiltonian structures);
  Ginzburg, V.L. (2005), Weinstein-conjecture survey, *Progr. Math.* **232**.)*

**Force-free / two-fluid companions (§1/§4/§4a).**
- Chandrasekhar, S. & Woltjer, L. (1958), *PNAS* **44**, 285 (DOI 10.1073/pnas.44.4.285) — force-free
  minimum-dissipation states (companion to the already-cited Woltjer 44, 489). Yoshida, Z. & Mahajan, S.M.
  (2002), *PRL* **88**, 095001 (DOI 10.1103/PhysRevLett.88.095001) — the coercive **canonical-enstrophy
  variational principle** whose relaxed states are double-Beltrami; the credited anchor §4a generalizes.
- Bellan, P.M. (2000), *Spheromaks* (Imperial College Press, ISBN 978-1-86094-141-2) — the standard force-free
  spheromak monograph (helicity, Taylor relaxation, the `tan x = x` ball eigenvalue). Loureiro, N.F. &
  Uzdensky, D.A. (2016), *Plasma Phys. Control. Fusion* **58**, 014021 — the plasmoid-chain review behind the
  EVO multibody-cascade grounding (companion to the cited Samtaney et al. 2009). `[credited]`.

**Hydrodynamic QM & topological-soliton experiments (§9 dual reading, §C).**
- Madelung, E. (1927), *Z. Phys.* **40**, 322 (DOI 10.1007/BF01400372) — the Schrödinger↔fluid (Madelung)
  equivalence. Bohm, D. (1952), *Phys. Rev.* **85**, 166 & 180 — the causal/quantum-potential reading. The
  primary sources for the field↔matter-wave convergence the §9 dual reading *instantiates*. `[credited-convergence]`.
- Structural analogues (fold as `[S]`, not load-bearing): Barceló, C., Liberati, S. & Visser, M. (2005),
  *Living Rev. Relativ.* **8**, 12 — analogue gravity / effective metric (keep firewall; route any promotion
  through the analogue-prior-art-verifier). Kleckner, D. & Irvine, W.T.M. (2013), *Nat. Phys.* **9**, 253 —
  lab creation of knotted vortices. Ackerman, P.J. & Smalyukh, I.I. (2017), *Nat. Mater.* **16**, 426 — static
  hopfions (`Q_H`-charged particle-like solitons). Nagaosa, N. & Tokura, Y. (2013), *Nat. Nanotechnol.* **8**,
  899 — magnetic skyrmions (topological protection, emergent EM). Empirical support that topological solitons
  are physical — in fluid/condensed-matter media, not the FTGB EM object itself. `[credited]` / `[S]` mapping.

---

### 1e–1j. Corpus-salvage clusters (2026-09-13)

*Salvaged from the Arc vault (science track only) and the ckfreefem corpus citation stores. The full
verification-tagged records are vendored frozen in `frontier_calcs/` (`REFERENCES_VERIFIED_LEDGER_2026-08-28.md`,
~198 rows `[V]`/`[T]`/`[P]`-tagged; `PAPER_PREP_CITATIONS_2026-09-01.md` with 4 bibliographic corrections;
`greenyer_61_entry_catalog_slice.md` for M14). Below is the curated fold — items that ground claims the jewel
already makes. `[real-checkable]` = venue+year verified in those stores; `[cited, unverified]` = carried with
its source flag. Companion history/people roster: `HISTORY_PEOPLE_EVO_CMNS.md`.*

**1e. Chandrasekhar–Kendall photon / Beltrami prior art (directly on the jewel's core).**
- Moses, H.E. (1971), *SIAM J. Appl. Math.* **21**, 114 — eigenfunctions of the curl operator (the CK basis
  as a general decomposition). Yoshida, Z. & Giga, Y. (1990), *Math. Z.* **204**, 235 — self-adjointness and
  spectrum of curl. Lakhtakia, A. (1994), *Czech. J. Phys.* **44**, 89 — Trkal/Beltrami history. Marsh, G.E.
  (1996), *Force-Free Magnetic Fields* (World Scientific) — the standard monograph. `[credited]`.
- **Tuchin, K. (2016), *Phys. Rev. C* 93, 054903** — the EM field quantized in the CK basis inside a plasma;
  **Xia, Y., Qin, H. & Wang, W. (2016), *Phys. Rev. D* 94, 054042** — chiral-plasma route to the CK-wave
  state. Direct prior art for "the photon in the medium lives on the CK/Beltrami basis." `[credited]`.
- Hall-MHD **wave topology**: Fu, Y. & Qin, H. (2024), *Phys. Rev. Res.* **6**, 023273 — Weyl point in Hall
  MHD; Mesa Dame, Palmerduca, Fu & Qin (2025), arXiv:2506.18830 — HMHD spectrum homotopic to ideal MHD,
  Chern numbers `C± = ±1`, **circularly-polarized Beltrami modes as limiting cases of the shear-Alfvén-Hall
  branch**. Modern topological-wave frame for the jewel's Hall-MHD + Chern (`C=±2` photon) threads. `[credited]`.
- Zanca, P. & Terranova, D. (2004), *Plasma Phys. Control. Fusion* **46**, 1115 — the external
  order-of-magnitude validity anchor used for the finite-ε `c_CK` pipeline (`freefem/`, corpus MVVC ledger). `[credited]`.

**1f. Ball lightning & laboratory plasmoids (the object's observational family).**
- Hill, M.J.M. (1894), *Phil. Trans. R. Soc. A* **185** — the spherical vortex (the exact toroidal
  equilibrium prototype). Kapitza, P.L. (1955) — microwave-resonance ball-lightning theory. Bostick, W.H.
  (1956), *Phys. Rev.* — "plasmoid" coined (already in LINEAGE). `[credited]`.
- Rañada, A.F. & Trueba, J.L. (1996), *Nature* **383**, 32 — "Ball lightning an electromagnetic knot?";
  Rañada, Soler & Trueba (2000), *Phys. Rev. E* **62**, 7181 — the Hopf-knot ball-lightning model (topological
  protection). The BL companions to the already-cited Rañada 1989/1990 EM knots. `[credited]`.
- **Cen, J., Yuan, P. & Xue, S. (2014), *Phys. Rev. Lett.* 112, 035001** — the first recorded optical
  spectrum of natural ball lightning (Si/Fe/Ca lines — soil elements; supports combustion/plasmoid readings).
  Peacock, N.J. & Norton, B.A. (1975), *Phys. Rev. A* **11**, 2142 — the measured MG-scale DPF field.
  Abrahamson, J. & Dinniss, J. (2000), *Nature* **403**, 519 — silicon-combustion BL precedent (the
  sustaining-power closure used in the corpus's dynamical-plasmoid work). Stenhoff, M. (1999), *Ball
  Lightning* (Kluwer) — the standard observational monograph. `[credited]`.
- Jennison, R.C. & Drinkwater, A.J. (1977), *J. Phys. A* **10** — phase-locked-cavity model (inertia of a
  trapped standing wave) + Jennison's in-cabin BL observation; a genuine precedent for "mass = trapped
  oscillation." Davis, E.W. (2002), AFRL-PR-ED-TR-2002-0039 — the AFRL ball-lightning literature survey
  (adopts Nachamkin force-free + Rañada topological models; **cited as a literature survey only** — the same
  author's teleportation-study speculation is excluded). Egorov & Stepanov (2002) reproducible lab BL
  `[cited, unverified venue]`. `[credited]` / noted.
- Spheromak stability anchors: Rosenbluth, M.N. & Bussac, M.N. (1979), *Nucl. Fusion* **19**, 489; Bondeson
  et al. (1981), *Phys. Fluids* **24**, 1682; Belova et al. (2000), *Phys. Plasmas* **7**, 4996. `[credited]`.

**1g. LENR / CMNS experimental record (contested field — cited as the record, not as settled).**
*The jewel's standing rule: energy accounting `[V]`, mechanism `[S]`, rate open; "consistent with a contested
anomaly," never "confirmed." These are the field's primary measurements + the honest negative.*
- Fleischmann, M. & Pons, S. (1989), *J. Electroanal. Chem.* **261**, 301 — the original excess-heat claim.
  **Miles, M.H. et al. (1993), *J. Electroanal. Chem.* 346, 99** — the He-4/excess-heat correlation (the
  measurement the jewel already leans on, now formally cited); Miles et al. (2000), *J. Electroanal. Chem.*
  **482**, 56 — `23±5 MeV`/⁴He calorimetry. McKubre, M.C.H. et al. — the loading-threshold record
  (`D/Pd ≳ 0.85–0.88` necessary-not-sufficient; ICCF-4 1994; *JCMNS* **15**, 137 (2015)). `[credited-measurement,
  contested field]`.
- Hagelstein, P.L., Letts, D. & Cravens, D. (2010), *JCMNS* **3**, 59 — the two-laser THz difference-frequency
  result (the field's key spectral anchor; relevant to any comb/beat reading). Iwamura, Y. et al. (2002),
  *Jpn. J. Appl. Phys.* **41**, 4642 — Cs→Pr permeation transmutation (+ Toyota 2013 replication). Szpak, S.
  & Mosier-Boss, P.A. — SPAWAR co-deposition morphology (*Naturwissenschaften* 2009) — **co-occurrence, not
  mechanism** (the corpus's own reading; NRL found "striking differences" vs neutron-exposed CR-39). `[credited-measurement, contested]`.
- Screening: Kasagi, J. et al. (2000) — the screening anomaly; Huke, A., Czerski, K. et al. (2008), *Phys.
  Rev. C* **78**, 015803; Czerski, K. (2022), *Phys. Rev. C*; Dubey et al. (2025), *Phys. Rev. X* `[cited
  in-corpus; verify before external use]`. The measured `U_s` the jewel's LENR module inherits. `[credited]`.
- **The honest negative: Berlinguette, C.P. et al. (2019), *Nature* 570, 45** — the Google-funded
  multi-lab null (no excess heat under controlled conditions at the loadings reached). Cited alongside the
  positives; the field's reproducibility statistics (50% null / 500% variability on identical samples, per
  the DoD 16-F-1333 briefing digest) ride with every positive claim. `[credited-negative]`.
- Storms, E. (2010), *Naturwissenschaften* **97**, 861 — the field review. Benyo, T. & Steinetz, B. et al.
  (2020), *Phys. Rev. C* **101**, 054604 — NASA lattice-confinement fusion (2.45 MeV D-D neutrons,
  gamma-driven): **real screened-fusion physics, a different mechanism — not an F-P confirmation**. Widom, A.
  & Larsen, L. (2006), *Eur. Phys. J. C* **46**, 107 — the ULM-neutron theory, cited AND **ruled out three
  independent ways in the corpus** (`11_verified_ark/helium_heat_nuclear_extensions`) — carried as a
  checked-and-closed alternative. Klimov, A. et al. (2016), *JCMNS* **19**, 67 — the Plasma Vortex Reactor
  43–46 kHz window + COP claims (**unreplicated outside his group; field journal**) — the source of the
  "43 kHz" clue in `COINCIDENCE_LEDGER.md`. `[credited]` / `[flag]` as marked.
- Strange radiation (fenced chain): Urutskoev, L.I. et al. (2002), *Ann. Fond. L. de Broglie* **27** —
  anomalous CR-39 tracks; Ivoilov, N.G. (2006), *Ann. Fond. L. de Broglie* **31**, 115; Fredericks, K.A.
  (2015), *JCMNS* **15**, 203; theory reading: Lochak, G. (2007), *Z. Naturforsch. A* **62**, 231 (leptonic
  monopole). **Phenomenon unrecognized by mainstream nuclear physics** — logged as contested observations
  with provenance, never as support. Rukhadze & Grachev (2017), *RENSIT* **9**(1) — the Russian-program
  history (incl. Filimonenko 1957/1962 priority claims, which rest on retrospective literature). `[contested-observation]` / `[framework]`.

**1h. Charged-drop fissility (the corpus's EVO-fissility backbone; do-not-merge pair flagged).**
- Rayleigh (1882), *Philos. Mag.* **14**, 184 — the charged-drop stability limit; Bohr, N. & Wheeler, J.A.
  (1939), *Phys. Rev.* **56**, 426 — the fissility parameter; Wong, C.-Y. (1973), *Ann. Phys.* **77**, 279 —
  toroidal nuclei. Duft, D. et al. (2002), *Phys. Rev. Lett.* **89**, 084503 **and** Duft, D. et al. (2003),
  *Nature* **421**, 128 — Rayleigh jets from levitated microdroplets (**two distinct papers — do not merge**,
  per the vendored citation store). Hill, R.J.A. & Eaves, L. (2012), *Appl. Phys. Lett.* **100**, 114106;
  Liao, L. & Hill, R.J.A. (2017), *Phys. Rev. Lett.* **119**, 114501 — charged-drop fission experiments. `[credited]`.

**1i. Dissipative time crystals (the driven-limit-cycle "heartbeat" family).**
- Kongkhambut, P. et al. (2022), *Science* **377**, 670 — observation of a continuous dissipative time
  crystal; Wu, J. et al. (2024), *Nat. Phys.* **20**, 1389; Liu, T. et al. (2025), *Nat. Commun.* **16**,
  1419. The experimental family the Stuart–Landau "heartbeat" (driven, dissipative, self-organized period)
  structurally belongs to — companions to the already-cited Cosme 2025. `[credited]` / `[S]` mapping.

**1j. Magnetic monopole searches & the electroweak monopole (fenced frontier).**
- MoEDAL Collaboration (2022), *Nature* **602**, 63 (**corrected citation** — not 604/64) — monopole search
  in heavy-ion collisions; MoEDAL (2024), *Phys. Rev. Lett.* **133**, 071803. Milton, K.A. (2006), *Rep.
  Prog. Phys.* **69**, 1637 — the monopole-status review. Cho, Y.M. & Maison, D. (1997), *Phys. Lett. B*
  **391**, 360 — the electroweak monopole (the corpus's from-scratch BVP solve is vendored:
  `frontier_calcs/cho_maison_real_monopole_solve.py`). **The corpus's six-angle monopole program is
  settled-NEGATIVE** for connecting the toroidal geometry to monopole physics — decisively: the Hopf
  invariant classifies `π₃(S²)`, monopole charge classifies `π₂(S²)` — **different invariants of different
  maps** (`11_verified_ark/topological_monopole_program`). Kept as a computed closure. `[credited]` /
  settled-negative.

**1k. LENR active-site & disposal physics (§ the anapole dipole-balance mechanism, 2026-09-14).**
*Grounding the `[S]` active-site synthesis (`results/LENR_ACTIVE_SITE_SYNTHESIS_2026-09-14.md`,
`results/verify/lenr_disposal_channel_check.py`). Credited-vs-novel verdicts independently checked by an
adversarial prior-art pass. The mechanism is `[S]`; the energy accounting `[V]`; the rate open.*
- **The E0 selection rule** (the crux): Church, E.L. & Weneser, J. (1956), *Phys. Rev.* **103**, 1035 — a
  single real photon cannot mediate a `0⁺→0⁺` transition (no `L=0` photon) — the credited nuclear-structure
  reason an aneutronic ⁴He channel must shed its 23.85 MeV **collectively**. `[credited]`.
- **The measured ~1e-7 aneutronic baseline** (the bar the open problem is defined against): Wilkinson, F.J.
  III & Cecil, F.E. (1985), *Phys. Rev. C* **31**, 2036 — `D(d,γ)⁴He` at low energy: the radiative-capture
  branch is ~seven orders of magnitude below the nucleon channels. `[credited — resolves the vendored
  ledger's "verify vol/page at lock" flag, 2026-09-14]`.
- **Spin-polarized fusion** (context for the spin/orientation gate, `spin_channel_gate_check.py`):
  Kulsrud, R.M., Furth, H.P., Valeo, E.J. & Goldhaber, M. (1982), *Phys. Rev. Lett.* **49**, 1248 —
  fusion-reactivity control by nuclear spin polarization (d-t). The **d+d "quintet suppression"**
  question (whether the S=2 channel of d+d is dynamically suppressed) is a NAMED, CONTESTED few-body
  issue (Paetz gen Schieck and collaborators) `[context — complete the specific citation before external
  use]`. FTGB's addition is the coherent-site, preparation-steered version (singlet gate 1/9 → 1/3 at
  m=0, → 0 at m=±1), minted as falsifier #9. `[credited]`-arith / `[S]` identification.
- **Ponderomotive (Miller) force**: Gaponov, A.V. & Miller, M.A. (1958), *Sov. Phys. JETP* **7**, 168
  (*ZhETF* **34**, 242) — `U_p = q²⟨E²⟩/4mω²`; real, but `∝1/m` (electron-mediated) and the non-relativistic
  form fails at `a₀~1` (Quesnel & Mora (1998), *Phys. Rev. E* **58**, 3719). Tajima, T. & Dawson, J.M.
  (1979), *Phys. Rev. Lett.* **43**, 267 — ponderomotive longitudinal-wakefield acceleration. `[credited]`
  (as the force/small-parameter regime; a *fast disposal-rate* role is settled-negative — kinematic wall).
- **Phase conjugation / time reversal**: Zel'dovich, B.Ya. et al. (1972), *JETP Lett.* **15**, 109 (SBS
  wavefront reversal); Yariv, A. & Pepper, D.M. (1977), *Opt. Lett.* **1**, 16 (DFWM, `R=tan²|κ|L` — any
  `R>1` is **pump** energy); Fink, M. (1997), *Phys. Today* **50**(3), 34 (acoustic time-reversal mirror).
  `[credited]` as *refocusing*; the "amplifies from nothing" reading is settled-negative (adds no coupling).
- **Coherent nuclear disposal (prior-art mechanism, contested)**: Hagelstein, P.L. (2018), *JCMNS* **27**, 97
  (phonon-mediated nuclear excitation transfer); Preparata, G. (1991), *Nuovo Cimento A* **104**, 1259, and
  *QED Coherence in Matter* (World Scientific, 1995) — a **distinct** coherent-domain tradition, cited as
  role-**analogue**, not identity; Dicke, R.H. (1954), *Phys. Rev.* **93**, 99 (superradiance — an
  atomic/photonic result, extrapolated to nuclear quanta, not a direct match). The direct phonon-coupling
  **rate** is settled-negative by ~66 orders (`corpus_settled_negatives_check.py`). `[contested]`/`[credited]`.
- **Bound-state β/EC transmutation trigger** (baryon-conserving, ionization-gated): Bosch, F. et al. (1996),
  *Phys. Rev. Lett.* **77**, 5190 (`¹⁸⁷Re` bound-state β, ~1e9× faster fully-ionized); Jung, M. et al.
  (1992), *Phys. Rev. Lett.* **69**, 2164 (`¹⁶³Dy` stable→47-day, ionized). The credited basis of the
  falsifiable `¹⁶³Dy→¹⁶³Ho` X-ray charge-state prediction. `[credited]` (mechanism) / `[S]` (the FTGB trigger).
- **The historical acceleration analogue**: Cockcroft, J.D. & Walton, E.T.S. (1932), *Nature* **129**, 649 —
  the first artificial nuclear disintegration (`⁷Li+p→2⁴He`) by an accelerated longitudinal field; cited as a
  *role*-analogue (a longitudinal field triggers a nuclear channel), **not** a scale identity. `[credited]`.
- **Impedance-matched open cavity** (the "open-fed" substrate): Haus, H.A. (1984), *Waves and Fields in
  Optoelectronics* (critical coupling = impedance matching); Forward, R.L. (1984), *Phys. Rev. B* **30**,
  1700 (the honest outer bound: vacuum "feeding" yields only one-shot Casimir work, never continuous power).
  `[credited]`; a "vacuum/ZPF net power source" reading is **not** supported and stays settled-negative.

**1l. Rhythm dynamics, anharmonic (Duffing) resonance & the parametric fence (§ M16, 2026-09-14).**
*Grounding the M16 fold (`toolkit/TOOLKIT_ADV_16_RHYTHM_PARAMETRIC_2026-09-14.md`,
`results/verify/rhythm_parametric_resonance_check.py`, `results/verify/duffing_backbone_check.py`). All
relations credited textbook physics, reproduced in-repo; the one speculative bridge (cross-scale pump) is
the fenced settled-negative.*
- **Beats as a nonlinear/energy observable**: Feynman, R.P. (1963), *Lectures on Physics* I-48 — the beat
  envelope is not a linear Fourier line; the difference frequency appears in a quadratic (energy/intensity)
  observable. `[credited]`.
- **Parametric resonance & the anharmonic oscillator**: Landau, L.D. & Lifshitz, E.M., *Mechanics* (3rd ed.,
  Pergamon 1976), §27 (parametric resonance, principal tongue `Ω=2ω₀`, threshold), §§28–29 (anharmonic
  oscillations & resonance in nonlinear oscillations — the amplitude-dependent frequency / backbone
  `ω(a)=ω₀+(3β/8ω₀)a²`; cited jointly since the 3rd-edition section split is edition-sensitive); Mathieu, É. (1868), *J. Math.
  Pures Appl.* **13**, 137 (the Mathieu equation); Nayfeh, A.H. & Mook, D.T. (1979), *Nonlinear Oscillations*
  (Wiley), ch.3–5 (multiple-scales, Duffing backbone, jump/hysteresis, odd harmonics). `[credited]`.
- **Entrainment / phase-locking**: Adler, R. (1946), *Proc. IRE* **34**, 351 (`dψ/dt=Δω−K sin ψ`, lock iff
  `|Δω|≤K`); Pikovsky, A., Rosenblum, M. & Kurths, J. (2001), *Synchronization* (CUP) — Arnold tongues,
  devil's-staircase mode-locking (the Arnold-tongue comb-lock, distinct from the M16-5 Duffing-pull).
  `[credited]`.
- **The sum-rule for parametric/three-wave pumping** (the settled-negative's basis): Kruer, W.L. (1988),
  *The Physics of Laser Plasma Interactions* (Addison-Wesley), ch.7 — parametric instabilities require a
  sum/twice-frequency match `Ω≈ω_j+ω_k`; a slow **difference** (beat) frequency is not a valid pump, so the
  kHz carrier beat cannot pump a MeV mode (15.7 OOM short). `[credited]`.
- **The CK inharmonic comb** (the linear-limit fingerprint): Chandrasekhar, S. & Kendall, P.C. (1957),
  *Astrophys. J.* **126**, 457 — force-free eigenvalues `tan x=x`, ratios `1:1.719:2.427`. `[credited]`
  (also reproduced two ways in `ck_eigenvalues_check.py`).

**1m. LENR prior-art completeness (§ folded by the explanatory-resolution-map novelty audit, 2026-09-14).**
*Prior art that FTGB's predictions/explanations must credit or be distinguished from — surfaced by an
adversarial novelty audit against the six named theorists (grounding
`results/LENR_EXPLANATORY_RESOLUTION_MAP_2026-09-14.md`). Each independently verified (author/year/venue).*
- **Beat-sweep excess-heat (the signature-CLASS predates FTGB)**: Hagelstein, P.L., Letts, D. & Cravens, D.
  (2010), *J. Condensed Matter Nucl. Sci.* **3**, 59 — two-laser THz difference-frequency (beat) response of
  Pd-D; excess-heat steps near 8.2/15.1/20.8 THz. The credited precedent for "sweep a beat frequency, look
  for a locked yield step." **Computed non-match** to the FTGB geometric ladder `f_b(L)=N^L` (the reported
  steps are not geometric): `beat_ladder_nonmatch_check.py`. `[credited]` (class) / FTGB's exact `N^L` form is
  the untested-novel residue.
- **Ionization-as-LENR-trigger (general concept)**: Gareev, F.A. & Zhidkova, I.E. (2005), arXiv:nucl-th/0505021
  — "the excitation and ionization of atoms may play a role as a trigger for LENR." The general precedent for
  the FTGB `¹⁶³Dy→¹⁶³Ho` ionization-gated trigger (which adds the specific isotope + X-ray charge-state
  protocol). `[credited]` (concept) / the isotope+protocol packaging is the novel residue.
- **TSC / 4D-cluster branching (the analogous question, a different route)**: Takahashi, A. (2014), *J.
  Condensed Matter Nucl. Sci.* **13**, 565 — the tetrahedral-symmetric-condensate `4d→2⁴He` picture answers
  the branching/product question via an EQPET/Gamow-barrier route, distinct from the FTGB B=4 Landau–Zener
  adiabaticity selector. `[credited, distinct mechanism]`.
- **Coherent-condensate fusion twins (the nearest structural rivals to the collective-disposal `[S]` core)**:
  Kim, Y.E. (2009), *Naturwissenschaften* **96**, 803 — Bose–Einstein-Condensation Nuclear Fusion (deuterons
  in a coherent BEC → ⁴He, momentum absorbed collectively); Chubb, T.A. & Chubb, S.R. (2000), *Proc. ICCF-8*
  — ion-band-state (coherent Bloch deuteron) theory. Distinguished from FTGB by the anapole/Hopf–Chern
  topological referent + CK-comb signature + LZ-Δ selector, none of which they carry. `[credited, distinct]`.
- **SAFIRE's peer-reviewed mechanism (in tension with the Beltrami reading)**: Morgan, T. & Childs, M. (2015),
  *Plasma Sources Sci. Technol.* **24**, 055022 — the anode-shell striations attributed to an **electrostatic**
  negative-ion space-charge mechanism, *disfavoring* (not merely untested against) a magnetic single-λ
  force-free reading. `[credited]`; the FTGB driven-Beltrami-attractor reading of SAFIRE is softened to a
  category analogy, not a structural identity.

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
**Identity fence (2026-09-13, from the Arc-vault audit):** the corpus's source vault conflates at least two
distinct authors under "Reed" — **Larry J. Reed** (*Quantum Wave Mechanics*, self-published, the QWM framework
folded here) and **Donald Reed** ("Beltrami Topology as Archetypal Vortex," 1992/94; extended-electrodynamics
work with **Lee M.** Hively — Reed & Hively (2020), *Symmetry* **12**, 2110 is the one peer-reviewed item of
that thread). Disentangle before citing any "Reed" item externally; QWM claims attach to Larry J. Reed only.

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
  Topological Physics (**peer-reviewed / accepted (multiple TUFT papers), Int. J. Topology** (lineage 2019 → 2025);
  *audit note 2026-09-14: this acceptance status rests on the project's own reconciliation — add the specific
  paper titles/DOIs/acceptance dates when available so it is externally checkable rather than asserted*). SM gauge
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
- **Corpus-salvage do-not-cite additions (2026-09-13,** from the vendored `PAPER_PREP_CITATIONS` store + the
  Arc-vault audit — each a *checked* provenance failure, not a style preference**):**
  - "Greenyer et al., MFMP Technical Report 2018" — **could not be located; do not cite** (the corpus's own
    verification failed). Vishnevskii (2008) — cite only *as the source Greenyer's program cites*, not as an
    independently verified primary. Huang et al., *Sci. Rep.* (2024) — real paper but **carries an Editor's
    Note**; do not treat its claims as confirmed.
  - Taleyarkhan (2002) bubble-fusion — **settled-negative (research misconduct finding)**; cite only as the
    cautionary case. Holmlid ultra-dense hydrogen H(0) — ~94% of the literature is one group, ~88%
    self-citation, zero outside replication, contradicted by Hansen (2016) reanalysis — do not lean on.
  - Heim "verified at DESY 1981" — community legend, no DESY publication; Feynman "acknowledged EVO reality" —
    an overstatement of an unverified private letter; the 2016 Nobel "confirms the vortex atom" — false
    equivalence. None of these enter the record.
  - Adamenko/Proton-21 energy-gain and Cu→Fe figures, Klimov COP 2.4–10, Podkletnov/Li-Torr/Pais/Buhler
    gravity-propulsion claims — **unreplicated single-source claims**; log in the history file with flags,
    never cite as support.
  - **The "scalar-EM/bidirectional-Whittaker" energy claim — RULED OUT by explicit symbolic proof** (corpus
    `cascade_vacuum_bridge` §2.3): Whittaker (1903), *Math. Ann.* **57**, 333 is a genuine, legitimate
    plane-wave-superposition theorem — but the Bearden-lineage extension (counter-propagating decomposition
    ⇒ extractable energy beyond the total field's Poynting bookkeeping) fails three ways (no global null
    from two real waves; `u_tot − (u₁+u₂) = 0` exactly; components at a node are superposed, not separately
    addressable). Cite Whittaker; never the extension. Bibliographic **corrections** that ride with the vendored store: MoEDAL is
    *Nature* **602**, 63 (2022); arXiv:1705.07052 is **Gould & Rajantie**, *PRL* **119**, 241601; PRAB **22**,
    054503 (2019) is **Bartalucci–Vysotskii–Vysotskyy**; the pear-shaped-fission paper is **Scamps & Simenel**,
    *Nature* **564**, 382 (2018).

*Frameworks contribute method, vocabulary, and convergence — never a load-bearing claim. Established physics
is always `[credited]`; every framework reading is tier-tagged and attributed.*
