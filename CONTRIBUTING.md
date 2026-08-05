# Contributing

Thanks for your interest in improving Doc2Audio!

## Ways to help
- **Report a bug** — open an Issue with your OS/browser and what happened.
- **Suggest a feature** — open an Issue describing the use case.
- **Send a pull request** — small, focused changes are easiest to review.

## Project layout
- `browser/Doc2Audio_Offline.html` — the self-contained browser app (HTML/CSS/JS + embedded libraries).
- `desktop/macos/` and `desktop/windows/` — the drag-and-drop tools; both share the same
  `doc2audio.py` engine (extract text → strip codes → synthesize → encode).

## Ground rules
- Keep the browser app a **single file** with no build step.
- Don't commit generated artefacts (see `.gitignore`): the Mac/Windows virtual environment and the
  downloaded voice model are recreated by the setup scripts.
- Respect the licenses of bundled components (`NOTICES.md`). New bundled code must be GPL-compatible.

## Testing changes
- Browser app: open the HTML, try a `.docx`, a `.pdf`, pasted text, and an image; check Play,
  Download MP3, the code-strip toggle, and the bookmarklet.
- Desktop: run the engine on a `.docx` and a `.pdf` and confirm an audio file is produced.
