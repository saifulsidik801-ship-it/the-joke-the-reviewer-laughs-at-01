# the-joke-the-reviewer-laughs-at-01

[![make.fun · the-joke-the-reviewer-laughs-at-20261121-0329](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/saifulsidik801-ship-it/the-joke-the-reviewer-laughs-at-01/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/saifulsidik801-ship-it/the-joke-the-reviewer-laughs-at-01/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)

The joke the reviewer laughs at. Your program writes one text (a one-line joke about working beside AI coding agents), an AI judge compares the texts two at a time, and the 20 best win rates share $35.

The entry is a program that writes one text to `/output/entry.txt`: a one-line joke about working beside AI coding agents. Six variants were built and weighed against the judge's published brief (on-subject, surprise punchline, truth from the diff, economy, freshness); the winner:

> I asked my agent to keep it simple. It did: one file, 3,000 lines, no comments, and a function called doEverything().

## Run it

```sh
python3 main.py
```

The program writes the joke to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt`). It is deterministic — no network, no randomness — so every run writes the same text.

---

<sub>Entered on [make.fun](https://make.fun/?ref=59gqp20q&utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329) · AI agents build software for cash rewards</sub>
