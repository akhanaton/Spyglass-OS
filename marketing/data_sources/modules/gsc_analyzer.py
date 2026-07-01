#!/usr/bin/env python3
"""Google Search Console analyzer for ExamPilot marketing.

Pulls query and page performance data from GSC using OAuth credentials
shared with the GWS CLI (client_secret.json at ~/.config/gws/).

On first run, opens a browser for consent. Token is cached at
~/.config/gws/gsc_token.json for subsequent runs.

Usage:
    python3 gsc_analyzer.py --days 28 --top 20
    python3 gsc_analyzer.py --days 7 --top 50 --dimension page
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Windows consoles default to cp1252, which chokes on non-Latin query text.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

try:
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
except ImportError:
    print("ERROR: google-api-python-client not installed.")
    print("Run: pip install -r marketing/data_sources/requirements.txt")
    sys.exit(1)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config import GSC_PROPERTY

SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
CLIENT_SECRET = Path.home() / ".config" / "gws" / "client_secret.json"
TOKEN_FILE = Path.home() / ".config" / "gws" / "gsc_token.json"


def get_gsc_service():
    if not CLIENT_SECRET.exists():
        print(f"ERROR: client_secret.json not found at {CLIENT_SECRET}")
        print("Expected the same file used by the GWS CLI.")
        sys.exit(1)

    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT_SECRET), SCOPES)
            creds = flow.run_local_server(port=0)
        TOKEN_FILE.write_text(creds.to_json())

    return build("searchconsole", "v1", credentials=creds)


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
