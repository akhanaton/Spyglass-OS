"""
Opportunity Scorer

Scores and ranks content opportunities by impact, effort, confidence, and exam urgency.
Used as a library by /priorities command and other pipeline tools.

Opportunity object shape:
  {
    "title": str,
    "type": "new_article" | "rewrite" | "optimize" | "cluster",
    "keyword": str,
    "impact": int,          # 0-10
    "effort": int,          # 1-5
    "confidence": float,    # 0-1
    "source": str,          # "dataforseo" | "manual" | "heuristic"
    "action": str,
    "exam_urgency": int,    # 0-5
  }

Priority formula: (impact * confidence * (1 + exam_urgency * 0.2)) / effort
Tiers: HIGH >= 6.0, MEDIUM 3.0-5.9, LOW < 3.0
"""

from typing import Optional

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


# ---------------------------------------------------------------------------
# Scoring constants
# ---------------------------------------------------------------------------

HIGH_THRESHOLD = 6.0
MEDIUM_THRESHOLD = 3.0

TIER_HIGH = "HIGH"
TIER_MEDIUM = "MEDIUM"
TIER_LOW = "LOW"

VALID_TYPES = {"new_article", "rewrite", "optimize", "cluster"}
VALID_SOURCES = {"dataforseo", "manual", "heuristic"}


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_opportunity(opp: dict) -> list[str]:
    """
    Validate an opportunity object. Returns list of error messages (empty = valid).
    """
    errors = []

    required = ["title", "type", "keyword", "impact", "effort", "confidence", "source", "action", "exam_urgency"]
    for field in required:
        if field not in opp:
            errors.append(f"Missing required field: '{field}'")

    if "impact" in opp and not (0 <= opp["impact"] <= 10):
        errors.append(f"'impact' must be 0-10, got {opp['impact']}")

    if "effort" in opp and not (1 <= opp["effort"] <= 5):
        errors.append(f"'effort' must be 1-5, got {opp['effort']}")

    if "confidence" in opp and not (0.0 <= opp["confidence"] <= 1.0):
        errors.append(f"'confidence' must be 0.0-1.0, got {opp['confidence']}")

    if "exam_urgency" in opp and not (0 <= opp["exam_urgency"] <= 5):
        errors.append(f"'exam_urgency' must be 0-5, got {opp['exam_urgency']}")

    if "type" in opp and opp["type"] not in VALID_TYPES:
        errors.append(f"'type' must be one of {VALID_TYPES}, got '{opp['type']}'")

    if "source" in opp and opp["source"] not in VALID_SOURCES:
        errors.append(f"'source' must be one of {VALID_SOURCES}, got '{opp['source']}'")

    return errors


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def score_opportunity(opp: dict) -> float:
    """
    Calculate priority score for a single opportunity.
    Formula: (impact * confidence * (1 + exam_urgency * 0.2)) / effort

    Raises ValueError if required fields are missing or invalid.
    """
    errors = validate_opportunity(opp)
    if errors:
        raise ValueError(f"Invalid opportunity: {'; '.join(errors)}")

    impact = float(opp["impact"])
    confidence = float(opp["confidence"])
    effort = float(opp["effort"])
    exam_urgency = float(opp["exam_urgency"])

    score = (impact * confidence * (1 + exam_urgency * 0.2)) / effort
    return round(score, 3)


def get_tier(score: float) -> str:
    """Return HIGH / MEDIUM / LOW tier label for a priority score."""
    if score >= HIGH_THRESHOLD:
        return TIER_HIGH
    elif score >= MEDIUM_THRESHOLD:
        return TIER_MEDIUM
    return TIER_LOW


def rank_opportunities(opportunities: list[dict]) -> list[dict]:
    """
    Score and sort a list of opportunity objects by priority score (descending).

    Each returned dict is the original opportunity with two added fields:
      - priority_score: float
      - tier: "HIGH" | "MEDIUM" | "LOW"

    Invalid opportunities are skipped and a warning is printed.
    """
    scored = []
    for opp in opportunities:
        try:
            ps = score_opportunity(opp)
            enriched = dict(opp)
            enriched["priority_score"] = ps
            enriched["tier"] = get_tier(ps)
            scored.append(enriched)
        except ValueError as e:
            print(f"Warning: Skipping opportunity '{opp.get('title', '?')}': {e}")

    scored.sort(key=lambda x: x["priority_score"], reverse=True)
    return scored


