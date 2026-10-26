# Launch and growth playbook

**Important:** unlike the other reference files, this one is mostly **general open-source practice**, not measured from the CSV. The CSV shows what top repos look like; it cannot show how they were promoted. Where a point comes from the data it is marked **[data]**. Do not present practice as measured fact.

## Contents
1. Set honest expectations
2. Diagnose a repo that is not getting stars
3. Pre-launch checklist (1-2 weeks)
4. Launch day
5. Weeks 1-4
6. Month 2 and beyond
7. Channels by archetype
8. Ethics: never fake it

---

## 1. Set honest expectations

- The 491 repos here are the extreme tail (50k-556k stars). Most excellent projects never get there, and that is normal. Healthy first milestones for a solo developer: **first 100 stars from real users, then 1,000**.
- Stars come from **reach x conversion**. Reach = how many people saw the repo. Conversion = share who starred. A great README fixes conversion only; if nobody sees the repo, nothing happens.
- Growth compounds. Plan a **portfolio**: ship 3 sharp projects over 6 months and apply what each launch teaches, rather than betting everything on one.
- **[data]** Winning repos are maintained continuously: 90% of 2025-26 repos had a push in the last 30 days.

## 2. Diagnose a repo that is not getting stars

Ask for (or check with the user) GitHub **Insights -> Traffic**: views, unique visitors, referrers; and stars count.

| Symptom | Likely problem | Fix |
|---|---|---|
| Almost no visitors | **Distribution** | Launch plan (sections 4-7); get listed in awesome lists and directories; post where the audience is |
| Visitors, but few stars (many visits, <1-2% star) | **Packaging** | Run `scripts/audit_readme.py`; fix tagline, hero, demo, install, comparison |
| Stars but no usage / issues | **Idea or quality** | Narrow the wedge; improve time-to-first-result; talk to users |
| Visitors from one post then flat | **One-shot launch** | Ship weekly updates, write follow-ups, keep a visible changelog |
| Everything weak | **Idea** | Re-run Star Score and archetype choice; consider a different segment |

Also check the repo page: About text set? Topics added? Social preview image uploaded? Website field filled? Release published? Many repos fail on these basics.

## 3. Pre-launch checklist (1-2 weeks)

1. README passes `audit_readme.py` with no placeholders and no broken images.
2. Install tested on a clean machine (macOS, Linux, Windows where relevant). Record the demo GIF **from that clean run**.
3. 3-10 real users tried it. Collect 2-3 honest quotes and one real before/after.
4. About description, topics (up to 20), social preview image, website, v0.1.0 release.
5. 5-10 `good first issue` items and a CONTRIBUTING file.
6. Prepare launch posts (section 4) and a one-paragraph "story" of why you built it.
7. If it is an AGENTTOOL / SKILLPACK: confirm it works with at least 3-6 different agents and name them.
8. Prepare to be online for the first 24-48 hours to answer comments fast.

## 4. Launch day

Write once, adapt per channel. Always include: the one-line tagline, the GIF or screenshot, the install command, and the link. Lead with the **problem and result**, not the tech stack.

- **Show HN** (if it is technical and works today): title shape "Show HN: Name - tagline". First comment: who you are, why you built it, what is rough, what feedback you want. Be honest and respond to every comment.
- **Reddit**: post in 1-2 *relevant* communities, read their self-promotion rules first, tell the story, not an ad. Do not cross-post the same text everywhere in one hour.
- **X / LinkedIn**: a short thread: problem -> GIF -> one command -> link. Tag tools you integrate with only when relevant. LinkedIn works well for developer audiences in India and for non-AI tools.
- **Dev blogs (dev.to, Hashnode, Medium, personal)**: "How I built X / what I learned / benchmarks". A technical story keeps getting found through search.
- **Product Hunt**: for apps with a UI and a visible result.
- **Communities**: Discord/Slack/Telegram groups around the ecosystem; follow rules; offer help first.
- **Chinese-language platforms** (V2EX, Juejin, Zhihu, WeChat accounts, Bilibili): **[data]** 27% of learning repos and several apps in the top list are Chinese-language; 50% of 2025-26 READMEs have translations. Add a Chinese README if the topic fits and you can verify quality.

## 5. Weeks 1-4

- Reply to every issue and comment within 24-48 hours. Responsiveness is a growth channel.
- Ship a visible improvement every week; publish release notes; thank contributors by name.
- Fold real user feedback into the README (quotes, new "Works with" entries, FAQ).
- Submit the repo (via PR) to relevant **awesome lists, directories and registries** in its niche. Each is a standing source of visitors. **[data]** 7 lists about AI-agent ecosystems were among the top repos created in 2025-26, which shows such lists matter.
- Write one deeper post per week on a real result, failure, or benchmark.
- Add integrations people ask for. Each integration is an audience that already lives somewhere (a "Works with X" mention, plus a PR to X's list).

## 6. Month 2 and beyond

- Add translations, a star-history chart, a docs site, sponsor links **after** there is traction (they are effects of growth **[data]**: star-history 43% and translations 50% of 2025-26 repos, but they correlate with growth more than they cause it).
- Run a small benchmark or comparison people can reproduce and link it.
- Record a 2-3 minute walkthrough video.
- Invite contributors to own an area (a platform, a language, a category).
- Revisit the Star Score; if the first project plateaus, apply the lessons to project #2 and cross-link them.

## 7. Channels by archetype

| Archetype | Best first channels |
|---|---|
| SKILLPACK | X thread with before/after, agent communities, skill/plugin directories, awesome lists for that agent, a short video |
| AGENTTOOL | Show HN, r/ClaudeAI-type and agent communities, benchmark post, MCP/tool registries, awesome lists |
| OUTCOMEAPP | Demo video/GIF on X and LinkedIn, Product Hunt, Reddit niche communities, YouTube short |
| LIST | Submit to ecosystem hubs; DM/PR the authors of listed projects; newsletter |
| LEARN | Blog series, YouTube/Bilibili, student communities, roadmap sites, Chinese-language platforms |
| DEVTOOL | Show HN, r/commandline-type communities, package managers (brew, npm, cargo, pip), Hacker Newsletter-style roundups |
| ALTERNATIVE | r/selfhosted-type communities, awesome-selfhosted, Product Hunt, comparison blog posts |

## 8. Ethics: never fake it

- **Never** buy stars, run star-swap groups, use bot accounts, or ask friends to mass-star. It violates GitHub's rules, can get repos hidden or accounts suspended, and destroys trust the moment someone notices.
- Disclose affiliation when you post your own project. Do not sock-puppet comments.
- Do not copy another repo's code or README; credit inspirations and respect licenses.
- Do not claim benchmarks you did not run.
- If asked to help with any of the above, decline briefly and offer the legitimate alternative (better packaging, honest launch).
