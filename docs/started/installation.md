
# Installation

## Linux

Run the following script in your terminal:

```bash
bash <(curl -s https://raw.githubusercontent.com/VN-Fin/xno_vn/main/install-linux.sh)
```

## Windows

Open **PowerShell as Administrator** and execute:

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/VN-Fin/xno_vn/main/install-win.bat" -OutFile "install-win.bat"
Start-Process ".\install-win.bat" -Wait
```

## macOS

Open your terminal and run:

```bash
bash <(curl -s https://raw.githubusercontent.com/VN-Fin/xno_vn/main/install-mac.sh)
```

## From Source

If you'd like to install from source:

```bash
git clone https://github.com/VN-Fin/xno_vn.git
cd xno_vn
pip install -r requirements.txt
python install .
```

## Python Package (Not Recommended)

Ensure the TA-Lib library is installed on your system, then install the `xno` package using pip:

```bash
pip install xno
```
