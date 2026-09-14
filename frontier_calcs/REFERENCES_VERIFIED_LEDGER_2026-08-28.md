# References — verified-citations ledger (master thesis + this session)

Consolidated bibliography for the lead document `TOROIDAL_SYNTHESIS_MASTER_THESIS.tex` and the companion
`ICCF27_DRIVEN_DISSIPATIVE_COMPANION_PAPER.tex`, with verification status. `[V]` = confirmed via live
search or primary-source read this session; `[T]` = textbook-canonical (high confidence, standard
reference); `[P]` = project's own document. Apply [[feedback_pre_promotion_validation_checklist]] before
locking; re-verify any `[T]` metadata (vol/page) at lock time.

## Foundational (established, textbook)
| Key | Reference | Status |
|---|---|---|
| chandrasekhar1957 | S. Chandrasekhar & P.C. Kendall, "On force-free magnetic fields," Astrophys. J. **126**, 457 (1957) | [T] |
| taylor1974 | J.B. Taylor, "Relaxation of toroidal plasma...," Phys. Rev. Lett. **33**, 1139 (1974) | [T] |
| moffatt1969 | H.K. Moffatt, "The degree of knottedness of tangled vortex lines," J. Fluid Mech. **35**, 117 (1969) | [T] |
| zeldovich1958 | Ya.B. Zel'dovich, "Electromagnetic interaction with parity violation," Sov. Phys. JETP **6**, 1184 (1958) | [T] |
| afanasiev1995 | G.N. Afanasiev & Yu.P. Stepanovsky, "The electromagnetic field of elementary time-dependent toroidal sources," J. Phys. A: Math. Gen. **28**, 4565 (1995) — the toroidal/anapole dipole has **zero external B** (confined "hidden" moment); its only external signature is a curl-free longitudinal `A`. Grounds the 2026-08-13 absolute transverse/longitudinal partition. | [T] |
| madelung1927 | E. Madelung, "Quantentheorie in hydrodynamischer Form," Z. Phys. **40**, 322 (1927) | [T] |
| manley1956 | J.M. Manley & H.E. Rowe, Proc. IRE **44**, 904–913 (1956) | [T] |

## Physical anchors (added 2026-08-23, primary-source-verified)
| Key | Reference | Anchor | Status |
|---|---|---|---|
| hill2000sspx | D.N. Hill et al., "Spheromak Formation Studies in SSPX," LLNL UCRL-JC-137828, 18th IAEA FEC, Sorrento (2000); review E.B. Hooper et al., Plasma Phys. Control. Fusion **54**, 113001 (2012) | `n_i=1.7×10¹⁹ m⁻³` (range 1×10¹⁹–1.3×10²⁰); edge field 0.2–0.4 T | [V] |
| stenhoff1999 | M. Stenhoff, *Ball Lightning: An Unsolved Problem in Atmospheric Physics*, Kluwer/Plenum (1999) | `R=0.12 m` (diam. 0.24 m; most-probable 10–50 cm, mean ~20 cm) | [V] |
| usstdatm1976 | U.S. Standard Atmosphere 1976, NOAA-S/T 76-1562 | `m_i=29 amu` (M(air)=28.9647 g/mol) | [V] |
| uman1984 | M.A. Uman, *Lightning* (channel-radius/field synthesis; via BALL_LIGHTNING_ENVELOPE_MODEL) | BL near-channel field 0.32–0.47 T (tension vs B=20.6 mT) | [T] |
| cen2014 | J. Cen, P. Yuan, S. Xue, "Observation of the Optical and Spectral Characteristics of Ball Lightning," Phys. Rev. Lett. **112**, 035001 (2014) | ~5 m outlier event (NOT the anchor); composition only, no B/n | [V] |
| versteegh2008 | A. Versteegh et al., "Long-living plasmoids from an atmospheric water discharge," Plasma Sources Sci. Technol. **17**, 024014 (2008) | CHECKED-NEGATIVE for anchor: density 10²⁰–10²² m⁻³ but **no magnetic field** (unmagnetized, double-layer confinement). A web claim of "300 G" is a FABRICATION — do not cite it. | [V, ruled out] |

*Anchor audit finding: B=20.6 mT / v_A=2.033×10⁴ m/s are a self-consistency residual, NOT independently
measured (density mismatch n_e=10²⁰ vs n_i=1.7×10¹⁹). See `30_CANONICAL_NUMBERS.md` §A and registry VAC-6.*

