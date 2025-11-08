@echo off
echo ============================================================
echo BEBE Task Recorder - Fresh Install Test from PyPI
echo ============================================================
echo.
echo This script will:
echo 1. Install bebe-task-recorder from PyPI
echo 2. Run tests to verify it works
echo 3. Optionally test the GUI
echo.
pause

echo.
echo [1/3] Installing from PyPI...
python -m pip install --upgrade bebe-task-recorder

if errorlevel 1 (
    echo ERROR: Installation failed!
    pause
    exit /b 1
)

echo.
echo [2/3] Running tests...
python test_from_pypi.py

if errorlevel 1 (
    echo.
    echo WARNING: Some tests failed!
    pause
    exit /b 1
)

echo.
echo [3/3] Test GUI? (y/n)
set /p test_gui="> "

if /i "%test_gui%"=="y" (
    echo.
    echo Starting GUI...
    python -c "from bebe_task_recorder import main; main()"
)

echo.
echo ============================================================
echo Test complete!
echo ============================================================
pause

