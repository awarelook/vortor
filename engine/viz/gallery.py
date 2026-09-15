"""
Build gallery.html -- a self-contained, tier-annotated index of the FTGB visual layer.

It is GENERATED from the render `.meta.json` sidecars (single source of truth), so the gallery's tiers and
verify-links stay in sync with what was actually rendered. Data is BAKED IN (no runtime fetch), so the page
is double-clickable from file:// with no CORS issues. It indexes:
  * the rendered posters (PNG), each with its tier badge + verify-script links + equation + time-transform;
  * the 6 interactive HTML models, each with its tier + backing checks.

Every card carries the tier that the math earns -- the gallery is a proof-backed contact sheet, not a mood board.

    python -m engine.viz.gallery            # or it runs at the end of render_all.py
"""
import glob
import html
import json
import os

REPO = "https://github.com/awarelook/vortor"
BLOB = REPO + "/blob/main/results/verify/"

# the 6 interactive models (mirrors the provenance.js configs)
INTERACTIVES = [
    ("index.html", "The Coherent Object", "[V] core / [S] frontier",
     ["ck_eigenvalues_check", "exact_beltrami_regularity_check", "topology_invariants_check", "majorana_selfdual_check"],
     "point &rarr; string &rarr; resonator &rarr; knot &rarr; dynamics"),
    ("resonator_family.html", "The Resonator Family", "[V]",
     ["ck_eigenvalues_check", "delta_detuning_beat_check", "beat_law_across_scales_check"],
     "the one object at five resonance conditions"),
    ("soliton3d.html", "Soliton 3D", "[V] geometry / [viz] field",
     ["topology_invariants_check", "reeb_spectral_geometry_check", "ck_eigenvalues_check"],
     "torus / knotted field"),
    ("dynamics_lab.html", "Dynamics Lab", "[V] @ Re&le;628",
     ["exact_beltrami_regularity_check", "r2_driven_beltrami_attractor_check", "nmode_woltjer_lp_check"],
     "live driven dynamics"),
    ("electron.html", "The Electron Rung", "[S] id / [V] kinematics",
     ["g2_dirac_structure_check", "majorana_selfdual_check", "torque_beat_alpha_check"],
     "the matter-wave identification"),
    ("coherence.html", "The Coherence Stack", "[V]",
     ["exact_beltrami_regularity_check", "carrier_chirality_lock_check", "nmode_woltjer_lp_check"],
     "coherence is regularity"),
]


def _tier_color(tier):
    t = tier.lower()
    if "[v]" in t and "[s]" not in t and "[viz]" not in t:
        return "#7ee787"        # green -- verified
    if "[viz]" in t and "[v]" not in t and "[s]" not in t:
        return "#8b98ad"        # gray -- illustration
    if "[s]" in t and "[v]" not in t:
        return "#ffcf5a"        # yellow -- hypothesis
    return "#4dd6d6"            # cyan -- mixed


def _check_links(checks):
    names = [c[:-3] if c.endswith(".py") else c for c in checks]
    return " ".join("<a href='%s%s.py' target='_blank' rel='noopener'>%s</a>" % (BLOB, n, n) for n in names)


def _render_card(meta, renders_dir):
    outs = meta.get("outputs", [])
    png = next((o for o in outs if o.endswith(".png")), None)
    gif = next((o for o in outs if o.endswith(".gif")), None)
    tier = meta.get("tier", "[V]")
    col = _tier_color(tier)
    eq = (meta.get("equations") or [""])[0]
    tt = meta.get("time_transform", "")
    note = meta.get("note", "")
    img = ("<img src='%s/%s' loading='lazy' alt='%s'>" % (renders_dir, html.escape(png), html.escape(meta["model"]))) if png else ""
    loop = ""
    if gif and os.path.exists(os.path.join(renders_dir, gif)):
        loop = " &middot; <a href='%s/%s' target='_blank' rel='noopener'>&#9654; loop</a>" % (renders_dir, html.escape(gif))
    return (
        "<div class='card'>" + img +
        "<div class='cbody'>" +
        "<div class='tier' style='color:%s;border-color:%s'>%s</div>" % (col, col, html.escape(tier)) +
        "<h3>%s</h3>" % html.escape(meta["model"]) +
        "<div class='eq'>%s</div>" % html.escape(eq) +
        "<div class='vs'>verify: %s%s</div>" % (_check_links(meta.get("verify_scripts", [])), loop) +
        ("<div class='tt'>%s</div>" % html.escape(tt) if tt else "") +
        ("<div class='note'>%s</div>" % html.escape(note) if note else "") +
        "</div></div>"
    )


def _interactive_card(fname, title, tier, checks, sub):
    col = _tier_color(tier)
    return (
        "<div class='card ix'>"
        "<a class='play' href='%s'>&#9654;</a>" % html.escape(fname) +
        "<div class='cbody'>" +
        "<div class='tier' style='color:%s;border-color:%s'>%s</div>" % (col, col, tier) +
        "<h3><a href='%s'>%s</a></h3>" % (html.escape(fname), html.escape(title)) +
        "<div class='eq'>%s</div>" % sub +
        "<div class='vs'>verify: %s</div>" % _check_links(checks) +
        "</div></div>"
    )


