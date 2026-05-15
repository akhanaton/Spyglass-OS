# Trigger Playbook

If→then rules that fire when signal thresholds are crossed. Each trigger has a destination, automation status (manual / auto), and owner.

**Phase 0:** All triggers are manual — `signal_processor.py` flags the threshold; Enitan takes the action.  
**Phase 1:** Behavioral triggers (Attio → Brevo) become automated once Attio API and Brevo are connected.

---

## Conversion triggers

| Threshold | Signal | Action | Destination | Phase 0 | Phase 1 |
|---|---|---|---|---|---|
| CRS reaches Hot (40+) | Trial user crossing tier | Enrich Attio contact (tier = Hot). Flag for conversion email. | Attio → Brevo | Manual flag in `/signal-review` | Auto: Brevo conversion sequence |
| In-app upgrade CTA click | PostHog event | Immediate high-priority flag — user is at the door. | Attio | Manual | Manual (too high-value to automate without personalisation) |
| Pricing page visit ≥ 2 times in 7 days | PostHog | Flag as conversion-ready. Add to conversion email list. | Attio → Brevo | Manual | Auto: Brevo conversion email next day |

---

## Onboarding / activation triggers

| Threshold | Signal | Action | Destination | Phase 0 | Phase 1 |
|---|---|---|---|---|---|
| New trial sign-up | PostHog event | Create contact in Attio (tier = Cold). Enrol in Brevo welcome sequence. | Attio + Brevo | Manual | Auto |
| Trial user: no session within 48 hours of sign-up | PostHog inactivity | Send activation nudge email (day 2 of welcome sequence). | Brevo | Manual | Auto |
| First session completed | PostHog event | CRS +15. Update Attio. Send "you did it" email if in welcome sequence. | Attio + Brevo | Manual | Auto |

---

## Retention triggers (paying subscribers)

| Threshold | Signal | Action | Destination | Phase 0 | Phase 1 |
|---|---|---|---|---|---|
| Active subscriber inactive ≥ 7 days (EHS At-risk) | PostHog inactivity | Flag for re-engagement. Check churn-prevention.md for sequence. | Brevo | Manual | Auto: re-engagement sequence |
| Subscriber EHS Fading for 2 consecutive weeks | PostHog | Send "how's it going?" in-app nudge or email. | Brevo | Manual | Auto |
| Subscriber completes all topics for current unit | PostHog | Prompt expansion to next unit. Upsell signal. | Attio + Brevo | Manual | Auto |

---

## Community triggers

| Threshold | Signal | Action | Destination | Phase 0 | Phase 1 |
|---|---|---|---|---|---|
| Brand mention in target subreddit | Syften | Flag for manual response. Check tone (positive / question / negative). | Coda Signals table | Manual response | Manual (always — community requires human voice) |
| Study struggle post (demand signal) in target sub | Syften | Route to `/write-reddit`. Draft value-first response. | Coda + /write-reddit | Manual | Manual |
| Competitor comparison thread | Syften | Flag for positioning response. Check if ExamPilot mentioned. | Coda Signals table | Manual | Manual |

---

## SEO triggers

| Threshold | Signal | Action | Destination | Phase 0 | Phase 1 |
|---|---|---|---|---|---|
| Keyword ranking drops > 5 positions | DataForSEO / GSC | Audit content. Check for SERP feature changes. Update or expand article. | Coda → /write-article | Manual | Manual |
| Keyword ranking gains > 5 positions | DataForSEO / GSC | Amplify: share on Reddit, add internal links, update GSC coverage. | Coda | Manual | Manual |
| New query triggering impressions with CTR < 5% | GSC | Create content brief via `/research-keywords`. | /research-keywords | Manual | Manual |
| Competitor outranking on target keyword | DataForSEO | Analyse content gap. Create superior resource. | /write-article | Manual | Manual |

---

## Campaign triggers (exam calendar)

| Threshold | Signal | Action | Destination | Phase 0 | Phase 1 |
|---|---|---|---|---|---|
| Results Day − 30 days (CIE: ~Jul 16) | Calendar | Activate Results Day campaign. Begin content sprint. Prepare Brevo campaign. | Coda checklist | Manual | Manual |
| Results Day − 7 days | Calendar | Final push: Reddit posts, Brevo campaign send, Discord activity. | Coda + Brevo | Manual | Semi-auto (Brevo) |
| Mock season start (~Jan 15) | Calendar | Demand gen pulse: increase Reddit activity, push study guides. | Coda | Manual | Manual |
| Exam month start (~May 1) | Calendar | Acquisition push: conversion emails to warm list, paid-trial offer if applicable. | Brevo | Manual | Semi-auto |

---

## Action log

When a trigger is actioned manually, log it in the Coda Signals table: set Status → Actioned. This is the data that enables Phase 2 weight validation.
