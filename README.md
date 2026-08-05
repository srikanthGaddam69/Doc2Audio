# Doc2Audio — turn documents into audio (Mac)

Reads a document out loud with the **reference codes stripped out** — no document
numbers, requirement IDs, transmittals, or revision codes — so you can just listen.

By default it uses **Amy**, the same voice as the narrated explainers. If the Amy
voice isn't installed yet, it automatically falls back to the built-in Mac voice.

Works with: **.docx .doc .rtf .odt .html .txt .md .pdf**

---

## 1. Put the files in one folder

Keep these four items together in a single folder (e.g. `Downloads/Doc2Audio`):

- `doc2audio.py`
- `Setup.command`
- `Convert to Audio.command`
- `README.md`

## 2. Run Setup once

Because the files came from a download, macOS needs you to allow them the first time.
The easiest way is one copy‑paste:

1. Open **Terminal** (press `Cmd‑Space`, type *Terminal*, press Return).
2. Copy‑paste this line and press Return (adjust the folder if you didn't use Downloads):

   ```
   cd ~/Downloads/Doc2Audio && chmod +x *.command && ./Setup.command
   ```

Setup installs the audio tools and downloads the Amy voice. It can take a few minutes
and may ask for your Mac password — that's normal.

*(After this first time, you can just double‑click the `.command` files.)*

## 3. Convert a document

Either:

- **Drag** your document onto **`Convert to Audio.command`**, **or**
- **Double‑click** `Convert to Audio.command`, then drag your file into the window and press Return.

The audio appears **next to your document**, named `YourDocument (audio).mp3`.
You can drop several files at once.

---

## Make it a true drag‑onto‑icon app (optional, ~1 minute)

If you'd like an app icon you can drop files onto (and keep in the Dock):

1. Open **Automator** → **New** → **Application**.
2. Search for **“Run Shell Script”**, drag it into the workflow.
3. Set **Pass input:** to **as arguments**.
4. Replace the script box with (edit the path if needed):

   ```bash
   cd ~/Downloads/Doc2Audio
   ./"Convert to Audio.command" "$@"
   ```

5. **File → Save**, name it *Doc2Audio*. Now you can drag documents onto that app.

---

## Notes

- **Voice:** run `Setup.command` to get the Amy voice. Without it, the tool uses the
  built‑in macOS “Samantha” voice — still clear, just different.
- **Output format:** if `ffmpeg` is installed (Setup does this) you get a
  loudness‑normalised **.mp3**; otherwise a **.m4a**.
- **What gets removed:** document/transmittal codes (e.g. long dashed/underscored
  IDs), requirement IDs (e.g. `SYS_1234`), bracketed references (e.g. `[P58]`),
  revision/version strings, table‑of‑contents lines, page numbers, and address/contact
  lines. Meaningful short terms like *L2*, *M2*, *E2E* are kept.
- **This is a plain read‑aloud**, not a rewritten explainer. It speaks the document’s
  own words (minus codes). For the fully rewritten, plain‑English explainer style,
  that step needs an AI model — ask and it can be added as a second mode.

## If something doesn't work

- *“can’t be opened because it is from an unidentified developer”* → right‑click the
  `.command` file → **Open** → **Open**. You only need to do this once per file.
- *PDF says it needs setup* → run `Setup.command` (it installs the PDF reader).
- Still stuck? Re‑run the Terminal line from step 2 — it re‑allows the files and runs Setup.
