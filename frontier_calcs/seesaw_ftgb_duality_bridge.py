#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SEESAW_FTGB_DUALITY_BRIDGE mapping-1 check: ASCII only; run with PYTHONIOENCODING=utf-8
# (a) m = hbar*omega/c^2 for the whirl ladder; confirm nu rung ~ 0.05 eV.
# (b) frequency-seesaw ladder scan omega_D^2/omega_R vs the nu rung.
import math

hbar = 1.054571817e-34   # J s (CODATA)
c    = 2.99792458e8      # m/s
c2   = c * c
eV   = 1.602176634e-19   # J per eV

def m_kg(omega): return hbar * omega / c2
def m_eV(omega): return hbar * omega / eV    # = m_kg*c^2/eV

# whirl ladder (rad/s)
ladder = {'EVO': 7.6e5, 'nu': 7.6e13, 'e': 7.76e20, 'p': 1.43e24, 'd': 2.85e24}
known_MeV = {'e': 0.51099895, 'p': 938.272, 'd': 1875.6129}   # PDG/CODATA cross-checks

print("=== (a) m = hbar*omega/c^2 per rung ===")
for k, w in ladder.items():
    line = f"{k:4s} omega={w:.3e} rad/s -> {m_eV(w):.6e} eV = {m_eV(w)/1e6:.5f} MeV"
    if k in known_MeV:
        dev = 100*abs(m_eV(w)/1e6 - known_MeV[k])/known_MeV[k]
        line += f"  (known {known_MeV[k]} MeV, {dev:.2f}%)"
    print(line)

w_nu = ladder['nu']
print(f"\nnu confirm: m_nu = {m_eV(w_nu):.5f} eV (target ~0.05 eV, "
      f"{100*abs(m_eV(w_nu)-0.05)/0.05:.2f}%)")
print(f"omega for exactly 0.05 eV = {0.05*eV/hbar:.4e} rad/s (ladder nu = {w_nu:.2e})")

print("\n=== (b) frequency-seesaw ladder scan: omega_D^2/omega_R vs nu rung ===")
tgt = w_nu
rows = []
for nd, wd in ladder.items():
    for nr, wr in ladder.items():
        val = wd*wd/wr
        rows.append((abs(math.log10(val/tgt)), nd, nr, val, val/tgt))
rows.sort()
for lg, nd, nr, val, ratio in rows:
    flag = "  <-- on-ladder hit" if abs(lg) < 0.01 else ("  (within 4 orders)" if abs(lg) < 4 else "")
    print(f"  omega_D={nd:3s} omega_R={nr:3s}: {val:.3e}  ratio={ratio:.3e}{flag}")

print("\n=== required (off-ladder) omega_R for each natural omega_D to hit nu rung ===")
for nd, wd in ladder.items():
    print(f"  omega_D={nd:3s}: omega_R needed = {wd*wd/tgt:.3e} rad/s")
