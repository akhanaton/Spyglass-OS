"""
Search Intent Analyzer

Classifies a keyword or article into search intent categories.
Helps match content format to user intent for ExamPilot's A-Level Maths content.

Intent categories:
  Standard:     informational, navigational, transactional, commercial_investigation
  A-Level specific: exam_prep, subject_understanding
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
# Intent signal definitions
# ---------------------------------------------------------------------------

INTENT_SIGNALS: dict[str, list[str]] = {
    "informational": [
        r"\bwhat is\b",
        r"\bwhat are\b",
        r"\bhow does\b",
        r"\bexplain\b",
        r"\bdefinition\b",
        r"\bdefine\b",
        r"\bwhy is\b",
        r"\bwhy does\b",
        r"\bmeaning of\b",
        r"\boverview\b",
        r"\bguide to\b",
        r"\bintroduction to\b",
        r"\bwhat\b",
        r"\bwho\b",
        r"\bwhen\b",
    ],
    "navigational": [
        r"\bexampilot\b",
        r"\bexam pilot\b",
        r"\bexampilot\.io\b",
        r"\bsavemyexams\b",
        r"\bpapacambridge\b",
        r"\bphysicsandmathstutor\b",
        r"\blogin\b",
        r"\bsign in\b",
        r"\bwebsite\b",
        r"\bapp\b",
        r"\bportal\b",
        r"\b9709 site\b",
    ],
    "transactional": [
        r"\bbuy\b",
        r"\bpurchase\b",
        r"\bdownload\b",
        r"\bfree trial\b",
        r"\bsign up\b",
        r"\bget started\b",
        r"\bsubscribe\b",
        r"\bprice\b",
        r"\bpricing\b",
        r"\bplan\b",
        r"\bdiscount\b",
        r"\bget access\b",
        r"\bstart for free\b",
        r"\bjoin\b",
    ],
    "commercial_investigation": [
        r"\bbest\b",
        r"\bvs\b",
        r"\bversus\b",
        r"\bcomparison\b",
        r"\bcompare\b",
        r"\breview\b",
        r"\balternative\b",
        r"\btop\b",
        r"\branking\b",
        r"\brecommended\b",
        r"\bworth it\b",
        r"\bpros and cons\b",
        r"\bpros & cons\b",
    ],
    "exam_prep": [
        r"\bpast paper\b",
        r"\bmark scheme\b",
        r"\bworked solution\b",
        r"\bworked example\b",
        r"\brevision\b",
        r"\bpractice question\b",
        r"\bexam tips\b",
        r"\bhow to pass\b",
        r"\bexam technique\b",
        r"\bgrade a\b",
        r"\ba\*\b",
        r"\bexam prep\b",
        r"\bsyllabus\b",
        r"\b9709\b",
        r"\bwma1[12]\b",
        r"\bwst\d+\b",
        r"\bcambridge a.?level\b",
        r"\bedexcel ial\b",
        r"\bexaminer report\b",
    ],
    "subject_understanding": [
        r"\bhow to solve\b",
        r"\bhow to do\b",
        r"\bhow to find\b",
        r"\bhow to calculate\b",
        r"\bhow to differentiate\b",
        r"\bhow to integrate\b",
        r"\bintegration by parts\b",
        r"\bchain rule\b",
        r"\bproduct rule\b",
        r"\bquotient rule\b",
        r"\bbinomial theorem\b",
        r"\btrigonometric identit\b",
        r"\bquadratic formula\b",
        r"\bstationary point\b",
        r"\bnormal distribution\b",
        r"\bhypothesis test\b",
        r"\bprobability\b",
        r"\bvectors\b",
        r"\bcalculus\b",
        r"\bintegration\b",
        r"\bdifferentiation\b",
        r"\btrigonometry\b",
        r"\bgeometry\b",
        r"\balgebra\b",
        r"\bsequence\b",
        r"\bseries\b",
        r"\blogarithm\b",
    ],
}

# Recommended content format per intent
CONTENT_FORMAT_MAP: dict[str, dict] = {
    "informational": {
        "format": "long-form guide",
        "word_count": "1800-2500",
        "features": ["FAQ section", "definition block", "summary table"],
        "command": "/write-article",
    },
    "navigational": {
        "format": "landing page",
        "word_count": "800-1200",
        "features": ["clear CTA", "feature overview", "trust signals"],
        "command": "/pre-write (landing page type)",
    },
    "transactional": {
        "format": "landing page with CTA",
        "word_count": "1200-2000",
        "features": ["benefit-first copy", "pricing table", "social proof", "CTA above fold"],
        "command": "/pre-write (landing page type)",
    },
    "commercial_investigation": {
        "format": "comparison article",
        "word_count": "1500-2500",
        "features": ["comparison table", "pros/cons", "clear recommendation", "verdict section"],
        "command": "/write-article",
    },
    "exam_prep": {
        "format": "worked example guide",
        "word_count": "1500-2500",
        "features": [
            "step-by-step worked examples",
            "past paper reference",
            "mark scheme logic",
            "common mistakes section",
        ],
        "command": "/write-article",
    },
    "subject_understanding": {
        "format": "concept explanation guide",
        "word_count": "2000-3000",
        "features": [
            "concept definition",
            "visual diagram",
            "worked examples with steps",
            "practice questions",
            "FAQ section",
        ],
        "command": "/write-article",
    },
}


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def _score_intent(keyword: str) -> dict[str, float]:
    """Score each intent category 0-10 based on keyword signal strength."""
    kw_lower = keyword.lower()
    scores: dict[str, float] = {k: 0.0 for k in INTENT_SIGNALS}

    for intent, patterns in INTENT_SIGNALS.items():
        hits = 0
        for pattern in patterns:
            if re.search(pattern, kw_lower):
                hits += 1
        # Scale hits to 0-10; each pattern hit adds proportional weight
        max_patterns = len(patterns)
        raw_score = (hits / max_patterns) * 10 if max_patterns else 0
        # Bonus for strong exact signal presence
        if hits >= 2:
            raw_score = min(10.0, raw_score * 1.5)
        scores[intent] = round(raw_score, 2)

    return scores


def _confidence(scores: dict[str, float]) -> float:
    """Estimate confidence 0-1 based on score separation between top and second."""
    sorted_scores = sorted(scores.values(), reverse=True)
    if not sorted_scores or sorted_scores[0] == 0:
        return 0.1
    top = sorted_scores[0]
    second = sorted_scores[1] if len(sorted_scores) > 1 else 0.0
    # High confidence when top score is high and well-separated from second
    separation = (top - second) / max(top, 1)
    raw_confidence = (top / 10) * (0.5 + separation * 0.5)
    return round(min(1.0, raw_confidence), 2)


# ---------------------------------------------------------------------------
# Main analyzer
# ---------------------------------------------------------------------------

def analyze_keyword(keyword: str) -> dict:
    """
    Classify a keyword into search intent categories.
    Returns primary intent, secondary intent, confidence, and recommended format.
    """
    scores = _score_intent(keyword)
    sorted_intents = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    primary_intent, primary_score = sorted_intents[0]
    secondary_intent = None
    secondary_score = 0.0
    if len(sorted_intents) > 1 and sorted_intents[1][1] >= 3.0:
        secondary_intent, secondary_score = sorted_intents[1]

    confidence = _confidence(scores)

    # Default informational if no strong signal
    if primary_score < 1.0:
        primary_intent = "informational"
        primary_score = 1.0
        confidence = 0.3

    content_format = CONTENT_FORMAT_MAP.get(primary_intent, CONTENT_FORMAT_MAP["informational"])

    return {
        "keyword": keyword,
        "primary_intent": primary_intent,
        "primary_score": primary_score,
        "secondary_intent": secondary_intent,
        "secondary_score": secondary_score,
        "confidence": confidence,
        "all_scores": scores,
        "recommended_format": content_format,
    }


def analyze_file(filepath: str) -> dict:
    """Extract keyword from a markdown file's frontmatter and run intent analysis."""
    path = Path(filepath)
    if not path.exists():
        return {"error": f"File not found: {filepath}"}

    text = path.read_text(encoding="utf-8")

    # Parse frontmatter
    keyword = ""
    if text.startswith("---"):
        match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
        if match:
            fm = match.group(1)
            kw_match = re.search(r"^keyword:\s*(.+)$", fm, re.MULTILINE)
            if kw_match:
                keyword = kw_match.group(1).strip().strip('"').strip("'")

    if not keyword:
        return {
            "error": "No 'keyword:' field found in YAML frontmatter.",
            "filepath": filepath,
        }

    result = analyze_keyword(keyword)
    result["filepath"] = filepath
    return result


