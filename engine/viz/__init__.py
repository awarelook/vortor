"""
FTGB visualization / publication layer (OPTIONAL -- deps in requirements-viz.txt, NOT in the verified core).

This package turns the jewel's already-verified models into shareable, tier-captioned artifacts. It is never
imported by verify_all.py; the 78-check core and CI stay numpy+mpmath and offline. Every artifact carries a
`.meta.json` sidecar naming its honesty tier and the verify script(s) that validate the numbers it draws.

    from engine.viz import render_scenes, SCENES
    render_scenes(SCENES, "outputs/renders")
"""
try:
    from .render import render_scene, render_scenes          # noqa: F401 (needs viz deps)
    from .scenes_m16 import SCENES as SCENES_M16             # noqa: F401
    from .scenes_core import SCENES_CORE                     # noqa: F401
    SCENES = SCENES_CORE + SCENES_M16                        # core [V] flagships first, then M16 rhythm
    _HAS_VIZ = True
except Exception as _e:                                       # pragma: no cover
    _HAS_VIZ = False
    _IMPORT_ERROR = _e
