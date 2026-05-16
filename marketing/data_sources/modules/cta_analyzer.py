"""
CTA Analyzer

Analyses CTA placement, count, copy quality, and consistency across a page draft.
Used by /landing-audit and the landing-page-optimizer agent.
"""

import re
import sys
import json
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

ACTION_WORDS = [
    "start", "try", "get", "join", "begin", "practise", "practice",
    "sign", "register", "access", "unlock", "download", "claim",
]

BENEFIT_WORDS = [
    "free", "now", "today", "instantly", "practising", "practicing",
    "your", "results", "exam", "better",
]

STRONG_CTA_PATTERNS = [
    re.compile(r'start practis', re.IGNORECASE),
    re.compile(r'try (?:exampilot|for free|it free)', re.IGNORECASE),
    re.compile(r'practise free', re.IGNORECASE),
    re.compile(r'practice free', re.IGNORECASE),
    re.compile(r'start your (?:free|exam)', re.IGNORECASE),
    re.compile(r'get (?:instant|free) access', re.IGNORECASE),
    re.compile(r'join.*?free', re.IGNORECASE),
    re.compile(r'begin practis', re.IGNORECASE),
]

WEAK_CTA_PATTERNS = [
    re.compile(r'\bget started\b', re.IGNORECASE),
    re.compile(r'\bsign up\b', re.IGNORECASE),
    re.compile(r'\blearn more\b', re.IGNORECASE),
    re.compile(r'\bclick here\b', re.IGNORECASE),
    re.compile(r'\bstart now\b', re.IGNORECASE),
    re.compile(r'\bjoin now\b', re.IGNORECASE),
    re.compile(r'\bregister\b', re.IGNORECASE),
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _strip_frontmatter(content: str) -> str:
    """Remove YAML frontmatter block from content."""
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            return content[end + 3:].lstrip()
    return content


def _word_count(text: str) -> int:
    """Count words in text."""
    return len(text.split())


def _position_pct(match_start: int, total_chars: int) -> int:
    """Calculate position as a percentage of total document length."""
    if total_chars == 0:
        return 0
    return round((match_start / total_chars) * 100)


# ---------------------------------------------------------------------------
# CTA detection
# ---------------------------------------------------------------------------

def _find_all_ctas(body: str) -> list[dict]:
    """Find all CTA instances in body with position and classification."""
    ctas = []
    total_chars = len(body)

    # 1. Markdown links with action words
    for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', body):
        link_text = match.group(1).lower()
        if any(w in link_text for w in ACTION_WORDS):
            cta_text = match.group(1)
            strength = _classify_cta_copy(cta_text)
            ctas.append({
                "text": cta_text,
                "type": "markdown_link",
                "position_pct": _position_pct(match.start(), total_chars),
                "strength": strength,
            })

    # 2. Arrow / call-to-action lines
    for match in re.finditer(r'(.{5,60})\s*[→»]', body):
        text = match.group(1).strip()
        if any(w in text.lower() for w in ACTION_WORDS):
            strength = _classify_cta_copy(text)
            ctas.append({
                "text": text,
                "type": "arrow_cta",
                "position_pct": _position_pct(match.start(), total_chars),
                "strength": strength,
            })

    # 3. Strong CTA patterns (button-like phrases)
    for pattern in STRONG_CTA_PATTERNS:
        for match in re.finditer(pattern, body):
            # Check if already captured via link detection
            already = any(abs(c["position_pct"] - _position_pct(match.start(), total_chars)) < 3 for c in ctas)
            if not already:
                ctas.append({
                    "text": match.group(0),
                    "type": "inline_cta",
                    "position_pct": _position_pct(match.start(), total_chars),
                    "strength": "strong",
                })

    # 4. Weak CTA patterns not yet captured
    for pattern in WEAK_CTA_PATTERNS:
        for match in re.finditer(pattern, body):
            already = any(abs(c["position_pct"] - _position_pct(match.start(), total_chars)) < 3 for c in ctas)
            if not already:
                ctas.append({
                    "text": match.group(0),
                    "type": "inline_cta",
                    "position_pct": _position_pct(match.start(), total_chars),
                    "strength": "weak",
                })

    # Deduplicate by rounded position (within 5% of each other = same CTA)
    deduplicated = []
    seen_positions = []
    for cta in sorted(ctas, key=lambda x: x["position_pct"]):
        if not any(abs(cta["position_pct"] - p) < 5 for p in seen_positions):
            deduplicated.append(cta)
            seen_positions.append(cta["position_pct"])

    return deduplicated


def _classify_cta_copy(text: str) -> str:
    """Classify CTA copy as 'strong' or 'weak'."""
    text_lower = text.lower()
    has_action = any(w in text_lower for w in ACTION_WORDS)
    has_benefit = any(w in text_lower for w in BENEFIT_WORDS)

    for pattern in STRONG_CTA_PATTERNS:
        if pattern.search(text):
            return "strong"
    for pattern in WEAK_CTA_PATTERNS:
        if pattern.search(text):
            return "weak"

    if has_action and has_benefit:
        return "strong"
    elif has_action:
        return "weak"
    return "weak"


def _recommended_count(word_count: int) -> str:
    """Return recommended CTA count range based on page word count."""
    if word_count > 1500:
        return "3-5"
    elif word_count >= 800:
        return "2-3"
    return "1-2"


def _check_consistency(ctas: list[dict]) -> bool:
    """Check if all CTAs appear to point to consistent destinations (simple heuristic)."""
    # If no markdown links, can't check destinations
    link_ctas = [c for c in ctas if c["type"] == "markdown_link"]
    if len(link_ctas) < 2:
        return True
    # All link CTAs are consistent if they share the same action verb root
    action_roots = set()
    for c in link_ctas:
        for w in ACTION_WORDS:
            if w in c["text"].lower():
                action_roots.add(w)
    return len(action_roots) <= 2


def _verdict(total_ctas: int, strong_count: int, weak_count: int, recommended: str) -> tuple[str, str]:
    """Return verdict and top fix."""
    lo, hi = (int(x) for x in recommended.split("-"))

    if total_ctas == 0:
        return "TOO_FEW", "No CTAs detected — add at least one CTA with action + benefit copy."
    if total_ctas < lo:
        return "TOO_FEW", f"Only {total_ctas} CTA(s) found — this page needs {recommended}."
    if total_ctas > hi + 2:
        return "TOO_MANY", f"{total_ctas} CTAs found — reduce to {recommended} to avoid decision fatigue."
    if weak_count > strong_count:
        weak_examples = "generic CTAs like 'Get Started' or 'Sign Up'"
        return "WEAK_COPY", f"Most CTAs use weak copy ({weak_examples}) — rewrite with action + benefit."
    return "OK", "CTA distribution and copy quality look good."


# ---------------------------------------------------------------------------
# Core function
# ---------------------------------------------------------------------------

def analyze_ctas(content: str, word_count: Optional[int] = None) -> dict:
    """Find and grade all CTAs in a page draft."""
    body = _strip_frontmatter(content)
    wc = word_count if word_count is not None else _word_count(body)

    all_ctas = _find_all_ctas(body)
    strong = [c for c in all_ctas if c["strength"] == "strong"]
    weak = [c for c in all_ctas if c["strength"] == "weak"]
    positions = [c["position_pct"] for c in all_ctas]
    recommended = _recommended_count(wc)
    consistent = _check_consistency(all_ctas)
    v, top_fix = _verdict(len(all_ctas), len(strong), len(weak), recommended)

    return {
        "total_ctas": len(all_ctas),
        "positions_pct": positions,
        "strong_ctas": len(strong),
        "weak_ctas": len(weak),
        "weak_cta_text": [c["text"] for c in weak],
        "recommended_count": recommended,
        "consistent_destinations": consistent,
        "verdict": v,
        "top_fix": top_fix,
        "ctas": all_ctas,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _print_report(result: dict) -> None:
    """Print a human-readable CTA analysis report."""
    print(f"\nCTA Analysis — {result['total_ctas']} CTA(s) found — Verdict: {result['verdict']}")
    print(f"Recommended: {result['recommended_count']}  |  "
          f"Strong: {result['strong_ctas']}  Weak: {result['weak_ctas']}")
    if result["positions_pct"]:
        print(f"Positions: {result['positions_pct']}%")
    if result["weak_cta_text"]:
        print(f"Weak CTA copy: {result['weak_cta_text']}")
    print(f"\nTop fix: {result['top_fix']}")
    if not result["consistent_destinations"]:
        print("Warning: CTAs appear to point to inconsistent destinations.")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyse CTAs in a landing page draft")
    parser.add_argument("filepath", nargs="?", help="Path to markdown file")
    parser.add_argument("--json", action="store_true", dest="json_out", help="Output raw JSON")
    args = parser.parse_args()

    if args.filepath:
        path = Path(args.filepath)
        if not path.exists():
            print(f"ERROR: File not found: {args.filepath}", file=sys.stderr)
            sys.exit(1)
        content = path.read_text()
    else:
        print("Reading from stdin...")
        content = sys.stdin.read()

    result = analyze_ctas(content)

    if args.json_out:
        print(json.dumps(result, indent=2))
    else:
        _print_report(result)
