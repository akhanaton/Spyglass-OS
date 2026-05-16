---
name: email-sequence
description: Write email sequences for Brevo. Covers welcome, nurture, re-engagement, and exam-calendar campaigns. All emails are mobile-optimized, under 200 words per email, with GDPR/PECR compliance for under-18 users.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.
  The Three Ms of AI™ is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.*

## What this skill does

Writes email sequences for ExamPilot's Brevo account. Covers four sequence types: welcome (new signups), nurture (free trial non-converters), re-engagement (inactive users), and exam-calendar campaigns (timed to exam season triggers). All emails are written mobile-first, under 200 words, with GDPR/PECR compliance baked in.

**Bike Method Phase 1:** All sequences require human review before uploading to Brevo. This skill produces drafts only.

## When `/email-sequence` runs

- Setting up Brevo sequences for the first time (welcome + nurture)
- Exam season approaching (mock season Jan, main exam May, results Aug, resit Oct)
- Re-engagement needed for inactive cohort
- User asks to write an email, email sequence, or campaign

## Context files — read at session start

```bash
cat references/voice-house.md
cat marketing/context/audience-segments.md
cat marketing/context/channel-playbooks.md
```

For exam-calendar campaigns, also read:
```bash
cat marketing/gtm-engineering/signal-registry.md
```

## Execution — five steps

### Step 1 — Identify sequence type

Confirm three parameters before writing:

| Parameter | Options | Example |
|---|---|---|
| Sequence type | welcome / nurture / re-engagement / exam-calendar | welcome |
| Target segment | cambridge-9709 / edexcel-ial / resit-student / parent | cambridge-9709 |
| Trigger event | signup / trial-day-7 / inactive-21d / exam-date | signup |

For exam-calendar campaigns, also confirm:
- Which exam date is being targeted (see calendar below)
- How many days before the exam to send Email 1

Show confirmation: *"Writing [sequence type] sequence for [segment], triggered by [event]. [N] emails over [timeframe]. Does this look right?"*

Do not proceed until confirmed.

---

### Step 2 — Write the sequence

Apply the correct module below.

---

#### Welcome sequence (5 emails over 14 days)

Triggered: user creates an account or joins the waitlist.

**Email 1 — Day 0: You're in**
- Subject line options (3):
  1. "You're in — here's how to get started"
  2. "Welcome to ExamPilot — your first session is waiting"
  3. "Start here [First name]"
- Preview text: under 90 characters. Expand on the subject with specificity.
- Body: Under 200 words.
  - One sentence on what ExamPilot does (not a feature list — the outcome)
  - One clear first step: "Start a practice session on your weakest topic"
  - CTA button: "Start My First Session"
- Tone: warm, peer-level. Not corporate. Not teacher-to-student.

**Email 2 — Day 2: Why spaced repetition actually works**
- Subject options:
  1. "The revision method that actually sticks"
  2. "Why re-reading your notes isn't working"
  3. "The science behind how ExamPilot builds your memory"
- Body:
  - Brief explanation of spaced repetition (2-3 sentences, plain language)
  - How ExamPilot applies it (1-2 sentences, specific to their study flow)
  - CTA: "Try a Smart Review session" (links to Smart Review feature)

**Email 3 — Day 5: Social proof**
- Subject options:
  1. "What students who pass 9709 do differently"
  2. "3 sessions a week. Here's what changes."
  3. "The pattern we see in students who improve"
- Body:
  - Generic but specific social proof: "Students who use ExamPilot 3x/week [outcome]" — use [VERIFY] for any numbers
  - What those students do in their sessions (concrete, actionable)
  - CTA: "Set your weekly session goal"
- Note: Do NOT fabricate specific named testimonials. Use [VERIFY] on any outcome claims.

**Email 4 — Day 9: Feature spotlight — Knowledge State**
- Subject options:
  1. "Do you know your actual weak topics?"
  2. "The map that shows where your gaps are"
  3. "Your Knowledge State — what it tells you"
- Body:
  - Explain the Knowledge State feature in plain terms (2-3 sentences)
  - How to use it to plan revision (numbered steps, max 3)
  - CTA: "Check my Knowledge State"

