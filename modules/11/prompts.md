# Module 11 — Prompt cards

## 1. Audit capstone completion

```text
Do not edit. Read the approved requirements/spec, current Jira stories, story delivery log, final branch diff, tests, and observed CI/runtime evidence. Build a criterion-to-story-to-code-to-verification table. Identify incomplete or unsupported claims, deferred work, security/compatibility concerns, and blockers to a PR. Cite paths, issue keys, commits, and run IDs where available. Do not infer remote state or mark work complete from a summary.
```

## 2. Draft a pull request

```text
Draft (do not create) a PR for branch [head] targeting [base]. Use the repository PR template. Summarize the user outcome, scope, linked Jira keys, criteria implemented/deferred, important decisions, exact local tests and results, CI run for the head commit, runtime verification, limitations, and rollback/follow-up where relevant. Compare every claim with the actual diff and evidence. Flag missing evidence rather than filling gaps.
```

## 3. Triage review feedback

```text
Analyze this PR feedback: [comment/review]. Do not edit or reply. Compare it with approved criteria, current behavior, tests, security requirements, and scope. Classify it as a confirmed defect, valid in-scope request, scope decision needed, or optional preference. Propose a focused test/fix or a concise evidence-backed response. Identify whether requirements/Jira need an approved update.
```

## 4. Final verification report

```text
Do not edit. Prepare a concise capstone report from the current source systems: Jira statuses, PR/review/merge state, commit SHA, local test commands/results, GitHub Actions run ID/result for the relevant commit, and staging/runtime evidence if present. Separate verified facts from limitations and unrun checks. Do not call the change deployed or complete unless the observed state supports that claim.
```
