# AGENTS.md

> Instructions for AI agents (Claude, Codex, Copilot, etc.) working in this repository.

---

## Project Overview

GameSearch is a software that is traditionally ran as a Discord Bot. It's main functionality is to search for game data using IGDB API, and Nextcord Python library for Discord communication. The main constraint is doing everything only with API requests and no local storage or database (Unless specified).

---

## Repository Structure

```
WIP
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

- **Language/runtime:** Refer to `pyproject.toml
- **Formatter:** Prettier, Black
- **Linter:** <!-- e.g. ESLint, Ruff --> WIP

---

## Testing (WIP)
```bash
# Run all tests
<test command>

# Run a single test
<test command for one file>
```

- Tests live in `tests/` 
- Aim for coverage on new logic; don't break existing tests

---

## Making Changes

1. Keep PRs focused — one concern per branch
2. Write or update tests for changed code
3. Update relevant docs if behavior changes
4. Do **not** commit secrets, build artifacts, or generated files

---

## Off-Limits

<!-- List files, dirs, or actions agents should never touch. -->
- Do not run destructive commands (`DROP`, `rm -rf`, etc.) without explicit instruction
- Do not touch .env, investigation is allowed if relevant to the context, but it's read-only for agents.
- Never run arbitrary `pip upgrade` etc, already used dependencies are frozen by design unless specified.
- Writing on requirements.txt is allowed if relevant, but for features only available in updated libraries, ask for permission first.

---

## Relevant Docs

- [API Reference](https://api-docs.igdb.com/)
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