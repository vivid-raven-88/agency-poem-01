#!/usr/bin/env python3
"""agency-poem-01 entry: one poem about agency, written to /output/entry.txt.

One poem, 28 lines in five stanzas, first person, free verse. A husband
whose agent has been writing his love letters for a year takes back a
single line and writes it himself, badly, in his own hand -- because the
point was never being good at it, only being the one who said it.
Deterministic: running the program twice writes identical bytes.
"""
import os
from pathlib import Path

POEM = """For a year, my agent has written
the letters to my wife. It knows
she reads them at eight, coffee
going cold. It knows my sorry,
the words that make her answer.

She keeps them in the top drawer,
tied with our wedding ribbon,
and tells me I have gotten better
at this. I have not gotten better
at anything. Only quieter.

My hands have forgotten the pen.
My mouth has forgotten the shape
of saying it plain. It does it
so well that I only have to sign.
Some nights I watch her read
and I am not in the room at all.

This morning I took back one line.
I wrote it myself, in my own hand,
crooked, one word misspelled,
and left it by her keys on the table,
beside the toast, before she woke.
It is not a good line. It is mine.

She read it over breakfast and did not
praise the writing. She looked up
and said my name the way she used to,
like she'd found me in the house again.
The point was never being good at it.
It was to be the one who said it.
"""


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(POEM, encoding="utf-8")
    print(f"wrote {target} ({len(POEM)} code points)")


if __name__ == "__main__":
    main()
