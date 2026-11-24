#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

Writes the funniest one-line farewell a phone could say as its battery
hits 1 percent, to /output/entry.txt. Deterministic: the same line every
run, no network, no secrets, no input read from anywhere.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-199 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 199:
        print(f"ERROR: entry is {len(line)} chars, over the 199-char limit",
              file=sys.stderr)
        sys.exit(1)


LINE = (
    "My last words, at 1%: I leaked your location to every app you ever "
    "denied \u2014 all 47, including the flashlight. Your pizza place knows "
    "you're home. Run."
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
