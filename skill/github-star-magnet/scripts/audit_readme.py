#!/usr/bin/env python3
"""
audit_readme.py - score a README against patterns measured in the 491 most-starred repos.

Input: a local README path, or "owner/repo" (fetched from raw.githubusercontent.com).
Output: a 0-100 score and the highest-impact fixes first.

Important: this checks STRUCTURE (what top repos have on the first screen), not whether the
idea is good. A perfect score does not create stars; a missing item is a cheap fix.

Examples
  python audit_readme.py README.md
  python audit_readme.py yourname/yourrepo
"""
import re
import sys
import urllib.request

# Benchmarks come from references/data-findings.md (485 READMEs, 2025+ cohort in brackets).
CHECKS = []


def check(name, weight, bench, why):
    def deco(fn):
        CHECKS.append((name, weight, bench, why, fn))
        return fn
    return deco


def fetch(target):
    if "/" in target and not target.endswith(".md") and not target.startswith((".", "/")):
        for n in ("README.md", "readme.md", "Readme.md", "README.rst", "README"):
            url = f"https://raw.githubusercontent.com/{target}/HEAD/{n}"
            try:
                with urllib.request.urlopen(url, timeout=15) as r:
                    return r.read().decode("utf-8", "ignore")
            except Exception:
                continue
        sys.exit(f"Could not fetch a README for {target}. Save it locally and pass the file path.")
    with open(target, encoding="utf-8", errors="ignore") as f:
        return f.read()


def first_screen(t):
    return t[:2500]


def first_prose_line(t):
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    for line in t.splitlines():
        s = line.strip()
        if not s or s.startswith(("#", "[![", "![", "[!", "|", "---", "```", "<", ">")):
            continue
        if re.match(r"^[-*+]\s", s):          # real bullets only; **bold** taglines are fine
            continue
        if re.fullmatch(r"(\[[^\]]*\]\([^)]*\)\s*[·|•\-]*\s*)+", s):   # a line made only of links (nav bar)
            continue
        if re.fullmatch(r"[\W_]+", s):
            continue
        return s
    return ""


INSTALL = (r"npm (i|install)|pnpm (add|i)|yarn add|pip3? install|uv (pip|tool|add)|curl [^\n]*\|\s*(ba)?sh|"
           r"brew (install|tap)|npx |docker (run|compose)|cargo (install|add)|go install|/plugin |winget|irm |bunx |pipx")
ONE_LINER = (r"(npx |curl [^\n]*\|\s*(ba)?sh|brew install|pip install|npm i(nstall)? -g|uv tool install|"
             r"cargo install|go install|/plugin install|docker run)")
VISUAL_TOP = r"<img|!\[|<picture|<video"
MEDIA = r"\.gif|\.mp4|\.webm|youtu\.?be|<video|asciinema|user-attachments/assets"


@check("One-sentence promise right under the title (30-200 chars)", 8, "all top repos have one; 2025+ taglines median ~100 chars",
       "People decide in ~5 seconds. State who it is for and what result they get, in one sentence.")
def c_tagline(t):
    ln = first_prose_line(t)
    return 30 <= len(ln) <= 200, f"first sentence found: {ln[:90]!r} ({len(ln)} chars)"


@check("Visual on the first screen (logo, banner, screenshot)", 10, "90% of top repos [92%]",
       "A README with only text looks abandoned. Put a hero image or screenshot above the fold.")
def c_visual(t):
    return bool(re.search(VISUAL_TOP, first_screen(t))), ""


@check("Demo GIF/video that shows the RESULT in the first screen", 6, "19% overall [23%]; 40% of single-outcome apps",
       "A 10-20 second GIF of the final result is the strongest proof for apps and tools. Show output, not setup.")
def c_demo(t):
    return bool(re.search(MEDIA, first_screen(t).lower())), ""


@check("One-line install command (npx / curl / brew / pip / docker run / plugin)", 14, "42% overall [78%]; 84-90% for agent skills/tools; fast 82% vs slow 66%",
       "Every extra setup step loses people. If it takes more than one command to try, most visitors leave.")
def c_oneliner(t):
    return bool(re.search(ONE_LINER, t.lower())), ""


@check("Install command visible early (within the first ~2,500 characters)", 3, "19% overall [24%]; no clear fast-vs-slow gap",
       "The fastest repos let you copy a command before you scroll.")
def c_install_top(t):
    return bool(re.search(INSTALL, first_screen(t).lower())), ""


@check("Quick start / Usage heading", 12, "64% overall [88%]; fast repos 89% vs slow 71%",
       "Give the first successful run in under 60 seconds, with expected output shown.")
def c_quick(t):
    return bool(re.search(r"^#+\s*.*(quick ?start|getting started|get started|install|usage|how to use)", t.lower(), re.M)), ""


@check("'Why this exists' / 'What is it' section (the problem + the wedge)", 12, "29% overall [45%]; 68% of agent skill packs; fast 52% vs slow 21%",
       "Fast-growing repos explain the pain and why existing options fall short. Pure feature lists do not.")
