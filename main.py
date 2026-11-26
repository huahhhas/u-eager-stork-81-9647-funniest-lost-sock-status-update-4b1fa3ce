"""Lost sock status update entry.

One status update, at most 120 characters, in the voice of a lost sock
that has ended up somewhere it should not be. The program writes the
line to /output/entry.txt for the grader and prints it.
"""

import os

LINE = "Day 12 behind the fridge: I've started a family with a dust bunny. Tell my pair I found someone better."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
