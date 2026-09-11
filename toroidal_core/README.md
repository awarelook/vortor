# `toroidal_core/` — vendored core-derivation package (frozen)

The `MATH_TOOLKIT_BASE.md` §1/§3/§9 `[V]` claims (the symbolic `curl B = λB` field construction, the Madelung
field↔matter-wave map, the Hopf/topology quantities) were originally computed by this small package in the
external ckfreefem corpus. Vendored here (frozen) so those cited names resolve in-repo:

- `fields.py` — the CK/Beltrami field construction; symbolic `curl(B) − λB = 0` for `(l,m)=(1,0),(2,0),(2,2),(4,4)`.
- `madelung.py` — the Madelung / quantum-hydrodynamic map (the field↔matter-wave reading).
- `topology.py` — Hopf linking / Chern helpers (the load-bearing `Q_H=1`, `C=±2` are *also* reproduced in-repo by
  `results/verify/topology_invariants_check.py`).
- `quantum_hydrodynamics.py`, `quantum_ring.py` — supporting QHD / ring-resonator derivations.

**Frozen provenance, not the CI gate.** Deps vary (some need sympy/scipy). The load-bearing CK spectrum,
topology invariants, and regularity results are all reproduced independently in the `numpy`+`mpmath` CI gate.
