# Module 1 — Trainer notes

## Suggested timing (90 minutes; adjust to cohort)

- 10 min: orient participants to Copilot Chat, model selector, and the Target project.
- 15 min: run app and complete Attempt A.
- 15 min: reset, add the repository instructions overlay, complete Attempt B.
- 15 min: compare available models or discuss account limitations.
- 10 min: continue one session and start a new one for the separate explanation task.
- 15 min: pair comparison and debrief.
- 10 min: buffer for setup and questions.

## Trainer setup

1. Provide the starter folder as a repository template or distribute a fresh copy per participant/pair.
2. Ensure the target starts clean, has no `.github` directory, and has no files from later modules.
3. Confirm Python and dependency installation before class. Do not preconfigure MCP or add agent/skill files.
4. Check which Copilot modes and models are exposed in the actual training accounts. Model availability varies by plan, policy, and client version; do not promise a specific comparison.
5. Keep the overlay separate from the starter so the first attempt genuinely has no repository instruction file.

## Facilitation guardrails

- This is an introductory Copilot lab, not an exercise in writing the perfect prompt. Let participants inspect what happens with the same bounded request.
- Ask learners to review changes before accepting them and to verify observable behavior.
- Encourage a clean reset between attempts. Comparing cumulative edits invalidates the comparison.
- The instructions file expresses conventions; it cannot guarantee correctness or replace review.
- Do not require a commit or push. Keep the exercise local unless the course environment explicitly calls for a remote repository.
- If model selection is unavailable, document that and continue; do not delay the group.

## Expected implementation shape

The filter can be implemented by adding an optional boolean query parameter to the existing `GET /tasks` endpoint and filtering the in-memory list only when the parameter is supplied. Exact code structure may differ. Review behavior, scope, and verification rather than requiring identical code.
