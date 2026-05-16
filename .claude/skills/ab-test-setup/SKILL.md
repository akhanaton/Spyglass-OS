---
name: ab-test-setup
description: Design A/B test hypotheses for ExamPilot's landing pages, CTAs, emails, and onboarding flows. Produces a complete test spec — hypothesis, variants, success metric, sample size estimate, and PostHog feature flag setup. Grounded in the experiment framework.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.
  The Three Ms of AI™ is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.*

## What this skill does

Designs complete A/B test specs for ExamPilot. Produces everything needed to implement the test: a falsifiable hypothesis, variant descriptions, primary and guard-rail metrics, sample size estimate, PostHog feature flag code, test duration, and decision criteria. Grounded in the experiment framework and the real constraints of ExamPilot's traffic levels.

**Bike Method Phase 1:** This skill produces a spec for developer implementation and human decision-making. It does not create PostHog feature flags directly.

## When `/ab-test-setup` runs

- "I want to test [element]" — CTA copy, headline, email subject line, onboarding step, pricing layout
- "What should I A/B test?"
- "Help me design an experiment for [page or flow]"
- Before shipping a major copy or design change to a high-traffic page

## Context files — read at session start

```bash
cat marketing/references/experiment-framework.md
cat marketing/context/funnel-strategy.md
```

If `marketing/references/experiment-framework.md` does not exist, proceed with the framework embedded in this skill.

## Execution — five steps

### Step 1 — Confirm test scope

Before designing the test, confirm:

| Parameter | Description | Example |
|---|---|---|
| What to test | The specific element — one thing only | CTA button copy |
| Where | The page or flow | Landing page hero |
| Current state | What is the control (A) right now | "Get Started" |
| Hypothesis direction | What you expect to happen and why | More specific copy will increase clicks |
| Current baseline metric | If known | CTA click rate: 3.2% |

Show: *"Designing an A/B test for [element] on [page]. Control is [current state]. Does this look right?"*

Do not proceed without confirmation.

---

### Step 2 — Write the hypothesis

A valid hypothesis is falsifiable. It names the change, the expected outcome, and the reason.

**Template:**
"We believe [changing X to Y] will [increase/decrease] [metric] because [behavioural or psychological reason]."

**Quality bar:**
- Specific: names the exact element and the exact change
- Measurable: names a metric that can be tracked in PostHog
- Reasoned: gives a real reason (not "because it sounds better")

**Examples of good hypotheses:**
- "We believe changing the CTA from 'Get Started' to 'Start Practising Free' will increase CTA click rate because it makes the benefit (free trial + action) explicit, reducing cognitive load and setting accurate expectations."
- "We believe adding the student's exam board ('Built for Cambridge 9709') to the homepage headline will increase registration rate among Cambridge 9709 visitors because exam-board specificity is a credibility signal for this audience."
- "We believe moving the annual plan to the left (default position) on the pricing page will increase annual plan selection rate because left-anchored options are selected more frequently in pricing contexts."

**Red flags — redesign the hypothesis if:**
- It tests two changes at once ("change the CTA copy AND the button colour") — split into two tests
- The metric isn't trackable in PostHog without a new event — flag this and note the event that needs adding
- The reason is vague ("we think it will convert better") — push for a behavioural reason

---

### Step 3 — Define variants

**Rule: two variants maximum.** ExamPilot does not have the traffic for multivariate testing yet.

