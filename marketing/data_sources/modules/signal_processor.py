"""
GTM Engineering: Signal Processor

Aggregates intent signals from all connected data sources, normalises them,
applies scoring weights, and outputs a scored signal report.

Usage:
    python3 signal_processor.py              # Full run, writes to report
    python3 signal_processor.py --dry-run    # Sample output, no writes
    python3 signal_processor.py --days 14    # Custom lookback window (default 7)

Output:
    - Console: scored signal report with recommended actions
    - Coda Signals table: written via MCP (when run inside Claude session)
    - Attio contact update report: printed to console for manual application

Connections required (graceful skip if missing):
    - PostHog: POSTHOG_API_KEY + POSTHOG_PROJECT_ID env vars
    - Reddit: REDDIT_CLIENT_ID + REDDIT_CLIENT_SECRET env vars
    - GSC: OAuth token at ~/.config/gws/gsc_token.json (run gsc_analyzer.py once to create)
    - DataForSEO: DATAFORSEO_LOGIN + DATAFORSEO_PASSWORD env vars
"""

import os
import sys
import json
import uuid
import argparse
from datetime import datetime, timedelta

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SIGNAL_WEIGHTS = {
    # First-party — behavioral
    "pricing_page_visit":            8,
    "free_trial_signup":             20,
    "first_session_completed":       15,
    "session_duration_over_20min":   10,   # capped at 3x
    "return_visit_within_7days":     12,
    "upgrade_cta_click":             25,
    "email_cta_click":               8,    # capped at 2x
    "inactivity_7_days":             -20,
    "topic_completion":              5,
    "eri_improvement_over_10pts":    8,
    # Second-party — community
    "brand_mention_reddit":          15,
    "demand_signal_reddit":          5,
    "competitor_comparison_reddit":  10,
    "tutor_referral_click":          18,
    # Third-party — SEO / calendar
    "ranking_drop_5_positions":      0,    # triggers SEO alert, not user score
    "ranking_gain_5_positions":      0,    # triggers SEO positive, not user score
    "new_query_low_ctr":             0,    # content opportunity, not user score
    "exam_season_minus_30_days":     0,    # campaign trigger, not user score
}

HOT_THRESHOLD  = 40
WARM_THRESHOLD = 20
COLD_THRESHOLD = 5

EXAM_CALENDAR = {
    "cie_results_day":    (8, 15),   # (month, day)
    "edexcel_results_day": (8, 22),
    "mock_season_start":  (1, 15),
    "exam_month_start":   (5,  1),
    "resit_window_start": (10, 1),
}

DRY_RUN_SAMPLE = {
    "posthog_events": [
        {"user_id": "u_sample_001", "event": "pricing_page_visit",          "timestamp": "2026-05-14T10:23:00Z"},
        {"user_id": "u_sample_001", "event": "free_trial_signup",            "timestamp": "2026-05-14T10:25:00Z"},
        {"user_id": "u_sample_001", "event": "first_session_completed",      "timestamp": "2026-05-14T11:00:00Z"},
        {"user_id": "u_sample_001", "event": "session_duration_over_20min",  "timestamp": "2026-05-14T11:21:00Z"},
        {"user_id": "u_sample_002", "event": "return_visit_within_7days",    "timestamp": "2026-05-15T09:00:00Z"},
        {"user_id": "u_sample_002", "event": "email_cta_click",              "timestamp": "2026-05-15T09:05:00Z"},
        {"user_id": "u_sample_003", "event": "inactivity_7_days",            "timestamp": "2026-05-15T00:00:00Z"},
    ],
    "reddit_signals": [
        {"thread_id": "r_abc123", "signal": "demand_signal_reddit",
         "text": "Anyone else struggling with 9709 integration topics?",
         "subreddit": "alevel", "timestamp": "2026-05-14T18:30:00Z"},
        {"thread_id": "r_def456", "signal": "brand_mention_reddit",
         "text": "Has anyone tried ExamPilot? Looks interesting for 9709.",
         "subreddit": "CambridgeInternational", "timestamp": "2026-05-15T08:00:00Z"},
    ],
    "seo_signals": [
        {"keyword": "cambridge 9709 pure 1 past papers", "position_change": -6,
         "signal": "ranking_drop_5_positions", "current_position": 14},
        {"keyword": "integration by parts a level maths", "impressions": 320,
         "ctr": 0.02, "signal": "new_query_low_ctr"},
    ],
}


