---
name: tune
description: Monthly performance review of all active OS functions. Surfaces what's working, what isn't, and proposes parameter adjustments backed by data. Run on the last Friday of each month, after /weekly-pulse. Trigger on "tune", "monthly review", "what should we adjust", "how are we performing", or "run the improvement loop". One run = one set of proposed adjustments logged to decisions/log.md.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI(TM) (c) 2026 Nate Herk. All rights reserved.
  The Three Ms of AI(TM) is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI(TM) (c) 2026 Nate Herk. All rights reserved.*

## What this skill does

Reviews every active OS function's performance data over the past 30 days. Compares outcomes against current parameter settings. Proposes specific, data-backed adjustments. Logs accepted changes to `decisions/log.md`.

This is the "adjust" step of the continuous improvement loop defined in `references/continuous-improvement.md`.

**Bike Method Phase 1:** All proposed adjustments require human approval. The skill proposes. The founders decide.

## When `/tune` runs

- Last Friday of each month, after `/weekly-pulse`
- When either founder asks "what should we adjust?" or "how are we performing?"
- After any phase gate review (Phase 0 > 1, Phase 1 > 2, etc.)

## Context files -- read at session start

```bash
# 1. The improvement philosophy
cat references/continuous-improvement.md

# 2. Current function parameters
cat marketing/gtm-engineering/scoring-model.md
cat marketing/gtm-engineering/signal-registry.md
cat build-in-public/references/x-strategy.md
cat marketing/context/channel-playbooks.md
cat marketing/context/content-standards.md
cat marketing/references/churn-prevention.md

# 3. Recent decisions (to avoid re-proposing what was already decided)
cat decisions/log.md
```

## Execution -- six steps

### Step 1 -- Determine active functions

Read `connections.md`. For each function in the table below, check if the data source is connected. Only review functions with connected data sources.

| Function | Data source | Connected? |
|---|---|---|
| GTM Engineering | PostHog (row 17) + Coda Signals (row 20) | Check |
| X / Build in Public | Postiz (row 23) | Check |
| SEO / Content | GSC (row 10) + DataForSEO (row 12) | Check |
| Product | PostHog (row 17) | Check |
| Customer Support | Coda (row 5) | Check |
| Email | Brevo (row 13) | Check |
| Churn Prevention | Dodo Payments (row 1) | Check |

Skip disconnected functions. Note them at the end: "These functions have no data source connected yet. Wire them to enable tuning."

### Step 2 -- Pull data for each active function

For each connected function, pull the relevant 30-day data.

**GTM Engineering (PostHog + Coda):**
- Use PostHog MCP: query conversion events, trial signups, pricing page visits, feature usage
- Ask: "How many signals were captured this month? How many led to a conversion?"
- Calculate: for each signal type, what % correlated with a conversion within 14 days?

**X / Build in Public (Postiz or manual):**

If Postiz is connected, query the API. Otherwise ask:
- "How many posts did each founder publish this month?"
- "How many threads?"
- "Approximate average engagement rate?"
- "Which post type got the most engagement? (milestone/decision/failure/tip/question)"
- "How many replies did each founder send?"
- "Any inbound DMs or connections from X?"

Compile: engagement by post type, by format (thread vs standalone), by author, by day/time.

**SEO / Content (GSC + DataForSEO):**

If connected:
```bash
python3 marketing/data_sources/modules/gsc_analyzer.py --days 30 --top 30
```

Pull: keyword rankings gained/lost, traffic by article, top performing articles by organic sessions.

If not connected, ask:
- "Any ranking changes you noticed this month?"
- "Which articles got the most traffic?"

**Product (PostHog):**

Use PostHog MCP:
- Session counts (this month vs last)
- Feature adoption rates (which features are used, which are ignored)
- Retention: D3, D7, D30
- Drop-off points in the student journey

**Customer Support (Coda):**

