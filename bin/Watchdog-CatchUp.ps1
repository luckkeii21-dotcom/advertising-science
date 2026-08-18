<#
.SYNOPSIS
  Watchdog for the Advertising Science Engine. If today's research or teacher
  run never COMPLETED (fired-then-killed counts as never completed), relaunch
  it. Registered at logon +6 min and daily 12:00 and 20:00.

  Completion markers (written by the runbook sessions):
    research : runs\<yyyy-MM-dd>-research-log.md
    teacher  : runs\<yyyy-MM-dd>-teacher-log.md

  Rules: research before teacher (teacher reads the day's harvest); max one
  watchdog relaunch per run per day (flag files); skip anything currently running.
#>
$ErrorActionPreference = 'Stop'
$SkillDir = Split-Path -Parent $PSScriptRoot
$stamp = (Get-Date -Format 'yyyy-MM-dd')
$runDir = Join-Path $SkillDir "runs\$stamp"
New-Item -ItemType Directory -Force -Path $runDir | Out-Null
$log = Join-Path $runDir 'watchdog.log'
function Log($m){ Add-Content -Path $log -Value ("[{0}] {1}" -f (Get-Date -Format 'HH:mm:ss'), $m) -Encoding utf8 }

function TaskRunning($name){ (Get-ScheduledTask -TaskName $name -ErrorAction SilentlyContinue).State -eq 'Running' }

$researchDone = Test-Path (Join-Path $SkillDir "runs\$stamp-research-log.md")
$teacherDone  = Test-Path (Join-Path $SkillDir "runs\$stamp-teacher-log.md")
$researchFlag = Join-Path $runDir 'watchdog-research.flag'
$teacherFlag  = Join-Path $runDir 'watchdog-teacher.flag'

if(TaskRunning 'EvAI-AdScience-Research' -or (TaskRunning 'EvAI-AdScience-Teacher')){
  Log 'a run is in progress; standing down'; exit 0
}

if(-not $researchDone){
  if(Test-Path $researchFlag){ Log 'research incomplete but already relaunched once today; standing down'; exit 0 }
  New-Item -ItemType File -Path $researchFlag -Force | Out-Null
  Log 'research run incomplete; relaunching EvAI-AdScience-Research'
  Start-ScheduledTask -TaskName 'EvAI-AdScience-Research'
  exit 0   # teacher waits for a later watchdog pass, research must finish first
}

if(-not $teacherDone){
  if(Test-Path $teacherFlag){ Log 'teacher incomplete but already relaunched once today; standing down'; exit 0 }
  New-Item -ItemType File -Path $teacherFlag -Force | Out-Null
  Log 'teacher run incomplete; relaunching EvAI-AdScience-Teacher'
  Start-ScheduledTask -TaskName 'EvAI-AdScience-Teacher'
  exit 0
}

Log 'both runs complete; nothing to do'
