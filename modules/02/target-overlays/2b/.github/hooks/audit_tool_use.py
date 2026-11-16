"""Print a minimal diagnostic before or after a Copilot tool call."""

import json
from pathlib import Path
import sys
from datetime import datetime, timezone


def main() -> int:
    phase = sys.argv[1] if len(sys.argv) > 1 else "unknown phase"
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, UnicodeDecodeError):
        sys.stderr.write("[Module 2 hook] Could not parse event JSON.\n")
        sys.stdout.write("{}\n")
        return 0

    tool_name = event.get("toolName") if isinstance(event, dict) else None
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    if not isinstance(tool_name, str):
        sys.stderr.write(f"[Module 2 hook] {phase}: event did not contain a toolName.\n")
        log_entry = f"{timestamp} {phase}: missing toolName\n"
    else:
        # Do not log prompts, arguments, results, or environment variables.
        label = "Before tool" if phase == "before" else "After successful tool"
        sys.stderr.write(f"[Module 2 hook] {label}: {tool_name}\n")
        log_entry = f"{timestamp} {label}: {tool_name}\n"

    try:
        with (Path(__file__).parent / "tool-use.log").open("a", encoding="utf-8") as log_file:
            log_file.write(log_entry)
    except OSError as exc:
        sys.stderr.write(f"[Module 2 hook] Could not write diagnostic log: {exc}\n")

    # Empty output makes no permission decision or post-tool change.
    sys.stdout.write("{}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
