# TOOLKIT ADV — Module M11: EGM / POLARIZABLE-VACUUM SPECTRAL METHODS (as REPRESENTATION-MAP, not theory)

Part of the FTGB math toolkit (see `MATH_TOOLKIT_BASE.md`, the M7–M10 modules, and
`FTGB_TOOLKIT_PROGRAM_PLAN`). This module folds in the **mathematical machinery** of Riccardo Storti's
*Electro-Gravi-Magnetics* (EGM) / *Quinta Essentia* series — the **polarizable-vacuum refractive-index
representation** and the **ZPF Fourier harmonic-beat spectrum** — as a *method and notation map*, and audits
its numerical claims against the project's honesty discipline. Every checkable number below is **computed**
(not restated) by `results/verify/egm_sense_checks.py`. Primary source: Storti, *Quinta Essentia — Part 2*
(Delta Group Engineering / Lulu, 2007; 328 pp.), the summary of Parts 3–4, read directly.

> **THE ONE LIMIT, STATED UP FRONT (read before using any result here).** EGM is — *in Storti's own words*
> (Part 2, §7.2.24) — **"A method of calculation (not a theory) based upon energy density"** that "does not
> favour or bias any particular theory." We therefore borrow it **exactly as a representation/bookkeeping
> method** (a Fourier harmonic encoding of a polarizable-vacuum energy-density gradient) and **adopt none of
> its physical predictions**. Its foundations (Puthoff's polarizable vacuum; the ZPF cubic spectrum of
> stochastic electrodynamics; Buckingham-Π) are established and are credited as such. Its *numerical outputs*
> (particle radii to 0.01%, H₀ = 67.08, α from geometry, the `e^(-2/3)` screening factor) are **NOT** adopted:
> §M11-4 shows the clean closed-forms do not reproduce them, so they are fits / full-numeric artifacts / open
> problems, not derivations. This continues the M7 tier `[UNASSESSED/fringe, method-only]` for Storti and the
> project's standing **excision** of the `e^(-2/3)` factor.

## Tier legend (honesty discipline)
- **[V]** verified here by `results/verify/egm_sense_checks.py`, `results/verify/egm_mode_count_closure.py`
  (the M11-6 mode-count closure), or a checked identity.
- **[credited]** established physics we build on: Puthoff (PV representation of GR); Sakharov / Haisch–Rueda–
  Puthoff (ZPF inertia/gravity); the SED cubic ZPF spectrum; Buckingham 1914.
- **[EGM method]** = Storti's representation/notation borrowed as a *calculation method only* (his own framing).
- **[flag]** = an EGM numerical claim that does **not** follow from a clean closed-form (fit / full-numeric /
  open); named explicitly so it is never cited as derived.
- **[excised]** = the `e^(-2/3)` screening factor — kept out per the standing excision protocol.
- No fabricated numbers. Constants are EGM's own NIST set (Part 2, p.157) where they differ from CODATA.

---

## M11-1 — What EGM actually is (from the primary source)   [credited foundations + EGM method]

- **WHAT (Storti Part 2, Synopsis + §7.2.24, 7.2.58).** EGM replaces GR's "curved" space-time with a
  **refractive** space-time: matter does work on the vacuum, producing a radial **energy-density gradient**
  read as a variable **refractive index `K_PV`** (the *Polarizable Vacuum*, PV). Light slows/bends in the
  `K_PV` gradient exactly as GR predicts; the claimed value-add is a *mechanism* ("why refractive"), not new
  dynamics. This is **Puthoff's PV representation of GR** `[credited: Puthoff 1999, gr-qc/9909037]`:
  `c_eff = c/√K_PV`, and for a static mass `K_PV(r) = exp(2GM/rc²)` (weak field `K_PV ≈ 1 + 2GM/rc²`).
- **THE VACUUM SPECTRUM (Part 2, Preface + §7.2.74, 7.2.79–80).** The vacuum is the **Zero-Point-Field** with
  the **cubic spectral energy density** `ρ₀(ω) = ħω³ / (2π²c³)` `[credited: SED; Sakharov 1968; Haisch–Rueda–
  Puthoff]`. **[V]** integrating it to the Planck frequency returns a Planck-scale energy density (script §1) —
  the standard ZPE spectrum, correctly reproduced.
