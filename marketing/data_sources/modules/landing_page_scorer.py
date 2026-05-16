"""
Landing Page Scorer

Scores a landing page draft on CRO quality (0-100) across 5 pillars.
Used by /landing-write and the landing-page-optimizer agent.

Pillars (20pts each):
  1. Above-fold
  2. CTA quality
  3. Trust signals
  4. Friction (deductions)
  5. Structure
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

PASS_THRESHOLD = 75
NEEDS_WORK_THRESHOLD = 60

OUTCOME_WORDS = ["improve", "pass", "master", "understand", "practise", "practice", "score", "ace", "revise"]

BANNED_PHRASES = ["leverage", "enterprise", "ai tutor", "ai-powered", "synergy", "streamline"]

BANNED_PHRASES_CRO = ["leverage", "enterprise", "ai tutor", "ai-powered", "synergy", "streamline",
                       "revolutionary", "game-changing"]

B2B_PHRASES = ["school licensing", "institutional", "department", "procurement", "b2b"]

EM_DASH_PATTERN = re.compile(r'—')

EXAM_BOARD_NAMES = [
    "cambridge assessment international education",
    "pearson edexcel",
    "ofqual",
    "cie",
]

INTERNAL_LINK_PATTERNS = ["/cambridge/", "/pricing", "/features", "/blog/", "/waitlist"]


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


def _extract_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter as a simple key-value dict (no yaml dependency)."""
    result = {}
    if not content.startswith("---"):
        return result
    end = content.find("---", 3)
    if end == -1:
        return result
    block = content[3:end]
    for line in block.splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            result[k.strip()] = v.strip()
    return result


def _first_n_words(body: str, n: int) -> str:
    """Return the first n words of body text as a string."""
    words = body.split()
    return " ".join(words[:n])


def _count_internal_links(body: str) -> int:
    """Count markdown links pointing to internal paths."""
    md_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', body)
    count = 0
    for _, href in md_links:
        if href.startswith("/") or any(p in href for p in INTERNAL_LINK_PATTERNS):
            count += 1
    return count


def _count_faq_pairs(body: str) -> int:
    """Count Q&A pairs in FAQ section."""
    faq_match = re.search(r'##\s+(?:FAQ|Frequently Asked Questions)(.*?)(?=##|\Z)', body, re.DOTALL | re.IGNORECASE)
    if not faq_match:
        return 0
    faq_text = faq_match.group(1)
    questions = re.findall(r'(?:\*\*Q:|###|\*\*)[^\n]+\?', faq_text)
    if not questions:
        questions = re.findall(r'\?\n', faq_text)
    return len(questions)


def _avg_paragraph_sentences(text: str, word_limit: int = 500) -> float:
    """Average sentences per paragraph in the first word_limit words."""
    excerpt = " ".join(text.split()[:word_limit])
    paragraphs = [p.strip() for p in re.split(r'\n\n+', excerpt) if p.strip()]
    if not paragraphs:
        return 0.0
    sentence_counts = []
    for para in paragraphs:
        sentences = re.split(r'(?<=[.!?])\s+', para)
        sentence_counts.append(len(sentences))
    return sum(sentence_counts) / len(sentence_counts)


# ---------------------------------------------------------------------------
# Pillar scorers
# ---------------------------------------------------------------------------

def _score_above_fold(body: str) -> tuple[int, list[str]]:
    """Score above-fold elements (20 pts). Returns (score, issues)."""
    score = 0
    issues = []
    first_400 = _first_n_words(body, 80)  # ~400 words approx

    # H1 present (3pts)
    h1_match = re.search(r'^#\s+.+', body, re.MULTILINE)
    if h1_match:
        score += 3
    else:
        issues.append("No H1 heading found")

    # H1 contains outcome word (5pts)
    if h1_match:
        h1_text = h1_match.group(0).lower()
        if any(w in h1_text for w in OUTCOME_WORDS):
            score += 5
        else:
            issues.append("H1 does not contain an outcome word (pass, master, improve, practise, etc.)")

    # First 2 sentences answer directly (4pts)
    first_sentences = re.split(r'(?<=[.!?])\s+', body.strip())[:3]
    first_two = " ".join(first_sentences[:2]).lower()
    direct_signals = ["is ", "are ", "means ", "allows ", "helps ", "enables "]
    if any(s in first_two for s in direct_signals):
        score += 4
    else:
        issues.append("First 2 sentences don't directly answer a question (GEO requirement)")

    # CTA present in first 400 words (5pts)
    cta_pattern = re.compile(r'\b(start|try|get|join|begin|practise|practice|sign|register)\b', re.IGNORECASE)
    if cta_pattern.search(first_400):
        score += 5
    else:
        issues.append("No CTA found in first 400 words")

    # Trust signal in first 400 words (3pts)
    trust_pattern = re.compile(
        r'(\d[\d,]*\s+students?|free trial|no credit card|cambridge|edexcel)', re.IGNORECASE
    )
    if trust_pattern.search(first_400):
        score += 3
    else:
        issues.append("No trust signal found in first 400 words")

    return score, issues


