---
name: onboarding-cro
description: Optimise ExamPilot's onboarding experience — from account creation to first completed practice session. Designs the activation path, in-app nudges, and empty-state copy that maximise D3 retention.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.
  The Three Ms of AI™ is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.*

## What this skill does

Designs and audits the in-product onboarding experience from account creation to first completed practice session. Where `/signup-flow-cro` handles the pre-registration and registration flow, this skill handles everything after the account exists: onboarding screens, empty states, day-0 through day-7 nudges, and the copy that drives D3 retention.

**Key metric:** First session completion rate and D3 retention (did the student return within 3 days of signing up?). These two metrics predict conversion to paid better than any other early signals.

**Activation event:** `first_session_completed` — submitting the first answer in a practice session.

**Bike Method Phase 1:** This skill produces copy and UX flow recommendations. All copy is marked [VERIFY before shipping]. No code, no auto-save.

## When `/onboarding-cro` runs

- "Improve the in-product onboarding"
- "D3 retention is low — what should I fix?"
- "What should the welcome screen say?"
- "Design the empty state for the dashboard"
- "What nudges should I send in the first 7 days?"
- Building the onboarding flow from scratch (pre-launch)

## Context files — read at session start

```bash
cat references/voice-house.md
cat marketing/context/audience-segments.md
cat marketing/context/funnel-strategy.md
```

## Execution — three steps

### Step 1: Define activation

Before designing anything, confirm what "activated" means in this context.

**ExamPilot's activation event:** `first_session_completed`
- The student has submitted at least one answer in a practice session
- This is the single event that predicts whether the student becomes a retained user

**Milestone sequence leading to activation:**
1. Account created (`trial_started`)
2. Exam board selected (during onboarding)
3. Paper/topic selected (during onboarding)
4. First session started (`session_started`)
5. First answer submitted
6. Session completed (`first_session_completed`)

**Design goal:** reduce the number of decisions between account creation and `first_session_completed`. Every extra step is a potential exit.

---

### Step 2: Onboarding flow design

Design or audit each screen in the onboarding sequence.

---

#### Welcome screen

**Headline:**
"Let's find your gaps"

Not: "Welcome to ExamPilot" — the student knows they just signed up. Skip the greeting and get to the value.

**Subheadline:**
"Answer 5 questions on [topic they'll select] — we'll show you exactly where to focus."

If topic is not yet known, use: "Answer a few questions — we'll show you exactly where your gaps are."

**Primary CTA:**
"Start your first session"

Not: "Explore", "Get Started", "Let's Go" — the CTA names the action and anchors to the outcome.

**Trust signal under the CTA:**
"Takes 5 minutes. No revision notes needed."

---

#### Exam board selection screen

**Headline:**
"Which exam are you preparing for?"

**Options:**
- Cambridge International AS & A Level Mathematics (9709)
- Edexcel International Advanced Level Mathematics (IAL)
- Other A-Level Maths

**If Cambridge selected:** show paper options immediately on the same screen (not a new screen):
- Pure Mathematics 1 (Paper 1)
- Pure Mathematics 3 (Paper 3)
- Statistics 1 (Paper 5)
- Mechanics 1 (Paper 4)

**If Edexcel selected:** show equivalent Edexcel papers [VERIFY exact Edexcel IAL paper names and codes].

**Immediate reinforcement after selection:**
Below the options, after the student taps: "ExamPilot has [N] practice questions mapped to Cambridge 9709 Pure 1." [VERIFY exact count]

**Progress indicator:** if showing multiple onboarding steps, a simple "Step 1 of 3" indicator is acceptable. Do not show a progress bar that suggests a long journey.

---

#### Knowledge state baseline (optional screen)

If a diagnostic session exists in the product, position it here.

**Headline:**
"Let's see where you are"

Not: "Take a test" or "Diagnostic assessment" — the word "test" creates anxiety.

**Subheadline:**
"5 questions. 5 minutes. We'll use your answers to personalise your practice so you're not wasting time on topics you already know."

**CTA:**
"Start the diagnostic"

**Skip option:**
"Skip — take me straight to practice"

Students who skip the diagnostic get a default starting topic. That's acceptable — the diagnostic is valuable but not required for activation.

---

#### Empty state — dashboard (no sessions yet)

When a student has registered but not yet started a session, the dashboard is empty. This is the highest-risk moment — it is where students bounce if the product doesn't make the next step obvious.

**Do:**

Main headline:
"Your first session is waiting."

Secondary text:
"Pick a topic and start practising. It takes 5 minutes to see your first results."

CTA button (large, prominent):
"Start practising — [topic from onboarding] →"

If topic is unknown (student skipped onboarding), use:
"Start practising — Cambridge 9709 Pure 1 →" (default to the most common exam board)

