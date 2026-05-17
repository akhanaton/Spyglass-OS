# Spyglass OS — Full Coverage Assessment

**Date:** 2026-05-16
**Owner:** Enitan
**Stage:** Pre-launch → Alpha (100 students)
**Linear issue:** EP-49
**Research basis:** Verified external sources (see inline citations). No assumptions.

---

## What's genuinely strong — don't touch it

The marketing machine is legitimately impressive for a 2-person team. 29 skills, 21 Python modules, a full content-to-publish pipeline with quality scoring, GTM signal architecture with a proper scoring model, and an 18-month strategy that's operationally precise. Most funded 5-person teams don't have this depth.

The wiki + OS separation is correct architecture. OS is the desk, wiki is the library. The decision to integrate everything into one OS rather than a separate repo was the right call — Teresa can operate marketing largely independently, and it feeds back into Enitan's product signals.

`churn-prevention.md` is ahead of where most pre-launch SaaS teams are — the dunning timeline, cancel flow design, and health score model are solid. The problem is it has no wiring yet.

---

## Critical gaps — fix before the first paid user

### 1. Involuntary churn is not wired

Involuntary churn (failed payments) accounts for 30–50% of total churn in SaaS. Single-retry logic recovers ~23% of failed payments. Intelligent retry + dunning sequence recovers ~68%.

**ChurnWard ($29/mo)** has a verified Dodo Payments integration — this matters because Dodo is non-standard and most dunning tools are Stripe-only. Covers: automated dunning email sequences, expiring card alerts, win-back campaigns, trial conversion emails, and revenue analytics.

`churn-prevention.md` has the strategy. The gap is that nothing is actually wired. Set this up before the first subscription payment, not after.

**Sources:** churnward.com (Dodo Payments integration confirmed), Dodo Payments RevOps blog, SaaS payment statistics 2025 (kaplancollectionagency.com)

**Actions:**
- Wire ChurnWard to Dodo Payments
- Add to `connections.md`
- Dunning email sequences → Brevo (already planned), follow timeline in `churn-prevention.md`

---

### 2. No production error monitoring

PostHog covers behavioral analytics and some frontend exception tracking. Nothing exists for backend errors, performance degradation, or silent failures. For an exam prep product, a broken session two days before a student's exam = 1-star review on Reddit, in the exact communities you're building reputation in.

**Sentry Team ($26/mo):** 50K errors/month, unlimited seats, Slack/Discord integration for instant alerts, performance tracing. PostHog free tier (already in place) + Sentry Team = $26/month for complete observability.

There is no observability row in `connections.md` at all.

**Sources:** sentry.io/pricing (verified), posthog.com/pricing (verified), SigNoz Sentry pricing guide

**Actions:**
- Add Sentry Team ($26/mo)
- Wire alerts to Discord
- Add observability row to `connections.md`

---

## Strategic additions — outsized positive outcomes

### 3. WhatsApp — Tier 1 markets run on it, not email

Verified penetration data for ExamPilot's markets:
- **UAE:** 85.8% of population (age 16–64) uses WhatsApp. It is the #1 social platform in the country.
- **India:** 500M+ WhatsApp users, 291.6M WhatsApp Business app downloads.
- **Pakistan:** Significant adoption (specific % unverifiable from available sources, but pattern is consistent with India/UAE).

Verified engagement stats: ~98% message open rate vs ~20% for email. 45–60% CTR on WhatsApp promotions vs 2–5% for email. When a student messages you first, the 24-hour inbound window is free to reply with any content.

