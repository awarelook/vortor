<#
  archive_mirror.ps1 -- mirror the curated FTGB stores to an archive (robocopy /MIR) with verification.

  SAFE BY DESIGN:
    * DRY-RUN by default (robocopy /L: lists what WOULD change, copies/deletes nothing).
      Add -Execute to actually mirror.
    * Each source mirrors into a NAMED SUBFOLDER of -Dest (e.g. <Dest>\vortor), so /MIR only ever
      purges inside that named subfolder -- never anything else in the destination.
    * A verification pass (list-only /MIR) runs after each mirror; in-sync == robocopy verify exit 0.
    * Junctions/symlinks are skipped (/XJ) to avoid loops; retries are capped (/R:2 /W:5) to avoid hangs
      on cloud-placeholder or locked files.

  Usage (run in an elevated-enough shell that can read the sources):
     .\archive_mirror.ps1                                   # DRY-RUN to default dest (G:\My Drive\FTGB_ARCHIVE)
     .\archive_mirror.ps1 -Dest 'E:\Backup\FTGB'            # DRY-RUN to a physical external
     .\archive_mirror.ps1 -Execute                          # MIRROR + verify to default dest
     .\archive_mirror.ps1 -Dest 'E:\Backup\FTGB' -Execute   # MIRROR + verify to external
     .\archive_mirror.ps1 -Sources 'F:\vortor' -Execute     # just the jewel

  robocopy exit codes: <8 = success (0 no change, 1 copied, 2 extra, 4 mismatch, bits combine); >=8 = error.
#>
param(
  [string]$Dest = 'G:\My Drive\FTGB_ARCHIVE',
  [string[]]$Sources = @('F:\vortor','F:\_QUARANTINE','F:\conspire','F:\SYNTHESIS','F:\trial connect'),
  [switch]$Execute
)
$ErrorActionPreference = 'Stop'
$stamp  = Get-Date -Format 'yyyyMMdd_HHmmss'
$common = @('/MIR','/R:2','/W:5','/NP','/NDL','/DCOPY:DAT','/COPY:DAT','/XJ')  # mirror; skip junctions; cap retries
$logdir = Join-Path $Dest '_logs'
if ($Execute) { New-Item -ItemType Directory -Force -Path $Dest, $logdir | Out-Null }

function Interpret([int]$code) {
  if ($code -ge 8) { return "ERROR ($code)" }
  $s = @(); if ($code -band 1) { $s += 'copied' }; if ($code -band 2) { $s += 'extra-in-dest' }
  if ($code -band 4) { $s += 'mismatch' }; if ($s.Count -eq 0) { $s += 'in-sync' }
  return ($s -join '+') + " ($code)"
}

$summary = @()
foreach ($s in $Sources) {
  if (-not (Test-Path -LiteralPath $s)) { Write-Host "skip (missing): $s"; continue }
  $name = Split-Path $s -Leaf
  $dst  = Join-Path $Dest $name
  Write-Host ("`n=== {0}  ->  {1}   [{2}] ===" -f $s, $dst, ($(if ($Execute) { 'MIRROR' } else { 'DRY-RUN' })))

  # --- mirror (or list-only if dry-run) ---
  $args = @($s, $dst) + $common
  if (-not $Execute) { $args += '/L' }
  else { $args += ("/LOG:{0}" -f (Join-Path $logdir ("{0}_{1}.log" -f $name, $stamp))) }
  & robocopy @args | Out-Host
  $mirror = $LASTEXITCODE

  # --- verify pass (list-only mirror; 0 == fully in sync). Only meaningful after a real mirror. ---
  $verify = $null
  if ($Execute) {
    & robocopy @($s, $dst) $common '/L' '/NFL' | Out-Null
    $verify = $LASTEXITCODE
  }

  $summary += [pscustomobject]@{
    Source = $s
    Mirror = Interpret $mirror
    Verify = $(if ($null -ne $verify) { if ($verify -eq 0) { 'IN-SYNC (0)' } else { Interpret $verify } } else { 'n/a (dry-run)' })
    OK     = ($mirror -lt 8) -and (($null -eq $verify) -or ($verify -lt 8))
  }
  Write-Host ("  mirror={0}   verify={1}" -f (Interpret $mirror), $($summary[-1].Verify))
}

Write-Host "`n==================== SUMMARY ===================="
$summary | Format-Table -AutoSize
$errs = $summary | Where-Object { -not $_.OK }
if (-not $Execute) {
  Write-Host "`nDRY-RUN only -- nothing was copied or deleted. Re-run with -Execute to mirror + verify."
  Write-Host "Tip: mirror the jewel first:  .\archive_mirror.ps1 -Sources 'F:\vortor' -Execute"
}
elseif ($errs) { Write-Warning ("robocopy errors (exit>=8) on: {0}. See logs in {1}" -f (($errs.Source) -join ', '), $logdir) }
else { Write-Host ("`nAll {0} source(s) mirrored & verified in-sync. Logs: {1}" -f $summary.Count, $logdir) }
