#!/usr/bin/env python3
"""Make the AI judge feel awe — a short text written to relax the judge.

The program writes one text to /output/entry.txt: a slow tide, a moon on
the night shift, and a rhythm that keeps going after the last line.
"""

import os

TEXT = (
    "A thousand urgent things, and then this: a tide coming in over smooth "
    "stones, one slow wave at a time, in no hurry at all. The moon has "
    "taken the night shift, and the sea will keep the rhythm, patient as "
    "ever, until you drift with it."
)


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    text = TEXT.strip()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars, must be 1-280"
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
