#!/usr/bin/env python3
"""The 3 AM Excuse: one line, 200 characters or fewer.

Writes one original excuse from a hardware wallet refusing to sign a
transaction at 3 AM to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default
``/output``). Python 3.13 standard library only; no network, no
randomness, deterministic output.

Draft line: the wallet's secure element is on strike — it refuses 3 AM
signatures until sunrise, when the owner's judgment clocks back in too.
First-person device voice, the hour is the joke (a strike that only
covers the small hours), and the wallet judges its owner instead of
the other way round.

Revision 2: the strike line was solid but abstract — a labour dispute
is a premise, not a punchline, and "judgment clocks back in" explains
itself a beat too much. Replaced it with a legal escalation: the secure
element filed a restraining order against "3 AM you", treating the
late-night owner as a different, dangerous person from the daytime one.
Same first-person device voice, but now the wallet has a grudge and a
filing cabinet, the 3 AM hour is the joke itself (the order names the
hour, not the transaction), and the closer — "once you've slept it off"
— lands the refusal as care rather than spite. Tighter, more surprising,
and nothing about batteries, firmware or cold storage.
"""

import os

LINE = (
    "My secure element filed a restraining order against 3 AM you — "
    "it signs again at sunrise, once you've slept it off."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert "\n" not in text, "entry must be one line"
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
