---
name: signup-flow-cro
description: Optimise ExamPilot's trial signup flow — from landing page CTA click to first practice session. Reduces friction, improves activation rate, and designs the micro-commitments that move students from visitor to paying subscriber.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.
  The Three Ms of AI™ is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.*

## What this skill does

Audits and redesigns ExamPilot's trial signup flow from the moment a visitor clicks a CTA to the moment they complete their first practice session. The activation metric that matters is not "registered" — it is "first session completed". Everything in the signup flow funnels toward that event.

**Bike Method Phase 1:** This skill produces copy and UX recommendations. All copy is marked [VERIFY before shipping]. Developer and designer review before any changes ship.

## When `/signup-flow-cro` runs

- "Audit my signup flow"
- "Why are people dropping off at registration?"
- "Improve the onboarding / sign up experience"
- "How do I increase trial-to-first-session rate?"
- Pre-launch: designing the signup flow for the first time
- Post-launch: when PostHog shows a drop-off between `trial_started` and `first_session_completed`

## Context files — read at session start

```bash
cat references/voice-house.md
cat marketing/context/audience-segments.md
cat marketing/context/funnel-strategy.md
```

## Execution — three steps

### Step 1: Map the current flow

Ask the user to describe the current signup steps, or provide a PostHog funnel screenshot. If neither is available, use the expected default flow:

```
1. Landing page (hero CTA)
2. Register page (email + password)
3. Onboarding (exam board selection, paper code)
4. Dashboard / first session prompt
```

Map each step to the PostHog event that tracks it:
- Step 1 → `cta_clicked`
- Step 2 → `trial_started`
- Step 3 → `onboarding_completed`
- Step 4 → `session_started` → `first_session_completed`

For each step, ask: what is the drop-off rate? (Pull from PostHog if available.) The highest drop-off step is the priority fix.

---

### Step 2: Apply 5 friction reduction principles

Work through each principle. For each one, state whether it is currently applied, partially applied, or missing — then give the recommendation.

---

#### Principle 1: Progressive disclosure

**Rule:** Only ask for the minimum information at each step. Collect additional data after trust is established.

**Step 1 (Registration) — collect:**
- Email address
- Password

**Do NOT collect at registration:**
- Full name (not needed for the product)
- Phone number
- School name
- Year group

**Steps 2+ (Onboarding) — collect after registration:**
- Exam board (Cambridge / Edexcel)
- Paper code (9709 Pure 1 / WMA11 / etc.)
- How long until the exam (optional)

**If more than two fields on the registration form:** flag it as friction and recommend removing.

**GDPR note:** Only collect data that is necessary for the service. Under-18 users — no field should be optional-but-harvested. Minimum data = minimum risk.

---

#### Principle 2: Social sign-in (Google OAuth)

**Why:** 16-18 year olds all have Google accounts (school or personal). Google sign-in eliminates the password creation step — the single highest drop-off point in registration.

**Recommendation:**
- Primary CTA: "Continue with Google" (above the email/password form)
- Secondary option: email + password (for users without Google accounts)
- Do not make email/password the primary path

**If Google OAuth is not implemented:** flag as the highest-leverage friction reduction. Estimated impact: significant reduction in registration drop-off [VERIFY with PostHog data post-implementation].

---

#### Principle 3: Instant value before registration (optional)

**Question to ask:** Can the student see any value before they register?

**Options (pick one, if feasible):**
- Show a sample practice question on the landing page (interactive, no account needed)
- Show a demo of the Knowledge State visualisation
- Offer a free tool (see `/free-tool-strategy`) that works without signing up

**If instant pre-registration value is available:**
- Move the register prompt to appear AFTER the student has seen value
- The register CTA becomes: "Save your progress and see your full Knowledge State →"
- This converts the register friction from "give us your email to start" to "give us your email to keep what you've built"

**If not feasible yet:** note it as a future lever. Do not block progress on this.

---

#### Principle 4: Onboarding questions = personalisation, not admin

**Rule:** Every question in onboarding must be framed as "so we can personalise your practice" — not as data collection for ExamPilot's benefit.

**Good framing:**
- "Which exam are you preparing for?" (not "Select your exam board")
- "Which paper are you focusing on?" (not "Select paper code")
- "When's your exam?" (not "Enter exam date")

**Maximum 3 questions in onboarding.** If more are needed, add them progressively as the student uses the product.

