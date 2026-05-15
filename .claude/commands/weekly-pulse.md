---
name: weekly-pulse
description: Generate a one-screen weekly performance summary across all active marketing channels. Designed as a Friday ritual.
---

## Input

$ARGUMENTS

Optional: date range override. Default is the last 7 days.

## Execution

### Step 1: Determine data availability

Read `connections.md` to check which data sources are connected:
- GSC (gsc_analyzer.py) — row 10
- GA4 (ga4_analyzer.py) — row 11
- Reddit (reddit_monitor.py) — row 14
- Brevo — row 13
- PostHog — check PostHog MCP

### Step 2: Pull available data

For each connected source, pull the data:

**GSC (if connected):**
```bash
python3 marketing/data_sources/modules/gsc_analyzer.py --days 7 --top 20
```

**Reddit (if connected):**
```bash
python3 marketing/data_sources/modules/reddit_monitor.py --subs "alevel,6thForm,CambridgeInternational,Edexcel" --days 7
```

**PostHog (if MCP available):**
Query key marketing metrics: new signups, trial starts, page views on key landing pages.

**Pipeline activity:**
```bash
find marketing/pipelines/ -name "*.md" -newer marketing/pipelines/.last-pulse 2>/dev/null | wc -l
ls -la marketing/pipelines/drafts/ marketing/pipelines/review/ marketing/pipelines/published/ marketing/pipelines/outreach/ 2>/dev/null
```

### Step 3: Manual input for unconnected sources

If data sources aren't connected yet, ask for manual inputs:
- "Any Reddit posts or comments this week? Approximate upvotes/replies?"
- "Any outreach sent? Responses received?"
- "Any new signups or trials?"
- "Anything notable from Discord communities?"

### Step 4: Generate the pulse

One-screen summary. No fluff.

```
## Weekly Pulse: [date range]

### Numbers
| Metric | This Week | Last Week | Trend |
|--------|----------|-----------|-------|
| [Available metrics from connected sources] |

### Content Pipeline
- Topics researched: X
- Drafts written: X
- In review: X
- Published: X
- Outreach sent: X

### Top Signal
[The single most important thing from this week's data. One sentence.]

### Top Opportunity
[The highest-leverage action for next week. One sentence with specific action.]

### Top Risk
[The biggest concern. One sentence.]

### Next Week Focus
- [ ] [Action 1]
- [ ] [Action 2]
- [ ] [Action 3]
```

### Step 5: Output

Display the pulse in the conversation (not saved to file by default).

If the user wants to save it:
- Save to `marketing/pipelines/research/weekly-pulse-YYYY-MM-DD.md`

### Step 6: GTM Signal Summary

Pull the latest signal data from the Coda Signals table (or from the most recent `/signal-review` output if run this week):

```
### GTM Signals (this week)
- Hot users: X  |  Warm: X  |  Churning: X
- Top community signal: [one sentence]
- Top SEO movement: [one sentence]
- Exam calendar alerts: [any events within 30 days]
→ Full detail: run /signal-review or view Coda Signals table
```

If `/signal-review` hasn't been run this week, prompt: "Run /signal-review first for a complete picture."

### Step 7: Strategy check

Compare this week's numbers against targets from `marketing/context/funnel-strategy.md`. If any metric is significantly off-track, flag it and suggest whether to adjust the strategy (with reference to which wiki article to update).

Reference `marketing/references/experiment-framework.md` for any active experiments and their status. Reference `marketing/references/churn-prevention.md` for retention metric targets if post-launch.
