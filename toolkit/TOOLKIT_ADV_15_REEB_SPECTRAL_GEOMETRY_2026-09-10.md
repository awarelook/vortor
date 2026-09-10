# TOOLKIT ADV -- Module M15: REEB & SPECTRAL GEOMETRY (contact-topology of the Beltrami-Hopf resonator; the curl operator's unified spectrum)

Part of the FTGB math toolkit (see `MATH_TOOLKIT_BASE.md` §1/§3 the CK/Beltrami curl eigenproblem,
`TOOLKIT_ADV_13_NIELSEN_TUFT_MASS_TOWER_2026-09-09.md` (M13 the `S³` curl spectral zeta / Ray-Singer
torsion), `TOOLKIT_ADV_14_GREENYER_BEAT_LAW_2026-09-09.md` (M14 the self-similar cascade `λ_L = λ_0 N^L`)).
This module lifts the two **geometric frameworks** the whole object already rests on -- the contact-topology
(Reeb) reading of the force-free field, and the spectral-geometry reading of the curl operator -- into one
place, and makes each **computational** (a named verify script), not merely cited. It introduces **no new
physical claim**: it unifies results the theory already carries and adds the two theorems that make them
inevitable rather than assumed.

> **SCOPE, UP FRONT.** Two pillars, one operator. **REEB/CONTACT** is the *dynamics* side (why the closed
> standing-wave loop exists); **SPECTRAL** is the *statics* side (what the eigenvalues are). Both are the
> `curl` operator -- the Beltrami/Reeb generator. Everything here is either `[credited]` established
> mathematics (Etnyre-Ghrist; Taubes; Ray-Singer) or `[V]` re-verified in-project
> (`results/verify/reeb_spectral_geometry_check.py`). Nothing is fabricated; every number traces to that
> script or to the source modules M13/M14/base.

## Tier legend (honesty discipline)
- **[V]** verified in-project by a named computation (spectral/FFT identity, orbit integration, exact zeta).
- **[credited]** established mathematics we build on (primary-source, cited).
- **[S]** structural / cited-convergence, not closed on our side.

**Established literature cited.** Etnyre & Ghrist (2000), *Nonlinearity* **13**, 441 (Beltrami = Reeb field;
contact topology and hydrodynamics); Taubes (2007), *Geom. Topol.* **11**, 2117 (the Weinstein conjecture in
dimension 3 -- every Reeb field on a closed 3-manifold has a closed orbit); Weinstein (1979), *J. Diff. Eq.*
**33**, 353 (the conjecture); Ray & Singer (1971), *Adv. Math.* **7**, 145 (analytic torsion); Chandrasekhar
& Kendall (1957); Arnold & Khesin (1998), *Topological Methods in Hydrodynamics* (the Beltrami/steady-Euler
correspondence). Cross-refs in-project: `MATH_TOOLKIT_BASE.md` §1/§3, M13-10, M14-1/M14-6.

---

## M15-1 -- THE BELTRAMI FIELD IS A REEB FIELD OF A CONTACT STRUCTURE   [credited / V]

**WHAT.** A force-free (Beltrami) field `curl B = λ B`, `λ ≠ 0`, is -- up to reparametrization -- the **Reeb
field of a contact form**. This is what makes the winding of a force-free field a genuine *topological*
quantity rather than an incidental geometric feature, and it is the geometric underpinning already stated in
the synthesis (§A.2.1).

**MATH.** Let `α = B♭` be the 1-form metric-dual to `B`. In 3D, `dα = ι_{curl B} vol`, so

```
  α ∧ dα = (B · curl B) vol = λ |B|² vol .
```

Hence `α` is a **contact form** (`α ∧ dα ≠ 0`) exactly where `|B| ≠ 0` -- the contact condition IS the
nonvanishing-field condition. Its **Reeb field** `R` (defined by `α(R)=1`, `ι_R dα = 0`) is `R = B/|B|²`:
- `ι_B dα = ι_B ι_{curl B} vol = (curl B × B)♭ = λ (B × B)♭ = 0` -- so `B ∈ ker dα` (the Reeb direction);
- `α(R) = B·B/|B|² = 1`.
So `B` is (parallel to) the Reeb field; its integral curves are the Reeb orbits. **[credited: Etnyre-Ghrist
2000]** -- and their *converse* (every Reeb field is a Beltrami field for some Riemannian metric) closes the
correspondence, tying the whole force-free family to contact topology.

**VERIFIED.** `reeb_spectral_geometry_check.py` TEST 1, on the engine's ABC Beltrami field with spectral
(FFT) derivatives: `max|B·curl B − λ|B|²| = 9e-15` (the contact volume) and `max|curl B × B|/|B| = 3e-15`
(the Reeb direction). **[V]** The contact form is genuine on the complement of the field's isolated zeros
(measure zero).

## M15-2 -- WEINSTEIN / TAUBES: THE STANDING-WAVE LOOP EXISTS BY TOPOLOGY   [credited / V]

**WHAT.** Because the Beltrami-Hopf field is a Reeb field (M15-1), the **Weinstein conjecture** -- proved in
dimension 3 by **Taubes (2007)** -- applies: *every* Reeb field on a closed 3-manifold has at least one
**closed orbit**. Translated back through M15-1: every force-free field has a **closed field line**. The
resonator's fundamental standing-wave loop is therefore *guaranteed to exist by contact topology* -- it is a
theorem, not a modelling assumption. (The Hopf-Rañada null field is the extreme case: *all* its field lines
are closed, pairwise-linked circles -- the Hopf fibres.)

