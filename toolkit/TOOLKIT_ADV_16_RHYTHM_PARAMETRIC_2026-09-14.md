# TOOLKIT ADV -- Module M16: RHYTHM DYNAMICS, ANHARMONIC (DUFFING) RESONANCE & THE SUM-vs-DIFFERENCE FREQUENCY FENCE

Part of the FTGB math toolkit (see `MATH_TOOLKIT_BASE.md`; `TOOLKIT_ADV_09_COUPLED_OSCILLATOR_SUBSTRATE_2026-09-08.md`
(M9 Stuart-Landau / Kuramoto / Adler beat law); `TOOLKIT_ADV_14_GREENYER_BEAT_LAW_2026-09-09.md`
(M14 beat ladder, triad dichotomy, Manley-Rowe, Floquet-Mathieu threshold)). This module is the
**RHYTHM-DYNAMICS completion pass**: it takes the standard theory of how repeated motion organizes in time
-- Fourier lines, beats, resonance, entrainment, parametric (Mathieu) subharmonics, and **anharmonic
(Duffing) resonance** -- and pins down (a) which of those relations are load-bearing for the FTGB coherent
object, (b) the **one standard concept the model currently switches OFF** (amplitude-dependent frequency),
and (c) the **frequency-matching fence** that disciplines the project's cross-scale (kHz -> MeV) claim. Every
relation here is either credited textbook physics reproduced in-repo or an honest settled-negative; nothing
is fabricated.

> **THE TWO THINGS THIS MODULE ADDS, STATED UP FRONT.**
> **(1) The new-physics leg -- Duffing / anharmonic resonance.** The FTGB engine's limit-cycle heartbeat is
> Stuart-Landau with the frequency term *constant*: `dz/dt = (mu + i om - |z|^2) z` (shear coefficient
> `c = 0`). That gives amplitude *saturation* but **zero amplitude -> frequency coupling** -- the defining
> Duffing effect is off by construction. A finite-amplitude force-free (Beltrami) equilibrium is generically
> anharmonic, so that term is *expected* nonzero. Restoring it makes the resonance frequency bend with drive
> (backbone), fold into a bistable jump, and shed odd (3f, 5f) harmonics -- and, crucially, makes the CK
> comb ratios `1.719 / 2.427` **drive-amplitude-dependent**. So the project's sharpest resonance-sector
> kill-switch (the inharmonic comb) must be quoted **at the linear/low-amplitude limit**, and a measured
> drift-with-amplitude is a **prediction, not a refutation**. Reproduced in
> `results/verify/duffing_backbone_check.py` `[V]`.
> **(2) The load-bearing settled-negative -- the sum-vs-difference fence.** A slow **difference** (beat)
> frequency cannot parametrically pump or directly drive a fast mode: parametric onset needs a **sum** /
> twice-frequency match `Omega ~ omega_j + omega_k`. The FTGB kHz carrier beat is ~16 orders too slow to
> pump a MeV nuclear mode. This retires the "beat dynamically pumps the nucleus" reading **only** -- it does
> **not** touch the `[V]`/conserved `d+d->4He = 23.847 MeV` energy ledger, the cold Landau-Zener B=4
> resolution, or a genuinely-slow (`omega_b ~ omega_slow`) nuclear-adjacent route. Reproduced in
> `results/verify/rhythm_parametric_resonance_check.py` TEST 4 `[settled-negative]`.

## Tier legend (honesty discipline)
- **[V]** verified in-project by a named computation (a reproduced textbook identity, an integration, a
  symbolic check). Trustworthy at the stated precision.
- **[credited]** established physics/mathematics we build on (textbook or primary-source, cited).
- **[V-us]** internal-consistency computation of the theory's *own* dictionary (structurally correct; not an
  independent physical measurement).
- **[S]** structural / hypothesis-level, not closed on our side.
- **[settled-negative]** a computed no-go, kept as a WIN (a disciplined clue, never a dead end).

**In-repo verify.** `results/verify/rhythm_parametric_resonance_check.py` (M16-1..M16-4, M16-6) and
`results/verify/duffing_backbone_check.py` (M16-5). Both numpy-only, deterministic, in `verify_all.py`.

**Established literature cited (per method below):** Feynman *Lectures* I-48 (beats); Mathieu (1868) /
Nayfeh-Mook *Nonlinear Oscillations* (1979) ch.3-5; Adler (1946); Pikovsky-Rosenblum-Kurths *Synchronization*
(2001); Landau-Lifshitz *Mechanics* secs.27-29 (parametric resonance, anharmonic oscillator); Kruer *Physics
of Laser Plasma Interactions* ch.7 (parametric instabilities, sum-rule); Chandrasekhar-Kendall (1957).

