#!/usr/bin/env bash
# Universal AI Skill Framework (UASF) — Linux / macOS Terminal Installer
set -e

echo "=== Universal AI Skill Framework (UASF) Installer ==="

# Check Python 3
if ! command -v python3 &>/dev/null; then
    echo "[!] Error: python3 is required but not installed." >&2
    exit 1
fi

echo "[*] Detected Python: $(python3 --version)"

# Check pip
if ! command -v pip3 &>/dev/null && ! command -v pip &>/dev/null; then
    echo "[!] Error: pip is required but not installed." >&2
    exit 1
fi

PIP_CMD="pip3"
if ! command -v pip3 &>/dev/null; then
    PIP_CMD="pip"
fi

# Install in user directory or virtual environment
echo "[*] Installing UASF package..."
$PIP_CMD install --upgrade --user .

# Verify installation
if command -v uasf &>/dev/null; then
    echo "[+] UASF installed successfully!"
    uasf modules
else
    echo "[*] UASF installed into user site-packages."
    echo "[*] Ensure ~/.local/bin is in your PATH to run 'uasf' directly."
    python3 -m uasf modules
fi
