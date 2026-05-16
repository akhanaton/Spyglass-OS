---
name: popup-cro
description: Write and optimise popups and modal copy for ExamPilot — trial expiry notices, feature gate modals, exit intent, and in-app nudges. Applies natural urgency (exam calendar) without dark patterns. Maximises dismissal-to-action rate.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.
  The Three Ms of AI™ is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.*

## What this skill does

Writes and audits copy for ExamPilot's popups, modals, and in-app banners. Covers trial expiry modals, feature gate modals, exit intent overlays, in-app nudges, and upgrade confirmation modals. Uses natural urgency from the exam calendar — no manufactured scarcity or dark patterns.

**Primary metric:** dismissal-to-action rate — the percentage of students who see the popup and take the primary action rather than dismissing it.

**Bike Method Phase 1:** This skill produces copy and UX recommendations only. All copy is marked [VERIFY before shipping]. No code, no auto-save.

## When `/popup-cro` runs

- "Write the trial expiry modal"
- "What should the feature gate say?"
- "Draft the exit intent popup for the pricing page"
- "What copy should the in-app nudge use when a student is inactive?"
- "Audit our current modal copy"
- Building the full popup system from scratch (pre-launch)

## Context files — read at session start

```bash
cat references/voice-house.md
cat marketing/context/audience-segments.md
cat marketing/gtm-engineering/signal-registry.md
```

---

## ExamPilot popup scenarios

Known popup types (update as product evolves):

1. Trial expiry modal — 7 days before
2. Trial expiry modal — 3 days before
3. Trial expiry modal — day of expiry
4. Feature gate modal (locked feature)
5. Exit intent overlay (pricing page only)
6. In-app nudge banner (inactive 3+ days)
7. Upgrade confirmation modal

---

## Popup anatomy — required elements for every popup

Every popup ExamPilot shows must include:

- **Headline:** ≤ 60 characters. States the situation or benefit directly.
- **Body:** ≤ 40 words. Popups get read in 2-3 seconds or not at all.
- **Primary CTA:** verb + benefit. Not just a verb.
- **Secondary action (dismiss):** always present — every popup must have an out.
- **Trigger condition:** exact rule for when this fires.
- **Frequency cap:** how often it can show per user. Mandatory — no cap = trust destruction.

---

## Popup specifications

### 1. Trial expiry modal — 7 days before

**Trigger:** 7 days before trial end date (pull from user record)
**Type:** full modal (blocking)
**Frequency cap:** once per user per trial period

**Headline:** "Your trial ends in 7 days"

**Body:** "You've completed [X] practice sessions. Keep your progress and your results." (personalised via PostHog if `identify()` is live [VERIFY PostHog identify() status — EP-42])

If personalisation is not yet live, fallback body: "Keep your practice history and your Knowledge State. Upgrade before your trial ends."

**Primary CTA:** "Continue for €12/mo →"
- Uses annual plan pricing (€144/yr ÷ 12) — lowest anchoring
- [VERIFY: confirm annual plan monthly equivalent is €12]

**Secondary action:** "Remind me in 3 days"
- This sets a flag to show the 3-day modal instead of the day-of modal next
- Copy: "Remind me in 3 days" — not "Dismiss" or "No thanks"

---

### 2. Trial expiry modal — 3 days before

**Trigger:** 3 days before trial end date, OR triggered by "Remind me in 3 days" from the 7-day modal
**Type:** full modal (blocking)
**Frequency cap:** once per user per trial period

**Headline:** "3 days left on your trial"

**Body:** "Your practice history and Knowledge State will be paused when your trial ends. Upgrade to keep going."

**Primary CTA:** "Upgrade now — from €12/mo"

**Secondary action:** "I'll decide before it ends"

---

### 3. Trial expiry modal — day of expiry

**Trigger:** trial end date (show on first app open on the expiry day)
**Type:** full modal (blocking — student must take one of the two actions to proceed)
**Frequency cap:** once per expiry event

**Headline:** "Your trial ends today"

**Body:** "Don't lose your practice history. Upgrade to keep going." (30 words max — this modal gets skimmed fastest)

**Primary CTA:** "Upgrade now — from €12/mo"

**Secondary action:** "I'll lose my progress"
- This is a friction label on the dismiss action — it describes what happens, not a guilt trip
- It must be accurate: the student's progress IS paused (confirm whether it is deleted or paused [VERIFY])
- If progress is retained for a grace period, change to: "Pause my account"
- If progress is deleted immediately, this label is factually correct and fair — not manipulative

**Note:** do not add countdown timers to this modal. The trial end date is already shown in the headline.

---

### 4. Feature gate modal

**Trigger:** student clicks or taps a locked feature (a feature that requires a paid plan)
**Type:** modal (blocking click action, but student can dismiss)
**Frequency cap:** once per session per feature — do not re-show the same feature gate modal during the same session

**Headline:** "[Feature Name] is available on paid plans"

Replace [Feature Name] with the exact feature the student tried to access. Never use a generic headline.

Examples:
- "Full Knowledge State is available on paid plans"
- "Unlimited practice sessions are available on paid plans"
- "Practice history is available on paid plans"

**Body:** "Unlock [specific benefit relevant to this feature] and keep building towards your exam."

Keep under 20 words. Name the benefit, not the feature.

Examples:
- "See every gap in your revision and fix them before your exam."
- "Practise as many sessions as you need — no limits until your exam."

**Primary CTA:** "Upgrade — from €12/mo"

**Secondary action:** "Maybe later"

**Design note:** the secondary action "Maybe later" should not be styled as a link that looks like it disappears. It must be clearly visible. Students who are not ready to upgrade should be able to dismiss without frustration.

