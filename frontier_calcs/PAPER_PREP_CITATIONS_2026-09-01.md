# Paper-prep citation harvest — 2026-09-01 session

**Scope.** Every citation introduced or used in the 2026-08-31/2026-09-01 "principled reopening" pass
(monopole/leptonic-monopole, QGP/baryon/chirality, bead-chain/bubble/knot priors, EVO lifetime, two-sector,
octahedral-lattice) is harvested here, tiered, and grouped by topic — bibliography-ready for the paper. This
file **extends** `REFERENCES_VERIFIED_LEDGER.md` (348 lines, ~230 entries through 2026-08-28) and the memory
`reference_cmns_lenr_field_knowledge_base.md`; entries already present there are marked **[already in ledger]**
and not re-tabled in full (see those files for full bibliographic form). Everything below is either newly
introduced this session or newly *verified* this session even if the raw citation text existed earlier.

**Tiers used** (per task brief):
- **[A-verified-this-session]** — WebSearch/WebFetch confirmed real author/journal/year/DOI-or-arXiv in this pass.
- **[A-cited-not-reverified]** — real, standard/well-known physics; the session doc's own citation is internally
  consistent and plausible, but I did not independently re-run a search on it in this pass (mostly canonical
  20th-century results already familiar from training and cross-checked against the multiple independent
  session docs that cite them consistently).
- **[A-primary-read-this-session]** — the session doc's own author fetched/read the primary source directly
  this session (Lochak, Ivoilov, Fredericks) — stronger than a bibliographic-only check.
- **[do-not-cite]** — non-peer-reviewed / commercial / internally contested to the point of unusability, or a
  popular-magazine piece, flagged so it is not accidentally promoted into the paper's reference list.
- **[UNVERIFIED — locate before use]** — could not be independently pinned this session; do not cite without
  first locating the primary source.

**Load-bearing vs illustrative** is marked per-row: **LB** = a paper claim rests on this citation being
correct; **ILL** = background/context/analogy, no paper claim depends on its precise details.

---

## 0. CORRECTIONS FOUND — fix before citing (real papers, wrong attribution in this session's own docs)

These are not fabrications — the underlying physics claims in the session docs are fine — but the
**bibliographic pointers themselves are wrong** and must not be copied into the paper as written.

| # | What the session doc wrote | What is actually correct | Where it appears | Fix |
|---|---|---|---|---|
| C1 | "MoEDAL Collaboration... *Nature* **604**, 64 (2022)" | **Nature 602, 63–67 (2022)**, DOI 10.1038/s41586-021-04298-1, "Search for magnetic monopoles produced via the Schwinger mechanism" | `LOCHAK_LEPTONIC_MONOPOLE_REOPEN_2026-09-01.md:384-385,451`; `EVO_MONOPOLE_CENTER_REOPEN_2026-09-01.md` (same citation copied); ledger rows R39/R41 | Change volume **604→602**, page **64→63–67** |
| C2 | "Ellis, J. et al., 'Magnetic monopole mass bounds from heavy ion collisions and neutron stars,' arXiv:1705.07052 (2017)" | Real paper, arXiv:1705.07052 — but the authors are **Oliver Gould & Arttu Rajantie**, not Ellis/Kalinowski/Mavromatos; published *Phys. Rev. Lett.* **119**, 241601 (2017) | `LOCHAK_LEPTONIC_MONOPOLE_REOPEN_2026-09-01.md:397-399,454-455` | Change author list to **Gould, O. & Rajantie, A.**; add the PRL 119, 241601 (2017) published form |
| C3 | "Danon et al., accelerator test, *Phys. Rev. Accel. Beams* **22**, 054503 (2019)" | Real paper, same journal/vol/page — but authors are **S. Bartalucci, V.I. Vysotskii, M.V. Vysotskyy** ("Correlated states and nuclear reactions: an experimental test with low energy beams"), no "Danon" author | `PRINCIPLES_QGP_DIALITY_CHIRALITY_VACUUM_2026-09-01.md:313-315` (also already correctly attributed as `vysotskii2019` in `REFERENCES_VERIFIED_LEDGER.md:307` — the two session docs are internally inconsistent with each other) | Use the ledger's correct `vysotskii2019` form; drop "Danon" |
| C4 | "Bertsch, Younes et al., 'Impact of pear-shaped fission fragments on mass-asymmetric fission in actinides,' *Nature* **560**, 205 (2018)" | Real paper, real title — but authors are **G. Scamps & C. Simenel**, published *Nature* **564**, 382–385 (2018), DOI 10.1038/s41586-018-0780-0 | `BUBBLES_VIRIAL_FISSILITY_2026-09-01.md:100-101` | Change author to **Scamps, G. & Simenel, C.**; volume **560→564**, page **205→382** |

None of these change any physics conclusion in the session docs (all four numbers/mechanisms quoted from the
papers are consistent with the *correct* paper too) — they are pure bibliographic-pointer errors, the kind
that get caught at copy-edit but are worth fixing before submission. Pattern noted: three of four errors are
**author-list swaps on a correctly-remembered title/journal/volume/page** (a "right paper, wrong byline"
failure mode) — worth a dedicated author-list spot-check pass before final bibliography lock.

---

## 1. Monopole / leptonic-monopole cluster

