# Sample Repo Blueprint (illustration)

> **Illustration only.** The idea is invented, the comparables are real rows from the dataset, and the Star Score is the honest result of the rubric. It is **not** a promise of stars. This is the kind of output the skill produces.

**User prompt:** "I made a Python tool that lists TODO comments in my codebase. Turn it into a repo that can get popular."

## Repo Blueprint: todo-scout

**Archetype:** AGENTTOOL. Plain "TODO listers" are a saturated utility; the data shows growth in add-ons that give AI coding agents better context.

**Promise (one sentence):** Give your coding agent a living map of every TODO, who wrote it, and how old it is.

**Who it is for / the pain:** Developers who run coding agents on big repos. The agent does not know which TODOs are stale, risky, or already tracked, so it guesses.

**Why now:** 81% of descriptions in repos created 2025-26 mention AI or agents (data). Context tools for agents are a proven category.

**Closest competitors and your wedge** (rows from `find_comparables.py`):

| Repo | Stars | Archetype | What it does | Your wedge |
|---|---|---|---|---|
| Graphify-Labs/graphify | 134k | AGENTTOOL | Turns a whole codebase into a queryable knowledge graph | Much broader. Todo-scout does one narrow job: *work debt* (TODOs, age, owner), in seconds |
| tt-a1i/archify | 88k | SKILLPACK | Turns a codebase into diagrams | Pictures, not task state |
| colbymchenry/codegraph | 75k | AGENTTOOL | Pre-indexed code knowledge graph for agents | Structure, not backlog |

Wedge: *"what is unfinished in this repo, and what should the agent do first?"* with git-blame age and owner.

**Name candidates:** metaphor: `scout`, `trailhead`, `tally`. Plain: `todo-map`, `agent-todos`, `todo-context`. Top pick: `todo-scout`. Checks to run: GitHub search, PyPI/npm, domain.

**Tagline options:**
1. Give your coding agent a living map of every TODO, owner and age in your repo.
2. Turn scattered TODO comments into a ranked task list your agent can act on.
3. Your repo's unfinished work, as one file your AI agent can read.

Pick: #1.

**Topics:** `ai-agents`, `claude-code`, `codex`, `mcp`, `todo`, `developer-tools`, `cli`, `code-quality`, `technical-debt`

**MVP scope for v0.1 (<= 2 weeks):** Will do: scan a repo, add git-blame age and owner, write `TODO_MAP.md`, one-line install, works with 3+ agents. Will NOT do: IDE plugins, dashboards, auto-fixing TODOs.

**Install design:** `pipx install todo-scout` then `todo-scout .`

**Proof plan:** run on 20 real open-source repos; measure how many tasks an agent completes correctly with vs without `TODO_MAP.md`. Publish the script and raw results. (No number is claimed until measured.)

**Demo plan:** 15-second recording: messy repo, one command, `TODO_MAP.md` appears, agent picks the oldest high-risk TODO.

**Star Score (0-20):**

| # | Criterion | Score | Why |
|---|---|---|---|
| 1 | Promise clarity | 1 | Clear once explained, "living map" is a little abstract |
| 2 | Audience size | 1 | Heavy agent users on large repos, not all developers |
| 3 | Wave fit | 2 | Built for coding agents |
| 4 | Time to first result | 2 | One command |
| 5 | Visible proof | 1 | A file and a recording, not yet a striking visual |
| 6 | Defensible number | 0 | Nothing measured yet |
| 7 | Wedge vs alternatives | 1 | Narrow wedge, overlaps with broader code-graph tools |
| 8 | Shareability | 1 | People may share the map, not obviously viral |
| 9 | Contribution surface | 1 | Language parsers and agent integrations |
| 10 | Builder fit | 2 | Already built; v0.1 is quick |
| | **Total** | **12 / 20** | Reshape band (11-15) |

**Honest odds and risks:** Reasonable first-100-stars candidate if launched well; reaching tens of thousands is unlikely without a strong measured result and wider appeal. Agent platforms may add similar features natively. Reshape before launch: run the measurement (criterion 6) and find a more visual demo (criterion 5). Those two moves alone could add 3-4 points.

**Next 7 days:**
- [ ] Run the 20-repo measurement and write down the result honestly
- [ ] Record the 15-second demo from a clean install
- [ ] Verify the install command on a clean machine
- [ ] Write README with `scaffold_repo.py`; aim for `audit_readme.py` 80+
- [ ] Prepare Show HN and X posts; find 3 awesome lists to submit to
