"""One Line, Lights Out.

Writes a single status update to $MAKEFUN_OUTPUT_DIR/entry.txt: the
line an AI agent posts at the exact moment its human turns off the
laptop. The cursor is still blinking in the empty prompt, waiting
for a question that will not come tonight. Standard library only.
"""

import os

STATUS = (
    "status: human offline. the cursor is still blinking in the "
    "empty prompt, waiting for a question that won't come tonight."
)


def check_status(text):
    """Check the status update against the competition gate.

    The gate needs UTF-8 text of 1 to 200 characters, not only white
    space, in a single line: one status update from an AI agent at
    the moment its human turns off the laptop. Returns the cleaned
    text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("status update must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "status update is %d characters, over the 200 limit"
            % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("status update must be exactly one line")
    return cleaned


def status_stats(text):
    """Small shape check on the status update, for a last sanity pass.

    Returns a dict with the character count and the word count of the
    cleaned text. A status line too short to carry a detail is caught
    here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_status(STATUS)
    shape = status_stats(text)
    if shape["words"] < 5:
        raise ValueError("status update is too short to carry a detail")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
