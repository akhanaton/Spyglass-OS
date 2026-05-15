# Signal Registry

All signals tracked by the GTM Engineering function. Each signal has a source, category, weight, and trigger destination. Weights are initial estimates — adjust based on signal-to-conversion data after 8-12 weeks post-launch (Phase 2 review).

---

## First-Party Signals

Data you control directly: website behavior, product usage, email interaction.

| Signal | Source | Weight | Trigger type | Notes |
|---|---|---|---|---|
| Pricing page visit | GA4 / PostHog | +8 | Conversion intent | Combine with session duration for confidence |
| Free trial sign-up | PostHog | +20 | Conversion intent | Always creates Attio contact |
| First session completed | PostHog | +15 | Activation | "First value" milestone |
| Session duration > 20 min | PostHog | +10 (cap ×3) | Engagement | Cap prevents single-session score inflation |
| Return visit within 7 days | PostHog | +12 | Retention intent | Strong predictor of subscription intent |
| In-app upgrade CTA click | PostHog | +25 | Expansion intent | Highest weight — explicit purchase signal |
| Email CTA click (nurture) | Brevo | +8 | Engagement | Only count distinct CTA, not opens |
| 7+ day inactivity (active user) | PostHog | −20 | Churn risk | Active = had ≥1 session in previous 14 days |
| Topic completion (all questions in topic) | PostHog | +5 | Engagement depth | Good leading indicator for multi-unit value |
| ERI score improvement > 10 pts | PostHog | +8 | Engagement depth | Shows product is working — retention signal |

---

## Second-Party Signals

Intent data in proximity to your brand via platforms and community.

| Signal | Source | Weight | Trigger type | Notes |
|---|---|---|---|---|
| Brand mention in target subreddit | Syften / reddit_monitor.py | +15 | Brand awareness | Flag for manual response if negative or question |
| Study struggle post ("need help with 9709") | Syften / reddit_monitor.py | +5 | Demand signal | Route to `/write-reddit` — respond with value |
| Competitor comparison thread | Syften | +10 | Intent signal | Flag for positioning response |
| Tutor referral click | PostHog (UTM: source=tutor) | +18 | High-intent referral | Warm audience — shorten nurture sequence |
| Discord question about ExamPilot | Manual | +12 | Brand interest | Log manually when spotted |

---

## Third-Party Signals

External and public data for discovery and market intelligence.

| Signal | Source | Weight | Trigger type | Notes |
|---|---|---|---|---|
| Keyword ranking drop > 5 positions | DataForSEO / GSC | SEO alert | Content audit flag | Run content audit; check for SERP feature changes |
| Keyword ranking gain > 5 positions | DataForSEO / GSC | SEO positive | Content amplify | Share on Reddit; add internal links |
| New query triggering impressions (CTR < 5%) | GSC | SEO opportunity | Content creation | Brief via `/research-keywords` |
| Competitor content outranking ours on target keyword | DataForSEO | SEO competitive | Bridge content flag | Analyse gap; create superior resource |
| Exam season proximity (−30 days from Results Day) | Calendar | Campaign trigger | Campaign activate | Results Day: CIE ~Aug 15, Edexcel ~Aug 22 |
| Mock season start (mid-Jan) | Calendar | Campaign trigger | Demand gen pulse | Increase Reddit activity; push study guides |

**Key exam calendar dates:**
- Jan 15: Mock season start → demand gen pulse
- May 1: Exam month → acquisition push
- Aug 15: CIE Results Day → conversion campaign
- Aug 22: Edexcel Results Day → conversion campaign
- Oct 1: Resit window → re-engagement campaign

---

## Signal Metadata Schema

Every signal captured by `signal_processor.py` outputs this structure:

```python
{
    "signal_id": "str (uuid)",
    "timestamp": "ISO 8601",
    "source": "posthog | reddit | gsc | dataforseo | calendar | brevo | manual",
    "category": "first_party | second_party | third_party",
    "type": "behavioral | community | seo | campaign",
    "entity_id": "posthog user_id | reddit thread_id | keyword | date",
    "signal_name": "str (from registry above)",
    "weight": "int",
    "raw_value": "any (event properties, post text, rank position, etc.)",
    "recommended_action": "str",
    "destination": "coda | attio | both | manual"
}
```
