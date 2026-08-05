# Third-party components

The offline browser app (`browser/Doc2Audio_Offline.html`) bundles the following open-source
libraries. Their licenses apply to the bundled copies.

| Component | Purpose | License |
|-----------|---------|---------|
| meSpeak.js (eSpeak) | Savable synthesizer voice | **GPL-3.0** |
| lamejs (LAME port) | WAV → MP3 encoding | LGPL |
| pdf.js (Mozilla) | Reading PDF files | Apache-2.0 |
| mammoth.js | Reading Word (.docx) files | BSD-2-Clause |
| Tesseract.js | Image OCR (loaded on demand) | Apache-2.0 |

Because meSpeak/eSpeak is GPL-3.0, the combined offline HTML — and therefore this repository —
is distributed under **GPL-3.0** (see `LICENSE`), which is compatible with the Apache-2.0, BSD
and LGPL components above.

The desktop tools use the Piper neural TTS engine and a Piper voice model, downloaded by the setup
scripts at install time (not redistributed here). The Windows tool can also fall back to the built-in
Windows Speech (SAPI) voice, and macOS to the built-in `say` voice.