**Micro-plasmoid / EVO / charge-cluster (B,n) — searched 2026-08-23; field is confinement-DERIVED field-wide:**
| Key | Reference | (B, n) | Status |
|---|---|---|---|
| hubler2022 | G.K. Hubler, "A Possible Heuristic Explanation of Exotic Vacuum Objects (EVOs, Charge Clusters)," JCMNS **36** (2022) 30–37 (quoting Shoulders) | 2 µm EVO, N=10¹¹–10¹³ e⁻ → n~10¹⁹–10²¹; **NO field measured** | [V] |
| jaitner2020 | L. Jaitner, "Condensed Plasmoids (CPs) — A Quantum-Mechanical Model of the Nuclear Active Environment of LENR," J. Condensed Matter Nucl. Sci. **33** (2020) 168–193 | z-pinch condensed plasmoid: I~9 kA, B~50 MT (Bennett z-pinch, model), n~1.5×10³⁵ m⁻³ | [V] |
| lerner2004 | E.J. Lerner, "Prospects for p¹¹B Fusion with the DPF: New Results," arXiv:physics/0401126 (2003/04) | DPF hot-spot **6 µm core**: **n_i=3.3×10²⁷ m⁻³ MEASURED** (3 independent: DT/DD neutron branching, X-ray+Te, Rogowski ion-beam); **B=400 MG COMPUTED** (gyroradius/confinement bound, NOT measured) | [V] primary |
| lerner2008 | E.J. Lerner & R.E. Terry, "Advances Towards pB11 Fusion with the Dense Plasma Focus," 6th Symp. Current Trends Int'l Fusion Research (2008) | DPF hot-spot: B=400 MG, n>10²⁷ m⁻³ — carries forward Lerner 2004's computed B | [V, 2nd-hand] |
| peacocknorton1975 | N.J. Peacock & B.A. Norton, "Measurement of megagauss magnetic fields in a plasma focus device," Phys. Rev. A **11**, 2142 (1975) | **B~1 MG=100 T MEASURED** (Zeeman splitting, CV line) — the ONLY confirmed spectroscopic DPF field; but mm-scale, lower field, no matched n | [V] |
| lewis2012 | E. Lewis, "Microscopic Ball Lightning...," JCMNS **7** (2012) 8–10 | 0.1–400 µm craters; morphology only, no B/n | [V, ruled out] |
| turnergolka2013 | D.A. Turner et al., IEEE Trans. Plasma Sci. (2013) + US Patent US20130188764A1 | ESTS: B=3.8 T (worked ex.), n>10²⁵ (sep. source) — not co-measured | [V, caution] |
*Verdict: no PRIMARY measured B for a micron EVO exists; confinement-derivation (Jaitner 50 MT, Lerner DPF
400 MG, this project's 33 kT/1000 T) is the FIELD-STANDARD method. The web "Greenyer >1000 T" claim is
unconfirmed — do NOT cite. See registry EVO-10.*

## LENR / CMNS field references (added 2026-08-26, live-verified — grounds Layer LNR)
*Ported from `LENR_FIELD_GROUNDING_AND_CONSISTENCY_2026-08-26.md` §Key-references into the master ledger.*
| Key | Reference | Grounds | Status |
|---|---|---|---|
| miles2003 | M.H. Miles, "Correlation of Excess Enthalpy and Helium-4 Production: A Review," Proc. ICCF-10, Cambridge MA (2003); lenr-canr.org (MilesMcorrelatioa.pdf) | He↔heat: 30/33 correlate, p=1/750,000; rate 10¹⁰–10¹² ⁴He·s⁻¹·W⁻¹; theoretical 2.6×10¹¹; **23.8 MeV/⁴He** (LNR-10, LNR-12) | [V] full text read |
| mckubre2000case | M.C.H. McKubre, F. Tanzella, P. Tripodi, P. Hagelstein, "The Emergence of a Coherent Explanation for Anomalies Observed in D/Pd and H/Pd Systems; Evidence for ⁴He and ³He Production," Proc. ICCF-8, Lerici (Italy), F. Scaramuzzi (ed.), Italian Physical Society Vol. **70** (2000) 3–10 | **Case-cell ⁴He/heat `Q = 31 ± 13 MeV/atom`** — the PRIMARY source (supersedes the MIT Tech. Review 2004 secondary) | [V] confirmed via search |
| case1998 | L.C. Case, "Catalytic Fusion of Deuterium into Helium-4," Proc. ICCF-7 (1998) 48 | the original Case experiment McKubre replicated | [V] |
| mckubre2015 | M.C.H. McKubre, "Cold Fusion (LENR): One Perspective on the State of the Science," *J. Condensed Matter Nucl. Sci.* **15** (2015) 137–148 | D/Pd ≳ 0.85 loading threshold; He/heat review | [V] full text read |
| iwamura2002 | Y. Iwamura, M. Sakano, T. Itoh, "Elemental Analysis of Pd Complexes: Effects of D₂ Gas Permeation," *Jpn. J. Appl. Phys.* **41** (2002) 4642 | Cs→Pr, Sr→Mo transmutation, `(+4,+8)`, multi-method detection (LNR-9) | [V] |
| takahashi2008tsc | A. Takahashi, "Dynamic Mechanism of TSC Condensation Motion," Proc. ICCF-14 (2008); "Physics of Cold Fusion by TSC Theory," JCMNS | 4-D Tetrahedral Symmetric Condensate → 2⁴He (LNR-9 convergence) | [V] |
| vysotskii2013ccs | V.I. Vysotskii, M.V. Vysotskyy, "Coherent correlated states and low-energy nuclear reactions in non-stationary systems," *Eur. Phys. J. A* **49** (2013) 99 | coherent correlated states; `G_eff=G√(1−r²)` (LNR-7) | [V] |
| li2000srt | X.Z. Li et al., "Sub-barrier fusion and selective resonant tunneling," *Phys. Rev. C* **61** (2000) 024610 | resonance replaces the Gamow factor; neutron-channel suppression (LNR-7) | [V] |
| storms2010 | E. Storms, "Status of Cold Fusion (2010)," *Naturwissenschaften* **97** (2010) 861; NAE papers via JCMNS | Nuclear Active Environment (1–10 nm cracks); irreproducibility driver (LNR-8) | [V] |
| srinivasan2015 | M. Srinivasan, "Revisiting the Early BARC Tritium Results," *J. Condensed Matter Nucl. Sci.* **15** (2015) 137–148 | tritium ≫ neutrons (3–7 orders); "tritium desert" (LNR-5) | [V] full text read |
| cecil_ddg | F.E. Cecil et al., branching-ratio measurements of low-energy deuteron reactions, *Nucl. Instrum. Methods B* | D+D→⁴He+γ branching ≈ **1.1×10⁻⁷** (aneutronic context) | [cited — verify vol/page at lock] |
| berlinguette2019 | C.P. Berlinguette et al. (Google/CleanHME), "Revisiting the cold case of cold fusion," *Nature* **570** (2019) 45 | rigorous COP≈unity negative control | [V] |
| klimov2024pvr | A. Klimov et al., "Highly Efficient Water Plasma Vortex Reactor…," *J. Condensed Matter Nucl. Sci.* **38** (2024/25) | COP 2–10, peer-reviewed; transmutation | [V] |

## Session additions (2026-08-25) — golden-comb / vacuum / metrology / neutrino passes (primary-source-verified)
*Promoted into the paper's list `REFERENCES_VERIFIED_2026-08-25.md`; here for the complete store.*
| Key | Reference | Status |
|---|---|---|
| aharonov1959 | Y. Aharonov & D. Bohm, "Significance of Electromagnetic Potentials in the Quantum Theory," Phys. Rev. **115**, 485 (1959) [ADS 1959PhRv..115..485A] — flux/AB phase `θ=qΦ/ħ_eff` (§§11,12) | [V] |
| udem2002 | T. Udem, R. Holzwarth & T.W. Hänsch, "Optical frequency metrology," Nature **416**, 233 (2002) — comb metrology; spectral-spacing readout (§§11,12) | [V] |
| hutchinson2002 | I.H. Hutchinson, *Principles of Plasma Diagnostics*, 2nd ed., Cambridge Univ. Press (2002) [ISBN 9780521803892] — plasma interferometry; probe-phase readout (§12) | [T] |
| tonomura1986 | A. Tonomura et al., "Evidence for Aharonov-Bohm Effect with Magnetic Field Completely Shielded from Electron Wave," Phys. Rev. Lett. **56**, 792 (1986) [ADS 1986PhRvL..56..792T] — AB phase of a **toroidal** source, measured (§12) | [V] |
| wolfenstein1978 | L. Wolfenstein, "Neutrino oscillations in matter," Phys. Rev. D **17**, 2369 (1978) [ADS 1978PhRvD..17.2369W] — MSW forward-scattering `V=√2 G_F n_e`; neutrino occupancy (§5) | [V] |
| winterberg1994 | F. Winterberg, "The Planck Aether Model for a Unified Theory of Elementary Particles," Int. J. Theor. Phys. **33**, 1275 (1994) [Springer BF00670794] — paired-Planck-mass-dipole polarizable vacuum; **background only**, not a derived EVO mechanism (§4) | [V, background] |
| puthoff2002 | H.E. Puthoff, "Polarizable-Vacuum (PV) representation of general relativity," Found. Phys. **32**, 927–943 (2002) [arXiv:gr-qc/9909037] — PV representation used as the *consistent-but-subdominant* substrate reading (`K_PV−1≈7×10⁻³⁵`, plasma index dominates by >40 orders); a magnitude statement, not a "no-vacuum" exclusion. FTGB ref 47 (§3.2). Literal `K_PV` mappings were tested and **ruled out** — cite only for the subdominant-substrate framing | [A/background] |

## Synthesis-convergence & prior-art (added 2026-08-23, search-verified)
*Added after the source-index + cmns-lenr-explorer passes flagged these as load-bearing but un-ledgered.*

**Force-free plasmoid ball-lightning prior art (MUST cite — the base idea is established, ours is EVO-specific/independently converging):**
| Key | Reference | Status |
|---|---|---|
| tsui2003 | K.H. Tsui, "Ball lightning as a magnetostatic spherical force-free field plasmoid," Phys. Plasmas **10**, 4112 (2003) | [V] |
| ranada1996 | A.F. Rañada & J.L. Trueba, "Ball lightning an electromagnetic knot?," Nature **383**, 32 (1996) | [V] |
| ranada1998 | A.F. Rañada, M. Soler & J.L. Trueba, "A model of ball lightning as a magnetic knot with linked streamers," J. Geophys. Res. Atmos. **103**(D18), 23309 (1998) | [V] |
| taveira2004 | Taveira & Sakanaka, triple-Beltrami ball-lightning formation, arXiv:physics/0411153 (2004) — *exact title/authors to confirm at lock* | [V-arxiv] |

**Division-algebra / octonionic gauge-tower lineage (underpins TOP-2/3/4/5, ELE-3, PRED-6):**
| Key | Reference | Status |
|---|---|---|
| baez2002 | J.C. Baez, "The Octonions," Bull. Amer. Math. Soc. **39**, 145–205 (2002); arXiv:math/0105155 | [V] |
| gunaydin1973 | M. Günaydin & F. Gürsey, "Quark structure and octonions," J. Math. Phys. **14**, 1651 (1973) | [V] |
| dixon1994 | G.M. Dixon, *Division Algebras: Octonions, Quaternions, Complex Numbers and the Algebraic Design of Physics*, Kluwer (1994), ISBN 0-7923-2890-6 | [V] |
| furey2016 | C. Furey, "Standard model physics from an algebra?," PhD thesis, Univ. Cambridge; arXiv:1611.09182 (2016) | [V] |
| furey2018 | C. Furey, "Braids, normed division algebras, and Standard Model symmetries," Phys. Lett. B **785**, 84 (2018) | [V] |

**Golden-ratio mode-splitting precedent (the numerology defense):**
| Key | Reference | Status |
|---|---|---|
| coldea2010 | R. Coldea et al., "Quantum Criticality in an Ising Chain: Experimental Evidence for Emergent E8 Symmetry," Science **327**, 177 (2010) — measured two-mode ratio = φ = 1.618 | [V] |
| koide1982 | Y. Koide, "Fermion-boson two-body model of quarks and leptons and Cabibbo mixing," Lett. Nuovo Cimento **34**, 201 (1982) — the empirical charged-lepton relation Q=2/3 (predicted τ=1776.97 MeV) | [V] (search-verified 2026-08-24) |
| ikedataniguchi1978 | A. Ikeda & Y. Taniguchi, "Spectra and eigenforms of the Laplacian on Sⁿ and Pⁿ(C)," Osaka J. Math. **15**(3), 515–546 (1978) — full spectrum/eigenforms on spheres; the S³/Sⁿ form-spectrum the ⋆d mass tower (TOP-6) builds on | [V] (search-verified 2026-08-24) |
| kongkhambut2022 | P. Kongkhambut et al., "Observation of a continuous time crystal," Science **377**, 670 (2022); arXiv:2202.06980 — limit-cycle phase (continuous time-translation breaking) in a driven-dissipative atom-cavity; anchor for the heartbeat (BEAT-5/8) | [V] (search-verified 2026-08-24) |
| agamalov2026 | O. Agamalov, "The Physics of the Stable Phase-Locked Attractor in Spheromak Plasma," Research Square rs-9449730 v1 (2026) — RF phase-locked to the Kramers rate → helicity self-transfer to the Taylor state; Grad-Shafranov sim amplifies 3 T→>12 T below the Chirikov threshold; independent convergent driven-attractor (BEAT-8) | [V] (search-verified 2026-08-24) |
| hestenes1990 | D. Hestenes, "The Zitterbewegung Interpretation of Quantum Mechanics," Found. Phys. **20**, 1213–1232 (1990) — Zitterbewegung as local circulatory motion = electron spin/moment; grounds the toroidal electron (ELE-1) | [V] (search-verified 2026-08-24) |
| calugareanu | G. Călugăreanu (1961) / J.H. White (1969), "Călugăreanu–White–Fuller theorem" Lk=Tw+Wr; ref: M.R. Dennis & J.H. Hannay, "Geometry of Călugăreanu's theorem," Proc. R. Soc. A **461**, 3245 (2005) — grounds TOP-1 (Lk=Tw+Wr) | [V] (search-verified 2026-08-24) |

## Round-2 deep-lead anchors (frontier expansion; verified 2026-08-24)
| Key | Reference | Frontier use | Status |
|---|---|---|---|
| torres2017 | T. Torres, S. Patrick, A. Coutant, M. Richartz, E.W. Tedford, S. Weinfurtner, "Rotational superradiant scattering in a vortex flow," Nature Physics **13**, 833 (2017) — first lab superradiance (14±8% at 3.70 Hz) | analogue-gravity superradiance (FR-5 gravitational, BEAT-9) | [V] |
| weidemann2020 | S. Weidemann et al., "Topological funneling of light," Science **368**, 311–314 (2020) — non-Hermitian skin effect / light funnel | amplification mechanism (round-2 item 4) | [V] |
| wilson2011 | C.M. Wilson et al., "Observation of the dynamical Casimir effect in a superconducting circuit," Nature **479**, 376 (2011) — photon pairs from modulation | legal "energy-from-modulation" emission channel | [V] |
| feiguin2007 | A. Feiguin, S. Trebst, A.W.W. Ludwig, M. Troyer, A. Kitaev, Z. Wang, M.H. Freedman, "Interacting anyons in topological quantum liquids: the golden chain," Phys. Rev. Lett. **98**, 160409 (2007) — Fibonacci-anyon chain, c=7/10 | φ²=φ+1 fusion rule (round-2 item 3) | [V] |
| avila2009 | A. Avila & S. Jitomirskaya, "The Ten Martini Problem," Ann. Math. **170**, 303–342 (2009) — Cantor spectrum of the almost-Mathieu operator | golden critical quasiperiodicity (round-2 item 2) | [V] |
| kraemer2006 | T. Kraemer et al., "Evidence for Efimov quantum states in an ultracold gas of caesium atoms," Nature **440**, 315–318 (2006) — geometric-ladder three-body states | RG limit cycle / discrete scale invariance (round-2 item 1, BEAT-7) | [V] |
| brenner2002 | M.P. Brenner, S. Hilgenfeldt, D. Lohse, "Single-bubble sonoluminescence," Rev. Mod. Phys. **74**, 425–484 (2002) — driven-bubble ℓ-mode stability | cavitation isomorph of the fissility ladder (round-2 item 6, EVO-9) | [V] |
| chengchenchance1985 | C.Z. Cheng, L. Chen, M.S. Chance, "High-n ideal and resistive shear Alfvén waves in tokamaks," Ann. Phys. **161**, 21 (1985) — foundational TAE-gap paper (toroidicity opens a continuum gap ∝ε); prior art for the beat comb | [V] (search-verified 2026-08-24) |
| ⚠ kramer2021 | "golden-ratio three-wave triad" — **UNVERIFIED / likely misattributed**: no such Kramer 2021 paper found. Real golden-ratio-parametric result = "Golden Ratio Gain Enhancement in Coherently Coupled Parametric Processes," Sci. Rep. **8**, 11407 (2018). **Do NOT cite kramer2021; substitute the 2018 Sci. Rep. or the N²=N+1 self-derivation for BEAT-2.** | [FLAGGED — do not use] |

## Hydrodynamic–wave frame (§operator) — the QM↔EM↔MHD unification
| Key | Reference | Status |
|---|---|---|
| bialynicki1996 | I. Bialynicki-Birula, "Photon wave function," in *Progress in Optics* **36**, ed. E. Wolf (Elsevier, 1996), pp. 245–294 — Riemann–Silberstein `i∂_tF=c∇×F` (Maxwell as a curl-operator wave equation) | [V] |
| bbm1976 | I. Bialynicki-Birula & J. Mycielski, "Nonlinear wave mechanics," Ann. Phys. **100**, 62 (1976) — the log-NLS used in the Madelung sector; SAME author as bialynicki1996 (loop-closure) | [T]/[V] |

## Golden-ratio triad + Fibonacci invariants (§triad) — PRIOR ART (theory = synthesis)
| Key | Reference | Status |
|---|---|---|
| kramer2022 | M.A. Kramer, "Golden rhythms...," Neurons, Behavior, Data analysis, and Theory (2022); arXiv:2111.09953 — golden-ratio three-wave triad resonance (prior art). NOTE: key renamed from the colliding `kramer2021` (that key is the do-not-use guard above); journal/store already cite "Kramer (2022)" | [V] |
| hanson1984 | J.D. Hanson & J.R. Cary, Phys. Fluids **27**, 767–769 (1984) — golden-mean anti-resonance/KAM (prior art) | [T] |
| vladimirova2021 | N. Vladimirova, M. Shavit & G. Falkovich, "Fibonacci turbulence," Phys. Rev. X **11**, 021063 (2021) — Fibonacci-coefficient conservation laws | [V] |
| devakul2019 | T. Devakul, Y. You, F.J. Burnell & S.L. Sondhi, "Fractal symmetric phases of matter," SciPost Phys. **6**, 007 (2019) — fractal→topological protection; conceptual convergence only, different mechanism (footnote scope) | [V] |

## Beat law = TAE gap scaling (§beatlaw) — PRIOR ART
| Key | Reference | Status |
|---|---|---|
| chengchen1985 | C.Z. Cheng, L. Chen & M.S. Chance, "High-n ideal and resistive shear Alfvén waves in tokamaks," Ann. Phys. **161**, 21–47 (1985) — toroidicity-induced Alfvén-eigenmode gap ∝ ε=a/R (the beat law reproduces this) | [V] |

## Dissipative structures / time crystals (§driven, §complete-picture)
| Key | Reference | Status |
|---|---|---|
| nicolisprigogine1977 | G. Nicolis & I. Prigogine, *Self-Organization in Nonequilibrium Systems* (Wiley, 1977) | [T] |
| glansdorffprigogine1971 | P. Glansdorff & I. Prigogine, *Thermodynamic Theory of Structure, Stability and Fluctuations* (Wiley, 1971) | [T] |
| kongkhambut2022 | P. Kongkhambut et al., "Observation of a continuous time crystal," Science **377**, 670 (2022); arXiv:2202.06980 — the landmark limit-cycle dissipative time crystal | [V] |
| cabotgiorgizambrini2024 | A. Cabot, G.L. Giorgi & R. Zambrini, "Nonequilibrium transition between dissipative time crystals," PRX Quantum **5**, 030325 (2024) | [V] |
| (nat.commun.2025) | "Observation of multiple time crystals in a driven-dissipative system with Rydberg gas," Nat. Commun. (2025), s41467-025-64488-7 | [V] |
| (commun.phys.2025) | "Emergent continuous time crystal in a dissipative quantum spin system without driving," Commun. Phys. (2025), s42005-025-02040-1 | [V] |
| toptc | K. Giergiel et al., "Topological time crystals," arXiv:1806.10536 (2018); "Observation of a symmetry-protected topological time crystal with superconducting qubits," arXiv:2109.05577 (2021) | [V] |

## Topology (§topology, §complete-picture)
| Key | Reference | Status |
|---|---|---|
| (fukui2005) | T. Fukui, Y. Hatsugai & H. Suzuki, "Chern numbers in discretized Brillouin zone," J. Phys. Soc. Jpn. **74**, 1674 (2005) — FHS lattice Berry-flux method (used for C=±2) [companion paper] | [T] |
| mesadame2025 | C. Mesa Dame, H. Qin, et al., "Wave topology in Hall magnetohydrodynamics," arXiv:2506.18830 (2025) — Hall-MHD wave-mode Chern C±=±1 (compared, not identical) | [V] |

## Discrete scale invariance / Efimov class (§complete-picture)
| Key | Reference | Status |
|---|---|---|
| efimov1970 | V. Efimov, "Energy levels...three-body system," Phys. Lett. B **33**, 563 (1970) — the DSI/RG-limit-cycle tower; s0=π/ln λ VALIDATED (reproduces s0=1.006 from λ=22.7) | [V] |
| braaten2006 | E. Braaten & H.-W. Hammer, "Universality in few-body systems with large scattering length," Phys. Rep. **428**, 259 (2006) | [T] |

## Holographic face (§holographic — boundary encodes bulk; 2026-08-10)
| Key | Reference | Status |
|---|---|---|
| berger1984 | M.A. Berger & G.B. Field, "The topological properties of magnetic helicity," J. Fluid Mech. **147**, 133–148 (1984) — helicity gauge-freedom = pure boundary flux ∮χB·n dS (relative helicity). VERIFIED numerically (ABC field: flux-closed⇒ΔH=0, open⇒the boundary integral) | [V] |
| thooft1993 | G. 't Hooft, "Dimensional reduction in quantum gravity," arXiv:gr-qc/9310026 (1993) — holographic principle. Cited as STRUCTURAL analogy only (boundary-encodes-bulk / area-law); explicitly NOT AdS/CFT | [V] |
| susskind1995 | L. Susskind, "The world as a hologram," J. Math. Phys. **36**, 6377–6396 (1995) — holographic principle. Structural analogy only, firewalled from any quantum-gravity claim | [V] |

## External frameworks (inspiration/convergence — NOT load-bearing; firewalled)
| Key | Reference | Status |
|---|---|---|
| nielsen-tuft | J.L. Nielsen, "The Topological Unified Field Theory on the Complex Hopf Fibration," in invited peer review, Int. J. Topology (EiC M. Planat); PhilArchive/ResearchGate/Academia. Rigorous, engaged: Beltrami operator `B=⋆d` (Thm 14, via Etnyre–Ghrist Reeb↔Beltrami), Aizawa-modulated Hopf = Stuart–Landau normal form (App. J). Grand-unification claims firewalled. [[reference_nielsen_tuft_assessment]] | [V] |
| agamalov2026 | O. Agamalov, "The Physics of the Stable Phase-Locked Attractor in Spheromak Plasma," Research Square rs-9449730 (2026) — independent convergent preprint (driven phase-locked attractor); corroboration only, different mechanism | [V] |
| reed-qwm | L.J. Reed, *Quantum Wave Mechanics* 4th ed. (Booklocker, 2022) — inspiration source, 16× checked, EXHAUSTED (confirms-not-extends; particle/gravity/aether framework). **Includes the "Particle Geometry" figure cited for ELE-1/TOP-1/EVO-4 (torus-knot particles, Lk=Tw+Wr, 48-ring EVO)** — [cited], self-published, low-citation. [[reference_reed_qwm_chapter_catalog_and_salvage_plan]] | [P/V] |
| whittaker1903 | E.T. Whittaker, Math. Ann. **57** (1903) — scalar-wave decomposition (legitimate math; the diagnostic "scalar channel" basis; NOT Bearden "scalar EM") | [T] |
| etnyre-ghrist | J. Etnyre & R. Ghrist, "Contact topology and hydrodynamics" (2000) — the Beltrami↔Reeb correspondence underlying Nielsen Thm 14 | [T] |

## Notes
- The two locked papers received the kramer2022 + chengchen1985 prior-art citations (2026-08-10 integrity pass, [[project_v11_lock_pass_status]]); their own bibliographies hold the full ~77-ref sets.
- `[To complete before lock]` (companion paper): the Bogoliubov/BdG reference for the ring-radial eigenvalue.

- **kedia2013** — H. Kedia, I. Bialynicki-Birula, D. Peralta-Salas, W. T. M. Irvine, "Tying Knots in
  Light Fields," Phys. Rev. Lett. **111**, 150404 (2013). VERIFIED (real PRL, DOI 10.1103/PhysRevLett.111.150404).
  Provides the two-integer (p,q) Hopf–Rañada field family with Hopf charge Q_H = p·q. Used for the
  surface-mode → Hopf-charge **seed selection rule** (thesis §topology; `hopfion_seed_selection_rule_from_surface_mode.py`,
  Q_H=p·q reconfirmed here by an independent 3-D Whitehead integral).

## Crystallized 10-page presentation v1.2-lock — additional refs (2026-08-13)
Consolidated from the author's external lock pass (web-verified there); classical entries are textbook-standard.
`[T]`=textbook/classical standard · `[V]`=verified (this project or the lock-pass ledger) · `[premise]`=starting geometry, scoped.
| Key | Reference | Status |
|---|---|---|
| woltjer1958 | L. Woltjer, Proc. Natl. Acad. Sci. **44**, 489 (1958) — force-free minimum-energy theorem | [T] |
| hill1894 | M.J.M. Hill, "On a spherical vortex," Phil. Trans. R. Soc. A **185**, 213 (1894) — nested toroidal stream surfaces | [T] |
| helmholtz1858 | H. von Helmholtz, J. Reine Angew. Math. **55**, 25 (1858) — vortex theorems; leapfrog description | [T] |
| kelvintait1867 | W. Thomson (Kelvin), Proc. R. Soc. Edinburgh **6**, 94 (1867); P.G. Tait, smoke-ring expts (1867) | [T] |
| bostick1956 | W.H. Bostick, Phys. Rev. **104**, 292 (1956) — coins "plasmoid"; self-similar force-free toroid | [T] |
| greenyer2023 | R. Greenyer, "Practical Applications of the Fractal Toroidal Moment," ICCF-25, Szczecin (2023) — six-fold nested morphology, taken as starting geometry; no other claim adopted | [premise] |
| whitehead1947 | J.H.C. Whitehead, Proc. Natl. Acad. Sci. **33**, 117 (1947) — Hopf invariant as an integral (Q_H) | [T] |
| bliokh2015 | K.Y. Bliokh, D. Smirnova & F. Nori, Science **348**, 1448 (2015) — photon spin-Hall / helicity Chern | [V] |
| palmerduca2024 | E. Palmerduca & H. Qin, Phys. Rev. D **109**, 085005 (2024); Phys. Rev. Res. **7**, L022001 (2025) — photon topology; C=±2 recovered-not-novel | [V] |
| hsu2016 | C.W. Hsu et al., Nat. Rev. Mater. **1**, 16048 (2016) — bound states in the continuum (review) | [T/V] |
| friedrichwintgen1985 | H. Friedrich & D. Wintgen, Phys. Rev. A **32**, 3231 (1985) — symmetry-protected BIC | [T/V] |
| sornette1998 | D. Sornette, Phys. Rep. **297**, 239 (1998) — discrete scale invariance & complex dimensions | [T/V] |
| cosme2025 | J.G. Cosme et al., Phys. Rev. Lett. **134**, 223601 (2025) — torus bifurcation of a dissipative time crystal (apposite to the beating limit-cycle) | [V] |
| rayleigh1882 | Lord Rayleigh, Philos. Mag. **14**, 184 (1882) — charged-drop instability (fissility origin) | [T] |
| duft2002 | D. Duft et al., Phys. Rev. Lett. **89**, 084503 (2002) — charged-microdroplet shape-oscillation threshold (lab) | [V] |
| hilleaves2012 | R.J.A. Hill & L. Eaves, Appl. Phys. Lett. **100**, 114106 (2012); L. Liao & R.J.A. Hill, Phys. Rev. Lett. **119**, 114501 (2017) — one lab lineage | [V] |
| singh2021 | M. Singh et al., Phys. Rev. E **103**, 053111 (2021) — Rayleigh breakup, levitated charged drop (lab) | [V] |
| wong1973 | C.Y. Wong, Ann. Phys. (N.Y.) **77**, 279 (1973) — toroidal/bubble nuclei breathing-stability threshold | [V] |

Reproducibility: every closed-form/derivable number in the presentation is recomputed and asserted by
`frontier_calcs/crystallized_10pp_recheck.py` (30/30 PASS, 2026-08-13); FEM/BEM rows cross-referenced to
`benchtop_quadruplet_decisive_neumann_crosscheck.py`, `horn_torus_fissility_threshold.py`, `ws6_cCK_convergence_and_analytic_limit.py`.

## FTGB_v3 folded advances (Fronts A–E, 2026-08-18) — verified this pass, primary-source
Promoted from `FTGB_v3.tex` (the six 2026-08-18 `\bibitem`s). Verified against primary bibliographic records
(Crossref DOI / APS / PubMed) on 2026-08-18; all `[V]`. ⚠ `torres2017` title corrected from the draft's
"superradiance in a vortex flow" to the published "superradiant **scattering** in a vortex flow" (DOI 10.1038/nphys4151).
| Key | Reference | Status |
|---|---|---|
| fruchartvitelli2021 | M. Fruchart, R. Hanai, P.B. Littlewood & V. Vitelli, "Non-reciprocal phase transitions," Nature **592**, 363–369 (2021); DOI 10.1038/s41586-021-03375-9 — non-reciprocal active-matter class (Front A active swimmer: non-reciprocal drive on a Goldstone mode) | [V] |
| hatanonelson1996 | N. Hatano & D.R. Nelson, "Localization Transitions in Non-Hermitian Quantum Mechanics," Phys. Rev. Lett. **77**, 570–573 (1996); DOI 10.1103/PhysRevLett.77.570 — non-Hermitian skin effect = directional funnel (Front A) | [V] |
| zeldovich1971 | Ya.B. Zel'dovich, "Generation of waves by a rotating body," JETP Lett. **14**, 180 (1971) [Russian: Pis'ma ZhETF **14**, 270 (1971)] — rotational superradiance ω<mΩ (Front C). No DOI (Soviet translation journal); confirmed across the superradiance literature | [V] |
| misner1972 | C.W. Misner, "Interpretation of Gravitational-Wave Observations," Phys. Rev. Lett. **28**, 994–997 (1972); DOI 10.1103/PhysRevLett.28.994 — Kerr rotational-superradiance / synchrotron condition (Front C) | [V] |
| torres2017 | T. Torres, S. Patrick, A. Coutant, M. Richartz, E.W. Tedford & S. Weinfurtner, "Rotational superradiant scattering in a vortex flow," Nat. Phys. **13**, 833–836 (2017); DOI 10.1038/nphys4151 — lab realization in a draining vortex (Front C) | [V] |
| jung1992 | M. Jung et al., "First observation of bound-state β⁻ decay," Phys. Rev. Lett. **69**, 2164–2167 (1992); DOI 10.1103/PhysRevLett.69.2164 — bare ¹⁶³Dy⁶⁶⁺ bound-state β⁻, T½=47±5 d (Front D ΔZ signature anchor) | [V] |

