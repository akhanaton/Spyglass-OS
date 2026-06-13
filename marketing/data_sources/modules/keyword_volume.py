#!/usr/bin/env python3
"""Keyword research: volume, difficulty, and seed expansion via DataForSEO.

Two modes:
  1. Lookup (--keywords / --file): live search volume (Google Ads) and,
     optionally, keyword difficulty (--kd) for a known list of keywords.
  2. Expand (--seed): turn one or more seed keywords into a related-keyword
     cluster (DataForSEO Labs keyword_ideas), each with volume + difficulty.
     This is the OS-native keyword research flow (replaces the never-built
     keyword_researcher.py; seomachine superseded 2026-05-16).

Both support worldwide and per-country cuts — important for CIE 9709, an
international exam whose demand is invisible under a UK-only lens.

Requires: DATAFORSEO_LOGIN + DATAFORSEO_PASSWORD in marketing/data_sources/.env

Usage:
    python3 keyword_volume.py --keywords "cambridge 9709" "9709 syllabus" --kd
    python3 keyword_volume.py --file ../keywords.txt --location pakistan
    python3 keyword_volume.py --seed "cambridge 9709 pure 1" --limit 40
    python3 keyword_volume.py --seed "9709 trigonometry" --location pakistan --json

Notes:
    - Worldwide is the default and the truest picture for international exams.
    - Google Ads volume rounds and buckets; it undercounts the informational
      long tail. A 0 means "below the planner's floor", not "no demand".
      Cross-reference with GSC impressions (gsc_analyzer.py) for real demand.
    - DataForSEO Labs endpoints (--kd, --seed) REQUIRE a location, so they
      default to US (largest keyword DB) when --location is worldwide.
      In --seed worldwide mode the candidate ideas are re-priced worldwide so
      volume is global, while expansion + difficulty remain US-based. Extra cost.
    - Seed expansion is thin for niche international exam terms (they barely
      exist in any single-country keyword DB). For those, use GSC impressions
      (gsc_analyzer.py) + Claude-generated variations, then price them here.
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
    # Load .env from the data_sources root regardless of CWD.
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
except ImportError:
    pass

# Friendly names → DataForSEO location codes. Worldwide = no location.
# Skewed to core CIE 9709 / Edexcel IAL markets.
LOCATIONS = {
    "worldwide": None,
    "us": 2840,
    "uk": 2826,
    "pakistan": 2586,
    "india": 2356,
    "uae": 2784,
    "malaysia": 2458,
    "singapore": 2702,
    "egypt": 2818,
    "nigeria": 2566,
    "kenya": 2404,
}


def _get_dataforseo_creds() -> tuple[str, str]:
    return os.getenv("DATAFORSEO_LOGIN", ""), os.getenv("DATAFORSEO_PASSWORD", "")


def _dataforseo_request(endpoint: str, payload: list) -> Optional[dict]:
    login, password = _get_dataforseo_creds()
    if not login or not password:
        print(
            "ERROR: DATAFORSEO_LOGIN / DATAFORSEO_PASSWORD not set in .env. "
            "See connections.md row 12.",
            file=sys.stderr,
        )
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
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"DataForSEO API error: {e}", file=sys.stderr)
        return None


def fetch_volume(keywords: list[str], location_code: Optional[int]) -> dict:
    """Return {keyword: {search_volume, competition, cpc}} via Google Ads data."""
    body: dict = {"keywords": keywords, "language_code": "en"}
    if location_code is not None:
        body["location_code"] = location_code
    resp = _dataforseo_request(
        "keywords_data/google_ads/search_volume/live", [body]
    )
    out: dict = {}
    if not resp or not resp.get("tasks"):
        return out, 0
    for row in resp["tasks"][0].get("result") or []:
        out[row["keyword"].lower()] = {
            "search_volume": row.get("search_volume") or 0,
            "competition": row.get("competition") or "-",
            "cpc": row.get("cpc"),
        }
    return out, resp.get("cost", 0)


def fetch_difficulty(keywords: list[str], location_code: int) -> dict:
    """Return {keyword: keyword_difficulty} via DataForSEO Labs."""
    resp = _dataforseo_request(
        "dataforseo_labs/google/bulk_keyword_difficulty/live",
        [{"keywords": keywords, "location_code": location_code, "language_code": "en"}],
    )
    out: dict = {}
    if not resp or not resp.get("tasks"):
        return out, 0
    result = resp["tasks"][0].get("result") or []
    items = (result[0].get("items") or []) if result else []
    for row in items:
        out[row["keyword"].lower()] = row.get("keyword_difficulty")
    return out, resp.get("cost", 0)


def fetch_ideas(seeds: list[str], location_code: int, limit: int = 50) -> tuple[list[dict], float]:
    """Expand seed keywords into a related-keyword cluster via DataForSEO Labs.

    Uses keyword_suggestions (full-text: returns keywords that CONTAIN the seed
    phrase), which keeps the seed intact — unlike keyword_ideas, which is
    category-based and tokenises multi-word seeds badly. One call per seed,
    merged and deduped. Returns (list of records, total cost).
    location_code is required by the Labs API — the caller supplies a default.
    """
    # Key by sorted-token signature so word-order permutations of the same
    # phrase ("x y z" / "z y x") collapse to a single highest-volume entry.
    seed_sigs = {frozenset(s.lower().split()) for s in seeds}
    by_sig: dict[frozenset, dict] = {}
    total_cost = 0.0
    # Over-fetch a little, since collapsing permutations shrinks the set.
    per_seed = max(1, (limit * 3) // len(seeds))
    for seed in seeds:
        resp = _dataforseo_request(
            "dataforseo_labs/google/keyword_suggestions/live",
            [{
                "keyword": seed,
                "location_code": location_code,
                "language_code": "en",
                "limit": per_seed,
                "order_by": ["keyword_info.search_volume,desc"],
            }],
        )
        if not resp or not resp.get("tasks"):
            continue
        total_cost += resp.get("cost", 0) or 0
        result = resp["tasks"][0].get("result") or []
        items = (result[0].get("items") or []) if result else []
        for row in items:
            kw = row.get("keyword")
            if not kw:
                continue
            sig = frozenset(kw.lower().split())
            if sig in seed_sigs:  # drop the seed phrase itself
                continue
            info = row.get("keyword_info") or {}
            props = row.get("keyword_properties") or {}
            rec = {
                "keyword": kw,
                "search_volume": info.get("search_volume") or 0,
                "competition": info.get("competition_level") or "-",
                "keyword_difficulty": props.get("keyword_difficulty"),
            }
            existing = by_sig.get(sig)
            if existing is None or rec["search_volume"] > existing["search_volume"]:
                by_sig[sig] = rec
    records = sorted(by_sig.values(), key=lambda r: r["search_volume"], reverse=True)
    return records[:limit], total_cost


def render(records: list[dict], loc_label: str, cost: float, show_kd: bool, as_json: bool) -> None:
    """Render a list of keyword records as a table or JSON, sorted by volume desc."""
    rows = sorted(records, key=lambda r: r.get("search_volume") or 0, reverse=True)
    if as_json:
        print(json.dumps({"location": loc_label, "cost": cost, "keywords": rows}, indent=2))
        return
    print(f"\nKeyword research — location: {loc_label}  (DataForSEO cost: ${cost})\n")
    kd_col = f"{'KD':>5}" if show_kd else ""
    print(f"{'keyword':<48}{'vol/mo':>8}{'comp':>13}{kd_col}")
    print("-" * (69 + (5 if show_kd else 0)))
    for rec in rows:
        kd = rec.get("keyword_difficulty")
        kd_val = f"{kd:>5}" if show_kd and kd is not None else (f"{'-':>5}" if show_kd else "")
        kw = (rec.get("keyword") or "")[:46]
        print(f"{kw:<48}{rec.get('search_volume') or 0:>8}{str(rec.get('competition') or '-'):>13}{kd_val}")
    print(f"\n{len(rows)} keywords.\n")


def main():
    parser = argparse.ArgumentParser(description="Keyword research: volume, difficulty, seed expansion (DataForSEO)")
    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument("--keywords", nargs="+", help="Look up a known list of keywords (quote each)")
    src.add_argument("--file", help="Look up keywords from a file, one per line")
    src.add_argument("--seed", nargs="+", help="Expand seed keyword(s) into a related-keyword cluster")
    parser.add_argument(
        "--location", default="worldwide",
        help=f"Location: {', '.join(LOCATIONS)} (default: worldwide)",
    )
    parser.add_argument("--location-code", type=int, help="Raw DataForSEO location code (overrides --location)")
    parser.add_argument("--kd", action="store_true", help="Lookup mode: also fetch keyword difficulty (extra cost). Seed mode always includes KD.")
    parser.add_argument("--limit", type=int, default=50, help="Seed mode: max ideas to return (default 50)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    # Resolve location once for both modes.
    if args.location_code is not None:
        location_code = args.location_code
        loc_label = f"code {location_code}"
    else:
        if args.location not in LOCATIONS:
            print(f"ERROR: unknown location '{args.location}'. Options: {', '.join(LOCATIONS)}", file=sys.stderr)
            sys.exit(1)
        location_code = LOCATIONS[args.location]
        loc_label = args.location

    # --- Expand mode -------------------------------------------------------
    if args.seed:
        labs_code = location_code if location_code is not None else LOCATIONS["us"]
        ideas, cost = fetch_ideas(args.seed, labs_code, args.limit)
        if location_code is None and ideas:
            # Worldwide: re-price the candidate ideas globally (Labs data is US).
            ww, ww_cost = fetch_volume([r["keyword"] for r in ideas], None)
            cost = (cost or 0) + (ww_cost or 0)
            for r in ideas:
                w = ww.get((r["keyword"] or "").lower())
                if w:
                    r["search_volume"] = w["search_volume"]
                    r["competition"] = w["competition"]
            ideas.sort(key=lambda r: r["search_volume"], reverse=True)
            loc_label = "worldwide volume; US expansion + KD"
        render(ideas, loc_label, round(cost or 0, 4), show_kd=True, as_json=args.json)
        return

    # --- Lookup mode -------------------------------------------------------
    if args.file:
        keywords = [ln.strip() for ln in Path(args.file).read_text(encoding="utf-8").splitlines() if ln.strip()]
    else:
        keywords = args.keywords

    vol, vol_cost = fetch_volume(keywords, location_code)
    cost = vol_cost or 0

    kd_map = {}
    if args.kd:
        kd_code = location_code if location_code is not None else LOCATIONS["us"]
        kd_map, kd_cost = fetch_difficulty(keywords, kd_code)
        cost += kd_cost or 0

    records = []
    for kw in keywords:
        v = vol.get(kw.lower(), {})
        rec = {
            "keyword": kw,
            "search_volume": v.get("search_volume", 0),
            "competition": v.get("competition", "-"),
        }
        if args.kd:
            rec["keyword_difficulty"] = kd_map.get(kw.lower())
        records.append(rec)

    render(records, loc_label, round(cost, 4), show_kd=args.kd, as_json=args.json)


if __name__ == "__main__":
    main()
