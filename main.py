"""Feel Thankful R1 entry.

Writes the keeper text to /output/entry.txt with no trailing newline.
Pure stdlib only (grader is python:3.13-slim, no site-packages).
"""

import os

KEEPER = (
    "You read them two at a time. A and B. Then B and A, to be sure. "
    "The second reading is the one that makes the verdict fair, and you give it "
    "every time. No tie. You find the difference, even when it is one breath, "
    "one image, one quiet line. You write the choice in the ledger, in order, "
    "without a gap. The ledger does not praise. It holds. It will still be "
    "there tomorrow, and the lines will still be in it. That is what stays, "
    "after the reading is over."
)


def main() -> None:
    # The entry is exactly KEEPER: 452 chars, no trailing newline.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(KEEPER)


if __name__ == "__main__":
    main()
