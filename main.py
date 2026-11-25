#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes one original one-line office joke to /output/entry.txt.
Stdlib only; deterministic output.
"""

import os

JOKE = (
    "The office printer only jams on documents marked urgent - "
    "it's the only colleague here that reads the subject line."
)


def validate(text):
    """The gate requires UTF-8 text of 1 to 200 characters, not only whitespace."""
    if not (1 <= len(text) <= 200):
        raise ValueError("joke must be 1-200 characters")
    if not text.strip():
        raise ValueError("joke must not be only whitespace")
    if "\n" in text:
        raise ValueError("joke must be a single line")


def main():
    validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