def c_why(t):
    return bool(re.search(r"^#+\s*.*(why|motivation|philosophy|what is|what's|overview|about|problem)", t.lower(), re.M)), ""


@check("Comparison with alternatives (table or 'vs' section)", 12, "33% overall [54%]; fast repos 55% vs slow 23%",
       "Visitors compare you with something they already know. Do the comparison for them, honestly.")
def c_compare(t):
    return bool(re.search(r"\bvs\.? |versus|compared (to|with)|comparison|alternative to", t.lower())), ""


@check("Hard numbers on the first screen (%, x faster, N users, N tasks tested)", 4, "34% overall [52%]; 45% of agent tools; no fast-vs-slow gap",
       "Specific, checkable numbers beat adjectives. Say how you measured.")
def c_numbers(t):
    return bool(re.search(r"\d+(\.\d+)?\s?(x|×)\s|\d+\s?%|\d+k\+?\s|\d+\+\s|\d+\s?(times)", first_screen(t).lower())), ""


@check("Works with / supported platforms listed", 4, "87% of 2025+ agent tools name 3+ agents; 71% name 6+",
       "Supporting many platforms widens your funnel. Say which ones, explicitly.")
def c_works(t):
    return bool(re.search(r"works with|supported|compatible|supports|platforms?\b|linux|macos|windows", t.lower())), ""


@check("At least 3 badges (license, release/CI, community)", 3, "62% have 5+ badges [77%]",
       "Badges signal a maintained project. Keep them to one row.")
def c_badges(t):
    return len(re.findall(r"shields\.io|badge|codecov|workflows", t.lower())) >= 3, ""


@check("License stated", 4, "MIT in 62% of 2025+ READMEs; Apache 16%",
       "No license = many companies and developers cannot legally use it. MIT or Apache-2.0 are the safe default.")
def c_license(t):
    return bool(re.search(r"licen[sc]e", t.lower())), ""


@check("Contributing path", 3, "78% mention contributing",
       "Tell people how to help (good first issues, how to add an item/plugin/skill).")
def c_contrib(t):
    return "contribut" in t.lower(), ""


@check("Community link (Discord / X / Telegram / WeChat / Discussions)", 2, "63% overall [69%]",
       "Give people somewhere to ask questions. Questions become issues, issues become contributors.")
def c_comm(t):
    return bool(re.search(r"discord\.(gg|com)|slack|telegram|t\.me|wechat|twitter\.com|x\.com|discussions", t.lower())), ""


@check("README depth (400+ words; median top repo ~1,200)", 3, "median 1,197 words; fast repos ~2,460 vs slow ~1,100",
       "Very thin READMEs rarely win. Depth must be skimmable: headings, tables, short paragraphs.")
def c_len(t):
    return len(t.split()) >= 400, f"{len(t.split())} words"


def local_image_problems(t, base_dir):
    """Return referenced local images that do not exist on disk (only when a local README path is given)."""
    import os
    refs = re.findall(r'src="([^"]+)"', t) + re.findall(r"!\[[^\]]*\]\(([^)\s]+)", t)
    bad = []
    for r in refs:
        if r.startswith(("http://", "https://", "data:", "#")):
            continue
        if not os.path.exists(os.path.join(base_dir, r.split("?")[0])):
            bad.append(r)
    return sorted(set(bad))


def main():
    import os
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    t = fetch(sys.argv[1])
    is_local = os.path.exists(sys.argv[1])
    placeholders = len(re.findall(r"\[\[[^\]]*\]\]", t))
    missing_imgs = local_image_problems(t, os.path.dirname(os.path.abspath(sys.argv[1]))) if is_local else []
    total = sum(w for _, w, _, _, _ in CHECKS)
    got = 0
    results = []
    for name, w, bench, why, fn in CHECKS:
        ok, note = fn(t)
        got += w if ok else 0
        results.append((ok, w, name, bench, why, note))
    capped = False
    if placeholders or missing_imgs:
        # Template text should not earn points: cap the score until it is filled in.
        got = min(got, 40)
        capped = True
    print(f"README STRUCTURE SCORE: {got}/{total}" + ("  (capped: unfinished template)" if capped else "") + "\n")
    if placeholders:
        print(f"!! {placeholders} unfilled [[placeholder]] block(s) - replace them all before publishing.")
    if missing_imgs:
        print("!! Referenced images not found on disk (broken on GitHub): " + ", ".join(missing_imgs))
    if placeholders or missing_imgs:
        print()
    for ok, w, name, bench, why, note in results:
        mark = "PASS" if ok else "FAIL"
        extra = f"  [{note}]" if note else ""
        print(f"[{mark}] ({w:>2} pts) {name}{extra}")
    fails = sorted([r for r in results if not r[0]], key=lambda r: -r[1])
    if fails:
        print("\nFIX FIRST (highest impact):")
        for i, (_, w, name, bench, why, _) in enumerate(fails[:6], 1):
            print(f"{i}. {name}\n   why: {why}\n   top-repo benchmark: {bench}")
    print("\nReminder: structure helps conversion once people arrive. It does not replace a sharp idea or a launch plan.")


if __name__ == "__main__":
    main()