- **THE EGM CONSTRUCTION (Part 2, §7.2.25, 7.2.32–36, 7.2.43–45).** EGM represents the PV energy-density
  gradient of a mass as a **Fourier harmonic-beat series** of ZPF modes — the "EGM/PV spectrum":
  - `ω_PV(1,r,M)` = **fundamental harmonic frequency** (lowest mode),
  - `ω_Ω`, `n_Ω` = **harmonic cut-off (terminating) frequency and mode** (the spectrum is band-limited),
  - `ρ₀(ω)` = energy per mode, `∆ω_δr` = the **fundamental beat frequency** across an elemental displacement.
  Gravity is the beat structure of this band-limited harmonic set. This is the `[EGM method]` — a
  band-limited-Fourier encoding of a scalar field, mathematically ordinary; the physics content is entirely
  in the choice of cut-off closure `n_Ω`.

## M11-2 — The EGM quantity dictionary → standard physics   [EGM method]

| EGM symbol (Part 2 §7.2) | EGM meaning | Standard-physics reading |
|---|---|---|
| `ω_Cx = m_x c²/ħ` | Compton (angular) frequency | Compton frequency — standard `[credited]` |
| `K_PV` (7.2.69) | vacuum refractive index | PV dielectric of GR, `c_eff=c/√K` `[credited: Puthoff]` |
| `ρ₀(ω)` (7.2.74) | spectral energy density / mode | ZPF cubic spectrum `ħω³/2π²c³` `[credited: SED]` |
| `ω_PV(1,r,M)` (7.2.36) | fundamental PV harmonic | lowest mode of a band-limited Fourier encoding `[EGM method]` |
| `ω_Ω, n_Ω` (7.2.43–45) | harmonic cut-off freq/mode | Nyquist-like band limit of that encoding `[EGM method]` |
| `St_β…St_θ` (7.2.84–90) | "sense checks" | Buckingham-Π dimensionless ratio tests `[credited: Buckingham]` → **M7** |
| EGM radius (7.2.65) | ZPF↔mass energy-equilibrium radius | see §M11-4(iii) — Compton-scale `[EGM method]` |
| `γ_g` (7.2.40) | "graviton = conjugate photon pair" | Storti's interpretation `[EGM method]`, not adopted |

> **CORRECTION to `storti_egm_missing.md`.** That secondary note labels `Stη = m_p/m_e = 1836.15`. This is a
> mislabel: Storti's `St_η` (Part 2 §7.2.89) is the **5th sense-check** relating a *proton's* harmonic cut-off
> frequency to the *proton's* Compton frequency — a Buckingham-Π consistency test, not the mass ratio. Use the
> primary definition.

## M11-3 — The four load-bearing maps into the FTGB toolkit   [EGM method → existing modules]

The reason EGM is worth folding in at all: each of its four pillars is the *same mathematics* as an FTGB
toolkit module already carries — so EGM becomes a **cross-check and a shared vocabulary**, not new physics.

1. **`ω_Ω` band-limited harmonic-beat comb ↔ M9 (coupled-oscillator substrate) + the inharmonic carrier
   comb + seesaw down-conversion.** EGM's "mass = a terminating Fourier beat spectrum with cut-off `ω_Ω`" is
   structurally the FTGB coherent object read as a **driven comb of beat modes** (the {121, 208, 294} kHz
   Chandrasekhar–Kendall carrier comb and its 7/4, 5/2 pulls in M9; the seesaw frequency-down-conversion in **M10-4**).
   Both encode a coherent object as a *band-limited harmonic set*; `ω_Ω`↔ the comb's high-mode cut-off,
   `∆ω_δr`↔ the fundamental beat. **Use:** EGM's cut-off-mode bookkeeping is a ready-made way to count the
   FTGB comb's modes; the FTGB comb gives EGM's abstract `ω_Ω` a concrete measured spectrum.
