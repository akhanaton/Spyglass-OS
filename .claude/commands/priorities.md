---
name: priorities
description: Comprehensive content roadmap. Combines quick wins, gaps, performance, topics, and trends into one ranked action list. Outputs inline — does not save to file.
---

## Input

$ARGUMENTS

Optional: a focus constraint. Examples:
- "quick wins only" — filter to HIGH tier, effort ≤ 2hrs
- "exam season" — weight exam calendar urgency higher
- "cambridge only" — filter to 9709 content only
- (no input) — full roadmap across all content types

## Execution

### Step 1: Check for recent research files

```bash
ls -lt marketing/pipelines/research/ | head -20
```

Look for files created in the last 7 days:
- `gaps-*.md` — competitor gap analysis
- `trending-*.md` — trending topics
- `topic-clusters-*.md` — cluster map
- `optimize-*.md` or `analysis-*.md` — performance audits

**If recent files exist (< 7 days old):** Read them and extract opportunity items.

**If no recent files:** Run inline mini-analysis:
- Exam calendar: check current date (2026-05-16) against exam windows. Flag active window.
- Coverage: `ls marketing/pipelines/published/` and `ls marketing/pipelines/topics/` — count published vs planned
- Quick structural check: are there any drafts in `marketing/pipelines/drafts/` that just need review?

### Step 2: Check GSC connection for performance data

Read `connections.md` and check if Google Search Console is connected.

If connected, surface:
- Top 5 pages by impressions with CTR < 3% (quick win: optimize title/meta)
- Pages ranked 5-15 (low-hanging fruit: improve to top 3)
- Pages with highest impressions but low clicks (title optimization opportunity)

If not connected: skip performance data. Note in output: "GSC not connected — add for performance-based prioritization."

### Step 3: Check for review-ready drafts

```bash
ls marketing/pipelines/drafts/
```

Any article in drafts/ that is NOT a rewrite (no "rewrite-" prefix) with a creation date > 3 days ago is a review candidate. Treat review + publish as HIGH priority — it's done work waiting to ship.

### Step 4: Score each opportunity

Apply this scoring formula to every identified opportunity:

```
Priority score = (Impact × Effort_inverse × Confidence)

Impact (0-10):
  10 — exam-calendar urgent (spike < 14 days) OR review-ready draft
  8  — Tier 1 gap (KD ≤20, no ExamPilot coverage)
  7  — GSC page ranked 5-15 (needs push to top 3)
  6  — trending topic (spike in 15-30 days)
  5  — Tier 2 gap (KD 20-35)
  4  — content cluster spoke (builds topical authority)
  3  — GSC title optimization (CTR < 3%)
  2  — Tier 3 gap (KD 35+)
  1  — nice-to-have

Effort_inverse (higher = less effort):
  5 — review only (draft exists, just needs approval)
  4 — light rewrite or meta fix (< 1 hour)
  3 — new short article (1-2 hrs, 1500-2000 words)
  2 — new full article (2-4 hrs, 2000-3000 words)
  1 — cluster pillar or research-heavy (5+ hrs)

Confidence (0.0 - 1.0):
  1.0 — live DataForSEO data
  0.8 — recent GSC data
  0.6 — manual SERP assessment + exam calendar signal
  0.4 — inferred from competitor patterns
  0.2 — assumption only
```

### Step 5: Build three-tier roadmap

**HIGH — Ship this week** (Priority score ≥ 32):
- These are quick wins or urgent exam-calendar items
- Maximum 5 items (pick the highest-scoring)
- Each needs a specific next action command

**MEDIUM — This month** (Priority score 15-31):
- High impact, moderate effort
- Maximum 8 items
- Can be sequenced across 4 weeks

**LOW — Backlog** (Priority score < 15):
- Good ideas, not urgent
- List up to 5, do not expand

### Step 6: Output inline (do not save to file)

Format:

```
## Content Priorities — [Date]
Data sources used: [list what was available]

---

### HIGH — Ship this week

1. [Action] "[keyword or article]"
   Why: [1 sentence — impact + urgency]
   Effort: [time estimate]
   Command: /[command] "[arg]"

2. [Action] ...

[Up to 5 items]

---

### MEDIUM — This month

Week 1:
- [Action] "[keyword]" — Command: /[command] "[arg]"
- [Action] "[keyword]" — Command: /[command] "[arg]"

Week 2:
- ...

Week 3:
- ...

Week 4:
- ...

---

### LOW — Backlog (review next month)
- [Keyword] — [reason it's low priority]
- ...

---

### Missing data that would improve this
- [e.g. "Connect DataForSEO for live KD data"]
- [e.g. "Connect GSC for performance-based prioritization"]
```

### Step 7: Prompt

After output, ask: "What do you want to start with? I can run any of these commands now."

If any item is exam-calendar urgent (spike < 14 days), surface it first:
"NOTE: '[keyword]' is exam-urgent — spike in [X] days. Recommend starting here."
