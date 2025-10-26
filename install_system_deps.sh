#!/usr/bin/env bash
set -e

# Script to install common system packages required to build Python packages
# This script requires root privileges. Run with sudo: sudo bash install_system_deps.sh

if [ "$(id -u)" -ne 0 ]; then
  echo "This script installs OS packages and requires sudo/root. Run: sudo bash $0"
  exit 1
fi

echo "Detected root privileges. Installing system build dependencies..."

if command -v apt-get >/dev/null 2>&1; then
  apt-get update
  apt-get install -y python3-distutils python3-dev build-essential
  echo "(Debian/Ubuntu) Installed python3-distutils, python3-dev, build-essential"

elif command -v dnf >/dev/null 2>&1; then
  dnf install -y python3-distutils python3-devel @development-tools
  echo "(Fedora) Installed python3-distutils and development tools"

elif command -v pacman >/dev/null 2>&1; then
  pacman -S --noconfirm python-distutils-extra base-devel
  echo "(Arch) Installed python-distutils-extra and base-devel"

else
  echo "Unsupported package manager. Please install the equivalent of: distutils (or setuptools that provides it), python-devel and build tools for your distro."
  exit 1
fi

echo "System packages installed. Return to project and run: bash setup_venv.sh" 