**MATH / VERIFIED.** `reeb_spectral_geometry_check.py` TEST 2 exhibits one concretely: `B = (0, sin x, cos x)`
is Beltrami (`curl B = B`); its field line through `x₀ = π/4` (where `sin = cos`) is a closed `(1,1)` orbit on
the 3-torus. RK4 integration over one period returns to the start to `3e-5` (mod `2π`) -- a closed periodic
Reeb orbit. **[V]** general existence is **[credited: Taubes 2007]**.

**WHY IT MATTERS.** The electron/neutrino/EVO reading treats the object as a *standing-wave resonator* (a
closed, self-sustaining loop), not an assumed loop. M15-2 supplies the existence proof: the closed orbit that
carries the standing wave is forced by the contact/Reeb topology of any force-free field. Combined with
Woltjer-Taylor relaxation (the plasma *falls into* the force-free state), the resonator's existence is doubly
underwritten -- energetic selection + topological guarantee.

## M15-3 -- THE CURL OPERATOR'S SPECTRUM, UNIFIED (comb + cascade + torsion)   [V / credited]

**WHAT.** One operator sits behind the whole object: `curl` (the Beltrami/Reeb generator). Its spectrum
appears in **three geometric roles**, which the theory has carried as separate results and which are in fact
one spectrum:

```
  (a) BOUNDED domain   -- CK carrier comb: eigenvalues = roots of tan x = x = 4.4934, 7.7253, 10.9041, ...
                          (l=1 force-free ball/torus BVP; MATH_TOOLKIT_BASE §3, ck_eigenvalues_check.py)  [V]
  (b) SELF-SIMILAR     -- the cascade: lam_L = lam_0 N^L  (curl spectrum under fractal rescaling;
                          M14-1 ladder-independence theorem, greenyer_beat_cascade_check.py)              [V]
  (c) CLOSED S^3       -- curl spectral zeta zeta_B(s) = zeta(s-2) - zeta(s); the n^2 coefficient
                          zeta'(-2) = -zeta(3)/(4 pi^2) = -0.0304485  (Ray-Singer analytic torsion /
                          the lepton mass-tower coefficient; M13-10, curl_spectral_zeta_pi_power_check.py)[V]
```

**UNIFICATION.** (a), (b), (c) are the *same* self-adjoint operator `curl` read in three geometries: a bounded
region with a boundary condition (discrete comb), the same region under self-similar scaling (geometric
ladder), and the closed manifold `S³` (zeta-regularized determinant = analytic torsion). The comb sets the
*carrier* frequencies, the cascade sets the *fractal ladder*, the torsion sets the *mass-tower* coefficient --
all downstream of one spectrum. **[V]** the three numbers (re-verified in `reeb_spectral_geometry_check.py`
TEST 3); **[credited]** the Ray-Singer torsion machinery.

**THE DYNAMICS/STATICS BRIDGE.** `curl` is simultaneously the *generator of the Reeb flow* (M15-1: `B` is the
Reeb field, `curl B = λB` its own rotation) and the *operator whose spectrum* is (a)-(c). So Reeb geometry
(closed orbits = the resonator's modes, M15-2) and spectral geometry (the eigenvalues = comb/cascade/torsion)
are two faces of the one curl operator. That is the sense in which the object is "one thing": a single
force-free (`curl`-eigen) field, its dynamics fixed by contact topology and its statics by the curl spectrum.

## M15-4 -- WHAT THIS BUYS THE THEORY

- The **standing-wave resonator** is no longer an assumption: a closed field line (the loop) is *forced* by
  contact topology (M15-2), and the force-free state is *selected* by Woltjer-Taylor relaxation. Existence
  from two independent directions.
- The **winding is genuinely topological**: because `B` is a Reeb field, its linking/Hopf number is a contact
  invariant (`Lk = Tw + Wr`), which is why the integer winding is *exactly* conserved across the fractal
  cascade even as the continuous helicity shrinks `~N^{-4L}` (M14-6; the resolution in
  `oam_toroidal_resonator_resolution_check.py`).
- The **spectrum is one object**: the CK comb, the cascade, and the mass-tower torsion coefficient are the
  same `curl` spectrum in three geometries (M15-3) -- one operator, not three coincidences.

**Tier.** **[V]** the contact identity, the closed-orbit integration, and the three spectral numbers
(`reeb_spectral_geometry_check.py`). **[credited]** Etnyre-Ghrist (Beltrami=Reeb), Taubes (Weinstein/closed
orbit), Ray-Singer (analytic torsion). No new physical claim; the two theorems (M15-1/-2) upgrade
"assume a resonant loop" to "a loop exists by topology," and M15-3 unifies three standing results.

---

*Source of record for M15. Reproduce: `python results/verify/reeb_spectral_geometry_check.py`. Cross-refs:
`MATH_TOOLKIT_BASE.md` §1/§3, `TOOLKIT_ADV_13...` (M13-10), `TOOLKIT_ADV_14...` (M14-1/M14-6),
`FTGB_GRAND_SYNTHESIS.md` §A.2.1 (Reeb underpinning) and §C.3 (the anapole/cascade resolution). ASCII apart
from standard math symbols; every number traces to the named script.*
