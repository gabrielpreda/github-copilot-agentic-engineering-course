# Module 11 — Capstone part II: pull request to verified result

Finish the capstone story set, review the complete change, and take it through a pull request using Module 10's CI checks. Present the product evidence, Jira traceability, implementation choices, test/CI results, and remaining limitations. Verify locally or in the prepared staging environment.

## Materials

- `participant-guide.md` — final story completion, PR preparation, review, merge, and verification steps.
- `prompts.md` — prompts for completion audit, PR drafting, review response, and presentation.
- `trainer-notes.md` — facilitation, expected evidence, and fallback paths.
- `target-overlays/pr/.github/pull_request_template.md` — PR template to **ADD** at `.github/pull_request_template.md`.
- `target-overlays/evidence/docs/handoffs/capstone-verification-template.md` — final evidence template to **ADD** at `docs/handoffs/capstone-verification.md` or **MERGE** into an existing handoff.

## Project progression

Module 10 created the CI workflow and runtime smoke check. Module 11 consumes the run attached to the actual PR commit; it does not create a second CI pipeline. Merge only after required review and checks succeed and the authorized reviewer approves. Deployment remains optional and uses only the trainer-prepared staging path from Module 10.