2. **`K_PV` refractive/dielectric index ↔ the RG dielectric-flow control (anti-numerology) + resonator
   `m = ħω/c²`.** `K_PV` is literally a frequency-independent vacuum dielectric; its gradient is the field.
   The toolkit's **RG dielectric-flow** module already handles a running dielectric with a built-in
   anti-numerology test — the correct home for any `K_PV(ω)` dispersion claim (§M11-4). The mass-from-index
   reading `c_eff=c/√K_PV` is the field-side twin of the resonator-family `m = ħω/c²` (mass from a resonance
   frequency), the same duality the `resonator_family.html` model animates.
3. **ZPF cubic spectrum `ρ₀ ∝ ω³` ↔ the "field = matter-wave" vacuum-energy reading.** The band-limited ZPF
   energy density is the physical substrate behind the synthesis's "read the object at once as a field and a
   matter wave." Credited and quantitatively reproduced (§M11-1 [V]); used only as the *energy accounting*
   backdrop, not as a derivation of particle properties.
4. **Sense checks `St_β…St_θ` ↔ M7 (Buckingham-Π claim-audit).** These are exactly M7's dimensionless-ratio
   audits. Fold them in as **claim-audit tools** (which knob a relation is allowed to depend on), never as
   theory generators — the M7 "ONE LIMIT" applies verbatim.

## M11-4 — Honest audit of EGM's numerical claims   [V] by `egm_sense_checks.py`

The value of folding EGM in is *disciplined*: adopt the methods, quarantine the numerology. Each headline
EGM "prediction" was recomputed:

- **(i) The "2:1 harmonic" `ω_Ω(e) = 2·ω_Ω(p) = ω_CP²/ω_Ce`.** **[flag — definitional.]** If `ω_Ω(e)` is
  *defined* as `ω_CP²/ω_Ce` and `ω_Ω(p)` as half of it, the 2:1 ratio is true **by construction** (script
  returns exactly 2.000), not an independent prediction. Interesting as a mnemonic; not evidence.
- **(ii) Proton RMS charge radius to ~0.01%.** **[flag — not a closed-form.]** The simple published forms
  (`(3/4)λ_CP²/λ_Ce`, `(5/4)λ_CP²/λ_Ce`, `n_Ω λ_CP/2π`) miss 0.84 fm by factors **10³–10⁴** (script §3). The
  quoted 0.01% match therefore does *not* follow from a clean formula — it is a full-numeric solution of the
  cut-off closure or a fit. Do not cite as a parameter-free derivation.
- **(iii) EGM radius = ZPF↔mass energy-equilibrium (§7.2.65).** Honest reconstruction (set uniform-sphere
  mass-energy density = ZPF energy density at `ω_C`) gives `r_eq = 0.42 λ_C` for *every* particle (script §4):
  a clean **Compton-scale** length (proton `r_eq ≈ 0.56 fm` vs charge radius 0.84 fm — right order, ~1.5×
  off). So the *idea* (a ZPF energy-balance radius at the Compton scale) is physically reasonable `[EGM
  method]`; the *precision* claim needs the full `n_Ω` machinery and is not reproduced by the balance alone.
- **(iv) H₀ = 67.08 km/s/Mpc from a cosmic cut-off.** **[flag — order-of-magnitude + fudge.]**
  `ω_cos ~ √(GM_u/R_u³)` gives H₀ ~ 9 km/s/Mpc (script §5); reaching 67 needs an unmotivated ×7.8 (the
  secondary doc used ×1.82 off sloppier inputs). The precise value is not derived this way. *(Storti's
  separate historical priority claim — a ΛCDM-like ~67 published in 2008 — is not verifiable from here and is
  left unassessed.)*
- **(v) α from toroidal winding (140.2) via `e^(-2/3)` screening.** **[excised.]** `e^(-2/3)=0.513` maps
  140.2→71.98 — nowhere near 137.04 — so `e^(-2/3)` does not even produce the required 2.3% correction
  (script §6). Per the standing excision protocol, the factor stays **out**; the 140.2 vs 137.036 (2.3%) gap
  is carried as an **open problem**, not a screening "derivation."

**Net:** fold in EGM's *representation* (PV index, ZPF harmonic-beat comb, sense-checks) and its *credited
foundations*; carry every numerical "prediction" at `[flag]`/`[excised]`. Nothing in §M11-4 is promoted.

