#!/usr/bin/env python3
"""
refresh_dataset.py - rebuild the enriched dataset from a NEW "top repos by stars" CSV.

Why: the market moves fast (AI-agent repos took over the top list within ~18 months). Re-run this
every few months with a fresh CSV so the skill's advice does not go stale.

Input CSV must have at least: Repository (owner/name), Stars, Forks, Language, Description,
Created, "Last Push". Extra columns are ignored.

What it does
  1. Downloads each README from raw.githubusercontent.com (no API token needed)
  2. Computes the structure features used by the skill
  3. Writes <out>.csv with an EMPTY `Archetype` column

Then (this part needs judgment, so Claude does it): read every Repository + Description and fill the
`Archetype` column using the 12 codes in references/archetypes.md. Hand labelling was far more
accurate than keyword rules. After labelling, replace references/top491_enriched.csv and re-derive the
numbers in references/data-findings.md.

Usage
  python refresh_dataset.py new_top_repos.csv --out enriched_new.csv [--limit 50]
"""
import argparse
import csv
import datetime as dt
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor

NAMES = ["README.md", "readme.md", "Readme.md", "README.rst", "README"]
INSTALL = (r"npm (i|install)|pnpm (add|i)|yarn add|pip3? install|uv (pip|tool|add)|curl [^\n]*\|\s*(ba)?sh|"
           r"brew (install|tap)|npx |docker (run|compose)|cargo (install|add)|go install|/plugin |winget|bunx |pipx")
ONE = (r"(npx |curl [^\n]*\|\s*(ba)?sh|brew install|pip install|npm i(nstall)? -g|uv tool install|"
       r"cargo install|go install|/plugin install|docker run)")
MEDIA = r"\.gif|\.mp4|\.webm|youtu\.?be|<video|asciinema|user-attachments/assets"


def fetch(repo):
    for n in NAMES:
        try:
            with urllib.request.urlopen(f"https://raw.githubusercontent.com/{repo}/HEAD/{n}", timeout=15) as r:
                return r.read().decode("utf-8", "ignore")
        except Exception:
            continue
    return ""


def feats(t):
    if not t:
        return {k: "" for k in ("readme_words", "img_top", "gif_top", "install_top", "one_liner_install",
                                "quickstart_h", "comparison", "why_section", "translations", "numbers_claim")}
    top, low, tl = t[:2500], t.lower(), t[:2500].lower()
    b = lambda x: int(bool(x))
    return {
        "readme_words": len(t.split()),
        "img_top": b(re.search(r"<img|!\[|<picture|<video", top)),
        "gif_top": b(re.search(MEDIA, tl)),
        "install_top": b(re.search(INSTALL, tl)),
        "one_liner_install": b(re.search(ONE, low)),
        "quickstart_h": b(re.search(r"^#+\s*.*(quick ?start|getting started|get started|install|usage|how to use)", low, re.M)),
        "comparison": b(re.search(r"\bvs\.? |versus|compared (to|with)|comparison|alternative to", low)),
        "why_section": b(re.search(r"^#+\s*.*(why|motivation|philosophy|what is|what's|overview|about)", low, re.M)),
        "translations": b(re.search(r"readme[._-]?(zh|cn|ja|jp|ko|es|fr|de|pt|ru)|简体中文|日本語|한국어|español|français", low)),
        "numbers_claim": b(re.search(r"\d+(\.\d+)?\s?(x|×)\s|\d+\s?%|\d+k\+?\s|\d+\+\s", tl)),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv_in")
    ap.add_argument("--out", default="enriched_new.csv")
    ap.add_argument("--limit", type=int, default=0, help="only process the first N rows (for a quick test)")
    a = ap.parse_args()

    with open(a.csv_in, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if a.limit:
        rows = rows[: a.limit]
    need = {"Repository", "Stars", "Forks", "Language", "Description", "Created"}
    missing = need - set(rows[0].keys())
    if missing:
        sys.exit(f"CSV is missing columns: {sorted(missing)}")

    today = dt.date.today()
    with ThreadPoolExecutor(max_workers=12) as ex:
        readmes = list(ex.map(fetch, [r["Repository"] for r in rows]))

    out = []
    for i, (r, t) in enumerate(zip(rows, readmes), 1):
        try:
            created = dt.date.fromisoformat(r["Created"][:10])
            age = max((today - created).days, 1)
        except Exception:
            created, age = None, 1
        stars = int(float(r["Stars"]))
        forks = int(float(r["Forks"]))
        d = {
            "Rank": r.get("Rank", i), "Repository": r["Repository"], "Stars": stars, "Forks": forks,
            "Language": r["Language"], "Created": r["Created"][:10], "LastPush": r.get("Last Push", "")[:10],
            "Archetype": "",  # <- fill by reading each Description
            "CreatedYear": created.year if created else "", "AgeDays": age,
            "StarsPerDay": round(stars / age, 1), "ForkRatio": round(forks / max(stars, 1), 3),
            "Description": re.sub(r"\s+", " ", r.get("Description", "") or "").strip()[:220],
        }
        d.update(feats(t))
        out.append(d)

    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)
    got = sum(1 for t in readmes if t)
    print(f"Wrote {a.out}: {len(out)} repos, {got} READMEs fetched. Next: fill the Archetype column.")


if __name__ == "__main__":
    main()