# ---------------------------------------------------------------------------
# Signal ingestion
# ---------------------------------------------------------------------------

def ingest_posthog(days: int, dry_run: bool) -> list[dict]:
    if dry_run:
        return DRY_RUN_SAMPLE["posthog_events"]
    api_key  = os.getenv("POSTHOG_API_KEY")
    proj_id  = os.getenv("POSTHOG_PROJECT_ID")
    if not api_key or not proj_id:
        print("[PostHog] SKIP — POSTHOG_API_KEY or POSTHOG_PROJECT_ID not set.")
        return []
    try:
        import requests
        since = (datetime.utcnow() - timedelta(days=days)).isoformat() + "Z"
        resp = requests.get(
            f"https://app.posthog.com/api/projects/{proj_id}/events/",
            headers={"Authorization": f"Bearer {api_key}"},
            params={"after": since, "limit": 500},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json().get("results", [])
    except Exception as e:
        print(f"[PostHog] ERROR — {e}")
        return []


def ingest_reddit(days: int, dry_run: bool) -> list[dict]:
    if dry_run:
        return DRY_RUN_SAMPLE["reddit_signals"]
    # Delegate to reddit_monitor.py output file if available
    monitor_output = "marketing/data_sources/outputs/reddit_latest.json"
    if os.path.exists(monitor_output):
        try:
            with open(monitor_output) as f:
                return json.load(f)
        except Exception as e:
            print(f"[Reddit] ERROR reading cached output — {e}")
    client_id = os.getenv("REDDIT_CLIENT_ID")
    if not client_id:
        print("[Reddit] SKIP — REDDIT_CLIENT_ID not set. Run reddit_monitor.py first.")
    return []


def ingest_seo(days: int, dry_run: bool) -> list[dict]:
    if dry_run:
        return DRY_RUN_SAMPLE["seo_signals"]
    from pathlib import Path
    gsc_token = Path.home() / ".config" / "gws" / "gsc_token.json"
    if not gsc_token.exists():
        print("[SEO] SKIP — GSC not authenticated. Run gsc_analyzer.py once to complete OAuth.")
        return []
    # Delegate to gsc_analyzer.py output file if available
    gsc_output = "marketing/data_sources/outputs/gsc_latest.json"
    if os.path.exists(gsc_output):
        try:
            with open(gsc_output) as f:
                return json.load(f)
        except Exception as e:
            print(f"[SEO] ERROR reading GSC output — {e}")
    return []


def ingest_calendar() -> list[dict]:
    today = datetime.utcnow()
    signals = []
    for event_name, (month, day) in EXAM_CALENDAR.items():
        target = datetime(today.year, month, day)
        if target < today:
            target = datetime(today.year + 1, month, day)
        days_until = (target - today).days
        if 0 <= days_until <= 30:
            signals.append({
                "signal": "exam_season_minus_30_days",
                "event_name": event_name,
                "days_until": days_until,
                "date": target.strftime("%Y-%m-%d"),
            })
    return signals


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def score_users(posthog_events: list[dict]) -> dict[str, dict]:
    """Compute Conversion Readiness Score per user from PostHog events."""
    scores: dict[str, dict] = {}
    signal_counts: dict[str, dict] = {}

    for event in posthog_events:
        uid    = event.get("user_id") or event.get("distinct_id", "unknown")
        signal = event.get("event") or event.get("event_name", "")

        if uid not in scores:
            scores[uid]        = {"crs": 0, "signals": [], "tier": "Prospect"}
            signal_counts[uid] = {}

        weight = SIGNAL_WEIGHTS.get(signal, 0)
        if weight == 0:
            continue

        # Apply caps
        count = signal_counts[uid].get(signal, 0)
        if signal == "session_duration_over_20min" and count >= 3:
            continue
        if signal == "email_cta_click" and count >= 2:
            continue

        signal_counts[uid][signal] = count + 1
        scores[uid]["crs"] += weight
        scores[uid]["signals"].append(signal)

    # Combination boost: ≥3 distinct signal types in window
    for uid, data in scores.items():
        distinct_types = len(set(data["signals"]))
        if distinct_types >= 3:
            data["crs"] += 5
            data["signals"].append("combination_boost")

    # Assign tiers
    for uid, data in scores.items():
        crs = data["crs"]
        if crs >= HOT_THRESHOLD:
            data["tier"] = "Hot"
        elif crs >= WARM_THRESHOLD:
            data["tier"] = "Warm"
        elif crs >= COLD_THRESHOLD:
            data["tier"] = "Cold"
        else:
            data["tier"] = "Prospect"

    return scores


def build_signal_records(
    user_scores: dict,
    reddit_signals: list[dict],
    seo_signals: list[dict],
    calendar_signals: list[dict],
) -> list[dict]:
    """Assemble normalised signal records for Coda and Attio output."""
    records = []

    for uid, data in user_scores.items():
        tier   = data["tier"]
        crs    = data["crs"]
        action = {
            "Hot":      "Enrich Attio → conversion email priority",
            "Warm":     "Add to Brevo nurture sequence",
            "Cold":     "Demand gen only — no conversion push",
            "Prospect": "No action",
        }.get(tier, "Review")

        records.append({
            "signal_id":          str(uuid.uuid4())[:8],
            "source":             "posthog",
            "category":           "first_party",
            "type":               "behavioral",
            "entity_id":          uid,
            "signal_name":        f"user_scored_{tier.lower()}",
            "weight":             crs,
            "tier":               tier,
            "recommended_action": action,
            "destination":        "attio" if tier in ("Hot", "Warm") else "coda",
            "timestamp":          datetime.utcnow().isoformat() + "Z",
        })

    for s in reddit_signals:
        signal  = s.get("signal", "")
        action  = "Draft response via /write-reddit" if "demand" in signal else "Review and respond manually"
        records.append({
            "signal_id":          str(uuid.uuid4())[:8],
            "source":             "reddit",
            "category":           "second_party",
            "type":               "community",
            "entity_id":          s.get("thread_id", ""),
            "signal_name":        signal,
            "weight":             SIGNAL_WEIGHTS.get(signal, 5),
            "tier":               "Demand",
            "recommended_action": action,
            "destination":        "coda",
            "timestamp":          s.get("timestamp", datetime.utcnow().isoformat() + "Z"),
            "raw_value":          s.get("text", ""),
        })

    for s in seo_signals:
        signal = s.get("signal", "")
        if signal == "ranking_drop_5_positions":
            action = f"Audit content for '{s.get('keyword')}' — now position {s.get('current_position')}"
        elif signal == "new_query_low_ctr":
            action = f"Create content brief for '{s.get('keyword')}' via /research-keywords"
        else:
            action = f"Amplify content for '{s.get('keyword')}'"
        records.append({
            "signal_id":          str(uuid.uuid4())[:8],
            "source":             "gsc" if "ctr" in s else "dataforseo",
            "category":           "third_party",
            "type":               "seo",
            "entity_id":          s.get("keyword", ""),
            "signal_name":        signal,
            "weight":             0,
            "tier":               "SEO",
            "recommended_action": action,
            "destination":        "coda",
            "timestamp":          datetime.utcnow().isoformat() + "Z",
            "raw_value":          json.dumps(s),
        })

    for s in calendar_signals:
        records.append({
            "signal_id":          str(uuid.uuid4())[:8],
            "source":             "calendar",
            "category":           "third_party",
            "type":               "campaign",
            "entity_id":          s.get("event_name", ""),
            "signal_name":        "exam_season_proximity",
            "weight":             0,
            "tier":               "Campaign",
            "recommended_action": f"{s['event_name'].replace('_', ' ').title()} in {s['days_until']} days — activate campaign checklist",
            "destination":        "coda",
            "timestamp":          datetime.utcnow().isoformat() + "Z",
            "raw_value":          json.dumps(s),
        })

    return records


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def print_report(records: list[dict], user_scores: dict) -> None:
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    print(f"\n{'='*60}")
    print(f"  GTM Engineering — Signal Review  [{now}]")
    print(f"{'='*60}\n")

    # User tiers summary
    tier_groups = {"Hot": [], "Warm": [], "Cold": [], "Prospect": []}
    for uid, data in user_scores.items():
        tier_groups[data["tier"]].append((uid, data["crs"]))

    print("## BEHAVIORAL SIGNALS (PostHog)\n")
    for tier in ("Hot", "Warm", "Cold"):
        users = tier_groups[tier]
        if users:
            print(f"  {tier.upper()} ({len(users)} users):")
            for uid, crs in sorted(users, key=lambda x: -x[1]):
                action = {
                    "Hot":  "→ Enrich Attio, conversion email",
                    "Warm": "→ Brevo nurture sequence",
                    "Cold": "→ Demand gen only",
                }[tier]
                print(f"    [{crs:3d} pts] {uid}  {action}")
            print()

    # Community signals
    community = [r for r in records if r["type"] == "community"]
    if community:
        print("## COMMUNITY SIGNALS (Reddit)\n")
        for r in community:
            print(f"  [{r['signal_name']}] {r['entity_id']}")
            print(f"    \"{r.get('raw_value', '')}\"")
            print(f"    → {r['recommended_action']}\n")

    # SEO signals
    seo = [r for r in records if r["type"] == "seo"]
    if seo:
        print("## SEO SIGNALS (GSC / DataForSEO)\n")
        for r in seo:
            print(f"  [{r['signal_name']}] {r['entity_id']}")
            print(f"    → {r['recommended_action']}\n")

    # Campaign signals
    campaign = [r for r in records if r["type"] == "campaign"]
    if campaign:
        print("## CAMPAIGN SIGNALS (Exam Calendar)\n")
        for r in campaign:
            print(f"  → {r['recommended_action']}\n")

    # Attio contact update report
    hot_warm = [r for r in records if r["tier"] in ("Hot", "Warm")]
    if hot_warm:
        print("## ATTIO CONTACT UPDATES (apply manually in Phase 0)\n")
        for r in hot_warm:
            print(f"  {r['entity_id']}")
            print(f"    tier={r['tier']}  score={r['weight']}")
            print(f"    action: {r['recommended_action']}\n")

    total = len(records)
    actionable = len([r for r in records if r["recommended_action"] != "No action"])
    print(f"{'='*60}")
    print(f"  {total} signals processed  |  {actionable} actionable")
    print(f"  Write to Coda Signals table via /signal-review command")
    print(f"{'='*60}\n")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="GTM Engineering Signal Processor")
    parser.add_argument("--dry-run", action="store_true", help="Use sample data, no external calls")
    parser.add_argument("--days",    type=int, default=7,  help="Lookback window in days (default 7)")
    args = parser.parse_args()

    if args.dry_run:
        print("[DRY RUN] Using sample data. No external API calls.")

    # Ingest
    posthog_events   = ingest_posthog(args.days, args.dry_run)
    reddit_signals   = ingest_reddit(args.days, args.dry_run)
    seo_signals      = ingest_seo(args.days, args.dry_run)
    calendar_signals = ingest_calendar()

    # Score
    user_scores = score_users(posthog_events)

    # Build records
    records = build_signal_records(user_scores, reddit_signals, seo_signals, calendar_signals)

    # Output
    print_report(records, user_scores)

    # Return records for use by /signal-review command (Claude MCP layer)
    return records


if __name__ == "__main__":
    main()
