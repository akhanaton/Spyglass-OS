"""
Trust Signal Analyzer

Detects and grades trust signals (social proof, authority markers, risk reversal)
in landing page or article content. Used by /landing-audit and the
landing-page-optimizer agent.
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
# Patterns
# ---------------------------------------------------------------------------

# Social proof
NAMED_TESTIMONIAL_PATTERN = re.compile(
    r'["""](.{20,300})["""][\s\n]*[-—]\s*\w+[\s,]',
    re.DOTALL,
)
STUDENT_COUNT_PATTERN = re.compile(
    r'\b(\d[\d,]*)\s+(?:cambridge\s+|international\s+|a.?level\s+)?students?\b',
    re.IGNORECASE,
)
USAGE_METRIC_PATTERN = re.compile(
    r'\b\d[\d,]+\s+(?:questions?\s+(?:answered|practised|completed)|practice\s+sessions?|'
    r'exam\s+sessions?|hours?\s+of\s+practice)\b',
    re.IGNORECASE,
)
GENERIC_SOCIAL_PATTERN = re.compile(
    r'\b(?:join\s+(?:thousands|hundreds)|trusted\s+by|used\s+by\s+students|'
    r'loved\s+by|popular\s+with)\b',
    re.IGNORECASE,
)

# Authority markers
EXAM_BOARD_FULL_PATTERN = re.compile(
    r'(?:cambridge\s+assessment\s+international\s+education|pearson\s+edexcel|ofqual|'
    r'cambridge\s+international|cambridge\s+a.?level)',
    re.IGNORECASE,
)
PAPER_CODE_PATTERN = re.compile(
    r'\b(9709|9MA\d|WMA\d{2}|WST\d{2}|9MA0|9FM0)[/\-\d]*\b',
    re.IGNORECASE,
)
OFFICIAL_URL_PATTERN = re.compile(
    r'\b(?:cambridge\.org|pearson\.com|ofqual\.gov\.uk|cambridgeinternational\.org)\b',
    re.IGNORECASE,
)

# Risk reversal
FREE_TRIAL_PATTERN = re.compile(
    r'\b(?:free\s+trial|try\s+(?:for\s+)?free|no\s+credit\s+card|'
    r'free\s+to\s+(?:try|use|start)|start\s+free)\b',
    re.IGNORECASE,
)
CANCEL_PATTERN = re.compile(
    r'\b(?:cancel\s+any\s+?time|no\s+commitment|no\s+lock.?in|month.?to.?month)\b',
    re.IGNORECASE,
)
MONEY_BACK_PATTERN = re.compile(
    r'\b(?:money.?back\s+guarantee|\d+.?day\s+guarantee|refund\s+policy)\b',
    re.IGNORECASE,
)

# Specific outcome with VERIFY flag
SPECIFIC_OUTCOME_PATTERN = re.compile(
    r'\b(?:improved|went\s+from|raised|boosted|increased)\b.{5,60}\b(?:grade|mark|score|'
    r'A\*|pass)\b',
    re.IGNORECASE | re.DOTALL,
)


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def _strip_frontmatter(content: str) -> str:
    """Remove YAML frontmatter block from content."""
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            return content[end + 3:].lstrip()
    return content


# ---------------------------------------------------------------------------
# Category analyzers
# ---------------------------------------------------------------------------

def _analyze_social_proof(body: str) -> dict:
    """Find social proof signals in body text."""
    named = NAMED_TESTIMONIAL_PATTERN.findall(body)
    student_counts = STUDENT_COUNT_PATTERN.findall(body)
    usage_metrics = USAGE_METRIC_PATTERN.findall(body)
    generic = GENERIC_SOCIAL_PATTERN.findall(body)
    specific_outcomes = SPECIFIC_OUTCOME_PATTERN.findall(body)

    return {
        "named_testimonials": len(named),
        "student_counts": len(student_counts),
        "usage_metrics": len(usage_metrics),
        "generic": len(generic),
        "specific_outcomes": len(specific_outcomes),
        "examples": {
            "testimonials": [t[:100] for t in named[:2]],
            "counts": [str(c) for c in student_counts[:2]],
        },
    }


def _analyze_authority_markers(body: str) -> dict:
    """Find authority markers in body text."""
    exam_board_refs = EXAM_BOARD_FULL_PATTERN.findall(body)
    paper_codes = PAPER_CODE_PATTERN.findall(body)
    official_urls = OFFICIAL_URL_PATTERN.findall(body)

    return {
        "exam_board_refs": len(exam_board_refs),
        "paper_codes": len(set(paper_codes)),  # unique codes
        "official_urls": len(official_urls),
        "boards_found": list(set(r.lower() for r in exam_board_refs))[:3],
    }


def _analyze_risk_reversal(body: str) -> dict:
    """Find risk reversal statements in body text."""
    has_free_trial = bool(FREE_TRIAL_PATTERN.search(body))
    has_cancel = bool(CANCEL_PATTERN.search(body))
    has_money_back = bool(MONEY_BACK_PATTERN.search(body))

    return {
        "free_trial": has_free_trial,
        "cancel_anytime": has_cancel,
        "money_back": has_money_back,
    }


# ---------------------------------------------------------------------------
# Grading
# ---------------------------------------------------------------------------

def _compute_grade(
    social: dict,
    authority: dict,
    risk: dict,
) -> tuple[str, str]:
    """Compute overall trust signal grade and top gap."""
    has_named_testimonial = social["named_testimonials"] > 0
    has_authority = authority["exam_board_refs"] > 0 or authority["paper_codes"] > 0
    has_risk_reversal = risk["free_trial"] or risk["cancel_anytime"]
    has_specific_social = social["student_counts"] > 0 or social["usage_metrics"] > 0

    categories_present = sum([
        has_named_testimonial or has_specific_social,
        has_authority,
        has_risk_reversal,
    ])

    if has_named_testimonial and has_authority and has_risk_reversal:
        grade = "Excellent"
        gap = ""
    elif categories_present >= 2:
        grade = "Good"
        if not has_named_testimonial:
            gap = ("Add a named testimonial with specific exam outcome "
                   "(e.g. 'Maya improved from D to A* in 6 weeks'). Add [VERIFY] flag.")
        elif not has_risk_reversal:
            gap = "Add a risk reversal statement: 'free trial', 'no credit card required', or 'cancel anytime'."
        else:
            gap = "Add an authority marker: reference Cambridge Assessment International Education or a specific paper code."
    elif categories_present == 1:
        grade = "Weak"
        if not (has_named_testimonial or has_specific_social):
            gap = "Add social proof: a student count or testimonial. Generic phrases like 'join thousands' are not enough."
        elif not has_authority:
            gap = "Add an exam board reference: name Cambridge Assessment International Education or Pearson Edexcel explicitly."
        else:
            gap = "Add a risk reversal: 'free trial', 'no credit card', or 'cancel anytime' reduces conversion friction."
    else:
        grade = "Missing"
        gap = ("No trust signals detected. Add: (1) a student count or testimonial, "
               "(2) exam board name, (3) risk reversal statement.")

    return grade, gap


# ---------------------------------------------------------------------------
# Core function
# ---------------------------------------------------------------------------

def analyze_trust_signals(content: str) -> dict:
    """Detect and grade trust signals in landing page or article content."""
    body = _strip_frontmatter(content)

    social = _analyze_social_proof(body)
    authority = _analyze_authority_markers(body)
    risk = _analyze_risk_reversal(body)
    grade, top_gap = _compute_grade(social, authority, risk)

    return {
        "social_proof": social,
        "authority_markers": authority,
        "risk_reversal": risk,
        "grade": grade,
        "top_gap": top_gap,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _print_report(result: dict) -> None:
    """Print a human-readable trust signal report."""
    print(f"\nTrust Signal Analysis — Grade: {result['grade']}")
    print("=" * 60)

    sp = result["social_proof"]
    print(f"  Social Proof:")
    print(f"    Named testimonials : {sp['named_testimonials']}")
    print(f"    Student counts     : {sp['student_counts']}")
    print(f"    Usage metrics      : {sp['usage_metrics']}")
    print(f"    Generic social     : {sp['generic']}")
    print(f"    Specific outcomes  : {sp['specific_outcomes']}")

    am = result["authority_markers"]
    print(f"\n  Authority Markers:")
    print(f"    Exam board refs    : {am['exam_board_refs']}")
    if am["boards_found"]:
        print(f"    Boards found       : {', '.join(am['boards_found'])}")
    print(f"    Paper codes        : {am['paper_codes']}")
    print(f"    Official URLs      : {am['official_urls']}")

    rr = result["risk_reversal"]
    print(f"\n  Risk Reversal:")
    print(f"    Free trial         : {rr['free_trial']}")
    print(f"    Cancel anytime     : {rr['cancel_anytime']}")
    print(f"    Money-back         : {rr['money_back']}")

    if result["top_gap"]:
        print(f"\nTop gap: {result['top_gap']}")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect and grade trust signals in a landing page draft")
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

    result = analyze_trust_signals(content)

    if args.json_out:
        print(json.dumps(result, indent=2))
    else:
        _print_report(result)
