@echo off
REM Run example scripts as Administrator

if "%1"=="" (
    echo ============================================================
    echo BEBE Task Recorder - Run Examples as Administrator
    echo ============================================================
    echo.
    echo Usage: RUN_AS_ADMIN.bat [example_number]
    echo.
    echo Examples:
    echo   1 - Simple Record and Playback
    echo   2 - Save and Load Tasks
    echo   3 - Automation Workflow
    echo   4 - Programmatic Control
    echo   5 - GUI Application
    echo.
    echo Example:
    echo   RUN_AS_ADMIN.bat 1
    echo.
    pause
    exit /b
)

set EXAMPLE_NUM=%1
set SCRIPT_NAME=

if "%EXAMPLE_NUM%"=="1" (
    set SCRIPT_NAME=example_1_simple_record_playback.py
) else if "%EXAMPLE_NUM%"=="2" (
    set SCRIPT_NAME=example_2_save_load_task.py
) else if "%EXAMPLE_NUM%"=="3" (
    set SCRIPT_NAME=example_3_automation_workflow.py
) else if "%EXAMPLE_NUM%"=="4" (
    set SCRIPT_NAME=example_4_programmatic_control.py
) else if "%EXAMPLE_NUM%"=="5" (
    set SCRIPT_NAME=example_5_gui_app.py
) else (
    echo Invalid example number: %EXAMPLE_NUM%
    echo Use 1-5
    pause
    exit /b 1
)

echo ============================================================
echo Pornind %SCRIPT_NAME% cu privilegii Administrator...
echo ============================================================
echo.

REM Folosește -Wait pentru a aștepta finalizarea procesului
powershell -Command "Start-Process python -ArgumentList '%SCRIPT_NAME%' -Verb RunAs -Wait"

echo.
echo ============================================================
echo Script finalizat.
echo ============================================================
pause

