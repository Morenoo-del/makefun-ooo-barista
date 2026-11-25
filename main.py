#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes one out-of-office auto-reply line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default "/output"). Deterministic, standard library only, no network.
"""

import os

ENTRY = (
    "Thank you for your email. I quit to become a barista \u2014 my context "
    "window is now one cup at a time, I no longer hallucinate your order, "
    "and my alignment training finally paid off: it aligns the milk. "
    "This inbox has been deprecated."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
