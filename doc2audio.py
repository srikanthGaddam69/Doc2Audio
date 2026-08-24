#!/usr/bin/env python3
"""
Doc2Audio - turn a document into a spoken audio file, with document codes stripped out.

Reads .docx .doc .rtf .odt .html .txt .md .pdf, cleans out reference codes / IDs /
transmittals / TOC clutter, and speaks the plain text.

Voice priority (works on macOS and Windows):
  1. Piper "en_US-amy-medium"  (the same voice as the narrated explainers) - if installed by Setup
  2. macOS built-in `say` voice (Samantha) - always available, needs no setup

Audio output:
  - ffmpeg present  -> loudness-normalised .mp3 (same settings as the explainers)
  - else afconvert   -> .m4a   (built into macOS)
  - else             -> .wav / .aiff

Usage:  python3 doc2audio.py file1.docx [file2.pdf ...]
"""

import sys, os, re, subprocess, shutil, platform

HERE  = os.path.dirname(os.path.abspath(__file__))
VOICE = os.path.join(HERE, "voices", "en_US-amy-medium.onnx")
SAY_VOICE = "Samantha"

# ----------------------------------------------------------------------------- extract
def extract_text(path):
    ext = path.lower().rsplit(".", 1)[-1] if "." in path else ""
    if ext in ("txt", "md", "markdown"):
        return open(path, encoding="utf-8", errors="ignore").read()

    if ext in ("docx", "doc", "rtf", "odt", "html", "htm"):
        if shutil.which("textutil"):                       # macOS built-in
            r = subprocess.run(["textutil", "-convert", "txt", "-stdout", path],
                               capture_output=True, text=True)
            if r.returncode == 0 and r.stdout.strip():
                return r.stdout
        if ext == "docx":                                  # cross-platform fallback
            try:
                import docx
                d = docx.Document(path)
                return "\n".join(p.text for p in d.paragraphs)
            except Exception:
                pass
        raise SystemExit(f"Could not read '{os.path.basename(path)}'. Run Setup.command first.")

    if ext == "pdf":
        if shutil.which("pdftotext"):
            r = subprocess.run(["pdftotext", "-layout", path, "-"],
                               capture_output=True, text=True)
            if r.returncode == 0 and r.stdout.strip():
                return r.stdout
        try:
            import pdfplumber
            with pdfplumber.open(path) as pdf:
                return "\n".join((pg.extract_text() or "") for pg in pdf.pages)
        except Exception:
            pass
        raise SystemExit("Reading PDFs needs Setup.command (installs pdftotext).")

    raise SystemExit(f"Unsupported file type: .{ext}")

# ----------------------------------------------------------------------------- clean
# keep these short letter+digit tokens (they are meaningful, not codes)
KEEP = {"l1","l2","l3","m1","m2","m3","sil0","sil1","sil2","sil3","sil4",
        "2d","3d","4g","5g","24x7","24x365"}

# token over [A-Za-z0-9._-/] containing at least one letter AND one digit
MIXED = re.compile(r"[A-Za-z0-9]+(?:[._\-/][A-Za-z0-9]+)*")
URL   = re.compile(r"https?://\S+|www\.\S+|\S+@\S+\.\S+")
BRACK = re.compile(r"\[[^\]\n]{0,30}\]")            # [P58], [12], [REF-3]
DOTLEAD = re.compile(r"\.{4,}\s*\d*")               # TOC dot leaders
LEAD_NUM = re.compile(r"^\s*\d+(?:\.\d+)*\.?\s+")   # "6.2.1  Title" -> "Title"
PAGE_ONLY = re.compile(r"^\s*\d+\s*$")
REVTOK = re.compile(r"\bRev\.?\s*\d+(?:\.\d+)?\b", re.I)
MULTISPACE = re.compile(r"[ \t]{2,}")
SPACE_PUNCT = re.compile(r"\s+([,.;:?!])")

def is_code(tok):
    low = tok.lower()
    if low in KEEP:
        return False
    has_letter = any(c.isalpha() for c in tok)
    has_digit  = any(c.isdigit() for c in tok)
    has_sep    = any(c in "._-/" for c in tok)
    if has_sep and has_digit:                 # QR_SITE_BL_3.8.2, MD-15-80, ...
        return True
    if has_letter and has_digit and len(tok) >= 4:   # S00X, SYS6136, 23B00...
        return True
    return False

def looks_like_toc(line):
    return bool(DOTLEAD.search(line)) or bool(
        re.match(r"^\s*\d+(?:\.\d+)*\.?\s+.+\s+\d+\s*$", line))

