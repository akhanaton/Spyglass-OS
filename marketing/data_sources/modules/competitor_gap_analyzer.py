"""
Competitor Gap Analyzer

Identifies keywords that ExamPilot's competitors rank for (positions 1-10)
but ExamPilot does not. Requires DataForSEO credentials for live data.

Default competitors:
  - SaveMyExams (savemyexams.com)
  - PapaCambridge (papacambridge.com)
  - Physics & Maths Tutor (physicsandmathstutor.com)

Falls back to curated manual guidance when DataForSEO is not connected.
"""

import os
import sys
import json
import re
import argparse
import base64
import urllib.request
import urllib.error
from typing import Optional

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

DEFAULT_COMPETITORS = [
    "savemyexams.com",
    "papacambridge.com",
    "physicsandmathstutor.com",
]

EXAMPILOT_DOMAIN = "exampilot.io"

# Keywords to filter OUT (irrelevant to ExamPilot's A-Level Maths focus)
IRRELEVANT_PATTERNS = [
    r"\bphysics\b(?!.*(maths|math))",  # physics without maths context
    r"\bchemistry\b",
    r"\bbiology\b",
    r"\bhistory\b",
    r"\bgeography\b",
    r"\benglish\b(?!.*(language|literature).*(maths|math))",
    r"\beconomics\b",
    r"\bcomputer science\b",
    r"\bgcse\b",                        # GCSE not A-Level
    r"\bks[34]\b",                      # Key Stage 3/4
    r"^\w+\.(com|co\.uk|io|net)$",      # brand/domain queries
]

RELEVANT_PATTERNS = [
    r"\ba.?level\b",
    r"\bcambridge\b",
    r"\bedexcel\b",
    r"\b9709\b",
    r"\bwma\d+\b",
    r"\bpure maths\b",
    r"\bstatistics\b",
    r"\bmechanics\b",
    r"\bcalculus\b",
    r"\bintegrat\b",
    r"\bdiffer\b",
    r"\btrigonom\b",
    r"\balgebra\b",
    r"\bvectors\b",
    r"\bprobabilit\b",
    r"\bnormal distribution\b",
    r"\bbinomial\b",
    r"\bpast paper\b",
    r"\bmark scheme\b",
    r"\bworked solution\b",
    r"\brevision\b",
    r"\bmaths\b",
    r"\bmath\b",
]

# Manual guidance when DataForSEO is not connected
MANUAL_GAP_GUIDANCE: dict[str, dict] = {
    "savemyexams.com": {
        "name": "SaveMyExams",
        "known_keyword_clusters": [
            {
                "cluster": "Topic revision notes",
                "examples": ["integration revision notes a level", "differentiation a level notes"],
                "estimated_volume": "medium",
                "difficulty_tier": "hard",
                "content_type": "long-form guide",
                "impact_estimate": 7,
            },
            {
                "cluster": "Past paper solutions by year",
                "examples": ["cambridge 9709 2023 paper 1 solutions", "9709 may june 2022 worked solutions"],
                "estimated_volume": "high",
                "difficulty_tier": "medium",
                "content_type": "worked example guide",
                "impact_estimate": 9,
            },
            {
                "cluster": "Topic-level practice questions",
                "examples": ["integration by parts practice questions", "binomial theorem questions a level"],
                "estimated_volume": "medium",
                "difficulty_tier": "medium",
                "content_type": "practice question set",
                "impact_estimate": 7,
            },
        ],
    },
    "papacambridge.com": {
        "name": "PapaCambridge",
        "known_keyword_clusters": [
            {
                "cluster": "Past papers by year and paper number",
                "examples": ["cambridge 9709 paper 1 2022", "9709 11 may june 2023"],
                "estimated_volume": "very high",
                "difficulty_tier": "very hard",
                "content_type": "resource page",
                "impact_estimate": 10,
            },
            {
                "cluster": "Mark schemes by year",
                "examples": ["9709 mark scheme 2022 paper 3", "cambridge a level maths mark scheme"],
                "estimated_volume": "high",
                "difficulty_tier": "hard",
                "content_type": "resource page with explanation",
                "impact_estimate": 9,
            },
        ],
    },
    "physicsandmathstutor.com": {
        "name": "Physics & Maths Tutor",
        "known_keyword_clusters": [
            {
                "cluster": "Worked solutions by topic",
                "examples": ["integration by parts worked solutions a level", "differentiation from first principles worked examples"],
                "estimated_volume": "medium",
                "difficulty_tier": "medium",
                "content_type": "worked example guide",
                "impact_estimate": 8,
            },
            {
                "cluster": "Revision notes by topic",
                "examples": ["pure maths 1 revision notes cambridge", "statistics 1 revision notes a level"],
                "estimated_volume": "medium-high",
                "difficulty_tier": "hard",
                "content_type": "long-form guide",
                "impact_estimate": 7,
            },
            {
                "cluster": "Exam technique and tips",
                "examples": ["a level maths exam tips", "how to get an A in a level maths"],
                "estimated_volume": "medium",
                "difficulty_tier": "low",
                "content_type": "blog article",
                "impact_estimate": 6,
            },
        ],
    },
}


