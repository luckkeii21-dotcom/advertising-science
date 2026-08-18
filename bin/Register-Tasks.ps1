<#
.SYNOPSIS
  Register (or refresh) the two daily Windows Scheduled Tasks for the
  Advertising Science Engine. Run ONCE (re-run to update).

    EvAI-AdScience-Research : daily 07:00 IST -> Run-ScienceResearch.ps1
    EvAI-AdScience-Teacher  : daily 08:00 IST -> Run-ScienceTeacher.ps1

  Same survivability pattern as the weekly reports: WakeToRun,
  StartWhenAvailable, retries, interactive logon (inherits CLI + MCP auth).

.PARAMETER ResearchAt  Default 07:00.
.PARAMETER TeacherAt   Default 08:00.
.PARAMETER Unregister  Remove both tasks.
#>
[CmdletBinding()]
param(
  [string]$ResearchAt = '07:00',
  [string]$TeacherAt  = '08:00',
  [switch]$Unregister
)
$ErrorActionPreference = 'Stop'
$SkillDir = Split-Path -Parent $PSScriptRoot

$tasks = @(
  @{ Name = 'EvAI-AdScience-Research'; Launcher = Join-Path $SkillDir 'bin\Run-ScienceResearch.ps1'; At = $ResearchAt;
     Desc = 'Advertising Science Engine: daily research pass (YouTube harvest + watchlist -> codex + skill). 07:00 IST.'; Hours = 2 },
  @{ Name = 'EvAI-AdScience-Teacher';  Launcher = Join-Path $SkillDir 'bin\Run-ScienceTeacher.ps1';  At = $TeacherAt;
     Desc = 'Advertising Science Engine: daily teacher pass (lesson + quiz for Lucky, video Mon/Wed/Fri). 08:00 IST.'; Hours = 2 }
)

if($Unregister){
  foreach($t in $tasks){ Unregister-ScheduledTask -TaskName $t.Name -Confirm:$false -ErrorAction SilentlyContinue }
  Unregister-ScheduledTask -TaskName 'EvAI-AdScience-Watchdog' -Confirm:$false -ErrorAction SilentlyContinue
  Write-Host 'Removed all AdScience tasks.'
  return
}

foreach($t in $tasks){
  if(-not (Test-Path $t.Launcher)){ throw "Launcher not found: $($t.Launcher)" }
  $action = New-ScheduledTaskAction -Execute 'powershell.exe' `
    -Argument ("-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$($t.Launcher)`"")
  $trigger = New-ScheduledTaskTrigger -Daily -At $t.At
  $settings = New-ScheduledTaskSettingsSet `
    -WakeToRun `
    -StartWhenAvailable `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -ExecutionTimeLimit (New-TimeSpan -Hours $t.Hours) `
    -RestartCount 3 -RestartInterval (New-TimeSpan -Minutes 10) `
    -MultipleInstances IgnoreNew
  $principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited
  Register-ScheduledTask -TaskName $t.Name -Action $action -Trigger $trigger `
    -Settings $settings -Principal $principal -Description $t.Desc -Force | Out-Null
  Write-Host "Registered '$($t.Name)' daily $($t.At) IST. Next run: $((Get-ScheduledTaskInfo -TaskName $t.Name).NextRunTime)"
}
# ---- watchdog: relaunch any run that fired but never completed ----
# (Covers the 2026-08-18 failure: catch-up runs fired 4 min after boot and were
# terminated during logon settling; same family as the weekly-reports 2026-07-03 kill.)
$Watchdog = Join-Path $SkillDir 'bin\Watchdog-CatchUp.ps1'
if(-not (Test-Path $Watchdog)){ throw "Watchdog not found: $Watchdog" }
$wdAction = New-ScheduledTaskAction -Execute 'powershell.exe' `
  -Argument ("-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$Watchdog`"")
$wdLogon = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME
$wdLogon.Delay = 'PT6M'   # let the boot/logon storm settle before relaunching anything
$wdNoon  = New-ScheduledTaskTrigger -Daily -At '12:00'
$wdEve   = New-ScheduledTaskTrigger -Daily -At '20:00'
$wdSettings = New-ScheduledTaskSettingsSet `
  -StartWhenAvailable `
  -AllowStartIfOnBatteries `
  -DontStopIfGoingOnBatteries `
  -ExecutionTimeLimit (New-TimeSpan -Minutes 10) `
  -MultipleInstances IgnoreNew
$wdPrincipal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited
Register-ScheduledTask -TaskName 'EvAI-AdScience-Watchdog' -Action $wdAction `
  -Trigger $wdLogon,$wdNoon,$wdEve -Settings $wdSettings -Principal $wdPrincipal `
  -Description 'Watchdog: relaunches EvAI-AdScience-Research/Teacher if a day''s run fired but never completed. At logon +6 min, daily 12:00 and 20:00.' `
  -Force | Out-Null
Write-Host "Registered 'EvAI-AdScience-Watchdog' (logon +6 min, daily 12:00 and 20:00)."

Write-Host "Test now:  Start-ScheduledTask -TaskName 'EvAI-AdScience-Research'"
Write-Host "Remove:    ./Register-Tasks.ps1 -Unregister"
