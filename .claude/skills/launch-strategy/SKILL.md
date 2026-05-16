---
name: launch-strategy
description: Plan and execute ExamPilot's product launch — first 100 students, soft launch sequencing, exam calendar gating, and the activation chain from waitlist to paying subscriber. Reads the launch playbook and produces a launch-ready execution plan.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.
  The Three Ms of AI™ is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.*

## What this skill does

Plans and sequences ExamPilot's launch. Covers launch readiness gating, the first 100 students acquisition plan, launch day execution, and exam calendar timing. Connects the product and GTM states to produce a concrete, sequenced plan — not a strategy deck.

**Bike Method Phase 1:** This skill produces plans and copy recommendations. All launch copy requires human review before posting. No auto-posting.

## When `/launch-strategy` runs

- "Are we ready to launch?"
- "What's blocking launch?"
- "How do we get our first 100 students?"
- "It's launch day — what do I do?"
- "When should we launch?"
- Planning the soft launch phase (first 10 students)
- Post-launch: diagnosing why acquisition is below target

## Context files — read at session start

```bash
cat marketing/context/funnel-strategy.md
cat marketing/context/audience-segments.md
cat marketing/context/channel-playbooks.md
cat marketing/references/launch-playbook.md
cat marketing/gtm-engineering/signal-registry.md
```

---

## ExamPilot launch context

**Current phase:** Phase 0 (pre-launch, command-driven, manual)

**Launch gates — all must be cleared before full public launch:**

Technical gates:
- QLP (Question Learning Pipeline) seed data for CIE 9709 Pure 1 — [VERIFY status]
- Dodo Payments integration live — [VERIFY status]
- PostHog `identify()` implemented (EP-42) — [VERIFY status]
- MSLQ (motivation) gate in product — [VERIFY status]

Marketing gates:
- 10+ Reddit karma on target subreddits (r/alevel, r/6thForm, r/CambridgeInternational)
- Discord presence established in at least 2 A-Level student servers
- 5+ tutor contacts warmed via WhatsApp or email

Content gates:
- 3+ blog articles published and indexed
- Cambridge 9709 hub page live on Sanity CMS

GTM gates:
- At least one signal source connected to `signal_processor.py`
- Coda Signals table populated with at least one week of signal data

**Soft launch threshold:** first 10 students can be onboarded without all gates cleared — technical + Dodo Payments gates only.

---

## Mode 1: Launch readiness check

Trigger: "are we ready to launch", "what's blocking launch", "launch readiness check"

### Step 1: Read current state

```bash
cat marketing/gtm-engineering/signal-registry.md
```

Fetch wiki path-to-revenue article:
```bash
gh api repos/akhanaton/spyglass-wiki/contents/wiki/product/strategy/path-to-revenue.md --jq '.content' | base64 -d
```

