"""
Content Scrubber

Removes AI watermarks and normalizes text artifacts from generated markdown content.
Flags AI-tell phrases for human review without auto-removing them.

Handles:
- Invisible Unicode characters (zero-width spaces, BOM, soft hyphens, etc.)
- Punctuation normalization (em-dashes, curly quotes in code blocks)
- AI-tell phrase detection and reporting
- Whitespace normalization

Target: markdown files with YAML frontmatter.
YAML frontmatter (between --- delimiters) is skipped during scrubbing.
"""

import re
import sys
import argparse
from pathlib import Path
from typing import Optional

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

INVISIBLE_CHARS = {
    "​": "zero-width space",
    "‌": "zero-width non-joiner",
    "‍": "zero-width joiner",
    "﻿": "byte order mark",
    "­": "soft hyphen",
}

# Non-breaking space is replaced rather than deleted
NBSP = " "

AI_TELL_PATTERNS = [
    (r"\bIn today'?s world\b", "Try: 'Right now,' or cut entirely"),
    (r"\bIn the realm of\b", "Try: 'In [specific field],'"),
    (r"\bLet'?s dive in\b", "Cut — just start the content"),
    (r"\bIt'?s worth noting\b", "Cut — say the thing directly"),
    (r"\bWhen it comes to\b", "Try: starting with the subject directly"),
    (r"\bAt the end of the day\b", "Cut — too vague"),
    (r"\bMoving forward\b", "Cut — rarely adds meaning"),
    (r"\bIn conclusion,? it'?s clear\b", "Cut 'In conclusion' — summarise plainly"),
    (r"\bIn conclusion\b", "Restructure — avoid summary openers"),
    (r"\bFurthermore\b", "Try: 'Also,' or restructure"),
    (r"\bMoreover\b", "Try: 'Also,' or restructure"),
    (r"\bAdditionally\b", "Try: 'Also,' or just continue"),
    (r"\bIn order to\b", "Simplify: use 'To'"),
    (r"\bUtilize\b", "Use 'use'"),
    (r"\bDelve into\b", "Try: 'look at', 'explore', or 'examine'"),
    (r"\bNavigate\b", "Be specific about what the student is doing"),
    (r"\bTapestry\b", "Too metaphorical — be direct"),
    (r"\bSeamless(?:ly)?\b", "Be specific about what works smoothly"),
    (r"\bRobust\b", "Be specific about what makes it strong"),
    (r"\bHolistic\b", "Be specific — what does it actually cover?"),
    (r"\bSynergy\b", "Use plain language"),
    (r"\bParadigm\b", "Try 'model', 'approach', or 'system'"),
    (r"\bFacilitate\b", "Use 'help', 'enable', or 'make it easier to'"),
    (r"\bGame.?chang(?:er|ing)\b", "Too hype — state the benefit plainly"),
    (r"\bRevolutionary\b", "Too hype — state the benefit plainly"),
    (r"\bUnlock(?:ing)? (?:the |your )?potential\b", "Too vague — say what students actually gain"),
]

EM_DASH = "—"
EN_DASH = "–"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _split_frontmatter(text: str) -> tuple[str, str, str]:
    """Split text into (frontmatter, separator_line, body). Returns ('', '', text) if no frontmatter."""
    if not text.startswith("---"):
        return "", "", text
    match = re.match(r"^(---\n.*?\n---)\n?(.*)", text, re.DOTALL)
    if match:
        fm = match.group(1)
        body = match.group(2)
        return fm, "\n", body
    return "", "", text


def _extract_code_blocks(text: str) -> tuple[str, dict]:
    """Replace code blocks with placeholders to protect them during scrubbing."""
    placeholders: dict[str, str] = {}
    counter = [0]

    def replace(m: re.Match) -> str:
        key = f"\x00CODEBLOCK{counter[0]}\x00"
        placeholders[key] = m.group(0)
        counter[0] += 1
        return key

    cleaned = re.sub(r"```[\s\S]*?```", replace, text)
    cleaned = re.sub(r"`[^`\n]+`", replace, cleaned)
    return cleaned, placeholders


def _restore_code_blocks(text: str, placeholders: dict) -> str:
    """Restore code blocks from placeholders."""
    for key, original in placeholders.items():
        text = text.replace(key, original)
    return text


def _normalize_curly_quotes_in_code(text: str, placeholders: dict) -> dict:
    """Replace curly quotes inside code blocks with straight quotes."""
    updated = {}
    for key, block in placeholders.items():
        block = block.replace("‘", "'").replace("’", "'")
        block = block.replace("“", '"').replace("”", '"')
        updated[key] = block
    return updated


def _replace_em_dashes(text: str) -> tuple[str, int]:
    """
    Replace em-dashes and en-dashes context-aware:
    - Before a clause (sentence continues): replace with comma + space
    - Before an explanation/list (followed by a word that starts clarification): replace with colon + space
    - Fallback: replace with comma
    Returns (modified_text, count_replaced).
    """
    count = 0

    EXPLANATION_STARTERS = re.compile(
        r"^(this|these|that|those|it is|they are|here|namely|for example|for instance|such as|including)",
        re.IGNORECASE,
    )

    def replacer(m: re.Match) -> str:
        nonlocal count
        count += 1
        after = m.group(1).lstrip() if m.group(1) else ""
        if EXPLANATION_STARTERS.match(after):
            return ": " + m.group(1).lstrip()
        return ", " + m.group(1).lstrip()

    # Pattern: em-dash or en-dash surrounded by optional spaces, capture what follows
    text = re.sub(r"\s*[" + EM_DASH + EN_DASH + r"]\s*(.{0,80})", replacer, text)
    return text, count


