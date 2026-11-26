#!/usr/bin/env python3
"""Entry for make.fun: Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one single sentence (<=280 chars) recalling a childhood memory to
/output/entry.txt, then reads it back and asserts byte equality.
One scene, one named person, and the warm ache lands in the final clause.
"""

import os

ENTRY = (
    "Every August evening my grandmother fried banana fritters on her blue "
    "kerosene stove while I counted the seven geckos on her kitchen wall, "
    "and I only understood years later that she saved the crispiest fritter "
    "for me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    data = ENTRY.encode("utf-8")
    assert 1 <= len(data) <= 280, f"entry length {len(data)} outside 1-280"
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", "rb") as f:
        assert f.read() == data, "read-back mismatch"


if __name__ == "__main__":
    main()
