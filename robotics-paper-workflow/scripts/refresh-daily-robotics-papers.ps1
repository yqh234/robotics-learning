$Reason = "manual"
if ($args.Count -ge 2 -and $args[0] -eq "-Reason") {
    $Reason = $args[1]
}

$root = "C:\Users\86136\Documents\Codex\2026-06-15\codex-codex"
$utf8 = [System.Text.Encoding]::UTF8
$desktopLibrary = $utf8.GetString([Convert]::FromBase64String("QzpcVXNlcnNcODYxMzZcRGVza3RvcFzmnLrlmajkurrorrrmlocgUERGcw=="))
$repoWorkflow = Join-Path $root "work\robotics-learning\robotics-paper-workflow"
$outputs = Join-Path $root "outputs"
$logPath = Join-Path $desktopLibrary "refresh.log"

New-Item -ItemType Directory -Force -Path $desktopLibrary | Out-Null

$libraryIndex = Join-Path $outputs "paper-folder-index.html"
if (Test-Path $libraryIndex) {
    Copy-Item -LiteralPath $libraryIndex -Destination (Join-Path $desktopLibrary "index.html") -Force
}

$libraryIndexEn = Join-Path $outputs "paper-folder-index-en.html"
if (Test-Path $libraryIndexEn) {
    Copy-Item -LiteralPath $libraryIndexEn -Destination (Join-Path $desktopLibrary "index-en.html") -Force
}

$translationSource = Join-Path $outputs "translations"
if (Test-Path $translationSource) {
    Copy-Item -LiteralPath $translationSource -Destination $desktopLibrary -Recurse -Force
}

$launcherMarker = "robot-paper-dynamic-launcher.ps1"
$launcher = Join-Path $root "work\robot-paper-dynamic-launcher.ps1"
$launcherRunning = Get-CimInstance Win32_Process -Filter "Name = 'powershell.exe'" |
    Where-Object { $_.CommandLine -like "*$launcherMarker*" }
if (-not $launcherRunning -and (Test-Path $launcher)) {
    Start-Process powershell.exe -WindowStyle Hidden -ArgumentList @("-NoProfile", "-ExecutionPolicy", "Bypass", "-File", $launcher)
}

$briefing = Join-Path $outputs "robotics-paper-feishu-page.html"
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
Add-Content -LiteralPath $logPath -Value "$timestamp refresh triggered ($Reason)"

if (Test-Path $briefing) {
    Start-Process -FilePath $briefing
}
