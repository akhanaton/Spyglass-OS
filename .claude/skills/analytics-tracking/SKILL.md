---
name: analytics-tracking
description: Design and implement PostHog event taxonomy, fix the identify() gap, add UTM capture, and audit ExamPilot's analytics coverage. Directly addresses EP-42 (identify) and EP-43 (event gaps) from the analytics audit. Primary tool is PostHog — GA4 is pageview-only on marketing routes.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.
  The Three Ms of AI™ is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.*

## What this skill does

Designs, audits, and implements ExamPilot's analytics event taxonomy. The primary analytics tool is PostHog — all product events, session recording, and GTM signal scoring run through it. GA4 is pageview-only on 7 marketing and Cambridge/waitlist routes. This skill directly addresses EP-42 (missing `posthog.identify()`) and EP-43 (funnel event gaps) from the analytics audit.

**Current stack:**
- PostHog: 15 custom events in `exampilot/lib/utils/analytics.ts`. No `posthog.identify()` — all users are anonymous. No UTM capture. No backend events. Masked session recording.
- GA4: pageview-only on 7 marketing/Cambridge/waitlist routes. No custom events.
- Clarity: session recording — unmasked on login/register routes (privacy concern).
- Vercel Analytics: Core Web Vitals only.

**Bike Method Phase 1:** All implementation code requires developer review before shipping. This skill produces specs and code patterns — the developer implements and verifies.

## When `/analytics-tracking` runs

- "Audit my analytics" or "what events am I missing"
- "Design an event for X"
- "Implement identify" or "fix the anonymous user problem"
- "Add UTM tracking" or "track where signups come from"
- Before a GTM Engineering signal-review cycle (GTM scoring requires `identify()` to work)

## Context files — read at session start

```bash
cat marketing/context/funnel-strategy.md
cat marketing/gtm-engineering/signal-registry.md
```

## Execution — four modes

Identify the mode from the user's request, then run the correct module below.

---

### Mode 1: Audit mode

Trigger: "audit my analytics", "what events am I missing", "check my tracking coverage"

**Step 1 — Map current events against the funnel**

Read `marketing/context/funnel-strategy.md` for funnel stages. Ask the user to paste their current `analytics.ts` event list, or read it if a file path is provided.

Map each existing event to a funnel stage:

| Funnel stage | Transition | Event needed | Status |
|---|---|---|---|
| Awareness → Consideration | Landing page visit | GA4 pageview (automatic) | Likely covered |
| Consideration → Activation | CTA click | `cta_clicked` | [VERIFY] |
| Activation → Trial | Register | `trial_started` | Check |
| Trial → First session | Session started | `session_started` | Check |
| First session → Engaged | Session completed | `session_completed` | Check |
| Engaged → Upgrade intent | Upgrade prompt viewed | `upgrade_viewed` | Likely missing |
| Upgrade intent → Paid | Subscription upgraded | `subscription_upgraded` | Likely missing |
| Paid → Retained | Subscription renewed | `subscription_renewed` | Backend — likely missing |
| Paid → Churned | Subscription cancelled | `subscription_cancelled` | Backend — likely missing |

**Step 2 — Produce the gap list**

Priority 1 — Critical (EP-42): `posthog.identify()` is absent. All users are anonymous. GTM signal scoring cannot work without user identity. Fix this before anything else.

Priority 2 — High (EP-43 funnel gaps):
- UTM capture on first visit (`utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`)
- `trial_started` — when a user completes registration
- `subscription_upgraded` — when a user converts from trial/free to paid
- `subscription_cancelled` — when a user cancels

Priority 3 — Medium:
- `onboarding_completed` — when the user finishes onboarding steps
- `first_session_completed` — activation milestone
- Backend events via PostHog Python SDK: `answer_submitted`, `session_completed` server-side (server-side events are more reliable than client-side for completion events)

