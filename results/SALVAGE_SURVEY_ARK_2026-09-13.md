# Salvage survey — ckfreefem ark & citation stores (frozen record, 2026-09-13)

**What this is.** The verbatim survey digest from the read-only sweep of the extended corpus
(`C:\Users\natha\ckfreefem\`) that identified what the jewel lacked: the vendored citation stores
(`frontier_calcs/REFERENCES_VERIFIED_LEDGER_2026-08-28.md`, `PAPER_PREP_CITATIONS_2026-09-01.md`,
`greenyer_61_entry_catalog_slice.md`), the ark salvage scripts, and the `REFERENCES.md` §1e–1j fold.
**Frozen provenance record.** Note: `08_references/` in the corpus is **empty** — the real citation stores
are the two `03_paper/main_draft/` files above. The ranked fold recommendations (§E) are the working list
for future sessions; items 1–4 were executed 2026-09-13, the rest are named-not-yet-folded.

---

## A. ARK inventory (`11_verified_ark\`, 10 entries)

**A1. iccf27_evo_d4d** — `verified_core\CORE_STATUS.md` (2026-07-12) is the authoritative verdict: the
original EVO/D4D LENR core is **mostly RETRACTED** — Beat Law absolute-frequency match (μ_A back-solved to
0.0003%), R*/n_e (citation error: Shoulders' real range 100nm–20μm, not ~10nm), AB gate (premise traces to
a real Dirac-1931 flux-quantization error), barrier closure (G_req back-solved), neutron floor,
ponderomotive P_diss (B_0 tuned per grid point). Survivors: cascade scaling theory (moved to A3's lineage)
and the **two-electron ring Madelung reduction** (`scripts\two_electron_ring_madelung.py` — ×4 ratio from
first-principles QHD, "real, exact, keeper" — now vendored). Citations carried: Kasagi 2000 (screening),
Czerski 2022 *PRC*, Dubey et al. 2025 *PRX*, Szpak/Mosier-Boss SPAWAR morphology, Letts-Cravens THz.
`salvage_notes\audit_methodology_and_retraction_chain.md` documents the 3-layer retraction chain
(LOCKED_NUMBERS_TABLE → GOLDEN_VALUES.md → CORE_STATUS.md) + reusable back-solve-detection audit method.
**In jewel: partial** → citations folded 2026-09-13; script vendored.

**A2. greenyer_toroidal_beat** — the locked ICCF27 paper
(`ICCF27_SELF_SIMILAR_TOROIDAL_BEAT_MADELUNG_FULL_PAPER.tex`), the
`TORUS_BEAT_TRIPLET_MADELUNG_MINIMUM_VIABLE_THEORY.md` (linked-torus mutual-inductance symmetry rule,
triplet spectra, Madelung agreement to 4 decimals), conceptual essay, **61-entry per-citation verified
catalog** (every entry status-tagged VERIFIED-REAL/USED — now vendored), and 4 headline scripts incl. the
**Cho-Maison electroweak monopole solve** (now vendored). **In jewel: partial** — beat-dynamics layer is
M14 `[V]`; the fissility, time-crystal, engineering-precedent, ponderomotive, and NLFFF citation clusters
folded 2026-09-13 (fissility + time crystals in REFERENCES §1h/§1i).

**A3. self_similar_cascade** — locked 41pp LENR-free applied-math paper + `MINIMUM_VIABLE_VERIFIED_CORE.md`,
a 3-way-check ledger: (1) general cascade scaling theorem `Q_L/Q_{L+1}=N^{ac+b}` **fully verified**
(symbolic + independent log-derivative route); (2) `c_CK(3D, ε=0.20)≈1.11–1.16` at 2.5/3 (pipeline
reproducible, scipy cross-check real, external validity only order-of-magnitude via **Zanca & Terranova,
PPCF 46, 1115 (2004)** — folded to REFERENCES §1e); (3) beat ladder `f_b∝N^L` + validity-boundary theorems
(particle floor, plasmoid-instability ceiling, S_crit~1e4 from Bhattacharjee 2009). Plus
`STAGE3_CK3D_CLOSURE_VERIFIED_2026-08-13.md` and stage3 FEM scripts. **In jewel: partial** — c_CK present;
the MVVC ledger and scaling-theorem proof script remain future folds.

**A4. cascade_vacuum_bridge** — single live doc: **winding number exactly conserved under FPUT collapse**
(positive); Burgers-vector correspondence **RULED OUT**; plus §0's three-way status restatement of Reed
(K_PV RULED OUT per tested version; Ch.17 lineage CONFIRMED-accurate; α formula OPEN), Nielsen
(lepton-mass out-of-sample 0.11σ CONFIRMED; W-mass ESTIMATE), Greenyer. **In jewel: partial** — verdicts
absorbed at module level; the FPUT winding result is a named future fold.

**A5. dislocation_core** — positive-only status doc: trapped D at measured Pd dislocation-core density
(**Heuser et al. 1991, Acta Metall. Mater. 39, 2815**) gives Γ=196.7, deep Wigner-crystal regime,
CONFIRMED; **generalized N-mode Woltjer theorem** (fixed-helicity minimization is a linear program; minimum
always the single lowest-eigenvalue pure mode — verified symbolically N=4 and on the real 40-mode spectrum)
⇒ "regeneration must outpace Taylor relaxation" is generic; **>99.7% s-wave entrance channel** (3 methods
agree); mobility-bottleneck-bypass claim DOWNGRADED (honest 4-reason teardown). **In jewel: no** — the
N-mode LP theorem + Heuser input are the top-ranked future fold (named in HISTORY §3).

**A6. dynamical_plasmoid** — both-era doc + salvage split. Real survivors: heartbeat-not-flywheel §6
thesis; ball-lightning closures (sustaining power <0.5W, **Abrahamson & Dinniss** silicon-combustion
precedent — folded to REFERENCES §1f; ionization order parameter `n_ss=√(S/α_DR)`); **Eshelby-tensor
theorem: torsional-mode→fusion-rate coupling exactly zero**. Retracted list mirrors A1 plus a Bostick
misattribution and FTG/ZPE claims. **In jewel: partial** — driven/heartbeat is jewel core; the Eshelby
theorem is a named future fold.

**A7. plasmoid_beat_lenr** — verdict NEGATIVE for direct phonon-nuclear coupling: Gamow suppression
G~90.35 confirmed 3 independent ways incl. Hagelstein's own published matrix element; Dicke √N would need
~1e104 coherent sites vs ~1e12 available. §12 non-nuclear ponderomotive/dissipative-structure heat channel
is the honest survivor (with A1's later caveat that the P_diss grid itself was tautological). **In jewel:**
the settled-negative is now recorded in `HISTORY_PEOPLE_EVO_CMNS.md` §3.

**A8. helium_heat_nuclear_extensions** — 6 Hopf-soliton scale-fixing attempts all failed (settled-negative
with diagnosed reasons); **Widom-Larsen tested and RULED OUT 3 independent ways**; capstone: "nuclear
coupling and plasmoid environment are different jobs" (4 environment mechanisms each fail by quantified
margins). Survivor: **Sector A** (`SECTOR_A_ENVIRONMENT_THEORY.md` — now vendored) — verified m=1 Beltrami
eigenmode + solved Madelung ring + **exact closed-form OAM ratio `R = π m_e R_L² f_L / ħ`**. **In jewel:**
negatives recorded; Sector-A form vendored, its fold into the OAM thread is a named future item.

**A9. topological_monopole_program** — six angles all NEGATIVE for connecting Greenyer geometry to
Rubakov-Callan nucleon decay, incl. the decisive topological argument: **Hopf invariant classifies π₃(S²),
monopole charge classifies π₂(S²) — different invariants of different maps**. One real artifact survives:
the from-scratch **Cho-Maison monopole BVP solve** (Cho & Maison, *Phys. Lett. B* 391, 360, 1997 — now
vendored). **In jewel:** the closure is recorded in REFERENCES §1j + HISTORY §3.

**A10. _governance** — `VALIDATION_RULES.md`: the **TVR two-check protocol** (V1 script validation <0.5% +
V2 independent method). `BEST_LESSONS.md`: derivation-vs-overfitting lessons (circular derivations labeled;
near-integers documented not promoted; two same-number routes must be proven equivalent). **In jewel:
embodied** — the verify harness + COINCIDENCE_LEDGER practice matches; cite, don't duplicate.

---

## B. CITATIONS harvest — the three stores

**Store 1: `03_paper\main_draft\REFERENCES_VERIFIED_LEDGER.md`** — 348 lines, ~198 rows, every row tagged
`[V]` (live-verified) / `[T]` (textbook-canonical) / `[P]` (project). **Vendored 2026-09-13.**
**Store 2: `03_paper\main_draft\PAPER_PREP_CITATIONS_2026-09-01.md`** — 13 `[A-verified-this-session]`,
2 primary-read-in-full, ~45 cited-not-reverified, plus **4 bibliographic corrections** (MoEDAL is *Nature*
**602**, 63 (2022), not 604/64; arXiv:1705.07052 is **Gould & Rajantie**, PRL 119, 241601, not "Ellis et
al."; PRAB 22, 054503 (2019) is **Bartalucci-Vysotskii-Vysotskyy**, not "Danon"; the pear-shaped-fission
paper is **Scamps & Simenel, Nature 564, 382 (2018)**, not "Bertsch-Younes 560, 205") and a do-not-cite
list (Cramer *Analog* 1984; Vishnevskii 2008 as independent source; the inconsistent Adamenko
monopole-mass figures; Rossi/Mills/Kervran standing). **Vendored 2026-09-13.**
**Store 3: `2862026\all_references_doc.md`** — 35 clean entries for the GST/TST draft (not vendored;
superseded lineage).

Key clusters folded into `REFERENCES.md` §1e–1j (2026-09-13): LENR/CMNS experimental canon (Miles 1993,
McKubre, Hagelstein-Letts-Cravens 2010, Iwamura, Szpak/Mosier-Boss, Kasagi/Czerski/Dubey screening,
Berlinguette 2019 null, Focardi-Piantelli, Storms, Benyo/Steinetz LCF, Widom-Larsen + ruled-out note,
Klimov, strange-radiation chain, Rukhadze-Grachev); fissility cluster (Rayleigh 1882, Bohr-Wheeler 1939,
Duft 2002 *PRL* + Duft 2003 *Nature* do-not-merge pair, Hill-Eaves 2012, Liao-Hill 2017, Wong 1973);
dissipative time crystals (Kongkhambut 2022, Wu 2024, Liu 2025); CK-photon prior art (Moses 1971,
Lakhtakia 1994, Marsh 1996, Yoshida-Giga 1990, **Tuchin PRC 93, 054903 (2016)**, **Xia-Qin-Wang PRD 94,
054042 (2016)**, Amari-Boulmezaoud-Mikić 1999); anapole (**Afanasiev & Stepanovsky J. Phys. A 28, 4565
(1995)**, Devaney-Wolf PRD 8, 1044 (1973), Radescu-Vaman PRE 65, 046609 (2002), Miroshnichenko Nat.
Commun. 6, 8069 (2015)); spheromak stability (Rosenbluth-Bussac 1979, Bondeson 1981, Belova 2000);
ball-lightning anchors (Stenhoff 1999, Rañada-Trueba 1996/2000, Cen-Yuan-Xue 2014, Peacock-Norton 1975,
Abrahamson-Dinniss 2000); monopole (MoEDAL 602, 63 corrected + PRL 133, 071803 (2024), Milton RPP 69,
Cho-Maison PLB 391). Remaining in the vendored stores (not individually folded): McKubre ICCF-4/ICCF-8/
JCMNS 15 details, Letts-Cravens ICCF-10, Toyota 2013, Li PRC 61 selective resonant tunneling, Takahashi
TSC, Vysotskii-Vysotskyy EPJ A 49, Preparata 1995, Hagelstein arXiv:2501.08338, Miley-Patterson (venue-tier
caveat), Srinivasan, Karabut-Savvatimova [unverified primary], Tsui 2003, Fryberger SLAC-PUB, Ralston
arXiv:2411.00240, Jaitner JCMNS 33, Lerner physics/0401126, Lochak Z. Naturforsch. A62 = arXiv:0801.2752,
Ivoilov AFLB 31, 115 (2006), Fredericks JCMNS 15, 203 (2015), Gaponov-Miller 1958 (ponderomotive origin),
Wiegelmann-Sakurai LRSP 9, 5 (NLFFF λ_eff), DuHamel-Isbell 1957 (log-periodic antennas), Faddeev J. Phys.
A 35, L133 (2002), Auckly-Speight CMP 263, 173 (2006), Kleckner-Irvine (already in), Watanabe-Brauner PRD
84, 125013, β-PdD phonon data (Rush 1966; Ikeda-Watanabe 1978 [unverified]).

---

## C. EVO/LENR history material preserved (corpus pointers)

1. **`EVO_LENR_PAPER_FINAL.md` §12** (~lines 877–910) — compact honest 1989→present narrative + 27-entry
   reference list (physics superseded by A1 retractions; history stands).
2. **`03_paper\main_draft\matsumoto\`** — ~25 primary-source Takaaki Matsumoto PDFs (1989–2000): Nattoh
   model (1989), "Cold Fusion Observed with Ordinary Water" (1990), discharge traces (Minsk 1994, EPRI
   1994), micro-craters 1991-95, Itonic cluster acceleration (2000). Plus **the full Shoulders monograph**
   (`EV A Tale of Discovery - Kenneth R. Shoulders.pdf`, 1987) and the Greenyer Bergamo lecture.
3. **Strange-radiation chain** with provenance caveats: Urutskoev 2000/2002 → Ivoilov 2006 → Fredericks
   2015, theory Lochak; Vishnevskii-2008 "cite as the source Greenyer's program cites."
4. **Greenyer/MFMP primaries**: ICCF-25 Szczecin talk (2023) [real, no peer-reviewed pub located]; Huang
   et al. *Sci. Rep.* 2024 [real, carries an Editor's Note — do not treat as confirmed]; the flagged
   **"MFMP Technical Report 2018" citation FAILED verification — do not rely on it**.
5. **`ACKNOWLEDGEMENTS_AND_INSPIRATIONS.md`** — inspiration-vs-source distinctions for
   MFMP/Greenyer/Reed/Nielsen (a model of the honesty discipline applied to community history).
6. **The retraction chain** (`iccf27_evo_d4d\salvage_notes\audit_methodology_and_retraction_chain.md`) +
   `_governance\BEST_LESSONS.md` — the program's self-correction record.

## D. PDF/report inventory (distinct holdings; 1138 PDFs total, mostly build artifacts)

- `matsumoto\` — ~25 Matsumoto primaries + Shoulders book + Greenyer Bergamo lecture.
- `Reed-QWM\` — QWM 4th ed. + ~40 per-chapter PDFs + **NielsenTUFT.pdf (290pp — larger than the jewel's
  180pp copy)** + TeslaScalarWaveGeometry.pdf.
- `Section Science\` — Davis DIRDs (Teleportation 2003, Wormhole 2000 — historical context at most, not
  physics), **ReedHively2020.pdf** (*Symmetry* 12, 2110 — the one peer-reviewed Donald-Reed-thread paper).
- Corpus root — the ICCF/TGST/TST paper-lineage fossil record (v1.0→v3.28 of the retracted framework).
- `main_draft\` — FTGB series builds + CRYSTAL_EVO_CMNS_LOCKED_2026-08-27.pdf +
  EXPERIMENT_NEARFIELD_FLUX_BEAT_PROPOSAL_2026-08-30.pdf (benchtop proposal — check jewel equivalence).

## E. RECOMMENDED folds (ranked; status as of 2026-09-13)

1. ✅ Vendor the two citation stores + merge absent clusters into REFERENCES.md — **done**.
2. ✅ Vendor the 61-entry Greenyer catalog (M14 citation appendix) — **done**.
3. ✅ Cite Afanasiev-Stepanovsky 1995, Tuchin 2016, Xia-Qin-Wang 2016, Zanca-Terranova 2004 — **done** (§1e).
4. ✅ Vendor `two_electron_ring_madelung.py` + `cho_maison_real_monopole_solve.py` + the monopole
   settled-negative closure — **done**.
5. ✅ Sector-A closed form (`R = π m_e R_L² f_L/ħ`) — **folded** (`sector_a_oam_ratio_check.py`, the
   `n_e` cancellation verified to 2e-16; joins the anapole-resonator OAM thread).
6. ✅ Tiered EVO/LENR history file — **done** (`HISTORY_PEOPLE_EVO_CMNS.md`, pointing at corpus PDF paths).
7. ✅ **N-mode Woltjer LP theorem + Γ=196.7/Heuser 1991** — **folded** (`nmode_woltjer_lp_check.py`:
   theorem verified on the jewel's 40-mode CK spectrum + near-degenerate spectrum + 20000 mixtures;
   Γ=196.7 reproduced from the Heuser density; "heartbeat not flywheel" generic → TIER_LEDGER §1).
8. ✅ Settled-negative imports — **folded** (`corpus_settled_negatives_check.py`: Gamow/Dicke, monopole
   π₂-degree computed, Widom-Larsen field requirement, Burgers classes) + the FPUT winding result
   (`fput_winding_conservation_check.py`, protection + boundary). Still corpus-only: 6 Hopf
   scale-fixings, D-ion heating, Thomson N≤6 (recorded in HISTORY §3).
9. ✅ Governance — **folded** (COINCIDENCE_LEDGER preamble: two-routes-must-prove-equivalence,
   near-integer discipline, self-consistency≠derivation, topology-check-before-machinery; the
   scalar-EM/Whittaker closure → REFERENCES §3). TVR superseded by the harness — cited, not duplicated.
10. ❌ Skip: all retracted EVO/D4D machinery (N_flux=896, CET routing, Channel B×C, G_eff/G_req,
    52.351 THz); the 1283-script `main_draft\frontier_calcs\` wholesale; superseded archive PDFs; DIRD
    material as physics; the Hagelstein 2025 "in press" citation until independently located.
