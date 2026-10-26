---
name: github-star-magnet
description: Turns any project idea into a GitHub repo designed to earn stars, real users and contributors, using patterns measured from the 491 most-starred GitHub repositories (12 repo archetypes, growth speed, naming, taglines, README structure, launch plan). Use this whenever the user wants to build, reshape, name, package, launch or fix a GitHub or open-source project so it becomes popular - for example "make my idea a popular repo", "my repos get no stars", "how do I get GitHub stars or go viral", "what should I build to get stars", "write a README that attracts people", "repo name or tagline ideas", "audit my repo", "launch my open-source project". Also use when the user describes any project idea and mentions GitHub, stars, open source, recognition, popularity or portfolio visibility, even if they never say "skill" or "viral".
---

# GitHub Star Magnet

Take a project idea (or an existing repo that is not getting noticed) and turn it into a repo shaped like the ones that actually won. The shape comes from a hand-labelled study of the 491 most-starred repos and the READMEs of 485 of them.

Files in this skill (paths are relative to this folder):
- `references/data-findings.md` - all measured numbers and their limits
- `references/archetypes.md` - the 12 repo shapes, exemplars, how to reshape an idea into each
- `references/idea-transformations.md` - 11 reshaping moves, the 20-point Star Score, anti-patterns, worked examples
- `references/readme-blueprint.md` - tagline formulas, naming rules, README anatomy, repo page settings
- `references/launch-playbook.md` - diagnosis of stalled repos, launch plan, channels, ethics (mostly general practice, not measured)
- `references/top491_enriched.csv` - the labelled dataset
- `scripts/find_comparables.py`, `scripts/scaffold_repo.py`, `scripts/audit_readme.py`, `scripts/refresh_dataset.py`

## Ground rules

1. **Be honest about what the data can and cannot say.** It contains only winners (survivorship bias), cannot show launch timing, author fame, or luck, and structural features are correlations. In the first reply, say this in two sentences, then move on. Never promise stars. Say "raises the odds", not "guarantees".
2. **Never help fake popularity.** No bought stars, star-swap groups, bot accounts, or fake testimonials. If asked, decline in one sentence and offer the honest route (better packaging, real launch).
3. **Never invent** benchmarks, user quotes, install commands, or version numbers. Everything in a README must be true and tested. If a number is unknown, write a plan to measure it.
4. **Reshape, do not clone.** Learn from winners, then find a different wedge or segment. Credit inspirations. Do not copy code or README text.
5. **Plain, short language.** The user may not be a native English speaker or may write quickly with typos. Use short sentences, explain any jargon in a few words, give copy-paste outputs. Keep chat replies to what fits on a phone screen; put the long material in files.
6. **Keep the user's goal central.** They want recognition for their work. Tell them clearly when the idea itself is the problem, and say what to change.

## Why repos win: three engines

Use these as the mental model when advising:

1. **Utility engine** - a painful, frequent task is solved in under a minute (agent tools, apps, dev tools, alternatives). Stars come from people who used it.
2. **Reference engine** - knowledge people bookmark (lists, learning repos). 15% of the top 491 have no real code; it is 23% of the top 100. Stars come from "save for later".
3. **Wave engine** - riding a platform wave with a portable artifact that costs nothing to adopt (2025-26: skills, agent add-ons built around coding agents). Stars come from curiosity plus authority.

The fastest repos in the data (created 2025-26: 20% of the top 491) combine one sharp promise + one-command adoption + a number + a point of view + wide compatibility.

## Workflow

Pick the mode first:
- **New idea** -> Steps 1-7
- **Existing repo(s) not getting stars** -> "Audit mode" below
- **"I don't know what to build"** -> "Ideation mode" below

### Step 1: Intake (at most two questions)

Needed: the idea in 1-3 sentences, who it is for, what the user can build in about 2 weeks (skills, languages), and whether they want you to build it now. If the idea is already clear, do not interrogate: state your assumptions in one line and proceed. If the idea is too vague to act on, use `ask_user_input_v0` when available (tappable options) with one question about what they know best or who the user is.

### Step 2: Find comparables

