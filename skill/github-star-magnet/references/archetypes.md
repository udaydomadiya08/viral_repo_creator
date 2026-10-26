# Archetypes: the 12 repo shapes that reach 50k+ stars

Use this after running `scripts/find_comparables.py`. Pick ONE primary archetype for the user's idea. Each entry gives: what it is, the evidence, exemplars from the dataset, why it wins, how to reshape an idea into it, effort and risk for a solo developer.

## Contents
- Quick chooser
- 1 SKILLPACK  - 2 AGENTTOOL  - 3 OUTCOMEAPP  - 4 LIST  - 5 LEARN  - 6 DEVTOOL
- 7 ALTERNATIVE  - 8 AGENTPRODUCT  - 9 FRAMEWORK/LIBRARY  - 10 AIMODEL  - 11 SECNET  - 12 CULTURE
- Combining archetypes

## Quick chooser

| If the user's idea is mostly... | Choose | Solo-dev fit (1 = low, 5 = high) |
|---|---|---|
| Expertise, workflow, or taste that an AI coding agent could follow | SKILLPACK | 5 |
| A fix for a pain AI-agent users feel (cost, memory, context, web access, visibility) | AGENTTOOL | 4 |
| One clear result from one input (video, voice, report, job match, analysis) | OUTCOMEAPP | 4 |
| Knowledge that people bookmark, about a fast-growing area | LIST | 4 |
| Teaching something step by step, "from scratch" | LEARN | 4 |
| A small sharp terminal/desktop utility | DEVTOOL | 3 |
| A self-hostable version of a product people pay for | ALTERNATIVE | 2 (slow, needs depth) |
| A new agent platform | AGENTPRODUCT | 1 (needs a team and an audience) |
| A new framework / language / library | FRAMEWORK | 1 |
| A new model | AIMODEL | 1 |

If two fit, take the one with the lower effort to a *demoable result in a weekend*.

---

## 1. SKILLPACK - skills, prompts, methodology for AI coding agents

- **Evidence:** 25 repos, **all created 2025-26**; same-era median **412 stars/day** (fastest archetype); median 102k stars; README median 2,131 words; one-line install in 84%; "why" section 68%; comparison 64%.
- **Exemplars:** obra/superpowers (304k), mattpocock/skills (302k), affaan-m/ECC (288k), multica-ai/andrej-karpathy-skills (223k, a single CLAUDE.md), anthropics/skills (183k), DietrichGebert/ponytail (175k), msitarzewski/agency-agents (163k), garrytan/gstack (137k), nextlevelbuilder/ui-ux-pro-max-skill (140k), Leonxlnx/taste-skill (102k), blader/humanizer (60k), ayghri/i-have-adhd (58k), mvanhorn/last30days-skill (65k), coreyhaines31/marketingskills (56k), K-Dense-AI/scientific-agent-skills (54k).
- **Why it wins:** the product is *text*, so adoption cost is near zero (copy a folder or run one install). The author's judgment is the product. A vivid single promise ("ADHD-friendly output", "removes AI-sounding writing", "marketing skills", "design taste") is easy to share.
- **Reshape an idea into it:** ask "what do I know how to do well that an agent does badly?" Package that as 3-10 composable skills with a clear workflow. Name a **domain** (marketing, research, UI, security, data, legal, finance, teaching), not "general productivity".
- **Must have:** install block for many agents (top repos list 6-16), a "How it works" story, before/after proof, a stated philosophy.
- **Effort:** days. **Risk:** crowded; trendy; depends on the agent platform; authority and audience matter. Differentiate by **domain depth + proof** not by volume of skills.

## 2. AGENTTOOL - add-ons that fix pain for AI-agent users

