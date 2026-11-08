# Module 9 — Miro-to-Jira story delivery loop

Turn product and design evidence into approved Jira stories, then implement each live story on its own branch. Keep story generation separate from implementation, use the repository's delivery-lifecycle Skill and agent, and require distinct approval for Jira writes, commits, pushes, PRs, merges, and deployment.

## Materials

- `participant-guide.md` — end-to-end story workflow and checkpoints.
- `prompts.md` — prompts for Miro/Figma discovery, Jira story drafting, one-story implementation, and delivery review.
- `trainer-notes.md` — integration setup and facilitation.
- `story-workflow.md` — evidence log linking source frames, Jira stories, branches, tests, and delivery status.
- `target-overlays/skills/.github/skills/` — story-generation and delivery-lifecycle Skills to **ADD** alongside existing Skills; paths are preserved.
- `target-overlays/agents/.github/agents/` — a delivery-lifecycle agent profile to **ADD** alongside existing agents; path is preserved.
- `target-overlays/vscode/.vscode/mcp.json` — MCP configuration example to **MERGE** with the Target project's existing file; do not replace other servers.
- The Module 2 `.github/hooks/audit.json` Hook is reused to observe tool calls; Module 9 adds no new Hook because it would duplicate that observation.

Miro is a product evidence source; Jira is the story source of truth; GitHub is used for code/PRs. Figma MCP is configured for UI design evidence when the story includes a UI. The current Task API is UI-less, so learners must identify Figma as not applicable when no UI is in scope.

Module 10 covers end-to-end CI in GitHub Actions and live HTTP verification, with an optional separately approved Cloud Run staging deployment. Module 11 completes formal PR review and capstone presentation.
