<#
.SYNOPSIS
  Launcher for the daily Advertising Science TEACHER run. Launches a headless
  Claude Code session that executes RUNBOOK-TEACHER.md. Called by the Windows
  task 'EvAI-AdScience-Teacher' daily 08:00 IST; runnable by hand any time.

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
$log = Join-Path $runDir 'teacher-launcher.log'
function Log($m){ $line = "[{0}] {1}" -f (Get-Date -Format 'HH:mm:ss'), $m; Write-Host $line; Add-Content -Path $log -Value $line -Encoding utf8 }

Log "=== Advertising Science teacher launcher ==="
if(-not (Get-Command claude -ErrorAction SilentlyContinue)){ Log 'PREFLIGHT FAILED: missing claude'; exit 1 }

$promptTemplate = @'
You are running the Advertising Science Engine daily TEACHER pass. The student is Lucky. Work from the runbook exactly.

1. Read .claude/skills/advertising-science/SKILL.md and .claude/skills/advertising-science/RUNBOOK-TEACHER.md.
2. Execute RUNBOOK-TEACHER.md top to bottom for today (grade inbox first, then lesson; video only on Mon/Wed/Fri).
3. Always leave .claude/skills/advertising-science/runs/__STAMP__-teacher-log.md so the run is visible.

Writing style: no em dashes, no contrast negating, short sentences, real numbers only, respect the student.
'@
$prompt = $promptTemplate.Replace('__STAMP__', $stamp)
Set-Content -Path (Join-Path $runDir 'teacher-prompt.txt') -Value $prompt -Encoding utf8

if($DryRun){ Log 'DRY RUN'; Write-Host "`n$prompt"; exit 0 }

Log "launching headless Claude (model=$Model)..."
$claudeLog = Join-Path $runDir 'teacher-claude.log'
& claude -p $prompt --model $Model --dangerously-skip-permissions *>&1 | Tee-Object -FilePath $claudeLog
$code = $LASTEXITCODE
Log "claude exited with code $code"
exit $code