def _score_cta_quality(body: str) -> tuple[int, list[str]]:
    """Score CTA quality (20 pts). Returns (score, issues)."""
    score = 0
    issues = []
    wc = _word_count(body)

    # At least 1 CTA (4pts)
    cta_pattern = re.compile(r'\b(start|try|get|join|begin|practise|practice|sign|register)\b', re.IGNORECASE)
    cta_matches = cta_pattern.findall(body)
    if cta_matches:
        score += 4
    else:
        issues.append("No CTA found anywhere on page")
        return score, issues

    # CTA uses action + benefit (6pts)
    strong_cta_pattern = re.compile(
        r'(start practis|try (?:for )?free|try exampilot|start your|begin practis|practise free)',
        re.IGNORECASE,
    )
    if strong_cta_pattern.search(body):
        score += 6
    else:
        issues.append("CTA copy is generic — use action + benefit (e.g. 'Start Practising Free')")

    # CTA appears 3+ times for long pages (5pts)
    if wc > 800:
        if len(cta_matches) >= 3:
            score += 5
        else:
            issues.append(f"Only {len(cta_matches)} CTA(s) found — long pages need 3+ CTAs")
    else:
        score += 5  # Not required for short pages

    # EUR pricing present if pricing mentioned (5pts)
    if re.search(r'\bpri(?:ce|cing)\b', body, re.IGNORECASE):
        if re.search(r'EUR\s*\d+|\d+\s*EUR|€\s*\d+|\d+\s*€', body):
            score += 5
        elif re.search(r'£|\$(?!\d{4})', body):  # GBP or USD
            issues.append("Pricing uses GBP (£) or USD ($) — ExamPilot pricing is EUR only")
        else:
            issues.append("Pricing mentioned but no EUR amount found")
    else:
        score += 5  # No pricing = not applicable

    return score, issues


def _score_trust_signals(body: str) -> tuple[int, list[str]]:
    """Score trust signals (20 pts). Returns (score, issues)."""
    score = 0
    issues = []

    # Testimonial or social proof (5pts, +3 bonus if named + specific)
    testimonial_pattern = re.compile(r'[""](.{20,200})[""].*?[-—]\s*\w+', re.DOTALL)
    student_count_pattern = re.compile(r'\d[\d,]*\s+(?:cambridge\s+)?students?', re.IGNORECASE)
    generic_social = re.compile(r'join\s+(?:thousands|hundreds|students)', re.IGNORECASE)

    if testimonial_pattern.search(body):
        score += 5
        specific_pattern = re.compile(r'[""].{20,200}[""].*?\b(?:A\*|grade|improved|passed)\b', re.DOTALL)
        if specific_pattern.search(body):
            score += 3  # bonus
    elif student_count_pattern.search(body):
        score += 5
    elif generic_social.search(body):
        score += 2
        issues.append("Social proof is generic — add a named testimonial or specific student count")
    else:
        issues.append("No social proof or testimonials found")

    # Exam board reference (5pts)
    exam_board_pattern = re.compile(
        r'(cambridge assessment international education|pearson edexcel|ofqual|cie)',
        re.IGNORECASE,
    )
    if exam_board_pattern.search(body):
        score += 5
    else:
        issues.append("No exam board reference found (Cambridge Assessment International Education, Pearson Edexcel)")

    # Risk reversal (5pts)
    risk_pattern = re.compile(r'free trial|try for free|no credit card|cancel anytime', re.IGNORECASE)
    if risk_pattern.search(body):
        score += 5
    else:
        issues.append("No risk reversal statement found ('free trial', 'no credit card', etc.)")

    # Specific metric or student outcome (5pts)
    metric_pattern = re.compile(r'\d+[\d,%]+\s+(?:students?|questions?|sessions?|%)', re.IGNORECASE)
    if metric_pattern.search(body):
        score += 5
    else:
        issues.append("No specific metric or student outcome found")

    return min(score, 20), issues  # Cap at 20 (testimonial bonus can push it over)


def _score_friction(body: str) -> tuple[int, list[str]]:
    """Score friction (20 pts starting, deductions applied). Returns (score, issues)."""
    score = 20
    issues = []

    # Banned phrases (deduct 4pts each)
    for phrase in BANNED_PHRASES:
        pattern = re.compile(re.escape(phrase), re.IGNORECASE)
        matches = pattern.findall(body)
        if matches:
            deduction = min(4 * len(matches), 8)  # cap per phrase
            score -= deduction
            issues.append(f"Banned phrase '{phrase}' found {len(matches)}x (remove it)")

    # Em-dashes (deduct 2pts each, max 6)
    em_count = len(EM_DASH_PATTERN.findall(body))
    if em_count:
        score -= min(em_count * 2, 6)
        issues.append(f"Em-dashes (—) found: {em_count} instance(s) — use commas or hyphens instead")

    # B2B language (deduct 5pts)
    for phrase in B2B_PHRASES:
        if re.search(re.escape(phrase), body, re.IGNORECASE):
            score -= 5
            issues.append(f"B2B language found: '{phrase}' — ExamPilot is consumer-only")
            break

    # Average paragraph sentence count (10pts proportional)
    avg_sentences = _avg_paragraph_sentences(body)
    if avg_sentences <= 4:
        score += 0  # already at full
    else:
        deduction = min(int((avg_sentences - 4) * 2), 10)
        score -= deduction
        if deduction > 0:
            issues.append(f"Paragraphs average {avg_sentences:.1f} sentences — keep to 4 or fewer")

    return max(0, score), issues


