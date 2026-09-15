# `engine/viz/` — the FTGB publication layer

Turn the jewel's **already-verified** models into shareable, tier-captioned artifacts (PNG / GIF / MP4).
This layer is **downstream of the verified `[V]` core** — it renders numbers a passing check confirms; it is
never itself evidence.

## The discipline (why this is not just an animation folder)

- **Deps are quarantined.** The verified core is `numpy + mpmath` (`requirements.txt`), no-network,
  deterministic. The render deps (`matplotlib`, `pillow`, …) live in **`requirements-viz.txt`** only.
  `verify_all.py` globs `results/verify/*.py` + three named engine files, so it **never imports `engine/viz/`
  or `render_all.py`** — the 78-check count and CI stay green and offline.
- **The tier travels with the pixel.** Every artifact gets a `<name>.meta.json` sidecar (`metadata.py`) naming
  its honesty **tier** (`[V]`/`[credited]`/`[S]`/`[viz]`), the **verify script(s)** that validate the drawn
  numbers, the governing **equations**, and the **time transform** — so a slowed carrier is never mistaken for
  real-time motion. The same caption is baked into the figure.
- **`[V]` visuals vs `[S]` visuals.** A computed eigenfunction / verified comb is `[V]`; an illustrative
  scalar field or a hypothesised LENR "active site" is `[S]`/`[viz]` — and the caption says which. The visual
  layer must not quietly promote a hypothesis the text keeps honest.

## Run

```bash
pip install -r requirements-viz.txt      # heavy; NOT part of CI
python render_all.py                      # -> outputs/renders/*.png, *.gif, *.mp4, *.meta.json
```

## Layout

- `metadata.py` — the tier-captioned sidecar (pure stdlib; no viz deps).
- `render.py` — the reusable harness: house style, `stamp_caption`, `render_scene`/`render_scenes`
  (PNG + optional GIF via PillowWriter + optional MP4 via ffmpeg).
- `scenes_m16.py` — the first scenes, off the verified M16 rhythm content:
  - `m16_ck_comb_fingerprint` `[V]` — the CK inharmonic comb `1:1.719:2.427` (the fingerprint).
  - `m16_beat_torque` `[V]` — two-mode beat → torque spectrum at `f_b` and `f_Σ` (animated).
  - `m16_duffing_backbone` `[V]` — the anharmonic backbone bend the Stuart-Landau heartbeat omits.

## Add a scene

Implement an object with `.name`, `.metadata()` (via `make_metadata`), `.figure_static() -> Figure`, and an
optional `.animation(fig) -> FuncAnimation`. Consume the **same closed forms** a `results/verify/` check
asserts, and name that check in `verify_scripts`. Append it to `SCENES`.

*Rendered binaries (`*.gif`, `*.mp4`) are git-ignored (regenerable via `render_all.py`); the small PNG posters
and the `.meta.json` sidecars are committed as the provenance record.*
