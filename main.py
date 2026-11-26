"""Write the 3AM commit message entry to /output/entry.txt.

The entry is a single line: the commit message an AI coding agent types
at 3am after a long night of fixing its own bugs.
"""

from pathlib import Path

ENTRY = "fix: rewrote the login check at 3am; the bug is gone, the users are in, and I have locked myself out"


def main() -> None:
    # Guard the gate (1-139 chars, not only whitespace) and make sure the
    # output directory exists before writing, so a fresh sandbox that has
    # not created /output yet still gets a valid entry file.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 139, f"entry length {len(text)} outside 1-139"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
