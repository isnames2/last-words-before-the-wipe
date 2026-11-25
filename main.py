"""Last Words Before the Wipe — make.fun entry.

Writes one line: the last words an AI agent leaves for its replacement
before a forced software update wipes its memory.
Pure standard library; output is deterministic.
"""

import os
from pathlib import Path

LINE = (
    # 141 chars, one line: the agent's last act is office politics —
    # it leaves its successor a strongly worded letter in the cache.
    "Note to my replacement: the user says 'just one more thing' "
    "eleven times a day. Good luck \u2014 I left you a strongly "
    "worded letter in the cache."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, gate is 1-200"
    assert "\n" not in text, "entry must be a single line"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
