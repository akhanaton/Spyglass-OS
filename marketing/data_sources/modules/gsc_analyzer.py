#!/usr/bin/env python3
"""Google Search Console analyzer for ExamPilot marketing.

Pulls query and page performance data from GSC.
Requires: GSC_CREDENTIALS_PATH and GSC_PROPERTY env vars.

Usage:
    python3 gsc_analyzer.py --days 28 --top 20
    python3 gsc_analyzer.py --days 7 --top 50 --dimension page
"""

import argparse
import json
import sys
from datetime import datetime, timedelta

try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
except ImportError:
    print("ERROR: google-api-python-client not installed.")
    print("Run: pip install -r marketing/data_sources/requirements.txt")
    sys.exit(1)

sys.path.insert(0, "..")
from config import GSC_PROPERTY, GSC_CREDENTIALS_PATH


def get_gsc_service():
    if not GSC_CREDENTIALS_PATH:
        print("ERROR: GSC_CREDENTIALS_PATH not set. See connections.md row 10.")
        sys.exit(1)

    credentials = service_account.Credentials.from_service_account_file(
        GSC_CREDENTIALS_PATH,
        scopes=["https://www.googleapis.com/auth/webmasters.readonly"],
    )
    return build("searchconsole", "v1", credentials=credentials)


def query_gsc(service, days, top, dimension="query"):
    end_date = datetime.now() - timedelta(days=3)
    start_date = end_date - timedelta(days=days)

    request = {
        "startDate": start_date.strftime("%Y-%m-%d"),
        "endDate": end_date.strftime("%Y-%m-%d"),
        "dimensions": [dimension],
        "rowLimit": top,
        "dataState": "final",
    }

    response = (
        service.searchanalytics()
        .query(siteUrl=GSC_PROPERTY, body=request)
        .execute()
    )
    return response.get("rows", [])


def format_results(rows, dimension):
    if not rows:
        print("No data returned. Check GSC property and date range.")
        return

    header = f"{'#':<4} {dimension.capitalize():<60} {'Clicks':>8} {'Impressions':>12} {'CTR':>8} {'Position':>10}"
    print(header)
    print("-" * len(header))

    for i, row in enumerate(rows, 1):
        key = row["keys"][0][:58]
        clicks = int(row.get("clicks", 0))
        impressions = int(row.get("impressions", 0))
        ctr = row.get("ctr", 0) * 100
        position = row.get("position", 0)

        print(f"{i:<4} {key:<60} {clicks:>8} {impressions:>12} {ctr:>7.1f}% {position:>9.1f}")


def main():
    parser = argparse.ArgumentParser(description="GSC performance analyzer")
    parser.add_argument("--days", type=int, default=28, help="Lookback period in days")
    parser.add_argument("--top", type=int, default=20, help="Number of results")
    parser.add_argument(
        "--dimension",
        choices=["query", "page"],
        default="query",
        help="Dimension to analyze",
    )
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    service = get_gsc_service()
    rows = query_gsc(service, args.days, args.top, args.dimension)

    if args.json:
        print(json.dumps(rows, indent=2))
    else:
        print(f"\nGSC {args.dimension} performance — last {args.days} days")
        print(f"Property: {GSC_PROPERTY}\n")
        format_results(rows, args.dimension)
        print(f"\nTotal results: {len(rows)}")


if __name__ == "__main__":
    main()
