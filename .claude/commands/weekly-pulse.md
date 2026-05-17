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
ls -la marketing/pipelines/drafts/ marketing/pipelines/review/ marketing/pipelines/published/ marketing/pipelines/outreach/ build-in-public/pipelines/outreach/ 2>/dev/null
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

### Step 6.5: X / Build in Public metrics

Check `connections.md` for Postiz (row 23).

**If Postiz is connected:**
Query Postiz dashboard for the past 7 days:
- Total posts published (both founders combined)
- Total threads published
- Total impressions and engagement rate
- Follower count and net change
- Top performing post (by engagement)

**If not yet connected, ask:**
- "How many tweets/threads did each of you post this week?"
- "Any posts get notable engagement? Approximate likes/replies?"
- "How many replies did you send to other accounts?"

**Display:**
```
### X / Build in Public (this week)
- Posts: X  |  Threads: X  |  Replies sent: X
- Impressions: X (trend)  |  Engagement rate: X%
- Followers: X (net +/- X)
- Top post: "[first 50 chars...]" -- X likes, X replies
- Reply ratio: X% replies vs X% original (target: 70/30 first 60 days, 50/50 after)
```

If this is the first week, set the baseline. No trend data yet.

Prompt: "What should next week's thread be about? The decisions log has [N] new entries since last pulse."

### Step 6.6: LinkedIn metrics

Check `connections.md` for LinkedIn (row 26) — Postiz scheduling.

**If Postiz is connected:**
Query Postiz dashboard for LinkedIn posts in the past 7 days (Teresa's account):
- Total posts published
- Total impressions and engagement rate
- Follower count and net change
- Top performing post (by engagement)

Also check LinkedIn native analytics if accessible:
- Profile views (indicator of outreach readiness — target 50+ before first teacher DM)
- Post reach breakdown (organic)

**If not yet connected, ask:**
- "How many LinkedIn posts did Teresa publish this week?"
- "Any posts get notable engagement? Approximate likes/comments?"
- "Any teacher or parent connections made this week?"
- "Any DMs sent or received from teachers?"

**Display:**
```
### LinkedIn / Professional Authority (this week)
- Posts: X  |  Format mix: X text, X carousel, X article
- Impressions: X (trend)  |  Engagement rate: X%
- Followers: X (net +/- X)
- Top post: "[first 50 chars...]" -- X likes, X comments
- Profile views: X (outreach readiness: [ready/not yet — target 50+ views/week])
- Teacher connections made: X  |  DMs sent: X  |  Responses: X
```

If fewer than 5 posts exist on Teresa's profile, flag: "Content warm-up insufficient for teacher outreach — post 5-10 more before sending any DMs."

Prompt: "What educator insight from this week could make a good LinkedIn post? The decisions log has [N] new entries — any worth reframing as a teacher-facing insight?"

### Step 7: Phase gate score

Determine the current phase from `marketing/strategy/marketing-plan-2026-2027.md`. Run the gate scoring block for that phase. This is the single most important output of the weekly pulse — it tells you whether you are on track to pass the gate before the deadline.

---

#### Phase 0 gate (active until gate passed or August arrives)

Query Linear via MCP for the Phase 0 milestone issues. Check completion status of these specific issues:

```
EP-55 — Landing page live (must-pass proxy: waitlist form live)
EP-62 — Waitlist email sequence loaded and tested (must-pass)
EP-60 — Facebook Groups joined ≥ 2
EP-61 — WhatsApp community created
EP-65 — "For Parents" page live
```

For data-dependent criteria, use available sources or ask manually:

| Criterion | How to check | Threshold | Weight | Must-pass? |
|---|---|---|---|---|
| Pages indexed | GSC (if connected) or ask: "How many pages indexed in GSC this week?" | ≥ 15 | 20% | Yes |
| Waitlist form live | EP-55 status in Linear | Done | 15% | Yes |
| Email sequences loaded + tested | EP-62 status in Linear | Done | 15% | Yes |
| Reddit accounts active with karma | Ask: "Reddit accounts aged 30+ days with 50+ karma?" | Yes/No | 10% | Yes |
| Blog articles published | Count files in `marketing/pipelines/published/` | ≥ 8 | 15% | No |
| Tutor conversations initiated | Ask: "How many tutor conversations started so far?" | ≥ 3 | 10% | No |
| Facebook Groups joined | EP-60 status in Linear | Done | 5% | No |
| WhatsApp community created | EP-61 status in Linear | Done | 5% | No |
| "For Parents" page live | EP-65 status in Linear | Done | 5% | No |

**Scoring:**
- Each criterion scores its full weight if met, 0 if not met
- Must-pass criteria: flag as ✗ BLOCKING if not yet met (score separately)
- Weighted score = sum of weights for met criteria

**Display:**
```
### Phase 0 Gate Score — [date]
Target: mid-July 2026  |  Hard override: August 1

Must-pass criteria:
  Pages indexed ≥ 15:          ✓/✗  (current: X pages)
  Waitlist form live:           ✓/✗  (EP-55: [status])
  Email sequences loaded:       ✓/✗  (EP-62: [status])
  Reddit accounts active:       ✓/✗

Scored criteria:
  Blog articles ≥ 8:           ✓/✗  (X/8)   [15%]
  Tutor conversations ≥ 3:     ✓/✗  (X/3)   [10%]
  Facebook Groups joined:       ✓/✗          [5%]
  WhatsApp community:           ✓/✗          [5%]
  "For Parents" page live:      ✓/✗          [5%]

Weighted score: X% / 65% threshold
Must-pass failures: X

Status: ON TRACK / AT RISK / BLOCKED
Blocking item this week: [the single highest-priority incomplete item]
```

**Status rules:**
- BLOCKED: any must-pass criterion not met AND due date < 2 weeks away
- AT RISK: weighted score < 65% AND fewer than 3 weeks to target date
- ON TRACK: all must-pass met OR sufficient time remaining

After displaying the score, state one action: "To move the needle this week: [specific next step linked to the lowest-scoring open Linear issue]."

---

#### Phase 1+ gate (once Phase 0 is passed)

Read the relevant phase gate criteria from `marketing/strategy/marketing-plan-2026-2027.md` and apply the same scoring pattern above. The Phase 0 block is replaced by the active phase's criteria.

---

**Strategy check (runs every week regardless of phase):**

Compare channel metrics from Steps 1-6 against targets from `marketing/context/funnel-strategy.md`. Flag any metric significantly off-track and note which wiki article or OS file governs it.

Reference `marketing/references/experiment-framework.md` for any active experiments. Reference `marketing/references/churn-prevention.md` for retention metrics post-launch.