---

## M16-1 -- THE BEAT IS A NONLINEAR (ENERGY) OBSERVABLE, NOT A LINEAR FOURIER LINE   [V / credited]

**WHAT.** Two close tones `A cos(w1 t) + A cos(w2 t) = 2A cos((w_b/2) t) cos(w_c t)` with `w_b = |w2 - w1|`.
The slow factor is an *envelope*, not a spectral line: a **linear** field has NO Fourier component at `w_b`.
A **quadratic** observable (energy / intensity / stress / torque, `I ~ x^2`) DOES carry a real line at `w_b`.
So the FTGB kHz beat lives in a quadratic/energy observable -- exactly how the resonator sim extracts it
(FFT-Hilbert envelope) and how a physical detector (a square-law power/stress sensor) sees it. This is the
precise reason the "beat" is physical without being a linear mode.

**MATH.** (reproduced in `rhythm_parametric_resonance_check.py` TEST 1.)
```
linear    x(t) = cos(w1 t) + cos(w2 t)     ->  amp @ w_b  =  0        (no line; only w1, w2)
quadratic x(t)^2                            ->  amp @ w_b  =  real     (a genuine difference line)
computed (f1,f2 = 120,124 Hz):  amp@f_b in x  ~ 8e-10 (numerically zero);  amp@f_b in x^2 ~ 0.49
```

**Tier.** **[credited]** -- elementary Fourier identity (Feynman I-48); the in-repo computation is the
`[V]` confirmation that the difference line is absent in the field and present in the energy observable.

**FTGB home.** The carrier comb `{121, 208, 294} kHz` and its `87 kHz` beat (M14-1); the resonator sim's
envelope extraction (`engine/ftgb_resonator_sim.py`).

---

## M16-2 -- PARAMETRIC (MATHIEU) SUBHARMONIC: TONGUE AT Omega ~ 2 w0, THRESHOLD ~ 2/Q   [V / credited]

**WHAT.** A parametrically-driven oscillator `x'' + 2 gamma x' + w0^2 [1 + h cos(Omega t)] x = 0` (the drive
modulates a *parameter*, not an additive force) has its **principal instability tongue at `Omega ~ 2 w0`**
-- the response is at *half* the drive frequency -- with onset threshold `h_th ~ 2/Q`, `Q = w0/2gamma`. This
grounds the FTGB "driven heartbeat" as a parametric drive and reproduces the M14-10 Floquet-Mathieu threshold
`eta_c = 2/Q`.

**MATH.** (reproduced in `rhythm_parametric_resonance_check.py` TEST 2.)
```
tongue:     integrate at Omega = 2 w0 vs Omega = w0, h = 0.15, Q = 25
            -> Omega = 2 w0 GROWS (subharmonic), Omega = w0 decays  (half-frequency response = the hallmark)
threshold:  at Omega = 2 w0, h = 0.05 (< 2/Q = 0.08) decays ; h = 0.12 (> 2/Q) grows   =>  h_th ~ 2/Q
```

**Tier.** **[credited]** for the Mathieu/Hill principal-tongue result (Mathieu 1868; Landau-Lifshitz sec.27;
Nayfeh-Mook ch.5); the integration is the `[V]` in-repo confirmation.

**FTGB home.** The driven-heartbeat reading (M14-2 "every persistent beat is driven"); the M14-10 EVO
Floquet-Mathieu `eta_c = 2/Q_5 = 0.1399`.

---

## M16-3 -- ADLER ENTRAINMENT: LOCK IFF |Delta_w| <= K (THE ARNOLD TONGUE)   [V / credited]

**WHAT.** The phase difference between a driven mode and its reference obeys `dpsi/dt = Delta_w - K sin psi`.
It **locks** (`psi -> const`, zero mean drift) iff `|Delta_w| <= K` -- the Arnold-tongue half-width is the
coupling `K` -- and phase-slips (nonzero mean drift) outside. This is the exact mechanism of the FTGB carrier
comb-lock (Kuramoto/Adler, M9/M14).

**MATH.** (reproduced in `rhythm_parametric_resonance_check.py` TEST 3.)
```
K = 1:  Delta_w = 0.5 -> drift 0 (locked) ;  0.9 -> drift 0 (locked) ;  1.3 -> drift != 0 (slipping)
```

