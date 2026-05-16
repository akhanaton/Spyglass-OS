---
name: paywall-upgrade-cro
description: Optimise ExamPilot's trial-to-paid conversion. Designs paywall copy, upgrade prompts, pricing page framing, and the in-app moments that maximise conversion without manipulative pressure. Uses exam calendar as natural urgency.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.
  The Three Ms of AI™ is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.*

## What this skill does

Designs the copy, framing, and timing of ExamPilot's upgrade prompts — from feature gates to trial expiry notices to the pricing page itself. The goal is to maximise trial-to-paid conversion using genuine urgency (exam calendar), accurate pricing anchoring, and honest risk reversal. No dark patterns, no manufactured scarcity, no guilt.

**Pricing (EUR only, non-negotiable):**
- Monthly: €29/mo
- Quarterly: €69 / 3 months (= €23/mo)
- Semi-annual: €96 / 6 months (= €16/mo)
- Annual: €144 / year (= €12/mo)

**Bike Method Phase 1:** All copy requires human review before shipping. This skill produces drafts and stops.

## When `/paywall-upgrade-cro` runs

- "What should the paywall say?"
- "Write the upgrade prompt for [scenario]"
- "Optimise the pricing page"
- "How should I handle trial expiry messaging?"
- "Design the post-upgrade experience"
- When PostHog shows low conversion from `trial_started` to `subscription_upgraded`

## Context files — read at session start

```bash
cat references/voice-house.md
cat marketing/context/funnel-strategy.md
cat marketing/gtm-engineering/trigger-playbook.md
cat marketing/gtm-engineering/signal-registry.md
```

## Execution — four steps

### Step 1: Map upgrade touchpoints

Identify where the student encounters the paywall or upgrade prompt. Four standard touchpoints — design copy for the ones that apply:

| Touchpoint | Trigger | Priority |
|---|---|---|
| Feature gate | Student tries to use a premium feature | High |
| Trial expiry in-app notice | X days before trial ends | High |
| Pricing page (direct visit) | Student navigates to /pricing | High |
| Email sequence | Day 14 nurture email | Medium (handled in /email-sequence) |

Ask the user which touchpoints to address, or design all four if "all" or no specific instruction is given.

---

### Step 2: Copy by touchpoint

---

#### Feature gate copy

The student hits a premium feature. This is the highest-intent moment — they wanted the feature, which means they see the value.

**Do not:**
"This feature requires a paid plan."

This is neutral at best, but it creates friction and doesn't sell the value.

**Do:**
Lead with the outcome, show the smallest monthly price (annual equivalent), and reduce risk.

```
Unlock [Feature Name]

[One sentence on what this feature does for them — specific to what they were trying to do.]

Start at €12/month (annual plan)

[Upgrade now →]  [See all plans →]

Cancel any time.
```

Feature-specific examples:

**Knowledge State tracking:**
```
Unlock Knowledge State Tracking

See exactly which Pure 1 topics you've mastered — and which ones are costing you marks.

Start at €12/month (annual plan)

[Upgrade now →]  [See all plans →]

Cancel any time.
```

**Smart Review:**
```
Unlock Smart Review

Your personalised review queue — questions resurface at the right moment, so you stop forgetting what you practised last week.

Start at €12/month (annual plan)

[Upgrade now →]  [See all plans →]

Cancel any time.
```

**Rules for feature gate copy:**
- Always show the annual price per month (€12/mo) as the primary price — not the total annual cost (€144) and not the monthly price (€29)
- The "Cancel any time" line is non-negotiable — it reduces the perceived risk of committing
- Never: "Upgrade to Premium", "Go Pro", "Unlock All Features" — be specific about the feature

---

#### Trial expiry in-app notices

Three notices. The copy escalates in directness without escalating in pressure.

**7 days before trial ends:**

Banner (dismissible):
"Your trial ends in 7 days. You've completed [N] sessions [if data available]. Keep your momentum — [Upgrade →]"

