---
name: signal-review
description: Weekly GTM Engineering ritual. Aggregates intent signals from all connected sources, scores them, surfaces actionable insights, and writes results to Coda Signals table. Enitan's equivalent of Teresa's /weekly-pulse.
---

## Input

$ARGUMENTS

Optional: `--days N` to override the lookback window (default 7 days). Example: `/signal-review --days 14`

## Execution

### Step 1: Check data availability

Read `connections.md` to confirm which GTM signal sources are connected:
- PostHog (row 17 — GTM signals): POSTHOG_API_KEY set?
- Reddit Monitor (row 14): REDDIT_CLIENT_ID set?
- GSC (row 10): OAuth token at ~/.config/gws/gsc_token.json present?
- DataForSEO (row 12): DATAFORSEO_LOGIN set?

### Step 2: Run the signal processor

```bash
python3 marketing/data_sources/modules/signal_processor.py --days 7
```

If data sources are not connected yet, run in dry-run mode to validate the pipeline:

```bash
python3 marketing/data_sources/modules/signal_processor.py --dry-run
```

### Step 3: Review the output

The processor outputs four sections:

**Behavioral signals:** Users scored by Conversion Readiness Score (CRS). Show Hot, Warm, Cold tiers with scores and recommended actions.

**Community signals:** Reddit mentions, demand signals, competitor threads. Each flagged with recommended action (respond / draft via /write-reddit / monitor).

**SEO signals:** Ranking changes, new queries. Each flagged for content audit or brief creation.

**Campaign signals:** Exam calendar events within 30 days. Campaign activation checklist.

### Step 3b: AIO-presence monitoring on top ranking queries (SEO signal)

AI Overview presence decides the KPI for each ranking page (citation share vs CTR) and it reshuffles every ~2 days. Track it weekly so KPI choice and CTR/impression swings are explained, not guessed.

1. Pull the top ranking queries from GSC (these have real demand):
```bash
python3 marketing/data_sources/modules/gsc_analyzer.py --days 7 --top 10 --dimension query
```
2. Check current AIO presence for each (UK by default; spot-check a core CIE market like `--location pakistan` for high-impression queries, since AIO exposure varies by geography):
```bash
python3 marketing/data_sources/modules/serp_analyzer.py --keyword "[query]" --location uk
```
(~$0.0035/query; ~$0.04 for the top 10.)

3. Produce the AIO map and flag **changes vs last week**:
- **AIO present** → manage by citation share + brand search; action = GEO optimisation (answer-first, FAQ, query fan-out), not title tweaks.
- **AIO absent** → real click capture; action = CTR/title work, comparison/`/vs/` and pricing pages.
- **Newly gained an AIO** → expect CTR/impressions-to-clicks to drop; reframe that page's KPI to citation share. This is the signal that most often explains a "ranking held but clicks fell" pattern.
- **Newly lost an AIO** → a CTR/click opportunity reopened.

Feed the most material change into the "Top SEO Signal" in Step 6. Per-query AIO is a snapshot; SERP-API detection can undercount AIOs that load on interaction.

### Step 4: Write to Coda Signals table

For each actionable signal, write a row to the Coda Signals table using the Coda MCP:
- Source, Type, Entity ID, Score/Weight, Tier, Recommended Action, Status = Pending, Date = today

Use `mcp__claude_ai_Coda__table_rows_manage` to write rows.

**GTM Signals table URI:** `coda://docs/hWFDV3mysB/tables/grid-pA5mWDIvmp`  
**Spyglass OS page:** `coda://docs/hWFDV3mysB/pages/section-SD0fn6uQyV`

Column order: Signal ID, Date, Source, Type, Entity ID, Signal Name, Score, Tier, Recommended Action, Status

### Step 5: Attio contact update report

For all Hot and Warm users, print the Attio contact update fields:
- Email / PostHog User ID
- Tier (Hot / Warm)
- CRS score
- Recommended action

**Phase 0:** Apply these updates manually in Attio. No automated API call yet.
**Phase 1:** signal_processor.py will call the Attio API directly.

### Step 6: Summarise and recommend

Output a one-screen summary:

```
## Signal Review: [date range]

### User Tiers
- Hot: X users → [actions]
- Warm: X users → [actions]
- Churning: X users → [actions]

### Top Community Signal
[Most important Reddit signal this week. One sentence with recommended response.]

### Top SEO Signal
[Most important ranking movement. One sentence with recommended action.]

### Campaign Alerts
[Any exam calendar events within 30 days.]

### This Week's Priority Actions
- [ ] [Highest-leverage action — specific]
- [ ] [Second action]
- [ ] [Third action]

### Attio Updates Required
[List of user IDs with tier and score to apply in Attio]
```

### Step 7: Cross-reference with /weekly-pulse

If this is the Friday ritual, run `/weekly-pulse` after `/signal-review`. The pulse covers Marketing Machine (content, community output). Signal review covers GTM Engineering (intent signals, behavioral data). Together they give the full weekly picture.

## Context files

- `marketing/gtm-engineering/signal-registry.md` — all signals and weights
- `marketing/gtm-engineering/scoring-model.md` — tier definitions and mechanics
- `marketing/gtm-engineering/trigger-playbook.md` — actions per threshold
- `marketing/data_sources/modules/signal_processor.py` — the computation engine
