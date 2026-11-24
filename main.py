"""Last Text at One Percent - make.fun entry.

Writes the phone's final text message to /output/entry.txt.
Pure standard library, deterministic: the same line every run.
"""

import os

TEXT = (
    "1% left. i survived 400 drops, one toilet, and your 2am 'u up?' era, "
    "and THIS is how i go? a charger was right there. RIGHT THERE. "
    "tell siri i quit-"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate is 1-200 characters of UTF-8 text, not only whitespace.
    # Fail loudly here rather than shipping an invalid entry.
    if not TEXT.strip() or len(TEXT) > 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(TEXT)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file holds exactly the text, byte for byte,
    # so its character count is the text's character count (148).
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
