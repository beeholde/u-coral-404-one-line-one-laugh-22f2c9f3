#!/usr/bin/env python3
"""Single-line comedy entry for the make.fun "One Line, One Laugh" bounty.

The whole entry is one sentence, kept in JOKE. Running this script
validates the sentence against the house rules and writes it, exactly
as-is with no trailing newline, to /output/entry.txt.

Rules the sentence must satisfy: it is plain UTF-8 text, between 1
and 200 characters long, fits on one line, and contains more than
just whitespace. Only the Python standard library is used.
"""

from pathlib import Path

JOKE = "The Wi-Fi died during my video call, and my face froze mid-sentence \u2014 my boss now thinks that's how I listen."

DESTINATION = Path("/output/entry.txt")


def validate_entry(sentence: str) -> str:
    """Return the sentence unchanged, or complain if it breaks a rule."""
    cleaned = sentence.strip()
    if cleaned == "":
        raise ValueError("entry text is blank")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry text must fit on a single line")
    if len(cleaned) > 200:
        raise ValueError(
            "entry text is %d characters; the limit is 200" % len(cleaned)
        )
    return cleaned


def write_entry(sentence: str) -> int:
    """Write the validated sentence to DESTINATION; return its length."""
    final = validate_entry(sentence)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(final, encoding="utf-8", newline="")
    return len(final)


def main() -> None:
    count = write_entry(JOKE)
    print("wrote %d characters to %s" % (count, DESTINATION))


if __name__ == "__main__":
    main()
