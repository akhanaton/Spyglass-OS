"""
YouTube Transcript Fetcher

Fetches video transcripts from a YouTube channel and formats them as
wiki-compliant raw/ source files ready for /ingest.

Each video becomes one markdown file with YAML frontmatter. Videos with
no available transcript are skipped and logged.

Usage:
    python3 yt_transcript_fetcher.py \\
        --channel https://www.youtube.com/@OfficialSEOBrothers/videos \\
        --output /path/to/wiki/raw/marketing/seo-brothers/ \\
        --limit 10
"""

import re
import sys
import time
import argparse
from pathlib import Path

try:
    from youtube_transcript_api import (
        YouTubeTranscriptApi,
        CouldNotRetrieveTranscript,
        TranscriptsDisabled,
        NoTranscriptFound,
    )
    TRANSCRIPT_API_AVAILABLE = True
except ImportError:
    TRANSCRIPT_API_AVAILABLE = False

try:
    import yt_dlp
    YTDLP_AVAILABLE = True
except ImportError:
    YTDLP_AVAILABLE = False


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _check_deps() -> None:
    missing = []
    if not YTDLP_AVAILABLE:
        missing.append("yt-dlp")
    if not TRANSCRIPT_API_AVAILABLE:
        missing.append("youtube-transcript-api")
    if missing:
        print(f"Error: missing dependencies: {', '.join(missing)}", file=sys.stderr)
        print(f"Install with: pip install {' '.join(missing)}", file=sys.stderr)
        sys.exit(1)


def slugify(title: str, max_length: int = 60) -> str:
    """Convert a video title to a kebab-case filename slug."""
    slug = title.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    slug = slug.strip("-")
    return slug[:max_length].rstrip("-")


def get_video_list(channel_url: str, limit: int = None) -> list[dict]:
    """
    Use yt-dlp to enumerate videos from a YouTube channel.
    Returns list of {id, title, date} dicts.
    """
    ydl_opts = {
        "quiet": True,
        "extract_flat": True,
        "skip_download": True,
    }
    if limit:
        ydl_opts["playlistend"] = limit

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(channel_url, download=False)

    entries = info.get("entries", []) if info else []
    videos = []
    for entry in entries:
        if not entry:
            continue
        video_id = entry.get("id", "")
        title = entry.get("title", "Untitled")
        upload_date = entry.get("upload_date", "")
        if upload_date and len(upload_date) == 8:
            upload_date = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}"
        if video_id:
            videos.append({"id": video_id, "title": title, "date": upload_date or ""})

    return videos


def fetch_transcript(video_id: str) -> str | None:
    """
    Fetch transcript for a YouTube video via youtube-transcript-api.
    Returns cleaned plain text, or None if unavailable.
    """
    try:
        api = YouTubeTranscriptApi()
        snippets = api.fetch(video_id, languages=["en", "en-GB", "en-US"])
    except (CouldNotRetrieveTranscript, TranscriptsDisabled, NoTranscriptFound):
        return None
    except Exception as e:
        print(f"  Warning: transcript error ({e})", file=sys.stderr)
        return None

    text = " ".join(snip.text.strip() for snip in snippets if snip.text)

    # Remove auto-caption noise artifacts
    text = re.sub(r"\[(?:Music|Applause|Laughter|Inaudible|MUSIC|APPLAUSE|music|applause)\]", "", text)
    text = re.sub(r"\s{2,}", " ", text)

    return text.strip()


def write_raw_file(output_dir: Path, video: dict, transcript: str) -> Path | None:
    """
    Write one wiki-compliant raw/ markdown file for a video.
    Returns None if the file already exists (idempotent — won't overwrite).
    """
    slug = slugify(video["title"])
    filepath = output_dir / f"{slug}.md"

    if filepath.exists():
        return None

    # Escape any double-quotes in the title for YAML safety
    safe_title = video["title"].replace('"', '\\"')

    content = f"""---
source_type: video-transcript
reliability: medium-high
domain: marketing
origin: YouTube - SEO Brothers
title: "{safe_title}"
url: https://youtu.be/{video['id']}
date: "{video['date']}"
ingested: false
---

{transcript}
"""
    filepath.write_text(content, encoding="utf-8")
    return filepath


# ---------------------------------------------------------------------------
# Core
# ---------------------------------------------------------------------------

def run(channel_url: str, output_dir: str, limit: int = None, delay: float = 3.0) -> dict:
    """
    Fetch transcripts from a YouTube channel and write raw/ source files.

    Returns:
      - written: list of file paths created
      - skipped: list of video dicts with no transcript
      - total: total videos found
    """
    _check_deps()

    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    print(f"Fetching video list from: {channel_url}")
    if limit:
        print(f"Limit: {limit} videos")

    videos = get_video_list(channel_url, limit=limit)
    print(f"Found {len(videos)} videos\n")

    written = []
    skipped = []

    for i, video in enumerate(videos, start=1):
        print(f"[{i}/{len(videos)}] {video['title'][:70]}")

        # Check existence before fetching to avoid unnecessary requests
        slug = slugify(video["title"])
        if (out_path / f"{slug}.md").exists():
            print("  Skipped — already exists")
            continue

        transcript = fetch_transcript(video["id"])

        if delay > 0 and i < len(videos):
            time.sleep(delay)

        if transcript is None:
            print("  Skipped — no transcript available")
            skipped.append(video)
            continue

        filepath = write_raw_file(out_path, video, transcript)
        if filepath is None:
            print("  Skipped — already exists")
            continue
        print(f"  Saved  → {filepath.name}")
        written.append(str(filepath))

    print(f"\nDone. {len(written)} written, {len(skipped)} skipped (no transcript).")

    if skipped:
        print("\nSkipped videos:")
        for v in skipped:
            print(f"  - {v['title'][:70]}")

    return {"written": written, "skipped": skipped, "total": len(videos)}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fetch YouTube channel transcripts and format as wiki raw/ source files."
    )
    parser.add_argument(
        "--channel",
        required=True,
        help="YouTube channel URL (e.g. https://www.youtube.com/@OfficialSEOBrothers/videos)",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output directory for raw/ markdown files",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Max videos to process (default: all)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=3.0,
        help="Seconds to wait between transcript requests (default: 3.0)",
    )
    args = parser.parse_args()

    run(args.channel, args.output, limit=args.limit, delay=args.delay)


if __name__ == "__main__":
    main()
