# Module 8 — Trainer notes

## Suggested timing (90–120 minutes)

- 10 min: establish branch/base and working-tree context.
- 20 min: learner-led review of the sample patch.
- 15 min: compare findings and discuss severity/evidence.
- 35–55 min: inspect and improve the participant's capstone branch.
- 10–20 min: final diff, test/CI evidence, and handoff.

## Preparation

1. Ensure participants have their Module 7 Target project, feature branch, requirements/spec/tasks, and handoff. Do not replace their local project with a trainer copy.
2. Verify the local test command and, where configured, the CI workflow and how to inspect its run. The sample exercise is framework-neutral enough to discuss even where a participant implementation differs.
3. Remind participants the sample patch is an inspection artifact and must not be applied to their Target project.
4. Review each participant's chosen feature and note a likely edge case or requirement coverage gap, but let them review independently first.

## Exercise answer key — keep hidden until Lab B

The sample patch has multiple findings. Learners should support each with evidence from the brief and patch; exact severity may depend on the application's documented security model.

1. **Authorization is absent.** A client-side visibility check is not an authorization boundary. The route calls the service without an authenticated principal or server-side ownership/access check. This is a blocking security finding if tasks are protected, as the criterion explicitly requires existing authorization rules.
2. **Filter input bypasses the existing contract.** `owner_id` changes from an integer to a string. The nonnumeric test expects success, contradicting the specified 422 behavior and the existing list signature's validation. Check whether the real service even accepts a string.
3. **The test asserts the wrong behavior and too little.** It encodes a 200 for invalid input, and only checks that the body is a list. It does not establish completed-only filtering, owner filtering, response shape, or authorization.
4. **Unnecessary/bogus dependency entry.** Python's `json` module is in the standard library; it must not be added to `requirements.txt` as a runtime package. This may also make dependency installation fail or resolve an unrelated distribution. Remove it and inspect lockfiles if any.
5. **Unnecessary serialization round trip.** `json.dumps` followed by `json.loads` and `default=str` may stringify unsupported values and conceal response-shape/type problems. Use the application's established response serialization and test the contract.
6. **Route matching/order risk.** In some frameworks or routers, a dynamic `/tasks/{task_id}` route declared earlier can capture `export` or fail integer parsing. Inspect actual route declarations and registration order; this is context-dependent and should be verified, not asserted blindly.

The endpoint name is a fixed route and the patch claims to leave listing unchanged, but the full existing route table and service behavior must be inspected before concluding there's no collision or regression. There is no evidence of a CI run in the exercise, so learners must not report CI status.

## Facilitation

- Ask learners to separate a finding from a proposed fix. A review comment needs a reproducible behavior or a clear violated criterion/security boundary.
- Have them trace authorization through the server, not infer it from frontend behavior or an integer identifier. If the course Target is intentionally unauthenticated, record that as an explicit project constraint and assess any newly introduced protected resource consistently with that model.
- Discuss dependency hygiene using the actual manifest and lockfile. Do not equate any dependency change with a defect; ask why it is needed, maintained, and permitted by the project.
- Encourage a focused regression test first, then a minimal correction. Changes beyond approved scope should be recorded for a decision rather than implemented silently.
- Distinguish local test results from CI results. A workflow file is not a passing run, and green tests do not prove security or requirement completeness.
- Do not require a finding in every participant's capstone. If review finds no verified defect, a concrete uncovered boundary case is a valid improvement target.
- Keep changes on the capstone branch and do not merge, push, or open a PR in this module.

## Completion evidence

Before ending, check that each learner can show the branch/base, final diff, one verified fix or coverage improvement, exact local check output, actual CI status or explicit unavailability, and a handoff that identifies remaining risks/questions.
