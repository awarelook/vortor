"""
dedup_scan.py -- reproducible triage of a downloads/inbox folder for the FTGB quarantine tooling.

Produces (into OUT):  candidates.csv, MANIFEST.md, quarantine_move.ps1
Tiers (all KEEP one canonical per group; nothing is moved or deleted here):
  A-version : explicit version series  name_vN(.ext)          -> keep highest version
  B-copies  : "(n)" copies of a titled document               -> keep newest
  C-auto    : collision-named DISTINCT files (generated-image, files*.zip, OIP-<id>, screenshots)
              -> REVIEW-ONLY, never in the move set (reported for size only)
  D-hash    : BYTE-IDENTICAL duplicates (SHA-256), any names   -> keep one, quarantine the rest
Merge rule: a file is QUARANTINE if any tier says so; the canonical KEEP is chosen consistently
(prefer an existing KEEP / protected primary; else newest). No group is ever fully quarantined.

Usage:  python dedup_scan.py
"""
import os, re, csv, time, hashlib
from collections import defaultdict

DOWNLOADS = r'C:\Users\natha\Downloads'
OUT       = r'F:\_QUARANTINE\2026-09-09'
PROTECT = {'larry_reed_qwm_derivations.md','tuft jenny nielsen.pdf','dtorti qe 2-4.pdf',
           'storti_egm_missing.md','excision-protocol-storti-factor.md'}
AUTO = re.compile(r'^(generated-image|files\b|files\d|OIP[-_]|image|images|download|screenshot|'
                  r'img[-_ ]|photo|Untitled|clipboard|unnamed|paste)', re.I)
VER  = re.compile(r'^(?P<base>.+?)[ _]v(?P<ver>\d+)(\s*\(\d+\))?$', re.I)
COPY = re.compile(r'^(?P<base>.+?)\s*\((?P<c>\d+)\)$')
os.makedirs(OUT, exist_ok=True)

# ---- enumerate ----
F=[]
for n in os.listdir(DOWNLOADS):
    p=os.path.join(DOWNLOADS,n)
    if os.path.isfile(p):
        try: st=os.stat(p)
        except OSError: continue
        F.append({'n':n,'ext':os.path.splitext(n)[1].lower(),'size':st.st_size,'mt':st.st_mtime})
byname={f['n']:f for f in F}

# decision store: name -> dict(tier, action, cluster, hash8)
dec={}
def mark(name,tier,action,cluster,hash8=''):
    # first assignment wins for KEEP; QUARANTINE never overrides a protected KEEP
    if name.lower() in PROTECT:
        dec[name]={'tier':tier if tier else 'protected','action':'KEEP','cluster':cluster,'hash8':hash8}; return
    cur=dec.get(name)
    if cur and cur['action']=='QUARANTINE': return           # already slated to move; keep first tier
    if cur and cur['action']=='KEEP' and action=='QUARANTINE': return  # keep the KEEP
    dec[name]={'tier':tier,'action':action,'cluster':cluster,'hash8':hash8}

# ---- name-based A/B ----
tierA=defaultdict(list); tierB=defaultdict(list); tierC=defaultdict(list)
for f in F:
    stem=os.path.splitext(f['n'])[0]
    if f['n'].lower() in PROTECT: continue
    m=VER.match(stem)
    if m: tierA[(m.group('base').strip().lower(),f['ext'])].append((f,int(m.group('ver')))); continue
    if AUTO.match(stem): tierC[(re.sub(r'\s*\(\d+\)$','',stem).lower(),f['ext'])].append(f); continue
    mc=COPY.match(stem); base=(mc.group('base').strip() if mc else stem)
    tierB[(base.lower(),f['ext'])].append(f)

for key,v in tierA.items():
    if len(v)<2: continue
    v=sorted(v,key=lambda t:(t[1],t[0]['mt'])); keep=v[-1][0]
    mark(keep['n'],'A-version','KEEP',key[0]+key[1])
    for f,_ in v[:-1]: mark(f['n'],'A-version','QUARANTINE',key[0]+key[1])
for key,v in tierB.items():
    if len(v)<2: continue
    v=sorted(v,key=lambda f:f['mt']); keep=v[-1]
    mark(keep['n'],'B-copies','KEEP',key[0]+key[1])
    for f in v[:-1]: mark(f['n'],'B-copies','QUARANTINE',key[0]+key[1])

# ---- D: byte-identical (size -> partial hash -> full hash) ----
def h(path,limit=None):
    hsh=hashlib.sha256();
    with open(path,'rb') as fh:
        if limit: hsh.update(fh.read(limit))
        else:
            for chunk in iter(lambda: fh.read(1<<20), b''): hsh.update(chunk)
    return hsh.hexdigest()

