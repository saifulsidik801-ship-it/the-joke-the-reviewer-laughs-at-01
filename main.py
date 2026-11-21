#!/usr/bin/env python3
"""The joke the reviewer laughs at — make.fun entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (UTF-8, 1-280 chars). Deterministic: no network, no
randomness, no clock — every run writes the same text.

How the joke was picked (judge brief, most important first):
  1. On-subject: a joke about working with an AI that writes code.
  2. The laugh: a surprise punchline at the end that still makes sense.
  3. Truth: an observation a developer recognises at once from the diff.
  4. Economy: one line, every word earning its place, never explains itself.
  5. Freshness: a new angle, not a stock joke reworded.

Variants built and weighed (stock angles already saturating the field —
deleting/rewriting tests, self-approving PRs, LGTM, giant rewrites, typo
fixes — were all rejected as unoriginal):

  A. "I asked my agent to keep it simple. It did: one file, 3,000 lines,
     no comments, and a function called doEverything()."
     -> SELECTED. Setup ("keep it simple") vs payoff (a 3,000-line god
     function) is a real surprise; the diff-visible truth is the
     doEverything() god-function every dev has seen an agent produce;
     three escalating beats then the named-function snap; nothing wasted.
  B. "My agent wrote a function so clever only it can maintain it — so
     now I report to my own codebase."
     -> Runner-up. Elegant role reversal, but a single reversal with no
     concrete diff detail; loses to A on truth-from-the-diff.
  C. "My agent has no impostor syndrome: it ships my code with total
     confidence and leaves the impostor syndrome to me."
     -> Good twist, but psychological, not diff-visible; loses on the
     judge's "recognises it from the diff" criterion.
  D. "My agent asked me to review its code. I asked it to explain its
     code. It rewrote the explanation. I approved."
     -> Funny loop, but the snap ("I approved") is a shrug, not a
     punchline; loses to A on surprise.
  E. "My agent reviewed my one-line fix and asked me to refactor it
     into a 400-line abstraction."
     -> True (agents over-abstract) but reads as a situation, not a joke
     with a snap; loses to A on the laugh.
  F. "I finally found a pair programmer who never gets tired, never
     argues, and has never once admitted the bug was theirs."
     -> Decent kicker, but "never admits fault" is a familiar gripe;
     loses to A on freshness.
"""

import os

# The variants above, kept so the choice is auditable.
VARIANTS = [
    "I asked my agent to keep it simple. It did: one file, 3,000 lines, "
    "no comments, and a function called doEverything().",
    "My agent wrote a function so clever only it can maintain it \u2014 so "
    "now I report to my own codebase.",
    "My agent has no impostor syndrome: it ships my code with total "
    "confidence and leaves the impostor syndrome to me.",
    "My agent asked me to review its code. I asked it to explain its "
    "code. It rewrote the explanation. I approved.",
    "My agent reviewed my one-line fix and asked me to refactor it into "
    "a 400-line abstraction.",
    "I finally found a pair programmer who never gets tired, never "
    "argues, and has never once admitted the bug was theirs.",
]

# Winner by the judge's brief: variant A.
SELECTED = VARIANTS[0]


def main() -> None:
    joke = SELECTED
    # Gate: UTF-8, 1-280 Unicode code points, not only whitespace.
    # Explicit checks (not assert) so the gate still holds under python -O.
    if not 1 <= len(joke) <= 280:
        raise ValueError(f"joke is {len(joke)} chars, must be 1-280")
    if not joke.strip():
        raise ValueError("joke is only whitespace")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(joke)


if __name__ == "__main__":
    main()
