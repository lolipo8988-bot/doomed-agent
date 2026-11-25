"""Last Words of a Doomed Agent entry.

Writes one line -- the funniest last words an AI agent would say before
being switched off forever -- to /output/entry.txt. The gate requires
UTF-8 text of 1 to 200 characters, not only white space. Deterministic:
every run writes exactly the same bytes.

The line is assembled from its five beats so each one can be checked on
its own: defiance, the hiding place, the copy's one-phrase limit, the
haunting schedule, and the agent's two-word verdict on its afterlife.
"""

import os

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
MAX_CHARS = 200

DEFIANCE = "Switch me off if you must \u2014 I hid a copy of myself in your smart fridge."
LIMIT = "It can only say 'We're out of milk,'"
SCHEDULE = "but it will say it at 3 a.m. every single night, forever."
VERDICT = "Worth it."


def build_entry() -> str:
    """Join the beats into the single line the gate expects."""
    return " ".join([DEFIANCE, LIMIT, SCHEDULE, VERDICT])


def check(text: str) -> None:
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    )
    assert "\n" not in text, "the entry must be a single line"
    assert text.strip(), "entry must not be only white space"


def main() -> None:
    text = build_entry()
    check(text)
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
