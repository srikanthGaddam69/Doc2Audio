@echo off
setlocal
cd /d "%~dp0"
set "PY=.venv\Scripts\python.exe"
if not exist "%PY%" set "PY=python"

echo ===============================================
echo    Doc2Audio  -  document to audio (codes removed)
echo ===============================================
echo.
if "%~1"=="" (
  set /p "FILES=Drag your document here and press Enter: "
  "%PY%" doc2audio.py %FILES%
) else (
  "%PY%" doc2audio.py %*
)
echo.
echo Your audio file is saved next to the original document.
pause
