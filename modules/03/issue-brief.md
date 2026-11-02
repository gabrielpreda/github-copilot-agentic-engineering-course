# Module 3 — Trainer-prepared GitHub Issue

Create this Issue in the GitHub Target repository before Module 3. If the class uses the same shared repository as Module 2, create a new Issue there. Record the issue number for participants. The Issue is a read-only source for the lab; do not assign it to Copilot.

**Title:** Reject whitespace-only task titles

**Body:**

## User need

As a user creating a task, I want a title containing at least one non-whitespace character so that blank-looking tasks are not accepted.

## Acceptance criteria

- `POST /tasks` returns HTTP 422 when `title` is empty or contains only whitespace characters.
- A normal non-empty title continues to be accepted.
- Do not change other request fields, endpoint behavior, dependencies, or documentation.
- Add a regression test before changing application code.

## Out of scope

- Trimming or otherwise rewriting non-empty titles.
- Changing the title length limit or other validation rules.
- Adding persistence, authentication, or unrelated refactoring.
