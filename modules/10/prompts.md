# Module 10 — Prompt cards

## 1. Review the workflow before adding it

```text
Do not edit files. Inspect the Target project's current workflow files, test configuration, dependency manifests, and runtime entry point. Compare them with the proposed Module 10 GitHub Actions workflow. Report exact commands and paths, trigger/permission implications, missing assumptions, and any conflict with existing CI. Do not assume GitHub Actions is enabled or that a workflow run passed.
```

## 2. Diagnose a specific CI failure

```text
Analyze this GitHub Actions run: [run URL]. Use the logs for the exact branch and commit [SHA]. Do not edit yet. Identify the first failing step, relevant error lines, likely cause category (application/test/dependency/workflow/environment), whether it reproduces locally, and the smallest correction. Check whether the failure is deterministic or flaky. Do not claim the whole pipeline passed.
```

## 3. Fix and verify

```text
Fix only the confirmed cause of CI failure [finding] on branch [branch]. Preserve the intended checks and existing acceptance criteria. Do not skip/soften tests, broaden permissions, add secrets, or change deployment behavior to get a green status. Show the diff, run the relevant local command, and tell me which exact new CI run/commit should be checked after push. Do not claim remote CI success until that run is observed.
```

## 4. Review runtime/deployment evidence

```text
Review the local/CI/staging evidence for revision [SHA]. Separate test results, CI status, deployment status, health/smoke results, and logs. Identify any missing or conflicting evidence and the next safe diagnostic step. Do not infer runtime health from a successful deploy action or invent an environment/revision.
```
