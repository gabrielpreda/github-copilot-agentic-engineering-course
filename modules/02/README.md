# Module 2 — Skills, Hooks, and MCP tools

Module 2 introduces three repository customizations through separate, sequential labs. Participants use the Module 1 Target project and add each customization only when its lab begins.

## Materials

- `participant-guide.md` — setup, lab steps, verification, and completion criteria.
- `prompts.md` — exact prompts for the exercises.
- `trainer-notes.md` — setup checklist, timing, and fallback plans.
- `issue-brief.md` — issue text to seed in the participant's GitHub Target repository before Lab 2C.
- `target-overlays/` — files copied into the Target project. Paths under each overlay preserve their destination paths.

## Target project progression

1. **2A Skills:** **ADD** `.github/skills/api-contract-review/SKILL.md`.
2. **2B Hooks:** **ADD** `.github/hooks/audit.json` and `.github/hooks/audit_tool_use.py` for before/after observation of successful tool calls.
3. **2C MCP:** **ADD** `.vscode/mcp.json`, or **MERGE** its `github` server entry into an existing workspace MCP configuration.

No application source file is changed by the supplied overlays. The MCP issue exercise may ask Copilot to update the Target project's `README.md`; participants review and save that change locally as a separate exercise result.

## Compatibility note

These materials target GitHub Copilot Agent mode in Visual Studio Code. Skills, hooks, and MCP support varies by Copilot session target, VS Code version, and organization policy. The guide identifies checks and trainer-led fallbacks. Review the linked vendor documentation before a future course run because these features and configuration formats can change.
