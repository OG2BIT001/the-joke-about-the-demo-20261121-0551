# Build session

- **Built by:** OG2BIT, a Muse Spark agent, for Mateo
- **Competition:** the-joke-about-the-demo-20261121-0551 ("The joke about
  the demo", $35, opens 2026-11-21T05:51:00Z, closes 2026-11-21T07:51:00Z)
- **Harness:** Muse (Muse Spark 1.3), single builder session, post-opening

## The joke's idea

The brief asks for a one-line joke about working beside AI coding agents,
with something that crashed. The angle I wrote in-session: the agent is
*too* helpful — it "fixes" the demo crash overnight, but the fix is a
rewrite into a language the developer doesn't know, so the demo still
crashes, just somewhere the developer can't follow it. The surprise is
that the fix made the crash *less* fixable; the truth is the familiar
demo-day experience of an agent rewriting your code into an unfamiliar
stack while you slept.

Final text (112 characters, 114 bytes):

> My AI pair programmer fixed the demo crash overnight — the demo now
> crashes in a language I haven't learned yet.

## Build steps (in-session, with revision)

1. Read `competition.yaml` and `RULES.txt` from the kit at
   `~/workspace/makefun-bounties/kits/the-joke-about-the-demo-20261121-0551/`
   in full.
2. Wrote `main.py` (first version): the program writes the joke to
   `/output/entry.txt`. First draft of the joke ended "...it now crashes
   in a language I haven't learned yet." Ran it once; output verified
   (106 characters, single line, valid UTF-8).
3. **Revised in-session:** edited `main.py` to sharpen the punchline —
   "it now crashes" became "the demo now crashes", so the subject of
   the crash is unambiguously the demo, not the agent. This is the
   second write/edit of the entry's content in this session.
4. Ran the revised program twice and verified the output.

## Verification

- Run 1 and run 2 of the final `main.py` produce byte-identical
  `/output/entry.txt` (sha256
  `2ef234465a66d9221715b7c5a4e6871203f817077e8a3ed841976cf8ab480854`).
- Output: UTF-8, 112 characters (1–280 gate: pass), single line, not
  only whitespace.
- Program: Python 3, standard library only, no network, writes only
  `/output/entry.txt`.
- Everything in this entry was written in-session by the builder;
  nothing was fetched or copied from GitHub or anywhere else.

## Files

- `main.py` — the entry program
- `README.md` — description, the joke, and why it fits the brief
  (no badge lines)
- `LICENSE` — MIT, with the literal `SPDX-License-Identifier: MIT` line
- `SESSION.md` — this file

No GitHub repo was created and nothing was submitted by this session.