## Historical precedent, scoped — Holt 1979 NASA "Field Resonance Propulsion Concept" (added 2026-08-24)
Primary source VERIFIED: the report is a real NASA Technical Memorandum in hand (NASA-TM-80961 = JSC-16073;
NTIS accession N80-19184; Alan C. Holt, Lyndon B. Johnson Space Center, August 1979; presented at the 15th
Joint AIAA/SAE/ASME Propulsion Conference, 18–20 June 1979). Its own inner references are real, citable physics
(Kruer & Estabrook, Phys. Fluids **20**, 1688 (1977); Nishihara & Ohsawa, Phys. Fluids **19**, 1833 (1976);
Max, Manheimer & Thompson, Phys. Fluids **21**, 128 (1978) — laser-generated megagauss fields; Petschek/Thorne
reconnection).
| Key | Reference | Status |
|---|---|---|
| holt1979 | A.C. Holt, *Field Resonance Propulsion Concept*, NASA-TM-80961 / JSC-16073 (NASA JSC, Aug. 1979); NTIS N80-19184 | [historical, scoped] |

**What is genuinely citable (real physics, convergent with the model):**
- Reconnection-driven *oscillating* toroidal field structure: "by alternately pulsing adjacent laser sets, the
  location of the merging processes can be made to oscillate back and forth at a **desired rate**" — a decades-old,
  institutionally-sourced precedent for a **tunable modulation frequency** of a merged-field toroid (structurally a
  two-drive beat/envelope). Maps to the model's carrier/beat picture and its coupled-mode splitting.
