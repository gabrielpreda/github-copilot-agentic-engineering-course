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
- `target-overlays/hook/.github/hooks/` — an optional Copilot `agentStop` pytest feedback Hook and script to **ADD** during implementation and verification, after the red-test exercise.

Keep the Module 2 Hook and GitHub MCP configuration available for the tool-observation and Issue-lookup exercises. The supplied overlays do not replace `app/main.py`, `pyproject.toml`, or the Module 2 Skill. The new test Skill and test setup are additions; the application fix is produced during the lab and reviewed separately from the test changes.

The optional Module 3 Hook is separate from the Module 2 tool-name diagnostic. It checks changed Python files under `app/` and `tests/` at Copilot `agentStop`, runs pytest, and can request one continuation with a bounded failure summary. Participants must select the **Copilot** session target in VS Code and use a compatible current Copilot command-hook runtime. Hook support is preview/host dependent; if unavailable, run pytest manually. This Hook is a local feedback aid, not human review or CI. The two overlay files are **ADD** only. If either destination already exists, preserve it and ask the trainer for merge instructions; do not overwrite the participant's configuration or script.

## Test story

The current request model requires a title length of at least one character. A string containing only spaces meets that length check, so the API currently accepts it. The red test expresses the expected behavior: reject a whitespace-only title with HTTP 422. Participants use that failure as evidence for a focused validation change.
