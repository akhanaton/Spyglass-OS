---
name: form-cro
description: Optimise ExamPilot's forms — signup, login, upgrade, and any data collection form. Reduces abandonment, applies progressive disclosure, and writes field labels and error messages that keep students moving forward.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.
  The Three Ms of AI™ is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.*

## What this skill does

Audits and writes copy for ExamPilot's forms: the registration form, upgrade/payment form, onboarding question screens, and any lead capture or waitlist forms. Reduces abandonment by applying progressive disclosure, fixing field labels and error messages, and removing unnecessary friction.

**Bike Method Phase 1:** This skill produces copy and UX recommendations. All copy is marked [VERIFY before shipping]. No code, no auto-save.

## When `/form-cro` runs

- "Audit the signup form"
- "The registration form has too many fields — what do we cut?"
- "Write the field labels and error messages for the registration form"
- "Design the onboarding questions"
- "What should the upgrade form say?"
- Any form in the product that has friction, abandonment, or unclear copy

## Context files — read at session start

```bash
cat references/voice-house.md
cat marketing/context/audience-segments.md
```

---

## ExamPilot form inventory

Known forms (update as product evolves):
- **Registration form:** email + password (minimum viable)
- **Onboarding questions:** exam board, paper code, exam proximity (max 3 questions)
- **Upgrade / payment form:** handled by Dodo Payments — ExamPilot controls the page copy surrounding it, not the payment fields themselves
- **Waitlist / lead capture:** email only (if applicable pre-launch)

---

## Mode 1: Audit an existing form

Trigger: "audit the [form name]", "what's wrong with the registration form"

### Step 1: Get form details

Ask the user to describe the form: field names, labels, placeholder text, button copy, error messages, and any trust signals near the form. Accept a screenshot description if no code is available.

### Step 2: Apply the 5 friction point framework

Score each friction point 0-10. Total score out of 50. Higher = less friction (better).

---

**Friction point 1: Field count (0-10)**

Rule: each extra field beyond the minimum costs approximately 5-10% completion rate.

Targets by form type:
- Registration: 2 fields maximum (email + password). Name, phone, school = friction, remove.
- Onboarding questions: 3 questions maximum; all skippable except exam board selection.
- Waitlist/lead capture: 1 field (email only). No name required.
- Upgrade: payment fields are Dodo Payments — ExamPilot does not control these. Note any pre-payment fields ExamPilot adds and flag extras.

Score: 10 = at or below target field count. Deduct 2 per extra field above target.

---

**Friction point 2: Field labels and placeholders (0-10)**

Rules:
- Labels sit above the field, not inside it. Inside labels (placeholder-as-label) disappear on focus — accessibility failure and UX failure simultaneously.
- Placeholder text: example values only ("e.g. your.name@gmail.com") — not instructions, not repeated label text.
- Field names: use the student's language.
  - "Your email" not "Email address"
  - "Choose a password" not "Password"
  - "Which exam are you preparing for?" not "Select exam board"
- Never use "Username" — students do not think in usernames.

Score: 10 = all labels above-field, placeholders are examples, student-language names. Deduct 2 per violation.

---

**Friction point 3: Error messages (0-10)**

Rules:
- Validation: inline and immediate (as the student leaves each field — not wait-until-submit).
- Error copy: specific + actionable.
  - "Password must be at least 8 characters" not "Invalid password"
  - "That email is already registered. [Sign in →]" not "Email already exists"
  - "Check your email format — try name@example.com" not "Invalid email"
- Tone: helpful not punitive.
  - "Let's fix that — " as a prefix is acceptable if it fits the voice
  - Never: "Error:", "Failed:", "Invalid" as standalone words
- Never clear the form on error. Preserve all previously entered values.
- Never redirect to a new page on error. Inline error states only.

Score: 10 = specific, actionable, inline, form preserved. Deduct 2-3 per violation.

---

**Friction point 4: CTA button (0-10)**

Rules:
- Button copy: specific to what happens next.
  - "Create my account" not "Submit"
  - "Start my free trial" not "Sign Up"
  - "Continue to practice" not "Next"