If the fetch fails (article doesn't exist or wiki is unavailable), proceed with known launch gate list from this skill.

### Step 2: Check current date against exam calendar

Key exam calendar dates (from signal-registry.md — verify and update each year):
- Cambridge 9709 main exam window: May-June
- Cambridge results day: mid-August (typically around Aug 15) [VERIFY exact date]
- Cambridge resit registration opens: August
- Cambridge resit window: October-November
- Edexcel IAL main window: May-June and January
- UK sixth form academic year: September start

Optimal launch windows: 8-10 weeks before a major exam window.
Poor launch windows: the week before exams (students are in panic mode, not signing up for new tools), mid-summer break, Christmas break.

### Step 3: Produce readiness checklist

For each gate, state: CLEARED / BLOCKED / UNKNOWN (requires manual check)

```
Launch Readiness Check — [current date]
---

Technical gates:
  [ ] QLP seed data for CIE 9709 Pure 1 — [status]
  [ ] Dodo Payments integration — [status]
  [ ] PostHog identify() (EP-42) — [status]
  [ ] MSLQ gate — [status]

Marketing gates:
  [ ] Reddit karma ≥ 10 on target subs — [status]
  [ ] Discord presence in 2+ servers — [status]
  [ ] 5+ tutor contacts warmed — [status]

Content gates:
  [ ] 3+ blog articles published — [status]
  [ ] Cambridge 9709 hub page live — [status]

GTM gates:
  [ ] Signal source connected to signal_processor.py — [status]
  [ ] Coda Signals table active — [status]

Overall status: READY | SOFT LAUNCH READY | BLOCKED
Blockers: [list]
Recommended next action: [specific task]
```

---

## Mode 2: First 100 students plan

Trigger: "how do we get our first 100 students", "first 100 plan", "acquisition plan"

### Step 1: Read context

```bash
cat marketing/context/audience-segments.md
cat marketing/context/channel-playbooks.md
cat marketing/references/launch-playbook.md
```

### Step 2: Produce phased acquisition plan

---

**Phase A: First 10 students — personal network + direct (Week 0-2)**

Goal: product feedback, not growth metrics. These students are beta testers.

Actions:
- Personal outreach via WhatsApp to any A-Level Maths students in Enitan and Teresa's personal or professional networks
- WhatsApp DMs to 3-5 known A-Level Maths tutors: offer free access for their students in exchange for feedback
- Message template: "I'm building a revision tool specifically for Cambridge 9709 and Edexcel IAL — can I give you free access in exchange for 15 minutes of feedback after a week?" [VERIFY — adapt to actual product name and feature set]

Success criteria: 10 students using the product, at least 5 completing a first practice session
Trigger to Phase B: 5+ students have completed their first session AND at least one piece of product feedback received

Budget: €0

---

**Phase B: First 10-50 students — Reddit + Discord community (Week 2-8)**

Goal: organic word-of-mouth, identify first super-users.

Timing: begin 6-8 weeks before the next major exam window. Students searching for revision tools earliest are the highest-intent users.

Actions:
- Reddit: post 2-3 value-first pieces of content per week in r/alevel, r/6thForm, r/CambridgeInternational before mentioning ExamPilot
  - Value-first means: answer a student's question, share a technique, explain a concept — not promote
  - Once karma > 10 on each sub: soft-mention ExamPilot as "something I'm working on" in a relevant thread
  - Run `/write-reddit` to generate compliant posts
- Discord: join 2-3 A-Level student servers. Lurk for one week before posting. Contribute to study help threads. Mention ExamPilot only after establishing presence.
- Community rule: never post ExamPilot as a cold promotion. Always value first, product mention as a follow-up or in response to a direct question about revision tools.

Success criteria: 50 students with accounts, 25+ have completed at least one session
Trigger to Phase C: organic mentions of ExamPilot appear in Reddit/Discord without prompting (first word-of-mouth signal)

Budget: €0

---

**Phase C: First 50-100 students — content SEO + tutor channel (Week 6-16)**

Goal: establish a repeatable acquisition channel.

Actions:

SEO content:
- 3+ articles indexed for low-KD keywords (Cambridge 9709, specific topic names)
- Cambridge 9709 hub page live and indexed
- Internal link structure connecting hub to blog articles (run `/cluster` for the 9709 cluster)
- Timeline: SEO content takes 6-12 weeks to index and rank — start content production in Phase A/B

Tutor channel:
- Reach out to 10-20 A-Level Maths tutors via:
  - Tutorful, Superprof, FirstTutors profiles (find tutors listing Cambridge 9709)
  - LinkedIn (search "A-Level Maths tutor Cambridge")
- Offer: free ExamPilot access for their students' current exam cycle
- Goal: one tutor with 5+ students = 5 students. 10 tutors = up to 50 students.
- Run `/outreach-draft` to generate tutor outreach messages

Results Day resit cohort (August 15 onwards):
- Students who received unexpected Cambridge results are immediately searching for resit resources
- Content targeting: "Cambridge 9709 resit guide", "how to improve your 9709 result", "resit in October"
- Run `/write-article` for resit-specific content 4 weeks before Results Day

Success criteria: 100 students with accounts, first paid conversion (any plan)
Trigger for paid acquisition evaluation: 100 students reached with 10%+ trial-to-paid conversion

Budget: €0 (tutor outreach requires Enitan/Teresa time only)

---

### Phase summary table

| Phase | Goal | Students | Channels | Trigger to next |
|---|---|---|---|---|
| A | Feedback | 0-10 | Personal network, tutor DMs | 5 sessions completed |
| B | Word-of-mouth | 10-50 | Reddit, Discord | Organic mentions appear |
| C | Repeatable channel | 50-100 | SEO content, tutor channel, resit cohort | First paid conversion |

---

## Mode 3: Launch day execution

Trigger: "it's launch day", "what do I do today", "launch day checklist"

### Morning (9:00-12:00 local)

1. Post to r/alevel or r/6thForm — value-first post with a soft mention of ExamPilot. Do not post "we just launched" — post something useful and mention ExamPilot as context.
   - Run `/write-reddit` to draft the post
2. Send email to waitlist if one exists — keep it short (3 sentences max), link to the product, no marketing copy [VERIFY: confirm GDPR consent was collected for waitlist]
3. Check Dodo Payments dashboard: confirm payment flow is live and test transactions cleared

### Afternoon (12:00-17:00 local)

4. Post in Discord servers where presence is established — same value-first approach
5. Send WhatsApp follow-ups to any tutors who were warmed in Phase A but haven't signed up their students
6. Check PostHog for first signup events — confirm `trial_started` is firing correctly
7. Monitor Reddit/Discord for comments or questions — respond within 2 hours

### Evening (17:00-21:00)

8. Check Dodo Payments for any payment errors or failed transactions
9. Review PostHog funnel: `cta_clicked` → `trial_started` → `first_session_completed`
10. Note first-day metrics: signups, sessions completed, any payment conversions

**Do not:** post on multiple channels simultaneously. Stagger by at least 2 hours to allow time to respond to engagement on each channel before moving to the next.

**Do not:** post on Saturday or Sunday. Student activity is lower on weekends for academic content.

---

### First 48 hours: daily checks

Check each morning and evening:

1. Signup count vs Phase A target (10 students)
2. Session completion rate (`first_session_completed` / `trial_started`) — target > 50%
3. Dodo Payments: any errors, failed transactions, or chargebacks
4. Product bugs: any error reports from new users (monitor error tracking)
5. Reddit/Discord sentiment: any negative feedback or confusion about the product

**Week 1 recovery — if below 10 signups by Day 7:**
- Do not panic and increase posting frequency — this looks spammy
- Identify which channel produced the most signups (even if all were low)
- Double down on that channel with more value-first content
- Run `/signal-review` to check if there are intent signals from other sources

---

## Mode 4: Launch timing

Trigger: "when should we launch", "what's the best time to launch", "is now a good time"

### Step 1: Read current date

Current date: pulled from context at session start.

### Step 2: Read exam calendar

```bash
cat marketing/gtm-engineering/signal-registry.md
```

### Step 3: Assess optimal windows

**Best windows (in order of priority):**

1. 8-10 weeks before Cambridge main exam (May-June window): highest urgency, longest revision runway. Students are planning their revision strategy. This is when ExamPilot is most compelling.
2. 4-6 weeks before Cambridge main exam: still good urgency, compressed runway. Some students will have already committed to other resources.
3. September (start of sixth form year): students are starting A-Level Maths fresh. No urgency but high intent to build good habits. Longer conversion timeline.
4. Results Day week (August 15 approximately): high intent from resit cohort. Smaller audience but very high motivation.
5. Resit window preparation (August-September): resit students have confirmed they are retaking.

**Poor windows:**
- The week immediately before exams: students are in panic mode and do not sign up for new tools
- Mid-summer (July): students are not in revision mindset
- Christmas break: same — low student activity
- Half-term breaks: lower activity, but acceptable if timing is otherwise good

### Step 4: Produce recommendation

```
Launch Timing Assessment — [current date]
---

Nearest optimal window: [window name] — [start date] to [end date]
Weeks until optimal window: [N]
Confidence: HIGH | MEDIUM | LOW

Recommended launch date: [specific date]
Rationale: [1-2 sentences]

Alternative window: [next best window] — [date]
Rationale: [1-2 sentences]

What to do between now and launch: [3-5 specific actions ranked by priority]
```

---

## Output format

```
Launch Strategy: [mode name]
---

[Mode 1 — Readiness check output as specified above]

[Mode 2 — Phase plan output as specified above]

[Mode 3 — Launch day checklist output as specified above]

[Mode 4 — Timing recommendation output as specified above]

[VERIFY] flags: [list all]
Next step: [specific recommended action]
```

---

## Guardrails

- Never promise specific acquisition numbers without data — all projections carry [VERIFY]
- All launch copy (Reddit posts, Discord messages, tutor outreach) requires human review before posting — no auto-posting
- GDPR compliance: any waitlist emails require confirmed opt-in consent
- Do not launch on a weekend — student acquisition activity is lower Saturday-Sunday
- Do not launch the same week as major exam dates — students in exam mode do not sign up for new products
- Tutor outreach: do not scrape or cold-email at scale — all outreach should be personalised
- Under-18 audience: any email or community post referencing student data must be GDPR/PECR compliant
- EUR pricing only in all launch copy

## What this skill does NOT do

- Does not write the full Reddit posts or outreach messages. Use `/write-reddit` and `/outreach-draft` for that.
- Does not write the launch email sequence. Use `/email-sequence` for that.
- Does not design the in-product onboarding after students sign up. Use `/onboarding-cro` for that.
- Does not configure PostHog events or analytics. Use `/analytics-tracking` for that.
- Does not auto-save output. Present inline; save only on user instruction.