Edtech-specific mechanic: daily study reminders via WhatsApp have documented 2–3x higher course completion rates (go4whatsup.com). Physics Wallah (India's largest edtech) uses AiSensy.

`funnel-strategy.md` already lists "Tutor WhatsApp referrals" as one of four paths to first 100 students — but there's zero infrastructure behind it.

**AiSensy (~$18/mo USD, Meta Business Partner):** Covers inbound student questions, exam date alerts, daily study nudges, and course reminders. Per-message cost for utility/service messages is near-zero (₹0.145/message ~ $0.002). Marketing messages ~$0.013 each.

**Sources:** wapikit.com WhatsApp Business Statistics 2025, aisensy.com pricing 2025, go4whatsup.com WhatsApp for Education 2026, fonada.com WhatsApp automation for education

**Actions:**
- Add WhatsApp (AiSensy) to `connections.md`
- Wire inbound support first (free 24hr window)
- Add exam calendar alerts and study reminders as sequences (Phase 1)
- Add `/whatsapp-broadcast` command for campaign messages tied to exam dates

---

### 4. Student outcome data — the moat, and it must be collected from day one

ExamPilot's core claim is that it improves exam performance. The ERI score improvement signal exists in the signal registry (+8 weight) — but that's internal product data. What's missing is the actual outcome: did the student improve their grade?

If you can demonstrate "students who completed 3+ topics on ExamPilot improved their mocks by an average of 1 grade boundary" — that becomes:
1. The most powerful conversion asset you have (no competitor can make this claim without the same data)
2. The strongest SEO content angle ("does exam revision software actually work?")
3. The single strongest proof point for the tutor referral channel (tutors recommend things that demonstrably work)

This data doesn't collect itself. The collection window is narrow: 2–3 days after Results Day, when students know their grades. If you miss the first cohort, you wait a year for the next exam cycle.

**Actions:**
- Design the outcome data schema now: student ID, exam board, topic coverage in product, mock scores pre/post, final grade
- Build a post-exam outcome collection flow: Brevo/WhatsApp trigger fires on Results Day (already in signal registry) → links to a simple Coda form
- Wire the collection trigger to the exam calendar signals in `signal-registry.md`

No new tool needed — Coda form + Brevo/WhatsApp trigger.

---

### 5. Event-driven automation middleware — the activation chain has no connective tissue

Current state: PostHog (behavioral events), Brevo (email sequences), Attio (CRM), Dodo Payments (billing). Nothing connects them when events fire.

The activation chain needed at launch: student signs up → PostHog event fires → Attio contact created (with source, exam board, score) → Brevo welcome sequence triggered → WhatsApp/Discord alert to Teresa. Right now, each step is manual or requires a custom script per integration.

**n8n ($35/mo cloud, or self-hosted free):** The research consensus for bootstrapped SaaS. Unlike Make (per-operation pricing that compounds) or Zapier (expensive at scale), n8n charges flat for unlimited workflows. Has native PostHog, Brevo, and Attio nodes. The trial → activation chain gets built once and runs forever.

At 100 students, manual activation is survivable. At 300, it's a part-time job.

**Sources:** n8n.io (pricing verified), soraia.io n8n startup workflows, modernoutreach.beehiiv.com n8n vs Make 2026

**Actions:**
- Add n8n to `connections.md`
- Build the trial → activation chain before launch: Dodo Payments webhook → n8n → Attio contact + Brevo sequence + Discord alert
- Phase 2: add dunning webhook chain (ChurnWard event → n8n → Brevo dunning sequence)

---

## Worth adding — lower urgency

### 6. Google Calendar MCP — 15-minute setup, meaningful weekly saving

Google Calendar is listed in `connections.md` as "not connected." It's a native claude.ai MCP — same mechanism as Coda and PostHog. The entire marketing strategy is exam-calendar-driven (5 campaign trigger dates in the signal registry). Connecting Calendar means the OS surfaces upcoming exam windows automatically during `/signal-review` and `/weekly-pulse` without manual tracking.

**Action:** Wire Google Calendar MCP. Costs nothing.

---

### 7. Engineering workflow — the OS doesn't serve Enitan's primary constraint

Enitan owns Engineering and the launch date is the critical path. `/review` and `/security-review` skills exist but aren't integrated into any engineering workflow. No GitHub PR awareness, no deployment tracking, no automated quality gate.

A lightweight `/eng-review` command — runs the review + security skills against a diff, logs outcome to Linear — gives Enitan a consistent quality gate without adding process overhead.

**Action:** Create `/eng-review` command that wraps existing `/review` and `/security-review` skills, outputs to Linear via MCP.

---

### 8. Tutor referral program — design the mechanic now, wire it at 30+ happy students

The research confirms: don't wire an affiliate program before 100 users (bottom 40.8% of program performance by revenue at early stage, per Rewardful benchmarks). But tutors are different from consumer affiliates — one tutor recommends to 10–20 students consistently. The tutor outreach is already in the acquisition plan.

**Tolt ($29/mo, Stripe/Dodo compatible):** Creates referral links in 10 minutes. Design the mechanic now (tutors get % commission on referred student subscriptions), have the link ready for the first tutor outreach.

**Sources:** rewardful.com SaaS affiliate program benchmarks (verified), refgrow.com best affiliate software 2026

**Action:** Design the referral mechanic now. Wire Tolt when you have 30+ students with exam results to show tutors.

---

## What NOT to add (verified, not instinct)

| Item | Why not |
|---|---|
| Intercom / Zendesk / Freshdesk | Designed for 500+ users. Under 100, every support conversation is a research conversation — automating it loses signal. |
| NPS surveys now | Meaningless before students have completed an exam cycle. No reliable baseline. |
| Zapier | Per-operation pricing compounds. n8n is strictly better at this scale. |
| LogRocket | $99/month. PostHog already covers session replay on free tier. |
| Amplitude / Mixpanel | PostHog covers everything at free tier. Second analytics tool fragments data. |
| Full roadmap tools (Aha!, ProductBoard) | Theatre at 2 people. Linear + decisions/log.md is sufficient until a PM hire. |
| Pre-built FAQ / knowledge base | Let the Coda support log tell you what to write first. |
| Affiliate program now | Too early. Correct timing: 30–50 students with verifiable exam results. |

---

## Acceptance criteria

**Before first paid user (non-negotiable):**
- [ ] ChurnWard wired to Dodo Payments — add to `connections.md`
- [ ] Dunning email sequences built in Brevo following `churn-prevention.md` timeline
- [ ] Sentry Team ($26/mo) added — wire Discord alerts — add to `connections.md`

**Phase 0–1 (high outsized returns):**
- [ ] AiSensy WhatsApp wired — inbound support first, then exam alerts + study nudges — add to `connections.md`
- [ ] `/whatsapp-broadcast` command created (campaign messages tied to exam calendar)
- [ ] Student outcome data schema designed (student ID, exam board, topic coverage, mock/final grade)
- [ ] Post-exam outcome collection flow built (Brevo/WhatsApp trigger on Results Day → Coda form)
- [ ] n8n wired — trial → activation chain: Dodo webhook → Attio contact + Brevo sequence + Discord alert

**Useful, lower urgency:**
- [ ] Google Calendar MCP connected
- [ ] `/eng-review` command created (wraps `/review` + `/security-review`, logs to Linear)
- [ ] Tutor referral mechanic designed (Tolt — wire when 30+ students with results)

**Don't build:**
- ~~Help desk (Intercom/Zendesk)~~
- ~~NPS automation~~
- ~~Zapier~~
- ~~LogRocket~~
- ~~Amplitude / Mixpanel~~
- ~~Pre-built FAQ~~

---

## Summary

The OS is well-covered on marketing execution, signal architecture, and content operations. The gaps are in revenue operations and production observability — infrastructure for when money actually flows and when things break.

The single highest-leverage addition that isn't tooling: **student outcome data collection**. Build the collection mechanism before the first exam cohort sits, or wait a year for the next cycle.