bysize=defaultdict(list)
for f in F: bysize[f['size']].append(f)
size_groups=[v for s,v in bysize.items() if len(v)>1 and s>0]
# partial hash within size groups
part=defaultdict(list)
for grp in size_groups:
    for f in grp:
        try: ph=h(os.path.join(DOWNLOADS,f['n']),limit=1<<18)   # first 256KB
        except OSError: continue
        part[(f['size'],ph)].append(f)
# full hash only for partial-collisions
full=defaultdict(list); nfull=0
for key,grp in part.items():
    if len(grp)<2: continue
    for f in grp:
        try: fh=h(os.path.join(DOWNLOADS,f['n'])); nfull+=1
        except OSError: continue
        full[fh].append(f)

d_quar=0
for hh,grp in full.items():
    if len(grp)<2: continue
    # canonical: an existing KEEP / protected, else a not-yet-quarantined newest, else newest
    keeps=[f for f in grp if f['n'].lower() in PROTECT or (dec.get(f['n'],{}).get('action')=='KEEP')]
    if keeps: canonical=sorted(keeps,key=lambda f:f['mt'])[-1]
    else:
        free=[f for f in grp if dec.get(f['n'],{}).get('action')!='QUARANTINE'] or grp
        canonical=sorted(free,key=lambda f:f['mt'])[-1]
    mark(canonical['n'],'D-hash','KEEP','hash:'+hh[:8],hh[:8])
    for f in grp:
        if f['n']==canonical['n']: continue
        if dec.get(f['n'],{}).get('action')=='QUARANTINE':          # already moving via A/B
            dec[f['n']]['hash8']=hh[:8]; continue
        mark(f['n'],'D-hash','QUARANTINE','hash:'+hh[:8],hh[:8]); d_quar+=1

# ---- write candidates.csv ----
rows=[]
for name,d in dec.items():
    f=byname.get(name);
    if not f: continue
    rows.append([d['cluster'],d['tier'],d['action'],name,round(f['size']/1e3,1),
                 time.strftime('%Y-%m-%d',time.localtime(f['mt'])),d['hash8']])
rows.sort(key=lambda r:(r[1],r[0],r[2]))
with open(os.path.join(OUT,'candidates.csv'),'w',encoding='utf-8',newline='') as fp:
    w=csv.writer(fp); w.writerow(['cluster','tier','action','file','sizeKB','date','hash8']); w.writerows(rows)

def q(tier): return [r for r in rows if r[2]=='QUARANTINE' and r[1]==tier]
def gb(rs): return sum(r[4] for r in rs)*1e3/1e9
nA,nB,nD=len(q('A-version')),len(q('B-copies')),len(q('D-hash'))
allq=[r for r in rows if r[2]=='QUARANTINE']
cCount=sum(len(v) for v in tierC.values() if len(v)>1); cSize=sum(f['size'] for v in tierC.values() if len(v)>1 for f in v)
print(f"Downloads: {len(F)} files, {sum(f['size'] for f in F)/1e9:.1f} GB   (full-hashed {nfull} files)")
print(f"Tier A (version series)      quarantine: {nA}")
print(f"Tier B ((n) copies)          quarantine: {nB}")
print(f"Tier D (byte-identical NEW)  quarantine: {nD}   <-- content-hash dedup adds these")
print(f"TOTAL quarantine: {len(allq)}   reclaimable: {gb(allq):.2f} GB")
print(f"Tier C (auto-named, review-only, NOT moved): {cCount} files, {cSize/1e9:.2f} GB")

