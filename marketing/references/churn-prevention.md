# Churn Prevention

Retention strategy for ExamPilot. Covers cancel flows, save offers, dunning (failed payment recovery), and proactive retention. Adapted from marketingskills churn-prevention patterns, tailored for B2C SaaS with under-18 audience.

**When to use this:** Post-launch, once ExamPilot has paying subscribers. Not needed pre-launch.

## Two Types of Churn

| Type | Cause | % of total | Solution |
|---|---|---|---|
| Voluntary | Customer chooses to cancel | 50-70% | Cancel flows, save offers, exit surveys |
| Involuntary | Payment fails | 30-50% | Dunning emails, smart retries, card updaters |

Involuntary churn is easier to fix. Start there.

## Cancel Flow Design

### Flow Structure

```
Cancel button → Exit survey → Dynamic save offer → Confirmation → Post-cancel
```

### Exit Survey (1 question, single-select)

| Reason | What it tells you | Save offer |
|---|---|---|
| Too expensive | Price sensitivity | Discount (20-25% for 2-3 months) or downgrade |
| Not using it enough | Low engagement | Pause (1-3 months) |
| Exams are over / seasonal | Usage pattern | Pause until next exam window |
| Missing topics I need | Content gap | Roadmap preview + timeline |
| Switching to another tool | Competitive pressure | Comparison + discount |
| Technical issues | Product quality | Escalate to support immediately |
| Other | Catch-all | Free text field |

**ExamPilot-specific reasons:** "Exams are over" will be the #1 cancel reason. This is seasonal, not a failure. Offer pause until next exam window (Oct/Nov resits or Jan-Mar mocks).

### Save Offer Rules

- Match offer to reason. Discount won't save someone who isn't using the product.
- Maximum 2 offers per cancel session (primary + fallback) (initial estimate)
- Never exceed 25% discount (initial estimate — higher trains cancel-for-discount behavior)
- Time-limit discounts: 2-3 months, then full price resumes (initial estimate)
- Keep "continue cancelling" visible at every step. No dark patterns. GDPR audience.
- Track discount accepters. If they cancel again at full price, don't re-offer.

### Pause Subscription

Best save option for ExamPilot's seasonal usage pattern.

| Setting | Recommendation |
|---|---|
| Duration options | 1, 2, or 3 months (initial estimate) |
| Default | 1 month (initial estimate) |
| Maximum | 3 months (initial estimate) |
| During pause | Keep data and progress, remove access |
| Reactivation | Auto-reactivate with 7-day advance email |
| Repeat pauses | 1 per 12-month period (initial estimate) |

**Reactivation sequence:**
- Day -7: "Your pause ends in 7 days. Here's what's new in ExamPilot."
- Day -1: "Welcome back tomorrow! Your revision plan is ready."
- Day 0: "You're back! Pick up where you left off."

## Churn Prediction

### Risk Signals

| Signal | Risk level | Timeframe |
|---|---|---|
| Login frequency drops 50%+ | High | 2-4 weeks before cancel |
| No SRS sessions for 7+ days | High | 1-3 weeks |
| Billing page visits | High | Days before cancel |
| Email open rates decline | Medium | 2-6 weeks |
| NPS/Sean Ellis score drops below 6 | Medium | 1-3 months |

### Health Score (0-100)

**All weights and tier boundaries below are initial estimates.** Adjust via `/tune` after 30 days of subscriber engagement data. See `references/continuous-improvement.md`.

```
Health = (
  Session frequency    x 0.30 +
  SRS completion rate  x 0.25 +
  Topic coverage       x 0.20 +
  Streak length        x 0.15 +
  Feature depth        x 0.10
)
```

| Score | Status | Action |
|---|---|---|
| 80-100 (initial estimate) | Healthy | Referral prompt |
| 60-79 (initial estimate) | Needs attention | "You haven't practiced in a few days" email |
| 40-59 (initial estimate) | At risk | Re-engagement campaign with specific weak topic nudge |
| 0-39 (initial estimate) | Critical | Personal email from Enitan |

## Involuntary Churn: Dunning

### The Dunning Timeline

**Timeline intervals are initial estimates.** Adjust via `/tune` based on recovery rates per retry attempt.

```
Day -30 to -7:  Pre-dunning (card expiry alerts)
Day 0:          Payment fails → Retry #1 + Email #1 (friendly)
Day 3:          Retry #2 + Email #2 (reminder)
Day 7:          Retry #3 + Email #3 (urgent, show consequences)
Day 10:         Final retry + Email #4 (final warning)
Day 14:         Grace period ends → Account paused
Day 14+:        Win-back sequence begins
```

### Pre-Dunning

- Card expiry alerts: 30, 15, and 7 days before expiry
- Pre-billing notification: 7 days before annual renewal
- Backup payment method prompt: after first successful payment

### Dunning Email Tone

ExamPilot audience includes under-18s. Parents may be the billing contact.

- Email #1 (Day 0): Friendly, matter-of-fact. "Your payment didn't go through. Update your card."
- Email #2 (Day 3): Helpful reminder. "Still having trouble. Here's the link to update."
- Email #3 (Day 7): Direct. "Your account will be paused in 3 days. You'll lose access to your revision plan and progress data."
- Email #4 (Day 10): Final. "Last chance to keep your account active."

### Smart Retry Logic

| Decline type | Examples | Action |
|---|---|---|
| Soft (temporary) | Insufficient funds, timeout | Retry 3-5 times over 10 days |
| Hard (permanent) | Expired card, stolen card | Don't retry. Ask for new card. |
| Auth required | 3D Secure, SCA | Send customer to authenticate |

**Retry timing:** Retry on the same day of month the original payment succeeded. Avoid weekends. Morning retries (8-10am) perform slightly better.

### Dodo Payments Integration

[VERIFY] Check Dodo Payments dunning capabilities:
- Does it support smart retries natively?
- Does it handle card updater services (VAU/ABU)?
- What webhooks are available for failed payment events?

## Metrics

**All targets are initial estimates.** Adjust via `/tune` after 90 days of subscriber data.

| Metric | Target |
|---|---|
| Monthly churn rate | <5% (initial estimate) |
| Voluntary save rate | 20-30% (initial estimate) |
| Involuntary recovery rate | 50-60% (initial estimate) |
| Pause reactivation rate | 60-80% (initial estimate) |
| Time to cancel (exit survey completion) | >80% (initial estimate) |

## Implementation Phases

**Phase 1 (launch):** Basic cancel flow with exit survey. No save offers yet. Collect reason data.

**Phase 2 (month 2-3):** Add dynamic save offers based on collected reason data. Wire dunning emails.

**Phase 3 (month 4+):** Health score model. Proactive retention. Churn prediction triggers.

Source: Adapted from coreyhaines31/marketingskills churn-prevention skill + cancel-flow-patterns + dunning-playbook references