Priority 4 — Low:
- `upgrade_viewed` — when the upgrade prompt is displayed
- `free_tool_used` — for any future free tool (see `/free-tool-strategy`)
- `free_tool_cta_clicked` — conversion from free tool to trial

**Privacy flags to surface in every audit:**
- Clarity is running unmasked on auth routes (login/register). This is a PRIVACY CONCERN — session recording that captures passwords or personal data violates GDPR. Flag for immediate masking.
- Confirm PostHog session recording is masked on auth routes.
- Confirm no email addresses are used as PostHog distinct IDs.

Output format:
```
Analytics Audit: ExamPilot
Date: [today]

Current event count: [N]
Funnel stages covered: [N of 9]
Funnel stages with gaps: [list]

Critical gaps (fix first):
  - EP-42: posthog.identify() missing — GTM scoring non-functional until fixed

High-priority gaps:
  - [list]

Medium-priority gaps:
  - [list]

Privacy flags:
  - [list any concerns]

Recommended next step: Run /analytics-tracking in Mode 3 to implement identify().
```

---

### Mode 2: Design mode

Trigger: "design an event for X", "what should I track when Y", "how do I name this event"

**Event naming convention:**

`noun_verb` in snake_case. The noun is the object being acted on. The verb is the action.

Examples: `session_started`, `answer_submitted`, `upgrade_clicked`, `knowledge_state_viewed`, `topic_selected`

Not: `startSession`, `userClickedUpgrade`, `sessionStart`

**For each event, produce this spec:**

```
Event: [event_name]
Trigger: [Exact moment this fires — be specific. "When the user clicks X" not "when the user upgrades"]
Properties:
  - exam_board: "cambridge" | "edexcel" (always include where relevant)
  - paper_code: "9709" | "WMA11" (always include where relevant)
  - [other properties specific to this event]
Implementation:
  - File: [which file or component — e.g. app/practice/page.tsx]
  - Side: client | server
  - Tool: PostHog (product events) | GA4 (do not add custom GA4 events — pageviews only)
  - Code: [TypeScript snippet]
```

**PostHog vs GA4 decision rule:**
- PostHog: all product events, conversion events, user behaviour
- GA4: do NOT add custom events — GA4 receives only automatic pageviews from the Next.js marketing routes. Adding custom GA4 events creates split-brain analytics.

---

### Mode 3: identify() implementation

Trigger: "implement identify", "fix the anonymous user problem", "set up PostHog identity"

**The problem:** Without `posthog.identify()`, every user is anonymous in PostHog. The GTM signal scoring model in `marketing/gtm-engineering/scoring-model.md` cannot assign signals to users. Cohort analysis is impossible. Funnel drop-off analysis is unreliable.

**The fix:**

Call `posthog.identify()` in the auth callback or session provider, immediately after the user is confirmed as authenticated.

**File location:** Likely `app/providers.tsx`, `app/auth/callback/route.ts`, or the NextAuth session callback. Ask the developer to confirm.

**Implementation pattern:**

```typescript
// After confirming the user is authenticated
// Use internal user ID — NOT email (GDPR: email is personal data)
const userId = session.user.id // internal DB ID, e.g. "usr_abc123"

posthog.identify(userId, {
  // Person properties — persisted on the PostHog person profile
  plan: user.plan, // "free" | "trial" | "monthly" | "quarterly" | "semi_annual" | "annual"
  exam_board: user.examBoard, // "cambridge" | "edexcel"
  paper_code: user.paperCode, // "9709" | "WMA11"
  account_created_at: user.createdAt, // ISO 8601 string
})

// Also set person properties explicitly for GTM scoring
posthog.setPersonProperties({
  plan: user.plan,
  exam_board: user.examBoard,
  paper_code: user.paperCode,
})
```

**Where to call it:**
- On every session load where the user is authenticated (not just on first login)
- In the NextAuth `session` callback or equivalent
- After `posthog.reset()` on logout

