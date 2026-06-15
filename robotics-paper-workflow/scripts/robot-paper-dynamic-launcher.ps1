Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$pagePath = "C:\Users\86136\Documents\Codex\2026-06-15\codex-codex\outputs\robotics-paper-feishu-page.html"
$utf8 = [System.Text.Encoding]::UTF8
$libraryPath = (Join-Path ($utf8.GetString([Convert]::FromBase64String("QzpcVXNlcnNcODYxMzZcRGVza3RvcFzmnLrlmajkurrorrrmlocgUERGcw=="))) "index.html")
$refreshScript = "C:\Users\86136\Documents\Codex\2026-06-15\codex-codex\work\refresh-daily-robotics-papers.ps1"

[System.Windows.Forms.Application]::EnableVisualStyles()

$form = New-Object System.Windows.Forms.Form
$form.Width = 96
$form.Height = 132
$form.FormBorderStyle = "None"
$form.StartPosition = "Manual"
$form.TopMost = $true
$form.ShowInTaskbar = $false
$transparentColor = [System.Drawing.Color]::FromArgb(1, 1, 1)
$form.BackColor = $transparentColor
$form.TransparencyKey = $transparentColor
$form.Cursor = [System.Windows.Forms.Cursors]::Hand
$doubleBufferedProp = [System.Windows.Forms.Control].GetProperty("DoubleBuffered", [System.Reflection.BindingFlags] "NonPublic,Instance")
$doubleBufferedProp.SetValue($form, $true, $null)

$area = [System.Windows.Forms.Screen]::PrimaryScreen.WorkingArea
$form.Location = New-Object System.Drawing.Point(($area.Right - $form.Width - 28), ($area.Top + 88))

$state = @{
    Tick = 0
    Hover = $false
}

function Get-NextRefreshText {
    $now = Get-Date
    $next = Get-Date -Hour 17 -Minute 0 -Second 0
    if ($now -ge $next) {
        $next = $next.AddDays(1)
    }

    $remaining = $next - $now
    if ($remaining.TotalHours -ge 1) {
        return ("{0:00}:{1:00}:{2:00}" -f [Math]::Floor($remaining.TotalHours), $remaining.Minutes, $remaining.Seconds)
    }

    return ("{0:00}:{1:00}" -f $remaining.Minutes, $remaining.Seconds)
}

$form.Add_Click({
    Start-Process -FilePath $pagePath
})

$menu = New-Object System.Windows.Forms.ContextMenuStrip
$openBriefing = New-Object System.Windows.Forms.ToolStripMenuItem("Open briefing")
$openLibrary = New-Object System.Windows.Forms.ToolStripMenuItem("Open paper library")
$refreshNow = New-Object System.Windows.Forms.ToolStripMenuItem("Refresh now")
$exitItem = New-Object System.Windows.Forms.ToolStripMenuItem("Exit")
$openBriefing.Add_Click({ Start-Process -FilePath $pagePath })
$openLibrary.Add_Click({ Start-Process -FilePath $libraryPath })
$refreshNow.Add_Click({
    if (Test-Path $refreshScript) {
        Start-Process -FilePath powershell.exe -ArgumentList @("-NoProfile", "-ExecutionPolicy", "Bypass", "-File", $refreshScript) -WindowStyle Hidden
    }
})
$exitItem.Add_Click({ $form.Close() })
[void]$menu.Items.Add($openBriefing)
[void]$menu.Items.Add($openLibrary)
[void]$menu.Items.Add($refreshNow)
[void]$menu.Items.Add((New-Object System.Windows.Forms.ToolStripSeparator))
[void]$menu.Items.Add($exitItem)
$form.ContextMenuStrip = $menu

$form.Add_MouseEnter({
    $state.Hover = $true
    $form.Invalidate()
})

$form.Add_MouseLeave({
    $state.Hover = $false
    $form.Invalidate()
})

