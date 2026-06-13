#!/usr/bin/env python3
"""SERP analyzer via DataForSEO — AI Overview presence, SERP features, who ranks.

Pulls the live top-N Google SERP for a keyword and returns:
  - AI Overview presence (+ cited references when DataForSEO exposes them)
  - SERP features present (featured snippet, PAA, video, images, etc.)
  - People-Also-Ask questions
  - Top organic results (rank, domain, title, url)

Consumed by the /research-serp skill (pre-writing SERP analysis) and the
/signal-review ritual (weekly AIO-presence monitoring on top ranking queries).

Why AIO presence matters: it decides the KPI. AIO-suppressed informational
queries are managed by citation share; AIO-free queries (navigational,
comparison, niche long-tail) are where CTR/title work still earns clicks.
AIO presence varies by geography and reshuffles every ~2 days — re-check.

Requires: DATAFORSEO_LOGIN + DATAFORSEO_PASSWORD in marketing/data_sources/.env

Usage:
    python3 serp_analyzer.py --keyword "9709 trigonometry"
    python3 serp_analyzer.py --keyword "9709 syllabus" --location pakistan --json
    python3 serp_analyzer.py --keyword "cambridge 9709" --location 2826 --results 10

Caveat: SERP-API AIO detection can undercount AIOs that load on interaction.
Treat "no" as "no AIO observed at fetch", not a guarantee.
"""

import argparse
import base64
import json
import os
import sys
import urllib.request
from pathlib import Path
from typing import Optional

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
except ImportError:
    pass

# Friendly names → DataForSEO location codes. SERP requires a location
# (no worldwide). Default UK: richest SERP-feature coverage + the documented
# /research-serp default. Core CIE markets included for geo cuts.
LOCATIONS = {
    "uk": 2826,
    "us": 2840,
    "pakistan": 2586,
    "india": 2356,
    "uae": 2784,
    "malaysia": 2458,
    "singapore": 2702,
    "egypt": 2818,
    "nigeria": 2566,
    "kenya": 2404,
}


def _dataforseo_request(endpoint: str, payload: list) -> Optional[dict]:
    login = os.getenv("DATAFORSEO_LOGIN", "")
    password = os.getenv("DATAFORSEO_PASSWORD", "")
    if not login or not password:
        print(
            "ERROR: DATAFORSEO_LOGIN / DATAFORSEO_PASSWORD not set in .env. "
            "See connections.md row 12.",
            file=sys.stderr,
        )
        return None
    try:
        creds = base64.b64encode(f"{login}:{password}".encode()).decode()
        req = urllib.request.Request(
            f"https://api.dataforseo.com/v3/{endpoint}",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Authorization": f"Basic {creds}", "Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"DataForSEO API error: {e}", file=sys.stderr)
        return None


def resolve_location(value: str) -> int:
    """Accept a friendly name (uk, pakistan, ...) or a raw numeric code."""
    if value.isdigit():
        return int(value)
    if value in LOCATIONS:
        return LOCATIONS[value]
    print(
        f"ERROR: unknown location '{value}'. Use a code (e.g. 2826) or one of: "
        f"{', '.join(LOCATIONS)}",
        file=sys.stderr,
    )
    sys.exit(1)


def _domain(url: str) -> str:
    if not url:
        return ""
    return url.split("//")[-1].split("/")[0].lstrip("www.")


def analyze_serp(keyword: str, location_code: int, language: str, results: int) -> Optional[dict]:
    payload = [{
        "keyword": keyword,
        "location_code": location_code,
        "language_code": language,
        "depth": max(results, 20),  # fetch enough to see features below the fold
    }]
    resp = _dataforseo_request("serp/google/organic/live/advanced", payload)
    if not resp or not resp.get("tasks"):
        return None
    task = resp["tasks"][0]
    result = (task.get("result") or [{}])[0]
    items = result.get("items") or []

    feature_types: list[str] = []
    organic: list[dict] = []
    paa_questions: list[str] = []
    aio_present = False
    aio_refs: list[str] = []

    for it in items:
        t = it.get("type")
        if t and t != "organic" and t not in feature_types:
            feature_types.append(t)
        if t == "ai_overview":
            aio_present = True
            for ref in (it.get("references") or []):
                dom = ref.get("domain") or _domain(ref.get("url", ""))
                if dom and dom not in aio_refs:
                    aio_refs.append(dom)
        elif t == "people_also_ask":
            for paa in (it.get("items") or []):
                q = paa.get("title")
                if q and q not in paa_questions:
                    paa_questions.append(q)
        elif t == "organic" and len(organic) < results:
            organic.append({
                "rank": it.get("rank_group"),
                "domain": _domain(it.get("url", "")),
                "title": it.get("title"),
                "url": it.get("url"),
            })

    return {
        "keyword": keyword,
        "location_code": location_code,
        "language": language,
        "ai_overview_present": aio_present,
        "ai_overview_references": aio_refs,
        "serp_features": feature_types,
        "paa_questions": paa_questions,
        "top_organic": organic,
        "cost": resp.get("cost", 0),
    }


def main():
    parser = argparse.ArgumentParser(description="SERP analyzer — AIO presence, features, who ranks (DataForSEO)")
    parser.add_argument("--keyword", required=True, help="Keyword to analyze")
    parser.add_argument("--location", default="uk", help=f"Friendly name or code. Names: {', '.join(LOCATIONS)} (default: uk)")
    parser.add_argument("--language", default="en", help="Language code (default: en)")
    parser.add_argument("--results", type=int, default=10, help="Top organic results to return (default 10)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    location_code = resolve_location(args.location)
    data = analyze_serp(args.keyword, location_code, args.language, args.results)
    if data is None:
        print("No SERP data returned (check connection / credits).", file=sys.stderr)
        sys.exit(1)

    if args.json:
        print(json.dumps(data, indent=2))
        return

    print(f"\nSERP analysis — \"{data['keyword']}\"  (location {location_code}, {data['language']})")
    print(f"DataForSEO cost: ${data['cost']}\n")
    print(f"AI Overview: {'YES' if data['ai_overview_present'] else 'no'}")
    if data["ai_overview_references"]:
        print(f"  AIO cites: {', '.join(data['ai_overview_references'][:8])}")
    print(f"SERP features: {', '.join(data['serp_features']) or '(none)'}")
    if data["paa_questions"]:
        print("\nPeople Also Ask:")
        for q in data["paa_questions"][:5]:
            print(f"  - {q}")
    print("\nTop organic:")
    print(f"{'#':>3}  {'domain':<34}{'title'}")
    print("-" * 78)
    for o in data["top_organic"]:
        print(f"{str(o['rank'] or '?'):>3}  {(o['domain'] or '')[:32]:<34}{(o['title'] or '')[:38]}")
    print()


if __name__ == "__main__":
    main()
