# Module 8 — Prompt cards

Use these prompts as review assistance. Supply the real branch artifacts and inspect every claim against source, tests, and command output.

## 1. Review the complete change

```text
Review this branch against its base and the approved requirements, specification, and task list. Do not edit files. Inspect the full diff, including tests and configuration. Report only actionable findings, each with severity, file/line, the violated criterion or risk, and evidence. Check for unintended changes, missed requirements, incorrect edge cases, validation and error behavior, authorization, secrets/data exposure, dependency changes, and test gaps. Separate confirmed defects from questions and style preferences. Do not claim tests or CI passed unless you inspect their actual output/status.
```

## 2. Check one finding

```text
Investigate this review finding: [finding]. Do not edit. Trace the relevant route/model/helper and existing tests. Determine whether the issue is real, what input or state reproduces it, which approved criterion or security rule applies, and the smallest test that would demonstrate it. Identify any uncertainty instead of guessing.
```

## 3. Correct a verified issue

```text
Fix only this verified finding: [finding], for criterion/risk [reference]. First add or update the focused regression test. Then make the smallest implementation change consistent with existing validation, authorization, and error conventions. Do not add dependencies or broaden scope without approval. Show the diff and run the focused test; report the exact command and result. Do not update task status based on an unobserved result.
```

## 4. Final pre-PR review

```text
Do not edit. Review the final branch diff against [base branch], the approved criteria, and current test/CI evidence. Report changed files, any remaining correctness/security/compatibility findings, dependency changes, exact checks and their observed status, and whether the evidence supports requesting review. Identify missing evidence plainly. Do not merge, push, or create a pull request.
```
