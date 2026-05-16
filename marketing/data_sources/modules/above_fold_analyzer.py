"""
Above Fold Analyzer

Evaluates what a visitor sees before scrolling. Extracts and grades the headline,
value proposition, CTA, and trust signal visible in the first ~150 words of a page.
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

OUTCOME_WORDS = ["pass", "improve", "master", "understand", "practise", "practice",
                 "score", "ace", "revise", "succeed", "confident"]

FEATURE_WORDS = ["platform", "system", "tool", "software", "app", "solution", "service",
                 "product", "powered", "built", "designed", "uses", "using"]

STRONG_CTA_PATTERN = re.compile(
    r'(start practis|try (?:for )?free|try exampilot|get started free|begin practis|'
    r'join.*?free|practise free|sign up free)',
    re.IGNORECASE,
)

GENERIC_CTA_PATTERN = re.compile(
    r'\b(sign up|get started|learn more|click here|join now|start now|register)\b',
    re.IGNORECASE,
)

ANY_CTA_PATTERN = re.compile(
    r'\b(start|try|get|join|begin|practise|practice|sign|register)\b',
    re.IGNORECASE,
)

NAMED_TRUST_PATTERN = re.compile(
    r'\d[\d,]*\s+(?:cambridge\s+)?students?\s+(?:practis|using|revising)',
    re.IGNORECASE,
)

GENERIC_TRUST_PATTERN = re.compile(
    r'join\s+(?:thousands|hundreds|students)|trusted by|used by',
    re.IGNORECASE,
)

BELOW_FOLD_TRUST_PATTERN = re.compile(
    r'(\d[\d,]*\s+students?|free trial|testimonial|".*?")',
    re.IGNORECASE,
)

EXAM_KEYWORD_PATTERN = re.compile(
    r'(9709|wma\d+|a.?level|cambridge|edexcel|gcse|alevel)',
    re.IGNORECASE,
)


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


def _first_n_words(body: str, n: int) -> str:
    """Return first n words of body as a single string."""
    words = body.split()
    return " ".join(words[:n])


def _extract_h1(body: str) -> Optional[str]:
    """Extract the H1 heading text from body."""
    match = re.search(r'^#\s+(.+)', body, re.MULTILINE)
    return match.group(1).strip() if match else None


def _extract_first_paragraph(body: str) -> str:
    """Extract the first non-heading paragraph."""
    lines = body.splitlines()
    para_lines = []
    in_para = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        if stripped == "":
            if in_para:
                break
            continue
        para_lines.append(stripped)
        in_para = True
    return " ".join(para_lines)


# ---------------------------------------------------------------------------
# Graders
# ---------------------------------------------------------------------------

def _grade_headline(h1: Optional[str]) -> tuple[str, str]:
    """Grade the H1 headline. Returns (grade, suggestion)."""
    if not h1:
        return "D", "No H1 heading found — add a single, clear H1 as the first heading."

    has_outcome = any(w in h1.lower() for w in OUTCOME_WORDS)
    has_keyword = bool(EXAM_KEYWORD_PATTERN.search(h1))
    char_count = len(h1)

    if has_outcome and has_keyword and char_count <= 60:
        return "A", ""
    elif has_keyword and char_count <= 60:
        return "B", "Add an outcome word to the H1 (e.g. 'master', 'pass', 'improve') for stronger impact."
    elif has_keyword and char_count > 60:
        return "C", f"H1 is {char_count} characters — trim to 60 or fewer for clarity and CTR."
    else:
        return "D", "H1 lacks a keyword. Include the exam topic/code so students immediately know this is for them."


def _grade_value_proposition(first_para: str) -> tuple[str, str]:
    """Grade the value proposition in the first paragraph."""
    if not first_para:
        return "D", "No opening paragraph found — add a direct answer as the first piece of body text."

    sentences = re.split(r'(?<=[.!?])\s+', first_para.strip())
    first_two = " ".join(sentences[:2]).lower()

    has_answer = any(sig in first_two for sig in ["is ", "are ", "means ", "allows ", "helps ", "enables ", "gives "])
    has_specific = bool(re.search(r'\d|specific|exactly|every|all ', first_two, re.IGNORECASE))
    is_feature_focused = any(w in first_two for w in FEATURE_WORDS)

    if has_answer and has_specific:
        return "A", ""
    elif has_answer and not is_feature_focused:
        return "B", "First 2 sentences answer the 'what', but add a specific claim (number, outcome, exam board)."
    elif is_feature_focused:
        return "C", "Opening is feature-focused — rewrite to lead with the student benefit, not the product."
    else:
        return "D", "Opening doesn't clearly answer 'what does ExamPilot do for me?' — be direct in sentence 1."


def _grade_cta(above_fold_text: str, full_body: str) -> tuple[str, str]:
    """Grade the CTA visible above the fold."""
    if STRONG_CTA_PATTERN.search(above_fold_text):
        return "A", ""
    elif GENERIC_CTA_PATTERN.search(above_fold_text):
        return "B", "CTA is present but generic — replace 'Get Started' with benefit copy like 'Start Practising Free'."
    elif ANY_CTA_PATTERN.search(above_fold_text):
        return "B", "CTA-like language present but not action+benefit format — be explicit about what happens next."
    elif ANY_CTA_PATTERN.search(full_body):
        return "C", "CTA found below the fold only — move the primary CTA into the first 150 words."
    else:
        return "D", "No CTA detected anywhere — add at least one CTA with action + benefit copy."


def _grade_trust_signal(above_fold_text: str, full_body: str) -> tuple[str, str]:
    """Grade the trust signal visible above the fold."""
    if NAMED_TRUST_PATTERN.search(above_fold_text):
        return "A", ""
    elif GENERIC_TRUST_PATTERN.search(above_fold_text):
        return "B", "Trust signal is generic ('join thousands') — add a specific, quantified number."
    elif BELOW_FOLD_TRUST_PATTERN.search(full_body):
        return "C", "Trust signal found below the fold — move it into the first 150 words."
    else:
        return "D", "No trust signal found — add a student count, testimonial, or exam board reference above the fold."


# ---------------------------------------------------------------------------
# Core function
# ---------------------------------------------------------------------------

def analyze_above_fold(content: str, approx_fold_words: int = 150) -> dict:
    """Analyze the first ~150 words of a page for above-fold CRO elements."""
    body = _strip_frontmatter(content)
    above_fold = _first_n_words(body, approx_fold_words)

    h1 = _extract_h1(body)
    first_para = _extract_first_paragraph(body)

    headline_grade, headline_suggestion = _grade_headline(h1)
    vp_grade, vp_suggestion = _grade_value_proposition(first_para)
    cta_grade, cta_suggestion = _grade_cta(above_fold, body)
    trust_grade, trust_suggestion = _grade_trust_signal(above_fold, body)

    grades = {
        "headline": {"grade": headline_grade, "text": h1, "suggestion": headline_suggestion},
        "value_proposition": {"grade": vp_grade, "text": first_para[:200] if first_para else None, "suggestion": vp_suggestion},
        "cta": {"grade": cta_grade, "suggestion": cta_suggestion},
        "trust_signal": {"grade": trust_grade, "suggestion": trust_suggestion},
    }

    grade_values = {"A": 4, "B": 3, "C": 2, "D": 1}
    avg_score = sum(grade_values[g["grade"]] for g in grades.values()) / len(grades)
    overall = "A" if avg_score >= 3.5 else "B" if avg_score >= 2.5 else "C" if avg_score >= 1.5 else "D"

    top_fixes = [
        g["suggestion"]
        for g in grades.values()
        if g["grade"] not in ("A",) and g["suggestion"]
    ]

    return {
        "overall_grade": overall,
        "fold_words_analyzed": approx_fold_words,
        "grades": grades,
        "top_fixes": top_fixes,
        "above_fold_excerpt": above_fold[:300],
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _print_report(result: dict) -> None:
    """Print a human-readable above-fold analysis report."""
    print(f"\nAbove-Fold Analysis — Overall Grade: {result['overall_grade']}")
    print(f"Analyzed first {result['fold_words_analyzed']} words")
    print("=" * 60)
    for element, data in result["grades"].items():
        label = element.replace("_", " ").title()
        print(f"  {label:22s} [{data['grade']}]")
        if data.get("text"):
            print(f"    Text: \"{data['text'][:80]}...\"" if len(data["text"]) > 80 else f"    Text: \"{data['text']}\"")
        if data["suggestion"]:
            print(f"    Fix: {data['suggestion']}")
    if result["top_fixes"]:
        print("\nTop Fixes:")
        for fix in result["top_fixes"]:
            print(f"  - {fix}")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze above-fold CRO elements in a landing page draft")
    parser.add_argument("filepath", nargs="?", help="Path to markdown file")
    parser.add_argument("--fold-words", type=int, default=150, help="Approx word count of above-fold area (default: 150)")
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

    result = analyze_above_fold(content, approx_fold_words=args.fold_words)

    if args.json_out:
        print(json.dumps(result, indent=2))
    else:
        _print_report(result)
