"""
Keyword Analyzer

Analyzes keyword density, distribution, and semantic coverage in a markdown article.
Extracts primary keyword from YAML frontmatter or CLI argument.

Outputs JSON-compatible dict and human-readable summary.
Target audience: ExamPilot — A-Level Maths content for 16-18 year old students.
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
# A-Level Maths LSI / semantic term groups
# ---------------------------------------------------------------------------

AMATH_LSI_GROUPS: dict[str, list[str]] = {
    "algebra": [
        "quadratic", "polynomial", "factori", "expand", "simplif", "expression",
        "equation", "inequality", "simultaneous", "logarithm", "exponent",
    ],
    "calculus": [
        "differentiat", "integrat", "derivative", "integral", "gradient", "stationary",
        "turning point", "chain rule", "product rule", "quotient rule",
        "definite integral", "indefinite integral", "area under", "rate of change",
    ],
    "trigonometry": [
        "sine", "cosine", "tangent", "sin", "cos", "tan", "radian", "degree",
        "identit", "pythagorean", "CAST diagram", "general solution",
    ],
    "statistics": [
        "mean", "median", "mode", "variance", "standard deviation", "probability",
        "distribution", "normal distribution", "binomial", "hypothesis test",
        "correlation", "regression", "sample", "population",
    ],
    "pure_maths": [
        "proof", "induction", "contradiction", "modulus", "argument", "complex",
        "vector", "matrix", "transform", "sequence", "series", "arithmetic",
        "geometric", "convergence", "divergence",
    ],
    "mechanics": [
        "force", "velocity", "acceleration", "displacement", "Newton", "momentum",
        "projectile", "friction", "equilibrium", "moment", "resolving",
    ],
    "exam_prep": [
        "mark scheme", "past paper", "worked example", "step by step", "cambridge 9709",
        "edexcel ial", "a level maths", "syllabus", "specification", "examiner",
        "practice question", "revision",
    ],
}


# ---------------------------------------------------------------------------
# Frontmatter helpers
# ---------------------------------------------------------------------------

def _parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML frontmatter and return (fields_dict, body_text)."""
    if not text.startswith("---"):
        return {}, text
    match = re.match(r"^---\n(.*?)\n---\n?(.*)", text, re.DOTALL)
    if not match:
        return {}, text
    fm_raw = match.group(1)
    body = match.group(2)
    fields: dict[str, str | list] = {}
    for line in fm_raw.split("\n"):
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            # Handle simple lists: "- item" lines following a key
            if value.startswith("[") and value.endswith("]"):
                items = [v.strip().strip('"').strip("'") for v in value[1:-1].split(",")]
                fields[key] = [i for i in items if i]
            else:
                fields[key] = value.strip('"').strip("'")
    return fields, body


def _strip_markdown(text: str) -> str:
    """Strip markdown formatting for word-count purposes."""
    text = re.sub(r"```[\s\S]*?```", "", text)       # fenced code
    text = re.sub(r"`[^`\n]+`", "", text)             # inline code
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)  # headings
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)       # links
    text = re.sub(r"[*_]{1,3}", "", text)             # bold/italic
    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.MULTILINE)  # list markers
    text = re.sub(r"^\s*\d+\.\s+", "", text, flags=re.MULTILINE)  # ordered lists
    return text.strip()


def _count_words(text: str) -> int:
    """Count words in plain text."""
    return len(text.split())


def _get_headings(body: str) -> dict[str, list[str]]:
    """Extract H1 and H2 headings from body markdown."""
    h1 = re.findall(r"^#\s+(.+)$", body, re.MULTILINE)
    h2 = re.findall(r"^##\s+(.+)$", body, re.MULTILINE)
    return {"h1": h1, "h2": h2}


# ---------------------------------------------------------------------------
# Keyword matching
# ---------------------------------------------------------------------------

def _normalize_keyword(kw: str) -> str:
    """Lowercase and strip punctuation for matching."""
    return re.sub(r"[^\w\s]", "", kw.lower()).strip()


def _count_keyword_occurrences(text: str, keyword: str) -> int:
    """Case-insensitive count of keyword (and simple plural) in text."""
    norm = _normalize_keyword(keyword)
    text_lower = text.lower()
    # Exact match
    count = len(re.findall(r"\b" + re.escape(norm) + r"\b", text_lower))
    # Simple plural: if keyword doesn't end in s, also count +s form
    if not norm.endswith("s"):
        plural = norm + "s"
        count += len(re.findall(r"\b" + re.escape(plural) + r"\b", text_lower))
    # Remove double-counting where base and plural are the same word
    # (handled by mutual exclusion via word boundary)
    return count


