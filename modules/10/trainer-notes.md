# Module 10 — Trainer notes

## Suggested timing (2–3 hours)

- 20 min: inspect repository tests, manifests, and current CI configuration.
- 30 min: add/merge the GitHub Actions workflow and smoke script.
- 25 min: push a prepared branch and inspect exact run evidence.
- 35 min: diagnose a seeded CI failure and verify the fix on a new run.
- 20 min: compare in-process tests with live service smoke behavior.
- Optional 30–60 min: approved Cloud Run staging deployment and runtime investigation.

## Preparation

1. Confirm GitHub Actions is enabled for the training Target repository and that students can read run logs. Protect default branch according to the class setup; do not rely on protection being configured unless verified.
2. Check the Target project has Module 3's `requirements-test.txt`, tests, and `pyproject.toml`. Module 9 branches may include feature-specific optional fields; ensure the CI smoke payload remains valid for the selected implementation.
3. Inspect the workflow's action versions before each course run. The current GitHub Python guide uses `actions/checkout@v6` and `actions/setup-python@v5`; verify vendor docs and organizational policy before teaching.
4. Prepare a harmless failing branch or edit (e.g. make the smoke assertion expect the wrong health value), record its intended failure, and keep it out of long-lived learner branches. Do not seed a failure in shared/default branch.
5. For Cloud Run, provide a non-production project and least-privilege identity. If demonstrating GitHub Actions deployment, preconfigure Workload Identity Federation, branch restrictions, protected environment, and approval reviewers. Do not put a service-account key in GitHub secrets as the default teaching pattern.
6. If no cloud environment is available, use the local Docker/runtime path and a prepared example of revision/log evidence. Do not claim a deployment occurred.

## Expected observations

- The workflow runs on every branch push and pull request, with manual dispatch as a diagnostic path. `contents: read` is sufficient for checkout; CI does not need write tokens or cloud credentials.
- The test matrix checks Python 3.10 and 3.12, reflecting the declared minimum and a current supported runtime. Confirm the app dependencies and Pydantic/FastAPI versions work on both for the actual Target branch.
- `pytest` exercises tests in-process through FastAPI TestClient. `ci_smoke.py` starts Uvicorn and sends real HTTP requests, adding a separate runtime/startup check.
- A green job is commit-specific. Learners must inspect run URL, commit SHA, each step, and PR status rather than reporting “CI passes” from the workflow file alone.
- Deployment is not part of ordinary CI. For cloud usage, prefer workload identity federation and a protected GitHub Environment; a push must not deploy automatically.
- Private Cloud Run endpoints need authenticated smoke checks. Do not solve a failing unauthenticated curl by making the service public without a product/security decision.

## Facilitation

- Ask participants to identify CI triggers, branch/PR status checks, Python matrix, minimal permissions, and whether any credentials are exposed.
- Have them map local commands to workflow steps and explain why each is included.
- Seed one failure. Require learners to identify the first failing step and actual commit before proposing a fix. Preserve the failed run in the history.
- Distinguish application failures from setup/runtime failures. If tests pass but the live smoke fails, inspect server startup, port binding, process lifetime, and response contract.
- Do not accept changed/removed tests, `continue-on-error`, broad permissions, or a skipped job as a valid way to green the pipeline.
- Keep Cloud Run deployment optional, separate from CI, and trainer-approved. Review target, access mode, runtime identity, costs, verification, and rollback before deployment.

## Completion evidence

Each group shows the committed workflow, one exact passing run tied to a commit (or recorded fallback), the tested API endpoints, a diagnosed failure/fix or prepared demonstration, and a handoff distinguishing CI from deployment/runtime status.

## References

- [GitHub Actions: Build and test Python](https://docs.github.com/en/actions/tutorials/build-and-test-code/python)
- [Google GitHub Actions authentication (Workload Identity Federation)](https://github.com/google-github-actions/auth)
- [Google GitHub Actions deploy to Cloud Run](https://github.com/google-github-actions/deploy-cloudrun)
- [GitHub Actions deployment environments](https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments)
