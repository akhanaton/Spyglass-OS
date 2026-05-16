---
name: content-calendar
description: Generates a 4-week content publishing calendar based on pipeline state, exam calendar, and available research. Outputs inline as a table — does not save unless asked.
---

## Input

$ARGUMENTS

Optional: a specific week to start from, or a focus constraint. Examples:
- "starting next Monday" — offset the 4-week window
- "cambridge only" — filter to 9709 content
- "include repurposing" — show full calendar including Reddit repurposing slots
- (no input) — standard 4-week calendar from today

## Execution

### Step 1: Read pipeline state

```bash
ls marketing/pipelines/topics/
ls marketing/pipelines/drafts/
ls marketing/pipelines/published/
ls marketing/pipelines/review/
```

Build status inventory:
- **Ready to publish:** Files in `review/` with status `in-review`
- **Ready to draft:** Files in `topics/` with status `researched` or `briefed`
- **In progress:** Files in `drafts/` with status `drafted`
- **Recent publishes:** Files in `published/` with dates in last 30 days (to check cadence)

Read frontmatter from each file for: `keyword`, `type`, `stage`, `target-segment`, `status`.

### Step 2: Load exam calendar

Read `marketing/gtm-engineering/signal-registry.md` for exam dates.

From today (2026-05-16), mark which exam windows fall within the next 4 weeks:
- Main exam season: May 1 – Jun 15 → ACTIVE NOW
- CIE Results Day: Aug 15
- Resit window: Oct 1 – Nov 30

Flag current active window: "ACTIVE: Main exam season (May 1 – Jun 15). Prioritize exam-specific content."

Calculate exam-urgency for each pipeline item:
- Content aligned to an active window = Week 1 priority
- Content 3-4 weeks before an upcoming window = Week 2-3 slot
- Evergreen content = fill remaining slots

### Step 3: Check DataForSEO and GSC connections

Read `connections.md`.

If DataForSEO connected: flag any trending topics that should be inserted into the calendar.
If GSC connected: flag any pages ranked 5-15 that could be refreshed for quick ranking gains.
If neither: note "Add DataForSEO or GSC for data-driven calendar prioritization."

### Step 4: Apply channel-playbooks rules

Read `marketing/context/channel-playbooks.md` for publishing constraints.

Key rules to enforce:
- Max 3 new articles per week (do not exceed this)
- Balance content types each week: at minimum 1 new article, no more than 2 rewrites per week
- Every published article should have a Reddit repurpose within 3 days (if including repurposing)
- No two articles targeting the same exam paper in the same week

### Step 5: Build 4-week calendar

**Week numbering from today:**
- Week 1: [Mon date] – [Sun date]
- Week 2: [Mon date] – [Sun date]
- Week 3: [Mon date] – [Sun date]
- Week 4: [Mon date] – [Sun date]

Slot each pipeline item using these rules:

Priority order for slotting:
1. Items in `review/` → slot earliest available (already written, just needs publishing)
2. Exam-urgent new articles (active window topics) → slot Week 1-2
3. Rewrites of stale published articles → slot Week 2-3
4. Planned new articles from `topics/` → slot Week 2-4 (need to write first)
5. Comparison / landing pages → slot Week 3-4 (lower urgency, higher effort)

Each calendar slot includes:
- Day (Mon/Wed/Fri preferred for blog cadence)
- Keyword / article title
- Content type (new article / rewrite / comparison / landing page)
- Action needed (draft / review / publish / repurpose)
- Command to execute
- Priority flag (URGENT / THIS WEEK / PLAN)

### Step 6: Add repurposing schedule (if requested or if pipeline is ahead)

For every article scheduled to publish, add a Reddit repurpose slot 1-3 days after.

Format: "Day X: Repurpose → `/repurpose [article path]` → r/[subreddit]"

Only add repurposing slots if there are articles to repurpose. Do not pad the calendar.

### Step 7: Output calendar as table

```
## 4-Week Content Calendar — Starting [Date]
Active exam window: [name or "none"]

| Week | Day | Content | Type | Action | Command | Priority |
|------|-----|---------|------|--------|---------|----------|
| W1 | Mon May 18 | [keyword] | new article | Draft | /write-article "[kw]" | URGENT |
| W1 | Wed May 20 | [keyword] | rewrite | Review | /rewrite "[path]" light | THIS WEEK |
| W1 | Fri May 22 | [keyword] | new article | Draft | /write-article "[kw]" | THIS WEEK |
| W1 | Sat May 23 | [Reddit] | repurpose | Repurpose | /repurpose "[path]" | THIS WEEK |
...
```

After table, add:

```
### Pipeline health
- Ready to publish now: [X items in review/]
- Ready to draft: [Y items in topics/]
- In progress: [Z items in drafts/]
- Gaps (weeks with < 2 items): [list if any]

### What's NOT in the calendar (backlog)
[List pipeline items that didn't fit in 4 weeks, with brief note]
```

### Step 8: Prompt

Show calendar and ask:
- "Calendar covers [X] articles, [Y] repurposes over 4 weeks."
- "Week 1 starts with [item] — should I draft this now with `/write-article '[keyword]'`?"
- "Want me to save this calendar to `marketing/pipelines/research/calendar-YYYY-MM-DD.md`?"

Do NOT save unless user explicitly asks.
