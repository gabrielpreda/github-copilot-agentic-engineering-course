# Module 5 — Trainer notes

## Suggested timing (90 minutes; adjust to cohort)

- 10 min: distinguish requirements, specification, task list, and implementation design.
- 15 min: inspect Module 4 worksheet and add the new Skill/templates.
- 20 min: draft and peer-review the one-page specification.
- 20 min: decompose the feature and check traceability.
- 15 min: introduce a scope change and update linked artifacts.
- 10 min: review handoff to Module 6 and discuss where detail became unnecessary.

## Preparation

1. Use a Target project with the Module 4 requirements worksheet and the Module 1 Task API. Preserve participant changes.
2. Review the Module 4 trainer answer card. Use the clarified priority behavior as the basis for the initial spec only if the requirements worksheet records those answers and their approval status.
3. Prepare one scope change for the exercise. Suggested trainer prompt: “For this release, the existing task-list endpoint should return tasks with priority `high` before tasks with other priorities. Keep the response shape and existing filters unchanged.” Present it as a proposal unless the product owner has approved it. This adds an observable ordering behavior to the priority feature while keeping the exercise focused on updating requirements, spec, tasks, and planned verification rather than implementation.
4. Have learners keep the Module 2 GitHub MCP connection and prior Hooks/Skills available. GitHub MCP may be used to retrieve the approved Issue context; no new remote server or external write is required.
5. Review the current Copilot Skill support and command syntax for the cohort's session target. Provide a manual prompt fallback if a Skill does not activate.

## Facilitation guidance

- Reinforce the separation: requirements capture desired behavior; the spec organizes that behavior and constraints; tasks sequence verifiable work; code expresses one implementation.
- Treat Module 4 status as authoritative. A draft worksheet should produce a draft specification and task list.
- Encourage a single page for the spec, but do not make page count a reason to omit material acceptance behavior or known constraints.
- Ask learners to explain why each sentence exists. Remove architecture prescriptions that do not follow from a requirement or project constraint.
- The Task API's in-memory storage, request/response shapes, and validation are useful context, but current behavior alone does not authorize a new requirement.
- Ensure planned tests are labeled as planned. Module 6 will add tests and implementation; Module 5 does not create test files.
- During decomposition, ask whether a task can be reviewed and verified independently. Avoid one-task-per-file or one-task-per-line breakdowns.
- Assign stable `AC-*` IDs to the Module 4 criteria before linking them. Preserve criterion wording and worksheet content.
- For the scope-change exercise, update the requirements first when the owner approves a behavior change. Preserve unaffected criterion and task IDs. For a proposal, leave approved requirements unchanged and mark its impact as pending in the downstream artifacts.
- Do not force a new Hook into this module. Module 4 already contributes a useful session-start continuity Hook; this lab's central value is better planning artifacts and a reusable Skill. Reuse the existing Hook where supported.
- No new MCP server is required. Use GitHub MCP as a context source if issue history is useful; adding another server would not improve the core spec/task exercise.

## Reference outcome for the priority feature

Assuming Module 4's clarification answers are recorded and approved, a concise spec could state:

- Tasks accept `low`, `normal`, and `high` priorities.
- Omitted priority defaults to `normal` for compatibility.
- Priority is returned in task responses.
- Invalid values follow the existing HTTP 422 validation response behavior.
- This release does not add sorting/filtering, persistence, authentication, or UI changes; existing title behavior remains unchanged.

A reasonable task breakdown might be:

| Task | Result | Criteria | Planned verification |
|---|---|---|---|
| T-1 | Add focused request validation tests for accepted values, omitted default, and invalid value | AC-1, AC-2, AC-3 | Automated API tests (planned) |
| T-2 | Implement priority request/response behavior while preserving existing API behavior | AC-1, AC-2, AC-4 | Run focused and full API tests (planned) |
| T-3 | Review exclusions and confirm no unrelated behavior changed | AC-4 and explicit non-goals | Diff review and representative manual API check (planned) |

Accept other sensible decompositions. Tests may be in the same task as a focused behavior change if the result remains verifiable. Do not prescribe Pydantic model details in the spec.

For the proposed high-priority ordering scope change, learners should identify the list endpoint behavior it changes and add a pending impact record without changing approved requirements. Once approved, they should add or revise the relevant criterion, add a planned ordering test, and update the affected task(s). Existing unaffected default/value-validation criteria should retain their IDs. The response shape and existing filters remain outside this change.

## Skill, Hook, and MCP connections

- **New Skill:** gives a repeatable approach to concise specifications, task decomposition, traceability, and scope-change updates.
- **Existing Skills:** help inspect the API contract, test evidence, and Module 4 requirements; they do not replace product approval.
- **Existing GitHub MCP:** retrieves remote Issue context when needed. The task list remains a local course artifact; learners do not need to create remote issues.
- **Existing Hooks:** Module 2 makes tool use observable; Module 4 can remind later sessions about requirements status. Module 5 adds no Hook because a distinct Hook would either duplicate that reminder or enforce a brittle planning convention.

## References

- [GitHub Copilot agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) — reusable agent workflows and instructions.
- [VS Code agent customization](https://code.visualstudio.com/docs/agent-customization/overview) — how Skills and other customizations fit the agent workflow.
