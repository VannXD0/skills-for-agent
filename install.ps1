# Universal AI Skill Framework (UASF) — Windows PowerShell Installer
$ErrorActionPreference = "Stop"

Write-Host "=== Universal AI Skill Framework (UASF) Installer ===" -ForegroundColor Cyan

# Check Python
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    Write-Error "Python 3 is required but not found in PATH."
    exit 1
}

$pyVer = & python --version
Write-Host "[*] Detected: $pyVer" -ForegroundColor Gray

# Install package locally
Write-Host "[*] Installing UASF package via pip..." -ForegroundColor Yellow
& python -m pip install --upgrade --user .

# Ensure Python Scripts directory is in user PATH
$userScripts = Join-Path ([Environment]::GetFolderPath("ApplicationData")) "Python\Python311\Scripts"
if (Test-Path $userScripts) {
    $currentEnvPath = [Environment]::GetEnvironmentVariable("PATH", "User")
    if ($currentEnvPath -notmatch [regex]::Escape($userScripts)) {
        Write-Host "[*] Adding $userScripts to User PATH..." -ForegroundColor Cyan
        [Environment]::SetEnvironmentVariable("PATH", "$currentEnvPath;$userScripts", "User")
    }
    if ($env:PATH -notmatch [regex]::Escape($userScripts)) {
        $env:PATH = "$env:PATH;$userScripts"
    }
}

# Verify
$uasfCmd = Get-Command uasf -ErrorAction SilentlyContinue
if ($uasfCmd) {
    Write-Host "[+] UASF installed successfully and executable from terminal!" -ForegroundColor Green
    & uasf modules
} else {
    Write-Host "[*] UASF installed into Python Scripts folder." -ForegroundColor Yellow
    Write-Host "[*] Testing execution via module runner:" -ForegroundColor Gray
    & python -m uasf modules
}
