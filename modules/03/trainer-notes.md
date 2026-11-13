# Module 3 — Trainer notes

## Suggested timing (90 minutes; adjust to cohort)

- 10 min: connect test feedback to the Module 1 API work.
- 15 min: add test dependencies and run the baseline suite.
- 20 min: retrieve the Issue through MCP, add the testing Skill, ask Copilot to write the red test, then run it and read the failure.
- 20 min: ask Copilot to diagnose, then implement a focused validation change.
- 15 min: rerun tests and manually inspect representative requests.
- 10 min: review diffs and discuss test limits.
- Optional Hook lab: reserve 10–15 min after the red-test discussion for inspection, enabling, and comparing Hook feedback with a manual pytest run.
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
9. For the optional Hook lab, confirm a current Copilot session target and command-hook execution host. Do not enable the Module 3 Hook before learners have run, inspected, and explained the red test. Ask learners to inspect both overlay files and check for destination collisions first.

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
- Preserve the teaching order: the learner adds and runs the red test, reads the failure, and explains it before copying/enabling the optional Module 3 test-feedback Hook. The new Hook is for implementation and verification. It may run pytest at agent stop after relevant Python changes, return a concise continuation reason on failure, and permit a continuation. Have learners compare that reason with a direct `python -m pytest -q` run.
- The Hook inspects Git's working-tree changes under `app/` and `tests/`, including untracked files, so use a clean checkpoint before the exercise. Its configured launcher is `uv run --no-sync --project . python ...`, which uses the Target project's existing uv environment without syncing dependencies; the script prefers that project's `.venv` Python and falls back to the Hook process's Python if pytest is installed. Confirm `uv` is on the VS Code process `PATH`; if not, substitute an absolute uv path or the Target project's `.venv` Python path. The Copilot session and Python/test environment must be on the same host with access to the Target checkout. This repository overlay is for the current Copilot command-hook contract, not the deprecated Local harness or Claude/Codex session targets.
- Explain the failure paths explicitly: missing pytest, inability to inspect changes, timeout, and nonzero test exit never produce a green result. The first detected problem can request one continuation. If `stop_hook_active` is already true, it reports that verification is still failing/unavailable to stderr and returns without another forced continuation; the learner must inspect pytest manually. Hook support, execution host, and behavior vary by runtime/version. When unavailable, learners continue with manual pytest.
- Do not describe this local feedback aid as a test gate, human review, or CI. It does not prove correctness, and Module 10 remains the CI exercise. No prompt, tool arguments, environment variables, or complete test output should be logged or returned to Copilot.
- Do not treat a green test suite as proof of correctness. Discuss untested inputs, concurrency, persistence, security, and behavior not represented by assertions.

## Expected behavior

- Baseline tests pass against the starter API and a correctly completed Module 1 target.
- The regression test sends `{"title": "   "}` to `POST /tasks` and expects HTTP 422. In the unmodified starter, the request satisfies `min_length=1` and is accepted, so the test fails. Copilot may write it using the Skill, or the learner may use the prepared reference file as a fallback.
- The MCP server returns the trainer-prepared Issue to Copilot; it does not edit local files. The Hook observes tool names, including the MCP and terminal tools when the runtime sends those events.
- After a focused validation change, the invalid request returns 422 and baseline valid task creation still passes.
- No test requires production dependencies, an external service, or live network access.

## References

The current Copilot command-hook contract uses `agentStop` input fields including `cwd` and boolean `stop_hook_active`; command output is a JSON object on stdout. For this event, top-level `decision: "block"` plus a non-empty `reason` forces another agent turn, while no decision allows completion. The Hook checks `stop_hook_active` and requests at most one continuation. This is distinct from the older Local harness `Stop` output envelope.

- [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/) — `TestClient`, HTTPX, and pytest.
- [pytest monkeypatch fixture](https://docs.pytest.org/en/stable/how-to/monkeypatch.html) — safely replacing attributes during a test.
- [Pydantic field validators](https://docs.pydantic.dev/latest/concepts/validators/) — one possible approach if a participant asks how to express model-level validation.
- [VS Code: Configure agent Hooks](https://code.visualstudio.com/docs/agent-customization/hooks) and [GitHub: Copilot hooks reference](https://docs.github.com/en/copilot/reference/hooks-reference) — official `agentStop` command-hook input/output contract, runtime selection, and continuation limit. Checked 2026-11-12.
