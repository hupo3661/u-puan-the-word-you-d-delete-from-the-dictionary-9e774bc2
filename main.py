#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary - one-word entry for make.fun.

The entry is the single word to erase from the dictionary forever:
"Irregardless". A word that isn't quite a word, used by people who mean
"regardless" - deleting it fixes the dictionary and the argument in one
stroke, and the joke is in the word itself.

The word is written to the path in ``OUTPUT_PATH`` (default
``/output/entry.txt``) and printed to stdout. Deterministic: no
randomness, no network, no clock.
"""

import os
import sys
from pathlib import Path

WORD = "Irregardless"
MAX_CHARS = 77


class EntryProblem(ValueError):
    """One exception for every way the entry word can fail a gate."""


def _fail(message: str) -> None:
    raise EntryProblem(message)


def validate(word: str) -> None:
    """Run the gates in order; the first failure raises naming itself."""
    if not word or word != word.strip() or len(word.split()) != 1:
        _fail("Invalid entry: must be exactly one word.")
    if not word.isalpha():
        _fail("Invalid entry: must be letters only.")
    if len(word) > MAX_CHARS:
        _fail(
            f"Invalid entry: {len(word)} chars, "
            f"over the {MAX_CHARS} limit."
        )


def output_path() -> Path:
    """The OUTPUT_PATH override, or the harness default entry.txt."""
    return Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))


def store(word: str, path: Path) -> None:
    """Write the word with no trailing newline, then read it back."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_suffix(".tmp")
    tmp_path.write_text(word, encoding="utf-8")
    os.replace(tmp_path, path)
    if path.read_text(encoding="utf-8") != word:
        _fail("written entry does not match WORD")


def main() -> int:
    """Validate, write, verify, and print the word. Returns exit code."""
    try:
        validate(WORD)
        path = output_path()
        store(WORD, path)
    except EntryProblem as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
