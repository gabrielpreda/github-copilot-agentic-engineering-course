# Module 3 — Prompt cards

## Lab B — Ask Copilot to add a regression test

> Use the GitHub MCP server's read-only `issue_read` tool to retrieve issue #<ISSUE_NUMBER> from <OWNER>/<REPOSITORY>. Summarize its acceptance criteria and cite the issue number. Then use the `test-feedback` Skill to add one pytest regression test in the existing `tests/` directory for the requested behavior. If an equivalent test already exists, review it instead of creating a duplicate. Do not change application code, other tests, project dependencies, or documentation. Do not run tests yet. Show me the test diff and explain why it should fail against the current implementation.

## Lab B — Run the new test

> Run only `python -m pytest -q tests/test_title_validation.py`. Do not edit files. Report the command, exit status, expected result, and actual result. Explain the failure using the test and application code.

## Lab C — Diagnose before changing code

Continue in the same chat and paste the failing pytest output where indicated:

> Use the `test-feedback` Skill. The regression test reports this failure:
>
> ```text
> <paste the relevant pytest failure output>
> ```
>
> Do not change files yet. Explain which behavior failed, what the test expected, what the application returned, and which code is most likely responsible. Use the test and application code as evidence. Do not suggest unrelated refactoring.

## Lab C — Request the focused fix

After checking the diagnosis, ask:

> Implement the smallest change needed so `POST /tasks` rejects titles that contain only whitespace with HTTP 422. Preserve the existing behavior for non-empty titles and keep the change limited to request validation. Do not edit the tests, README, project dependencies, or unrelated code. Show me the diff and explain how to verify it.

## Optional follow-up

> Explain what the passing tests establish about this change and name two relevant cases or risks they do not cover. Do not change files.