$form.Add_Paint({
    param($sender, $eventArgs)

    $g = $eventArgs.Graphics
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $g.Clear($transparentColor)

    $tick = $state.Tick
    $bob = [Math]::Sin($tick / 12.0) * 2
    $blink = (($tick % 120) -gt 112)
    $pulse = [int](14 + ([Math]::Sin($tick / 10.0) * 8))

    $shadowBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(32, 0, 0, 0))
    $glowBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb((42 + $pulse), 118, 118, 118))
    $bodyBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(252, 252, 252))
    $faceBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(255, 255, 255))
    $stripeBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(42, 42, 42))
    $accentBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(20, 20, 20))
    $eyeBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(0, 0, 0))
    $linePen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(24, 24, 24), 2.6)
    $accentPen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(0, 0, 0), 2.6)
    $textBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(20, 20, 20))
    $countFont = New-Object System.Drawing.Font("Times New Roman", 15, [System.Drawing.FontStyle]::Bold)

    $g.FillEllipse($shadowBrush, 25, 75, 46, 8)

    $originY = 18 + $bob
    $g.FillPie($bodyBrush, 24, ([int]$originY - 6), 20, 25, 200, 135)
    $g.FillPie($bodyBrush, 52, ([int]$originY - 6), 20, 25, 205, 135)
    $g.DrawArc($linePen, 24, ([int]$originY - 6), 20, 25, 205, 125)
    $g.DrawArc($linePen, 52, ([int]$originY - 6), 20, 25, 210, 125)

    $path = New-Object System.Drawing.Drawing2D.GraphicsPath
    $x = 20
    $y = [int]$originY
    $w = 56
    $h = 46
    $r = 18
    $d = $r * 2
    $path.AddArc($x, $y, $d, $d, 180, 90)
    $path.AddArc($x + $w - $d, $y, $d, $d, 270, 90)
    $path.AddArc($x + $w - $d, $y + $h - $d, $d, $d, 0, 90)
    $path.AddArc($x, $y + $h - $d, $d, $d, 90, 90)
    $path.CloseFigure()

    $g.FillPath($bodyBrush, $path)
    $g.DrawPath($linePen, $path)
    $g.FillEllipse($faceBrush, 23, ($y + 7), 50, 32)

    $g.FillEllipse($stripeBrush, 43, ($y + 8), 4, 12)
    $g.FillEllipse($stripeBrush, 49, ($y + 8), 4, 12)
    $g.DrawArc($linePen, 31, ($y + 10), 12, 14, 210, 70)
    $g.DrawArc($linePen, 53, ($y + 10), 12, 14, 260, 70)

    if ($blink) {
        $g.DrawLine($linePen, 34, ($y + 22), 42, ($y + 22))
        $g.DrawLine($linePen, 54, ($y + 22), 62, ($y + 22))
    } else {
        $g.FillEllipse($eyeBrush, 35, ($y + 18), 7, 7)
        $g.FillEllipse($eyeBrush, 55, ($y + 18), 7, 7)
    }

    $g.FillEllipse($eyeBrush, 46, ($y + 28), 4, 4)
    $g.DrawArc($accentPen, 39, ($y + 28), 9, 8, 20, 120)
    $g.DrawArc($accentPen, 49, ($y + 28), 9, 8, 40, 120)
    $g.DrawLine($linePen, 29, ($y + 29), 16, ($y + 25))
    $g.DrawLine($linePen, 29, ($y + 32), 16, ($y + 32))
    $g.DrawLine($linePen, 29, ($y + 35), 16, ($y + 39))
    $g.DrawLine($linePen, 67, ($y + 29), 80, ($y + 25))
    $g.DrawLine($linePen, 67, ($y + 32), 80, ($y + 32))
    $g.DrawLine($linePen, 67, ($y + 35), 80, ($y + 39))
    $g.DrawLine($linePen, 14, ($y + 23), 20, ($y + 23))
    $g.DrawLine($linePen, 76, ($y + 23), 82, ($y + 23))
    $g.DrawLine($linePen, 34, ($y + 47), 34, ($y + 53))
    $g.DrawLine($linePen, 62, ($y + 47), 62, ($y + 53))

    $countdown = Get-NextRefreshText
    $centerFormat = New-Object System.Drawing.StringFormat
    $centerFormat.Alignment = [System.Drawing.StringAlignment]::Center
    $centerFormat.LineAlignment = [System.Drawing.StringAlignment]::Near
    $countRect = New-Object System.Drawing.RectangleF(-18, 82, $form.Width, 28)
    $g.DrawString($countdown, $countFont, $textBrush, $countRect, $centerFormat)

    $path.Dispose()
    $shadowBrush.Dispose()
    $glowBrush.Dispose()
    $bodyBrush.Dispose()
    $faceBrush.Dispose()
    $stripeBrush.Dispose()
    $accentBrush.Dispose()
    $eyeBrush.Dispose()
    $linePen.Dispose()
    $accentPen.Dispose()
    $textBrush.Dispose()
    $countFont.Dispose()
    $centerFormat.Dispose()
})

$timer = New-Object System.Windows.Forms.Timer
$timer.Interval = 16
$timer.Add_Tick({
    $state.Tick += 1
    $form.Invalidate()
})
$timer.Start()

[System.Windows.Forms.Application]::Run($form)
