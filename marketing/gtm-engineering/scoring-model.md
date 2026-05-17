# Scoring Model

Defines how signals are combined into a score, what tiers mean, and how tiers map to actions. Weights are initialised from the signal registry and updated empirically post-launch.

**All thresholds, caps, and tier boundaries below are initial estimates.** Adjust via `/tune` after 8-12 weeks of signal-to-conversion data. See `references/continuous-improvement.md`.

---

## Score types

Two independent scores per student contact:

### 1. Conversion Readiness Score (CRS)
Measures likelihood to convert from trial to paid. Applies to trial and prospect users.

Signals that contribute:
- Website signals (pricing page, free trial click)
- Activation signals (first session, session depth)
- Engagement signals (return visits, CTA clicks)
- Referral signals (tutor referral, teacher referral, school cohort signup)
- Community signals (WhatsApp community join, WhatsApp broadcast click, Facebook Group mention)

**CRS is reset at subscription start.** Once paid, track Engagement Health Score instead.

### 2. Engagement Health Score (EHS)
Measures retention risk for paying subscribers.

Signals that contribute:
- Session frequency and depth
- Topic completion rate
- ERI improvement
- Inactivity penalties

**EHS is not used for conversion tiers** — it feeds churn prevention logic only.

---

## Tier definitions (CRS)

| Tier | Score range | Meaning | Action |
|---|---|---|---|
| **Hot** | 40+ (initial estimate) | High engagement trial user — showing strong purchase intent | Prioritise for conversion email in Brevo. Enrich Attio with tier = Hot. |
| **Warm** | 20–39 (initial estimate) | Engaged but not yet ready to convert | Add to active nurture sequence. Monitor for tier upgrade weekly. |
| **Cold** | 5–19 (initial estimate) | Discovery stage — low or no product interaction | Demand gen content. No direct conversion push. |
| **Prospect** | 1–4 (initial estimate) | Website visitor or one-time touch | No action unless combined with community signal. |

---

## Tier definitions (EHS — paying subscribers)

| Tier | Score delta (7-day) | Meaning | Action |
|---|---|---|---|
| **Healthy** | +10 or above (initial estimate) | Regularly engaged | No action needed. |
| **Fading** | −5 to +9 (initial estimate) | Reduced engagement | Trigger re-engagement nudge (in-app or email). |
| **At-risk** | −20 or below (initial estimate) | Inactivity penalty triggered | Activate churn prevention sequence. See `references/churn-prevention.md`. |

---

## Scoring mechanics

### Rolling window
CRS is computed over a **30-day rolling window** (initial estimate). Signals older than 30 days decay to 50% weight; signals older than 60 days are excluded. This prevents a single viral session from permanently inflating a score.

### Score cap
Maximum CRS per signal type per window (initial estimates):
- Session duration signals: cap at ×3 (max +30 from this signal alone)
- Email CTA clicks: cap at ×2 (max +16)
- No cap on explicit intent signals (upgrade CTA click, pricing page)

### Signal combination boost
If a user triggers ≥3 distinct signal types in the same 7-day window, apply a +5 combination boost (initial estimate). Multi-signal engagement is a stronger predictor of conversion than depth in one channel.

---

## Scoring cadence

- **Weekly** (Phase 0): Run `/signal-review` manually each Friday. Scores computed fresh from available data sources.
- **Real-time** (Phase 1): signal_processor.py triggered on PostHog webhook events; Attio contact updated immediately.

---

## Model validation (Phase 2 review)

After 8–12 weeks post-launch, compare signal weights against actual conversion outcomes:

1. Pull conversion events from PostHog (trial → paid)
2. Pull signal history per converted user from Coda Signals table
3. Identify which signals had the highest pre-conversion frequency
4. Increase weights for high-correlation signals; decrease or remove non-correlating ones
5. Log weight changes in `decisions/log.md` with rationale

The blog framework (workflows.io) calls this the feedback loop: capture → score → act → measure → adjust. Phase 2 is when this loop closes empirically.
