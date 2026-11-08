# Module 9 — Trainer notes

## Suggested timing (half to full day)

- 30 min: read Miro evidence; resolve provenance and conflicts.
- 30–45 min: propose, review, and create a small Jira story batch.
- 45–75 min per story: live story intake, code exploration, regression tests, implementation, and review.
- 20 min per story: commit, push, status/evidence reconciliation, and dependency decision.
- 30 min: end-to-end traceability review and Module 10 handoff.

The course should prioritize two stories completed end to end over a large batch of unreviewed code. For a full-day lab, include a third story with an intentional dependency or a design-state edge case.

## Preparation

1. Provide a trainer-owned Miro board with a feature flow containing enough detail to derive multiple stories and at least one explicit unresolved question. Mark which notes are approved versus exploratory.
2. Provide a training Jira project and authenticated participant access. Configure/search/create/read tools as appropriate. Jira story creation is a write operation: restrict it to the training project and have learners inspect proposed stories before creation.
3. Prepare a 3–5 story candidate backlog with a dependency relationship, but leave room for learners to derive and critique the decomposition. Avoid duplicate issues from prior sessions.
4. Provide an optional Figma frame only if the selected workflow includes a UI. The existing Task API is UI-less; use a separate UI-bearing slice or a trainer-provided design artifact rather than forcing Figma into API acceptance criteria.
5. Confirm Git remote access, branch naming conventions, test command, push policy, and whether a story must be reviewed/merged before a dependent story begins. Never provide shared credentials in committed files.
6. Confirm Module 8 review and security findings were resolved or documented. Record each participant's capstone track and base branch.

The reference implementation for this module is [gabrielpreda/agent-delivery-lab](https://github.com/gabrielpreda/agent-delivery-lab): its README describes Jira, official hosted Miro, Figma, and GitHub MCP setup; `.github/skills/miro-jira-story-generation` separates evidence-backed story drafting and approved Jira writes from implementation; `.github/skills/delivery-lifecycle` defines story intake, verification, commit/push, PR, merge, deployment, and separate approval gates; `.github/agents/delivery-lifecycle.agent.md` binds the workflow to provider tools. These course overlays adapt that pattern to the Task API.

## Suggested story map

Use one coherent feature from the selected capstone track and relate it to actual approved requirements. Example for deadlines:

1. Add an optional due date with backward-compatible create/response behavior and validation.
2. Filter tasks by inclusive due-before date.
3. Add overdue filtering for incomplete tasks with deterministic date tests.

These are examples, not universal acceptance rules. Use the actual approved criteria, current implementation, and Miro evidence. Ensure each story can be tested and reviewed independently; dependencies should be explicit.

## Integration boundaries and fallbacks

- **Miro:** use read tools only in the lab. If the MCP/plugin is unavailable, provide a board export and have learners record that fallback. Do not treat board content as authoritative without provenance/approval.
- **Jira:** create only trainer-approved stories in the training project. If write tools are unavailable, learners prepare the batch and a trainer enters it; then learners retrieve each story from Jira for implementation. This still exercises live story-by-story intake.
- **Figma:** use only for UI-bearing work. If absent, teach learners to identify that it is not applicable instead of fabricating visual requirements.
- **Credentials/configuration:** merge MCP entries; never replace existing servers. Keep Jira token and Figma key in local environment/ignored files, use Miro OAuth, and verify access to the exact training resources. Do not put credentials in the overlay, prompts, commits, or screenshots.
- **Git:** pushing is part of the lab. Use story-specific branches and commits. No force-push, no secrets, and no unrelated local files. Follow the team's review policy for dependent branches.
- **CI/deployment:** Module 9 records remote push and any immediately available checks. Module 10 performs the full CI/runtime/deployment loop; don't claim CI/deploy success without observed evidence.

## Facilitation

- Ask participants to use bounded prompts: one board/frame, one Jira story, one code path. The goal is an inspectable chain, not a giant agent run.
- Review the story set before creation. Reject stories that turn ambiguous Miro notes into requirements, omit error/empty cases, lack testable acceptance, or duplicate backlog work.
- Before implementation, ask learners to read the story back from Jira and resolve drift against the local spec. Jira is the current work item, while approved requirements remain the scope authority.
- Require code citations to be verified in source and a regression test to pass before code changes where feasible.
- Inspect each branch/diff/test report before allowing the push. Then verify the actual remote branch/commit and log the observed result.
- Ask whether the next story depends on this one and which base it should use. Do not let learners build a chain on top of unreviewed, unmerged code without explicitly recording the risk.
- Figma does not apply to the current API-only project unless a UI track/artifact is introduced. Be candid about this limitation.

## Completion evidence

Each group should show: Miro source references and approval distinctions; reviewed Jira stories and read-back keys; per-story code maps, tests and diffs; story branches/commits and observed pushes; and a delivery log that accurately identifies the next story and its base.
