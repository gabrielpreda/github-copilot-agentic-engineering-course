# Module 4 — Trainer notes

## Suggested timing (90 minutes; adjust to cohort)

- 10 min: connect Module 3's test evidence to the difference between behavior and requirement.
- 15 min: add the requirements Skill and worksheet; inspect the starter request.
- 20 min: search/read the GitHub Issue and inspect code/tests.
- 15 min: learners formulate questions; provide only the answers they request.
- 20 min: draft and peer-review criteria and open questions.
- 10 min: demonstrate the Miro source and/or session-start Hook; discuss continuity into Modules 5 and 9.

## Preparation

1. Prepare a Target project that retains the Module 1 API and Module 2 and 3 customizations. Module 2 overlay copies are not present in this Training materials tree in the current checkout; if learners lack them, use their previously committed Target-project versions or have the trainer demonstrate those concepts. Do not imply that a missing overlay was copied.
2. Create the GitHub Issue from `issue-brief.md` in the Target repository and verify participant read access through the existing GitHub MCP connection.
3. Prepare a Miro board for the core product-evidence exercise. Include a workflow sketch with a few notes, such as a proposed priority selector, default, or ordering. Keep some relevant decisions intentionally unresolved. Provide a full board URL and confirm learners have access; if MCP access is unavailable, provide an export.
4. Before enabling Miro MCP, review its currently exposed tools and organization policy. Miro MCP may expose write actions; use a read-only or supervised setup for the exercise. If write tools cannot be constrained, provide exported evidence instead.
5. Check which Copilot harness and hook format the session uses. The included example targets the Copilot command-hook format with `sessionStart`; Hook preview/availability and configuration differ by runtime. Use a trainer demo if participants cannot run it.

## Facilitation guidance

- Begin with the exact request in `issue-brief.md`; do not reveal the clarification card immediately.
- Have learners search for related issues before reading the prepared issue, so MCP is used to investigate repository history rather than as a ceremonial lookup.
- Ask learners to compare acceptance criteria with current code and tests. Existing behavior is evidence about the current system, not automatic evidence about desired behavior.
- Require learners to cite where each confirmed fact came from. Inferences should stay labeled as inferences.
- Let groups ask questions before providing answers. Give only answers to questions actually asked; this makes the cost of ambiguity visible.
- Do not reward the longest list of questions. Focus on the few decisions that change implementation, compatibility, or observable results.
- Have learners keep the worksheet in Draft. A course exercise does not itself authorize product approval.
- For Miro, emphasize that board contents can be outdated or exploratory. Ask who authored the information and whether it is approved before treating it as a requirement.
- Demonstrate the session-start Hook by opening a fresh session with the worksheet present. Its JSON `additionalContext` should contain the path and status, not the worksheet body. Explain that it is a reminder, not a gate or enforcement control.
- If students lack a supported Hook runtime, use the handoff prompt and discuss that the same continuity goal can be handled in a session handoff note.

## Clarification card — provide only when asked

These are exercise answers, not universal product requirements. If learners ask about these topics, answer accordingly:

- **Allowed values?** Use `low`, `normal`, and `high` for this first exercise. Other values are invalid.
- **Default for existing and newly created tasks?** `normal`.
- **Where does priority appear?** Accept it when creating a task and return it in task responses. Existing clients that omit it continue to work through the default.
- **Can users sort or filter by priority?** Not in this release.
- **What happens for invalid values?** The API returns HTTP 422 using the existing validation-error response style.
- **Case and whitespace?** Values are lowercase. Do not silently trim or normalize invalid priority values.
- **Does it change title behavior?** No. Preserve current title validation behavior.
- **Does this require persistent storage, authentication, a UI, or deployment changes?** No. Keep current in-memory storage and current API-only scope.
- **What happens after a server restart?** In-memory tasks still reset as they do today.

If a group asks an unlisted question, do not improvise policy. Mark it unresolved for the product owner.

## Expected worksheet shape

After the listed clarification answers, a reasonable draft should capture the default, accepted values, create/response behavior, invalid-value behavior, and exclusions. It should also note current in-memory behavior, preserve current title behavior, and leave any unasked/unanswered details open. Accept different wording if criteria are observable and faithful to answers.

Possible criteria (for trainer comparison after groups have drafted):

1. When a task is created without a priority, the API stores and returns `normal`.
2. When a task is created with `low`, `normal`, or `high`, the API accepts it and returns that value in the task response.
3. When a task is created with any other priority value, the API returns HTTP 422 using its existing validation-error response format.
4. Existing clients that omit priority remain compatible.

No criterion should require sorting, filtering, persistent storage, authentication, a UI, or a change to title validation.

## MCP and Hook discussion

- **GitHub MCP:** discover and read related Issues; it supplies remote repository context. The existing configuration remains the one from Module 2.
- **Optional Miro MCP:** inspect visual product/design evidence. It adds a different source and representation, but board content still needs provenance and approval checks. Do not duplicate a Miro connection if one is already provided by a plugin.
- **Module 2 Hook:** observe tool names before/after calls; it makes the investigation visible.
- **Optional Module 3 Hook:** checks changed Python files and supplies bounded pytest failure feedback at agent stop during implementation; it is distinct from both the Module 2 diagnostic and this module's session-start reminder.
- **Module 4 Hook:** on session start, add a small contextual reminder to read the worksheet and respect its status/open questions. It cannot verify or enforce the content.
- **Requirements Skill:** guides a repeatable reasoning workflow; it is not an external tool and does not fetch evidence by itself.

## References

- [VS Code agent hooks](https://code.visualstudio.com/docs/agent-customization/hooks) — current Copilot hook setup, event names, and command input/output behavior.
- [Miro MCP Server getting started](https://developers.miro.com/docs/connecting-to-miro-mcp) — official endpoint and OAuth connection flow.
- [Miro MCP Server FAQ](https://developers.miro.com/docs/miro-mcp-server-frequently-asked-questions) — supported objects, access, and tool capability notes.
