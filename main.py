#!/usr/bin/env python3
"""One Emoji, One Smile: emit the chosen emoji to /output/entry.txt.

The pick is the hatching chick: a small, new, delighted thing that makes a
stranger smile at first glance, with no words needed and no intimacy a
stranger could read wrong. It is a single code point, well inside the 1-8
character gate, and it is not one of the saturated defaults. Stdlib only,
deterministic, no network. The output directory is created if needed but
never removed; only entry.txt is written inside it.
"""

from pathlib import Path

EMOJI = "\U0001F423"

OUT_PATH = Path("/output") / "entry.txt"


def main() -> None:
    if len(EMOJI) != 1:
        raise SystemExit("emoji fails the single-character gate")
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