# ---------------------------------------------------------------------------
# Heatmap
# ---------------------------------------------------------------------------

def _build_heatmap(plain_text: str, keyword: str) -> dict:
    """Split body into 4 quarters, count keyword per quarter, return heatmap data."""
    words = plain_text.split()
    total = len(words)
    if total == 0:
        return {"quarters": [0, 0, 0, 0], "visual": "Q1[░░░░░] Q2[░░░░░] Q3[░░░░░] Q4[░░░░░]"}

    quarter_size = max(total // 4, 1)
    quarters_text = []
    for i in range(4):
        start = i * quarter_size
        end = start + quarter_size if i < 3 else total
        quarters_text.append(" ".join(words[start:end]))

    counts = [_count_keyword_occurrences(qt, keyword) for qt in quarters_text]
    max_count = max(counts) if any(counts) else 1

    def bar(n: int) -> str:
        filled = round((n / max_count) * 5) if max_count else 0
        return "█" * filled + "░" * (5 - filled)

    visual = " ".join(f"Q{i+1}[{bar(counts[i])}]" for i in range(4))
    missing_quarters = [i + 1 for i, c in enumerate(counts) if c == 0]

    return {
        "counts": counts,
        "visual": visual,
        "missing_quarters": missing_quarters,
    }


# ---------------------------------------------------------------------------
# LSI semantic detection
# ---------------------------------------------------------------------------

def _detect_lsi_terms(plain_text: str, keyword: str) -> dict:
    """Detect which LSI/semantic term groups appear in the text."""
    text_lower = plain_text.lower()
    kw_lower = keyword.lower()

    # Determine which group(s) are most relevant to the keyword
    relevant_groups = []
    for group_name, terms in AMATH_LSI_GROUPS.items():
        if any(t.lower() in kw_lower for t in terms):
            relevant_groups.append(group_name)

    # Default: check all groups if none matched
    if not relevant_groups:
        relevant_groups = list(AMATH_LSI_GROUPS.keys())

    found: dict[str, list[str]] = {}
    missing: dict[str, list[str]] = {}
    for group in relevant_groups:
        present = []
        absent = []
        for term in AMATH_LSI_GROUPS[group]:
            if term.lower() in text_lower:
                present.append(term)
            else:
                absent.append(term)
        if present:
            found[group] = present
        if absent:
            missing[group] = absent

    return {"found": found, "missing": missing, "relevant_groups": relevant_groups}


# ---------------------------------------------------------------------------
# Main analyzer
# ---------------------------------------------------------------------------

def analyze(filepath: str, keyword_override: Optional[str] = None) -> dict:
    """
    Analyze keyword density, placement, distribution, and semantic coverage for a markdown file.
    Returns a result dict with all analysis data.
    """
    path = Path(filepath)
    if not path.exists():
        return {"error": f"File not found: {filepath}"}

    text = path.read_text(encoding="utf-8")
    frontmatter, body = _parse_frontmatter(text)

    # Determine primary keyword
    keyword = keyword_override or frontmatter.get("keyword", "")
    if not keyword:
        return {
            "error": "No keyword found. Set 'keyword:' in YAML frontmatter or pass --keyword.",
            "frontmatter": frontmatter,
        }

    plain_body = _strip_markdown(body)
    word_count = _count_words(plain_body)

    # --- Density ---
    occurrences = _count_keyword_occurrences(plain_body, keyword)
    density = round((occurrences / word_count * 100), 2) if word_count else 0.0

    if density < 0.7:
        density_flag = "under_optimized"
    elif density > 2.5:
        density_flag = "stuffing_risk"
    elif density >= 1.0 and density <= 2.0:
        density_flag = "optimal"
    else:
        density_flag = "acceptable"

    # --- Placement ---
    headings = _get_headings(body)
    first_100_words = " ".join(plain_body.split()[:100])

    h1_has_kw = any(
        _count_keyword_occurrences(h, keyword) > 0 for h in headings["h1"]
    )
    first_100_has_kw = _count_keyword_occurrences(first_100_words, keyword) > 0
    h2_with_kw = [h for h in headings["h2"] if _count_keyword_occurrences(h, keyword) > 0]
    h2_count_with_kw = len(h2_with_kw)

    meta_title = frontmatter.get("meta_title", "")
    meta_desc = frontmatter.get("meta_description", "")
    meta_title_has_kw = _count_keyword_occurrences(meta_title, keyword) > 0 if meta_title else False
    meta_desc_has_kw = _count_keyword_occurrences(meta_desc, keyword) > 0 if meta_desc else False

    placement = {
        "in_h1": h1_has_kw,
        "in_first_100_words": first_100_has_kw,
        "h2_headings_with_keyword": h2_count_with_kw,
        "h2_headings_with_keyword_names": h2_with_kw,
        "in_meta_title": meta_title_has_kw,
        "in_meta_description": meta_desc_has_kw,
    }

    placement_score = sum([
        h1_has_kw,
        first_100_has_kw,
        h2_count_with_kw >= 2,
        meta_title_has_kw,
        meta_desc_has_kw,
    ])

    # --- Heatmap ---
    heatmap = _build_heatmap(plain_body, keyword)

    # --- Secondary keywords ---
    secondary_raw = frontmatter.get("secondary_keywords", [])
    if isinstance(secondary_raw, str):
        secondary_raw = [s.strip() for s in secondary_raw.split(",") if s.strip()]
    secondary_found = []
    secondary_missing = []
    for sk in secondary_raw:
        if _count_keyword_occurrences(plain_body, sk) > 0:
            secondary_found.append(sk)
        else:
            secondary_missing.append(sk)

    # --- LSI / Semantic terms ---
    lsi = _detect_lsi_terms(plain_body, keyword)

    # --- Assemble result ---
    result = {
        "keyword": keyword,
        "word_count": word_count,
        "density": {
            "occurrences": occurrences,
            "percentage": density,
            "flag": density_flag,
            "target": "1.0-2.0%",
        },
        "placement": placement,
        "placement_score": f"{placement_score}/5",
        "heatmap": heatmap,
        "secondary_keywords": {
            "found": secondary_found,
            "missing": secondary_missing,
        },
        "lsi_terms": lsi,
    }
    return result


def _print_report(result: dict) -> None:
    """Print a human-readable summary of the analysis."""
    if "error" in result:
        print(f"Error: {result['error']}")
        return

    kw = result["keyword"]
    d = result["density"]
    p = result["placement"]
    hm = result["heatmap"]
    sk = result["secondary_keywords"]

    print(f"\nKeyword Analysis — '{kw}'")
    print("=" * 50)
    print(f"Word count      : {result['word_count']}")
    print(f"Occurrences     : {d['occurrences']}")
    print(f"Density         : {d['percentage']}% ({d['flag'].replace('_', ' ')}, target {d['target']})")
    print()
    print(f"Placement score : {result['placement_score']}")
    print(f"  In H1          : {'Yes' if p['in_h1'] else 'No'}")
    print(f"  First 100 words: {'Yes' if p['in_first_100_words'] else 'No'}")
    print(f"  In 2+ H2s      : {'Yes' if p['h2_headings_with_keyword'] >= 2 else 'No'} ({p['h2_headings_with_keyword']} H2s)")
    print(f"  In meta_title  : {'Yes' if p['in_meta_title'] else 'No (or missing)'}")
    print(f"  In meta_desc   : {'Yes' if p['in_meta_description'] else 'No (or missing)'}")
    print()
    print(f"Distribution    : {hm['visual']}")
    if hm["missing_quarters"]:
        print(f"  Warning: Keyword absent from Q{hm['missing_quarters']}")
    print()
    if sk["missing"]:
        print(f"Secondary keywords missing: {', '.join(sk['missing'])}")
    if sk["found"]:
        print(f"Secondary keywords found  : {', '.join(sk['found'])}")
    print()

    lsi = result["lsi_terms"]
    if lsi["found"]:
        for group, terms in lsi["found"].items():
            print(f"LSI found ({group}): {', '.join(terms[:6])}")
    if lsi["missing"]:
        for group, terms in lsi["missing"].items():
            print(f"LSI missing ({group}): {', '.join(terms[:6])}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Analyze keyword density and semantic coverage in a markdown article."
    )
    parser.add_argument("filepath", help="Path to the markdown file")
    parser.add_argument(
        "--keyword", "-k", default=None,
        help="Primary keyword (overrides frontmatter 'keyword:' field)",
    )
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    result = analyze(args.filepath, keyword_override=args.keyword)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        _print_report(result)


if __name__ == "__main__":
    main()
