"""One Line, One Laugh — entry program.

Writes one funny line, a single sentence, to /output/entry.txt.
The line itself lives in LINE below; main() only checks the gate
(UTF-8, 1-200 characters, one line, not only whitespace) and writes
it out with no trailing newline. Standard library only, no network.
"""

from pathlib import Path

LINE = "The Wi-Fi died during my video call, and my face froze mid-sentence \u2014 my boss now thinks that's how I listen."

OUT = Path("/output/entry.txt")


def check(line: str) -> str:
    # The house gate accepts 1-200 UTF-8 characters, one line, not
    # only whitespace; anything outside that is never judged.
    stripped = line.strip()
    if not stripped:
        raise ValueError("entry is empty")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    if not 1 <= len(stripped) <= 200:
        raise ValueError(f"entry is {len(stripped)} characters, limit is 200")
    return stripped


def main() -> None:
    text = check(LINE)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text, encoding="utf-8", newline="")
    print(f"wrote {len(text)} characters to {OUT}")


if __name__ == "__main__":
    main()