If session count is not available: "Your trial ends in 7 days. Your practice history and Knowledge State carry over when you upgrade. [Upgrade →]"

**3 days before trial ends:**

Banner (dismissible, but more prominent — e.g. yellow background):
"3 days left on your trial. [Exam board] exams are in [X weeks — pull from signal-registry.md]. Don't lose your revision progress. [€12/mo, annual plan →]"

If exam date is unknown: "3 days left. Your Knowledge State and Smart Review queue won't transfer to the free plan after your trial ends. [€12/mo →]"

**Day of trial expiry:**

Modal (shown once on login or dashboard visit, non-dismissible without a click):

```
Your trial ends today.

You've built [N sessions / topics practised] in the last 14 days.
[If data not available, omit this line.]

Keep your practice history and Knowledge State.

[Continue for €12/mo →]   [See all plans]

or [Continue on the free plan] (link, not a button — shows what the free plan includes)
```

**Rules for trial expiry copy:**
- Always reference the exam calendar when available — real urgency from a real deadline
- "Your trial ends today" not "Your trial has expired" — today implies still actionable
- Show the annual monthly equivalent (€12/mo), not the annual total (€144)
- Always provide a path to the free plan — students who are forced into a decision they don't understand will churn faster anyway

---

#### Pricing page

The pricing page must answer one question: "Is this worth it for me?"

**Structure:**

**Page headline:**
"Revision that pays off"

or: "Your exam prep, sorted."

Not: "ExamPilot Pricing" — that's a navigation label, not a headline.

**Anchor plan — show annual first:**

Lead with the annual plan. It is the best value for the student and the highest LTV for ExamPilot.

```
Most popular

Annual
€144 / year — just €12 a month

[Start your free trial →]
```

Then show all four tiers:

| Plan | Price | Equivalent |
|---|---|---|
| Annual | €144 / year | €12 / month |
| Semi-annual | €96 / 6 months | €16 / month |
| Quarterly | €69 / 3 months | €23 / month |
| Monthly | €29 / month | €29 / month |

Do not hide the monthly plan — students will want flexibility and hiding it creates distrust.

**Value framing (near the pricing table):**

"One session with a private maths tutor costs €30-60. ExamPilot's annual plan is the equivalent of two sessions — for a full year of daily, personalised practice." [VERIFY tutor pricing range for target markets]

**Exam calendar framing (below the pricing table):**

Pull the next major exam date from `marketing/gtm-engineering/signal-registry.md`. Use the real date.

"Cambridge 9709 exams start [month]. That's [X] months away — less than €[X×12] to exam day on the annual plan."

If exam date is unavailable from the signal registry, omit this section rather than approximating.

**Risk reversal section:**

```
What if it doesn't work for me?

Your free trial gives you full access for [X] days — no credit card required.
After that, cancel any time. Your practice data stays in your account.
If ExamPilot isn't helping you prepare, we'd rather you tell us why than keep your money.
```

**Pricing FAQ (minimum 4 questions):**

1. Do I need to pay upfront for the annual plan?
   "Yes — the annual plan is billed once a year at €144. You can cancel before renewal."

2. Can I switch plans?
   "Yes — you can switch plans at any time. We'll prorate the difference." [VERIFY Dodo Payments supports proration]

3. What happens when my trial ends?
   "If you don't upgrade, you move to the free plan. Your practice history and Knowledge State are [preserved / limited to X] on the free plan." [VERIFY exact free plan limitations]

4. Is VAT included?
   "Prices shown include VAT where applicable." [VERIFY VAT treatment in target markets]

5. What currencies do you accept?
   "All prices are in EUR. Payments are processed securely by Dodo Payments."

**Final CTA (bottom of page):**
"Start your free trial — no credit card needed"

---

#### Post-upgrade confirmation screen

The student has just upgraded. This is a high-emotion moment. Handle it correctly.

**Headline:**
"You're in. Now let's get to work."

Not: "Congratulations!" — students want to study, not celebrate
Not: "Thank you for your purchase" — transactional, not motivating