**Email 5 — Day 14: Upgrade offer (if still on free trial)**
- Subject options:
  1. "Your trial ends soon — here's what you'd lose"
  2. "Exam season is [X] weeks away — ready?"
  3. "Lock in your revision plan before [exam date]"
- Body:
  - Reference the exam timeline (make it real, not manufactured urgency)
  - State the upgrade offer simply: price + what they keep
  - Loss-aversion frame: "Your practice history, Knowledge State, and Smart Review queue won't carry over on the free plan after [date]" — use [VERIFY] on exact plan limitations
  - CTA: "Keep my progress — upgrade now"

---

#### Nurture sequence (3 emails for free trial users who haven't converted)

Triggered: user is on free trial, hasn't converted, 7+ days into trial.

**Email 1 — Trial Day 7: Check-in**
- Subject options:
  1. "How's ExamPilot going so far?"
  2. "A quick check-in — are you getting value?"
  3. "One question about your revision"
- Body:
  - Ask one question: "What's the biggest challenge you're facing right now with 9709 revision?"
  - No hard sell. Pure value signal gathering.
  - CTA: "Reply to this email" (soft — this builds deliverability and goodwill)

**Email 2 — Trial Day 12: The knowing vs memorising distinction**
- Subject options:
  1. "There's a difference between remembering and knowing"
  2. "Why memorising past papers isn't enough for Cambridge 9709"
  3. "The exam trap most students fall into"
- Body:
  - Brief explanation of the difference between passive revision (re-reading, watching videos) and active recall
  - How ExamPilot is built for the second kind
  - CTA: "Try an active recall session on [their weakest topic from Knowledge State, if known]"

**Email 3 — Trial Day 14: Last chance framing**
- Subject options:
  1. "Your trial ends tomorrow — [specific price] to continue"
  2. "Before your trial ends — one thing to know"
  3. "[Exam board] exams are in [X] weeks. Are you ready?"
- Body:
  - State the deadline clearly (no false urgency — if the trial truly ends, say so)
  - Show the EUR12/mo (annual) price prominently as the starting anchor
  - One-sentence risk reversal: "Cancel any time. Your practice data is yours."
  - CTA: "Continue my revision — EUR12/mo"

---

#### Re-engagement sequence (3 emails for users inactive >21 days)

Triggered: user has not logged in for 21+ days.

**Email 1 — Re-engagement open**
- Subject options:
  1. "We noticed you've been away"
  2. "Your Knowledge State is waiting for you"
  3. "A lot can change in 3 weeks of practice"
- Body:
  - No guilt framing. Acknowledge absence lightly: "Life gets busy."
  - Practical hook: "Your 9709 exam is [X] weeks away. Here's a 15-minute session to get back on track." (Use real exam dates if known from signal-registry.md)
  - CTA: "Start a 15-minute session"

**Email 2 — Day 3 after Email 1: Exam calendar hook**
- Subject options:
  1. "[Upcoming exam] is [X] weeks away"
  2. "The window is closing for 9709 Paper 1"
  3. "[Exam name] — here's what students do in the final weeks"
- Body:
  - Anchor to the real exam date (use signal-registry.md exam dates — no manufactured urgency)
  - Specific revision tip for the final weeks (short, practical)
  - CTA: "Get back to it — [specific topic] practice"

**Email 3 — Day 7 after Email 1: Fresh start offer**
- Subject options:
  1. "Come back with a fresh start"
  2. "Reset and refocus — here's how"
  3. "One session to get your knowledge state current"
- Body:
  - Offer a "knowledge state reset" concept (run a diagnostic session to refresh their topic map)
  - Position this as a clean starting point, not a punishment for being away
  - CTA: "Run my 9709 diagnostic"
  - Footer note: "If you're not preparing for an A-Level Maths exam right now, you can [pause your subscription] or [unsubscribe from these emails]."

After 3 emails with no engagement: stop. Do not send more than 3 re-engagement emails.

---

#### Exam-calendar campaigns (triggered by exam dates)

These are one-off sends (or short sequences of 2-3) timed to the exam calendar.

**Reference exam dates from `marketing/gtm-engineering/signal-registry.md`.** Do not use dates from memory — always read the signal registry.

**Mock season (approx. Jan 15):**
- Subject: "Mock exams in 2 weeks — are you ready?"
- Body: Mock exams as diagnostic opportunity, not threat. Specific prep tip. CTA: "Prep for mocks with ExamPilot"

