# Module 10 — GitHub Actions CI and runtime verification

## Purpose

Make the Module 9 story-by-story workflow verifiable after code leaves a laptop. Add continuous integration with GitHub Actions, run tests and a live API smoke check on pushed code and pull requests, investigate a CI failure, and inspect runtime evidence. Cloud deployment is a separate optional path with its own approval and access requirements.

## Learning outcomes

By the end of this lab, you can:

- Explain when CI runs and what the workflow actually checks.
- Add or merge a GitHub Actions workflow that installs dependencies, runs tests, and exercises the running service.
- Inspect a specific CI run, find the failing step, diagnose the cause, and verify a correction.
- Distinguish local test results, CI results, deployment state, and runtime health evidence.
- Deploy to a prepared Cloud Run staging service only through an approved path, then verify its revision and health.

## Before you begin

- Continue with the Target project and pushed story branches from Module 9. Use a branch with a completed, reviewed story and passing local tests.
- Confirm `tests/`, `requirements-test.txt`, `app/main.py`, and the installable project manifest are present. Resolve or document baseline failures first.
- Confirm GitHub Actions is enabled for the training repository and the workflow can run on the chosen branch. If Actions is unavailable, use a trainer demo and record that CI was not run for your repository.
- Check whether `.github/workflows/ci.yml` or `scripts/ci_smoke.py` already exists. **ADD** files only when absent; otherwise **MERGE** behavior and preserve current workflow triggers, jobs, permissions, and conventions.
- Copy `target-overlays/ci/.github/workflows/ci.yml` to `.github/workflows/ci.yml` (**ADD**, or merge into existing CI). Copy `target-overlays/ci/scripts/ci_smoke.py` to `scripts/ci_smoke.py` (**ADD**). These run the local project's own checks and don't deploy or access secrets.
- Do not add cloud credentials to repository files or workflow YAML. Cloud deployment is optional and requires trainer authorization and a prepared non-production target.

## Lab A — Install and inspect the CI workflow

1. Read the complete workflow before adding it. Identify trigger events, Python versions, permissions, dependencies, test command, smoke check, concurrency, and timeout.
2. Confirm the install commands match the Target project. The supplied workflow assumes Module 3's `requirements-test.txt` and an editable install from `pyproject.toml`.
3. Review that `permissions` uses the minimum required (`contents: read`) and that CI does not receive production secrets or deployment permissions.
4. Add the workflow and smoke script as described above. If merging, retain existing steps and do not overwrite security controls.
5. Run the workflow's test and smoke commands locally if available. Fix path or dependency differences before pushing; don't change tests just to make CI green.

## Lab B — Trigger CI and trace the evidence

1. Push the reviewed Module 9 story branch through the agreed Git workflow. If a push is not authorized or allowed in the class environment, ask the trainer to trigger the run and observe.
2. Open the repository's **Actions** tab and select the run for the exact branch and commit. Confirm it is not an older run from another commit.
3. Inspect each job: checkout, Python setup, dependency installation, pytest, server startup, and live API smoke. Record workflow URL/run ID, branch, commit SHA, job outcome, and step logs.
4. Create or update a pull request if the training workflow requires it. Confirm the `pull_request` trigger runs against the proposed merge and the status check appears on that PR.
5. Explain what CI proves and what it doesn't. It verifies only the checked code, environment, and cases at that commit; it does not prove production behavior, security, or untested requirements.

## Lab C — Diagnose a CI failure

1. The trainer may seed a temporary failure on a separate exercise branch, such as a wrong import path in the smoke script or a test that fails only on Python 3.10. Never inject the seed into a participant's main feature branch.
2. Read the failing step and traceback. Identify whether the cause is code, dependency installation, environment/version differences, workflow configuration, or flaky test behavior.
3. Reproduce the failure locally where possible. Make the smallest correction, add/adjust a test when appropriate, and inspect the diff.
4. Push the correction and verify the new run is attached to the new commit and all required jobs pass. Keep the earlier failed run as learning evidence; do not hide it or claim that it passed.
5. If a failure is environmental or the runner is unavailable, document the exact evidence and use the trainer's prepared run rather than claiming a green result.

## Lab D — Runtime and optional Cloud Run verification

1. The CI smoke script starts Uvicorn in a subprocess, checks `/healthz`, creates a task through HTTP, and checks it appears in `GET /tasks`. Inspect the script and explain the difference from FastAPI's in-process `TestClient` tests.
2. If a trainer-provided staging service is available, follow `cloud-run-guide.md`. The trainer must confirm the project, region, service identity, access mode, and approved source revision before a deployment action.
3. Verify the deployed revision is ready and the health endpoint behaves as expected using an authorized request path. Record the service/revision, URL or resource ID, timestamp, request/result, and logs inspected.
4. Compare local, CI, and deployed behavior. Investigate discrepancies instead of treating a successful deployment command as proof of a healthy service.
5. Do not deploy to production in this exercise. If no staging environment is prepared, use the local container/runtime path and record Cloud Run as not exercised.

## Completion criteria

- The workflow is added or merged without discarding existing workflow behavior.
- A CI run was observed for the exact story branch/commit, or the trainer fallback and limitation are recorded.
- The run checks the test suite and a live service smoke path; outcomes are described from logs.
- At least one failure was diagnosed from evidence and corrected or analyzed using the trainer seed.
- Local, CI, and runtime/deployment evidence are reported separately.
- Optional Cloud Run work used an explicitly approved staging target and records the deployed revision and verification; no production deployment was attempted.