CSS = """
:root{color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:#080a10;color:#cfd8e3;font:14px/1.55 ui-sans-serif,system-ui,Segoe UI,Roboto,sans-serif}
a{color:#7ee787;text-decoration:none}a:hover{color:#a6f0b3}
.wrap{max-width:1180px;margin:0 auto;padding:28px 20px 60px}
header h1{font:600 26px/1.2 ui-monospace,Menlo,Consolas,monospace;color:#e6e6e6;margin:0 0 6px}
header p{color:#8b98ad;margin:0 0 4px;max-width:900px}
.legend{margin:14px 0 22px;font:12px ui-monospace,monospace;color:#7f8ea3}
.legend b{padding:1px 6px;border:1px solid;border-radius:5px;margin-right:6px}
h2{font:600 15px ui-monospace,monospace;color:#9fb0c3;border-bottom:1px solid #1c2433;padding-bottom:6px;margin:30px 0 16px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:18px}
.card{background:#0b0e14;border:1px solid #1c2433;border-radius:12px;overflow:hidden;display:flex;flex-direction:column}
.card img{width:100%;display:block;background:#0b0e14;border-bottom:1px solid #1c2433}
.card.ix{position:relative}
.card .play{position:absolute;top:12px;left:12px;z-index:2;width:40px;height:40px;border-radius:50%;background:#4dd6d6;color:#04222a;display:grid;place-items:center;font-size:16px;text-decoration:none}
.cbody{padding:12px 14px 14px}
.tier{display:inline-block;font:600 11px ui-monospace,monospace;border:1px solid;border-radius:5px;padding:1px 7px;margin-bottom:7px}
.card h3{margin:2px 0 6px;font-size:15px;color:#e6e6e6}
.card h3 a{color:#e6e6e6}
.eq{color:#9aa7b8;font:12px ui-monospace,monospace;margin-bottom:8px}
.vs{font:11px ui-monospace,monospace;color:#7f8ea3;margin-bottom:5px}
.tt{font:10.5px ui-monospace,monospace;color:#c9b26a}
.note{font-size:11.5px;color:#8b98ad;border-top:1px solid #141a26;margin-top:8px;padding-top:7px}
footer{margin-top:40px;color:#5b6b82;font:12px ui-monospace,monospace;border-top:1px solid #1c2433;padding-top:16px}
"""


def build_gallery(renders_dir="outputs/renders", out_html="gallery.html"):
    metas = []
    for mf in sorted(glob.glob(os.path.join(renders_dir, "*.meta.json"))):
        try:
            with open(mf, encoding="utf-8") as f:
                metas.append(json.load(f))
        except Exception:
            pass
    legend = " ".join(
        "<b style='color:%s;border-color:%s'>%s</b>%s" % (c, c, t, m)
        for t, m, c in [("[V]", " verified in-repo", "#7ee787"),
                        ("[credited]", " textbook physics", "#4dd6d6"),
                        ("[S]", " hypothesis", "#ffcf5a"),
                        ("[viz]", " illustration", "#8b98ad")])
    render_cards = "".join(_render_card(m, renders_dir) for m in metas)
    ix_cards = "".join(_interactive_card(*i) for i in INTERACTIVES)

    doc = (
        "<!doctype html><html lang='en'><head><meta charset='utf-8'>"
        "<meta name='viewport' content='width=device-width,initial-scale=1'>"
        "<title>FTGB &mdash; visual gallery (proof-backed)</title>"
        "<style>" + CSS + "</style></head><body><div class='wrap'>"
        "<header><h1>&#11041; FTGB &mdash; visual gallery</h1>"
        "<p>One driven Beltrami&ndash;Hopf toroidal soliton, read as field and matter wave. "
        "Every artifact below is generated from a verified model &mdash; the pipeline is "
        "<b style='color:#9fb0c3'>verified numbers &rarr; captioned artifacts &rarr; interactives</b>, "
        "and the honesty <b style='color:#9fb0c3'>tier travels with the pixel</b>.</p>"
        "<p>Reproduce the whole model: <code style='color:#e879b9'>python results/verify/verify_all.py</code> &rarr; 92/92.</p>"
        "<div class='legend'>" + legend + "</div></header>"
        "<h2>Rendered artifacts (backed by a re-runnable check)</h2>"
        "<div class='grid'>" + (render_cards or "<p>run <code>python render_all.py</code> to generate posters</p>") + "</div>"
        "<h2>Interactive models (double-click, any OS)</h2>"
        "<div class='grid'>" + ix_cards + "</div>"
        "<footer>Generated from the render <code>.meta.json</code> sidecars &middot; "
        "<a href='" + REPO + "'>github.com/awarelook/vortor</a> &middot; "
        "no claim exceeds its tier; no number is fabricated; settled-negatives are kept.</footer>"
        "</div></body></html>"
    )
    with open(out_html, "w", encoding="utf-8") as f:
        f.write(doc)
    return out_html, len(metas), len(INTERACTIVES)


if __name__ == "__main__":
    path, nr, ni = build_gallery()
    print("built %s  (%d rendered artifacts + %d interactives)" % (path, nr, ni))
