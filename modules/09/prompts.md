# Module 9 — Prompt cards

Use these prompts with the connected Miro/Jira tools where available. Review every proposed story and edit. The prompt does not authorize a tool write by itself; follow the trainer's access and review process.

## 1. Read a Miro flow

```text
Do not edit or create anything. Inspect only Miro board [board URL/name], frame [frame name]. Summarize the flow relevant to [feature] with exact board/frame/object references. Separate approved decisions, proposals, assumptions, and open questions; report ownership/status where visible. Compare it with [requirements/spec] and identify conflicts or missing behavior. If Figma frame [link] is relevant, compare its states and interactions; otherwise say UI evidence is not applicable. Do not turn ambiguous diagram content into requirements.
```

## 2. Propose Jira stories from approved evidence

```text
Do not call Jira create/update tools yet. Use approved criteria [IDs], Miro evidence [locations], and spec [path] to propose a dependency-ordered set of small Jira stories. Each story needs a title, user value, scope, observable acceptance criteria, exclusions, test ideas, and source links. Keep open decisions out of implementation-ready criteria. Check for overlap with existing Jira work. Show the proposed stories for review and identify any criterion with no story.
```

## 3. Create the reviewed stories

```text
Create only the stories I have explicitly approved below in training Jira project [key]: [approved story list]. Preserve the reviewed text and links. Do not create duplicates; search first. After creation, read each created story back and report its key, title, acceptance criteria, links, and status. Do not transition status or modify unrelated Jira issues.
```

## 4. Intake one story before coding

```text
Do not edit files. Read Jira story [key] as it currently exists. Compare its description, acceptance criteria, status, dependencies, and links with [requirements/spec/handoff]. Summarize the requested behavior and exclusions, then map likely code/test locations using targeted searches. Identify ambiguity, conflicting sources, existing behavior to preserve, and a focused regression-test plan. Do not implement until I confirm the story is ready.
```

## 5. Test and implement one story

```text
Work only on Jira story [key] and acceptance criteria [IDs]. Use the inspected code map and the live story, not a prior summary. First add or confirm focused regression tests for important existing behavior, then add story-specific tests and show the test diff. After review, implement the smallest coherent change. Preserve unrelated features, validation, authorization, security rules, and compatibility. Run focused and relevant regression tests; report exact commands and results. Do not start another story or push until I review the diff and evidence.
```

## 6. Prepare a story branch for push

```text
Do not push or edit. Review branch [branch] against [base] and Jira story [key]. Check acceptance coverage, tests actually run, unintended changes, security/authorization/validation, dependencies, secrets, and whether the branch contains unrelated work. Report remaining blockers and exact evidence. If ready, propose a commit message containing [key]. Do not claim CI passed unless the run was observed.
```

## 7. Handoff before the next story

```text
Do not edit or push. Update the delivery log with the verified status of story [key]: branch, commit, changed files, exact tests/results, remote push confirmation supplied by me, review/CI status, and unresolved issues. Clearly state whether dependent story [next key] may start and what base it should use. Do not mark work complete from an unobserved tool result.
```
