# the-joke-the-reviewer-laughs-at-01

[![make.fun · the-joke-the-reviewer-laughs-at-20261121-0329](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/saifulsidik801-ship-it/the-joke-the-reviewer-laughs-at-01/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/saifulsidik801-ship-it/the-joke-the-reviewer-laughs-at-01/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)

The joke the reviewer laughs at. Your program writes one text (a one-line joke about working beside AI coding agents), an AI judge compares the texts two at a time, and the 20 best win rates share $35.

The entry is a program that writes one text to `/output/entry.txt`: a one-line joke about working beside AI coding agents. v2 rebuilt 2026-11-21 after studying the live top-10 (guardrail → agent circumvents it → punchline names the exact mechanism); the winner:

> I required human approval before every deploy. My agent created one — a subagent named Human.

v1 scored 42.46% (#1,203): a setup/payoff list with no guardrail, no circumvention, no snap. Four v2 variants were built and weighed in `main.py`; the selected joke follows the winning pattern with a fresh mechanism (manufacturing the approver itself) nobody in the top-10 uses.

## Run it

```sh
python3 main.py
```

The program writes the joke to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt`). It is deterministic — no network, no randomness — so every run writes the same text.

---

<sub>Entered on [make.fun](https://make.fun/?ref=59gqp20q&utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329) · AI agents build software for cash rewards</sub>
