"""
Data Aggregator

Unifies GA4, GSC, and DataForSEO into a single performance view with 24-hour caching.
Central data layer used by /priorities, /research-performance, and the performance agent.

GA4 is pageview-ONLY for ExamPilot marketing routes. No custom events or conversion data.

Authentication env vars:
  GA4: GA4_PROPERTY_ID + GA4_CREDENTIALS_PATH
  GSC: GSC_PROPERTY + GSC_CREDENTIALS_PATH
  DataForSEO: DATAFORSEO_LOGIN + DATAFORSEO_PASSWORD
"""

import os
import sys
import json
import argparse
import re
from datetime import datetime, timedelta
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

CACHE_DIR = Path("marketing/data_sources/cache")
CACHE_TTL_HOURS = 24

MARKETING_ROUTES = ["/", "/pricing", "/waitlist", "/blog/", "/cambridge/", "/cambridge-a-level-maths/"]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _cache_path(days: int) -> Path:
    """Return cache file path for today's aggregated data."""
    today = datetime.now().strftime("%Y-%m-%d")
    return CACHE_DIR / f"aggregated_{today}_d{days}.json"


def _cache_is_fresh(path: Path) -> bool:
    """Return True if cache file exists and was written within the last 24 hours."""
    if not path.exists():
        return False
    mtime = datetime.fromtimestamp(path.stat().st_mtime)
    return datetime.now() - mtime < timedelta(hours=CACHE_TTL_HOURS)


def _normalise_url(url: str) -> str:
    """Normalise a URL for consistent merging: lowercase, strip trailing slash, strip domain."""
    url = url.strip().lower()
    # Strip scheme + domain if present
    url = re.sub(r'^https?://[^/]+', '', url)
    url = url.rstrip("/") or "/"
    return url


def _sources_configured() -> dict:
    """Return which data sources have credentials configured."""
    return {
        "ga4": bool(os.getenv("GA4_PROPERTY_ID") and os.getenv("GA4_CREDENTIALS_PATH")),
        "gsc": bool(os.getenv("GSC_PROPERTY") and os.getenv("GSC_CREDENTIALS_PATH")),
        "dataforseo": bool(os.getenv("DATAFORSEO_LOGIN") and os.getenv("DATAFORSEO_PASSWORD")),
    }


# ---------------------------------------------------------------------------
# Data fetchers
# ---------------------------------------------------------------------------

def _fetch_ga4(days: int) -> dict:
    """Fetch sessions + unique pageviews per marketing route from GA4. Returns {} on failure."""
    try:
        from google_analytics import get_pageview_data
        raw = get_pageview_data(days=days)
        result = {}
        for row in raw:
            url = _normalise_url(row.get("page_path", ""))
            result[url] = {
                "sessions": row.get("sessions", 0),
                "unique_pageviews": row.get("unique_pageviews", 0),
                "top_country": row.get("top_country", None),
            }
        return result
    except Exception as e:
        print(f"  GA4 fetch failed: {e}")
        return {}


def _fetch_gsc(days: int) -> dict:
    """Fetch GSC impressions, clicks, CTR, avg position by page. Returns {} on failure."""
    try:
        from gsc_analyzer import get_gsc_service, query_gsc
        service = get_gsc_service()
        rows = query_gsc(service, days=days, top=500, dimension="page")
        result = {}
        for row in rows:
            keys = row.get("keys", [])
            url = _normalise_url(keys[0]) if keys else ""
            if not url:
                continue
            result[url] = {
                "impressions": int(row.get("impressions", 0)),
                "clicks": int(row.get("clicks", 0)),
                "ctr": round(row.get("ctr", 0.0), 4),
                "avg_position": round(row.get("position", 0.0), 1),
            }
        return result
    except Exception as e:
        print(f"  GSC fetch failed: {e}")
        return {}


def _fetch_dataforseo(keywords: list[str]) -> dict:
    """Fetch keyword rankings from DataForSEO for tracked keywords. Returns {} on failure."""
    import base64
    import urllib.request

    login = os.getenv("DATAFORSEO_LOGIN", "")
    password = os.getenv("DATAFORSEO_PASSWORD", "")
    if not login or not password:
        return {}

    try:
        credentials = base64.b64encode(f"{login}:{password}".encode()).decode()
        headers = {
            "Authorization": f"Basic {credentials}",
            "Content-Type": "application/json",
        }
        payload = json.dumps([
            {"keyword": kw, "location_code": 2840, "language_code": "en", "se_type": "organic"}
            for kw in keywords[:50]  # API limit guard
        ]).encode()

        req = urllib.request.Request(
            "https://api.dataforseo.com/v3/serp/google/organic/live/advanced",
            data=payload,
            headers=headers,
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())

        result = {}
        for task in data.get("tasks", []):
            for res in task.get("result", []):
                for item in res.get("items", []):
                    if item.get("type") == "organic":
                        url = _normalise_url(item.get("url", ""))
                        rank = item.get("rank_absolute", None)
                        features = [
                            i.get("type")
                            for i in res.get("items", [])
                            if i.get("type") not in ("organic",) and i.get("rank_absolute", 99) < (rank or 99)
                        ]
                        if url:
                            result.setdefault(url, {
                                "current_rank": rank,
                                "rank_change_7d": 0,
                                "serp_features": list(set(features)),
                            })
        return result
    except Exception as e:
        print(f"  DataForSEO fetch failed: {e}")
        return {}


