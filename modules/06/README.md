# Module 6 — Plan, test, and implement incrementally

Implement the Task Priority feature from the reviewed requirements, specification, and task list. Work in small test/code steps, review each diff against acceptance criteria, update task state from actual evidence, and carry a concise handoff into a new Copilot session.

## Materials

- `participant-guide.md` — implementation sequence, verification, session handoff, and completion criteria.
- `prompts.md` — prompts for selecting a task, writing tests, implementing, reviewing, and handing off.
- `trainer-notes.md` — setup, expected outcomes, branching for approved scope, and facilitation notes.
- `target-overlays/skill/` — reusable incremental-implementation Skill to **ADD** alongside existing Skills.
- `target-overlays/handoff/` — task-state template to **ADD** at `docs/handoffs/task-priority.md`.
- `target-overlays/hook/` — optional session-start Hook to **ADD** alongside Module 4's requirements-context Hook.

## Progression and complexity

The Module 1 starter is deliberately small, but this feature exercises a real change across request validation, backward-compatible defaults, response data, automated tests, task traceability, and session handoff. Keep the existing in-memory service and endpoints so learners can focus on change control rather than adding infrastructure prematurely.

The core track implements only the behavior in the approved Module 4/5 artifacts. Priority ordering is an advanced extension only when the Module 5 scope-change exercise resulted in an approved requirement and task. This keeps the learning project growing while preserving scope traceability.

Reuse Module 3's test-feedback Skill and Module 2's GitHub MCP and tool-observation Hook. Module 6 adds an optional session-start Hook that reports the current task/status from the handoff note, complementing Module 4's requirements reminder. No new MCP server is needed; the existing GitHub connection is used only when remote Issue context is relevant.
