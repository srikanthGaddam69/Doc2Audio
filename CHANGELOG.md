# Changelog

## 1.0.0
- Browser app (`Doc2Audio_Offline.html`): reads .docx/.pdf/.txt/.md/.html, pasted text, and images (OCR).
- Offline by design — document readers, both voices and MP3 export are embedded; only OCR needs the network.
- Voice engines: system voices (play) and a savable synthesizer voice; speed & pitch.
- **MP3 export** in the browser (WAV → MP3 via lamejs).
- **More OCR languages**, including Telugu, Hindi, Tamil, Kannada.
- Code-stripping with a verbatim toggle; select-to-read and a read-anywhere bookmarklet.
- Desktop drag-and-drop tools for **macOS** and **Windows** sharing one cross-platform engine,
  producing loudness-normalised MP3 in a natural neural voice (with a system-voice fallback).