**Skip option:** every question except exam board selection should have a skip option. Students who skip get a default experience; ExamPilot fills in the gaps from their session behaviour.

**Immediate reinforcement after each answer:**
- After exam board selection: "Great — ExamPilot has [N] practice questions mapped to Cambridge 9709." [VERIFY exact count]
- After paper selection: "You've chosen Pure 1. We'll start with [first topic]."

---

#### Principle 5: First session as the activation gate

**The activation event is not registration. It is `first_session_completed`.**

Every element in the signup flow must point toward starting that first session.

**Landing page CTA:** "Start Practising Free" — not "Sign Up" or "Get Started"

**Post-registration redirect:** Do not drop the student on a generic dashboard. Redirect them immediately to the onboarding flow, which ends with starting their first session.

**Final onboarding CTA:** "Start your first session on [paper they selected] →"

**If the student has selected a topic:** pre-fill the session with that topic. Do not make them navigate to find it.

**Activation metric to track:**
```
trial_started → first_session_completed
```
Target: >50% of registered users complete a first session within 24 hours [VERIFY with product data post-launch].

---

### Step 3: Copy and voice review

For any page in the signup flow that has existing copy, apply the voice check from `references/voice-house.md`:

**Registration page:**
- Headline options:
  - "Start practising in 30 seconds"
  - "Your Cambridge 9709 revision starts here"
  - "Join free — no card needed"
- Subheadline: name the exam board if known from UTM or referrer context
- Form label: "Your email" not "Email address"
- Submit button: "Create my account" or "Start for free" — not "Submit" or "Sign Up"
- Below the button: "Free trial. No credit card required." — one line, no period at the end

**Error states:**
- Email already registered: "Looks like you already have an account. [Sign in →]" — not "Error: email exists"
- Password too short: "Password needs at least 8 characters" — direct, no blame

**Privacy line (required — GDPR):**
Below the submit button, in small text:
"By continuing, you agree to ExamPilot's [Terms of Service] and [Privacy Policy]. We won't share your email."

**Trust signals to add near the registration form:**
- "Free [X]-day trial — cancel any time"
- "Built for Cambridge 9709 and Edexcel IAL"
- One specific social proof line — use [VERIFY] if numbers are unconfirmed

---

### Output format

```
Signup Flow CRO Audit
---

Current flow mapped:
  [Step 1] → [event] — drop-off: [% if known | unknown]
  [Step 2] → [event] — drop-off: [% if known | unknown]
  [Step N] → [event] — drop-off: [% if known | unknown]

Priority friction points (highest to lowest drop-off):
  1. [Step] — [friction identified] — [recommendation]
  2. [Step] — [friction identified] — [recommendation]
  3. [Step] — [friction identified] — [recommendation]

Friction principles applied:
  1. Progressive disclosure: [Applied | Partially applied | Missing] — [recommendation]
  2. Social sign-in: [Applied | Missing] — [recommendation]
  3. Instant value: [Applied | Not feasible yet | Missing] — [recommendation]
  4. Onboarding framing: [Applied | Partially applied | Missing] — [recommendation]
  5. Activation gate: [Applied | Missing] — [recommendation]

Copy recommendations:
  Registration page:
    Headline: [recommended copy]
    CTA button: [recommended copy]
    Privacy line: [required GDPR text]

  [Additional pages if applicable]

[VERIFY] flags: [list all]
Next step: Review recommendations. Prioritise by drop-off rate. Hand copy to developer for implementation.
```

## Guardrails

- No dark patterns: no pre-checked marketing opt-in boxes, no misleading free trial terms
- GDPR compliance: minimum data collection, clear consent for under-18 users
- Under-18: parental consent mechanism for marketing communications — confirm with Enitan that this is in place at signup [VERIFY]
- No fabricated social proof on the registration page — use [VERIFY] on all numbers
- All copy in UK English: "practise" (verb), "practice" (noun), "colour", "optimise"

## What this skill does NOT do

- Does not design the post-first-session product experience. Use `/onboarding-cro` for in-product onboarding.
- Does not implement feature flags for A/B testing the signup flow. Use `/ab-test-setup` for that.
- Does not audit the paywall or upgrade flow. Use `/paywall-upgrade-cro` for that.
- Does not write email sequences triggered after signup. Use `/email-sequence` for that.
- Does not auto-save recommendations to a file. Present inline; save only on user instruction.