- Geometry-over-magnitude: "Alfvén waves ... change only the **geometry** of the field lines," and the flare rate
  "depends on geometrical relationships ... more important ... than the magnitude of the field strength" — the same
  geometry-first stance the force-free model takes.
- Frequency-dependent enhancement/inhibition of merging by hydromagnetic waves (Holt 1979 thesis) — a **resonance**
  condition on a toroidal reconnecting structure.
- Figure 3 "Field Resonance System": a toroidal, multi-lobed nested-vortex morphology (eight paired vortices about a
  central pattern) — a morphological echo of the octahedral/toroidal ring structure. Cite as visual precedent only.

**What is firewalled (NOT adopted — speculation with no verified basis):** EM↔gravitational/space-time-metric
"resonance"; space-time as a projection of higher-dimensional space; black-hole/white-hole energy transfer; UFO/
extraterrestrial framing; Rachman & Dutheil superluminal-world relativity; and energy extraction "through resonance
with gravitational fields" (an over-unity claim — routed through the chase-the-source discipline, not taken as a
mechanism). Use `holt1979` strictly as a **historical convergence** on reconnection-driven, tunably-modulated,
geometry-dominated toroidal field structures — never for its propulsion/gravity thesis.

## Support for the 2026-08-24 stability + torsion results (canonical, added 2026-08-24)
Direct literature support for STAB-1/STAB-2/PRED-18. Canonical papers; `[T]`=textbook-standard, `[V*]`=known
result, exact bibliographic fields to be final-checked at lock (flagged, not guessed).
| Key | Reference | Supports | Status |
|---|---|---|---|
| yoshidagiga1990 | Z. Yoshida & Y. Giga, "Remarks on spectra of operator rot," Math. Z. **204**, 235–245 (1990) | curl operator is self-adjoint with a real, discrete spectrum → STAB-2 (real force-free spectrum, no growing ideal eigenmode) | [V*] |
| cazenave1983 | T. Cazenave, "Stable solutions of the logarithmic Schrödinger equation," Nonlinear Anal. TMA **7**, 1127–1140 (1983) | orbital stability of the log-NLS gausson → STAB-1 (medium-sector stability) | [V*] |
| berry1984 | M.V. Berry, "Quantal phase factors accompanying adiabatic changes," Proc. R. Soc. A **392**, 45–57 (1984) | geometric (Berry) phase = the O(1) parallel-transport factor in the torsion-odd splitting → PRED-18 | [T] |
| tomitachiao1986 | A. Tomita & R.Y. Chiao, "Observation of Berry's topological phase by use of an optical fiber," Phys. Rev. Lett. **57**, 937–940 (1986) | helical-path (torsion) → polarization/frequency rotation; the physical realization of the torsion-odd mechanism → PRED-18 | [V*] |
| moffattricca1992 | H.K. Moffatt & R.L. Ricca, "Helicity and the Calugareanu invariant," Proc. R. Soc. A **439**, 411–429 (1992) | field-line torsion, twist+writhe=linking in flux tubes → the torsion framing of PRED-18 | [T] |

