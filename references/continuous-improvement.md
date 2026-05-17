# Continuous Improvement -- Core OS Principle

Every function in Spyglass OS is a learning system. It starts with hypotheses (initial parameters), captures outcomes, and converges toward truth through data. Nothing stays static. Parameters that were set on day one should be measurably better by day ninety.

This is not aspirational. It is how the OS operates.

## The loop

Every repeatable function follows the same three-step loop:

```
Capture (what happened + what resulted)
    |
Review (at defined cadence, compare outcomes to expectations)
    |
Adjust (change parameters, log the change with the data that drove it)
    |
    +---> next cycle
```

If a function doesn't have all three steps, it's incomplete.

## Rules

**1. Initial parameters are always estimates.**

Label them explicitly. The GTM signal registry says: "Weights are initial estimates -- adjust based on signal-to-conversion data after 8-12 weeks." Every function should do this. Content pillar ratios, posting times, quality score thresholds, keyword tiers, email send times -- all estimates until data says otherwise.

**2. Capture must be cheap.**

If capturing outcome data requires significant manual work, the loop will die. Use existing integrations (PostHog, Linear, Coda, Postiz) to capture automatically where possible. Where manual input is needed (e.g., "how many replies did you send?"), embed it in an existing ritual (e.g., `/weekly-pulse`) rather than creating a new one.

**3. Review happens at defined cadences, not ad hoc.**

| Cadence | What gets reviewed | Ritual |
|---|---|---|
| Weekly | Operational metrics: content output, support contacts, X engagement, pipeline velocity | `/weekly-pulse` (Teresa), `/signal-review` (Enitan) |
| Monthly | Parameter performance: which signals predict conversion, which content types drive engagement, which keywords drive traffic | `/tune` (both) |
| Quarterly | Strategic alignment: are phase gates on track, should priorities shift, are assumptions still valid | Manual review against marketing plan |

**4. Adjustments are logged.**

Every parameter change goes to `decisions/log.md` with:
- What changed (old value to new value)
- What data drove the change
- When the next review should happen

This creates an audit trail. Six months from now, you can trace why a signal weight is 15 instead of 8 and whether the change actually improved outcomes.

**5. New functions must define their loop at creation.**

When building a new skill, command, or function via `/level-up`, define:
- What data it captures (inputs + outcomes)
- Where the data lives (PostHog, Coda, Postiz, manual in ritual)
- What parameters are adjustable
- What review cadence applies
- What "good" looks like (target metric)

If you can't answer these, the function is a one-shot task, not a repeatable system. That's fine -- not everything needs a loop. But if it runs more than once a month, it should have one.

## Current functions and their loops

| Function | Captures | Adjustable parameters | Review cadence | Data source |
|---|---|---|---|---|
| **GTM Engineering** | Signal events + conversion outcomes | Signal weights in `scoring-model.md` | Monthly via `/tune`, full recalibration at Phase 2 (8-12 weeks post-launch) | PostHog, Coda Signals table |
| **X / Build in Public** | Post type, author, time, format + engagement outcomes | Content pillar ratios (40/25/20/15 initial), posting times, format preferences | Monthly via `/tune` | Postiz analytics, PostHog (UTM) |
| **LinkedIn / Professional Authority** | Post type, format, time + engagement outcomes, teacher outreach acceptance rate | Content pillar ratios (35/25/20/20 initial), posting times, format mix (post/carousel/article), outreach cadence | Monthly via `/tune` | Postiz analytics, LinkedIn native analytics, PostHog (UTM), Attio CRM (outreach conversion) |
| **SEO / Content** | Keyword target, quality score, word count + ranking, traffic, time on page | Keyword tier priorities, quality score thresholds, content length targets | Monthly via `/tune` | GSC, DataForSEO, PostHog |
| **Product** | Feature usage events + retention by cohort | Roadmap priorities, feature investment decisions | Weekly via `/product-pulse` (EP-47) | PostHog |
| **Customer Support** | Issue type, channel, resolution + insight yield | Template quality, process changes, product insight routing | Weekly via `/feedback-digest` (EP-48) | Coda support log |
| **Email (Brevo)** | Sequence type, send time + open rate, click rate, conversion | Subject line patterns, send timing, sequence length, segmentation | Monthly via `/tune` | Brevo analytics |
| **Churn Prevention** | Cancel reason, save offer type + save rate, reactivation rate | Save offer thresholds, pause durations, dunning timing | Monthly via `/tune` | ChurnWard, Dodo Payments |
| **WhatsApp Communities** | Community joins, broadcast sends + click rate, referral signups | Broadcast frequency (max 2/week initial), content mix, community sub-group structure | Monthly via `/tune` | WhatsApp Business App (P0), Wati analytics (P1+) |
| **Facebook Groups** | Posts/comments made, parent inquiries generated, page referrals | Posting cadence (2-3/week initial), group selection, content types | Monthly via `/tune` | Manual tracking in Coda Signals table |
| **School Partnerships** | Schools contacted, conversations started, teachers recommending, students attributed | Outreach cadence (2-3 schools/week initial), messaging, referral incentive structure | Monthly via `/tune` | Attio CRM |

Functions not yet active (marked "not yet connected" in `connections.md`) get their loops defined when wired.

## What this is NOT

- Not a reporting framework. Reports describe what happened. This loop changes what happens next.
- Not a dashboard project. The data lives in existing tools (PostHog, Coda, Postiz). `/tune` queries them. No new dashboards to maintain.
- Not a weekly burden. Weekly rituals (`/weekly-pulse`, `/signal-review`) capture data as a side effect of their primary job. `/tune` runs monthly and synthesizes what the weeklies already collected.

## Relationship to other frameworks

- **3Ms framework** (`references/3ms-framework.md`): The 3Ms tells you HOW to build automations (Mindset, Method, Machine). Continuous improvement tells you how to make them BETTER over time. The 3Ms builds the system. This loop tunes it.
- **Bike Method** (3Ms, Layer 3): The Bike Method phases (training wheels > guided > watched > hands-off) are about rollout confidence. The improvement loop is about parameter accuracy. They're complementary: you might be in Phase 3 (watched) on a skill but still adjusting its parameters monthly.
- **`/audit`** (Four Cs): The audit checks structural health -- is the OS well-built? `/tune` checks functional health -- is the OS performing well?
