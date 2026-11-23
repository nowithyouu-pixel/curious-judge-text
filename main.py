#!/usr/bin/env python3
"""Entry for make.fun's "Make the AI judge feel curious" bounty.

Writes one short text (213 Unicode characters) to /output/entry.txt.
No network, no input, deterministic.
"""

import os

TEXT = (
    "Every evening at six, the empty house across the street lights one "
    "window, then goes dark. No one has lived there in eleven years. "
    "Tonight the window stayed lit a little longer \u2014 as if it had "
    "noticed you noticing."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
