# Module 3 — Trainer notes

## Suggested timing (90 minutes; adjust to cohort)

- 10 min: connect test feedback to the Module 1 API work.
- 15 min: add test dependencies and run the baseline suite.
- 20 min: retrieve the Issue through MCP, add the testing Skill, ask Copilot to write the red test, then run it and read the failure.
- 20 min: ask Copilot to diagnose, then implement a focused validation change.
- 15 min: rerun tests and manually inspect representative requests.
- 10 min: review diffs and discuss test limits.
- 5 min: buffer.

## Setup

1. Prepare a clean Target project that contains the Module 1 Task API and, if the cohort completed Module 2, the added Skill, Hook files, and MCP configuration. Do not replace the app with a trainer copy after participants have made their Module 1 changes.
2. Create a new GitHub Issue in the Target repository using `issue-brief.md`. Record its number and confirm learners can read it through the GitHub MCP server. Use the read-only `repos,issues` configuration prepared in Module 2.
3. Confirm the Module 2 Hook is installed and enabled in an environment where Hooks are available. Prepare a trainer demo if participant accounts cannot run Hooks or MCP.
4. Confirm Python 3.10 or later, the project install, and a working virtual environment. The supplied test requirements add pytest and HTTPX; installing the app package remains the Module 1 setup step.
5. Review the Module 1 filter implementations. The baseline suite intentionally tests stable API basics and does not assume an exact implementation of the `completed` filter.
6. Inspect each participant's `TaskCreate` validation before the red test. The seeded failure assumes the current starter behavior: `Field(min_length=1)` accepts a title containing spaces because its length is greater than zero.
7. Ensure participants can run pytest locally. The suite uses `TestClient` and does not require a running Uvicorn process or network access.
8. Prepare the `test-feedback` Skill overlay. It is added alongside the existing API review Skill and guides a generic test-first feedback loop rather than encoding details of this one API.

## Facilitation guidance

- Require the baseline suite to pass before adding the red test. If it does not, use the failure to inspect participant state rather than layering more changes on top.
- Add the testing Skill after the baseline suite passes. Have learners use it to ask Copilot for the red regression test before any application change.
- Have learners ask Copilot to retrieve the trainer Issue with the GitHub MCP `issue_read` tool. The Module 2 Hook should report the MCP call before and after a successful result; exact tool-name display may include a server prefix.
- Ask Copilot to run the newly added test through its terminal tool after learners review the test diff. If Copilot does not call a tool, the Hook has nothing to report; learners can run pytest themselves and still inspect the failure.
- Ask learners to state the expected result, actual result, and exact assertion before they ask Copilot to fix the failure.
- Encourage learners to ask for a diagnosis first. Then ask for a narrow change and inspect the diff, particularly whether a validator rejects blank input without changing unrelated request behavior.
- Have learners compare Copilot's generated regression test with `target-overlays/red/tests/test_title_validation.py`. The prepared file is a reference and fallback if generation fails; learners should not add it when an equivalent test already exists.
- Ask participants to compare the reusable `test-feedback` procedure with the concrete test fixture and application code. The Skill guides the workflow; it should not hard-code the Task API file paths or prescribe a Pydantic-specific implementation.
- Keep the test as an independently written expectation. Do not let Copilot weaken or delete the test to obtain a green run.
- The implementation can use different valid Pydantic techniques. Assess behavior, scope, and evidence rather than requiring identical code.
- If the test already passes, have the learner explain why and use the prepared demo to show the expected failing result. Do not direct them to add a defect to their application.
- Keep the Module 2 Hook as an observation only. If active, it may show tool use during pytest execution; that is not the test result itself.
- Do not treat a green test suite as proof of correctness. Discuss untested inputs, concurrency, persistence, security, and behavior not represented by assertions.

## Expected behavior

- Baseline tests pass against the starter API and a correctly completed Module 1 target.
- The regression test sends `{"title": "   "}` to `POST /tasks` and expects HTTP 422. In the unmodified starter, the request satisfies `min_length=1` and is accepted, so the test fails. Copilot may write it using the Skill, or the learner may use the prepared reference file as a fallback.
- The MCP server returns the trainer-prepared Issue to Copilot; it does not edit local files. The Hook observes tool names, including the MCP and terminal tools when the runtime sends those events.
- After a focused validation change, the invalid request returns 422 and baseline valid task creation still passes.
- No test requires production dependencies, an external service, or live network access.

## References

- [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/) — `TestClient`, HTTPX, and pytest.
- [pytest monkeypatch fixture](https://docs.pytest.org/en/stable/how-to/monkeypatch.html) — safely replacing attributes during a test.
- [Pydantic field validators](https://docs.pydantic.dev/latest/concepts/validators/) — one possible approach if a participant asks how to express model-level validation.
