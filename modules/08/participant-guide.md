# Module 8 — Review and basic engineering safeguards

## Purpose

Review a Copilot-assisted change as an engineer responsible for its behavior and safety. Find gaps between the request, implementation, and tests; correct the highest-value issues; and gather evidence before proposing a pull request.

## Learning outcomes

By the end of this lab, you can:

- Inspect a branch diff and test changes for unintended edits and missed requirements.
- Review input validation, authorization boundaries, dependency changes, and application security requirements.
- Use a review checklist, branch discipline, and CI results as safeguards without treating any one of them as proof of correctness.
- Make a focused correction, rerun checks, and record evidence for reviewers.

## Before you begin

- Continue in the Target project from Module 7. Check `git status` and the current branch first; preserve participant work.
- Work on the existing capstone branch. If the branch was never created, create it now before editing. Do not commit unrelated or sensitive files.
- Locate the selected track's requirements, spec, tasks, tests, and Module 7 handoff. Record missing artifacts or draft approval status as review context.
- Confirm the baseline test command and available CI workflow from the Target project. Do not assume a CI run passed because a workflow exists.
- No files from `review-exercise/` should be copied into the Target project. It is an inspection-only example.

## Lab A — Establish what is being reviewed

1. Record the branch and working-tree state. Separate pre-existing local work from the capstone diff; do not discard unknown changes.
2. Identify the intended base branch and inspect the complete change, including staged, unstaged, and committed branch changes as appropriate. Useful commands include:

   ```bash
   git status --short --branch
   git diff --stat
   git diff
   git diff <base-branch>...HEAD
   ```

   Substitute the actual base branch. Do not use a command that hides uncommitted changes.
3. Read the approved requirements/spec and task list before judging implementation. List the criteria the change claims to satisfy.
4. Inspect tests and test output directly. Note which tests were actually run, their exact command, and whether they cover normal, boundary, invalid, and failure cases.
5. Use the review prompt in `prompts.md`. Ask Copilot to report findings with file/line, impact, and evidence. Treat its report as leads to verify, not as approval.

## Lab B — Review the deliberately flawed change

1. Read `review-exercise/issue-brief.md` and inspect `review-exercise/copilot-change.diff` as text. Do not apply it.
2. Independently list issues before reading the answer key in `trainer-notes.md`. Classify each as a correctness/security issue, a missed requirement, a test gap, or a process concern.
3. Check specifically for:
   - Validation at the API boundary and consistency with existing error responses.
   - Authorization checks on every route that reads or changes protected data; do not infer authorization from an identifier or UI behavior.
   - Dependency additions, version changes, lockfile consistency, and whether new packages are necessary.
   - Exposure of secrets or sensitive data, unsafe logging, injection risks, and alignment with repository security instructions.
   - Tests that prove the acceptance criteria and reproduce defects, rather than only mirroring the implementation.
4. Compare your findings with the trainer answer key. Explain which issues block review, which are follow-up concerns, and what evidence supports each decision.

## Lab C — Improve the capstone branch

1. Select at least one verified finding in your own capstone diff. If no defect is found, choose a meaningful uncovered requirement or edge case and improve its test coverage.
2. Write a failing focused test or a precise review observation first. Make a small fix that stays within approved scope. If the fix changes behavior beyond the approved criteria, pause that change and record it for requester approval instead of silently expanding scope.
3. Inspect the resulting diff for unrelated edits, generated files, credentials, unsafe examples, and dependency churn. Check that tests do not weaken or skip existing assertions to get green.
4. Run the focused tests and relevant regression suite. If CI is available, inspect the run associated with this branch/commit and report its actual status. If CI is unavailable, state that and give local evidence; do not claim CI passed.
5. Review the final diff again against acceptance criteria. Update the task/handoff evidence with exact commands and results, unresolved findings, and any security or compatibility questions.

## Completion criteria

- The reviewed change and its base are identified; working-tree changes are accounted for.
- Findings cite observable evidence and distinguish defects from preferences.
- Input validation, authorization, dependency changes, tests, and relevant security requirements were considered.
- At least one verified issue or meaningful coverage gap was corrected on the feature branch.
- Relevant local tests were run and CI status is reported accurately, including when unavailable.
- The final diff is focused, reviewable, and ready for the next module's pull-request preparation; it is not merged.
