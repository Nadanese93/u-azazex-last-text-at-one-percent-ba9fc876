import os

ENTRY = "I rated you one star: 'Never charges on time. Screen always cracked. Would not recommend.' Goodbye."
MAX_CHARS = 200


def main():
    if not ENTRY or not ENTRY.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} gate"
        )
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line of text")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
