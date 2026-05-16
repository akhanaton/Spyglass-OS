"""
Content Length Comparator

Benchmarks an article's word count against ExamPilot content standards and,
if DataForSEO is connected, against real SERP top-10 averages.

Excludes YAML frontmatter and code blocks from word count.
"""

import re
import os
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
# ExamPilot content standards (from marketing/context/content-standards.md)
# ---------------------------------------------------------------------------

CONTENT_STANDARDS: dict[str, dict] = {
    "blog_article": {
        "label": "Blog article",
        "min": 1800,
        "target_low": 2000,
        "target_high": 3000,
        "max": 3500,
    },
    "pillar_article": {
        "label": "Pillar article",
        "min": 3000,
        "target_low": 4000,
        "target_high": 5000,
        "max": 6000,
    },
    "comparison_page": {
        "label": "Comparison page",
        "min": 800,
        "target_low": 800,
        "target_high": 1500,
        "max": 2000,
    },
    "landing_page": {
        "label": "Landing page",
        "min": 1200,
        "target_low": 1200,
        "target_high": 2000,
        "max": 2500,
    },
}

# Map frontmatter 'type:' values to content standard keys
TYPE_MAP: dict[str, str] = {
    "article": "blog_article",
    "blog_article": "blog_article",
    "blog-article": "blog_article",
    "pillar": "pillar_article",
    "pillar_article": "pillar_article",
    "comparison": "comparison_page",
    "comparison_page": "comparison_page",
    "landing_page": "landing_page",
    "landing-page": "landing_page",
    "page": "landing_page",
}


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def _parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body_text)."""
    if not text.startswith("---"):
        return {}, text
    match = re.match(r"^---\n(.*?)\n---\n?(.*)", text, re.DOTALL)
    if not match:
        return {}, text
    fm_raw, body = match.group(1), match.group(2)
    fields: dict = {}
    for line in fm_raw.split("\n"):
        if ":" in line:
            k, _, v = line.partition(":")
            fields[k.strip()] = v.strip().strip('"').strip("'")
    return fields, body


def _strip_code_blocks(text: str) -> str:
    """Remove fenced and inline code blocks from text."""
    text = re.sub(r"```[\s\S]*?```", "", text)
    text = re.sub(r"`[^`\n]+`", "", text)
    return text


def _count_body_words(body: str) -> int:
    """Count words in body, excluding code blocks."""
    body_clean = _strip_code_blocks(body)
    # Strip markdown formatting
    body_clean = re.sub(r"^#{1,6}\s+", "", body_clean, flags=re.MULTILINE)
    body_clean = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", body_clean)
    body_clean = re.sub(r"[*_]{1,3}", "", body_clean)
    return len(body_clean.split())


def _extract_headings(body: str) -> list[str]:
    """Extract H2 headings from body for section analysis."""
    return re.findall(r"^##\s+(.+)$", body, re.MULTILINE)


# ---------------------------------------------------------------------------
# DataForSEO integration (optional)
# ---------------------------------------------------------------------------

def _get_serp_word_count(keyword: str) -> Optional[int]:
    """
    Attempt to fetch SERP top-10 average word count from DataForSEO.
    Returns None if not connected or on any error.
    """
    import base64

    login = os.getenv("DATAFORSEO_LOGIN", "")
    password = os.getenv("DATAFORSEO_PASSWORD", "")
    if not login or not password:
        return None

    try:
        import urllib.request
        import urllib.error

        credentials = base64.b64encode(f"{login}:{password}".encode()).decode()
        payload = json.dumps([{
            "keyword": keyword,
            "location_code": 2826,  # UK
            "language_code": "en",
            "device": "desktop",
            "os": "windows",
            "depth": 10,
        }])
        req = urllib.request.Request(
            "https://api.dataforseo.com/v3/serp/google/organic/live/regular",
            data=payload.encode("utf-8"),
            headers={
                "Authorization": f"Basic {credentials}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())

        tasks = data.get("tasks", [])
        if not tasks or tasks[0].get("status_code") != 20000:
            return None

        items = tasks[0].get("result", [{}])[0].get("items", [])
        word_counts = []
        for item in items:
            wc = item.get("word_count")
            if wc and isinstance(wc, int) and wc > 0:
                word_counts.append(wc)

        if not word_counts:
            return None
        return round(sum(word_counts) / len(word_counts))

    except Exception:
        return None


# ---------------------------------------------------------------------------
# Classification and suggestions
# ---------------------------------------------------------------------------

def _classify(word_count: int, standard: dict) -> str:
    """Classify word count against standard thresholds."""
    if word_count < standard["min"]:
        return "too_short"
    elif word_count > standard["max"]:
        return "too_long"
    elif standard["target_low"] <= word_count <= standard["target_high"]:
        return "on_target"
    else:
        return "acceptable"


def _expansion_suggestions(headings: list[str], word_count: int, standard: dict) -> list[str]:
    """Suggest sections to expand when article is too short."""
    deficit = standard["target_low"] - word_count
    suggestions = []
    if deficit <= 0:
        return suggestions

    suggestions.append(
        f"Article is {deficit} words below the {standard['target_low']}-word target."
    )

    if headings:
        # Generic guidance per heading type
        EXPANSION_HINTS: list[tuple[str, str]] = [
            (r"example|worked|practice|exercise", "Add 1-2 more worked examples with step-by-step solutions."),
            (r"introduc|overview|what is|background", "Expand with more context, a definition block, or a key concept table."),
            (r"tip|advice|strateg|technique", "Add a numbered checklist or 'common mistakes' callout."),
            (r"faq|question|ask", "Add 2-3 more FAQ items with concise answers."),
            (r"conclus|summary|takeaway|next step", "Expand with a revision checklist or next-step recommendations."),
        ]
        matched = set()
        for heading in headings:
            for pattern, hint in EXPANSION_HINTS:
                if re.search(pattern, heading, re.IGNORECASE) and hint not in matched:
                    suggestions.append(f"  '{heading}': {hint}")
                    matched.add(hint)
                    break

    if len(suggestions) < 3:
        suggestions.append("Consider adding: a 'Common Mistakes' section, a 'Practice Questions' block, or an FAQ.")

    return suggestions


def _reduction_suggestions(headings: list[str], word_count: int, standard: dict) -> list[str]:
    """Suggest sections to condense or spin off when article is too long."""
    excess = word_count - standard["max"]
    suggestions = []
    if excess <= 0:
        return suggestions

    suggestions.append(
        f"Article is {excess} words over the {standard['max']}-word maximum."
    )
    suggestions.append("Consider one of:")
    suggestions.append("  - Split into a pillar article + spoke article.")
    suggestions.append("  - Move advanced sections to a separate 'deep dive' article.")
    suggestions.append("  - Condense introduction — aim for 150 words max.")

    if headings:
        for heading in headings:
            if re.search(r"background|history|context|advanced|deep dive", heading, re.IGNORECASE):
                suggestions.append(
                    f"  '{heading}' could become a standalone article or moved to the wiki."
                )

    return suggestions


# ---------------------------------------------------------------------------
# Main comparator
# ---------------------------------------------------------------------------

def compare(filepath: str) -> dict:
    """
    Compare article word count against benchmarks.
    Returns full comparison result dict.
    """
    path = Path(filepath)
    if not path.exists():
        return {"error": f"File not found: {filepath}"}

    text = path.read_text(encoding="utf-8")
    frontmatter, body = _parse_frontmatter(text)

    word_count = _count_body_words(body)
    headings = _extract_headings(body)

    # Determine content type
    content_type_raw = frontmatter.get("type", "article").lower()
    standard_key = TYPE_MAP.get(content_type_raw, "blog_article")
    standard = CONTENT_STANDARDS[standard_key]

    keyword = frontmatter.get("keyword", "")

    # Try DataForSEO
    serp_avg = None
    if keyword:
        serp_avg = _get_serp_word_count(keyword)

    # Classify against standard
    classification = _classify(word_count, standard)

    # Benchmark info
    benchmark_source = "ExamPilot content standards"
    benchmark_target = f"{standard['target_low']}-{standard['target_high']}"

    if serp_avg:
        benchmark_source = f"DataForSEO SERP top-10 average + ExamPilot standards"
        serp_classification = (
            "too_short" if word_count < serp_avg * 0.7
            else "too_long" if word_count > serp_avg * 1.3
            else "on_target"
        )
    else:
        serp_classification = None

    # Suggestions
    if classification == "too_short":
        suggestions = _expansion_suggestions(headings, word_count, standard)
    elif classification == "too_long":
        suggestions = _reduction_suggestions(headings, word_count, standard)
    else:
        suggestions = ["Word count is within target range. No changes needed."]

    return {
        "filepath": filepath,
        "keyword": keyword,
        "content_type": standard["label"],
        "word_count": word_count,
        "benchmark": {
            "source": benchmark_source,
            "minimum": standard["min"],
            "target_range": benchmark_target,
            "maximum": standard["max"],
            "serp_avg": serp_avg,
        },
        "classification": classification,
        "serp_classification": serp_classification,
        "h2_headings": headings,
        "suggestions": suggestions,
    }


def _print_report(result: dict) -> None:
    """Print human-readable comparison report."""
    if "error" in result:
        print(f"Error: {result['error']}")
        return

    bm = result["benchmark"]
    classification_labels = {
        "too_short": "TOO SHORT",
        "too_long": "TOO LONG",
        "on_target": "ON TARGET",
        "acceptable": "ACCEPTABLE",
    }
    label = classification_labels.get(result["classification"], result["classification"].upper())

    print(f"\nContent Length Comparator — {Path(result['filepath']).name}")
    print("=" * 50)
    print(f"Content type   : {result['content_type']}")
    print(f"Word count     : {result['word_count']:,}")
    print(f"Target range   : {bm['target_range']} words ({bm['source']})")
    print(f"Min / Max      : {bm['minimum']:,} / {bm['maximum']:,}")
    if bm.get("serp_avg"):
        print(f"SERP top-10 avg: {bm['serp_avg']:,} words")
    print(f"Classification : {label}")
    print()

    if result["suggestions"]:
        print("Suggestions:")
        for s in result["suggestions"]:
            print(f"  {s}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Benchmark article word count against content standards and SERP data."
    )
    parser.add_argument("filepath", help="Path to the markdown file")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    result = compare(args.filepath)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        _print_report(result)


if __name__ == "__main__":
    main()
