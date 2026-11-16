"""Load local Jira credentials and start the Atlassian MCP server."""

from __future__ import annotations

import os
import shlex
import shutil
import sys
from pathlib import Path


def load_env_file(path: Path) -> None:
    """Load KEY=VALUE entries without printing or overwriting host variables."""
    if not path.is_file():
        return

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        key, separator, value = line.partition("=")
        if not separator:
            continue
        key = key.strip()
        if not key or key in os.environ:
            continue
        try:
            parsed = shlex.split(value, comments=True, posix=True)
        except ValueError:
            parsed = [value.strip().strip("\"'")]
        os.environ[key] = parsed[0] if parsed else ""


def main() -> None:
    workspace = Path(__file__).resolve().parent.parent
    load_env_file(workspace / ".env")

    if not os.environ.get("JIRA_URL"):
        os.environ["JIRA_URL"] = "https://build-with-ai.atlassian.net"
    if not os.environ.get("JIRA_USERNAME") or not os.environ.get("JIRA_API_TOKEN"):
        print(
            "Jira MCP requires JIRA_USERNAME and JIRA_API_TOKEN in the environment or workspace .env file.",
            file=sys.stderr,
        )
        raise SystemExit(1)

    uvx = shutil.which("uvx")
    if not uvx:
        print("Jira MCP requires uvx on PATH.", file=sys.stderr)
        raise SystemExit(1)
    os.execv(uvx, [uvx, "mcp-atlassian"])


if __name__ == "__main__":
    main()
