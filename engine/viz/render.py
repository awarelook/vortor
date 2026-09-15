"""
The reusable FTGB render harness: turn a verified model's numbers into a tier-captioned PNG (+ GIF/MP4),
with the honesty caption baked into every figure. Downstream of [V] -- never inside the verified core.

A Scene is any object exposing:
    .name            -> str
    .metadata()      -> dict (from engine.viz.metadata.make_metadata)
    .figure_static() -> matplotlib.figure.Figure   (the poster frame)
    .animation(fig)  -> matplotlib.animation.FuncAnimation or None  (optional loop)

render_scene() draws the poster PNG, writes the `.meta.json` sidecar, stamps the tier caption, and (if the
scene defines one) writes a looping GIF. MP4 is attempted only if an ffmpeg writer is available.

Requires the viz deps (requirements-viz.txt); importing this module is what makes engine/viz optional.
"""
import os

import matplotlib
matplotlib.use("Agg")   # headless / deterministic-enough for publication frames
import matplotlib.pyplot as plt

from .metadata import write_sidecar, caption_text

# FTGB house style -- dark, clean, dense-but-legible (the "Mathelerium" look, backed by real numbers)
STYLE = {
    "figure.facecolor": "#0b0e14", "axes.facecolor": "#0b0e14", "savefig.facecolor": "#0b0e14",
    "text.color": "#e6e6e6", "axes.labelcolor": "#cfd8e3", "axes.edgecolor": "#33405a",
    "xtick.color": "#9aa7b8", "ytick.color": "#9aa7b8", "grid.color": "#1c2433",
    "axes.grid": True, "grid.alpha": 0.5, "font.size": 11, "axes.titlesize": 13,
    "figure.dpi": 120, "lines.linewidth": 1.8,
}
# FTGB palette
CY, MG, YE, GR = "#4dd6d6", "#e879b9", "#ffcf5a", "#7ee787"


def apply_style():
    plt.rcParams.update(STYLE)


def stamp_caption(fig, meta):
    """Bake the tier/verify/time-transform caption along the bottom of every figure (honesty travels with pixel)."""
    fig.text(0.5, 0.012, caption_text(meta), ha="center", va="bottom", fontsize=8.5,
             color="#8b98ad", family="monospace")
    fig.text(0.985, 0.975, "FTGB", ha="right", va="top", fontsize=8.5, color="#33405a", family="monospace")


def save_png(fig, path):
    fig.savefig(path, bbox_inches="tight", pad_inches=0.25)
    return path


def save_gif(anim, path, fps=25):
    from matplotlib.animation import PillowWriter
    anim.save(path, writer=PillowWriter(fps=fps))
    return path


def _try_mp4(anim, path, fps=25):
    try:
        from matplotlib.animation import FFMpegWriter
        if not FFMpegWriter.isAvailable():
            return None
        anim.save(path, writer=FFMpegWriter(fps=fps, bitrate=3000))
        return path
    except Exception:
        return None


def render_scene(scene, outdir, do_gif=True, do_mp4=False, fps=25):
    """Render one scene -> {png, meta, gif?, mp4?}. Returns the manifest dict of produced paths."""
    apply_style()
    os.makedirs(outdir, exist_ok=True)
    meta = scene.metadata()
    produced = {}

    # poster PNG + sidecar
    fig = scene.figure_static()
    stamp_caption(fig, meta)
    png = os.path.join(outdir, scene.name + ".png")
    save_png(fig, png); produced["png"] = png
    meta.setdefault("outputs", []).append(os.path.basename(png))

    # optional looping animation
    if do_gif and hasattr(scene, "animation"):
        figa = scene.figure_static() if not hasattr(scene, "figure_anim") else scene.figure_anim()
        anim = scene.animation(figa)
        if anim is not None:
            stamp_caption(figa, meta)
            gif = os.path.join(outdir, scene.name + ".gif")
            try:
                save_gif(anim, gif, fps=fps); produced["gif"] = gif
                meta["outputs"].append(os.path.basename(gif))
                if do_mp4:
                    mp4 = _try_mp4(anim, os.path.join(outdir, scene.name + ".mp4"), fps=fps)
                    if mp4:
                        produced["mp4"] = mp4; meta["outputs"].append(os.path.basename(mp4))
            finally:
                plt.close(figa)

    produced["meta"] = write_sidecar(meta, png)
    plt.close(fig)
    return produced


def render_scenes(scenes, outdir, **kw):
    """Render a list of scenes; return {scene_name: manifest}."""
    out = {}
    for sc in scenes:
        out[sc.name] = render_scene(sc, outdir, **kw)
    return out
