$root = "C:\Users\86136\Documents\Codex\2026-06-15\codex-codex"
$watchdog = Join-Path $root "work\robot-paper-cat-watchdog.ps1"
$startup = [Environment]::GetFolderPath("Startup")
$shortcutPath = Join-Path $startup "Robot Paper Cat.lnk"

$shell = New-Object -ComObject WScript.Shell
$shortcut = $shell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = "powershell.exe"
$shortcut.Arguments = "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$watchdog`""
$shortcut.WorkingDirectory = $root
$shortcut.IconLocation = Join-Path $root "outputs\robotics-paper-robot.ico"
$shortcut.Description = "Keep the robotics paper cat launcher running."
$shortcut.Save()

Start-Process powershell.exe -WindowStyle Hidden -ArgumentList @(
    "-NoProfile",
    "-ExecutionPolicy",
    "Bypass",
    "-File",
    $watchdog
)

Write-Host "Installed startup shortcut: $shortcutPath"
