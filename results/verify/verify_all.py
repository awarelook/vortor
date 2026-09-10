#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
verify_all.py  --  reproduce the ENTIRE FTGB math model in one command.

Runs every physics/theory verification script in results/verify/ plus the
executable engine, captures each exit code, and prints a PASS/FAIL summary.
Exit status is 0 iff every check passes -- so this doubles as a CI gate.

    python results/verify/verify_all.py

Dependencies: mpmath, numpy (see requirements.txt). No network, deterministic.
Tooling scripts that are NOT theory verification (dedup_scan.py quarantine
scanner, archive_mirror.ps1 backup) are excluded by design and listed as such.
"""
import glob
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))

# scripts in results/verify/ that are infrastructure, not theory verification
NOT_THEORY = {"verify_all.py", "dedup_scan.py"}

PER_SCRIPT_TIMEOUT = 300  # seconds


def theory_scripts():
    out = []
    for p in sorted(glob.glob(os.path.join(HERE, "*.py"))):
        if os.path.basename(p) in NOT_THEORY:
            continue
        out.append(p)
    return out


def run(path):
    """Run one target; return (rc, seconds, tail_line)."""
    t0 = time.perf_counter()
    try:
        r = subprocess.run(
            [sys.executable, path],
            cwd=REPO, capture_output=True, text=True,
            timeout=PER_SCRIPT_TIMEOUT,
        )
        dt = time.perf_counter() - t0
        tail = ""
        for line in reversed((r.stdout or "").strip().splitlines()):
            if line.strip():
                tail = line.strip()[:60]
                break
        if r.returncode != 0 and not tail:
            tail = ((r.stderr or "").strip().splitlines() or [""])[-1][:60]
        return r.returncode, dt, tail
    except subprocess.TimeoutExpired:
        return 124, time.perf_counter() - t0, "TIMEOUT > %ds" % PER_SCRIPT_TIMEOUT
    except Exception as e:
        return 1, time.perf_counter() - t0, ("EXC: %s" % e)[:60]


def main():
    targets = theory_scripts()
    for extra in ("ftgb_engine.py", "ftgb_synthesis_modeler.py"):
        p = os.path.join(REPO, "engine", extra)
        if os.path.isfile(p):
            targets.append(p)

    print("=" * 78)
    print("  FTGB MATH MODEL -- full reproducible verification")
    print("  python =", sys.version.split()[0], " repo =", REPO)
    print("=" * 78)

    results = []
    for path in targets:
        name = os.path.relpath(path, REPO).replace("\\", "/")
        sys.stdout.write("  running  %-44s ... " % name)
        sys.stdout.flush()
        rc, dt, tail = run(path)
        ok = (rc == 0)
        results.append((name, ok, dt, tail))
        print("%s  (%.1fs)  %s" % ("PASS" if ok else "FAIL", dt, tail))

    npass = sum(1 for _, ok, _, _ in results if ok)
    ntot = len(results)
    print("=" * 78)
    print("  SUMMARY:  %d / %d checks PASS" % (npass, ntot))
    if npass != ntot:
        print("  FAILED:")
        for name, ok, _, tail in results:
            if not ok:
                print("    - %s   %s" % (name, tail))
    print("  (excluded as tooling, not theory: %s)" % ", ".join(sorted(NOT_THEORY - {"verify_all.py"})))
    print("=" * 78)
    return 0 if npass == ntot else 1


if __name__ == "__main__":
    raise SystemExit(main())