def summarize(ranked: list[dict]) -> dict:
    """Return a tier summary dict from a ranked opportunity list."""
    high = [o for o in ranked if o["tier"] == TIER_HIGH]
    medium = [o for o in ranked if o["tier"] == TIER_MEDIUM]
    low = [o for o in ranked if o["tier"] == TIER_LOW]

    return {
        "total": len(ranked),
        "high": len(high),
        "medium": len(medium),
        "low": len(low),
        "top_opportunity": ranked[0] if ranked else None,
    }


def print_ranked(ranked: list[dict]) -> None:
    """Print a human-readable ranked opportunity list."""
    if not ranked:
        print("No opportunities to display.")
        return

    summary = summarize(ranked)
    print(f"\nOpportunity Rankings ({summary['total']} total)")
    print(f"HIGH: {summary['high']}  MEDIUM: {summary['medium']}  LOW: {summary['low']}")
    print("=" * 60)

    current_tier = None
    for opp in ranked:
        tier = opp["tier"]
        if tier != current_tier:
            current_tier = tier
            print(f"\n--- {tier} PRIORITY ---")

        print(f"\n  {opp['title']}")
        print(f"    Keyword   : {opp['keyword']}")
        print(f"    Type      : {opp['type']}")
        print(f"    Score     : {opp['priority_score']} | Impact {opp['impact']}/10 | Effort {opp['effort']}/5 | Urgency {opp['exam_urgency']}/5")
        print(f"    Confidence: {opp['confidence']} ({opp['source']})")
        print(f"    Action    : {opp['action']}")


# ---------------------------------------------------------------------------
# Impact and effort helper guides (for use by callers building opportunities)
# ---------------------------------------------------------------------------

IMPACT_GUIDE = """
Impact scoring (0-10):
  10  : Featured snippet opportunity + high search volume + BOFU keyword
  8-9 : High volume + moderate competition + MOFU
  5-7 : Medium volume, good fit, TOFU
  1-4 : Low volume or long-tail, niche value only
"""

EFFORT_GUIDE = """
Effort scoring (1-5):
  1 : /optimize fix on existing article (1-2 changes)
  2 : Light rewrite or new 1500-word article
  3 : Standard 2000-word article + full research
  4 : Pillar article or complete rewrite
  5 : Cluster build (pillar + 3+ spokes)
"""

URGENCY_GUIDE = """
Exam urgency (0-5):
  5 : Content needed within 2 weeks of exam
  3 : Content needed within 4-6 weeks
  1 : Content needed >6 weeks out
  0 : Not exam-calendar dependent
"""


# ---------------------------------------------------------------------------
# Example usage (not a CLI — library only)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Demo
    sample_opportunities = [
        {
            "title": "Integration by parts — Cambridge 9709 worked guide",
            "type": "new_article",
            "keyword": "integration by parts cambridge 9709",
            "impact": 8,
            "effort": 3,
            "confidence": 0.8,
            "source": "manual",
            "action": "/write-article integration by parts cambridge 9709",
            "exam_urgency": 3,
        },
        {
            "title": "Optimize: Normal distribution revision notes (title tag fix)",
            "type": "optimize",
            "keyword": "normal distribution a level maths",
            "impact": 5,
            "effort": 1,
            "confidence": 0.9,
            "source": "heuristic",
            "action": "/optimize marketing/pipelines/published/normal-distribution.md",
            "exam_urgency": 2,
        },
        {
            "title": "ExamPilot vs SaveMyExams comparison",
            "type": "new_article",
            "keyword": "exampilot vs savemyexams",
            "impact": 9,
            "effort": 2,
            "confidence": 0.5,
            "source": "heuristic",
            "action": "/write-article exampilot vs savemyexams",
            "exam_urgency": 0,
        },
    ]

    ranked = rank_opportunities(sample_opportunities)
    print_ranked(ranked)
    print(f"\n{IMPACT_GUIDE}")
    print(f"{EFFORT_GUIDE}")
    print(f"{URGENCY_GUIDE}")
