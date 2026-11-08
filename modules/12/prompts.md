# Module 12 — Prompt cards

## 1. Evidence-based capstone reflection

```text
Do not edit files or external systems. Using the capstone evidence I provide (Miro/Figma references, Jira stories, diffs, tests, CI runs, PR review, and runtime results), reconstruct the delivery path. Mark each statement as observed, reported, not applicable, or missing. Identify one useful Copilot contribution, one verified limitation/error or plausible risk, and one human decision that materially affected scope, safety, or release. Do not invent evidence or claim deployment/merge when it is pending.
```

## 2. Delegate or keep human-owned?

```text
Classify each proposed task as: good candidate for assistance, assistance with close review, or human decision/approval required. For each, explain impact and uncertainty, what evidence a person should inspect, and which external actions require separate approval. Tasks: [list]. Avoid assuming automation is safer or faster without context.
```

## 3. Select proportionate safeguards

```text
For this change profile [describe impact, users, data, uncertainty, reversibility], identify the smallest useful set of checks across tests, code review, security/authorization, dependency review, CI, staging, rollback, and human approval. Map each check to a concrete failure it can catch. State what it cannot establish. Do not add process steps without a risk-based reason.
```

## 4. Draft a team practice proposal

```text
Turn these observations into no more than five specific team practices. For each, state the trigger, expected behavior, accountable owner, and a simple signal to review after [time period]. Keep the practices tool-neutral where possible and preserve explicit human approval for external writes and releases. Do not modify repository configuration or create new automation.
```
