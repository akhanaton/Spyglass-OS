---
name: research-trending
description: Identifies keywords with rapid growth in search interest using exam season triggers. Outputs time-sensitive content opportunities ranked by urgency.
---

## Input

$ARGUMENTS

Optional: a topic area or exam board to focus on. Examples:
- "cambridge 9709" — trending topics for CAIE students only
- "edexcel ial" — trending topics for Edexcel IAL students only
- (no input) — full trending analysis across all tracked topics

## Execution

### Step 1: Check DataForSEO connection

Read `connections.md` and check if DataForSEO is connected.

**If connected:** Compare 7-day vs 30-day search volume for tracked keywords:
```bash
python3 marketing/data_sources/modules/trending_analyzer.py --location 2826 --language en --compare-periods 7d,30d
```
Use live volume trends for ranking in Step 4.

**If not connected:** Proceed with exam-calendar-driven seasonal analysis (Steps 2-4).

### Step 2: Read exam calendar signals

Read `marketing/gtm-engineering/signal-registry.md` for the ExamPilot exam calendar.

Key seasonal windows (use these if file is unavailable):
```
Mock season:         Jan 15 – Feb 15
Main exam season:    May 1 – Jun 15
CIE Results Day:     Aug 15
Edexcel Results Day: Aug 22
Resit window:        Oct 1 – Nov 30
Post-results panic:  Aug 15 – Sep 15
```

Check Google Calendar connection in `connections.md`. If connected:
```
Use Google Calendar MCP to check for any upcoming exam dates or student milestones added to calendar
```

Calculate days from today (2026-05-16) to each key window:
- Mock season start: [days away]
- Main exam season: [days away — CURRENTLY ACTIVE if between May 1 and Jun 15]
- CIE Results Day: [days away]
- Resit window start: [days away]

Flag active window: "Currently in [window name]. High urgency for [topic types]."

### Step 3: Apply topic-to-season mapping

Map which topics spike in each window:

**Mock season (Jan-Feb):** Integration techniques, differentiation rules, trigonometric identities, P1 past paper practice, "how to revise for mocks", "cambridge 9709 mock paper"

**Pre-exam (Mar-Apr):** P3 topics (complex numbers, vectors, differential equations), statistics revision, mechanics formulas, grade boundary predictions, "last minute revision 9709", "what topics come up most in 9709 P1"

**Main exam season (May-Jun):** Specific paper help, past paper solutions, "9709 P1 June 2026" [VERIFY], "WMA11 2026 paper" [VERIFY], mark scheme interpretation, "how to check answers A level maths"

**Post-results (Aug 15 - Sep 15):** Grade boundary lookups, resit decisions, "cambridge 9709 grade boundaries 2026" [VERIFY], "should I resit WMA11", "best way to improve A level maths grade"

**Resit window (Oct-Nov):** Resit-specific keywords, "how to pass cambridge 9709 resit", "edexcel ial resit tips", "how many marks do I need to pass WMA11"

### Step 4: Rank trending opportunities by urgency

For each trending topic, score urgency:

**Urgency score = (proximity to spike × 3) + (content gap × 2) + (volume tier × 1)**

- Proximity to spike: content 4-6 weeks before spike = 10, 2-4 weeks = 7, 0-2 weeks (urgent!) = 5, post-spike = 1
- Content gap: ExamPilot has nothing = 5, has adjacent content = 3, has this content = 0
- Volume tier: estimated high volume = 3, medium = 2, low = 1

Output ranked list with urgency score and recommended publish date.

### Step 5: Output trending topics list

Format each entry:
```
Topic: [keyword or topic]
Exam board: Cambridge 9709 | Edexcel IAL | Both
Season window: [window name]
Days to spike peak: [X days]
Urgency score: [score/50]
ExamPilot coverage: none | adjacent | covered
Content type: new article | rewrite | comparison | landing page
Recommended publish by: [date — 4-6 weeks before spike]
Command: /write-article "[keyword]" | /rewrite [file] | /research-keywords "[keyword]"
```

### Step 6: Time-sensitive alerts

Flag any item where days to spike peak < 14 as URGENT:

> URGENT: "[keyword]" spikes in [X] days. Publish by [date]. Run `/write-article "[keyword]"` now.

Flag any item where days to spike peak is 14-28 as THIS WEEK:

> THIS WEEK: "[keyword]" spikes in [X] days. Add to calendar. Run `/research-keywords "[keyword]"` to start brief.

### Step 7: Save report

Save to `marketing/pipelines/research/trending-YYYY-MM-DD.md`

```yaml
---
type: trending-analysis
dataforseo_connected: true | false
current_season_window: ""
active_urgency_alerts: []
topics_analyzed: 0
analysis_date: YYYY-MM-DD
---

## Trending Analysis — [Date]

### Active Season Window
[Current window + days remaining]

### URGENT (Publish within 2 weeks)
[Topics with score ≥ 35]

### THIS WEEK (Brief this week, publish within 4 weeks)
[Topics with score 20-34]

### PLAN AHEAD (Brief next 30 days)
[Topics with score 10-19]

### Seasonal Calendar Summary
[Overview of upcoming spikes by month]
```

### Step 8: Prompt

Show urgent items only and ask: "Found [X] urgent trending opportunities. Top pick: '[keyword]' — spike in [Y] days. Run `/write-article '[keyword]'` to start drafting?"
