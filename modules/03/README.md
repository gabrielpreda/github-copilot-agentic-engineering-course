# Module 3 — Testing and feedback

Add a small automated test suite to the Module 1 Target project, run it, and use one failing test to guide a focused application fix.

## Materials

- `participant-guide.md` — setup, lab sequence, verification, and completion criteria.
- `prompts.md` — exact Copilot prompts for investigating test feedback and requesting a narrow fix.
- `trainer-notes.md` — setup, timing, expected observations, and facilitation guidance.
- `issue-brief.md` — text for a trainer-prepared GitHub Issue, retrieved through the Module 2 MCP setup.
- `target-overlays/skill/` — a reusable testing and feedback Skill to **ADD** alongside Module 2's API review Skill.
- `target-overlays/setup/` — test dependencies and passing API tests to **ADD** to the Target project.
- `target-overlays/red/` — the expected failing validation test, used to compare Copilot's test or **ADD** as a fallback if needed.

Keep the Module 2 Hook and GitHub MCP configuration available for the tool-observation and Issue-lookup exercises. The supplied overlays do not replace `app/main.py`, `pyproject.toml`, or the Module 2 Skill. The new test Skill and test setup are additions; the application fix is produced during the lab and reviewed separately from the test changes.

## Test story

The current request model requires a title length of at least one character. A string containing only spaces meets that length check, so the API currently accepts it. The red test expresses the expected behavior: reject a whitespace-only title with HTTP 422. Participants use that failure as evidence for a focused validation change.
