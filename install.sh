#!/bin/bash

set -e

echo "[*] Detecting OS and installing system dependencies..."

# Detect package manager
if [ -x "$(command -v apt-get)" ]; then
    PKG_MANAGER="apt-get"
    UPDATE_CMD="apt-get update"
    INSTALL_CMD="apt-get install -y"
elif [ -x "$(command -v dnf)" ]; then
    PKG_MANAGER="dnf"
    UPDATE_CMD="dnf makecache"
    INSTALL_CMD="dnf install -y"
elif [ -x "$(command -v yum)" ]; then
    PKG_MANAGER="yum"
    UPDATE_CMD="yum makecache"
    INSTALL_CMD="yum install -y"
elif [ -x "$(command -v pacman)" ]; then
    PKG_MANAGER="pacman"
    UPDATE_CMD="pacman -Sy"
    INSTALL_CMD="pacman -S --noconfirm"
else
    echo "[!] Unsupported OS: no known package manager found."
    exit 1
fi

# Update package index and install dependencies
$UPDATE_CMD

$INSTALL_CMD git gcc make wget tar ca-certificates \
    libffi-dev || true
$INSTALL_CMD libatlas-base-dev liblapack-dev libssl-dev build-essential || true
$INSTALL_CMD base-devel lapack blas || true # for Arch-based systems

# Clone the repo if not already present
if [ ! -d "xno_vn" ]; then
    echo "[*] Cloning repository..."
    git clone https://github.com/VN-Fin/xno_vn.git
fi

cd xno_vn

# Pull latest changes
echo "[*] Pulling latest changes..."
git pull origin main

echo "[*] Building and installing TA-Lib C library..."

cd /tmp
wget -q https://github.com/ta-lib/ta-lib/releases/download/v0.6.4/ta-lib-0.6.4-src.tar.gz
tar -xzf ta-lib-0.6.4-src.tar.gz
cd ta-lib-0.6.4
./configure --prefix=/usr
make
make install
cd ..
rm -rf ta-lib-0.6.4*

echo "[*] Installing Python TA-Lib wrapper..."
python3 -m pip install --upgrade pip
python3 -m pip install TA-Lib

echo "[*] Installing Python requirements..."
pip install -r requirements.txt

echo "[*] Installing project in editable mode..."
pip install -e .

echo "[✔] Setup completed successfully."

cd ..
echo "[*] Cleaning up cloned repo..."
rm -rf xno_vn

echo "[*] Cleaning up install script..."
rm -f install.sh

echo "[✔] All done. You can now use the 'xno' package."
