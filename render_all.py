#!/usr/bin/env python3
"""
render_all.py -- render the FTGB models into tier-captioned, shareable artifacts (PNG/GIF/MP4).

This is the PUBLICATION layer, downstream of the verified [V] core. It consumes the SAME numbers the 78 checks
validate and emits, for each scene, a poster PNG (+ looping GIF where defined) alongside a `.meta.json` sidecar
that names the scene's honesty tier and its verify script(s). The tier travels with the pixel.

IT IS NOT PART OF THE VERIFIED CORE OR CI: verify_all.py globs only results/verify/*.py + three named engine
files, so this driver and engine/viz/ never change the harness count (84/84). Rendering needs the quarantined viz deps:

    pip install -r requirements-viz.txt
    python render_all.py                 # -> outputs/renders/*.png, *.gif, *.meta.json

Run: python render_all.py [outdir]
"""
import os
import sys


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else os.path.join("outputs", "renders")
    try:
        from engine.viz import render_scenes, SCENES, _HAS_VIZ
    except Exception as e:
        print("[render_all] could not import engine.viz:", e)
        print("             install the viz layer:  pip install -r requirements-viz.txt")
        return 0
    if not _HAS_VIZ:
        from engine.viz import _IMPORT_ERROR
        print("[render_all] viz deps missing (%s)." % (_IMPORT_ERROR,))
        print("             install:  pip install -r requirements-viz.txt   (matplotlib, pillow)")
        return 0

    print("=" * 78)
    print("  FTGB render_all -- publication layer (downstream of the verified [V] core)")
    print("  outdir =", os.path.abspath(outdir))
    print("=" * 78)
    manifest = render_scenes(SCENES, outdir, do_gif=True, do_mp4=True, fps=25)
    total = 0
    for name, produced in manifest.items():
        arts = [k for k in produced if k != "meta"]
        total += len(arts)
        print("  %-28s -> %s" % (name, ", ".join(os.path.basename(produced[k]) for k in arts)))
        print("  %-28s    sidecar: %s" % ("", os.path.basename(produced["meta"])))
    print("=" * 78)
    print("  rendered %d artifacts from %d scenes; each carries a tier-captioned .meta.json." % (total, len(manifest)))
    # build the tier-annotated gallery from the sidecars (single source of truth)
    try:
        from engine.viz.gallery import build_gallery
        gpath, nr, ni = build_gallery(renders_dir=outdir, out_html="gallery.html")
        print("  gallery: %s  (%d posters + %d interactives, tiers from the sidecars)" % (gpath, nr, ni))
    except Exception as e:
        print("  (gallery build skipped: %s)" % e)
    print("  (CI untouched: verify_all.py does not import engine/viz or this driver.)")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
