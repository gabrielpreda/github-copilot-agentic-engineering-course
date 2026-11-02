# Module 3 — Testing and feedback

## Purpose

Add automated checks to the Task API and use a failing test to guide a small application change. The goal is to use test output as evidence, inspect Copilot's proposed fix, and verify that the rest of the API still behaves as expected.

## Learning outcomes

By the end of this lab, you can:

- Install and run a small pytest suite for a FastAPI application.
- Read a failure report and identify the assertion, actual result, and relevant code.
- Ask Copilot to diagnose a failure before asking it to change code.
- Make a focused validation change and rerun relevant checks.
- Describe what the tests establish and what remains unchecked.

## Before you begin

- Continue with the same Target project you used in Modules 1 and 2. Keep the application and all Module 2 customizations. This module adds a separate `test-feedback` Skill. Keep the Module 2 Hook enabled to observe tool calls and re-enable the GitHub MCP server to retrieve the trainer-prepared Issue.
- Make sure you can run the app from the Target project's virtual environment and can open `/docs`.
- Confirm that the GitHub MCP server from Module 2 can connect and that you can read the trainer-prepared Issue in the Target repository. If the server is disabled, start it again; do not add a second server or create a new token.
- Start from a clean Git checkpoint or save a copy of the current Target project. The test files and the application fix should be reviewable in your diff.
- Do not open the Training materials project as the application workspace.

## Lab A — Add and run the baseline tests

1. Check whether `requirements-test.txt` or `tests/conftest.py` and `tests/test_api.py` already exist in the Target project. If they do, do not overwrite them; ask the trainer how to merge the exercise.
2. Copy these files from `target-overlays/setup/` to the Target project at the same paths. Each is **ADD**:
   - `requirements-test.txt`
   - `tests/conftest.py`
   - `tests/test_api.py`
3. Activate the Target project's virtual environment and install the test-only dependencies:

   ```bash
   python -m pip install -r requirements-test.txt
   ```

   Use `python3` instead of `python` if that is the Python command used for the Target project on your system.
4. Run the baseline suite:

   ```bash
   python -m pytest -q
   ```

5. Review what each test sends to the API and checks in the response. The fixture resets the in-memory task list and ID counter between tests so one test does not depend on another's data.
6. If a baseline test fails, stop and inspect the failure before continuing. Check whether the Target project's Module 1 changes or local edits changed the expected behavior. Ask the trainer if the failure is due to a different implementation.

The baseline suite covers the health response, an empty task list, task creation defaults, and listing a created task. It does not yet cover every route behavior or the Module 1 filter in every implementation.

## Lab B — Retrieve the requirement and add a regression test

1. Confirm the baseline tests pass before adding the red test.
2. Add the supplied testing Skill by copying `target-overlays/skill/.github/skills/test-feedback/SKILL.md` to `.github/skills/test-feedback/SKILL.md` in the Target project. This is **ADD** alongside the Module 2 `api-contract-review` Skill; keep both.
3. In a fresh Copilot Agent chat, use the Lab B prompt from `prompts.md`. Ask Copilot to retrieve the issue using the GitHub MCP server's read-only `issue_read` tool, then use `test-feedback` to add one regression test only. Ask it not to change application code or run tests yet.
4. Observe the Module 2 Hook output. Look for a before/after report for the GitHub issue lookup. Tool names may appear with a VS Code or server prefix.
5. Check whether Copilot loaded or followed the Skill. If it did not and your VS Code setup offers Skills as slash commands, invoke `test-feedback` explicitly and ask it to review or finish the existing test without creating a duplicate.
6. Review the proposed test. It should send a title containing only spaces to `POST /tasks` and expect HTTP 422. Compare it with `target-overlays/red/tests/test_title_validation.py`, which is the reference test.
7. If Copilot did not create an equivalent test, copy the reference file to `tests/test_title_validation.py`. This is **ADD**. Do not create a duplicate or edit the test to make it pass.
8. Ask Copilot to run only the new test using the Lab B test-run prompt. Observe the Hook output for the terminal or test-run tool before and after it runs.
9. Read the failure. Identify the test name, expected status code, actual status code, and request payload. The starter's current length validation accepts a title made only of spaces, so the test should fail with a successful response instead of HTTP 422.
10. Inspect the `TaskCreate` model in `app/main.py` and explain why `min_length=1` does not reject a non-empty string consisting of spaces.

If the MCP server is unavailable, use the trainer's fallback: read the issue text in GitHub and paste its acceptance criteria into the prompt. Record that MCP was not used. If the test already passes because the Target project has been changed, record that result and ask the trainer for the prepared failing variant. Do not introduce a bug into your application just to force a failure.

## Lab C — Use test feedback to make a focused fix

1. Continue in the same Copilot chat so it retains the issue criteria and test result. Paste the Lab C prompt from `prompts.md`, include the actual failure output, and ask Copilot to use the `test-feedback` Skill. First ask for an explanation without changing files.
2. Check whether the diagnosis matches the test and model. Ask Copilot for a focused change that rejects titles containing only whitespace while preserving normal title validation and the existing API contract.
3. Review the proposed diff before accepting it. The test file should remain unchanged. The intended application change is limited to request validation in `TaskCreate`.
4. Run the complete suite again:

   ```bash
   python -m pytest -q
   ```

5. Inspect the result. All baseline tests and the new validation test should pass.
6. Run the app and manually check a normal title and a whitespace-only title through `/docs` or an HTTP client. Confirm the normal request still succeeds and the invalid title receives HTTP 422.
7. Review the final diff. Separate the test additions from the implementation fix and check for unrelated file or dependency changes.

## Completion criteria

- The baseline tests pass before the Skill-guided red test is added.
- You used the `test-feedback` Skill to ask Copilot to add a test before changing application code, or documented why the Skill did not activate.
- You retrieved the trainer Issue through GitHub MCP and observed the MCP/test-run calls through the Hook, or recorded which integration was unavailable and used the fallback.
- You can explain the failing assertion and connect it to the current validation rule.
- You reviewed a focused application fix rather than accepting it solely because the test became green.
- The full suite passes after the fix, and you manually checked representative valid and invalid requests.
- You can state what the suite does not cover. Passing tests are evidence about the checked cases, not proof that the application is defect-free.

## Test environment notes

- The tests use FastAPI's `TestClient`, pytest, and HTTPX. The tests call the application in-process; they do not require the Uvicorn server to be running.
- This module uses test dependencies in a separate `requirements-test.txt` file. It does not **REPLACE** the Target project's `pyproject.toml` or change the application install requirements.
- If your operating system requires `python3 -m pip` or `python3 -m pytest`, use the same Python executable for dependency installation and test execution.
