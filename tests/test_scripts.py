"""Tests for GitHub Star Magnet. Standard library only. Run: python3 -m unittest discover -s tests -v"""
import csv
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = os.path.join(ROOT, "skill", "github-star-magnet")
SCRIPTS = os.path.join(SKILL, "scripts")
DATA = os.path.join(SKILL, "references", "top491_enriched.csv")
CODES = {"SKILLPACK", "AGENTTOOL", "AGENTPRODUCT", "OUTCOMEAPP", "AIMODEL", "LEARN", "LIST",
         "ALTERNATIVE", "DEVTOOL", "FRAMEWORK", "SECNET", "CULTURE"}


def run(script, *args):
    return subprocess.run([sys.executable, os.path.join(SCRIPTS, script), *args],
                          capture_output=True, text=True, timeout=60)


class TestDataset(unittest.TestCase):
    def setUp(self):
        with open(DATA, encoding="utf-8") as f:
            self.rows = list(csv.DictReader(f))

    def test_row_count_and_unique_ranks(self):
        self.assertEqual(len(self.rows), 491)
        self.assertEqual(len({r["Rank"] for r in self.rows}), 491)

    def test_every_repo_has_valid_archetype(self):
        bad = [r["Repository"] for r in self.rows if r["Archetype"] not in CODES]
        self.assertEqual(bad, [])

    def test_stars_are_sorted_descending(self):
        stars = [int(r["Stars"]) for r in self.rows]
        self.assertEqual(stars, sorted(stars, reverse=True))


class TestSkillFile(unittest.TestCase):
    def test_frontmatter(self):
        with open(os.path.join(SKILL, "SKILL.md"), encoding="utf-8") as f:
            text = f.read()
        self.assertTrue(text.startswith("---\n"))
        head = text.split("---")[1]
        self.assertIn("name: github-star-magnet", head)
        self.assertIn("description:", head)

    def test_referenced_files_exist(self):
        for rel in ["references/data-findings.md", "references/archetypes.md",
                    "references/idea-transformations.md", "references/readme-blueprint.md",
                    "references/launch-playbook.md", "scripts/find_comparables.py",
                    "scripts/scaffold_repo.py", "scripts/audit_readme.py", "scripts/refresh_dataset.py"]:
            self.assertTrue(os.path.exists(os.path.join(SKILL, rel)), rel)


class TestFindComparables(unittest.TestCase):
    def test_archetype_table(self):
        p = run("find_comparables.py", "--archetypes")
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("SKILLPACK", p.stdout)

    def test_keyword_search(self):
        p = run("find_comparables.py", "agent memory", "--since", "2025", "--top", "3")
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("Query:", p.stdout)

    def test_no_match_message(self):
        p = run("find_comparables.py", "zzzqqqxxx")
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("No close match", p.stdout)


class TestScaffoldAndAudit(unittest.TestCase):
    def test_scaffold_creates_files_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "demo")
            p = run("scaffold_repo.py", "--name", "demo", "--tagline", "A test tagline for the demo project",
                    "--archetype", "SKILLPACK", "--author", "Tester", "--user", "tester", "--out", out)
            self.assertEqual(p.returncode, 0, p.stderr)
            for rel in ["README.md", "LICENSE", "CONTRIBUTING.md", ".github/PULL_REQUEST_TEMPLATE.md",
                        "skills/example-skill/SKILL.md", "docs/assets/README.md"]:
                self.assertTrue(os.path.exists(os.path.join(out, rel)), rel)
            with open(os.path.join(out, "README.md"), encoding="utf-8") as f:
                self.assertIn("demo", f.read())
            again = run("scaffold_repo.py", "--name", "demo", "--tagline", "x", "--out", out)
            self.assertNotEqual(again.returncode, 0)

    def test_audit_caps_unfinished_template(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "demo")
            run("scaffold_repo.py", "--name", "demo", "--tagline", "A test tagline for the demo project",
                "--archetype", "AGENTTOOL", "--out", out)
            p = run("audit_readme.py", os.path.join(out, "README.md"))
            self.assertEqual(p.returncode, 0, p.stderr)
            self.assertIn("capped", p.stdout)
            self.assertIn("unfilled", p.stdout)

    def test_audit_rewards_a_well_structured_readme(self):
        good = """<div align="center">
<img src="https://example.com/hero.png" width="600">

# Foo

**Cut your agent's token bill by 60% with one command.**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![CI](https://img.shields.io/badge/ci-passing-green.svg)](x)
[![Release](https://img.shields.io/badge/release-v1-blue.svg)](x)

<img src="https://example.com/demo.gif" width="600">
</div>

## Why Foo?
Agents waste tokens re-reading output. Foo trims it. Measured on 40 tasks: 60% fewer tokens.

| | Foo | Raw |
|---|---|---|
| Setup | 1 command | none |

Compared with raw output, Foo keeps answers identical in our tests.

## Install
```bash
npx foo-cli
```

## Quick start
Run `foo run`. Works with Claude Code, Codex, Cursor, Gemini CLI on macOS, Linux, Windows.

""" + ("More detail about how it works and how it was measured. " * 80) + """

## Contributing
PRs welcome. Join us on discord.gg/example

## License
MIT
"""
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "README.md")
            with open(path, "w", encoding="utf-8") as f:
                f.write(good)
            p = run("audit_readme.py", path)
            self.assertEqual(p.returncode, 0, p.stderr)
            score = int(p.stdout.split("SCORE:")[1].split("/")[0])
            self.assertGreaterEqual(score, 80, p.stdout)


if __name__ == "__main__":
    unittest.main()
