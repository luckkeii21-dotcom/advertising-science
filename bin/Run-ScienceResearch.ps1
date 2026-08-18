<#
.SYNOPSIS
  Launcher for the daily Advertising Science RESEARCH run. Launches a headless
  Claude Code session that executes RUNBOOK-RESEARCH.md. Called by the Windows
  task 'EvAI-AdScience-Research' daily 07:00 IST; runnable by hand any time.

.PARAMETER Model   Claude model. Default claude-opus-5.
.PARAMETER DryRun  Print the prompt, don't launch Claude.
#>
[CmdletBinding()]
param(
  [string]$Model = 'claude-opus-5',
  [switch]$DryRun
)
$ErrorActionPreference = 'Stop'
$SkillDir = Split-Path -Parent $PSScriptRoot
$Root = (Resolve-Path (Join-Path $SkillDir '..\..\..')).Path
Set-Location $Root

$stamp = (Get-Date -Format 'yyyy-MM-dd')
$runDir = Join-Path $SkillDir "runs\$stamp"
New-Item -ItemType Directory -Force -Path $runDir | Out-Null
$log = Join-Path $runDir 'research-launcher.log'
function Log($m){ $line = "[{0}] {1}" -f (Get-Date -Format 'HH:mm:ss'), $m; Write-Host $line; Add-Content -Path $log -Value $line -Encoding utf8 }

Log "=== Advertising Science research launcher ==="

# preflight
$fail = @()
foreach($exe in 'claude'){ if(-not (Get-Command $exe -ErrorAction SilentlyContinue)){ $fail += "missing exe: $exe" } }
if(-not (Test-Path (Join-Path $Root '.venv-research\Scripts\python.exe'))){ $fail += 'missing .venv-research python' }
if($fail.Count){ Log ("PREFLIGHT FAILED: " + ($fail -join '; ')); exit 1 }
Log "preflight OK"

$promptTemplate = @'
You are running the Advertising Science Engine daily RESEARCH pass. Work from the runbook exactly, do not improvise the structure.

1. Read .claude/skills/advertising-science/SKILL.md and .claude/skills/advertising-science/RUNBOOK-RESEARCH.md.
2. Execute RUNBOOK-RESEARCH.md top to bottom for today.
3. Always leave .claude/skills/advertising-science/runs/__STAMP__-research-log.md, even on a quiet or failed day, so the run is visible.

Honesty rules: only bank claims from sources you actually read; a quiet day is a good result, log one line and stop. Writing style: no em dashes, no contrast negating, numbers over adjectives.
'@
$prompt = $promptTemplate.Replace('__STAMP__', $stamp)
Set-Content -Path (Join-Path $runDir 'research-prompt.txt') -Value $prompt -Encoding utf8

if($DryRun){ Log 'DRY RUN'; Write-Host "`n$prompt"; exit 0 }

Log "launching headless Claude (model=$Model)..."
$claudeLog = Join-Path $runDir 'research-claude.log'
# --dangerously-skip-permissions: trusted local automation, runs unattended.
& claude -p $prompt --model $Model --dangerously-skip-permissions *>&1 | Tee-Object -FilePath $claudeLog
$code = $LASTEXITCODE
Log "claude exited with code $code"
exit $code