**Tier.** **[credited]** (Adler 1946; Pikovsky-Rosenblum-Kurths 2001); the integration is the `[V]`
confirmation. **Cross-link:** the Arnold-tongue comb-lock is one of the two mechanisms that pull the CK comb
ratios off geometry (`1.719 -> 7/4`, `2.427 -> 5/2`); the *other* is the Duffing-pull of M16-5 -- they are
physically distinct and experimentally separable (see M16-5).

---

## M16-4 -- THE SUM-vs-DIFFERENCE FENCE: a slow BEAT cannot pump a fast MODE   [settled-negative / V-arithmetic / credited]

**WHAT.** The load-bearing settled-negative. Parametric excitation of a mode `w0` requires a pump on a
Mathieu/Hill tongue `Omega ~ 2 w0 / n` (principal `n = 1`); multimode / three-wave transfer obeys the **sum**
rule `Omega = w_j + w_k`. A slow **difference** (beat) frequency is **not** a valid pump for a fast mode. The
FTGB kHz carrier beat is therefore ~16 orders too slow to parametrically pump -- or directly drive -- a MeV
nuclear mode.

**MATH.** (reproduced in `rhythm_parametric_resonance_check.py` TEST 4; arithmetic reproduced independently.)
```
FTGB carrier beat:   w_b = 2 pi * 87.14 kHz = 5.47e5 rad/s        (a DIFFERENCE frequency)
MeV nuclear mode:    w_nuc(1 MeV) = E/hbar = 1.52e21 rad/s
pump target:         2 w_nuc = 3.04e21 rad/s
ratio:               w_b / (2 w_nuc) = 1.80e-16      (log10 = -15.7  ->  15.7 orders of magnitude short)
intermediate steps:  293 eV -> 12.2 OOM ,  1 keV -> 12.7 OOM        (every channel 12-16 OOM short)
only tongue it hits:  n ~ 5.6e15  ->  width ~ h^n = numerically zero  (adiabatic, not resonant)
```

**Tier.** **[V]** arithmetic (numpy), **[credited]** physics (Landau-Lifshitz sec.27 / Kruer ch.7),
**[settled-negative]** scoping.

