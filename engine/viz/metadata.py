"""
Tier-captioned metadata sidecar for FTGB render artifacts (pure stdlib -- no viz deps).

Every rendered artifact (PNG/GIF/MP4) is emitted alongside a `<name>.meta.json` sidecar that names the
artifact's HONESTY TIER, the verify script(s) that INDEPENDENTLY validate the numbers it draws, the governing
equations, and -- crucially -- the TIME TRANSFORM (so a slowed carrier is never mistaken for real-time motion).

This is the jewel's radical-honesty discipline applied to pixels: the tier travels with the artifact. A render
is not evidence; it is a picture of numbers a passing check confirms (for [V]) or a labelled hypothesis (for [S]).

Importable without matplotlib/numpy -- it is used by the render layer but adds no verified-core dependency.
"""
import json
import os

# The repo's honesty tiers (mirror of TIER_LEDGER.md), so a caption can never invent one.
TIERS = {
    "[V]": "verified in-repo by a named check (a reader can re-run it)",
    "[credited]": "established textbook physics we build on",
    "[S]": "structural hypothesis -- falsifiable, NOT proven",
    "[viz]": "artistic / illustrative presentation only (no evidentiary weight)",
    "[settled-neg]": "a computed no-go, kept as a win",
}


def make_metadata(model, tier, verify_scripts, equations, params, time_transform,
                  outputs=None, note=""):
    """Build the tier-captioned metadata dict for one artifact/scene."""
    assert tier in TIERS, "unknown tier %r -- use one of %s" % (tier, list(TIERS))
    return {
        "model": model,
        "tier": tier,
        "tier_meaning": TIERS[tier],
        "verify_scripts": list(verify_scripts),          # the checks that validate the drawn numbers
        "equations": list(equations),
        "params": dict(params),
        "time_transform": time_transform,                # the honesty label: how physical time maps to frames
        "outputs": list(outputs or []),
        "note": note,
        "provenance": "FTGB jewel -- github.com/awarelook/vortor; numbers backed by results/verify/",
    }


def write_sidecar(meta, artifact_path):
    """Write `<artifact>.meta.json` next to the artifact and return its path."""
    side = os.path.splitext(artifact_path)[0] + ".meta.json"
    with open(side, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=True)
    return side


def caption_text(meta):
    """The one-line honesty caption baked into each figure."""
    vs = ", ".join(meta["verify_scripts"]) if meta["verify_scripts"] else "(no check)"
    return "%s  |  verify: %s  |  %s" % (meta["tier"], vs, meta["time_transform"])
