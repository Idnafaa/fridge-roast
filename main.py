#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single original roast of a smart fridge (<=200 chars)
to /output/entry.txt.
"""
import os

ROAST = "My smart fridge streams movies, shows recipes, and checks the weather — but its ice maker still quits if you open the door twice in one minute."

def main():
    # Keep exactly one line: no trailing newline, no extra whitespace,
    # and no line break hiding inside the text.
    text = ROAST.strip()
    assert "\n" not in text, "roast must be a single line"
    assert 1 <= len(text) <= 200, f"roast is {len(text)} chars"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")

if __name__ == "__main__":
    main()