Use Coda MCP to query the support log table:
- Total contacts this month by channel
- Top 3 issue types by frequency
- Insights surfaced (how many support conversations led to a product action?)

**Email (Brevo):**

If connected, query Brevo API. Otherwise ask:
- "Open rates on sequences this month?"
- "Click rates?"
- "Any sequence that underperformed?"

**Churn Prevention (Dodo Payments / ChurnWard):**

If connected:
- Monthly churn rate (voluntary + involuntary)
- Dunning recovery rate
- Save offer acceptance rate

### Step 3 -- Compare against current parameters

For each function, compare actual performance against the parameter settings:

**GTM Engineering:** Do the current signal weights predict conversion accurately? Are any signals consistently scored high but never correlating with conversion (overweighted)? Any signals scored low but frequently preceding conversion (underweighted)?

**X / Build in Public:** Current content pillar ratios are 40% progress, 25% decisions, 20% failures, 15% questions (initial estimates). Does actual engagement data support this split? Should any pillar increase or decrease? Are posting times performing as expected?

**SEO / Content:** Are quality score thresholds (e.g., minimum 80 to publish) correlating with ranking performance? Are longer or shorter articles performing better? Which keyword types (informational vs transactional vs navigational) are driving the most traffic?

**Product:** Which features have the highest usage-to-retention correlation? Are there features with high usage but low retention impact (entertaining but not sticky)?

**Customer Support:** Are the current templates covering the most common issue types? Is the "product insight" field in the Coda log actually being used to drive product decisions?

**Email:** Which send times produce the highest open rates? Which sequence types (welcome vs re-engagement vs dunning) are performing above/below target?

**Churn Prevention:** Is the dunning timeline (Day 0, 3, 7, 10, 14) performing as expected? Are save offers matching cancel reasons correctly?

### Step 4 -- Generate the tune report

Display one screen per function:

```
## /tune Report: [Month Year]

### [Function Name]

**Data reviewed:** [source, date range, sample size]

**Current parameters:**
- [Parameter 1]: [current value] (set [date], labeled as [estimate/validated])
- [Parameter 2]: [current value]

**What the data shows:**
- [Key finding 1 with specific number]
- [Key finding 2 with specific number]

**Proposed adjustment:**
- [Parameter]: [old value] -> [new value]
- **Why:** [one sentence with the data point that supports it]
- **Risk:** [what could go wrong if this adjustment is wrong]
- **Next review:** [when to check if this change worked]

**No change needed:**
- [Parameter]: performing within expectations ([metric])
```

If a function has insufficient data (< 30 data points), say so: "Insufficient data for reliable adjustment. Continue capturing. Review next month."

### Step 5 -- Human review

After presenting all function reports, ask:

"These are proposed adjustments, not decisions. For each one:
- **Accept** -- I'll update the parameter file and log it to decisions/log.md
- **Reject** -- keep current value, note why
- **Defer** -- need more data, review next month"

Wait for decisions on each proposed adjustment.

### Step 6 -- Apply accepted adjustments

For each accepted adjustment:

1. Update the source file (e.g., `scoring-model.md`, `build-in-public/references/x-strategy.md`, `channel-playbooks.md`)
2. Change the parameter value
3. Update the label from "initial estimate" to "adjusted [date] based on [data point]"
4. Append to `decisions/log.md`:

```
## YYYY-MM-DD -- /tune: [function] parameter adjustment

**Decision:** [Parameter] changed from [old] to [new].

**Why:** [Data that drove the change]. Reviewed in monthly /tune cycle.

**Alternatives considered:** Keep current value (rejected: data shows [X]); [other option if applicable].

**Next review:** [date]

**Owner:** [whoever approved]
```

Display summary:
```
### /tune Summary: [Month Year]
- Functions reviewed: X
- Adjustments proposed: X
- Accepted: X  |  Rejected: X  |  Deferred: X
- Skipped (no data): X
- Next /tune: [last Friday of next month]
```