## M11-5 — The one limit, restated (use / do-not-use)
- **USE** as: a shared vocabulary and cross-check for the FTGB comb (M9), a home for `K_PV(ω)` dielectric
  questions (RG flow), the ZPF energy backdrop, and Buckingham-Π sense-checks (M7). All method, no adopted
  claim.
- **DO NOT USE** as: a source of particle radii, mass ratios, α, or H₀ "derivations." EGM is Storti's stated
  *calculation method*; its numerology is `[flag]`/`[excised]` here and must never be cited as FTGB-derived.

## M11-6 — The spectral mode-count closure: constructing `ω_Ω` and its length   [credited: Debye/Nyquist mode-count + EGM method]

M11-1 names `ω_Ω, n_Ω` as the harmonic cut-off frequency/mode but leaves the *closure* — how `n_Ω` is fixed —
a black box ("the physics content is entirely in the choice of cut-off closure `n_Ω`"). The reusable technique
behind that closure is a **spectral mode-count band-limit**, foldable as *method only* because it is the
ordinary **Debye-frequency / Nyquist mode-count** construction — not new physics. Reproduced by
`results/verify/egm_mode_count_closure.py`.

- **WHAT (Storti Part 2, §7.2.43–45, with the spectrum §7.2.74, 7.2.79–80; the radius §7.2.65).** Band-limit
  the ZPF harmonic set by counting its modes and terminating at a chosen count; read a length from the
  cut-off. This is the same construction that fixes a Debye frequency from a mode budget `[credited]`.
- **CONSTRUCTION (method, no values).** From the credited cubic spectrum `ρ₀(ω) = ħω³/(2π²c³)` (M11-1), the
  energy-per-mode is `~ħω`, so the **mode density** is `g(ω) = ρ₀(ω)/(ħω) ∝ ω²/c³` — the ordinary free-field
  3-D density of states. Define an **integrated mode count** to a trial band limit `Ω`,
  `N(Ω) = ∫₀^Ω g(ω) dω ∝ (Ω/c)³` (per volume; `∝ (Ωℓ/c)³` in a region of scale `ℓ`). **Terminate** the set by
  *fixing that count to an integer* `n_Ω`; the closure returns the cut-off `ω_Ω`, and a characteristic length
  is its wavelength `ℓ ~ 2πc/ω_Ω`. Structurally identical to the Debye cut-off and to a band-limited signal's
  Nyquist mode number. **[V]** `egm_mode_count_closure.py` confirms the quadratic DOS, `N(2Ω)/N(Ω)=8`, and the
  cube-root closure exactly.
- **DIMENSIONAL CONTENT.** `g(ω) dω` and `N` are dimensionless counts; `ω_Ω` is `[T⁻¹]`; `ℓ ~ c/ω_Ω` is `[L]`.
  **No new constant enters** — the length is fixed by `{c, the cubic shape, the chosen count}` alone. Referred
  to the object's Compton frequency `ω_C` (the natural scale, M11-2), the cubic count gives `N ∝ (ω_Ω/ω_C)³`,
  so the closure fixes `ω_Ω/ω_C ∝ n_Ω^{1/3}` and hence `ℓ ~ c/ω_Ω ∝ λ_C/n_Ω^{1/3}` — a **Compton-scale**
  length, which is *why* the independent energy-balance reconstruction in M11-4(iii) also lands at the Compton
  scale.
- **THE FREE CHOICE (load-bearing caveat).** All content sits in the **boundary-condition choice of `n_Ω`**;
  the theorem-like part fixes only the *scaling* (`ℓ ∝ c/ω_Ω`, `ω_Ω ∝ n_Ω^{1/3}`), never a number — the exact
  analogue of M7-2's "`Λ_n` is an eigenvalue fixed by the boundary condition, not by the theorem." Because
  `ℓ ∝ n_Ω^{-1/3}`, the length is only **weakly** sensitive to the count: a `10×` change in `n_Ω` moves `ℓ` by
  only `0.46×` (`= 10^{-1/3}`, `[V]` in the script), so the Compton **scale** is robust but the **precise**
  value is set by solving the free integer `n_Ω = (k·λ_C/ℓ)³` — a fit knob. This is a structural reason the
  M11-4(ii) sub-0.01% radius "match" **cannot** be read as parameter-free, reinforcing that `[flag]`. Every
  specific `n_Ω`, cut-off frequency, or radius the closure yields is a **value**, quarantined at M11-4, not
  folded here.
