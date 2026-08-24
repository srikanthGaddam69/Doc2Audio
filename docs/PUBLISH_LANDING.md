# Publish the Doc2Audio landing page (GitHub Pages)

This `docs/` folder is a complete landing page **plus a working live demo** (`app.html`).
Put it in your GitHub repo and turn on Pages — about 5 minutes.

## 1. Add the folder to your repo
Copy this **`docs/`** folder into your `doc2audio` repository (top level), so you have:
```
doc2audio/
  docs/
    index.html        ← the landing page
    app.html          ← the live app (linked from the page)
    assets/           ← icon, demo.gif, screenshots, sample.mp3
```

## 2. Personalise the links (1 minute)
Open `docs/index.html` and **replace `OWNER`** with your GitHub username (it appears 3 times — the
stars badge and the two “View on GitHub” links). If your repo isn’t named `doc2audio`, update that too.
On GitHub you can do this in the browser: open the file → pencil icon → edit → **Commit**.

## 3. Turn on GitHub Pages
1. In your repo: **Settings → Pages**.
2. **Build and deployment → Source: Deploy from a branch.**
3. **Branch:** `main`  ·  **Folder:** `/docs`  →  **Save**.
4. Wait ~1 minute. Your landing page is live at:
   **`https://YOUR-USERNAME.github.io/doc2audio/`**
   (the live app is at `.../doc2audio/app.html`, already linked by the **Try it live** button.)

## 4. Submit
Submit the Pages URL above — **not** the raw GitHub repo. The page links back to the repo for anyone
who wants the source.

---

### Notes
- The **badges** (stars, license, etc.) load from shields.io when the page is online — they’ll appear once it’s on Pages.
- The **live app** (`app.html`) is the full offline browser tool; image OCR needs internet, everything else works offline.
- Assets are lightweight (~2 MB total) so the page loads fast.
