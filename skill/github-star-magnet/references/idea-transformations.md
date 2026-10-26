# Idea transformations and the Star Score

Read this when the user hands over an idea and you must reshape it into something with real star potential. The moves below come from patterns in the 491 top repos; the rubric is a **heuristic synthesis, not a validated model**. Say so if asked.

## Contents
1. The eleven transformation moves
2. Star Score rubric (0-20)
3. Validate before building
4. Anti-patterns (what the data says not to build)
5. Worked examples (invented, for illustration)

---

## 1. The eleven transformation moves

Apply them in order. After each, ask "is the idea sharper?" Stop when it is.

1. **Name the person and the pain.** "Developers who use coding agents all day and watch their token bill climb." Not "developers".
2. **Pick where the audience is now.** In 2025-26, 81% of new top-repo descriptions are about AI/agents. Ask: *can this plug into an AI-agent workflow without feeling forced?* If yes, reshape it that way (it is where attention and growth are). If not, choose LEARN / LIST / ALTERNATIVE / DEVTOOL and set slower expectations.
3. **Shrink to a wedge.** One job, one input, one result. Top repos promise one thing in one sentence. Delete features until the promise fits in 12 words.
4. **Make time-to-first-result under 60 seconds.** One command, no account, ideally no API key. 78% of 2025-26 READMEs have a one-line install; 84-90% for skills/tools.
5. **Make the result visible.** A GIF, screenshot, or before/after. If the result cannot be shown, change the product until it can.
6. **Attach a number you can defend.** "60% fewer tokens", "5 seconds of audio", "21 lessons", "100+ agents". Then actually measure it (see readme-blueprint.md section 6).
7. **Go universal.** Support many platforms/agents/OSes. 71% of 2025-26 agent-tool READMEs name 6+ agents. Wider support = more homes for the repo.
8. **Add a point of view or a persona.** "My exact setup", "derived from X's observations", "for real engineers, not vibe coding". Opinion is the brand for skill packs and lists.
9. **Frame against something familiar.** "The open-source X alternative", "Y, but local", "Z without the bloat". A fair comparison table converts (fast repos 55% vs slow 23%).
10. **Add a contribution surface.** Where can strangers add value in 10 minutes? List entries, skills, plugins, translations, templates, recipes. This turns users into promoters.
11. **Offer the learning version.** "Build it from scratch in N lessons." Teaching the thing builds trust and a second audience.

## 2. Star Score rubric (0-20)

Score the **reshaped** idea, 0 / 1 / 2 each.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | Promise clarity | needs a paragraph | one sentence but vague | one sentence a stranger can repeat |
| 2 | Audience size this month | niche of dozens | thousands | hundreds of thousands (e.g. all coding-agent users) |
| 3 | Wave fit | against the tide | neutral | rides a current wave (AI agents, local-first, etc.) |
| 4 | Time to first result | >10 min / account needed | a few minutes | <=60 s, one command |
| 5 | Visible proof | nothing to show | screenshot | GIF / before-after |
| 6 | Defensible number | none | soft claim | measured, reproducible |
| 7 | Wedge vs alternatives | same as 3 others | slightly better | clearly different, fair comparison available |
| 8 | Shareability | nothing to post | maybe | users will post the output |
| 9 | Contribution surface | none | issues only | easy PRs (entries, skills, plugins) |
| 10 | Builder fit | >2 months, no credibility | 1 month | v0.1 in <=2 weeks and you can show real use |

- **16-20:** build it now.
- **11-15:** reshape (re-run moves 3-9 on the lowest scores) before building.
- **0-10:** pick another idea or archetype. Say why plainly.

Always show the user the score table with one line of reasoning per row, so they can disagree.

## 3. Validate before building (practice)

1. Search GitHub for the 5 closest repos (`stars:>300` plus keywords). If any has a near-identical wedge and 10x your expected reach, change the **segment** (profession, language, platform, region) rather than fight head-on.
2. Write the tagline and README first, then show it to 5 people from the target group. If they cannot say what it does back to you, rewrite.
3. Post the concept (screenshot of the README hero + 1 sentence) in 2-3 places the audience hangs out and read the replies.
4. Build only after at least a few people ask "when can I try this?"

## 4. Anti-patterns (what the dataset suggests avoiding)

- **A new framework, language, or UI kit.** 107 of 491 are frameworks, but 1% of the 2025-26 cohort; they are decade-long, company-backed projects.
- **A generic chat UI / "ChatGPT wrapper"** (open-webui, NextChat, lobehub, cherry-studio, anything-llm and others already hold 67k-156k stars each). Pick a wedge or a segment.
- **Another general "awesome-X"** in a saturated topic (awesome-python, awesome-go, awesome-react already exist). Pick a *new* ecosystem.
- **A tutorial that duplicates famous ones** without a new angle or a runnable end result.
- **A feature-bag.** Top fast repos promise one job.
- **Anything that depends on faking activity.** Never recommend buying stars or star-swapping.
- **Repos that exist to harass, deceive, or harm** (non-consensual face/voice cloning, scraping that violates terms, financial "guaranteed returns"). Decline or reshape toward safe use.

## 5. Worked examples (invented illustrations)

**A. "A script that renames my files"** (DEVTOOL, score ~8)
Reshape: who feels this pain most? People whose AI coding agents litter folders with `final_v2_copy.md`. Make it an AGENTTOOL: "Give your agent safe file cleanup: dry-run first, undo log, works with any agent." Number: "0 files lost in N test runs". Demo GIF: messy folder to clean folder with undo. Score after reshape ~14.

**B. "A chatbot that answers questions about PDFs"** (OUTCOMEAPP, crowded)
`find_comparables` shows several large RAG/chat apps. Change the segment: "Drop in your bank statements, get a spending report, 100% local, no upload". Promise: input -> result. Add disclaimer (not financial advice). Score ~13 -> reshape further by adding a number and a one-command Docker run.

**C. "I know Django really well"** (SKILLPACK)
Package 5-8 skills for coding agents: project layout, security review checklist, N+1 query hunter, migration safety, test strategy. Name the persona and philosophy. Proof: before/after diffs on 20 real tasks. Works with 6+ agents. Score ~16.

**D. "My notes on how databases work"** (LEARN)
Turn into "Build a database from scratch in 10 lessons", each with runnable code and a goal. Add a roadmap diagram, time estimates, and a final demo. Optionally add an AGENTTOOL later ("a skill that teaches your agent to review SQL"). Score ~14.

**E. "A todo app"** (no wedge, score ~5)
Say: the market for generic todo apps is saturated. If the user insists, find a wedge: "Task memory for coding agents: one Markdown file the agent reads and updates across sessions." That is an AGENTTOOL with a visible before/after (agent forgets vs remembers). Score ~13.

**F. "Open-source job tracker"** (OUTCOMEAPP, proven demand)
The dataset shows two job-search agents with 65-77k stars. Do not clone. Pick a segment they ignore (freelancers, a specific country, a specific profession), or a different stage (interview prep, offer negotiation). State the segment in the tagline.