def _print_report(result: dict) -> None:
    """Print human-readable intent analysis."""
    if "error" in result:
        print(f"Error: {result['error']}")
        return

    kw = result["keyword"]
    fmt = result["recommended_format"]

    print(f"\nSearch Intent Analysis — '{kw}'")
    print("=" * 50)
    print(f"Primary intent   : {result['primary_intent'].replace('_', ' ').title()} (score: {result['primary_score']}/10)")
    if result["secondary_intent"]:
        print(f"Secondary intent : {result['secondary_intent'].replace('_', ' ').title()} (score: {result['secondary_score']}/10)")
    print(f"Confidence       : {result['confidence']}")
    print()
    print(f"Recommended format : {fmt['format']} ({fmt['word_count']} words)")
    print(f"Key features       :")
    for feature in fmt["features"]:
        print(f"  - {feature}")
    print(f"Command to run     : {fmt['command']}")
    print()
    print("All intent scores:")
    for intent, score in sorted(result["all_scores"].items(), key=lambda x: x[1], reverse=True):
        bar = "█" * int(score) + "░" * (10 - int(score))
        print(f"  {intent:<25} [{bar}] {score}/10")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Classify search intent for a keyword or article."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--keyword", "-k", help="Keyword to classify")
    group.add_argument("--file", "-f", help="Path to markdown file (reads keyword from frontmatter)")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    if args.keyword:
        result = analyze_keyword(args.keyword)
    else:
        result = analyze_file(args.file)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        _print_report(result)


if __name__ == "__main__":
    main()