**4 weeks before main exam (approx. May 1 for CIE, May 15 for Edexcel):**
- Subject: "The home stretch — your final revision plan"
- Body: Week-by-week plan for the last 4 weeks. Specific to exam board. CTA: "Build my final revision plan"

**Results Day (Aug 15 CIE / Aug 22 Edexcel):**
- Segment: split by expected result (if data available)
- Send: AFTER results are released, not before
- Subject (passed): "Congratulations — what's next for A2?" [VERIFY exact CIE/Edexcel stage terminology]
- Subject (resitting): "Got your results? Here's how to prepare differently for the resit"
- Body for resit path: no shame framing. Practical. Specific to resit timeline (Oct/Nov sitting is ~10 weeks away). CTA: "Build my resit plan"

**Resit window (approx. Oct 1 — 4 weeks before Oct/Nov sitting):**
- Subject: "Resitting 9709? Here's what to do differently"
- Body: Focus on targeted gap work (not full-course revision). What ExamPilot does for resit students specifically. CTA: "Start targeted resit prep"

---

### Step 3 — Format each email

For every email in the sequence, present in this format:

```
Email [N] — Day [X]
Trigger: [what triggers this email]

Subject line options:
  A. [Option 1]
  B. [Option 2]
  C. [Option 3]

Preview text: [under 90 chars]

Body:
[Full email body — under 200 words]

CTA button: [button text]
CTA link: [URL or placeholder]
```

---

### Step 4 — Apply guardrails

After writing all emails, apply these checks:

**Content guardrails:**
- No "AI tutor", "AI-powered", "game-changing", "revolutionary"
- "learning science", "spaced repetition", "active recall", "adaptive practice" are preferred terms
- ExamPilot is always one word, capital E and P
- Pricing in EUR only. If any pricing appears, must match: EUR29/mo, EUR69/3mo, EUR96/6mo, EUR144/yr
- No B2B or school/institution language

**GDPR/PECR compliance — include in footer of every email:**
- Unsubscribe link (mandatory — "Unsubscribe from these emails")
- Physical address or registered business address for Brevo compliance [VERIFY — confirm registered address]
- Data use statement: "You're receiving this because you signed up for ExamPilot. We won't share your email with anyone."

**Under-18 audience flags:**
- No tracking pixels on under-18 user segments without explicit consent — note this for Brevo setup
- Parental consent required for marketing emails to under-18s — flag this for Enitan to confirm consent mechanism at signup
- Do not use language that exploits exam anxiety. Natural urgency (real exam dates) is fine. Manufactured anxiety is not.

**[VERIFY] flags:**
- Any outcome data ("students who use ExamPilot 3x/week improve by X")
- Plan limitations and trial terms
- Exact exam dates (always read signal-registry.md, don't rely on memory)
- Product feature availability

---

### Step 5 — Present and save

Show the full sequence. Ask for review before offering to save.

```
Sequence: [type] for [segment]
Trigger: [event]
Emails: [count] over [timeframe]

[All emails formatted as above]

GDPR notes:
  - Unsubscribe link: required in every email ✓ (flagged in template)
  - Under-18 consent: [any flags noted]
  - Tracking pixels: confirm with Brevo settings before sending

[VERIFY] flags in this sequence: [count and list]

Next step: Review and edit. Say "save this sequence" to write to file.
```

**Save path** (only on user instruction): `marketing/pipelines/emails/[sequence-type]-[segment]-YYYY-MM-DD.md`

Frontmatter:
```yaml
---
type: email-sequence
sequence: welcome | nurture | re-engagement | exam-calendar
segment: ""
trigger: ""
email-count: [n]
status: draft
date: YYYY-MM-DD
brevo-status: not-uploaded
---
```

## What this skill does NOT do

- Does not upload to Brevo. The user uploads manually after review.
- Does not set up automation triggers in Brevo. That's a manual configuration step.
- Does not write transactional emails (password reset, receipt). Those are product emails, not marketing.
- Does not write for channels other than email. For Reddit, use `/write-reddit`. For outreach DMs, use `/outreach-draft`.
- Does not fabricate student testimonials or outcome statistics. All social proof carries [VERIFY].
