"""
CRO Checker

Runs 31 checklist-based CRO best practice validations on a landing page draft.
Binary pass/fail per check. Catches specific, fixable problems.

Categories: Headlines (5), Above-fold (4), CTAs (5), Content (6), Trust (4),
            Structure (5), ExamPilot-specific (2)
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
                 "score", "ace", "revise", "succeed"]

FEATURE_WORDS = ["platform", "system", "tool", "software", "app", "solution",
                 "powered", "built", "designed", "uses"]

BANNED_PHRASES = [
    "leverage", "ai tutor", "ai-powered", "revolutionary",
    "game-changing", "enterprise", "ai wrapper", "ai driven",
]

B2B_PHRASES = [
    "school licensing", "institutional", "procurement", "b2b",
    "for schools", "department head",
]

WEAK_CTA_PHRASES = ["get started", "sign up", "learn more", "click here", "start now"]

STRONG_CTA_PATTERN = re.compile(
    r'(start practis|try (?:for )?free|try exampilot|practise free|'
    r'start your free|get (?:instant|free) access|begin practis)',
    re.IGNORECASE,
)

ACTION_VERB_PATTERN = re.compile(
    r'\b(start|try|get|join|begin|practise|practice|sign|register|access|claim)\b',
    re.IGNORECASE,
)

EM_DASH_PATTERN = re.compile(r'—')

EUR_PATTERN = re.compile(r'EUR\s*\d+|\d+\s*EUR|€\s*\d+|\d+\s*€')
GBP_PATTERN = re.compile(r'£\s*\d+|\d+\s*£')
USD_PATTERN = re.compile(r'\$\s*\d{1,4}(?!\d{4})')  # Avoid matching years like $2026

VERIFY_PATTERN = re.compile(r'\[VERIFY\]')
METRIC_PATTERN = re.compile(r'\b\d[\d,]+\s*(?:%|students?|questions?|sessions?)\b', re.IGNORECASE)

EXAM_BOARD_PATTERN = re.compile(
    r'(cambridge assessment international education|pearson edexcel|ofqual|cambridge international)',
    re.IGNORECASE,
)
PAPER_CODE_PATTERN = re.compile(r'\b(9709|wma\d{2}|wst\d{2}|9ma\d)[/\-\d]*\b', re.IGNORECASE)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _strip_frontmatter(content: str) -> tuple[str, dict]:
    """Remove YAML frontmatter and return (body, frontmatter_dict)."""
    fm = {}
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            block = content[3:end]
            for line in block.splitlines():
                if ":" in line:
                    k, _, v = line.partition(":")
                    fm[k.strip()] = v.strip()
            return content[end + 3:].lstrip(), fm
    return content, fm


def _word_count(text: str) -> int:
    """Count words in text."""
    return len(text.split())


def _first_n_words(text: str, n: int) -> str:
    """Return first n words as string."""
    return " ".join(text.split()[:n])


def _count_h2s(body: str) -> int:
    """Count H2 headings."""
    return len(re.findall(r'^##\s+', body, re.MULTILINE))


def _count_ctas(body: str) -> int:
    """Count CTA-like action words."""
    return len(ACTION_VERB_PATTERN.findall(body))


def _faq_section(body: str) -> Optional[str]:
    """Extract FAQ section text if present."""
    match = re.search(r'##\s+(?:FAQ|Frequently Asked Questions)(.*?)(?=\n##|\Z)', body, re.DOTALL | re.IGNORECASE)
    return match.group(1) if match else None


def _count_faq_pairs(faq_text: str) -> int:
    """Count Q&A pairs in FAQ section text."""
    questions = re.findall(r'(?:\*\*Q:|###|\*\*)[^\n]+\?', faq_text)
    if not questions:
        questions = re.findall(r'\w[^\n]+\?(?=\n)', faq_text)
    return len(questions)


def _avg_sentence_length(text: str, word_limit: int = 500) -> float:
    """Average sentence word count in first word_limit words."""
    excerpt = " ".join(text.split()[:word_limit])
    sentences = re.split(r'(?<=[.!?])\s+', excerpt.strip())
    if not sentences:
        return 0.0
    lengths = [len(s.split()) for s in sentences if s.strip()]
    return sum(lengths) / len(lengths) if lengths else 0.0


def _max_paragraph_sentences(text: str, word_limit: int = 500) -> int:
    """Max sentence count in any single paragraph in first word_limit words."""
    excerpt = " ".join(text.split()[:word_limit])
    paragraphs = [p.strip() for p in re.split(r'\n\n+', excerpt) if p.strip()]
    if not paragraphs:
        return 0
    return max(len(re.split(r'(?<=[.!?])\s+', p)) for p in paragraphs)


def _jargon_density(text: str, word_limit: int = 500) -> float:
    """Ratio of 4+ syllable words in first word_limit words (rough estimate)."""
    excerpt = text.split()[:word_limit]
    if not excerpt:
        return 0.0
    # Rough syllable count: count vowel groups
    def syllables(word: str) -> int:
        word = re.sub(r'[^a-z]', '', word.lower())
        return max(1, len(re.findall(r'[aeiou]+', word)))

    long_words = sum(1 for w in excerpt if syllables(w) >= 4)
    return long_words / len(excerpt)


def _count_internal_links(body: str) -> int:
    """Count internal markdown links."""
    links = re.findall(r'\[([^\]]+)\]\((/[^)]+)\)', body)
    return len(links)


def _h2_sections_with_content(body: str, min_words: int = 100) -> bool:
    """Check that every H2 section has at least min_words of body content."""
    sections = re.split(r'^##\s+', body, flags=re.MULTILINE)
    if len(sections) <= 1:
        return True  # No H2s — not this check's concern
    for section in sections[1:]:  # Skip pre-H2 content
        # Get text until next heading
        section_body = re.split(r'^#', section, flags=re.MULTILINE)[0]
        if _word_count(section_body) < min_words:
            return False
    return True


# ---------------------------------------------------------------------------
# Checklist runner
# ---------------------------------------------------------------------------

def run_checklist(content: str, page_type: str = "topic_hub") -> dict:
    """Run 31 CRO checklist items against a landing page draft."""
    body, fm = _strip_frontmatter(content)
    wc = _word_count(body)
    first_150 = _first_n_words(body, 150)
    first_200 = _first_n_words(body, 200)
    first_300 = _first_n_words(body, 300)
    first_500 = _first_n_words(body, 500)

    h1_matches = re.findall(r'^#\s+(.+)', body, re.MULTILINE)
    h1_text = h1_matches[0] if h1_matches else ""
    keyword_from_fm = fm.get("keyword", "")

    faq_text = _faq_section(body)

    checks: list[tuple[str, bool, str]] = []

    # --- Headlines (5 checks) ---
    # 1. Exactly one H1
    checks.append((
        "Exactly one H1 present",
        len(h1_matches) == 1,
        "Remove duplicate H1 headings or add a missing H1."
    ))
    # 2. H1 <= 60 chars
    checks.append((
        "H1 <= 60 characters",
        len(h1_text) <= 60 if h1_text else False,
        f"H1 is {len(h1_text)} chars — trim to 60 or fewer.",
    ))
    # 3. H1 contains primary keyword
    kw_in_h1 = bool(keyword_from_fm and keyword_from_fm.lower() in h1_text.lower())
    checks.append((
        "H1 contains primary keyword",
        kw_in_h1 or not keyword_from_fm,  # pass if no keyword in frontmatter
        f"H1 missing primary keyword '{keyword_from_fm}' from frontmatter.",
    ))
    # 4. H1 uses outcome language
    checks.append((
        "H1 uses outcome language",
        any(w in h1_text.lower() for w in OUTCOME_WORDS),
        "H1 is feature-focused — add an outcome word (master, pass, improve, practise).",
    ))
    # 5. H2s present (at least 3)
    checks.append((
        "At least 3 H2 headings present",
        _count_h2s(body) >= 3,
        f"Only {_count_h2s(body)} H2(s) found — add more section headings.",
    ))

    # --- Above-fold (4 checks) ---
    cta_in_first_150 = bool(ACTION_VERB_PATTERN.search(first_150))
    # 6. CTA in first 150 words
    checks.append((
        "CTA present in first 150 words",
        cta_in_first_150,
        "Add a CTA button or link in the first 150 words.",
    ))
    # 7. Value proposition in first 2 sentences
    first_sentences = re.split(r'(?<=[.!?])\s+', body.strip())
    first_two = " ".join(first_sentences[:2]).lower()
    has_vp = any(s in first_two for s in ["is ", "are ", "means ", "allows ", "helps ", "enables "])
    checks.append((
        "Value proposition in first 2 sentences",
        has_vp,
        "First 2 sentences don't state what ExamPilot does — lead with a direct answer.",
    ))
    # 8. Trust signal in first 300 words
    trust_in_300 = bool(re.search(
        r'(\d[\d,]+\s+students?|free trial|cambridge|edexcel|testimonial|")',
        first_300, re.IGNORECASE,
    ))
    checks.append((
        "Trust signal in first 300 words",
        trust_in_300,
        "Add a student count, exam board reference, or free trial mention within the first 300 words.",
    ))
    # 9. No navigation overload (<=3 links in first 200 words)
    links_in_200 = len(re.findall(r'\[([^\]]+)\]\(([^)]+)\)', first_200))
    checks.append((
        "No navigation overload in first 200 words (<=3 links)",
        links_in_200 <= 3,
        f"{links_in_200} links in first 200 words — trim to 3 or fewer to reduce distraction.",
    ))

    # --- CTAs (5 checks) ---
    total_ctas = _count_ctas(body)
    # 10. At least 1 CTA
    checks.append((
        "At least 1 CTA present",
        total_ctas >= 1,
        "No CTA found — add at least one call to action.",
    ))
    # 11. CTA copy contains action verb
    checks.append((
        "CTA copy contains action verb",
        total_ctas >= 1,  # ACTION_VERB_PATTERN already requires action words
        "CTA text missing a clear action verb (start, try, join, practise).",
    ))
    # 12. CTA copy contains benefit
    has_strong_cta = bool(STRONG_CTA_PATTERN.search(body))
    checks.append((
        "CTA copy contains benefit (not just action)",
        has_strong_cta,
        "Change generic CTA ('Get Started') to action + benefit ('Start Practising Free').",
    ))
    # 13. For >1000 word pages: at least 2 CTAs
    if wc > 1000:
        checks.append((
            "Long page has at least 2 CTAs",
            total_ctas >= 2,
            f"Page is {wc} words — add a second CTA at mid-page or end.",
        ))
    else:
        checks.append(("Long page CTA count (n/a for short pages)", True, ""))

    # 14. No competing equal-weight CTAs adjacent to each other
    # Heuristic: two strong CTAs within 30 words of each other
    strong_cta_positions = [m.start() for m in STRONG_CTA_PATTERN.finditer(body)]
    competing = False
    for i in range(len(strong_cta_positions) - 1):
        gap_words = _word_count(body[strong_cta_positions[i]:strong_cta_positions[i+1]])
        if gap_words < 30:
            competing = True
            break
    checks.append((
        "No competing equal-weight CTAs adjacent",
        not competing,
        "Two CTAs appear next to each other — separate them or make one secondary.",
    ))

    # --- Content (6 checks) ---
    # 15. No em-dashes
    em_count = len(EM_DASH_PATTERN.findall(body))
    checks.append((
        "No em-dashes (—) — ExamPilot style rule",
        em_count == 0,
        f"{em_count} em-dash(es) found — replace with hyphens or commas.",
    ))
    # 16. No banned phrases
    found_banned = [p for p in BANNED_PHRASES if re.search(re.escape(p), body, re.IGNORECASE)]
    checks.append((
        "No banned phrases",
        len(found_banned) == 0,
        f"Banned phrase(s) found: {', '.join(found_banned)}. Remove them.",
    ))
    # 17. No B2B language
    found_b2b = [p for p in B2B_PHRASES if re.search(re.escape(p), body, re.IGNORECASE)]
    checks.append((
        "No B2B language",
        len(found_b2b) == 0,
        f"B2B phrase(s) found: {', '.join(found_b2b)}. ExamPilot is consumer-only.",
    ))
    # 18. Average sentence <= 25 words (first 500 words)
    avg_sent = _avg_sentence_length(body)
    checks.append((
        "Average sentence <= 25 words in first 500 words",
        avg_sent <= 25,
        f"Average sentence is {avg_sent:.0f} words — shorten sentences for readability.",
    ))
    # 19. No paragraph > 5 sentences (first 500 words)
    max_para = _max_paragraph_sentences(body)
    checks.append((
        "No paragraph > 5 sentences in first 500 words",
        max_para <= 5,
        f"Longest paragraph has {max_para} sentences — split into shorter blocks.",
    ))
    # 20. Low jargon density (<10% of 4+ syllable words)
    jargon = _jargon_density(body)
    checks.append((
        "Low jargon density (<10% long words in first 500)",
        jargon < 0.10,
        f"Jargon density is {jargon:.0%} — simplify vocabulary for 16-18 year old readers.",
    ))

    # --- Trust (4 checks) ---
    # 21. At least 1 trust signal
    has_any_trust = bool(re.search(
        r'(\d[\d,]+\s+students?|free trial|cambridge|edexcel|testimonial|")',
        body, re.IGNORECASE,
    ))
    checks.append((
        "At least 1 trust signal present",
        has_any_trust,
        "No trust signals found — add student count, testimonial, or exam board reference.",
    ))
    # 22. Risk reversal present
    has_risk_reversal = bool(re.search(
        r'(free trial|try for free|no credit card|cancel any.?time)', body, re.IGNORECASE,
    ))
    checks.append((
        "Risk reversal statement present",
        has_risk_reversal,
        "Add a risk reversal: 'free trial', 'no credit card required', or 'cancel anytime'.",
    ))
    # 23. EUR pricing only
    has_pricing_mention = bool(re.search(r'\bpri(?:ce|cing)\b', body, re.IGNORECASE))
    if has_pricing_mention:
        has_gbp = bool(GBP_PATTERN.search(body))
        has_usd = bool(USD_PATTERN.search(body))
        has_eur = bool(EUR_PATTERN.search(body))
        pricing_ok = has_eur and not has_gbp and not has_usd
        checks.append((
            "Pricing in EUR only (no GBP £ or USD $)",
            pricing_ok,
            "Pricing must use EUR only. Remove £ or $ symbols and add EUR amounts.",
        ))
    else:
        checks.append(("Pricing currency check (n/a — no pricing on page)", True, ""))

    # 24. Metric claims have [VERIFY] flag or are attributable
    metrics_present = bool(METRIC_PATTERN.search(body))
    verify_present = bool(VERIFY_PATTERN.search(body))
    checks.append((
        "Metric claims have [VERIFY] flag or are clearly attributable",
        not metrics_present or verify_present,
        "Metric claims found without [VERIFY] flag — add [VERIFY] to unconfirmed statistics.",
    ))

    # --- Structure (5 checks) ---
    # 25. FAQ section present
    checks.append((
        "FAQ section present",
        faq_text is not None,
        "Add a '## FAQ' or '## Frequently Asked Questions' section.",
    ))
    # 26. At least 4 Q&A pairs
    faq_pairs = _count_faq_pairs(faq_text) if faq_text else 0
    checks.append((
        "At least 4 Q&A pairs in FAQ section",
        faq_pairs >= 4,
        f"Only {faq_pairs} FAQ pair(s) found — add at least 4 Q&A pairs.",
    ))
    # 27. Conclusion section present
    conclusion_present = bool(re.search(
        r'##\s+(?:conclusion|next steps?|get started|ready to|start practis)',
        body, re.IGNORECASE,
    ))
    # Also accept if last 150 words contain a CTA
    last_150 = " ".join(body.split()[-150:])
    has_closing_cta = bool(ACTION_VERB_PATTERN.search(last_150))
    checks.append((
        "Conclusion section present",
        conclusion_present or has_closing_cta,
        "Add a conclusion section with a closing CTA (## Conclusion or ## Get Started).",
    ))
    # 28. At least 1 internal link
    internal_links = _count_internal_links(body)
    checks.append((
        "At least 1 internal link present",
        internal_links >= 1,
        "Add at least one internal link (to /pricing, /features, /cambridge/, /blog/).",
    ))
    # 29. No orphan content (every H2 has >= 100 words)
    checks.append((
        "No orphan H2 sections (each has >= 100 words of content)",
        _h2_sections_with_content(body),
        "One or more H2 sections have fewer than 100 words — expand or merge thin sections.",
    ))

    # --- ExamPilot-specific (2 checks — always critical if failed) ---
    # 30. No 'AI tutor' phrasing
    no_ai_tutor = not bool(re.search(r'\bai.?tutor\b', body, re.IGNORECASE))
    checks.append((
        "No 'AI tutor' phrasing",
        no_ai_tutor,
        "Remove 'AI tutor' — ExamPilot is a learning science tool, not an AI tutor.",
    ))
    # 31. No 'AI-powered' phrasing
    no_ai_powered = not bool(re.search(r'\bai.?powered\b', body, re.IGNORECASE))
    checks.append((
        "No 'AI-powered' phrasing (use 'adaptive' instead)",
        no_ai_powered,
        "Replace 'AI-powered' with 'adaptive' — brand guideline.",
    ))

    # --- Compile results ---
    passed = [(label, fix) for label, result, fix in checks if result]
    failed = [(label, fix) for label, result, fix in checks if not result]

    # Checks 30 and 31 (indices 29, 30) are critical
    critical_indices = {29, 30}
    critical_failures = [
        {"check": label, "fix": fix}
        for i, (label, result, fix) in enumerate(checks)
        if not result and i in critical_indices
    ]

    score_pct = round((len(passed) / len(checks)) * 100) if checks else 0

    return {
        "total_checks": len(checks),
        "passed": len(passed),
        "failed": len(failed),
        "score_pct": score_pct,
        "failed_items": [{"check": label, "fix": fix} for label, fix in failed if fix],
        "critical_failures": critical_failures,
        "page_type": page_type,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _print_report(result: dict) -> None:
    """Print a human-readable checklist report."""
    print(f"\nCRO Checklist — {result['passed']}/{result['total_checks']} passed ({result['score_pct']}%)")
    print(f"Page type: {result['page_type']}")

    if result["critical_failures"]:
        print("\nCRITICAL FAILURES:")
        for item in result["critical_failures"]:
            print(f"  [CRITICAL] {item['check']}")
            print(f"             Fix: {item['fix']}")

    if result["failed_items"]:
        print("\nFailed checks:")
        for item in result["failed_items"]:
            is_critical = any(c["check"] == item["check"] for c in result["critical_failures"])
            prefix = "[CRITICAL]" if is_critical else "[FAIL]"
            print(f"  {prefix} {item['check']}")
            if item["fix"]:
                print(f"           Fix: {item['fix']}")
    else:
        print("\nAll checks passed.")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run 31 CRO checklist items against a landing page draft")
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

    result = run_checklist(content, page_type=args.page_type)

    if args.json_out:
        print(json.dumps(result, indent=2))
    else:
        _print_report(result)
