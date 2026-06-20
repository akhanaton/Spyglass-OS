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
cat build-in-public/references/linkedin-strategy.md
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
| LinkedIn / Professional Authority | Postiz (row 23) + LinkedIn native analytics | Check |
| SEO / Content | GSC (row 10) + DataForSEO (row 12) | Check |
| Product | PostHog (row 17) | Check |
| Customer Support | Coda (row 5) | Check |
| Email | Brevo (row 13) | Check |
| Churn Prevention | Dodo Payments (row 1) | Check |
| Move 37 (strategic plays) | `marketing/pipelines/strategy/` | Always on |
| Design System Sync | Claude Design (connections.md row 27) | Quarterly only — run on March, June, September, December cycles; skip all other months |

**Move 37 has a different shape than other functions.** Other functions adjust parameters from data. Move 37 captures outcomes on past strategic plays and surfaces patterns about which sediment-breaks work in this business's context. The output is pattern knowledge, not parameter changes. See Move 37-specific notes in Steps 2, 3, 4, 5, 6 below.

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

**LinkedIn / Professional Authority (Postiz or manual):**

If Postiz is connected, query LinkedIn post data. Otherwise ask:
- "How many posts did Teresa publish this month?"
- "Approximate average engagement rate?"
- "Which post type got the most engagement? (insight/milestone/teaching-moment/educator-recognition/behind-the-scenes)"
- "Which format performed best? (text post/carousel/article)"
- "How many teacher or parent connections made?"
- "Any inbound DMs from teachers or school administrators?"
- "How many outreach DMs sent? How many responded?"

Compile: engagement by post type, by format, by day/time; outreach acceptance rate; inbound DM rate.

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

**Design System Sync (quarterly only — skip if not a March/June/September/December run):**

Open Claude Design (connections.md row 27). Compare the current `@theme {}` token values against `brand/exampilot-theme.css` in the product repo. Ask:
- Are there any token values in Claude Design that differ from what's in `brand/exampilot-theme.css`?
- Are there new tokens in Claude Design not yet in the repo?
- Does `exampilot/app/globals.css` still match `brand/exampilot-theme.css` on the shared token values (excluding product-specific tokens)?

This check has no "data" in the PostHog sense — it's a manual diff exercise.

**Move 37 (strategic plays):**

Scan `marketing/pipelines/strategy/` for all `move-37-*.md` artifacts. For each, read the frontmatter and group by status:

- `status: proposed` -- not yet chosen. No action this cycle.
- `status: chosen` or `status: shipped` with `outcome: TBD` -- these need outcome capture. List them.
- `status: chosen` or `status: shipped` with outcome already filled -- pull into pattern analysis pool.
- `status: retired` -- include in pattern analysis as a "did not pursue" signal.

For each artifact needing outcome capture, list: artifact filename, frame, the 3 plays, sediment contradicted, ceiling estimate, status.

### Step 3 -- Compare against current parameters

For each function, compare actual performance against the parameter settings:

**GTM Engineering:** Do the current signal weights predict conversion accurately? Are any signals consistently scored high but never correlating with conversion (overweighted)? Any signals scored low but frequently preceding conversion (underweighted)?

**X / Build in Public:** Current content pillar ratios are 40% progress, 25% decisions, 20% failures, 15% questions (initial estimates). Does actual engagement data support this split? Should any pillar increase or decrease? Are posting times performing as expected?

**LinkedIn / Professional Authority:** Current content pillar ratios are 35% educational insights, 25% behind-the-scenes educator angle, 20% teacher recognition, 20% milestones (initial estimates). Does engagement data support this split? Is teacher outreach acceptance rate above 30% (cold outreach benchmark)? Is the warm-up content sufficient (5-10 relevant posts visible on profile before outreach)? Are posts targeted to teachers outperforming posts targeted to parents, or vice versa?

**SEO / Content:** Are quality score thresholds (e.g., minimum 80 to publish) correlating with ranking performance? Are longer or shorter articles performing better? Which keyword types (informational vs transactional vs navigational) are driving the most traffic?

**Product:** Which features have the highest usage-to-retention correlation? Are there features with high usage but low retention impact (entertaining but not sticky)?

**Customer Support:** Are the current templates covering the most common issue types? Is the "product insight" field in the Coda log actually being used to drive product decisions?

**Email:** Which send times produce the highest open rates? Which sequence types (welcome vs re-engagement vs dunning) are performing above/below target?

