@echo off

echo [*] Detecting OS and checking system dependencies...

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python is not installed. Please install Python 3 from https://www.python.org/downloads/
    exit /b 1
)

:: Check if Pip is installed
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Pip is not installed. Please install Pip.
    exit /b 1
)

:: Upgrade Pip
echo [*] Upgrading Pip...
python -m pip install --upgrade pip setuptools wheel

:: Check if Git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Git is not installed. Please install Git from https://git-scm.com/download/win
    exit /b 1
)

:: Check for build tools (required for TA-Lib compilation)
echo [*] Ensure you have Visual Studio Build Tools installed for compiling TA-Lib.
echo     Download from https://visualstudio.microsoft.com/visual-cpp-build-tools/

:: Build and Install TA-Lib C Library
echo [*] Building and installing TA-Lib C library...
cd %TEMP%
powershell -Command "Invoke-WebRequest -Uri https://github.com/ta-lib/ta-lib/releases/download/v0.6.4/ta-lib-0.6.4-src.tar.gz -OutFile ta-lib-0.6.4-src.tar.gz"
tar -xzf ta-lib-0.6.4-src.tar.gz
cd ta-lib-0.6.4
:: Assuming MSBuild is installed with Visual Studio Build Tools
msbuild ta-lib.sln /p:Configuration=Release
mkdir C:\ta-lib
copy Release\* C:\ta-lib
cd ..
del /q ta-lib-0.6.4-src.tar.gz
rmdir /s /q ta-lib-0.6.4

:: Set environment variables for TA-Lib
setx TA_INCLUDE_PATH C:\ta-lib\include
setx TA_LIBRARY_PATH C:\ta-lib\lib

:: Install Python TA-Lib wrapper
echo [*] Installing Python TA-Lib wrapper...
pip install TA-Lib

:: Clone the repo if not already present
if not exist xno_vn (
    echo [*] Cloning repository...
    git clone https://github.com/VN-Fin/xno_vn.git
)

cd xno_vn

:: Pull latest changes
echo [*] Pulling latest changes...
git pull origin main

:: Install Python requirements
echo [*] Installing Python requirements...
pip install -r requirements.txt

:: Install project in editable mode
echo [*] Installing project in editable mode...
pip install .

echo [✔] Setup completed successfully.

cd ..
echo [*] Cleaning up cloned repo...
rmdir /s /q xno_vn

echo [*] Cleaning up install script...
del install.bat

echo [✔] All done. You can now use the 'xno' package.