def _score_structure(body: str) -> tuple[int, list[str]]:
    """Score structure (20 pts). Returns (score, issues)."""
    score = 0
    issues = []

    # FAQ section present (6pts)
    faq_present = bool(re.search(r'##\s+(?:FAQ|Frequently Asked Questions)', body, re.IGNORECASE))
    if faq_present:
        score += 6
    else:
        issues.append("No FAQ section found (## FAQ or ## Frequently Asked Questions)")

    # 4+ Q&A pairs in FAQ (4pts)
    faq_count = _count_faq_pairs(body)
    if faq_count >= 4:
        score += 4
    elif faq_count > 0:
        issues.append(f"Only {faq_count} FAQ pair(s) found — add at least 4 Q&A pairs")
    else:
        issues.append("FAQ section is empty or Q&A pairs not detected")

    # Internal links (5pts)
    internal_links = _count_internal_links(body)
    if internal_links >= 3:
        score += 5
    else:
        issues.append(f"Only {internal_links} internal link(s) — add at least 3 internal links")

    # Conclusion/CTA section at end (5pts)
    conclusion_pattern = re.compile(r'##\s+(?:conclusion|next steps?|get started|ready to|start practis)', re.IGNORECASE)
    # Also check last 200 words for CTA presence
    last_200 = " ".join(body.split()[-200:])
    cta_in_last = re.search(r'\b(start|try|practise|practice)\b', last_200, re.IGNORECASE)
    if conclusion_pattern.search(body) or cta_in_last:
        score += 5
    else:
        issues.append("No conclusion or closing CTA section found at end of page")

    return score, issues


# ---------------------------------------------------------------------------
# Core function
# ---------------------------------------------------------------------------

def score_landing_page(content: str, page_type: str = "topic_hub") -> dict:
    """Score a landing page draft across 5 CRO pillars. Returns score and breakdown."""
    body = _strip_frontmatter(content)

    above_fold_score, above_fold_issues = _score_above_fold(body)
    cta_score, cta_issues = _score_cta_quality(body)
    trust_score, trust_issues = _score_trust_signals(body)
    friction_score, friction_issues = _score_friction(body)
    structure_score, structure_issues = _score_structure(body)

    total = above_fold_score + cta_score + trust_score + friction_score + structure_score
    total = max(0, min(100, total))

    all_issues = above_fold_issues + cta_issues + trust_issues + friction_issues + structure_issues

    if total >= PASS_THRESHOLD:
        verdict = "PASS"
        recommendation = "Ready for review."
    elif total >= NEEDS_WORK_THRESHOLD:
        verdict = "NEEDS WORK"
        recommendation = f"Fix these issues: {'; '.join(all_issues[:3])}"
    else:
        verdict = "BLOCKED"
        recommendation = f"Critical issues: {'; '.join(all_issues)}"

    return {
        "total_score": total,
        "verdict": verdict,
        "recommendation": recommendation,
        "pillars": {
            "above_fold": {"score": above_fold_score, "max": 20, "issues": above_fold_issues},
            "cta_quality": {"score": cta_score, "max": 20, "issues": cta_issues},
            "trust_signals": {"score": trust_score, "max": 20, "issues": trust_issues},
            "friction": {"score": friction_score, "max": 20, "issues": friction_issues},
            "structure": {"score": structure_score, "max": 20, "issues": structure_issues},
        },
        "all_issues": all_issues,
        "page_type": page_type,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _print_report(result: dict) -> None:
    """Print a human-readable scoring report."""
    print(f"\nLanding Page CRO Score: {result['total_score']}/100 — {result['verdict']}")
    print(f"Recommendation: {result['recommendation']}")
    print("=" * 60)
    for pillar, data in result["pillars"].items():
        status = "OK" if not data["issues"] else "ISSUES"
        print(f"  {pillar.replace('_', ' ').title():20s} {data['score']:>3}/{data['max']}  [{status}]")
        for issue in data["issues"]:
            print(f"    - {issue}")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Score a landing page draft on CRO quality")
    parser.add_argument("filepath", nargs="?", help="Path to markdown file")
    parser.add_argument(
        "--page-type",
        choices=["topic_hub", "comparison", "feature"],
        default="topic_hub",
        help="Page type (default: topic_hub)",
    )
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

    result = score_landing_page(content, page_type=args.page_type)

    if args.json_out:
        print(json.dumps(result, indent=2))
    else:
        _print_report(result)
