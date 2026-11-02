# Module 2 — Prompt cards

Use these prompts in the Target project. Keep each lab in a fresh Copilot Agent chat so observations from one customization do not carry into another.

## Lab 2A — Skill review

> Review the Task API contract in this repository. Do not change files. Identify each endpoint, the request and response fields, and the validation rules visible in the code. Explain how a participant could manually inspect the behavior through `/docs`. Use the `api-contract-review` Skill if it is available, and say which repository files support your conclusions.

## Lab 2B — Hook observation

Use the same prompt before and after adding the Hook:

> Read the Target project's README and summarize the API endpoints it documents. Do not change files and do not run commands.

The Hook commands in the supplied `audit.json` use `python3` and pass a `before` or `after` label so the diagnostic is easy to read. These labels are command arguments; the Hook event itself still arrives as JSON on standard input.

- On Windows, if `python3` is not available in the VS Code process environment, edit both `command` values to use `py -3 .github/hooks/audit_tool_use.py before` and `py -3 .github/hooks/audit_tool_use.py after` (or the Python launcher confirmed by your trainer).
- On macOS or Linux, keep `python3 .github/hooks/audit_tool_use.py before` for `preToolUse` and `python3 .github/hooks/audit_tool_use.py after` for `postToolUse`.

Keep the `before` label with `preToolUse` and the `after` label with `postToolUse`. The script receives the event data as JSON on standard input; do not add prompt text, tool arguments, or secrets to the command.

## Lab 2C — MCP issue lookup and README change

Replace `<OWNER>`, `<REPOSITORY>`, and `<ISSUE_NUMBER>` with the values provided by your trainer:

> Use the GitHub MCP server's read-only tools to retrieve issue #<ISSUE_NUMBER> from <OWNER>/<REPOSITORY>. First summarize its acceptance criteria and cite the issue number. Then update only this Target project's README.md to satisfy those criteria. Do not change application code, dependencies, tests, or other files. Do not create or edit GitHub content. Show me the local diff and identify any criterion that is ambiguous or missing.
