# Module 7 — Trainer notes

## Suggested timing (one half-day; adjust to cohort)

- 20 min: choose a track, protect existing work, create branch, inspect baseline.
- 35 min: refine request and answer learner questions.
- 30 min: create requirements, spec, tasks, and traceability.
- 60–90 min: implement a test-backed vertical slice.
- 20 min: review branch diff and prepare handoff/checkpoint.

For a shorter session, have learners complete refinement and planning beforehand, then implement one vertical slice in class. Do not compress testing and diff review into an unreviewed code-generation exercise.

## Preparation

1. Prepare the shared Target project with the Module 1 API, the Module 3 test setup, and any completed Module 4–6 work. Preserve participant changes and note differences between implementations.
2. Select which feature tracks are available for the cohort. Dependency-aware completion is advanced; combined Team Planning requires trainer approval.
3. Create a trainer Issue in each participating Target repository using the matching file in `issue-briefs/`. Record each Issue number and verify learners can read it through the existing GitHub MCP server.
4. Confirm that the GitHub MCP connection remains read-only and exposes issue search/read tools. No GitHub write is needed.
5. Confirm participants can safely save or commit prior work and create a local feature branch. Do not reset their repository to a trainer copy.
6. Confirm the baseline test result for the provided Target. If Module 6 priority behavior changed exact response payloads, ensure the baseline tests reflect that agreed state.
7. Keep the clarification cards below hidden until participants ask questions. Give each group only the answers relevant to its chosen track.

## Track selection guidance

- **Deadlines** is the recommended core choice for most groups. It has date boundaries and filtering but stays within the existing task resource and API.
- **Labels** is a good alternative for groups ready to reason about collection validation, duplicate/case policy, and query behavior.
- **Dependencies** is an advanced alternative. Use it for learners who have time to reason about graph validation and state transitions; do not combine it with another track in the standard session.
- **Team Planning** combines deadlines and labels for groups with stronger experience and sufficient time. Require one coherent end-to-end slice and explicitly defer the rest if needed.
- Avoid implementing all three feature tracks in one capstone part. The choices broaden relevance; the branch still needs a focused, reviewable scope.

## Trainer clarification cards — keep hidden until learners ask

Answers below are proposed course defaults to keep tracks runnable. If a learner asks a materially different question, treat that as a product decision and record the answer; do not disclose all answers at the start.

### Track A — Deadlines

- A due date is an optional calendar date (`YYYY-MM-DD`), not a time or timezone.
- Omitted due date remains absent (`null` in API responses); existing clients remain valid.
- A supplied invalid date is rejected with HTTP 422 using the existing validation-error style.
- `GET /tasks?due_before=YYYY-MM-DD` returns tasks with a non-null due date on or before the inclusive date.
- `GET /tasks?overdue=true` returns tasks whose due date is before the current date and that are not completed. Tests must use a deterministic technique to evaluate overdue behavior at a chosen reference date; do not rely on the wall-clock date when tests run.
- Invalid query dates receive HTTP 422. An empty result is HTTP 200 with an empty list.
- Keep current in-memory persistence and do not add a UI, authentication, or database.

### Track B — Labels

- A task may have zero or more labels; existing requests that omit labels remain valid.
- Accept at most five labels; each label has 1–24 characters after trimming surrounding whitespace.
- Normalize labels to lowercase after trimming; remove duplicates after normalization while preserving first-seen order.
- `GET /tasks?label=<value>` matches a single label case-insensitively after the same normalization. A task with that label is returned once.
- Invalid label counts/lengths receive HTTP 422. A no-match filter returns HTTP 200 with an empty list.
- Keep current in-memory persistence and do not add a UI, authentication, or database.

### Track C — Dependencies (advanced)

- Dependencies are task IDs supplied at task creation; omitted dependencies default to an empty list.
- Each dependency must refer to an already existing task. Reject self-dependencies, unknown IDs, and duplicate IDs with HTTP 422.
- A task cannot be marked complete while any direct dependency is incomplete. Existing completion behavior must be preserved where no dependencies exist.
- Add the smallest status-update route needed by the approved spec. Do not add dependency editing/deletion or recursive cascade behavior in this capstone slice.
- The graph cannot contain cycles because a new task may depend only on existing tasks; still test self-dependency and invalid references explicitly.
- Keep current in-memory persistence and do not add a UI, authentication, or database.

### Combined Team Planning

Use the confirmed Track A and Track B answers above. Require each acceptance criterion to map to a task and test; learners may complete one track as the full vertical slice and leave the other explicitly deferred if time is limited. Do not add dependencies.

## Reference acceptance criteria

Use only after groups have drafted criteria and questions.

### Deadlines

1. Tasks can be created with or without an optional calendar due date, and responses expose the chosen value or null.
2. Invalid due-date values are rejected with the API's HTTP 422 validation response.
3. `due_before` returns only tasks with non-null due dates on or before the inclusive supplied date.
4. `overdue=true` returns incomplete tasks with due dates strictly earlier than the current date; completed and undated tasks are excluded.
5. Existing clients and task fields continue to work.

### Labels

1. Tasks accept up to five labels and return normalized labels in first-seen order.
2. Omitted labels remain valid and produce an empty label list.
3. Too many labels or labels outside the allowed length receive HTTP 422.
4. Filtering by one label returns tasks containing the normalized label; no match is an empty successful result.
5. Existing task fields and clients continue to work.

### Dependencies

1. Tasks may be created with references to existing prerequisite tasks.
2. Self, duplicate, and unknown dependency IDs are rejected.
3. A task with an incomplete dependency cannot transition to complete.
4. A task with no dependencies or only completed dependencies can transition to complete.
5. Existing task creation/list behavior remains compatible.

## Facilitation and review

- Require a branch and working-tree check before edits. Help learners save existing work safely; do not reset it.
- Use the existing GitHub MCP for issue search/read if available. Keep the existing read-only permissions; learners do not need GitHub write access to complete this module.
- Have learners ask their own clarification questions before you provide the relevant answer card.
- Require a spec and task list before implementation; ask learners to explain why selected work is one vertical slice and what is deferred.
- Ask the group to predict test outcomes. Then inspect actual test output and implementation diffs.
- Encourage modest implementation choices that fit the existing FastAPI design. Do not turn this capstone into an unrequested database/authentication/UI rewrite.
- Keep work on the branch. Do not merge; Module 8 reviews safeguards, and later modules cover completion and delivery.
- Existing Module 2 audit Hook observes tool calls. Existing Module 4/6 session-start Hooks provide requirement/task context where supported. No additional hook is needed to enforce branching; the guide has learners verify branch state directly.

## References

- [FastAPI query parameters](https://fastapi.tiangolo.com/tutorial/query-params/) — query-string behavior and validation.
- [FastAPI request bodies](https://fastapi.tiangolo.com/tutorial/body/) — request models and validation.
- [pytest monkeypatch](https://docs.pytest.org/en/stable/how-to/monkeypatch.html) — controlling date-related dependencies in tests.
- [VS Code agent customization](https://code.visualstudio.com/docs/agent-customization/overview) — Skill, Hook, MCP, and session-target compatibility.