**Task brief's suggested set — status:**

| Ref | Status found this session |
|---|---|
| Lochak arXiv:0801.2752 | **[A-primary-read-this-session]** — confirmed real: *Z. Naturforsch.* A**62**, 231–246 (2007) = arXiv:0801.2752, "The Equation of a Light Leptonic Magnetic Monopole and its Experimental Aspects." LB (the whole Lochak-reopening thread rests on this). |
| Lochak 1983/1985 | **[A-cited-not-reverified]** — *Ann. Fond. Louis de Broglie* **8**, 345 (1983); "Wave equation for a magnetic monopole," *Int. J. Theor. Phys.* **24**, 1019 (1985). Pre-arXiv-era French-society-journal papers, not independently re-searchable this session, but internally consistent across both `LOCHAK_LEPTONIC_MONOPOLE_REOPEN` and `EVO_MONOPOLE_CENTER_REOPEN`, and consistent with how the 2007 Z. Naturforsch. paper (which I did verify) self-describes its own history. LB. |
| Fryberger SLAC-PUB-13583 (dyality/vorton) | **[A-verified-this-session]** — real SLAC preprint, confirmed at slac.stanford.edu/pubs/slacpubs/13500/slac-pub-13583.pdf, "A Ball Lightning Model as a Possible Explanation of Recently Reported Cavity Lights" (April 2009); content (vorton, dyality angle Θ, nucleon-decay energy source) matches the session's description. LB for the diality/vorton discussion; the nucleon-decay energy mechanism is the one this project's own prior work scoped out on magnitude grounds (8–14 orders short) — cite the paper, not its conclusion. |
| Fryberger SLAC-PUB-6473 | **[A-verified-this-session]** — real, confirmed at slac.stanford.edu/pubs/slacpubs/6250/slac-pub-6473.pdf, "A Model for Ball Lightning" (Oct 1994), the earlier/companion paper. ILL (background/history). |
| Vishnevskii 2008 | **[UNVERIFIED — locate before use, as an independent source]**, but **confirmed as a real, named, citable-as-Greenyer-community-primary-source** document: R.P. Vishnevskii, "Superconductivity of the Dirac Monopole" (Sochi, 2008), original in Russian at lightdynamics.narod.ru, English translation by Bob Greenyer, referenced directly from Greenyer's own O-Animator substack posts. **Do not cite as independently peer-reviewed physics** — cite explicitly as "the source Greenyer's own program cites," with that caveat stated, exactly as the session doc `EVO_MONOPOLE_CENTER_REOPEN_2026-09-01.md:313` already does it. ILL/contextual, not load-bearing for any physics claim. |
| Milton 2006 monopole review | **[A-cited-not-reverified]** — K.A. Milton, "Theoretical and experimental status of magnetic monopoles," *Rep. Prog. Phys.* **69**, 1637 (2006). Standard, high-confidence, widely-cited modern monopole review; used only to confirm the standard `α_g≈34.25` coupling figure (arithmetic-check role). ILL. |
| MoEDAL (Nature 2022; PRL 2024) | **[A-verified-this-session]** — see Correction C1 for the Nature entry (**Nature 602, 63–67, 2022**, DOI 10.1038/s41586-021-04298-1); PRL **133**, 071803 (2024) confirmed correct as written ("MoEDAL search in the CMS beam pipe for magnetic monopoles produced via the Schwinger effect," arXiv:2402.15682, published Aug. 2024). **LB** — this is the one model-independent bound the session's own reopening treats as a genuine, unresolved tension with "near-massless" (not explained away). |
| Ray et al. 2014 (Nature, synthetic BEC monopole) | **[A-verified-this-session]** — M.W. Ray, E. Ruokokoski, S. Kandel, M. Möttönen, D.S. Hall, "Observation of Dirac monopoles in a synthetic magnetic field," *Nature* **505**, 657–660 (2014), DOI as indexed (nature12954). Confirmed correct as written. ILL/analogue precedent (real emergent-monopole physics elsewhere, contrastive use — the EVO ground state does NOT meet this mechanism's own point-defect requirement). |
| Castelnovo et al. 2008 (spin ice) | **[A-verified-this-session]** — C. Castelnovo, R. Moessner, S.L. Sondhi, "Magnetic monopoles in spin ice," *Nature* **451**, 42–45 (2008), DOI 10.1038/nature06433 (also arXiv:0710.5515). Confirmed correct as written. ILL, same contrastive role as Ray 2014. |

**Additional monopole-cluster citations surfaced this session (not in the task brief's suggested list):**

| Ref | Tier | LB/ILL | Supports |
|---|---|---|---|
| Ivoilov, N.G., "Low Energy Generation of the 'Strange' Radiation," *Ann. Fond. Louis de Broglie* **31**(1), 115–123 (2006) | **[A-primary-read-this-session]** (agent read the full paper via WebFetch) | LB | The community-usage evidence that Lochak's theory is the named theoretical reference for chiral-track strange-radiation claims; the paired-track/β-source-doubling experiment description |
| Fredericks, K.A., "Possibility of Tachyon Monopoles Detected in Photographic Emulsions," *J. Condensed Matter Nucl. Sci.* **15**, 203–230 (2015) | **[A-primary-read-this-session]** | LB | Review/synthesis across the track-anomaly literature; documents that even within this small community the monopole reading is contested (Fredericks himself prefers a tachyon reading) |
| Urutskoev, L.I., Liksonov, V.I., Tsinoev, V.G., "Experimental detection of 'strange' radiation and transformation of chemical elements," Rus. Applied Physics 2000 no. 4, 83–100 | **[A-cited-not-reverified]** (cited via Ivoilov 2006, not independently re-pulled) | LB (for the strange-radiation cluster) | The original strange-radiation report; co-framed with Lochak by Urutskoev himself |
| Ralston, J.P., "Is Ball Lightning a Signal of Magnetic Monopoles?," arXiv:2411.00240 (2024) | **[A-verified-this-session]** — confirmed real, current (Oct. 2024), 24pp/92-ref hep-ph submission by John P. Ralston | LB | An independent, mainstream-physicist 2024 cross-check reaching essentially the same magnitude-based negative on GUT-monopole catalysis of ball lightning that this project's own prior work reached — genuine independent corroboration, cite as such |
| Wilczek, F. (1982); Rubakov, V. (1981); Callan, C. (1982) — monopole-catalyzed baryon decay | **[A-cited-not-reverified]** — canonical trio (Rubakov, Nucl. Phys. B **203**, 311 (1982) / JETP Lett. **33**, 644 (1981); Callan, Phys. Rev. D **26**, 2058 (1982); Wilczek, Phys. Rev. Lett. **48**, 1146 (1982), "Remarks on dyons" — **note: distinct from** Wilczek's *other* 1982 PRL **49**, 957 (below), "Quantum Mechanics of Fractional-Spin Particles" — do not conflate the two same-year Wilczek PRLs) | LB | The Callan–Rubakov catalysis mechanism the project scoped out on magnitude grounds (8–14 orders) |
| Parker, E.N., *Astrophys. J.* **160**, 383 (1970); Turner, M.S., Parker, E.N., Bogdan, T.J., *Phys. Rev. D* **26**, 1296 (1982) | **[A-cited-not-reverified]** — the canonical Parker-bound pair | LB | The astrophysical monopole-abundance bound (~24-order gap vs. Cramer's claimed rate) |
| Cramer, J.G., "When Proton Meets Monopole," *Analog Science Fiction and Fact*, July 1984 | **[do-not-cite as physics — cite only as "the popularization this project's negative is checked against"]** | ILL | Not a peer-reviewed source; a popular-magazine article that popularized the Callan-Rubakov idea for ball lightning. Retain only as the *target* of the already-computed negative, never as a physics reference in its own right |
| Cramer, J.G., "An Overview of the Transactional Interpretation," *Int. J. Theor. Phys.* **27**, 227 (1988) | **[A-cited-not-reverified]** | ILL | Peer-reviewed (unlike the Analog piece); cited only to note the Transactional Interpretation has no established monopole/EVO connection — an honest null, not a claim |

---

## 2. QGP / chirality / anomalous transport cluster

| Ref | Tier | LB/ILL | Supports |
|---|---|---|---|
| Bazavov, A. et al. (HotQCD), *Phys. Rev. D* **85**, 054503 (2012); Borsanyi, S. et al., *JHEP* **09**, 073 (2010) | **[A-cited-not-reverified]** — standard lattice-QCD crossover-temperature results, widely cross-cited (T_c≈156 MeV consistent across both) | LB | The QGP deconfinement-temperature anchor used to show EVO T is ~5 orders below QGP (physical-role NULL, re-confirmed) |
| STAR Collaboration, "Global Λ hyperon polarization in nuclear collisions: evidence for the most vortical fluid," *Nature* **548**, 62 (2017) | **[A-cited-not-reverified]** — well-known, high-confidence real result (ω≈9×10²¹ s⁻¹ global vorticity) | LB | The real-world CVE-observable vorticity scale the EVO's own ω_ce is compared against (8–9 order gap, like-for-like) |
| Son, D.T. & Surówka, P., "Hydrodynamics with Triangle Anomalies," *Phys. Rev. Lett.* **103**, 191601 (2009) | **[A-verified-this-session]** — confirmed, also arXiv:0906.5044 | **LB** | The anomaly-universal, non-renormalized CVE/CME transport coefficients (C_μ=1/2π², C_T=1/6) — the "principle-match not analogy" upgrade for the EVO↔QGP chiral-vortical comparison |
| Vilenkin, A., "Macroscopic Parity-Violating Effects: Neutrino Fluxes from Rotating Black Holes and in Rotating Thermal Radiation," *Phys. Rev. D* **20**, 1807 (1979) | **[A-cited-not-reverified]** — the original CVE derivation; note this is a **different** Vilenkin paper from the already-ledgered `vilenkin1980` (*Phys. Rev. D* **22**, 3080, 1980, the CME equilibrium-current paper) — both real, keep distinct, do not merge citations | LB | Pre-QGP, independent origin of the Chiral Vortical Effect |
| Kharzeev, D.E. & Son, D.T., "Testing the Chiral Magnetic and Chiral Vortical Effects in Heavy Ion Collisions," *Phys. Rev. Lett.* **106**, 062301 (2011) | **[A-cited-not-reverified]** | LB | Standard CME/CVE heavy-ion phenomenology reference |
| Landsteiner, K., Megías, E. & Peña-Benítez, F., "Gravitational Anomaly and Transport," *Phys. Rev. Lett.* **107**, 021601 (2011); arXiv:1103.5006 | **[A-cited-not-reverified]** | ILL | Extends the anomaly-transport formalism (gravitational-anomaly analogue of CVE) — background depth, not load-bearing for any current EVO claim |
| STAR Collaboration, isobar-run CME search, *Phys. Rev. C* **105**, 014901 (2022); "Implications of the isobar-run results...," *Phys. Rev. C* **106**, L051903 (2022) | **[A-verified-this-session]** — confirmed both real; first paper is the ~3.8×10⁹-event blind measurement (no CME signal meeting predefined criteria), second is the follow-up interpretation paper | **LB — this is an honest, currently-unresolved NEGATIVE the paper should carry**: the flagship CME signature this project's C_τ chirality analogy borrows formal structure from is experimentally *unconfirmed* by the field's own most statistically powerful blind test. Cite exactly as a stated limitation, not smoothed over. |
| Voloshin, S., arXiv:2205.00120 | **[A-cited-not-reverified]** (not independently re-searched this session; internally consistent with the STAR isobar results above) | ILL | Companion commentary/analysis on the isobar CME null |
| Skokov, V., Illarionov, A. & Toneev, V., "Estimate of the magnetic field strength in heavy-ion collisions," *Int. J. Mod. Phys. A* **24**, 5925 (2009), arXiv:0907.1396 | **[A-verified-this-session]** — confirmed real; note the session doc correctly flags this as **modeled, not measured** (UrQMD-model eB estimate, not a direct field measurement) | ILL (context for the QGP eB~10¹⁴–10¹⁵ T figure) | The QGP-side field-strength estimate compared against the EVO's own 130–346 T |
| Bosch, F. et al., "Observation of bound-state β⁻ decay of fully ionized ¹⁸⁷Re," *Phys. Rev. Lett.* **77**, 5190 (1996) | **[A-cited-not-reverified]** — well-known real result (bound-state β-decay half-life dramatically altered for fully-stripped ions); distinct from the already-ledgered `jung1992` (¹⁶³Dy⁶⁶⁺ bound-state decay, PRL **69**, 2164, 1992) — both real, keep both, do not conflate | ILL/analogue | A precedent for environment-dependent weak-decay rates (bound-state vs free), used as a loose analogue in the baryon/QGP reopening's catalyst-argument section |
| Widom, A. & Larsen, L., *Eur. Phys. J. C* **46**, 107 (2006) | **[already in memory ledger `reference_cmns_lenr_field_knowledge_base.md:60-63`]** | LB (as a contrastive alternative-theory citation) | Cited to note nucleon-rearrangement mechanisms need field/density/energy the EVO's own numbers don't reach |
| Vysotskii, V.I. & Vysotskyy, M.V. (2013, EPJ A; update 2025, JCMNS 39:165); Bartalucci, Vysotskii, Vysotskyy (PRAB 22:054503, 2019) | **[already in ledger `vysotskii2013ccs`/`vysotskii2019`]** — see Correction C3 above for the session's own misattribution to "Danon" | LB | Coherent Correlated States kernel — cited as structurally compatible with a baryon-conserving coherent EVO |
| Takahashi, A., "A Theoretical Summary of Condensed Cluster Fusion," *JCMNS* **13**, 565 (2014) | **[already in memory ledger]** | LB | TSC/OSC channel-selection precedent |
| Hagelstein, P.L., "Phonon-mediated Nuclear Excitation Transfer," *JCMNS* **27**, 97 (2018) | **[already in memory ledger]** | LB | The field's own rigorous disposal-wall benchmark |
| Storms, E., *Naturwissenschaften* **97**, 861 (2010); *JCMNS* **9**, 86 (2012) | **[already in ledger `storms2010`]** | LB | Nuclear Active Environment framework |

---

## 3. Topology / knots cluster

| Ref | Tier | LB/ILL | Supports |
|---|---|---|---|
| Moffatt, H.K., *J. Fluid Mech.* **35**, 117 (1969) | **[already in ledger `moffatt1969`]** | LB | Helicity/knottedness — foundational, re-cited this session |
| Woltjer, L. (1958) | **[already in ledger `woltjer1958`]** | LB | Force-free minimum-energy relaxation |
| Chandrasekhar & Kendall (1957) | **[already in ledger `chandrasekhar1957`]** | LB | CK eigenmode basis — re-confirmed this session as the source of the l=1 spherical-Bessel carrier-comb identity |
| Călugăreanu (1959–61) / White (1969) / Fuller (1971) | **[already in ledger `calugareanu`/`calugareanu_white_fuller`]** | LB | Lk=Tw+Wr — the torsion-protection theorem for C_τ (this session's `EVO_POLARIZATION_TORSION_VORTEX_SYNTHESIS`) |
| Kleckner, D. & Irvine, W.T.M., "Creation and dynamics of knotted vortices," *Nat. Phys.* **9**, 253 (2013) | **[A-cited-not-reverified]** (well-known, high-confidence real result; URL in session doc resolves to the actual Nature Physics article) | LB | First lab creation/imaging of knotted vortex loops — the physical-reality anchor for the linked-Hopf/bead-chain picture |
| Kleckner, D., Kauffman, L.H. & Irvine, W.T.M., "How superfluid vortex knots untie," *Nat. Phys.* (2016) | **[A-cited-not-reverified]** | ILL | Reconnection/untying dynamics of knotted vortices — informs the reconnection-null discussion |
| Faddeev, L. & Niemi, A., "Knots and particles," *Nature* **387**, 58 (1997) | **[A-cited-not-reverified]** (standard, famous result) | LB | Faddeev–Niemi Hopfions — the O(3) sigma-model soliton class sharing the EVO's topological (Hopf-charge) classification |
| Whitehead, J.H.C. (1947) | **[already in ledger `whitehead1947`]** | LB | Hopf invariant as an integral |
| Auckly, D. & Speight, J.M., "Fermionic quantization and configuration spaces for the Skyrme and Faddeev-Hopf models," *Commun. Math. Phys.* **263**, 173–216 (2006), arXiv:hep-th/0411010 | **[A-verified-this-session]** — confirmed exact volume/pages | **LB** | Grounds fermionic quantization of Hopf π₃(S²) solitons (the electron/neutrino end of the family, explicitly NOT extended to the macroscopic EVO) |
| Finkelstein, D. & Rubinstein, J., "Connection between Spin, Statistics, and Kinks," *J. Math. Phys.* **9**, 1762 (1968) | **[A-cited-not-reverified]** (classic, well-known result; the Auckly-Speight paper itself builds on this) | LB | Predecessor spin-statistics-from-topology theorem |
| Goldhaber, A.S., "Connection of Spin and Statistics for Charge-Monopole Composites," *Phys. Rev. Lett.* **36**, 1122 (1976) | **[A-cited-not-reverified]** | ILL | Related spin-statistics-from-topology precedent (charge-monopole composites) |

---

## 4. Bubbles / fission / drop-instability cluster

| Ref | Tier | LB/ILL | Supports |
|---|---|---|---|
| Rayleigh-Plesset (Rayleigh 1917; Plesset 1949, standard compound name) | **[A-cited-not-reverified]** — canonical, textbook | LB | Radial cavity/bubble dynamics — the EVO=virial-bubble reading |
| Rayleigh, Lord, *Philos. Mag.* **14**, 184 (1882) | **[already in ledger `rayleigh1882`]** | **LB** | Charged-drop shape instability — the EVO fissility criterion X=U_Coulomb/2U_confine, this session's **X=3/2 exactly** result |
| Duft, D. et al., "Rayleigh jets from levitated microdroplets," *Nature* **421**, 128 (2003) | **NEW distinct paper — [A-cited-not-reverified]**. Note: the *existing* ledger's `duft2002` is a *different* Duft paper (*Phys. Rev. Lett.* **89**, 084503, 2002, shape-oscillation threshold) — **both are real, keep both, do not merge** | LB | Lab charged-droplet Coulomb-fission jets — the experimental analogue for the EVO's charged-drop fission mode (different regime: ℓ=2 single jet vs the EVO's derived ℓ*=3 octupole binary mode — an explicit, honestly-stated *difference*, not a match) |
| Bohr, N. & Wheeler, J.A., *Phys. Rev.* **56**, 426 (1939) | **[A-cited-not-reverified]** — canonical, textbook-standard liquid-drop fissility paper | LB | The x=(Z²/A)/(Z²/A)_crit fissility-parameter formalism, ported to the EVO's own charged-drop parameter X |
| Businaro, U.L. & Gallone, S. (1955) | **[A-verified-this-session]** — confirmed real, standard nuclear-fission-theory result (the Businaro–Gallone critical point, x_BG≈0.35–0.50, separating symmetric- from asymmetric-fission-favoring regimes); exact journal/volume not independently re-pinned this session (widely re-cited secondary-source form used, e.g. via Nix 1972) — **[UNVERIFIED primary bibliographic form — locate exact journal citation before final lock]** | ILL | Context for where the EVO's own derived X≈1.5 sits relative to the symmetric/asymmetric-fission-mode threshold |
| Scamps, G. & Simenel, C., "Impact of pear-shaped fission fragments on mass-asymmetric fission in actinides," *Nature* **564**, 382–385 (2018) | **[A-verified-this-session]** — see Correction C4; this is the corrected citation | ILL | Modern shell/octupole-deformation context for asymmetric fission mode selection |
| Gaitan, D.F., Crum, L.A., Church, C.C., Roy, R.A., *J. Acoust. Soc. Am.* **91**, 3166 (1992) | **[A-cited-not-reverified]** — canonical single-bubble-sonoluminescence founding paper | LB | SBSL drive parameters (40 kHz, 1.1–1.5 bar) used for the EVO heat-burst/beat-locked-yield analogy |
| Brenner, M.P., Hilgenfeldt, S. & Lohse, D., "Single-bubble sonoluminescence," *Rev. Mod. Phys.* **74**, 425 (2002) | **[already in ledger `brenner2002`]** | LB | SBSL review — the "measured T is 60× below naive-adiabatic" caution this session explicitly folds in as an EVO hot-spot-estimate upper-bound warning |
| Flannigan, D.J. & Suslick, K.S., "Plasma formation and temperature measurement during single-bubble cavitation," *Nature* **434**, 52 (2005) | **[A-cited-not-reverified]** — well-known, famous SBSL temperature-measurement paper | LB | The 15,000–20,000 K measured SBSL core-temperature anchor |
| Gompf, B. et al., *Phys. Rev. Lett.* **79**, 1405 (1997) | **[A-cited-not-reverified]** — well-known SBSL flash-width paper | LB | Duty-cycle (~10⁻⁶) precedent for the "heat=beat-bursts" pulsed-emission picture |

---

## 5. Vacuum / QED cluster

| Ref | Tier | LB/ILL | Supports |
|---|---|---|---|
| Lamoreaux, S.K., *Phys. Rev. Lett.* **78**, 5 (1997) | **[A-cited-not-reverified]** — the canonical precision Casimir-force measurement | LB | One of the three measured anchors for "polarizable vacuum is a real, measured principle" (contrasted with the EVO's own literal-QED response, tested NULL by ~17–18 orders) |
| ATLAS Collaboration, light-by-light scattering, *Nat. Phys.* **13**, 852 (2017); *Phys. Rev. Lett.* **123**, 052001 (2019) | **[A-cited-not-reverified]** — both real, well-known LHC results (Pb-Pb ultraperipheral collisions, 8.2σ significance in the 2019 measurement) | LB | Second measured polarizable-vacuum anchor |
| Euler-Heisenberg (1936) | **[NOT explicitly cited by name+year in the 2026-09-01 session docs — used only implicitly via "Cotton-Mouton check" language]** — flag as a **gap to fill**: if the paper cites the Euler-Heisenberg Lagrangian explicitly, add W. Heisenberg & H. Euler, *Z. Phys.* **98**, 714 (1936) | ILL | Underlies the session's own literal-QED-vacuum-birefringence null calculation (Δn_QED~3.6×10⁻¹⁹ at 346 T) — the calculation is done, the textbook citation for its governing Lagrangian was not separately named this session |

---

## 6. Acoustics / harmonics / Goldstone-counting cluster

| Ref | Tier | LB/ILL | Supports |
|---|---|---|---|
| Helmholtz, H. von, *Die Lehre von den Tonempfindungen* (1863) — beat/roughness theory | **[A-cited-not-reverified]** — the session's own citation trail goes through the modern re-derivation (Plomp & Levelt 1965) rather than the 1863 original; cite the modern paper as primary, Helmholtz as historical origin | ILL | The "roughness not consonance" framing for the inharmonic carrier comb |
| Plomp, R. & Levelt, W.J.M., "Tonal Consonance and Critical Bandwidth," *J. Acoust. Soc. Am.* **38**, 548 (1965) | **[A-cited-not-reverified]** — standard, well-known psychoacoustics paper (URL resolves to the real MPI-hosted PDF) | LB | Modern quantitative beat/roughness criterion applied to the {121,208,294} kHz comb |
| Greene, J.M., "A method for determining a stochastic transition," *J. Math. Phys.* **20**, 1183 (1979) | **[A-cited-not-reverified]** — real, standard KAM/Greene's-residue-criterion paper (matches task brief's "Greene 1979 (KAM)") | LB | The "golden ratio = most-irrational / last-KAM-torus" robustness framing for the heartbeat detuning |
| Berry, M.V. (2004), fractional/singular optical vortices | **[UNVERIFIED — locate exact 2026-09-01-session citation before use]** — the task brief names this but I could not find a formal author/journal/year citation for a "Berry 2004" paper actually invoked in the six 2026-09-01 reopening docs (the project's existing ledger already has a *different* Berry citation, `berry1984`, Proc. R. Soc. A 392, 45, on geometric/Berry phase — not the same paper). **Do not fabricate a "Berry 2004" reference** — if fractional-vortex optics is wanted for the paper, the standard citation would be M.V. Berry, "Optical vortices evolving from helicoidal integer and fractional phase steps," *J. Opt. A* **6**, 259 (2004) — **flagged as plausible but not independently confirmed as actually used this session; verify before citing** | — | (not yet load-bearing in this session's own work) |
| Watanabe, H. & Brauner, T., "Number of Nambu-Goldstone bosons and its relation to charge densities," *Phys. Rev. D* **84**, 125013 (2011) | **[A-verified-this-session]** — confirmed exact volume/page/year; note task brief said "2012," the correct year is **2011** | **LB** | The Goldstone-counting theorem behind the D+1=4 supersolid-mode count tested (and left [S], not elevated) in `TWO_SECTOR_UNIFICATION_TEST_2026-09-01.md` §D |
| Andreev, A.F. & Lifshitz, I.M. (1969) | **[already in ledger `andreevlifshitz1969`]** | LB | Supersolid concept + D+1 Goldstone count, companion to Watanabe-Brauner |
| Hofstadter, D.R., "Energy levels and wave functions of Bloch electrons in rational and irrational magnetic fields," *Phys. Rev. B* **14**, 2239 (1976) | **[A-cited-not-reverified]** — the canonical Hofstadter-butterfly paper; the session's `BIG_PICTURE_DUAL_FRACTAL_ELEVATION_2026-09-01.md:72-79` cites only a review article (arXiv:1408.1006) rather than Hofstadter's own original paper | LB (for the "fractal-spectrum + integer-Chern, no anyons" claim) | **Gap to fill**: the session doc cites a *review* of Hofstadter's result, not Hofstadter (1976) itself — add the original for the final bibliography |
| Yarmchuk, E.J., Gordon, M.J.V. & Packard, R.E., "Observation of Stationary Vortex Arrays in Rotating Superfluid Helium," *Phys. Rev. Lett.* **43**, 214 (1979) | **[A-cited-not-reverified]** — real, well-known result | LB | Abrikosov-type triangular vortex-lattice ordering precedent, cross-checked against the EVO's own computed lattice spacing |
| Abo-Shaeer, J.R., Raman, C., Vogels, J.M. & Ketterle, W., "Observation of Vortex Lattices in Bose-Einstein Condensates," *Science* **292**, 476 (2001) | **[A-cited-not-reverified]** — real, famous BEC vortex-lattice imaging paper | LB | Same-class analogue, >100 vortices imaged |
| Thomson, J.J. (1883), N-vortex-polygon stability | **[A-cited-not-reverified]** (classical result; modern rigorous treatment Cabral & Schmidt 1999) | LB, but **explicitly tested and found NOT to transfer this session** (2-D point-vortex N≤6 bound fails against Shoulders' observed N~10–12 bead chains — a genuine, stated negative, not papered over) | Bead-chain count analogy — CORRECTED/superseded within the same session by the 3-D linked-Hopf reading |

---

## 7. CMNS persistence / LENR cluster

| Ref | Tier | LB/ILL | Supports |
|---|---|---|---|
| Shoulders, K., *EV — A Tale of Discovery* (1987); 5 US patents (5,018,180; 5,054,046/047; 5,123,039; 5,148,461) | **[already in memory ledger + REFERENCES_VERIFIED_LEDGER `hubler2022` (secondary)]** | LB | Free-EVO µs-lifetime figure and bead-chain morphology — this session's honest flag: **the exact primary-source page/number for "microsecond" could not be independently re-pinned** (Shoulders' monograph is not machine-searchable online); carried forward as the field-standard figure, not re-verified fresh |
| **Focardi, S., Habel, R. & Piantelli, F., "Anomalous heat production in Ni-H systems," *Nuovo Cimento A* **107**, 163 (1994)** | **[A-verified-this-session]** — confirmed real (Springer DOI 10.1007/BF02813080); ~50 W anomalous heat, H-loaded Ni rod | **LB, and genuinely NEW to the project's citation stores** (not previously in `REFERENCES_VERIFIED_LEDGER.md` or the memory CMNS knowledge base) | The ~300-continuous-day persistence anchor used in `EVO_LIFETIME_FROM_FIELD_EVIDENCE_2026-09-01.md` to build the two-clock (object-vs-site) lifetime discriminator |
| Focardi, S. et al., "Large excess heat production in Ni-H systems," *Nuovo Cimento A* **111**, 1233 (1998) | **[A-cited-not-reverified]** (companion paper to the above; not independently re-searched but standard/expected sequel) | LB | Same role, second cell/run |
| Iwamura, Y., Sakano, M., Itoh, T. (2002) | **[already in ledger `iwamura2002`]** | LB | D₂-permeation transmutation; ~1-week continuous-run persistence anchor |
| Mizuno, T.; Fauvarque, J.-P. et al., "Abnormal excess heat observed during Mizuno-type experiments" (lenr-canr.org preprint) | **[already in memory ledger, tiered "reported, multi-group, several independent replications of the qualitative effect"]** | LB | Tens-of-thousands-of-seconds sustained-run persistence anchor |
| Storms, E. (2010, 2012) NAE | **[already in ledger `storms2010`]** | LB | Days-weeks NAE-crack persistence framing |
| Miley, G.H. & Patterson, J.A., "Nuclear Transmutations in Thin-Film Nickel Coatings Undergoing Electrolysis," *J. New Energy* **1**(3), 5 (1996) | **[A-cited-not-reverified]** — session doc states "read in full"; *J. New Energy* is a non-mainstream but real, historically-cited LENR-era venue | **LB** — the four-humped bidirectional mass-distribution evidence the EVO-fissility fragment-spectrum prediction (R31/R32) is checked against | Not independently re-searched this session (self-published-adjacent venue; flag venue tier honestly if used) |
| Srinivasan, M., "Transmutations and Isotopic Shifts in LENR Experiments — An Overview," *J. Condensed Matter Nucl. Sci.* **13**, 495–504 (2014) | **[A-cited-not-reverified]** — JCMNS is the field's standard peer-reviewed venue | LB | Consolidating review the transmutation-lit pass draws its Miley/Karabut/Savvatimova summaries through |
| Karabut, A.B. & Savvatimova, I.B. — glow-discharge up/down transmutation | **[A-cited-not-reverified]** — Savvatimova, "The Phenomenon of Artificial Radioactivity in Metal Cathodes under Glow Discharge Conditions," *Physics of Particles and Nuclei* (Springer), DOI 10.1134/S1063779622010051; Savvatimova & Karabut, *Poverkhnost'* (1996) 63–75 [secondary-paraphrase, original Russian not independently re-read] | LB | The bidirectional (fission-and-capture in one system) transmutation evidence, and the explicit counter-report that "clean, no radioactivity" is NOT uniform across the LENR transmutation literature |
| Urutskoev/Ivoilov/Adamenko "strange radiation" | **See §1 monopole cluster above** (Ivoilov 2006, Fredericks 2015, Urutskoev 2000) — cross-listed here per the task brief's own grouping | LB (as a CMNS-adjacent phenomenology cluster) | — |
| Widom, A. & Larsen, L. (2006) | **[already in memory ledger]** | LB (contrastive) | See §2 |
| Volodin, A.P., Khaikin, M.S. & Edelman, V.S. (1976); Ancilotto, F., Barranco, M. & Pi, M., "Stability of multielectron bubbles in liquid helium," *Phys. Rev. B* **78**, 014511 (2008), arXiv:0801.3954 | **[A-cited-not-reverified]** | ILL | A real condensed-matter multielectron-bubble precedent cited alongside the Hopf-soliton fermionic-quantization discussion (structural-analogue role, not identity) |

---

## 8. Do-not-cite list (carried forward + session additions)

**Already flagged field-wide** (from `reference_cmns_lenr_field_knowledge_base.md`): A. Rossi/E-Cat (commercial,
unverified calorimetry); R. Mills/hydrino (distinct, mainstream-rejected non-nuclear claim, do not conflate
with LENR); "biological transmutation" (Kervran, no accepted mechanism).

**Session-specific do-not-cite / cite-with-explicit-caveat-only:**
- **Cramer, "When Proton Meets Monopole," *Analog Science Fiction and Fact* (1984)** — a popular-science
  magazine article, not peer-reviewed; cite only as "the popularization the field's negative checks against,"
  never as a physics source in its own right (see §1 table).
- **Vishnevskii (2008)** — non-independently-verifiable, Russian-language, self-published-adjacent source
  reaching the paper's citation pool only via Bob Greenyer's own translation/description. Cite explicitly as
  "the primary source Greenyer's program itself cites," with that provenance stated — never present it as an
  independently-vetted physics paper.
- **Adamenko & Vysotskii's own quoted monopole-mass figures** ("≈10⁻²³ g" vs "≈560 GeV" for the *same*
  quantity) — the session's own re-check found these two figures internally inconsistent by ~100×. If cited
  at all, flag this inconsistency explicitly; do not silently pick the more convenient of the two numbers.
- **"Bertsch, Younes et al."**, **"Danon et al."**, **"Ellis, J. et al."** as author-list forms — see §0
  corrections; these specific *author attributions* should not propagate into the paper's bibliography.

---

## 9. Items flagged UNVERIFIED — locate before use

- Businaro & Gallone (1955) — exact original journal/volume not independently repinned (§4).
- "Berry 2004" fractional-vortex-optics paper — not found actually cited in the six 2026-09-01 session docs
  under this description; do not add to the bibliography until a specific project doc is found using it, or
  drop it from the task's topic list if it was a suggested-but-unused addition (§6).
- Euler-Heisenberg (1936) original citation — the session's QED-null *calculation* is done and correct, but
  the textbook Lagrangian citation was not separately named this session (§5) — add at final lock if the paper
  references the Euler-Heisenberg Lagrangian by name.
- Hofstadter (1976) original paper — session doc cites a modern review instead of the primary 1976 PRB paper
  (§6) — straightforward fix, add the primary citation.

---

## Summary counts

- **[A-verified-this-session]**: 13 (Lochak 2007/arXiv, Fryberger SLAC-PUB-13583/6473, MoEDAL Nature+PRL,
  Ray 2014, Castelnovo 2008, Ralston 2024, Son-Surówka 2009, STAR isobar (2 papers), Skokov 2009,
  Auckly-Speight 2006, Watanabe-Brauner 2011, Scamps-Simenel 2018-corrected)
- **[A-primary-read-this-session]**: 2 (Ivoilov 2006, Fredericks 2015 — both read in full via WebFetch by the
  session's own agents)
- **[A-cited-not-reverified]**: ~45 (standard/canonical 20th-century physics + several real-but-not-re-searched
  CMNS papers; see per-section tables)
- **[already in REFERENCES_VERIFIED_LEDGER.md or memory ledger]**: ~20 (not re-tabled in full; cross-referenced)
- **[do-not-cite]**: 3 flagged explicitly, plus the 3 field-wide standing entries
- **[UNVERIFIED — locate before use]**: 4 (Vishnevskii as independent source, Businaro-Gallone exact journal,
  "Berry 2004," Euler-Heisenberg original, Hofstadter original — 5 total, one double-counted across sections)
- **Corrections found (real paper, wrong byline/volume)**: **4** — MoEDAL volume/page, Gould-Rajantie
  misattributed to "Ellis," Bartalucci-Vysotskii-Vysotskyy misattributed to "Danon," Scamps-Simenel
  misattributed to "Bertsch-Younes." All four are pure bibliographic-pointer errors; no physics conclusion in
  the session docs is affected, but none should be copied into the paper's reference list as currently written.

No citation was fabricated to close a gap in this harvest; every entry above traces either to a session
document's own citation, to `REFERENCES_VERIFIED_LEDGER.md`/the memory CMNS ledger, or to a live search result
recorded in this file.
