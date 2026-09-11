# NOTATION — the symbol reference

Every symbol used across the FTGB jewel, with its meaning, dimension/value, and tier. Concepts are defined in
[`GLOSSARY.md`](GLOSSARY.md); numbers live in [`foundation/30_CANONICAL_NUMBERS.md`](foundation/30_CANONICAL_NUMBERS.md).
**Absolute magnitudes carry the `v_A` band; only ratios are load-bearing** ([`V_A_RESIDUAL…`](V_A_RESIDUAL_AND_ABSOLUTE_MAGNITUDES.md)).

## Field & force-free geometry
| Symbol | Meaning | Notes |
|---|---|---|
| `B`, `u` | magnetic field / velocity field | the object's field; force-free below |
| `∇×B = λB` | the **Beltrami / force-free** condition | current parallel to field, zero Lorentz force `[credited]` |
| `λ` | the force-free eigenvalue (curl eigenvalue) | `[V]`; `λ₁R = 4.4934` (first CK root) |
| `ω = ∇×u` | vorticity | `ω = λu` at Beltrami |
| `J = ∇×B` | current density | `J = λB` (force-free); the radiating current |
| `α = B♭` | the contact 1-form (metric dual of `B`) | `α∧dα = λ‖B‖²vol` ⇒ Reeb field `[credited]` |
| `L = u×ω` | the Lamb vector (rotational part of advection) | `= 0` at Beltrami ⇒ regularity (§A.3) `[V]` |
| `H = ∫A·B` | magnetic helicity | conserved (Woltjer–Taylor); `sign H = sign λ` = chirality |

## Spectrum, cascade & beat
| Symbol | Meaning | Value / tier |
|---|---|---|
| `λ_n R` | CK/Beltrami eigenvalues (roots of `tan x = x`) | `4.4934, 7.7253, 10.9041, …` `[V]` |
| ratios | carrier-comb ratios `λ_n/λ_1` | `1 : 1.719 : 2.427` `[V]` (v_A-invariant) |
| `c_CK` | Beat-Law prefactor | `c_CK(ε→0) = 1/(2 j₀,₁) = 0.20792` `[V]`; `c_CK(1/φ)=0.2234` `[V,FE]` |
| `ε` | torus aspect ratio `a/R` | `ε = 1/φ` (golden) the design point |
| `N`, `N^L` | fractal cascade base / ladder | `λ_L = λ_0 N^L`; anapole `T_L/T_{L+1}=N⁴` `[V]` (M14) |
| `f_b` | beat frequency | `f_b = (v_A/2πR)|Δλ|` `[V]`; absolute (carries band) |
| `{121, 208, 294} kHz` | the carrier comb | absolute — **carries the v_A band** |
| `ζ_B(s)`, `ζ′(−2)` | `S³` curl spectral zeta; mass-tower coeff | `ζ_B(s)=ζ(s−2)−ζ(s)`, `ζ′(−2)=−ζ(3)/4π²` `[V]` |

## Topology
| Symbol | Meaning | Value / tier |
|---|---|---|
| `Q_H` | Hopf charge (Whitehead / fibre-linking) | `Q_H = 1` `[V]` |
| `C` | wave-mode Chern number (spin-1 photon helicity) | `C = ±2 = 2s`; `|C|=2Q_H` `[V]/[credited]` |
| `Lk = Tw + Wr` | linking = twist + writhe (Călugăreanu) | integer `Lk` conserved across the cascade |
| `π₁`, `π₃` | fundamental / third homotopy (charge winding / Hopf spin) | the `g=2` lock is `π₁↔π₃` `[S]` |
| `T` | toroidal (anapole) dipole moment | ordinary dipole `~1e-16` ⇒ nonradiating `[V]` |

## Plasma / medium anchors & regularity
| Symbol | Meaning | Value / tier |
|---|---|---|
| `v_A` | Alfvén speed | `2.033×10⁴ m/s` `[residual]` — **not measured; sets the band** |
| `B` (anchor) | field magnitude | `20.6 mT` `[residual]` |
| `n_i` | ion density | `1.7×10¹⁹ m⁻³` `[credited: SSPX]` |
| `m_i` | mean air-ion mass | `29 AMU` `[credited]` |
| `R` | object radius | `0.12 m` `[credited]` |
| `d_i = λ_L` | ion skin depth = penetration depth | `0.2963 m` `[V]`; `d_i > R` ⇒ strongly Hall-mediated |
| `η`, `ν` | magnetic / kinematic diffusivity | `Pm = ν/η` (magnetic Prandtl); `η` Spitzer |
| `⟨η²⟩ < ν²λ₁` | the R2 enstrophy/BKM threshold | `[V-cond]` (bounded ⇒ no blow-up) |
| `S_di = d_i v_A/η` | Hall-smallness number (R3 (iii)) | `≈ 15–2400 ≫ 1` ⇒ (iii) violated `[V]` |

## Matter-wave / medium reading (tiered `[S]`/`[QWM]`)
| Symbol | Meaning | Notes |
|---|---|---|
| `m = ħω/c²` | whirl-mass (matter-wave rung) | `[V-dim]`; the field↔matter reading |
| `ħ_eff` | emergent action | `6.16×10⁻²³ J·s`, size-scaled `[V/residual]` (not fundamental ħ) |
| `b_eff` | medium energy per ion | `65 eV = 1.047×(B²/2μ₀n_i)` `[V/residual]`; **square-law band** |
| `K_PV` | polarizable-vacuum refractive index | `√(1+ρ_EM/ρ_vac)` `[EGM method]` |
| `θ_χ` | chirality duality angle | `H = H_max cos2θ_χ`; `45°` = self-dual Majorana `[S,computed]` |
| `α` | fine-structure constant | `1/137.036`; the winding derivation is **settled-negative** (`ι≈1`, not 137) |

## Dynamics & dimensionless
| Symbol | Meaning | Value / tier |
|---|---|---|
| `Γ_dim`, `R_dim` | universal FPUT growth / breathing radius | `0.9987`, `1.380` `[ansatz-band]` (theory dynamics, not fits) |
| `r* = √μ` | Stuart–Landau limit-cycle radius | the driven heartbeat `[V]` |
| `S(t)` | the current-leg scalar (no-go) | `S = 0` at the driven state (trilogy) `[V]` |
| `φ` | golden ratio | `φ² = φ+1`; the unique self-phase-matching cascade ratio |
| `μ₀, ε₀, c, e, ħ` | physical constants | SI; `μ₀ = 4π×10⁻⁷`, etc. |

**Tier key** (as `GLOSSARY.md`): `[V]` verified in-repo · `[credited]` established · `[S]` structural/contingent
· `[V-cond]` conditional · `[residual]`/`[flag]` disclosed calibration/coincidence · settled-negative = a kept win.
