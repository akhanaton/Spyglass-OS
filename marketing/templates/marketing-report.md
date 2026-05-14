# Marketing Report Template

Monthly cross-channel performance summary. Data-driven, actionable, concise.

## Frontmatter

```yaml
---
type: marketing-report
report_period: "YYYY-MM"
status: draft
date: YYYY-MM-DD
---
```

## Structure

### Executive Summary

3 bullet points max. What happened, what it means, what to do next.

### Funnel Metrics

**TOFU (Awareness)**

| Metric | This Month | Last Month | Target | Status |
|--------|-----------|------------|--------|--------|
| Total impressions (all channels) | | | | |
| New unique visitors (organic + social) | | | | |
| Brand mentions (Reddit, AI tools, social) | | | | |
| Content published (articles, posts, videos) | | | | |

**MOFU (Consideration)**

| Metric | This Month | Last Month | Target | Status |
|--------|-----------|------------|--------|--------|
| Avg time on site | | | | |
| Return visitors (within 7 days) | | | | |
| Email/waitlist signups | | | | |
| AI citations (ExamPilot in AI answers) | | | | |
| Reddit thread participation | | | | |

**BOFU (Conversion)**

| Metric | This Month | Last Month | Target | Status |
|--------|-----------|------------|--------|--------|
| Trial signups | | | | |
| Visitor-to-signup rate | | | | |
| Signup-to-paid rate | | | | |
| CAC by channel | | | | |
| First session completion rate | | | | |

**Retention**

| Metric | This Month | Last Month | Target | Status |
|--------|-----------|------------|--------|--------|
| D3 retention | | | | |
| D7 retention | | | | |
| Avg cards per session | | | | |
| Premium gate hit rate | | | | |
| NPS / Sean Ellis score | | | | |
| Organic referral rate | | | | |

### Channel Performance

| Channel | Impressions | Clicks/Visits | Conversions | Cost | Notes |
|---------|------------|---------------|-------------|------|-------|
| SEO/Blog | | | | | |
| Reddit | | | | | |
| Discord | | | | | |
| Email (Brevo) | | | | | |
| TikTok | | | | | |
| Tutor outreach | | | | | |
| Direct outreach | | | | | |
| AI Search | | | | | |

### Micro-Funnel Health

Are channels feeding each other? Evidence:
- Reddit threads ranking on Google? (Y/N, examples)
- SEO content cited by AI tools? (Y/N, examples)
- TikTok driving search traffic? (Y/N, evidence)
- Cross-channel attribution signals?

### Experiment Results

| Experiment | Hypothesis | Variants | Winner | Lift | Next Step |
|-----------|-----------|----------|--------|------|-----------|
| | | | | | |

### Top 3 Opportunities

Data-backed. Each with specific action and expected impact.

1. **[Opportunity]** — Evidence: [data]. Action: [what to do]. Expected impact: [metric improvement].
2. **[Opportunity]** — Evidence: [data]. Action: [what to do]. Expected impact: [metric improvement].
3. **[Opportunity]** — Evidence: [data]. Action: [what to do]. Expected impact: [metric improvement].

### Top 3 Risks

1. **[Risk]** — Evidence: [data]. Mitigation: [what to do].
2. **[Risk]** — Evidence: [data]. Mitigation: [what to do].
3. **[Risk]** — Evidence: [data]. Mitigation: [what to do].

### Strategy Adjustments

Recommended changes based on this month's data. Reference specific wiki articles to update if strategy changes.

- [ ] [Adjustment] — Update wiki: [article name]
- [ ] [Adjustment] — Update wiki: [article name]

## Data Sources

List which data sources were used and which were unavailable:
- [ ] GSC (gsc_analyzer.py)
- [ ] GA4 (ga4_analyzer.py)
- [ ] PostHog (posthog_marketing.py)
- [ ] Reddit (reddit_monitor.py)
- [ ] Brevo
- [ ] Manual tracking

## File Output

Save to: `marketing/pipelines/research/marketing-report-YYYY-MM.md`
