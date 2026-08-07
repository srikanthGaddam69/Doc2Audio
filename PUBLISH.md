# How to publish this on GitHub (public)

No Git knowledge needed. Pick a method.

## Option A — GitHub website (easiest)
1. Sign in at https://github.com and click **+ → New repository**.
2. Name it `doc2audio`, choose **Public**, leave "Add a README" unticked, **Create repository**.
3. Click **“uploading an existing file”**, drag in the *contents* of this folder (keep the subfolders), **Commit changes**.

## Option B — GitHub Desktop
1. Install https://desktop.github.com and sign in.
2. **File → New Repository**, name `doc2audio`, **Create**.
3. Copy the contents of this folder into the new repo folder, **Commit to main**, then **Publish repository** with "Keep this code private" **unticked**.

## Before you go public
- ✅ Only the Doc2Audio tool is here.
- ❌ Do **not** add work/project documents (plans, reports, decks, client material).
- `.gitignore` already excludes local install files (downloaded voice + virtual environment).

## One last touch — the CI badge
This repo includes a GitHub Actions check (`.github/workflows/ci.yml`). After you publish, edit
`README.md` and replace `OWNER` in the CI badge URL with your GitHub username so the green
**passing** badge shows. (On GitHub: open README → pencil icon → change `OWNER` → Commit.)
You can also run the check any time from the **Actions** tab → *CI* → **Run workflow**.
