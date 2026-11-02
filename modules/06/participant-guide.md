# Module 6 — Plan, test, and implement incrementally

## Purpose

Implement the Task Priority feature through small, verifiable steps. Keep tests and code connected to the approved acceptance criteria, update task notes from actual results, and carry essential state into a fresh Copilot session.

## Learning outcomes

By the end of this lab, you can:

- Choose a sensible implementation order from a specification and task list.
- Add or update tests alongside a focused code change.
- Use test results and code review to decide whether a task meets its acceptance criteria.
- Keep one Copilot session focused on one implementation task and decide when to start a new one.
- Record task state, decisions, changed files, and verification so another session can continue reliably.

## Before you begin

- Continue in the Target project from Modules 1–5. Preserve local work and all earlier Skills, Hooks, and MCP configuration.
- Confirm `docs/requirements/task-priority.md`, `docs/specs/task-priority.md`, and `docs/tasks/task-priority.md` exist and have consistent status and scope.
- If the approved requirements or task plan are missing, stop and use the trainer's prepared versions. Do not infer product approval from a generated spec.
- Check that the Module 3 pytest setup and tests are present and that the current Target project has a known baseline. If the baseline fails, record and resolve the discrepancy with the trainer before layering changes on it.
- Copy `.github/skills/incremental-implementation/SKILL.md` from `target-overlays/skill/` to the same path in the Target project (**ADD**). Keep the existing Skills.
- If absent, copy `target-overlays/handoff/docs/handoffs/task-priority.md` to `docs/handoffs/task-priority.md` (**ADD**). If it exists, preserve and update it rather than replacing it.
- Optionally copy `target-overlays/hook/.github/hooks/implementation-context.json` and `load_implementation_context.py` into the corresponding Target project paths (**ADD**). Keep Module 2 and Module 4 Hook files. Check hook format and runtime compatibility first.
- Do not open the Training materials project as the application workspace.

## Lab A — Select and sequence the work

1. Read the spec and task list. Check that each task links to an acceptance criterion and planned evidence.
2. Use the first prompt in `prompts.md` to identify prerequisites and recommend an implementation order. Review the recommendation against the plan; do not accept extra scope.
3. Select one task to start. Record its task ID and criterion IDs in your working notes.
4. Reuse the Module 3 `test-feedback` Skill, Module 2 GitHub MCP (if issue context is needed), and existing Hooks where available. The MCP server is for context retrieval, not for implementing or changing Issues.

## Lab B — Add a focused test for the current task

1. Start a Copilot session focused on the selected task. Use the test-first prompt in `prompts.md` and invoke the `test-feedback` Skill.
2. Ask Copilot to add or update only tests for the selected criterion. Do not change application code in this step.
3. Inspect the test diff. It should express observable behavior from the spec and preserve existing tests.
4. Run the focused test and record the exact command and result. For a new behavior, the expected initial failure should show the missing behavior. If it unexpectedly passes or fails for an unrelated reason, investigate before continuing.
5. Observe the Module 2 tool Hook if enabled. It can make tool calls visible, but the test output is the evidence about behavior.

## Lab C — Implement and verify one task

1. Continue in the focused session with the implementation prompt. Ask Copilot to change only what is needed for this task and acceptance criterion.
2. Review the code diff before accepting it. Check request and response compatibility, default behavior, validation, and the explicit non-goals in the spec.
3. Run the focused test again. Read the result and update the task state only after the result is understood.
4. Run the relevant regression suite when the task is complete. Record exact commands and results; do not state that tests passed if they were not run.
5. Inspect the full diff and update the task list with status and evidence. Do not mark a task complete based only on Copilot's summary.

## Lab D — Prepare a handoff and continue in a fresh session

1. Before ending the first session, update `docs/handoffs/task-priority.md` from the repository state. Record the current task, criteria, decisions, files changed, exact checks/results, blockers, and next task.
2. If the current task is complete, choose the next task from the plan. If it is incomplete, state what remains instead of marking it complete.
3. Start a new Copilot session in the same Target project. Do not paste the entire old conversation.
4. Use the new-session prompt in `prompts.md`. Ask the new session to read the requirements, spec, task list, handoff, current diff, and test state before proposing changes.
5. Check whether the summary matches the files and command output. Correct it if it relies on missing or stale information.
6. Continue the next task only after reviewing the new session's understanding and confirming the task.

If the Module 6 session-start Hook is enabled, compare its reminder with the handoff note. It reports only the current task and status and asks the agent to verify repository state; it cannot prove that the task is complete.

## Optional advanced track — priority ordering

Use this track only if Module 5 recorded an **approved** scope change requiring high-priority tasks to appear before other tasks in `GET /tasks`, and the spec/task list include corresponding criteria and tests.

1. Verify the approved criterion and ordering/tie behavior are clear. If tie behavior is unresolved, ask the trainer; do not invent it.
2. Add an ordering-focused test as its own task step before changing the list endpoint.
3. Implement only the specified ordering behavior. Preserve task creation semantics and stable behavior for equal priorities as required by the approved spec.
4. Run focused and regression tests, then update the task/handoff evidence.

If the Module 5 change remained a proposal, skip this track. Do not implement a proposed requirement.

## Completion criteria

- Implementation order follows the task list and respects dependencies.
- Each code change has focused test evidence or a clearly recorded reason why a check was not run.
- Each task is linked to acceptance criteria and updated from observed results.
- The complete relevant test suite passes, or remaining failures are accurately recorded and explained.
- The implementation preserves explicitly required compatibility and non-goals.
- A fresh Copilot session can identify current state and next step from repository artifacts without relying on the old transcript.
- The handoff reflects actual files, decisions, and test results.

## Handoff to Module 7

Keep the requirements, specification, task list, tests, implementation, and handoff in the Target project. Module 7 will use a branch and build a capstone vertical slice. Carry forward verified evidence and unresolved decisions; do not treat an incomplete task as done.
