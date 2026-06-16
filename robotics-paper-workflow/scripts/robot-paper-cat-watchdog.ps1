$launcher = "C:\Users\86136\Documents\Codex\2026-06-15\codex-codex\work\robot-paper-dynamic-launcher.ps1"
$marker = "robot-paper-dynamic-launcher.ps1"

while ($true) {
    $running = Get-CimInstance Win32_Process -Filter "Name = 'powershell.exe'" |
        Where-Object { $_.CommandLine -like "*$marker*" -and $_.CommandLine -notlike "*robot-paper-cat-watchdog*" }

    if (-not $running -and (Test-Path $launcher)) {
        Start-Process powershell.exe -WindowStyle Hidden -ArgumentList @(
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            $launcher
        )
    }

    Start-Sleep -Seconds 20
}