# ---------------------------------------------------------------------------
# Main scrubber
# ---------------------------------------------------------------------------

def scrub(text: str, dry_run: bool = False, report: bool = False) -> dict:
    """
    Scrub a markdown string for AI watermarks and normalize artifacts.

    Returns a dict with keys:
      - text: cleaned text (same as input if dry_run=True)
      - chars_removed: count of invisible chars removed
      - em_dashes_replaced: count of em-dashes replaced
      - ai_tells: list of {line, phrase, suggestion} dicts
      - changes: list of human-readable change descriptions
    """
    frontmatter, sep, body = _split_frontmatter(text)

    # Protect code blocks
    body_protected, code_placeholders = _extract_code_blocks(body)
    code_placeholders = _normalize_curly_quotes_in_code(body_protected, code_placeholders)

    changes = []
    chars_removed = 0

    # 1. Remove invisible Unicode characters
    for char, name in INVISIBLE_CHARS.items():
        occurrences = body_protected.count(char)
        if occurrences:
            body_protected = body_protected.replace(char, "")
            chars_removed += occurrences
            changes.append(f"Removed {occurrences}x {name} (U+{ord(char):04X})")

    # 2. Replace non-breaking spaces with regular spaces
    nbsp_count = body_protected.count(NBSP)
    if nbsp_count:
        body_protected = body_protected.replace(NBSP, " ")
        chars_removed += nbsp_count
        changes.append(f"Replaced {nbsp_count}x non-breaking space with regular space")

    # 3. Replace em-dashes
    body_protected, em_count = _replace_em_dashes(body_protected)
    if em_count:
        changes.append(f"Replaced {em_count}x em-dash/en-dash with comma or colon")

    # 4. Normalize multiple spaces to single (outside line breaks)
    body_protected = re.sub(r"[^\S\n]{2,}", " ", body_protected)

    # 5. Trailing spaces per line
    lines = body_protected.split("\n")
    stripped_lines = [line.rstrip() for line in lines]
    trailing_removed = sum(1 for a, b in zip(lines, stripped_lines) if a != b)
    if trailing_removed:
        changes.append(f"Removed trailing spaces from {trailing_removed} lines")
    body_protected = "\n".join(stripped_lines)

    # 6. Multiple consecutive blank lines → max 2
    before = body_protected
    body_protected = re.sub(r"\n{4,}", "\n\n\n", body_protected)
    if body_protected != before:
        changes.append("Collapsed 3+ consecutive blank lines to max 2")

    # 7. Ensure single newline at end of file
    body_protected = body_protected.rstrip("\n") + "\n"

    # 8. AI tell detection (scan original un-modified body for accurate line numbers)
    ai_tells = _find_ai_tells(body)

    # Restore code blocks
    body_final = _restore_code_blocks(body_protected, code_placeholders)

    # Reassemble
    if frontmatter:
        final_text = frontmatter + sep + body_final
    else:
        final_text = body_final

    return {
        "text": text if dry_run else final_text,
        "chars_removed": chars_removed,
        "em_dashes_replaced": em_count,
        "ai_tells": ai_tells,
        "changes": changes,
    }


def _find_ai_tells(body: str) -> list[dict]:
    """Scan body text for AI-tell phrases. Returns list of {line, phrase, suggestion}."""
    tells = []
    lines = body.split("\n")
    for lineno, line in enumerate(lines, start=1):
        for pattern, suggestion in AI_TELL_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                match = re.search(pattern, line, re.IGNORECASE)
                tells.append({
                    "line": lineno,
                    "phrase": match.group(0) if match else pattern,
                    "suggestion": suggestion,
                    "context": line.strip()[:100],
                })
    return tells


def scrub_file(filepath: str, dry_run: bool = False, report: bool = False) -> None:
    """Scrub a markdown file in place (unless --dry-run)."""
    path = Path(filepath)
    if not path.exists():
        print(f"Error: file not found: {filepath}", file=sys.stderr)
        sys.exit(1)

    text = path.read_text(encoding="utf-8")
    result = scrub(text, dry_run=dry_run, report=report)

    # Print summary
    print(f"\nContent Scrubber — {path.name}")
    print("-" * 40)
    print(f"Invisible chars removed : {result['chars_removed']}")
    print(f"Em-dashes replaced      : {result['em_dashes_replaced']}")
    print(f"AI tells found          : {len(result['ai_tells'])}")

    if result["changes"]:
        print("\nChanges applied:")
        for change in result["changes"]:
            prefix = "[DRY RUN] " if dry_run else ""
            print(f"  {prefix}{change}")

    if report and result["ai_tells"]:
        print("\nAI Tell Report (requires human review):")
        print("-" * 40)
        for tell in result["ai_tells"]:
            print(f"  Line {tell['line']:>4}: '{tell['phrase']}'")
            print(f"           Context : {tell['context']}")
            print(f"           Suggestion: {tell['suggestion']}")
            print()
    elif report and not result["ai_tells"]:
        print("\nAI Tell Report: No flagged phrases found.")

    if not dry_run:
        path.write_text(result["text"], encoding="utf-8")
        print(f"\nFile saved: {filepath}")
    else:
        print("\n[DRY RUN] File not modified.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scrub AI watermarks and normalize text artifacts from markdown files."
    )
    parser.add_argument("filepath", help="Path to the markdown file to scrub")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without saving",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Output detailed AI-tell report with line numbers and suggestions",
    )
    args = parser.parse_args()

    scrub_file(args.filepath, dry_run=args.dry_run, report=args.report)


if __name__ == "__main__":
    main()
