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

## Channel-to-Stage Mapping

| Channel | Primary Stage | Role | Key Metric |
|---|---|---|---|
| TikTok | TOFU (awareness) | Emotional hook, "oh this exists" | Views, profile visits |
| Reddit | TOFU/MOFU (awareness/consideration) | Peer validation, social proof | Upvotes, thread rank on Google, DM requests |
| SEO/Blog | TOFU/MOFU (awareness/consideration) | Intent capture, authority building | Organic sessions, keyword rankings, time on page |
| AI Search (GEO) | MOFU/BOFU (consideration/decision) | Recommendation, citation | Brand mentions in AI responses |
| Email (Brevo) | MOFU/BOFU (nurture/conversion) | Drip nurture, conversion push | Open rate, click rate, trial signup rate |
| Direct outreach | MOFU/BOFU (conversion) | Personal touch, founder-led | Response rate, signup rate |
| Landing page | BOFU (conversion) | Final conversion | Signup rate, trial-to-paid |

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

The May/June 2026 exam window is too close for SEO to rank. Direct channels are the only path to the first 100 students:
1. Reddit (r/alevel, r/6thForm, r/CambridgeInternational) — 15-25 students
2. Discord study servers — 10-20 students
3. Tutor WhatsApp referrals — 10-15 students
4. Direct tutor outreach — 15-25 via their students

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

**Weekly ritual:** Run `/signal-review` (Enitan) before `/weekly-pulse` (Teresa). Together they give the full picture: content output + intent response.

**Destinations:**
- Coda Signals table — operational review of all signals needing action
- Attio CRM — enriched student contacts (tier, score, exam board, topic focus, source)
- Brevo sequences — conversion and re-engagement emails triggered by tier thresholds

See `marketing/gtm-engineering/` for the full signal registry, scoring mechanics, and trigger playbook.

## The Flywheel

Short-term: manual outreach (Reddit, Discord, tutors) drives the first 100 students.
Medium-term: SEO content starts ranking, Reddit threads compound, AI tools cite ExamPilot.
Long-term: organic channels dominate, CAC drops, each channel reinforces the others.

Every piece of content should serve at least two channels. A blog article can be repurposed into a Reddit post, an email, and a TikTok script. A Reddit answer can surface in Google and get cited by AI search.

## The Builder Funnel (X / Build in Public)

Separate from the student micro-funnel. Different audience, different goal.

```
X posts/threads (founder credibility)
    "interesting, they're building this"
         |
Personal profile (trust)
    "real people, real progress"
         |
ExamPilot awareness (word of mouth)
    founders tell other founders
         |
Inbound interest (advisors, beta testers, press, partnerships)
```

This funnel does not convert students directly. It builds the credibility layer that makes everything else easier: press coverage, partnership requests, tutor referrals from the edtech community, and a launch-day audience that amplifies the student-facing channels.

| Stage | What happens | Key metric |
|---|---|---|
| Credibility | Consistent posting builds "these people are real" trust | Engagement rate (target 3-6%) |
| Network | Quality replies and threads attract builders at similar stage | Follower growth, DM conversations |
| Amplification | Builder audience retweets launch announcements to their audiences | Impressions on launch content |
| Inbound | Advisors, press, partners reach out because they've followed the journey | Inbound DMs, partnership requests |
