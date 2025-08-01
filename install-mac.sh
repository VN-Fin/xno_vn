#!/bin/bash

set -e

echo "[*] Checking for Xcode command line tools..."
if ! xcode-select -p &> /dev/null; then
    echo "[!] Xcode command line tools are not installed. Please install them by running: xcode-select --install"
    exit 1
fi

echo "[*] Checking for Homebrew..."
if ! command -v brew &> /dev/null; then
    echo "[*] Homebrew is not installed. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

echo "[*] Installing system dependencies using Homebrew..."
brew install git wget

echo "[*] Checking for Python 3..."
if ! command -v python3 &> /dev/null; then
    echo "[*] Installing Python 3 using Homebrew..."
    brew install python
fi

echo "[*] Upgrading pip..."
python3 -m pip install --upgrade pip setuptools wheel

echo "[*] Building and installing TA-Lib C library..."
cd /tmp
wget -q https://github.com/ta-lib/ta-lib/releases/download/v0.6.4/ta-lib-0.6.4-src.tar.gz
tar -xzf ta-lib-0.6.4-src.tar.gz
cd ta-lib-0.6.4
./configure --prefix=/usr/local
make
sudo make install
cd ..
rm -rf ta-lib-0.6.4*

echo "[*] Installing Python TA-Lib wrapper..."
python3 -m pip install TA-Lib

if [ ! -d "xno_vn" ]; then
    echo "[*] Cloning repository..."
    git clone https://github.com/VN-Fin/xno_vn.git
fi

cd xno_vn
echo "[*] Pulling latest changes..."
git pull origin main
echo "[*] Installing Python requirements..."
pip install -r requirements.txt
echo "[*] Installing project..."
pip install .
echo "[✔] Setup completed successfully."
cd ..

echo "[*] Cleaning up cloned repo..."
rm -rf xno_vn

echo "[*] Cleaning up install script..."
rm -f install.sh

echo "[✔] All done. You can now use the 'xno' package."