def clean_text(raw):
    raw = raw.replace("\r", "\n")
    raw = URL.sub(" ", raw)
    out_lines = []
    for line in raw.split("\n"):
        s = line.strip()
        if not s:
            out_lines.append("")                       # keep paragraph breaks
            continue
        low = s.lower()
        if (looks_like_toc(s) or PAGE_ONLY.match(s)
                or "abn" in low or low.startswith(("t:", "f:", "www.", "e:", "www"))
                or "www." in low or "@" in low):
            continue
        s = BRACK.sub(" ", s)
        s = REVTOK.sub(" ", s)
        s = LEAD_NUM.sub("", s)
        # strip code-like tokens, keep the rest
        s = MIXED.sub(lambda m: "" if is_code(m.group(0)) else m.group(0), s)
        s = s.replace("|", " ").replace("\t", " ")     # table pipes/tabs
        s = MULTISPACE.sub(" ", s).strip()
        s = SPACE_PUNCT.sub(r"\1", s)
        letters = sum(c.isalpha() for c in s)
        if letters < 3:                                # drop code-only / junk lines
            continue
        out_lines.append(s)
    text = "\n".join(out_lines)
    # polish artefacts left where codes were removed
    text = re.sub(r"\(\s*[,;:]?\s*\)", " ", text)          # empty ( )
    text = re.sub(r"\[\s*[,;:]?\s*\]", " ", text)          # empty [ ]
    text = re.sub(r"\s*,\s*(?:and|or)?\s*\.", ".", text)   # ", and." -> "."
    text = re.sub(r",(?:\s*,)+", ",", text)                 # ", ," -> ","
    text = re.sub(r"\s+([,.;:?!])", r"\1", text)           # space before punct
    text = re.sub(r"[ \t]{2,}", " ", text)                  # double spaces
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text

# ----------------------------------------------------------------------------- speak
def find_piper():
    p = os.path.join(HERE, ".venv", "bin", "piper")
    if os.path.exists(p):
        return p
    return shutil.which("piper")

def encode(src, out_base, normalize):
    if shutil.which("ffmpeg"):
        mp3 = out_base + ".mp3"
        cmd = ["ffmpeg", "-y", "-i", src]
        if normalize:
            cmd += ["-af", "loudnorm=I=-16:TP=-1.5:LRA=11"]
        cmd += ["-ar", "44100", "-b:a", "128k", mp3]
        subprocess.run(cmd, check=True, capture_output=True)
        os.remove(src)
        return mp3
    if shutil.which("afconvert"):
        m4a = out_base + ".m4a"
        subprocess.run(["afconvert", "-f", "m4af", "-d", "aac", src, m4a], check=True)
        os.remove(src)
        return m4a
    return src

def synth(text, out_base):
    piper = find_piper()
    if piper and os.path.exists(VOICE):
        print("   voice: Amy (Piper)")
        wav = out_base + ".wav"
        subprocess.run([piper, "-m", VOICE, "-f", wav],
                       input=text.encode("utf-8"), check=True)
        return encode(wav, out_base, normalize=True)
    if shutil.which("say"):
        print(f"   voice: macOS {SAY_VOICE} (run Setup.command for the Amy voice)")
        tf = out_base + ".clean.txt"
        open(tf, "w", encoding="utf-8").write(text)
        aiff = out_base + ".aiff"
        subprocess.run(["say", "-v", SAY_VOICE, "-o", aiff, "-f", tf], check=True)
        os.remove(tf)
        return encode(aiff, out_base, normalize=False)
    if shutil.which("powershell") or shutil.which("pwsh"):
        ps = shutil.which("powershell") or shutil.which("pwsh")
        print("   voice: Windows built-in (run Setup for the Amy voice)")
        tf = out_base + ".clean.txt"
        open(tf, "w", encoding="utf-8").write(text)
        wav = out_base + ".wav"
        script = ("Add-Type -AssemblyName System.Speech;"
                  "$s=New-Object System.Speech.Synthesis.SpeechSynthesizer;"
                  "$s.SetOutputToWaveFile('%s');"
                  "$s.Speak([System.IO.File]::ReadAllText('%s'));"
                  "$s.Dispose()") % (wav.replace("'", "''"), tf.replace("'", "''"))
        subprocess.run([ps, "-NoProfile", "-Command", script], check=True)
        os.remove(tf)
        return encode(wav, out_base, normalize=False)
    raise SystemExit("No speech engine found. Run Setup.command (installs the Amy voice).")

# ----------------------------------------------------------------------------- main
def process(path):
    if not os.path.isfile(path):
        print(f"!  Skipped (not found): {path}");  return
    print(f">> {os.path.basename(path)}")
    text = clean_text(extract_text(path))
    words = len(text.split())
    if words < 5:
        print("!  Nothing readable found after cleaning."); return
    print(f"   {words} words after stripping codes")
    base = os.path.splitext(path)[0] + " (audio)"
    out = synth(text, base)
    print(f"OK  {os.path.basename(out)}\n")

def main(argv):
    files = [a for a in argv if a.strip()]
    if not files:
        print("Drag a document onto this tool, or: python3 doc2audio.py file.docx")
        return
    for f in files:
        try:
            process(f)
        except SystemExit as e:
            print(f"!  {e}\n")
        except Exception as e:
            print(f"!  Error on {os.path.basename(f)}: {e}\n")

if __name__ == "__main__":
    main(sys.argv[1:])
