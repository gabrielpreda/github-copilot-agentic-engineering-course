# Agentic Engineering with GitHub Copilot — Training Materials

This is the instructor-owned **Training materials project**. It contains the participant guides and the exact files participants copy into their separate **Target project** during a module.

## Course overview

The course follows one small Python FastAPI Task API through a sequence of increasingly realistic engineering tasks. Participants use GitHub Copilot as an assistant while keeping responsibility for scope, tests, review, and delivery. Modules 1–12 have participant materials in this repository. See [`course-map.md`](course-map.md) for the Target-project progression and exact artifact plan.

| Module | What participants do |
|---|---|
| [1. Copilot and project context](modules/01/participant-guide.md) | Explore a deliberately small Task API, compare work with and without repository context, then add `.github/copilot-instructions.md` to the separate Target project. |
| [2. Skills, Hooks, and MCP](modules/02/README.md) | Add a reusable API review Skill, explore bounded tool-use Hooks, and connect a read-only GitHub MCP server to retrieve issue context. |
| [3. Testing and feedback](modules/03/README.md) | Set up pytest, inspect a failing validation case, use a regression test to diagnose and fix whitespace-only task titles, and verify the result. |
| [4. Requirements](modules/04/README.md) | Read the request, current code/tests, and Miro flow; clarify evidence and produce traceable draft requirements. |
| [5. Lightweight Spec-Driven Development](modules/05/README.md) | Turn reviewed requirements into a spec and dependency-ordered stories/tasks linked to acceptance criteria and tests. |
| [6. Incremental implementation](modules/06/README.md) | Implement the first story in test-backed steps, review each diff, and hand off verified status. |
| [7. Capstone part I](modules/07/README.md) | Select a substantial feature and build its first focused vertical slice from the reviewed story/spec on a branch. |
| [8. Review and safeguards](modules/08/README.md) | Review the capstone diff and tests, check validation, authorization, dependencies, and security requirements, correct a verified issue, and record local/CI evidence before PR preparation. |
| [9. Miro-to-Jira story delivery loop](modules/09/README.md) | Read Miro evidence, review/create Jira stories, then read, test, implement, commit, and push each story sequentially while preserving existing behavior. |
| [10. GitHub Actions CI and runtime verification](modules/10/README.md) | Run CI on pushes and pull requests with tests plus a live API smoke check, diagnose a failure, and optionally deploy to an approved Cloud Run staging service. |
| [11. Capstone part II: pull request to verified result](modules/11/README.md) | Finish the capstone, open and complete a pull request using Module 10's CI checks, then verify locally or in the prepared staging environment and present decisions, evidence, and limitations. |
| [12. Practical judgment and wrap-up](modules/12/README.md) | Assess the full delivery workflow, decide where Copilot helps and where human judgment is essential, and agree on proportionate team practices. |

Modules 1–11 continue the same Target project; Module 12 closes with reflection and team practices. Miro is a product-evidence source from Module 4 onward; Jira becomes the story source of truth for sequential implementation. Figma is used when a UI-bearing feature and design frame are in scope. The current Task API is UI-less, so Figma is not a required input for API-only stories. Each module guide identifies whether artifacts should be added, replaced, or merged. Do not use this Training materials project as the application's working repository during the labs.

## Repository roles

- `modules/` contains teaching instructions, prompts, and artifacts for participants.
- `modules/01/target-project-starter/` is copied to a participant's Target project to begin Module 1.
- `modules/01/target-overlays/with-instructions/` contains the exact new file to copy into that target halfway through Module 1.
- Files under `target-overlays` preserve their destination paths. A module guide must say whether each file is added or replaces an existing file.
- The Training materials project is not opened as the application's working repository during the lab.

## Module 1 quick start

1. Copy `modules/01/target-project-starter/` into a new Target project folder or repository.
2. Follow `modules/01/participant-guide.md` in order. The first attempt starts with no `.github` directory.
3. For the focused-context attempt, copy the overlay file into the target at the same path. It adds `.github/copilot-instructions.md`.
4. Return the Target project to its original starter state before repeating a prompt; do not compare two attempts on top of each other's edits.
5. Run and inspect the app manually using `/docs`.

## Requirements

Python 3.10 or later. Follow the per-module guide for local setup. This starter is a teaching example, not a production service.
