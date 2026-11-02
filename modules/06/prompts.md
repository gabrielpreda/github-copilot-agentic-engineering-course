# Module 6 — Prompt cards

Use these prompts in the Target project. Replace bracketed fields with IDs from your approved plan. Review every diff and test result.

## 1. Recommend an implementation order

```text
Use the incremental-implementation Skill. Read the approved requirements, feature specification, task list, relevant implementation, and tests. Recommend a sensible task order based on dependencies and verification. For each task, state its acceptance criteria and planned evidence. Do not implement anything or add scope. Identify any unclear prerequisite or mismatch among the artifacts.
```

## 2. Add a test for one task only

```text
Use incremental-implementation and test-feedback. Work only on task [T-ID], which addresses [AC-ID]. Read the task plan and current code/tests. Add or update only the focused test(s) that express the specified behavior. Do not edit application code, dependencies, requirements, or unrelated tests. Explain the expected result against the current implementation and show the diff before running the test.
```

## 3. Diagnose the test result

```text
For task [T-ID] and criterion [AC-ID], inspect this exact test output: [paste output]. Explain the assertion, expected result, actual result, and whether the failure demonstrates the missing specified behavior or a test/setup issue. Do not edit files yet. Do not weaken or remove the test to make it pass.
```

## 4. Implement one task and verify it

```text
Use incremental-implementation. Implement only task [T-ID] for acceptance criterion(s) [AC-ID], using the approved specification and the reviewed test. Preserve the explicit compatibility requirements and non-goals. Do not change other tasks or add behavior not in the spec. Show the proposed code diff and explain how each change addresses the criterion. After I review it, run the focused test and relevant regression tests, report exact commands/results, and update the task status only from that evidence.
```

## 5. Review and record a task

```text
Review the current diff for task [T-ID] against its acceptance criterion(s), specification, existing API behavior, and test results. Do not make additional edits. Report scope, compatibility, and regression concerns; list tests actually run and results; identify any planned check not run. Recommend whether the task is complete, in progress, or blocked and why. Do not mark it complete without evidence.
```

## 6. Write the handoff before changing sessions

```text
Use incremental-implementation. Update only docs/handoffs/task-priority.md from the current repository state and observed test output. Record requirements/spec status, current task and criteria, task status, decisions, files changed, exact tests and results, unresolved questions, blockers, and next task. Keep it concise. Do not claim unverified work is complete and do not change application code or tests.
```

## 7. Begin a fresh session from the handoff

```text
Use incremental-implementation. Before proposing edits, read docs/requirements/task-priority.md, docs/specs/task-priority.md, docs/tasks/task-priority.md, docs/handoffs/task-priority.md, the current git diff, relevant source/tests, and the actual latest test state if available. Summarize the current task, completed and remaining work, acceptance criteria, evidence, decisions, blockers, and next step. Flag anything the handoff claims that the repository does not support. Do not edit files until I confirm the next task.
```

## 8. Optional priority-ordering task

```text
Only if the approved requirements, specification, and task list include priority-based list ordering: use incremental-implementation and test-feedback to work only on [T-ID]/[AC-ID]. First add a focused ordering test and show me the test diff. Do not change code yet. Confirm the approved tie behavior from the specification; if it is unresolved, stop and ask the trainer rather than choosing one.
```