**Precise wording (this is the canonical form; it also sharpens `TIER_LEDGER` line "Cross-scale Delta
identity").**
> The carrier-comb beat `w_b = 2 pi * 87 kHz ~ 5.47e5 rad/s` is a **difference** frequency and cannot
> parametrically pump or directly drive a MeV nuclear mode (`w_nuc ~ 1.52e21 rad/s`): parametric onset needs
> a **sum** / twice-frequency match `Omega ~ 2 w_nuc ~ 3.04e21 rad/s` -- short by `1.8e-16` (15.7 OOM); the
> only tongue it hits, `n ~ 5.6e15`, has exponentially vanishing width (adiabatic, not resonant). This
> retires the "beat dynamically pumps the nucleus" reading **only**.

**The three carve-outs (carried verbatim so the no-go is never misread as killing the LENR resolution).**
It does **not** touch: (i) the mechanism-independent `[V]`/conserved `d+d->4He = 23.847 MeV` energy ledger
(energy conservation is not a frequency claim); (ii) the cold/structural **Landau-Zener B=4** resolution
(decoupled from the frequency desert by construction); (iii) a genuinely-slow (`w_b ~ w_slow`)
nuclear-*adjacent* collective / small-level-splitting route. The sole survivable cross-scale form is a
**structural detuning-gap (Landau-Zener) analogy, never a dynamical pump.**

**FTGB home.** Disciplines the "cross-scale Delta identity (kHz detuning <-> MeV gap)" -- keeps it `[S]`, and
names *which* reading is dead (the pump) vs which survives (the structural gap). Consistent with the already
`[V]`/NEGATIVE route-4 seesaw (`eta^N = R^-2`, NEET `P < 4.1e-10`) in `FTGB_GRAND_SYNTHESIS.md` E.2.3.

**AUDIT EXTENSION (2026-09-14, `cross_scale_slow_scale_audit_check.py`) -- the third carve-out RESOLVED.**
The fence left "a genuinely-slow (`w_b ~ w_slow`) nuclear-adjacent route" as an open carve-out. An 8-scale
audit (compute-and-log every candidate slow scale vs the 87.14 kHz beat) resolves it:
- The **LITERAL "kHz = MeV gap" identity is DEAD** -- a settled-negative by **~16.8 OOM** (`E_beat = h f_beat
  = 0.360 neV` vs `Q = 23.847 MeV`). Every nuclear-internal / lattice / plasma / LZ-sweep scale sits **+7.5 to
  +17.6 OOM ABOVE** the beat; the only kHz hits are the object-Alfven beat itself (0 OOM **by construction** --
  tautological) or **field-tunable** atomic/molecular splittings a control target also hits (`4He` has `I=0` ->
  no nuclear Zeeman -> the reactant-only bridge is empty). So **87 kHz is a MACROSCOPIC-COLLECTIVE
  (object-Alfven/MHD) scale, not nuclear-internal** -- kHz order is generic to any lab-scale collective object.
- The **PUMP reading is DOUBLY-closed**: parametric short by 15.7 OOM (this M16-4) **AND** slow-adiabatic
  killed by `tau_cross/T_kHz ~ 1e-18` (the nuclear crossing is frozen/DC across a kHz cycle -- the quantitative
  form of the already-rejected "slow lattice sets the sweep" lesson: the sweep is set by nuclear velocity).
- **Two ideas that wore the one phrase "detuning-gap" are separated:** **(A)** the structural nuclear LZ gap
  `Delta_nuc` -- **kHz-FREE**, the legitimate B=4 theory (LZ formula `[credited]` math / d+d identification
  `[S]` / rate open); "detuning-gap" is a **shared-schema analogy** (von Neumann-Wigner codim-1, disjoint
  Pi-groups, **zero transferred number**, NOT a forced law, NOT a pump). **(B)** the macroscopic beat as a slow
  **yield-GATE / duty-cycle** -- **`[S]`, FALSIFIABLE** by a beat-locked yield step surviving an `H2`
  (non-fusable) control; does not touch the conserved 23.847 MeV `[V]` ledger. The half-beat 43.57 kHz (Klimov
  43-46 kHz window) is tiered identically to the object-beat: macroscopic/environmental, not nuclear-internal.

---

## M16-5 -- ANHARMONIC (DUFFING) RESONANCE: the amplitude-dependent frequency the heartbeat omits   [V / credited], and its consequence for the comb falsifier   [V-us -> S]

**WHAT.** The one standard rhythm-dynamics concept absent from the model. The Duffing oscillator
`x'' + 2 gamma x' + w0^2 x + beta x^3 = F cos(Omega t)` has a **restoring force that stiffens with
amplitude**, so its resonance *frequency* moves with drive. Three reproduced consequences, then the
load-bearing one for the theory:

**MATH.** (reproduced in `duffing_backbone_check.py`.)
```
(a) BACKBONE bending:     Omega_peak(A) ~ w0 (1 + 3 beta A^2 / 8 w0^2)   (hardening for beta > 0)
      computed (beta=0.4): F=0.05 -> Omega_peak=1.025 (textbook 1.035) ; F=0.30 -> Omega_peak=1.250
      -> the peak frequency climbs with drive amplitude (small-amplitude limit matches the textbook backbone)
(b) BISTABILITY / JUMP:   in the folded region two stable steady states coexist at one Omega
      computed (F=0.6): Omega=1.55 -> A=0.45 (from small IC) vs A=2.38 (from large IC)  = two states
      -> the mechanism behind the swept-drive amplitude discontinuity (up-sweep != down-sweep hysteresis)
(c) ODD HARMONICS:        the cubic (odd) force feeds Omega into 3 Omega, 5 Omega ... ; evens suppressed by x->-x
      computed: amp@3f >> amp@2f (3f/2f ~ 700)  -> an odd-harmonic tell, distinct from a quadratic nonlinearity
(d) THE COMB-PULL IS AMPLITUDE-DEPENDENT (the load-bearing consequence):
      amplitude-equation form of Duffing = Stuart-Landau WITH SHEAR:  dz/dt = (mu + i om - (1 + i c)|z|^2) z
      limit cycle: |z|^2 = mu,  w_eff = om - c mu   (numerically confirmed: om=1,c=0.5,mu=0.4 -> w=0.80)
      => CK comb ratios drift with drive: c=0.10, mu(drive^2) 0->1 pulls 1.719 -> 1.736, 2.427 -> 2.459
      => c = 0 (the CURRENT engine) gives the FIXED comb; c != 0 (a generic finite-amplitude equilibrium) drifts
```

**Tier.** **[V]** for the reproduced textbook Duffing identities (backbone, bistability, odd harmonics) and
the Stuart-Landau shear-law `w_eff = om - c|z|^2` (numerically confirmed). **[credited]** Landau-Lifshitz
*Mechanics* sec.29; Nayfeh-Mook *Nonlinear Oscillations* ch.4. **[V-us -> S]** for the consequence: the comb
ratios' drift is an internal computation on the theory's own dictionary; that a *physical* finite-amplitude
Beltrami equilibrium carries a nonzero shear is the `[S]` expectation.

**Consequence for the falsifier (the honest sharpening).** The inharmonic comb `1 : 1.719 : 2.427` is
FTGB's sharpest resonance-sector kill-switch (`FTGB_MINIMUM_VIABLE_PAPER.md` sec.5). Duffing makes those
ratios **drive-amplitude-dependent**, so:
- the honest falsifier is "the comb ratios **at the linear (low-amplitude) limit**";
- a measured **drift-with-amplitude is a PREDICTION**, not a refutation;
- **two distinct comb-pull mechanisms** are now on the table and are **experimentally separable**:
  **Duffing-pull** = a CONTINUOUS single-oscillator drift of a ratio with drive amplitude; the
  **Arnold-tongue comb-lock** (M16-3) = a DISCONTINUOUS *plateau* that snaps a ratio onto a rational
  (`7/4`, `5/2`) and holds it across a finite detuning band (a devil's-staircase plateau), and needs a
  second mode to lock to. Smooth amplitude-drift vs a locked staircase plateau -- a measurement can tell
  them apart.

**FTGB home.** Closes the gap flagged by the M16 completeness pass: the engine's Stuart-Landau heartbeat has
`c = 0`, so it models amplitude saturation but not the amplitude->frequency coupling that a real anharmonic
resonator has. This module makes the comb-pull falsifier amplitude-explicit and supplies the odd overtones
(3f, 5f) that feed the M14-3/M14-4 three-wave triads.

---

## M16-6 -- THE CK COMB IS INHARMONIC (THE FINGERPRINT, RESTATED AT THE LINEAR LIMIT)   [V / credited]

**WHAT.** Real force-free resonators have `w_n != n w_1`. The CK comb (roots of `tan x = x`) gives ratios
`1 : 1.719 : 2.427`, NOT the harmonic `1 : 2 : 3` of a string. A harmonic `1:2:3` lock would falsify the
Beltrami-carrier reading -- the sharpest FTGB spectral fingerprint. **Read together with M16-5:** these
ratios are the **linear-amplitude-limit** fingerprint; the drive-dependent drift is the M16-5 prediction.

**MATH.** (reproduced in `rhythm_parametric_resonance_check.py` TEST 5.)
```
roots of tan x = x:   4.4934, 7.7253, 10.9041   ->  ratios  1 : 1.7193 : 2.4267   (bisection)
harmonic series:      1 : 2 : 3   (a string)     ->  clearly distinct (|1.719 - 2| = 0.28)
```

**Tier.** **[V]** (the roots and ratios are reproduced two ways in `ck_eigenvalues_check.py` as well);
**[credited]** Chandrasekhar-Kendall 1957.

---

## Reading (what M16 does for the jewel)

Rhythm dynamics **grounds** the FTGB core -- the beat is a nonlinear/energy observable (M16-1), the driven
heartbeat is a parametric (Mathieu) drive with its tongue at `2 w0` and threshold `2/Q` (M16-2), the carrier
comb-lock is Adler/Arnold entrainment (M16-3), the comb is inharmonic (M16-6, the fingerprint). It **adds one
new-physics leg** -- the anharmonic (Duffing) amplitude-dependent frequency the model currently omits (M16-5),
which turns the comb falsifier into a linear-limit statement plus a drift prediction and distinguishes
Duffing-pull from Arnold-pull. And it **adds one load-bearing settled-negative** -- the sum-vs-difference
fence (M16-4): a slow kHz beat cannot parametrically pump a MeV mode, retiring the pump reading of the
cross-scale claim while leaving the conserved energy ledger, the Landau-Zener B=4 resolution, and a
genuinely-slow route untouched. Every relation is credited or computed; the one speculative bridge is fenced,
not fabricated.

**Source scripts.** `results/verify/rhythm_parametric_resonance_check.py`,
`results/verify/duffing_backbone_check.py`. **Cite:** Feynman I-48; Mathieu 1868 / Nayfeh-Mook 1979;
Adler 1946 / Pikovsky-Rosenblum-Kurths 2001; Landau-Lifshitz *Mechanics* secs.27-29; Kruer ch.7;
Chandrasekhar-Kendall ApJ 126, 457 (1957).
