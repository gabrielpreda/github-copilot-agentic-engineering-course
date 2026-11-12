# Module 4 — From request to requirements

## Purpose

Turn a short, ambiguous feature request into a useful draft that a product owner and engineer can review before implementation. Practice using the project and connected sources as evidence, asking focused questions, and keeping facts, assumptions, and open decisions separate.

## Learning outcomes

By the end of this lab, you can:

- Explain the difference between a request, a requirement, an assumption, and an acceptance criterion.
- Inspect existing code, tests, and related issues to find relevant evidence.
- Ask focused questions that resolve meaningful behavior or scope decisions.
- Produce a traceable requirements worksheet with testable criteria and explicit open questions.
- Explain how a Skill, MCP server, and session-start Hook contribute different capabilities to this workflow.

## Before you begin

- Continue with your Module 1 Target project and keep your Module 2 and 3 additions and local changes.
- Use the GitHub MCP server already configured in Module 2. Do not add another GitHub server.
- Keep the Module 2 tool-observation Hook and the Module 3 test-feedback Skill available. If you completed optional Module 3 Lab D, its `agentStop` test-feedback Hook may also be present; it checks changed application/test Python files, while this module's optional session-start Hook has a separate continuity purpose.
- Copy the worksheet template and the new Skill as described below. Each is **ADD**; retain any files already at those paths and merge by hand if a conflict exists.
- Do not open the Training materials project as the application workspace.
- Start from a clean Git checkpoint or save a copy so the worksheet and customizations are easy to inspect.

## Lab A — Add the requirements Skill and worksheet

1. Check whether `.github/skills/requirements-refinement/SKILL.md` already exists. If not, copy `target-overlays/skill/.github/skills/requirements-refinement/SKILL.md` to that path in the Target project (**ADD**). Keep the Module 2 API review Skill and Module 3 test-feedback Skill.
2. Check whether `docs/requirements/task-priority.md` already exists. If not, copy `target-overlays/template/docs/requirements/task-priority.md` to that path (**ADD**). Create parent folders if needed. If a worksheet exists, merge the template sections without discarding your content.
3. Read both additions. The Skill guides a reusable refinement process; the worksheet is a blank exercise artifact. The Skill does not decide priority behavior for this particular API.

## Lab B — Investigate the request using existing project context

1. Publish `issue-brief.md` as a GitHub Issue in the Target repository, or use the trainer's prepared Issue. Do not create an Issue if your trainer already prepared one.
2. Start a Copilot Agent session in the Target project. Use the first prompt in `prompts.md`.
3. Ask Copilot to search for related Issues through the existing GitHub MCP server, then read the relevant prepared Issue. The server is the external context source; the Skill guides how to reason about that evidence.
4. Ask Copilot to inspect the current API and tests. If available, use the Module 2 `api-contract-review` Skill to summarize the existing contract and the Module 3 `test-feedback` Skill to identify what the current tests do and do not establish.
5. Observe the Module 2 Hook's before/after tool-use output. It reports tool names; it does not check whether requirements are correct.
6. Review the evidence and record source paths or Issue identifiers. Do not edit application files or ask Copilot to implement anything.

If GitHub MCP is unavailable, use the Issue text supplied by the trainer and record that the source was pasted rather than retrieved. If a prior Skill or Hook is unavailable in your editor, follow the workflow manually and note the limitation.

## Lab C — Ask questions before drafting

1. Use the clarification prompt in `prompts.md`. First ask Copilot to list the important unknowns and propose a short set of questions for the requester. Have the trainer answer only the questions that learners actually ask.
2. Compare each question with the available evidence. Remove questions already answered by the request, current implementation, tests, or a trusted source.
3. Keep unanswered items open. Do not accept plausible defaults as approved requirements.

### Lab C extension — inspect the Miro product flow

Use the trainer's prepared Miro board that describes the priority workflow. Connect the Miro MCP server as described in `trainer-notes.md`, or use the supplied board export if the MCP connection is unavailable. Ask Copilot to inspect the named board and report relevant evidence with locations, then compare that evidence with the Issue and local code. This evidence will be used to create and implement traceable Jira stories in Module 9.

Miro MCP can expose actions as well as reads. For this exercise, do not invoke create, update, delete, or other write tools. Only use it if your environment lets you constrain or supervise tool access appropriately; otherwise the trainer can provide a board export or screenshots as evidence. Do not treat board content as approved if it conflicts with the requester or lacks an owner.

## Lab D — Draft and review the worksheet

1. Use the drafting prompt in `prompts.md` to update only `docs/requirements/task-priority.md`.
2. Require the worksheet to include the request, sources reviewed, confirmed facts, assumptions/inferences, acceptance criteria, non-goals/constraints, and open questions.
3. Keep the status as `Draft` and approval owner unassigned unless a responsible person explicitly approves the requirements.
4. Review each criterion: can someone determine whether it is satisfied from observable behavior? Is it supported by evidence or explicitly marked provisional?
5. Inspect the diff. Confirm the application source and tests were not changed and that no external Issue or board was modified.

## Lab E — Add a continuity Hook (optional, with trainer approval)

1. Check for existing session-start Hooks and review the current Copilot hook format for your session target. Hook formats vary across runtimes and can change.
2. Copy `target-overlays/hook/.github/hooks/requirements-context.json` and `load_requirements_context.py` into the matching paths in the Target project. Both are **ADD**; keep `.github/hooks/audit.json` and its script from Module 2.
3. If the Target project already has a hook configuration or uses a different Python command, merge the `sessionStart` entry and adapt the command with the trainer. Do not replace another hook file.
4. Start a new disposable Copilot session. Confirm that the Hook adds only a reminder naming the worksheet and its status. Check its output; it should not include the worksheet's content.
5. Change nothing in the worksheet during this check. Verify that the Hook does not alter files or block tool calls.

This Hook is a continuity aid. It reminds a fresh session to read the draft, preserve unresolved questions, and avoid treating a draft as approval. It does not enforce a policy, approve requirements, or prevent edits. If the hook cannot run in your session target, mention the worksheet in the next-session handoff instead.

## Completion criteria

- You used the existing project and available external sources to gather relevant evidence, or recorded the fallback used.
- You separated confirmed facts from assumptions and inferences.
- You asked focused clarification questions before drafting acceptance criteria.
- The worksheet has concise, observable criteria and clearly listed non-goals and open questions.
- The worksheet remains a draft unless an authorized reviewer approved it.
- The Target application code, tests, GitHub Issues, and Miro board were not modified during the lab.
- You can describe what the new Skill guides, what the MCP source provides, and what the Hook contributes.

## Handoff to Module 5

Keep `docs/requirements/task-priority.md` in the Target project. Module 5 will use the reviewed requirements to create a lightweight specification and trace tasks back to acceptance criteria. If requirements remain unresolved, carry those questions forward rather than silently deciding them.
