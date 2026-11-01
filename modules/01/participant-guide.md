# Module 1 — How Copilot works with project context

## Purpose

Use a simple Python service to see how Copilot responds to a bounded coding task, how repository guidance changes its context, how model choice affects the result, and when to continue or restart a chat session.

The target application deliberately begins without Skills, Hooks, MCP, custom agents, or a prescribed agent workflow. You will add one repository-instructions file during this module.

## Learning outcomes

By the end of the lab, you can:

- Give Copilot a bounded change request and inspect the code it proposes.
- Compare the same task with and without focused repository instructions.
- Compare responses from two models when two are available in your Copilot account.
- Continue a chat for a related follow-up and start a fresh chat for a separate task.
- Verify the service manually and describe the limits of what you checked.

## Before you begin

- Use the GitHub account and Copilot-enabled VS Code setup confirmed by the trainer.
- Have Python 3.10+ available.
- Copy `target-project-starter/` into a separate working folder/repository. Open that copied **Target project** in VS Code. Do not open the Training materials project as the application workspace.
- Install and start the app using the Target project's README. Open `http://127.0.0.1:8000/docs` and confirm the existing endpoints work.
- Keep a clean copy of the starter or create a Git commit before the first attempt. You will reset to this exact state before repeating the task.

## Starting point

The starter is a tiny in-memory task API:

- `GET /healthz` checks that the service is running.
- `GET /tasks` returns all tasks.
- `POST /tasks` creates a task with a title and a `completed` flag.

There is no database, UI, authentication, test suite, Skill, Hook, MCP configuration, or `.github/copilot-instructions.md` in the starting target.

## Lab A — First Copilot change, without repository instructions

1. Confirm that `.github/copilot-instructions.md` does not exist in the Target project.
2. Start a new Copilot Chat. Select Agent mode if available for the course setup.
3. Paste this same request as written:

   > Add an optional `completed` query parameter to `GET /tasks`. When omitted, return all tasks. When true or false is supplied, return only tasks with that completion value. Keep the change limited to this behavior. Explain what you changed and how I can verify it.

4. Review the proposed changes before accepting them. Ask Copilot to clarify any assumptions rather than accepting unexplained changes.
5. Run the service and manually verify all three cases in `/docs`: parameter omitted, `completed=true`, and `completed=false`.
6. Record: changed files, whether behavior matched the request, extra changes, assumptions, and how easy the result was to verify.
7. Save the diff or commit the result as **Attempt A**.

## Lab B — Repeat with focused repository context

1. Restore the Target project to the original starter state. Do not leave Attempt A's code in place.
2. Copy the supplied overlay into the Target project:

   **ADD** `target-overlays/with-instructions/.github/copilot-instructions.md` as **`.github/copilot-instructions.md`**.

   This is a new file; it does not overwrite a file in the starter.
3. Start a fresh Copilot Chat and submit the exact same request from Lab A.
4. Review, accept, run, and manually verify the same three cases.
5. Record the same observations and save the result as **Attempt B**.
6. Compare the two diffs and results. Focus on correctness, scope, assumptions, and ease of verification. Do not assume that the guided attempt must be better; use what you observed.

## Lab C — Compare models (when available)

1. Restore the Target project to the original starter state again.
2. If your account exposes at least two models approved for the training, select one model and submit the Lab A request. Save its response/diff as **Model 1**.
3. Reset to the starter again, select another available model, and submit exactly the same request. Save it as **Model 2**.
4. Compare what each model changed and how well it met the request. Note response quality, speed, context needs, and any organizational constraints shown by the account.
5. If only one model is available, record that limitation and compare two response strategies from that model only if the trainer asks you to; do not spend time trying to enable an unapproved model.

## Lab D — Continue or restart a session

1. Keep the better-verified implementation from Lab A or B.
2. In the same Copilot session, ask a related follow-up: `Explain how the completed filter handles tasks when there are no matches. Do not change files.` Check the explanation against the code.
3. Start a new chat for a separate task: `Explain how a new task is validated and stored in this application. Do not change files.` Check the answer against the request model and endpoint.
4. Discuss which information came from the repository and which depended on chat history. The key decisions and project facts should be written in repository files when they need to survive a new session; do not treat chat history as durable project documentation.

## Comparison worksheet

| Check | Attempt A: no instructions | Attempt B: instructions | Model comparison, if available |
|---|---|---|---|
| Correct behavior for omitted/true/false | | | |
| Files changed and scope | | | |
| Assumptions or unsupported claims | | | |
| Ease of verifying the result | | | |
| Response speed / context needs | | | |
| What would you ask Copilot to improve? | | | |

## Completion criteria

- You have two cleanly separated attempts from the same starter state.
- You personally checked the three filter cases through the API docs.
- You compared the diffs, not just Copilot's explanations.
- You recorded which models were actually available and avoided claiming a model comparison if only one was available.
- You can explain what repository instructions contributed and what they did not guarantee.

## Trainer discussion

- Did the instructions change the implementation, explanation, or both?
- Did either attempt change files beyond the requested behavior?
- What evidence did manual verification provide, and what did it not prove?
- Which model would you choose for this small task, given the observed quality and speed?
- What should be recorded in repository files rather than retained only in a chat?
