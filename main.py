#!/usr/bin/env python3
"""Entry for the-joke-about-the-demo-20261121-0551.

Writes one line -- a joke about working beside an AI coding agent --
to /output/entry.txt. No network, no input, deterministic output.
"""

import os

JOKE = (
    "My AI pair programmer fixed the demo crash overnight "
    "\u2014 the demo now crashes in a language I haven't learned yet."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
