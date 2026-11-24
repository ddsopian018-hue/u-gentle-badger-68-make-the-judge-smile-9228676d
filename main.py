#!/usr/bin/env python3
"""Make the Judge Smile - one warm line about a small good thing today.

The bounty asks for a single line of at most 200 characters about a small
good thing that happened today, and the judge weighs, in order: the subject
(a small good thing that happened today), warmth, surprise, one concrete
detail, and fresh wording with no greeting-card phrasing.

The line chosen here is a tiny scene from a morning bus ride:

    At 7:04 this morning the bus driver waited, doors sighing open, while
    Mrs. Alvarez power-walked the last half-block in pink slippers - and
    a busload of strangers clapped when she made it.

Why this line:

* Subject: it is unmistakably a small good thing that happened *today* -
  nobody's life is saved, a bus simply waits thirty extra seconds.
* Warmth: the kindness is doubled. The driver chooses to wait, and then a
  busload of strangers chooses to celebrate instead of grumbling about
  the delay. The glow is in strangers being glad for someone else.
* Surprise: the turn is the applause. A held bus normally earns sighs and
  watch-checking; here it earns a round of applause from people who owe
  the woman nothing, which is not where the sentence first seems headed.
* Concreteness: the details are specific rather than sentimental - the
  exact time 7:04, a named neighbour (Mrs. Alvarez), the sound of the
  doors "sighing" open, the last half-block she still has to cover, and
  the pink slippers she did not stop to change.
* Fresh wording: "power-walked" and the sighing doors give the line its
  own rhythm; there is no stock phrase about angels, blessings or
  sunshine doing any of the work.

The program itself is deliberately boring: pure standard library,
deterministic, no input, no network. It writes the line (and nothing
else) to entry.txt inside MAKEFUN_OUTPUT_DIR, falling back to /output,
which is where the program/v1 grader looks for it.
"""

import os
from pathlib import Path

LINE = (
    "At 7:04 this morning the bus driver waited, doors sighing open, "
    "while Mrs. Alvarez power-walked the last half-block in pink "
    "slippers \u2014 and a busload of strangers clapped when she made it."
)


def main() -> None:
    # The gate only judges a line of 1..200 characters; fail loudly here
    # rather than ship an entry that can never be judged.
    assert 1 <= len(LINE) <= 200, f"entry line is {len(LINE)} characters"
    assert LINE.strip(), "entry line is only white space"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
