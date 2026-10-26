# Data findings: what the 491 most-starred repos show

Read this when you need the evidence behind a recommendation, or want to answer "how do you know?".

## Contents
1. What was analysed and how
2. Limits of this data (read first)
3. Finding 1: the market has shifted to AI-agent ecosystems
4. Finding 2: archetype table
5. Finding 3: README structure
6. Finding 4: fast vs slow growers
7. Finding 5: taglines and names
8. Finding 6: content-only repos, language, forks, activity, license
9. Finding 7: who is in the 2025-26 wave

---

## 1. What was analysed and how

- Source: user-supplied CSV `github_top_500_by_stars` (it actually holds **491** repos). Stars range 50,903 to 556,044 (median 75,713). Snapshot date 2026-10-25.
- Columns used: repository, stars, forks, language, description, created date, last push. (The "Watchers" column equals stars for every row, so it was ignored.)
- Every repo was read and **hand-labelled** into one of 12 archetypes (keyword rules were tried first and were too noisy). Labels are in `top491_enriched.csv`.
- README files were downloaded for **485 of 491** repos and measured for structure (hero image, GIF, install command, comparison, etc.).
- "Stars/day" = stars / days since creation. It is a **lifetime average**.

## 2. Limits of this data (read first)

1. **Survivorship bias.** Only winners are present. There is no list of the thousands of repos that did the same things and got 40 stars. So "winners often do X" does not prove "doing X makes you win".
2. **Stars/day is biased toward young repos.** Viral growth is front-loaded, so a 9-month-old repo looks faster than a 10-year-old one. Compare archetypes inside the same era only.
3. **Distribution is invisible.** The CSV cannot show the author's follower count, a launch on Hacker News, a retweet from a famous account, or luck. Some fast repos come from well-known companies or developers (at least 18 of the 96 repos created in 2025-26 come from 15 owners I recognise, e.g. anthropics, openai, github, karpathy, garrytan, addyosmani, mattpocock). Many others come from lesser-known accounts, so fame is not required, but it helps and cannot be measured here.
4. **Some structural features are effects, not causes.** Translations, star-history charts and sponsor links are mostly added *after* a repo takes off.
5. Star counts can be inflated or odd (for example one repo has 107k forks on 195k stars). Do not treat any single repo as a clean model.

Use the findings as a map of what the market rewarded, not as a guarantee.

## 3. Finding 1: the market shifted to AI-agent ecosystems

Created in 2025-26: **96 of 491 repos (20%)**. Median age 290 days, median 79k stars, and **32 of the 96 already have 100k+ stars**.