**On logout:**
```typescript
posthog.reset() // clears the identified user, resets to anonymous
```

**Distinct ID rules:**
- Use the internal user ID (database UUID or similar opaque ID)
- Never use email — it is personal data under GDPR
- Never use name, phone number, or any PII as the distinct ID

**[VERIFY] before implementing:**
- Confirm which file handles session state in the Next.js app
- Confirm the shape of `user` object available in that context
- Confirm the plan values match exactly what's stored in the database

---

### Mode 4: UTM capture

Trigger: "add UTM tracking", "track where signups come from", "capture campaign parameters"

**The problem:** Without UTM capture, ExamPilot cannot attribute trial signups or upgrades to the marketing channel that drove them. Reddit posts, email campaigns, and any future paid activity are invisible in the funnel.

**The approach:**
1. On first page load, read UTM parameters from the URL
2. Store them in `localStorage` (persists through the session and across pages)
3. Attach the stored UTMs to conversion events: `trial_started`, `subscription_upgraded`

**Implementation pattern:**

```typescript
// lib/utils/utm.ts

const UTM_KEYS = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term'] as const

export function captureUTMs(): void {
  if (typeof window === 'undefined') return
  const params = new URLSearchParams(window.location.search)
  const hasUtm = UTM_KEYS.some(key => params.has(key))
  if (!hasUtm) return // don't overwrite existing UTMs if this page has none

  const utms: Record<string, string> = {}
  UTM_KEYS.forEach(key => {
    const value = params.get(key)
    if (value) utms[key] = value
  })
  localStorage.setItem('exampilot_utms', JSON.stringify(utms))
}

export function getStoredUTMs(): Record<string, string> {
  if (typeof window === 'undefined') return {}
  try {
    return JSON.parse(localStorage.getItem('exampilot_utms') ?? '{}')
  } catch {
    return {}
  }
}
```

```typescript
// In the root layout or a client component that runs on first load
'use client'
import { useEffect } from 'react'
import { captureUTMs } from '@/lib/utils/utm'

export function UTMCapture() {
  useEffect(() => { captureUTMs() }, [])
  return null
}
```

```typescript
// In the trial_started and subscription_upgraded event calls
import { getStoredUTMs } from '@/lib/utils/utm'

posthog.capture('trial_started', {
  exam_board: user.examBoard,
  paper_code: user.paperCode,
  ...getStoredUTMs(), // spreads utm_source, utm_medium, etc.
})
```

**[VERIFY] before implementing:**
- Confirm `localStorage` is acceptable (alternative: first-party cookie with SameSite=Lax)
- Confirm under-18 GDPR implications of storing UTMs — first-party localStorage is generally acceptable but confirm with legal review
- Confirm UTM parameter names match what's used in Brevo and any Reddit campaign links

## Guardrails — non-negotiable

- Under-18 users: no cross-site tracking, no third-party pixel data sharing
- All tracking must comply with GDPR/PECR — confirm consent mechanism covers PostHog
- Clarity unmasked auth-route recording is a PRIVACY CONCERN — flag it in every audit, do not leave it unflagged
- Never recommend tracking email addresses as PostHog distinct IDs
- GA4 receives automatic pageviews only — do not add custom GA4 events
- All implementation code carries [VERIFY before shipping] — the developer confirms file locations and data shapes

## What this skill does NOT do

- Does not push events to PostHog directly. It produces specs and code patterns for developer implementation.
- Does not configure PostHog project settings, dashboards, or funnels — those are manual PostHog UI operations.
- Does not audit GA4 — GA4 is pageview-only and intentionally minimal. If GA4 custom events are needed, that's a separate decision.
- Does not set up Clarity masking — flag the concern and direct the developer to Clarity's masking configuration.
- Does not design GTM signal scoring. For signal scoring logic, see `marketing/gtm-engineering/scoring-model.md` and run `/signal-review`.