- Loading state: show progress after click.
  - "Creating your account..." (spinner + message)
  - Never: button goes inactive with no feedback (student thinks it didn't work and clicks again)
- Success state: immediate positive feedback before redirect.
  - "Account created. Setting up your practice..." (1-2 seconds, then redirect)
  - Not: silent redirect with no acknowledgment

Score: 10 = specific copy, loading state present, success feedback present. Deduct 2-3 per gap.

---

**Friction point 5: Trust signals on the form page (0-10)**

Required trust signals near ExamPilot's forms:

Near the registration form submit button:
- "No credit card required" (for trial)
- "Free [X]-day trial — cancel any time"
- Privacy assurance: "We'll never share your email" (GDPR signal for under-18 parents)

Near the upgrade form:
- "Secure payment via [Dodo Payments / payment processor name]" [VERIFY processor name]
- "Cancel any time — no lock-in"

Across all forms:
- GDPR consent line below the submit button: "By continuing, you agree to ExamPilot's [Terms of Service] and [Privacy Policy]." (small text, never hidden)

Score: 10 = all required trust signals present and positioned near the CTA. Deduct 2 per missing signal.

---

### Step 3: Score and top 3 fixes

Total score out of 50.

Verdict:
- 42-50: PASS — minor polish only
- 30-41: NEEDS WORK — address priority friction points
- 0-29: BLOCKED — significant rework needed

**Top 3 fixes:** ranked by estimated abandonment reduction impact. For each:
- Friction point affected
- Specific change
- Before copy → After copy
- Rationale

---

## Mode 2: Write form copy

Trigger: "write the copy for the [form type]", "give me the labels and error messages for registration"

Given: form type + list of required fields.

Produce the following for each field:
- Field label text (above the field)
- Placeholder text (example value)
- Validation error message (specific and actionable)

Plus:
- Page headline above the form (outcome-focused: "Start your free trial" not "Register")
- Subheadline (optional — 1 sentence, names the exam board if known)
- CTA button copy
- Loading state copy
- Success state copy (shown briefly before redirect)
- GDPR consent line (required)
- Trust signal lines near the CTA (2-3)

---

## Mode 3: Onboarding question design

Trigger: "design the onboarding questions", "what should we ask new students"

ExamPilot's post-registration onboarding: 3 questions maximum.

Frame each question as personalisation — "so we can personalise your practice" — not data collection.

---

**Question 1 (required): Exam board selection**

Page headline: "Which exam are you preparing for?"

Options:
- Cambridge International AS & A Level Mathematics (9709)
- Edexcel International Advanced Level Mathematics (IAL)
- Other A-Level Maths

If Cambridge is selected: show paper options immediately on the same screen (not a new page):
- Pure Mathematics 1 (Paper 1)
- Pure Mathematics 3 (Paper 3)
- Statistics 1 (Paper 5)
- Mechanics 1 (Paper 4)

If Edexcel is selected: show equivalent Edexcel IAL papers [VERIFY exact Edexcel IAL paper names and codes].

Immediate reinforcement after selection:
"ExamPilot has [N] practice questions mapped to [selected exam]. We'll start there." [VERIFY question count]

Skip option: no skip for this question — exam board is required to personalise the experience.

---

**Question 2 (optional): Paper focus**

Shown only if exam board has multiple papers (conditional on Question 1).

Page headline: "Which paper are you focusing on first?"

Skip link copy: "Not sure yet — show me everything"

When student skips: default to the first paper in their exam board sequence.

---

**Question 3 (optional): Exam proximity**

Page headline: "How long until your exam?"

Options:
- Less than 4 weeks
- 1-3 months
- Just exploring for now

Purpose: adjusts urgency framing and recommended starting pace in the product.
Skip link copy: "I'll set this later"

---

**Progress indicator copy:**

If showing step count: "Step [N] of 3 — takes 30 seconds"
Do not use a progress bar that looks like a long journey. A simple step count is sufficient.

---

### Output format

```
Form CRO: [Form name]
---

[Mode 1 — Audit]
Friction point scores:
  Field count:             [score]/10
  Labels and placeholders: [score]/10
  Error messages:          [score]/10
  CTA button:              [score]/10
  Trust signals:           [score]/10
  TOTAL:                   [score]/50

Verdict: PASS | NEEDS WORK | BLOCKED

Top 3 fixes:
  1. [friction point] — Before: "[copy]" → After: "[copy]" — [rationale]
  2. [friction point] — Before: "[copy]" → After: "[copy]" — [rationale]
  3. [friction point] — [rationale]

[Mode 2 — Write form copy]
Page headline: [copy]
Subheadline: [copy] (if applicable)

Fields:
  [Field name]:
    Label: [copy]
    Placeholder: [copy]
    Error message: [copy]

CTA button: [copy]
Loading state: [copy]
Success state: [copy]
GDPR line: [copy]
Trust signals: [list]

[Mode 3 — Onboarding questions]
Q1: [question copy + options + reinforcement + skip rules]
Q2: [question copy + options + skip copy]
Q3: [question copy + options + skip copy]
Progress indicator: [copy]

[VERIFY] flags: [list all]
Next step: Review copy. Pass to developer. Resolve [VERIFY] items before shipping.
```

---

## Guardrails

- GDPR/PECR compliance for under-18 users: no marketing opt-in checkbox pre-ticked, no optional fields that harvest data unnecessarily
- Password fields: do not show a password strength meter that delays submission — show strength feedback only after the first failed attempt or on a second visit
- Email fields: auto-lowercase and trim whitespace on input (note for developer)
- Do not collect data you do not use in the product (name, phone, school are all unnecessary for ExamPilot's core function)
- All copy in UK English: "practise" (verb), "practice" (noun), "personalise", "optimise"

## What this skill does NOT do

- Does not audit popups, modals, or banners. Use `/popup-cro` for that.
- Does not audit full landing pages or product pages. Use `/page-cro` for that.
- Does not configure Dodo Payments or payment form fields — those are controlled by the payment processor.
- Does not write email sequences triggered after form submission. Use `/email-sequence` for that.
- Does not implement anything. Recommendations only.
- Does not auto-save output. Present inline; save only on user instruction.
