#!/bin/bash
# Doc2Audio - one-time setup.  Double-click to run.
cd "$(dirname "$0")" || exit 1
clear
echo "=================================================="
echo "   Doc2Audio  -  Setup"
echo "=================================================="
echo "This installs everything the tool needs. It can take"
echo "a few minutes the first time. You may be asked for your"
echo "Mac password, and a system dialog may pop up - that's normal."
echo

# 1) Apple Command Line Tools (provides python3, git, tar, curl)
if ! xcode-select -p >/dev/null 2>&1; then
  echo "-> Installing Apple Command Line Tools (accept the pop-up)..."
  xcode-select --install 2>/dev/null
  echo "   When that finishes, run this Setup again."
fi

# 2) Homebrew  (used to install ffmpeg / poppler / python)
if ! command -v brew >/dev/null 2>&1; then
  echo "-> Installing Homebrew..."
  NONINTERACTIVE=1 /bin/bash -c \
    "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" || true
fi
eval "$(/opt/homebrew/bin/brew shellenv 2>/dev/null)" || true
eval "$(/usr/local/bin/brew shellenv 2>/dev/null)"  || true

if command -v brew >/dev/null 2>&1; then
  echo "-> Installing ffmpeg, poppler, python (for audio, PDFs, scripting)..."
  brew install ffmpeg poppler python >/dev/null 2>&1 || brew install ffmpeg poppler python || true
fi

# 3) Private Python environment + the Amy voice engine (Piper)
PY="$(command -v python3 || echo python3)"
echo "-> Creating a private Python environment..."
"$PY" -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate
python -m pip install --upgrade pip >/dev/null 2>&1
echo "-> Installing the Amy voice engine + document readers..."
if pip install piper-tts python-docx pdfplumber >/dev/null 2>&1; then
  echo "   Amy voice engine installed."
else
  echo "   (Piper could not install - the tool will use the built-in Mac voice.)"
  pip install python-docx pdfplumber >/dev/null 2>&1 || true
fi

# 4) Download the Amy voice - the SAME voice used in the narrated explainers
mkdir -p voices
if [ ! -f voices/en_US-amy-medium.onnx ]; then
  echo "-> Downloading the Amy voice (about 60 MB)..."
  URL="https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-en_US-amy-medium.tar.bz2"
  if curl -L -o voices/_amy.tar.bz2 "$URL"; then
    tar -xjf voices/_amy.tar.bz2 -C voices --strip-components=1 \
        vits-piper-en_US-amy-medium/en_US-amy-medium.onnx \
        vits-piper-en_US-amy-medium/en_US-amy-medium.onnx.json 2>/dev/null
    rm -f voices/_amy.tar.bz2
  fi
fi
if [ -f voices/en_US-amy-medium.onnx ]; then
  echo "   Amy voice ready."
else
  echo "   (Amy voice not downloaded - the built-in Mac voice will be used instead.)"
fi

echo
echo "=================================================="
echo "   Setup complete."
echo
echo "   To use it: drag a document onto"
echo "   'Convert to Audio.command'  (or double-click it"
echo "   and drag your file into the window)."
echo "=================================================="
echo
echo "Press Return to close."; read -r _
