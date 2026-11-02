# Module 6 — Trainer notes

## Suggested timing (120 minutes; adjust to cohort)

- 10 min: check approved requirements/spec/task state and baseline.
- 15 min: choose task order and identify dependencies.
- 25 min: add and run the first focused test.
- 25 min: implement and review the first task; run focused and regression checks.
- 15 min: prepare the handoff and start a fresh session.
- 20 min: continue with the next task or use the optional approved ordering track.
- 10 min: review evidence, task state, and remaining work.

## Preparation

1. Prepare a Target project with the Module 1 API, Module 3 tests, and the Module 4/5 requirement/spec/task artifacts. Do not reset participant work to a trainer copy.
2. Confirm the artifacts agree on approval status and feature scope. The core feature is accepted priority values (`low`, `normal`, `high`), default `normal`, priority in task responses, and HTTP 422 for unsupported values, while preserving existing title behavior and the in-memory store.
3. Confirm Python and pytest are available. Do not proceed on top of an unexplained failing baseline; record it and use the trainer's known-good target if needed.
4. Confirm which Skills and Hooks are present. Module 2 tool observation and Module 4 session-start continuity are useful but are not prerequisites for the code/test workflow. The optional Module 6 session-start Hook can remind a fresh session of the handoff's current task and status.
5. If the Module 5 ordering scope change was approved, ensure the requirement, spec, task, and tie behavior are explicit. If it was not approved, leave it out of the implementation lab.

## Facilitation guidance

- Have learners choose an order before asking Copilot to code. A sensible core path is tests for accepted/default/invalid priority, implementation of request and response behavior, then full regression and compatibility review.
- Keep each Copilot session focused on one task. The first fresh session transition should happen after task evidence is recorded, not while important unrecorded context remains only in chat.
- Require learners to inspect tests before implementation and read exact test output afterward. Copilot's summary is not test evidence.
- Ask participants to state how each changed test maps to an AC ID, and how each task status follows from the test result and diff review.
- Check that `completed` remains unchanged, title validation is not accidentally broadened, omitted priority remains compatible, and response data includes the agreed default/value.
- If a new test fails for an unexpected reason, diagnose setup or existing project drift before implementing.
- Do not let participants implement an unapproved scope change. For the optional ordering track, require an approved AC and a defined tie rule before work begins.
- The project is still intentionally a compact API. The feature now spans models, validation, serialization, tests, acceptance traceability, and multi-session handoff. Later modules add review, existing-code constraints, CI/runtime delivery, and capstone work. Avoid premature persistence, database, UI, auth, or service architecture changes.
- Explain the integration roles: the new Skill guides a repeatable test-and-code process; Module 3's Skill supports test feedback; the existing GitHub MCP supplies remote Issue context if needed; Hooks observe tool calls and remind a new session about requirements and task state. No additional MCP server is required for this module.

## Expected core outcomes

- Creating a task without priority remains valid and returns priority `normal`.
- Creating a task with each accepted priority returns that value.
- An unsupported priority is rejected with HTTP 422 in the existing validation-error style.
- Existing fields, routes, and in-memory reset behavior remain unchanged.
- Tests cover the agreed behavior and relevant regressions. Learner code may use different valid Pydantic techniques.
- The handoff note records actual changed files, task state, test commands/results, decisions, and next task; the new session verifies those claims against the repository.

## Optional ordering scope

Use only when explicitly approved in the Module 5 artifacts. The approved spec must define at least the priority ordering and what happens for equal priorities. A straightforward teaching rule is descending priority (`high`, `normal`, `low`) while preserving creation order within a priority group, but do not impose this rule if the product owner has not approved it. Require a focused test for both group ordering and tie behavior.

## References

- [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/) — API tests with `TestClient`.
- [pytest documentation](https://docs.pytest.org/en/stable/) — running and organizing tests.
- [VS Code agent customizations](https://code.visualstudio.com/docs/agent-customization/overview) — Skills, Hooks, MCP configuration, and harness compatibility.
