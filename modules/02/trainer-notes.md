# Module 2 — Trainer notes

## Suggested timing

Allow about 120 minutes, adjusting for account and repository setup:

- 10 min: explain the three customization types and confirm the Copilot session target.
- 25 min: Lab 2A Skill installation, use, and report review.
- 30 min: Lab 2B baseline, Hook inspection, enabled demonstration, and safety discussion.
- 40 min: Lab 2C issue lookup, MCP access review, and README diff review.
- 15 min: compare the three mechanisms and capture account/policy limitations.

If Hooks or MCP access needs troubleshooting, keep the stated fallback and preserve the time for discussion rather than changing organization policies during class.

## Before the session

1. Confirm participants completed Module 1 and have a clean Target project based on its starter. The target must be open in VS Code; the Training materials project is not the lab workspace.
2. Confirm each target is available in GitHub and the participant can read its Issues. Create an Issue from `issue-brief.md` in the repository used for Lab 2C; record the owner, repository, and issue number. If the class uses one shared Target repository, one issue is sufficient. If targets are separate repositories, seed the same issue in each target or direct learners to the prepared shared repository.
3. Check the actual VS Code build, Copilot Agent mode, and **Copilot** session target. Confirm Skills and MCP policy are enabled for the training accounts.
4. Check whether Hooks are enabled and available in the chosen Copilot harness. The VS Code Hooks experience is Preview, and provider implementations may have different support. Prepare a trainer demo in an enabled environment if learner accounts cannot run them.
5. Check the GitHub MCP remote endpoint and OAuth policies with the training organization. If remote MCP access is unavailable, prepare a live demo and let participants complete the README exercise from the visible Issue text.
6. Review any existing `.github/skills/`, `.github/hooks/`, or `.vscode/mcp.json` files in the Target. The exercise copies are ADD-only; prepare merge instructions for a collision rather than overwriting participant content.
7. Confirm participants understand that the MCP configuration is a shared server definition and should not contain personal credentials. The supplied configuration is read-only and limits toolsets to repository and issue operations.

## Facilitation notes

- Keep the Skill exercise read-only. Ask participants to identify whether the procedure influenced the report and whether the facts were supported by repository files.
- Skills may be available for automatic selection without being invoked. Compare automatic selection with explicit invocation only if the participant's client exposes it.
- In the Hook exercise, the `preToolUse` event reports before a call and `postToolUse` reports after a successful call. The script records only the tool name to standard error and returns `{}` on standard output. It makes no permission decision and cannot undo a completed action. Do not present either Hook as an enforcement control.
- Have learners inspect Hook source and output before enabling it. Avoid adding examples that auto-approve commands, evaluate untrusted shell text, or capture prompts and full tool arguments.
- In the MCP lab, ask participants to name the server, transport, toolsets, authentication path, and access boundaries before using it. The read-only header limits server tools but does not change the participant's GitHub permissions or prevent Copilot from editing local files.
- Keep the README change local. Do not ask participants to push or commit it as part of this module.

## Expected results

- **2A:** a structured report of the Task API contract, with routes and model validation supported by `app/main.py`.
- **2B:** a before/after pair is visible for one or more successful tool calls; the normal permission flow remains active. A denied or unsuccessful call may have no after-event.
- **2C:** Copilot retrieves the specified Issue from GitHub, then makes a focused local README change. Participants catch any claims that do not match the Issue or implementation.

## Current product references

Checked for this draft on 2026-11-02. Recheck before each course run because UI labels, preview status, server access, and configuration formats can change.

- [Use Agent Skills in VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills)
- [Configure agent Hooks in Visual Studio Code](https://code.visualstudio.com/docs/agent-customization/hooks)
- [MCP configuration reference for VS Code](https://code.visualstudio.com/docs/agents/reference/mcp-configuration)
- [Add MCP servers in VS Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers)
- [Remote GitHub MCP server configuration](https://github.com/github/github-mcp-server/blob/main/docs/remote-server.md)
- [Set up the GitHub MCP server in Copilot](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/customize-copilot/extend-copilot-with-tools-and-context/set-up-the-github-mcp-server)
