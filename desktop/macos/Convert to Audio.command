#!/bin/bash
# Doc2Audio - drag a document onto this file, OR double-click and drag the file in.
cd "$(dirname "$0")" || exit 1
PY=".venv/bin/python3"; [ -x "$PY" ] || PY="$(command -v python3 || echo python3)"

clear
echo "==============================================="
echo "   Doc2Audio"
echo "   Turn a document into spoken audio - codes removed"
echo "==============================================="
echo

if [ "$#" -gt 0 ]; then
  "$PY" doc2audio.py "$@"
else
  echo "Drag your document(s) into this window, then press Return."
  echo "Supported: .docx  .pdf  .txt  .rtf  .md"
  echo
  printf "> "
  read -r line
  # Terminal pastes dragged files as space-separated, backslash-escaped paths
  eval "set -- $line"
  if [ "$#" -eq 0 ]; then
    echo "No file was given."
  else
    "$PY" doc2audio.py "$@"
  fi
fi

echo
echo "-> Your audio file is saved next to the original document"
echo "   (named '<document> (audio).mp3')."
echo
echo "Press Return to close."; read -r _
