# Module 7 — Capstone part I: build a feature

## Purpose

Use the complete workflow from Modules 1–6 on a substantial feature: understand the request, inspect the current project, clarify behavior, create traceable requirements and tasks, then implement a focused vertical slice on a branch.

## Learning outcomes

By the end of this lab, you can:

- Select and scope a significant feature that fits the time and project.
- Work from a request through acceptance criteria, a concise spec, and a task plan.
- Create and use a dedicated branch while preserving unrelated work.
- Implement a vertical slice with tests and API behavior connected to acceptance criteria.
- Prepare a clear review checkpoint for continuation in Module 8 and Capstone part II.

## Before you begin

- Continue with the shared Target project from Modules 1–6. Preserve local changes.
- Confirm the current priority feature and its tests are in a known state. Record any participant-specific implementation differences.
- Keep earlier Skills, Hooks, and MCP configuration. Add the capstone Skill from `target-overlays/skill/.github/skills/capstone-vertical-slice/SKILL.md` as **ADD** alongside them.
- Review `feature-catalog.md` and choose one track with your trainer: deadlines, labels, or dependency-aware completion. The combined Team Planning track requires trainer approval.
- Copy the four templates from `target-overlays/templates/` into the Target project as **ADD** files, using these paths:
  - `docs/requirements/capstone-<track>.md`
  - `docs/specs/capstone-<track>.md`
  - `docs/tasks/capstone-<track>.md`
  - `docs/handoffs/capstone-<track>.md`
  Replace `<track>` with your selected track name (for example, `deadlines`). If a destination already exists, preserve and merge its content.
- Confirm the GitHub MCP server can read Issues in the Target repository, if available. The trainer will provide the selected feature Issue; do not create a duplicate.
- Save or commit existing work before creating the capstone branch. Do not switch branches with uncommitted work you cannot safely carry.

## Lab A — Create the capstone branch and inspect the project

1. Check `git status` and the current branch. Preserve or safely save participant changes.
2. Create a feature branch using a name from `feature-catalog.md`, for example:

   ```bash
   git switch -c capstone/deadlines
   ```

   Use a different suffix for your selected track. If the branch already exists, switch to it only after checking its contents and working tree.
3. Run the existing test suite and save the result. If it fails, resolve or document the baseline before capstone work.
4. Use the `capstone-vertical-slice` Skill and the first prompt in `prompts.md` to inspect current routes, data models, tests, requirements, and prior implementation notes.
5. If available, use GitHub MCP to search for related issues and read the trainer-prepared feature Issue. Observe the Module 2 Hook output. If MCP is unavailable, use the trainer brief and record the fallback.

## Lab B — Refine the selected feature request

1. Read your selected initial request in `feature-catalog.md` or the trainer's Issue. Do not read the trainer clarification card yet.
2. Use the clarification prompt to list the most consequential open questions. Ask the trainer only questions your group believes matter to scope or observable behavior.
3. Record confirmed facts, assumptions, open questions, non-goals, and approval status in `docs/requirements/capstone-<track>.md` using the template. If the path exists, preserve and merge participant content rather than replacing it.
4. Have the trainer provide the matching answer card. Update acceptance criteria with stable IDs and mark any unanswered decisions explicitly.
5. If the scope is too large, propose a vertical slice that still delivers a useful end-to-end outcome. Record deferred capabilities as non-goals or future work, not as silently dropped criteria.

## Lab C — Create the specification and task plan

1. Create `docs/specs/capstone-<track>.md` and `docs/tasks/capstone-<track>.md`, or preserve and update existing files at those paths.
2. Use the planning prompt in `prompts.md`. Keep the spec focused on observable behavior, constraints, compatibility, and exclusions.
3. Divide work into small tasks with stable IDs, linked acceptance criteria, planned tests, dependencies, and clear review outcomes.
4. Check traceability both ways. Every criterion should have a task and verification plan, or an explicit deferral; every task should support an approved criterion or necessary quality constraint.
5. Do not prescribe implementation details unless project evidence or an approved constraint requires them.

## Lab D — Implement one vertical slice

1. Select the first task that creates a useful end-to-end part of the feature. State the task and criteria in the Copilot session.
2. Use the test-first prompt to add focused tests for the slice. Review the tests and run them before changing application code where the task plan allows.
3. Use the implementation prompt to make the smallest coherent change that fulfills the test and criterion. Keep the diff on the feature branch and avoid unrelated refactoring.
4. Run focused tests, then relevant regression tests. Check the API response and error behavior, including edge cases named in the spec.
5. Update the task list and handoff with exact test commands/results, changed files, and remaining work.
6. Continue only while time allows and each step remains reviewable. It is acceptable to leave later tasks in progress or not started if the vertical slice is complete and honestly documented.

## Lab E — Prepare the review checkpoint

1. Review the branch diff against requirements, spec, task list, and tests.
2. Confirm there are no unrelated changes, accidental files, secrets, or unsupported scope additions.
3. Record implemented criteria, deferred criteria, tests run, known limitations, and the next review question in `docs/handoffs/capstone-<track>.md`.
4. Do not merge the branch. Module 8 will examine the work and its safeguards; later capstone work will complete the path to a verified review.

## Completion criteria

- Work is on a dedicated capstone branch with unrelated changes preserved.
- A significant feature request was refined into approved or clearly draft requirements.
- The spec and task plan are linked to acceptance criteria and verification.
- At least one useful vertical slice is implemented with corresponding tests.
- Relevant test results and code diffs were reviewed, not inferred from Copilot's summary.
- Scope, deferred work, and remaining questions are recorded for review.

## Capstone tracks

- **Deadlines:** optional due dates and useful due/overdue list views.
- **Labels:** multi-label task organization and filtered list views.
- **Dependencies:** prerequisite links and dependency-aware completion; advanced track.
- **Team Planning:** deadlines plus labels, only with trainer approval and a narrowed, reviewable plan.

See `trainer-notes.md` for clarification cards and reference acceptance criteria.