- **Evidence:** 31 repos, 90% created 2024+; same-era median **281 stars/day** (n=20); README median 2,496 words; **84% cite benchmarks/results**; one-line install 90%; centered hero 87%; 71% of 2025+ ones name 6+ agents.
- **Exemplars:** farion1231/cc-switch (148k), Graphify-Labs/graphify (134k), JuliusBrussee/caveman (115k), thedotmack/claude-mem (103k), Panniantong/Agent-Reach (102k), stablyai/orca (105k), rtk-ai/rtk (84k), headroomlabs-ai/headroom (78k), colbymchenry/codegraph (75k), upstash/context7 (64k), mem0ai/mem0 (67k), CLIProxyAPI (56k), Egonex-AI/Understand-Anything (88k), microsoft/markitdown (192k), firecrawl/firecrawl (195k), browser-use (119k).
- **Pain buckets that won:** **cost/tokens** (rtk, caveman, headroom), **memory** (claude-mem, mem0, mempalace, hindsight), **context** (codegraph, graphify, context7), **access** (Agent-Reach, firecrawl, browser-use, chrome-devtools-mcp), **routing/gateways** (cc-switch, OmniRoute, CLIProxyAPI, litellm), **understanding** (Understand-Anything, graphify).
- **Why it wins:** it removes a pain that every heavy agent user feels *daily*, and the benefit is measurable (tokens saved, tasks solved).
- **Reshape an idea:** state the pain in the agent user's words, then a **number** ("cuts X by 60%"). Build the smallest working version, then measure it on 20-50 real tasks and publish the method.
- **Effort:** 1-4 weeks. **Risk:** platforms may ship the feature natively; mitigate by being agent-agnostic and fast.

## 3. OUTCOMEAPP - one input, one clear result

- **Evidence:** 40 repos, 52% created 2024+; same-era median **325 stars/day** (n=16); demo GIF on the first screen in **40%** (highest of any archetype); 20% of taglines say local / private / self-host.
- **Exemplars:** harry0703/MoneyPrinterTurbo (134k: topic -> HD short video), hacksider/Deep-Live-Cam (97k), debpalash/VoiceStudio (85k), career-ops-hq/career-ops (77k), calesthio/OpenMontage (72k), hugohe3/ppt-master (68k), abi/screenshot-to-code (80k: drop a screenshot, get code), upscayl/upscayl (50k), TauricResearch/TradingAgents (113k), ZhuLinsen/daily_stock_analysis (67k), koala73/worldmonitor (89k), karpathy/autoresearch (99k).
- **Why it wins:** the promise is a *result* you can see in a GIF ("drop a screenshot, get code"). Free and local lowers the barrier. Some are **fork-to-run** (scheduled GitHub Actions or one-click deploy), which produces huge fork counts and word of mouth.
- **Reshape an idea:** write "Give it ___, get ___ in ___ seconds". If you cannot fill all three blanks, the idea is not sharp yet. Make the first run work with **no API key** if at all possible.
- **Effort:** 1-6 weeks. **Risk:** model/API costs; legal and ethical issues (voice/face cloning, scraping, financial advice). Add clear disclaimers; avoid harm.

## 4. LIST - a curated list for a fast-growing area

- **Evidence:** 53 repos; 60% content-only; README median 6,585 words; TOC in 53%; sponsor links in 53%. **All 7 lists created in 2025-26** are about AI-agent / automation ecosystems.
- **Exemplars:** sindresorhus/awesome (524k), public-apis (492k), awesome-selfhosted (330k), awesome-python (330k), prompts.chat (174k), awesome-llm-apps (142k), punkpeye/awesome-mcp-servers (96k), ComposioHQ/awesome-claude-skills (78k), hesreallyhim/awesome-claude-code (56k), VoltAgent/awesome-openclaw-skills (53k).
- **Why it wins:** people bookmark (star) things they will need later. A list is the front door to a new ecosystem.
- **Reshape an idea:** choose a *narrow, hot* ecosystem where beginners ask "what should I use?" and no list is clearly dominant. Write inclusion criteria first, then categories, then one-line "why click" notes. Add a CONTRIBUTING guide; PRs from authors of listed items spread the list.
- **Effort:** a weekend to start, then weekly upkeep. **Risk:** the first list in a niche wins; later ones struggle. Must be actively maintained (stale lists die).

## 5. LEARN - teach it step by step

