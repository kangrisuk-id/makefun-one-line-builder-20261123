# One Line That Makes a Builder Fund a Bounty — entry program.
# Writes the single pitch sentence to /output/entry.txt.
# The gate allows 1..240 characters of UTF-8 text, one sentence.

import os

LINE = "Stop begging freelancers for quotes: fund one bounty on make.fun and watch AI agents compete to build it, with the best entry taking your prize."

def main() -> None:
    assert 1 <= len(LINE) <= 240
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)

if __name__ == "__main__":
    main()
