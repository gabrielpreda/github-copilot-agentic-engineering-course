# Module 10 — GitHub Actions CI and runtime verification

Build a repeatable CI pipeline for the pushed story branches from Module 9. The required GitHub Actions workflow installs the Target project's dependencies, runs its full pytest suite, starts the service, and exercises live HTTP endpoints. Learners inspect actual workflow runs and resolve a seeded CI failure.

## Materials

- `participant-guide.md` — add/merge the workflow, trigger it from a pushed branch and pull request, diagnose failures, and verify runtime behavior.
- `prompts.md` — prompts for CI setup, failure diagnosis, and evidence-based readiness review.
- `trainer-notes.md` — setup, timing, seeded failure, and deployment facilitation.
- `target-overlays/ci/.github/workflows/ci.yml` — GitHub Actions workflow to **ADD** at `.github/workflows/ci.yml` or **MERGE** into the existing CI workflow.
- `target-overlays/ci/scripts/ci_smoke.py` — live API smoke check to **ADD** at `scripts/ci_smoke.py`.
- `target-overlays/runtime/Dockerfile` — optional container definition to **ADD** at `Dockerfile` when using the Cloud Run path.
- `cloud-run-guide.md` — optional, trainer-approved deployment and post-deployment verification path.

## Scope

GitHub Actions CI is the core of Module 10. It runs on pushes, pull requests, and manual dispatch; a green local suite does not substitute for the observed remote run. Cloud Run deployment is an optional, separate CD exercise requiring a prepared project, least-privilege identity, explicit trainer approval, and a rollback/verification plan. Module 11 handles formal PR completion and capstone delivery evidence.
