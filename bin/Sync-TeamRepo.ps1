<#
.SYNOPSIS
  Publish the advertising-science skill + codex snapshot to the team repo
  EverythingAI-Pro/advertising-science. Called by the daily research run
  (RUNBOOK-RESEARCH.md step 5); safe to run by hand any time.

  Commits and pushes ONLY when something changed. Excludes machine state
  (state.json, runs/, cache/), Lucky's personal quiz files (_answers-inbox,
  _scoreboard, _rotation), and lesson videos (too heavy for git).

.PARAMETER RepoClone  Local clone path. Default E:\ClaudeCode\advertising-science.
#>
[CmdletBinding()]
param(
  [string]$RepoClone = 'E:\ClaudeCode\advertising-science'
)
$ErrorActionPreference = 'Stop'
$SkillDir = Split-Path -Parent $PSScriptRoot
$Root = (Resolve-Path (Join-Path $SkillDir '..\..\..')).Path
$Science = Join-Path $Root 'Obsidian God-level Marketing Vault\God-level Marketing\wiki\science'
$RepoUrl = 'https://github.com/EverythingAI-Pro/advertising-science.git'

# git writes progress to stderr; in PS 5.1 with EAP=Stop that becomes a fatal
# NativeCommandError, so every git call goes through this wrapper.
function G {
  $e = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
  $out = & git @args 2>&1 | ForEach-Object { "$_" }
  $script:GitExit = $LASTEXITCODE
  $ErrorActionPreference = $e
  return $out
}

if(-not (Test-Path (Join-Path $RepoClone '.git'))){
  G clone $RepoUrl $RepoClone | Out-Null
  if(-not (Test-Path (Join-Path $RepoClone '.git'))){ throw "clone failed: $RepoUrl" }
}
# tolerate an empty just-created repo (pull fails when origin has no commits)
G -C $RepoClone pull --rebase --quiet | Out-Null

# ---- skill files ----
foreach($f in 'SKILL.md','README.md','channels.json','RUNBOOK-RESEARCH.md','RUNBOOK-TEACHER.md'){
  $src = Join-Path $SkillDir $f
  if(Test-Path $src){ Copy-Item $src -Destination (Join-Path $RepoClone $f) -Force }
}
foreach($d in 'lib','bin'){
  $dst = Join-Path $RepoClone $d
  New-Item -ItemType Directory -Force -Path $dst | Out-Null
  Copy-Item (Join-Path $SkillDir "$d\*") -Destination $dst -Force
}

# ---- codex snapshot (vault science top-level .md files) ----
$codexDst = Join-Path $RepoClone 'references\codex'
New-Item -ItemType Directory -Force -Path $codexDst | Out-Null
Copy-Item (Join-Path $Science '*.md') -Destination $codexDst -Force

# ---- lessons (skip personal underscore files and video binaries) ----
$lessonsDst = Join-Path $RepoClone 'references\lessons'
New-Item -ItemType Directory -Force -Path $lessonsDst | Out-Null
Get-ChildItem (Join-Path $Science 'lessons') -Filter '*.md' |
  Where-Object { $_.Name -notlike '_*' } |
  ForEach-Object { Copy-Item $_.FullName -Destination $lessonsDst -Force }

# ---- .gitignore for the team repo ----
Set-Content -Path (Join-Path $RepoClone '.gitignore') -Value "state.json`nruns/`ncache/`n" -Encoding utf8

# ---- claim count for the commit message ----
$claims = 0
Get-ChildItem $codexDst -Filter '*.md' | ForEach-Object {
  $claims += ([regex]::Matches((Get-Content $_.FullName -Raw), '(?m)^### [A-Z]{2}-\d')).Count
}

# ---- commit + push only on change ----
G -C $RepoClone add -A | Out-Null
$pending = G -C $RepoClone status --porcelain
if(-not $pending){ Write-Output "team repo sync: no changes"; exit 0 }

$stamp = Get-Date -Format 'yyyy-MM-dd'
$msg = "Daily science sync ${stamp}: codex $claims claims`n`nCo-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
G -C $RepoClone commit -m $msg --quiet | Out-Null
if($script:GitExit -ne 0){ throw "commit failed" }
G -C $RepoClone push --quiet origin HEAD | Out-Null
if($script:GitExit -ne 0){ throw "push failed" }
Write-Output "team repo sync: pushed ($claims claims)"