**Subheadline:**
"Your [plan] plan is active. Full access to every ExamPilot feature."

**Immediate next step:**
"Your next session is ready. [Continue with [topic] →]"

- If the student has a previous topic or Knowledge State, surface the most relevant next session
- If no history, surface the most common starting point: "Cambridge 9709 Pure 1 — Functions"

**No confetti, no celebration animations.** Students want to get back to studying. The confirmation screen should feel like the on-ramp to more work, not a reward.

**Email confirmation note:**
"We've sent your receipt to [email]. Check your spam folder if it doesn't arrive within a few minutes."

---

### Step 3: GTM signal trigger (for reference)

When the PostHog event `upgrade_clicked` fires with a `crs_tier: hot` property, the GTM trigger playbook (`marketing/gtm-engineering/trigger-playbook.md`) defines the action — typically an outreach sequence or manual review.

This skill does not duplicate the trigger logic. Reference `trigger-playbook.md` for the if→then rules. The copy in this skill feeds into the upgrade flow that the trigger playbook monitors.

---

### Step 4: A/B test candidates

Identify the highest-value test candidates from the upgrade flow:

**Priority 1 (highest impact, test first):**
- Pricing page: annual plan position (left vs centre vs right in a 3-column layout)
- Feature gate: benefit-led vs price-led framing
- Trial expiry Day 3 banner: exam calendar urgency vs progress-based ("you've done 5 sessions") framing

**Priority 2:**
- Post-upgrade confirmation headline: "You're in" vs name-based ("Enitan, you're in")
- Pricing page headline: value-oriented ("Revision that pays off") vs outcome-oriented ("Pass 9709 for €12/month") [VERIFY this claim format against ExamPilot's brand guardrails]

For each test, use `/ab-test-setup` to produce a full spec before implementing.

---

### Output format

```
Paywall Upgrade CRO: ExamPilot
---

Touchpoints addressed: [list]

Feature gate copy:
  [Feature name]: [copy block]

Trial expiry notices:
  7 days: [copy]
  3 days: [copy]
  Day of: [copy]

Pricing page:
  Headline: [copy]
  Pricing table: [confirm EUR tiers correct]
  Value framing: [copy]
  Exam calendar framing: [copy — [VERIFY] date from signal-registry.md]
  Risk reversal: [copy]
  FAQ: [questions and answers]
  Final CTA: [copy]

Post-upgrade screen:
  Headline: [copy]
  Subheadline: [copy]
  Next step CTA: [copy]

A/B test candidates: [list, ranked by priority]

[VERIFY] flags: [list all]
Next step: Review copy. Check [VERIFY] items against Dodo Payments terms and PostHog data. Run /ab-test-setup for the top test candidate.
```

## Guardrails — non-negotiable

- No fake urgency: no countdown timers without real deadlines, no "limited spots" (there are no limited spots for a software product)
- No guilt-tripping: "Don't lose your progress" is acceptable. "You'll fail your exam without ExamPilot" is not.
- Exam calendar urgency must use real dates from `marketing/gtm-engineering/signal-registry.md` — never approximate
- Pricing in EUR only. Never GBP, USD, or any other currency.
- Pricing must match exactly: €29/mo, €69/3mo, €96/6mo, €144/yr
- Annual monthly equivalent (€12/mo) is always shown as the lead price on upgrade prompts
- Under-18 users: no pressure tactics, no FOMO exploitation — natural urgency from real exam dates is acceptable

## What this skill does NOT do

- Does not write day-14 nurture emails. Use `/email-sequence` for that.
- Does not configure Dodo Payments or Stripe pricing. The copy is for the UI layer; payment configuration is a separate engineering task.
- Does not implement PostHog feature flags for A/B testing upgrade flows. Use `/ab-test-setup` for that.
- Does not design the trial structure (length, what's included). That's a product decision — this skill assumes the trial exists and works with its parameters.
- Does not auto-save anything. Present inline; save only on user instruction.