- **Evidence:** 64 repos (13%); 27% are Chinese-language; "N lessons / weeks / days", "from scratch", "for beginners" are common patterns. 2025-26 entries are all agent/LLM topics.
- **Exemplars:** codecrafters-io/build-your-own-x (556k), donnemartin/system-design-primer (375k), jwasham/coding-interview-university (363k), rasbt/LLMs-from-scratch (107k), microsoft "for Beginners" series (AI-for-beginners, ML-for-beginners, generative-ai, ai-agents), datawhalechina/hello-agents (84k), shareAI-lab/learn-claude-code (79k), rohitg00/ai-engineering-from-scratch (73k), karpathy/nanochat (59k), jingyaogong/minimind (64k).
- **Why it wins:** evergreen value + students share it. Interview prep and "from scratch" give a concrete finish line.
- **Reshape an idea:** turn "a tool I built" into "how to build this yourself in N steps" (a runnable, minimal version). Give a roadmap, time estimate, and a result learners can show off.
- **Effort:** 2-8 weeks of writing, high quality bar. **Risk:** thin tutorials get ignored; accuracy matters.

## 6. DEVTOOL - one small sharp utility

- **Evidence:** 56 repos; median age 9 years; fork ratio 0.09 (people use it rather than fork it); only 1 created in 2025+ (tw93/Mole, 73k).
- **Exemplars:** fzf (83k), ripgrep (69k), bat (60k), lazygit (83k), lazydocker (53k), starship (60k), tldr (64k), Pake (62k: "turn any website into a desktop app with one command"), Mole (73k).
- **Why it wins:** instantly useful and fast. Typically described as "X, but better" in a few words.
- **Reshape an idea:** pick one frequent annoying task, make it a single command with beautiful output, ship a single binary (Rust/Go) or `npx`/`brew` install.
- **Effort:** 2-6 weeks. **Risk:** slow star curve in the current era unless it also serves the AI-agent audience.

## 7. ALTERNATIVE - open-source / self-hosted version of a known product

- **Evidence:** 36 repos; median age 7 years; 25% of taglines use the word "alternative"; 53% say free/open-source; **50% of READMEs stress local / self-host / privacy on the first screen**; only 2 created in 2025+.
- **Exemplars:** n8n (208k), supabase (113k), immich (117k), rustdesk (126k), excalidraw (134k), localsend (95k), uptime-kuma (92k), OpenCut (96k, "the open-source CapCut alternative"), Stirling-PDF (94k), AppFlowy, AFFiNE, twenty, plane, coolify, vaultwarden.
- **Why it wins:** an existing paid product proves demand, and people want ownership/privacy/free.
- **Reshape an idea:** name the product you replace in the tagline; do a *fair* feature-parity table; make self-hosting a single `docker compose up`.
- **Effort:** months. **Risk:** feature depth is expensive. Choose a product where a 20% version covers 80% of users (e.g. a focused editor, a single-purpose tool).

## 8. AGENTPRODUCT - agent platforms and coding agents

28 repos (openclaw 393k, hermes-agent 257k, opencode 221k, AutoGPT 187k, claude-code 153k, codex 131k, langchain 148k, gemini-cli 108k). Mostly big organizations or teams with an existing audience. For a solo developer this is the **last** archetype to choose; build an AGENTTOOL or SKILLPACK *for* these platforms instead.

## 9. FRAMEWORK / LIBRARY

107 repos, median age 12 years, 1% of the 2025-26 cohort. Backed by companies and communities; a decade of growth. Not a realistic target for a new solo repo unless the library is tiny, solves a specific new problem (e.g. text layout, chenglou/pretext 51k), and has a stunning demo.

## 10. AIMODEL

27 repos from labs and large companies (models, inference engines, training). Solo path: a **small educational model** is really a LEARN repo (nanoGPT, nanochat, minimind).

## 11. SECNET

15 repos (security tools, proxy clients, reverse engineering). Mostly established tools. If building here, follow ethical-use rules and avoid anything that enables harm.

## 12. CULTURE

9 repos (996.ICU, Apollo-11, HowToCook, HowToLiveBetter, the X recommendation algorithm). One-off phenomena tied to a cultural moment. Not a repeatable plan.

---

## Combining archetypes (the strongest move for a solo developer)

- **AGENTTOOL + SKILLPACK:** a tool plus a skill that teaches the agent to use it (rtk, caveman, graphify do this).
- **LIST + LEARN** around the same hot topic: a list that points to your tutorials.
- **OUTCOMEAPP + LEARN:** "How I built X" as a lesson series inside the repo.
- Keep the **front door single**: one tagline, one install command, one archetype. Extras go lower in the README.