Archetype mix by era (% of that era's repos):

| Era | Skill packs | Agent tools | Agent products | Single-outcome apps | Lists | Learning | Frameworks | Alternatives | Dev tools |
|---|---|---|---|---|---|---|---|---|---|
| <=2019 | 0 | 0 | 0 | 2 | 15 | 16 | 35 | 8 | 15 |
| 2020-22 | 0 | 0 | 4 | 5 | 5 | 14 | 12 | 21 | 19 |
| 2023-24 | 0 | 15 | 16 | 23 | 3 | 11 | 7 | 3 | 4 |
| 2025-26 | **26** | **21** | 15 | 17 | 7 | 6 | 1 | 2 | 1 |

- 81% of 2025-26 repo descriptions mention AI / agent / Claude / Codex / LLM (4% of pre-2020 repos).
- Languages of 2025-26 repos: Python 42%, TypeScript 24%, JavaScript 9%, Rust 7%, Shell 4%, Go 3%.
- New frameworks, languages, and classic dev tools almost stopped entering the top list (1% each in 2025-26). The winners now are things that **plug into an AI workflow**.

## 4. Finding 2: archetype table

| Archetype | n | Share | Median stars | Same-era speed (stars/day) | Notes |
|---|---|---|---|---|---|
| FRAMEWORK (libs, languages, infra) | 107 | 21.8% | 73k | 2025+: n=1 | Median age 12 years. Almost all company/foundation backed. 90% still active. |
| LEARN (courses, interview prep, from-scratch) | 64 | 13.0% | 84k | 2025+: 177 (n=6) | 42% content-only. 27% are Chinese-language. Evergreen: 13 of 64 are dormant >1 yr and still huge. |
| DEVTOOL (CLI, terminal, utilities) | 56 | 11.4% | 66k | 2025+: 183 (n=1) | Median age 9 years. Fork ratio only 0.09 (people use it, not fork it). |
| LIST (awesome lists, link collections) | 53 | 10.8% | 78k | 2025+: 130 (n=7) | 60% content-only. README median 6,585 words. All 7 lists made in 2025-26 are about AI-agent / automation ecosystems (Claude skills, Claude Code, OpenClaw skills, system prompts, n8n workflows). |
| OUTCOMEAPP (single-outcome apps, mostly AI) | 40 | 8.1% | 72k | 2025+: 325 (n=16) | 52% created 2024+. Demo GIF on first screen in 40%. |
| ALTERNATIVE (open-source / self-hosted X) | 36 | 7.3% | 65k | slow burn | Median age 7 years. 50% of READMEs stress local / self-host / privacy on the first screen. |
| AGENTTOOL (add-ons for AI agents) | 31 | 6.3% | 78k | 2025+: 281 (n=20) | 90% created 2024+. 84% of READMEs cite benchmarks/results. |
| AGENTPRODUCT (agent frameworks / coding agents) | 28 | 5.7% | 100k | 2025+: 259 (n=14) | Mostly well-resourced orgs. |
| AIMODEL (models, inference, ML libs) | 27 | 5.5% | 76k | 2025+: 136 (n=2) | Labs and big companies. |
| SKILLPACK (skills / prompts / methods for coding agents) | 25 | 5.1% | 102k | 2025+: **412 (n=25)** | **100% created 2025-26.** Fastest archetype. README median 2,131 words. Mostly Markdown + a little code. |
| SECNET (security, proxy tools) | 15 | 3.1% | 74k | n=1 | Mostly established tools. |
| CULTURE (unusual / viral non-code) | 9 | 1.8% | 74k | n=1 | One-off phenomena. Not repeatable. |

## 5. Finding 3: README structure (485 READMEs)

Share of READMEs with each feature. "2025+" = repos created 2025 or later.

| Feature | All | 2025+ | Agent skill packs | Agent tools | Single-outcome apps | Lists |
|---|---|---|---|---|---|---|
| Image in first ~2,500 characters | 90% | 92% | 80% | 97% | 98% | 87% |
| Centered "hero" block | 54% | 71% | 44% | 87% | 78% | 45% |
| 5+ badges | 62% | 77% | 56% | 84% | 75% | 51% |
| GIF or video anywhere | 43% | 46% | 36% | 61% | 62% | 72% |
| GIF or video in first screen | 19% | 23% | 16% | 23% | **40%** | 23% |
| Any install command | 62% | **88%** | 92% | 94% | 85% | 38% |
| One-line install (npx/curl/brew/pip/docker/plugin) | 42% | **78%** | **84%** | **90%** | 70% | 19% |
| Quick start / install / usage heading | 64% | 88% | 88% | 94% | 90% | 19% |
| "Why / what is / overview" heading | 29% | 45% | **68%** | 55% | 32% | 17% |
| Comparison / "vs" content | 33% | 54% | **64%** | 61% | 40% | 68% |
| Numeric claim on first screen (%, x, N+) | 34% | 52% | 52% | 45% | 32% | 28% |
| Translations (other-language READMEs) | 26% | 50% | 44% | 39% | 45% | 25% |
| Star-history chart | 15% | 43% | 28% | 39% | 40% | 9% |
| Table of contents | 20% | 11% | 8% | 6% | 10% | **53%** |

Median README length: 1,197 words overall. By archetype: Lists 6,585 / Agent tools 2,496 / Skill packs 2,131 / Single-outcome apps 1,854 / Learning 1,689 / Dev tools 1,186 / Alternatives 864 / Frameworks 631.

Even the #13 repo (obra/superpowers, 304k stars) has no image on its first screen. Structure converts visitors; it does not replace a strong idea or distribution.

## 6. Finding 4: fast vs slow growers

Within repos created 2023 or later (n=169), top third by stars/day (n=56) vs bottom third (n=56). The "fast" threshold is above ~236 stars/day, "slow" below ~100.

| Feature | Fast | Slow | Gap | Likely cause or effect? |
|---|---|---|---|---|
| Comparison / "vs" content | 55% | 23% | +32 | Plausibly a cause (clear positioning) |
| "Why / what is" section | 52% | 21% | +31 | Plausibly a cause |
| Translations | 54% | 25% | +29 | Mostly an effect |
| Star-history chart | 52% | 25% | +27 | Effect |
| Sponsors | 41% | 20% | +21 | Effect |
| Quick-start heading | 89% | 71% | +18 | Plausibly a cause |
| One-line install | 82% | 66% | +16 | Plausibly a cause |
| 5+ badges | 77% | 62% | +15 | Weak |
| Any install command | 95% | 80% | +15 | Plausibly a cause |
| Image on first screen | 93% | 89% | +4 | No real gap |
| Table of contents | 7% | 23% | -16 | Fast repos use fewer TOCs |
| Generic "Features" section | 36% | 50% | -14 | Fast repos explain *why*, not only list features |

Other gaps: median README **2,464 words (fast) vs 1,100 (slow)**; median images 11.5 vs 7.5; median `##` sections 13 vs 7.5; median GitHub description **121 chars vs 76**.

Breadth: among 2025-26 skill packs and agent tools (n=45), 87% name 3+ coding agents and 71% name 6+ (median 9). Those naming 6+ had median 318 stars/day vs 223 for the rest.

## 7. Finding 5: taglines and names

GitHub "About" descriptions:
- Median length: **100 chars for 2025+ repos vs 60 for pre-2020**. Modern winners spend more words on the promise.
- Numbers in the tagline: agent tools 32%, single-outcome apps 35%, learning 28% (all repos 17%). Percent / "x" claims in 19% of agent-tool taglines.
- Verb-first imperative taglines ("Turn...", "Make your agent...", "Cut...", "Give your agent...") in 23% of agent-tool taglines.
- "Turn any X into Y" pattern: 5% of 2025+ taglines (8% of skill packs).
- "alternative" appears in 25% of alternative-archetype taglines; "free / open-source" in 53%; self-hosted/local/private in 28%.
- Learning repos use "from scratch" (6%), lesson/day/week counts, "for beginners" (23%).

Repo names:
- 60% are one token (no hyphen, underscore, or dot). Median length 9-10 characters. Names for 2025+ are slightly more often hyphenated (46%).
- 12% of 2025+ repo names contain "skill"; 14% contain claude/claw/code; 8% contain "agent".
- Roughly half of the fast skill/tool repos use a memorable metaphor or personality name (caveman, ponytail, humanizer, superpowers, impeccable, mempalace, headroom, graphify); the other half use plain descriptive names (claude-mem, last30days-skill, academic-research-skills, context7). Both work **if the tagline carries the promise**.

## 8. Finding 6: content-only, language, forks, activity, license

- **15% of the 491 have no real code language** (Markdown / Unknown / HTML / Notebook / Roff). In the top 100 by stars it is **23%**. You do not need a big codebase to win; knowledge and curation repos are overrepresented at the very top.
- **Chinese-language** descriptions: 34 repos (7%), of which 17 are in LEARN (27% of all learning repos) and 6 in LIST. Chinese-language study guides (JavaGuide, CS-Notes, leetcode-master, Python-100-Days) are among the biggest learning repos.
- **Fork ratio** (forks / stars): median 0.12. Utility tools like CLIs have 0.03-0.09 (people install, not fork). Repos you *fork to run yourself* have high ratios: daily_stock_analysis 0.83 (runs on scheduled GitHub Actions), NextChat 0.66 (one-click deploy), TrendRadar ~0.4. Practice repos (first-contributions, 1.98) are forked to be used.
- **Activity:** 76% were pushed in the last 30 days (90% for 2025+). 10% have had no push in a year, mostly learning, framework and list repos. Fast-growing repos are maintained continuously.
- **License** (as mentioned in README text, not the LICENSE file): MIT 39% overall and **62% of 2025+**; Apache 14% / 16%; GPL/AGPL 7% / 6%; not stated 38% / 16%.

## 9. Finding 7: who is in the 2025-26 wave

Fastest 2025-26 repos by lifetime stars/day (selection): deepseek-harness (3,572/day), photocraft (2,900), morluto/rea (1,959), HowToLiveBetter (1,432), ponytail (1,301), openclaw (1,173), mattpocock/skills (1,146), ECC (1,030), claw-code (938), andrej-karpathy-skills (825), superpowers (800), graphify (657), gstack (603), awesome-design-md (593), caveman (563).

Patterns across them:
1. **One painful job, stated in one line**: "stops your agent burying the answer", "cuts tokens 60-90%", "removes signs of AI-generated writing", "turn any codebase into a knowledge graph".
2. **Zero-cost adoption**: copy a file, one command, or install a plugin.
3. **A point of view or an authority**: "my setup", "derived from Karpathy's observations", "Garry Tan's exact setup".
4. **Measured claims** or before/after output.
5. **Works with many agents**, not locked to one.
6. **Rides the platform wave** (Claude Code, Codex, OpenClaw, MCP, skills) at the moment developers were hungry for help.
