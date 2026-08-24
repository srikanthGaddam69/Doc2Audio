# Doc2Audio — Windows drag-and-drop tool

Reads a document aloud with the reference codes stripped out, and saves an **MP3**.
Uses the natural **Amy** voice once set up; otherwise the built-in Windows voice.

## Setup (once)
1. Keep these files together in one folder: `doc2audio.py`, `Setup.bat`, `Convert to Audio.bat`.
2. **Double-click `Setup.bat`.** (If SmartScreen warns: *More info → Run anyway*.)
   It installs Python, ffmpeg and the Amy voice. Takes a few minutes.

## Use
- **Drag** a document onto **`Convert to Audio.bat`** — or double-click it and paste a file path.
- The audio is saved next to your document as `YourDocument (audio).mp3`.
- Works with `.docx`, `.pdf`, `.txt`, `.md`, `.html`. Drop several at once.

## Notes
- Needs **Windows 10 (21H2)+ or Windows 11** (for `winget` and `tar`).
- If Piper can't install, the tool automatically uses the built-in Windows voice.
