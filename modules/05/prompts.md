# Module 5 — Prompt cards

Use these prompts in the Target project. Replace bracketed text with actual criterion IDs or trainer-provided scope change. Review diffs before accepting them.

## 1. Draft the concise feature specification

```text
Use the spec-and-task-planning Skill. Read docs/requirements/task-priority.md and the relevant current API implementation/tests. If available, use api-contract-review to summarize current behavior. Do not implement anything.

If acceptance criteria have no stable IDs, first propose IDs such as AC-1 in docs/requirements/task-priority.md, preserving its wording and content. Then draft or update only docs/specs/task-priority.md. Keep it concise and behavior-focused: user outcome, in-scope behavior, constraints, exclusions, assumptions/open questions, and planned verification intent. Link each behavior to the source acceptance criterion ID. Preserve the requirements' approval status. Do not prescribe classes, functions, file layout, or algorithms unless an evidenced project constraint requires them. Identify any contradiction or unresolved decision instead of silently resolving it. Show all diffs.
```

## 2. Decompose into small, verifiable tasks

```text
Use the spec-and-task-planning Skill. Read the requirements and feature specification, then update only docs/tasks/task-priority.md.

Create a small list of stable-ID tasks. Each task must state a reviewable result, link to acceptance criterion IDs, and name planned verification evidence (for example, a focused automated test or manual check). Do not claim planned tests already exist. Keep tasks small and implementation-independent unless the spec establishes a technical constraint. Include dependencies only where necessary. Fill in the criterion-to-task traceability table and identify uncovered criteria or unrelated tasks. Do not edit application source or test files. Show the diff and explain any open decision.
```

## 3. Apply a scope change

```text
Use the spec-and-task-planning Skill. The requester/trainer has supplied this scope change: [paste the change and identify whether it is approved or proposed]. Do not implement it.

If the change is approved, update docs/requirements/task-priority.md first with the confirmed decision and affected acceptance criterion(s). If it is only proposed, do not alter approved requirements; record the proposal and potential impact in the spec and task list as pending while preserving the approved baseline. Update docs/specs/task-priority.md and docs/tasks/task-priority.md together. Record the change, source, and approval status. Identify affected acceptance criteria, tasks, and planned verification. Preserve stable IDs for unaffected work; mark removed or superseded work clearly. Show all diffs and any required owner decision.
```

## 4. Audit traceability and detail

```text
Review docs/requirements/task-priority.md, docs/specs/task-priority.md, and docs/tasks/task-priority.md without editing. Return:
1. Each acceptance criterion and its linked task(s) and planned verification.
2. Any criterion without coverage or any task without a justified link.
3. Any conflict in status, assumptions, or scope-change records.
4. Any specification detail that prescribes implementation without a stated constraint.
5. Any planned test described as if it already exists.
Recommend the smallest corrections. Do not change files or implement work.
```

## 5. Handoff into a later session

```text
Read the requirements, feature specification, and task list. Summarize their approval status, task IDs and order, acceptance criteria covered by each task, planned verification, scope changes, and open decisions. Do not start implementation until I select a task. Do not treat a Draft as approval.
```
