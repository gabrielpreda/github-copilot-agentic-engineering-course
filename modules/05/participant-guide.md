# Module 5 — Lightweight Spec-Driven Development

## Purpose

Turn reviewed requirements into a short specification and a small task list that can guide later implementation. Keep every task connected to the behavior it serves and the evidence that will verify it, while leaving coding choices open where they are not requirements.

## Learning outcomes

By the end of this lab, you can:

- Explain how a specification differs from a request, a requirements worksheet, and an implementation design.
- Write a concise behavior-focused feature specification from reviewed requirements.
- Divide the feature into small tasks with clear results and verification evidence.
- Trace acceptance criteria to tasks and tests or other checks.
- Update the spec and task list together when scope changes.

## Before you begin

- Continue in the same Target project used for Modules 1–4. Keep local work and all existing customizations.
- Bring forward `docs/requirements/task-priority.md` from Module 4. Check its status and open questions before planning.
- If Module 4 was not completed, use the trainer-approved requirements worksheet. Do not treat an unapproved draft as approved.
- Do not open the Training materials project as the application workspace.
- No application code is changed in this module. Module 6 uses the tasks for implementation.

## Lab A — Add the planning Skill and templates

1. Check whether `.github/skills/spec-and-task-planning/SKILL.md` exists. If not, copy `target-overlays/skill/.github/skills/spec-and-task-planning/SKILL.md` to that path (**ADD**). Keep the Module 2 API-review Skill and Modules 3–4 Skills.
2. Check whether `docs/specs/task-priority.md` and `docs/tasks/task-priority.md` exist. If absent, copy the matching files from `target-overlays/templates/` into the Target project (**ADD** both). Create parent directories as needed.
3. If a destination exists, preserve it and merge the relevant template sections by hand. Do not replace prior requirements or planning work.
4. Read the new Skill and templates. The Skill guides a general process; it does not determine the feature's behavior or prescribe a software architecture.

## Lab B — Create a one-page specification

1. Review the Module 4 requirements worksheet. Confirm the source of each acceptance criterion and whether it is approved. If behavior remains unresolved, ask the trainer or keep the spec marked Draft with the open question visible.
2. Give each acceptance criterion a stable ID (`AC-1`, `AC-2`, and so on) in the requirements worksheet, preserving its wording and order. If you edit the worksheet, inspect the diff and **MERGE** the IDs without replacing its content.
3. Use the first prompt in `prompts.md` to ask Copilot to draft `docs/specs/task-priority.md` from the requirements and current API contract.
4. Keep the specification focused on user outcome, observable behavior, constraints, exclusions, and verification intent. Link behavior to criteria IDs.
5. Remove coding prescriptions that are not needed to express the required behavior. Keep real compatibility or project constraints.
6. Review the diff. The task list may still be blank at this point; do not change application code.

## Lab C — Divide the feature into verifiable tasks

1. Ask Copilot to propose a small task list in `docs/tasks/task-priority.md` using the second prompt in `prompts.md`.
2. Give each task a stable ID, a result a reviewer can recognize, the criterion IDs it supports, and a planned verification method.
3. Check traceability in both directions: every criterion has a task and verification evidence (or an explicit deferral); every task supports a criterion or an agreed enabling constraint.
4. Keep tasks implementation-independent where possible. A task may describe a test-first step, but do not specify internals unless the project requires them.
5. Ask Copilot to revise until the list is small enough to complete in short, reviewable steps. Avoid splitting trivial work into ceremonial tasks.

## Lab D — Practice a scope change

The trainer will introduce a small change to the requirements. Use the scope-change prompt in `prompts.md`.

1. Identify the source and whether the change is approved or still a proposal.
2. If approved, update the requirements worksheet first: record the decision/source, revise or add the affected acceptance criterion, and preserve its approval/status information. If it is only proposed, do not alter approved requirements; record the proposed impact separately.
3. Update the specification to reflect the approved requirement change, or label the proposed change as pending. Record the source and affected criteria.
4. Update only the affected tasks and verification evidence; keep unaffected IDs stable.
5. Update traceability tables and mark removed or superseded work explicitly.
6. If the change is not approved, preserve the existing approved baseline and show the potential impact as pending; do not present the proposal as settled scope.

## Lab E — Review the plan and check the handoff

1. Use the final prompt in `prompts.md` to audit traceability and unnecessary detail.
2. Review the requirements, spec, and task list side by side. Check that assumptions and status agree.
3. Inspect the full diff. Confirm only planning files changed and no Issue, board, application source, or test file was modified.
4. Prepare to hand the spec and tasks to Module 6. Keep unresolved decisions visible.

## Completion criteria

- The specification is concise and states the required behavior and constraints without unnecessary implementation prescriptions.
- The specification links each behavior to a requirement or acceptance criterion.
- Tasks have stable IDs, clear verifiable outcomes, criterion links, and planned verification evidence.
- Every criterion is covered by a task and a verification method or explicitly deferred.
- An approved scope change is reflected in the requirements, specification, and task list, with affected verification updated; an unapproved proposal is clearly marked as pending.
- Artifact status reflects approval; a draft remains a draft.
- No application code or tests were implemented as part of this planning lab.

## Handoff to Module 6

Keep the requirements worksheet, feature specification, and task list together in the Target project. Module 6 will implement tasks incrementally and update task status based on actual changes and test evidence. If the scope changes again, update the planning artifacts before continuing.
