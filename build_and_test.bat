@echo off
echo ============================================================
echo BEBE Task Recorder - Build and Test Package
echo ============================================================
echo.

REM Verifica Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python nu este instalat sau nu este in PATH!
    pause
    exit /b 1
)

echo [1/5] Cleaning old build files...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist *.egg-info rmdir /s /q *.egg-info
if exist bebe_task_recorder.egg-info rmdir /s /q bebe_task_recorder.egg-info

echo.
echo [2/5] Installing/upgrading build tools...
python -m pip install --upgrade pip setuptools wheel build twine

echo.
echo [3/5] Building package...
python -m build

if errorlevel 1 (
    echo ERROR: Build failed!
    pause
    exit /b 1
)

echo.
echo [4/5] Installing package locally for testing...
python -m pip install -e .

if errorlevel 1 (
    echo ERROR: Local installation failed!
    pause
    exit /b 1
)

echo.
echo [5/5] Running tests...
python test_install.py

echo.
echo ============================================================
echo Build complete! Package files are in dist/
echo.
echo To upload to PyPI:
echo   1. Test upload: python -m twine upload --repository testpypi dist/*
echo   2. Real upload: python -m twine upload dist/*
echo ============================================================
pause