**Horn-torus tilt stability — spheromak/compact-toroid tilt references (agent primary-read verified, added 2026-08-26; support S5/O4 = oblate tilt lock):**
| Key | Reference | Supports | Status |
|---|---|---|---|
| rosenbluthbussac1979 | M.N. Rosenbluth & M.N. Bussac, "MHD stability of spheromak," Nucl. Fusion **19**, 489 (1979) | oblate ("oblimak") spheromak is MHD+tearing stable; prolate/spherical tilt-unstable → the oblateness stabilizer for the horn torus | [V] |
| bondeson1981 | A. Bondeson, G. Marklin, Z.G. An, H.H. Chen, Y.C. Lee, C.S. Liu, "Tilting instability of a cylindrical spheromak," Phys. Fluids **24**, 1682 (1981) | cylindrical flux-conserver tilt-unstable for L/R≳1.67 → the elongation threshold. (Correct co-authors: An, Chen, Lee, Liu — NOT Fowler/Nebel) | [V] |
| mehta2020 | R. Mehta, A.M. Barkov, L. Sironi, M. Lyutikov, "Kink/tilt instability of spheromaks," arXiv:2006.14656 (2020) | 3-D ideal-MHD + relativistic PIC: spheromak tilt growth γ·τ_A ≈ 0.6–0.8 → the Alfvénic growth rate | [V-arxiv] |
| belova2000 | E.V. Belova, S.C. Jardin, H. Ji, M. Yamada, R. Kulsrud, "Numerical study of tilt stability of prolate FRCs," Phys. Plasmas **7**, 4996 (2000) | FRC tilt γ=C·v_A/Z_s, C≈1–3; rotational stabilization needs Mach M≳1–2 (Milroy 1989) → the rotation ruling-out | [V] |
| schaffer2008 | M.J. Schaffer, FESAC memo (2008-06-03), SSX operating parameters | SSX operates tilt-stably at separatrix elongation E=0.6 → the experimental oblate stable point (matches horn-torus E=0.5) | [V*] |

