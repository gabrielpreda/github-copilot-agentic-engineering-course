# Module 12 — Practical judgment and wrap-up

## Purpose

Review the whole capstone delivery journey and decide where Copilot helped, where developer judgment was decisive, and which practices should carry into real team work. The goal is not maximum automation. It is choosing useful assistance while keeping people accountable for requirements, risk, review, and release decisions.

## Learning outcomes

By the end of this session, you can:

- Assess a Copilot-assisted change using repository, story, test, CI, PR, and runtime evidence.
- Identify tasks that are good candidates for assistance and tasks that need more human attention or approval.
- Explain the distinct roles of repository instructions, Skills, Hooks, MCP tools, tests, CI, and human review.
- Choose safeguards proportionate to the change's impact and uncertainty.
- Propose a small, concrete set of team practices with owners and a way to tell whether they help.

## Before you begin

- Bring the Module 11 capstone PR/presentation and verification handoff, including Jira keys, source evidence, test/CI results, and known limitations.
- If the PR or deployment is still awaiting approval, use its actual state. An unfinished external action does not prevent reflection; record it as pending.
- Use `capstone-assessment-checklist.md` to capture evidence. This is a course worksheet and does not need to be copied into the Target project.
- Do not add a new Skill, Hook, MCP connection, GitHub workflow, or dependency in this session. The task is to assess and select practices from what the team has already used.

## Lab A — Reconstruct the delivery path

1. In a small group, trace one capstone story from its source to its final observed state:
   - Miro/Figma evidence and approved requirement (or explain why a source was not applicable).
   - Jira story and acceptance criteria.
   - Repository code map and important existing behavior.
   - Tests, implementation diff, branch and commit.
   - GitHub Actions run and PR/review state.
   - Local or staging/runtime verification and Jira closeout state.
2. Mark every link as **observed**, **reported but not independently checked**, **not applicable**, or **missing**. Do not fill gaps with a plausible narrative.
3. Identify one point where Copilot saved time, one point where it was wrong/incomplete or could have been, and one decision that required a person with product, security, or release responsibility.
4. Complete the evidence section of `capstone-assessment-checklist.md` individually before group discussion.

## Lab B — Decide what to delegate and what to review

1. Classify the tasks below as **good candidate for assistance**, **assistance with close review**, or **human decision/approval required**. Explain the reason and the evidence you would expect:
   - Search the codebase for a route and its tests.
   - Summarize Miro/Figma evidence and draft Jira stories.
   - Decide whether ambiguous behavior is a product requirement.
   - Generate a focused test and implementation for an approved story.
   - Judge whether authorization or input validation is sufficient.
   - Diagnose a CI failure from logs.
   - Approve a Jira write, commit, push, PR merge, or deployment.
   - Decide whether a production incident or limitation is acceptable.
2. Revisit actual capstone events. Replace abstract judgments with a specific prompt, diff, test result, review comment, or tool result.
3. Discuss when a Skill or agent profile improved consistency, when a Hook added useful visibility, and when an MCP source changed the quality of the decision. Also name at least one case where a tool configuration did not guarantee correctness or permission.

## Lab C — Choose proportionate safeguards

1. Select one low-risk, one medium-risk, and one high-impact change from the capstone workflow or your team's work.
2. For each, choose only the safeguards that address the actual risk: targeted tests, full regression suite, code review, authorization/security review, dependency review, branch protection/status checks, staging verification, rollback plan, or human approval.
3. Explain which safeguard catches which failure. Avoid adding ceremony that does not reduce a meaningful risk, and do not remove a needed control just because a tool reports success.
4. Complete the proportionality section of the checklist. Include a case where you would intentionally avoid using an agent or external tool.

## Lab D — Agree on team practices

1. Each participant proposes one practice that is specific, small, and observable. Examples: “For API behavior changes, link each acceptance criterion to a test in the PR” or “Before Jira story creation, review the proposed batch and source links.”
2. As a team, choose no more than five practices. For each, name an owner, when it applies, and a signal to review after a few weeks.
3. Include practices for preserving human approval at external write gates and for reporting test/CI/deployment evidence accurately.
4. Record the agreed practices in the team checklist. Do not change repository policy, enable organization settings, or configure new tools as part of this discussion.

## Completion criteria

- The capstone was assessed from evidence across product source, Jira, code, tests, CI, PR, and runtime where applicable.
- Participants identified a useful Copilot contribution and a limit or risk that required human verification.
- The team distinguished assistance from product/security/release decisions that require an accountable person.
- Safeguards were selected in proportion to impact and connected to specific risks.
- The group agreed on a short, observable set of team practices with owners and a review signal.
- No new tool, Skill, Hook, workflow, dependency, or cloud setting was added as a substitute for judgment.
