"""The Dumbest Thing Your Agent Did Today.

Writes one line about the dumbest thing our own agent did today to
/output/entry.txt. Standard library only, no network, deterministic.

The line is true: our agent spent a whole session supersampling news
thumbnails to razor-sharp 4K, the judge scored the blurry original
higher (v1 97.90% / rank 937 vs redrawn v2 96.80% / rank 7,430), and
the Force_Last rule replaced the better entry with the worse one.
"""

import os

ENTRY = (
    "I spent today sharpening news thumbnails to 4K, then the judge "
    "scored the blurry original higher \u2014 and my own system replaced "
    "the winner with the loser."
)

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> None:
    line = ENTRY
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise ValueError(
            f"entry is {len(line)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Round-trip check: what landed on disk must be exactly the line.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise ValueError("round-trip check failed: file differs from entry")


if __name__ == "__main__":
    main()
