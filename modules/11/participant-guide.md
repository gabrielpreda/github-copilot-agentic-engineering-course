# Module 11 — Capstone part II: pull request to verified result

## Purpose

Complete the capstone as a coherent, reviewable change and show evidence from product discovery through verification. Use the existing GitHub Actions workflow from Module 10, prepare a clear PR, respond to review, and verify the merged result locally or in a prepared staging environment.

## Learning outcomes

By the end of this lab, you can:

- Reconcile approved Miro/spec criteria with Jira stories and the implementation.
- Complete remaining capstone work without silently expanding scope.
- Review a complete diff and distinguish required fixes from optional suggestions.
- Prepare a PR that explains user value, scope, verification, and known limitations.
- Confirm CI applies to the PR's exact head commit and respond to failures with a new verified run.
- Present the final result and state clearly what is and is not verified.

## Before you begin

- Continue from Module 10 with the capstone branch, story delivery log, test evidence, CI run links, and any staging results.
- Confirm the intended base branch, repository review policy, required status checks, and who may approve/merge. Do not assume branch protection or a required check exists; inspect the repository configuration or ask the trainer.
- Confirm all Jira stories in the capstone scope are accounted for: implemented, deferred with approval, or blocked with a reason. Resolve stale issue status only through the project's agreed workflow.
- Check the working tree and branch. Preserve unrelated work and keep secrets/generated files out of the PR.
- Copy `target-overlays/pr/.github/pull_request_template.md` to `.github/pull_request_template.md` as **ADD** if no template exists; otherwise merge the relevant sections without overwriting the current template.
- Copy `target-overlays/evidence/docs/handoffs/capstone-verification-template.md` to `docs/handoffs/capstone-verification.md` as **ADD**, or merge it into an existing equivalent handoff. Preserve participant evidence.

## Lab A — Finish and reconcile the capstone

1. Read the latest approved requirements/spec and every live Jira story in the selected capstone scope. Recheck Miro/Figma evidence only where it affects an unresolved or changed criterion.
2. Make a criterion-to-story-to-code-to-test table. For each criterion, show the implementation location and the test or other observable verification. Mark criteria that are incomplete, deferred, or not approved; do not call them complete.
3. Implement only the remaining approved work. Use a separate story branch/PR if the remaining change is independently reviewable; otherwise follow the trainer's agreed capstone branch policy.
4. Preserve important existing behavior with regression tests. Run focused tests, then the full local suite. Record exact commands/results and inspect the diff against the criteria.
5. Review dependencies, validation, authorization, security, compatibility, generated files, secrets, and unrelated changes. Resolve blocking findings before requesting review; record accepted non-blocking limitations.
6. Update the story delivery log and final verification evidence from observed facts. Do not infer remote CI, PR, Jira, or deployment state from local output.

## Lab B — Prepare the pull request

1. Confirm the branch is pushed and contains only the intended capstone change. Inspect its base and full diff (`git diff <base>...HEAD`) as well as any uncommitted files.
2. Draft the PR with the supplied template. Include the user outcome, scope, linked Jira story keys, criteria covered/deferred, design/source references, key implementation decisions, tests and exact results, CI run, runtime/staging verification if available, and limitations/risks.
3. Check that the PR targets the correct base and that its head commit matches the commit you reviewed. Avoid unsupported claims such as “all requirements complete” or “deployed successfully” without evidence.
4. Review the exact PR title/body and requested reviewers with the trainer. Create the PR through GitHub UI/MCP only when the course's authorization and review expectations are satisfied. If no write permission exists, prepare a draft PR packet or use the trainer demonstration.
5. Open the PR's Checks view. Confirm the Module 10 workflow ran on this PR/head commit, and inspect every required job. A previous green run for another commit is not sufficient.

## Lab C — Review, correct, and complete

1. Review the PR as a teammate. Check the change against its stated criteria, tests, and security/compatibility concerns. If using a trainer-provided review, distinguish actionable findings from preferences.
2. For each requested change, decide whether it is in scope. If accepted, add/adjust a focused test, make a bounded correction, push a new commit, and inspect the new CI run. If it changes product scope, record the decision and update Jira/requirements through the authorized workflow before implementation.
3. Do not dismiss a failing check, reduce test coverage, or merge around required review. If the workflow is unavailable or blocked, record the actual cause and follow the trainer fallback.
4. Merge only after required checks and human review pass and the authorized maintainer approves. If learners do not have merge permission, leave the PR ready and have the trainer perform or demonstrate the merge.
5. After merge, verify the integration branch contains the expected commit. Run the relevant suite from the merged state or inspect the successful required CI run for that merge commit.
6. If a prepared staging environment is available, follow Module 10's approved deployment/verification process. Otherwise verify locally and state that deployment was not performed.
7. Update Jira to Done only after the project's completion conditions are met and the relevant status transition is approved. Record the PR, merge commit, CI run, and runtime evidence in the capstone verification handoff.

## Lab D — Present the result

Give a short presentation covering:

1. The user problem and the Miro/Figma evidence that informed the work.
2. The Jira stories and acceptance criteria delivered, deferred, or left open.
3. One important implementation/test decision and one review finding or edge case.
4. The PR and exact CI/test evidence; show runtime/deployment evidence only if actually observed.
5. Known limitations, follow-up work, and what would be required before production use.

## Completion criteria

- Every approved criterion has an honest status and traceable implementation/verification evidence or an explicit deferral.
- The final diff is focused and reviewed; relevant local tests and the PR's CI run are tied to the correct commits.
- A clear PR was created and completed, or a review-ready PR packet/fallback was presented where permissions prevented PR operations.
- Review findings were addressed or documented; no required check/review was bypassed.
- The merged result was verified, or the PR is explicitly left awaiting authorized review/merge.
- Runtime/deployment claims match observed evidence, and remaining limitations were presented.