# ---------------------------------------------------------------------------
# DataForSEO helpers
# ---------------------------------------------------------------------------

def _get_dataforseo_creds() -> tuple[str, str]:
    """Return (login, password) from env vars."""
    return os.getenv("DATAFORSEO_LOGIN", ""), os.getenv("DATAFORSEO_PASSWORD", "")


def _dataforseo_request(endpoint: str, payload: list) -> Optional[dict]:
    """Make a DataForSEO API request. Returns parsed JSON or None on error."""
    login, password = _get_dataforseo_creds()
    if not login or not password:
        return None

    try:
        credentials = base64.b64encode(f"{login}:{password}".encode()).decode()
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            f"https://api.dataforseo.com/v3/{endpoint}",
            data=data,
            headers={
                "Authorization": f"Basic {credentials}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"DataForSEO API error: {e}", file=sys.stderr)
        return None


def _fetch_competitor_keywords(domain: str, limit: int = 50) -> list[dict]:
    """
    Fetch top keywords a competitor ranks for (positions 1-10) via DataForSEO.
    Returns list of {keyword, position, search_volume} dicts.
    """
    payload = [{
        "target": domain,
        "location_code": 2826,  # UK
        "language_code": "en",
        "filters": [
            ["ranked_serp_element.serp_item.rank_group", "<=", 10]
        ],
        "order_by": ["keyword_data.keyword_info.search_volume,desc"],
        "limit": limit,
    }]

    response = _dataforseo_request("dataforseo_labs/google/ranked_keywords/live", payload)
    if not response:
        return []

    try:
        items = response["tasks"][0]["result"][0]["items"]
        keywords = []
        for item in items:
            kd = item.get("keyword_data", {})
            kw = kd.get("keyword", "")
            volume = kd.get("keyword_info", {}).get("search_volume", 0)
            position = item.get("ranked_serp_element", {}).get("serp_item", {}).get("rank_group", 99)
            keywords.append({"keyword": kw, "position": position, "search_volume": volume or 0})
        return keywords
    except (KeyError, IndexError, TypeError):
        return []


def _fetch_exampilot_keywords() -> set[str]:
    """Fetch ExamPilot's currently ranking keywords via DataForSEO."""
    keywords = _fetch_competitor_keywords(EXAMPILOT_DOMAIN, limit=200)
    return {kw["keyword"].lower() for kw in keywords}


# ---------------------------------------------------------------------------
# Keyword relevance filtering
# ---------------------------------------------------------------------------

def _is_relevant(keyword: str) -> bool:
    """Return True if keyword is relevant to ExamPilot's A-Level Maths focus."""
    kw_lower = keyword.lower()
    # Must match at least one relevant pattern
    if not any(re.search(p, kw_lower) for p in RELEVANT_PATTERNS):
        return False
    # Must not match irrelevant patterns
    if any(re.search(p, kw_lower) for p in IRRELEVANT_PATTERNS):
        return False
    return True


# ---------------------------------------------------------------------------
# Difficulty and impact estimation
# ---------------------------------------------------------------------------

def _estimate_difficulty(keyword: str, search_volume: int) -> str:
    """Rough difficulty tier estimate based on keyword characteristics and volume."""
    if search_volume >= 10000:
        return "very hard"
    elif search_volume >= 2000:
        return "hard"
    elif search_volume >= 500:
        return "medium"
    return "low"


def _estimate_impact(keyword: str, search_volume: int, position: int) -> int:
    """Estimate impact score 1-10 for a gap keyword."""
    base = 5
    # Volume bonus
    if search_volume >= 10000:
        base = 9
    elif search_volume >= 2000:
        base = 7
    elif search_volume >= 500:
        base = 6
    # Position bonus: if competitor is in top 3, opportunity is high-value
    if position <= 3:
        base = min(10, base + 1)
    # Exam prep signals boost
    if any(kw in keyword.lower() for kw in ["past paper", "mark scheme", "worked solution", "revision"]):
        base = min(10, base + 1)
    return base


def _suggest_content_type(keyword: str) -> str:
    """Suggest content type for a gap keyword."""
    kw = keyword.lower()
    if "past paper" in kw or "mark scheme" in kw:
        return "worked example guide"
    elif "revision" in kw or "notes" in kw:
        return "long-form guide"
    elif "how to" in kw or "solve" in kw or "worked" in kw:
        return "step-by-step tutorial"
    elif "vs" in kw or "comparison" in kw or "best" in kw:
        return "comparison article"
    elif "tips" in kw or "technique" in kw:
        return "blog article"
    return "blog article"


# ---------------------------------------------------------------------------
# Main analyzer
# ---------------------------------------------------------------------------

def analyze(
    competitors: Optional[list[str]] = None,
    limit: int = 20,
) -> dict:
    """
    Analyze keyword gaps between competitors and ExamPilot.
    Returns a dict with gap_keywords list and metadata.
    """
    if competitors is None:
        competitors = DEFAULT_COMPETITORS

    login, password = _get_dataforseo_creds()
    connected = bool(login and password)

    if not connected:
        return _manual_guidance(competitors)

    # Fetch ExamPilot's current keywords
    exampilot_kws = _fetch_exampilot_keywords()
    print(f"ExamPilot ranking keywords fetched: {len(exampilot_kws)}")

    all_gaps: list[dict] = []

    for domain in competitors:
        print(f"Fetching keywords for {domain}...")
        competitor_kws = _fetch_competitor_keywords(domain, limit=50)

        for item in competitor_kws:
            kw = item["keyword"].lower()
            if kw in exampilot_kws:
                continue
            if not _is_relevant(kw):
                continue

            volume = item["search_volume"]
            position = item["position"]
            impact = _estimate_impact(kw, volume, position)
            difficulty = _estimate_difficulty(kw, volume)
            content_type = _suggest_content_type(kw)
            opportunity_score = round(impact / max(1, {"very hard": 4, "hard": 3, "medium": 2, "low": 1}.get(difficulty, 2)), 2)

            all_gaps.append({
                "keyword": kw,
                "competitor": domain,
                "competitor_position": position,
                "search_volume": volume,
                "difficulty_tier": difficulty,
                "suggested_content_type": content_type,
                "impact_score": impact,
                "opportunity_score": opportunity_score,
                "action": f"/write-article {kw}",
            })

    # Sort by opportunity score
    all_gaps.sort(key=lambda x: x["opportunity_score"], reverse=True)
    all_gaps = all_gaps[:limit]

    return {
        "source": "dataforseo",
        "competitors_analyzed": competitors,
        "exampilot_keywords_tracked": len(exampilot_kws),
        "gaps_found": len(all_gaps),
        "gap_keywords": all_gaps,
    }


def _manual_guidance(competitors: list[str]) -> dict:
    """Return manual gap guidance when DataForSEO is not connected."""
    print("DataForSEO not connected — returning manual keyword gap guidance.")
    print("Set DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD in .env to enable live gap analysis.\n")

    guidance = []
    for domain in competitors:
        if domain in MANUAL_GAP_GUIDANCE:
            guidance.append(MANUAL_GAP_GUIDANCE[domain])

    return {
        "source": "manual",
        "message": "Live gap analysis requires DataForSEO credentials. See setup instructions in connections.md.",
        "competitors_analyzed": competitors,
        "manual_guidance": guidance,
    }


def _print_report(result: dict) -> None:
    """Print human-readable gap analysis."""
    source = result.get("source", "unknown")

    if source == "manual":
        print("\nCompetitor Gap Analysis — Manual Guidance Mode")
        print("=" * 55)
        print(f"DataForSEO not connected. Showing known gap clusters.\n")
        for comp in result.get("manual_guidance", []):
            print(f"\n{comp['name']} ({comp.get('domain', '')})")
            print("-" * 40)
            for cluster in comp["known_keyword_clusters"]:
                print(f"  Cluster  : {cluster['cluster']}")
                print(f"  Volume   : {cluster['estimated_volume']} | Difficulty: {cluster['difficulty_tier']}")
                print(f"  Format   : {cluster['content_type']} | Impact: {cluster['impact_estimate']}/10")
                print(f"  Examples : {', '.join(cluster['examples'][:2])}")
                print()
        return

    print(f"\nCompetitor Gap Analysis — DataForSEO Live Data")
    print("=" * 55)
    print(f"ExamPilot keywords tracked : {result.get('exampilot_keywords_tracked', 0)}")
    print(f"Gaps found                 : {result.get('gaps_found', 0)}")
    print()

    gaps = result.get("gap_keywords", [])
    if not gaps:
        print("No relevant keyword gaps found.")
        return

    for gap in gaps:
        print(f"  [{gap['opportunity_score']:.2f}] {gap['keyword']}")
        print(f"         Competitor: {gap['competitor']} (pos #{gap['competitor_position']}) | Vol: {gap['search_volume']} | {gap['difficulty_tier']}")
        print(f"         Format: {gap['suggested_content_type']} | Action: {gap['action']}")
        print()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Identify keyword gaps between ExamPilot and competitor domains."
    )
    parser.add_argument(
        "--competitors",
        default=",".join(DEFAULT_COMPETITORS),
        help="Comma-separated list of competitor domains (default: SaveMyExams, PapaCambridge, PMT)",
    )
    parser.add_argument(
        "--limit", type=int, default=20,
        help="Maximum number of gap keywords to return (default: 20)",
    )
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    competitors = [c.strip() for c in args.competitors.split(",") if c.strip()]
    result = analyze(competitors=competitors, limit=args.limit)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        _print_report(result)


if __name__ == "__main__":
    main()