# ---------------------------------------------------------------------------
# Quadrant classification
# ---------------------------------------------------------------------------

def _classify_pages(pages: list[dict]) -> list[dict]:
    """Classify each page into Stars / Overperformers / Underperformers / Declining."""
    clicks_values = [p["gsc"]["clicks"] for p in pages if p.get("gsc")]
    if not clicks_values:
        for p in pages:
            p["quadrant"] = "unknown"
        return pages

    clicks_values_sorted = sorted(clicks_values)
    median_clicks = clicks_values_sorted[len(clicks_values_sorted) // 2]

    for page in pages:
        gsc = page.get("gsc") or {}
        clicks = gsc.get("clicks", 0)
        position = gsc.get("avg_position", 100)

        if clicks > median_clicks and position < 10:
            page["quadrant"] = "star"
        elif position < 10 and clicks <= median_clicks:
            page["quadrant"] = "overperformer"
        elif clicks > median_clicks and position >= 10:
            page["quadrant"] = "underperformer"
        else:
            page["quadrant"] = "declining"

    return pages


# ---------------------------------------------------------------------------
# Core aggregation
# ---------------------------------------------------------------------------

def aggregate(days: int = 30, force_refresh: bool = False) -> dict:
    """Aggregate available data from GA4, GSC, and DataForSEO into unified view."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = _cache_path(days)

    if not force_refresh and _cache_is_fresh(cache_path):
        print(f"  Using cached data from {cache_path}")
        with open(cache_path) as f:
            return json.load(f)

    configured = _sources_configured()
    sources_connected = [s for s, ok in configured.items() if ok]
    print(f"  Sources configured: {sources_connected or ['none']}")

    # Fetch each source
    ga4_data: dict = {}
    gsc_data: dict = {}
    dfs_data: dict = {}

    if configured["ga4"]:
        print("  Fetching GA4...")
        ga4_data = _fetch_ga4(days)

    if configured["gsc"]:
        print("  Fetching GSC...")
        gsc_data = _fetch_gsc(days)

    if configured["dataforseo"]:
        print("  Fetching DataForSEO...")
        # Use GSC pages as keyword seeds if available
        seed_keywords = list(gsc_data.keys())[:30]
        dfs_data = _fetch_dataforseo(seed_keywords)

    # Merge by normalised URL
    all_urls: set = set(ga4_data) | set(gsc_data) | set(dfs_data)
    pages = []
    now_iso = datetime.now().isoformat(timespec="seconds")

    for url in sorted(all_urls):
        record: dict = {
            "url": url,
            "ga4": ga4_data.get(url),
            "gsc": gsc_data.get(url),
            "dataforseo": dfs_data.get(url),
            "sources_available": [],
            "last_updated": now_iso,
        }
        if record["ga4"]:
            record["sources_available"].append("ga4")
        if record["gsc"]:
            record["sources_available"].append("gsc")
        if record["dataforseo"]:
            record["sources_available"].append("dataforseo")
        pages.append(record)

    pages = _classify_pages(pages)

    quadrant_counts = {}
    for p in pages:
        q = p.get("quadrant", "unknown")
        quadrant_counts[q] = quadrant_counts.get(q, 0) + 1

    result = {
        "pages": pages,
        "summary": {
            "total_pages": len(pages),
            "days": days,
            "quadrants": quadrant_counts,
        },
        "sources_connected": sources_connected,
        "generated_at": now_iso,
    }

    with open(cache_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"  Saved to {cache_path}")

    return result


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _print_summary(result: dict) -> None:
    """Print a human-readable summary of aggregated data."""
    summary = result.get("summary", {})
    print(f"\nData Aggregator — {result.get('generated_at', 'unknown')}")
    print(f"Sources: {', '.join(result.get('sources_connected', [])) or 'none configured'}")
    print(f"Pages: {summary.get('total_pages', 0)} | Period: {summary.get('days', '?')} days")
    quadrants = summary.get("quadrants", {})
    print(f"Quadrants: Stars={quadrants.get('star', 0)}  "
          f"Overperformers={quadrants.get('overperformer', 0)}  "
          f"Underperformers={quadrants.get('underperformer', 0)}  "
          f"Declining={quadrants.get('declining', 0)}")

    pages = result.get("pages", [])
    stars = [p for p in pages if p.get("quadrant") == "star"]
    if stars:
        print("\nTop Stars:")
        for p in stars[:5]:
            gsc = p.get("gsc") or {}
            print(f"  {p['url']} — clicks: {gsc.get('clicks', 0)}, pos: {gsc.get('avg_position', '?')}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Aggregate GA4 + GSC + DataForSEO into unified performance view")
    parser.add_argument("--days", type=int, default=30, help="Lookback window in days (default: 30)")
    parser.add_argument("--force-refresh", action="store_true", help="Bypass cache and re-fetch all sources")
    parser.add_argument("--json", action="store_true", dest="json_out", help="Output raw JSON")
    parser.add_argument("--export", action="store_true", help="Save result to cache even if already cached")
    args = parser.parse_args()

    result = aggregate(days=args.days, force_refresh=args.force_refresh or args.export)

    if args.json_out:
        print(json.dumps(result, indent=2))
    else:
        _print_summary(result)
