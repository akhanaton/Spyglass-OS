# Channel Playbooks

Operational rules for each active marketing channel. Strategy lives in the wiki. This file covers HOW to operate day-to-day.

## Reddit

**Active subreddits:**
- r/alevel — primary target, high activity, international students
- r/6thForm — UK-focused, overlapping audience
- r/CambridgeInternational — Cambridge 9709 students directly
- r/Edexcel — Edexcel IAL students directly

**Rules of engagement:**
- Value first, always. Answer the question before anything else.
- Never self-promote in first interaction with a community. Build karma first.
- Only mention ExamPilot when directly relevant to the question being asked.
- No link drops. If mentioning ExamPilot, describe what it does. Let them Google it.
- Read the sub rules before posting. r/alevel and r/6thForm have specific self-promo restrictions.
- If asked directly "what tools do you recommend", that is the green light.
- Account must have sufficient karma and age. Minimum: 50+ karma, 30+ days.

**Posting cadence:** 2-3 genuinely helpful contributions per week per sub. No flooding.

**Best posting times:** Evenings GMT (after school, 4pm-9pm UK) and weekends. Target audience is 16-18 year olds in UK, UAE, Pakistan, Malaysia, Singapore, Nigeria timezones.

**What gets banned/downvoted:**
- Obvious marketing language ("revolutionary", "game-changing")
- Linking to your product in every comment
- Posting the same content across multiple subs
- Not answering the actual question before mentioning your product

## Discord

**Target servers:** A-Level study servers, Cambridge Maths groups, Edexcel revision communities.

**Norms:**
- Join and contribute before promoting anything.
- Share study tips, answer maths questions, be helpful.
- Only share ExamPilot in dedicated "resources" or "tools" channels if they exist.
- Never DM-spam server members.

## WhatsApp

**Use case:** Tutor group referrals only. Not cold outreach to students.

**Rules:**
- Only message tutors you have a warm intro to or have engaged with elsewhere.
- Keep messages brief: who you are, what ExamPilot does, what's in it for their students.
- Maximum 1 follow-up if no response. Do not chase.
- Frequency: no more than 1 message per tutor per month.

## Email (Brevo)

**Status:** Stub until P2. Brevo selected but not yet connected.

**When wired:**
- Welcome sequence: 5 emails over 14 days after signup
- Campaign emails: maximum 1 per week to engaged list
- Re-engagement: after 14 days inactive, maximum 3 emails
- Always include unsubscribe. GDPR compliance mandatory (under-18 audience).
- Segment by exam board (Cambridge vs Edexcel) and status (active vs churned).

## SEO / Blog

**Publishing cadence:** Maximum 3 articles per week. Quality over velocity.

**Review process:**
1. Draft generated via `/write-article` to `marketing/pipelines/drafts/`
2. Human reviews: resolve all [VERIFY] flags, check voice, check factual accuracy
3. Move to `marketing/pipelines/review/` when edits complete
4. Publish via `/publish-article` (P2) or manual CMS upload
5. Move to `marketing/pipelines/published/` with live URL

**URL architecture:** Follows wiki seo-strategy.md. Read it before creating any content.

## TikTok (P2)

**Status:** Planned. Not yet active.

**When active:**
- Short-form study tips (30-60 seconds)
- Search-optimized: keywords in caption, on-screen text, and spoken audio in first 3 seconds
- Focus on Cambridge 9709 and Edexcel IAL specific content
- No hard sell. Educational value first.
- 2-3 videos per week
