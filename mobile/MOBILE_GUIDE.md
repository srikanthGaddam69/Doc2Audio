# Doc2Audio — Mobile App: Step‑by‑Step

Doc2Audio installs to your phone's home screen like a normal app (it's a **PWA**).
It keeps **all** the features — read files, paste, screenshot OCR, voices, MP3 — and works offline.

There are two parts: **(A) put the app online once**, then **(B) install it on your phone**.

---

## A. Put the app online (one time, ~2 minutes)

You need a web address (https) for the app. Pick one:

### Easiest — Netlify Drop (no account)
1. On a computer, unzip the app folder (it has `index.html`, `manifest.webmanifest`, `service-worker.js`, `icons/`).
2. Go to **https://app.netlify.com/drop**.
3. **Drag the whole folder** onto the page.
4. You get a link like `https://random-name.netlify.app` — that's your app. (Optionally make a free account to keep it.)

### Or — GitHub Pages (if you use GitHub)
1. Put these app files in a repository (e.g. in a `docs/` folder).
2. Repo **Settings → Pages → Build and deployment → Deploy from a branch**, choose your branch and the `/docs` folder, **Save**.
3. After a minute your app is at `https://YOUR-USERNAME.github.io/REPO/`.

---

## B. Install it on your phone

### iPhone / iPad (Safari)
1. Open the app link in **Safari**.
2. Tap the **Share** button (square with an up‑arrow).
3. Tap **Add to Home Screen** → **Add**.
4. Open **Doc2Audio** from your home screen — it runs full‑screen.

### Android (Chrome)
1. Open the app link in **Chrome**.
2. Tap the **⋮** menu → **Install app** (or **Add to Home screen**).
3. Tap **Install**. Open **Doc2Audio** from your app drawer/home screen.

---

## C. Use it

- **File** tab — pick a document (.docx, .pdf, .txt, .md, .html).
- **Paste text** tab — paste anything and tap *Use this text*.
- **Image / Screenshot** tab — pick a photo/screenshot; choose the OCR language (English, Telugu, Hindi, Tamil, Kannada, and more).
- Pick a **voice**, set **Speed/Pitch**, tap **Play**. Tap a sentence to start there.
- **Download MP3** with the *Downloadable* voice.

### Read text from other apps
On Android (and newer iOS), select text in any app → **Share** → **Doc2Audio** → it opens and reads it.
For anything else, take a **screenshot** and open it in the **Image** tab.

---

## Good to know (mobile)

- **First launch needs internet** (to download the app once). After that it works **offline** — only image OCR fetches a language pack the first time each language is used.
- On **iPhone**, tap **Play** to start speech (iOS requires a tap). Saving an MP3 opens the iOS share/save sheet.
- The **system voice** sounds best but only plays; the **Downloadable** voice is the one that saves to a file.
- Nothing is uploaded — it all runs on your phone.

### Want a true App Store / Play Store listing?
That's possible by wrapping this app with a tool called **Capacitor**, but it needs a Mac (Xcode) or
Android Studio and paid developer accounts (Apple $99/yr). The PWA above gives you a real installable
app for free — ask if you'd like the store route and I'll provide those steps too.

---

## D. Read images in ANY language (AI) — recommended

The **Image / Screenshot** tab has two methods:
- **✨ AI (any language)** — uses Google Gemini to read the image accurately in almost any language (needs internet + a free key).
- **Offline OCR** — works without internet, lower accuracy.

### Get a free Gemini key (2 minutes, no credit card)
1. Go to **https://aistudio.google.com/apikey** and sign in with a Google account.
2. Tap **Create API key** → copy it.
3. In Doc2Audio → **Image** tab → paste it into the **Gemini API key** box (it's saved only on your device).

Now drop a screenshot with **AI (any language)** selected — it reads the text in its original language.

> Privacy: with AI extract, the image is sent to Google to be read. Don't use it on confidential images. Offline OCR keeps everything on your device.
