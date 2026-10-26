#!/usr/bin/env python3
"""
scaffold_repo.py - create a launch-ready repo skeleton with an archetype-specific README.

The README follows the structure measured in the most-starred repos (see
references/readme-blueprint.md). Anything in [[DOUBLE BRACKETS]] is a TODO that must be
replaced before publishing - run `grep -rn "\\[\\[" .` to find what is left.

Archetypes: SKILLPACK, AGENTTOOL, OUTCOMEAPP, ALTERNATIVE, DEVTOOL, LEARN, LIST, LIBRARY

Example
  python scaffold_repo.py --name tokentrim --tagline "Cut your agent's token bill by 60% with one command" \
      --archetype AGENTTOOL --author "Your Name" --user yourgithub --out ./tokentrim
"""
import argparse
import datetime
import os
import sys

MIT = """MIT License

Copyright (c) {year} {author}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

HERO = """<div align="center">

<img src="docs/assets/hero.png" alt="__NAME__" width="720">

# __NAME__

**__TAGLINE__**

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/__USER__/__NAME__?style=flat-square)](https://github.com/__USER__/__NAME__/stargazers)
[![Release](https://img.shields.io/github/v/release/__USER__/__NAME__?style=flat-square)](https://github.com/__USER__/__NAME__/releases)

<!-- [[ADD: 10-20 second GIF of the FINAL RESULT -> docs/assets/demo.gif ]] -->
<img src="docs/assets/demo.gif" alt="__NAME__ demo" width="720">

[Install](#install-30-seconds) · [Quick start](#quick-start) · [Why](#why-__NAME__) · [Contributing](#contributing)

</div>

---
"""

WHY = """## Why __NAME__?

[[ONE paragraph: the painful situation your reader is in today. Be concrete: what they do now, what it costs (time, money, tokens, errors).]]

[[ONE paragraph: what changes with __NAME__, in the reader's words. Before -> After.]]

| | __NAME__ | [[Alternative A]] | [[Alternative B]] |
|---|---|---|---|
| [[Key difference 1]] | | | |
| [[Key difference 2]] | | | |
| [[Setup time]] | | | |

> Be honest in this table. A fair comparison is more convincing than a rigged one.
"""

TAIL = """## Contributing

[[Say exactly how to help: "add an entry", "write a skill", "pick a `good first issue`". Link CONTRIBUTING.md.]]
See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT - see [LICENSE](LICENSE).
"""

UTILITY = HERO + WHY + """
## Install (30 seconds)

```bash
[[ONE command. Verify it on a clean machine before publishing.]]
```

## Quick start

```bash
[[The first successful run. Show the expected output right below.]]
```

[[Expected output / screenshot]]

## Proof

[[Numbers with method: "X% fewer / Nx faster / N tasks tested". Say how it was measured and link the script so anyone can reproduce it. Delete this section if you cannot back it up.]]

## How it works

[[3-5 short steps or one small diagram. Keep it skimmable.]]

## Works with

[[List every platform / agent / OS you actually tested. A wider list widens your funnel.]]

## Roadmap

- [x] [[Shipped thing]]
- [ ] [[Next thing - invite votes via issues]]

""" + TAIL

SKILLPACK = HERO + WHY + """
## Install (30 seconds)

[[Provide a copy-paste command or steps for EACH agent you support. Top repos in this category list 6-16 agents. Use <details> blocks to keep it tidy. Verify each one.]]

<details>
<summary><strong>[[Agent 1]]</strong></summary>

```bash
[[command]]
```
</details>

<details>
<summary><strong>[[Agent 2]]</strong></summary>

```bash
[[command]]
```
</details>

## How it works

[[Describe the workflow the pack gives the agent, as a short numbered story: what the agent does first, next, last. People install what they can picture.]]

## What's inside

| Skill | What it does | Use it when |
|---|---|---|
| [[skill-one]] | [[...]] | [[...]] |
| [[skill-two]] | [[...]] | [[...]] |

## Philosophy

[[3-5 opinionated beliefs. A clear point of view is the brand of this archetype.]]

## Proof

[[Show before/after output or a measured result on real tasks. Link raw transcripts if you can.]]

## Updating

[[How to update safely.]]

""" + TAIL

ALTERNATIVE = HERO + WHY + """
## Self-host in 5 minutes

```bash
[[docker run ... / docker compose up -d]]
```

Open `http://localhost:[[port]]`.

## Screenshots

[[3-4 real screenshots in docs/assets/ - dark and light if possible]]

## Feature parity with [[Paid Product]]

| Feature | [[Paid Product]] | __NAME__ |
|---|---|---|
| [[...]] | | |

## Your data stays yours

[[Where data lives, how to back up, what telemetry exists (ideally none).]]

## Roadmap

- [ ] [[...]]

""" + TAIL

LEARN = HERO + """## Who this is for

[[Exact reader: their level, goal, and what they will be able to do after.]]

## Curriculum

| # | Lesson | You will build / learn | Time |
|---|---|---|---|
| 1 | [[...]] | [[...]] | [[...]] |

## How to use this repo

```bash
[[clone / open in Codespaces / run the first lesson]]
```

## Prerequisites

[[...]]

## Community

[[Where to ask questions; how to share what you built.]]

""" + TAIL

LIST = """# __NAME__

> __TAGLINE__

[[One-sentence scope: what is in, what is out.]]

## Contents

- [[Category 1]](#category-1)
- [[Category 2]](#category-2)

## [[Category 1]]

- [[Item name]](URL) - [[one line: what it is and why it is worth the click]]

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) first. Every entry needs: [[criteria, e.g. active in the last 12 months, has docs, free tier]].

## License

[[CC0-1.0 or MIT]]
"""

TEMPLATES = {
    "SKILLPACK": SKILLPACK, "AGENTTOOL": UTILITY, "OUTCOMEAPP": UTILITY, "DEVTOOL": UTILITY,
    "LIBRARY": UTILITY, "ALTERNATIVE": ALTERNATIVE, "LEARN": LEARN, "LIST": LIST,
}

CONTRIB = """# Contributing to __NAME__

Thanks for helping! Small contributions are welcome.

## Quick ways to help
- Report a bug or confusing doc (open an issue with the template)
- Pick an issue labelled `good first issue`
- [[For lists: add an entry. For skill packs: add a skill. For tools: add a platform/plugin.]]

## Ground rules
- One focused change per pull request
- Explain the *why* in the PR description
- Be kind. Assume good intent.

## Local setup
```bash
[[git clone ... && install deps && run tests]]
```
"""

BUG = """---
name: Bug report
about: Something is broken
labels: bug
---

**What happened?**

**What did you expect?**

**Steps to reproduce**
1.

**Environment** (OS, version, agent/runtime):
"""

FEATURE = """---
name: Feature request
about: Suggest an idea
labels: enhancement
---

**What problem would this solve for you?**

**What would you like to see?**

**Alternatives you considered**
"""

PR = """## What and why

## How to test

## Checklist
- [ ] Docs updated if behavior changed
"""

ASSETS_NOTE = """# Visual assets checklist

Put these here before launch (most-starred repos have a visual on the first screen):

- `hero.png`  - 1280x640 banner or logo. Also upload it as the repo's *Social preview* (Settings -> General).
- `demo.gif`  - 10-20 seconds showing the FINAL RESULT. Keep under ~8 MB. Record at 1.5x speed.
- `screenshot-*.png` - real screenshots (light and dark if the app has both).
"""

GITIGNORE = """.DS_Store
node_modules/
__pycache__/
*.pyc
.env
.venv/
dist/
build/
.idea/
.vscode/
"""

SKILL_EXAMPLE = """---
name: [[skill-name]]
description: [[What it does AND when to trigger it. Be specific and a little pushy.]]
---

# [[Skill title]]

[[Instructions the agent follows, in the imperative. Explain WHY, not just WHAT.]]
"""


def write(path, text):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--name", required=True, help="repo name, e.g. tokentrim")
    ap.add_argument("--tagline", required=True, help="one-sentence promise")
    ap.add_argument("--archetype", default="AGENTTOOL", choices=sorted(TEMPLATES))
    ap.add_argument("--author", default="[[Your Name]]")
    ap.add_argument("--user", default="[[github-username]]")
    ap.add_argument("--out", default=None, help="output folder (default: ./<name>)")
    a = ap.parse_args()

    out = a.out or os.path.join(".", a.name)
    if os.path.exists(out) and os.listdir(out):
        sys.exit(f"{out} exists and is not empty. Choose another --out.")

    def fill(s):
        return (s.replace("__NAME__", a.name).replace("__TAGLINE__", a.tagline)
                 .replace("__USER__", a.user).replace("__AUTHOR__", a.author))

    write(os.path.join(out, "README.md"), fill(TEMPLATES[a.archetype]))
    write(os.path.join(out, "LICENSE"), MIT.format(year=datetime.date.today().year, author=a.author))
    write(os.path.join(out, "CONTRIBUTING.md"), fill(CONTRIB))
    write(os.path.join(out, ".github", "ISSUE_TEMPLATE", "bug_report.md"), BUG)
    write(os.path.join(out, ".github", "ISSUE_TEMPLATE", "feature_request.md"), FEATURE)
    write(os.path.join(out, ".github", "PULL_REQUEST_TEMPLATE.md"), PR)
    write(os.path.join(out, "docs", "assets", "README.md"), ASSETS_NOTE)
    write(os.path.join(out, ".gitignore"), GITIGNORE)
    if a.archetype == "SKILLPACK":
        write(os.path.join(out, "skills", "example-skill", "SKILL.md"), SKILL_EXAMPLE)
    if a.archetype == "LEARN":
        write(os.path.join(out, "lessons", "01-start-here", "README.md"), "# Lesson 1\n\n[[Goal, steps, exercise, solution link]]\n")

    print(f"Created {a.archetype} skeleton in {out}")
    print("Next: replace every [[...]] (grep -rn '\\[\\[' .), add docs/assets/hero.png and demo.gif, "
          "verify every install command on a clean machine, then publish.")


if __name__ == "__main__":
    main()
