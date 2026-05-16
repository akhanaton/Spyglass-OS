"""
Google Analytics 4 Module

Reads pageview data from GA4 for ExamPilot's marketing routes.
Reads ONLY pageview metrics — no custom events, no conversion tracking.

Tracked marketing routes:
  /
  /pricing
  /waitlist
  /blog/*
  /cambridge/*
  /cambridge-a-level-maths/*

Authentication:
  GA4_PROPERTY_ID   : GA4 property ID (format: "properties/XXXXXXXXX")
  GA4_CREDENTIALS_PATH : path to service account JSON file

Graceful degradation:
  - No credentials: prints setup instructions
  - Quota exceeded: uses cached results (24-hour TTL)
  - Untracked route: returns None
"""

import os
import sys
import json
import argparse
from datetime import datetime, date, timedelta
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
CACHE_FILE = CACHE_DIR / "ga4_cache.json"
CACHE_TTL_HOURS = 24

MARKETING_ROUTE_PREFIXES = [
    "/",
    "/pricing",
    "/waitlist",
    "/blog/",
    "/cambridge/",
    "/cambridge-a-level-maths/",
]

GA4_SETUP_INSTRUCTIONS = """
GA4 is not configured. To connect:

1. Create a Google Analytics service account:
   https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries

2. Grant the service account "Viewer" role in GA4 > Admin > Account Access Management

3. Add to your .env file:
   GA4_PROPERTY_ID=properties/XXXXXXXXX
   GA4_CREDENTIALS_PATH=/path/to/service-account.json

4. Install the GA4 client:
   pip install google-analytics-data

5. Re-run this module.
"""


# ---------------------------------------------------------------------------
# Route validation
# ---------------------------------------------------------------------------

def _is_marketing_route(path: str) -> bool:
    """Return True if path is a tracked ExamPilot marketing route."""
    for prefix in MARKETING_ROUTE_PREFIXES:
        if prefix == "/" and path == "/":
            return True
        elif prefix != "/" and path.startswith(prefix):
            return True
    return False


# ---------------------------------------------------------------------------
# Cache management
# ---------------------------------------------------------------------------

def _load_cache() -> Optional[dict]:
    """Load cached GA4 results if within TTL. Returns None if expired or missing."""
    if not CACHE_FILE.exists():
        return None
    try:
        data = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        cached_at = datetime.fromisoformat(data.get("cached_at", "2000-01-01"))
        if datetime.utcnow() - cached_at > timedelta(hours=CACHE_TTL_HOURS):
            return None
        return data.get("result")
    except Exception:
        return None


