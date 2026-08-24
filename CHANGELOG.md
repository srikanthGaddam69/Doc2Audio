# Changelog

## 1.2.0
- Added a **GitHub Pages landing page** (`docs/`) with live demo, screenshots, demo GIF and a sample MP3.
- Polished README: stars/license/Python/PWA/platform badges, screenshots, and a sample-audio link.

## 1.1.2
- **Offline OCR now guides you to AI** for Telugu and other non-Latin scripts (where offline OCR is weak/unreliable), and AI errors are reported clearly (network/CORS, key). Gemini request uses canonical field names.

## 1.1.1
- **Fix:** non-Latin scripts (Telugu, Hindi, Tamil, Kannada, Arabic, CJK, etc.) were being dropped by the code-cleaner and couldn't be shown/read. Now counts letters from any script, lists all-language voices, and auto-selects a matching voice when available.

## 1.1.0
- **AI extract (online):** the Image tab can now use Google Gemini (free tier) to read screenshots accurately in almost any language; offline OCR remains as a no-internet fallback. Key stored on-device.

## 1.0.0
- Browser app (`Doc2Audio_Offline.html`): reads .docx/.pdf/.txt/.md/.html, pasted text, and images (OCR).
- Offline by design — document readers, both voices and MP3 export are embedded; only OCR needs the network.
- Voice engines: system voices (play) and a savable synthesizer voice; speed & pitch.
- **MP3 export** in the browser (WAV → MP3 via lamejs).
- **More OCR languages**, including Telugu, Hindi, Tamil, Kannada.
- Code-stripping with a verbatim toggle; select-to-read and a read-anywhere bookmarklet.
- Desktop drag-and-drop tools for **macOS** and **Windows** sharing one cross-platform engine,
  producing loudness-normalised MP3 in a natural neural voice (with a system-voice fallback).
