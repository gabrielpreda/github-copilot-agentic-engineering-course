# Module 11 — Trainer notes

## Suggested timing (2–3 hours)

- 25 min: capstone traceability and completion audit.
- 35 min: final diff and local test review.
- 25 min: PR preparation and status-check inspection.
- 30–45 min: review feedback, correction, and rerun CI.
- 20 min: merge/verified-result path or trainer demonstration.
- 20–30 min: capstone presentations.

## Preparation

1. Confirm participants have Module 9 story branches/logs and Module 10 CI runs. Ensure a CI workflow is present in the Target repository and has succeeded at least once on a relevant branch.
2. Decide which participants can create PRs, request reviewers, merge, update Jira, and deploy. Provide a trainer-operated fallback where these permissions are intentionally withheld.
3. Confirm the integration branch and any required status checks/review policy in GitHub. Do not tell learners that a branch is protected or a check is required until verified.
4. Provide a staging service only if it is non-production, budgeted, and access/rollback details are prepared. Otherwise make local verification the standard path.
5. Seed a realistic review comment for discussion (for example, a missing boundary test or a claim in the PR body that lacks evidence). Do not seed a defect that requires unapproved scope expansion.

## Facilitation

- Require traceability from Miro decision to approved requirement, Jira story, code, test, PR, and observed CI result. Let learners mark legitimate deferrals rather than hide them.
- Keep Module 10 and 11 responsibilities distinct: Module 10 authors and diagnoses the CI workflow; Module 11 consumes the workflow as PR evidence and responds to findings.
- Verify the CI run corresponds to the current PR head SHA. A green run on an earlier commit does not verify later changes.
- Ask reviewers to explain why each comment matters and what evidence would resolve it. Distinguish required corrections from optional preferences.
- Follow repository policy for merge and Jira status. If the trainer performs an external write, show the action and verify the resulting state.
- Use local verification if no staging access is prepared. Do not make deployment a prerequisite for a valid course completion.
- Presentations should include one human judgment call, one Copilot contribution, and one limitation or follow-up—not just a feature demo.

## Completion evidence

Each group shows the criterion map, final diff, tests, PR and exact CI status, review disposition, merge/awaiting-approval status, runtime evidence or explicit local-only path, and a clear presentation of limitations.