## Session 2026-08-26 — referee-pass additions (agent-verified)
*New refs surfaced by the maximal-paper referee pass (novelty + CMNS agents). Verification per the agent that fetched
them. See `REFEREE_AND_COMPREHENSION_MAXIMAL_2026-08-26.md` §D and `KNOWLEDGE_MULTIMAP_INDEX.md` timeline 2026-08-26.*

**A. Operator-spine / EM–plasma–Beltrami convergence (novelty agent):**
| Key | Reference | Note | Status |
|---|---|---|---|
| bialynickibirula1996 | I. Bialynicki-Birula, "Photon wave function," Prog. Optics **36**, 245 (1996) | The Riemann–Silberstein one-photon wavefunction; the correct EM-leg credit (was missing from paper bib) | [V] |
| bialynickabirula2013 | I. Bialynicki-Birula & Z. Bialynicka-Birula, "The role of the Riemann–Silberstein vector...," J. Phys. A **46**, 053001 (2013) | States explicitly: monochromatic RS fields are **curl eigenfunctions = Trkalian fields** → EM-leg = Beltrami, ESTABLISHED (agent fetched directly) | [V] |
| moses1971 | H.E. Moses, "Eigenfunctions of the curl operator...," SIAM J. Appl. Math. **21**, 114 (1971) | Curl-eigenfunction decomposition applied jointly to EM + fluid mechanics | [V] |
| lakhtakia1994 | A. Lakhtakia, "Viktor Trkal, Beltrami fields, and Trkalian flows," Czechoslovak J. Phys. **44**, 89 (1994) | Historical synthesis: fluid + EM + astrophysical Beltrami as one family | [V] |
| marsh1996 | G.E. Marsh, *Force-Free Magnetic Fields: Solutions, Topology and Applications* (World Scientific, 1996) | Textbook chapter "Force-Free Fields and Electromagnetic Waves" → EM/force-free identity is textbook | [V*] |
| tuchin2016 | K. Tuchin, "Excitation of Chandrasekhar–Kendall photons in QGP...," Phys. Rev. C **93**, 054903 (2016) | ★ Quantizes EM **inside a plasma** in the CK basis ("CK photons") — the EM–plasma coincidence made literal, a decade before this paper (agent fetched) | [V] |
| xiaqinwang2016 | X.-L. Xia, H. Qin, Q. Wang, "Approach to Chandrasekhar–Kendall–Woltjer state in a chiral plasma," Phys. Rev. D **94**, 054042 (2016) | Companion joint EM/force-free result in a chiral plasma | [V] |
| takabayasi1952 | T. Takabayasi, "On the formulation of QM associated with classical pictures," Prog. Theor. Phys. **8**, 143 (1952) | Spin-vorticity (Pauli/Dirac) hydrodynamics — the route a rigorous quantum/log-NLS (leg-ii) Beltrami reading would need; scalar Madelung flow is irrotational, so leg-ii is [S] not [V] | [V] |
| ranadasolertrueba2000 | A.F. Rañada, M. Soler, J.L. Trueba, "Ball lightning as a force-free magnetic knot," Phys. Rev. E **62**, 7181 (2000) | Distinct from the 1996 Nature "electromagnetic knot?" paper — earlier drafts conflated the two titles | [V] |

