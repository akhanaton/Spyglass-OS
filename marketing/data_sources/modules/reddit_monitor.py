#!/usr/bin/env python3
"""Reddit monitor for ExamPilot marketing.

Tracks keyword mentions, trending questions, and brand mentions
in target subreddits.

Requires: REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET env vars.

Usage:
    python3 reddit_monitor.py --subs "alevel,6thForm" --days 7
    python3 reddit_monitor.py --subs "CambridgeInternational,Edexcel" --days 3 --brand-only
"""

import argparse
import json
import sys
from datetime import datetime, timedelta

try:
    import praw
except ImportError:
    print("ERROR: praw not installed.")
    print("Run: pip install -r marketing/data_sources/requirements.txt")
    sys.exit(1)

sys.path.insert(0, "..")
from config import (
    BRAND_KEYWORDS,
    REDDIT_CLIENT_ID,
    REDDIT_CLIENT_SECRET,
    REDDIT_USER_AGENT,
    TARGET_SUBREDDITS,
    TOPIC_KEYWORDS,
)


def get_reddit():
    if not REDDIT_CLIENT_ID or not REDDIT_CLIENT_SECRET:
        print("ERROR: REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET not set.")
        print("See connections.md row 14.")
        sys.exit(1)

    return praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT,
    )


def search_subreddit(reddit, sub_name, keywords, days, limit=100):
    subreddit = reddit.subreddit(sub_name)
    cutoff = datetime.utcnow() - timedelta(days=days)
    results = []

    for keyword in keywords:
        for submission in subreddit.search(keyword, time_filter="week", limit=limit):
            created = datetime.utcfromtimestamp(submission.created_utc)
            if created < cutoff:
                continue

            results.append(
                {
                    "subreddit": sub_name,
                    "title": submission.title,
                    "url": f"https://reddit.com{submission.permalink}",
                    "score": submission.score,
                    "num_comments": submission.num_comments,
                    "created": created.strftime("%Y-%m-%d %H:%M"),
                    "matched_keyword": keyword,
                    "is_brand_mention": any(
                        bk in submission.title.lower()
                        or bk in (submission.selftext or "").lower()
                        for bk in BRAND_KEYWORDS
                    ),
                }
            )

    seen_urls = set()
    unique = []
    for r in results:
        if r["url"] not in seen_urls:
            seen_urls.add(r["url"])
            unique.append(r)

    return sorted(unique, key=lambda x: x["score"], reverse=True)


def get_trending(reddit, sub_name, days, limit=25):
    subreddit = reddit.subreddit(sub_name)
    cutoff = datetime.utcnow() - timedelta(days=days)
    results = []

    for submission in subreddit.hot(limit=limit):
        created = datetime.utcfromtimestamp(submission.created_utc)
        if created < cutoff:
            continue

        results.append(
            {
                "subreddit": sub_name,
                "title": submission.title,
                "url": f"https://reddit.com{submission.permalink}",
                "score": submission.score,
                "num_comments": submission.num_comments,
                "created": created.strftime("%Y-%m-%d %H:%M"),
            }
        )

    return results


def format_results(results, section_title):
    if not results:
        print(f"  No results found.\n")
        return

    for r in results[:15]:
        brand_flag = " [BRAND]" if r.get("is_brand_mention") else ""
        print(
            f"  [{r['score']:>4}] r/{r['subreddit']} — {r['title'][:70]}{brand_flag}"
        )
        print(f"         {r['url']}")
        print(f"         {r['num_comments']} comments | {r['created']}")
        if r.get("matched_keyword"):
            print(f"         Matched: {r['matched_keyword']}")
        print()


def main():
    parser = argparse.ArgumentParser(description="Reddit monitor for ExamPilot")
    parser.add_argument(
        "--subs",
        type=str,
        default=",".join(TARGET_SUBREDDITS),
        help="Comma-separated subreddit names",
    )
    parser.add_argument("--days", type=int, default=7, help="Lookback period in days")
    parser.add_argument(
        "--brand-only", action="store_true", help="Only show brand mentions"
    )
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument(
        "--trending", action="store_true", help="Also show trending posts"
    )
    args = parser.parse_args()

    subs = [s.strip() for s in args.subs.split(",")]
    reddit = get_reddit()

    all_keyword_results = []
    all_trending_results = []

    keywords = BRAND_KEYWORDS if args.brand_only else BRAND_KEYWORDS + TOPIC_KEYWORDS

    for sub in subs:
        keyword_results = search_subreddit(reddit, sub, keywords, args.days)
        all_keyword_results.extend(keyword_results)

        if args.trending:
            trending_results = get_trending(reddit, sub, args.days)
            all_trending_results.extend(trending_results)

    if args.json:
        output = {"keyword_matches": all_keyword_results}
        if args.trending:
            output["trending"] = all_trending_results
        print(json.dumps(output, indent=2))
    else:
        print(f"\nReddit Monitor — last {args.days} days")
        print(f"Subreddits: {', '.join('r/' + s for s in subs)}")
        print(f"Keywords: {len(keywords)} tracked\n")

        brand_results = [r for r in all_keyword_results if r.get("is_brand_mention")]
        topic_results = [
            r for r in all_keyword_results if not r.get("is_brand_mention")
        ]

        if brand_results:
            print(f"--- Brand Mentions ({len(brand_results)}) ---\n")
            format_results(brand_results, "Brand Mentions")

        print(f"--- Topic Mentions ({len(topic_results)}) ---\n")
        format_results(topic_results, "Topic Mentions")

        if args.trending and all_trending_results:
            print(f"--- Trending ({len(all_trending_results)}) ---\n")
            for r in all_trending_results[:10]:
                print(f"  [{r['score']:>4}] r/{r['subreddit']} — {r['title'][:70]}")
                print(f"         {r['num_comments']} comments | {r['created']}\n")

        print(f"Total keyword matches: {len(all_keyword_results)}")
        if brand_results:
            print(f"Brand mentions: {len(brand_results)}")


if __name__ == "__main__":
    main()
