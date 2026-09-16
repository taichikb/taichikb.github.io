@echo off
REM ==========================================================
REM  Tai Chi Knowledge Base - Local Intranet Launcher
REM  Serves the repo on a local HTTP server and opens the page
REM ==========================================================

setlocal enabledelayedexpansion

set REPO_DIR=%~dp0
set PORT=8767
set URL=http://localhost:%PORT%/en/techniques/unified-framework/

echo.
echo ============================================================
echo  Tai Chi Knowledge Base - Local Intranet
echo ============================================================
echo.
echo  Repo:    %REPO_DIR%
echo  Port:    %PORT%
echo  Page:    %URL%
echo.

REM Pick Python (try python3 then python)
where python >nul 2>nul
if %ERRORLEVEL%==0 (
    set PY=python
) else (
    where python3 >nul 2>nul
    if %ERRORLEVEL%==0 (
        set PY=python3
    ) else (
        echo [ERROR] Python is not installed or not in PATH.
        echo Install Python from https://www.python.org/downloads/
        pause
        exit /b 1
    )
)

echo [OK] Using Python: %PY%
echo.

REM Open browser after a short delay so the server has time to start
echo [INFO] Opening your default browser in 2 seconds...
start "" /b timeout /t 2 /nobreak >nul
start "" "%URL%"

REM Start the HTTP server (this will block until Ctrl+C)
cd /d "%REPO_DIR%"
echo [INFO] Starting HTTP server on port %PORT%...
echo        Press Ctrl+C to stop the server.
echo.
%PY% -m http.server %PORT%

endlocal
