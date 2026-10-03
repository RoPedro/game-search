# AGENTS.md

> Instructions for AI agents (Claude, Codex, Copilot, etc.) working in this repository.

---

## Project Overview

GameSearch is a software that is traditionally ran as a Discord Bot. It's main functionality is to search for game data using IGDB API, and Nextcord Python library for Discord communication. The main constraint is doing everything only with API requests and no local storage or database (Unless specified).

---

## Skills
Instructions for repetitive tasks live at /agents/skills

- [pr-descriptor](/agents/skills/pr-descriptor/skill.md) - For writing Pull Requests

---

## Repository Structure

```
/config - Handles log setup and environment variables;
/core - Handles small utilitarians like date conversion, IGDB Auth, app greeter;
/docs - [WIP] For now, used for taking notes on edge cases (gotchas.md);
/integrations - Basic functionality for third party services like IGDB and isThereAnyDeal;
/src - Main app logic, models, controllers, i18n;
/tests - Standard test suite, includes /factories for reusable data
```

---

## Development Setup

```bash
# Install dependencies
pip install -r requirements.txt
# Run locally
python3 main.py
```

---

## Code Style & Conventions

- **Language/runtime:** Refer to `pyproject.toml`
- **Formatter:** Prettier, Black
- **Linter:** Ruff 

---

## Testing 
```bash
# Run all tests
pytest
```
- Aim for coverage on new logic; don't break existing tests

---

## Making Changes

1. Keep PRs focused — one concern per branch
2. Write or update tests for changed code
3. Update relevant docs if behavior changes
4. Do **not** commit secrets, build artifacts, or generated files

---

## Off-Limits
- Do not run destructive commands (`DROP`, `rm -rf`, etc.) without explicit instruction
- Do not touch .env, investigation is allowed if relevant to the context, but it's read-only for agents, unless specified by user.
- Never run arbitrary `pip upgrade` etc, already used dependencies are frozen by design unless specified.
- Writing on requirements.txt is allowed if relevant, but for features only available in updated libraries, ask for permission first.

---

## Relevant Docs

- [IGDB API Reference](https://api-docs.igdb.com/)
- [isThereAnyDeal API Reference](https://docs.isthereanydeal.com/)
- [Nextcord Reference](https://docs.nextcord.dev/en/stable/index.html)
- [GameSearch Repository](https://github.com/RoPedro/GameSearch)
<!-- Add more as needed -->

## Pull request description framework

When asked to generate a PR description:
1. Read the changes of current branch;
2. Link commit hashes to changes description when feasible;
3. Use this formatting;
4. Try opening a PR using Github CLI, if it doesn't exist/Not authenticated/Other errors, skip gracefully and tell the user why it skipped;
5. *Never* try merging anything, only open.

## Features:
- Lorem ipsum
- sit amet

## Fix:
- consectur adpiscing
- elit, sed

## Chore:
- Version bump x.y.z
- README.md reflects K