- **CROSS-CHECK / USE.** `[credited]` as the Debye/Nyquist mode-count; `[EGM method]` as Storti's closure
  framing. Dovetails with **M11-3 pt 1** (`n_Ω` is the same mode budget `∫g dω` the FTGB carrier comb realises
  ↔ M9) and **M7-2** (closure = boundary-condition eigenvalue). Use it as the explicit construction for
  M11-1's cut-off closure and as shared vocabulary for counting the FTGB comb's modes — never to *generate* a
  radius.

## M11-7 — Candidates audited, not folded: dispositions + quarantine ledger   [flag / credited / excised]

Two further EGM candidates were examined against M11-1..M11-6 and found **already covered** — folding them
would add no reusable method, only numerology to quarantine.

- **(b) A frequency-dependent `K_PV(ω)` "dispersion" relation — NOT folded; already homed.** `[credited,
  already routed]` Storti's own `K_PV = exp(2GM/rc²)` is **static and frequency-independent** (M11-1, M11-2).
  The only genuine frequency/scale dependence of a vacuum index is the **running-coupling-as-dielectric**
  duality `K_PV(q²) = α(0)/α(q²)` — exact, textbook QED — for which **M11-3 pt 2 already designates the RG
  dielectric-flow module as the home**. No distinct Storti dispersion law exists to fold; the value it would
  "predict" is `[flag]` (an RG integration constant, not forced).
- **(c) A Buckingham-Π "log identity" for non-dimensionalisation — NOT folded; subsumed by M7.** `[credited:
  Buckingham; already routed]` Taking logs of a dimensionless monomial, `ln Π = Σ_j a_j ln q_j`, is merely the
  linearisation of the null-space condition `D a = 0` already folded in **M7-1**; Storti's Π-usage
  (`St_β…St_θ`) is `[method-only]`, already routed at **M11-2** (the `St` row) and **M11-3 pt 4**. It adds no
  technique beyond M7's exact rank/null-space construction.
- **QUARANTINE LEDGER (outputs of the M11-6 closure; kept flagged, never cited as FTGB-derived).**
  - electron/proton **2:1 harmonic** `ω_Ω(e) = 2·ω_Ω(p) = ω_CP²/ω_Ce` — `[flag: numerical coincidence —
    quarantined]` (definitional/by-construction; M11-4(i)).
  - **sub-0.01% particle-radius** closures — `[flag]` full-numeric/fit, not a clean closed form (M11-4(ii),
    now with the M11-6 weak-sensitivity structural reason).
  - **H₀** from a cosmic cut-off — `[flag]` order-of-magnitude + fudge (M11-4(iv)).
  - **α** from toroidal winding via `e^(-2/3)` — `[excised]` (M11-4(v); standing excision protocol).
  The **method** (M11-6) is folded; these **values** are not — the M11-5 discipline, verbatim.

## References
Storti, R.C. (2007). *Quinta Essentia — Part 2 (US Letter)*, Delta Group Engineering / Lulu (primary, read
directly). Series: Parts 1 (layman intro), 2–4, 5.1 (solution algorithm) — ResearchGate. Puthoff, H.E.
(1999), "Polarizable-Vacuum representation of general relativity," arXiv:gr-qc/9909037. Sakharov, A.D.
(1968), Sov. Phys. Dokl. 12, 1040. Haisch, Rueda & Puthoff (1994), Phys. Rev. A 49, 678 (ZPF inertia).
Buckingham, E. (1914), Phys. Rev. 4, 345. Provenance: `results/verify/egm_sense_checks.py`,
`results/verify/egm_mode_count_closure.py` (M11-6); secondary
working notes `storti_egm_missing.md` (corrected here) and `excision-protocol-storti-factor.md` (discipline
carried). Cross-refs: M7 (Buckingham-Π), M9 (coupled-oscillator substrate), `resonator_family.html`.

*Every number here is computed in the named script; no EGM physical claim is adopted or endorsed. ASCII apart
from standard math symbols.*
