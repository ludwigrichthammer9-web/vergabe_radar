# Iteration 9: Leser-Läufe automatisch starten (je Teil eine neue, leere Sitzung ohne Projektkontext).
#
# Aufruf (PowerShell, im Projektordner):
#   powershell -ExecutionPolicy Bypass -File src\prepare\leser_lauf_iteration9.ps1 -Leser a     # Opus
#   powershell -ExecutionPolicy Bypass -File src\prepare\leser_lauf_iteration9.ps1 -Leser b     # Sonnet
#   Optional: -Teile 3,4,5   (nur diese Teile; Standard: alle Teile, für die noch keine Antwortdatei im Projekt liegt)
#
# Was das Skript tut, je Teil:
#   1. entpackt pakete\teil_k.zip in einen neuen, leeren Ordner C:\leser9\<leser>_teil<k> (außerhalb des Projekts),
#   2. prüft, dass in keinem übergeordneten Ordner eine CLAUDE.md liegt (Nachweis ersetzt /memory), und schreibt das ins Protokoll,
#   3. startet eine neue Claude-Sitzung (claude -p) in diesem Ordner mit dem Satz aus start_prompt.txt, nur mit den Werkzeugen Read und Write,
#      ohne Skills, ohne MCP-Server, ohne gespeicherte Sitzung,
#   4. kopiert die entstandene ergebnis.tsv unverändert nach reports\zweitlesung_iteration9_roh\leser_<leser>_teil<k>.tsv,
#   5. prüft Spaltenzahl (16) und die Nummern gegen aufgabe.md und schreibt ein Protokoll nach C:\leser9\protokoll_<leser>.txt.
# Das Skript ändert nichts an Inhalten und wiederholt nichts automatisch.

param(
    [Parameter(Mandatory = $true)][ValidateSet("a", "b")][string]$Leser,
    [string]$Teile = "1,2,3,4,5"   # als Text, weil powershell -File "3,4,5" sonst zu 345 zusammenzieht
)
$teilListe = @($Teile -split '[,\s]+' | Where-Object { $_ } | ForEach-Object { [int]$_ })   # nicht $Teile überschreiben: der Parameter ist vom Typ string

$ErrorActionPreference = "Stop"
$projekt = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$pakete = Join-Path $projekt "reports\zweitlesung_iteration9\pakete"
$ziel = Join-Path $projekt "reports\zweitlesung_iteration9_roh"
$prompt = (Get-Content (Join-Path $projekt "reports\zweitlesung_iteration9\start_prompt.txt") -Raw -Encoding UTF8).Trim()
$basis = "C:\leser9"
$modell = if ($Leser -eq "a") { "claude-opus-5-5" } else { "claude-sonnet-5-5" }
$claude = Get-ChildItem "$env:USERPROFILE\.vscode\extensions" -Directory -Filter "anthropic.claude-code*" |
    Sort-Object Name -Descending | ForEach-Object { Join-Path $_.FullName "resources\native-binary\claude.exe" } |
    Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $claude) { throw "claude.exe nicht gefunden (VS-Code-Erweiterung)." }

New-Item -ItemType Directory -Force $basis, $ziel | Out-Null
$protokoll = Join-Path $basis "protokoll_$Leser.txt"
function Log($text) { $z = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')  $text"; Write-Host $z; Add-Content $protokoll $z -Encoding UTF8 }

Log "Start Leser $Leser, Modell $modell, claude $(& $claude --version)"
foreach ($k in $teilListe) {
    $antwort = Join-Path $ziel "leser_${Leser}_teil$k.tsv"
    if (Test-Path $antwort) { Log "Teil ${k}: Antwortdatei liegt schon im Projekt, übersprungen."; continue }
    $ordner = Join-Path $basis "${Leser}_teil$k"
    if (Test-Path $ordner) { Log "Teil ${k}: Ordner $ordner existiert schon. Bitte prüfen oder löschen, übersprungen."; continue }

    Expand-Archive -Path (Join-Path $pakete "teil_$k.zip") -DestinationPath $ordner
    $eltern = @(); $p = Split-Path $ordner -Parent
    while ($p) { if (Test-Path (Join-Path $p "CLAUDE.md")) { $eltern += $p }; $n = Split-Path $p -Parent; if ($n -eq $p) { break }; $p = $n }
    if ($eltern.Count -gt 0 -or (Test-Path (Join-Path $ordner "CLAUDE.md"))) { throw "CLAUDE.md gefunden in: $($eltern -join ', ')" }
    Log "Teil ${k}: Ordner $ordner angelegt, keine CLAUDE.md im Ordner oder in übergeordneten Ordnern."

    Push-Location $ordner
    try {
        $ausgabe = & $claude -p $prompt --model $modell --effort high --permission-mode acceptEdits --tools "Read,Write" `
            --disable-slash-commands --strict-mcp-config --no-session-persistence 2>&1
        Log "Teil ${k}: Sitzung beendet (Exitcode $LASTEXITCODE)."
    }
    finally { Pop-Location }
    Set-Content (Join-Path $basis "${Leser}_teil${k}_chat.txt") ($ausgabe | Out-String) -Encoding UTF8

    $tsv = Join-Path $ordner "ergebnis.tsv"
    if (-not (Test-Path $tsv)) { Log "Teil ${k}: KEINE ergebnis.tsv entstanden, siehe ${Leser}_teil${k}_chat.txt. Nichts kopiert."; continue }
    $zeilen = [IO.File]::ReadAllLines($tsv, [Text.Encoding]::UTF8)
    $falsch = @($zeilen | Where-Object { ($_ -split "`t").Count -ne 16 }).Count
    $soll = @(Select-String -Path (Join-Path $ordner "aufgabe.md") -Pattern '^\|\s*(N\d+)\s*\|' | ForEach-Object { $_.Matches[0].Groups[1].Value })
    $ist = @($zeilen | Select-Object -Skip 1 | ForEach-Object { ($_ -split "`t")[0] })
    $fehlt = @($soll | Where-Object { $_ -notin $ist }); $zuviel = @($ist | Where-Object { $_ -notin $soll })
    Copy-Item $tsv $antwort
    $hash = (Get-FileHash $antwort).Hash
    Log "Teil ${k}: kopiert nach $antwort, $($zeilen.Count - 1) Zeilen, Zeilen mit falscher Spaltenzahl: $falsch, fehlende Nummern: $($fehlt -join ',') , überzählige: $($zuviel -join ','), SHA-256 $hash"
}
Log "Fertig."
