# Module 6 — Plan, test, and implement incrementally

Implement the first Jira story from the reviewed requirements, specification, and task list. Work in small test/code steps, review each diff against acceptance criteria, update story/task state from actual evidence, and carry a concise handoff into a new Copilot session. Later stories follow the same one-at-a-time loop in Modules 7–9.

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

Reuse Module 3's test-feedback Skill and Module 2's tool-observation Hook. Module 6 works from the reviewed first story; Modules 5 and 9 establish the Jira story source of truth and integrations. Module 6 adds an optional session-start Hook that reports current story/task status from the handoff note.
