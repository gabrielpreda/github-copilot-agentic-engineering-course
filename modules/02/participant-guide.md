# Module 2 — Skills, Hooks, and MCP tools

## Purpose

Explore three ways to extend an agent workflow: Skills provide a reusable procedure, Hooks run configured code at a lifecycle event, and MCP connects the agent to an external service. In each lab, inspect the customization, observe what it does, and verify the result.

## Learning outcomes

By the end of these labs, you can:

- Explain when repository instructions are sufficient and when a reusable Skill is useful.
- Add and invoke a repository Skill, then check whether Copilot followed its procedure.
- Inspect a Hook's event, command, permissions, and output before enabling it.
- Explain how an MCP server exposes tools and what access the configured server has.
- Use MCP-provided information in a small change and verify the source and resulting diff.

## Before you begin

- Use the GitHub account and Copilot-enabled VS Code setup confirmed by the trainer. Select **Copilot** as the session target and use **Agent** mode for these labs.
- Start from your Module 1 Target project in a clean state. Keep its application files and any repository instructions you deliberately added in Module 1. Do not open the Training materials project as the Target project.
- Make sure your Target project is a GitHub repository and that you can view its Issues. Lab 2C needs a trainer-prepared issue in that repository.
- Confirm with the trainer that Skills, Hooks, and MCP tools are allowed by the training account and organization policy. Hooks are a preview feature in the VS Code experience; the trainer may run that portion as a demo if it is unavailable.
- Do not paste credentials into chat or commit credentials to the Target project. Lab 2C uses GitHub's browser-based OAuth flow and read-only server settings.

## Lab 2A — Reusable Skill

### What to notice

Repository instructions describe conventions that apply broadly. A Skill packages a procedure for a particular kind of task and is available for Copilot to use when its description matches the request. Discovery makes a Skill available; it does not guarantee the model will load or follow it.

### Steps

1. In the Target project, check whether `.github/skills/api-contract-review/SKILL.md` already exists. If it does, stop and ask the trainer how to handle the existing Skill; do not overwrite it.
2. Copy the supplied file from `target-overlays/2a/.github/skills/api-contract-review/SKILL.md` to the same destination path in the Target project. This is **ADD**.
3. Start a fresh Copilot Agent chat in the Target project. Ask the Lab 2A prompt from `prompts.md` to review the Task API without changing files.
4. Check whether Copilot discovered or loaded the Skill. Inspect its report against `app/main.py` and the Target project's `README.md`.
5. If automatic selection did not happen and the Skill is available as a slash command in your setup, invoke it explicitly and repeat the review. Record the difference between automatic and explicit invocation.
6. Note which steps came from the Skill, which facts came from the repository, and any unsupported claims or omitted details.

### Completion check

- You can locate the Skill and explain its name and description metadata.
- You compared Copilot's report with the actual route and Pydantic models.
- You can explain that a Skill guides work but does not verify correctness by itself.

## Lab 2B — Hook

### What to notice

A Hook is configured code that the agent runtime invokes at a supported lifecycle event. The prepared Hook uses two events: `preToolUse` reports the tool name before it runs, and `postToolUse` reports the tool name after a successful call. Neither Hook approves, denies, or modifies the call. Their output is not a substitute for the VS Code permission prompt.

### Steps

1. Before adding the Hook, use the Lab 2B prompt and notice which tools Copilot uses to inspect the project. This is your baseline.
2. Check whether the Target project already has `.github/hooks/audit.json` or `.github/hooks/audit_tool_use.py`. If either exists, do not overwrite it; ask the trainer for the merge instructions.
3. Copy both files from `target-overlays/2b/.github/hooks/` into the Target project at the same paths. This is **ADD**.
4. Open and read both files. Confirm the event name, command, timeout, input parsing, and the fact that the script outputs `{}` and does not return a permission decision.
5. If the Hook command needs a Python launcher adjustment on your operating system, follow the note in `prompts.md` before starting the session.
6. Start a fresh Copilot Agent session. Repeat the same harmless, read-only Lab 2B prompt. Inspect the Hooks/session output in VS Code and look for a before/after pair for a successful tool call. Identify the observed tool names and confirm normal approval settings remain in effect.
7. Discuss why an unsuccessful or denied tool call may not have a matching `postToolUse` event. Also discuss what could go wrong if a Hook command fails, times out, logs too much information, or runs a mutating command. Do not modify the supplied Hook to deny or auto-approve actions.

### Fallback when Hooks are unavailable

Do not change organization or preview settings. The trainer can inspect the files and demonstrate them in an enabled environment. Participants can trace the event payload and output contract without enabling the Hook locally.

### Completion check

- You can identify the two lifecycle events, commands, and data the script records.
- You observed the before/after diagnostics or completed the trainer-led inspection.
- You can distinguish an observation Hook from a policy or permission control, and explain why a failed call may have no after-event.

## Lab 2C — MCP tools

### Trainer preparation

Before the lab, the trainer creates a GitHub Issue in each participant's Target repository using `issue-brief.md` and records its issue number. Participants need read access to the repository and approval to use the GitHub MCP server. If organization policy or account access blocks it, use the trainer's prepared demonstration or the fallback below.

### Steps

1. Confirm the trainer-prepared Issue is visible in the Target repository. Note its number and verify its acceptance criteria in GitHub before using Copilot.
2. Check whether `.vscode/mcp.json` exists in the Target project.
   - If it does not exist, copy `target-overlays/2c/.vscode/mcp.json` to that path. This is **ADD**.
   - If it already exists, **MERGE** only the supplied `github` server entry into its top-level `servers` object. Preserve other entries and settings. Do not replace the file.
3. Review the configuration. It points to GitHub's hosted MCP endpoint and limits enabled toolsets to repository and issue information in read-only mode. It contains no token.
4. Use VS Code's MCP server controls to start or authenticate to the server. Complete the GitHub OAuth flow in the browser if prompted. Review the requested access before granting it. Do not create or paste a personal access token for this lab.
5. Inspect the available server tools and note what repository information they can read. Confirm that the tools needed to create or edit GitHub content are not enabled by this configuration.
6. In a fresh Copilot Agent chat, use the Lab 2C prompt. Replace the placeholders with your repository owner, repository name, and issue number. Ask Copilot to retrieve the issue through the GitHub MCP tool, then update only the Target project's `README.md` to meet its documentation criteria.
7. Verify the issue number and acceptance criteria in GitHub. Review the local diff and check that Copilot did not edit other files or invent requirements. Keep the change local unless the trainer asks for a commit.
8. In VS Code's MCP controls, stop or disable the server when the exercise is complete if you do not need it for later work.

### Fallback when MCP is unavailable

The trainer can demonstrate the prepared issue retrieval. Participants can complete the same README exercise using the issue text copied from GitHub, then identify which step the MCP tool would have supplied. Record that the MCP integration was not tested locally.

### Completion check

- You inspected the server configuration and the tools it exposes.
- Copilot retrieved the intended issue through MCP, or you recorded the fallback limitation.
- You checked the source issue and reviewed the local diff for scope and accuracy.
- You can explain the difference between MCP discovery/tool access and the model's decision about whether to call a tool.

## Debrief

Compare the three mechanisms:

| Mechanism | What it contributes | What you checked |
|---|---|---|
| Skill | A reusable task procedure | Whether it loaded and whether the procedure was followed |
| Hook | A configured action at a lifecycle point | Event, command, output, and permissions |
| MCP | Tools or information from an external service | Server identity, access, tool list, retrieved source, and resulting diff |

Discuss which controls guide the model, which actions the runtime triggers, and which access comes from the server. None removes the need to review the result.
