---
name: pr-descriptor 
description: Pull request description generator skill for AI Agents. Triggered by prompts like "Prepare this branch for a PR...", "Start a PR for this branch...", "Open a Pull Request for the current branch", or aliases like "pr-open", "start-pr". If the prompt is not descriptive enough but it looks like it matches this skill, ask for confirmation, the reason of the confirmation is to avoid wasting tokens.
---
In case of ambiguous user prompt that matches this skill, ask: "It sounds like you want to start a Pull Request, proceed?"

## Start here
1. Read changes: `git log <desired_args>`;
2. Use the `/.github/PULL_REQUEST_TEMPLATE.md` for writing, and the `/.github/PULL_REQUEST_EXAMPLE.md` to guide your language and organization. The example file reflects mock changes, it's almost never related to what is being pulled.
3. Link commit hashes to changes description when feasible;
4. Try opening a PR using Github CLI, if it doesn't exist/Not authenticated/Other errors, skip gracefully and tell the user why it skipped;
5. *Never* try merging anything to main/master, only open.

## In case step 4 fails
Save the full description /ai-tmp/pr-desc_{yearmonthday}.md