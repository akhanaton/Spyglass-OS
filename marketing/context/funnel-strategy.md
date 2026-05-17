# Funnel Strategy

## Demand Generation vs. Customer Acquisition

Demand generation targets the ~95% of the market not actively shopping. It builds awareness, trust, and brand preference before a buyer ever signs up. Customer acquisition converts the ~5% who are actively evaluating. They are sequential and interdependent.

ExamPilot needs both. Demand gen without acquisition wastes leads. Acquisition without demand gen caps the pipeline at whoever already knows they need an exam prep tool.

## The Micro-Funnel (SEO + AI Search + TikTok + Reddit)

Four discovery channels form an interlocking micro-funnel. The end goal: a warm, pre-qualified visitor arriving at exampilot.io with high intent and pre-built trust.

```
TikTok (emotional discovery)
    "oh this exists"
         ↓
Reddit (peer validation)
    "is it actually good?"
         ↓
SEO (intent capture)
    "how do I solve my problem?"
         ↓
AI Search (recommendation)
    "what should I use?"
         ↓
Website (conversion)
    pre-built trust, low friction
```

**How they feed each other:**
- SEO content gets cited by AI tools (Google AI Overviews, ChatGPT, Perplexity)
- Reddit threads rank on Google and feed AI training data / RAG systems
- TikTok drives curiosity that triggers search (Google and Reddit)
- AI Search aggregates all three into recommendations

This is "zero-click nurturing": the student is already sold before they click through to exampilot.io.

### Parent Funnel (Parallel Path)

In target markets (Pakistan, UAE, Nigeria, Malaysia), the parent is the economic buyer. A parallel parent funnel operates alongside the student micro-funnel:

```
Facebook Groups / WhatsApp (parent discovery: "other parents use this")
    ↓ research
"For Parents" Landing Page (trust-building: "safe, affordable, works")
    ↓ decision
Website → Trial (parent creates account for child) → Paid
```

Both funnels converge at the website. A student may discover ExamPilot through TikTok and tell their parent. A parent may discover it through a Facebook Group and tell their child.

## Channel-to-Stage Mapping

| Channel | Primary Stage | Role | Key Metric |
|---|---|---|---|
| TikTok | TOFU (awareness) | Emotional hook, "oh this exists" (region-specific) | Views, profile visits |
| Reddit | TOFU/MOFU (awareness/consideration) | SEO/AI citation seeding engine | Google indexing, AI citations, thread rank |
| SEO/Blog | TOFU/MOFU (awareness/consideration) | Intent capture, authority building | Organic sessions, keyword rankings, time on page |
| AI Search (GEO) | MOFU/BOFU (consideration/decision) | Recommendation, citation | Brand mentions in AI responses |
| Facebook Groups | TOFU/MOFU (parent awareness/consideration) | Parent discovery, trust-building | Parent inquiries, page referrals |
| WhatsApp Communities | TOFU/MOFU (student awareness/consideration) | Community, peer engagement (international) | Members, broadcast clicks, referrals |
| Email (Brevo) | MOFU/BOFU (nurture/conversion) | Drip nurture, conversion push (student + parent) | Open rate, click rate, trial signup rate |
| School/Teacher outreach | MOFU/BOFU (referral/conversion) | B2C2B referral partnerships | Schools recommending, students attributed |
| Direct outreach | MOFU/BOFU (conversion) | Personal touch, founder-led | Response rate, signup rate |
| Landing page | BOFU (conversion) | Final conversion (student + "For Parents" page) | Signup rate, trial-to-paid |

## Stage-Specific KPIs

**TOFU (awareness):**
- Reach: total impressions across channels
- New visitors: unique visitors from organic/social
- Brand mentions: ExamPilot mentions on Reddit, AI tools, social
- Content published: articles, posts, videos per week

**MOFU (consideration):**
- Engagement: time on site, pages per session, Reddit thread participation
- Email signups: waitlist or newsletter captures
- Return visitors: how many come back within 7 days
- AI citations: ExamPilot mentioned in AI-generated answers

