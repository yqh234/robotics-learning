Add-Type -AssemblyName System.Drawing

$utf8 = [System.Text.Encoding]::UTF8
$root = "C:\Users\86136\Documents\Codex\2026-06-15\codex-codex"
$pagePath = Join-Path $root "outputs\robotics-paper-feishu-page.html"
$iconPath = Join-Path $root "outputs\robotics-paper-robot.ico"
$desktopPath = [Environment]::GetFolderPath("Desktop")
$shortcutName = $utf8.GetString([Convert]::FromBase64String("5py65Zmo5Lq66K665paHIEJyaWVmaW5nLmxuaw=="))
$description = $utf8.GetString([Convert]::FromBase64String("5omT5byA5q+P5pel5py65Zmo5Lq66K665paH5a+55q+U6aG16Z2i"))
$shortcutPath = Join-Path $desktopPath $shortcutName

$bitmap = New-Object System.Drawing.Bitmap 64, 64
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$graphics.Clear([System.Drawing.Color]::Transparent)

$bodyBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(244, 247, 250))
$accentBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(76, 76, 76))
$darkBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(58, 64, 72))
$linePen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(118, 128, 138), 3)
$accentPen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(76, 76, 76), 3)

$path = New-Object System.Drawing.Drawing2D.GraphicsPath
$radius = 10
$x = 12
$y = 18
$w = 40
$h = 34
$d = $radius * 2
$path.AddArc($x, $y, $d, $d, 180, 90)
$path.AddArc($x + $w - $d, $y, $d, $d, 270, 90)
$path.AddArc($x + $w - $d, $y + $h - $d, $d, $d, 0, 90)
$path.AddArc($x, $y + $h - $d, $d, $d, 90, 90)
$path.CloseFigure()

$graphics.FillEllipse($accentBrush, 27, 4, 10, 10)
$graphics.DrawLine($accentPen, 32, 14, 32, 21)
$graphics.FillPath($bodyBrush, $path)
$graphics.DrawPath($linePen, $path)
$graphics.FillEllipse($darkBrush, 23, 31, 6, 6)
$graphics.FillEllipse($darkBrush, 36, 31, 6, 6)
$graphics.DrawArc($accentPen, 24, 36, 17, 9, 15, 150)
$graphics.DrawLine($linePen, 8, 32, 12, 32)
$graphics.DrawLine($linePen, 52, 32, 56, 32)
$graphics.DrawLine($linePen, 22, 54, 22, 59)
$graphics.DrawLine($linePen, 42, 54, 42, 59)

$iconHandle = $bitmap.GetHicon()
$icon = [System.Drawing.Icon]::FromHandle($iconHandle)
$stream = [System.IO.File]::Open($iconPath, [System.IO.FileMode]::Create)
$icon.Save($stream)
$stream.Close()

$icon.Dispose()
$path.Dispose()
$graphics.Dispose()
$bitmap.Dispose()
$bodyBrush.Dispose()
$accentBrush.Dispose()
$darkBrush.Dispose()
$linePen.Dispose()
$accentPen.Dispose()

$shell = New-Object -ComObject WScript.Shell
$shortcut = $shell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = $pagePath
$shortcut.Arguments = ""
$shortcut.WorkingDirectory = Split-Path $pagePath
$shortcut.IconLocation = $iconPath
$shortcut.Description = $description
$shortcut.Save()

Write-Output $shortcutPath
