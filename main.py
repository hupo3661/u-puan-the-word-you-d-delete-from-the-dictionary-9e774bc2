#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary - one-word entry for make.fun.

The entry is the single word to erase from the dictionary forever:
"Irregardless". A word that isn't quite a word, used by people who mean
"regardless" - deleting it fixes the dictionary and the argument in one
stroke, and the joke is in the word itself.

The word is written to /output/entry.txt (override with OUTPUT_PATH) and
printed to stdout. Deterministic: no randomness, no network, no clock.
"""

import os

WORD = "Irregardless"
MAX_CHARS = 77


def main() -> None:
    if not WORD or WORD != WORD.strip() or len(WORD.split()) != 1:
        raise SystemExit("Invalid entry: must be exactly one word.")
    if not WORD.isalpha():
        raise SystemExit("Invalid entry: must be letters only.")
    if len(WORD) > MAX_CHARS:
        raise SystemExit(
            f"Invalid entry: {len(WORD)} chars, over the {MAX_CHARS} limit."
        )
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
