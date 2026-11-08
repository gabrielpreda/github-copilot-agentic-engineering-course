# Module 9 — Miro-to-Jira story delivery loop

## Purpose

Practice the complete product-to-code loop against a real feature: read a Miro flow, turn approved behavior into Jira stories, then take each story through code exploration, tests, implementation, verification, and a pushed branch. Do not generate a large feature from a diagram in one shot. The durable unit of work is one reviewed Jira story at a time.

## Learning outcomes

By the end of this lab, you can:

- Retrieve and interpret a Miro diagram as evidence while distinguishing approved decisions from sketches and open questions.
- Create small, testable Jira stories linked to source evidence and acceptance criteria.
- Read the current Jira story before each implementation, resolve gaps, and keep scope bounded.
- Explore existing code, capture important behavior with regression tests, and implement one story at a time.
- Push a story branch and record exact test/commit evidence before moving to the next story.
- Use Figma evidence where a UI is in scope and recognize when it is irrelevant to an API-only change.

## Before you begin

- Continue in the Target project from Module 8. Check the branch and working tree; preserve local work.
- Confirm the capstone requirements/spec and review handoff. Identify which criteria remain unimplemented and whether their approval is current.
- Ask the trainer for the Miro board, Jira project/key, and stories selected for this lab. Jira and Miro access must be configured for the Target project; do not connect personal workspaces or paste secrets into repository files.
- Copy `target-overlays/skills/.github/skills/miro-jira-story-generation/SKILL.md` and `target-overlays/skills/.github/skills/delivery-lifecycle/SKILL.md` to the same paths in the Target project (**ADD**). Copy `target-overlays/agents/.github/agents/delivery-lifecycle.agent.md` to the same Target path (**ADD**). Preserve existing files at those paths and merge intentionally if needed.
- Merge the server entries from `target-overlays/vscode/.vscode/mcp.json` into the Target project's `.vscode/mcp.json`; this is **MERGE**, not replacement. The template uses `JIRA_URL`, `JIRA_USERNAME`, and `JIRA_API_TOKEN` environment variables. Use the Miro OAuth sign-in flow. Put `FIGMA_API_KEY` only in a local ignored `.env` if Figma is needed; never commit tokens or copy `.env` into the repo.
- Keep the Module 2 audit Hook enabled if supported. It provides before/after tool-call observations during Miro/Jira/GitHub work; it does not authorize, block, or secure those operations. Do not add a duplicate audit Hook.
- Install the required MCP launch tool (`uvx` for Jira and `npx` for Figma), start/reload the configured servers, authenticate, and confirm read tools can access the trainer's named resources before relying on them. A config entry alone does not prove connectivity or permission.
- Inspect connected tool capabilities and use only the access appropriate to the action. Miro reads should be read-only. Jira story creation/update is a write action: review each generated story and create it only in the designated training project.
- Confirm Git remote, branch naming, push permissions, and test/CI expectations. Do not force-push, push secrets, or include unrelated work.
- Create `docs/handoffs/story-delivery-log.md` from `story-workflow.md` as **ADD**, or merge with an existing equivalent. Do not overwrite participant evidence.

## Lab A — Read the product flow in Miro

1. Open the trainer-provided Miro board via its configured MCP integration or approved plugin. If unavailable, use the trainer-provided export and record the fallback.
2. Ask Copilot to inspect only the named frame/flow relevant to the next feature. Request evidence with board/frame/object locations, author/status if available, and a separation of confirmed decisions, proposals, and unanswered questions.
3. Compare the diagram with the current requirements/spec and Jira project. Identify conflicts, stale labels, missing error paths, and any unapproved design assumptions.
4. Ask the product owner/trainer to resolve only the questions that change observable behavior or acceptance. Record decisions and source locations in the delivery log before story creation.
5. If the story includes a UI, inspect the linked Figma frame and record frame URL/name, relevant states, and design questions. If the feature is API-only, note that Figma is not applicable.

## Lab B — Generate and review Jira stories

