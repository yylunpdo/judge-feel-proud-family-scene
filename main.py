"""Make the AI Judge Feel Proud: A Family Scene (entry 222).

Writes one short family scene (two lines) to /output/entry.txt.
Python standard library only; fully deterministic.
"""

import os

SCENE = (
    "Dad burns the pancakes every Sunday \u2014 on purpose now, he says, "
    "because the burnt edges are the only ones worth fighting over.\n"
    "Mum steals the best one when no one's looking, and the dog gets "
    "the one nobody wanted, like always."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = SCENE
    assert 1 <= len(text) <= 280, f"scene is {len(text)} chars, must be 1-280"
    assert text.strip(), "scene must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
