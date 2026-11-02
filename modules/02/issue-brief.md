# Module 2C — Trainer-prepared GitHub Issue

Create one Issue in each participant's GitHub Target repository before the MCP lab. Do not assign it to Copilot. Record the issue number for the participant.

**Title:** Document the Task API response contract

**Body:**

## User need

As a developer using this service, I want the README to explain the Task API's request and response contract so I can try it without inspecting the implementation first.

## Acceptance criteria

- Document `GET /healthz` and its successful response.
- Document `GET /tasks` and the shape of each returned task.
- Document `POST /tasks`, its accepted fields, validation limits, and successful status code.
- State that tasks are held in memory and reset when the service restarts.
- Keep the change limited to the Target project's README. Do not change application code or add dependencies.

## Out of scope

- Adding authentication, persistence, a user interface, or automated tests.
- Changing endpoint behavior.

## Notes

Use the repository's implementation as the source of truth if a detail in this Issue conflicts with the code. Ask for clarification rather than guessing if a requirement cannot be reconciled.
