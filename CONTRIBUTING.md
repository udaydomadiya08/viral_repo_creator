# Contributing to GitHub Star Magnet

Thanks for helping! Small contributions are welcome.

## Quick ways to help
- **Fix a label.** Think a repo is in the wrong archetype? Open a *Data correction* issue with the repo name, the code you suggest, and one sentence of why. (Codes are in `skill/github-star-magnet/references/archetypes.md`.)
- **Add a worked example** to `examples/` (an idea, the Repo Blueprint, an honest Star Score).
- **Improve a script** (`skill/github-star-magnet/scripts/`) or add a test.
- **Translate** a guide from `skill/github-star-magnet/references/`.
- **Refresh the data** with a newer top-repos CSV (see below).
- **Report a bug or confusing instruction** with the issue templates.

## Ground rules
- One focused change per pull request. Explain the *why*.
- **Evidence over hype.** Every number in the docs must come from the dataset or be labelled as general practice. No invented benchmarks, quotes, or install commands.
- **No growth hacks that fake popularity** (bought stars, star swaps, bots). Pull requests that add them will be closed.
- Scripts use only the Python standard library. Keep it that way.
- Be kind. Assume good intent. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Local setup
```bash
git clone https://github.com/udaydomadiya08/viral_repo_creator.git
cd viral_repo_creator
python3 -m unittest discover -s tests -v
bash build.sh        # rebuilds dist/github-star-magnet.skill
```

## Refreshing the dataset
1. `python3 skill/github-star-magnet/scripts/refresh_dataset.py new_top_repos.csv --out enriched_new.csv`
2. Fill the empty `Archetype` column by reading each description (hand labels were much more accurate than keyword rules).
3. Replace `skill/github-star-magnet/references/top491_enriched.csv`.
4. Recompute the numbers in `references/data-findings.md` and the charts in `docs/assets/`.
5. Run the tests (they check that every repo has a valid archetype).
