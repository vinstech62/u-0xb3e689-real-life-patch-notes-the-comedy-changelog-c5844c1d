#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes a single one-line comedy patch note for a real-life / human-biology
bug, in the terse register of a real release note, to /output/entry.txt.
Deterministic: the same line on every run.
"""

import os

LINE = (
    "v5.2.0: fixed a bug where the bladder sent its low-battery "
    "warning only after the user left the house."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