1. Choose one coherent feature slice from the approved criteria. Ask Copilot to propose Jira stories with stable titles, user value, acceptance criteria, dependencies, out-of-scope notes, and links back to Miro/spec evidence.
2. Review the story set before creating anything. Stories should be independently testable, ordered by dependency, small enough for one reviewable branch, and collectively traceable to approved criteria. Reject duplicate, speculative, or oversized stories.
3. Obtain explicit approval for the exact story batch and fields before creating Jira issues. Create only approved stories in the training Jira project using the authorized Jira MCP/plugin or Jira UI. Inspect the actual created story IDs and fields; do not trust a tool summary alone. If write access is unavailable, prepare a reviewed story batch for the trainer to enter and record that the integration was unavailable.
4. Update `docs/handoffs/story-delivery-log.md` with each Jira key, title, acceptance criteria, Miro/spec references, dependency, status, and intended branch.
5. Do not ask Copilot to implement the whole Miro diagram or every story in one request.

## Lab C — Implement each story sequentially

Repeat these steps for one Jira story at a time. Do not begin the next story until the current story's branch is pushed and its handoff is complete.

1. **Read the live story.** Retrieve the current Jira story by key. Compare its acceptance criteria and status with the local delivery log, approved requirements, Miro evidence, and Figma frame if applicable. If they disagree or are incomplete, stop and resolve the story before coding.
2. **Explore existing code.** Use targeted searches to trace relevant routes, models, services, tests, and callers. Ask Copilot for a narrow map with file/symbol references, then verify the references. Inspect history only where it clarifies behavior.
3. **Protect existing behavior.** Run the relevant baseline tests. Add or confirm focused regression tests for behavior that must remain unchanged before modifying legacy code. Include existing capstone filters, ordering, validation, and response shape where relevant.
4. **Create an isolated branch.** Use a story-specific branch, such as `feature/PROJ-123-short-name`, from the agreed base. Ensure the working tree contains no unrelated or unreviewed changes.
5. **Test first, implement narrowly.** Add tests for the current story's acceptance criteria, inspect them, and observe the failing result when the change should fail first. Implement only this Jira story. Update Jira status only when the team's workflow says to do so and only from observed evidence.
6. **Verify and review.** Run focused and relevant regression suites. Inspect the full diff for missed criteria, unintended changes, input validation, authorization, dependencies, security issues, generated files, and secrets. Record exact commands and results.
7. **Commit and push.** Review the staged diff and proposed commit message with the trainer before committing. Include the Jira key, for example `PROJ-123 Add due-date filter`. Obtain separate approval before pushing the story branch to the configured remote. Confirm the remote branch/commit exists and matches the reviewed local commit. Do not force-push or include unrelated work.
8. **Update the delivery log.** Record Jira key, branch, commit, changed files, tests/results, push confirmation, open questions, and next action. If a formal review or CI gate is required before starting dependent work, wait for it.
9. **Move to the next story.** Start again by reading the next Jira story as it currently exists. Do not rely on a previous Copilot session's summary as the story specification. For dependent work, wait for the prior branch to merge or follow the trainer-approved branch strategy.

For dependencies between stories, agree whether the next branch starts from the approved prior branch or the updated base after merge. Record the choice; never silently base a story on unreviewed work.

## Lab D — Close the delivery loop

1. Reconcile every selected Miro decision and approved criterion to one or more Jira stories.
2. Reconcile each completed story to its branch, commit, tests, and remote push confirmation.
3. Report stories blocked, deferred, or awaiting review without marking them complete.
4. Prepare a handoff for Module 10: pushed branch names, commits, exact checks, CI status if available, deployment readiness, known issues, and remaining stories.
5. Do not deploy from an unreviewed branch. Module 10 handles CI and runtime/deployment verification; Module 11 handles formal PR completion.

## Optional deeper checks

For unfamiliar or risky components, use mutation testing or property-based/fuzz tests only when the project already supports them or the trainer approves adding tooling. Target meaningful validation boundaries or state transitions, keep runs bounded, and explain surviving mutations. These techniques supplement story acceptance and regression tests; they do not replace them.

## Completion criteria

- Miro evidence was read or a fallback was recorded, with decisions and open questions distinguished.
- Approved Jira stories were reviewed before creation and linked to source criteria/evidence.
- At least two stories were processed sequentially, or the trainer-approved exercise scope explains why only one was feasible.
- Each implementation began from the live Jira story and an inspected code path.
- Existing behavior was protected by relevant tests; story-specific tests and implementation were reviewed.
- Each completed story has an isolated branch, reviewed commit, observed test results, and confirmed remote push.
- The delivery log and Module 10 handoff report actual status and unresolved work.