---

### 5. Exit intent overlay — pricing page only

**Trigger:** mouse moves toward browser tab bar or close button on the pricing page (desktop only — no exit intent on mobile)
**Type:** overlay (full-screen or large modal)
**Frequency cap:** once per session, once per 30 days per user
**Use sparingly:** this is the highest-friction popup type. Only on the pricing page. Never on the homepage, hub pages, or blog.

**Headline:** "Before you go — your exam is [X weeks] away"

Pull exam proximity from user onboarding data if available. If not available, use: "Before you go — revision season has started"

**Body:** "Students who start structured practice now build compound knowledge before their exam." [VERIFY — do not claim a specific percentage improvement without data]

**Primary CTA:** "Start my free trial"

**Secondary action:** "I'll come back later"

**Design notes:**
- Does not trigger on mobile (Google penalises full-screen popups on mobile for SEO)
- Does not trigger on auth pages (login, register)
- Requires a clear X button in the top corner regardless of secondary action text

---

### 6. In-app nudge — inactive 3+ days

**Trigger:** student opens the app after 3 or more days with no `session_started` event
**Type:** banner or toast — NOT a blocking modal. This nudge must not interrupt the student who is returning to use the product.
**Frequency cap:** once per re-engagement event (do not show again until they are inactive for another 3 days)

**Copy:** "Welcome back. You left off on [last topic]. Pick up where you were?"

If last topic is not available: "Welcome back. Your practice is ready — start where you left off?"

**CTA:** "Continue →" (link or button that goes directly to the last session topic or the dashboard)

**Dismiss:** X button only. No text label needed on the dismiss for this nudge — it is a low-stakes banner, not a conversion modal.

**Design notes:**
- Appears at the top of the screen (not a bottom sheet or pop-in — those interrupt content)
- Disappears on dismiss and does not return during the same session
- Does not display on the login or register pages

---

### 7. Upgrade confirmation modal

**Trigger:** student completes the Dodo Payments upgrade flow and is redirected back to ExamPilot
**Type:** celebratory modal (non-blocking — student can dismiss immediately)
**Frequency cap:** once per upgrade event

**Headline:** "You're in. Welcome to ExamPilot."

**Body:** "Your full access starts now. Let's get back to where you were."

**Primary CTA:** "Continue practising →"

**Secondary action:** none — the student has already converted. Do not add upsell or cross-sell here.

**Design notes:**
- Do not use "Congratulations!" — students are here to study, not to celebrate
- Do not show pricing again — the student has just paid
- Redirect should go back to the last topic or the dashboard, not to the homepage

---

## Audit mode — reviewing existing popup copy

If auditing an existing popup, apply these criteria for each popup:

1. **Headline ≤ 60 chars?** State actual char count.
2. **Body ≤ 40 words?** State actual word count.
3. **Primary CTA specific?** Does it name the action and the benefit?
4. **Dismiss option present?** Is it clearly visible (not hidden or grey-on-grey)?
5. **Trigger appropriate?** Does the popup fire at the right moment?
6. **Frequency cap set?** What is the cap? Is it documented anywhere?
7. **Dark patterns present?** Fake countdown timers, pre-ticked checkboxes, manipulative dismiss labels? Flag each.
8. **Mobile safe?** Would this popup cover the full mobile screen? Flag if yes.

Score each 0-1. Total out of 8. 7-8 = strong, 5-6 = needs work, 0-4 = blocked.

---

## Output format

```
Popup CRO: [popup name / scenario]
---

[For each popup specified or audited]

[Popup name]:
  Trigger: [exact trigger condition]
  Type: [blocking modal | banner | toast | overlay]
  Frequency cap: [rule]

  Headline: [copy] ([char count])
  Body: [copy] ([word count])
  Primary CTA: [copy]
  Secondary action: [copy]
  Design notes: [any implementation flags]

  [VERIFY] flags: [list]

[Audit mode only]
Audit scores:
  Headline length:    [0-1]
  Body length:        [0-1]
  CTA specificity:    [0-1]
  Dismiss present:    [0-1]
  Trigger timing:     [0-1]
  Frequency cap:      [0-1]
  No dark patterns:   [0-1]
  Mobile safe:        [0-1]
  TOTAL:              [score]/8

Verdict: STRONG | NEEDS WORK | BLOCKED

Top fixes:
  1. [element] — Before: "[copy]" → After: "[copy]"
  2. [element] — [recommendation]

Next step: Review copy. Pass to developer with trigger conditions and frequency cap rules. Resolve [VERIFY] flags before shipping.
```

---

## Guardrails

- Every popup must have a clear, low-friction dismiss option — no exceptions
- No fake countdown timers (timers not tied to a real event are dark patterns)
- No "Are you sure you want to leave?" browser dialogs
- No full-screen popups on mobile (Google penalises these; they also violate basic UX for students using their phone)
- No popups on auth pages (login, register, password reset)
- Frequency caps are mandatory — every popup specification must include one
- Dismiss labels: must be honest (can be friction-inducing if accurate, not if misleading)
- Under-18 users: no popups that exploit exam anxiety — urgency framing is appropriate only when the exam is genuinely close and the claim is accurate
- EUR pricing only in all copy (€12/mo annual equivalent, €29/mo monthly)
- All copy in UK English: "practise" (verb), "practice" (noun)

## What this skill does NOT do

- Does not design in-app email notifications or push notifications. Use `/email-sequence` for email and document push notification copy separately.
- Does not design the paywall page itself. Use `/paywall-upgrade-cro` for that.
- Does not implement anything — trigger conditions and frequency caps must be implemented by the developer.
- Does not auto-save output. Present inline; save only on user instruction.
