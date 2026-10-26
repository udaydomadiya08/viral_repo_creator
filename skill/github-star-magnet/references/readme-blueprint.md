# README, name, tagline and repo-page blueprint

Read this when writing or rewriting the front door of a repo. Numbers come from `data-findings.md` (485 READMEs from the top 491 repos). Items marked **[practice]** are general open-source practice, not measured in the dataset.

## Contents
1. The first-screen test
2. Tagline formulas
3. Naming rules
4. README anatomy (top to bottom)
5. Repo page settings (About, topics, social preview)
6. Proof: how to make numbers believable
7. Common README mistakes

---

## 1. The first-screen test

A visitor decides in about five seconds. Within the first screen (roughly the first 2,500 characters) the README must answer:

1. **What is it?** One sentence, specific. (Top repos: 90% put a visual here too.)
2. **What do I get?** A result, a number, or a picture of the result.
3. **How do I try it?** One command, or an obvious Quick Start link. (2025-26 repos: 78% have a one-line install.)

If a stranger cannot answer these three in five seconds, rewrite before doing anything else.

## 2. Tagline formulas

Use the same sentence for the GitHub "About" box, the first line of the README, and the first line of every launch post. Modern winners write longer, more specific taglines (median 100 chars for 2025+ vs 60 before 2020). Aim for **70-140 characters**.

| Formula | When | Pattern | Example shape (invented) |
|---|---|---|---|
| Result + number | Tools that save something | "[Verb] your [thing] by [N%] with one command" | "Cut your agent's token bill by 60% with one command" |
| Turn any X into Y | Converters, apps | "Turn any [input] into [output]" | "Turn any website into a desktop app" |
| Give / make your agent... | Skills, agent tools | "Give your agent [ability]" / "Make your agent [behavior]" | "Give your coding agent a memory that survives restarts" |
| Open-source alternative | Alternatives | "The open-source [Product] alternative. Self-hosted, private." | "The open-source Notion alternative you can self-host" |
| From scratch / N lessons | Learning | "Build [thing] from scratch in [N steps/lessons]" | "Build a working search engine from scratch in 12 lessons" |
| Curated + scope | Lists | "A curated list of [what] for [who], updated [cadence]" | "A curated list of MCP servers that actually work" |
| Persona + stance | Skill packs | "[My/Name's] exact [setup/method] for [job]" | "My exact review workflow for AI-written code" |

Rules:
- **Name the user and the result**, not the technology. "A Rust-based, modular, extensible framework" says nothing.
- Include **one real number** if you can defend it (32-35% of agent-tool and app taglines include a number).
- Put the **primary keyword** people search for in the first 60 characters.
- No hype words you cannot prove ("revolutionary", "best ever"). If you claim "#1" or "fastest", link the evidence.

## 3. Naming rules

Data: 60% of top repo names are a single token (no hyphen), median 9-10 characters. In 2025-26, roughly half of fast skill/tool repos use a memorable metaphor name (caveman, ponytail, humanizer, headroom, graphify) and half use plain descriptive names (claude-mem, context7, last30days-skill).

Choose by this test:
1. **Say it aloud**: easy to spell and say after hearing it once.
2. **Searchable**: not a common word that buries you in results; check GitHub, npm/PyPI/crates, and the `.com`/`.dev` domain.
3. **Signals the job** within the tagline even if the name is abstract.
4. **Works as a CLI command** if it is a tool (short, lowercase, no underscores).
5. **Avoid trademarks**: do not put another company's product name in your repo name unless it is clearly a plugin for it (many do, e.g. "...-for-claude-code"); describe compatibility in the tagline instead.

Generate 8-10 candidates in two styles (metaphor/personality and plain descriptive), then pick the top 3 and run the checks.

## 4. README anatomy (top to bottom)

Order that the fastest 2025-26 repos use:

1. **Hero block** (centered): logo or banner (1280x640), name, tagline, 3-5 badges (license, release/CI, stars, community). 71% of 2025+ READMEs use a centered hero; 77% have 5+ badges.
2. **Demo**: a 10-20 second GIF/video of the **final result** (not the setup). Apps: 40% put this on the first screen. If it is a CLI, record the terminal; if it is a skill, show before/after output side by side.
3. **Nav row**: Install - Quick start - Why - Docs - Community. **[practice]**
4. **Why this exists**: the pain in 2-3 sentences, then what changes. (Fast repos 52% vs slow 21%.)
5. **Comparison table** vs what people use today: fair, specific rows (setup time, cost, privacy, speed, what it cannot do). (Fast 55% vs slow 23%.)
6. **Install (30 seconds)**: one command per platform. Verify on a clean machine.
7. **Quick start**: the first successful run with the expected output shown.
8. **Proof**: numbers with method (see section 6).
9. **How it works**: 3-5 steps or one diagram.
10. **Works with**: every platform/agent/OS you tested. Top 2025-26 agent repos name a median of 9 agents.
11. **What's inside / features** as a table (not an endless bullet list).
12. **Roadmap** with checkboxes; invite issues to vote.
13. **Contributing** (specific ways to help) and **License** (MIT or Apache-2.0 are the safe default; MIT appears in 62% of 2025+ READMEs).
14. Added later, after traction: translations (50% of 2025+ READMEs have them), star-history chart, sponsors, community links.

Length: median 1,197 words overall; fast growers about 2,460 vs 1,100 for slow ones. Depth helps *if it is skimmable*: many `##` sections (fast median 13), tables, collapsible `<details>` blocks. Skip a table of contents unless the page is very long (lists: 53% use TOCs; fast agent repos rarely do).

## 5. Repo page settings

**[practice]** unless noted.
- **About description** = the tagline (data: fast repos have 121-char descriptions vs 76).
- **Website field**: demo page, docs, or the package page.
- **Topics (up to 20)**: mix broad + specific: the archetype word (`cli`, `agent-skills`, `self-hosted`), the platforms (`claude-code`, `codex`, `mcp`), the language, and the problem (`token-optimization`, `pdf`, `web-scraping`).
- **Social preview image** (Settings -> General): upload the 1280x640 hero. It controls how links look on X, Slack, LinkedIn, Discord.
- **Releases**: tag v0.1.0 with notes. A release badge signals a living project.
- **Issues + Discussions** on; add 3-5 `good first issue` items.
- **Pin** the repo on your profile and write a profile README that links it.

## 6. Proof: how to make numbers believable

Agent tools: 84% of READMEs cite benchmarks / evals / results. A number is persuasive only when checkable:
1. State **what you measured** ("input tokens per session").
2. State **how** (N tasks, which models, which dates) and give the script.
3. Show **before/after** raw output, not only a percentage.
4. Show **where it does not help**. Honest limits earn trust.
5. Never invent numbers. If you have none yet, write "Early results" with your real sample, or leave the Proof section out.

## 7. Common README mistakes

- Text-only first screen, or a logo with no explanation of what the project does.
- A long feature list before the pain is explained.
- Install instructions that need 6 steps, or that were never tested on a clean machine.
- Demo that shows installation instead of the result.
- A comparison that is obviously rigged.
- No license, or placeholder text left in ("[[TODO]]").
- Marketing words instead of specifics.
- Abandoned badges (broken CI, 404 images).