**B. LENR kernel / CMNS (CMNS agent):**
| Key | Reference | Note | Status |
|---|---|---|---|
| dicke1954 | R.H. Dicke, "Coherence in spontaneous radiation processes," Phys. Rev. **93**, 99 (1954) | Superradiance foundation; the collective-emission kernel route (Dicke ≠ the project's *rotational* superradiance — naming-collision guard) | [T] |
| dicke1953 | R.H. Dicke, "The effect of collisions upon the Doppler width of spectral lines," Phys. Rev. **89**, 472 (1953) | Lamb–Dicke / recoil-narrowing origin | [T] |
| hagelsteinchaudhary2011 | P.L. Hagelstein & I.U. Chaudhary, "Energy exchange using spin-boson models with infinite loss," JCMNS **4**, 202 (2011) | The lossy-spin-boson phonon–nuclear disposal model; the field's most on-point kernel theory | [V] |
| hagelstein2025 | P.L. Hagelstein, F. Metzler, M.K. Lilley, J.F. Messinger, N. Galvanetto, "Models for nuclear fusion in the solid state," arXiv:2501.08338 (2025) | "Generalized nuclear Dicke model"; lists decoherence/receiver-decay/resonance as still-unresolved → kernel still open in the field | [V-arxiv] |
| hagelsteinlettscravens2010 | P.L. Hagelstein, D. Letts, D. Cravens, "Terahertz difference frequency response of PdD in two-laser experiments," JCMNS **3**, 59 (2010) | ★ Excess heat only at beat (difference) frequencies near {8.3,15.3,20.4} THz → direct experimental precedent for the beat-locked-yield falsifier (P§17.4) | [V] |
| preparata1995 | G. Preparata, *QED Coherence in Matter* (World Scientific, 1995) | Bressani–Preparata superradiance as the cold-fusion coherence mechanism | [V*] |
| vysotskii2019 | V.I. Vysotskii et al., "Correlated states and nuclear reactions: an experimental test with low energy beams," Phys. Rev. Accel. Beams **22**, 054503 (2019) | Mainstream-venue *experimental* CCS test → lifts CCS above "purely theoretical" (input-kernel) | [V] |
| hukeczerski2008 | A. Huke, K. Czerski et al., "Enhancement of deuteron-fusion reactions in metals," Phys. Rev. C **78**, 015803 (2008) | Measured electron screening ~300 eV in ZrD₂ (>> gas-target) → corroborates that static screening alone is insufficient (P§12.1) | [V] |
| czerskidubey2024 | K. Czerski, ... Dubey, "Observation of thermal deuteron-deuteron fusion in ion tracks," arXiv:2409.02112 (2024) | Recent measured d-d fusion enhancement | [V-arxiv] |
| chengchenchance1985 | C.Z. Cheng, L. Chen, M.S. Chance, "High-n ideal and resistive shear Alfvén waves in tokamaks," Ann. Phys. **161**, 21 (1985) | Establishes the toroidicity-induced gap mode (TAE) — the credited anchor for the beat doublet as its plasmoid realization (P4, FTGB ref 49) | [V] |
| chechinetal2003 | V.A. Chechin, V.A. Tsarev, M. Rabinowitz, Y.E. Kim, "Critical review of theoretical models for cold fusion," arXiv:nucl-th/0303057 | Surveys 25+ CMNS theories, none complete → context: crowded, unresolved field | [V-arxiv] |
| toyota2013 | T. Toyota et al., independent replication of Cs→Pr transmutation, peer-reviewed venue (2013) | Makes Cs→Pr the stronger of the two "demonstrated" cages vs Sr→Mo (S₃⁻-interference critique) | [V?] ⚠ venue unverified — confirm before lock |
| shanahan_miles | K. Shanahan (calorimetric-recombination critique); M.H. Miles et al., "A new look at LENR research: a response to Shanahan" (MIT DSpace) | The active Miles helium-heat calorimetry dispute (metal-flask controls rebut) → cite both sides | [V*] |

**C. Torsion / supersolid medium / collective-coherence (2026-08-27 agent sweep; surfaced+checked by WebSearch, not re-derived here):**
| Key | Reference | Note | Status |
|---|---|---|---|
| moffattricca1992 | H.K. Moffatt & R.L. Ricca, "Helicity and the Călugăreanu invariant," Proc. R. Soc. Lond. A **439**, 411 (1992) | Helicity = linking = twist + writhe (`H = Lk·Φ²`); with `λ = α =` twist-per-length this grounds `C_τ = sgn(λ)` (flagship §7.1) | [V*] |
| calugareanu_white_fuller | Călugăreanu (1961) / F.B. Fuller, "The writhing number of a space curve," PNAS **68**, 815 (1971) / J.H. White (1969) | Self-linking `Lk = Tw + Wr` theorem — the decomposition behind the torsion sign | [V*] |
| zloshchastiev_svt | K.G. Zloshchastiev, logarithmic superfluid-vacuum theory, arXiv:2011.11897; arXiv:2011.12565 (+ Int. J. Mod. Phys. B review, 2025) | log-NLS **is** a superfluid-vacuum / Korteweg (crystallizing) medium → the supersolid elevation of the §3 medium; equation-level correspondence [S], plasmoid=condensate analogy [A] | [A-arxiv] |
| toroidal_supersolid_pra2023 | *Phys. Rev. A* **107**, 063316 (2023); arXiv:2308.05981 | Toroidal dipolar supersolid: quantized ring circulation coexisting with angular crystalline order — lab cousin of a toroidal Beltrami with winding | [V-arxiv] |
| andreevlifshitz1969 | A.F. Andreev & I.M. Lifshitz, *Sov. Phys. JETP* **29**, 1107 (1969) | Supersolid concept + the `D+1` Goldstone count (second-sound ↔ beat, first-sound ↔ breathing) | [V*] |
| tanzi2019 | L. Tanzi et al., *Nature* **574**, 382 (2019) | Dipolar-BEC supersolid observed (roton softening → crystallization) | [V*] |
| acebron2005 | J.A. Acebrón et al., "The Kuramoto model: a simple paradigm for synchronization phenomena," *Rev. Mod. Phys.* **77**, 137 (2005) | Phase-lock threshold `K_c` — the "more drive → more coherence" continuous 2nd-order onset (flagship §12.5) | [V*] |
| baumann2010 | K. Baumann, C. Guerlin, F. Brennecke, T. Esslinger, "Dicke quantum phase transition with a superfluid gas in an optical cavity," *Nature* **464**, 1301 (2010) | Driven–dissipative superradiant ordered phase above a pump-power threshold — energy flows environment→collective | [V*] |
| lidar1998 | D.A. Lidar, I.L. Chuang, K.B. Whaley, "Decoherence-free subspaces for quantum computation," *Phys. Rev. Lett.* **81**, 2594 (1998) | Subradiant = decoherence-free subspace under shared-bath coupling → collective protection (why "black" EVs are long-lived, §12.5) | [V*] |
| stix1992 | T.H. Stix, *Waves in Plasmas* (AIP, 1992) | Cold-plasma perpendicular dielectric `ε_⊥ = 1 + c²/v_A²` (Alfvén) → the medium's `ε`-part; `n_A = √(ε_rμ_r) = c/v_A` (product = speed), impedance `Z = Z_vac/n_A` (ratio = stiffness); the two-part ε/μ reading of §3.1 | [V*] |

**D. Chiral anomaly / C_τ sign-lock (§7.1 helicity-ladder fold, 2026-08-28; established chiral-MHD literature):**
| Key | Reference | Note | Status |
|---|---|---|---|
| vilenkin1980 | A. Vilenkin, "Equilibrium parity-violating current in a magnetic field," *Phys. Rev. D* **22**, 3080 (1980) | Origin of the chiral magnetic effect: `J = (e²/2π²ħc)μ₅B` — the parity-odd current linear in `B` that couples `μ₅` to helicity (§7.1) | [V*] |
| fukushima_kharzeev_warringa2008 | K. Fukushima, D.E. Kharzeev, H.J. Warringa, "The chiral magnetic effect," *Phys. Rev. D* **78**, 074033 (2008) | Modern CME derivation; the Chern–Simons/axion term `(e²/2π²ħc)μ₅(A·B)` (§7.1) | [V*] |
| joyce_shaposhnikov1997 | M. Joyce & M. Shaposhnikov, "Primordial magnetic fields, right electrons, and the Abelian anomaly," *Phys. Rev. Lett.* **79**, 1193 (1997) | Anomaly ties chiral charge `N₅` and magnetic helicity `H` into one conserved quantity → chiral dynamo amplifies helicity of sign `sgn(μ₅)`; and baryon-number↔helicity link (§7.1) | [V*] |
| boyarsky_frohlich_ruchayskiy2012 | A. Boyarsky, J. Fröhlich, O. Ruchayskiy, "Self-consistent evolution of magnetic fields and chiral asymmetry in the early universe," *Phys. Rev. Lett.* **108**, 031301 (2012) | Chiral MHD: coupled evolution of `H` and `μ₅`; the sign-locking conservation law behind the C_τ selection (§7.1) | [V*] |
| cornwall1997 | J.M. Cornwall, "Speculations on primordial magnetic helicity," *Phys. Rev. D* **56**, 6146 (1997) | Baryon asymmetry ↔ definite-sign primordial magnetic helicity via the anomaly (§7.1 absolute-sign, model-dependent) | [A] |
| vachaspati2001 | T. Vachaspati, "Estimate of the primordial magnetic field helicity," *Phys. Rev. Lett.* **87**, 251302 (2001) | Estimates primordial field is left-handed (negative helicity) for `ΔB>0` — the tentative absolute-sign basis (§7.1) | [A] |
| tashiro2014 | H. Tashiro, W. Chen, F. Ferrer, T. Vachaspati, "Search for CP violation in the gamma-ray sky," *MNRAS* **445**, L41 (2014) | Tentative (~2–3σ, disputed) observational hint of left-handed intergalactic magnetic helicity — soft support for the absolute sign (§7.1) | [A-tentative] |
| ivoilov2006 | N.G. Ivoilov, "Low energy generation of the 'strange' radiation," *Ann. Fond. Louis de Broglie* **31**(1), 115 (2006) | The one CMNS dataset naming track "chirality": rare mirror-image track *pairs*, statistically *symmetric* (S/N born in pairs) — a DIFFERENT observable (reflection-geometry, per Fredericks 2013); mild adjacent tension to the universal-handedness prediction, NOT a like-for-like test (§7.1). Do not conflate with EVO winding sense | [A-adjacent] |

**E. Double-Beltrami / EVO varieties (§8.1a charge-balance fold, 2026-08-28):**
| Key | Reference | Note | Status |
|---|---|---|---|
| mahajan_yoshida1998 | S.M. Mahajan & Z. Yoshida, "Double curl Beltrami flow: diamagnetic structures," *Phys. Rev. Lett.* **81**, 4863 (1998) | Hall two-fluid double-Beltrami `(∇×−λ₊)(∇×−λ₋)B=0` from two conserved helicities (`K_M`, `K_G`); the stable nested electron-core (`λ₊=1/d_e`) / ion-body (`λ₋R=4.4934`) profile, real-roots stability (discriminant `S²−4P>0`), and `K_G`-protection of the core — the two-fluid generalization of Woltjer–Taylor (§8.1a, §8.3) | [V*] |
| grossharoche1982 | M. Gross & S. Haroche, "Superradiance: an essay on the theory of collective spontaneous emission," *Phys. Rep.* **93**, 301 (1982) | `N²` cooperative-emission review — the fast-scale disposal layer | [V*] |
| hafstadteller1938 | L.R. Hafstad & E. Teller, "The alpha-particle model of the nucleus," *Phys. Rev.* **54**, 681 (1938) | α-cluster binding = `ε·(α–α bonds)`, bonds = edges of the configuration — the geometric edge-count law the cage products obey (⁸Be/¹²C/¹⁶O/²⁴Mg to ~2%, R²≈0.98; §14.1). The geometric *scaling*; per-bond `ε≈2.4 MeV` is a nuclear input | [V*] |
| ikedaetal1968 | K. Ikeda, N. Takigawa, H. Horiuchi, *Prog. Theor. Phys. Suppl.* Extra (1968) | The **Ikeda diagram** — α-cluster threshold structure; the geometric-cluster tradition the cage products sit in | [V*] |
| freer2018 | M. Freer, H. Horiuchi, Y. Kanada-En'yo, D. Lee, U.-G. Meißner, "Microscopic clustering in light nuclei," *Rev. Mod. Phys.* **90**, 035004 (2018) | Modern review: ab-initio confirmation of the ¹²C Hoyle-triangle and ¹⁶O-tetrahedron cluster states | [V*] |
