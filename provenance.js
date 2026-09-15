/* FTGB provenance chip -- a shared, self-contained honesty badge for the interactive HTML models.
 *
 * Each page declares, before including this file:
 *     <script>window.FTGB_PROVENANCE = {
 *         page:  "The Coherent Object",
 *         tier:  "[V] core / [S] frontier",
 *         checks:["ck_eigenvalues_check", "exact_beltrami_regularity_check"],  // results/verify/*.py
 *         note:  "one honest caveat"
 *     };</script>
 *     <script src="provenance.js"></script>
 *
 * It injects a small fixed chip that expands to name the page's honesty TIER, link the verify SCRIPT(s)
 * that reproduce its claims, and give the one-command reproduce. Same contract as the render sidecars:
 * the tier travels with the artifact -- a beautiful interactive never outruns what the math earns.
 * No external deps; works from file://; silently no-ops if no config is present.
 */
(function () {
  "use strict";
  var P = window.FTGB_PROVENANCE;
  if (!P) return;
  var REPO = "https://github.com/awarelook/vortor";
  var BLOB = REPO + "/blob/main/results/verify/";

  var TIERS = [
    ["[V]", "verified in-repo by a named check (re-runnable)"],
    ["[credited]", "established textbook physics we build on"],
    ["[S]", "structural hypothesis -- falsifiable, not proven"],
    ["[viz]", "illustrative presentation only (no evidentiary weight)"]
  ];

  var css = document.createElement("style");
  css.textContent =
    ".ftgb-prov{position:fixed;right:12px;bottom:12px;z-index:99999;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:12px}" +
    ".ftgb-prov *{box-sizing:border-box}" +
    ".ftgb-chip{cursor:pointer;background:#0b0e14ee;color:#9fb0c3;border:1px solid #33405a;border-radius:8px;padding:6px 10px;backdrop-filter:blur(4px);box-shadow:0 4px 18px #0008;user-select:none}" +
    ".ftgb-chip b{color:#4dd6d6}" +
    ".ftgb-chip .t{color:#ffcf5a}" +
    ".ftgb-panel{display:none;position:absolute;right:0;bottom:34px;width:340px;max-width:86vw;background:#0b0e14f7;color:#cfd8e3;border:1px solid #33405a;border-radius:10px;padding:14px 15px;box-shadow:0 10px 40px #000a;line-height:1.5}" +
    ".ftgb-panel.open{display:block}" +
    ".ftgb-panel h4{margin:0 0 6px;color:#e6e6e6;font-size:13px}" +
    ".ftgb-panel a{color:#7ee787;text-decoration:none;border-bottom:1px dotted #33506a}" +
    ".ftgb-panel a:hover{color:#a6f0b3}" +
    ".ftgb-panel code{color:#e879b9;background:#141a26;padding:1px 5px;border-radius:4px;font-size:11px}" +
    ".ftgb-panel .leg{color:#7f8ea3;font-size:10.5px;margin:8px 0 2px}" +
    ".ftgb-panel .leg b{color:#9fb0c3}" +
    ".ftgb-panel ul{margin:4px 0 8px;padding-left:16px}" +
    ".ftgb-panel .note{color:#c9b26a;font-size:11px;margin-top:8px;border-top:1px solid #1c2433;padding-top:8px}" +
    ".ftgb-x{float:right;cursor:pointer;color:#5b6b82}";
  document.head.appendChild(css);

  var root = document.createElement("div");
  root.className = "ftgb-prov";

  var checksHtml = (P.checks || []).map(function (c) {
    return "<li><a href='" + BLOB + c + ".py' target='_blank' rel='noopener'>" + c + "</a></li>";
  }).join("");

  var legHtml = TIERS.map(function (t) {
    return "<div><b>" + t[0] + "</b> &mdash; " + t[1] + "</div>";
  }).join("");

  root.innerHTML =
    "<div class='ftgb-panel' id='ftgbPanel'>" +
      "<span class='ftgb-x' id='ftgbX'>&#10005;</span>" +
      "<h4>&#11041; " + (P.page || "FTGB model") + "</h4>" +
      "<div>tier: <span style='color:#ffcf5a'>" + (P.tier || "[V]") + "</span></div>" +
      "<div style='margin-top:8px'>reproduced by:</div>" +
      "<ul>" + (checksHtml || "<li>(no check named)</li>") + "</ul>" +
      "<div>reproduce all: <code>python results/verify/verify_all.py</code> &rarr; 92/92</div>" +
      "<div class='leg'>" + legHtml + "</div>" +
      (P.note ? "<div class='note'>" + P.note + "</div>" : "") +
      "<div class='note' style='color:#5b6b82'><a href='" + REPO + "' target='_blank' rel='noopener'>github.com/awarelook/vortor</a> &middot; the tier travels with the artifact</div>" +
    "</div>" +
    "<div class='ftgb-chip' id='ftgbChip'>&#11041; <b>FTGB</b> &middot; <span class='t'>" + (P.tier || "[V]") + "</span> &middot; verify &#9656;</div>";

  document.body.appendChild(root);
  var panel = document.getElementById("ftgbPanel");
  document.getElementById("ftgbChip").addEventListener("click", function () { panel.classList.toggle("open"); });
  document.getElementById("ftgbX").addEventListener("click", function () { panel.classList.remove("open"); });
})();