def _save_cache(result: dict) -> None:
    """Save GA4 result to cache file."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_data = {
        "cached_at": datetime.utcnow().isoformat(),
        "result": result,
    }
    CACHE_FILE.write_text(json.dumps(cache_data, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# GA4 API client
# ---------------------------------------------------------------------------

def _get_ga4_client():
    """
    Return a GA4 BetaAnalyticsDataClient.
    Returns None if credentials not configured.
    """
    creds_path = os.getenv("GA4_CREDENTIALS_PATH", "")
    if not creds_path or not Path(creds_path).exists():
        return None

    try:
        from google.analytics.data_v1beta import BetaAnalyticsDataClient
        from google.oauth2 import service_account

        credentials = service_account.Credentials.from_service_account_file(
            creds_path,
            scopes=["https://www.googleapis.com/auth/analytics.readonly"],
        )
        client = BetaAnalyticsDataClient(credentials=credentials)
        return client
    except ImportError:
        print("google-analytics-data package not installed.")
        print("Install with: pip install google-analytics-data")
        return None
    except Exception as e:
        print(f"GA4 client error: {e}")
        return None


def _run_ga4_report(client, property_id: str, days: int, page_filter: Optional[str] = None) -> Optional[dict]:
    """
    Run pageview report against GA4. Returns raw API response or None on error.
    """
    from google.analytics.data_v1beta.types import (
        RunReportRequest,
        DateRange,
        Dimension,
        Metric,
        FilterExpression,
        Filter,
        FilterExpressionList,
    )

    end_date = date.today().isoformat()
    start_date = (date.today() - timedelta(days=days)).isoformat()

    dimensions = [
        Dimension(name="pagePath"),
        Dimension(name="sessionSourceMedium"),
        Dimension(name="country"),
    ]
    metrics = [
        Metric(name="sessions"),
        Metric(name="screenPageViews"),
        Metric(name="averageSessionDuration"),
    ]

    try:
        request = RunReportRequest(
            property=property_id,
            date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
            dimensions=dimensions,
            metrics=metrics,
            limit=200,
        )
        response = client.run_report(request)
        return response
    except Exception as e:
        error_str = str(e)
        if "quota" in error_str.lower() or "429" in error_str:
            print("GA4 API quota exceeded — using cached data if available.")
            return "QUOTA_EXCEEDED"
        print(f"GA4 API error: {e}")
        return None


# ---------------------------------------------------------------------------
# Response parsing
# ---------------------------------------------------------------------------

def _parse_ga4_response(response, days: int) -> dict:
    """
    Parse GA4 API response into the ExamPilot output format.
    Only includes marketing routes.
    """
    page_data: dict[str, dict] = {}
    total_sessions = 0

    for row in response.rows:
        path = row.dimension_values[0].value
        source_medium = row.dimension_values[1].value
        country = row.dimension_values[2].value

        sessions = int(row.metric_values[0].value)
        pageviews = int(row.metric_values[1].value)
        avg_duration = float(row.metric_values[2].value)

        if not _is_marketing_route(path):
            continue

        if path not in page_data:
            page_data[path] = {
                "path": path,
                "sessions": 0,
                "unique_pageviews": 0,
                "avg_session_duration_seconds": 0,
                "source_breakdown": {"organic": 0, "direct": 0, "referral": 0, "other": 0},
                "top_countries": {},
                "_duration_sum": 0,
                "_duration_count": 0,
            }

        pd = page_data[path]
        pd["sessions"] += sessions
        pd["unique_pageviews"] += pageviews
        pd["_duration_sum"] += avg_duration * sessions
        pd["_duration_count"] += sessions
        total_sessions += sessions

        # Source/medium classification
        sm_lower = source_medium.lower()
        if "organic" in sm_lower:
            pd["source_breakdown"]["organic"] += sessions
        elif sm_lower in ("(none) / (none)", "(direct) / (none)", "(direct) / (not set)"):
            pd["source_breakdown"]["direct"] += sessions
        elif "referral" in sm_lower:
            pd["source_breakdown"]["referral"] += sessions
        else:
            pd["source_breakdown"]["other"] += sessions

        # Country aggregation
        if country not in pd["top_countries"]:
            pd["top_countries"][country] = 0
        pd["top_countries"][country] += sessions

    # Post-process
    pages_out = []
    for path, pd in page_data.items():
        session_total = max(pd["sessions"], 1)
        avg_dur = round(pd["_duration_sum"] / session_total)

        source_total = sum(pd["source_breakdown"].values())
        source_norm = {
            k: round(v / max(source_total, 1), 3)
            for k, v in pd["source_breakdown"].items()
        }

        top_countries_sorted = sorted(
            pd["top_countries"].items(), key=lambda x: x[1], reverse=True
        )[:5]
        top_countries_out = [{"country": c, "sessions": s} for c, s in top_countries_sorted]

        pages_out.append({
            "path": path,
            "sessions": pd["sessions"],
            "unique_pageviews": pd["unique_pageviews"],
            "avg_session_duration_seconds": avg_dur,
            "source_breakdown": source_norm,
            "top_countries": top_countries_out,
        })

    pages_out.sort(key=lambda x: x["sessions"], reverse=True)
    top_page = pages_out[0]["path"] if pages_out else None
    top_country = (
        pages_out[0]["top_countries"][0]["country"]
        if pages_out and pages_out[0]["top_countries"]
        else None
    )

    end_dt = date.today()
    start_dt = end_dt - timedelta(days=days)

    return {
        "date_range": {
            "start": start_dt.isoformat(),
            "end": end_dt.isoformat(),
        },
        "pages": pages_out,
        "summary": {
            "total_marketing_sessions": total_sessions,
            "top_page": top_page,
            "top_country": top_country,
        },
    }


# ---------------------------------------------------------------------------
# Main fetch function
# ---------------------------------------------------------------------------

def fetch(
    days: int = 30,
    page_filter: Optional[str] = None,
    export: bool = False,
) -> Optional[dict]:
    """
    Fetch GA4 pageview data for ExamPilot's marketing routes.

    Returns the result dict, or None if page_filter is for an untracked route.
    Falls back to cache on quota errors.
    """
    property_id = os.getenv("GA4_PROPERTY_ID", "")

    # Validate page_filter against marketing routes
    if page_filter and not _is_marketing_route(page_filter):
        print(f"Route '{page_filter}' is not a tracked marketing route. Returning None.")
        return None

    # Check credentials
    client = _get_ga4_client()
    if not client:
        if not property_id:
            print(GA4_SETUP_INSTRUCTIONS)
            return None
        print("GA4 credentials not found. " + GA4_SETUP_INSTRUCTIONS)
        return None

    if not property_id:
        print("GA4_PROPERTY_ID not set in .env. Format: properties/XXXXXXXXX")
        return None

    # Try live data
    response = _run_ga4_report(client, property_id, days, page_filter)

    if response == "QUOTA_EXCEEDED":
        cached = _load_cache()
        if cached:
            print("Using cached GA4 data.")
            return cached
        print("No cached data available. Try again later.")
        return None

    if response is None:
        return None

    result = _parse_ga4_response(response, days)

    # Filter to specific page if requested
    if page_filter:
        result["pages"] = [p for p in result["pages"] if p["path"] == page_filter]

    # Cache the full result
    _save_cache(result)

    # Export if requested
    if export:
        export_path = CACHE_DIR / f"ga4_results_{date.today().isoformat()}.json"
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        export_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
        print(f"Results exported to: {export_path.resolve()}")

    return result


# ---------------------------------------------------------------------------
# Print helpers
# ---------------------------------------------------------------------------

def _print_report(result: dict, page_filter: Optional[str] = None) -> None:
    """Print human-readable GA4 report."""
    if not result:
        return

    dr = result["date_range"]
    summary = result["summary"]

    print(f"\nGA4 Pageview Report — {dr['start']} to {dr['end']}")
    print("=" * 55)
    print(f"Total marketing sessions : {summary['total_marketing_sessions']:,}")
    print(f"Top page                 : {summary['top_page']}")
    print(f"Top country              : {summary['top_country']}")
    print()

    pages = result.get("pages", [])
    if page_filter:
        pages = [p for p in pages if p["path"] == page_filter]

    if not pages:
        print("No data for the specified filters.")
        return

    for page in pages[:10]:  # Show top 10 pages
        print(f"  {page['path']}")
        print(f"    Sessions      : {page['sessions']:,} | Unique views: {page['unique_pageviews']:,}")
        print(f"    Avg duration  : {page['avg_session_duration_seconds']}s")

        sb = page["source_breakdown"]
        print(f"    Sources       : organic {sb.get('organic', 0):.0%} | direct {sb.get('direct', 0):.0%} | referral {sb.get('referral', 0):.0%}")

        if page["top_countries"]:
            top_c = ", ".join(f"{c['country']} ({c['sessions']})" for c in page["top_countries"][:3])
            print(f"    Top countries : {top_c}")
        print()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fetch GA4 pageview data for ExamPilot's marketing routes."
    )
    parser.add_argument(
        "--days", type=int, default=30,
        help="Number of days to look back (default: 30)",
    )
    parser.add_argument(
        "--page", default=None,
        help="Filter to a specific page path (e.g. /blog/integration-by-parts-9709)",
    )
    parser.add_argument(
        "--export", action="store_true",
        help="Save results to data_sources/cache/ga4_results_YYYY-MM-DD.json",
    )
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    result = fetch(days=args.days, page_filter=args.page, export=args.export)

    if result:
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            _print_report(result, page_filter=args.page)
    else:
        print("No data returned.")


if __name__ == "__main__":
    main()
