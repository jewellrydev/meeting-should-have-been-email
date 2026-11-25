"""The Meeting That Should Have Been an Email — a make.fun entry.

Prints exactly one line of plain text, at most 200 characters: one
joke about a meeting that should have been an email.
"""

LINE = (
    "This meeting should have been an email, and the email should "
    "have been one line: 'per my last email.'"
)


def build_line() -> str:
    line = LINE
    assert len(line) <= 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