From the skill folder:

```bash
python3 scripts/find_comparables.py "keywords about the idea" --since 2023
python3 scripts/find_comparables.py --archetypes          # benchmark table
python3 scripts/find_comparables.py --list-archetype SKILLPACK --since 2025
```

Read the closest matches: who already won, which archetype, how fast. The CSV only holds 491 repos, so mid-size competitors are invisible. If web search is available, also search GitHub for the 3-5 closest repos with 300+ stars and note their wedge.

### Step 3: Choose the archetype and reshape the idea

Quick chooser (details and exemplars in `references/archetypes.md`):

| If the idea is mostly... | Archetype | Solo fit (1-5) |
|---|---|---|
| expertise/workflow/taste an AI coding agent could follow | SKILLPACK | 5 |
| a fix for pain AI-agent users feel (cost, memory, context, web access) | AGENTTOOL | 4 |
| one input -> one visible result | OUTCOMEAPP | 4 |
| bookmark-worthy knowledge about a hot, fast-growing area | LIST | 4 |
| teaching something step by step ("from scratch") | LEARN | 4 |
| a small sharp terminal/desktop utility | DEVTOOL | 3 |
| a self-hostable version of a paid product | ALTERNATIVE | 2 |
| new agent platform / framework / library / model | AGENTPRODUCT, FRAMEWORK, AIMODEL | 1 |

Same-era speed (stars/day, repos created 2025-26): SKILLPACK 412, OUTCOMEAPP 325, AGENTTOOL 281, AGENTPRODUCT 259, LEARN 177, LIST 130. These show what the market rewarded, not a promise for new repos.

Then apply the reshaping moves in `references/idea-transformations.md` (name the person and pain, ride the wave if it fits, shrink to one wedge, 60-second first result, visible result, defensible number, go universal, add a point of view, frame against something familiar, add a contribution surface, offer the learning version). If the idea has nothing to do with AI, do not force it: pick LEARN, LIST, ALTERNATIVE or DEVTOOL and tell the user the curve is usually slower (median age of those top repos is 7-10 years).

### Step 4: Score it

Fill the Star Score table from `references/idea-transformations.md` (10 criteria, 0-2 each, one line of reasoning per row). 16+ build now; 11-15 reshape once or twice more; 0-10 recommend another idea or archetype and say why. Show the table so the user can disagree.

### Step 5: Produce the Repo Blueprint

Use exactly this structure (concise; bullets or short table cells):

```
## Repo Blueprint: <working title>
**Archetype:** <code> - why it fits
**Promise (one sentence, <=140 chars):**
**Who it is for / the pain:**
**Why now:** <wave or reason>
**Closest competitors and your wedge:** (table, 3 rows)
**Name candidates:** 3 metaphor + 3 plain; top pick; checks to run (GitHub, npm/PyPI, domain)
**Tagline options:** 3, pick one (formulas in references/readme-blueprint.md)
**Topics (<=20):**
**MVP scope for v0.1 (<=2 weeks):** will do / will NOT do
**Install design:** the single command a user runs
**Proof plan:** what number you will measure and how
**Demo plan:** what the 10-20 second GIF shows (the RESULT)
**Star Score:** table
**Honest odds and risks:**
**Next 7 days:** checklist
```

### Step 6: Build it (when the user says "make it", "build it", or has agreed to the blueprint)

