#!/usr/bin/env python3
"""
find_comparables.py - find the closest repos (among the 491 most-starred) to a project idea.

Why: before designing a repo, look at who already won in the same space and
what archetype they used. Uses only the Python standard library.

Examples
  python find_comparables.py "pdf converter markdown"
  python find_comparables.py "memory agent" --archetype AGENTTOOL --since 2025
  python find_comparables.py --archetypes            # benchmark table only
  python find_comparables.py --list-archetype SKILLPACK --top 15
"""
import argparse
import csv
import os
import re
import statistics as st
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "references", "top491_enriched.csv")

ARCH_HELP = {
    "SKILLPACK": "Agent skills / prompt packs / methodology for AI coding agents",
    "AGENTTOOL": "Add-on tools for AI agents (memory, token savers, MCP, gateways, visualizers)",
    "AGENTPRODUCT": "Agent products & frameworks (coding agents, agent builders)",
    "OUTCOMEAPP": "Single-outcome apps, mostly AI (video, voice, trading, jobs, research)",
    "AIMODEL": "Models, inference, training, ML libraries",
    "LEARN": "Courses, interview prep, roadmaps, from-scratch tutorials",
    "LIST": "Curated lists / link collections / prompt libraries",
    "ALTERNATIVE": "Open-source / self-hosted alternative to a known product",
    "DEVTOOL": "CLI, terminal, editor, system utilities",
    "FRAMEWORK": "Frameworks, libraries, languages, runtimes, infra",
    "SECNET": "Security, reverse engineering, proxy / network tools",
    "CULTURE": "Cultural / viral / unusual non-code repos",
}


def load():
    if not os.path.exists(DATA):
        sys.exit(f"Data file not found: {DATA}")
    with open(DATA, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        for k in ("Rank", "Stars", "Forks", "CreatedYear", "AgeDays"):
            r[k] = int(float(r[k]))
        for k in ("StarsPerDay", "ForkRatio"):
            r[k] = float(r[k])
    return rows


def tokens(q):
    return [t for t in re.split(r"[\s,;/]+", q.lower()) if len(t) >= 2]


def score(row, toks):
    name = row["Repository"].lower()
    desc = row["Description"].lower()
    s = 0
    for t in toks:
        if t in name:
            s += 3
        if t in desc:
            s += 1
    return s


def fmt_row(r):
    desc = r["Description"]
    desc = (desc[:78] + "...") if len(desc) > 80 else desc
    return (f"#{r['Rank']:<4} {r['Repository'][:38]:<38} {r['Stars']//1000:>4}k  "
            f"{r['Archetype']:<12} {r['CreatedYear']}  {r['StarsPerDay']:>6.0f}/day  {desc}")


def archetype_table(rows):
    print("\nARCHETYPE BENCHMARKS (all 491 repos; stars/day = lifetime average)")
    print(f"{'archetype':<13}{'n':>4}{'med stars':>10}{'n 2025+':>9}{'spd 2025+':>10}{'spd 2023-24':>12}  what it is")
    by = {}
    for r in rows:
        by.setdefault(r["Archetype"], []).append(r)
    order = sorted(by, key=lambda a: -len(by[a]))
    for a in order:
        g = by[a]
        new = [x["StarsPerDay"] for x in g if x["CreatedYear"] >= 2025]
        mid = [x["StarsPerDay"] for x in g if 2023 <= x["CreatedYear"] <= 2024]
        med = lambda v: f"{st.median(v):.0f}" if v else "-"
        print(f"{a:<13}{len(g):>4}{st.median([x['Stars'] for x in g])/1000:>9.0f}k{len(new):>9}{med(new):>10}{med(mid):>12}  {ARCH_HELP.get(a,'')}")
    print("\nRead with care: only winners are in this data, and young repos look faster because"
          " viral growth is front-loaded. Compare archetypes within the same era.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="?", default="", help="keywords describing the idea")
    ap.add_argument("--archetype", help="restrict to one archetype code, e.g. SKILLPACK")
    ap.add_argument("--list-archetype", help="list top repos of an archetype (no keyword needed)")
    ap.add_argument("--since", type=int, help="only repos created in or after this year")
    ap.add_argument("--top", type=int, default=12)
    ap.add_argument("--archetypes", action="store_true", help="print only the archetype benchmark table")
    a = ap.parse_args()

    rows = load()
    if a.archetypes:
        archetype_table(rows)
        return

    pool = rows
    arch = a.archetype or a.list_archetype
    if arch:
        pool = [r for r in pool if r["Archetype"].upper() == arch.upper()]
        if not pool:
            sys.exit(f"Unknown archetype '{arch}'. Options: {', '.join(ARCH_HELP)}")
    if a.since:
        pool = [r for r in pool if r["CreatedYear"] >= a.since]

    if a.list_archetype and not a.query:
        pool = sorted(pool, key=lambda r: -r["StarsPerDay"])[: a.top]
        print(f"Fastest-growing '{a.list_archetype.upper()}' repos (lifetime stars/day):\n")
        for r in pool:
            print(fmt_row(r))
        return

    toks = tokens(a.query)
    if not toks:
        archetype_table(rows)
        return
    scored = [(score(r, toks), r) for r in pool]
    hits = [(s, r) for s, r in scored if s > 0]
    hits.sort(key=lambda x: (-x[0], -x[1]["Stars"]))
    print(f"Query: {toks}  | pool: {len(pool)} repos\n")
    if not hits:
        print("No close match in the top 491. That does NOT prove the space is empty:")
        print("  - search GitHub directly (stars:>500 + your keywords) to find mid-size competitors")
        print("  - try broader synonyms, or pick an archetype with --archetype and study its leaders")
    else:
        for s, r in hits[: a.top]:
            print(fmt_row(r))
        arch_count = {}
        for s, r in hits[:20]:
            arch_count[r["Archetype"]] = arch_count.get(r["Archetype"], 0) + 1
        top_arch = sorted(arch_count.items(), key=lambda kv: -kv[1])
        print("\nArchetypes among closest matches:", ", ".join(f"{k} x{v}" for k, v in top_arch))
    archetype_table(rows)


if __name__ == "__main__":
    main()