**Control (A):** Document the current state exactly. Include:
- The exact copy or design element
- The page/component it appears on
- Any relevant context (e.g. what's visible above/below it)

**Treatment (B):** Document the proposed change exactly. Include:
- The exact new copy or design element
- What changes and what stays the same

**What NOT to test (for now):**
- Page layout changes that require significant engineering — test copy first
- Multivariate combinations — one variable per test
- Changes on pages with <100 daily visitors — not enough traffic to reach significance

---

### Step 4 — Success metrics

**Primary metric:** One measurable outcome. This is the decision metric.

Examples:
- CTA click rate: `cta_clicked` events / page sessions
- Email open rate: measured in Brevo
- Trial start rate: `trial_started` events / CTA clicks
- Session completion rate: `session_completed` / `session_started`
- Upgrade rate: `subscription_upgraded` / `trial_started`

**Guard-rail metrics:** 1-2 secondary metrics that must not degrade.

The test "wins" only if:
- The primary metric improves AND
- No guard-rail metric falls by more than the threshold

Example guard rails:
- If testing CTA copy: guard rail = bounce rate must not increase by >5%
- If testing pricing page layout: guard rail = overall trial start rate must not decrease

**How to measure:** PostHog feature flag + event filter.

```
Primary metric:
  Event: [event_name]
  Filter: feature flag = 'treatment'
  Denominator: [what defines the exposure — page sessions, CTA views, etc.]

Guard rails:
  1. [metric]: must not change by more than [threshold]
  2. [metric]: must not change by more than [threshold]
```

---

### Step 5 — Sample size, duration, and PostHog setup

**Sample size estimate:**

For conversion rate tests, use this simplified approach:

Given:
- Baseline rate (p): the current conversion rate as a decimal (e.g. 3.2% = 0.032)
- Minimum detectable effect (MDE): the smallest relative lift worth detecting — use 15% relative as default
  - If baseline is 3.2%, a 15% relative lift = new rate of 3.68%
- Confidence level: 95% (standard)
- Statistical power: 80% (standard)

Approximate formula:
```
n ≈ (16 × p × (1 - p)) / (MDE_absolute)²
```

Where MDE_absolute = baseline × MDE_relative = 0.032 × 0.15 = 0.0048

Example: n ≈ (16 × 0.032 × 0.968) / (0.0048)² ≈ (0.495) / (0.000023) ≈ 21,500 exposures per variant

If this number is unreachable within 8 weeks, increase the MDE (test only if you expect a larger effect) or reduce scope to a higher-traffic element.

**Duration:**
- Minimum: 2 weeks — to capture the weekly student activity cycle (active Mon-Thu, lower Fri-Sun)
- Maximum: 8 weeks — beyond 8 weeks, external factors (exam calendar, marketing changes) contaminate results
- At [X] daily exposures: this test needs approximately [Y] days to reach [N per variant]

**Exam calendar caveat:**

Do NOT run or start tests during:
- The 2 weeks immediately before Cambridge 9709 main sitting (approx. late April to mid-May)
- The 2 weeks before Edexcel IAL main sitting
- Results week

Student behaviour changes dramatically in these windows — test results from those periods are not representative of steady-state behaviour.

Check `marketing/gtm-engineering/signal-registry.md` for exact exam dates before scheduling.

**PostHog feature flag setup:**

```typescript
// In the component being tested
'use client'
import { usePostHog } from 'posthog-js/react'
import { useEffect, useState } from 'react'

export function HeroCTA() {
  const posthog = usePostHog()
  const [variant, setVariant] = useState<string | undefined>(undefined)

  useEffect(() => {
    const flagValue = posthog.getFeatureFlag('[flag-name]')
    setVariant(typeof flagValue === 'string' ? flagValue : 'control')

    // Track exposure — fires once per page load
    posthog.capture('experiment_viewed', {
      experiment: '[flag-name]',
      variant: flagValue ?? 'control',
    })
  }, [posthog])

  const ctaText = variant === 'treatment' ? '[treatment copy]' : '[control copy]'

  return <button>{ctaText}</button>
}
```

**PostHog flag configuration (manual step in PostHog UI):**
- Flag name: `[flag-name]` (kebab-case, descriptive — e.g. `cta-copy-v1`)
- Rollout: 50% control / 50% treatment
- Targeting: all users (or specific cohort if testing on a segment)
- Multivariate: no — binary on/off

---

### Output format

Present as a complete spec:

```
A/B Test Spec: [test name]
---

Hypothesis:
"We believe [X] will [outcome] because [reason]."

Variants:
  Control (A): [exact description]
  Treatment (B): [exact description]

Success metrics:
  Primary: [metric] — measured by [PostHog event + denominator]
  Guard rail 1: [metric] — threshold: no more than [X]% change
  Guard rail 2: [metric] — threshold: no more than [X]% change

Sample size:
  Baseline: [current rate]
  MDE (relative): [15%]
  MDE (absolute): [calculated]
  Required per variant: ~[N] exposures
  At current traffic (~[X]/day): approximately [Y] days

Duration:
  Minimum: 2 weeks
  Recommended: [N] weeks
  Do not start between: [exam window dates from signal-registry.md]

PostHog feature flag:
  Flag name: [flag-name]
  Rollout: 50/50
  [Code snippet above]

Decision criteria:
  Ship if: p < 0.05 AND effect ≥ MDE AND minimum 2 weeks completed
  Stop early for harm if: any guard rail falls by >[threshold] within the first week
  Roll back if: primary metric reverses within 1 week of shipping

[VERIFY] flags:
  - Confirm baseline metric from PostHog before starting
  - Confirm exam dates from signal-registry.md before scheduling
  - Confirm developer can implement the feature flag in [component]

Next step: Review spec, confirm baseline metric in PostHog, schedule start date (check exam calendar), then hand to developer for flag implementation.
```

## Guardrails

- Two variants only — ExamPilot does not have the traffic for multivariate tests
- Minimum 2-week run — no early calls based on a few days of data
- No tests during exam season windows — results are not representative
- Primary metric must be trackable in PostHog — if the event doesn't exist, add it first (see `/analytics-tracking`)
- Do not test changes that involve GDPR-sensitive data collection — any change that affects what data is collected requires a separate legal review

## What this skill does NOT do

- Does not create PostHog feature flags in the PostHog UI. The developer creates the flag manually.
- Does not run statistical significance calculations in real time. It provides the spec; PostHog's experiment feature or a separate calculator is used during the test.
- Does not run tests. It designs them. The developer implements and PostHog records results.
- Does not recommend testing more than one variable at a time.
- Does not approve tests that lack a falsifiable hypothesis or a trackable primary metric.
