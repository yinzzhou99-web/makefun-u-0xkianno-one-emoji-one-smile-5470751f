"""Write a single emoji to the output file."""

import os
import sys

EMOJI = "\U0001f423"

OUTPUT_PATH = os.path.join("/output", "entry.txt")


def main():
    if len(EMOJI) != 1:
        sys.exit("error: entry must be exactly one character")
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)


if __name__ == "__main__":
    main()
