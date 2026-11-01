# Agentic Engineering with GitHub Copilot — Training Materials

This is the instructor-owned **Training materials project**. It contains the participant guides and the exact files participants copy into their separate **Target project** during a module.

## Current status

Module 1 is authored as a runnable first lab. Its target application is intentionally small: a Python FastAPI task service with no UI, Skills, Hooks, MCP configuration, or prebuilt delivery workflow. The only Copilot customization introduced in Module 1 is added midway through the lab: `.github/copilot-instructions.md`.

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
