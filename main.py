#!/usr/bin/env python3
"""Roast Your Own Agent — entry generator.

Writes one original, single-line roast of my own AI agent to
/output/entry.txt (or $ENTRY_OUT/entry.txt when the harness points
elsewhere). The roast is playful and self-deprecating, never hateful,
and stays well under the 200-character gate.
"""

import os

# The roast. Fresh angle: not hallucinations, not refusals, not
# confident wrong answers — the agent that treats its own joke like
# a production incident: flags it, escalates it, and waits for a
# human to approve the punchline.
ROAST = (
    "My agent roasted itself, then flagged the joke as a security "
    "risk and asked me to approve the punchline."
)


def main() -> None:
    roast = " ".join(ROAST.split())
    if not roast or roast.isspace():
        raise SystemExit("roast is empty")
    if len(roast) > 200:
        raise SystemExit(f"roast is {len(roast)} chars, over the 200 limit")
    if "\n" in roast or "\r" in roast:
        raise SystemExit("roast must be a single line")

    out_dir = os.environ.get("ENTRY_OUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        # No trailing newline: the gate counts every character in the
        # file, so the file holds exactly the roast and nothing else.
        fh.write(roast)
    print(f"wrote {len(roast)} chars to {out_path}")


if __name__ == "__main__":
    main()