# ---- write MANIFEST.md ----
man=f"""# Quarantine manifest -- batch 2026-09-09 (Downloads triage, name + content-hash)

**Source:** `C:\\\\Users\\\\natha\\\\Downloads` ({len(F)} files, {sum(f['size'] for f in F)/1e9:.1f} GB) - **Generated:** 2026-09-09
**Action taken:** NONE. `candidates.csv` lists KEEP vs QUARANTINE; the mover is dry-run by default.
**Reproduce:** `python F:\\\\vortor\\\\results\\\\verify\\\\dedup_scan.py`

## Summary
| Tier | What | -> quarantine | Confidence |
|---|---|---|---|
| A | explicit version series (`..._vN`) | {nA} | high |
| B | `(n)` copies of titled docs (keep newest) | {nB} | medium |
| D | **byte-identical (SHA-256) duplicates, any names** | {nD} | **exact** |
| - | **TOTAL to quarantine** | **{len(allq)}** ({gb(allq):.2f} GB) | |
| C | auto-named collision series (distinct files) | 0 (review-only) | {cCount} files, {cSize/1e9:.2f} GB - NOT moved |

## Method
- **D (content hash)** cascades size -> first-256KB hash -> full SHA-256, so only genuine collisions are fully
  read. A `D-hash` group is byte-identical; one canonical is KEPT (preferring an existing KEEP / protected
  primary, else newest), the rest quarantined. `hash8` in the CSV is the short digest.
- **KEEP heuristic:** highest version (A) / newest (B) / canonical (D). Edit `candidates.csv` if a different
  member is canonical.
- **Protected (never moved):** the folded primaries (Reed / Nielsen / Storti sources).
- **Tier C** (generated-image, files*.zip, OIP-<id>, screenshots) are collision-named but DISTINCT content;
  they are never in the move set -- sort by hand.

## Run (safe; nothing moves without -Execute)
```powershell
cd 'F:\\_QUARANTINE\\2026-09-09'
.\\quarantine_move.ps1                     # dry-run, Tier A only
.\\quarantine_move.ps1 -Tier D             # dry-run, byte-identical duplicates only (safest of all)
.\\quarantine_move.ps1 -Tier All           # dry-run, A + B + D
.\\quarantine_move.ps1 -Tier D -Execute    # move exact duplicates (zero information loss)
.\\quarantine_move.ps1 -Tier All -Execute  # then the rest
```
Restore by moving anything back to Downloads. KEEP rows are never touched. `EXCISION_LEDGER.md` (in the jewel)
tracks false/numerology *claims* separately.
"""
open(os.path.join(OUT,'MANIFEST.md'),'w',encoding='utf-8').write(man)

# ---- write move script (A/B/D/All) ----
ps=r'''<#  quarantine_move.ps1 -- move superseded / duplicate candidates from Downloads into this folder.
    SAFE BY DEFAULT (dry-run). Nothing moves unless -Execute. KEEP rows are never touched. Files are MOVED
    (reversible), never deleted. Tiers: A=version series, B=(n) copies, D=byte-identical, All=A+B+D.
      .\quarantine_move.ps1                    # dry-run, Tier A
      .\quarantine_move.ps1 -Tier D            # dry-run, exact duplicates only
      .\quarantine_move.ps1 -Tier D -Execute   # move exact duplicates (zero info loss)
      .\quarantine_move.ps1 -Tier All -Execute #>
param([ValidateSet('A','B','D','All')][string]$Tier='A',[switch]$Execute)
$ErrorActionPreference='Stop'
$here=Split-Path -Parent $MyInvocation.MyCommand.Path
$src='C:\Users\natha\Downloads'
$csv=Join-Path $here 'candidates.csv'
if(-not(Test-Path -LiteralPath $csv)){throw "candidates.csv not found."}
$log=Join-Path $here ("move-log_{0}.txt" -f (Get-Date -Format 'yyyyMMdd_HHmmss'))
$rows=Import-Csv -LiteralPath $csv | Where-Object {$_.action -eq 'QUARANTINE'}
switch($Tier){ 'A'{$rows=$rows|?{$_.tier -eq 'A-version'}} 'B'{$rows=$rows|?{$_.tier -eq 'B-copies'}} 'D'{$rows=$rows|?{$_.tier -eq 'D-hash'}} }
$n=0;$moved=0;$missing=0
foreach($r in $rows){
  $from=Join-Path $src $r.file
  if(-not(Test-Path -LiteralPath $from)){$missing++;continue}
  $n++; $to=Join-Path $here $r.file; $i=1
  while(Test-Path -LiteralPath $to){$to=Join-Path $here (("_dup{0}_" -f $i)+$r.file);$i++}
  if($Execute){Move-Item -LiteralPath $from -Destination $to;$moved++;Add-Content -LiteralPath $log -Value ("MOVED`t{0}`t->`t{1}" -f $from,$to)}
  else{Write-Host ("[dry-run] would move: {0}" -f $r.file)}
}
Write-Host ""
if($Execute){Write-Host ("DONE. Moved {0} Tier-{1} file(s). (missing: {2}) Log: {3}" -f $moved,$Tier,$missing,$log)}
else{Write-Host ("DRY-RUN: {0} Tier-{1} file(s) WOULD move (missing: {2}). Re-run with -Execute." -f $n,$Tier,$missing)}
'''
open(os.path.join(OUT,'quarantine_move.ps1'),'w',encoding='utf-8').write(ps)
print("wrote candidates.csv, MANIFEST.md, quarantine_move.ps1 ->", OUT)