**Churn Prevention:** Is the dunning timeline (Day 0, 3, 7, 10, 14) performing as expected? Are save offers matching cancel reasons correctly?

**Design System Sync (quarterly):** Is the repo in sync with Claude Design? Note any drifted token values or new tokens not yet committed. If in sync: one line confirming. If out of sync: list the diffs.

**Move 37 (strategic plays):** No parameters to compare. Instead, look across artifacts with known outcomes (`outcome` not TBD) and ask:

- Which kinds of sediment-breaks have won? (e.g. distribution arbitrage, counter-positioning, time-based events, niche-then-expand)
- Which kinds consistently lost or got retired? Why -- execution failure, wrong frame, or genuinely bad bet?
- Which altitudes worked best -- whole-business plays or single-artifact plays?
- After 6+ outcomes exist, summarise: "Move 37 plays in this business tend to work when [X], tend to fail when [Y]." If fewer than 6 outcomes exist, say so and skip the pattern summary.

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

**Design System Sync report format (quarterly only):**

```
### Design System Sync

**Checked:** Claude Design vs brand/exampilot-theme.css vs exampilot/app/globals.css

**Status:** In sync | Out of sync

**Drifted tokens (if any):**
- [token name]: Claude Design = [value] / repo = [value]

**Missing tokens (if any):**
- [token name]: in Claude Design, not yet in brand/exampilot-theme.css

**Action required:** [None — in sync] OR [File issue / sync now]
```

If a sync is needed and straightforward (paste-and-commit), offer to do it in this session. Otherwise file a Linear issue.

**Move 37 report format (different shape):**

```
### Move 37

**Outcome capture needed (status: chosen/shipped, outcome: TBD):**
- [filename] -- [frame] -- chosen play: [name]
- [filename] -- [frame] -- chosen play: [name]

**Pattern analysis ([N] artifacts with known outcomes):**

What's working:
- [Pattern 1 with the artifact references that support it]
- [Pattern 2]

What's not:
- [Pattern with references]

Heuristic for future plays: [one sentence the user can use next time `/move-37` runs]

(If N < 6: "Not enough closed outcomes yet to surface reliable patterns. [N] needed before pattern analysis kicks in.")
```

### Step 5 -- Human review

After presenting all function reports, ask:

"These are proposed adjustments, not decisions. For each one:
- **Accept** -- I'll update the parameter file and log it to decisions/log.md
- **Reject** -- keep current value, note why
- **Defer** -- need more data, review next month"

Wait for decisions on each proposed adjustment.

**For Move 37 artifacts needing outcome capture, ask separately:**

"For each Move 37 artifact below, mark outcome:
- **Won** -- the play moved the commercial metric materially
- **Lost** -- the play shipped but didn't move the metric (or hurt it)
- **Inconclusive** -- shipped but signal is too noisy to call
- **Still running** -- in flight, check again next cycle
- **Retired (never shipped)** -- decided not to pursue; status changes to `retired`"

Also ask: "Anything about *why* it won or lost that's worth recording? One sentence per artifact." This is the pattern fuel.

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

**For Move 37 outcomes:**

1. Edit the artifact frontmatter in `marketing/pipelines/strategy/move-37-{slug}-{date}.md`:
   - Update `outcome:` from `TBD` to `won` / `lost` / `inconclusive` / `still-running` / `retired`
   - If status changed (e.g. proposed -> retired), update `status:` too
2. Append a `## Outcome` section to the artifact body with the one-sentence reason captured in Step 5
3. Log to `decisions/log.md` as a single grouped entry:

```
## YYYY-MM-DD -- /tune: Move 37 outcome capture

**Outcomes recorded:**
- [artifact] -> [outcome]: [reason]
- [artifact] -> [outcome]: [reason]

**Patterns surfaced this cycle:** [one-line summary, or "none -- need more outcomes"]

**Owner:** [whoever approved]
```

Do not edit the body of past artifacts beyond appending the `## Outcome` section. The original sediment scan and plays are historical record.

Display summary:
```
### /tune Summary: [Month Year]
- Functions reviewed: X
- Adjustments proposed: X
- Accepted: X  |  Rejected: X  |  Deferred: X
- Skipped (no data): X
- Move 37 outcomes captured: X  |  TBD remaining: X
- Next /tune: [last Friday of next month]
```