**Do not:**
- "You haven't started yet" — negative framing
- "Complete your profile" — admin-sounding
- "Explore our features" — vague
- "You have 0 sessions" — unhelpful data point

**Progress prompt (if using a Knowledge State visualisation):**
"Complete your first session to unlock your Knowledge State"

---

#### Empty state — topic map / Knowledge State (no data yet)

If the Knowledge State or topic map view has no data yet:

**Do not show:** an empty map or blank chart. This signals that the product is incomplete.

**Show instead:**
A greyed-out example Knowledge State with copy:
"Your Knowledge State builds as you practise. [Start a session →]"

---

#### First session prompt (top priority on all empty states)

On every empty state in the product during the first 7 days, the highest-priority call to action is always starting a practice session. Nothing competes with this in the empty state period.

---

### Step 3: In-app nudges (Day 0 to Day 7)

These are in-app notifications or banners, not emails. Refer to `/email-sequence` for the email equivalents.

**Day 0 (same day, no session started within 4 hours of signup):**
- Trigger: `trial_started` and no `session_started` within 4 hours
- Nudge: top-of-screen banner
- Copy: "Your first session is ready. Pick up where you left off — [topic] →"
- CTA: "Start practising"

**Day 1 (next day, no session started):**
- Trigger: 24 hours since `trial_started`, no `session_started`
- Nudge: in-app banner or modal on next visit
- Copy: "Start with just one topic. A 5-minute session is enough to see your first gap."
- CTA: "Start a 5-minute session"

**Day 3 (no second session):**
- Trigger: `first_session_completed` exists, no second `session_started` within 72 hours
- Nudge: in-app banner
- Copy: "Students who practise 3 times in their first week see the biggest improvement in their Knowledge State. [VERIFY — mark this as claim requiring data] You've done 1. Two to go."
- CTA: "Continue — [next topic] →"

**Day 7 (trial approaching end):**
- Trigger: 7 days before trial end (pull trial end date from user record)
- Nudge: prominent banner (not dismissible without action)
- Copy: "Your trial ends in [X] days. Here's what you've covered so far: [list of completed topics, if available]. Keep your progress — upgrade before [date]."
- CTA: "See plans →"
- Note: this nudge connects to `/paywall-upgrade-cro` — the banner click leads to the pricing page

---

### Copy principles for all onboarding copy

**Second person, direct:**
- "You", "Your", "You'll" — address the student, not "the user" or "students"

**Active voice:**
- "ExamPilot shows you your gaps" not "Your gaps are shown by ExamPilot"

**Specific over generic:**
- "Cambridge 9709 Pure 1 — Integration" not "your selected topic"
- "5 questions, 5 minutes" not "a quick session"

**Exam-calendar aware:**
- If the student's exam is fewer than 4 weeks away, urgency copy is appropriate:
  "You have 4 weeks. Let's focus on your weakest topics first."
- If the exam is more than 8 weeks away, urgency is not the right lever — use curiosity and progress framing instead

---

### Output format

```
Onboarding CRO: ExamPilot
---

Activation event: first_session_completed
Funnel sequence: [list the steps]

Screen designs:

  Welcome screen:
    Headline: [copy]
    Subheadline: [copy]
    CTA: [copy]
    Trust signal: [copy]

  Exam board selection:
    Headline: [copy]
    Options: [list]
    Reinforcement: [copy — with [VERIFY]]

  Empty state (dashboard):
    Headline: [copy]
    Secondary: [copy]
    CTA: [copy]

  Empty state (topic map):
    [copy]

In-app nudges:
  Day 0: [trigger] → [copy]
  Day 1: [trigger] → [copy]
  Day 3: [trigger] → [copy]
  Day 7: [trigger] → [copy]

[VERIFY] flags: [list all]
Priority fixes (if auditing existing flow):
  1. [highest impact change]
  2. [second highest]
  3. [third]

Next step: Review all copy. Pass to developer for implementation. Flag any [VERIFY] items before shipping.
```

## Guardrails

- Do not exploit exam anxiety in onboarding — urgency framing is only appropriate when the exam is genuinely close
- No fabricated social proof numbers — all outcome claims carry [VERIFY]
- Under-18 users: in-app nudges do not require PECR consent (they are product communications, not marketing), but do not use them to push marketing content without consent
- All copy in UK English: "practise" (verb), "practice" (noun)
- No confetti, celebration animations, or "Congratulations!" on activation — students want to study, not be entertained

## What this skill does NOT do

- Does not design the pre-registration or registration flow. Use `/signup-flow-cro` for that.
- Does not write email sequences. Use `/email-sequence` for day-7+ email nurture.
- Does not design the paywall or upgrade prompt. Use `/paywall-upgrade-cro` for that.
- Does not implement anything. Recommendations only — developer implements.
- Does not auto-save output. Present inline; save only on user instruction.