1. Scaffold: `python3 scripts/scaffold_repo.py --name <name> --tagline "<tagline>" --archetype <CODE> --author "<name>" --user <github-user> --out /mnt/user-data/outputs/<name>` (codes: SKILLPACK, AGENTTOOL, OUTCOMEAPP, DEVTOOL, LIBRARY, ALTERNATIVE, LEARN, LIST).
2. Implement the **smallest working version** of the MVP in the repo. For SKILLPACK, write real, useful skills (follow the skill-writing style: imperative, explain why). For LIST, research real entries with a web tool and verify each link. For LEARN, write runnable lessons.
3. **Run it.** Execute the quick start exactly as the README describes. Fix whatever breaks. Do not publish unverified install commands.
4. Replace every `[[placeholder]]` in README and CONTRIBUTING (`grep -rn "\[\[" .`). Remove sections you cannot support (for example Proof with no data).
5. Demo: if you can produce a real terminal recording or screenshot, do it. If not, write `docs/demo-script.md` with the exact commands and what to show, and tell the user to record it with any screen recorder (the GIF must come from a clean run). Never fabricate a demo.
6. Self-check: `python3 scripts/audit_readme.py <path>/README.md`. Aim for 80+ with no warnings, and the first-screen test in `references/readme-blueprint.md` passing.
7. Deliver: zip the folder (`cd /mnt/user-data/outputs && zip -r <name>.zip <name>`) and call `present_files` with the README and the zip. Add a short note: where to put hero.png and demo.gif, and the git commands to publish (`git init`, `git add .`, `git commit`, `gh repo create` or push to a new GitHub repo).

### Step 7: Launch kit

Using `references/launch-playbook.md`, write only what fits the archetype: the GitHub About text and topics; a Show HN title plus first comment; an X/LinkedIn thread; a Reddit post (check rules); a dev-blog outline ("how I built X / benchmarks"); a list of awesome lists, directories and registries to submit to; and a 4-week plan with the first-100-stars milestone. Label practice advice as practice, data as data. Remind the user to reply to issues within 24-48 hours.

## Audit mode (existing repos)

1. Get the repo link(s) or the README text. Run `python3 scripts/audit_readme.py owner/repo` (fetches from raw.githubusercontent.com) or point it at a local file.
2. Check the repo page too: About text, website, topics, social preview image, release, `good first issue` labels. Use `web_fetch` on the repo URL if available; otherwise ask the user to paste them.
3. Diagnose with the table in `references/launch-playbook.md` section 2: **distribution** (few visitors), **packaging** (visitors but few stars), **idea** (stars but no usage, or everything weak). Ask for GitHub Insights -> Traffic numbers if they have them.
4. Output: the score, the top 5 fixes, a rewritten tagline and README first screen, and a plain verdict on whether the idea needs a new wedge (use Steps 2-4).
5. With several repos: score each (Star Score), recommend focusing on the best 1-2, and explain that spreading effort over many weak repos is the common reason none gets noticed.

A structure score is a conversion tool. A perfect README on a weak idea with no distribution will still get few stars. Say this plainly.

## Ideation mode ("what should I build?")

1. Ask one question: what do you know best, or use daily (domain, language, tools)?
2. Run `find_comparables.py --archetypes` and `--list-archetype SKILLPACK --since 2025` (and one other archetype that fits).
3. Propose 3 ideas, each as: one-line promise, archetype, closest comparable from the data, Star Score, and the first weekend's work. Recommend one and say why (prefer demoable in a weekend, with a measurable claim and a clear wedge).

## Keeping the skill fresh

The dataset is a snapshot (2026-10-25) and the AI-agent wave may fade or crowd. If the user supplies a newer CSV, run `scripts/refresh_dataset.py`, label the `Archetype` column by reading each description, replace `references/top491_enriched.csv`, and recompute the numbers in `references/data-findings.md`. Prefer fresh web search over the dataset for anything about "what is hot right now".

## Quick facts for "how do you know?"

- 491 repos, 50.9k-556k stars; 485 READMEs analysed; every repo hand-labelled.
- 96 repos (20%) were created in 2025-26; 32 of them already exceed 100k stars; 81% of their descriptions mention AI or agents.
- Skill packs: all 25 created 2025-26, fastest archetype. Agent tools: 90% created 2024+.
- 2025-26 READMEs: 88% have an install command, 78% a one-line install, 54% a comparison, 45% a "why" section, 50% translations (translations and star-history charts are mostly effects of growth).
- Fast vs slow growers (created 2023+): comparison content 55% vs 23%, "why" section 52% vs 21%, quick-start heading 89% vs 71%, README length ~2,460 vs ~1,100 words, GitHub description ~121 vs ~76 characters.
- Even the #13 repo (superpowers) has no image on its first screen: packaging helps, but the idea and reach matter more.