**BOFU (conversion):**
- Trial signups: free account creations
- Conversion rate: visitor-to-signup, signup-to-paid
- CAC: cost per acquired customer by channel
- First session completion: onboarded to first SRS session

**Post-purchase (retention/advocacy):**
- D3 and D7 retention
- Session depth: cards per session
- Premium gate hit rate
- NPS or Sean Ellis score (post-session-3)
- Referral rate: organic referrals from existing users

## Current Priority (Pre-Launch)

The May/June 2026 exam window is too close for SEO to rank. Direct and community channels are the only path to the first 100 students:

| Channel | Target | Method |
|---|---|---|
| Tutor WhatsApp referrals | 15-25 | Warm intros, tutor group broadcasts |
| WhatsApp Communities | 10-20 | ExamPilot community, existing CIE student groups |
| School/teacher outreach | 10-20 | B2C2B referral partnerships (5-10 schools) |
| Facebook Groups (parent) | 5-10 | COALI, CIE parent communities, value-first engagement |
| Reddit (SEO/AI seeding) | 5-10 | Organic interest from helpful contributions (not targeted) |
| Discord | 5-10 | Study servers, secondary to WhatsApp |
| **Total** | **50-95** | |

SEO and TikTok are being built now for the August 2026 Results Day window (Oct/Nov resit cohort) and long-term compounding.

## Measurement Layer — GTM Engineering

The funnel above defines how content and community activity flow through discovery stages. GTM Engineering (Enitan's function) is the measurement and routing layer that closes the feedback loop.

Every event in the funnel generates a signal scored by `marketing/gtm-engineering/scoring-model.md`:

| Funnel event | Signal type | Where it goes |
|---|---|---|
| Pricing page visit, trial signup | Behavioral (PostHog) | CRS score → Attio contact enriched |
| Reddit post, brand mention | Community (Syften/Reddit API) | Coda Signals table → manual response |
| Keyword ranking change | SEO (GSC/DataForSEO) | Coda Signals table → content audit or brief |
| Exam season −30 days | Campaign (calendar) | Coda checklist → campaign activation |
| WhatsApp community join | Engagement (WhatsApp Business App) | Coda Signals table → welcome message |
| WhatsApp broadcast click | Engagement (Wati/WhatsApp API) | CRS score → engagement tracking |
| Facebook Group mention | Brand awareness (manual/Syften) | Coda Signals table → flag for response |
| Teacher referral click | High-intent referral (PostHog UTM) | CRS score → Attio partner enriched |
| School cohort signup | High-intent referral (PostHog UTM) | CRS score → Attio partner enriched → follow-up |

**Weekly ritual:** Run `/signal-review` (Enitan) before `/weekly-pulse` (Teresa). Together they give the full picture: content output + intent response.

**Destinations:**
- Coda Signals table — operational review of all signals needing action
- Attio CRM — enriched student contacts (tier, score, exam board, topic focus, source)
- Brevo sequences — conversion and re-engagement emails triggered by tier thresholds

See `marketing/gtm-engineering/` for the full signal registry, scoring mechanics, and trigger playbook.

## The Flywheel

Short-term: manual outreach (tutor referrals, WhatsApp communities, school partnerships, Facebook Groups, Reddit, Discord) drives the first 100 students. Parent and school channels run in parallel with student acquisition.
Medium-term: SEO content starts ranking, Reddit threads compound, AI tools cite ExamPilot. School partnerships begin generating cohort signups. Parent word-of-mouth spreads through Facebook and WhatsApp groups.
Long-term: organic channels dominate, CAC drops, each channel reinforces the others. School referrals become a scalable acquisition engine.

Every piece of content should serve at least two channels. A blog article can be repurposed into a Reddit post, an email, a WhatsApp broadcast, and a TikTok script. A Reddit answer can surface in Google and get cited by AI search. A Facebook Group contribution builds parent trust that converts via the "For Parents" page.

## The Builder Funnel (X / Build in Public)

Moved to dedicated sub-OS. See `build-in-public/context/funnel.md`.
