@echo off
setlocal
cd /d "%~dp0"
echo ==================================================
echo    Doc2Audio - Setup (Windows)
echo ==================================================
echo This installs what the tool needs. It can take a few
echo minutes. A User Account Control prompt may appear.
echo.

where python >nul 2>&1
if errorlevel 1 (
  echo -^> Installing Python...
  winget install -e --id Python.Python.3.12 --silent --accept-package-agreements --accept-source-agreements
)
where ffmpeg >nul 2>&1
if errorlevel 1 (
  echo -^> Installing ffmpeg (for MP3)...
  winget install -e --id Gyan.FFmpeg --silent --accept-package-agreements --accept-source-agreements
)

echo -^> Creating a private Python environment...
python -m venv .venv
call ".venv\Scripts\activate.bat"
python -m pip install --upgrade pip >nul 2>&1
echo -^> Installing the Amy voice engine + document readers...
pip install piper-tts python-docx pdfplumber
if errorlevel 1 (
  echo    (Piper could not install - the built-in Windows voice will be used.)
  pip install python-docx pdfplumber
)

if not exist voices mkdir voices
if not exist "voices\en_US-amy-medium.onnx" (
  echo -^> Downloading the Amy voice (about 60 MB)...
  powershell -NoProfile -Command "Invoke-WebRequest -Uri 'https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-en_US-amy-medium.tar.bz2' -OutFile 'voices\amy.tar.bz2'"
  tar -xjf "voices\amy.tar.bz2" -C voices --strip-components=1 vits-piper-en_US-amy-medium/en_US-amy-medium.onnx vits-piper-en_US-amy-medium/en_US-amy-medium.onnx.json
  del "voices\amy.tar.bz2"
)

echo.
echo ==================================================
echo    Setup complete.
echo    Now drag a document onto "Convert to Audio.bat".
echo ==================================================
pause
