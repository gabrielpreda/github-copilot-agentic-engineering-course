# Capstone feature catalog

Choose one primary feature track. Each track expands the existing in-memory Task API beyond a single-field change. Ask the trainer for the matching clarification card only after your group has identified its questions.

## Track A — Deadline tracking and overdue views

### Initial request

> Teams need to plan work against dates. Add due dates to tasks and make it easy to see what is coming due or already late. Keep existing clients working.

### Why this is substantial

This feature crosses request validation, response compatibility, date semantics, list query behavior, boundary cases, and tests. It does not require a database or user interface.

### Candidate areas to clarify

- Whether dates include a time or are calendar dates.
- How a missing due date is represented.
- How the API selects overdue or upcoming tasks and what date boundary is inclusive.
- Whether completed tasks appear in overdue results.
- Behavior for malformed dates and existing clients that omit the field.

## Track B — Labels and filtered views

### Initial request

> Teams need to organize tasks by project or workstream. Add labels to tasks and let users view tasks with a chosen label. Existing tasks and clients must continue to work.

### Why this is substantial

This feature crosses collection validation, request/response behavior, query semantics, filtering, compatibility, and tests. It raises decisions about duplicate labels, casing, limits, and matching behavior.

### Candidate areas to clarify

- Whether tasks may have multiple labels and how many.
- Whether labels are case-sensitive and whether whitespace is normalized.
- Whether filtering matches one label or several.
- What happens when a task has no labels or a filter matches nothing.
- How omitted labels behave for existing clients.

## Track C — Dependency-aware completion (advanced alternative)

### Initial request

> Some tasks cannot start until other tasks are finished. Let a task name the work it depends on and stop users from completing it too early. Make sure the API does not allow impossible dependency chains.

### Why this is substantial

This feature introduces cross-task references, invalid/missing/self references, cycle prevention, task state transitions, and multi-task tests. It affects the API contract and requires a more careful validation plan than a simple field addition.

### Candidate areas to clarify

- Whether dependencies can be added at creation, later, or both.
- Whether dependency IDs must refer to existing tasks.
- Whether self-dependencies and indirect cycles are rejected.
- Whether a task can be completed while any prerequisite is incomplete.
- What happens if a dependency is later changed or removed.

## Combined track — Team planning (advanced, trainer approval required)

Combine **Track A (deadlines)** and **Track B (labels)** into a single feature package. Each capability must have its own criteria and tests, with at least one end-to-end API workflow showing both together. Do not include Track C in this combination. The trainer may limit the package to one complete vertical slice plus a second partial slice if time is short; the spec and task list must clearly label what is in and out of the current delivery.

## Branch names

Use a clear local branch name, for example:

- `capstone/deadlines`
- `capstone/labels`
- `capstone/dependencies`
- `capstone/team-planning`

Do not use a combined track unless the trainer approves the scope and the team has time for review.
